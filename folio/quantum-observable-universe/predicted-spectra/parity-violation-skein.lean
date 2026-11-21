import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp


/-!
# QOU.Archimedean.parity_violation_skein — Parity non-conservation from q ≠ 1

The Skein relation q[L₊] - q⁻¹[L₋] = (q^½ - q^⁻½)[L₀] is invariant
under parity (L₊ ↔ L₋) if and only if q = 1.  For any q ≠ 1, the weak
interaction violates parity.

LaTeX label: `prop:parity-violation-skein`

## References
- [leitner2026] §6/parity-violation-skein
- Lee, Yang (1956): Question of parity conservation in weak interactions
- Wu et al. (1957): Experimental test of parity conservation in beta decay

**Ground ring**: `ℝ` (archimedean realisation). The parity-invariance
claim uses the strict order `0 < q` and the field inverse `1 / q`
(`q⁻¹`), so it lives past the substrate→archimedean wall (§7c) and is
stated over `ℝ` at the evaluation `q ↦ q₀`. The categorical
`R_q = ℤ[q, q⁻¹]` layer is the pre-evaluation home of the coefficients;
the order/field statements here are facts about their `ℝ`-evaluation.
-/

namespace QOU.Archimedean

/- The Skein parity statements below are genuinely archimedean: they use
   division (`1 / q`, `q⁻¹`) and the strict order (`0 < q`, `1 < q`), so
   they live past the substrate→archimedean wall and are stated over `ℝ`
   (per §7c). The categorical `R_q = ℤ[q, q⁻¹]` Laurent layer is the
   pre-evaluation home of the *coefficients*; the parity-invariance claim
   itself is an order/field fact about the evaluation `q ↦ q₀ ∈ ℝ`. -/

/-- The Skein relation coefficients for L₊ and L₋.
    Parity exchanges these: (q, q⁻¹) ↔ (q⁻¹, q).
    The relation is parity-invariant iff q = q⁻¹, i.e., q = 1. -/
-- Ref: [leitner2026] §6/parity-violation-skein
structure SkeinCoefficients where
  /-- The deformation parameter (archimedean evaluation `q₀ ∈ ℝ`). -/
  q : ℝ
  /-- The parameter is positive. -/
  q_pos : 0 < q
  /-- Coefficient of [L₊]. -/
  coeff_plus : ℝ := q
  /-- Coefficient of [L₋]. -/
  coeff_minus : ℝ := 1 / q

/-- Parity invariance means the coefficients are equal. -/
-- Ref: [leitner2026] §6/parity-violation-skein
def SkeinCoefficients.parityInvariant (s : SkeinCoefficients) : Prop :=
  s.coeff_plus = s.coeff_minus

/-- The Skein relation is parity-invariant if and only if q = 1. -/
-- Ref: [leitner2026] §6/parity-violation-skein
theorem parity_violation_skein (q : ℝ) (hq : 0 < q) :
    ({ q := q, q_pos := hq } : SkeinCoefficients).parityInvariant ↔ q = 1 := by
  unfold SkeinCoefficients.parityInvariant SkeinCoefficients.coeff_plus SkeinCoefficients.coeff_minus
  simp only
  constructor
  · intro h
    have hqq : q * q = 1 := by
      field_simp at h
      nlinarith
    nlinarith [sq_nonneg (q - 1)]
  · intro h
    subst h
    norm_num

/-- At q = 1.1097, the parity violation parameter q - q⁻¹ ≈ 0.209. -/
-- Ref: [leitner2026] §6/parity-violation-skein
noncomputable def parityViolationStrength (q : ℝ) : ℝ := q - 1 / q

/-- The parity violation strength is positive for q > 1. -/
-- Ref: [leitner2026] §6/parity-violation-skein
theorem parityViolationStrength_pos {q : ℝ} (hq : 1 < q) :
    0 < parityViolationStrength q := by
  unfold parityViolationStrength
  rw [sub_pos, div_lt_iff₀ (by linarith : (0 : ℝ) < q)]
  nlinarith

/-- The parity violation strength vanishes at q = 1. -/
-- Ref: [leitner2026] §6/parity-violation-skein
theorem parityViolationStrength_classical :
    parityViolationStrength 1 = 0 := by
  unfold parityViolationStrength
  norm_num

/-- CP is conserved: the q ↔ q⁻¹ involution IS a symmetry.
    Under CP: coeff_plus ↔ coeff_minus AND L₊ ↔ L₋,
    The Skein relation maps to itself. -/
-- Ref: [leitner2026] §6/parity-violation-skein
theorem cp_conservation (q : ℝ) (hq : 0 < q) :
    let s : SkeinCoefficients := { q := q, q_pos := hq }
    let s_cp : SkeinCoefficients := { q := 1/q, q_pos := by positivity }
    s.coeff_plus = s_cp.coeff_minus ∧ s.coeff_minus = s_cp.coeff_plus := by
  show q = 1 / (1 / q) ∧ 1 / q = 1 / q
  exact ⟨(one_div_one_div q).symm, rfl⟩

end QOU.Archimedean
