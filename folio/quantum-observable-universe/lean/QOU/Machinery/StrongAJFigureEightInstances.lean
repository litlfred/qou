import QOU.Machinery.StrongAJFigureEight

/-!
# `TransferLemmas`: why the `topDeg` form was unsatisfiable, and the L-length form

**History.** Until 2026-11-21 the `minimality` field read "every element of `I`
of smaller `topDeg` than `Â` is `0`". On the Laurent ring `A⟨L^±⟩` that is
unsatisfiable: `L` is a unit, so `L⁻¹ · Â ∈ I`, it is nonzero, and its `topDeg`
is one less. The class was restated in L-length (owner "Fix", bean `qou-c8p8`).

**What is proved (sorry-free).**
* `topDeg_minimality_forces_zero` — over a nontrivial ring, if `Aop ∈ I` and
  every element of `I` of smaller `topDeg` vanishes, then `Aop = 0`. So the old
  `minimality` field could hold only at `Â = 0`, where the old `division` field
  fails. This is the defect, kept as a plain lemma.
* `transferLemmas_top` — the restated class is consistent: `I = ⊤`, `Â = 1` is
  an instance. This is a consistency witness only. It says nothing about the
  recurrence ideal of `4₁`.

**What is not proved.** Strong AJ for `4₁`; an instance at the AJ operator.

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

/-- **The old `topDeg` minimality forces `Â = 0`** over a nontrivial ring. -/
theorem topDeg_minimality_forces_zero [Nontrivial A] (I : Ideal (QuantumTorus A))
    (Aop : QuantumTorus A) (hmem : Aop ∈ I)
    (hmin : ∀ r ∈ I, topDeg r < topDeg Aop → r = 0) : Aop = 0 := by
  by_contra h0
  exact Linv_mul_ne_zero Aop h0
    (hmin _ (I.mul_mem_left Linv hmem) (topDeg_Linv_mul_lt Aop h0))

/-- **The restated class is consistent**: `I = ⊤`, `Â = 1`. -/
theorem transferLemmas_top [Nontrivial A] :
    TransferLemmas (⊤ : Ideal (QuantumTorus A)) 1 where
  aj_mem := Submodule.mem_top
  division P := ⟨P, 0, by rw [mul_one, add_zero], Or.inl rfl⟩
  minimality _ _ _ := by rw [lLength_one]; exact Nat.zero_le _

end QOU.Machinery.StrongAJFigureEight.Instances
