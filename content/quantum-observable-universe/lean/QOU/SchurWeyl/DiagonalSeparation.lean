import Mathlib.Data.Matrix.Basis
import Mathlib.Data.Matrix.Basic
import Mathlib.Algebra.Algebra.Subalgebra.Basic
import Mathlib.Tactic

/-!
# QOU.SchurWeyl.DiagonalSeparation — separating diagonals generate the diagonal matrix units

A purely algebraic brick, with no Hecke or tableau content: if a subalgebra `A` of
`Matrix ι ι R` contains a family of **diagonal** matrices whose entry-tuples **separate** the
index set, then `A` contains every diagonal matrix unit `single i i 1`.

This is finite-set Lagrange interpolation, written as a product rather than a sum: for each
`j ≠ i` pick a member of the family whose `i`- and `j`-entries differ, and multiply the
corresponding normalised differences.  The product is `1` at `i` — every factor is — and `0` at
any other `U`, because the factor indexed by `j = U` vanishes there.

**Why the separation hypothesis is the whole content.** Diagonal alone gives nothing: a family of
diagonal matrices all of whose entry-tuples agree on two indices can never distinguish them, and
the subalgebra it generates cannot contain either matrix unit.  Separation is exactly the missing
ingredient, and it is what `SeminormalSimpleSpectrum.seminormalRep_qJM_spectrum_injective`
supplies for the `q`-Jucys–Murphy family.

Stated over a `Field R` because the normalisation divides by `d i v − d j v`; the index type is a
`Fintype` with `DecidableEq`, and the family index `V` need only be nonempty.

LaTeX label: `lem:separating-diagonals-generate-units`
-/

namespace QOU.SchurWeyl

variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {R : Type*} [Field R]
variable {V : Type*} [Nonempty V]

/-- **Separating diagonals generate the diagonal matrix units.**  If `A` contains
`diagonal (d · v)` for every `v`, and the tuples `d i ·` separate the indices, then
`single i i 1 ∈ A` for every `i`. -/
theorem single_self_mem_of_separating (A : Subalgebra R (Matrix ι ι R)) (d : ι → V → R)
    (hmem : ∀ v : V, Matrix.diagonal (fun i => d i v) ∈ A)
    (hsep : ∀ i j : ι, i ≠ j → ∃ v : V, d i v ≠ d j v) (i : ι) :
    Matrix.single i i (1 : R) ∈ A := by
  classical
  -- a separating index for every `j`, total (arbitrary and unused at `j = i`)
  have htot : ∀ j : ι, ∃ v : V, j ≠ i → d i v ≠ d j v := by
    intro j
    by_cases h : j = i
    · exact ⟨Classical.arbitrary V, fun hne => absurd h hne⟩
    · obtain ⟨v, hv⟩ := hsep i j (Ne.symm h)
      exact ⟨v, fun _ => hv⟩
  choose w hw using htot
  -- the normalised difference indexed by `j`; at `U = i` it is `1`, at `U = j` it is `0`
  set g : ι → ι → R := fun j U => (d i (w j) - d j (w j))⁻¹ * (d U (w j) - d j (w j)) with hg
  have hfactor_mem : ∀ j : ι, Matrix.diagonal (fun U => g j U) ∈ A := by
    intro j
    have hconst : Matrix.diagonal (fun _ : ι => d j (w j))
        = (d j (w j)) • (1 : Matrix ι ι R) := by
      ext U W
      by_cases h : U = W <;>
        simp [Matrix.smul_apply, h]
    have hrw : Matrix.diagonal (fun U => g j U)
        = (d i (w j) - d j (w j))⁻¹ •
            (Matrix.diagonal (fun U => d U (w j)) - Matrix.diagonal (fun _ : ι => d j (w j))) := by
      ext U W
      by_cases h : U = W <;>
        simp [hg, Matrix.smul_apply, smul_eq_mul, h]
    rw [hrw, hconst]
    exact Subalgebra.smul_mem _
      (sub_mem (hmem (w j)) (Subalgebra.smul_mem _ (one_mem _) _)) _
  -- Matrices do not form a `CommMonoid`, so the product is taken in `ι → R` (which does) and
  -- `diagonal` is applied once; membership then comes by induction on the index set, using that
  -- `diagonal` is multiplicative.
  set P := Matrix.diagonal (∏ j ∈ Finset.univ.erase i, (fun U => g j U)) with hP
  have hprod_mem : ∀ s : Finset ι, Matrix.diagonal (∏ j ∈ s, (fun U => g j U)) ∈ A := by
    intro s
    refine Finset.induction_on s ?_ ?_
    · simpa only [Finset.prod_empty, Matrix.diagonal_one] using one_mem A
    · intro j t hj ih
      rw [Finset.prod_insert hj]
      have hmul : Matrix.diagonal ((fun U => g j U) * ∏ k ∈ t, (fun U => g k U))
          = Matrix.diagonal (fun U => g j U)
              * Matrix.diagonal (∏ k ∈ t, (fun U => g k U)) := by
        have := map_mul (Matrix.diagonalRingHom ι R) (fun U => g j U)
          (∏ k ∈ t, (fun U => g k U))
        simpa only [Matrix.diagonalRingHom_apply] using this
      rw [hmul]
      exact mul_mem (hfactor_mem j) ih
  have hPmem : P ∈ A := hprod_mem _
  -- value at `i`: every factor is `1`
  have hPi : (∏ j ∈ Finset.univ.erase i, (fun U => g j U)) i = 1 := by
    rw [Finset.prod_apply]
    refine Finset.prod_eq_one (fun j hj => ?_)
    have hji : j ≠ i := (Finset.mem_erase.mp hj).1
    have hne : d i (w j) - d j (w j) ≠ 0 := sub_ne_zero_of_ne (hw j hji)
    show (d i (w j) - d j (w j))⁻¹ * (d i (w j) - d j (w j)) = 1
    exact inv_mul_cancel₀ hne
  -- value at any `U ≠ i`: the factor indexed by `j = U` vanishes there
  have hPU : ∀ U : ι, U ≠ i → (∏ j ∈ Finset.univ.erase i, (fun U => g j U)) U = 0 := by
    intro U hU
    rw [Finset.prod_apply]
    refine Finset.prod_eq_zero (Finset.mem_erase.mpr ⟨hU, Finset.mem_univ U⟩) ?_
    show (d i (w U) - d U (w U))⁻¹ * (d U (w U) - d U (w U)) = 0
    rw [sub_self, mul_zero]
  have hPeq : P = Matrix.single i i (1 : R) := by
    ext U W
    by_cases hUW : U = W
    · subst hUW
      by_cases hUi : U = i
      · subst hUi
        simp only [hP, Matrix.diagonal_apply_eq, hPi, Matrix.single, Matrix.of_apply,
          and_self]
        simp
      · simp only [hP, Matrix.diagonal_apply_eq, hPU U hUi, Matrix.single, Matrix.of_apply]
        rw [if_neg]
        rintro ⟨rfl, -⟩
        exact hUi rfl
    · simp only [hP, Matrix.diagonal_apply_ne _ hUW, Matrix.single, Matrix.of_apply]
      rw [if_neg]
      rintro ⟨rfl, rfl⟩
      exact hUW rfl
  exact hPeq ▸ hPmem

/-- **The matrix units generate everything.**  A subalgebra containing every `single i j 1` is all
of `Matrix ι ι R`, since every matrix is the sum of its entries times the units. -/
theorem eq_top_of_single_mem (A : Subalgebra R (Matrix ι ι R))
    (h : ∀ i j : ι, Matrix.single i j (1 : R) ∈ A) : A = ⊤ := by
  refine eq_top_iff.mpr (fun x _ => ?_)
  rw [Matrix.matrix_eq_sum_single x]
  refine sum_mem (fun i _ => sum_mem (fun j _ => ?_))
  have : Matrix.single i j (x i j) = (x i j) • Matrix.single i j (1 : R) := by
    rw [Matrix.smul_single, smul_eq_mul, mul_one]
  rw [this]
  exact Subalgebra.smul_mem _ (h i j) _

end QOU.SchurWeyl
