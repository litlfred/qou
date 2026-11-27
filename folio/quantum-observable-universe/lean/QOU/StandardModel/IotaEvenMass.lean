import QOU.StandardModel.ChargeConjugationTrace

/-!
# `ι` transposes Young diagrams; the `ι`-even part flips sign under `C` on odd words

* `tauIota_eq_tau_transpose`: on `H₃(q)`, `ι : σᵢ ↦ −σᵢ⁻¹` acts on the three block
  characters by the transpose `λ ↦ λ'`: it swaps `χ₍₃₎` and `χ₍₁³₎` and fixes
  `χ₍₂,₁₎`. So "odd under `ι`" means "antisymmetric under transposing the Young diagram".
* `iotaEven_flip`: an `ι`-even block functional (equal weights on `(3)` and `(1³)`)
  satisfies `E(Cw) = (−1)^{|w|} E(w)` under crossing reversal `C`. On an odd-length word,
  such as the electron `σ₀σ₁σ₀`, the `ι`-even part of `tr_M` changes sign under `C`.
-/

namespace QOU.AlphaEM.IotaEven

open QOU.AlphaEM.IotaOdd QOU.AlphaEM.ChargeConj

variable {K : Type*} [Field K]

/-- **`ι` is the transpose on block weights.** -/
theorem tauIota_eq_tau_transpose (q a c b : K) (hq : q ≠ 0)
    (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0) (w : List Letter) :
    tauIota q a c b w = tau q b c a w := by
  simp only [tauIota, tau, trace_iota_hook q hq h3]; ring

/-- **The `ι`-even part flips sign under `C` on odd-length words.** -/
theorem iotaEven_flip (q a c : K) (hq : q ≠ 0) (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0)
    (w : List Letter) :
    tau q a c a (w.map flip) = (-1) ^ w.length * tau q a c a w := by
  have e := tauIota_eq_sign_tau_flip q a c a w
  rw [tauIota_eq_tau_transpose q a c a hq h3] at e
  rw [e, ← mul_assoc, ← pow_add, ← two_mul, pow_mul]; simp

/-- The electron word `σ₀σ₁σ₀` has odd length: its `ι`-even part is `C`-odd. -/
theorem electron_iotaEven_flip (q a c : K) (hq : q ≠ 0)
    (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0) :
    tau q a c a ([(0, true), (1, true), (0, true)].map flip) =
      -tau q a c a [(0, true), (1, true), (0, true)] := by
  rw [iotaEven_flip q a c hq h3]; simp; ring

end QOU.AlphaEM.IotaEven

