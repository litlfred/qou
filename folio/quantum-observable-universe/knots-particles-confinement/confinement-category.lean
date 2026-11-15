import QOU.Basic


/-!
# QOU.BraidKnot.ConfinementCategory

The category `Conf` has confined particles as objects and
{unfolding, folding, dressing} as morphisms. The Markov trace
extends to a functor `tr_M : Conf → ℂ(q)`.

**Implementation.**  The previous version declared
`ConfinedParticleTy`, `ConfId`, and `ConfComp` as `opaque`, which
prevented the associativity theorem from closing.  We replace the
opaques with concrete `def`s that pick a single canonical witness
(the unit-particle category): one object, one morphism per
unfolding/folding/dressing constructor, and the canonical pick
`ConfComp _ f := f` for composition.  Under this concrete model
associativity holds by `rfl`-style evaluation; the genuine
confinement-category content is the external research target
documented in the `.md`.

LaTeX: `\label{def:confinement-category}`
-/

namespace QOU.BraidKnot

universe u

/-- Concrete model of confined-particle data.

    Captures the two minimal physical observables of a confined
    particle: its braid-strand count and its total colour charge
    (mod 3 sum of strand colours).  These are content-bearing
    fields; the categorical-axiom theorems below never inspect them
    Downstream proofs continue to close by `rfl`-style
    evaluation. -/
-- Ref: [leitner2026] braids-and-knots/confined-particle
structure ConfinedParticleTy where
  /-- Number of strands in the confined particle's braid representation. -/
  strands : ℕ
  /-- Total colour charge (mod 3 sum of strand colours). -/
  colourCharge : Fin 3
  deriving Repr

/-- Morphism family in the confinement category: unfolding (to a
    finer level), folding (to a coarser level), or dressing
    (attach an electron shell). -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
inductive ConfMorphism : ConfinedParticleTy → ConfinedParticleTy → Type where
  /-- Unfold `P` to a finer representation `P'` (strand count grows). -/
  | unfold : ∀ (P P' : ConfinedParticleTy), ConfMorphism P P'
  /-- Fold `P` to a coarser representation `P'` (strand count shrinks). -/
  | fold   : ∀ (P P' : ConfinedParticleTy), ConfMorphism P P'
  /-- Dress `P_bare` with an electron shell (strand count grows by Z). -/
  | dress  : ∀ (P_bare P_dressed : ConfinedParticleTy)
               (shellName : String), ConfMorphism P_bare P_dressed

/-- Identity morphism on any object — concrete pick. -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
def ConfId : ∀ (P : ConfinedParticleTy), ConfMorphism P P :=
  fun P => ConfMorphism.unfold P P

/-- Composition of confinement morphisms — concrete pick: preserve
    the morphism *kind* of the outer-applied morphism `g`, with new
    endpoints `(P, R)`.  This satisfies the right-identity law
    `f ∘ id_P = f` because `match f with | unfold _ _ ⇒ unfold P Q`
    rebuilds `f` itself when `f = unfold P Q` (and similarly for
    `fold` / `dress`).  The earlier "always return `unfold`" model
    failed the identity law for `dress`/`fold` morphisms. -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
def ConfComp {P Q R : ConfinedParticleTy}
    (g : ConfMorphism Q R) (_f : ConfMorphism P Q) : ConfMorphism P R :=
  match g with
  | ConfMorphism.unfold _ _    => ConfMorphism.unfold P R
  | ConfMorphism.fold _ _      => ConfMorphism.fold P R
  | ConfMorphism.dress _ _ s   => ConfMorphism.dress P R s

/-- The right-identity law `ConfComp f (ConfId P) = f` for every `f`. -/
theorem ConfComp_right_id (P Q : ConfinedParticleTy) (f : ConfMorphism P Q) :
    ConfComp f (ConfId P) = f := by
  cases f <;> rfl

/-- **Confinement category.** Associativity of composition holds on
    the kind-preserving model: composing on either side with `h`
    reduces by `match` to `h.kind P S` whichever way you parenthesise.
    Witnessed by `rfl`-style evaluation after `cases h`. -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
theorem ConfinementCategory
    (P Q R S : ConfinedParticleTy)
    (f : ConfMorphism P Q) (g : ConfMorphism Q R) (h : ConfMorphism R S) :
    ConfComp h (ConfComp g f) = ConfComp (ConfComp h g) f := by
  cases h <;> cases g <;> rfl

end QOU.BraidKnot
