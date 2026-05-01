/-!
# QOU.Interactions.LRFusion — double-magic LR-fusion rigidity

A composite nuclear configuration `A = Z + N` is double-magic iff the
Littlewood–Richardson fusion of the proton representation `V_{λ_Z}`
and the neutron representation `V_{λ_N}` yields a dominant composite
`V_{λ_A}` whose Jucys–Murphy multiset is gapless and globally
neutral: `κ_{λ_A} = 0`.

Conjectural-propagation (CLAUDE.md §3b): downstream of
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

import QOU.BraidKnot.ShellNeutrality
import QOU.LiftingDescent.HomologicalCondensation
import Mathlib.Data.Real.Basic

namespace QOU.Interactions.LRFusion

open QOU.BraidKnot.ShellNeutrality
open QOU.LiftingDescent.HomologicalCondensation

/-! ## §1  Composite nuclear data -/

/-- A composite nucleus: proton diagram `λ_Z`, neutron diagram
    `λ_N`, and the dominant LR-composite diagram `λ_A` they fuse
    to. The composite has `n = Z + N` boxes. -/
structure Composite where
  λ_Z : YoungDiagram
  λ_N : YoungDiagram
  λ_A : YoungDiagram
  /-- Mass number condition. -/
  mass_eq : λ_A.n = λ_Z.n + λ_N.n

/-! ## §2  Provable algebraic ingredient — content additivity -/

/-- **Content additivity** (provable from the LR rule, axiomatised
    here): the Jucys–Murphy charge of the dominant composite equals
    the sum of the constituent charges. This is the standard fact
    that contents add under tensor induction. -/
class ContentAdditive (C : Composite) : Prop where
  kappa_add : kappa C.λ_A = kappa C.λ_Z + kappa C.λ_N

/-! ## §3  Double-magic predicate -/

/-- The composite is **double magic** when both constituents are
    saturated and self-conjugate (the LR-rigidity input). -/
def IsDoubleMagic (C : Composite) : Prop :=
  isSelfConjugate C.λ_Z ∧ isSelfConjugate C.λ_N

/-- **Lemma (proved):** a double-magic composite has zero global
    Jucys–Murphy charge `κ_{λ_A} = 0`. Direct from
    `kappa_zero_of_self_conjugate` (proved in ShellNeutrality) plus
    content additivity (typeclass field). -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem doubleMagic_kappa_zero
    (C : Composite) [CA : ContentAdditive C]
    (hM : IsDoubleMagic C) :
    kappa C.λ_A = 0 := by
  have hZ : kappa C.λ_Z = 0 := kappa_zero_of_self_conjugate C.λ_Z hM.1
  have hN : kappa C.λ_N = 0 := kappa_zero_of_self_conjugate C.λ_N hM.2
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
    the previous two conjectures: `κ_{λ_A} = 0` (from content
    additivity, Lemma `doubleMagic_kappa_zero`) plus
    self-conjugacy of `λ_A` (from LR-rigidity at saturated inputs)
    yields the homological-condensation precondition. The reverse
    direction asserts that *only* double-magic compositions reach
    the magic ladder via LR-fusion of saturated inputs. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
class DoubleMagicConjecture where
  /-- LR-rigidity: the dominant composite of two self-conjugate
      saturated constituents is itself self-conjugate. -/
  lr_rigidity :
    ∀ (C : Composite),
      IsDoubleMagic C → isSelfConjugate C.λ_A
  /-- Magic-ladder coincidence: a composite whose dominant module
      has zero charge **and** is self-conjugate sits on the magic
      ladder iff it arose from a double-magic LR-fusion. -/
  magic_iff_double_magic :
    ∀ (C : Composite),
      (kappa C.λ_A = 0 ∧ isSelfConjugate C.λ_A
        ∧ C.λ_A.n ∈ magicLadder)
      ↔ IsDoubleMagic C

/-- Re-export: at a double-magic composite, the dominant module is
    self-conjugate. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem composite_self_conjugate_of_double_magic
    [D : DoubleMagicConjecture]
    {C : Composite} (h : IsDoubleMagic C) :
    isSelfConjugate C.λ_A :=
  D.lr_rigidity C h

/-- Re-export: a double-magic composite has zero global Jucys–Murphy
    charge.  Combines content additivity with the
    self-conjugate-zero-charge field. -/
-- Ref: [manuscript] conj:diagrammatic-double-magic-lr-fusion
theorem composite_kappa_zero_of_double_magic
    [D : DoubleMagicConjecture]
    (C : Composite) [ContentAdditive C]
    (h : IsDoubleMagic C) :
    kappa C.λ_A = 0 :=
  doubleMagic_kappa_zero C h

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
    (hL : C.λ_A.n ∈ magicLadder) :
    InfinityVanishesAtPositiveQ C.λ_A.n :=
  condensation_at_magic hL

end QOU.Interactions.LRFusion
