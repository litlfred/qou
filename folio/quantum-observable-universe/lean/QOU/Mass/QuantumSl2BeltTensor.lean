import QOU.Mass.QuantumSl2TwistClaspTrace

/-!
# The belt on `V_{m+1} ⊗ V_{m+1}` (van der Veen, Lemma 1, the factor `B`)

Stage 4d-ii of the derivation of Zheng's tangle formula (van der Veen 2008, Lemma 1). A belt
coloured `V_{m+1}` encircling the two parallel strands of a Whitehead-chain component acts on
`W = V_{m+1} ⊗ V_{m+1}`. On the summand `V_{2n+1} ⊂ W` it is the scalar
`B(n) = [(m+1)(2n+1)]/[2n+1]`.

The belt on a representation `ρ` with weights `w` is defined from the universal `R`-matrix
`R = q^{H⊗H/2} Σ_n c_n Eⁿ ⊗ Fⁿ` evaluated on `ρ ⊗ V_{b+1}` and `V_{b+1} ⊗ ρ`, as the partial
quantum trace of the monodromy over the belt factor. The proof has three parts.

* **Naturality.** If `φ` intertwines `E` and `F` and preserves weights, it commutes with the
  belt (`beltG_nat`).
* **Agreement on irreducibles.** On `V_{a+1}` the belt is `beltOp` of `QuantumSl2Belt`, whose
  scalar is known (`belt_eq`).
* **The string embeddings.** `p ↦ F^p w_j/[p]!` intertwines `V_{2(m−j)+1}` into `W`. This needs
  the strings to close: `Δ(F)^{2(m−j)+1} w_j = 0` (`deltaF_pow_hwVec_close`), proved from the
  injectivity of `Δ(E)` on grades above `m` (`highGrade_ker_eq_zero`).

All statements are over a generic field `𝕜`; nothing archimedean is used.
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

/-! ### Generic matrix facts -/

/-- Swapping the factors of a Kronecker product past a row swap. -/
theorem kron_mul_submatrix_swap {α α' β β' ζ : Type*} [Fintype α'] [Fintype β']
    (A : Matrix α α' 𝕜) (B : Matrix β β' 𝕜) (X : Matrix (α' × β') ζ 𝕜) :
    ((A ⊗ₖ B) * X).submatrix Prod.swap id = (B ⊗ₖ A) * X.submatrix Prod.swap id := by
  ext y z
  simp only [submatrix_apply, mul_apply, kroneckerMap_apply, Fintype.sum_prod_type, Prod.fst_swap,
    Prod.snd_swap, id]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  simp only [Prod.swap_prod_mk]
  ring

theorem submatrix_id_mul {α β γ ζ : Type*} [Fintype β] (X : Matrix α β 𝕜) (Y : Matrix β ζ 𝕜)
    (f : γ → α) : X.submatrix f id * Y = (X * Y).submatrix f id := by
  ext a c; simp [mul_apply]

namespace Rep

variable {ι ι' κ : Type*} [Fintype ι] [DecidableEq ι] [Fintype ι'] [DecidableEq ι']
  [Fintype κ] [DecidableEq κ]

/-- The truncation order of `Σ_{n ≤ M} c_n Eⁿ ⊗ Fⁿ` can be raised once the terms vanish. -/
theorem rSum_trunc (s : 𝕜) (ρ : Rep (s ^ 2) ι) (σ : Rep (s ^ 2) κ) (M M' : ℕ) (hM : M ≤ M')
    (h : ∀ n, M < n → (ρ.E ^ n) ⊗ₖ (σ.F ^ n) = 0) : rSum s ρ σ M' = rSum s ρ σ M := by
  unfold rSum
  rw [← Finset.sum_range_add_sum_Ico _ (by omega : M + 1 ≤ M' + 1)]
  rw [Finset.sum_eq_zero (s := Finset.Ico (M + 1) (M' + 1)), add_zero]
  intro n hn
  rw [Finset.mem_Ico] at hn
  rw [h n (by omega), smul_zero]

variable {q : 𝕜}

theorem pow_mul_comm_of_mul_comm (A : Matrix ι ι 𝕜) (A' : Matrix ι' ι' 𝕜) (φ : Matrix ι ι' 𝕜)
    (h : A * φ = φ * A') (n : ℕ) : A ^ n * φ = φ * A' ^ n := by
  induction n with
  | zero => simp
  | succ n ih => rw [pow_succ, Matrix.mul_assoc, h, ← Matrix.mul_assoc, ih, Matrix.mul_assoc, ← pow_succ]

/-- `Σ c_n Eⁿ ⊗ Fⁿ` is natural in its first factor for `E`-intertwiners. -/
theorem rSum_natL (s : 𝕜) (ρ : Rep (s ^ 2) ι) (ρ' : Rep (s ^ 2) ι') (σ : Rep (s ^ 2) κ)
    (φ : Matrix ι ι' 𝕜) (hE : ρ.E * φ = φ * ρ'.E) (M : ℕ) :
    rSum s ρ σ M * (φ ⊗ₖ (1 : Matrix κ κ 𝕜)) = (φ ⊗ₖ (1 : Matrix κ κ 𝕜)) * rSum s ρ' σ M := by
  unfold rSum
  rw [Matrix.sum_mul, Matrix.mul_sum]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [Matrix.smul_mul, Matrix.mul_smul, ← mul_kronecker_mul, ← mul_kronecker_mul,
    pow_mul_comm_of_mul_comm _ _ φ hE n, mul_one, one_mul]

/-- `Σ c_n Eⁿ ⊗ Fⁿ` is natural in its second factor for `F`-intertwiners. -/
theorem rSum_natR (s : 𝕜) (σ : Rep (s ^ 2) κ) (ρ : Rep (s ^ 2) ι) (ρ' : Rep (s ^ 2) ι')
    (φ : Matrix ι ι' 𝕜) (hF : ρ.F * φ = φ * ρ'.F) (M : ℕ) :
    rSum s σ ρ M * ((1 : Matrix κ κ 𝕜) ⊗ₖ φ) = ((1 : Matrix κ κ 𝕜) ⊗ₖ φ) * rSum s σ ρ' M := by
  unfold rSum
  rw [Matrix.sum_mul, Matrix.mul_sum]
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [Matrix.smul_mul, Matrix.mul_smul, ← mul_kronecker_mul, ← mul_kronecker_mul,
    pow_mul_comm_of_mul_comm _ _ φ hF n, mul_one, one_mul]

end Rep

/-! ### The belt on a weighted representation -/

section BeltGeneric

variable (s : 𝕜) (hs : s ≠ 0)
variable {ι ι' : Type*} [Fintype ι] [DecidableEq ι] [Fintype ι'] [DecidableEq ι']

/-- The Cartan factor `q^{H⊗H/2}` on `ρ ⊗ V_{b+1}`, for `ρ` with weights `w`. -/
def thetaL (w : ι → ℤ) (b : ℕ) : Matrix (ι × Fin (b + 1)) (ι × Fin (b + 1)) 𝕜 :=
  diagonal fun x => s ^ (w x.1 * wt b x.2)

/-- The Cartan factor `q^{H⊗H/2}` on `V_{b+1} ⊗ ρ`. -/
def thetaR (b : ℕ) (w : ι → ℤ) : Matrix (Fin (b + 1) × ι) (Fin (b + 1) × ι) 𝕜 :=
  diagonal fun x => s ^ (wt b x.1 * w x.2)

/-- The `R`-matrix on `ρ ⊗ V_{b+1}`. -/
def rL (ρ : Rep (s ^ 2) ι) (w : ι → ℤ) (b : ℕ) : Matrix (ι × Fin (b + 1)) (ι × Fin (b + 1)) 𝕜 :=
  thetaL s w b * Rep.rSum s ρ (irrep (pow_ne_zero 2 hs) b) b

/-- The `R`-matrix on `V_{b+1} ⊗ ρ`. -/
def rR (b : ℕ) (ρ : Rep (s ^ 2) ι) (w : ι → ℤ) : Matrix (Fin (b + 1) × ι) (Fin (b + 1) × ι) 𝕜 :=
  thetaR s b w * Rep.rSum s (irrep (pow_ne_zero 2 hs) b) ρ b

/-- The monodromy `Ř′Ř` on `ρ ⊗ V_{b+1}`. -/
def monoG (ρ : Rep (s ^ 2) ι) (w : ι → ℤ) (b : ℕ) :
    Matrix (ι × Fin (b + 1)) (ι × Fin (b + 1)) 𝕜 :=
  (rR s hs b ρ w).submatrix Prod.swap id * (rL s hs ρ w b).submatrix Prod.swap id

/-- **The belt** on `ρ`: the partial quantum trace of the monodromy over a `V_{b+1}` belt. -/
def beltG (ρ : Rep (s ^ 2) ι) (w : ι → ℤ) (b : ℕ) : Matrix ι ι 𝕜 :=
  fun i j => ∑ r : Fin (b + 1), s ^ (2 * wt b r) * monoG s hs ρ w b (i, r) (j, r)

variable (ρ : Rep (s ^ 2) ι) (ρ' : Rep (s ^ 2) ι') (w : ι → ℤ) (w' : ι' → ℤ)
  (φ : Matrix ι ι' 𝕜) (hE : ρ.E * φ = φ * ρ'.E) (hF : ρ.F * φ = φ * ρ'.F)
  (hw : ∀ i i', φ i i' ≠ 0 → w i = w' i')

include hw in
theorem thetaL_nat (b : ℕ) :
    thetaL s w b * (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜))
      = (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜)) * thetaL s w' b := by
  ext x y
  simp only [thetaL, diagonal_mul, mul_diagonal, kroneckerMap_apply]
  by_cases h : φ x.1 y.1 = 0
  · simp [h]
  rw [hw _ _ h]
  by_cases h2 : x.2 = y.2
  · rw [h2]; ring
  · simp [one_apply_ne h2]

include hw in
theorem thetaR_nat (b : ℕ) :
    thetaR s b w * ((1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜) ⊗ₖ φ)
      = ((1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜) ⊗ₖ φ) * thetaR s b w' := by
  ext x y
  simp only [thetaR, diagonal_mul, mul_diagonal, kroneckerMap_apply]
  by_cases h : φ x.2 y.2 = 0
  · simp [h]
  rw [hw _ _ h]
  by_cases h2 : x.1 = y.1
  · rw [h2]; ring
  · simp [one_apply_ne h2]

include hE hw in
theorem rL_nat (b : ℕ) :
    rL s hs ρ w b * (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜))
      = (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜)) * rL s hs ρ' w' b := by
  unfold rL
  rw [Matrix.mul_assoc, Rep.rSum_natL s ρ ρ' _ φ hE, ← Matrix.mul_assoc, thetaL_nat s w w' φ hw,
    Matrix.mul_assoc]

include hF hw in
theorem rR_nat (b : ℕ) :
    rR s hs b ρ w * ((1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜) ⊗ₖ φ)
      = ((1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜) ⊗ₖ φ) * rR s hs b ρ' w' := by
  unfold rR
  rw [Matrix.mul_assoc, Rep.rSum_natR s _ ρ ρ' φ hF, ← Matrix.mul_assoc, thetaR_nat s w w' φ hw,
    Matrix.mul_assoc]

include hE hF hw in
/-- **Naturality of the monodromy.** -/
theorem monoG_nat (b : ℕ) :
    monoG s hs ρ w b * (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜))
      = (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜)) * monoG s hs ρ' w' b := by
  unfold monoG
  rw [Matrix.mul_assoc, submatrix_id_mul (rL s hs ρ w b), rL_nat s hs ρ ρ' w w' φ hE hw, kron_mul_submatrix_swap,
    ← Matrix.mul_assoc, submatrix_id_mul (rR s hs b ρ w), rR_nat s hs ρ ρ' w w' φ hF hw, kron_mul_submatrix_swap,
    Matrix.mul_assoc]

include hE hF hw in
/-- **Naturality of the belt.** -/
theorem beltG_nat (b : ℕ) : beltG s hs ρ w b * φ = φ * beltG s hs ρ' w' b := by
  ext i j
  simp only [mul_apply, beltG, Finset.sum_mul, Finset.mul_sum]
  conv_lhs => rw [Finset.sum_comm]
  conv_rhs => rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun r _ => ?_
  have key : (monoG s hs ρ w b * (φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜))) (i, r) (j, r)
      = ((φ ⊗ₖ (1 : Matrix (Fin (b + 1)) (Fin (b + 1)) 𝕜)) * monoG s hs ρ' w' b) (i, r) (j, r) := by
    rw [monoG_nat s hs ρ ρ' w w' φ hE hF hw b]
  simp only [mul_apply, Fintype.sum_prod_type, kroneckerMap_apply, one_apply, mul_ite, mul_one,
    mul_zero, ite_mul, zero_mul, Finset.sum_ite_eq', Finset.sum_ite_eq, Finset.mem_univ,
    if_true] at key
  simp_rw [mul_assoc, mul_left_comm (φ _ _)]
  rw [← Finset.mul_sum, ← Finset.mul_sum, key]

end BeltGeneric

/-! ### Agreement with `beltOp` on irreducibles -/

section Irreducible

variable (s : 𝕜) (hs : s ≠ 0)

theorem rL_irrep (a b : ℕ) :
    rL s hs (irrep (pow_ne_zero 2 hs) a) (fun p => wt a p) b = rMat s hs a b := by
  unfold rL rMat
  congr 1
  refine (Rep.rSum_trunc s _ _ b (rOrder a b) (le_max_right a b) fun n hn => ?_).symm
  have : irrepF (s ^ 2) b ^ n = 0 := pow_eq_zero_of_le (by omega) (irrepF_pow_nil (s ^ 2) b)
  show (irrepE (s ^ 2) a ^ n) ⊗ₖ (irrepF (s ^ 2) b ^ n) = 0
  rw [this, kronecker_zero]

theorem rR_irrep (a b : ℕ) :
    rR s hs b (irrep (pow_ne_zero 2 hs) a) (fun p => wt a p) = rMat s hs b a := by
  unfold rR rMat
  congr 1
  refine (Rep.rSum_trunc s _ _ b (rOrder b a) (le_max_left b a) fun n hn => ?_).symm
  have : irrepE (s ^ 2) b ^ n = 0 := pow_eq_zero_of_le (by omega) (irrepE_pow_nil (s ^ 2) b)
  show (irrepE (s ^ 2) b ^ n) ⊗ₖ (irrepF (s ^ 2) a ^ n) = 0
  rw [this, zero_kronecker]

theorem monoG_irrep (a b : ℕ) :
    monoG s hs (irrep (pow_ne_zero 2 hs) a) (fun p => wt a p) b = mono s hs a b := by
  unfold monoG mono rCheckMat
  rw [rL_irrep, rR_irrep]

/-- On `V_{a+1}` the belt is `beltOp` of `QuantumSl2Belt`. -/
theorem beltG_irrep (a b : ℕ) :
    beltG s hs (irrep (pow_ne_zero 2 hs) a) (fun p => wt a p) b = beltOp s hs a b := by
  funext i j
  simp only [beltG, beltOp, monoG_irrep]

end Irreducible

/-! ### The strings close -/

section Close

variable (q : 𝕜) (hq : q ≠ 0) (m : ℕ)

include hq in
/-- `Δ(E)` is injective on the grades above `m` of `V_{m+1} ⊗ V_{m+1}`. -/
theorem highGrade_ker_eq_zero (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) (g : ℕ) (hg : m < g)
    (u : Fin (m + 1) × Fin (m + 1) → 𝕜) (hu : InGrade m g u)
    (hE : (irrepE q m ⊗ₖ irrepKp q m + 1 ⊗ₖ irrepE q m) *ᵥ u = 0) : u = 0 := by
  by_cases hg2 : 2 * m < g
  · funext x; exact hu x (by omega)
  push_neg at hg2
  have key : ∀ k p (hp : p < m + 1) (hr : g - p < m + 1), p = g - m + k →
      u (⟨p, hp⟩, ⟨g - p, hr⟩) = 0 := by
    intro k
    induction k with
    | zero =>
      intro p hp hr hpk
      have h := congrFun hE (⟨g - m - 1, by omega⟩, ⟨m, by omega⟩)
      rw [dE_apply q hq, dif_pos (by omega), dif_neg (by omega), add_zero, Pi.zero_apply] at h
      have e : u (⟨g - m - 1 + 1, by omega⟩, ⟨m, by omega⟩) = u (⟨p, hp⟩, ⟨g - p, hr⟩) := by
        congr 3 <;> omega
      rw [e] at h
      have h1 : qint q (m - (g - m - 1)) ≠ 0 := hint _ (by omega) (by omega)
      have h2 : q ^ wt m m ≠ 0 := zpow_ne_zero _ hq
      exact (mul_eq_zero.mp h).resolve_left (mul_ne_zero h1 h2)
    | succ k ih =>
      intro p hp hr hpk
      have h := congrFun hE (⟨p - 1, by omega⟩, ⟨g - p, by omega⟩)
      rw [dE_apply q hq, dif_pos (by omega), dif_pos (by omega), Pi.zero_apply] at h
      have e1 : u (⟨p - 1 + 1, by omega⟩, ⟨g - p, by omega⟩) = u (⟨p, hp⟩, ⟨g - p, hr⟩) := by
        congr 3; omega
      have e2 : u (⟨p - 1, by omega⟩, ⟨g - p + 1, by omega⟩) = 0 := by
        have := ih (p - 1) (by omega) (by omega) (by omega)
        rw [← this]; congr 3; omega
      rw [e1, e2, mul_zero, add_zero] at h
      have h1 : qint q (m - (p - 1)) ≠ 0 := hint _ (by omega) (by omega)
      have h2 : q ^ wt m (g - p) ≠ 0 := zpow_ne_zero _ hq
      exact (mul_eq_zero.mp h).resolve_left (mul_ne_zero h1 h2)
  funext ⟨⟨p, hp⟩, ⟨r, hr⟩⟩
  by_cases hpr : p + r = g
  · have := key (p - (g - m)) p hp (by omega) (by omega)
    rw [Pi.zero_apply, ← this]; congr 3; omega
  · exact hu _ (by dsimp only; omega)

variable (hq2 : q - q⁻¹ ≠ 0)

include hq hq2 in
/-- **The strings close**: `Δ(F)^{2(m−j)+1} w_j = 0`. -/
theorem deltaF_pow_hwVec_close (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0) (j : ℕ) (hj : j ≤ m) :
    deltaF q m m ^ (2 * (m - j) + 1) *ᵥ hwVec q m m j = 0 := by
  have hEw : (tens q hq m).E *ᵥ hwVec q m m j = 0 :=
    hwVec_E q hq m m j hj hj (fun p hp => hint _ (by omega) (by omega))
  have hKw : (tens q hq m).Kp *ᵥ hwVec q m m j = q ^ (2 * (m - j)) • hwVec q m m j :=
    deltaK_hwVec q hq m j hj
  have h := Rep.E_F_succ_hw hq hq2 (tens q hq m) (hwVec q m m j) (2 * (m - j)) hEw hKw
    (2 * (m - j))
  have hz : strSc q (2 * (m - j)) (2 * (m - j)) = 0 := by unfold strSc; ring
  rw [hz, zero_smul, tens_F] at h
  refine highGrade_ker_eq_zero q hq m hint (j + (2 * (m - j) + 1)) (by omega) _
    (inGrade_strVec q m j _) ?_
  rw [← tens_E q hq m]; exact h

end Close

/-! ### The string embedding `V_{2(m−j)+1} → V_{m+1} ⊗ V_{m+1}` -/

section Embedding

variable (q : 𝕜) (hq : q ≠ 0) (hq2 : q - q⁻¹ ≠ 0) (m : ℕ)

/-- The weights `(m−2p) + (m−2r)` of `V_{m+1} ⊗ V_{m+1}`. -/
def tensWt (x : Fin (m + 1) × Fin (m + 1)) : ℤ := wt m x.1 + wt m x.2

/-- The embedding `e_p ↦ Δ(F)^p w_j / [p]!` of `V_{2(m−j)+1}`. -/
def strEmb (j : ℕ) : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (2 * (m - j) + 1)) 𝕜 :=
  fun x p => (qfact q p)⁻¹ * (deltaF q m m ^ (p : ℕ) *ᵥ hwVec q m m j) x

theorem mul_apply_eq_mulVec {α β γ : Type*} [Fintype β] (A : Matrix α β 𝕜) (B : Matrix β γ 𝕜)
    (x : α) (p : γ) : (A * B) x p = (A *ᵥ fun y => B y p) x := rfl

theorem strEmb_col (j : ℕ) (p : Fin (2 * (m - j) + 1)) :
    (fun y => strEmb q m j y p) = (qfact q p)⁻¹ • (deltaF q m m ^ (p : ℕ) *ᵥ hwVec q m m j) := by
  funext y; simp [strEmb]

theorem qfact_ne_zero (n : ℕ) (h : ∀ i, 0 < i → i ≤ n → qint q i ≠ 0) : qfact q n ≠ 0 := by
  unfold qfact
  exact Finset.prod_ne_zero_iff.mpr fun k hk => h _ (by omega) (by simp at hk; omega)

include hq hq2 in
theorem strEmb_E (hint : ∀ i, 0 < i → i ≤ 2 * m → qint q i ≠ 0) (j : ℕ) (hj : j ≤ m) :
    (tens q hq m).E * strEmb q m j = strEmb q m j * (irrep hq (2 * (m - j))).E := by
  have hEw : (tens q hq m).E *ᵥ hwVec q m m j = 0 :=
    hwVec_E q hq m m j hj hj (fun p hp => hint _ (by omega) (by omega))
  have hKw : (tens q hq m).Kp *ᵥ hwVec q m m j = q ^ (2 * (m - j)) • hwVec q m m j :=
    deltaK_hwVec q hq m j hj
  ext x ⟨p, hp⟩
  rw [mul_apply_eq_mulVec, strEmb_col, mulVec_smul]
  simp only [irrep, mul_apply, irrepE, mul_ite, mul_zero]
  rcases p with _ | p
  · simp only [pow_zero, one_mulVec] at *
    rw [hEw, smul_zero, Pi.zero_apply]
    symm
    exact Finset.sum_eq_zero fun k _ => if_neg (by omega)
  · have h := Rep.E_F_succ_hw hq hq2 (tens q hq m) (hwVec q m m j) (2 * (m - j)) hEw hKw p
    rw [tens_F] at h
    rw [h, strSc_eq q hq _ _ (by omega), Finset.sum_eq_single ⟨p, by omega⟩]
    · simp only [strEmb, Pi.smul_apply, smul_eq_mul]
      rw [if_pos (by simp)]
      have hp1 : qint q (p + 1) ≠ 0 := hint _ (by omega) (by omega)
      rw [qfact_succ q, show 2 * (m - j) - (p + 1) + 1 = 2 * (m - j) - p by omega]
      field_simp
    · intro k _ hk
      rw [if_neg]
      intro h'; exact hk (Fin.ext (by simp at h'; omega))
    · simp

include hq hq2 in
theorem strEmb_F (hint : ∀ i, 0 < i → i ≤ 2 * m → qint q i ≠ 0) (j : ℕ) (hj : j ≤ m) :
    (tens q hq m).F * strEmb q m j = strEmb q m j * (irrep hq (2 * (m - j))).F := by
  ext x ⟨p, hp⟩
  rw [mul_apply_eq_mulVec, strEmb_col, mulVec_smul, tens_F, mulVec_mulVec, ← pow_succ']
  simp only [irrep, mul_apply, irrepF, mul_ite, mul_zero]
  by_cases hpN : p + 1 ≤ 2 * (m - j)
  · rw [Finset.sum_eq_single ⟨p + 1, by omega⟩]
    · simp only [strEmb, Pi.smul_apply, smul_eq_mul]
      rw [if_pos (by simp)]
      have hp1 : qint q (p + 1) ≠ 0 := hint _ (by omega) (by omega)
      rw [qfact_succ q]
      field_simp
    · intro k _ hk
      rw [if_neg]
      intro h'; exact hk (Fin.ext (by simpa using h'))
    · simp
  · have hp' : p = 2 * (m - j) := by omega
    subst hp'
    rw [deltaF_pow_hwVec_close q hq m hq2 (fun i h1 h2 => hint i h1 (by omega)) j hj, smul_zero,
      Pi.zero_apply]
    symm
    exact Finset.sum_eq_zero fun k _ => if_neg (by omega)

theorem strEmb_wt (j : ℕ) (hj : j ≤ m) (x : Fin (m + 1) × Fin (m + 1)) (p : Fin (2 * (m - j) + 1))
    (h : strEmb q m j x p ≠ 0) : tensWt m x = (fun p : Fin (2 * (m - j) + 1) => wt (2 * (m - j)) p) p := by
  have hx : (x.1 : ℕ) + x.2 = j + p := by
    by_contra hne
    apply h
    simp only [strEmb, inGrade_strVec q m j p x hne, mul_zero]
  simp only [tensWt, wt]
  omega

end Embedding

/-! ### The belt on `V_{m+1} ⊗ V_{m+1}` -/

section BeltTensor

variable (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (m : ℕ)
  (hint : ∀ i, 0 < i → i ≤ 2 * m + 1 → qint (s ^ 2) i ≠ 0)

/-- **The belt on `V_{m+1} ⊗ V_{m+1}`** with a `V_{m+1}` belt. -/
def beltW : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  beltG s hs (tens (s ^ 2) (pow_ne_zero 2 hs) m) (tensWt m) m

/-- The belt scalar on `V_{2n+1}`, `n = m − j`: `[(2n+1)(m+1)]/[2n+1]` (Zheng's `B(n)`). -/
def beltSc (j : ℕ) : 𝕜 :=
  qint (s ^ 2) ((2 * (m - j) + 1) * (m + 1)) / qint (s ^ 2) (2 * (m - j) + 1)

include hq2 hint in
theorem beltW_strVec (x : StrIdx m) :
    beltW s hs m *ᵥ strVec (s ^ 2) m x = beltSc s m x.1 • strVec (s ^ 2) m x := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hjm : (x.1 : ℕ) ≤ m := by omega
  have hint' : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  -- naturality along the string embedding
  have hnat := beltG_nat s hs (tens (s ^ 2) hq m) (irrep hq (2 * (m - x.1))) (tensWt m)
    (fun p : Fin (2 * (m - x.1) + 1) => wt (2 * (m - x.1)) p) (strEmb (s ^ 2) m x.1)
    (strEmb_E (s ^ 2) hq hq2 m hint' x.1 hjm) (strEmb_F (s ^ 2) hq hq2 m hint' x.1 hjm)
    (fun y p h => strEmb_wt (s ^ 2) m x.1 hjm y p h) m
  rw [beltG_irrep] at hnat
  have hbelt := belt_eq s hs hq2 (2 * (m - x.1)) m (fun k hk => hint _ (by omega)
    (by simp only [rOrder] at hk; omega)) (fun k hk => hint _ (by omega) (by omega))
  have hN : qint (s ^ 2) (2 * (m - x.1) + 1) ≠ 0 := hint _ (by omega) (by omega)
  have h1 : qint (s ^ 2) (2 * (m - x.1) + 1) • (beltW s hs m * strEmb (s ^ 2) m x.1)
      = qint (s ^ 2) ((2 * (m - x.1) + 1) * (m + 1)) • strEmb (s ^ 2) m x.1 := by
    rw [beltW, hnat, ← Matrix.mul_smul, hbelt, Matrix.mul_smul, Matrix.mul_one]
  have h2 : qint (s ^ 2) (2 * (m - x.1) + 1)
        • ((qfact (s ^ 2) x.2)⁻¹ • (beltW s hs m *ᵥ strVec (s ^ 2) m x))
      = qint (s ^ 2) ((2 * (m - x.1) + 1) * (m + 1))
        • ((qfact (s ^ 2) x.2)⁻¹ • strVec (s ^ 2) m x) := by
    rw [strVec, ← mulVec_smul, ← strEmb_col]
    funext y
    have := congrArg (fun A : Matrix _ _ 𝕜 => A y x.2) h1
    simpa only [Matrix.smul_apply, mul_apply_eq_mulVec, Pi.smul_apply] using this
  have hpf : (qfact (s ^ 2) x.2)⁻¹ ≠ 0 :=
    inv_ne_zero (qfact_ne_zero (s ^ 2) _ fun i h1 h2 => hint _ h1 (by omega))
  rw [smul_smul, smul_smul, mul_comm _ ((qfact (s ^ 2) x.2)⁻¹),
    mul_comm _ ((qfact (s ^ 2) x.2)⁻¹), ← smul_smul, ← smul_smul] at h2
  have h3 := smul_right_injective _ hpf h2
  simp only at h3
  unfold beltSc
  rw [div_eq_inv_mul, ← smul_smul, ← h3, smul_smul, inv_mul_cancel₀ hN, one_smul]

include hq2 hint in
/-- **Zheng's sum for twists, belts and clasps.** -/
theorem trace_twist_belt_clasp (a b c : ℕ) :
    trace (deltaK (s ^ 2) m m * (twist0 s hs m ^ a * beltW s hs m ^ b * clasp s hs m ^ c))
      = ∑ j : Fin (m + 1), twistSc s m j ^ a * beltSc s m j ^ b * claspSc s m j ^ c
          * qint (s ^ 2) (2 * (m - j) + 1) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hint' : ∀ i, 0 < i → i ≤ 2 * m → qint (s ^ 2) i ≠ 0 := fun i h1 h2 => hint i h1 (by omega)
  refine trace_deltaK_mul (s ^ 2) hq m hq2 hint' _
    (fun j => twistSc s m j ^ a * beltSc s m j ^ b * claspSc s m j ^ c) fun x => ?_
  rw [← mulVec_mulVec, mulVec_pow_of_eigen m _ _ _ (clasp_strVec s hs hq2 m hint' x) c,
    mulVec_smul, ← mulVec_mulVec, mulVec_pow_of_eigen m _ _ _ (beltW_strVec s hs hq2 m hint x) b,
    mulVec_smul, mulVec_pow_of_eigen m _ _ _ (twist0_strVec s hs hq2 m hint' x) a, smul_smul,
    smul_smul]
  congr 1
  ring

end BeltTensor

end QOU.Mass.QuantumSl2
