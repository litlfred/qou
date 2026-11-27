/-
Copyright (c) 2026 litlfred. All rights reserved.

# The Hopf-cubic odd carrier of Q_β's c_3

The bar-ODD channel of the Q_β precision-ladder coefficient `c_3` is carried by a
degree-3 field, sourced entirely by the **chiral Hopf-link** (double-crossing)
sector of the `H_3` normal form (`mass-theory/qbeta-odd-carrier-hopf-cubic.md`).
In the bar-even loop-trace variable `y = q² + q⁻² = 2cosh 2λ`, the bar-odd carrier
collapses to `C(y) = y³ − 4y² + 3y − 2`, decomposing over the knot sectors as

    C = C_Hopf + C_unknot,
    C_Hopf(y)   = y³ − 6y² + 10y − 6   (the chiral 2-crossing sector),
    C_unknot(y) = 2y² − 7y + 4          (the trivial sector, quadratic).

This is the odd-channel companion to the amphichiral **even** channel
(`self-dual-higgs-real-volume`: 4₁ amphichiral ⇒ CS = 0 ⇒ 𝔙 real), completing the
parity ↔ chirality dictionary:

  * bar-EVEN (cosh, m_π, CAL-3) ↔ amphichiral 4₁ ↔ CS = 0, 𝔙 real ↔ ℚ(√3).
  * bar-ODD  (sinh, Q_β, CAL-2) ↔ chiral Hopf ↔ negative discriminant, complex
    roots ↔ the degree-3 field (S₃, disc −76, prime 19).

All statements here are exact ring identities (base ring generic per §7c — no
archimedean structure). The "complex roots" fact is recorded as the negative
integer discriminant; the actual root-finding is archimedean and lives in the
companion probe.
-/
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace QOU.QBeta.HopfCubic

variable {R : Type*} [CommRing R]

/-- The chiral Hopf-link (double-crossing) sector's bar-odd cubic. -/
def cHopf (y : R) : R := y ^ 3 - 6 * y ^ 2 + 10 * y - 6

/-- The trivial (unknot) sector's bar-odd quadratic. -/
def cUnknot (y : R) : R := 2 * y ^ 2 - 7 * y + 4

/-- The total bar-odd carrier `C(y) = y³ − 4y² + 3y − 2`. -/
def cTotal (y : R) : R := y ^ 3 - 4 * y ^ 2 + 3 * y - 2

/-- **Sector decomposition** `C = C_Hopf + C_unknot`: the cubic (degree-3 field)
    is sourced by the Hopf sector; the unknot contributes only a quadratic. -/
theorem cTotal_eq_cHopf_add_cUnknot (y : R) :
    cTotal y = cHopf y + cUnknot y := by
  unfold cTotal cHopf cUnknot; ring

/-- **Classical (`q = 1`, `y = 2`) value of the Hopf sector is the `c_3`
    near-match `−2`** = `J_Hopf(q=1)`. At the classical anchor the Hopf sector
    alone reproduces the empirical `c_3 ≈ −2`. -/
theorem cHopf_at_two : cHopf (2 : R) = -2 := by
  unfold cHopf; norm_num

/-- The unknot sector also gives `−2` at `y = 2`, so the total `C(2) = −4`. -/
theorem cUnknot_at_two : cUnknot (2 : R) = -2 := by
  unfold cUnknot; norm_num

/-- **The Hopf cubic has negative discriminant `−76 = −2²·19`.** A depressed real
    cubic with negative discriminant has exactly one real root and a
    complex-conjugate pair — so the odd channel's arithmetic is genuinely
    complex (the chiral realization), not real like the amphichiral even channel.
    The prime `19` is the arithmetic fingerprint shared with the total `C`
    (disc `−152 = −2³·19`). Stated as the exact integer discriminant of
    `y³ − 6y² + 10y − 6` (a = −6, b = 10, c = −6). -/
theorem cHopf_discriminant_eq :
    (18 * (-6) * 10 * (-6) - 4 * (-6) ^ 3 * (-6) + (-6) ^ 2 * 10 ^ 2
      - 4 * 10 ^ 3 - 27 * (-6) ^ 2 : ℤ) = -76 := by
  norm_num

/-- The total carrier's discriminant is `−152 = −2³·19`, sharing the prime-19
    fingerprint (a = −4, b = 3, c = −2). -/
theorem cTotal_discriminant_eq :
    (18 * (-4) * 3 * (-2) - 4 * (-4) ^ 3 * (-2) + (-4) ^ 2 * 3 ^ 2
      - 4 * 3 ^ 3 - 27 * (-2) ^ 2 : ℤ) = -152 := by
  norm_num

/-- Both discriminants are divisible by 19 (the shared fingerprint). -/
theorem prime_19_divides_both_discriminants :
    (19 : ℤ) ∣ (-76) ∧ (19 : ℤ) ∣ (-152) := by
  refine ⟨⟨-4, by norm_num⟩, ⟨-8, by norm_num⟩⟩

end QOU.QBeta.HopfCubic
