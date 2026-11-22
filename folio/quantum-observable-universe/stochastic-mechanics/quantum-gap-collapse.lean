import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Analysis.SpecialFunctions.Log.Basic

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

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. The
    algebraic indeterminate lives here; the analytic degenerations
    below are stated after the archimedean specialisation `ι : R_q → ℝ`,
    `q ↦ q₀`, since `nhdsWithin`/`atTop`/ordering require an ordered
    topological field (§7c: archimedean constructs ⇒ `ℝ`). -/
abbrev R_q := LaurentPolynomial ℤ
def q_param : R_q := LaurentPolynomial.T 1
def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-- The Planck constant as a plain real function: ℏ(q) = 1 - q⁻¹.
    Archimedean specialisation of the formal `1 - q⁻¹` to real `q`. -/
noncomputable def planck (q : ℝ) : ℝ := 1 - q⁻¹

/-- The Reeb period as a plain real function: Ω(q) = (1 - q⁻¹)⁻¹. -/
noncomputable def reebPeriod (q : ℝ) : ℝ := (planck q)⁻¹

/-- ℏ(1) = 0. -/
@[simp] theorem planck_one : planck 1 = 0 := by
  simp [planck, inv_one]

/-- For q > 1, ℏ(q) > 0. -/
theorem planck_pos {q : ℝ} (hq : 1 < q) : 0 < planck q := by
  simp only [planck]
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-- For q > 1, ℏ(q) ≠ 0. -/
theorem planck_ne_zero {q : ℝ} (hq : 1 < q) : planck q ≠ 0 :=
  ne_of_gt (planck_pos hq)

/-- **Quantum gap collapse (part 1)**: ℏ_q → 0 as q → 1⁺.

    Since ℏ(q) = 1 - q⁻¹ is continuous and ℏ(1) = 0, this follows
    from continuity of subtraction and inversion at q = 1 ≠ 0. -/
-- Ref: [leitner2026] Chapter 8, Section 5
theorem planck_tendsto_zero :
    Tendsto planck (nhdsWithin 1 (Set.Ioi 1)) (nhds 0) := by
  rw [← planck_one]
  exact (Tendsto.const_sub _
    (continuousAt_inv₀ (by norm_num : (1:ℝ) ≠ 0))).mono_left nhdsWithin_le_nhds

/-- **Quantum gap collapse (part 2)**: |Ω_q| → ∞ as q → 1⁺.

    Since Ω(q) = ℏ(q)⁻¹ and ℏ(q) → 0⁺ from the right,
    the Reeb period diverges. -/
-- Ref: [leitner2026] Chapter 8, Section 5
theorem reeb_period_tendsto_atTop :
    Tendsto (fun q => |reebPeriod q|)
      (nhdsWithin 1 (Set.Ioi 1)) atTop := by
  -- planck q → 0⁺ as q → 1⁺ (planck_tendsto_zero), and planck q > 0
  -- for q > 1 (planck_pos). The inverse of a positive function tending
  -- to 0⁺ tends to +∞; the absolute value then also tends to +∞.
  -- Ref: [leitner2026] Chapter 8, Section 5
  have hgt : Tendsto planck (nhdsWithin 1 (Set.Ioi 1)) (𝓝[>] 0) := by
    apply tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _
      planck_tendsto_zero
    filter_upwards [self_mem_nhdsWithin] with q hq
    exact planck_pos hq
  have h : Tendsto reebPeriod (nhdsWithin 1 (Set.Ioi 1)) atTop :=
    hgt.inv_tendsto_nhdsGT_zero
  exact tendsto_abs_atTop_atTop.comp h

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

end

end QOU.AlgebraicSubstrate
