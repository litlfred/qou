---
name: rendering-fixes
roles: [reader, collaborator, owner]
description: >
  Quick-fix reference for common rendering errors found by the rendering-auditor.
  Agents should consult this when editing content blocks to avoid introducing
  issues and to fix flagged problems efficiently.
---

# Rendering Fixes

## Role

Quick-fix cookbook for common rendering errors in `.md` and `.ts` content
files. Each entry shows the error pattern, why it breaks, and the exact fix.
Agents editing content blocks should check this list before committing.

## Fix Index

| # | Error | Severity | Auto-fixable? |
|---|-------|----------|---------------|
| F1 | Backtick/dollar mismatch | Error | Yes |
| F2 | Bare `\eqref{}` outside math | Error | Yes |
| F3 | Bare TeX in `.ts` title | Error | Yes |
| F4 | Single-line `$$...$$` inside list | Error | Yes |
| F5 | Extra trailing pipe in table | Warning | Yes |
| F6 | `\operatorname` vs `\mathrm` | Style | Yes |
| F7 | `\mathscr` KaTeX compat | Warning | Yes |
| F8 | `$$` without preceding blank line | Warning | Yes |
| F9 | `&` in prose outside math | Error | Yes |
| F10 | Raw TeX outside math delimiters | Error | Yes |
| F11 | Wrong notation register | Error | Yes (pattern) |
| F12 | Missing SVG pre-render for fenced tex | Warning | Script |
| F13 | Orphan cross-reference | Warning | Manual |
| F14 | Missing bibliography entry | Error | Manual |

---

## F1: Backtick/dollar mismatch

**Pattern**: A backtick `` ` `` opens what should be math, but `$` closes it
(or vice versa). Creates an unclosed math environment that swallows
subsequent lines.

```md
<!-- BROKEN: backtick opens, dollar closes -->
$q = 1.10998$ from `Vol(4_1) = 2.02988321281931$ and

<!-- FIXED: consistent delimiters -->
$q = 1.10998$ from $\mathrm{Vol}(4_1) = 2.02988321281931$ and
```

**Detection**: Grep for lines with mismatched `` ` `` and `$` counts.
**Fix**: Replace `` ` `` with `$` (for math) or `$` with `` ` `` (for code).
If the content is mathematical, use `$...$` and wrap function names in
`\mathrm{}`.

---

## F2: Bare `\eqref{}` outside math mode

**Pattern**: `\eqref{eq:label}` used in prose text without `$...$` wrapping.
Works in LaTeX but renders as literal text in the HTML viewer (KaTeX only
processes content inside math delimiters).

```md
<!-- BROKEN: bare \eqref in prose -->
diagram \eqref{eq:su2-emergence-diagram} from the top-left

<!-- FIX OPTION 1: markdown cross-ref (preferred) -->
diagram [above](#eq:su2-emergence-diagram) from the top-left

<!-- FIX OPTION 2: wrap in math (if equation number needed) -->
diagram $\eqref{eq:su2-emergence-diagram}$ from the top-left
```

**Detection**: `grep -n '\\eqref' *.md | grep -v '\$'`
**Fix**: Convert to `[text](#label)` cross-ref (works in both pipelines).

---

## F3: Bare TeX in `.ts` title field

**Pattern**: Title contains TeX like `d_q^2` without `$...$` wrapping.
The `escapeLatex()` function escapes `_` and `^` as `\_` and
`\textasciicircum{}`, producing garbled output.

```ts
// BROKEN: bare TeX — renders as "d\_q\textasciicircum{}2"
title: "d_q^2 does not vanish",

// FIXED: wrapped in $...$
title: "$d_q^2$ does not vanish",
```

**Detection**: Grep `.ts` title fields for `_` or `^` outside `$...$`.
**Rule**: Any TeX in a title MUST be inside `$...$` delimiters.

---

## F4: Single-line `$$...$$` inside list items

**Pattern**: Display math `$$...$$` written on a single line (or spanning
2 lines with both `$$` at line boundaries) inside a markdown list item.
The pipeline may convert the opening `$$` to `\[` but leave the closing
`$$` as-is, producing a mixed-delimiter error.

```md
<!-- BROKEN: single-line display math in list -->
3. Define the Chern classes:
   $$c_i(X) := c_i(\tau(X)) \in H^{2i}_{\mathrm{dR}}(\mathrm{Spec}\,R),$$

<!-- FIXED: display math on separate lines -->
3. Define the Chern classes:

   $$
   c_i(X) := c_i(\tau(X)) \in H^{2i}_{\mathrm{dR}}(\mathrm{Spec}\,R),
   $$
```

**Detection**: Grep for `$$` that starts and ends on the same line.
**Fix**: Put `$$` on its own line, with a blank line before the opening `$$`.

---

## F5: Extra trailing pipe in markdown table

**Pattern**: Table rows have more `|` separators than the header row,
creating an extra empty column.

```md
<!-- BROKEN: trailing | | creates extra column -->
| Red | $S_3^{(r)}$ | $c_r = w_2 - z$ | |
| Green | $S_3^{(g)}$ | $c_g = w_3 - z$ | |

<!-- FIXED: consistent column count -->
| Red | $S_3^{(r)}$ | $c_r = w_2 - z$ |
| Green | $S_3^{(g)}$ | $c_g = w_3 - z$ |
```

**Detection**: Count `|` per row; flag rows with more than header.
**Caveat**: `|` inside `$...$` (absolute values) creates false positives.

---

## F6: `\operatorname` vs `\mathrm`

**Pattern**: `\operatorname{Vol}` works in both LaTeX and KaTeX but
is inconsistent with the project convention of `\mathrm{Vol}`.

```md
<!-- INCONSISTENT (works but non-standard for project) -->
$\operatorname{Vol}(K)$

<!-- PREFERRED -->
$\mathrm{Vol}(K)$
```

**When to use `\operatorname`**: Only for operators that need special
spacing (like `\lim`, `\sup`). For named functions, use `\mathrm{}`.

---

## F7: `\mathscr` KaTeX compatibility

**Pattern**: `\mathscr{L}` may not render in older KaTeX versions.

```md
<!-- RISKY: needs KaTeX >=0.16 -->
$\mathscr{L}_q$

<!-- SAFE: always renders -->
$\mathcal{L}_q$
```

**Fix**: Use `\mathcal{}` unless the script font distinction is
semantically necessary.

---

## F8: `$$` without preceding blank line

**Pattern**: Display math `$$` immediately follows text without a blank
line. Some markdown parsers may treat it as inline math.

```md
<!-- RISKY: may parse as inline -->
The formula is:
$$
  x = y
$$

<!-- SAFE: blank line forces display -->
The formula is:

$$
  x = y
$$
```

**Fix**: Add a blank line before `$$`.

---

## F9: Ampersand in prose

**Pattern**: `&` in prose text (outside `$...$` or `` ```tex `` blocks)
becomes a column separator in LaTeX, causing compilation errors.

```md
<!-- BROKEN in LaTeX -->
protons & neutrons form nuclei

<!-- FIXED -->
protons and neutrons form nuclei
```

**Exception**: `&` inside math mode is fine (matrix/alignment separators).

---

## F10: Raw TeX outside math delimiters

**Pattern**: LaTeX commands like `\mathrm{}`, `\textbf{}`, `\emph{}`,
`\frac{}{}` used in prose without `$...$` wrapping. Renders as literal
text in both pipelines.

```md
<!-- BROKEN: raw TeX in prose -->
the group \mathrm{SU}(2) acts on

<!-- FIXED: wrapped in math -->
the group $\mathrm{SU}(2)$ acts on
```

**Detection**: Grep for `\commandname{` on lines without `$`.

---

## F11: Notation register violations

These are the most common register violations. Each has a mechanical fix.

### Elliptic curves: `$E_z$` or `$E_q$` for curves

```md
<!-- WRONG -->
the elliptic curve $E_z$
the Descartes curve $E_q$

<!-- RIGHT -->
the elliptic curve $\mathcal{E}_z$
the Descartes curve $\mathcal{E}_q$
```

### Categories: `$\mathcal{C}$` for categories

```md
<!-- WRONG (calligraphic is for sheaves/bundles) -->
$(\mathcal{C}, A, \tau)$

<!-- RIGHT (bold for categories) -->
$(\mathbf{C}, A, \tau)$
```

### Mass: plain `$m$` for categorical mass

```md
<!-- WRONG -->
the mass $m(\varrho) = \mathrm{Vol}(K)$

<!-- RIGHT -->
the mass $\mathfrak{m}(\varrho) = \mathrm{Vol}(K)$
```

### Energy: standalone `$E$` for categorical energy

```md
<!-- WRONG -->
the energy function $E$

<!-- RIGHT -->
the energy function $\mathbf{E}$
```

### Vortex: `$\gamma$` for vortex/closed cycle

```md
<!-- WRONG (gamma is for Euler-Mascheroni / Dirac) -->
let $\gamma \colon S^1 \to \tau(A)$ be a knot embedding

<!-- RIGHT -->
let $\varrho \colon S^1 \to \tau(A)$ be a knot embedding
```

### Hecke relation: `$\sigma_i$` in the Hecke relation

```md
<!-- WRONG (sigma is the braid generator, T is the Hecke image) -->
the Hecke relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$

<!-- RIGHT -->
the Hecke relation $T_i^2 = (q - q^{-1})T_i + 1$
```

**Note**: `$\sigma_i$` IS correct for the braid group generator in
`$B_n$`. Only change to `$T_i$` when writing the Hecke relation itself.

### Fibre functor: `$\omega$` for the canonical fibre functor

```md
<!-- WRONG (omega for the canonical functor) -->
the fibre functor $\omega$

<!-- RIGHT -->
the fibre functor $\tau$
```

**Exception**: When discussing the atlas of ALL fibre functors,
`$\omega, \omega'$` for generic (non-canonical) functors is acceptable.

### Numerical q outside allowed chapters

```md
<!-- WRONG (in ch2/ch3/ch4/ch5/ch6) -->
At $q = 1.1097$, the ...

<!-- RIGHT (use symbolic q) -->
For the substrate parameter $q$, the ...
```

Numerical `$q$` values allowed only in: ch0 (introduction), ch7
(physical observations), ch9 (information theory).

---

## F12: Missing SVG pre-render for fenced tex blocks

**Pattern**: A `.md` file contains a `` ```tex `` fenced block (typically
tikzcd) but the corresponding `.ts` manifest has no `rendered:` array.
The block shows as raw LaTeX in the HTML viewer.

**Fix**: Run the pre-render pipeline:
```bash
cd content && bun run render-tex
```

Then add the generated SVG paths to the `.ts` manifest:
```ts
rendered: [
  { mime: "image/svg+xml", url: "rendered/block-name-0.svg", blockIndex: 0, hash: "..." },
],
```

---

## F13: Orphan cross-reference

**Pattern**: `[text](#label)` in `.md` or `\hyperref[label]{}` in rendered
`.tex` points to a label that doesn't exist. Renders as `??` in PDF.

**Causes**:
- Block was deleted but references remain
- Label was renamed without updating `uses[]`
- Cross-paper ref in single-paper build (expected)

**Fix**: Search for the label; if it was renamed, update the reference.
If the block doesn't exist yet, create it or remove the reference.

---

## F14: Missing bibliography entry

**Pattern**: `\cite{key}` in `.md` or `-- Ref: [key]` in `.lean` refers
to a key not in `content/schema/references.ts`.

**Fix**: Add a `ref()` entry in `references.ts`:
```ts
ref({
  id: "author2024",
  type: "article-journal",
  title: "Paper title",
  author: [{ family: "Author", given: "A." }],
  issued: { "date-parts": [[2024]] },
  DOI: "10.xxxx/xxxxx",
}),
```

Then run `bun run export-bibtex` and `bun run validate-refs`.

---

## Pre-commit checklist (for agents editing content)

Before committing changes to a content block, verify:

- [ ] All `$...$` delimiters are balanced (no mixed backtick/dollar)
- [ ] Display math `$$` is on its own line with blank line before
- [ ] No raw TeX commands outside math delimiters
- [ ] `.ts` title fields wrap TeX in `$...$`
- [ ] Markdown tables have consistent column counts
- [ ] No `\eqref{}` outside math — use `[text](#label)` instead
- [ ] Notation register compliance (check F11 patterns)
- [ ] `\cite{key}` keys exist in `references.ts`
- [ ] `uses[]` labels resolve to existing blocks
- [ ] Fenced `` ```tex `` blocks have `rendered:` SVGs in manifest
