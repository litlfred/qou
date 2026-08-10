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
[`cor:pbw-corollary`](../../../unital-groebner-bases/buchberger-and-pbw/pbw-corollary.md):
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

* every PBW monomial `m` is in normal form under the `q`-Serre system
  (`pbw_monomials_are_normal_forms`) — the PBW monomials really are the
  `S𝔤`-basis representatives; and
* every element reduces to a *unique* normal form
  (`normal_form_unique` against `qSerre_is_gs_basis`).

The `R`-linear bijection `U𝔤 ≅ S𝔤` itself is not assembled (raw
`AlgElement` data type). The existence/termination half of `ReducesToNF` is
now proved — `normal_form_exists`, from termination plus the
unit-leading-coefficient hypothesis `hlc` (bean qou-lzoo; the axiom it
replaced was **false**). `hlc` is a hypothesis here rather than discharged,
because `qSerreRewritingSystem` is itself an axiom and its rules cannot be
inspected; see the note at the use site. The PBW-normality and uniqueness
halves are discharged by `NormalForms.lean`'s
`pbw_monomials_are_normal_forms` and `normal_form_unique`.
-/

namespace UGB.BuchbergerPBW

open UGB.GrobnerShirshov

universe v

variable {k : Type v} [Field k]

/-- **PBW corollary — `U_q(su(2))` instance.**

    With `qs` the `q`-Serre data: (1) every PBW monomial
    `m = E_+^a K^b E_-^c` is in normal form under the `q`-Serre
    rewriting system, and (2) every element reduces to a unique normal
    form. So the PBW monomials are exactly the canonical representatives
    of `U_q(su(2)) ≅ S𝔤` — the substantive content the former
    `holds : Prop` lacked.

    The conclusion is a **concrete conjunction over real `SU2Gen`
    types** (`isNormalForm` + `ReducesToNF` + uniqueness). -/
-- Ref: [manuscript] unital-groebner-bases/buchberger-and-pbw/pbw-corollary.ts
theorem ugb_pbw_corollary (qs : QSerreRelations k)
    (hlc : ∀ r ∈ (qSerreRewritingSystem k qs).rules,
      IsUnit (r.lc degLexOrder)) :
    (∀ m : PBWMonomial,
       isNormalForm degLexOrder (qSerreRewritingSystem k qs)
         ⟨fun w => if w = m.toMonomial then (1 : k) else 0,
          {m.toMonomial},
          fun w hw => by simp at hw; simp [hw]⟩) ∧
    (∀ f : AlgElement SU2Gen k,
       (∃ nf : AlgElement SU2Gen k,
          ReducesToNF degLexOrder (qSerreRewritingSystem k qs) f nf) ∧
       (∀ nf₁ nf₂ : AlgElement SU2Gen k,
          ReducesToNF degLexOrder (qSerreRewritingSystem k qs) f nf₁ →
          ReducesToNF degLexOrder (qSerreRewritingSystem k qs) f nf₂ →
          nf₁ = nf₂)) := by
  refine ⟨?_, ?_⟩
  · -- PBW monomials are normal forms: NormalForms.lean axiom.
    intro m
    exact pbw_monomials_are_normal_forms k qs m
  · intro f
    refine ⟨?_, ?_⟩
    · -- Existence of the normal form — now proved, from termination plus `hlc`
      -- (bean qou-lzoo); it used to invoke an axiom that is in fact false.
      --
      -- Unlike the "no quasi-zeros" hypothesis below, `hlc` is NOT discharged
      -- here, and deliberately so. `qSerreRewritingSystem` is itself an axiom,
      -- so its rules cannot be inspected to show their leading coefficients are
      -- units — and asserting monicity as a fresh axiom in order to discharge
      -- this one would be assuming the thing, not proving it. The honest place
      -- to close this is a strengthened specification of
      -- `qSerreRewritingSystem` that carries monic rules (the q-Serre relations
      -- are monic by construction, each oriented so its leading monomial has
      -- coefficient 1); until that lands, the dependency stays visible in the
      -- type rather than hidden in an axiom.
      exact normal_form_exists degLexOrder (qSerreRewritingSystem k qs) hlc f
    · -- Uniqueness against the q-Serre GS basis.
      intro nf₁ nf₂ h₁ h₂
      -- The "no quasi-zeros" hypothesis (Leitner–Pawloski) is discharged
      -- here: the ground algebra is the free algebra on `SU2Gen`, which has
      -- generators, so left multiplication by one of them is injective.
      exact normal_form_unique degLexOrder (qSerreRewritingSystem k qs)
        (qSerre_is_gs_basis k qs) (noQuasiZerosFree_of_generator SU2Gen.K)
        f nf₁ nf₂ h₁ h₂

end UGB.BuchbergerPBW
