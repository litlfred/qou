import QOU.KZ.GLnResidues
import Mathlib.LinearAlgebra.Matrix.Charpoly.Coeff
import Mathlib.RingTheory.Algebraic.Integral
import Mathlib.Analysis.Complex.Polynomial.Basic

/-!
# Non-resonance of `ℏ T` for every integer matrix `T` and transcendental `ℏ`

Stage S2 prerequisite of bean `qou-zoyv`. The KZ residues of the Drinfeld category on tensor
powers of `V` are block Casimirs `t_{X,Y} = ∑_{i ∈ X, j ∈ Y} P_{ij}`, sums of permutation matrices,
hence integer matrices. For any integer matrix `T` the characteristic polynomial has integer
coefficients, so its complex roots `r_i` are algebraic over `ℚ`. By
`GLnResidues.aeval_adL_eq_zero`, `ad_{ℏT}` is killed by `∏_{i,j} (X − ℏ(r_i − r_j))`. So for
`k ≥ 1`, `k = ℏ(r_i − r_j)` would make `ℏ = k/(r_i − r_j)` algebraic. Hence **`ℏ T` is
non-resonant whenever `ℏ` is transcendental** (`nonResonant_smul_intMatrix`). This covers all
block sizes at once, with no spectral computation.

Sorry-free.

-- Ref: [leitner2026] beans/defs/qou-zoyv (stage S2)
-/

namespace QOU.KZ.NonResonantInt

open Polynomial QOU.KZ.FuchsianFormal QOU.KZ.GLnResidues

variable {ι : Type*} [Fintype ι] [DecidableEq ι]

/-- **Non-resonance for integer matrices.** If `M` is an integer matrix and `c ∈ ℂ` is
transcendental over `ℚ`, then `c • M` (over `ℂ`) is non-resonant. -/
theorem nonResonant_smul_intMatrix (M : Matrix ι ι ℤ) (c : ℂ) (hc : Transcendental ℚ c) :
    NonResonant (c • M.map (Int.cast : ℤ → ℂ)) := by
  set T := M.map (Int.cast : ℤ → ℂ)
  set p : ℂ[X] := M.charpoly.map (Int.castRingHom ℂ)
  have hpm : p.Monic := M.charpoly_monic.map _
  have hT : aeval T p = 0 := by
    have := Matrix.aeval_self_charpoly T
    rwa [show T = M.map (Int.castRingHom ℂ) from rfl, Matrix.charpoly_map] at this
  have hsplit : p = (p.roots.map fun a => X - C a).prod := by
    conv_lhs => rw [eq_prod_roots_of_splits_id (IsAlgClosed.splits p)]
    rw [hpm.leadingCoeff, C_1, one_mul]
  set l := p.roots.toList
  set a : Fin l.length → ℂ := fun i => l[i]
  have hprod : (∏ i, (X - C (a i)) : ℂ[X]) = p := by
    calc (∏ i, (X - C (a i)) : ℂ[X]) = (l.map fun x => X - C x).prod :=
          Fin.prod_univ_fun_getElem l (fun x => X - C x)
      _ = p := by rw [← Multiset.prod_coe, ← Multiset.map_coe, Multiset.coe_toList, ← hsplit]
  -- each root is algebraic over `ℚ`
  have halg : ∀ i, IsAlgebraic ℚ (a i) := by
    intro i
    have hmem : a i ∈ p.roots := by
      rw [← Multiset.mem_toList]; exact List.getElem_mem _
    refine ⟨M.charpoly.map (Int.castRingHom ℚ), (M.charpoly_monic.map _).ne_zero, ?_⟩
    have hr := (mem_roots hpm.ne_zero).1 hmem
    rw [IsRoot, show p = (M.charpoly.map (Int.castRingHom ℚ)).map (algebraMap ℚ ℂ) by
      rw [Polynomial.map_map]; congr 1] at hr
    rwa [aeval_def, eval₂_eq_eval_map]
  refine nonResonant_of_aeval (K := ℂ) _ _
    (aeval_adL_eq_zero _ _ (aeval_smul_of_roots a c T (by rw [hprod]; exact hT))) fun k hk => ?_
  simp only [eval_prod, eval_sub, eval_X, eval_C]
  refine Finset.prod_ne_zero_iff.2 fun j _ => Finset.prod_ne_zero_iff.2 fun i _ => ?_
  intro h
  by_cases hij : a i = a j
  · rw [hij, sub_self, sub_zero] at h
    exact (Nat.cast_ne_zero.2 hk.ne') h
  · apply hc
    have hd : a i - a j ≠ 0 := sub_ne_zero.2 hij
    have hc' : c = (k : ℂ) * (a i - a j)⁻¹ := by
      field_simp
      linear_combination -h
    have := (isAlgebraic_algebraMap (R := ℚ) (A := ℂ) (k : ℚ)).mul
      (IsAlgebraic.inv_iff.mpr ((halg i).sub (halg j)))
    rw [hc']
    simpa using this
