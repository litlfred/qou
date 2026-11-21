import QOU.Mass.QuantumSl2BeltTensor

/-!
# The inverse monodromy as a twisted copy of the monodromy at `s⁻¹`

Stage 4d-iii (part) of the derivation of Zheng's tangle formula (van der Veen 2008, Lemma 1).
The mirror clasp uses the inverse crossings, so it needs `M⁻¹`, the inverse of the monodromy
`M = Ř′Ř` on `V_{m+1} ⊗ V_{m+1}`. We show that `M⁻¹` is the monodromy at `s⁻¹`, conjugated by
the factor swap `P` and the diagonal `D = diag(q^{2ab})` on `v_a ⊗ v_b`:

    M(s)⁻¹ = D P M(s⁻¹) P D⁻¹        (`mono_mul_monoBar`, `monoBar_eq_inv`).

The same conjugation sends `Δ_{s⁻¹}(E)` to `q^{−m} Δ_s(E)` and `Δ_{s⁻¹}(F)` to `q^m Δ_s(F)`
(`conjM_deltaE`, `conjM_deltaF`), so it maps highest-weight vectors and `F`-strings at `s⁻¹` to
multiples of those at `s`. On the string through `w_j`, `M(s)` acts by `q^{2n(n+1)−m(m+2)}` and the
conjugated `M(s⁻¹)` by the inverse scalar, so their product is the identity on the string basis.

All statements are over a generic field `𝕜`.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-- `[k]` is invariant under `q ↦ q⁻¹`. -/
theorem qint_inv (q : 𝕜) (k : ℕ) : qint q⁻¹ k = qint q k := by
  unfold qint
  rw [inv_inv, ← neg_sub q⁻¹ q, ← neg_sub (q⁻¹ ^ k) (q ^ k), neg_div_neg_eq]

theorem irrepE_inv (q : 𝕜) (m : ℕ) : irrepE q⁻¹ m = irrepE q m := by
  ext i j; simp [irrepE, qint_inv]

theorem irrepF_inv (q : 𝕜) (m : ℕ) : irrepF q⁻¹ m = irrepF q m := by
  ext i j; simp [irrepF, qint_inv]

section Conj

variable (q : 𝕜) (m : ℕ)

/-- The diagonal weight `q^{2ab}` on `v_a ⊗ v_b`. -/
def dw (x : Fin (m + 1) × Fin (m + 1)) : 𝕜 := q ^ (2 * (x.1 : ℤ) * x.2)

/-- `v ↦ D P v`. -/
def conjV (v : Fin (m + 1) × Fin (m + 1) → 𝕜) : Fin (m + 1) × Fin (m + 1) → 𝕜 :=
  fun x => dw q m x * v x.swap

/-- `Y ↦ D P Y P D⁻¹`. -/
def conjM (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  fun x y => dw q m x / dw q m y * Y x.swap y.swap

variable {q}

theorem dw_ne_zero (hq : q ≠ 0) (x : Fin (m + 1) × Fin (m + 1)) : dw q m x ≠ 0 :=
  zpow_ne_zero _ hq

theorem dw_swap (x : Fin (m + 1) × Fin (m + 1)) : dw q m x.swap = dw q m x := by
  unfold dw; simp only [Prod.fst_swap, Prod.snd_swap]; ring_nf

theorem conjM_mul (hq : q ≠ 0) (A B : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    conjM q m (A * B) = conjM q m A * conjM q m B := by
  ext x y
  simp only [conjM, mul_apply, Finset.mul_sum]
  rw [← (Equiv.prodComm (Fin (m + 1)) (Fin (m + 1))).sum_comp]
  refine Finset.sum_congr rfl fun z _ => ?_
  have h1 := dw_ne_zero m hq z
  have h1' := dw_ne_zero m hq z.swap
  have h2 := dw_ne_zero m hq y
  simp only [Equiv.prodComm_apply]
  field_simp

theorem conjM_one (hq : q ≠ 0) : conjM q m 1 = 1 := by
  ext x y
  simp only [conjM, one_apply]
  by_cases h : x = y
  · subst h; simp [div_self (dw_ne_zero m hq x)]
  · have : x.swap ≠ y.swap := fun h' => h (Prod.swap_injective h')
    simp [h, this]

theorem conjM_pow (hq : q ≠ 0) (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (k : ℕ) : conjM q m (Y ^ k) = conjM q m Y ^ k := by
  induction k with
  | zero => simp [conjM_one m hq]
  | succ k ih => rw [pow_succ, conjM_mul m hq, ih, pow_succ]

theorem conjM_smul (c : 𝕜) (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    conjM q m (c • Y) = c • conjM q m Y := by
  ext x y; simp only [conjM, smul_apply, smul_eq_mul]; ring

theorem conjM_mulVec (hq : q ≠ 0)
    (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (v : Fin (m + 1) × Fin (m + 1) → 𝕜) :
    conjM q m Y *ᵥ conjV q m v = conjV q m (Y *ᵥ v) := by
  funext x
  simp only [mulVec, dotProduct, conjM, conjV, Finset.mul_sum]
  rw [← (Equiv.prodComm (Fin (m + 1)) (Fin (m + 1))).sum_comp]
  refine Finset.sum_congr rfl fun z _ => ?_
  have h1 := dw_ne_zero m hq z
  have h1' := dw_ne_zero m hq z.swap
  simp only [Equiv.prodComm_apply, Prod.swap_swap]
  field_simp

theorem conjV_smul (c : 𝕜) (v : Fin (m + 1) × Fin (m + 1) → 𝕜) :
    conjV q m (c • v) = c • conjV q m v := by
  funext x; simp only [conjV, Pi.smul_apply, smul_eq_mul]; ring

/-- `K` at `q⁻¹` on `v_p` as a power of `q`. -/
theorem kp_inv_eq_zpow (hq : q ≠ 0) {p : ℕ} (hp : p ≤ m) :
    q⁻¹ ^ (m - p) * q⁻¹⁻¹ ^ p = q ^ (-(wt m p)) := by
  rw [kp_eq_zpow q⁻¹ (inv_ne_zero hq) hp, inv_zpow', ]

/-- **`D P Δ_{q⁻¹}(E) P D⁻¹ = q^{−m} Δ_q(E)`.** -/
theorem conjM_deltaE (hq : q ≠ 0) :
    conjM q m (deltaE q⁻¹ m m) = q ^ (-(m : ℤ)) • deltaE q m m := by
  ext ⟨⟨a, ha⟩, ⟨b, hb⟩⟩ ⟨⟨c, hc⟩, ⟨e, he⟩⟩
  simp only [conjM, dw, deltaE, Prod.swap, add_apply, kroneckerMap_apply, irrepE_inv,
    smul_apply, smul_eq_mul, irrepKp, diagonal_apply, one_apply, Fin.mk.injEq]
  rw [kp_inv_eq_zpow m hq (show a ≤ m by omega)]
  simp only [irrepE]
  by_cases h1 : b + 1 = e <;> by_cases h2 : a = c <;> by_cases h3 : a + 1 = c <;>
    by_cases h4 : b = e <;> simp only [h1, h2, h3, h4, if_true, if_false] <;>
    first | omega | (subst_vars; simp)
  · have key : q ^ (2 * (c : ℤ) * b) / q ^ (2 * (c : ℤ) * (b + 1)) * (q ^ wt m c)⁻¹ = (q ^ m)⁻¹ := by
      rw [div_eq_mul_inv, ← zpow_neg, ← zpow_neg, ← zpow_add₀ hq, ← zpow_add₀ hq,
        ← zpow_natCast, ← zpow_neg]
      congr 1; unfold wt; ring
    rw [← key]; ring
  · have key : q ^ (2 * (a : ℤ) * e) / q ^ (2 * ((a : ℤ) + 1) * e)
        = (q ^ m)⁻¹ * (q ^ (m - e) * (q ^ e)⁻¹) := by
      rw [← inv_pow q e, kp_eq_zpow q hq (show e ≤ m by omega), div_eq_mul_inv, ← zpow_neg, ← zpow_add₀ hq,
        ← zpow_natCast, ← zpow_neg, ← zpow_add₀ hq]
      congr 1; unfold wt; ring
    rw [key]; ring


/-- **`D P Δ_{q⁻¹}(F) P D⁻¹ = q^m Δ_q(F)`.** -/
theorem conjM_deltaF (hq : q ≠ 0) :
    conjM q m (deltaF q⁻¹ m m) = q ^ (m : ℤ) • deltaF q m m := by
  ext ⟨⟨a, ha⟩, ⟨b, hb⟩⟩ ⟨⟨c, hc⟩, ⟨e, he⟩⟩
  simp only [conjM, dw, deltaF, Prod.swap, add_apply, kroneckerMap_apply, irrepF_inv,
    smul_apply, smul_eq_mul, irrepKm, diagonal_apply, one_apply, Fin.mk.injEq, inv_inv]
  simp only [irrepF]
  by_cases h1 : b = e + 1 <;> by_cases h2 : a = c <;> by_cases h3 : a = c + 1 <;>
    by_cases h4 : b = e <;> simp only [h1, h2, h3, h4, if_true, if_false] <;>
    first | omega | (subst_vars; simp)
  · have key : q ^ (2 * (c : ℤ) * (e + 1)) / q ^ (2 * (c : ℤ) * e)
        = q ^ m * ((q ^ (m - c))⁻¹ * q ^ c) := by
      rw [← zpow_natCast q (m - c), ← zpow_natCast q c, ← zpow_natCast q m,
        Nat.cast_sub (by omega : c ≤ m), ← zpow_neg, div_eq_mul_inv, ← zpow_neg,
        ← zpow_add₀ hq, ← zpow_add₀ hq, ← zpow_add₀ hq]
      congr 1; ring
    rw [key]; ring
  · have key : q ^ (2 * ((c : ℤ) + 1) * e) / q ^ (2 * (c : ℤ) * e) * (q ^ (m - e) * (q ^ e)⁻¹)
        = q ^ m := by
      rw [← zpow_natCast q (m - e), ← zpow_natCast q e, ← zpow_natCast q m,
        Nat.cast_sub (by omega : e ≤ m), ← zpow_neg, div_eq_mul_inv, ← zpow_neg,
        ← zpow_add₀ hq, ← zpow_add₀ hq, ← zpow_add₀ hq]
      congr 1; ring
    rw [← key]; ring

section Strings

variable (hq : q ≠ 0)
include hq

/-- `D P` maps the highest-weight vector at `q⁻¹` to a multiple of the one at `q`. -/
theorem conjV_hwVec (j : ℕ) (hj : j ≤ m) (hint : ∀ p < j, qint q (m - p) ≠ 0) :
    conjV q m (hwVec q⁻¹ m m j) = hwCoef q⁻¹ m m j j • hwVec q m m j := by
  have hint' : ∀ p < j, qint q⁻¹ (m - p) ≠ 0 := fun p hp => by rw [qint_inv]; exact hint p hp
  have hsupp : ∀ x : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ j →
      conjV q m (hwVec q⁻¹ m m j) x = 0 := by
    intro x hx
    simp only [conjV, hwVec, Prod.fst_swap, Prod.snd_swap]
    rw [if_neg (by omega), mul_zero]
  have hE : deltaE q m m *ᵥ conjV q m (hwVec q⁻¹ m m j) = 0 := by
    have h := conjM_deltaE m hq
    have hd : deltaE q m m = q ^ (m : ℤ) • conjM q m (deltaE q⁻¹ m m) := by
      rw [h, smul_smul, ← zpow_add₀ hq, add_neg_cancel, zpow_zero, one_smul]
    rw [hd, smul_mulVec, conjM_mulVec m hq,
      show deltaE q⁻¹ m m *ᵥ hwVec q⁻¹ m m j = 0 from
        hwVec_E q⁻¹ (inv_ne_zero hq) m m j hj hj hint']
    funext x; simp [conjV]
  have hu := hw_unique q hq m m j hj hint _ hsupp hE
  rw [hu]
  congr 1
  simp [conjV, dw, hwVec]

/-- `D P` maps the string vectors at `q⁻¹` to multiples of those at `q`. -/
theorem conjV_strVec (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) (x : StrIdx m) :
    conjV q m (strVec q⁻¹ m x)
      = ((q ^ (m : ℤ)) ^ (x.2 : ℕ) * hwCoef q⁻¹ m m x.1 x.1) • strVec q m x := by
  have hF : conjM q m (deltaF q⁻¹ m m ^ (x.2 : ℕ)) = (q ^ (m : ℤ)) ^ (x.2 : ℕ) • deltaF q m m ^ (x.2 : ℕ) := by
    rw [conjM_pow m hq, conjM_deltaF m hq, smul_pow]
  rw [strVec, ← conjM_mulVec m hq, hF,
    conjV_hwVec m hq x.1 (by omega) (fun p hp => hint _ (by omega) (by omega)),
    smul_mulVec, mulVec_smul, smul_smul, strVec]

theorem hwCoef_inv_ne_zero (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) (j : ℕ) (hj : j ≤ m) :
    hwCoef q⁻¹ m m j j ≠ 0 :=
  hwCoef_ne_zero_of_le q⁻¹ (inv_ne_zero hq) m j hj
    (fun i h1 h2 => by rw [qint_inv]; exact hint i h1 h2) j le_rfl

end Strings

end Conj

section MonoBar

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ)

/-- **The inverse monodromy**, written as the monodromy at `s⁻¹` conjugated by `D P`. -/
def monoBar : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  conjM (s ^ 2) m (mono s⁻¹ (inv_ne_zero hs) m m)

/-- A right inverse commutes with whatever the matrix commutes with. -/
theorem commute_of_mul_eq_one {ι : Type*} [Fintype ι] [DecidableEq ι] {A B X : Matrix ι ι 𝕜}
    (hAB : A * B = 1) (hX : A * X = X * A) : B * X = X * B := by
  have hBA : B * A = 1 := mul_eq_one_comm.mp hAB
  calc B * X = B * X * (A * B) := by rw [hAB, Matrix.mul_one]
    _ = B * (A * X) * B := by rw [hX]; simp only [Matrix.mul_assoc]
    _ = X * B := by rw [← Matrix.mul_assoc, hBA, Matrix.one_mul]

theorem hq2_inv (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) : (s⁻¹) ^ 2 - ((s⁻¹) ^ 2)⁻¹ ≠ 0 := by
  rw [inv_pow, inv_inv, ← neg_sub]; exact neg_ne_zero.mpr hq2

theorem hint_inv (N : ℕ) (hint : ∀ i, 0 < i → i ≤ N → qint (s ^ 2) i ≠ 0) :
    ∀ i, 0 < i → i ≤ N → qint ((s⁻¹) ^ 2) i ≠ 0 := fun i h1 h2 => by
  rw [inv_pow, qint_inv]; exact hint i h1 h2

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- `M` on the string through `w_j`: `q^{2n(n+1) − m(m+2)}`. -/
theorem mono_strVec (x : StrIdx m) :
    mono s hs m m *ᵥ strVec (s ^ 2) m x
      = (((s ^ 2) ^ ((m : ℤ) * (m + 2)))⁻¹ * twistSc s m x.1) • strVec (s ^ 2) m x := by
  have h := twist0_strVec s hs hq2 m hint x
  have hK : (s ^ 2) ^ ((m : ℤ) * (m + 2)) ≠ 0 := zpow_ne_zero _ (pow_ne_zero 2 hs)
  rw [twist0, smul_mulVec] at h
  rw [← smul_smul, ← h, smul_smul, inv_mul_cancel₀ hK, one_smul]

include hq2 hint in
/-- `D P M(s⁻¹) P D⁻¹` on the string through `w_j`: the inverse scalar. -/
theorem monoBar_strVec (x : StrIdx m) :
    monoBar s hs m *ᵥ strVec (s ^ 2) m x
      = ((s ^ 2) ^ ((m : ℤ) * (m + 2)) * (twistSc s m x.1)⁻¹) • strVec (s ^ 2) m x := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hm : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  have hc := conjV_strVec m hq hm x
  have hcne : ((s ^ 2) ^ (m : ℤ)) ^ (x.2 : ℕ) * hwCoef (s ^ 2)⁻¹ m m x.1 x.1 ≠ 0 :=
    mul_ne_zero (pow_ne_zero _ (zpow_ne_zero _ hq)) (hwCoef_inv_ne_zero m hq hm x.1 (by omega))
  have hstr : strVec (s ^ 2) m x
      = (((s ^ 2) ^ (m : ℤ)) ^ (x.2 : ℕ) * hwCoef (s ^ 2)⁻¹ m m x.1 x.1)⁻¹
          • conjV (s ^ 2) m (strVec (s ^ 2)⁻¹ m x) := by
    rw [hc, smul_smul, inv_mul_cancel₀ hcne, one_smul]
  have h' := twist0_strVec s⁻¹ (inv_ne_zero hs) (hq2_inv s hq2) m (hint_inv s (2 * m) hint) x
  rw [twist0, smul_mulVec, inv_pow] at h'
  have hT : twistSc s⁻¹ m x.1 = (twistSc s m x.1)⁻¹ := by unfold twistSc; rw [inv_pow, inv_zpow]
  have hK' : ((s ^ 2)⁻¹) ^ ((m : ℤ) * (m + 2)) ≠ 0 := zpow_ne_zero _ (inv_ne_zero hq)
  have hmono : mono s⁻¹ (inv_ne_zero hs) m m *ᵥ strVec (s ^ 2)⁻¹ m x
      = ((s ^ 2) ^ ((m : ℤ) * (m + 2)) * (twistSc s m x.1)⁻¹) • strVec (s ^ 2)⁻¹ m x := by
    have := congrArg (fun v => (((s ^ 2)⁻¹) ^ ((m : ℤ) * (m + 2)))⁻¹ • v) h'
    simp only [smul_smul, inv_mul_cancel₀ hK', one_smul] at this
    rw [this, hT, inv_zpow, inv_inv]
  conv_lhs => rw [hstr]
  rw [mulVec_smul, monoBar, conjM_mulVec m hq, hmono, conjV_smul, smul_comm, ← hstr]

include hq2 hint in
/-- **`M · D P M(s⁻¹) P D⁻¹ = 1`.** -/
theorem mono_mul_monoBar : mono s hs m m * monoBar s hs m = 1 := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  apply Matrix.toLin'.injective
  refine (strBasis (s ^ 2) hq m hq2 hint).ext fun x => ?_
  rw [strBasis_apply, Matrix.toLin'_apply, Matrix.toLin'_apply, ← mulVec_mulVec,
    monoBar_strVec s hs m hq2 hint x, mulVec_smul, mono_strVec s hs m hq2 hint x, smul_smul,
    one_mulVec]
  have hK : (s ^ 2) ^ ((m : ℤ) * (m + 2)) ≠ 0 := zpow_ne_zero _ hq
  have hT : twistSc s m x.1 ≠ 0 := zpow_ne_zero _ hq
  rw [show (s ^ 2) ^ ((m : ℤ) * (m + 2)) * (twistSc s m x.1)⁻¹
      * (((s ^ 2) ^ ((m : ℤ) * (m + 2)))⁻¹ * twistSc s m x.1) = 1 by field_simp, one_smul]

include hq2 hint in
/-- **The inverse monodromy is `D P M(s⁻¹) P D⁻¹`.** -/
theorem monoBar_eq_inv : (mono s hs m m)⁻¹ = monoBar s hs m :=
  Matrix.inv_eq_right_inv (mono_mul_monoBar s hs m hq2 hint)

include hq2 hint in
theorem monoBar_deltaE :
    monoBar s hs m * deltaE (s ^ 2) m m = deltaE (s ^ 2) m m * monoBar s hs m :=
  commute_of_mul_eq_one (mono_mul_monoBar s hs m hq2 hint)
    (mono_deltaE s hs hq2 m m fun k hk => hint (k + 1) (by omega) (by unfold rOrder at hk; omega))

include hq2 hint in
theorem monoBar_deltaF :
    monoBar s hs m * deltaF (s ^ 2) m m = deltaF (s ^ 2) m m * monoBar s hs m :=
  commute_of_mul_eq_one (mono_mul_monoBar s hs m hq2 hint)
    (mono_deltaF s hs hq2 m m fun k hk => hint (k + 1) (by omega) (by unfold rOrder at hk; omega))

include hq2 hint in
theorem monoBar_deltaK :
    monoBar s hs m * deltaK (s ^ 2) m m = deltaK (s ^ 2) m m * monoBar s hs m :=
  commute_of_mul_eq_one (mono_mul_monoBar s hs m hq2 hint) (mono_deltaK s hs m m)

include hq2 hint in
theorem monoBar_deltaKm :
    monoBar s hs m * deltaKm (s ^ 2) m m = deltaKm (s ^ 2) m m * monoBar s hs m :=
  commute_of_mul_eq_one (mono_mul_monoBar s hs m hq2 hint) (mono_deltaKm s hs m m)

end MonoBar

end QOU.Mass.QuantumSl2
