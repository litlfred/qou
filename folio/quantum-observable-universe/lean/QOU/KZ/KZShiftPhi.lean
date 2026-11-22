import QOU.KZ.KZShift
import QOU.KZ.KZPentagon

/-!
# Shift invariance for the normalised KZ associator `KZPentagon.Φ`

`Φ(A, B + z) = Φ(A, B)` and `Φ(A + z, B) = Φ(A, B)` for `z` commuting with `A` and `B`, for the
associator built from the normalised formal solutions (`KZPentagon.Φ`). Stage S2 prerequisite of
bean `qou-zoyv`: it converts the pentagon of `KZPentagon` (with `T₁₂₃`, `T₂₃₄`) into Drinfeld's
coproduct form (with `t₁₃ + t₂₃`, `t₂₄ + t₃₄`). Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2, shift invariance)
-/

namespace QOU.KZ.KZShiftPhi

open QOU.KZ.FuchsianFormal QOU.KZ.FuchsianParam QOU.KZ.AssociatorKZ QOU.KZ.KZShift
  QOU.KZ.KZPentagon

variable {R : Type*} [NormedRing R] [NormedAlgebra ℂ R] [CompleteSpace R]

omit [CompleteSpace R] in
/-- `0` is non-resonant. -/
theorem nonResonant_zero : NonResonant (0 : R) := by
  refine nonResonant_of_aeval (K := ℂ) (0 : R) Polynomial.X ?_ fun k hk => ?_
  · ext X; simp [adL_apply, ad]
  · simp only [Polynomial.eval_X]; exact_mod_cast hk.ne'

omit [CompleteSpace R] in
theorem nonResonant_kzM0_zero (z : R) : NonResonant (kzM0 (0 : R) z 0) := nonResonant_zero

/-- The binomial coefficients of `(1 − t)^z`. -/
noncomputable def binom (z : R) : ℕ → R := formalSol (kzM0 0 z) (nonResonant_kzM0_zero z)

theorem phiKZ_congr {A B : R} {H₀ H₀' H₁ H₁' : ℕ → R} (e₀ : H₀ = H₀') (e₁ : H₁ = H₁')
    (h₀ : H₀ 0 = 1) (hH₀ : IsFormalGauge (kzM0 A B) H₀) (h₁ : H₁ 0 = 1)
    (hH₁ : IsFormalGauge (kzM0 B A) H₁) (h₀' : H₀' 0 = 1) (hH₀' : IsFormalGauge (kzM0 A B) H₀')
    (h₁' : H₁' 0 = 1) (hH₁' : IsFormalGauge (kzM0 B A) H₁') :
    phiKZ A B H₀ H₁ h₀ hH₀ h₁ hH₁ = phiKZ A B H₀' H₁' h₀' hH₀' h₁' hH₁' := by
  subst e₀ e₁; rfl

/-- **`Φ(A, B + z) = Φ(A, B)`** for `z` commuting with `A` and `B`. -/
theorem Φ_shift_right (A B z : R) (hA : NonResonant A) (hB : NonResonant B)
    (hBz : NonResonant (B + z)) (hzA : Commute z A) (hzB : Commute z B) :
    Φ A (B + z) hA hBz = Φ A B hA hB := by
  have hz₀ : ∀ k, Commute z (H0 A B hA k) := commute_H0 hA hzA hzB
  have hz₁ : ∀ k, Commute z (H0 B A hB k) := commute_H0 hB hzB hzA
  have hEA : ∀ k, Commute (binom z k) A := fun k =>
    (commute_formalSol _ _ A (fun j => by
      rcases j with _ | j
      · exact Commute.zero_right A
      · exact (hzA.symm).neg_right) k).symm
  have hE0 : binom z 0 = 1 := formalSol_zero _ _
  have hE : IsFormalGauge (kzM0 0 z) (binom z) := formalSol_isFormalGauge _ _
  have e₀ : H0 A (B + z) hA = conv (H0 A B hA) (binom z) :=
    formalGauge_unique _ _ _ (fun k hk => (hA k hk).1) (H0_zero _ _ hA)
      (conv_zero _ _ (H0_zero _ _ hA) hE0) (H0_gauge _ _ hA)
      (isFormalGauge_conv A B z _ _ (H0_gauge _ _ hA) hE hz₀ hEA)
  have e₁ : H0 (B + z) A hBz = H0 B A hB :=
    formalGauge_unique _ _ _ (fun k hk => (hBz k hk).1) (H0_zero _ _ hBz) (H0_zero _ _ hB)
      (H0_gauge _ _ hBz) (isFormalGauge_kzM0_add_left A B z _ hz₁ (H0_gauge _ _ hB))
  unfold Φ
  rw [phiKZ_congr e₀ e₁]
  exact phiKZ_shift_right A B z _ _ _ _ _ _ _ hE0 hE hzA hzB hz₀ hz₁ hEA

/-- Inversion for `Φ`: `Φ(B, A) Φ(A, B) = 1 = Φ(A, B) Φ(B, A)`. -/
theorem Φ_swap_mul (A B : R) (hA : NonResonant A) (hB : NonResonant B) :
    Φ B A hB hA * Φ A B hA hB = 1 ∧ Φ A B hA hB * Φ B A hB hA = 1 :=
  phiKZ_swap_mul A B _ _ _ _ _ _

/-- **`Φ(A + z, B) = Φ(A, B)`** for `z` commuting with `A` and `B`. -/
theorem Φ_shift_left (A B z : R) (hA : NonResonant A) (hB : NonResonant B)
    (hAz : NonResonant (A + z)) (hzA : Commute z A) (hzB : Commute z B) :
    Φ (A + z) B hAz hB = Φ A B hA hB := by
  have h := Φ_shift_right B A z hB hA hAz hzB hzA
  have i1 := (Φ_swap_mul (A + z) B hAz hB).2
  have i2 := (Φ_swap_mul A B hA hB).1
  rw [h] at i1
  calc _ = Φ (A + z) B hAz hB * (Φ B A hB hA * Φ A B hA hB) := by rw [i2, mul_one]
    _ = _ := by rw [← mul_assoc, i1, one_mul]

/-- **`Φ(0, B) = 1`** (the unitor compatibility of the associator). -/
theorem Φ_zero_left (B : R) (h0 : NonResonant (0 : R)) (hB : NonResonant B) :
    Φ 0 B h0 hB = 1 := by
  have e₁ : H0 B 0 hB = delta0 :=
    formalGauge_unique _ _ _ (fun k hk => (hB k hk).1) (H0_zero _ _ hB) (by simp [delta0])
      (H0_gauge _ _ hB) (isFormalGauge_delta0 B)
  obtain ⟨-, hΦ⟩ := phiKZ_spec (0 : R) B (H0 0 B h0) (H0 B 0 hB) (H0_zero _ _ h0)
    (H0_gauge _ _ h0) (H0_zero _ _ hB) (H0_gauge _ _ hB)
  have ht : (1 / 2 : ℝ) ∈ Set.Ioo (0 : ℝ) 1 := ⟨by norm_num, by norm_num⟩
  have h := hΦ (1 / 2) ht
  have hbin := series_eq_tpow_one_sub B (H0 0 B h0) (H0_zero _ _ h0) (H0_gauge _ _ h0) ht
  have hG₁ : G₁ B (H0 B 0 hB) (1 / 2) = FuchsianAnalytic.tpow B (1 - 1 / 2) := by
    rw [G₁, e₁, series_delta0, one_mul]
  have hG₀ : G₀ 0 (H0 0 B h0) (1 / 2) = FuchsianAnalytic.tpow B (1 - 1 / 2) := by
    rw [G₀, tpow_zero, mul_one, hbin]
  rw [hG₀, hG₁] at h
  have hu := isUnit_tpow B (1 - 1 / 2)
  exact (hu.mul_left_cancel ((mul_one _).trans h)).symm

/-- **`Φ(A, 0) = 1`.** -/
theorem Φ_zero_right (A : R) (hA : NonResonant A) (h0 : NonResonant (0 : R)) :
    Φ A 0 hA h0 = 1 := by
  have := (Φ_swap_mul A 0 hA h0).1
  rwa [Φ_zero_left A h0 hA, one_mul] at this

theorem Φ_congr {A A' B B' : R} (eA : A = A') (eB : B = B') (hA : NonResonant A)
    (hB : NonResonant B) (hA' : NonResonant A') (hB' : NonResonant B') :
    Φ A B hA hB = Φ A' B' hA' hB' := by
  subst eA eB; rfl

open QOU.KZ.KZ4 in
/-- **The pentagon in Drinfeld's coproduct form.** For four-point residues satisfying the
infinitesimal braid relations, with the relevant residues non-resonant,
`Φ^{234} Φ^{1,23,4} Φ^{123} = Φ^{1,2,34} Φ^{12,3,4}`, where
`Φ^{123} = Φ(t₁₂, t₂₃)`, `Φ^{234} = Φ(t₂₃, t₃₄)`, `Φ^{1,23,4} = Φ(t₁₂ + t₁₃, t₂₄ + t₃₄)`,
`Φ^{1,2,34} = Φ(t₁₂, t₂₃ + t₂₄)`, `Φ^{12,3,4} = Φ(t₁₃ + t₂₃, t₃₄)`. -/
theorem pentagon_drinfeld (t : Res R) (h : t.Rel) (h12 : NonResonant t.t12)
    (h23 : NonResonant t.t23) (h34 : NonResonant t.t34) (h123 : NonResonant t.T123)
    (h234 : NonResonant t.T234) (h1213 : NonResonant (t.t12 + t.t13))
    (h2434 : NonResonant (t.t24 + t.t34)) (h2324 : NonResonant (t.t23 + t.t24))
    (h1323 : NonResonant (t.t13 + t.t23)) :
    Φ t.t23 t.t34 h23 h34 * Φ (t.t12 + t.t13) (t.t24 + t.t34) h1213 h2434 *
        Φ t.t12 t.t23 h12 h23 =
      Φ t.t12 (t.t23 + t.t24) h12 h2324 * Φ (t.t13 + t.t23) t.t34 h1323 h34 := by
  have P := pentagon t h h12 h123 h23 h234 h34
  -- commutation facts
  have c34 : Commute t.t34 (t.t23 + t.t24) := by
    have := h.c4.symm
    have e : t.t23 + t.t24 = t.T234 - t.t34 := by simp only [Res.T234]; abel
    rw [e]; exact this.sub_right (Commute.refl _)
  have c34_12 : Commute t.t34 t.t12 := h.r1.symm
  have c23_1213 : Commute t.t23 (t.t12 + t.t13) := h.r4
  have c23_234 : Commute t.t23 t.T234 := h.c3
  have c23_2434 : Commute t.t23 (t.t24 + t.t34) := h.r5
  have c12_34 : Commute t.t12 t.t34 := h.r1
  have c12_1323 : Commute t.t12 (t.t13 + t.t23) := h.r3
  -- the three shifts
  have s1 : Φ t.T234 t.t12 h234 h12 = Φ (t.t23 + t.t24) t.t12 h2324 h12 := by
    have := Φ_shift_left (t.t23 + t.t24) t.t12 t.t34 h2324 h12 h234 c34 c34_12
    exact this
  have s2 : Φ t.T123 t.T234 h123 h234 = Φ (t.t12 + t.t13) (t.t24 + t.t34) h1213 h2434 := by
    have e : t.T234 = (t.t24 + t.t34) + t.t23 := by simp only [Res.T234]; abel
    have h234' : NonResonant ((t.t24 + t.t34) + t.t23) := e ▸ h234
    calc Φ t.T123 t.T234 h123 h234 = Φ (t.t12 + t.t13) t.T234 h1213 h234 :=
          Φ_shift_left (t.t12 + t.t13) t.T234 t.t23 h1213 h234 h123 c23_1213 c23_234
      _ = Φ (t.t12 + t.t13) ((t.t24 + t.t34) + t.t23) h1213 h234' :=
          Φ_congr rfl e h1213 h234 h1213 h234'
      _ = _ := Φ_shift_right (t.t12 + t.t13) (t.t24 + t.t34) t.t23 h1213 h2434 h234' c23_1213
          c23_2434
  have s3 : Φ t.t34 t.T123 h34 h123 = Φ t.t34 (t.t13 + t.t23) h34 h1323 := by
    have e : t.T123 = (t.t13 + t.t23) + t.t12 := by simp only [Res.T123]; abel
    have h123' : NonResonant ((t.t13 + t.t23) + t.t12) := e ▸ h123
    rw [Φ_congr rfl e h34 h123 h34 h123',
      Φ_shift_right t.t34 (t.t13 + t.t23) t.t12 h34 h1323 h123' c12_34 c12_1323]
  rw [s1, s2, s3] at P
  -- invert the outer factors
  obtain ⟨i1, i1'⟩ := Φ_swap_mul t.t12 (t.t23 + t.t24) h12 h2324
  obtain ⟨i2, i2'⟩ := Φ_swap_mul (t.t13 + t.t23) t.t34 h1323 h34
  set X := Φ t.t12 (t.t23 + t.t24) h12 h2324
  set Xi := Φ (t.t23 + t.t24) t.t12 h2324 h12
  set Y := Φ (t.t13 + t.t23) t.t34 h1323 h34
  set Yi := Φ t.t34 (t.t13 + t.t23) h34 h1323
  set M := Φ t.t23 t.t34 h23 h34 * Φ (t.t12 + t.t13) (t.t24 + t.t34) h1213 h2434 *
    Φ t.t12 t.t23 h12 h23
  have P' : Xi * M * Yi = 1 := by rw [← P]; simp only [M, mul_assoc]
  calc M = (X * Xi) * M * (Yi * Y) := by rw [i1', i2, one_mul, mul_one]
    _ = X * (Xi * M * Yi) * Y := by simp only [mul_assoc]
    _ = X * Y := by rw [P', mul_one]

end QOU.KZ.KZShiftPhi
