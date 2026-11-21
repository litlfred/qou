import QOU.Mass.QuantumSl2RMatrix
import Mathlib.Algebra.BigOperators.Intervals

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
    zero_mul, mul_ite, mul_zero, Finset.sum_ite_eq,
    Finset.mem_univ, if_true, Pi.zero_apply]
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, one_mul]
  rw [sum_fin_succ_ite, sum_fin_succ_ite]
  unfold hwVec
  by_cases hj : p + r + 1 = j
  · subst hj
    rw [dif_pos (by omega), dif_pos (by omega)]
    simp only [if_pos (show p + 1 + r = p + r + 1 by omega),
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
    zero_mul, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true]
  rw [Finset.sum_comm]
  simp only [Finset.sum_ite_irrel, Finset.sum_const_zero, Finset.sum_ite_eq, Finset.mem_univ,
    if_true, one_mul]
  rw [sum_fin_succ_ite, sum_fin_succ_ite]
  congr 1
  · split_ifs with h
    · simp only [show m - (p + 1) + 1 = m - p by omega,
        kp_eq_zpow q hq (by omega : r ≤ m')]
    · rfl
  · split_ifs with h
    · simp only [show m' - (r + 1) + 1 = m' - r by omega]
    · rfl

/-- **Uniqueness of the highest-weight vector.** A vector of weight `m+m'−2j` killed by `Δ(E)`
is a multiple of `w_j`. -/
theorem hw_unique (q : 𝕜) (hq : q ≠ 0) (m m' j : ℕ) (hjm' : j ≤ m')
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

/-! ### The braiding on highest-weight vectors -/

/-- Swapping tensor factors: `(B⊗A)(v∘swap) = ((A⊗B) v)∘swap`. -/
theorem kron_mulVec_swap {ι κ : Type*} [Fintype ι] [Fintype κ] (A : Matrix ι ι 𝕜)
    (B : Matrix κ κ 𝕜) (v : ι × κ → 𝕜) :
    (B ⊗ₖ A) *ᵥ (fun y : κ × ι => v y.swap) = fun y => ((A ⊗ₖ B) *ᵥ v) y.swap := by
  funext y
  simp only [mulVec, dotProduct, Fintype.sum_prod_type, kroneckerMap_apply, Prod.swap]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  ring

section Braiding

variable (s : 𝕜) (hs : s ≠ 0)

/-- `S` preserves the grading `p + r`. -/
theorem rSum_apply_grade (m m' M : ℕ) (x y : Fin (m + 1) × Fin (m' + 1))
    (h : (x.1 : ℕ) + x.2 ≠ y.1 + y.2) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') M x y = 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply]
  refine Finset.sum_eq_zero fun n _ => ?_
  rw [Matrix.smul_apply, kroneckerMap_apply]
  by_cases h1 : (x.1 : ℕ) + n = y.1
  · rw [show (irrep (pow_ne_zero 2 hs) m').F = irrepF (s ^ 2) m' from rfl,
      irrepF_pow_apply (s ^ 2) m' n x.2 y.2 (by omega), mul_zero, smul_zero]
  · rw [show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
      irrepE_pow_apply (s ^ 2) m n x.1 y.1 h1, zero_mul, smul_zero]

/-- The row of `S` at `v_j ⊗ v_0` is the unit row. -/
theorem rSum_apply_top (m m' M j : ℕ) (hj : j < m + 1) (y : Fin (m + 1) × Fin (m' + 1)) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') M
      (⟨j, hj⟩, ⟨0, by omega⟩) y = if y = (⟨j, hj⟩, ⟨0, by omega⟩) then 1 else 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply, Finset.sum_eq_single 0]
  · simp only [Matrix.smul_apply, kroneckerMap_apply, pow_zero, one_apply, smul_eq_mul]
    have hc : rcoef s 0 = 1 := by simp [rcoef, qfact]
    rw [hc, one_mul]
    by_cases hy : y = (⟨j, hj⟩, ⟨0, by omega⟩)
    · subst hy; simp
    · rw [if_neg hy]
      by_cases h1 : (⟨j, hj⟩ : Fin (m + 1)) = y.1
      · have h2 : (⟨0, by omega⟩ : Fin (m' + 1)) ≠ y.2 := by
          intro h2; apply hy; ext <;> simp [← h1, ← h2]
        rw [if_neg h2, mul_zero]
      · rw [if_neg h1, zero_mul]
  · intro n _ hn
    rw [Matrix.smul_apply, kroneckerMap_apply,
      show (irrep (pow_ne_zero 2 hs) m').F = irrepF (s ^ 2) m' from rfl,
      irrepF_pow_apply (s ^ 2) m' n _ y.2 (by simp; omega), mul_zero, smul_zero]
  · simp

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **The braiding on highest-weight vectors.** `Ř = P∘R` sends `w_j ∈ V_{m+1}⊗V_{m'+1}` to
`λ_j w'_j ∈ V_{m'+1}⊗V_{m+1}`, with `λ_j = s^{(m−2j)m'} a_j`. -/
theorem rCheck_hwVec (m m' j : ℕ) (hjm : j ≤ m) (hjm' : j ≤ m')
    (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0)
    (hint1 : ∀ p < j, qint (s ^ 2) (m - p) ≠ 0) (hint2 : ∀ p < j, qint (s ^ 2) (m' - p) ≠ 0) :
    (fun y : Fin (m' + 1) × Fin (m + 1) => (rMat s hs m m' *ᵥ hwVec (s ^ 2) m m' j) y.swap)
      = (s ^ (wt m j * wt m' 0) * hwCoef (s ^ 2) m m' j j) • hwVec (s ^ 2) m' m j := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  set w := hwVec (s ^ 2) m m' j with hw
  set u : Fin (m' + 1) × Fin (m + 1) → 𝕜 := fun y => (rMat s hs m m' *ᵥ w) y.swap with hu
  -- `u` is killed by `Δ(E)` on `V_{m'+1}⊗V_{m+1}`.
  have hRw : (irrepKp (s ^ 2) m ⊗ₖ irrepE (s ^ 2) m' + irrepE (s ^ 2) m ⊗ₖ 1) *ᵥ
      (rMat s hs m m' *ᵥ w) = 0 := by
    rw [mulVec_mulVec, ← rMat_E s hs hq2 m m' hint, ← mulVec_mulVec,
      hwVec_E (s ^ 2) hq m m' j hjm hjm' hint1, mulVec_zero]
  have hE : (irrepE (s ^ 2) m' ⊗ₖ irrepKp (s ^ 2) m + 1 ⊗ₖ irrepE (s ^ 2) m) *ᵥ u = 0 := by
    rw [add_mulVec, hu, kron_mulVec_swap, kron_mulVec_swap]
    funext y
    have := congrFun hRw y.swap
    rw [add_mulVec, Pi.add_apply] at this
    simpa using this
  -- `u` has weight `m+m'−2j`.
  have hsupp : ∀ y : Fin (m' + 1) × Fin (m + 1), (y.1 : ℕ) + y.2 ≠ j → u y = 0 := by
    intro y hy
    simp only [hu, rMat, ← mulVec_mulVec, cartanTheta, mulVec_diagonal]
    rw [mulVec, dotProduct, Finset.sum_eq_zero, mul_zero]
    intro z _
    by_cases hz : (z.1 : ℕ) + z.2 = j
    · rw [rSum_apply_grade s hs m m' _ _ _ (by simp [Prod.swap]; omega), zero_mul]
    · rw [hw, hwVec, if_neg hz, mul_zero]
  rw [hw, hw] at *
  rw [hw] at hu
  refine (hw_unique (s ^ 2) hq m' m j hjm hint2 u hsupp hE).trans ?_
  congr 1
  simp only [hu, Prod.swap, rMat, ← mulVec_mulVec, cartanTheta, mulVec_diagonal]
  rw [mulVec, dotProduct]
  simp only [rSum_apply_top s hs m m' _ j (by omega), ite_mul, one_mul, zero_mul,
    Finset.sum_ite_eq', Finset.mem_univ, if_true, hwVec]
  rw [if_pos (by simp)]

end Braiding

/-! ### Closed form of the braiding eigenvalue -/

/-- Closed form of the highest-weight coefficients:
`a_p · Π_{i<p} [m−i] = (−1)^p q^{−Σ_{i<p} (m'−2(j−1−i))} Π_{i<p} [m'−j+i+1]`. -/
theorem hwCoef_mul_prod (q : 𝕜) (hq : q ≠ 0) (m m' j p : ℕ) (hp : ∀ i < p, qint q (m - i) ≠ 0) :
    hwCoef q m m' j p * ∏ i ∈ Finset.range p, qint q (m - i)
      = (-1) ^ p * q ^ (-∑ i ∈ Finset.range p, wt m' (j - 1 - i))
          * ∏ i ∈ Finset.range p, qint q (m' - j + i + 1) := by
  induction p with
  | zero => simp [hwCoef]
  | succ p ih =>
    have hmp : qint q (m - p) ≠ 0 := hp p (by omega)
    rw [hwCoef, Finset.prod_range_succ, Finset.prod_range_succ, Finset.sum_range_succ, neg_add,
      zpow_add₀ hq]
    have : -(hwCoef q m m' j p * qint q (m' - j + p + 1) * q ^ (-wt m' (j - 1 - p)))
            / qint q (m - p) * ((∏ i ∈ Finset.range p, qint q (m - i)) * qint q (m - p))
          = -(hwCoef q m m' j p * ∏ i ∈ Finset.range p, qint q (m - i))
          * qint q (m' - j + p + 1) * q ^ (-wt m' (j - 1 - p)) := by
      field_simp
    rw [this, ih (fun i hi => hp i (by omega))]
    ring

/-- `Σ_{i<j} (m − 2i) = j m − j (j − 1)`. -/
theorem sum_wt_range (m j : ℕ) :
    ∑ i ∈ Finset.range j, wt m i = (j : ℤ) * m - (j : ℤ) * ((j : ℤ) - 1) := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [Finset.sum_range_succ, ih]
    unfold wt; push_cast; ring

/-- **The braiding eigenvalue on `V_{2m−2j+1} ⊂ V_{m+1} ⊗ V_{m+1}`:**
`λ_j = s^{(m−2j)m} a_j = (−1)^j s^{m² − 4jm + 2j² − 2j}`. -/
theorem braidEigen_eq (s : 𝕜) (hs : s ≠ 0) (m j : ℕ) (hj : j ≤ m)
    (hint : ∀ i < j, qint (s ^ 2) (m - i) ≠ 0) :
    s ^ (wt m j * wt m 0) * hwCoef (s ^ 2) m m j j
      = (-1) ^ j * s ^ ((m : ℤ) ^ 2 - 4 * j * m + 2 * (j : ℤ) ^ 2 - 2 * j) := by
  have hP : ∏ i ∈ Finset.range j, qint (s ^ 2) (m - i) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun i hi => hint i (Finset.mem_range.mp hi)
  have hrefl : ∏ i ∈ Finset.range j, qint (s ^ 2) (m - j + i + 1)
      = ∏ i ∈ Finset.range j, qint (s ^ 2) (m - i) := by
    rw [← Finset.prod_range_reflect]
    refine Finset.prod_congr rfl fun i hi => ?_
    have := Finset.mem_range.mp hi
    congr 1; omega
  have hsum : ∑ i ∈ Finset.range j, wt m (j - 1 - i) = (j : ℤ) * m - (j : ℤ) * ((j : ℤ) - 1) := by
    rw [← sum_wt_range]
    exact Finset.sum_range_reflect (fun i => wt m i) j
  have hc := hwCoef_mul_prod (s ^ 2) (pow_ne_zero 2 hs) m m j j hint
  rw [hrefl, hsum] at hc
  have ha : hwCoef (s ^ 2) m m j j
      = (-1) ^ j * (s ^ 2) ^ (-((j : ℤ) * m - (j : ℤ) * ((j : ℤ) - 1))) := by
    apply mul_right_cancel₀ hP
    rw [hc]
  rw [ha, ← zpow_natCast s 2, ← zpow_mul, mul_left_comm, ← zpow_add₀ hs]
  congr 2
  unfold wt; push_cast; ring

/-! ### The double braiding (monodromy) `Ř′Ř` -/

/-- Reflection of the hook product: `Π_{i<j} [m−j+i+1] = Π_{i<j} [m−i]` for `j ≤ m`. -/
theorem prod_qint_reflect (q : 𝕜) (m j : ℕ) (hj : j ≤ m) :
    ∏ i ∈ Finset.range j, qint q (m - j + i + 1) = ∏ i ∈ Finset.range j, qint q (m - i) := by
  rw [← Finset.prod_range_reflect]
  refine Finset.prod_congr rfl fun i hi => ?_
  have := Finset.mem_range.mp hi
  congr 1; omega

/-- `Σ_{i<j} (m − 2(j−1−i)) = j m − j (j − 1)`. -/
theorem sum_wt_reflect (m j : ℕ) :
    ∑ i ∈ Finset.range j, wt m (j - 1 - i) = (j : ℤ) * m - (j : ℤ) * ((j : ℤ) - 1) := by
  rw [← sum_wt_range]
  exact Finset.sum_range_reflect (fun i => wt m i) j

/-- **Product of the two top coefficients:** `a_j(m,m') a_j(m',m) = q^{−j(m+m') + 2j(j−1)}`. -/
theorem hwCoef_pair (q : 𝕜) (hq : q ≠ 0) (m m' j : ℕ) (hjm : j ≤ m) (hjm' : j ≤ m')
    (h1 : ∀ i < j, qint q (m - i) ≠ 0) (h2 : ∀ i < j, qint q (m' - i) ≠ 0) :
    hwCoef q m m' j j * hwCoef q m' m j j
      = q ^ (-(j : ℤ) * (m + m') + 2 * j * ((j : ℤ) - 1)) := by
  have P1 : ∏ i ∈ Finset.range j, qint q (m - i) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun i hi => h1 i (Finset.mem_range.mp hi)
  have P2 : ∏ i ∈ Finset.range j, qint q (m' - i) ≠ 0 :=
    Finset.prod_ne_zero_iff.mpr fun i hi => h2 i (Finset.mem_range.mp hi)
  have c1 := hwCoef_mul_prod q hq m m' j j h1
  have c2 := hwCoef_mul_prod q hq m' m j j h2
  rw [prod_qint_reflect q m' j hjm', sum_wt_reflect] at c1
  rw [prod_qint_reflect q m j hjm, sum_wt_reflect] at c2
  apply mul_right_cancel₀ (mul_ne_zero P1 P2)
  calc hwCoef q m m' j j * hwCoef q m' m j j
        * ((∏ i ∈ Finset.range j, qint q (m - i)) * ∏ i ∈ Finset.range j, qint q (m' - i))
      = (hwCoef q m m' j j * ∏ i ∈ Finset.range j, qint q (m - i))
        * (hwCoef q m' m j j * ∏ i ∈ Finset.range j, qint q (m' - i)) := by ring
    _ = ((-1) ^ j * (-1) ^ j) * (q ^ (-((j : ℤ) * m' - j * (j - 1)))
          * q ^ (-((j : ℤ) * m - j * (j - 1))))
        * ((∏ i ∈ Finset.range j, qint q (m - i)) * ∏ i ∈ Finset.range j, qint q (m' - i)) := by
          rw [c1, c2]; ring
    _ = _ := by
          rw [← mul_pow, show ((-1 : 𝕜) * -1) = 1 by ring, one_pow, one_mul, ← zpow_add₀ hq]
          congr 2; ring

section Monodromy

variable (s : 𝕜) (hs : s ≠ 0)

/-- **The braiding** `Ř = P ∘ R : V_{m+1} ⊗ V_{m'+1} → V_{m'+1} ⊗ V_{m+1}` as a matrix. -/
def rCheckMat (m m' : ℕ) : Matrix (Fin (m' + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  (rMat s hs m m').submatrix Prod.swap id

theorem rCheckMat_mulVec (m m' : ℕ) (v : Fin (m + 1) × Fin (m' + 1) → 𝕜) :
    rCheckMat s hs m m' *ᵥ v = fun y => (rMat s hs m m' *ᵥ v) y.swap := rfl

/-- The coproduct `Δ(F) = K⁻¹ ⊗ F + F ⊗ 1` on `V_{m+1} ⊗ V_{m'+1}`. -/
def deltaF (q : 𝕜) (m m' : ℕ) : Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜 :=
  irrepKm q m ⊗ₖ irrepF q m' + irrepF q m ⊗ₖ 1

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **`Ř` is a module map for `F`:** `Ř Δ(F) = Δ(F) Ř`. -/
theorem rCheckMat_deltaF (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0) :
    rCheckMat s hs m m' * deltaF (s ^ 2) m m' = deltaF (s ^ 2) m' m * rCheckMat s hs m m' := by
  unfold rCheckMat deltaF
  rw [← submatrix_id_id (irrepKm (s ^ 2) m ⊗ₖ irrepF (s ^ 2) m' + irrepF (s ^ 2) m ⊗ₖ 1),
    ← submatrix_mul _ _ _ _ _ Function.bijective_id, rMat_F s hs hq2 m m' hint,
    submatrix_mul _ _ _ Prod.swap _ Prod.swap_bijective]
  congr 1
  ext x y
  simp only [submatrix_apply, Prod.swap, add_apply, kroneckerMap_apply, one_apply]
  ring

include hq2 in
/-- **The monodromy `Ř′Ř` commutes with `Δ(F)`.** -/
theorem monodromy_deltaF (m m' : ℕ) (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0) :
    (rCheckMat s hs m' m * rCheckMat s hs m m') * deltaF (s ^ 2) m m'
      = deltaF (s ^ 2) m m' * (rCheckMat s hs m' m * rCheckMat s hs m m') := by
  have hint' : ∀ k < rOrder m' m, qint (s ^ 2) (k + 1) ≠ 0 := by
    intro k hk; exact hint k (by unfold rOrder at *; omega)
  rw [Matrix.mul_assoc, rCheckMat_deltaF s hs hq2 m m' hint, ← Matrix.mul_assoc,
    rCheckMat_deltaF s hs hq2 m' m hint', Matrix.mul_assoc]

include hq2 in
/-- **The monodromy scalar on highest-weight vectors:**
`Ř′Ř w_j = q^{m m' − 2j(m+m') + 2j(j−1)} w_j`, `q = s²`. -/
theorem monodromy_hwVec (m m' j : ℕ) (hjm : j ≤ m) (hjm' : j ≤ m')
    (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0)
    (hint1 : ∀ p < j, qint (s ^ 2) (m - p) ≠ 0) (hint2 : ∀ p < j, qint (s ^ 2) (m' - p) ≠ 0) :
    (rCheckMat s hs m' m * rCheckMat s hs m m') *ᵥ hwVec (s ^ 2) m m' j
      = (s ^ 2) ^ ((m : ℤ) * m' - 2 * j * (m + m') + 2 * j * ((j : ℤ) - 1))
          • hwVec (s ^ 2) m m' j := by
  have hint' : ∀ k < rOrder m' m, qint (s ^ 2) (k + 1) ≠ 0 := by
    intro k hk; exact hint k (by unfold rOrder at *; omega)
  rw [← mulVec_mulVec, rCheckMat_mulVec s hs m m',
    rCheck_hwVec s hs hq2 m m' j hjm hjm' hint hint1 hint2,
    mulVec_smul, rCheckMat_mulVec s hs m' m, rCheck_hwVec s hs hq2 m' m j hjm' hjm hint' hint2 hint1,
    smul_smul]
  congr 1
  have hp := hwCoef_pair (s ^ 2) (pow_ne_zero 2 hs) m m' j hjm hjm' hint1 hint2
  calc s ^ (wt m j * wt m' 0) * hwCoef (s ^ 2) m m' j j
        * (s ^ (wt m' j * wt m 0) * hwCoef (s ^ 2) m' m j j)
      = (s ^ (wt m' j * wt m 0) * s ^ (wt m j * wt m' 0))
        * (hwCoef (s ^ 2) m m' j j * hwCoef (s ^ 2) m' m j j) := by ring
    _ = _ := by
      rw [hp, ← zpow_add₀ hs, ← zpow_natCast s 2, ← zpow_mul, ← zpow_mul, ← zpow_add₀ hs]
      congr 1
      unfold wt; push_cast; ring

include hq2 in
/-- **The monodromy is scalar on each `F`-string:** `Ř′Ř (Δ(F)^i w_j) = μ_j Δ(F)^i w_j`. -/
theorem monodromy_deltaF_pow_hwVec (m m' j i : ℕ) (hjm : j ≤ m) (hjm' : j ≤ m')
    (hint : ∀ k < rOrder m m', qint (s ^ 2) (k + 1) ≠ 0)
    (hint1 : ∀ p < j, qint (s ^ 2) (m - p) ≠ 0) (hint2 : ∀ p < j, qint (s ^ 2) (m' - p) ≠ 0) :
    (rCheckMat s hs m' m * rCheckMat s hs m m') *ᵥ (deltaF (s ^ 2) m m' ^ i *ᵥ hwVec (s ^ 2) m m' j)
      = (s ^ 2) ^ ((m : ℤ) * m' - 2 * j * (m + m') + 2 * j * ((j : ℤ) - 1))
          • (deltaF (s ^ 2) m m' ^ i *ᵥ hwVec (s ^ 2) m m' j) := by
  have hc : Commute (rCheckMat s hs m' m * rCheckMat s hs m m') (deltaF (s ^ 2) m m' ^ i) :=
    (Commute.pow_right (monodromy_deltaF s hs hq2 m m' hint) i)
  rw [mulVec_mulVec, hc.eq, ← mulVec_mulVec,
    monodromy_hwVec s hs hq2 m m' j hjm hjm' hint hint1 hint2, mulVec_smul]

end Monodromy

end QOU.Mass.QuantumSl2
