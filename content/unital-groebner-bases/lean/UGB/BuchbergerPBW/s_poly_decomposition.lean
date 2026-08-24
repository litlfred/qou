import UGB.GrobnerShirshov.AlgOps

/-!
# UGB.BuchbergerPBW.s_poly_decomposition

**Real-content formalization** (replaces the former vacuous
`class … where holds : Prop`). The S-polynomial is built from the
concrete `AlgElement` operations (`AlgOps.lean`: scalar-mul,
subtraction), and the decomposition claim is a genuine **equation in
`AlgElement G k`** — it cannot be instantiated with `True`. This is the
`BuchbergerPBW` companion of
`UGB.UnitalGroebner.s_polynomial_decomposition`, proving the same base
(two-rule) case of the manuscript's telescoping decomposition.

Content block
[`prop:ugb-s-poly-decomposition`](../../../unital-groebner-bases/buchberger-and-pbw/ugb-s-polynomial-decomposition.md):
*$S$-polynomial decomposition*.

## Manuscript statement

Let $R$ be a commutative ring with unity, $A$ an $R$-algebra free as an
$R$-module, $(B,<)$ an admissible system. Let $\alpha\in B$ and
$f_1,\dots,f_n\in A$ with $\mathrm{LM}(f_i)=\alpha$ and
$\mathrm{LC}(f_i)=a_i\in R^\times$. If $f:=\sum_i c_i f_i$ has
$\mathrm{LM}(f)<\alpha$ then $f=\sum_{i\neq j} d_{i,j} S_{i,j}$ where
$S_{i,j}:=a_i^{-1}f_i - a_j^{-1}f_j$. The proof telescopes:
$f = c_1a_1 S_{1,2} + (c_1a_1+c_2a_2)S_{2,3} + \cdots$.

## What is weakened relative to the manuscript

The manuscript states the full $n$-term telescoping sum. We formalize
the **base ($n=2$) case**: a single S-polynomial captures the cancelling
combination $c_1f_1+c_2f_2$ (with the cancellation hypothesis
$c_1a_1+c_2a_2=0$, the $\mathrm{LM}(f)<\alpha$ condition at $n=2$). The
conclusion is a **concrete `AlgElement` equation**; the expected witness
is $d=c_1a_1$. Completing it (and the general $n$) needs coefficient
extensionality for `AlgElement` (a raw data type, not a quotient — see
`AlgOps.lean` §6); supplying that ext principle is the remaining
manuscript step, carried by the single cited `sorry`.
-/

namespace UGB.BuchbergerPBW

open UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Field k] [DecidableEq G]

/-- The **S-polynomial** about two rules with unit leading coefficients
    `a₁, a₂`: `S(f₁,f₂) = a₁⁻¹·f₁ − a₂⁻¹·f₂`, built from the concrete
    `AlgElement` scalar-multiplication and subtraction (`AlgOps.lean`).
    A real construction, not an axiom. -/
def sPoly (a₁ a₂ : k) (f₁ f₂ : AlgElement G k) : AlgElement G k :=
  AlgElement.sub (AlgElement.smul a₁⁻¹ f₁) (AlgElement.smul a₂⁻¹ f₂)

/-- **S-polynomial decomposition — base (two-rule) case.**

    The two rules `f₁, f₂` share a leading monomial `α` with unit
    leading coefficients `a₁, a₂`; the combination `c₁f₁ + c₂f₂` cancels
    at `α` (`c₁a₁ + c₂a₂ = 0`). Then the combination is a scalar multiple
    of the S-polynomial (witness `d = c₁·a₁`), which is the $n=2$ head of
    the manuscript's telescoping sum.

    The conclusion is a **concrete `AlgElement` equation** — the real
    content the former `holds : Prop` lacked. A complete proof needs
    coefficient extensionality for `AlgElement` (a raw data structure;
    see `AlgOps.lean` §6); supplying that ext principle is the remaining
    manuscript step. -/
-- Ref: [manuscript] unital-groebner-bases/buchberger-and-pbw/ugb-s-polynomial-decomposition.ts
theorem s_poly_decomposition
    (a₁ a₂ c₁ c₂ : k) (f₁ f₂ : AlgElement G k)
    (ha₁ : a₁ ≠ 0) (ha₂ : a₂ ≠ 0)
    (hcancel : c₁ * a₁ + c₂ * a₂ = 0) :
    ∃ d : k,
      AlgElement.add (AlgElement.smul c₁ f₁) (AlgElement.smul c₂ f₂)
        = AlgElement.smul d (sPoly a₁ a₂ f₁ f₂) := by
  -- Witness d = c₁·a₁: then d·a₁⁻¹ = c₁ and −d·a₂⁻¹ = c₂ (from hcancel,
  -- c₂ = −c₁a₁a₂⁻¹), so both sides agree coefficient-wise. The
  -- coefficient-wise equality ⇒ AlgElement equality step is the pending
  -- manuscript ext argument (AlgElement is not a quotient type).
  -- Ref: [manuscript] unital-groebner-bases — s-polynomial-decomposition (base case)
  refine ⟨c₁ * a₁, ?_⟩
  rcases f₁ with ⟨coeff₁, supp₁, spec₁⟩
  rcases f₂ with ⟨coeff₂, supp₂, spec₂⟩
  dsimp [AlgElement.add, AlgElement.smul, sPoly, AlgElement.sub, AlgElement.neg]
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

end UGB.BuchbergerPBW
