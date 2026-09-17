#!/usr/bin/env python3
"""Build the static site: content/<lang>/*.md -> docs/<lang>/*.html"""
import re, shutil, html
from pathlib import Path
import markdown

ROOT = Path(__file__).parent
CONTENT, DOCS, TPL = ROOT / "content", ROOT / "docs", ROOT / "templates"

SITE = {"ru": "Идеонология", "en": "Ideonology"}
DESC = {"ru": "Теория смысла жизни, в которой смысл оцениваем с точностью до порядка: идеон, Вита, паритет.",
        "en": "A theory of the meaning of life in which meaning can be estimated to an order of magnitude: ideon, Vita, parity."}
NAV = [("index", {"ru": "Главная", "en": "Home"}),
       ("manifesto", {"ru": "Манифест", "en": "Manifesto"}),
       ("glossary", {"ru": "Словарь", "en": "Glossary"}),
       ("math", {"ru": "Математика", "en": "Mathematics"}),
       ("examples", {"ru": "Примеры", "en": "Examples"}),
       ("comparison", {"ru": "Сравнение", "en": "Comparison"}),
       ("protocol", {"ru": "Протокол", "en": "Protocol"})]
ALT = {"ru": ("en", "English"), "en": ("ru", "Русский")}
FOOTER = {"ru": "Идеонология · 2026 · текст свободен для переизлучения (CC BY 4.0)",
          "en": "Ideonology · 2026 · free to re-emit (CC BY 4.0)"}

def parse(src: str):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", src, re.S)
    meta = dict(l.split(":", 1) for l in m.group(1).splitlines() if ":" in l) if m else {}
    return {k.strip(): v.strip() for k, v in meta.items()}, (m.group(2) if m else src)

def build_page(lang: str, slug: str, template: str):
    meta, body_md = parse((CONTENT / lang / f"{slug}.md").read_text(encoding="utf-8"))
    body = markdown.markdown(body_md, extensions=["tables", "sane_lists", "smarty", "toc"],
                             extension_configs={"smarty": {"smart_quotes": False, "smart_dashes": False}})
    body = body.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    nav = " ".join(f'<a href="{s}.html"{" class=\"current\"" if s == slug else ""}>{names[lang]}</a>'
                   for s, names in NAV)
    alt_lang, alt_label = ALT[lang]
    page = template.format(lang=lang, title=html.escape(meta.get("title", slug)), site=SITE[lang],
                           description=html.escape(DESC[lang]), root="../", nav=nav, body=body,
                           alt_lang=alt_lang, alt_label=alt_label, alt_href=f"../{alt_lang}/{slug}.html",
                           footer=FOOTER[lang])
    out = DOCS / lang / f"{slug}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

def main():
    template = (TPL / "page.html").read_text(encoding="utf-8")
    for lang in SITE:
        for md in sorted((CONTENT / lang).glob("*.md")):
            build_page(lang, md.stem, template)
    shutil.copy(TPL / "style.css", DOCS / "style.css")
    (DOCS / "index.html").write_text(
        '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8">'
        '<meta http-equiv="refresh" content="0; url=ru/index.html">'
        '<link rel="canonical" href="ru/index.html"><title>Идеонология / Ideonology</title></head>'
        '<body><p><a href="ru/index.html">Идеонология (русский)</a> · <a href="en/index.html">Ideonology (English)</a></p>'
        '</body></html>', encoding="utf-8")
    (DOCS / ".nojekyll").touch()
    print("built:", ", ".join(str(p.relative_to(DOCS)) for p in sorted(DOCS.rglob("*.html"))))

if __name__ == "__main__":
    main()
