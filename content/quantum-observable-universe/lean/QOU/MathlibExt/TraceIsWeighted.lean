import QOU.MathlibExt.WeightedTraceGram
import Mathlib.LinearAlgebra.Matrix.StdBasis

/-!
# QOU.MathlibExt.TraceIsWeighted — every trace on a product of matrix algebras is weighted

`QOU.MathlibExt.WeightedTraceGram` computes the Gram determinant of
`weightedTrace c`.  It does **not** establish that the traces one cares about
have that shape; its docstring asserted it as motivation.  This file proves it.

On `A = ∏_i M_{d_i}(K)`, a linear functional `t` satisfying `t(xy) = t(yx)` is
exactly `weightedTrace c` with

  `c i = t (E^{(i)}_{aa})`   (any diagonal matrix unit of block `i`).

Two one-line matrix-unit identities do all the work, and both are *consequences
of the trace property*, not extra hypotheses:

* `E_ab = E_aa · E_ab` while `E_ab · E_aa = 0` for `b ≠ a` — so a trace kills
  every off-diagonal unit;
* `E_aa = E_ab · E_ba` and `E_bb = E_ba · E_ab` — so a trace is *constant* on
  the diagonal units of a block, which is what makes `c i` well defined
  independently of the chosen `a`.

## Why it is worth a file

It is the step that turns the Gram determinant into a statement about a
*named* trace.  In particular it is what lets the Wedderburn block weights of
the canonical symmetrizing trace `τ` (`QOU.Hecke.TauSymmetrizing`,
`QOU.Hecke.TauStructureConstants`) be **defined** rather than assumed — the
abstract Schur element is `1 / c_λ`, and without well-definedness of `c_λ`
there is no such object.

## What is proved

* `weightedTraceₗ` — `weightedTrace` bundled as a `LinearMap`.
* `blockUnitBasis` — the matrix units are a basis of the product; its elements
  are exactly `blockUnit`.
* `apply_blockUnit_of_ne` / `apply_blockUnit_diag_eq` — the two identities.
* `eq_weightedTrace` — **the theorem**.
* `blockWeight_eq` — the weight read off any diagonal unit.

Generic over `[Field K]` with no ordering and no archimedean structure, per the
§7c base-ring convention.
-/

namespace QOU.MathlibExt

open Matrix

section Weighted

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]

/-- `weightedTrace c` as a linear map. -/
def weightedTraceₗ (c : ι → K) : (∀ i, Matrix (J i) (J i) K) →ₗ[K] K where
  toFun := weightedTrace c
  map_add' x y := by
    simp only [weightedTrace, Pi.add_apply, Matrix.trace_add, mul_add]
    exact Finset.sum_add_distrib
  map_smul' r x := by
    simp only [weightedTrace, Pi.smul_apply, Matrix.trace_smul, smul_eq_mul,
      RingHom.id_apply, Finset.mul_sum]
    exact Finset.sum_congr rfl fun i _ => by ring

omit [DecidableEq ι] [∀ i, DecidableEq (J i)] in
@[simp] theorem weightedTraceₗ_apply (c : ι → K) (x : ∀ i, Matrix (J i) (J i) K) :
    weightedTraceₗ c x = weightedTrace c x := rfl

/-- **The matrix units are a basis of the product**, indexed exactly as
    `weightedGram` is. -/
noncomputable def blockUnitBasis :
    Module.Basis ((i : ι) × (J i × J i)) K (∀ i, Matrix (J i) (J i) K) :=
  Pi.basis fun i => Matrix.stdBasis K (J i) (J i)

@[simp] theorem blockUnitBasis_apply (p : (i : ι) × (J i × J i)) :
    blockUnitBasis (K := K) (J := J) p = blockUnit p.1 p.2.1 p.2.2 := by
  rw [blockUnitBasis, Pi.basis_apply, Matrix.stdBasis_eq_single, blockUnit]

/-! ### The two matrix-unit identities -/

omit [Fintype ι] in
/-- **A trace kills off-diagonal matrix units.**  `E_ab = E_aa E_ab` while
    `E_ab E_aa = 0` when `b ≠ a`. -/
theorem apply_blockUnit_of_ne (t : (∀ i, Matrix (J i) (J i) K) →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) (i : ι) {a b : J i} (hab : a ≠ b) :
    t (blockUnit (K := K) (J := J) i a b) = 0 := by
  have hsplit : blockUnit (K := K) (J := J) i a b
      = blockUnit (K := K) (J := J) i a a * blockUnit (K := K) (J := J) i a b := by
    funext j
    by_cases hj : j = i
    · subst hj
      simp
    · simp [blockUnit_of_ne _ _ _ hj]
  have hba : b ≠ a := Ne.symm hab
  have hzero : blockUnit (K := K) (J := J) i a b * blockUnit (K := K) (J := J) i a a = 0 := by
    funext j
    by_cases hj : j = i
    · subst hj
      simp [hba]
    · simp [blockUnit_of_ne _ _ _ hj]
  rw [hsplit, ht, hzero, map_zero]

omit [Fintype ι] in
/-- **A trace is constant on the diagonal units of a block.**  `E_aa = E_ab E_ba`
    and `E_bb = E_ba E_ab`, so the two values agree.  This is what makes the
    block weight independent of the chosen diagonal unit. -/
theorem apply_blockUnit_diag_eq (t : (∀ i, Matrix (J i) (J i) K) →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) (i : ι) (a b : J i) :
    t (blockUnit (K := K) (J := J) i a a) = t (blockUnit (K := K) (J := J) i b b) := by
  have h1 : blockUnit (K := K) (J := J) i a a
      = blockUnit (K := K) (J := J) i a b * blockUnit (K := K) (J := J) i b a := by
    funext j
    by_cases hj : j = i
    · subst hj; simp
    · simp [blockUnit_of_ne _ _ _ hj]
  have h2 : blockUnit (K := K) (J := J) i b a * blockUnit (K := K) (J := J) i a b
      = blockUnit (K := K) (J := J) i b b := by
    funext j
    by_cases hj : j = i
    · subst hj; simp
    · simp [blockUnit_of_ne _ _ _ hj]
  rw [h1, ht, h2]

/-! ### The theorem -/

/-- **Every trace on a product of matrix algebras is a weighted trace.**

    `t(xy) = t(yx)` forces `t = Σ_i c_i · tr(x_i)` with `c_i` the value of `t`
    on any diagonal matrix unit of block `i`. -/
theorem eq_weightedTrace (t : (∀ i, Matrix (J i) (J i) K) →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) (a : ∀ i, J i)
    (x : ∀ i, Matrix (J i) (J i) K) :
    t x = weightedTrace (fun i => t (blockUnit (K := K) (J := J) i (a i) (a i))) x := by
  have hmap : t = weightedTraceₗ (J := J)
      (fun i => t (blockUnit (K := K) (J := J) i (a i) (a i))) := by
    refine Module.Basis.ext (blockUnitBasis (K := K) (J := J)) ?_
    rintro ⟨i, b, c⟩
    rw [blockUnitBasis_apply, weightedTraceₗ_apply, weightedTrace]
    have hblk : ∀ j, (blockUnit (K := K) (J := J) i b c j).trace
        = if j = i then (if b = c then (1 : K) else 0) else 0 := by
      intro j
      by_cases hj : j = i
      · subst hj
        rcases eq_or_ne b c with rfl | hbc
        · simp [Matrix.trace_single_eq_same]
        · simp [Matrix.trace_single_eq_of_ne _ _ _ hbc, hbc]
      · simp [hj]
    simp only [hblk, mul_ite, mul_one, mul_zero, Finset.sum_ite_eq', Finset.mem_univ,
      if_true]
    by_cases hbc : b = c
    · subst hbc
      rw [if_pos rfl]
      exact apply_blockUnit_diag_eq t ht i b (a i)
    · rw [if_neg hbc]
      exact apply_blockUnit_of_ne t ht i hbc
  exact DFunLike.congr_fun hmap x

omit [Fintype ι] in
/-- The block weight, read off any diagonal unit — independent of the choice. -/
theorem blockWeight_eq (t : (∀ i, Matrix (J i) (J i) K) →ₗ[K] K)
    (ht : ∀ x y, t (x * y) = t (y * x)) (i : ι) (a b : J i) :
    t (blockUnit (K := K) (J := J) i a a) = t (blockUnit (K := K) (J := J) i b b) :=
  apply_blockUnit_diag_eq t ht i a b

end Weighted

end QOU.MathlibExt
