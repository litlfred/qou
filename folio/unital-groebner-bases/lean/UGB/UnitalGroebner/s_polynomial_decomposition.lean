import UGB.GrobnerShirshov.AlgOps

/-!
# UGB.UnitalGroebner.s_polynomial_decomposition

**Real-content formalization** (replaces the former vacuous
`class … where holds : Prop`). The S-polynomial is built from the
concrete `AlgElement` operations (`AlgOps.lean`: scalar-mul, subtraction),
and the decomposition claim is a genuine **equation in `AlgElement G k`** —
it cannot be instantiated with `True`. The manuscript proof of the base
case is still pending (`sorry`, cited), but the *statement* is now
substantive: this is the §3b-cond real-content template for the UGB
placeholder theorems.

Content block
[`prop:s-polynomial-decomposition`](../../../unital-groebner-bases/unital-groebner-bases-chapter/s-polynomial-decomposition.md):
*$S$-polynomial decomposition of cancelling sums*.

## Manuscript statement

Let $R$ be a commutative ring with unity, $A$ an $R$-algebra free as an
$R$-module, $(B,<)$ an admissible system. Let $\alpha \in B$ and suppose
$f_1,\dots,f_n \in A$ satisfy $\mathrm{LM}(f_i)=\alpha$ and
$\mathrm{LC}(f_i)\in R^\times$. If $f := \sum_i c_i f_i$ (with $c_i\in R$)
satisfies $\mathrm{LM}(f) < \alpha$, then $f = \sum_{i\neq j} d_{i,j}\,S_{i,j}$
where $S_{i,j} := a_i^{-1} f_i - a_j^{-1} f_j$, $a_i := \mathrm{LC}(f_i)$.
-/

namespace UGB.UnitalGroebner

open UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Field k] [DecidableEq G]

/-- The **S-polynomial** about two rules with unit leading coefficients
    `a₁, a₂`:  `S(f₁,f₂) = a₁⁻¹ · f₁  −  a₂⁻¹ · f₂`, built from the
    concrete `AlgElement` scalar-multiplication and subtraction
    (`AlgOps.lean`). A real construction, not an axiom. -/
def sPolynomial (a₁ a₂ : k) (f₁ f₂ : AlgElement G k) : AlgElement G k :=
  AlgElement.sub (AlgElement.smul a₁⁻¹ f₁) (AlgElement.smul a₂⁻¹ f₂)

/-- **S-polynomial decomposition — base (two-rule) case.**

    The two rules `f₁, f₂` share a leading monomial `α` with unit leading
    coefficients `a₁, a₂`; the combination `c₁f₁ + c₂f₂` cancels at `α`
    (`c₁a₁ + c₂a₂ = 0`, i.e. its leading monomial drops strictly below
    `α`). Then the combination is a scalar multiple of the S-polynomial.

    The conclusion is a **concrete `AlgElement` equation** — the real
    content the former `holds : Prop` lacked. The expected witness is
    `d = c₁·a₁`. A complete proof needs coefficient extensionality for
    `AlgElement` (which is a raw data structure, not a quotient — see the
    `AlgOps.lean` §6 design note); supplying that ext principle is the
    remaining manuscript step. -/
-- Ref: [leitner2026] unital-groebner-bases/unital-groebner-bases-chapter/s-polynomial-decomposition.ts
theorem s_polynomial_decomposition
    (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k)
    (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0)
    (hcancel : c₁ * a₁ + c₂ * a₂ = 0) :
    ∃ d : k,
      AlgElement.add (AlgElement.smul c₁ f₁) (AlgElement.smul c₂ f₂)
        = AlgElement.smul d (sPolynomial a₁ a₂ f₁ f₂) := by
  -- Witness d = c₁·a₁: then d·a₁⁻¹ = c₁ and −d·a₂⁻¹ = c₂ (by hcancel,
  -- c₂ = −c₁a₁a₂⁻¹), so the two sides agree coefficient-wise. The
  -- coefficient-wise equality ⇒ AlgElement equality step is the pending
  -- manuscript ext argument (AlgElement is not a quotient type).
  -- Ref: [leitner2026] unital-groebner-bases — s-polynomial-decomposition
  refine ⟨c₁ * a₁, ?_⟩
  rcases f₁ with ⟨coeff₁, supp₁, spec₁⟩
  rcases f₂ with ⟨coeff₂, supp₂, spec₂⟩
  dsimp [AlgElement.add, AlgElement.smul, sPolynomial, AlgElement.sub, AlgElement.neg]
  congr 1
  funext m
  have h3 : c₂ * a₂ = - (c₁ * a₁) := by
    calc c₂ * a₂ = (c₁ * a₁ + c₂ * a₂) - c₁ * a₁ := by ring
         _       = 0 - c₁ * a₁ := by rw [hcancel]
         _       = - (c₁ * a₁) := by ring
  have h2 : c₂ = - (c₁ * a₁) * a₂⁻¹ := by
    calc c₂ = c₂ * (a₂ * a₂⁻¹) := by rw [mul_inv_cancel₀ ha₂, mul_one]
         _  = (c₂ * a₂) * a₂⁻¹ := by ring
         _  = - (c₁ * a₁) * a₂⁻¹ := by rw [h3]
  rw [h2]
  calc c₁ * coeff₁ m + - (c₁ * a₁) * a₂⁻¹ * coeff₂ m
    _ = c₁ * (a₁ * a₁⁻¹) * coeff₁ m - c₁ * a₁ * a₂⁻¹ * coeff₂ m := by rw [mul_inv_cancel₀ ha₁, mul_one]; ring
    _ = (c₁ * a₁) * (a₁⁻¹ * coeff₁ m + - (a₂⁻¹ * coeff₂ m)) := by ring

end UGB.UnitalGroebner
