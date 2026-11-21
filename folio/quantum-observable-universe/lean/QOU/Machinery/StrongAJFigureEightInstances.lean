import QOU.Machinery.StrongAJFigureEight

/-!
# `TransferLemmas` is unsatisfiable over any nontrivial coefficient ring

**What is proved (sorry-free).** `not_transferLemmas`: for every nontrivial
coefficient ring `A`, every left ideal `I` of the quantum torus
`QuantumTorus A = A⟨L^±⟩` and every `Aop`, the class
`QOU.Machinery.StrongAJFigureEight.TransferLemmas I Aop` has **no** instance.

**Why.** `L` is a unit of the torus (`Lgen_mul_Linv`). If `Aop ≠ 0` lies in
the left ideal `I`, then `L⁻¹ · Aop` also lies in `I`, is nonzero, and has
`topDeg` one less than `Aop` — so the `minimality` field (every element of `I`
of smaller `topDeg` is `0`) fails. If `Aop = 0`, the `division` field fails at
`P = 1`, since no remainder can have `topDeg < topDeg 0 = ⊥`.

**Consequence.** `strong_aj_figure_eight_of_transfer` is a theorem with an
uninhabitable hypothesis, so it is vacuous as stated. The defect is in the
`minimality` field: on a Laurent ring in `L`, `topDeg` is not a well-founded
measure of "order" on a left ideal (multiplying by `L⁻¹` lowers it forever).
Nguyen–Tran's minimality is about the *L-order* (the length
`topDeg − bottomDeg` of the L-support), or equivalently about the ideal of the
non-localized ring `A⟨L⟩`. Restating the field that way is a refactor of the
source class and needs owner approval; it is NOT done here.

**What is not proved.** Nothing about the strong AJ conjecture for `4₁`
itself; only that this encoding of its transfer inputs cannot be instantiated.

-- Ref: [leitner2026] QOU.Machinery.StrongAJFigureEight; [nguyen-tran-2021]
-- Theorem 1 and Lemmas 2.1–2.2 (the order there is the L-length, not topDeg).
-/

noncomputable section

namespace QOU.Machinery.StrongAJFigureEight.Instances

open QOU.Machinery.QuantumTorus SkewMonoidAlgebra

variable {A : Type*} [CommRing A] [MulSemiringAction Ldeg A]

/-- The torus over a nontrivial ring is nontrivial: `1 ≠ 0`. -/
theorem torus_one_ne_zero [Nontrivial A] : (1 : QuantumTorus A) ≠ 0 := by
  intro h
  apply Lgen_ne_zero (A := A)
  rw [← mul_one (Lgen : QuantumTorus A), h, mul_zero]

/-- Left multiplication by `L⁻¹` shifts coefficients: the `L^n` coefficient of
`L⁻¹ · f` is `σ⁻¹` of the `L^{n+1}` coefficient of `f`. -/
theorem coeffAt_Linv_mul (f : QuantumTorus A) (n : ℤ) :
    coeffAt (Linv * f) n
      = (Multiplicative.ofAdd (-1 : ℤ)) • coeffAt f (n + 1) := by
  have hidx : (Multiplicative.ofAdd (-1 : ℤ))⁻¹ * Multiplicative.ofAdd n
      = Multiplicative.ofAdd (n + 1) := by
    rw [← ofAdd_neg, ← ofAdd_add]; congr 1; ring
  rw [Linv, coeffAt, coeff_single_mul, hidx, one_mul]
  rfl

/-- `L⁻¹ · f` has strictly smaller top L-degree than a nonzero `f`. -/
theorem topDeg_Linv_mul_lt (f : QuantumTorus A) (hf : f ≠ 0) :
    topDeg (Linv * f) < topDeg f := by
  have hfb : topDeg f ≠ ⊥ := fun hb => hf ((topDeg_eq_bot_iff f).mp hb)
  obtain ⟨d, hd⟩ := WithBot.ne_bot_iff_exists.mp hfb
  rw [← hd]
  apply topDeg_lt_of_forall_ge_eq_zero
  intro n hn
  rw [coeffAt_Linv_mul]
  have h0 : coeffAt f (n + 1) = 0 :=
    coeffAt_eq_zero_of_topDeg_lt f (by rw [← hd]; exact_mod_cast (by omega : d < n + 1))
  rw [h0, smul_zero]

/-- `L⁻¹ · f ≠ 0` whenever `f ≠ 0` (`L` is a unit). -/
theorem Linv_mul_ne_zero (f : QuantumTorus A) (hf : f ≠ 0) : Linv * f ≠ 0 := by
  intro h
  apply hf
  rw [← one_mul f, ← Lgen_mul_Linv (A := A), mul_assoc, h, mul_zero]

/-- **`TransferLemmas` has no instance over a nontrivial coefficient ring.** -/
theorem not_transferLemmas [Nontrivial A] (I : Ideal (QuantumTorus A))
    (Aop : QuantumTorus A) : ¬ TransferLemmas I Aop := by
  intro h
  by_cases h0 : Aop = 0
  · obtain ⟨q, r, hqr, hr⟩ := h.division 1
    rw [h0, mul_zero, zero_add] at hqr
    rcases hr with hr | hr
    · exact torus_one_ne_zero (hqr.trans hr)
    · rw [h0, topDeg_zero] at hr
      exact not_lt_bot hr
  · have hmem : Linv * Aop ∈ I := I.mul_mem_left Linv h.aj_mem
    exact Linv_mul_ne_zero Aop h0
      (h.minimality _ hmem (topDeg_Linv_mul_lt Aop h0))

/-- Hence the conditional strong-AJ theorem is vacuous: its class hypothesis
can never be supplied when `A` is nontrivial. -/
theorem transferLemmas_isEmpty [Nontrivial A] (I : Ideal (QuantumTorus A))
    (Aop : QuantumTorus A) : IsEmpty (TransferLemmas I Aop) :=
  ⟨not_transferLemmas I Aop⟩

end QOU.Machinery.StrongAJFigureEight.Instances
