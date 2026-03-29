---
name: md-authoring
roles: [reader, collaborator, owner]
---

# Markdown Authoring Conventions

## Role

Enforce authoring conventions for `.md` content files so they render
correctly in both the HTML viewer (KaTeX + `mdToHtml`) and the LaTeX
pipeline. Flag violations before they reach the viewer.

## Rendering pipeline

Content `.md` files are rendered by two pipelines:

1. **HTML viewer** (`folio-assistant/ui/app.js` → `mdToHtml()`) —
   KaTeX for math, custom regex for markdown → HTML.
2. **LaTeX pipeline** (`content/pipeline/render-latex.ts`) —
   remark parse → LaTeX AST.

Both pipelines have limitations. These conventions ensure content
works in both.

## Rules

### 1. Bold and italic may span lines

The HTML renderer supports `**bold**` and `*italic*` spanning
multiple lines. This is the standard pattern for wrapped prose:

```md
the **quantum observable
universe** (QOU).
```

### 2. `\cite{key}` renders as `[key]` in HTML

The HTML viewer converts `\cite{key}` to a bracketed reference
`[key]`. The LaTeX pipeline handles it natively. Both work, but
be aware the HTML rendering is simple — no bibliography lookup,
no hyperlinks, just `[key]`.

### 3. Use `--` for en-dash, `---` for em-dash

The HTML renderer converts `--` → `–` and `---` → `—`.
**Do not** use Unicode en/em dash characters directly — they work
but are less portable.

### 4. Display math: blank line before `$$`

The `mdToHtml` regex for display math requires `$$` to be preceded
by a paragraph break (blank line) to reliably detect it as display
rather than inline:

```md
The archimedean tuple is

$$
  (\mathbf{C},\; \theta,\; G,\; \mathcal{S}).
$$
```

**Wrong** (may render inline or break):
```md
The archimedean tuple is
$$
  ...
$$
```

### 5. No `\operatorname{}` — use `\mathrm{}`

KaTeX in the viewer does not support `\operatorname{}` by default.
Use `\mathrm{}` instead:

```md
$\mathrm{Vol}(K)$     ← correct
$\operatorname{Vol}(K)$ ← KaTeX error
```

### 6. No raw LaTeX commands outside math

The markdown → HTML converter only passes through content inside
`$...$` or `` ```tex `` blocks. Bare `\mathrm{...}` outside
delimiters renders as literal text.

### 7. Math in titles is supported

Block titles (in `.ts` manifests) may contain inline math in
`$...$` delimiters. The `escapeLatex()` function preserves these.

### 8. Tables use pipe syntax

```md
| Header 1 | Header 2 |
|----------|----------|
| cell     | cell     |
```

Tables are rendered as `<table class="md-table">` in the viewer.

### 9. Headings use `##` and `###`

In `.md` content files, `## Heading` renders as `<h3>` and
`### Heading` as `<h4>`. `# Heading` is reserved for chapter titles.

### 10. Lists

Ordered (`1. item`) and unordered (`- item`) lists are supported.
Nested lists are not yet supported by `mdToHtml`.

### 11. Cross-references

Use `[text](#label)` for cross-references. These become clickable
`<a class="uref">` links with hover preview in the viewer.

### 12. Inline code

Use backticks for inline code: `` `code` ``. Rendered with
monospace font and subtle background.

## QC checklist

When reviewing `.md` content, check:

- [ ] No `\operatorname{}` — replaced with `\mathrm{}`
- [ ] Display math has blank line before `$$`
- [ ] No raw LaTeX outside `$...$` or `` ```tex `` blocks
- [ ] `\cite{}` keys match entries in `content/schema/references.ts`
- [ ] Cross-refs `[text](#label)` point to valid labels
- [ ] Bold/italic delimiters are properly closed
- [ ] Tables have separator row (`|---|---|`)
- [ ] No Unicode math symbols that should be in `$...$`
