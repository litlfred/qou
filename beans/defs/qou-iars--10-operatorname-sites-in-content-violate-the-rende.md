---
# qou-iars
title: 10 \operatorname sites in content/ violate the render-QA gate
status: completed
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-31T06:01:00Z
updated_at: 2026-11-15T14:40:00Z
parent: qou-mub3
---

AGENTS.md's render-QA gate lists, among the mandatory preflight greps, *"no
`\operatorname{}` (KaTeX rejects → use `\mathrm{}`)"*. Measured on `main`
2026-08-31: **10 sites** — 9 in `.ts` block titles, 1 in `.md`.

Found incidentally: regenerating `definition-index.md` produced a one-line diff
where a title's `\mathrm{Re}`/`\mathrm{Im}` read `\operatorname{Re}`/`\operatorname{Im}`.
The index was faithfully carrying its source; the source is what violates the
rule.

**My first read was that main had just regressed. It had not** — the population
is pre-existing and spread across five files, and only one of the ten happens to
sit in a block *title*, which is the only place the index can see. A generated
file surfaces exactly the subset of a defect that it happens to carry, and that
subset is not the defect's size.

Known sites:

- `observations/observations.ts:183`
- `mass-theory/mass-theory.ts:196` (×2 on the line), `:1190` (×2)
- `mass-endomorphism/mass-endomorphism.ts:99` (×2)
- `mass-theory/c1-theta-zero-locus-and-pole-divisor.ts:153` — note this one is
  `\operatorname{re}`, **lowercase**, and probably means Lean's `Complex.re`
  rather than the operator. Do not sweep it with the others without reading it.

**Not fixed here, deliberately.** Ten sites across five files of content this PR
does not otherwise touch is widening, and the fix is a judgement about each
title's intent rather than a substitution.

**One thing NOT established, and it matters for priority:** whether these
actually break rendering today. The AGENTS.md rule asserts KaTeX rejects
`\operatorname`, but current KaTeX does support it, so the rule may predate that
or may be about the LaTeX path rather than KaTeX. I did not run the renderer.
So this is *"violates a stated repo rule, ten times"* — not *"the paper renders
wrong"*. Someone should settle which before spending effort on it.

SUPERSEDED 2026-11-15. AGENTS.md (corrected 2026-09-03, citing this bean) rules that \operatorname is NOT a violation: the viewer loads KaTeX 0.16.11, which supports it, and pdflatex/amsmath always did. Nothing to fix.
