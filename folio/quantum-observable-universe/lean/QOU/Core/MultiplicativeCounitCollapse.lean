/-
Copyright (c) 2026 litlfred. All rights reserved.
-/
import Mathlib.RingTheory.TensorProduct.Basic
import Mathlib.LinearAlgebra.TensorProduct.Finiteness

/-!
# A multiplicative counit collapses a Frobenius algebra (no antipode needed)

The prose definition `def:frobenius-hopf-substrate` once listed, as its axiom 2,
that the counit is multiplicative, `ε(ab) = ε(a)ε(b)`. This file proves that
this axiom alone, together with the Frobenius relation and one counit law,
forces every element to be a scalar multiple of `1`:

  `x = ε(x) • 1`  for every `x : A`.

So the only algebra satisfying the old axiom list is spanned by `1`.

**No antipode is used.** The argument uses no antipode and no
`ConvolutionLeft` hypothesis. That separates it from
`FrobeniusBialgebraCollapse.counit_not_unital_of_nontrivial`, which reaches a
related conclusion from the unit normalisation `ε(1) = 1` plus the antipode.
Note that a multiplicative counit needs no braiding to state
(`μ ≫ ε = (ε ⊗ ε) ≫ λ_`), contrary to the remark in
`FrobeniusBialgebraCollapse.lean`.

The Lean structure `FrobeniusHopfData` has never carried a multiplicative-counit
field, so it is unaffected. This file records why the prose axiom has to go
(bean `qou-aj49`).

## Hypotheses

- `A` is an `R`-algebra over a commutative ring `R` (base ring generic, §7c).
- `comul : A →ₗ[R] A ⊗[R] A` satisfies the right half of the Frobenius relation:
  `comul (x * y) = comul x * (1 ⊗ₜ y)`.
- `counit : A →ₗ[R] R` satisfies the right counit law:
  `rid ((lTensor counit) (comul x)) = x`.
- `counit` is multiplicative: `counit (x * y) = counit x * counit y`.

## Proof

1. The Frobenius relation gives `comul x = comul 1 * (1 ⊗ₜ x)`.
2. Write `comul 1 = Σᵢ aᵢ ⊗ₜ bᵢ`. Then `comul x = Σᵢ aᵢ ⊗ₜ (bᵢ * x)`.
3. The counit law gives `x = Σᵢ ε(bᵢ x) • aᵢ`.
4. Multiplicativity gives `x = ε(x) • Σᵢ ε(bᵢ) • aᵢ`.
5. The counit law at `x = 1` gives `Σᵢ ε(bᵢ) • aᵢ = 1`.
-/

namespace QOU.QuantumObservableUniverse.MultiplicativeCounitCollapse

open TensorProduct

variable {R A : Type*} [CommRing R] [Ring A] [Algebra R A]

/-- The counit-law contraction `rid ∘ lTensor ε` applied to `comul 1 * (1 ⊗ₜ x)`,
when `comul 1 = Σᵢ aᵢ ⊗ₜ bᵢ`, is `Σᵢ ε(bᵢ x) • aᵢ`. Proved by induction on
the tensor `t = comul 1`. -/
theorem contract_mul_one_tmul (counit : A →ₗ[R] R) (t : A ⊗[R] A) (x : A) :
    ∃ (s : Finset (A × A)),
      t = ∑ p ∈ s, p.1 ⊗ₜ[R] p.2 ∧
      TensorProduct.rid R A (counit.lTensor A (t * (1 ⊗ₜ[R] x))) =
        ∑ p ∈ s, counit (p.2 * x) • p.1 := by
  classical
  obtain ⟨s, hs⟩ := TensorProduct.exists_finset (R := R) t
  refine ⟨s, hs, ?_⟩
  subst hs
  simp [Finset.sum_mul, Algebra.TensorProduct.tmul_mul_tmul, map_sum]

/-- **Collapse.** A multiplicative counit on a Frobenius algebra forces
`x = ε(x) • 1` for every `x`. No antipode is used. -/
theorem eq_counit_smul_one
    (comul : A →ₗ[R] A ⊗[R] A) (counit : A →ₗ[R] R)
    (frob : ∀ x y : A, comul (x * y) = comul x * (1 ⊗ₜ[R] y))
    (counit_law : ∀ x : A, TensorProduct.rid R A (counit.lTensor A (comul x)) = x)
    (mul_counit : ∀ x y : A, counit (x * y) = counit x * counit y)
    (x : A) : x = counit x • (1 : A) := by
  classical
  have hx : comul x = comul 1 * (1 ⊗ₜ[R] x) := by
    simpa using frob 1 x
  have h1 : comul 1 = comul 1 * (1 ⊗ₜ[R] (1 : A)) := by
    simpa using frob 1 1
  obtain ⟨s, hs, hsx⟩ := contract_mul_one_tmul counit (comul 1) x
  have hs1 : TensorProduct.rid R A (counit.lTensor A (comul 1 * (1 ⊗ₜ[R] (1 : A)))) =
      ∑ p ∈ s, counit (p.2 * 1) • p.1 := by
    rw [hs]
    simp [Finset.sum_mul, Algebra.TensorProduct.tmul_mul_tmul, map_sum]
  have e1 : (1 : A) = ∑ p ∈ s, counit p.2 • p.1 := by
    have := counit_law 1
    rw [h1, hs1] at this
    simpa using this.symm
  have ex : x = ∑ p ∈ s, counit (p.2 * x) • p.1 := by
    have := counit_law x
    rw [hx, hsx] at this
    exact this.symm
  calc x = ∑ p ∈ s, counit (p.2 * x) • p.1 := ex
    _ = ∑ p ∈ s, counit x • (counit p.2 • p.1) := by
        refine Finset.sum_congr rfl fun p _ => ?_
        rw [mul_counit, smul_smul, mul_comm]
    _ = counit x • ∑ p ∈ s, counit p.2 • p.1 := by rw [Finset.smul_sum]
    _ = counit x • (1 : A) := by rw [← e1]

/-- Consequence: every element of `A` lies in the image of `algebraMap R A`.
So `A` is a quotient of `R`, i.e. at most one-dimensional. -/
theorem surjective_algebraMap
    (comul : A →ₗ[R] A ⊗[R] A) (counit : A →ₗ[R] R)
    (frob : ∀ x y : A, comul (x * y) = comul x * (1 ⊗ₜ[R] y))
    (counit_law : ∀ x : A, TensorProduct.rid R A (counit.lTensor A (comul x)) = x)
    (mul_counit : ∀ x y : A, counit (x * y) = counit x * counit y) :
    Function.Surjective (algebraMap R A) := fun x =>
  ⟨counit x, by
    rw [Algebra.algebraMap_eq_smul_one]
    exact (eq_counit_smul_one comul counit frob counit_law mul_counit x).symm⟩

end QOU.QuantumObservableUniverse.MultiplicativeCounitCollapse
