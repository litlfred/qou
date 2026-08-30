---
# qou-2u39
title: building-block-knots.lean asserts Vol(4_1) = a truncated decimal with an equals sign
status: todo
type: bug
priority: normal
created_at: 2026-08-30T15:04:15Z
updated_at: 2026-08-30T15:05:01Z
---

Found while exactifying `MostowRigidity.knot5_2` (bean `qou-f8lit` item 1, PR #6263). Two
`:leanval[Vol_4_1]` truncation sites survive outside the `Encounter` chapter; both were
assessed and **only one carries a defect, and it is not the exactification defect.**

## The two sites

    observations/building-block-knots.lean:43
      /-- Vol(4₁) = 2.02988321281930 (figure-eight, exact: 2·Cl₂(π/3)). -/
      noncomputable def vol_figure_eight : ℝ := 2.02988321281930  -- :leanval[Vol_4_1]{precision=15}

    knots-particles-confinement/knot-particle-generation.lean:71
      /-- Vol(4₁) = 2·Cl₂(π/3) ≈ 2.0298832128 (figure-eight knot, muon). -/
      noncomputable def vol_figure_eight : ℝ := 2.0298832128  -- :leanval[Vol_4_1]{precision=11}

## The defect: one docstring asserts `=` where the claim is false

`building-block-knots.lean` writes *"Vol(4₁) **=** 2.02988321281930 ... exact:
2·Cl₂(π/3)"*, putting an equals sign between a 15-digit truncation and the exact form it
names in the same sentence. They differ at the 16th digit. `knot-particle-generation.lean`
writes `≈` and is correct.

This is the AGENTS.md §7ab rule (`$\approx$`, never `$=$`, for a derived numerical value)
applied to a Lean docstring. One-character fix: `=` → `≈`.

## What is NOT wrong: these should NOT be exactified

The `MostowRigidity` defect was specific — a bridge statement keyed on the literal was
**unsatisfiable** against the sorry-free `figureEightTriangulation.volume = VOL_4_1`. There
is no such equality here. Both sites are **tables of numerical constants** whose other
entries are decimals or `0` (`vol_trefoil := 0`, `vol_cinquefoil := 0` — non-hyperbolic),
feeding numerical mass computations rather than exact comparisons. Exactifying one entry of
a decimal table makes the table inconsistent and buys nothing.

Recording that assessment explicitly, because "two more `:leanval[Vol_4_1]` sites" reads
like remaining drain from the same arc and it is not.

## Why it is not fixed in #6263

Different chapter, and these are content-block Lean with `.qa.json` sidecars — the fix is
one character but its verification path is `qa-sweep` on the touched criteria, which is
heavier than the change and unrelated to that PR's scope (strict `0 < D(z)`).
