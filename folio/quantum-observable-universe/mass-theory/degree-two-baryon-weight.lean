import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.MathlibExt.QIntegerCanonical


/-!
# Degree-2 Baryon Weight β₂ = -2[3]_q

The coefficient of Φ₂ in the mass formula comes from the
quantum 3-integer, encoding the 3-quark baryon structure.

-- Ref: [leitner2026] prop:degree-two-baryon-weight
-/

namespace QOU.BaryonWeight

/-- Quantum n-integer [n]_q = (q^n - q^{-n}) / (q - q^{-1}). -/
-- Consolidated onto the canonical q-integer (bean `qou-qint`): this was a
-- verbatim duplicate of `QOU.QInteger.qIntBal`.  Kept as a local `abbrev` so
-- every call site and proof below is unchanged, while the DEFINITION now has a
-- single home.  See QOU/MathlibExt/QIntegerCanonical.lean.
noncomputable abbrev qInt (q : ℝ) (n : ℕ) : ℝ := QOU.QInteger.qIntBal q n

/-- At q₀ = 1.10998: [3]_q ≈ 3.044. -/
theorem qInt3_approx :
    abs (qInt 1.10998 3 - 3.044) < 0.001 := by
  unfold qInt
  rw [abs_lt]
  norm_num

/-- β₂ = -2[3]_q arises from the baryon quantum number:
    3 color channels produce C(3,2) = 3 pairwise products,
    q-deformed to [3]_q. Factor -2 from pn doubling and
    alternating channel sign. -/
noncomputable def beta2 (q : ℝ) : ℝ := -2 * qInt q 3

/-- At q₀: β₂ ≈ -6.087. -/
theorem beta2_approx :
    abs (beta2 1.10998 - (-6.087)) < 0.01 := by
  unfold beta2 qInt
  rw [abs_lt]
  norm_num

end QOU.BaryonWeight
