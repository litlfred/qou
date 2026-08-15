---
# qou-igaj
title: 'Render defect: raw LaTeX in .md prose is escaped, not passed through (575 occurrences, 64 files)'
status: todo
type: task
created_at: 2026-08-15T03:33:53Z
updated_at: 2026-08-15T03:33:53Z
---


## What is wrong

`markdownToLatex` (folio-assistant `content/pipeline/render-latex.ts`) escapes
raw LaTeX appearing in `.md` prose instead of passing it through. Measured
directly against the renderer, not inferred:

| written in `.md` | renders as |
|---|---|
| `\emph{x}` | `\textbackslash\{\}emph\{x\}` |
| `\textbf{x}` | `\textbackslash\{\}textbf\{x\}` |
| `Prop~\ref{prop:foo}` | `Prop\textasciitilde{}\textbackslash\{\}ref\{prop\}` (note: also truncates at the `:`) |
| `\S\ref{sec:bar}` | `\textbackslash\{\}S\textbackslash\{\}ref\{sec\}` |
| `\begin{center}` / `\begin{tabular}` | `\textbackslash\{\}begin\{center\}` etc. |
| `\cite{key}` | `\cite{key}` — the only one that survives |

This is exactly what `AGENTS.md` §"TeX authoring patterns for agents" rule 3
already says ("Never use raw TeX commands in prose outside `$...$`"), so the
renderer is behaving as documented. The defect is that ~64 files do not follow
it and nothing catches them.

## Correct forms (all verified against the renderer)

- `[text](#label)` -> `\hyperref[label]{text}`
- `**bold**` -> `\textbf{...}`
- markdown table -> proper `booktabs` `tabular` inside `adjustbox` (better
  than the hand-written `\begin{center}\begin{tabular}`, which currently
  renders as literal escaped text)
- fenced ```tex block -> passthrough, for anything genuinely needing raw LaTeX

## Measured scope (this paper)

3580 `.md` scanned; **64 files, 575 occurrences**. Epicentre is the
eightfold-way chapter, 368 (~64%):

```
  58 eightfold-way/color-su3-from-g2.md
  53 eightfold-way/dictionary-flavor-layer.md
  50 eightfold-way/eightfold-open-problems.md
  42 eightfold-way/schur-weyl-eightfold.md
  33 eightfold-way/q-deformation-weight-lattice.md
  30 eightfold-way/borromean-decuplet-derivation.md   <- weight table is escaped
  28 eightfold-way/eightfold-intro.md
  28 eightfold-way/meson-mass-splitting.md
  26 eightfold-way/flavor-charge-assignments.md
  20 eightfold-way/meson-octet-decomposition.md
  24 fluid-dynamics/p1-spectral-sobolev-proof.md
  17 mass-theory/phi-q-tower-algebraic-stratification-proof.md
  15 mass-theory/skein-generation-proof.md
   3 eightfold-way/a2-from-three-strands.md
```

Reproduce: render each `.md` through `markdownToLatex` and count
`/textbackslash|textasciitilde/`.

## Why it went unnoticed

`loadAndRenderBlock` in the same platform file is a **stub** — it always
returns `latex: ""` regardless of input:

```ts
// Placeholder — actual block loading happens in async pipeline
return { latex: "", block: { kind: "prose" } as Block, mdContent };
```

So any render-QA that goes through it AST-validates the empty string and
reports `valid: true`. That is a guaranteed false pass. Use `renderBlock`
(block + md content) instead. Fixing or removing that stub belongs in
`litlfred/folio-assistant`, not here.

## Suggested next step

Not a blind sweep — the table conversions need per-file care, and `\ref`
targets must be checked to resolve (`run-validate` does **not** verify
`](#anchor)` targets; verify against the corpus label set separately).
Do the eightfold-way chapter first: it is the epicentre, and it is the
chapter where a reader now sees a clean block (`prop:baryon-octet-decomposition`,
PR #5075) sitting next to broken siblings.

Worth adding alongside the fix: a render-QA criterion that fails on
`textbackslash`/`textasciitilde` in rendered output, so this cannot recur.

Found 2026-08-15 while authoring the baryon-octet block (bean qou-wd07,
PR #5075). Deliberately NOT fixed in that PR — the new block is clean, the
sweep is separate work.
