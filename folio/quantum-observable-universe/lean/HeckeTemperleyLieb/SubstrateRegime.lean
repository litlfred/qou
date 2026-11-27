import HeckeTemperleyLieb.QIntegerFactorial
import Mathlib.Tactic

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


/-- The golden ratio as a ring symbol: any `φ > 0` with `φ² = φ + 1` exceeds `1`.
The `Real.sqrt 5` form `(1 + √5)/2` is in
`QOU.Transcendental.HeckeTemperleyLieb.SubstrateRegimeReal` (bean `qou-dk7p`). -/
theorem one_lt_of_sq_eq_add_one {φ : ℝ} (hφ : 0 < φ) (h : φ ^ 2 = φ + 1) : 1 < φ := by
  nlinarith

/-- The substrate window `1 < q < φ`, for `φ` the golden-ratio symbol. -/
def SubstrateRegime (φ q : ℝ) : Prop := 1 < q ∧ q < φ

theorem substrateRegime_one_lt {φ q : ℝ} (h : SubstrateRegime φ q) : 1 < q := h.1

/-- **The substrate window lies inside Wenzl genericity (sorry-free).**
    Any `q` with `1 < q < φ` — in particular the physical `q₀ ≈ 1.10998`
    — is Wenzl-generic at every rank, so `H_n(q)` semisimplicity applies
    throughout the regime. -/
theorem qGeneric_of_substrateRegime {φ q : ℝ} (h : SubstrateRegime φ q) (n : ℕ) :
    QGeneric q n :=
  qGeneric_of_one_lt h.1 n

/-- **The quantum factorial is nonzero throughout the substrate window
    (sorry-free).** -/
theorem qFactorial_ne_zero_of_substrateRegime {φ q : ℝ} (h : SubstrateRegime φ q)
    (n : ℕ) : qFactorial q n ≠ 0 :=
  qFactorial_ne_zero_of_one_lt h.1 n

end QOU.MathlibExt
