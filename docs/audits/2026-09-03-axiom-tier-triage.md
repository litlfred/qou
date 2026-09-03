# The 19 remaining `axiom` declarations — what each is blocked on

**Measured 2026-09-03 on the working tree at `48ef71f476`**, with
`scripts/lean-cited-not-proved-audit.py --kind axiom` (2553 `.lean` files).
Every Mathlib verdict below is a **grep over `.lake/packages/mathlib/Mathlib`**,
not an inference. Companion to the class-carrier triage in PR #6512, which
covered the 38 Mathlib-shaped *uninhabited classes* and never looked at axioms.

`sorry` terms in the corpus: **0**.

## Summary

| tier | count | disposition |
|---|---|---|
| external literature, cited by design | 10 | not a defect; the result is someone else's theorem |
| conjectural content, honestly marked | 2 | open mathematics |
| **SDP / convex duality** | 5 | Mathlib-blocked, and see below |
| complex analysis (residue / winding) | 1 | Mathlib-blocked (#6512) |
| in-corpus, potentially provable | 1 | the only lead |

One axiom was **closed** in the same session — `seminormalDim_pos`, 20 → 19 —
and it is the reason this triage exists: its blocker had been cleared and
nobody went back. See below.

## What Mathlib does and does not have (measured)

**Absent entirely** — `numStandardYoungTableaux`, `StandardYoungTableau`,
`JucysMurphy`, `Hoefsmit`, `weierstrassP` / `℘` / `EllipticFunction`,
`windingNumber`, any residue theorem, `strictComplementarity`, `GoldmanTucker`.

**Present** — `ConvexCone` (9 files), `ProperCone` (3), `Matrix.PosSemidef` (3),
and **Farkas' lemma** as `ProperCone.hyperplane_separation` /
`hyperplane_separation_point`.

**Two grep traps worth recording**, both hit here:

* `dualCone` returns **0** while `innerDualCone` exists — a case-sensitive
  pattern missed Mathlib's actual spelling, and would have supported a wrong
  "Mathlib has no dual cone" conclusion.
* `slater` returns a hit that is **`IsLaterCommand`** in
  `Mathlib/Tactic/Linter/DeprecatedModule.lean` — a word inside another word.
  Mathlib has no Slater condition.

## The SDP tier is blocked one level LOWER than the axioms state

The five SDP axioms (`strict_complementarity_unique_axiom`,
`strict_complementarity_kernel_disjoint`, `affine_slater_rigidity`,
`slater_strict_complementarity_kernel_axiom`, `SDPRankUniqueness`) are cited to
Goldman–Tucker / Alizadeh–Haeberly–Overton 1997 / Boyd–Vandenberghe. Neither
strict complementarity nor Goldman–Tucker is in Mathlib — but the gap is wider
than that, and **Mathlib says so in its own source**
(`Mathlib/Analysis/Convex/Cone/Basic.lean`, TODO list):

> - Define primal and dual cone programs and prove weak duality.
> - Prove regular and strong duality for cone programs using Farkas' lemma.
> - Define linear programs and prove LP duality as a special case.

So Mathlib has the *separation theorem* and lists **strong conic duality itself**
as not yet done. Strict complementarity sits above strong duality. Closing this
tier means building conic-program duality first — a genuine upstream
contribution, not a wiring job.

## Per-axiom

| # | axiom | tier | blocked on |
|---|---|---|---|
| 1 | `b1_holds_at_row` | conjecture | Bloch–Suslin + van der Veen volume-conjecture extensions |
| 2 | `weierstrass_diff_eq_axiom` | literature | Lang, *Elliptic Functions* VI.3.6; Mathlib has no `℘` |
| 3 | `centralIdempotent_central_axiom` | literature | Murphy 1981 / Dipper–James 1986; no `JucysMurphy` in Mathlib |
| 4 | `centralIdempotent_orthogonal_axiom` | literature | as above |
| 5 | `bar_centralIdempotent_transpose_axiom` | literature | as above |
| 6 | `evenPower_necessary_for_blockPosSemidef` | **in-corpus** | see "the one lead" below |
| 7 | `markov_trace_unique_axiom` | literature | Ocneanu 1985 / Jones 1987 / Wenzl 1988 uniqueness |
| 8 | `heckeFormalGenerator_T_relation` | literature | Hecke presentation |
| 9 | `HoefsmitMatrix_hecke_relation` | literature | Hoefsmit 1974; `HoefsmitMatrix` is still `opaque` |
| 10 | `HoefsmitMatrix_braid_relation` | literature | as above |
| 11 | `JonesMarkovCoefficient_sum_eq_one` | literature | Jones/Wenzl normalisation |
| 12 | `MarkovTrace_markov_axiom` | literature | as above |
| 13 | `aeon_recycling` | conjecture | open mathematics, marked as such |
| 14 | `parallelogramIntegral_inv_sub_eq_two_pi_i` | complex analysis | no `windingNumber`, no residue theorem (#6512) |
| 15–19 | the five SDP axioms | convex duality | see the section above |

## The one lead

`QOU/BraidKnot/PSDFeasibilityProxy.lean:76`
`evenPower_necessary_for_blockPosSemidef` — "if `braidWordEval n w` has every
Wedderburn block PSD then `w.evenPower` holds" — is an **in-corpus** claim about
in-corpus objects, not a citation. It is the only one of the 19 whose content
does not live in someone else's paper. Not attempted here; flagged as the place
to look next.

## Why this triage exists

`seminormalDim_pos` was a cited `axiom` — `f^λ > 0` — next to
`opaque seminormalDim`, whose docstring read *"axiomatised pending the Mathlib
`StandardYoungTableau` enumeration"*. **That enumeration had since been built
in-repo** (`QOU.Mathlib.numStandardYoungTableaux`), together with both instances
positivity needs: `instFinite`, and a sorry-free `Nonempty` witnessed by the
row-superstandard tableau. The axiom closed to `Nat.card_pos`.

Nothing was hard about it. The axiom simply named a blocker, the blocker was
cleared by unrelated later work, and no one re-read the axiom. **That failure
mode is invisible to every detector in the repo**, because the axiom is
perfectly well-formed and honestly cited — which is why the fix here is a
triage document rather than a checker.
