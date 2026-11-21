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

section Cup

variable {q : 𝕜} (m : ℕ) (hq : q ≠ 0) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **First snake identity**, coefficientwise: `Σ_z cap(b,z) cup(z,v) = δ_{bv}`. -/
theorem sum_cap_cup (b v : Fin (m + 1)) :
    ∑ z : Fin (m + 1), capVec q m (b, z) * cupVec q m (z, v) = if b = v then 1 else 0 := by
  rw [sum_capVec q m b (fun z => cupVec q m (z, v))]
  by_cases h : b = v
  · subst h; rw [if_pos rfl]; exact cap_mul_cup_rev m hq hint b
  · rw [if_neg h, cupVec_eq_zero q m (a := b.rev) (b := v) (fun h' => h (Fin.rev_inj.mp h')),
      mul_zero]

include hq hint in
/-- **A cup on the second output of a turned operator.** If `rot² M = M`, then
`Σ_z (rot M)_{(y₁,y₂),(u,z)} cup(z,v) = Σ_c cup(y₁,c) M_{(y₂,v),(c,u)}`. -/
theorem sum_rotOp_cup_out (M : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (hM : rotOp q m (rotOp q m M) = M) (y1 y2 u v : Fin (m + 1)) :
    ∑ z : Fin (m + 1), rotOp q m M (y1, y2) (u, z) * cupVec q m (z, v)
      = ∑ c : Fin (m + 1), cupVec q m (y1, c) * M (y2, v) (c, u) := by
  have h : ∀ z : Fin (m + 1), rotOp q m M (y1, y2) (u, z) = ∑ c : Fin (m + 1),
      ∑ b : Fin (m + 1), cupVec q m (y1, c) * M (y2, b) (c, u) * capVec q m (b, z) := by
    intro z
    have := sum_cup_rotOp_cap m hq hint (rotOp q m M) y1 y2 u z
    rw [hM] at this
    exact this.symm
  simp only [h, Finset.sum_mul]
  rw [Finset.sum_comm]
  refine Finset.sum_congr rfl fun c _ => ?_
  rw [Finset.sum_comm]
  have e : ∀ b : Fin (m + 1), ∑ z : Fin (m + 1), cupVec q m (y1, c) * M (y2, b) (c, u)
      * capVec q m (b, z) * cupVec q m (z, v)
      = cupVec q m (y1, c) * M (y2, b) (c, u)
        * ∑ z : Fin (m + 1), capVec q m (b, z) * cupVec q m (z, v) := by
    intro b; rw [Finset.mul_sum]; refine Finset.sum_congr rfl fun z _ => ?_; ring
  simp only [e, sum_cap_cup m hq hint, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq',
    Finset.mem_univ, if_true]

end Cup

section Reorder

variable {ι : Type*} [Fintype ι]

/-- Move the third and sixth indices of a six-fold sum outward. -/
theorem sum_reorder6 (T : ι → ι → ι → ι → ι → ι → 𝕜) :
    ∑ a : ι, ∑ d : ι, ∑ r : ι, ∑ u : ι, ∑ w : ι, ∑ v : ι, T a d r u w v
      = ∑ a : ι, ∑ u : ι, ∑ v : ι, ∑ d : ι, ∑ r : ι, ∑ w : ι, T a d r u w v := by
  refine Finset.sum_congr rfl fun a _ => ?_
  calc ∑ d : ι, ∑ r : ι, ∑ u : ι, ∑ w : ι, ∑ v : ι, T a d r u w v
      = ∑ d : ι, ∑ u : ι, ∑ r : ι, ∑ w : ι, ∑ v : ι, T a d r u w v :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ u : ι, ∑ d : ι, ∑ r : ι, ∑ w : ι, ∑ v : ι, T a d r u w v := Finset.sum_comm
    _ = ∑ u : ι, ∑ d : ι, ∑ r : ι, ∑ v : ι, ∑ w : ι, T a d r u w v :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ =>
          Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ u : ι, ∑ d : ι, ∑ v : ι, ∑ r : ι, ∑ w : ι, T a d r u w v :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ u : ι, ∑ v : ι, ∑ d : ι, ∑ r : ι, ∑ w : ι, T a d r u w v :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm

/-- Reorder a four-fold sum `(z₁, z₂, a, d) ↦ (a, z₁, d, z₂)`. -/
theorem sum_reorder4 (T : ι → ι → ι → ι → 𝕜) :
    ∑ z1 : ι, ∑ z2 : ι, ∑ a : ι, ∑ d : ι, T z1 z2 a d
      = ∑ a : ι, ∑ z1 : ι, ∑ d : ι, ∑ z2 : ι, T z1 z2 a d := by
  calc ∑ z1 : ι, ∑ z2 : ι, ∑ a : ι, ∑ d : ι, T z1 z2 a d
      = ∑ z1 : ι, ∑ a : ι, ∑ z2 : ι, ∑ d : ι, T z1 z2 a d :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_comm
    _ = ∑ a : ι, ∑ z1 : ι, ∑ z2 : ι, ∑ d : ι, T z1 z2 a d := Finset.sum_comm
    _ = ∑ a : ι, ∑ z1 : ι, ∑ d : ι, ∑ z2 : ι, T z1 z2 a d :=
        Finset.sum_congr rfl fun _ _ => Finset.sum_congr rfl fun _ _ => Finset.sum_comm

end Reorder

section HookOp

variable (q : 𝕜) (m : ℕ)

/-- **The hook.** Close the third strand of `Ř₂ (Y ⊗ 1) Ř₂` with the weight `K`:
`X(Y)_{(a,b),(c,d)} = Σ_{r,u,w,v} K_r R_{(b,r),(u,w)} Y_{(a,u),(c,v)} R_{(v,w),(d,r)}`. -/
def hookOp (R Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  fun y x => ∑ r : Fin (m + 1), ∑ u : Fin (m + 1), ∑ w : Fin (m + 1), ∑ v : Fin (m + 1),
    q ^ wt m r * R (y.2, r) (u, w) * Y (y.1, u) (x.1, v) * R (v, w) (x.2, r)

/-- The weight `K ⊗ K` as a diagonal matrix. -/
def kk : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜 :=
  diagonal fun x => q ^ wt m x.1 * q ^ wt m x.2

end HookOp

section Loop

variable (s : 𝕜) (hs : s ≠ 0) (m : ℕ) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- **The loop lemma.** Bending the hook turns the closed loop into a mirror clasp:
`nat((K ⊗ K) X(Y)) = (−1)^m rot(Ř⁻¹ Ř⁻¹) · nat((K ⊗ K) Y)`, with `Ř⁻¹ = rot Ř`. -/
theorem natOp_hookOp (Y : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    natOp (s ^ 2) m (kk (s ^ 2) m * hookOp (s ^ 2) m (rCheckMat s hs m m) Y)
      = ((-1) ^ m : 𝕜) • (rotOp (s ^ 2) m
          (rotOp (s ^ 2) m (rCheckMat s hs m m) * rotOp (s ^ 2) m (rCheckMat s hs m m))
          * natOp (s ^ 2) m (kk (s ^ 2) m * Y)) := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  set R := rCheckMat s hs m m with hRdef
  set Ri := rotOp (s ^ 2) m R with hRidef
  have hRR : rotOp (s ^ 2) m Ri = R := rotOp_rotOp_rCheck s hs m hq2 hint
  have hM : rotOp (s ^ 2) m (rotOp (s ^ 2) m (Ri * Ri)) = Ri * Ri := by
    rw [rotOp_rotOp_mul m hq hint, hRidef, hRR]
  ext ⟨y1, y2⟩ ⟨x1, x2⟩
  have eL : natOp (s ^ 2) m (kk (s ^ 2) m * hookOp (s ^ 2) m R Y) (y1, y2) (x1, x2)
      = ∑ a : Fin (m + 1), ∑ u : Fin (m + 1), ∑ v : Fin (m + 1),
          capVec (s ^ 2) m (a, x1) * (s ^ 2) ^ wt m a * Y (a, u) (x2, v)
          * ((s ^ 2) ^ wt m y1 * ∑ d : Fin (m + 1), ∑ r : Fin (m + 1), ∑ w : Fin (m + 1),
            (s ^ 2) ^ wt m r * R (y1, r) (u, w) * R (v, w) (d, r) * cupVec (s ^ 2) m (y2, d)) := by
    simp only [natOp, kk, diagonal_mul, hookOp, Finset.mul_sum, Finset.sum_mul]
    rw [sum_reorder6]
    refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun u _ =>
      Finset.sum_congr rfl fun v _ => Finset.sum_congr rfl fun d _ =>
      Finset.sum_congr rfl fun r _ => Finset.sum_congr rfl fun w _ => ?_
    ring
  have eR : (((-1) ^ m : 𝕜) • (rotOp (s ^ 2) m (Ri * Ri) * natOp (s ^ 2) m (kk (s ^ 2) m * Y)))
        (y1, y2) (x1, x2)
      = ∑ a : Fin (m + 1), ∑ u : Fin (m + 1), ∑ v : Fin (m + 1),
          capVec (s ^ 2) m (a, x1) * (s ^ 2) ^ wt m a * Y (a, u) (x2, v)
          * ((-1) ^ m * (s ^ 2) ^ wt m u * ∑ c : Fin (m + 1),
            cupVec (s ^ 2) m (y1, c) * (Ri * Ri) (y2, v) (c, u)) := by
    simp only [← sum_rotOp_cup_out m hq hint (Ri * Ri) hM]
    simp only [smul_apply, smul_eq_mul, mul_apply, Fintype.sum_prod_type]
    simp only [natOp, kk, diagonal_mul]
    simp only [Finset.mul_sum]
    rw [sum_reorder4]
    refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun u _ =>
      Finset.sum_congr rfl fun v _ => Finset.sum_congr rfl fun z _ => ?_
    ring
  rw [eL, eR]
  refine Finset.sum_congr rfl fun a _ => Finset.sum_congr rfl fun u _ =>
    Finset.sum_congr rfl fun v _ => ?_
  rw [hook_kernel s hs m hq2 hint y1 y2 u v]

end Loop

end QOU.Mass.QuantumSl2
