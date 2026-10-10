---
# qou-igaj
title: 'Render defect: raw LaTeX in .md prose is escaped, not passed through (575 occurrences, 64 files)'
status: completed
type: task
priority: normal
created_at: 2026-08-15T03:33:53Z
updated_at: 2026-08-15T21:31:47Z
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

---

## Progress (PR #5075)

The **eightfold-way chapter is done** — 15/15 blocks clean, 0 escaping
defects, 0 dead anchors. Corpus **575 -> 204** (53 files remain).

Per-file, all markup-only:

```
  color-su3-from-g2.md            58 -> 0     borromean-decuplet-derivation.md 30 -> 0
  dictionary-flavor-layer.md      53 -> 0     schur-weyl-eightfold.md          42 -> 0
  eightfold-open-problems.md      50 -> 0     eightfold-intro.md               28 -> 0
  q-deformation-weight-lattice.md 33 -> 0     meson-mass-splitting.md          28 -> 0
  flavor-charge-assignments.md    26 -> 0     meson-octet-decomposition.md     20 -> 0
  a2-from-three-strands.md         3 -> 0
```

### Verification recipe for the remaining 53

A checker was written for this and is worth reusing rather than
re-deriving: render each block with `renderBlock` (NOT
`loadAndRenderBlock` — stub, always returns `""`), then assert

  - `/textbackslash|textasciitilde/` count is 0,
  - `validateLatexAst(latex).valid`,
  - every `\hyperref[...]` anchor is in the corpus label set
    (`grep -rho 'label: "[^"]*"' content --include=*.ts`).

That last check matters: `run-validate` does **not** verify
`](#anchor)` targets, so a converted `\ref` can silently point nowhere.

### What escaping was hiding (the reason this is worth doing)

Converting `\ref` to a checkable form surfaced **three dead
cross-references** that had never resolved, because the mangled form was
never resolved by anything:

| written | actual label |
|---|---|
| `chap:braids-and-knots` | `chap:path-integrals-braiding` |
| `chap:appendix-standard-model` | `app:standard-model` |
| `chap:knots-particles` | `chap:knots-particles-confinement` |

Expect more in the remaining 53 files. This is the argument for doing the
sweep at all: it is not cosmetic.

Also found, unrelated to escaping but in the same file:
`eightfold-open-problems`'s ledger pointed at its own numbered items by
number, and **4 of 8 pointers were wrong** (the list had been reordered
without updating the table). Fixed by pointing at item *names* instead,
which cannot rot. Worth checking for the same pattern elsewhere.

### Two constructs that must stay raw

Markdown cannot express them; keep them in fenced ```tex blocks, where
they pass through verbatim and their LaTeX is genuine again:

  - `\multicolumn` group-header rows in a tabular
  - `\begin{equation}\label{...}` (a numbered, referenceable equation)

### Deliberately NOT fixed (dependency-graph, not markup)

Surfaced by the qa-sweep re-runs; left for a separate pass so the
markup commits stay honest about their scope:

  - `meson-mass-splitting` **detangler-no-forward-ref FAIL** — uses
    `rem:q-deformation-weight-lattice` (manifest pos 9) from pos 4.
    Needs a block move.
  - `flavor-charge-assignments` **detangler-block-tanglement WARN** —
    forward ref to `conj:sm-hypercharge-invariant` in the SM appendix.
  - 5 blocks with `uses-editorial-hygiene` WARN, 1-2 transitively
    redundant edges each.

---

## CORRECTION (2026-08-15): most of the remainder is BROKEN MATH, not raw LaTeX

This bean was opened describing the defect as *"raw LaTeX in `.md` prose is
escaped, not passed through"* — an authoring error against AGENTS.md rule 3.
That is accurate for the eightfold-way chapter (fixed, PR #5075). It is
**not** accurate for the rest, and the rest is worse.

**The dominant remaining class is a markdown LIST-PARSER HIJACK of valid
math.** A multi-line inline `$...$` span whose continuation line begins with
`+`, `-` or `*` is parsed as a list item. The math span is split, an `\item`
is emitted mid-formula, and the remainder of the expression is escaped into
literal text.

AGENTS.md's render-QA rule already warns about this for `$$...$$` (*"no line
starting with `+`/`-`/`*` inside `$$…$$` — markdown list-parser hijack"*). It
happens in multi-line **inline** math too, which the rule does not mention.

Consequences that change how this drain should be run:

- **The author did nothing wrong** in these files. The math is correct, the
  authoring is legal, only the line-wrap position is wrong.
- **The fix is one line** — move the operator to the end of the previous
  line. No symbol of mathematics changes.
- **It corrupts MATHEMATICS, not formatting.** `q-ns-proof-details`' entire
  uniqueness argument (the Gronwall energy estimate) was rendering as
  escaped text with a stray `\item` in the middle.

Eight such edits took the corpus **204 -> 104** occurrences, **53 -> 45**
files. Highest-leverage work in this bean by a wide margin.

### Detection — two things that do NOT work

Both learned by getting them wrong:

1. **Grepping for lines starting with `+`/`-`/`*` is not a detector.** Most
   are ordinary markdown lists — `notation-collisions` has 46 and is fine.
2. **Keying on "an escaped output line contains `\item`" also miscounts**,
   because a genuine list containing math that escapes for some other reason
   matches too. An A/B classifier built on this reported 132/71; do not trust
   that split.

**The renderer is the only reliable oracle.** Render with `markdownToLatex`,
count `textbackslash|textasciitilde` in the output, print the offending
OUTPUT lines, and read back to the source. `where.ts` in the session
scratchpad does exactly this and is worth re-creating: it prints each
escaped output line, which makes the cause obvious in one look.

### One file needs a different repair

`mass-theory/phi-q-tower-algebraic-stratification-proof.md` (17) is **not** a
line-wrap case. Its **source** is already corrupted, carrying escaped `\$` and
`\_` from some earlier bad pass:

```
   \$\bigl\lvert\prod\_i \hat V\_i\bigr\rvert + \sum\_{i} \Phi\_q(|\hat V\_i|)
   * z^2 \sum\_{(i,j)} \Phi\_q(|\hat V\_i \hat V\_j|)$.
```

That needs the original expression reconstructed, not shuffled. Left alone
deliberately. Worth checking whether other files carry the same `\$`/`\_`
signature — it implies a bad escaping pass ran over the corpus at some point.

### State after this pass

**104 occurrences across 45 files.** Remaining top offenders:

```
  17  mass-theory/phi-q-tower-algebraic-stratification-proof  (corrupted source, see above)
  12  predicted-spectra/bloch-group-quotient-construction
   9  observations/w-boson-mass-discrepancy-table3-data
   7  observations/w-boson-mass-discrepancy-table5-data
   6  appendix-surreals/spectral-normal-form
```

Note also: `lean/.lake/...` appears in the raw scan and is a **build
artifact**, not corpus content — exclude `-not -path '*/.lake/*'` so it is
not in the denominator.

## Closed 2026-08-15 — drained to zero (PR #5138)

Re-measured against the renderer over the whole corpus rather than by
regex. Every `.md` with a `.ts` sibling was rendered through
`renderBlock` and the output searched for `\textbackslash{}`:

    rendered=3580  threw=5  no-ts=23
    FILES WITH \textbackslash{}: 0   TOTAL: 0

Zero. The class is drained.

**The intermediate counts in this bean were wrong and should not be
cited.** The 575/64 opening figure and the 56/34 I was carrying at the
end both came from regex heuristics over the source, which over- and
then under-counted. Only the render-side `\textbackslash{}` measurement
is authoritative, because it is the actual artifact the defect produces.

**Do not treat `findMathTextSeams` as a successor metric.** It reports
70 seams across 33 files, but those are a different and benign thing —
the largest (17 in `recursive-atom-knot-atlas-registry`) are footnote
markers like `Helium$^{\diamond\star}$`, which render as
`Potassium\allowbreak{}$^{\star}$`. That is the pipeline's ordinary
math/text seam handling working, not a backlog.

Last repairs, all on PR #5138:
- `phi-q-tower-algebraic-stratification-proof` — the corrupted mass
  formula, reconstructed from the parent proposition (a list parser had
  turned the middle `+` into a `*`, making it read as a product)
- `quantum-peter-weyl-proof` — two Lean field names in prose
- `mass-tower-syt-cells` — a bare `Φ\_q`

Spun out of the same corpus render: five blocks whose manifest the
pipeline cannot load at all (bean `qou-6y28`), and
`content/pipeline/block-manifest-audit.ts` to keep that class closed.
