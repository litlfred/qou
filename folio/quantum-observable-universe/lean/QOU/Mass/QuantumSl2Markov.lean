import QOU.Mass.QuantumSl2BraidAction
import QOU.Mass.QuantumSl2Belt

/-!
# Markov II for the `U_q(sl₂)` braiding: the partial quantum trace of `Ř^{±1}`

Stage 4 of issue #8894 (the local computation). On `V ⊗ V` with `V = V_{d+1}`, the partial
quantum trace over the second factor,

    ptr(M)_{ij} = Σ_r q^{d−2r} M_{(i,r),(j,r)},   q = s²,

satisfies

    ptr(Ř) = θ · 1,   ptr(Ř⁻¹) = θ⁻¹ · 1,   θ = s^{d(d+2)} = q^{(N²−1)/2}, N = d+1.

The method is the one `QuantumSl2Belt` uses for the monodromy. A matrix that commutes with
`Δ(F)` has a partial trace that is constant along the `F`-chain (`ptr_step`). A matrix that
preserves the grading `p + r` has a diagonal partial trace. So `ptr` is one entry times `1`.
For `Ř` that entry is the top one, `(0,0)`. For `Ř⁻¹` it is the bottom one, `(d,d)`, where row
`(d,r)` of the polynomial part is a unit row.

-- Ref: [kassel1995] Kassel, "Quantum Groups", Ch. XIV.3 (quantum trace, twist)
-- Ref: [turaev1988] Turaev, "The Yang–Baxter equation and invariants of links"
-/

namespace QOU.Mass.QuantumSl2.Markov

open Matrix
open scoped Kronecker

set_option linter.unusedSectionVars false

variable {𝕜 : Type*} [Field 𝕜] (s : 𝕜) (hs : s ≠ 0)

section PartialTrace

variable {m m' : ℕ} (M : Matrix (Fin (m + 1) × Fin (m' + 1)) (Fin (m + 1) × Fin (m' + 1)) 𝕜)

/-- The partial quantum trace over the second factor, with weight `K = q^H`. -/
def ptr : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜 :=
  fun i j => ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * M (i, r) (j, r)

include hs in
/-- `(M Δ(F))_{(a,r),(b,r)}` for `a = b+1`. -/
theorem M_deltaF_apply (a b : Fin (m + 1)) (hab : (a : ℕ) = b + 1)
    (r : Fin (m' + 1)) :
    (M * deltaF (s ^ 2) m m') (a, r) (b, r)
      = qint (s ^ 2) (b + 1) * M (a, r) (a, r)
        + s ^ (-(2 * wt m b)) * ∑ y, M (a, r) (b, y) * irrepF (s ^ 2) m' y r := by
  rw [mul_apply, Fintype.sum_prod_type]
  simp only [deltaF_apply, mul_add, Finset.sum_add_distrib, irrepKm_apply_eq s hs]
  rw [add_comm]
  congr 1
  · rw [Finset.sum_eq_single a]
    · rw [Finset.sum_eq_single r]
      · simp [irrepF, hab, mul_comm]
      · intro y _ hy; rw [one_apply, if_neg hy]; ring
      · simp
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      have : irrepF (s ^ 2) m x b = 0 := by
        simp only [irrepF]; rw [if_neg]; intro h; apply hx; ext; omega
      rw [this]; ring
    · simp
  · rw [Finset.sum_eq_single b]
    · simp only [if_true, Finset.mul_sum]
      refine Finset.sum_congr rfl fun y _ => ?_
      ring
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      rw [if_neg hx]; ring
    · simp

include hs in
/-- `(Δ(F) M)_{(a,r),(b,r)}` for `a = b+1`. -/
theorem deltaF_M_apply (a b : Fin (m + 1)) (hab : (a : ℕ) = b + 1)
    (r : Fin (m' + 1)) :
    (deltaF (s ^ 2) m m' * M) (a, r) (b, r)
      = qint (s ^ 2) (b + 1) * M (b, r) (b, r)
        + s ^ (-(2 * wt m a)) * ∑ y, irrepF (s ^ 2) m' r y * M (a, y) (b, r) := by
  rw [mul_apply, Fintype.sum_prod_type]
  simp only [deltaF_apply, add_mul, Finset.sum_add_distrib, irrepKm_apply_eq s hs]
  rw [add_comm]
  congr 1
  · rw [Finset.sum_eq_single b]
    · rw [Finset.sum_eq_single r]
      · simp [irrepF, hab]
      · intro y _ hy; rw [one_apply, if_neg (Ne.symm hy)]; ring
      · simp
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      have : irrepF (s ^ 2) m a x = 0 := by
        simp only [irrepF]; rw [if_neg]; intro h; apply hx; ext; omega
      rw [this]; ring
    · simp
  · rw [Finset.sum_eq_single a]
    · simp only [if_true, Finset.mul_sum]
      refine Finset.sum_congr rfl fun y _ => ?_
      ring
    · intro x _ hx
      refine Finset.sum_eq_zero fun y _ => ?_
      rw [if_neg (Ne.symm hx)]; ring
    · simp

include hs in
/-- **The partial trace of an `F`-module map is constant along the `F`-chain.** -/
theorem ptr_step (hc : M * deltaF (s ^ 2) m m' = deltaF (s ^ 2) m m' * M)
    (a b : Fin (m + 1)) (hab : (a : ℕ) = b + 1) :
    qint (s ^ 2) (b + 1) * ptr s M a a = qint (s ^ 2) (b + 1) * ptr s M b b := by
  have hsum : ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (M * deltaF (s ^ 2) m m') (a, r) (b, r)
      = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (deltaF (s ^ 2) m m' * M) (a, r) (b, r) := by
    rw [hc]
  simp only [M_deltaF_apply s hs M a b hab, deltaF_M_apply s hs M a b hab, mul_add,
    Finset.sum_add_distrib] at hsum
  have hcross : ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (s ^ (-(2 * wt m b)) *
        ∑ y, M (a, r) (b, y) * irrepF (s ^ 2) m' y r)
      = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (s ^ (-(2 * wt m a)) *
        ∑ y, irrepF (s ^ 2) m' r y * M (a, y) (b, r)) := by
    simp only [Finset.mul_sum]
    rw [Finset.sum_comm (f := fun (r y : Fin (m' + 1)) => s ^ (2 * wt m' r) * (s ^ (-(2 * wt m a)) *
      (irrepF (s ^ 2) m' r y * M (a, y) (b, r))))]
    refine Finset.sum_congr rfl fun r _ => Finset.sum_congr rfl fun y _ => ?_
    by_cases h : (y : ℕ) = r + 1
    · have he : s ^ (2 * wt m' r) * s ^ (-(2 * wt m b)) = s ^ (2 * wt m' y) * s ^ (-(2 * wt m a)) := by
        rw [← zpow_add₀ hs, ← zpow_add₀ hs]
        congr 1; unfold wt; omega
      calc s ^ (2 * wt m' r) * (s ^ (-(2 * wt m b)) * (M (a, r) (b, y) * irrepF (s ^ 2) m' y r))
          = (s ^ (2 * wt m' r) * s ^ (-(2 * wt m b))) * (irrepF (s ^ 2) m' y r * M (a, r) (b, y)) := by ring
        _ = _ := by rw [he]; ring
    · have hF : irrepF (s ^ 2) m' y r = 0 := by simp only [irrepF]; rw [if_neg h]
      rw [hF]; ring
  rw [hcross] at hsum
  have h := add_right_cancel hsum
  unfold ptr
  simp only [Finset.mul_sum]
  calc ∑ r : Fin (m' + 1), qint (s ^ 2) (b + 1) * (s ^ (2 * wt m' r) * M (a, r) (a, r))
      = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (qint (s ^ 2) (b + 1) * M (a, r) (a, r)) :=
        Finset.sum_congr rfl fun r _ => by ring
    _ = ∑ r : Fin (m' + 1), s ^ (2 * wt m' r) * (qint (s ^ 2) (b + 1) * M (b, r) (b, r)) := h
    _ = _ := Finset.sum_congr rfl fun r _ => by ring

/-- A grading-preserving matrix has a diagonal partial trace. -/
theorem ptr_offdiag (hgr : ∀ x y : Fin (m + 1) × Fin (m' + 1),
      (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → M x y = 0) (i j : Fin (m + 1)) (h : i ≠ j) :
    ptr s M i j = 0 := by
  unfold ptr
  refine Finset.sum_eq_zero fun r _ => ?_
  rw [hgr _ _ (by simp; omega), mul_zero]

include hs in
/-- **A grading-preserving `F`-module map has scalar partial trace**, equal to any one of its
diagonal entries. -/
theorem ptr_eq_smul_one (hc : M * deltaF (s ^ 2) m m' = deltaF (s ^ 2) m m' * M)
    (hgr : ∀ x y : Fin (m + 1) × Fin (m' + 1), (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → M x y = 0)
    (hstr : ∀ k < m, qint (s ^ 2) (k + 1) ≠ 0) (i : Fin (m + 1)) :
    ptr s M = ptr s M i i • (1 : Matrix (Fin (m + 1)) (Fin (m + 1)) 𝕜) := by
  have hdiag : ∀ (i : ℕ) (hi : i < m + 1), ptr s M ⟨i, hi⟩ ⟨i, hi⟩
      = ptr s M ⟨0, by omega⟩ ⟨0, by omega⟩ := by
    intro i
    induction i with
    | zero => intro hi; rfl
    | succ i ih =>
      intro hi
      have hst := ptr_step s hs M hc ⟨i + 1, hi⟩ ⟨i, by omega⟩ rfl
      rw [← ih (by omega)]
      exact mul_left_cancel₀ (hstr i (by omega)) hst
  have hi : ptr s M i i = ptr s M ⟨0, by omega⟩ ⟨0, by omega⟩ := hdiag i i.isLt
  ext a b
  rw [smul_apply, one_apply, smul_eq_mul, hi]
  by_cases h : a = b
  · subst h; rw [if_pos rfl, mul_one]; exact hdiag a a.isLt
  · rw [if_neg h, mul_zero]; exact ptr_offdiag s M hgr a b h

end PartialTrace

section RCheck

variable (d : ℕ)

/-- The row of `S` at `v_d ⊗ v_r` is the unit row (`E` kills the bottom vector `v_d`... from
the row side: `(Eⁿ)_{d,x} = 0` for `n > 0`). -/
theorem rSum_apply_bot (m' M : ℕ) (r : Fin (m' + 1)) (x : Fin (d + 1) × Fin (m' + 1)) :
    Rep.rSum s (irrep (pow_ne_zero 2 hs) d) (irrep (pow_ne_zero 2 hs) m') M (Fin.last d, r) x
      = if x = (Fin.last d, r) then 1 else 0 := by
  unfold Rep.rSum
  rw [Matrix.sum_apply, Finset.sum_eq_single 0]
  · simp only [Matrix.smul_apply, kroneckerMap_apply, pow_zero, one_apply, smul_eq_mul,
      rcoef_zero, one_mul]
    by_cases hx : x = (Fin.last d, r)
    · subst hx; simp
    · rw [if_neg hx]
      by_cases h1 : Fin.last d = x.1
      · have h2 : r ≠ x.2 := by
          intro h2; apply hx; ext <;> simp [← h1, ← h2]
        rw [if_neg h2, mul_zero]
      · rw [if_neg h1, zero_mul]
  · intro n _ hn
    rw [Matrix.smul_apply, kroneckerMap_apply,
      show (irrep (pow_ne_zero 2 hs) d).E = irrepE (s ^ 2) d from rfl,
      irrepE_pow_apply (s ^ 2) d n _ x.1 (by simp; omega), zero_mul, smul_zero]
  · simp

/-- Entries of `Ř = P Θ S`. -/
theorem rCheckMat_apply (y x : Fin (d + 1) × Fin (d + 1)) :
    rCheckMat s hs d d y x = s ^ (wt d y.2 * wt d y.1)
      * Rep.rSum s (irrep (pow_ne_zero 2 hs) d) (irrep (pow_ne_zero 2 hs) d) (rOrder d d) y.swap x := by
  unfold rCheckMat rMat cartanTheta
  rw [submatrix_apply, diagonal_mul]
  rfl

/-- The twist scalar `θ = s^{d(d+2)} = q^{(N²−1)/2}` on `V_{d+1}`, `N = d+1`. -/
def theta : 𝕜 := s ^ ((d : ℤ) * (d + 2))

theorem wt_zero : wt d 0 = d := by simp [wt]

theorem wt_last : wt d (Fin.last d) = -d := by simp [wt]; ring

/-- The top diagonal entry of `ptr Ř` is `θ`. -/
theorem ptr_rCheck_top :
    ptr s (rCheckMat s hs d d) 0 0 = theta s d := by
  unfold ptr
  rw [Finset.sum_eq_single 0]
  · rw [rCheckMat_apply]
    have h := rSum_apply_top s hs d d (rOrder d d) 0 (by omega) ((0 : Fin (d + 1)), (0 : Fin (d + 1)))
    simp only [Fin.zero_eta] at h
    simp only [Prod.swap, h, if_true, mul_one]
    rw [show ((0 : Fin (d + 1)) : ℕ) = 0 from rfl, wt_zero, ← zpow_add₀ hs, theta]
    congr 1; ring
  · intro r _ hr
    rw [rCheckMat_apply]
    have h := rSum_apply_top s hs d d (rOrder d d) r r.isLt ((0 : Fin (d + 1)), r)
    simp only [Fin.eta, Fin.zero_eta] at h
    simp only [Prod.swap]
    rw [h, if_neg, mul_zero, mul_zero]
    intro he
    exact hr (congrArg Prod.fst he).symm
  · simp

variable (hq2 : s ^ 2 - (s ^ 2)⁻¹ ≠ 0)
  (hint : ∀ k, 0 < k → k ≤ 2 * d → qint (s ^ 2) k ≠ 0)

include hq2 hint in
theorem rCheck_deltaF :
    rCheckMat s hs d d * deltaF (s ^ 2) d d = deltaF (s ^ 2) d d * rCheckMat s hs d d :=
  rCheckMat_deltaF s hs hq2 d d (fun k hk => hint (k + 1) (by omega) (by unfold rOrder at hk; omega))

theorem rCheck_grade : ∀ x y : Fin (d + 1) × Fin (d + 1),
    (x.1 : ℕ) + x.2 ≠ y.1 + y.2 → rCheckMat s hs d d x y = 0 :=
  fun x y h => rCheckMat_grade s hs d d x y h

include hq2 hint in
/-- **Markov II, local form (positive crossing).** `ptr(Ř) = θ · 1`. -/
theorem ptr_rCheck : ptr s (rCheckMat s hs d d) = theta s d • (1 : Matrix (Fin (d + 1)) (Fin (d + 1)) 𝕜) := by
  rw [ptr_eq_smul_one s hs _ (rCheck_deltaF s hs d hq2 hint) (rCheck_grade s hs d)
    (fun k hk => hint (k + 1) (by omega) (by omega)) 0, ptr_rCheck_top]

end RCheck

end QOU.Mass.QuantumSl2.Markov
