import Mathlib.Analysis.SpecialFunctions.Pow.Real


/-!
# QOU.Archimedean.parity_violation_skein — Parity non-conservation from q ≠ 1

The Skein relation q[L₊] - q⁻¹[L₋] = (q^½ - q^⁻½)[L₀] is invariant
under parity (L₊ ↔ L₋) if and only if q = 1.  For any q ≠ 1, the weak
interaction violates parity.

LaTeX label: `prop:parity-violation-skein`

## References
- [manuscript] §6/parity-violation-skein
- Lee, Yang (1956): Question of parity conservation in weak interactions
- Wu et al. (1957): Experimental test of parity conservation in beta decay

**Ground ring.** This is the **archimedean realisation** (namespace
`QOU.Archimedean`): the parity claims are order statements (`0 < q`,
`1 < q`, `q = 1`) and use the reciprocal `1/q`, none of which live on
the formal ground ring `R_q = ℤ[q, q⁻¹]`. They hold over `ℝ` at the
substrate image `ι : R_q → ℝ, q ↦ q₀` (§7c).
-/

namespace QOU.Archimedean

/-- The Skein relation coefficients for L₊ and L₋.
    Parity exchanges these: (q, q⁻¹) ↔ (q⁻¹, q).
    The relation is parity-invariant iff q = q⁻¹, i.e., q = 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
structure SkeinCoefficients where
  /-- Substrate parameter (archimedean image of the formal `q`). -/
  q : ℝ
  /-- Coefficient of [L₊]. -/
  coeff_plus : ℝ := q
  /-- Coefficient of [L₋]. -/
  coeff_minus : ℝ := 1 / q

/-- Parity invariance means the coefficients are equal. -/
-- Ref: [manuscript] §6/parity-violation-skein
def SkeinCoefficients.parityInvariant (s : SkeinCoefficients) : Prop :=
  s.coeff_plus = s.coeff_minus

/-- The Skein relation is parity-invariant if and only if q = 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
theorem parity_violation_skein (q : ℝ) (hq : 0 < q) :
    ({ q := q } : SkeinCoefficients).parityInvariant ↔ q = 1 := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  unfold SkeinCoefficients.parityInvariant
  show q = 1 / q ↔ q = 1
  rw [eq_div_iff hq0]
  constructor
  · intro h
    have h1 : q ≤ 1 := by nlinarith [sq_nonneg (q - 1)]
    have h2 : (1 : ℝ) ≤ q := by nlinarith [h, hq]
    exact le_antisymm h1 h2
  · intro h; subst h; norm_num

/-- At q = 1.1097, the parity violation parameter q - q⁻¹ ≈ 0.209. -/
-- Ref: [manuscript] §6/parity-violation-skein
noncomputable def parityViolationStrength (q : ℝ) : ℝ := q - 1 / q

/-- The parity violation strength is positive for q > 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
theorem parityViolationStrength_pos {q : ℝ} (hq : 1 < q) :
    0 < parityViolationStrength q := by
  have hq0 : 0 < q := by linarith
  unfold parityViolationStrength
  rw [sub_pos, div_lt_iff₀ hq0]
  nlinarith

/-- The parity violation strength vanishes at q = 1. -/
-- Ref: [manuscript] §6/parity-violation-skein
theorem parityViolationStrength_classical :
    parityViolationStrength 1 = 0 := by
  unfold parityViolationStrength
  norm_num

/-- CP is conserved: the q ↔ q⁻¹ involution IS a symmetry.
    Under CP: coeff_plus ↔ coeff_minus AND L₊ ↔ L₋,
    the Skein relation maps to itself. -/
-- Ref: [manuscript] §6/parity-violation-skein
theorem cp_conservation (q : ℝ) (hq : 0 < q) :
    ({ q := q } : SkeinCoefficients).coeff_plus
        = ({ q := 1 / q } : SkeinCoefficients).coeff_minus
      ∧ ({ q := q } : SkeinCoefficients).coeff_minus
        = ({ q := 1 / q } : SkeinCoefficients).coeff_plus := by
  have hq0 : q ≠ 0 := ne_of_gt hq
  refine ⟨?_, ?_⟩
  · show q = 1 / (1 / q)
    rw [one_div_one_div]
  · show 1 / q = 1 / q
    rfl

end QOU.Archimedean
