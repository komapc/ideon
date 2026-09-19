# Идеонология / Ideonology

Теория смысла жизни, в которой смысл оцениваем с точностью до порядка. **Идеон** — то, что ты сдвинул в чужой голове; его величина меряется в **пирсах**: один пирс — одна чужая минута, целиком твоя.
A theory of the meaning of life in which meaning can be estimated to an order of magnitude. An **ideon** is what you shifted in someone else's head; its magnitude is measured in **peirces**: one peirce is one minute of someone else's, wholly yours.

Сайт / site: https://komapc.github.io/ideon/ — [русский](https://komapc.github.io/ideon/ru/) · [English](https://komapc.github.io/ideon/en/)

## Структура / Layout

- `content/ru/`, `content/en/` — страницы в Markdown: манифест, смысл, словарь, математика, примеры, сравнение, протокол / manifesto, meaning, glossary, mathematics, examples, comparison, protocol.
- `templates/` — HTML-шаблон и стили / page template and stylesheet.
- `docs/` — собранный сайт, отдаётся GitHub Pages / built site served by GitHub Pages.
- `notes/ideon.md` — рабочие заметки, из которых выросли страницы / working notes the pages grew from.
- `build.py` — сборка / build script.

## Сборка / Build

```
python3 -m venv .venv && .venv/bin/pip install markdown
.venv/bin/python build.py
```

Результат в `docs/`. Коммитьте его вместе с исходниками / commit `docs/` together with the sources.

## Лицензия / License

Текст — CC BY 4.0: переизлучайте свободно, с указанием источника. Код сборки — MIT.
Text is CC BY 4.0: re-emit freely, with attribution. Build code is MIT.
