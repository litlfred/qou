import QOU.StandardModel.IotaOddTrace

/-!
# `ι` is charge conjugation times the writhe-parity sign

The corpus takes charge conjugation to be crossing reversal, `C : σᵢ ↦ σᵢ⁻¹`
(`knot-notation-convention`, `c-equals-bar-iff-all-1dim`). The α_em functional
`τ = χ_(3) − χ_(1³)` is odd under `ι : σᵢ ↦ −σᵢ⁻¹` (`IotaOddTrace.iota_odd_iff`).
This file relates the two and fixes the sign.

* `tauIota_eq_sign_tau_flip`: `ι = (−1)^{length} · C` on block functionals. So `τ`
  satisfies `τ(Cw) = −(−1)^{|w|} τ(w)`: `C`-even on words of odd length (odd
  writhe), `C`-odd on words of even length.
* `C_odd_iff`: the only block functional that is `C`-odd on every word is zero.
  So `C` alone cannot select the α_em functional; the writhe-parity sign is needed.
* `tau_iota_split` and `iotaOdd_coeff_pos`: under convention D the `ι`-odd part of
  the Markov trace is `(y₃/2)·τ` with `y₃/2 > 0` for real `q`. Once α_em is read as
  the `ι`-odd part of `tr_M`, its sign is fixed by the trace; it is not a choice.

What this does not show: why α_em should be the `ι`-odd part at all.
-/

namespace QOU.AlphaEM.ChargeConj

open QOU.AlphaEM.IotaOdd Matrix

variable {K : Type*} [Field K]

/-- Crossing reversal on a letter. -/
def flip : Letter → Letter
  | (i, b) => (i, !b)

theorem symLetter_flip (q : K) (l : Letter) : altLetter q l = -symLetter q (flip l) := by
  obtain ⟨i, b⟩ := l; cases b <;> simp [altLetter, symLetter, flip]

theorem altLetter_flip (q : K) (l : Letter) : symLetter q l = -altLetter q (flip l) := by
  obtain ⟨i, b⟩ := l; cases b <;> simp [altLetter, symLetter, flip]

theorem hookLetter_flip (q : K) (l : Letter) : iotaHook q l = -hookLetter q (flip l) := by
  obtain ⟨i, b⟩ := l; cases b <;> simp [iotaHook, hookLetter, flip]

/-- Product of negated scalar factors. -/
theorem prod_map_neg (f g : Letter → K) (h : ∀ l, f l = -g l) (w : List Letter) :
    (w.map f).prod = (-1) ^ w.length * (w.map g).prod := by
  induction w with
  | nil => simp
  | cons l w ih =>
    simp only [List.map_cons, List.prod_cons, List.length_cons, ih, h l, pow_succ]
    ring

/-- Product of negated matrix factors. -/
theorem prod_map_neg_mat (f g : Letter → Matrix (Fin 2) (Fin 2) K) (h : ∀ l, f l = -g l)
    (w : List Letter) : (w.map f).prod = ((-1 : K) ^ w.length) • (w.map g).prod := by
  induction w with
  | nil => simp
  | cons l w ih =>
    simp only [List.map_cons, List.prod_cons, List.length_cons, ih, h l]
    simp [pow_succ, neg_smul, neg_mul, mul_comm]

/-- **`ι` is `C` times the sign `(−1)^{length}`.** -/
theorem tauIota_eq_sign_tau_flip (q w3 w21 w111 : K) (w : List Letter) :
    tauIota q w3 w21 w111 w = (-1) ^ w.length * tau q w3 w21 w111 (w.map flip) := by
  have hs : altWord q w = (-1) ^ w.length * symWord q (w.map flip) := by
    simpa [altWord, symWord, List.map_map] using
      prod_map_neg (altLetter q) (symLetter q ∘ flip) (symLetter_flip q) w
  have ha : symWord q w = (-1) ^ w.length * altWord q (w.map flip) := by
    simpa [altWord, symWord, List.map_map] using
      prod_map_neg (symLetter q) (altLetter q ∘ flip) (altLetter_flip q) w
  have hh : iotaHookWord q w = ((-1 : K) ^ w.length) • hookWord q (w.map flip) := by
    simpa [iotaHookWord, hookWord, List.map_map] using
      prod_map_neg_mat (iotaHook q) (hookLetter q ∘ flip) (hookLetter_flip q) w
  simp only [tauIota, tau, hs, ha, hh, Matrix.trace_smul, smul_eq_mul]
  ring

/-- **No nonzero block functional is `C`-odd on every word.** -/
theorem C_odd_iff [CharZero K] (q w3 w21 w111 : K) (hq : q ≠ 0)
    (h1 : q + q⁻¹ ≠ 0) (h3 : q ^ 2 + 1 + (q ^ 2)⁻¹ ≠ 0) :
    (∀ w, tau q w3 w21 w111 (w.map flip) = -tau q w3 w21 w111 w) ↔
      (w3 = 0 ∧ w21 = 0 ∧ w111 = 0) := by
  constructor
  · intro h
    have e0 := h []
    have e1 := h [(0, true)]
    have e2 := h [(0, true), (1, false)]
    simp [tau, symWord, altWord, hookWord, hookLetter, symLetter, altLetter, flip,
      hookGen, hookGenInv, Matrix.trace_fin_two,
      mul_inv_cancel₀ hq, inv_mul_cancel₀ hq] at e0 e1 e2
    have h2 : (2 : K) ≠ 0 := two_ne_zero
    have hA : w3 + w111 + 2 * w21 = 0 := by
      apply mul_left_cancel₀ h2; linear_combination e0
    have hB : (w3 - w111) * (q + q⁻¹) = 0 := by linear_combination e1
    have hab : w3 = w111 := sub_eq_zero.1 ((mul_eq_zero.1 hB).resolve_right h1)
    have hC : w21 * (q ^ 2 + 1 + (q ^ 2)⁻¹) = 0 := by
      linear_combination (-1 / 2 : K) * e2 + hA
    have h21 : w21 = 0 := (mul_eq_zero.1 hC).resolve_right h3
    have h3' : w3 = 0 := by
      apply mul_left_cancel₀ h2; linear_combination hA - 2 * h21 + hab
    exact ⟨h3', h21, by rw [← hab, h3']⟩
  · rintro ⟨rfl, rfl, rfl⟩ w; simp [tau]

/-- **The `ι` split of a block functional.** Any weights `(a, c, b)` decompose as
an `ι`-odd part `((a − b)/2)·τ` plus an `ι`-even remainder. -/
theorem tau_iota_split [CharZero K] (q a c b : K) (w : List Letter) :
    tau q a c b w = ((a - b) / 2) * tau q 1 0 (-1) w + tau q ((a + b) / 2) c ((a + b) / 2) w := by
  simp only [tau]; field_simp; ring

/-- **Sign of the `ι`-odd part of the convention-D trace.** With
`y₃ = (q⁴+1)/(q²+1)²` and `y₁₁₁ = 0`, the coefficient `(y₃ − y₁₁₁)/2` of `τ` is
positive for every real `q` (indeed in any ordered field). -/
theorem iotaOdd_coeff_pos {L : Type*} [Field L] [LinearOrder L] [IsStrictOrderedRing L]
    (q : L) : 0 < ((q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 - 0) / 2 := by
  have : 0 < q ^ 4 + 1 := by positivity
  have : 0 < (q ^ 2 + 1) ^ 2 := by positivity
  rw [sub_zero]; positivity

end QOU.AlphaEM.ChargeConj
