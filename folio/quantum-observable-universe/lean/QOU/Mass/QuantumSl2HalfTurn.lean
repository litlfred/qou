import QOU.Mass.QuantumSl2Loop

/-!
# The half turn of an operator on `V ⊗ V`

Turning an operator on `V_{m+1} ⊗ V_{m+1}` twice by a quarter turn (`rotOp`) is a half turn. It
reverses the order of the four legs, `(rot² Z)_{y,x} = c(x) Z_{x̄,ȳ} d(y)`, with `x̄ = (x₂*, x₁*)`
and `a* = m − a` (`rotOp_rotOp_apply`). Two consequences:

* the half turn reverses products, `rot²(A B) = rot² B · rot² A` (`rotOp_rotOp_mul`);
* the crossing is fixed by the half turn, `rot² Ř = Ř` (`rotOp_rotOp_rCheck`), so with crossing
  symmetry `rot Ř = Ř⁻¹` also `rot Ř⁻¹ = Ř`.

These are the planar facts behind the loop lemma of the Whitehead flype (issue #7912).

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV
-- Ref: [kauffman1987] Kauffman, "State models and the Jones polynomial", Topology 26 (1987)
-/

namespace QOU.Mass.QuantumSl2

open Matrix

variable {𝕜 : Type*} [Field 𝕜]

section Collapse

variable (q : 𝕜) (m : ℕ)

theorem capVec_eq_zero {a b : Fin (m + 1)} (h : b ≠ a.rev) : capVec q m (a, b) = 0 := by
  simp only [capVec]
  rw [if_neg]
  intro h'; apply h; ext; simp [Fin.val_rev]; omega

theorem cupVec_eq_zero {a b : Fin (m + 1)} (h : a ≠ b.rev) : cupVec q m (a, b) = 0 := by
  simp only [cupVec, hwVec]
  rw [if_neg]
  intro h'; apply h; ext; simp [Fin.val_rev]; omega

/-- A sum against a cap row collapses to the partner index `a* = m − a`. -/
theorem sum_capVec (a : Fin (m + 1)) (f : Fin (m + 1) → 𝕜) :
    ∑ β, capVec q m (a, β) * f β = capVec q m (a, a.rev) * f a.rev := by
  rw [Finset.sum_eq_single a.rev]
  · intro β _ hβ; rw [capVec_eq_zero q m hβ, zero_mul]
  · simp

/-- A sum against a cup column collapses to the partner index. -/
theorem sum_cupVec (b : Fin (m + 1)) (f : Fin (m + 1) → 𝕜) :
    ∑ γ, f γ * cupVec q m (γ, b) = f b.rev * cupVec q m (b.rev, b) := by
  rw [Finset.sum_eq_single b.rev]
  · intro γ _ hγ; rw [cupVec_eq_zero q m hγ, mul_zero]
  · simp

variable {q} in
theorem cap_mul_cup_rev (hq : q ≠ 0) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)
    (a : Fin (m + 1)) : capVec q m (a, a.rev) * cupVec q m (a.rev, a) = 1 := by
  simp only [capVec, cupVec, hwVec, Fin.val_rev]
  rw [if_pos (by omega), if_pos (by omega)]
  have := snake_coef q hq m hint a (by omega)
  rwa [show m + 1 - (a + 1) = m - a by omega]

end Collapse

section HalfTurn

variable (q : 𝕜) (m : ℕ)

/-- **The half turn**: `(rot² Z)_{(y₁,y₂),(x₁,x₂)} = cap(x₁,x₁*) cap(x₂,x₂*) Z_{(x₂*,x₁*),(y₂*,y₁*)}
cup(y₁*,y₁) cup(y₂*,y₂)`. -/
theorem rotOp_rotOp_apply (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (y x : Fin (m + 1) × Fin (m + 1)) :
    rotOp q m (rotOp q m Z) y x = capVec q m (x.1, x.1.rev) * capVec q m (x.2, x.2.rev)
      * Z (x.2.rev, x.1.rev) (y.2.rev, y.1.rev) * cupVec q m (y.1.rev, y.1)
      * cupVec q m (y.2.rev, y.2) := by
  rw [rotOp_apply]
  simp only [rotOp_apply, Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_eq_single x.1.rev]
  · rw [Finset.sum_eq_single y.2.rev]
    · rw [Finset.sum_eq_single x.2.rev]
      · rw [Finset.sum_eq_single y.1.rev]
        · ring
        · intro γ _ hγ; rw [cupVec_eq_zero q m hγ]; ring
        · simp
      · intro β _ hβ
        refine Finset.sum_eq_zero fun γ _ => ?_
        rw [capVec_eq_zero q m hβ]; ring
      · simp
    · intro γ _ hγ
      refine Finset.sum_eq_zero fun β _ => Finset.sum_eq_zero fun γ' _ => ?_
      rw [cupVec_eq_zero q m hγ]; ring
    · simp
  · intro β _ hβ
    refine Finset.sum_eq_zero fun γ _ => Finset.sum_eq_zero fun β' _ =>
      Finset.sum_eq_zero fun γ' _ => ?_
    rw [capVec_eq_zero q m hβ]; ring
  · simp

end HalfTurn

section CrossingHalfTurn

variable (s : 𝕜) (hs : s ≠ 0)

/-- The row of `S` at `v_m ⊗ v_r` is the unit row (`E` never lands on `v_m`... from below). -/
theorem rSum_apply_rowBot (m m' M : ℕ) (r : Fin (m' + 1)) (x : Fin (m + 1) × Fin (m' + 1)) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) m) (irrep (pow_ne_zero 2 hs) m') M (⟨m, by omega⟩, r) x
      = if x = (⟨m, by omega⟩, r) then 1 else 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply, Finset.sum_eq_single 0]
  · simp only [Matrix.smul_apply, kroneckerMap_apply, pow_zero, one_apply, smul_eq_mul]
    have hc : rcoef s 0 = 1 := by simp [rcoef, qfact]
    rw [hc, one_mul]
    by_cases hx : x = (⟨m, by omega⟩, r)
    · subst hx; simp
    · rw [if_neg hx]
      by_cases h1 : (⟨m, by omega⟩ : Fin (m + 1)) = x.1
      · have h2 : r ≠ x.2 := by
          intro h2; exact hx (Prod.ext h1.symm h2.symm)
        rw [if_neg h2, mul_zero]
      · rw [if_neg h1, zero_mul]
  · intro n _ hn
    rw [Matrix.smul_apply, kroneckerMap_apply,
      show (irrep (pow_ne_zero 2 hs) m).E = irrepE (s ^ 2) m from rfl,
      irrepE_pow_apply (s ^ 2) m n _ x.1 (by have := x.1.isLt; simp; omega), zero_mul, smul_zero]
  · simp

/-- **The row of `Ř` at `v_a ⊗ v_m`:** only `v_m ⊗ v_a` maps there, with weight `s^{wt m · wt a}`. -/
theorem rCheckMat_apply_rowBot (m : ℕ) (a : Fin (m + 1)) (x : Fin (m + 1) × Fin (m + 1)) :
    rCheckMat s hs m m (a, ⟨m, by omega⟩) x
      = if x = (⟨m, by omega⟩, a) then s ^ (wt m m * wt m a) else 0 := by
  unfold rCheckMat rMat cartanTheta
  rw [submatrix_apply, id, diagonal_mul]
  simp only [Prod.swap_prod_mk]
  rw [rSum_apply_rowBot s hs m m]
  split_ifs <;> simp

variable (m : ℕ) (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
  (hint : ∀ i, 0 < i → i ≤ m → qint (s ^ 2) i ≠ 0)

include hq2 hint in
/-- `rot Ř` is again a `Δ(K⁻¹)`-module map (it is `Ř⁻¹`). -/
theorem rotOp_rCheck_deltaKm :
    rotOp (s ^ 2) m (rCheckMat s hs m m) * deltaKm (s ^ 2) m m
      = deltaKm (s ^ 2) m m * rotOp (s ^ 2) m (rCheckMat s hs m m) :=
  commute_of_mul_eq_one (mul_eq_one_comm.mp (rotOp_rCheck_mul_rCheck s hs m hq2 hint))
    (rCheckMat_deltaKm s hs m m)

include hq2 hint in
/-- **The crossing is fixed by the half turn:** `rot² Ř = Ř`. -/
theorem rotOp_rotOp_rCheck :
    rotOp (s ^ 2) m (rotOp (s ^ 2) m (rCheckMat s hs m m)) = rCheckMat s hs m m := by
  have hq : s ^ 2 ≠ 0 := pow_ne_zero 2 hs
  have hr : ∀ k < rOrder m m, qint (s ^ 2) (k + 1) ≠ 0 := fun k hk =>
    hint (k + 1) (by omega) (by unfold rOrder at hk; omega)
  have hRF := rCheckMat_deltaF s hs hq2 m m hr
  have hRK := rCheckMat_deltaKm s hs m m
  have hF1 := rotOp_deltaF (s ^ 2) m hq hint (rCheckMat s hs m m) hRF hRK
  have hF2 := rotOp_deltaF (s ^ 2) m hq hint _ hF1 (rotOp_rCheck_deltaKm s hs m hq2 hint)
  rw [← sub_eq_zero]
  refine eq_zero_of_deltaF_comm (s ^ 2) m (fun i hi => hint (i + 1) (by omega) (by omega)) _ ?_ ?_
  · rw [sub_mul, mul_sub, hF2, hRF]
  · intro y k
    have h0 : (⟨0, by omega⟩ : Fin (m + 1)).rev = ⟨m, by omega⟩ := by ext; simp
    rw [sub_apply, rotOp_rotOp_apply]
    simp only
    rw [h0, rCheckMat_apply_rowBot, rCheckMat_apply_col0]
    by_cases hy : y = (k, ⟨0, by omega⟩)
    · subst hy
      simp only [h0, if_true, sub_eq_zero]
      have e1 := cap_mul_cup_rev m hq hint (⟨0, by omega⟩ : Fin (m + 1))
      have e2 := cap_mul_cup_rev m hq hint k
      rw [h0] at e1
      have hexp : s ^ (wt m m * wt m (k.rev : ℕ)) = s ^ (wt m 0 * wt m k) := by
        have hk : ((k.rev : ℕ) : ℤ) = (m : ℤ) - k := by rw [Fin.val_rev]; omega
        congr 1; unfold wt; rw [hk]; ring
      rw [hexp]
      linear_combination (s ^ (wt m 0 * wt m k)) * (capVec (s ^ 2) m (k, k.rev)
        * cupVec (s ^ 2) m (k.rev, k) * e1 + e2)
    · have hne : ¬ ((y.2.rev, y.1.rev) = ((⟨m, by omega⟩ : Fin (m + 1)), k.rev)) := by
        intro h; apply hy
        obtain ⟨h1, h2⟩ := Prod.mk.injEq _ _ _ _ ▸ h
        have := congrArg Fin.rev h1; have := congrArg Fin.rev h2
        simp only [Fin.rev_rev] at *
        ext <;> simp_all
      rw [if_neg hne, if_neg hy]; ring

end CrossingHalfTurn

section Products

variable {q : 𝕜} (m : ℕ) (hq : q ≠ 0) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

theorem ne_rev_comm {a b : Fin (m + 1)} (h : b ≠ a.rev) : a ≠ b.rev := fun h' =>
  h (by rw [h', Fin.rev_rev])

include hq hint in
/-- **The half turn reverses products:** `rot²(A B) = rot² B · rot² A`. -/
theorem rotOp_rotOp_mul (A B : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜) :
    rotOp q m (rotOp q m (A * B)) = rotOp q m (rotOp q m B) * rotOp q m (rotOp q m A) := by
  ext y x
  rw [rotOp_rotOp_apply, mul_apply, mul_apply, Finset.mul_sum, Finset.sum_mul, Finset.sum_mul]
  simp only [rotOp_rotOp_apply]
  let e : (Fin (m + 1) × Fin (m + 1)) ≃ (Fin (m + 1) × Fin (m + 1)) :=
    (Equiv.prodComm _ _).trans (Equiv.prodCongr Fin.revPerm Fin.revPerm)
  rw [← Equiv.sum_comp e]
  refine Finset.sum_congr rfl fun w _ => ?_
  have h1 := cap_mul_cup_rev m hq hint w.1
  have h2 := cap_mul_cup_rev m hq hint w.2
  have hw : capVec q m (w.1, w.1.rev) * capVec q m (w.2, w.2.rev) * cupVec q m (w.1.rev, w.1)
      * cupVec q m (w.2.rev, w.2) = 1 := by
    rw [show capVec q m (w.1, w.1.rev) * capVec q m (w.2, w.2.rev) * cupVec q m (w.1.rev, w.1)
      * cupVec q m (w.2.rev, w.2) = (capVec q m (w.1, w.1.rev) * cupVec q m (w.1.rev, w.1))
      * (capVec q m (w.2, w.2.rev) * cupVec q m (w.2.rev, w.2)) by ring, h1, h2, one_mul]
  simp only [e, Equiv.trans_apply, Equiv.prodComm_apply, Equiv.prodCongr_apply,
    Prod.map, Fin.revPerm_apply, Prod.fst_swap, Prod.snd_swap]
  linear_combination (-(capVec q m (x.1, x.1.rev) * capVec q m (x.2, x.2.rev)
    * A (x.2.rev, x.1.rev) (w.2.rev, w.1.rev) * B (w.2.rev, w.1.rev) (y.2.rev, y.1.rev)
    * cupVec q m (y.1.rev, y.1) * cupVec q m (y.2.rev, y.2))) * hw

include hq hint in
/-- **Undoing a quarter turn:** `Σ_{c,b} cup(i,c) (rot Z)_{(r,b),(c,u)} cap(b,w) = Z_{(i,r),(u,w)}`. -/
theorem sum_cup_rotOp_cap (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (i r u w : Fin (m + 1)) :
    ∑ c : Fin (m + 1), ∑ b : Fin (m + 1),
      cupVec q m (i, c) * rotOp q m Z (r, b) (c, u) * capVec q m (b, w) = Z (i, r) (u, w) := by
  simp only [rotOp_apply, Finset.mul_sum, Finset.sum_mul]
  rw [Finset.sum_eq_single i.rev]
  · rw [Finset.sum_eq_single w.rev]
    · rw [Finset.sum_eq_single i]
      · rw [Finset.sum_eq_single w]
        · have h1 := cap_mul_cup_rev m hq hint i.rev
          have h2 := cap_mul_cup_rev m hq hint w.rev
          rw [Fin.rev_rev] at h1 h2
          linear_combination (Z (i, r) (u, w) * capVec q m (w.rev, w) * cupVec q m (w, w.rev)) * h1
            + Z (i, r) (u, w) * h2
        · intro γ _ hγ; rw [cupVec_eq_zero q m (a := γ) (b := w.rev) (by rw [Fin.rev_rev]; exact hγ)]; ring
        · simp
      · intro β _ hβ
        refine Finset.sum_eq_zero fun γ _ => ?_
        rw [capVec_eq_zero q m (a := i.rev) (b := β) (by rw [Fin.rev_rev]; exact hβ)]; ring
      · simp
    · intro b _ hb
      refine Finset.sum_eq_zero fun β _ => Finset.sum_eq_zero fun γ _ => ?_
      rw [capVec_eq_zero q m (b := w) (ne_rev_comm m hb)]; ring
    · simp
  · intro c _ hc
    refine Finset.sum_eq_zero fun b _ => Finset.sum_eq_zero fun β _ =>
      Finset.sum_eq_zero fun γ _ => ?_
    rw [cupVec_eq_zero q m (ne_rev_comm m hc)]; ring
  · simp

end Products

section Moves

variable {q : 𝕜} (m : ℕ) (hq : q ≠ 0) (hint : ∀ i, 0 < i → i ≤ m → qint q i ≠ 0)

include hq hint in
/-- **A cup through a turned operator:** `Σ_d (rot Z)_{(v,w),(d,r)} cup(y,d) = Σ_γ Z_{(y,v),(r,γ)} cup(γ,w)`. -/
theorem sum_rotOp_cup (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (y v w r : Fin (m + 1)) :
    ∑ d : Fin (m + 1), rotOp q m Z (v, w) (d, r) * cupVec q m (y, d)
      = ∑ γ : Fin (m + 1), Z (y, v) (r, γ) * cupVec q m (γ, w) := by
  simp only [rotOp_apply, Finset.sum_mul]
  rw [Finset.sum_eq_single y.rev]
  · rw [Finset.sum_eq_single y]
    · have h1 := cap_mul_cup_rev m hq hint y.rev
      rw [Fin.rev_rev] at h1
      refine Finset.sum_congr rfl fun γ _ => ?_
      linear_combination (Z (y, v) (r, γ) * cupVec q m (γ, w)) * h1
    · intro β _ hβ
      refine Finset.sum_eq_zero fun γ _ => ?_
      rw [capVec_eq_zero q m (a := y.rev) (b := β) (by rw [Fin.rev_rev]; exact hβ)]; ring
    · simp
  · intro d _ hd
    refine Finset.sum_eq_zero fun β _ => Finset.sum_eq_zero fun γ _ => ?_
    rw [cupVec_eq_zero q m (a := y) (b := d) (ne_rev_comm m hd)]; ring
  · simp

include hq hint in
/-- **Closing a cap against a cup** gives the `K` weight: `Σ_w cap(b,w) cup(γ,w) = (−1)^m q^{wt b} δ_{bγ}`. -/
theorem sum_capVec_cupVec (b γ : Fin (m + 1)) :
    ∑ w : Fin (m + 1), capVec q m (b, w) * cupVec q m (γ, w)
      = if b = γ then (-1) ^ m * q ^ wt m b else 0 := by
  rw [Finset.sum_eq_single b.rev]
  · split_ifs with h
    · subst h
      simp only [capVec, cupVec, hwVec, Fin.val_rev]
      rw [if_pos (by omega), if_pos (by omega)]
      have hA := hwCoef_ne_zero q hq m hint b (by omega)
      unfold capCoefQ
      rw [show ((m : ℤ) - 2 * ((b : ℕ) : ℤ)) = wt m b from rfl]
      field_simp
    · rw [cupVec_eq_zero q m (a := γ) (b := b.rev) (by rw [Fin.rev_rev]; exact Ne.symm h), mul_zero]
  · intro w _ hw; rw [capVec_eq_zero q m hw, zero_mul]
  · simp

/-- **A turned graded operator is graded.** -/
theorem rotOp_grade (Z : Matrix (Fin (m + 1) × Fin (m + 1)) (Fin (m + 1) × Fin (m + 1)) 𝕜)
    (hZ : ∀ x y : Fin (m + 1) × Fin (m + 1), (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → Z x y = 0)
    (y x : Fin (m + 1) × Fin (m + 1)) (h : (y.1 : ℕ) + y.2 ≠ x.1 + x.2) :
    rotOp q m Z y x = 0 := by
  rw [rotOp_apply]
  refine Finset.sum_eq_zero fun β _ => Finset.sum_eq_zero fun γ _ => ?_
  by_cases h1 : (x.1 : ℕ) + β = m
  · by_cases h2 : (γ : ℕ) + y.2 = m
    · rw [hZ (β, y.1) (x.2, γ) (by simp only; omega)]; ring
    · simp [cupVec, hwVec, h2]
  · simp [capVec, h1]

end Moves

end QOU.Mass.QuantumSl2
