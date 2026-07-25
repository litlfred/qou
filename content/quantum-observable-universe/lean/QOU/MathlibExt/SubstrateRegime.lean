import QOU.MathlibExt.QIntegerFactorial
import Mathlib.Analysis.SpecialFunctions.Sqrt

/-!
# QOU.MathlibExt.SubstrateRegime — the golden-ratio substrate window `1 < q < φ`

The physical substrate parameter satisfies `1 < q₀ ≈ 1.10998 < φ`, where
`φ = (1 + √5)/2 = 2·cos(π/5)` is the golden ratio — the root of
`q² - q - 1`.  Per the corpus, `q = φ` is exactly where the substrate
deformation *resonates with the S₅ symmetry of Bring's surface* (the
`ζ = e^{2πi/5}` action on the Lagrange resolvents; the same icosahedral
`A₅` geometry that fixes the genus-4 / `χ(A) = -6` obstruction).  So the
window `1 < q < φ` is the "stable colour structure" regime: above the
classical point `q = 1`, below the golden resonance.

This file records the regime and shows it lands inside Wenzl genericity
(`QGeneric`): being `> 1` already forces genericity at every rank, so
the whole Hecke-semisimplicity machinery applies throughout the
substrate window.
-/

namespace QOU.MathlibExt

open Real

/-- The **golden ratio** `φ = (1 + √5)/2`, root of `q² - q - 1`. -/
noncomputable def goldenRatio : ℝ := (1 + Real.sqrt 5) / 2

/-- `φ² = φ + 1` (sorry-free). -/
theorem goldenRatio_sq : goldenRatio ^ 2 = goldenRatio + 1 := by
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  unfold goldenRatio
  field_simp
  nlinarith [h5]

/-- `1 < φ` (sorry-free). -/
theorem one_lt_goldenRatio : 1 < goldenRatio := by
  have h5 : (1 : ℝ) < Real.sqrt 5 := by
    have : Real.sqrt 1 < Real.sqrt 5 := Real.sqrt_lt_sqrt (by norm_num) (by norm_num)
    simpa using this
  unfold goldenRatio; linarith

/-- **The substrate regime**: `1 < q < φ`.  Above the classical point,
    below the golden-ratio `S₅`/Bring resonance. -/
def SubstrateRegime (q : ℝ) : Prop := 1 < q ∧ q < goldenRatio

theorem substrateRegime_one_lt {q : ℝ} (h : SubstrateRegime q) : 1 < q := h.1

/-- **The substrate window lies inside Wenzl genericity (sorry-free).**
    Any `q` with `1 < q < φ` — in particular the physical `q₀ ≈ 1.10998`
    — is Wenzl-generic at every rank, so `H_n(q)` semisimplicity applies
    throughout the regime. -/
theorem qGeneric_of_substrateRegime {q : ℝ} (h : SubstrateRegime q) (n : ℕ) :
    QGeneric q n :=
  qGeneric_of_one_lt h.1 n

/-- **The quantum factorial is nonzero throughout the substrate window
    (sorry-free).** -/
theorem qFactorial_ne_zero_of_substrateRegime {q : ℝ} (h : SubstrateRegime q)
    (n : ℕ) : qFactorial q n ≠ 0 :=
  qFactorial_ne_zero_of_one_lt h.1 n

end QOU.MathlibExt
