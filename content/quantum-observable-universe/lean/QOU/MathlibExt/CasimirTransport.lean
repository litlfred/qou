import QOU.MathlibExt.CasimirBlockScalar
import QOU.MathlibExt.TraceWeightsOfAlgEquiv

/-!
# QOU.MathlibExt.CasimirTransport — pulling the matrix-unit dual pair back along a splitting

`QOU.MathlibExt.CasimirBlockScalar` proves the left-expansion for the matrix
units on a product of matrix algebras.  `QOU.MathlibExt.CasimirBasisIndependence`
turns such an expansion into a statement about *any* Casimir.  What is missing
between them is that the matrix units, pulled back along a splitting
`E : A ≃ₐ[K] ∏_i M_{d_i}(K)`, still expand — and that is this file.

The proof is bookkeeping, and the only step with content is that `E` is an
*algebra* equivalence, so `t (E.symm u · y) = weightedTrace c (u · E y)`: the
product survives the transport, which is what lets the product-side expansion
be applied at `E y` and then pulled back.

## What is proved

* `pullbackUnit` / `pullbackUnitDual` — the matrix units and their duals,
  pulled back through `E.symm`.
* `sum_pullback_expansion` — they satisfy the left-expansion on `A`.

That is exactly the hypothesis `casimir_eq_of_dual_pair` asks a caller to
supply, so with this the Casimir of any trace on a split algebra is computable
block by block.

Generic over `[Field K]`, `[Ring A]`, `[Algebra K A]` per §7c.
-/

namespace QOU.MathlibExt

open Matrix

section Transport

variable {K : Type*} [Field K]
variable {ι : Type*} [Fintype ι] [DecidableEq ι]
variable {J : ι → Type*} [∀ i, Fintype (J i)] [∀ i, DecidableEq (J i)]
variable {A : Type*} [Ring A] [Algebra K A]

/-- A matrix unit, pulled back to `A` along the splitting. -/
noncomputable def pullbackUnit (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (p : (i : ι) × (J i × J i)) : A :=
  E.symm (blockUnit (K := K) (J := J) p.1 p.2.1 p.2.2)

/-- Its dual, pulled back along the splitting. -/
noncomputable def pullbackUnitDual (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (c : ι → K) (p : (i : ι) × (J i × J i)) : A :=
  E.symm (blockUnitDual (K := K) (J := J) c p.1 p.2.1 p.2.2)

/-- **The pulled-back pair expands.**

    The one step with content: `E` is an *algebra* equivalence, so the product
    survives the transport and the product-side expansion applies at `E y`. -/
theorem sum_pullback_expansion (E : A ≃ₐ[K] ∀ i, Matrix (J i) (J i) K)
    (t : A →ₗ[K] K) (ht : ∀ x y : A, t (x * y) = t (y * x)) (a : ∀ i, J i)
    (hc : ∀ i, traceWeight E t a i ≠ 0) (y : A) :
    (∑ p : (i : ι) × (J i × J i),
        t (pullbackUnit E p * y) • pullbackUnitDual E (traceWeight E t a) p) = y := by
  classical
  set c := traceWeight E t a with hcdef
  have hval : ∀ p : (i : ι) × (J i × J i),
      t (pullbackUnit (J := J) E p * y)
        = weightedTrace c (blockUnit (K := K) (J := J) p.1 p.2.1 p.2.2 * E y) := by
    intro p
    rw [eq_weightedTrace_of_algEquiv E t ht a, pullbackUnit, map_mul,
      AlgEquiv.apply_symm_apply]
  calc (∑ p : (i : ι) × (J i × J i),
          t (pullbackUnit (J := J) E p * y) • pullbackUnitDual E c p)
      = ∑ p : (i : ι) × (J i × J i),
          E.symm (weightedTrace c (blockUnit (K := K) (J := J) p.1 p.2.1 p.2.2 * E y)
            • blockUnitDual (K := K) (J := J) c p.1 p.2.1 p.2.2) := by
        exact Finset.sum_congr rfl fun p _ => by
          rw [hval p, pullbackUnitDual, map_smul]
    _ = E.symm (∑ p : (i : ι) × (J i × J i),
          weightedTrace c (blockUnit (K := K) (J := J) p.1 p.2.1 p.2.2 * E y)
            • blockUnitDual (K := K) (J := J) c p.1 p.2.1 p.2.2) := by
        rw [map_sum]
    _ = y := by
        rw [sum_weightedTrace_blockUnit_mul_smul_blockUnitDual c hc (E y),
          AlgEquiv.symm_apply_apply]

end Transport

end QOU.MathlibExt
