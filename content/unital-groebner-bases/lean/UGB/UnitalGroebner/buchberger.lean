import UGB.GrobnerShirshov.CompositionLemma

/-!
# UGB.UnitalGroebner.buchberger

**Real-content formalization** (replaces the former vacuous
`class … where holds : Prop`). Buchberger's theorem is stated as its
operational consequence over the concrete reduction system: a
Gröbner–Shirshov basis is **confluent** — any two multi-step reducts of
the same element have a common reduct. The conclusion is a concrete
existential over `AlgElement` / `MultiStepReduction`, not a bare `Prop`,
and is **fully proved** from the composition-lemma `confluence`.

Content block
[`thm:buchberger`](../../../unital-groebner-bases/unital-groebner-bases-chapter/buchberger.md):
*Buchberger's theorem over commutative rings*.

## Manuscript statement

Let $R$ be a commutative ring with unity, $A$ an $R$-algebra free as an
$R$-module, $(B,<)$ an admissible system, $I \leq A$ an ideal generated
by a unital set $G=\{g_\gamma\mid\gamma\in\Gamma\}$. Then $G$ is a
Gröbner–Shirshov basis for $I$ iff all S-polynomials for $G$ have zero
remainder under the division algorithm.

## What is weakened relative to the manuscript

The full biconditional (with the "zero-remainder of all S-polynomials"
side) is recorded separately, on the concrete S-polynomial structures,
in `BuchbergerPBW.buchberger_theorem`. Here we formalize the principal
*content* of "G is a Gröbner–Shirshov basis": the resulting reduction is
**confluent**. Operationally this is what makes the division algorithm
well-defined — it is the property that distinguishes a GS basis from an
arbitrary generating set. The statement is a concrete existence of a
common reduct (`MultiStepReduction`), proved from the `confluence`
result of `CompositionLemma.lean` (itself the Newman's-lemma corollary
of the resolved S-polynomials). No `sorry`.
-/

namespace UGB.UnitalGroebner

open UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [Ring k] [DecidableEq G]

/-- **Buchberger's theorem — confluence consequence.**

    A Gröbner–Shirshov basis `sys` is confluent: whenever `f →* g₁` and
    `f →* g₂`, there is a common reduct `h` with `g₁ →* h` and
    `g₂ →* h`. This is the operational meaning of "`G` is a GS basis for
    `I`" — the division algorithm produces well-defined remainders.

    The conclusion is a **concrete existential over `AlgElement`** (a
    common `MultiStepReduction` target), not a bare `Prop`. Proved from
    `confluence`. -/
-- Ref: [manuscript] unital-groebner-bases/unital-groebner-bases-chapter/buchberger.ts
theorem buchberger
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (f g₁ g₂ : AlgElement G k)
    (h₁ : MultiStepReduction ord sys f g₁)
    (h₂ : MultiStepReduction ord sys f g₂) :
    ∃ h : AlgElement G k,
      MultiStepReduction ord sys g₁ h ∧ MultiStepReduction ord sys g₂ h :=
  -- Confluence of a GS basis (Newman's lemma over the resolved S-polys).
  confluence ord sys hgs f g₁ g₂ h₁ h₂

end UGB.UnitalGroebner
