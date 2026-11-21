import QOU.Mass.QuantumSl2YangBaxter
import QOU.Mass.QuantumSl2HighestWeight

/-!
# The hexagon identity and the Yang–Baxter equation for the `U_q(sl₂)` R-matrix

Stage 1 of issue #8894. On `V ⊗ V ⊗ V` with `V = V_{m+1}` we prove

* `R₁₃ R₂₃ = Θ₁₃ Θ₂₃ Σ_n c_n Δ(E)ⁿ ⊗ Fⁿ`, i.e. `(Δ ⊗ 1) R = R₁₃ R₂₃`;
* `R₂₃ R₁₃ = Θ₁₃ Θ₂₃ Σ_n c_n Δ^{op}(E)ⁿ ⊗ Fⁿ`, i.e. `(Δ^{op} ⊗ 1) R = R₂₃ R₁₃`;
* the Yang–Baxter equation `R₁₂ R₁₃ R₂₃ = R₂₃ R₁₃ R₁₂`;
* the braid relation `Ř₁ Ř₂ Ř₁ = Ř₂ Ř₁ Ř₂` for `Ř = P R` (`rCheckMat`).

The two hexagon identities come from the q-exponential product formula `qexp_mul` after moving
the Cartan factors to the left; Yang–Baxter then follows from `R Δ(E) = Δ^{op}(E) R`.
Everything is exact algebra over a field `𝕜`; the hypotheses are `s ≠ 0`, `q − q⁻¹ ≠ 0` and
`[k]_q ≠ 0` for `1 ≤ k ≤ 2m` (`q = s²`).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VIII.2–VIII.3 (hexagon, Yang–Baxter)
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

set_option linter.unusedSectionVars false

variable {𝕜 : Type*} [Field 𝕜]

/-! ### Legs of a two-tensor on a triple tensor product -/

section Legs

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- `((a, b), c) ↦ ((b, a), c)`: exchange the first two factors. -/
def swap12 (ι : Type*) : (ι × ι) × ι ≃ (ι × ι) × ι where
  toFun x := ((x.1.2, x.1.1), x.2)
  invFun x := ((x.1.2, x.1.1), x.2)
  left_inv _ := rfl
  right_inv _ := rfl

/-- `((a, b), c) ↦ ((a, c), b)`: exchange the last two factors. -/
def swap23 (ι : Type*) : (ι × ι) × ι ≃ (ι × ι) × ι where
  toFun x := ((x.1.1, x.2), x.1.2)
  invFun x := ((x.1.1, x.2), x.1.2)
  left_inv _ := rfl
  right_inv _ := rfl

/-- `A₁₂ = A ⊗ 1`. -/
def leg12 (A : Matrix (ι × ι) (ι × ι) 𝕜) : Matrix ((ι × ι) × ι) ((ι × ι) × ι) 𝕜 :=
  A ⊗ₖ (1 : Matrix ι ι 𝕜)

/-- `A₁₃`: `A` on the first and third factors. -/
def leg13 (A : Matrix (ι × ι) (ι × ι) 𝕜) : Matrix ((ι × ι) × ι) ((ι × ι) × ι) 𝕜 :=
  (leg12 A).submatrix (swap23 ι) (swap23 ι)

/-- `A₂₃`: `A` on the second and third factors. -/
def leg23 (A : Matrix (ι × ι) (ι × ι) 𝕜) : Matrix ((ι × ι) × ι) ((ι × ι) × ι) 𝕜 :=
  (leg13 A).submatrix (swap12 ι) (swap12 ι)

theorem leg12_apply (A : Matrix (ι × ι) (ι × ι) 𝕜) (x y : (ι × ι) × ι) :
    leg12 A x y = A x.1 y.1 * (1 : Matrix ι ι 𝕜) x.2 y.2 := rfl

theorem leg13_apply (A : Matrix (ι × ι) (ι × ι) 𝕜) (x y : (ι × ι) × ι) :
    leg13 A x y = A (x.1.1, x.2) (y.1.1, y.2) * (1 : Matrix ι ι 𝕜) x.1.2 y.1.2 := rfl

theorem leg23_apply (A : Matrix (ι × ι) (ι × ι) 𝕜) (x y : (ι × ι) × ι) :
    leg23 A x y = A (x.1.2, x.2) (y.1.2, y.2) * (1 : Matrix ι ι 𝕜) x.1.1 y.1.1 := rfl

theorem leg12_mul (A B : Matrix (ι × ι) (ι × ι) 𝕜) : leg12 (A * B) = leg12 A * leg12 B := by
  unfold leg12; rw [← mul_kronecker_mul, one_mul]

theorem leg13_mul (A B : Matrix (ι × ι) (ι × ι) 𝕜) : leg13 (A * B) = leg13 A * leg13 B := by
  unfold leg13; rw [leg12_mul, submatrix_mul_equiv]

theorem leg23_mul (A B : Matrix (ι × ι) (ι × ι) 𝕜) : leg23 (A * B) = leg23 A * leg23 B := by
  unfold leg23; rw [leg13_mul, submatrix_mul_equiv]

theorem leg13_kron (B C : Matrix ι ι 𝕜) : leg13 (B ⊗ₖ C) = (B ⊗ₖ (1 : Matrix ι ι 𝕜)) ⊗ₖ C := by
  ext x y
  simp only [leg13_apply, kroneckerMap_apply]
  ring

theorem leg23_kron (B C : Matrix ι ι 𝕜) : leg23 (B ⊗ₖ C) = ((1 : Matrix ι ι 𝕜) ⊗ₖ B) ⊗ₖ C := by
  ext x y
  simp only [leg23_apply, kroneckerMap_apply]
  ring

theorem leg13_sum {S : Finset ℕ} (c : ℕ → 𝕜) (B C : ℕ → Matrix ι ι 𝕜) :
    leg13 (∑ n ∈ S, c n • (B n ⊗ₖ C n))
      = ∑ n ∈ S, c n • ((B n ⊗ₖ (1 : Matrix ι ι 𝕜)) ⊗ₖ C n) := by
  ext x y
  simp only [leg13_apply, sum_apply, smul_apply, kroneckerMap_apply, smul_eq_mul, Finset.sum_mul]
  refine Finset.sum_congr rfl fun n _ => ?_
  ring

theorem leg23_sum {S : Finset ℕ} (c : ℕ → 𝕜) (B C : ℕ → Matrix ι ι 𝕜) :
    leg23 (∑ n ∈ S, c n • (B n ⊗ₖ C n))
      = ∑ n ∈ S, c n • (((1 : Matrix ι ι 𝕜) ⊗ₖ B n) ⊗ₖ C n) := by
  ext x y
  simp only [leg23_apply, sum_apply, smul_apply, kroneckerMap_apply, smul_eq_mul, Finset.sum_mul]
  refine Finset.sum_congr rfl fun n _ => ?_
  ring

theorem leg13_diagonal (d : ι × ι → 𝕜) :
    leg13 (diagonal d) = diagonal fun x : (ι × ι) × ι => d (x.1.1, x.2) := by
  unfold leg13 leg12
  rw [← diagonal_one, diagonal_kronecker_diagonal, submatrix_diagonal_equiv]
  congr 1; funext x; simp [swap23]

theorem leg23_diagonal (d : ι × ι → 𝕜) :
    leg23 (diagonal d) = diagonal fun x : (ι × ι) × ι => d (x.1.2, x.2) := by
  unfold leg23
  rw [leg13_diagonal, submatrix_diagonal_equiv]
  rfl

theorem kron_pow {κ : Type*} [Fintype κ] [DecidableEq κ] (B : Matrix ι ι 𝕜) (C : Matrix κ κ 𝕜)
    (n : ℕ) : (B ⊗ₖ C) ^ n = (B ^ n) ⊗ₖ (C ^ n) := by
  induction n with
  | zero => simp
  | succ n ih => rw [pow_succ, ih, ← mul_kronecker_mul, ← pow_succ, ← pow_succ]

/-! #### Conjugating legs by the factor swaps -/

theorem leg12_conj23 (A : Matrix (ι × ι) (ι × ι) 𝕜) :
    (leg12 A).submatrix (swap23 ι) (swap23 ι) = leg13 A := rfl

theorem leg13_conj23 (A : Matrix (ι × ι) (ι × ι) 𝕜) :
    (leg13 A).submatrix (swap23 ι) (swap23 ι) = leg12 A := rfl

theorem leg13_conj12 (A : Matrix (ι × ι) (ι × ι) 𝕜) :
    (leg13 A).submatrix (swap12 ι) (swap12 ι) = leg23 A := rfl

theorem leg23_conj12 (A : Matrix (ι × ι) (ι × ι) 𝕜) :
    (leg23 A).submatrix (swap12 ι) (swap12 ι) = leg13 A := rfl

/-- Moving a row permutation through a product, for an involutive `g`. -/
theorem sub_mul_sub {T : Type*} [Fintype T] [DecidableEq T] (X Z : Matrix T T 𝕜) (φ : T → T)
    (g : T ≃ T) (hg : ∀ x, g (g x) = x) :
    X.submatrix φ id * Z.submatrix g id = ((X.submatrix g g) * Z).submatrix (g ∘ φ) id := by
  ext x z
  simp only [mul_apply, submatrix_apply, id, Function.comp_apply, hg]
  exact Fintype.sum_equiv g _ _ fun y => by simp [hg]

theorem triple_sub {T : Type*} [Fintype T] [DecidableEq T] (A B C : Matrix T T 𝕜)
    (f g h : T ≃ T) (hg : ∀ x, g (g x) = x) (hh : ∀ x, h (h x) = x) :
    A.submatrix f id * B.submatrix g id * C.submatrix h id
      = (((A.submatrix g g) * B).submatrix h h * C).submatrix (h ∘ g ∘ f) id := by
  rw [sub_mul_sub A B f g hg, sub_mul_sub _ C _ h hh]

end Legs

/-! ### The hexagon on `V_{m+1}^{⊗3}` -/

section Hexagon

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ)

/-- The triple tensor power `(V ⊗ V) ⊗ V` of `V = V_{m+1}`, as an index type. -/
abbrev Tri (m : ℕ) := (Fin (m + 1) × Fin (m + 1)) × Fin (m + 1)

/-- `Θ₁₃ Θ₂₃ = q^{(H ⊗ 1 + 1 ⊗ H) ⊗ H / 2}`: `v_p ⊗ v_r ⊗ v_t ↦ s^{(wt p + wt r) wt t}`. -/
def theta123 : Matrix (Tri m) (Tri m) 𝕜 :=
  diagonal fun x => s ^ ((wt m x.1.1 + wt m x.1.2) * wt m x.2)

theorem leg13_cartanTheta :
    leg13 (cartanTheta s m m) = diagonal fun x : Tri m => s ^ (wt m x.1.1 * wt m x.2) := by
  unfold cartanTheta; rw [leg13_diagonal]

theorem leg23_cartanTheta :
    leg23 (cartanTheta s m m) = diagonal fun x : Tri m => s ^ (wt m x.1.2 * wt m x.2) := by
  unfold cartanTheta; rw [leg23_diagonal]

include hs in
theorem theta13_mul_theta23 :
    leg13 (cartanTheta s m m) * leg23 (cartanTheta s m m) = theta123 s m := by
  rw [leg13_cartanTheta, leg23_cartanTheta, diagonal_mul_diagonal, theta123]
  congr 1; funext x; rw [← zpow_add₀ hs]; ring_nf

include hs in
theorem theta23_mul_theta13 :
    leg23 (cartanTheta s m m) * leg13 (cartanTheta s m m) = theta123 s m := by
  rw [leg13_cartanTheta, leg23_cartanTheta, diagonal_mul_diagonal, theta123]
  congr 1; funext x; rw [← zpow_add₀ hs]; ring_nf

include hs in
/-- `Kᵃ v_r = s^{2a·wt r} v_r`. -/
theorem irrepKp_pow_apply (a : ℕ) (r r' : Fin (m + 1)) :
    (irrepKp (s ^ 2) m ^ a) r r' = if r = r' then s ^ (2 * wt m r * a) else 0 := by
  rw [irrepKp, diagonal_pow, diagonal_apply]
  split_ifs
  · simp only [Pi.pow_apply]
    rw [irrepKp_diag_eq s hs (Nat.lt_succ_iff.mp r.isLt), ← zpow_natCast, ← zpow_mul]
  · rfl

include hs in
/-- Moving `Θ₂₃` left through `B ⊗ 1 ⊗ Fᵃ` produces `B ⊗ Kᵃ ⊗ Fᵃ`. -/
theorem conj23_F (B : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) (a : ℕ) :
    ((B ⊗ₖ (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜)) ⊗ₖ (irrepF (s ^ 2) m ^ a))
        * leg23 (cartanTheta s m m)
      = leg23 (cartanTheta s m m)
        * ((B ⊗ₖ (irrepKp (s ^ 2) m ^ a)) ⊗ₖ (irrepF (s ^ 2) m ^ a)) := by
  rw [leg23_cartanTheta]
  ext ⟨⟨p, r⟩, t⟩ ⟨⟨p', r'⟩, t'⟩
  simp only [mul_diagonal, diagonal_mul, kroneckerMap_apply, one_apply, irrepKp_pow_apply s hs]
  by_cases hr : r = r'
  · subst hr
    by_cases ht : (t : ℕ) = t' + a
    · have h : s ^ (wt m r * wt m t') = s ^ (wt m r * wt m t) * s ^ (2 * wt m r * a) := by
        rw [← zpow_add₀ hs]; congr 1; unfold wt; rw [ht]; push_cast; ring
      simp only [if_true, h]; ring
    · rw [irrepF_pow_apply _ m a t t' ht]; ring
  · simp [hr]

include hs in
/-- Moving `Θ₁₃` left through `1 ⊗ B ⊗ Fᵃ` produces `Kᵃ ⊗ B ⊗ Fᵃ`. -/
theorem conj13_F (B : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) (a : ℕ) :
    (((1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) ⊗ₖ B) ⊗ₖ (irrepF (s ^ 2) m ^ a))
        * leg13 (cartanTheta s m m)
      = leg13 (cartanTheta s m m)
        * (((irrepKp (s ^ 2) m ^ a) ⊗ₖ B) ⊗ₖ (irrepF (s ^ 2) m ^ a)) := by
  rw [leg13_cartanTheta]
  ext ⟨⟨p, r⟩, t⟩ ⟨⟨p', r'⟩, t'⟩
  simp only [mul_diagonal, diagonal_mul, kroneckerMap_apply, one_apply, irrepKp_pow_apply s hs]
  by_cases hp : p = p'
  · subst hp
    by_cases ht : (t : ℕ) = t' + a
    · have h : s ^ (wt m p * wt m t') = s ^ (wt m p * wt m t) * s ^ (2 * wt m p * a) := by
        rw [← zpow_add₀ hs]; congr 1; unfold wt; rw [ht]; push_cast; ring
      simp only [if_true, h]; ring
    · rw [irrepF_pow_apply _ m a t t' ht]; ring
  · simp [hp]

theorem rSum_irrep :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m) (rOrder m m)
      = ∑ n ∈ Finset.range (m + 1), rcoef s n • ((irrepE (s ^ 2) m ^ n) ⊗ₖ (irrepF (s ^ 2) m ^ n)) := by
  unfold rOrder; rw [max_self]; rfl

end Hexagon

/-! ### The two hexagon identities -/

section HexagonMain

variable (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0) (m : ℕ)

local notation "𝔼" => irrepE (s ^ 2) m
local notation "𝔽" => irrepF (s ^ 2) m
local notation "𝕂" => irrepKp (s ^ 2) m
local notation "𝟙" => (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜)

include hs in
theorem irrepE_mul_Kp : 𝔼 * 𝕂 = ((s ^ 2)⁻¹ ^ 2) • (𝕂 * 𝔼) :=
  Rep.E_Kp (pow_ne_zero 2 hs) (irrep (pow_ne_zero 2 hs) m)

include hs hq2 in
/-- **Hexagon, `(Δ ⊗ 1) R = R₁₃ R₂₃`.** On `V_{m+1}^{⊗3}`,
`R₁₃ R₂₃ = Θ₁₃ Θ₂₃ Σ_{n ≤ 2m} c_n Δ(E)ⁿ ⊗ Fⁿ` with `Δ(E) = E ⊗ K + 1 ⊗ E`. -/
theorem hexagon_13_23 (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    leg13 (rMat s hs m m) * leg23 (rMat s hs m m)
      = theta123 s m * ∑ n ∈ Finset.range (2 * m + 1),
          rcoef s n • (((𝔼 ⊗ₖ 𝕂 + 𝟙 ⊗ₖ 𝔼) ^ n) ⊗ₖ (𝔽 ^ n)) := by
  have h13 : leg13 (rMat s hs m m) = leg13 (cartanTheta s m m)
      * ∑ a ∈ Finset.range (m + 1), rcoef s a • (((𝔼 ^ a) ⊗ₖ 𝟙) ⊗ₖ (𝔽 ^ a)) := by
    unfold rMat; rw [leg13_mul, rSum_irrep s hs m, leg13_sum]
  have h23 : leg23 (rMat s hs m m) = leg23 (cartanTheta s m m)
      * ∑ b ∈ Finset.range (m + 1), rcoef s b • ((𝟙 ⊗ₖ 𝔼) ⊗ₖ 𝔽) ^ b := by
    unfold rMat; rw [leg23_mul, rSum_irrep s hs m, leg23_sum]
    congr 1; refine Finset.sum_congr rfl fun b _ => ?_
    rw [kron_pow, kron_pow, one_pow]
  have hmove : (∑ a ∈ Finset.range (m + 1), rcoef s a • (((𝔼 ^ a) ⊗ₖ 𝟙) ⊗ₖ (𝔽 ^ a)))
        * leg23 (cartanTheta s m m)
      = leg23 (cartanTheta s m m)
        * ∑ a ∈ Finset.range (m + 1), rcoef s a • ((𝔼 ⊗ₖ 𝕂) ⊗ₖ 𝔽) ^ a := by
    rw [Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [smul_mul_assoc, conj23_F s hs m, mul_smul_comm, kron_pow, kron_pow]
  have hYX : ((𝟙 ⊗ₖ 𝔼) ⊗ₖ 𝔽) * ((𝔼 ⊗ₖ 𝕂) ⊗ₖ 𝔽)
      = ((s ^ 2)⁻¹ ^ 2) • (((𝔼 ⊗ₖ 𝕂) ⊗ₖ 𝔽) * ((𝟙 ⊗ₖ 𝔼) ⊗ₖ 𝔽)) := by
    simp only [← mul_kronecker_mul, one_mul, mul_one]
    rw [irrepE_mul_Kp s hs m, kronecker_smul, smul_kronecker]
  have hXn : ((𝔼 ⊗ₖ 𝕂) ⊗ₖ 𝔽) ^ (m + 1) = 0 := by
    rw [kron_pow, kron_pow, irrepE_pow_nil, zero_kronecker, zero_kronecker]
  have hYn : ((𝟙 ⊗ₖ 𝔼) ⊗ₖ 𝔽) ^ (m + 1) = 0 := by
    rw [kron_pow, kron_pow, irrepE_pow_nil, kronecker_zero, zero_kronecker]
  rw [h13, h23, ← theta13_mul_theta23 s hs m]
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc _ (leg23 (cartanTheta s m m)), hmove]
  simp only [Matrix.mul_assoc]
  rw [qexp_mul s hs hq2 hYX m hXn hYn hint]
  congr 2
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [← add_kronecker, kron_pow]

include hs hq2 in
/-- **Hexagon, `(Δ^{op} ⊗ 1) R = R₂₃ R₁₃`.** On `V_{m+1}^{⊗3}`,
`R₂₃ R₁₃ = Θ₁₃ Θ₂₃ Σ_{n ≤ 2m} c_n Δ^{op}(E)ⁿ ⊗ Fⁿ` with `Δ^{op}(E) = K ⊗ E + E ⊗ 1`. -/
theorem hexagon_23_13 (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    leg23 (rMat s hs m m) * leg13 (rMat s hs m m)
      = theta123 s m * ∑ n ∈ Finset.range (2 * m + 1),
          rcoef s n • (((𝕂 ⊗ₖ 𝔼 + 𝔼 ⊗ₖ 𝟙) ^ n) ⊗ₖ (𝔽 ^ n)) := by
  have h23 : leg23 (rMat s hs m m) = leg23 (cartanTheta s m m)
      * ∑ b ∈ Finset.range (m + 1), rcoef s b • ((𝟙 ⊗ₖ (𝔼 ^ b)) ⊗ₖ (𝔽 ^ b)) := by
    unfold rMat; rw [leg23_mul, rSum_irrep s hs m, leg23_sum]
  have h13 : leg13 (rMat s hs m m) = leg13 (cartanTheta s m m)
      * ∑ a ∈ Finset.range (m + 1), rcoef s a • ((𝔼 ⊗ₖ 𝟙) ⊗ₖ 𝔽) ^ a := by
    unfold rMat; rw [leg13_mul, rSum_irrep s hs m, leg13_sum]
    congr 1; refine Finset.sum_congr rfl fun a _ => ?_
    rw [kron_pow, kron_pow, one_pow]
  have hmove : (∑ b ∈ Finset.range (m + 1), rcoef s b • ((𝟙 ⊗ₖ (𝔼 ^ b)) ⊗ₖ (𝔽 ^ b)))
        * leg13 (cartanTheta s m m)
      = leg13 (cartanTheta s m m)
        * ∑ b ∈ Finset.range (m + 1), rcoef s b • ((𝕂 ⊗ₖ 𝔼) ⊗ₖ 𝔽) ^ b := by
    rw [Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_congr rfl fun b _ => ?_
    rw [smul_mul_assoc, conj13_F s hs m, mul_smul_comm, kron_pow, kron_pow]
  have hYX : ((𝔼 ⊗ₖ 𝟙) ⊗ₖ 𝔽) * ((𝕂 ⊗ₖ 𝔼) ⊗ₖ 𝔽)
      = ((s ^ 2)⁻¹ ^ 2) • (((𝕂 ⊗ₖ 𝔼) ⊗ₖ 𝔽) * ((𝔼 ⊗ₖ 𝟙) ⊗ₖ 𝔽)) := by
    simp only [← mul_kronecker_mul, one_mul, mul_one]
    rw [irrepE_mul_Kp s hs m, smul_kronecker, smul_kronecker]
  have hXn : ((𝕂 ⊗ₖ 𝔼) ⊗ₖ 𝔽) ^ (m + 1) = 0 := by
    rw [kron_pow, kron_pow, irrepE_pow_nil, kronecker_zero, zero_kronecker]
  have hYn : ((𝔼 ⊗ₖ 𝟙) ⊗ₖ 𝔽) ^ (m + 1) = 0 := by
    rw [kron_pow, kron_pow, irrepE_pow_nil, zero_kronecker, zero_kronecker]
  rw [h13, h23, ← theta23_mul_theta13 s hs m]
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc _ (leg13 (cartanTheta s m m)), hmove]
  simp only [Matrix.mul_assoc]
  rw [qexp_mul s hs hq2 hYX m hXn hYn hint]
  congr 2
  refine Finset.sum_congr rfl fun n _ => ?_
  rw [← add_kronecker, kron_pow]

end HexagonMain

end QOU.Mass.QuantumSl2
