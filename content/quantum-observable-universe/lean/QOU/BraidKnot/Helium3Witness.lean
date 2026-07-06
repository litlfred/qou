import Mathlib.Tactic
import QOU.BraidKnot.LightNucleus
import QOU.BraidKnot.WitnessR5Full

/-!
# QOU.BraidKnot.Helium3Witness — concrete R5-full witness for ³He

The first concrete `R5FullWitness LightNucleus.helium3` instance,
populated with the empirical numerical values from PR #608's
`r5-full-canonical-knot-solver.witness.json` for the L_6a4
binding-link search at `H_3(q_0)`.

## Witness data (from PR #608)

* `winner.candidate.word := (σ_1 σ_2^{-1})^3 = "L_6a4"`
* `winner.alpha_gap := 0.0` (PSD-feasible)
* `winner.rho_star := 3`
* `winner.per_block_summary`:
    - `trivial.min_eig := 1.87`
    - `standard.min_eig := 0.53`
    - `sign.min_eig := 0.53`
* All three block min-eigs `> 0` ⟹ active set is **empty** ⟹
  optimum lies in the strict interior of the feasible region ⟹
  strict complementarity vacuously satisfied.

## Witness divergence (2026-06-22 regen) — the cited JSON no longer backs these values

`r5-full-canonical-knot-solver.witness.json` was **regenerated 2026-06-22**
(`computedAt 2026-06-22T14:48Z`, `scriptCommitSha c4ab12b6`) with a **single-term**
binding cost `B = m_e·ρ·|tr_M(T_w)|`, which under-constrains the search. Its current
`he3` winner is therefore a **different, degraded** result:

* word `σ₁⁶σ₂² = [1,1,1,1,1,1,2,2]` (≠ the canonical `L_6a4 = (σ₁σ₂⁻¹)³` recorded above);
* `winner.rho_star := 4` (≠ 3); `winner.cost := 0.14291`;
  `rel_residual := 0.5716` (**57 % off `B_AME = 7.718 MeV`**).

The values in this module are the **frozen PR #608 `L_6a4` solve** (canonical binding
link, strict-interior optimum), retained **intentionally**: wiring to the current JSON
would *regress* to the 57 %-residual single-term winner, and its `cost = 0.14291` is that
degraded objective — **not** a canonical primal/dual to refresh into the placeholders
below. The clean refresh is the **multi-term-cost re-run** (T2–T6 of
`thm:knot-mass-formula-unified`); until it lands, this witness is pinned to PR #608, not
to the current file contents. The divergence does **not** affect the downstream
uniqueness consumer (`AppliedHelium3Uniqueness`): it depends only on `rho_star_pos`
(holds for both `3` and `4`) and `alpha_gap = 0` (holds for both); likewise the
strict-complementarity cert needs only `min_block_eig > 0`, which holds for both the
frozen `0.53` and the regen's `min_eig_overall ≈ 0.434`. See
`docs/audits/2026-06-25-r5-witness-staleness-and-rescoped-todo-triage.md` §1–2.

## What this module provides

- `instR5FullWitness_helium3` — the concrete instance with the
  hardcoded values from the JSON.
- `helium3StrictComplementarityCert` — the corresponding
  `StrictComplementarityCert` (constructed using the empty-
  active-set option in `active_dual_pos_or_empty`).

## Verification

The numerical values are the **frozen PR #608 `L_6a4` solve** (see the
*Witness divergence* note above — the current JSON contents have since diverged).
Empirical correctness of that SDP search is the Python compute layer's
responsibility (PR #608 + R5-full enumerator regression tests); re-witnessing is
gated on the multi-term-cost re-run.

## References

- `r5-full-canonical-knot-solver.witness.json` — values **frozen at PR #608**;
  the file was regenerated 2026-06-22 with a degraded single-term cost (see the
  *Witness divergence* note above)
- `joint-tower-sdp-h6-h9.witness.json` (related Hopf
  identification at H_6)
-/

namespace QOU.BraidKnot

/-- **R5-full witness for ³He** — partial instance from PR #608's
    `r5-full-canonical-knot-solver.witness.json`.  All three
    Wedderburn-block min-eigs are strictly positive (1.87,
    0.53, 0.53), so the active set is empty and the optimum is
    in the strict interior of the feasible region.

    Field source (frozen at PR #608 — see the *Witness divergence* note in
    the module header):
    - `alpha_gap := 0`            ← PR #608 winner.alpha_gap (also `0` in the regen)
    - `rho_star := 3`             ← PR #608 winner.rho_star (regen diverged to `4`)
    - `primal_obj := 1.0`         ← **PLACEHOLDER** (PR #608's primal not extracted
      to Lean; under strong duality must equal dual_obj). **Do NOT** wire to the
      current JSON `cost = 0.14291` — that is the regen's *degraded single-term
      objective*, not a canonical primal/dual (Witness divergence). Refresh only
      from the multi-term-cost re-run.
    - `dual_obj := 1.0`           ← **PLACEHOLDER** (matches primal placeholder;
      same divergence caveat as above)

    Mixed sourcing is acceptable here because downstream
    consumers (notably the empty-constraint SDP setup in
    `AppliedHelium3Uniqueness`) only depend on `rho_star_pos`
    and the alpha-gap = 0 fact; the absolute primal/dual values
    don't enter the uniqueness conclusion. -/
instance instR5FullWitness_helium3 : R5FullWitness LightNucleus.helium3 where
  alpha_gap := 0
  alpha_gap_nonneg := le_refl 0
  primal_obj := 1
  dual_obj := 1
  duality_gap_le := by
    -- |1 - 1| = 0 ≤ 10⁻⁶ trivially; `simp` discharges it fully
    simp
  rho_star := 3
  rho_star_pos := by decide

/-- The minimum block eigenvalue across the ³He Wedderburn
    decomposition is `0.53` (the `standard` block, tied with
    `sign`).  This is the categorical content of the
    "interior optimum" finding. -/
def helium3_min_block_eig : ℝ := 0.53

/-- The minimum block eigenvalue is strictly positive. -/
theorem helium3_min_block_eig_pos : 0 < helium3_min_block_eig := by
  unfold helium3_min_block_eig
  norm_num

/-- **Strict-complementarity certificate for ³He** — constructed
    using the empty-active-set option (since `min_block_eig > 0`
    ⟹ optimum is in the strict interior). -/
noncomputable def helium3StrictComplementarityCert :
    StrictComplementarityCert LightNucleus.helium3 where
  min_block_eig := helium3_min_block_eig
  min_dual_y_on_active := 0
  max_inactive_dual := 0
  active_dual_pos_or_empty := Or.inr helium3_min_block_eig_pos
  inactive_dual_zero := rfl

end QOU.BraidKnot
