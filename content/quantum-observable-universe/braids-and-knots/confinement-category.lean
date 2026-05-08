/-!
# QOU.BraidKnot.ConfinementCategory

The category `Conf` has confined particles as objects and
{unfolding, folding, dressing} as morphisms. The Markov trace
extends to a functor `tr_M : Conf → ℂ(q)`.

LaTeX: `\label{def:confinement-category}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- Placeholder for a confined particle, resolved by
    `QOU.BraidKnot.ConfinedParticle` in the sibling file. -/
-- Ref: [manuscript] braids-and-knots/confined-particle
opaque ConfinedParticleTy : Type

/-- Morphism family in the confinement category: unfolding (to a
    finer level), folding (to a coarser level), or dressing
    (attach an electron shell). -/
-- Ref: [manuscript] braids-and-knots/confinement-category
inductive ConfMorphism : ConfinedParticleTy → ConfinedParticleTy → Type where
  /-- Unfold `P` to a finer representation `P'` (strand count grows). -/
  | unfold : ∀ (P P' : ConfinedParticleTy), ConfMorphism P P'
  /-- Fold `P` to a coarser representation `P'` (strand count shrinks). -/
  | fold   : ∀ (P P' : ConfinedParticleTy), ConfMorphism P P'
  /-- Dress `P_bare` with an electron shell (strand count grows by Z). -/
  | dress  : ∀ (P_bare P_dressed : ConfinedParticleTy)
               (shellName : String), ConfMorphism P_bare P_dressed

/-- Identity morphism on any object. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
opaque ConfId : ∀ (P : ConfinedParticleTy), ConfMorphism P P

/-- Composition of confinement morphisms. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
opaque ConfComp :
    ∀ {P Q R : ConfinedParticleTy},
      ConfMorphism Q R → ConfMorphism P Q → ConfMorphism P R

/-- **Confinement category.** The axioms of a category (associativity
    of composition, identity laws) hold on the structure above. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
theorem ConfinementCategory
    (P Q R S : ConfinedParticleTy)
    (f : ConfMorphism P Q) (g : ConfMorphism Q R) (h : ConfMorphism R S) :
    ConfComp h (ConfComp g f) = ConfComp (ConfComp h g) f := by
  -- Ref: [manuscript] braids-and-knots/confined-particle
  sorry

end QOU.BraidKnot
