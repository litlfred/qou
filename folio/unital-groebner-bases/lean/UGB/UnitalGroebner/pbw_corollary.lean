import UGB.GrobnerShirshov.Basic
import UGB.GrobnerShirshov.CompositionLemma

/-!
# UGB.UnitalGroebner.pbw_corollary

**Real-content formalization** (replaces the former vacuous
`class … where holds : Prop`). The PBW corollary `U𝔤 ≅ S𝔤` is stated
as its Gröbner–Shirshov core: the canonical-form map `U𝔤 → S𝔤` is
class-injective (normal forms — the PBW monomials — are unique) and
total (every element reduces to a PBW normal form). The conclusion is a
**concrete claim over `AlgElement`**, not a bare `Prop`.

Content block
[`cor:pbw-corollary`](../../../unital-groebner-bases/unital-groebner-bases-chapter/pbw-corollary.md):
*Poincaré–Birkhoff–Witt theorem over commutative rings*.

## Manuscript statement

For a Lie algebra $\mathfrak{g}$ over a commutative ring $R$ with unity,
the universal enveloping algebra
$U\mathfrak{g} = T\mathfrak{g}/J$ (with
$J = (xy - yx - [x,y]_{\mathfrak g})$) is isomorphic as an $R$-module to
the symmetric algebra $S\mathfrak{g}$. (When $R$ is a $\mathbb Q$-algebra
this is the GS-basis route to the Lie-algebra / smooth-formal-group
equivalence.)

## What is weakened relative to the manuscript

The manuscript asserts a full $R$-module isomorphism
$U\mathfrak{g}\cong S\mathfrak{g}$. We state the **PBW-basis core** at
the level of the canonical-form map: with the Serre/commutator relations
of $U\mathfrak g$ presented as a GS basis `sys`, the normal-form
monomials are the PBW monomials $S\mathfrak g$, every element reduces to
one (`ReducesToNF`), and that normal form is unique
(`normal_form_unique`). Together these say each `U𝔤`-class has a unique
$S\mathfrak g$-representative — the bijective PBW correspondence. The
`R`-linearity of the bijection is not formalized (raw `AlgElement` data
type, `AlgOps.lean` §6). Both halves are now proved: existence by
`normal_form_exists` (from termination plus the unit-leading-coefficient
hypothesis `hlc` — bean qou-lzoo; the axiom it replaced was false), and
uniqueness by `normal_form_unique`.
-/

namespace UGB.UnitalGroebner

open UGB.GrobnerShirshov

universe u v

variable {G : Type u} {k : Type v} [CommRing k] [DecidableEq G]

/-- **PBW corollary — canonical-form core.**

    Presenting `U𝔤` by a Gröbner–Shirshov basis `sys`, every element
    reduces to a normal form (a PBW monomial / element of `S𝔤`), and any
    two normal forms of the same element coincide. This is the bijective
    PBW correspondence `U𝔤 ↔ S𝔤` at the canonical-form level.

    The conclusion is a **concrete conjunction over `AlgElement`** — a
    `ReducesToNF` existential plus a `∀`-uniqueness clause — the
    substantive content the former `holds : Prop` lacked.

    **Restated 2026-11-20 (bean `qou-lc7q`):** over a commutative ring, with
    uniqueness up to `CoeffEq`. The structural form (`nf₁ = nf₂`) is false: a
    normal form is determined only up to its free `support` field
    (`LocalConfluenceSupportRefutation`). -/
-- Ref: [leitner2026] unital-groebner-bases/unital-groebner-bases-chapter/pbw-corollary.ts
theorem pbw_corollary
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
  · -- Existence of the PBW normal form — now a theorem, not the false axiom it
    -- used to invoke (bean qou-lzoo). `hlc` is what makes it true: without unit
    -- leading coefficients an element can be stuck, reducible-looking with no
    -- reduction available (`NormalFormExistsRefutation`).
    exact normal_form_exists ord sys hlc f
  · -- Uniqueness of the PBW representative: proved via normal_form_unique.
    intro nf₁ nf₂ h₁ h₂
    exact normal_form_unique ord sys hgs hnqz hlc f nf₁ nf₂ h₁ h₂

end UGB.UnitalGroebner
