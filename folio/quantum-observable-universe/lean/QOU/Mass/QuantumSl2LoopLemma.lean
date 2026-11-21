import QOU.Mass.QuantumSl2HalfTurn

/-!
# The loop around a hook

Close the third strand of `Ř₂ (Y ⊗ 1) Ř₂` with the quantum trace. The closed strand is a loop
hooked around the second leg of `Y`. After the bending `nat` of `QuantumSl2Loop`, the loop is a
mirror clasp on the two upward strands:

    nat(K² · X(Y)) = (−1)^m · rot(Ř⁻²) · nat(K² · Y)        for every `Y`.

The `Y`-free core is the hook identity `hook_kernel`. It uses only planar moves: crossing
symmetry `rot Ř = Ř⁻¹`, the half turn `rot Ř⁻¹ = Ř`, the snake identities and the cap/cup
closure.

This is the loop lemma of the Whitehead flype (issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Hook

/-- Reordering a product of two sums against a common index. -/
theorem sum_reorder {ι : Type*} [Fintype ι] (k : 𝕜) (A : ι → ι → 𝕜) (B : ι → 𝕜) (P Q : ι → ι → 𝕜) :
    ∑ w : ι, (k * ∑ c : ι, ∑ b : ι, A c b * P b w) * (∑ γ : ι, B γ * Q γ w)
      = ∑ c : ι, ∑ b : ι, k * A c b * ∑ γ : ι, B γ * ∑ w : ι, P b w * Q γ w := by
  calc ∑ w : ι, (k * ∑ c : ι, ∑ b : ι, A c b * P b w) * (∑ γ : ι, B γ * Q γ w)
      = ∑ w : ι, ∑ γ : ι, ∑ c : ι, ∑ b : ι, k * A c b * P b w * B γ * Q γ w := by
        simp only [Finset.mul_sum, Finset.sum_mul]
        refine Finset.sum_congr rfl fun w _ => Finset.sum_congr rfl fun γ _ =>
          Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun b _ => ?_
        ring
    _ = ∑ w : ι, ∑ c : ι, ∑ γ : ι, ∑ b : ι, k * A c b * P b w * B γ * Q γ w :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ c : ι, ∑ w : ι, ∑ γ : ι, ∑ b : ι, k * A c b * P b w * B γ * Q γ w := Finset.sum_comm
    _ = ∑ c : ι, ∑ w : ι, ∑ b : ι, ∑ γ : ι, k * A c b * P b w * B γ * Q γ w :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ c : ι, ∑ b : ι, ∑ w : ι, ∑ γ : ι, k * A c b * P b w * B γ * Q γ w :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ c : ι, ∑ b : ι, ∑ γ : ι, ∑ w : ι, k * A c b * P b w * B γ * Q γ w :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = _ := by
        simp only [Finset.mul_sum]
        refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun b _ =>
          Finset.sum_congr rfl fun γ _ => Finset.sum_congr rfl fun w _ => ?_
        ring

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- **The hook identity.** Closing the third strand of two crossings, against a cup:
`K_{y₁} Σ_{d,r,w} K_r Ř_{(y₁,r),(u,w)} Ř_{(v,w),(d,r)} cup(y₂,d)
  = (−1)^m K_u Σ_c cup(y₁,c) (Ř⁻²)_{(y₂,v),(c,u)}`, with `Ř⁻¹ = rot Ř`. -/
theorem hook_kernel (y1 y2 u v : Fin (m + 1)) :
    (s ^ 2) ^ wt m y1 * ∑ d : Fin (m + 1), ∑ r : Fin (m + 1), ∑ w : Fin (m + 1),
        (s ^ 2) ^ wt m r * rCheckMat s hs m m (y1, r) (u, w) * rCheckMat s hs m m (v, w) (d, r)
          * cupVec (s ^ 2) m (y2, d)
      = (-1) ^ m * (s ^ 2) ^ wt m u * ∑ c : Fin (m + 1), cupVec (s ^ 2) m (y1, c)
          * (rotOp (s ^ 2) m (rCheckMat s hs m m) * rotOp (s ^ 2) m (rCheckMat s hs m m))
            (y2, v) (c, u) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  set R := rCheckMat s hs m m with hRdef
  set Ri := rotOp (s ^ 2) m R with hRidef
  have hRR : rotOp (s ^ 2) m Ri = R := rotOp_rotOp_rCheck s hs m hq2 hint
  have hA : ∀ w r : Fin (m + 1), ∑ d : Fin (m + 1), R (v, w) (d, r) * cupVec (s ^ 2) m (y2, d)
      = ∑ γ : Fin (m + 1), Ri (y2, v) (r, γ) * cupVec (s ^ 2) m (γ, w) := by
    intro w r
    have := sum_rotOp_cup m hq hint Ri y2 v w r
    rwa [hRR] at this
  have hB : ∀ r w : Fin (m + 1), R (y1, r) (u, w) = ∑ c : Fin (m + 1), ∑ b : Fin (m + 1),
      cupVec (s ^ 2) m (y1, c) * Ri (r, b) (c, u) * capVec (s ^ 2) m (b, w) := fun r w =>
    (sum_cup_rotOp_cap m hq hint R y1 r u w).symm
  have hgR : ∀ x y : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → Ri x y = 0 :=
    fun x y h => rotOp_grade m R (fun a b h => rCheckMat_grade s hs m m a b h) x y h
  -- move the `d` sum innermost
  have e1 : ∑ d : Fin (m + 1), ∑ r : Fin (m + 1), ∑ w : Fin (m + 1),
        (s ^ 2) ^ wt m r * R (y1, r) (u, w) * R (v, w) (d, r) * cupVec (s ^ 2) m (y2, d)
      = ∑ r : Fin (m + 1), ∑ w : Fin (m + 1), (s ^ 2) ^ wt m r * R (y1, r) (u, w)
          * ∑ d : Fin (m + 1), R (v, w) (d, r) * cupVec (s ^ 2) m (y2, d) := by
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun r _ => ?_
    rw [Finset.sum_comm]
    refine Finset.sum_congr rfl fun w _ => ?_
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun d _ => ?_
    ring
  -- substitute, then move the `w` sum innermost and close it
  have e2 : ∀ r : Fin (m + 1), ∑ w : Fin (m + 1), (s ^ 2) ^ wt m r * R (y1, r) (u, w)
        * ∑ d : Fin (m + 1), R (v, w) (d, r) * cupVec (s ^ 2) m (y2, d)
      = ∑ c : Fin (m + 1), ∑ b : Fin (m + 1), (s ^ 2) ^ wt m r * cupVec (s ^ 2) m (y1, c)
          * Ri (r, b) (c, u) * (Ri (y2, v) (r, b) * ((-1) ^ m * (s ^ 2) ^ wt m b)) := by
    intro r
    have hC : ∀ b γ : Fin (m + 1), ∑ w : Fin (m + 1), capVec (s ^ 2) m (b, w)
        * cupVec (s ^ 2) m (γ, w) = if b = γ then (-1) ^ m * (s ^ 2) ^ wt m b else 0 :=
      sum_capVec_cupVec m hq hint
    rw [Finset.sum_congr rfl fun w _ => by rw [hA w r, hB r w]]
    rw [sum_reorder ((s ^ 2) ^ wt m r) (fun c b => cupVec (s ^ 2) m (y1, c) * Ri (r, b) (c, u))
      (fun γ => Ri (y2, v) (r, γ)) (fun b w => capVec (s ^ 2) m (b, w))
      (fun γ w => cupVec (s ^ 2) m (γ, w))]
    simp only [hC, mul_ite, mul_zero, Finset.sum_ite_eq, Finset.mem_univ, if_true]
    refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun b _ => ?_
    ring
  rw [e1, Finset.sum_congr rfl fun r _ => e2 r, Finset.mul_sum, Finset.mul_sum]
  simp only [mul_apply, Fintype.sum_prod_type, Finset.mul_sum]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun c _ => Finset.sum_congr rfl fun r _ =>
    Finset.sum_congr rfl fun b _ => ?_
  by_cases hc : (y1 : ℕ) + c = m
  · by_cases hg : (r : ℕ) + b = c + u
    · have hw : wt m y1 + wt m r + wt m b = wt m u := by
        unfold wt
        have hc' : ((y1 : ℕ) : ℤ) + (c : ℕ) = m := by exact_mod_cast hc
        have hg' : ((r : ℕ) : ℤ) + (b : ℕ) = (c : ℕ) + (u : ℕ) := by exact_mod_cast hg
        linarith
      have hz : (s ^ 2) ^ wt m y1 * (s ^ 2) ^ wt m r * (s ^ 2) ^ wt m b = (s ^ 2) ^ wt m u := by
        rw [← zpow_add₀ hq, ← zpow_add₀ hq, hw]
      linear_combination (-1) ^ m * cupVec (s ^ 2) m (y1, c) * Ri (r, b) (c, u)
        * Ri (y2, v) (r, b) * hz
    · rw [hgR (r, b) (c, u) hg]; ring
  · have : cupVec (s ^ 2) m (y1, c) = 0 := by simp [cupVec, hwVec, hc]
    rw [this]; ring

end Hook

end QOU.Mass.QuantumSl2
