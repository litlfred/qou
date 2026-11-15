import QOU.Mass.QuantumSl2RMatrix

/-!
# Highest-weight vectors in `V_{m+1} ⊗ V_{m'+1}`

Stage 2a of deriving Zheng's tangle functions. For `j ≤ min m m'` the vector

    w_j = Σ_{p+r=j} a_p v_p ⊗ v_r,   a_0 = 1,
    a_{p+1} = −a_p [m'−j+p+1] q^{−(m'−2(j−1−p))} / [m−p],

is annihilated by `Δ(E) = E⊗K + 1⊗E` (`hwVec_E`). It spans the highest-weight line of the
summand `V_{m+m'−2j+1}` of the Clebsch–Gordan decomposition.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VII.7
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-- `Σ_x [p+1 = x] f x` over `Fin (m+1)`. -/
theorem sum_fin_succ_ite (m p : ℕ) (f : Fin (m + 1) → 𝕜) :
    (∑ x : Fin (m + 1), if p + 1 = (x : ℕ) then f x else 0)
      = if h : p + 1 < m + 1 then f ⟨p + 1, h⟩ else 0 := by
  split_ifs with h
  · rw [Finset.sum_eq_single ⟨p + 1, h⟩]
    · simp
    · intro b _ hb
      rw [if_neg]
      intro e; apply hb; ext; simp [e]
    · simp
  · refine Finset.sum_eq_zero fun x _ => ?_
    rw [if_neg]; omega

/-- The `K` eigenvalue `q^{m−p} q^{−p}` as the integer power `q^{m−2p}`. -/
theorem kp_eq_zpow (q : 𝕜) (hq : q ≠ 0) {m p : ℕ} (hp : p ≤ m) :
    q ^ (m - p) * q⁻¹ ^ p = q ^ (wt m p) := by
  obtain ⟨k, rfl⟩ := Nat.exists_eq_add_of_le hp
  unfold wt
  rw [Nat.add_sub_cancel_left,
    show (((p + k : ℕ) : ℤ) - 2 * p) = (k : ℤ) - (p : ℤ) by push_cast; ring,
    zpow_sub₀ hq, zpow_natCast, zpow_natCast, inv_pow, div_eq_mul_inv]

/-- The highest-weight coefficients `a_p`. -/
def hwCoef (q : 𝕜) (m m' j : ℕ) : ℕ → 𝕜
  | 0 => 1
  | p + 1 => -(hwCoef q m m' j p * qint q (m' - j + p + 1) * q ^ (-(wt m' (j - 1 - p))))
      / qint q (m - p)

/-- The highest-weight vector `w_j ∈ V_{m+1} ⊗ V_{m'+1}`. -/
def hwVec (q : 𝕜) (m m' j : ℕ) : Fin (m + 1) × Fin (m' + 1) → 𝕜 :=
  fun x => if (x.1 : ℕ) + x.2 = j then hwCoef q m m' j x.1 else 0

/-- **`Δ(E) w_j = 0`.** -/
theorem hwVec_E (q : 𝕜) (hq : q ≠ 0) (m m' j : ℕ) (hjm : j ≤ m) (hjm' : j ≤ m')
    (hint : ∀ p < j, qint q (m - p) ≠ 0) :
    (irrepE q m ⊗ₖ irrepKp q m' + 1 ⊗ₖ irrepE q m') *ᵥ hwVec q m m' j = 0 := by
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  simp only [mulVec, dotProduct, Fintype.sum_prod_type, Matrix.add_apply, kroneckerMap_apply,
    add_mul, Finset.sum_add_distrib, irrepE, irrepKp, diagonal_apply, one_apply, ite_mul,
    zero_mul, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.sum_ite_eq',
    Finset.mem_univ, if_true, Pi.zero_apply]
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, one_mul]
  rw [sum_fin_succ_ite, sum_fin_succ_ite]
  unfold hwVec
  by_cases hj : p + r + 1 = j
  · subst hj
    rw [dif_pos (by omega), dif_pos (by omega)]
    simp only [Fin.val_mk, if_pos (show p + 1 + r = p + r + 1 by omega),
      if_pos (show p + (r + 1) = p + r + 1 by omega)]
    have hmp : qint q (m - p) ≠ 0 := hint p (by omega)
    rw [hwCoef, show m - (p + 1) + 1 = m - p by omega, show m' - (p + r + 1) + p + 1 = m' - r by omega,
      show m' - (r + 1) + 1 = m' - r by omega, show p + r + 1 - 1 - p = r by omega,
      kp_eq_zpow q hq (by omega : r ≤ m')]
    field_simp
    rw [mul_assoc, ← zpow_add₀ hq, add_neg_cancel, zpow_zero]
    ring
  · simp [show ¬(p + 1 + r = j) by omega, show ¬(p + (r + 1) = j) by omega]

/-- The entries of `Δ(E) u` on `V_{m+1} ⊗ V_{m'+1}`. -/
theorem dE_apply (q : 𝕜) (hq : q ≠ 0) (m m' : ℕ) (u : Fin (m + 1) × Fin (m' + 1) → 𝕜)
    (p r : ℕ) (hp : p < m + 1) (hr : r < m' + 1) :
    ((irrepE q m ⊗ₖ irrepKp q m' + 1 ⊗ₖ irrepE q m') *ᵥ u) (⟨p, hp⟩, ⟨r, hr⟩)
      = (if h : p + 1 < m + 1 then qint q (m - p) * q ^ (wt m' r) * u (⟨p + 1, h⟩, ⟨r, hr⟩)
          else 0)
        + (if h : r + 1 < m' + 1 then qint q (m' - r) * u (⟨p, hp⟩, ⟨r + 1, h⟩) else 0) := by
  simp only [mulVec, dotProduct, Fintype.sum_prod_type, Matrix.add_apply, kroneckerMap_apply,
    add_mul, Finset.sum_add_distrib, irrepE, irrepKp, diagonal_apply, one_apply, ite_mul,
    zero_mul, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ,
    if_true]
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, one_mul]
  rw [sum_fin_succ_ite, sum_fin_succ_ite]
  congr 1
  · split_ifs with h
    · simp only [Fin.val_mk, show m - (p + 1) + 1 = m - p by omega,
        kp_eq_zpow q hq (by omega : r ≤ m')]
    · rfl
  · split_ifs with h
    · simp only [Fin.val_mk, show m' - (r + 1) + 1 = m' - r by omega]
    · rfl

/-- **Uniqueness of the highest-weight vector.** A vector of weight `m+m'−2j` killed by `Δ(E)`
is a multiple of `w_j`. -/
theorem hw_unique (q : 𝕜) (hq : q ≠ 0) (m m' j : ℕ) (hjm : j ≤ m) (hjm' : j ≤ m')
    (hint : ∀ p < j, qint q (m - p) ≠ 0) (u : Fin (m + 1) × Fin (m' + 1) → 𝕜)
    (hsupp : ∀ x : Fin (m + 1) × Fin (m' + 1), (x.1 : ℕ) + x.2 ≠ j → u x = 0)
    (hE : (irrepE q m ⊗ₖ irrepKp q m' + 1 ⊗ₖ irrepE q m') *ᵥ u = 0) :
    u = u (⟨0, by omega⟩, ⟨j, by omega⟩) • hwVec q m m' j := by
  have key : ∀ p (h1 : p < m + 1) (h2 : j - p < m' + 1), p ≤ j →
      u (⟨p, h1⟩, ⟨j - p, h2⟩) = u (⟨0, by omega⟩, ⟨j, by omega⟩) * hwCoef q m m' j p := by
    intro p
    induction p with
    | zero => intro h1 h2 _; simp [hwCoef]
    | succ p ih =>
      intro h1 h2 hpj
      have hE' := congrFun hE (⟨p, by omega⟩, ⟨j - 1 - p, by omega⟩)
      rw [dE_apply q hq, dif_pos h1, dif_pos (by omega), Pi.zero_apply] at hE'
      have e1 : u (⟨p + 1, h1⟩, ⟨j - 1 - p, by omega⟩) = u (⟨p + 1, h1⟩, ⟨j - (p + 1), h2⟩) := by
        congr 3; omega
      have e2 : u (⟨p, by omega⟩, ⟨j - 1 - p + 1, by omega⟩) = u (⟨p, by omega⟩, ⟨j - p, by omega⟩) := by
        congr 3; omega
      rw [e1, e2, ih (by omega) (by omega) (by omega)] at hE'
      have hmp : qint q (m - p) ≠ 0 := hint p (by omega)
      rw [hwCoef, show m' - j + p + 1 = m' - (j - 1 - p) by omega]
      field_simp
      have hz : q ^ (wt m' (j - 1 - p)) * q ^ (-wt m' (j - 1 - p)) = 1 := by
        rw [← zpow_add₀ hq, add_neg_cancel, zpow_zero]
      linear_combination (q ^ (-wt m' (j - 1 - p))) * hE' - (u (⟨p + 1, h1⟩, ⟨j - (p + 1), h2⟩)
        * qint q (m - p)) * hz
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  simp only [Pi.smul_apply, smul_eq_mul, hwVec]
  by_cases hpr : p + r = j
  · rw [if_pos hpr]
    have := key p hp (by omega) (by omega)
    rw [← this]
    congr 3; omega
  · rw [if_neg hpr, mul_zero]
    exact hsupp _ hpr

end QOU.Mass.QuantumSl2
