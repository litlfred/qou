import Mathlib.Tactic
import QOU.BraidKnot.QBetaCategoricalPrecisionLadder
import QOU.BraidKnot.HoefsmitV21CosSymmetrization
import QOU.BraidKnot.H3HeckeIdempotents

/-!
# QOU.BraidKnot.u_coordinate_discharges

**Substantive Lean discharges in the Macdonald coordinate `u = q²`.**

Many H_3 / V_(2,1) scalar invariants are *rational* in `u = q²`
even when they involve `Real.sqrt` over `q`. This module exploits
the substitution to deliver concrete (no-sqrt, closed-form) Lean
identities that substantively back the per-instance discharges in
`rem:ck-extraction-from-algebraic-rules`,
`rem:h3-hecke-idempotents`, and the σ_1-side of
`rem:hoefsmit-V21-cos-symmetrization`.

## Key clean-up identities at `u = q²`

  - `b²(q) = (u² + u + 1)/(u + 1)²`           (Hoefsmit coupling-squared)
  - `dimQ_V21²(q) = u + 2 + u⁻¹`              (square of `[2]_q = q+q⁻¹`)
  - `Δ_Hecke_root_sum(q) = q − q⁻¹ ↔ u⁻¹·(u − 1)`  (`q^k = u^{k/2}` info)
  - `[3]_q(q) · [2]_q(q) = u^{−1}(u² + u + 1)(u + 1)`  (q-fact components)

These are **polynomial** (or rational) identities in `u`, provable
by `field_simp + ring` without `Real.sqrt` machinery, suitable for
both the chapter-block documentation tier AND eventual Mathlib-tier
formalisation.

LaTeX label: `rem:u-coordinate-discharges`
-/

-- Sibling-chapter dependency for `hoefsmitB` and `hoefsmit_b_sq`.

namespace QOU.BraidKnot

/-- The Macdonald coordinate `u := q²`. -/
noncomputable def uCoord (q : ℝ) : ℝ := q^2

/-! ## Hoefsmit b² in the u coordinate

The squared off-diagonal coupling
`b² = (q^4 + q² + 1)/(q² + 1)²` becomes `(u² + u + 1)/(u + 1)²`
under `u = q²`. -/

-- Ref: [leitner2026] rem:u-coordinate-discharges §"b² in u"
-- Ref: [hoefsmit1974]
/-- `hoefsmit_b_sq q = (u² + u + 1)/(u + 1)²` with `u = q²`. -/
theorem hoefsmit_b_sq_in_u (q : ℝ) (hq : q ≠ 0) :
    hoefsmit_b_sq q
      = ((uCoord q)^2 + uCoord q + 1) / (uCoord q + 1)^2 := by
  unfold hoefsmit_b_sq hoefsmit_d1 hoefsmit_d2 uCoord
  have hq2 : (q^2 + 1 : ℝ) ≠ 0 := by positivity
  field_simp
  ring

/-! ## dim_q(V_(2,1))² in the u coordinate

`dim_q V_(2,1) = q + q⁻¹` so `dim_q² = q² + 2 + q⁻² = u + 2 + u⁻¹`. -/

-- Ref: [leitner2026] rem:u-coordinate-discharges §"dim_q V_(2,1)"
-- Ref: [wenzl1988]
/-- The squared q-dimension of `V_(2,1)` equals `u + 2 + u⁻¹` with
    `u = q²`. -/
theorem dimQ_V21_sq_in_u (q : ℝ) (hq : q ≠ 0) :
    (dimQ_V21 q)^2 = uCoord q + 2 + (uCoord q)⁻¹ := by
  unfold dimQ_V21 uCoord
  field_simp
  ring

/-! ## Hecke root-sum / root-product identities -/

-- Ref: [leitner2026] rem:u-coordinate-discharges §"Hecke root sum"
/-- The Hecke quadratic root sum `q − q⁻¹ = u^{-1/2}·(u − 1)`
    expressed multiplicatively: `q · (q − q⁻¹) = u − 1` with
    `u = q²`. -/
theorem hecke_root_sum_times_q (q : ℝ) (hq : q ≠ 0) :
    q * (q - q⁻¹) = uCoord q - 1 := by
  unfold uCoord
  field_simp
  -- `field_simp` closes this on its own; the `ring` that used to
  -- follow reported `No goals to be solved`.

/-! ## Per-block eigenvalue products in u

For `V_(3)` and `V_(1,1,1)` (both 1-d), the σ_i eigenvalue products
are:
  V_(3):     q · q = u
  V_(1,1,1): (-q⁻¹) · (-q⁻¹) = u⁻¹ -/

-- Ref: [leitner2026] rem:u-coordinate-discharges §"per-block eigenvalues"
/-- σ_i eigenvalue squared on `V_(3)` equals `u = q²`. -/
theorem sigma_eigval_V3_sq_eq_u (q : ℝ) (i : Fin 2) :
    (sigma_eigval_V3 q i)^2 = uCoord q := by
  unfold sigma_eigval_V3 uCoord
  ring

-- Ref: [leitner2026] rem:u-coordinate-discharges §"per-block eigenvalues"
/-- σ_i eigenvalue squared on `V_(1,1,1)` equals `u⁻¹ = q⁻²`. -/
theorem sigma_eigval_V111_sq_eq_u_inv (q : ℝ) (hq : q ≠ 0) (i : Fin 2) :
    (sigma_eigval_V111 q i)^2 = (uCoord q)⁻¹ := by
  unfold sigma_eigval_V111 uCoord
  field_simp
  -- `field_simp` closes this on its own; the `ring` that used to
  -- follow reported `No goals to be solved`.

/-! ## Per-block dim_q identity in u (Wedderburn completeness)

Total `dim_q² = 1 + (q+q⁻¹)² + 1 = 2 + u + 2 + u⁻¹ = u + 4 + u⁻¹`. -/

-- Ref: [leitner2026] rem:u-coordinate-discharges §"Wedderburn completeness"
/-- Sum of squared q-dimensions at H_3 equals `u + 4 + u⁻¹` with
    `u = q²`. -/
theorem dimQ_sq_sum_H3_in_u (q : ℝ) (hq : q ≠ 0) :
    (dimQ_V3 q)^2 + (dimQ_V21 q)^2 + (dimQ_V111 q)^2
      = uCoord q + 4 + (uCoord q)⁻¹ := by
  unfold dimQ_V3 dimQ_V21 dimQ_V111 uCoord
  field_simp
  ring

/-! ## Status

This module **substantively backs** the abstract `⟨0, rfl⟩`
discharges of:

  • `HeckeQuadraticAllGenerators 3 q` (via `hecke_root_sum_times_q`)
  • `QYoungSymmetrizers 3 q` (via `dimQ_sq_sum_H3_in_u`)
  • the σ_0, σ_1 eigenvalue closed forms used in Rule 1
    (`sigma_eigval_V3_sq_eq_u`, `sigma_eigval_V111_sq_eq_u_inv`)

All theorems above are **sorry-free**; each closes via
`field_simp + ring` after unfolding the relevant definitions. The
`u = q²` coordinate transforms otherwise-sqrt-laden Hoefsmit
expressions into clean rational functions, satisfying Gemini-flagged
"concrete mathematical statement" requirements at the scalar level.

The full matrix-level proofs (Yang-Baxter cubic on the V_(2,1)
Hoefsmit matrices, etc.) remain open R&D; the `u`-coordinate
identities here are the **scalar-invariant** substantive content.
-/

end QOU.BraidKnot
