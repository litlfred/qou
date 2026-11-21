import QOU.SchurWeyl.JMProjector

/-!
# The Wedderburn isomorphism of `H_{n+1}(q)` in any characteristic (bean `qou-2150`)

`HeckeWedderburnGeneral.heckeWedderburn` assumes `[CharZero K]`. That hypothesis enters at one
step, the surjectivity of `Φ = ⊕_λ ρ_λ` (`HeckeProductSurjective`), which separates the blocks by
the Murphy power sums `Σ_c (q^{2c})^m`. Recovering a multiset from its power sums needs every
multiplicity to be nonzero in `K`, so the argument fails in characteristic `p`.

This file replaces that step with the explicit Murphy–Lagrange projectors from
`QOU.SchurWeyl.JMProjector`. `Φ(Σ_T π_T) = 1_λ` (`heckeProductF_blockUnit`) gives every block unit
directly, so no separation argument is needed. Each block is surjective
(`seminormalRep_range_eq_top`, any field), so `Φ` is onto (`heckeProductF_surjective`). The upper
bound `dim H_{n+1}(q) ≤ (n+1)!` holds over any field (`HeckeCoset.finrank_le_factorial`), so `Φ` is
an isomorphism (`heckeWedderburnF`).

Hypotheses: a field `K` of **any characteristic**, `q ≠ 0`, `q` not a root of unity. Nothing else:
the seminormal denominators are `1 − q^{2d}`, `d ≠ 0`, and the Lagrange denominators are
`[c]_{q²} − [d]_{q²}`, all nonzero exactly when `q` is not a root of unity. For example `K = 𝔽_p(q)`,
with `q` transcendental, satisfies them.
-/

namespace QOU.SchurWeyl

namespace AnyChar

open QOU.Mathlib (StandardYoungTableau)
open TableauCells SeminormalRep JMProjector Hecke

variable {K : Type*} [Field K] (q : K) (hq0 : q ≠ 0) (hq2 : GenericParameter.NotRootOfUnity q)
  (n : ℕ)

/-- The block product map `Φ = ⊕_λ ρ_λ`, over any field. -/
noncomputable def heckeProductF :
    Hecke K q q⁻¹ n →ₐ[K] (∀ lam : Partition (n + 1),
      Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
        (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K) :=
  Pi.algHom _ _ (fun lam => seminormalRep q hq0 hq2 n (partitionShape_card_succ lam))

@[simp] theorem heckeProductF_apply (x : Hecke K q q⁻¹ n) (lam : Partition (n + 1)) :
    heckeProductF q hq0 hq2 n x lam
      = seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) x := rfl

/-- The JM projector of `T` maps to the matrix unit `E^λ_{TT}`, over any field. -/
theorem heckeProductF_jmProj (lam : Nat.Partition (n + 1))
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    heckeProductF q hq0 hq2 n (jmProjIn q (σ K q q⁻¹ n) (contentVec T))
      = Pi.single lam (Matrix.single T T 1) := by
  classical
  have hinj : Set.InjOn (qInt2 q) {d | d ∈ contentRange n} :=
    (qInt2_injective q hq0 hq2).injOn
  funext mu
  rw [heckeProductF_apply, seminormalRep_jmProj]
  ext S U
  by_cases hmu : mu = lam
  · subst hmu
    rw [Pi.single_eq_same]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      by_cases hST : S = T
      · subst hST
        rw [projVal_self q n hinj _ (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)]
        exact (Matrix.single_apply_same _ _ _).symm
      · have : ∃ k ∈ Finset.range (n + 1), contentVec S k ≠ contentVec T k := by
          by_contra hcon
          push_neg at hcon
          exact hST (eq_of_contentVec_eq (partitionShape_card_succ mu) S T hcon)
        obtain ⟨k, hk, hne⟩ := this
        rw [projVal_eq_zero q n _ _ (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)
          hk hne]
        exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hST h.1.symm)).symm
    · rw [Matrix.diagonal_apply_ne _ hSU]
      exact (Matrix.single_apply_of_ne _ _ _ _ _ (fun h => hSU (h.1.symm.trans h.2))).symm
  · rw [Pi.single_eq_of_ne hmu]
    by_cases hSU : S = U
    · subst hSU
      rw [Matrix.diagonal_apply_eq]
      have : ∃ k ∈ Finset.range (n + 1), contentVec S k ≠ contentVec T k := by
        by_contra hcon
        push_neg at hcon
        exact hmu (QOU.Mathlib.partitionShape_injective
          (shape_eq_of_contentVec_eq (partitionShape_card_succ mu) (partitionShape_card_succ lam)
            S T hcon))
      obtain ⟨k, hk, hne⟩ := this
      rw [projVal_eq_zero q n _ _ (fun k hk => contentVec_mem (partitionShape_card_succ mu) S hk)
        hk hne]
      rfl
    · rw [Matrix.diagonal_apply_ne _ hSU]
      rfl

/-- The block unit `Pi.single λ 1` is in the image: it is the image of `Σ_T π_T`. -/
theorem heckeProductF_blockUnit (lam : Nat.Partition (n + 1)) :
    heckeProductF q hq0 hq2 n
        (∑ T : StandardYoungTableau (QOU.Mathlib.partitionShape lam),
          jmProjIn q (σ K q q⁻¹ n) (contentVec T))
      = Pi.single lam 1 := by
  classical
  rw [map_sum]
  simp only [heckeProductF_jmProj q hq0 hq2 n lam]
  funext mu
  by_cases h : mu = lam
  · subst h
    simp only [Finset.sum_apply, Pi.single_eq_same]
    ext a b
    simp only [Matrix.sum_apply, Matrix.single, Matrix.of_apply, Matrix.one_apply]
    by_cases hab : a = b
    · subst hab; simp
    · simp only [hab, if_false]
      exact Finset.sum_eq_zero (fun c _ => if_neg (fun hc => hab (hc.1.symm.trans hc.2)))
  · simp [Finset.sum_apply, Pi.single_eq_of_ne h]

/-- **`Φ` is surjective over any field** (no characteristic hypothesis): the block units are
images of the explicit Murphy–Lagrange sums, and each block is surjective. -/
theorem heckeProductF_surjective : Function.Surjective (heckeProductF q hq0 hq2 n) := by
  classical
  intro x
  have hblk : ∀ lam : Nat.Partition (n + 1), ∃ h : Hecke K q q⁻¹ n,
      seminormalRep q hq0 hq2 n (partitionShape_card_succ lam) h = x lam := by
    intro lam
    have hx : x lam ∈ (seminormalRep q hq0 hq2 n (partitionShape_card_succ lam)).range := by
      rw [seminormalRep_range_eq_top]; exact Algebra.mem_top
    exact hx
  choose h hh using hblk
  refine ⟨∑ lam, (∑ T : StandardYoungTableau (QOU.Mathlib.partitionShape lam),
      jmProjIn q (σ K q q⁻¹ n) (contentVec T)) * h lam, ?_⟩
  rw [map_sum]
  simp only [map_mul, heckeProductF_blockUnit q hq0 hq2 n]
  funext mu
  rw [Finset.sum_apply, Finset.sum_eq_single mu]
  · rw [Pi.mul_apply, Pi.single_eq_same, one_mul, heckeProductF_apply, hh]
  · intro lam _ hne
    rw [Pi.mul_apply, Pi.single_eq_of_ne (Ne.symm hne), zero_mul]
  · intro h'; exact absurd (Finset.mem_univ mu) h'

include hq0 hq2 in
theorem finrank_hecke_eq_factorialF :
    Module.finrank K (Hecke K q q⁻¹ n) = (n + 1).factorial := by
  classical
  haveI := finiteDimensional_hecke (K := K) q q⁻¹ n
  have hle : Module.finrank K (Hecke K q q⁻¹ n) ≤ (n + 1).factorial := by
    have h := HeckeCoset.finrank_le_factorial (K := K) (q := q) (qi := q⁻¹) n
    simpa using h
  have hge : (n + 1).factorial ≤ Module.finrank K (Hecke K q q⁻¹ n) := by
    have hrange : LinearMap.range (heckeProductF q hq0 hq2 n).toLinearMap = ⊤ :=
      LinearMap.range_eq_top.mpr (heckeProductF_surjective q hq0 hq2 n)
    have h1 := LinearMap.finrank_range_le (R := K) (heckeProductF q hq0 hq2 n).toLinearMap
    rw [hrange, finrank_top] at h1
    rw [← finrank_blocks_eq_factorial (K := K) n]
    exact h1
  omega

/-- **`Φ` is injective over any field.** -/
theorem heckeProductF_injective : Function.Injective (heckeProductF q hq0 hq2 n) := by
  classical
  haveI := finiteDimensional_hecke (K := K) q q⁻¹ n
  have hfr : Module.finrank K (Hecke K q q⁻¹ n)
      = Module.finrank K (∀ lam : Partition (n + 1),
          Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
            (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K) := by
    rw [finrank_hecke_eq_factorialF q hq0 hq2 n, finrank_blocks_eq_factorial (K := K) n]
  exact (LinearMap.injective_iff_surjective_of_finrank_eq_finrank hfr
    (f := (heckeProductF q hq0 hq2 n).toLinearMap)).mpr (heckeProductF_surjective q hq0 hq2 n)

/-- **The Wedderburn isomorphism of `H_{n+1}(q)` over any field**, at `q` not a root of unity. -/
noncomputable def heckeWedderburnF :
    Hecke K q q⁻¹ n ≃ₐ[K] (∀ lam : Partition (n + 1),
      Matrix (StandardYoungTableau (QOU.Mathlib.partitionShape lam))
        (StandardYoungTableau (QOU.Mathlib.partitionShape lam)) K) :=
  AlgEquiv.ofBijective (heckeProductF q hq0 hq2 n)
    ⟨heckeProductF_injective q hq0 hq2 n, heckeProductF_surjective q hq0 hq2 n⟩

theorem heckeWedderburnF_symm_single (lam : Nat.Partition (n + 1))
    (T : StandardYoungTableau (QOU.Mathlib.partitionShape lam)) :
    (heckeWedderburnF q hq0 hq2 n).symm (Pi.single lam (Matrix.single T T 1))
      = jmProjIn q (σ K q q⁻¹ n) (contentVec T) := by
  rw [AlgEquiv.symm_apply_eq]
  exact (heckeProductF_jmProj q hq0 hq2 n lam T).symm

end AnyChar

end QOU.SchurWeyl

