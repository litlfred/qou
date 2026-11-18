/-
  # The two coefficients of `thm:wedderburn-mass-formula` are not independent

  The published formula reads

      m(Z,N) = Z·m_p + N·m_n + Z·m_e + α·( Φ₁ − 2[3]_q·Φ₂ + h_A²·Φ₃ )

  with `h_A = q − q⁻¹`, the Hecke–Skein parameter of AGENTS.md §7a.  The two
  non-unit coefficients therefore look like independent inputs: one a q-integer,
  one a square.  **They are not.**  Because

      (q − q⁻¹)² = q² + q⁻² − 2 = [3]_q − 3,

  the third coefficient is an affine function of the second, so the formula has
  **one** q-integer degree of freedom in its correction term, not two.

  ## Why this is worth stating

  The recovered witness `atom-mass-complete-wedderburn` (added 2026-04-10 in
  `1359fe23ac`, recovered 2026-08-25) records the pair

      beta2 = −6.087415        beta3 = 0.0499

  and `"fitted": 0` beside them.  `beta2` matches `−2[3]_q` at the substrate
  modulus to 4.2 × 10⁻⁷.  `beta3_of_beta2` below then *forces* the third
  coefficient to `−beta2/2 − 3 = 0.0437073`; the recorded `0.0499` is 14.2 %
  away.  So the two recorded numbers are **mutually inconsistent as a pair**,
  independently of which one anyone prefers — a stronger statement than
  "they disagree with the published `h_A²`", and one that needs no appeal to
  the substrate value of `q` at all.

  Measured counterpart, with the pre-declared candidate set showing `0.0499` is
  not reachable from the Wedderburn weights its producer's comment claims:
  `computations/wedderburn_beta3_provenance_probe.py`.

  Base ring: a generic `Field R` (§7c).  Nothing here is archimedean — no
  ordering, no `Real.sqrt`, no substrate value of `q` is used or needed.

  -- Ref: [leitner2026] AGENTS.md §7a (Hecke–Skein convention)
  -- Ref: [leitner2026] docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md
-/

import QOU.MathlibExt.QIntegerCanonical

namespace QOU.Mass.WedderburnMassFormulaCoefficients

open QOU.QInteger

variable {R : Type*} [Field R]

/-- **The third balanced q-integer, in closed form**: `[3]_q = q² + 1 + q⁻²`. -/
theorem qIntBal_three_eq (q : R) (hq : q ≠ 0) (hqq : q - q⁻¹ ≠ 0) :
    qIntBal q 3 = q ^ 2 + 1 + (q⁻¹) ^ 2 := by
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [qIntBal_def, div_eq_iff hqq]
  linear_combination (q - q⁻¹) * hinv

/-- **The identity.** The Hecke–Skein parameter squared is the third balanced
q-integer, shifted by `3`:  `h_A² = [3]_q − 3`.

Needs `q ≠ q⁻¹` only because `qIntBal` divides by `q − q⁻¹`; at `q = ±1` the
quantum integer degenerates and the statement is vacuous rather than false. -/
theorem haSq_eq_qIntBal_three_sub_three (q : R) (hq : q ≠ 0) (hqq : q - q⁻¹ ≠ 0) :
    (q - q⁻¹) ^ 2 = qIntBal q 3 - 3 := by
  have hinv : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  rw [qIntBal_three_eq q hq hqq]
  linear_combination (-2 : R) * hinv

/-- **The dependency.** Given the published shapes `β₂ = −2[3]_q` and
`β₃ = h_A²`, the two coefficients satisfy one linear relation with **no `q` in
it at all**:

    2·β₃ + β₂ + 6 = 0        (equivalently `β₃ = −β₂/2 − 3` wherever `2` is a unit)

So the correction term carries **one** q-integer degree of freedom, not two.
Stated multiplicatively to stay valid in every characteristic — dividing by `2`
would need `(2 : R) ≠ 0`, a hypothesis the content does not require.

Falsifiable, and it is exactly what the recorded pair `(β₂, β₃) =
(−6.087415, 0.0499)` violates: it evaluates to `2(0.0499) − 6.087415 + 6 =
+0.012385`, not `0`.  The same `β₂` forces `β₃ = 0.0437073`. -/
theorem beta3_of_beta2 (q b₂ b₃ : R) (hq : q ≠ 0) (hqq : q - q⁻¹ ≠ 0)
    (h₂ : b₂ = -2 * qIntBal q 3) (h₃ : b₃ = (q - q⁻¹) ^ 2) :
    2 * b₃ + b₂ + 6 = 0 := by
  subst h₂
  subst h₃
  rw [haSq_eq_qIntBal_three_sub_three q hq hqq]
  ring

/-- **The contrapositive, as the audit actually uses it.** A recorded pair
failing `2·β₃ + β₂ + 6 = 0` cannot be the published formula's two coefficients —
for **any** `q`.  This is what makes the finding independent of which pin, which
convention, and which rounding produced the recorded numbers. -/
theorem coeffs_inconsistent_of_ne (q b₂ b₃ : R) (hq : q ≠ 0) (hqq : q - q⁻¹ ≠ 0)
    (hne : 2 * b₃ + b₂ + 6 ≠ 0) :
    ¬ (b₂ = -2 * qIntBal q 3 ∧ b₃ = (q - q⁻¹) ^ 2) := by
  rintro ⟨h₂, h₃⟩
  exact hne (beta3_of_beta2 q b₂ b₃ hq hqq h₂ h₃)

/-- Subtracting the Laurent expansion from the third balanced quotient cancels to zero (`qou-dld9`). -/
theorem qIntBal_three_sub_eq_zero (q : R) (hq : q ≠ 0) (hqq : q - q⁻¹ ≠ 0) :
    qIntBal q 3 - (q ^ 2 + 1 + (q⁻¹) ^ 2) = 0 := by
  rw [qIntBal_three_eq q hq hqq, sub_self]

end QOU.Mass.WedderburnMassFormulaCoefficients
