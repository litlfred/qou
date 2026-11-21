import QOU.Mass.QuantumSl2Flype
import QOU.Mass.QuantumSl2Hexagon
import QOU.Mass.QuantumSl2BeltTensor

/-!
# The belt as a braid

The belt `beltW` on `W = V_{m+1} ⊗ V_{m+1}` is the partial quantum trace of the monodromy of `W`
with a `V_{m+1}` belt. Written with the crossings of `V^{⊗3}`, that monodromy is the braid
`Ř₂ Ř₁ Ř₁ Ř₂`:

* `R_{W,V} = R₁₃ R₂₃` is the first hexagon `(Δ ⊗ 1) R` (`hexagon_13_23`);
* `R_{V,W} = R₁₃ R₁₂` is the second hexagon `(1 ⊗ Δ) R` (`hexagon_13_12`, proved here).

So `beltW` is the hook `X(Ř²)` of `QuantumSl2LoopLemma` (`hookOp_mono_eq_beltW`).

This is a step of the Whitehead link trace (issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. VIII.2–VIII.3 (hexagon)
-/

namespace QOU.Mass.QuantumSl2

open Matrix
open scoped Kronecker

variable {𝕜 : Type*} [Field 𝕜]

section Leg12

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

omit [Fintype ι] in
theorem leg12_diagonal (d : ι × ι → 𝕜) :
    leg12 (diagonal d) = diagonal fun x : (ι × ι) × ι => d x.1 := by
  unfold leg12
  rw [← diagonal_one, diagonal_kronecker_diagonal]
  congr 1; funext x; simp

omit [Fintype ι] in
theorem leg12_sum {S : Finset ℕ} (c : ℕ → 𝕜) (B C : ℕ → Matrix ι ι 𝕜) :
    leg12 (∑ n ∈ S, c n • (B n ⊗ₖ C n))
      = ∑ n ∈ S, c n • ((B n ⊗ₖ C n) ⊗ₖ (1 : Matrix ι ι 𝕜)) := by
  ext x y
  simp only [leg12_apply, sum_apply, smul_apply, kroneckerMap_apply, smul_eq_mul, Finset.sum_mul]
  refine Finset.sum_congr rfl fun n _ => ?_
  ring

end Leg12

section Hexagon2

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ)

local notation "𝔼" => irrepE (s ^ 2) m
local notation "𝔽" => irrepF (s ^ 2) m
local notation "𝕂m" => irrepKm (s ^ 2) m
local notation "𝟙" => (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜)

include hs in
/-- `K⁻ᵃ v_r = s^{−2a·wt r} v_r`. -/
theorem irrepKm_pow_apply (a : ℕ) (r r' : Fin (m + 1)) :
    (irrepKm (s ^ 2) m ^ a) r r' = if r = r' then s ^ (-(2 * wt m r * a)) else 0 := by
  rw [irrepKm, diagonal_pow, diagonal_apply]
  split_ifs
  · simp only [Pi.pow_apply]
    rw [irrepKm_diag_eq s hs (Nat.lt_succ_iff.mp r.isLt), ← zpow_natCast, ← zpow_mul]
    congr 1; ring
  · rfl

theorem leg12_cartanTheta :
    leg12 (cartanTheta s m m) = diagonal fun x : Tri m => s ^ (wt m x.1.1 * wt m x.1.2) := by
  unfold cartanTheta; rw [leg12_diagonal]

include hs in
/-- Moving `Θ₁₂` left through `Eᵃ ⊗ 1 ⊗ B` produces `Eᵃ ⊗ K⁻ᵃ ⊗ B`. -/
theorem conj12_E (B : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) (a : ℕ) :
    (((𝔼 ^ a) ⊗ₖ 𝟙) ⊗ₖ B) * leg12 (cartanTheta s m m)
      = leg12 (cartanTheta s m m) * (((𝔼 ^ a) ⊗ₖ (𝕂m ^ a)) ⊗ₖ B) := by
  rw [leg12_cartanTheta]
  ext ⟨⟨p, r⟩, t⟩ ⟨⟨p', r'⟩, t'⟩
  simp only [mul_diagonal, diagonal_mul, kroneckerMap_apply, one_apply, irrepKm_pow_apply s hs]
  by_cases hr : r = r'
  · subst hr
    by_cases hp : (p : ℕ) + a = p'
    · have h : s ^ (wt m p' * wt m r) = s ^ (wt m p * wt m r) * s ^ (-(2 * wt m r * a)) := by
        rw [← zpow_add₀ hs]; congr 1; unfold wt; rw [← hp]; push_cast; ring
      simp only [if_true, h]; ring
    · rw [irrepE_pow_apply _ m a p p' hp]; ring
  · simp [hr]

include hs in
theorem irrepF_mul_Km : 𝔽 * 𝕂m = ((s ^ 2)⁻¹ ^ 2) • (𝕂m * 𝔽) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have h1 := (irrep hq m).KF
  have h2 := (irrep hq m).Km_Kp
  change irrepKp (s ^ 2) m * 𝔽 * 𝕂m = _ at h1
  change 𝕂m * irrepKp (s ^ 2) m = 1 at h2
  calc 𝔽 * 𝕂m = 𝕂m * (irrepKp (s ^ 2) m * 𝔽 * 𝕂m) := by
        rw [← Matrix.mul_assoc, ← Matrix.mul_assoc, h2, Matrix.one_mul]
    _ = _ := by rw [h1, Matrix.mul_smul]; rfl

/-- `Θ₁₂ Θ₁₃ = q^{H ⊗ (H ⊗ 1 + 1 ⊗ H)/2}`: `v_p ⊗ v_r ⊗ v_t ↦ s^{wt p (wt r + wt t)}`. -/
def theta1W : Matrix (Tri m) (Tri m) 𝕜 :=
  diagonal fun x => s ^ (wt m x.1.1 * (wt m x.1.2 + wt m x.2))

include hs in
theorem theta13_mul_theta12 :
    leg13 (cartanTheta s m m) * leg12 (cartanTheta s m m) = theta1W s m := by
  rw [leg13_cartanTheta, leg12_cartanTheta, diagonal_mul_diagonal, theta1W]
  congr 1; funext x; rw [← zpow_add₀ hs]; ring_nf

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hs hq2 in
/-- **Hexagon, `(1 ⊗ Δ) R = R₁₃ R₁₂`.** On `V_{m+1}^{⊗3}`,
`R₁₃ R₁₂ = Θ₁₂ Θ₁₃ Σ_{n ≤ 2m} c_n (Eⁿ ⊗ Δ(F)ⁿ)` with `Δ(F) = F ⊗ 1 + K⁻¹ ⊗ F`. -/
theorem hexagon_13_12 (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    leg13 (rMat s hs m m) * leg12 (rMat s hs m m)
      = theta1W s m * ∑ n ∈ Finset.range (2 * m + 1),
          rcoef s n • ((𝔼 ⊗ₖ 𝕂m) ⊗ₖ 𝔽 + (𝔼 ⊗ₖ 𝔽) ⊗ₖ 𝟙) ^ n := by
  have h13 : leg13 (rMat s hs m m) = leg13 (cartanTheta s m m)
      * ∑ a ∈ Finset.range (m + 1), rcoef s a • (((𝔼 ^ a) ⊗ₖ 𝟙) ⊗ₖ (𝔽 ^ a)) := by
    unfold rMat; rw [leg13_mul, rSum_irrep s hs m, leg13_sum]
  have h12 : leg12 (rMat s hs m m) = leg12 (cartanTheta s m m)
      * ∑ b ∈ Finset.range (m + 1), rcoef s b • ((𝔼 ⊗ₖ 𝔽) ⊗ₖ 𝟙) ^ b := by
    unfold rMat; rw [leg12_mul, rSum_irrep s hs m, leg12_sum]
    congr 1; refine Finset.sum_congr rfl fun b _ => ?_
    rw [kron_pow, kron_pow, one_pow]
  have hmove : (∑ a ∈ Finset.range (m + 1), rcoef s a • (((𝔼 ^ a) ⊗ₖ 𝟙) ⊗ₖ (𝔽 ^ a)))
        * leg12 (cartanTheta s m m)
      = leg12 (cartanTheta s m m)
        * ∑ a ∈ Finset.range (m + 1), rcoef s a • ((𝔼 ⊗ₖ 𝕂m) ⊗ₖ 𝔽) ^ a := by
    rw [Finset.sum_mul, Finset.mul_sum]
    refine Finset.sum_congr rfl fun a _ => ?_
    rw [smul_mul_assoc, conj12_E s hs m, mul_smul_comm, kron_pow, kron_pow]
  have hYX : ((𝔼 ⊗ₖ 𝔽) ⊗ₖ 𝟙) * ((𝔼 ⊗ₖ 𝕂m) ⊗ₖ 𝔽)
      = ((s ^ 2)⁻¹ ^ 2) • (((𝔼 ⊗ₖ 𝕂m) ⊗ₖ 𝔽) * ((𝔼 ⊗ₖ 𝔽) ⊗ₖ 𝟙)) := by
    simp only [← mul_kronecker_mul, one_mul, mul_one]
    rw [irrepF_mul_Km s hs m, kronecker_smul, smul_kronecker]
  have hXn : ((𝔼 ⊗ₖ 𝕂m) ⊗ₖ 𝔽) ^ (m + 1) = 0 := by
    rw [kron_pow, kron_pow, irrepE_pow_nil, zero_kronecker, zero_kronecker]
  have hYn : ((𝔼 ⊗ₖ 𝔽) ⊗ₖ 𝟙) ^ (m + 1) = 0 := by
    rw [kron_pow, kron_pow, irrepE_pow_nil, zero_kronecker, zero_kronecker]
  rw [h13, h12, ← theta13_mul_theta12 s hs m]
  simp only [Matrix.mul_assoc]
  rw [← Matrix.mul_assoc _ (leg12 (cartanTheta s m m)), hmove]
  simp only [Matrix.mul_assoc]
  rw [qexp_mul s hs hq2 hYX m hXn hYn hint]

end Hexagon2

/-! ### The belt is the hook of `Ř²` -/

section BeltBraid

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

local notation "𝔼" => irrepE (s ^ 2) m
local notation "𝔽" => irrepF (s ^ 2) m
local notation "𝕂m" => irrepKm (s ^ 2) m
local notation "𝟙" => (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜)

/-- The reindexing `((c, a), b) ↦ (c, (a, b))` of `V^{⊗3}`. -/
abbrev assocE (m : ℕ) : Tri m ≃ Fin (m + 1) × (Fin (m + 1) × Fin (m + 1)) :=
  Equiv.prodAssoc _ _ _

include hq2 in
/-- `R_{W,V} = R₁₃ R₂₃` on `W ⊗ V = (V ⊗ V) ⊗ V`. -/
theorem rL_tens_eq (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    rL s hs (tens (s ^ 2) (pow_ne_zero 2 hs) m) (tensWt m) m
      = leg13 (rMat s hs m m) * leg23 (rMat s hs m m) := by
  rw [hexagon_13_23 s hs hq2 m hint, rL,
    ← Rep.rSum_trunc s _ _ m (2 * m) (by omega) fun n hn => ?_]
  · rfl
  · rw [show (irrep (pow_ne_zero 2 hs) m).F ^ n = 0 from
      pow_eq_zero_of_le (by omega) (irrepF_pow_nil _ m), kronecker_zero]

include hq2 in
/-- `R_{V,W} = R₁₃ R₁₂` on `V ⊗ W = V ⊗ (V ⊗ V)`, read through `((c, a), b) ↦ (c, (a, b))`. -/
theorem rR_tens_eq (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    rR s hs m (tens (s ^ 2) (pow_ne_zero 2 hs) m) (tensWt m)
      = reindex (assocE m) (assocE m) (leg13 (rMat s hs m m) * leg12 (rMat s hs m m)) := by
  rw [hexagon_13_12 s hs m hq2 hint, ← reindexAlgEquiv_apply 𝕜 𝕜, map_mul, map_sum, rR]
  congr 1
  · ext ⟨c, a, b⟩ ⟨c', a', b'⟩
    simp only [thetaR, theta1W, reindexAlgEquiv_apply, reindex_apply, submatrix_apply,
      diagonal_apply, tensWt, Equiv.prodAssoc_symm_apply, Prod.mk.injEq, and_assoc]
  · rw [← Rep.rSum_trunc s _ _ m (2 * m) (by omega) fun n hn => ?_]
    · unfold Rep.rSum
      refine Finset.sum_congr rfl fun n _ => ?_
      rw [map_smul, map_pow, map_add, reindexAlgEquiv_apply, reindexAlgEquiv_apply,
        kronecker_assoc, kronecker_assoc,
        add_comm (𝔼 ⊗ₖ (𝕂m ⊗ₖ 𝔽)), ← kronecker_add, kron_pow]
      rfl
    · rw [show (irrep (pow_ne_zero 2 hs) m).E ^ n = 0 from
        pow_eq_zero_of_le (by omega) (irrepE_pow_nil _ m), zero_kronecker]

include hq2 in
/-- **The monodromy of `W` with a `V` belt** is the braid `Ř₂ (Ř²)₁ Ř₂` on `V^{⊗3}`. -/
theorem monoG_tens_eq (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    monoG s hs (tens (s ^ 2) (pow_ne_zero 2 hs) m) (tensWt m) m
      = leg23 (rCheckMat s hs m m) * leg12 (mono s hs m m) * leg23 (rCheckMat s hs m m) := by
  have hA : leg23 (rCheckMat s hs m m) * leg12 (rCheckMat s hs m m)
      = (leg13 (rMat s hs m m) * leg12 (rMat s hs m m)).submatrix (swap12 _ ∘ swap23 _) id := by
    rw [leg23_rCheckMat, leg12_rCheckMat, sub_mul_sub _ _ _ _ (fun _ => rfl)]; rfl
  have hB : leg12 (rCheckMat s hs m m) * leg23 (rCheckMat s hs m m)
      = (leg13 (rMat s hs m m) * leg23 (rMat s hs m m)).submatrix (swap23 _ ∘ swap12 _) id := by
    rw [leg12_rCheckMat, leg23_rCheckMat, sub_mul_sub _ _ _ _ (fun _ => rfl)]; rfl
  rw [mono, leg12_mul]
  simp only [← Matrix.mul_assoc]
  rw [Matrix.mul_assoc (leg23 (rCheckMat s hs m m) * leg12 (rCheckMat s hs m m)), hA, hB, monoG,
    rR_tens_eq s hs m hq2 hint, rL_tens_eq s hs m hq2 hint]
  ext x y
  simp only [mul_apply, submatrix_apply, reindex_apply, id]
  exact Fintype.sum_equiv (assocE m).symm _ _ fun z => rfl

omit [Field 𝕜] in
theorem sum_ite_const_zero {α : Type*} [Fintype α] {M : Type*} [AddCommMonoid M] (p : Prop)
    [Decidable p] (f : α → M) : ∑ i, (if p then f i else 0) = if p then ∑ i, f i else 0 := by
  split_ifs <;> simp

/-- The hook is the `K`-weighted partial trace over the third factor of `R₂₃ Y₁₂ R₂₃`. -/
theorem hookOp_eq_ptr (q : 𝕜) (R Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (y x : Fin (m + 1) × Fin (m + 1)) :
    hookOp q m R Y y x = ∑ r : Fin (m + 1), q ^ wt m r * (leg23 R * leg12 Y * leg23 R) (y, r) (x, r) := by
  simp only [hookOp, mul_apply, leg23_apply, leg12_apply, Fintype.sum_prod_type, one_apply, mul_ite,
    ite_mul, mul_one, mul_zero, zero_mul, Finset.sum_mul, Finset.mul_sum, sum_ite_const_zero,
    Finset.sum_ite_eq, Finset.sum_ite_eq', Finset.mem_univ, if_true]
  refine Finset.sum_congr rfl fun r _ => ?_
  calc _ = ∑ w : Fin (m + 1), ∑ u : Fin (m + 1), ∑ v : Fin (m + 1),
        q ^ wt m r * R (y.2, r) (u, w) * Y (y.1, u) (x.1, v) * R (v, w) (x.2, r) := Finset.sum_comm
    _ = ∑ w : Fin (m + 1), ∑ v : Fin (m + 1), ∑ u : Fin (m + 1),
        q ^ wt m r * R (y.2, r) (u, w) * Y (y.1, u) (x.1, v) * R (v, w) (x.2, r) :=
      Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = _ := by
      rw [Finset.sum_comm]
      refine Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
        Finset.sum_congr rfl fun _ _ => ?_
      ring

include hq2 in
/-- **The belt is the hook of `Ř²`:** `X(Ř²) = beltW`. -/
theorem hookOp_mono_eq_beltW (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    hookOp (s ^ 2) m (rCheckMat s hs m m) (mono s hs m m) = beltW s hs m := by
  ext y x
  rw [hookOp_eq_ptr, beltW, beltG, monoG_tens_eq s hs m hq2 hint]
  refine Finset.sum_congr rfl fun r _ => ?_
  rw [zpow_mul]; norm_cast

end BeltBraid

/-! ### The braid-closure trace of the Whitehead braid -/

section Assembly

variable (q : 𝕜) (m : ℕ)

/-- `K ⊗ K ⊗ K` on `V^{⊗3}`. -/
def kTri : Matrix (Tri m) (Tri m) 𝕜 :=
  diagonal fun x => q ^ wt m x.1.1 * q ^ wt m x.1.2 * q ^ wt m x.2

/-- Closing the third strand of `R₂₃ Y₁₂ R₂₃ Z₁₂` with `K³` closes the hook against `Z`. -/
theorem trace_kTri_hook (R Y Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    trace (kTri q m * (leg23 R * leg12 Y * leg23 R * leg12 Z))
      = trace (kk q m * hookOp q m R Y * Z) := by
  have hh : hookOp q m R Y = fun y x => ∑ r : Fin (m + 1),
      q ^ wt m r * (leg23 R * leg12 Y * leg23 R) (y, r) (x, r) := by
    funext y x; exact hookOp_eq_ptr m q R Y y x
  rw [hh]
  generalize leg23 R * leg12 Y * leg23 R = H
  simp only [trace, diag, kTri, kk, Matrix.mul_assoc, diagonal_mul]
  simp only [mul_apply, leg12_apply, Fintype.sum_prod_type, one_apply, mul_ite, mul_one, mul_zero,
    Finset.sum_ite_eq', Finset.mem_univ, if_true, Finset.sum_mul, Finset.mul_sum]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun b _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun d _ => Finset.sum_congr rfl fun r _ => ?_
  ring

variable {q} in
theorem kk_eq_deltaK (hq : q ≠ 0) : kk q m = deltaK q m m := by
  rw [kk, deltaK, irrepKp, diagonal_kronecker_diagonal]
  congr 1; funext x
  rw [kp_eq_zpow q hq (Nat.lt_succ_iff.mp x.1.isLt), kp_eq_zpow q hq (Nat.lt_succ_iff.mp x.2.isLt)]

/-- `K³` commutes with `A₂₃` when `K ⊗ K` commutes with `A`. -/
theorem leg23_mul_kTri (A : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (hA : A * kk q m = kk q m * A) : leg23 A * kTri q m = kTri q m * leg23 A := by
  ext x y
  have h := congrFun (congrFun hA (x.1.2, x.2)) (y.1.2, y.2)
  simp only [kk, mul_diagonal, diagonal_mul] at h
  simp only [kTri, mul_diagonal, diagonal_mul, leg23_apply, one_apply]
  split_ifs with hxy
  · rw [hxy]; linear_combination (q ^ wt m y.1.1) * h
  · simp

variable (s : 𝕜) (hs : s ≠ 0) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)

include hq2 in
/-- **The Whitehead braid closed with `K³`.** For `β = σ₁⁻² σ₂ σ₁⁻¹ σ₂` on `V_{m+1}^{⊗3}`
(`σ₁ = Ř ⊗ 1`, `σ₂ = 1 ⊗ Ř`, `σ⁻¹` the quarter turn of `Ř`),
`tr(K³ β) = (−1)^m s^{m(m+2)} tr((K ⊗ K) · beltW · clasp)`. -/
theorem trace_kTri_whitehead (hint : ∀ k, 0 < k → k ≤ 2 * m → qint (s ^ 2) k ≠ 0) :
    trace (kTri (s ^ 2) m
        * (leg12 (rotOp (s ^ 2) m (rCheckMat s hs m m)) * leg12 (rotOp (s ^ 2) m (rCheckMat s hs m m))
          * leg23 (rCheckMat s hs m m) * leg12 (rotOp (s ^ 2) m (rCheckMat s hs m m))
          * leg23 (rCheckMat s hs m m)))
      = ((-1) ^ m * s ^ (m * (m + 2))) * trace (kk (s ^ 2) m * beltW s hs m * clasp s hs m) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  set Ř := rCheckMat s hs m m with hŘ
  set Ri := rotOp (s ^ 2) m Ř with hRi
  have hcomm : leg23 Ř * kTri (s ^ 2) m = kTri (s ^ 2) m * leg23 Ř :=
    leg23_mul_kTri _ m _ (by rw [kk_eq_deltaK m hq, hŘ, rCheckMat_deltaK s hs m m])
  have h1 : trace (kTri (s ^ 2) m * (leg12 Ri * leg12 Ri * leg23 Ř * leg12 Ri * leg23 Ř))
      = trace (kTri (s ^ 2) m * (leg23 Ř * leg12 (Ri * Ri) * leg23 Ř * leg12 Ri)) := by
    rw [← Matrix.mul_assoc, trace_mul_comm, ← Matrix.mul_assoc, hcomm, leg12_mul]
    simp only [Matrix.mul_assoc]
  rw [h1, trace_kTri_hook, hRi, trace_mul_rotOp, natOp_flype s hs m hq2 hint, smul_mul_assoc,
    trace_smul, smul_eq_mul, Matrix.mul_assoc, trace_mul_comm, Matrix.mul_assoc,
    show Ř * Ř = mono s hs m m from rfl, ← trace_mul_rotOp, ← clasp_eq_rotOp,
    hookOp_mono_eq_beltW s hs m hq2 hint]

end Assembly

end QOU.Mass.QuantumSl2
