import UGB.GrobnerShirshov.NormalForms

/-!
# UGB.BuchbergerPBW.ugb_pbw_corollary

**Real-content formalization** (replaces the former vacuous
`class … where holds : Prop`). The PBW corollary `U𝔤 ≅ S𝔤` is stated
on the **concrete `U_q(su(2))` instance**: the PBW monomials
`E_+^a K^b E_-^c` (`PBWMonomial`) are exactly the normal forms of the
`q`-Serre rewriting system, and reduction gives each element a unique
normal form. The conclusion is a concrete `isNormalForm` /
`ReducesToNF` claim over real `SU2Gen` types — not a bare `Prop`.

Content block
[`cor:ugb-pbw`](../../../unital-groebner-bases/buchberger-and-pbw/ugb-pbw-corollary.md):
*Poincaré–Birkhoff–Witt theorem over a commutative ring*.

## Manuscript statement

For a Lie algebra $\mathfrak g$ over a commutative ring $R$,
$U\mathfrak g = T\mathfrak g/J$ is $R$-module isomorphic to
$S\mathfrak g$; the PBW basis arises as the Gröbner–Shirshov normal
forms of the commutator relations $G = \{x_ix_j - x_jx_i - [x_i,x_j]\}$.

## What is weakened relative to the manuscript

The abstract isomorphism is instantiated on the **`U_q(su(2))`
realisation** carried by `NormalForms.lean`, where the GS basis is the
`q`-Serre system `qSerreRewritingSystem` and the PBW basis is the
divided-power basis `{E_+^a K^b E_-^c}` (`PBWMonomial`). We state two
concrete consequences:

* ~~every PBW monomial `m` is in normal form under the `q`-Serre system~~
  — **withdrawn: this is false as it was stated**, see below; and
* every element reduces to a *unique* normal form
  (`normal_form_unique` against `qSerre_is_gs_basis`).

The `R`-linear bijection `U𝔤 ≅ S𝔤` itself is not assembled (raw
`AlgElement` data type).

## The PBW-normality half was withdrawn (bean qou-ix9e)

It rested on the axiom `pbw_monomials_are_normal_forms`, which became
checkable once `qSerreRewritingSystem` was built rather than axiomatised —
and it fails. `PBWMonomial.toMonomial` lays the letters out as
`E_+^a K^{b₊} K⁻¹^{b₋} E_-^c`, and three of its joins are leading monomials
of the system: `[K,K⁻¹]`, `[K,E_-]`, `[E_+,E_-]`. So those words are
*reducible*, not normal.
`NormalForms.pbw_monomials_are_not_all_normal_forms` proves the negation at
`⟨0,1,1,0⟩`, which is the word `[K,K⁻¹]` — rule 1's leading monomial exactly.

The letter order `E_+ … K … E_-` is simply not this system's normal-form
order: reading the orientations off the rules, reduction moves `E_-` left past
`E_+` and moves `K` right past both, so normal words are `E_-^c E_+^a K^b`
with `K` and `K⁻¹` never mixed. Establishing *that* is the genuine remaining
content of Bokut–Malcolmson Thm 3.2 and is open, so this theorem no longer
claims it rather than importing it from a false axiom.

The existence/termination half is proved (`normal_form_exists`, bean
qou-lzoo), and its unit-leading-coefficient hypothesis is now **discharged**
by `qSerre_rules_monic` — the thing that was left hanging when the system was
opaque.
-/

namespace UGB.BuchbergerPBW

open UGB.GrobnerShirshov

universe v

variable {k : Type v} [Field k]

/-- **PBW corollary — `U_q(su(2))` instance.**

    With `qs` the `q`-Serre data: every element reduces to a **unique** normal
    form under the `q`-Serre rewriting system. Existence is
    `normal_form_exists` (termination + monic rules, both discharged here);
    uniqueness is `normal_form_unique` against `qSerre_is_gs_basis`.

    The former first conjunct — "every PBW monomial is in normal form" — is
    **gone, because it is false**; see the module docstring and
    `NormalForms.pbw_monomials_are_not_all_normal_forms`. What survives is a
    statement about `ReducesToNF` over real `SU2Gen` types, and it no longer
    depends on any refuted claim. -/
-- Ref: [leitner2026] unital-groebner-bases/buchberger-and-pbw/ugb-pbw-corollary.ts
theorem ugb_pbw_corollary (qs : QSerreRelations k) :
    (∀ f : AlgElement SU2Gen k,
       (∃ nf : AlgElement SU2Gen k,
          ReducesToNF degLexOrder (qSerreRewritingSystem k qs) f nf) ∧
       (∀ nf₁ nf₂ : AlgElement SU2Gen k,
          ReducesToNF degLexOrder (qSerreRewritingSystem k qs) f nf₁ →
          ReducesToNF degLexOrder (qSerreRewritingSystem k qs) f nf₂ →
          AlgElement.CoeffEq nf₁ nf₂)) := by
  · intro f
    refine ⟨?_, ?_⟩
    · -- Existence of the normal form: proved, and its unit-leading-coefficient
      -- hypothesis is now **discharged** rather than assumed.
      --
      -- bean qou-lzoo left it hanging on purpose: `qSerreRewritingSystem` was an
      -- axiom, so its rules could not be inspected, and asserting monicity as a
      -- fresh axiom would have been assuming the thing. The system is now built
      -- (`NormalForms.lean` §3.1), so `qSerre_rules_monic` proves it outright.
      exact normal_form_exists degLexOrder (qSerreRewritingSystem k qs)
        (qSerre_rules_monic k qs) f
    · -- Uniqueness against the q-Serre GS basis.
      intro nf₁ nf₂ h₁ h₂
      -- The "no quasi-zeros" hypothesis (Leitner–Pawloski) is discharged
      -- here: the ground algebra is the free algebra on `SU2Gen`, which has
      -- generators, so left multiplication by one of them is injective.
      exact normal_form_unique degLexOrder (qSerreRewritingSystem k qs)
        (qSerre_is_gs_basis k qs) (noQuasiZerosFree_of_generator SU2Gen.K)
        (qSerre_rules_monic k qs) f nf₁ nf₂ h₁ h₂

end UGB.BuchbergerPBW
