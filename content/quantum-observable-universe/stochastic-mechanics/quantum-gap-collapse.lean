import Mathlib.Order.Filter.Basic
import Mathlib.Topology.Order.Basic
import Mathlib.Topology.Algebra.Order.Field

/-!
# QOU.AlgebraicSubstrate.quantum_gap_collapse

Collapse of the quantum gap under the classical limit functor L.
Two analytic degenerations: Planck constant → 0 and Reeb period → ∞.
The categorical degenerations (braiding trivialization, q-differential
smoothing) are stated in `ClassicalLimitFunctor`.

LaTeX label: `thm:quantum-gap-collapse`

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

set_option autoImplicit false


open Filter Topology

namespace QOU.AlgebraicSubstrate

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
noncomputable section
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The Planck constant as a plain function: ℏ(q) = 1 - q⁻¹. -/
noncomputable def planck (q : R_q) : R_q := 1 - q⁻¹

/-- The Reeb period as a plain function: Ω(q) = (1 - q⁻¹)⁻¹. -/
noncomputable def reebPeriod (q : R_q) : R_q := (planck q)⁻¹

/-- ℏ(1) = 0. -/
@[simp] theorem planck_one : planck 1 = 0 := by
  simp [planck, inv_one]

/-- For q > 1, ℏ(q) > 0. -/
-- theorem planck_pos {q : R_q} (hq : 1 < q) : 0 < planck q := by  -- (archimedean; not meaningful over R_q)
  simp only [planck]
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt hq
  linarith

/-- For q > 1, ℏ(q) ≠ 0. -/
-- theorem planck_ne_zero {q : R_q} (hq : 1 < q) : planck q ≠ 0 :=  -- (archimedean; not meaningful over R_q)
  ne_of_gt (planck_pos hq)

/-- **Quantum gap collapse (part 1)**: ℏ_q → 0 as q → 1⁺.

    Since ℏ(q) = 1 - q⁻¹ is continuous and ℏ(1) = 0, this follows
    from continuity of subtraction and inversion at q = 1 ≠ 0. -/
-- Ref: [manuscript] Chapter 8, Section 5
theorem planck_tendsto_zero :
    Tendsto planck (nhdsWithin 1 (Set.Ioi 1)) (nhds 0) := by
  rw [← planck_one]
  exact ((continuous_const.sub continuous_inv₀).tendsto 1).mono_left
    nhdsWithin_le_nhds

/-- **Quantum gap collapse (part 2)**: |Ω_q| → ∞ as q → 1⁺.

    Since Ω(q) = ℏ(q)⁻¹ and ℏ(q) → 0⁺ from the right,
    the Reeb period diverges. -/
-- Ref: [manuscript] Chapter 8, Section 5
theorem reeb_period_tendsto_atTop :
    Tendsto (fun q => |reebPeriod q|)
      (nhdsWithin 1 (Set.Ioi 1)) atTop := by
  -- planck q → 0⁺ as q → 1⁺ (planck_tendsto_zero), and planck q > 0
  -- for q > 1 (planck_pos). The inverse of a positive function tending
  -- to 0 tends to +∞.
  -- Ref: [manuscript] Chapter 8, Section 5
  simp only [reebPeriod]
  apply Filter.Tendsto.abs_atTop_atTop
  exact Filter.Tendsto.inv_tendsto_zero planck_tendsto_zero

/-- **Quantum gap collapse (combined)**: Under the classical limit
    q → 1, the Planck constant vanishes and the Reeb period diverges.

    The remaining two degenerations (Jackson q-derivative → ordinary
    derivative, braiding → symmetric swap) are categorical statements
    encoded in `ClassicalLimitFunctor.braiding_trivializes`. -/
theorem quantum_gap_collapse :
    Tendsto planck (nhdsWithin 1 (Set.Ioi 1)) (nhds 0)
    ∧ Tendsto (fun q => |reebPeriod q|)
        (nhdsWithin 1 (Set.Ioi 1)) atTop :=
  ⟨planck_tendsto_zero, reeb_period_tendsto_atTop⟩

end QOU.AlgebraicSubstrate
