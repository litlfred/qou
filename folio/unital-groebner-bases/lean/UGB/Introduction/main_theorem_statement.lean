import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.CompositionLemma

/-!
# UGB.Introduction.main_theorem_statement

**Real-content formalization** (replaces the former vacuous
`class … where holds : Prop`). The freeness theorem is stated as a
**concrete claim about the reduction system** `RewritingSystem G k`:
for a Gröbner–Shirshov basis, every algebra element has a *unique*
normal form (the canonical representative of its class in `A/I`), and
distinct elements of the remainder module `Õ(G)` — already in normal
form — are their own representatives. This is the module-isomorphism
content `A/I ≅ Õ(G)` at the level of the canonical-form map: it
cannot be instantiated with `True`.

Content block
[`thm:ugb-main-theorem-statement`](../../../unital-groebner-bases/introduction/ugb-main-theorem-statement.md):
*Freeness of quotient by unital Gröbner–Shirshov basis*.

## Manuscript statement

Let $R$ be a commutative algebra with unity, $A$ an $R$-algebra free as
an $R$-module without quasi-zeros, $(B,<)$ an admissible system, and
$I \trianglelefteq A$ a two-sided ideal with a unital Gröbner–Shirshov
basis $G$. Let $\widetilde{O}(G)$ be the free $R$-module spanned by the
monomials that are *not* leading monomials of members of $G$. Then
(1) $A/I \cong \widetilde{O}(G)$ as free $R$-modules, and
(2) $A = I \oplus \widetilde{O}(G)$.

## What is weakened relative to the manuscript

The manuscript asserts a full $R$-module isomorphism and direct-sum
decomposition. We state its **algorithmic core**: the canonical-form
map $A \to \widetilde{O}(G)$ is well-defined (existence) and
class-injective (uniqueness of normal forms). Concretely this is the
conjunction of `ReducesToNF` (every element reaches a normal form,
i.e. an element of `Õ(G)`) and `normal_form_unique` (the normal form is
unique), which is exactly the statement that each `A/I`-class has a
unique `Õ(G)`-representative. The `R`-linearity of the resulting
bijection and the internal-direct-sum statement are not formalized
here (they require the full module structure on `AlgElement`, which is
a raw data type — see `AlgOps.lean` §6). Both halves are now proved:
*existence* is `normal_form_exists`, from `reduction_well_founded` plus
the hypothesis `hlc` that every rule has a unit leading coefficient
(bean qou-lzoo — the axiom of that name it used to invoke was **false**,
refuted in `NormalFormExistsRefutation`); *uniqueness* is
`normal_form_unique`.
-/

namespace UGB.Introduction

open UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [CommRing k] [DecidableEq G]

/-- **Freeness theorem — canonical-form core.**

    For a Gröbner–Shirshov basis `sys` (admissible order `ord`), every
    algebra element `f` admits a normal form, and *any two* normal
    forms of `f` coincide. The normal forms are precisely the elements
    of the remainder module `Õ(G)` (those whose support avoids every
    leading monomial of `sys`), so this is the statement that the
    canonical-form map `A → Õ(G)` descends to a well-defined injection
    `A/I ↪ Õ(G)` — the substantive content the former `holds : Prop`
    lacked.

    The conclusion is a **concrete conjunction over `AlgElement`** (an
    existential `ReducesToNF` plus a `∀`-uniqueness clause), not a bare
    `Prop` field.

    **Restated 2026-11-20 (bean `qou-lc7q`):** over a commutative ring, with
    uniqueness up to `CoeffEq`. The structural form (`nf₁ = nf₂`) is false: a
    normal form is determined only up to its free `support` field
    (`LocalConfluenceSupportRefutation`). -/
-- Ref: [leitner2026] unital-groebner-bases/introduction/ugb-main-theorem-statement.ts
theorem main_theorem_statement
    (ord : AdmissibleOrder G)
    (sys : RewritingSystem G k)
    (hgs : IsGrobnerShirshovBasis G k ord sys)
    (hnqz : NoQuasiZerosFree G k)
    (hlc : ∀ r ∈ sys.rules, IsUnit (r.lc ord)) :
    ∀ f : AlgElement G k,
      (∃ nf : AlgElement G k, ReducesToNF ord sys f nf) ∧
      (∀ nf₁ nf₂ : AlgElement G k,
        ReducesToNF ord sys f nf₁ → ReducesToNF ord sys f nf₂ →
          AlgElement.CoeffEq nf₁ nf₂) := by
  intro f
  refine ⟨?_, ?_⟩
  · -- Existence: no longer "the single remaining manuscript step" invoking an
    -- axiom — it is `normal_form_exists`, proved from termination plus `hlc`
    -- (bean qou-lzoo). The axiom it replaced was not merely unproved but false.
    exact normal_form_exists ord sys hlc f
  · -- Uniqueness: fully discharged by the proved composition-lemma
    -- corollary `normal_form_unique` (confluence of a GS basis).
    intro nf₁ nf₂ h₁ h₂
    exact normal_form_unique ord sys hgs hnqz hlc f nf₁ nf₂ h₁ h₂

end UGB.Introduction
