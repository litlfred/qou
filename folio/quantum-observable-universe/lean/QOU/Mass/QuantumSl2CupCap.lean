import QOU.Mass.QuantumSl2Clasp

/-!
# Cup, cap and the snake identity on `V_{m+1} ⊗ V_{m+1}`

Stage 3b of deriving Zheng's tangle functions (van der Veen 2008, Lemma 1). The clasp file
(`QuantumSl2Clasp`) uses cup coefficients `a_p` and cap coefficients `b_p` as given numbers.
This file shows they are the right ones:

* the cup `Σ_p a_p v_p ⊗ v_{m−p}` is invariant: killed by `Δ(E)` and `Δ(F)`, fixed by `K ⊗ K`
  (`cupVec_E`, `cupVec_F`, `cupVec_K`);
* the cap functional `Σ_p b_p (v_p ⊗ v_{m−p})^*`, with `b_p = (−1)^m q^{m−2p} / a_p`, is
  invariant: `cap ∘ Δ(E) = 0`, `cap ∘ Δ(F) = 0`, `cap ∘ (K ⊗ K) = cap`
  (`capVec_E`, `capVec_F`, `capVec_K`);
* both snake identities hold, in coefficient form `b_i a_{m−i} = 1` and `a_i b_{m−i} = 1`
  (`snake_coef`, `snake_coef'`).

Both cap conditions reduce to one recursion, `cap_rel`. All statements are over a general field
with the `q`-integers `[1], …, [m]` nonzero; nothing archimedean is used.

-- Ref: [vanderveen2008] van der Veen, AGT 8 (2008) 603–624, proof of Lemma 1
-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VII, XIV
-/

namespace QOU.Mass.QuantumSl2
open Matrix
open scoped Kronecker
variable {𝕜 : Type*} [Field 𝕜]

/-- `Σ_x [p = x+1] f x` over `Fin (m+1)`. -/
theorem sum_fin_pred_ite (m p : ℕ) (f : Fin (m + 1) → 𝕜) (hp : p < m + 1) :
    (∑ x : Fin (m + 1), if p = (x : ℕ) + 1 then f x else 0)
      = if h : 0 < p then f ⟨p - 1, by omega⟩ else 0 := by
  split_ifs with h
  · rw [Finset.sum_eq_single ⟨p - 1, by omega⟩]
    · simp; omega
    · intro b _ hb
      rw [if_neg]
      intro e; apply hb; ext; simp; omega
    · simp
  · refine Finset.sum_eq_zero fun x _ => ?_
    rw [if_neg]; omega

/-- The entries of `Δ(F) u` on `V_{m+1} ⊗ V_{m'+1}`. -/
theorem dF_apply (q : 𝕜) (m m' : ℕ) (u : Fin (m + 1) × Fin (m' + 1) → 𝕜)
    (p r : ℕ) (hp : p < m + 1) (hr : r < m' + 1) :
    (deltaF q m m' *ᵥ u) (⟨p, hp⟩, ⟨r, hr⟩)
      = (if h : 0 < r then q⁻¹ ^ (m - p) * q ^ p * qint q r * u (⟨p, hp⟩, ⟨r - 1, by omega⟩)
          else 0)
        + (if h : 0 < p then qint q p * u (⟨p - 1, by omega⟩, ⟨r, hr⟩) else 0) := by
  simp only [deltaF, mulVec, dotProduct, Fintype.sum_prod_type, Matrix.add_apply,
    kroneckerMap_apply, add_mul, Finset.sum_add_distrib, irrepF, irrepKm, diagonal_apply,
    one_apply, ite_mul, zero_mul, mul_ite, mul_zero, Finset.sum_ite_eq,
    Finset.mem_univ, if_true]
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, mul_one]
  rw [sum_fin_pred_ite m' r _ hr, sum_fin_pred_ite m p _ hp]
  congr 1
  · split_ifs with h
    · simp only [show r - 1 + 1 = r by omega]
    · rfl
  · split_ifs with h
    · simp only [show p - 1 + 1 = p by omega]
    · rfl

/-- The cup vector `Σ_p a_p v_p ⊗ v_{m−p}` (the highest-weight vector `w_m` of weight 0). -/
def cupVec (q : 𝕜) (m : ℕ) : Fin (m + 1) × Fin (m + 1) → 𝕜 := hwVec q m m m

/-- **The cup is killed by `Δ(E)`.** -/
theorem cupVec_E (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ p < m, qint q (m - p) ≠ 0) :
    (irrepE q m ⊗ₖ irrepKp q m + 1 ⊗ₖ irrepE q m) *ᵥ cupVec q m = 0 :=
  hwVec_E q hq m m m le_rfl le_rfl hint

/-- **The cup is killed by `Δ(F)`.** -/
theorem cupVec_F (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ p < m, qint q (m - p) ≠ 0) :
    deltaF q m m *ᵥ cupVec q m = 0 := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  rw [dF_apply, Pi.zero_apply]
  unfold cupVec hwVec
  dsimp only
  by_cases hpr : p + r = m + 1
  · obtain ⟨p', rfl⟩ : ∃ p', p = p' + 1 := ⟨p - 1, by omega⟩
    rw [dif_pos (by omega), dif_pos (by omega), if_pos (by omega), if_pos (by omega),
      Nat.add_sub_cancel]
    have hmp : qint q (m - p') ≠ 0 := hint p' (by omega)
    have hz : q⁻¹ ^ (m - (p' + 1)) * q ^ (p' + 1) * q ^ (-wt m (m - 1 - p')) = 1 := by
      rw [show -wt m (m - 1 - p') = ((m - (p' + 1) : ℕ) : ℤ) - ((p' + 1 : ℕ) : ℤ) by
          unfold wt; push_cast [Nat.cast_sub (show m - 1 - p' ≤ m by omega),
            Nat.cast_sub (show 1 + p' ≤ m by omega), Nat.cast_sub (show p' + 1 ≤ m by omega)]; omega,
        zpow_sub₀ hq, zpow_natCast, zpow_natCast, inv_pow]
      field_simp
    rw [hwCoef, show m - m + p' + 1 = p' + 1 by omega, show r = m - p' by omega]
    field_simp
    linear_combination (-(hwCoef q m m m p' * qint q (p' + 1))) * hz
  · split_ifs <;> first | omega | simp

theorem inv_pow_mul_pow (q : 𝕜) (hq : q ≠ 0) (a b : ℕ) :
    q⁻¹ ^ a * q ^ b = q ^ ((b : ℤ) - a) := by
  rw [zpow_sub₀ hq, zpow_natCast, zpow_natCast, inv_pow, div_eq_mul_inv, mul_comm]

/-- **The cup has weight 0.** -/
theorem cupVec_K (q : 𝕜) (hq : q ≠ 0) (m : ℕ) :
    (irrepKp q m ⊗ₖ irrepKp q m) *ᵥ cupVec q m = cupVec q m := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  simp only [mulVec, dotProduct, Fintype.sum_prod_type, kroneckerMap_apply, irrepKp,
    diagonal_apply, ite_mul, zero_mul, mul_ite, mul_zero]
  rw [Finset.sum_eq_single ⟨p, hp⟩, Finset.sum_eq_single ⟨r, hr⟩]
  · simp only [if_true]
    unfold cupVec hwVec
    dsimp only
    split_ifs with h
    · rw [show m - r = p by omega, show r = m - p by omega]
      simp only [inv_pow]
      field_simp
    · simp
  all_goals first
    | (intro b _ hb; simp [Ne.symm hb])
    | simp

theorem qfact_ne_zero_of (q : 𝕜) (N : ℕ) (hint : ∀ i, 0 < i → i ≤ N → qint q i ≠ 0) (i : ℕ)
    (hi : i ≤ N) : qfact q i ≠ 0 := by
  unfold qfact
  exact Finset.prod_ne_zero_iff.mpr (fun r hr => hint _ (by omega)
    (by have := Finset.mem_range.mp hr; omega))

/-- `a_p ≠ 0`. -/
theorem hwCoef_ne_zero (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (p : ℕ) (hp : p ≤ m) : hwCoef q m m m p ≠ 0 := by
  induction p with
  | zero => simp [hwCoef]
  | succ p ih =>
    rw [hwCoef]
    refine div_ne_zero (neg_ne_zero.mpr (mul_ne_zero (mul_ne_zero (ih (by omega))
      (hint _ (by omega) (by omega))) (zpow_ne_zero _ hq))) (hint _ (by omega) (by omega))

/-- The cap coefficient `b_p = (−1)^m q^{m−2p} / a_p` over a general `q`. -/
def capCoefQ (q : 𝕜) (m p : ℕ) : 𝕜 := (-1) ^ m * q ^ ((m : ℤ) - 2 * p) / hwCoef q m m m p

/-- The cap functional `Σ_p b_p (v_p ⊗ v_{m−p})^*`. -/
def capVec (q : 𝕜) (m : ℕ) : Fin (m + 1) × Fin (m + 1) → 𝕜 :=
  fun x => if (x.1 : ℕ) + x.2 = m then capCoefQ q m x.1 else 0

/-- **Snake identity.** `(cap ⊗ 1)(1 ⊗ cup) = 1` on `V_{m+1}`: its `i`-th diagonal entry is
`b_i a_{m−i}`, and every off-diagonal entry vanishes by weight. -/
theorem snake_coef (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (i : ℕ) (hi : i ≤ m) : capCoefQ q m i * hwCoef q m m m (m - i) = 1 := by
  have hf := qfact_ne_zero_of q m hint
  have hint' : ∀ k, k < m → qint q (m - k) ≠ 0 := fun k hk => hint _ (by omega) (by omega)
  have h1 := hwCoef_closed q hq m m i hi le_rfl (fun k hk => hint' k (by omega))
  have h2 := hwCoef_closed q hq m m (m - i) (by omega) le_rfl (fun k hk => hint' k (by omega))
  rw [Nat.sub_self, zero_add] at h1 h2
  rw [show m - (m - i) = i by omega] at h2
  have hA := hwCoef_ne_zero q hq m hint i hi
  have hf0 : qfact q 0 = 1 := by simp [qfact]
  rw [hf0, mul_one] at h1 h2
  have hexp : q ^ ((m : ℤ) - 2 * i) * q ^ (-(((m - i : ℕ) : ℤ) * ((m : ℤ) - 2 * m + ((m - i : ℕ) : ℤ) + 1)))
      = q ^ (-((i : ℤ) * ((m : ℤ) - 2 * m + i + 1))) := by
    rw [← zpow_add₀ hq]; congr 1; push_cast [Nat.cast_sub hi]; ring
  have hsign : ((-1 : 𝕜)) ^ m * (-1) ^ (m - i) = (-1) ^ i := by
    rw [show (-1 : 𝕜) ^ m = (-1) ^ (m - i) * (-1) ^ i by rw [← pow_add, Nat.sub_add_cancel hi],
      mul_comm, ← mul_assoc, ← pow_add, ← two_mul, pow_mul, neg_one_sq, one_pow, one_mul]
  unfold capCoefQ
  rw [div_mul_eq_mul_div, div_eq_one_iff_eq hA]
  apply mul_right_cancel₀ (hf m le_rfl)
  linear_combination (-1) ^ m * q ^ ((m : ℤ) - 2 * i) * h2 - h1
    + qfact q (m - i) * qfact q i * (-1) ^ m * (-1) ^ (m - i) * hexp
    + qfact q (m - i) * qfact q i * q ^ (-((i : ℤ) * ((m : ℤ) - 2 * m + i + 1))) * hsign

theorem cap_rel (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (p : ℕ) (hp : p < m)
    (ha : hwCoef q m m m p ≠ 0) (ha' : hwCoef q m m m (p + 1) ≠ 0) :
    capCoefQ q m p * q ^ ((2 * p : ℤ) - m) * qint q (m - p)
      + capCoefQ q m (p + 1) * qint q (p + 1) = 0 := by
  have hrec : hwCoef q m m m (p + 1)
      = -(hwCoef q m m m p * qint q (p + 1) * q ^ ((m : ℤ) - 2 * p - 2)) / qint q (m - p) := by
    rw [hwCoef, show m - m + p + 1 = p + 1 by omega]
    congr 3
    unfold wt; congr 1
    rw [show m - 1 - p = m - (p + 1) by omega, Nat.cast_sub (show p + 1 ≤ m by omega)]; push_cast; ring
  have hE : q ^ ((m : ℤ) - 2 * p - 2) ≠ 0 := zpow_ne_zero _ hq
  have h1 : q ^ ((m : ℤ) - 2 * p) = q ^ ((m : ℤ) - 2 * p - 2) * q ^ 2 := by
    rw [← zpow_natCast, ← zpow_add₀ hq]; congr 1; push_cast; ring
  have h2 : q ^ ((2 * p : ℤ) - m) * q ^ ((m : ℤ) - 2 * p - 2) * q ^ 2 = 1 := by
    rw [← zpow_natCast, ← zpow_add₀ hq, ← zpow_add₀ hq]
    rw [show (2 * p : ℤ) - m + ((m : ℤ) - 2 * p - 2) + ((2 : ℕ) : ℤ) = 0 by push_cast; ring, zpow_zero]
  have h3 : q ^ ((m : ℤ) - 2 * ((p + 1 : ℕ) : ℤ)) = q ^ ((m : ℤ) - 2 * p - 2) := by
    congr 1; push_cast; ring
  have hq1 : qint q (p + 1) ≠ 0 := by
    intro h; apply ha'; rw [hrec, h]; simp
  unfold capCoefQ
  rw [h3, hrec, h1]
  field_simp
  linear_combination (-1) ^ m * qint q (m - p) * h2


theorem sum_fin_eq_ite (m a : ℕ) (f : Fin (m + 1) → 𝕜) :
    (∑ x : Fin (m + 1), if (x : ℕ) = a then f x else 0)
      = if h : a < m + 1 then f ⟨a, h⟩ else 0 := by
  split_ifs with h
  · rw [Finset.sum_eq_single ⟨a, h⟩]
    · simp
    · intro b _ hb; rw [if_neg]; intro e; apply hb; ext; exact e
    · simp
  · refine Finset.sum_eq_zero fun x _ => ?_
    rw [if_neg]; omega

theorem vF_apply (q : 𝕜) (m m' : ℕ) (u : Fin (m + 1) × Fin (m' + 1) → 𝕜)
    (p r : ℕ) (hp : p < m + 1) (hr : r < m' + 1) :
    (u ᵥ* deltaF q m m') (⟨p, hp⟩, ⟨r, hr⟩)
      = (if h : r + 1 < m' + 1 then q⁻¹ ^ (m - p) * q ^ p * qint q (r + 1) * u (⟨p, hp⟩, ⟨r + 1, h⟩)
          else 0)
        + (if h : p + 1 < m + 1 then qint q (p + 1) * u (⟨p + 1, h⟩, ⟨r, hr⟩) else 0) := by
  simp only [deltaF, vecMul, dotProduct, Fintype.sum_prod_type, Matrix.add_apply,
    kroneckerMap_apply, mul_add, Finset.sum_add_distrib, irrepF, irrepKm, diagonal_apply,
    one_apply, ite_mul, zero_mul, mul_ite, mul_zero, Fin.ext_iff]
  simp only [sum_fin_eq_ite, Finset.sum_dite_irrel, Finset.sum_const_zero, mul_one]
  simp only [dif_pos hr, dif_pos hp]
  congr 1
  · split_ifs <;> ring
  · split_ifs <;> ring


theorem sum_fin_succ_eq (m a : ℕ) (f : Fin (m + 1) → 𝕜) (ha : a < m + 2) :
    (∑ x : Fin (m + 1), if (x : ℕ) + 1 = a then f x else 0)
      = if h : 0 < a then f ⟨a - 1, by omega⟩ else 0 := by
  split_ifs with h
  · rw [Finset.sum_eq_single ⟨a - 1, by omega⟩]
    · simp; omega
    · intro b _ hb; rw [if_neg]; intro e; apply hb; ext; simp; omega
    · simp
  · refine Finset.sum_eq_zero fun x _ => ?_
    rw [if_neg]; omega

theorem vE_apply (q : 𝕜) (m m' : ℕ) (u : Fin (m + 1) × Fin (m' + 1) → 𝕜)
    (p r : ℕ) (hp : p < m + 1) (hr : r < m' + 1) :
    (u ᵥ* (irrepE q m ⊗ₖ irrepKp q m' + 1 ⊗ₖ irrepE q m')) (⟨p, hp⟩, ⟨r, hr⟩)
      = (if h : 0 < p then qint q (m - p + 1) * (q ^ (m' - r) * q⁻¹ ^ r)
            * u (⟨p - 1, by omega⟩, ⟨r, hr⟩) else 0)
        + (if h : 0 < r then qint q (m' - r + 1) * u (⟨p, hp⟩, ⟨r - 1, by omega⟩) else 0) := by
  simp only [vecMul, dotProduct, Fintype.sum_prod_type, Matrix.add_apply,
    kroneckerMap_apply, mul_add, Finset.sum_add_distrib, irrepE, irrepKp, diagonal_apply,
    one_apply, ite_mul, zero_mul, mul_ite, mul_zero, Fin.ext_iff]
  simp only [sum_fin_eq_ite, sum_fin_succ_eq _ _ _ (show p < m + 2 by omega),
    sum_fin_succ_eq _ _ _ (show r < m' + 2 by omega), Finset.sum_dite_irrel,
    Finset.sum_const_zero, one_mul]
  simp only [dif_pos hr, dif_pos hp]
  congr 1
  · split_ifs <;> ring
  · split_ifs <;> ring

/-- `q⁻¹^(m−p) q^p = q^(2p−m)`. -/
theorem inv_pow_sub_mul_pow (q : 𝕜) (hq : q ≠ 0) (m p : ℕ) (hp : p ≤ m) :
    q⁻¹ ^ (m - p) * q ^ p = q ^ ((2 * p : ℤ) - m) := by
  rw [inv_pow_mul_pow q hq]; congr 1; push_cast [Nat.cast_sub hp]; ring

/-- **The cap is killed by `Δ(F)`.** -/
theorem capVec_F (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) :
    capVec q m ᵥ* deltaF q m m = 0 := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  rw [vF_apply, Pi.zero_apply]
  unfold capVec
  dsimp only
  by_cases hpr : p + r + 1 = m
  · rw [dif_pos (by omega), dif_pos (by omega), if_pos (by omega), if_pos (by omega),
      show r + 1 = m - p by omega, inv_pow_sub_mul_pow q hq m p (by omega)]
    have := cap_rel q hq m p (by omega) (hwCoef_ne_zero q hq m hint p (by omega))
      (hwCoef_ne_zero q hq m hint (p + 1) (by omega))
    linear_combination this
  · split_ifs <;> first | omega | simp

/-- **The cap is killed by `Δ(E)`.** -/
theorem capVec_E (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) :
    capVec q m ᵥ* (irrepE q m ⊗ₖ irrepKp q m + 1 ⊗ₖ irrepE q m) = 0 := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  rw [vE_apply, Pi.zero_apply]
  unfold capVec
  dsimp only
  by_cases hpr : p + r = m + 1
  · obtain ⟨p', rfl⟩ : ∃ p', p = p' + 1 := ⟨p - 1, by omega⟩
    rw [dif_pos (by omega), dif_pos (by omega), if_pos (by omega), if_pos (by omega),
      Nat.add_sub_cancel, show m - (p' + 1) + 1 = m - p' by omega,
      show m - r + 1 = p' + 1 by omega, show r = m - p' by omega,
      show m - (m - p') = p' by omega, mul_comm (q ^ p'),
      inv_pow_sub_mul_pow q hq m p' (by omega)]
    have := cap_rel q hq m p' (by omega) (hwCoef_ne_zero q hq m hint p' (by omega))
      (hwCoef_ne_zero q hq m hint (p' + 1) (by omega))
    linear_combination this
  · split_ifs <;> first | omega | simp

/-- **The cap has weight 0.** -/
theorem capVec_K (q : 𝕜) (hq : q ≠ 0) (m : ℕ) :
    capVec q m ᵥ* (irrepKp q m ⊗ₖ irrepKp q m) = capVec q m := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  simp only [vecMul, dotProduct, Fintype.sum_prod_type, kroneckerMap_apply, irrepKp,
    diagonal_apply, ite_mul, zero_mul, mul_ite, mul_zero, Fin.ext_iff]
  simp only [sum_fin_eq_ite, dif_pos hr, dif_pos hp]
  unfold capVec
  dsimp only
  split_ifs with h
  · rw [show m - p = r by omega, show m - r = p by omega]
    simp only [inv_pow]
    field_simp
  · simp

/-- **The second snake identity**, coefficient form: `a_i b_{m−i} = 1`. -/
theorem snake_coef' (q : 𝕜) (hq : q ≠ 0) (m : ℕ) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (i : ℕ) (hi : i ≤ m) : hwCoef q m m m i * capCoefQ q m (m - i) = 1 := by
  rw [mul_comm]
  have := snake_coef q hq m hint (m - i) (by omega)
  rwa [show m - (m - i) = i by omega] at this

/-- The `s`-form cap coefficient of the clasp is `capCoefQ` at `q = s²`. -/
theorem capCoef_eq (s : 𝕜) (m p : ℕ) : capCoef s m p = capCoefQ (s ^ 2) m p := rfl

end QOU.Mass.QuantumSl2
