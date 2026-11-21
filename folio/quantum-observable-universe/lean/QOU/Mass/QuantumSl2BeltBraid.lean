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

So `beltW` is the hook `X(Ř²)` of `QuantumSl2LoopLemma`. This file proves the second hexagon;
the identification with `beltW` follows.

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

end QOU.Mass.QuantumSl2
