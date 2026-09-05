import QOU.MathlibExt.TraceIsWeighted

/-!
# QOU.MathlibExt.TraceWeightsOfAlgEquiv — a trace's block weights, through a splitting

`QOU.MathlibExt.TraceIsWeighted` shows a trace on `∏_i M_{d_i}(K)` is
`weightedTrace c`.  This file transports that along an algebra equivalence, so
the weights become attached to a trace on an *abstract* split semisimple
algebra `A` — which is where the abstract Schur element lives.

## What is proved

* `traceWeight E t a i` — the weight of block `i`, the value of `t` on the
  pullback of a diagonal matrix unit.
* `traceWeight_indep` — it does not depend on which diagonal unit is chosen.
  (`blockWeight_eq` transported; this is what `tau_mul_comm` was needed for.)
* `eq_weightedTrace_of_algEquiv` — `t x = weightedTrace (traceWeight …) (E x)`.
* `exists_ne_zero_forall_mul_eq_zero_of_traceWeight_eq_zero` — **a vanishing
  weight puts a whole block in the radical**: it exhibits `z ≠ 0` with
  `t (z y) = 0` for every `y`.

That last one is the direction that matters downstream.  Its contrapositive is:
if the form `(x, y) ↦ t(x y)` is nondegenerate, then **every** block weight is
nonzero — so every abstract Schur element `1 / c_λ` exists.  Applied to the
canonical symmetrizing trace, whose Gram determinant
`QOU.Hecke.TwBasis.tauGram_det_ne_zero` computes, that is the statement
`some s_λ = 0 ⟹ the algebra is not split semisimple`.

Nothing here is Hecke-specific and nothing is archimedean: `[Field K]`,
`[Ring A]`, `[Algebra K A]`, per §7c.
-/

namespace QOU.MathlibExt

open Matrix

section Transport

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]
variable {A : Type*} [Ring A] [Algebra K A]

/-- **The weight of block `i`**: the value of `t` on the pullback of a diagonal
    matrix unit.  Well defined independently of the unit — `traceWeight_indep`. -/
def traceWeight (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K) (t : A →ₗ[K] K)
    (a : ∀ i, J i) (i : ι) : K :=
  t (E.symm (blockUnit i (a i) (a i)))

omit [Fintype ι] [DecidableEq ι] in
/-- The composite `t ∘ E.symm` is a trace on the product whenever `t` is one. -/
theorem comp_symm_mul_comm (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K) (t : A →ₗ[K] K)
    (ht : ∀ x y : A, t (x * y) = t (y * x))
    (u v : ∀ i, Matrix (J i) (J i) K) :
    (t.comp E.symm.toLinearMap) (u * v) = (t.comp E.symm.toLinearMap) (v * u) := by
  simp only [LinearMap.comp_apply, AlgEquiv.toLinearMap_apply, map_mul]
  exact ht _ _

omit [Fintype ι] in
/-- **The weight does not depend on which diagonal unit is used.** -/
theorem traceWeight_indep (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K) (t : A →ₗ[K] K)
    (ht : ∀ x y : A, t (x * y) = t (y * x)) (a b : ∀ i, J i) (i : ι) :
    traceWeight E t a i = traceWeight E t b i :=
  apply_blockUnit_diag_eq (t.comp E.symm.toLinearMap) (comp_symm_mul_comm E t ht) i _ _

/-- **A trace on a split algebra is a weighted trace, through the splitting.** -/
theorem eq_weightedTrace_of_algEquiv (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t : A →ₗ[K] K) (ht : ∀ x y : A, t (x * y) = t (y * x)) (a : ∀ i, J i) (x : A) :
    t x = weightedTrace (traceWeight E t a) (E x) := by
  have h := eq_weightedTrace (t.comp E.symm.toLinearMap) (comp_symm_mul_comm E t ht) a (E x)
  simpa [traceWeight] using h

/-- **A vanishing block weight puts a whole block in the radical.**

    If `c_i = 0` then the pullback of the diagonal unit `E^{(i)}_{aa}` is a
    nonzero element `z` with `t (z y) = 0` for *every* `y` — so the form
    `(x, y) ↦ t(x y)` is degenerate.  Contrapositive: a nondegenerate `t` has
    every weight nonzero. -/
theorem exists_ne_zero_forall_mul_eq_zero_of_traceWeight_eq_zero
    (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K) (t : A →ₗ[K] K)
    (ht : ∀ x y : A, t (x * y) = t (y * x)) (a : ∀ i, J i) {i : ι}
    (hc : traceWeight E t a i = 0) :
    ∃ z : A, z ≠ 0 ∧ ∀ y : A, t (z * y) = 0 := by
  refine ⟨E.symm (blockUnit i (a i) (a i)), ?_, ?_⟩
  · intro hz
    have h0 : blockUnit (K := K) (J := J) i (a i) (a i) = 0 := by
      have := congrArg E hz
      simpa using this
    have := congrFun h0 i
    rw [blockUnit_self] at this
    have h1 : (Matrix.single (a i) (a i) (1 : K)) (a i) (a i) = 0 := by rw [this]; rfl
    rw [Matrix.single_apply_same] at h1
    exact one_ne_zero h1
  · intro y
    rw [eq_weightedTrace_of_algEquiv E t ht a, weightedTrace, map_mul,
      AlgEquiv.apply_symm_apply]
    refine Finset.sum_eq_zero ?_
    intro j _
    by_cases hj : j = i
    · subst hj; rw [hc, zero_mul]
    · rw [Pi.mul_apply, blockUnit_of_ne _ _ _ hj, zero_mul, Matrix.trace_zero, mul_zero]

end Transport

end QOU.MathlibExt
