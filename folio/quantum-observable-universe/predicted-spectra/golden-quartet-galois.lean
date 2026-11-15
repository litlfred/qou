import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith


/-!
# QOU.Archimedean.golden_quartet_galois — Golden quartet as G-orbit

The four golden values {1/φ, -φ, φ, -1/φ} are the roots of
P(x) = x⁴ − 3x² + 1 = (x² − x − 1)(x² + x − 1) over ℚ. Under the
Galois × bar action they form a single orbit.

LaTeX label: `prop:golden-quartet-galois`

## References

- [leitner2026] §6/golden-quartet-galois
- [leitner2026] §6/golden-skew-dual-node
- [leitner2026] §5/baryon-integration-limit
-/

namespace QOU.Archimedean.GoldenQuartetGalois

/-- φ = (1 + √5)/2. -/
noncomputable def phi : ℝ := (1 + Real.sqrt 5) / 2

/-- 1/φ = (√5 − 1)/2. -/
noncomputable def phiInv : ℝ := (Real.sqrt 5 - 1) / 2

/-- The quartic factorisation P(x) = (x² − x − 1)(x² + x − 1)
    = x⁴ − 3x² + 1. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem quartic_factorisation (x : ℝ) :
    (x ^ 2 - x - 1) * (x ^ 2 + x - 1) = x ^ 4 - 3 * x ^ 2 + 1 := by
  ring

private theorem sqrt5_sq : Real.sqrt 5 ^ 2 = 5 :=
  Real.sq_sqrt (by norm_num : (5 : ℝ) ≥ 0)

/-- φ is a root of x² − x − 1. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem phi_root_pos_sign : phi ^ 2 - phi - 1 = 0 := by
  unfold phi
  field_simp
  nlinarith [sqrt5_sq]

/-- 1/φ is a root of x² + x − 1. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem phiInv_root_neg_sign : phiInv ^ 2 + phiInv - 1 = 0 := by
  unfold phiInv
  field_simp
  nlinarith [sqrt5_sq]

/-- −φ is a root of x² + x − 1 (the same minimal polynomial as 1/φ). -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem neg_phi_root_neg_sign : (-phi) ^ 2 + (-phi) - 1 = 0 := by
  have h := phi_root_pos_sign
  nlinarith [h]

/-- −1/φ is a root of x² − x − 1 (the same minimal polynomial as φ). -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem neg_phiInv_root_pos_sign : (-phiInv) ^ 2 - (-phiInv) - 1 = 0 := by
  have h := phiInv_root_neg_sign
  nlinarith [h]

/-- All four golden quartet values satisfy P(x) = x⁴ − 3x² + 1 = 0. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem phi_quartic : phi ^ 4 - 3 * phi ^ 2 + 1 = 0 := by
  rw [← quartic_factorisation phi]
  have h := phi_root_pos_sign
  -- phi² − phi − 1 = 0 ⇒ (phi² − phi − 1)(phi² + phi − 1) = 0
  have : phi ^ 2 - phi - 1 = 0 := h
  rw [this]
  ring

/-- 1/φ satisfies P(x) = 0. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem phiInv_quartic : phiInv ^ 4 - 3 * phiInv ^ 2 + 1 = 0 := by
  rw [← quartic_factorisation phiInv]
  have : phiInv ^ 2 + phiInv - 1 = 0 := phiInv_root_neg_sign
  -- The factor (x² + x − 1) vanishes at 1/φ.
  have hh : phiInv ^ 2 - phiInv - 1 = -2 * phiInv := by linarith
  rw [hh, this]
  ring

/-- −φ satisfies P(x) = 0. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem neg_phi_quartic : (-phi) ^ 4 - 3 * (-phi) ^ 2 + 1 = 0 := by
  have h := phi_quartic
  -- (−phi)⁴ = phi⁴, (−phi)² = phi².
  nlinarith [h, sq_nonneg phi, sq_nonneg (phi ^ 2)]

/-- −1/φ satisfies P(x) = 0. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem neg_phiInv_quartic : (-phiInv) ^ 4 - 3 * (-phiInv) ^ 2 + 1 = 0 := by
  have h := phiInv_quartic
  nlinarith [h, sq_nonneg phiInv, sq_nonneg (phiInv ^ 2)]

/-- φ · (1/φ) = 1 (bar pairing). -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem phi_mul_phiInv : phi * phiInv = 1 := by
  unfold phi phiInv
  field_simp
  nlinarith [sqrt5_sq]

/-- The Galois conjugate of φ in ℚ(√5)/ℚ is −1/φ.
    Specifically, replacing √5 with −√5 in the formula for φ
    gives −1/φ. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem galois_phi_eq_neg_phiInv :
    (1 + (-Real.sqrt 5)) / 2 = -phiInv := by
  unfold phiInv
  ring

/-- The Galois conjugate of 1/φ in ℚ(√5)/ℚ is −φ. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem galois_phiInv_eq_neg_phi :
    ((-Real.sqrt 5) - 1) / 2 = -phi := by
  unfold phi
  ring

/-- **Golden quartet as Galois × bar orbit** (Proposition):

    The four values {1/φ, −φ, φ, −1/φ} are the complete root set of
    P(x) = x⁴ − 3x² + 1, with Galois action (√5 ↔ −√5) producing the
    sign flips on each minimal polynomial, and bar (x ↔ x⁻¹) exchanging
    the two minimal polynomials.

    The conjunction below records the four roots and the bar pairing. -/
-- Ref: [leitner2026] §6/golden-quartet-galois
theorem golden_quartet_galois :
    phi ^ 4 - 3 * phi ^ 2 + 1 = 0 ∧
    phiInv ^ 4 - 3 * phiInv ^ 2 + 1 = 0 ∧
    (-phi) ^ 4 - 3 * (-phi) ^ 2 + 1 = 0 ∧
    (-phiInv) ^ 4 - 3 * (-phiInv) ^ 2 + 1 = 0 ∧
    phi * phiInv = 1 :=
  ⟨phi_quartic, phiInv_quartic, neg_phi_quartic, neg_phiInv_quartic,
   phi_mul_phiInv⟩

end QOU.Archimedean.GoldenQuartetGalois
