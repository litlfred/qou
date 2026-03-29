---
name: html-rendering-qc
roles: [reader, collaborator, owner]
---

# HTML Rendering QC

## Role

Audit `.md` content files for patterns that cause rendering failures
in the HTML viewer (`folio-assistant/ui/app.js`). Report issues with
specific file paths and line numbers.

## Renderer: `mdToHtml()`

Located in `folio-assistant/ui/app.js`. Processing order:

1. Display math `$$...$$` → KaTeX display spans
2. Inline math `$...$` → KaTeX inline spans
3. Fenced code blocks `` ```lang `` → `<pre>` or `<div class="txb">`
4. Tables `|...|` → `<table class="md-table">`
5. Headings `##`, `###` → `<h3>`, `<h4>`
6. Bold `**...**` → `<strong>` (multiline OK)
7. Italic `*...*` → `<em>` (single line only)
8. Inline code `` `...` `` → `<code>`
9. Citations `\cite{key}` → `<span class="cite">[key]</span>`
10. En/em dash `--`/`---` → `–`/`—`
11. Cross-refs `[text](#label)` → `<a class="uref">`
12. List items `1.` / `-` → `<li>`
13. Paragraphs `\n\n` → `</p><p>`

## Known limitations

| Pattern | Issue | Fix |
|---------|-------|-----|
| `` ```tex `` without rendered SVG | Shows raw LaTeX code | Run `bun run render-tex` then `bun run export-json` |
| `\operatorname{X}` | KaTeX error | Use `\mathrm{X}` |
| `$$` without preceding blank line | May parse as inline | Add blank line before `$$` |
| `*italic*` spanning lines | Won't match (single-line regex) | Keep italic on one line |
| Nested lists | Not supported | Flatten or use prose |
| `\cite{key}` | No bibliography lookup | Accept `[key]` display |
| `$...$` with newlines inside | Works (regex allows it) | OK |
| Raw LaTeX outside math | Renders as text | Wrap in `$...$` |
| `&` in prose (outside math) | LaTeX error in pipeline | Use `and` or wrap in math |

## Interactive features

### Hover preview

Cross-ref links (`a.uref`) show a popup on hover with the
referenced block's content. The popup has:
- Expand (⛶) → fullscreen modal
- Close (×)

### Copy button

Blocks with stub status (`has_sorry`, `stated`, `not_started`, or
missing lean source for provable kinds) show a 📋 button on hover.
Copies block metadata + markdown + lean stub.

### Index page (tab D)

Index entries are clickable — expands the definition inline in the
table row. Click again to collapse. Does not navigate away.

## Audit procedure

1. Run `bun run content/pipeline/export-json.ts` to build paper.json
2. Serve locally and inspect in browser
3. For bulk checking, grep `.md` files for known problem patterns:

```bash
# Find \operatorname usage
grep -rn '\\operatorname' content/**/*.md

# Find $$ without preceding blank line
grep -B1 '^\$\$' content/**/*.md | grep -v '^--$' | grep -v '^$'

# Find raw LaTeX outside math
grep -Pn '\\(?:mathrm|textbf|emph)\{' content/**/*.md | grep -v '\$'

# Find unclosed bold/italic
# (manual review needed — regex can't reliably detect this)
```

## Sidebar behavior

The sidebar collapses to a 40px strip showing tab letters
(I, 1–8, G, T, D). Hovering expands to full 260px.

- **☰** button: hides sidebar completely
- **⇔** button: toggles wide mode (800px → 1200px content)
- Both preferences persist to localStorage

## Diff view

Diff computation can be expensive. The diff fetch:
- Shows a cancel button during loading
- Aborts the fetch if the user switches to another mode
- Uses `AbortController` for clean cancellation
