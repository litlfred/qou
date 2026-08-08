---
# qou-2tkh
title: 'fDimSkew missing containment guard made branching_two_one FALSE — fixed; sweep the other cited sorries for falsity'
status: completed
type: task
created_at: 2026-08-08T16:20:00Z
updated_at: 2026-08-08T16:20:00Z
---

Branch: `claude/sorry-audit-joo5` (qou).
File: `content/quantum-observable-universe/lean/QOU/BraidKnot/YoungTableauStandard.lean`.

## The finding (second of its kind today — see qou-0z7n)

`SkewStandardYoungTableau outer inner` fills `outer.cells \ inner.cells` and
imposes **no** containment `inner ⊆ outer`. The set difference is still
well-behaved — and inhabited — when `inner ⊄ outer`, so the raw
`Nat.card (SkewStandardYoungTableau outer inner)` is not the classical skew count
`f^{outer/inner}`, which is `0` off containment.

`fDimSkew` was the raw `Nat.card`. That made `branching_two_one`
(`3 · Σ_{λ⊢k} f^λ f^{λ/(2,1)} = k!`) **false, not merely open**, already at
`k = 3`:

| λ ⊢ 3 | f^λ | raw skew count | true f^{λ/(2,1)} |
|---|---|---|---|
| (3) | 1 | 1 (spurious) | 0 |
| (2,1) | 2 | 1 | 1 |
| (1,1,1) | 1 | 1 (spurious) | 0 |

raw sum `= 4`, `3 · 4 = 12 ≠ 6 = 3!`. Guarded sum `= 2`, `3 · 2 = 6` ✓.
(k = 4: surviving `(3,1), (2,2), (2,1,1)` give `3+2+3 = 8`, `3 · 8 = 24 = 4!` ✓.)

## Fix (DONE)

* `fDimSkew` guards: `if inner ≤ outer then Nat.card … else 0`.
* `row3` + `skewSYT_nonempty_of_not_le` — machine-proved witness that the guard
  is necessary, not defensive: `(2,1) ⊄ (3)` yet
  `SkewStandardYoungTableau (3) (2,1)` is inhabited (skew region is the single
  cell `(0,2)`; both strictness fields vacuous; the all-zero filling works).
  Axioms `[propext, Classical.choice, Quot.sound]`.
* Header scope note + `branching_two_one` docstring record the arithmetic and the
  representation-theoretic derivation (`k!·f^μ/m!` counted two ways).

The three RSK `sorry`s stay — they are genuinely open — but they now sit in front
of *true* statements.

## TODO — the general sweep

Two false-behind-a-`sorry` findings in one pass is a pattern, not a coincidence.
Both had the same shape: **a cited `sorry` whose statement was never checked at a
small instance.** Sweep every remaining cited `sorry` the same way — evaluate the
claim at the smallest nontrivial parameter and check it by hand:

- [x] `QGevreyOrder.cauchyMul_order` — **was false** (qou-0z7n). No
      non-cancellation hypothesis; `b = 0` breaks it. Fixed + `≤` half proved.
- [x] `YoungTableauStandard.branching_two_one` — **was false**. Unguarded
      `fDimSkew`. Fixed.
- [x] `HadamardFactorization.hadamard_factorization` — **was false**.
      `IsEntireOfOrderLE f ρ` is satisfiable at `ρ < 0` (the constant `1`;
      `‖z‖^ρ` is bounded on `‖z‖ ≥ 1` and `rpow` sends `0^ρ ↦ 0`), while the
      conclusion needs `(p : ℝ) ≤ ρ` for `p : ℕ`. Fixed by adding `0 ≤ ρ`;
      `hadamard_factorization_needs_nonneg_order` machine-proves the necessity.
- [x] `YoungTableauStandard.skew_le_straight` — checked at k = 3 (raw `3 ≤ 4` ✓,
      guarded `1 ≤ 4` ✓). Sound.
- [x] `YoungTableauStandard.sum_dimSYT_eq_involution` — checked at k = 3
      (`1+2+1 = 4 = I(3)` ✓). Sound.
- [x] `Mathlib/EllipticDivisorDegree.elliptic_divisor_degree_zero` — the cell is
      **half-open** (`Ico 0 1` in both coordinates), so no boundary
      double-counting; nonconstancy and rank-2 independence are both hypotheses;
      `hS` pins `S` exactly. Sound.
- [x] `SnWedderburnPartitionBridge.sn_isotypic_specht_split` — dimension count
      checks at n ≤ 3 (`1`; `1+1`; `1+4+1 = 6 = 3!`) and the `C₂` eigenvalue at
      n = 2 (`contentSqSum (2) = contentSqSum (1,1) = 1`, matching
      `centralC2_coeff_one`). Sound.
- [x] `JucysMurphy.seminormalVector_base_exists` — existential over `T₀`, and
      `StandardYoungTableau μ` / `S^μ` are nonempty/nonzero for every diagram
      including `⊥`. Sound.
- [x] `TopologicalMass/cat_descended_is_base_mass` ×2 — over `opaque` constants,
      so neither provable nor refutable as stated; documented as such in-file,
      left alone deliberately.
- [x] `Archimedean/HyperbolicVolumeIndependence`,
      `BraidsAndKnots/YoungDiagramKernel.covariance_kernel_conjecture` — both
      correctly marked OPEN CONJECTURE; nothing to do.

**Sweep result: 3 of 12 cited `sorry`s stood in front of false propositions.**
All three had the same shape — a statement never evaluated at its smallest
instance — and all three failed on a *degenerate* input the informal theorem
silently excludes (the zero sequence; a non-containing shape; a negative order).
Worth making the small-instance check part of the recipe for planting a cited
`sorry` at all.
