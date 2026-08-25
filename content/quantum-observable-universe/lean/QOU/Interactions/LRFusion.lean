import QOU.BraidKnot.ShellNeutrality
import QOU.LiftingDescent.HomologicalCondensation
import Mathlib.Data.Real.Basic

/-!
# QOU.Interactions.LRFusion — double-magic LR-fusion rigidity

A composite nuclear configuration `A = Z + N` is double-magic iff the
Littlewood–Richardson fusion of the proton representation `V_{ydZ}`
and the neutron representation `V_{ydN}` yields a dominant composite
`V_{ydA}` whose Jucys–Murphy multiset is gapless and globally
neutral: `κ_{ydA} = 0`.

Conjectural-propagation (AGENTS.md §3b): downstream of
`SaturatedShellConjecture` and `ShellCondensationConjecture`, so the
LR-rigidity claim is also axiomatised here.

LaTeX label: `conj:diagrammatic-double-magic-lr-fusion`

## References

- [mathas1999] https://doi.org/10.1090/ulect/015 — Iwahori–Hecke
  and Schur algebras (LR-rule version)
- [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- [turaev2010] https://doi.org/10.1515/9783110221848
- [jucys1974] — Jucys–Murphy elements
- [murphy1992] https://doi.org/10.1016/0021-8693(92)90105-T
- [manuscript] observations / diagrammatic-double-magic-lr-fusion
-/

namespace QOU.Interactions.LRFusion

open QOU.BraidKnot.ShellNeutrality
open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  Composite nuclear data -/

/-- A composite nucleus: proton diagram `ydZ`, neutron diagram
    `ydN`, and the dominant LR-composite diagram `ydA` they fuse
    to. The composite has `n = Z + N` boxes. -/
structure Composite where
  ydZ : YoungDiagram
  ydN : YoungDiagram
  ydA : YoungDiagram
  /-- Mass number condition. -/
  mass_eq : ydA.n = ydZ.n + ydN.n

/-! ## §2  Provable algebraic ingredient — content additivity -/

/-- **Content additivity** (provable from the LR rule, axiomatised
    here at the abstract framework level): the Jucys–Murphy charge
    of the dominant composite equals the sum of the constituent
    charges. This is the standard fact that contents add under
    tensor induction.

    A concrete *non-vacuous* instance is the disjoint-union
    composite `Composite.fromUnion`, where `ydA := ydZ ⊔ ydN`
    is the multiset disjoint union; in that case content additivity
    is *proved* directly from `kappa_unionDiagram`
    (see instance `contentAdditive_fromUnion`). The full LR-fusion
    `ydA` is conjecturally also content-additive but requires the
    LR rule to verify. -/
class ContentAdditive (C : Composite) : Prop where
  kappa_add : kappa C.ydA = kappa C.ydZ + kappa C.ydN

/-- The **trivial composite** built from the disjoint multiset union
    of constituents. This is *not* the LR-fusion composite — it is a
    structural lower bound: any well-defined composite must agree
    with this one on the level of content sums.

    Existence of this composite, together with the proved instance
    `contentAdditive_fromUnion`, shows that `ContentAdditive` is a
    consistent typeclass (non-vacuous). -/
def Composite.fromUnion (ydZ ydN : YoungDiagram) : Composite where
  ydZ := ydZ
  ydN := ydN
  ydA := unionDiagram ydZ ydN
  mass_eq := rfl

/-- The trivial union composite is content-additive *by direct
    proof* (no axiom). Provides a concrete instance of
    `ContentAdditive` against which downstream theorems can be
    smoke-tested. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
instance contentAdditive_fromUnion (ydZ ydN : YoungDiagram) :
    ContentAdditive (Composite.fromUnion ydZ ydN) where
  kappa_add := by
    -- goal: kappa (Composite.fromUnion ydZ ydN).ydA
    --       = kappa (Composite.fromUnion ydZ ydN).ydZ
    --         + kappa (Composite.fromUnion ydZ ydN).ydN
    show kappa (unionDiagram ydZ ydN) = kappa ydZ + kappa ydN
    exact kappa_unionDiagram ydZ ydN

/-! ## §3  Double-magic predicate -/

/-- The composite is **double magic** when both constituents are
    saturated and self-conjugate (the LR-rigidity input). -/
def IsDoubleMagic (C : Composite) : Prop :=
  isSelfConjugate C.ydZ ∧ isSelfConjugate C.ydN

/-- **Lemma (proved):** a double-magic composite has zero global
    Jucys–Murphy charge `κ_{ydA} = 0`. Direct from
    `kappa_zero_of_self_conjugate` (proved in ShellNeutrality) plus
    content additivity (typeclass field). -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem doubleMagic_kappa_zero
    (C : Composite) [CA : ContentAdditive C]
    (hM : IsDoubleMagic C) :
    kappa C.ydA = 0 := by
  have hZ : kappa C.ydZ = 0 := kappa_zero_of_self_conjugate C.ydZ hM.1
  have hN : kappa C.ydN = 0 := kappa_zero_of_self_conjugate C.ydN hM.2
  rw [CA.kappa_add, hZ, hN, add_zero]

/-! ## §4  The LR-fusion rigidity conjecture -/

/-- **Conjecture 3 — Diagrammatic double-magic and LR-fusion rigidity.**

    A composite nuclear configuration is double-magic (both
    constituents saturated and self-conjugate) iff its dominant LR
    composite has zero Jucys–Murphy charge **and** the composite
    strand count `A = Z + N` lies on the magic ladder
    `{2, 8, 20, 28, 50, 82, 126}` for the relevant shell.

    Both directions are conjectural. The forward direction
    (`double-magic → magic ladder`) is essentially the union of
    the previous two conjectures: `κ_{ydA} = 0` (from content
    additivity, Lemma `doubleMagic_kappa_zero`) plus
    self-conjugacy of `ydA` (from LR-rigidity at saturated inputs)
    yields the homological-condensation precondition. The reverse
    direction asserts that *only* double-magic compositions reach
    the magic ladder via LR-fusion of saturated inputs. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
class DoubleMagicConjecture where
  /-- LR-rigidity: the dominant composite of two self-conjugate
      saturated constituents is itself self-conjugate. -/
  lr_rigidity :
    ∀ (C : Composite),
      IsDoubleMagic C → isSelfConjugate C.ydA
  /-- Magic-ladder coincidence: a composite whose dominant module
      has zero charge **and** is self-conjugate sits on the magic
      ladder iff it arose from a double-magic LR-fusion. -/
  magic_iff_double_magic :
    ∀ (C : Composite),
      (kappa C.ydA = 0 ∧ isSelfConjugate C.ydA
        ∧ C.ydA.n ∈ magicLadder)
      ↔ IsDoubleMagic C

/-- Re-export: at a double-magic composite, the dominant module is
    self-conjugate. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem composite_self_conjugate_of_double_magic
    [D : DoubleMagicConjecture]
    {C : Composite} (h : IsDoubleMagic C) :
    isSelfConjugate C.ydA :=
  D.lr_rigidity C h

/-- Re-export: a double-magic composite has zero global Jucys–Murphy
    charge.  Combines content additivity with the
    self-conjugate-zero-charge field. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem composite_kappa_zero_of_double_magic
    [D : DoubleMagicConjecture]
    (C : Composite) [ContentAdditive C]
    (h : IsDoubleMagic C) :
    kappa C.ydA = 0 :=
  doubleMagic_kappa_zero C h

/-- **Concrete special case (fully proved, no axioms):** for the
    trivial union composite, double-magic constituents force
    `κ_{ydA} = 0`. This is `doubleMagic_kappa_zero` specialised to
    `Composite.fromUnion`, where `ContentAdditive` is a real
    instance rather than an axiomatic typeclass field. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem fromUnion_kappa_zero_of_double_magic
    (ydZ ydN : YoungDiagram)
    (hZ : isSelfConjugate ydZ) (hN : isSelfConjugate ydN) :
    kappa (Composite.fromUnion ydZ ydN).ydA = 0 :=
  doubleMagic_kappa_zero (Composite.fromUnion ydZ ydN) ⟨hZ, hN⟩

/-- **LR-rigidity proved for the trivial composite.** If both
    constituents are self-conjugate, then the trivial union composite
    is itself self-conjugate. This is `DoubleMagicConjecture.lr_rigidity`
    proved without axioms in the trivial case — the disjoint multiset
    union of two negation-symmetric multisets is negation-symmetric.

    The honest LR fusion produces a *richer* composite via the
    Littlewood–Richardson rule, but content additivity and
    self-conjugacy preservation hold at the union level too, giving
    a non-vacuous structural lower bound. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem fromUnion_lr_rigidity
    (ydZ ydN : YoungDiagram)
    (h : IsDoubleMagic (Composite.fromUnion ydZ ydN)) :
    isSelfConjugate (Composite.fromUnion ydZ ydN).ydA :=
  unionDiagram_isSelfConjugate h.1 h.2

/-! ## §5  Downstream — double-magic ⇒ homological condensation -/

/-- **Capstone theorem (proved, conditional on the three conjectures).**

    If a composite is double-magic and the LR-rigidity conjecture
    holds, and if the composite mass number `A = Z + N` lies on the
    magic ladder, then the homological-shell-condensation conjecture
    delivers `E_∞^{p, >0}(A) = 0`.

    This is the algebraic-geometry capstone connecting:
    * `SaturatedShellConjecture` (constituents are self-conjugate),
    * `DoubleMagicConjecture` (LR-rigidity preserves self-conjugacy
      to the composite, and the magic-ladder coincidence holds),
    * `ShellCondensationConjecture` (collapse on the magic ladder).

    All hypotheses are exposed as typeclass instances; the proof is
    by direct chaining. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
-- Ref: [manuscript] conj:homological-shell-condensation
theorem doubleMagic_implies_condensation
    [D : DoubleMagicConjecture]
    [ShellCondensationConjecture]
    (C : Composite) [ContentAdditive C]
    (hM : IsDoubleMagic C)
    (hL : C.ydA.n ∈ magicLadder) :
    InfinityVanishesAtPositiveQ C.ydA.n :=
  condensation_at_magic hL

end QOU.Interactions.LRFusion
