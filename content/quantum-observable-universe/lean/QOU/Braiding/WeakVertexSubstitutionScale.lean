import QOU.Braiding.WeakVertexT35TraceClosedForm

/-!
# The `s² → |W|²` substitution is not a small correction

`prf:hadron-half-life` (item 1) and `rem:hadron-half-life-fermi` (open
computation 2) prescribe replacing the single-crossing coupling
`s² = (q^{1/2} − q^{-1/2})² = (q − 1)²/q` in the decay rate by the full
weak-vertex form factor `|W(q)|²`, with
`W(q) = tr_M((σ₀σ₁)⁵) = q²(q¹² + q⁸ − 1)/(q² + 1)²`
(`WeakVertexT35TraceClosedForm`). The rate scales by `|W|²/s⁴` under that
substitution, so the half-lives scale by `s⁴/|W|²`.

This file records, as a checked inequality at the proton pin
`q₀ ≈ 1.1099785`, that the factor exceeds `10⁴` — the substitution shortens
every predicted half-life by four orders of magnitude. It therefore cannot
be the `10–17 %` correction the corpus attributed to it. This is a
scope-(a) negative about the *prescribed substitution*, not about `W`: the
closed form is correct, the coupling it was to replace is a different
normalisation. Bean `qou-ix74`.

Ground ring `ℝ` (archimedean evaluation at `q₀`); the identities are stated
over a field. Verified `lean`-direct.
-/

namespace QOU.Braiding.WeakVertexT35

variable {K : Type*} [Field K]

/-- The single-crossing coupling `s² = (q^{1/2} − q^{-1/2})² = q + q⁻¹ − 2 = (q − 1)²/q`,
written without the square root. -/
noncomputable def sSq (q : K) : K := (q - 1) ^ 2 / q

/-- `s² = q + q⁻¹ − 2`: the square-root form and the rational form agree. -/
theorem sSq_eq (q : K) (hq : q ≠ 0) : sSq q = q + q⁻¹ - 2 := by
  unfold sSq
  field_simp
  ring

/-- The rate-scaling factor of the prescribed substitution, `|W|²/s⁴`, as a rational
function of `q`. -/
noncomputable def substitutionRateFactor (q : K) : K :=
  (weakVertexTrace q) ^ 2 / (sSq q) ^ 2

/-- Closed form of the factor: `q⁶ (q¹² + q⁸ − 1)² / ((q² + 1)⁴ (q − 1)⁴)`. -/
theorem substitutionRateFactor_eq (q : K) (hq0 : q ≠ 0) (hq1 : q ≠ 1) (h2 : q ^ 2 + 1 ≠ 0) :
    substitutionRateFactor q =
      q ^ 6 * (q ^ 12 + q ^ 8 - 1) ^ 2 / ((q ^ 2 + 1) ^ 4 * (q - 1) ^ 4) := by
  unfold substitutionRateFactor weakVertexTrace sSq
  have hq1' : q - 1 ≠ 0 := sub_ne_zero.mpr hq1
  field_simp

/-- **The negative, checked at the proton pin.** At `q₀ = 1.1099785` the factor exceeds
`10⁴`: the substitution multiplies every decay rate by more than ten thousand, so it
shortens every predicted half-life by more than four orders of magnitude. -/
theorem substitutionRateFactor_gt_ten_thousand :
    (10000 : ℝ) < substitutionRateFactor (1.1099785 : ℝ) := by
  rw [substitutionRateFactor_eq _ (by norm_num) (by norm_num) (by positivity)]
  norm_num

/-- And it is below `2·10⁴`: the factor is `≈ 1.19·10⁴`, not merely large. -/
theorem substitutionRateFactor_lt_twenty_thousand :
    substitutionRateFactor (1.1099785 : ℝ) < (20000 : ℝ) := by
  rw [substitutionRateFactor_eq _ (by norm_num) (by norm_num) (by positivity)]
  norm_num

end QOU.Braiding.WeakVertexT35
