#!/usr/bin/env python3
"""Build the static site: content/<lang>/*.md -> docs/<lang>/*.html"""
import re, shutil, html, json, subprocess
from datetime import date
from pathlib import Path
import markdown

ROOT = Path(__file__).parent
CONTENT, DOCS, TPL = ROOT / "content", ROOT / "docs", ROOT / "templates"

HOST = "ideon.lipu.dev"
BASE = f"https://{HOST}/"
SITE = {"ru": "Идеонология", "en": "Ideonology"}
LOCALE = {"ru": "ru_RU", "en": "en_US"}
TAGLINE = {"ru": "сколько чужой мысли ты сдвинул", "en": "measuring how thoughts change other minds"}
OG_IMAGE = f"{BASE}og.png"
DESC = {"ru": "Идеонология измеряет, насколько ты изменил чужое мышление, с точностью до порядка: теория значимости с единицей влияния (пирс) и шкалой от минуты до жизни.",
        "en": "Ideonology measures how much of other people's thought you shifted, to an order of magnitude: a theory of significance with a unit of impact, the peirce."}
# The root page is the language picker and the x-default of the home pages; it gets its own short bilingual description.
ROOT_DESC = "Идеонология — теория значимости: сколько чужой мысли ты сдвинул. Ideonology, a theory of significance: how much of other people's thought you shifted."
NAV = [("index", {"ru": "Главная", "en": "Home"}),
       ("start", {"ru": "За пять минут", "en": "In five minutes"}),
       ("manifesto", {"ru": "Манифест", "en": "Manifesto"}),
       ("meaning", {"ru": "Смысл", "en": "Meaning"}),
       ("selfhood", {"ru": "Самость", "en": "Selfhood"}),
       ("glossary", {"ru": "Словарь", "en": "Glossary"}),
       ("math", {"ru": "Математика", "en": "Mathematics"}),
       ("examples", {"ru": "Примеры", "en": "Examples"}),
       ("comparison", {"ru": "Сравнение", "en": "Comparison"}),
       ("protocol", {"ru": "Протокол", "en": "Protocol"}),
       ("notability", {"ru": "Википедия", "en": "Notability"}),
       ("hall", {"ru": "Зал славы", "en": "Hall of fame"})]
ALT = {"ru": ("en", "English"), "en": ("ru", "Русский")}

# Terms: (slug, regex, hint). The first occurrence on a page becomes a link to the glossary
# entry with the hint as a tooltip. The glossary page itself is left alone.
TERMS = {"ru": [
    ("ideon", r"\bидеон(?:а|ы|ов|у|е|ом|ами|ах)?\b", "порция влияния: то, что ты сдвинул в чужой голове; величина меряется в пирсах"),
    ("peirce", r"\bпирс(?:а|у|ом|е|ы|ов|ам|ами|ах)?\b", "единица импакта: одна чужая минута, целиком твоя"),
    ("vita", r"\bВит(?:а|ы|у|е|ой)\b", "вся мысль одного человека за жизнь: 2,5 × 10⁷ пирсов"),
    ("parity", r"\bпаритет\w*", "порог в одну Виту: вернул в чужие головы столько же, сколько получил"),
    ("degree", r"\bградус\w*", "какую часть чужой минуты захватил идеон, от 0 до 1; измеряется углом"),
    ("impact", r"\bимпакт\w*", "сумма твоих частей во всех чужих минутах: I ≈ охват × градус × доля"),
    ("sign", r"\bзнак\w*", "направление сдвига, к лучшему или к худшему; отдельная от величины ось"),
    ("coherence", r"\bкогерентност\w*", "насколько результат совпал с намерением; свойство излучателя"),
    ("share", r"\bдол(?:я|и|ю|е|ей|ям|ями|ях)\b", "твоя часть захваченной минуты: что исчезло бы без тебя; вектор Шепли"),
    ("irreplaceability", r"\bнезаменимост\w*", "насколько без тебя результат был бы иным"),
    ("damping", r"\bзатухани\w*", "убывание долей вдоль цепочки: чем дальше звено, тем оно заменимее"),
    ("selfhood", r"\bсамост(?:ь|и|ью)\b", "твоя часть в собственной минуте: что было бы другим с другой головой на твоём месте; в импакт не входит"),
    ("reemission", r"\bпереизлучени\w*", "передача идеона дальше: пересказ, запись, воспитание, поступок"),
    ("chain", r"\bцепочк\w*", "путь идеона от источника до головы, в которой он сработал"),
    ("anonymous", r"\bАноним\w*", "счёт, на который записан импакт без известного источника: язык, огонь, пословицы"),
    ("arbiter", r"\bарбитр(?:а|у|ом|е|ы|ов|ам|ами|ах)?\b", "кто ставит знак: Бог, история, карма, собственный разум, никто"),
    ("horizon", r"\bгоризонт\w*", "когда счёт закрывается: смерть, Суд, никогда"),
    ("r0", r"\bR₀", "сколько новых носителей порождает один носитель; больше 1 — цепочка живёт сама"),
], "en": [
    ("ideon", r"\bideons?\b", "a portion of influence: what you shifted in someone else's head; its magnitude is measured in peirces"),
    ("peirce", r"\bpeirces?\b", "the unit of impact: one minute of someone else's, wholly yours"),
    ("vita", r"\bVita\b", "all the thought of one person over a lifetime: 2.5 × 10⁷ peirces"),
    ("parity", r"\bparity\b", "the threshold of one Vita: returned into other heads as much as you received"),
    ("degree", r"\bdegrees?\b", "what part of someone else's minute the ideon captured, 0 to 1; measured as an angle"),
    ("impact", r"\bimpact\b", "the sum of your parts in all other people's minutes: I ≈ reach × degree × share"),
    ("sign", r"\bsigns?\b", "the direction of the shift, for better or worse; an axis separate from magnitude"),
    ("coherence", r"\bcoherence\b", "how far the result matched the intention; a property of the emitter"),
    ("share", r"\bshares?\b", "your part of the captured minute: what would disappear without you; the Shapley value"),
    ("irreplaceability", r"\birreplaceab\w+", "how different the result would have been without you"),
    ("damping", r"\bdamping\b", "the decline of shares along the chain: the further the link, the more replaceable"),
    ("selfhood", r"\bselfhood\b", "your part in your own minute: what would differ with another head in your place; not counted as impact"),
    ("reemission", r"\bre-emi\w+", "passing an ideon on: retelling, writing, upbringing, a deed"),
    ("chain", r"\bchains?\b", "the path of an ideon from its source to the head in which it took effect"),
    ("anonymous", r"\bAnonymous\b", "the account holding impact with no known source: language, fire, proverbs"),
    ("arbiter", r"\barbiters?\b", "who assigns the sign: God, history, karma, one's own reason, nobody"),
    ("horizon", r"\bhorizons?\b", "when the account closes: death, Judgment, never"),
    ("r0", r"\bR₀", "how many new carriers one carrier produces; above 1 the chain sustains itself"),
]}
GLOSSARY_HEADS = {"ru": {"ideon": "Идеон", "peirce": "Пирс", "vita": "Вита", "parity": "Паритет", "degree": "Градус", "impact": "Импакт",
                         "sign": "Знак", "coherence": "Когерентность", "share": "Доля", "irreplaceability": "Незаменимость",
                         "damping": "Затухание", "selfhood": "Самость", "reemission": "Переизлучение", "chain": "Цепочка", "anonymous": "Аноним",
                         "arbiter": "Арбитр", "horizon": "Горизонт", "r0": "R₀"},
                  "en": {"ideon": "Ideon", "peirce": "Peirce", "vita": "Vita", "parity": "Parity", "degree": "Degree", "impact": "Impact",
                         "sign": "Sign", "coherence": "Coherence", "share": "Share", "irreplaceability": "Irreplaceability",
                         "damping": "Damping", "selfhood": "Selfhood", "reemission": "Re-emission", "chain": "Chain", "anonymous": "The Anonymous",
                         "arbiter": "Arbiter", "horizon": "Horizon", "r0": "R₀"}}
SKIP_TAGS = {"a", "h1", "h2", "h3", "h4", "h5", "h6", "code", "pre", "sub", "sup", "th"}

def anchor_glossary(body: str, lang: str) -> str:
    """Give each glossary entry an id so term links can point at it."""
    for slug, head in GLOSSARY_HEADS[lang].items():
        # The head must end the word ("Sign (S)", "R₀, ..."), or "Sign" would land on "Significance".
        body = re.sub(rf"<p><strong>{re.escape(head)}(?=</strong>| \(|,)", f'<p id="{slug}"><strong>{head}', body, count=1)
    return body

def glossary_terms(body: str, lang: str):
    """DefinedTerm entries from the rendered glossary: <p [id]><strong>NAME</strong> — DEFINITION</p>, exactly as shown."""
    url = page_url(lang, "glossary")
    terms = []
    for m in re.finditer(r'<p(?: id="([^"]+)")?><strong>(.*?)</strong> — (.*?)</p>', body, re.S):
        slug, name, definition = m.groups()
        term = {"@type": "DefinedTerm", "name": html.unescape(re.sub(r"<[^>]+>", "", name)),
                "description": html.unescape(re.sub(r"<[^>]+>", "", definition)).strip(),
                "inDefinedTermSet": url, "inLanguage": lang}
        if slug:
            term["url"] = f"{url}#{slug}"
        terms.append(term)
    return terms

def linkify_terms(body: str, lang: str) -> str:
    """Turn the first occurrence of each term into a glossary link with a tooltip."""
    pending = [(s, re.compile(rx, re.I if s not in ("anonymous", "peirce") else 0), hint) for s, rx, hint in TERMS[lang]]
    out, depth = [], 0
    for chunk in re.split(r"(<[^>]+>)", body):
        if chunk.startswith("<"):
            m = re.match(r"<(/?)(\w+)", chunk)
            if m and m.group(2).lower() in SKIP_TAGS and not chunk.endswith("/>"):
                depth += -1 if m.group(1) else 1
            out.append(chunk); continue
        if depth > 0 or not pending or not chunk.strip():
            out.append(chunk); continue
        hits = []
        for slug, rx, hint in pending:
            m = rx.search(chunk)
            if m: hits.append((m.start(), m.end(), slug, hint))
        hits.sort()
        pos, done, parts = 0, set(), []
        for start, end, slug, hint in hits:
            if start < pos: continue
            parts.append(chunk[pos:start])
            parts.append(f'<a class="term" href="glossary.html#{slug}" title="{html.escape(hint, quote=True)}">{chunk[start:end]}</a>')
            pos = end; done.add(slug)
        parts.append(chunk[pos:])
        out.append("".join(parts))
        pending = [p for p in pending if p[0] not in done]
    return "".join(out)

FOOTER = {"ru": "Идеонология · 2026 · текст свободен для переизлучения (CC BY 4.0)",
          "en": "Ideonology · 2026 · free to re-emit (CC BY 4.0)"}
ABOUT = {
    "ru": ("Что это?", "Закрыть", """<h2>Что это?</h2>
<ul>
<li><b>Идеонология</b> — теория значимости: сколько чужой мысли сдвинул человек, событие, место или идея.</li>
<li><b>Единица</b> — пирс: одна чужая минута, целиком твоя. Вся мысль одного человека за жизнь — одна Вита, 25 миллионов минут.</li>
<li><b>Кредит</b> идёт по незаменимости: каждому столько, сколько без него бы исчезло.</li>
<li><b>Цифры</b> — оценки по Ферми, с точностью до порядка; кто выше, кто ниже — надёжнее самих чисел.</li>
</ul>
<p><a href="start.html">Разобрать на одном примере</a></p>"""),
    "en": ("What is this?", "Close", """<h2>What is this?</h2>
<ul>
<li><b>Ideonology</b> is a theory of significance: how much of other people's thought a person, event, place or idea shifted.</li>
<li><b>The unit</b> is the peirce: one minute of someone else's, wholly yours. All the thought of one person over a lifetime is one Vita, 25 million minutes.</li>
<li><b>Credit</b> follows irreplaceability: each gets as much as would disappear without them.</li>
<li><b>The numbers</b> are Fermi estimates, to an order of magnitude; who is above whom holds better than the figures.</li>
</ul>
<p><a href="start.html">Walk through one example</a></p>"""),
}
UPDATED = {"ru": "обновлено", "en": "updated"}
def parse(src: str):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    meta = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l) if m else {}
    return {k.strip(): v.strip() for k, v in meta.items()}, (m.group(2) if m else src)

def page_url(lang: str, slug: str) -> str:
    return f"{BASE}{lang}/" if slug == "index" else f"{BASE}{lang}/{slug}.html"

def lastmod(path: Path) -> str:
    """Date of the last commit that touched the source file; today if it has never been committed."""
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", str(path)], cwd=ROOT,
                         capture_output=True, text=True).stdout.strip()
    return out or date.today().isoformat()

def alternates(slug: str):
    """(hreflang, url) for every version of a page. The home pages' x-default is the root language picker;
    every other page has no neutral version, so its x-default is English."""
    return [("ru", page_url("ru", slug)), ("en", page_url("en", slug)),
            ("x-default", BASE if slug == "index" else page_url("en", slug))]

def write_sitemap(slugs):
    home = "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>' for h, u in alternates("index"))
    root_mod = max(lastmod(CONTENT / lang / "index.md") for lang in SITE)
    rows = [f"<url><loc>{BASE}</loc><lastmod>{root_mod}</lastmod>{home}</url>"]
    for slug in slugs:
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{h}" href="{u}"/>' for h, u in alternates(slug))
        for lang in SITE:
            rows.append(f"<url><loc>{page_url(lang, slug)}</loc>"
                        f"<lastmod>{lastmod(CONTENT / lang / f'{slug}.md')}</lastmod>{alts}</url>")
    (DOCS / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(rows) + "\n</urlset>\n", encoding="utf-8")

def projects_html(lang: str) -> str:
    return '<p class="projects"><a href="https://lipu.dev/">lipu.dev</a></p>'

def jsonld(lang: str, slug: str, title: str, description: str, terms=None) -> str:
    """WebSite on the home page, Article + BreadcrumbList on the rest. No author/publisher: not stated anywhere."""
    url = page_url(lang, slug)
    site = {"@type": "WebSite", "name": SITE[lang], "url": page_url(lang, "index"), "inLanguage": lang}
    if slug == "index":
        data = [{"@context": "https://schema.org", **site, "description": description}]
    else:
        names = dict((s_, n[lang]) for s_, n in NAV)
        data = [
            {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": description,
             "inLanguage": lang, "url": url, "mainEntityOfPage": url, "image": OG_IMAGE,
             "dateModified": lastmod(CONTENT / lang / f"{slug}.md"), "isPartOf": site},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": SITE[lang], "item": page_url(lang, "index")},
                {"@type": "ListItem", "position": 2, "name": names.get(slug, title), "item": url}]},
        ]
        if terms:
            data.append({"@context": "https://schema.org", "@type": "DefinedTermSet", "@id": url, "name": title,
                         "description": description, "url": url, "inLanguage": lang, "hasDefinedTerm": terms})
    return "".join(f'<script type="application/ld+json">{json.dumps(d, ensure_ascii=False)}</script>' for d in data)

def build_page(lang: str, slug: str, template: str):
    meta, body_md = parse((CONTENT / lang / f"{slug}.md").read_text(encoding="utf-8"))
    body = markdown.markdown(body_md, extensions=["tables", "sane_lists", "smarty", "toc"],
                             extension_configs={"smarty": {"smart_quotes": False, "smart_dashes": False}})
    body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    body = anchor_glossary(body, lang) if slug == "glossary" else linkify_terms(body, lang)
    nav = " ".join(f'<a href="{s}.html"{" class=\"current\"" if s == slug else ""}>{names[lang]}</a>'
                   for s, names in NAV)
    alt_lang, alt_label = ALT[lang]
    # hreflang must be absolute and list every version including the page itself (see alternates())
    hreflangs = "\n".join(f'<link rel="alternate" hreflang="{h}" href="{u}">' for h, u in alternates(slug))
    title = meta.get("title", slug)
    desc = meta.get("description", DESC[lang])
    # The home page's title equals the site name ("Идеонология · Идеонология"): give it a real one.
    doc_title = f"{SITE[lang]} — {TAGLINE[lang]}" if title == SITE[lang] else f"{title} · {SITE[lang]}"
    page = template.format(lang=lang, title=html.escape(title), doc_title=html.escape(doc_title), site=SITE[lang],
                           description=html.escape(desc, quote=True), og_image=OG_IMAGE,
                           jsonld=jsonld(lang, slug, title, desc, glossary_terms(body, lang) if slug == "glossary" else None),
                           root="../", nav=nav, body=body, url=page_url(lang, slug), hreflangs=hreflangs,
                           og_type="website" if slug == "index" else "article", locale=LOCALE[lang],
                           alt_lang=alt_lang, alt_label=alt_label, about_btn=ABOUT[lang][0], about_close=ABOUT[lang][1], about_html=ABOUT[lang][2], alt_href=f"../{alt_lang}/{slug}.html",
                           footer=f"{FOOTER[lang]} · {UPDATED[lang]} {lastmod(CONTENT / lang / f'{slug}.md')}", projects=projects_html(lang))
    out = DOCS / lang / f"{slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

def main():
    template = (TPL / "page.html").read_text(encoding="utf-8")
    for lang in SITE:
        for md in sorted((CONTENT / lang).glob("*.md")):
            build_page(lang, md.stem, template)
    shutil.copy(TPL / "style.css", DOCS / "style.css")
    shutil.copy(TPL / "og.png", DOCS / "og.png")
    for f in TPL.glob("google*.html"):  # Search Console ownership file: must stay at the site root forever
        shutil.copy(f, DOCS / f.name)
    shutil.copy(TPL / "404.html", DOCS / "404.html")  # GitHub Pages serves it, with status 404, for any missing path
    # The root is a language picker, not a redirect: it is the x-default of the home pages and canonical to itself.
    root_desc = html.escape(ROOT_DESC, quote=True)
    root_alts = "".join(f'<link rel="alternate" hreflang="{h}" href="{u}">' for h, u in alternates("index"))
    (DOCS / "index.html").write_text(
        '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1">'
        '<title>Идеонология / Ideonology</title>'
        f'<meta name="description" content="{root_desc}">'
        f'<link rel="canonical" href="{BASE}">{root_alts}'
        '<meta name="msvalidate.01" content="CAFA7BE0D5D83695993D635831499022">'
        '<meta property="og:type" content="website"><meta property="og:site_name" content="Идеонология / Ideonology">'
        '<meta property="og:title" content="Идеонология / Ideonology">'
        f'<meta property="og:description" content="{root_desc}"><meta property="og:url" content="{BASE}">'
        f'<meta property="og:image" content="{OG_IMAGE}"><meta name="twitter:card" content="summary_large_image">'
        f'<meta name="twitter:image" content="{OG_IMAGE}">'
        '<link rel="stylesheet" href="style.css"></head>'
        '<body><main class="picker"><h1>Идеонология / Ideonology</h1>'
        f'<p lang="ru">{html.escape(DESC["ru"])}</p><p lang="en">{html.escape(DESC["en"])}</p>'
        '<p class="choose"><a href="ru/" hreflang="ru" lang="ru">Читать по-русски</a>'
        '<a href="en/" hreflang="en" lang="en">Read in English</a></p>'
        '</main></body></html>', encoding="utf-8")
    write_sitemap([s for s, _ in NAV])
    (DOCS / ".nojekyll").touch()
    (DOCS / "CNAME").write_text(HOST + "\n")  # GitHub Pages custom domain
    (DOCS / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")
    print("built:", ", ".join(str(p.relative_to(DOCS)) for p in sorted(DOCS.rglob("*.html"))))

if __name__ == "__main__":
    main()
