/-!
# Confinement Category

The category `Conf` has confined particles as objects and
{unfolding, folding, dressing} as morphisms. The Markov trace
extends to a functor `tr_M : Conf → R_q`.

## References

- [def:confinement-category]
- [def:confined-particle]
- [prop:level-sufficiency]
-/

import QOU.BraidKnot.ConfinedParticle
import Mathlib.CategoryTheory.Category.Basic

namespace QOU.BraidKnot

open QOU.Descartes

/-- **Confinement morphism.** A morphism in the confinement
    category: unfolding (to a finer level), folding (to a coarser
    level), or dressing (attach a named shell). -/
-- Ref: [manuscript] braids-and-knots/confinement-category
inductive ConfMorphism : ConfinedParticle → ConfinedParticle → Type where
  /-- Identity morphism on `P`. -/
  | id : (P : ConfinedParticle) → ConfMorphism P P
  /-- Unfold `P` to a finer representation `P'`
      (`P'.level = P.level − 1`, more strands). -/
  | unfold : (P P' : ConfinedParticle) → P.level = P'.level + 1 →
             ConfMorphism P P'
  /-- Fold `P` to a coarser representation `P'`
      (`P'.level = P.level + 1`, fewer strands). -/
  | fold : (P P' : ConfinedParticle) → P'.level = P.level + 1 →
           ConfMorphism P P'
  /-- Dress `P_bare` with a shell, producing `P_dressed`. -/
  | dress : (P_bare P_dressed : ConfinedParticle) → (shellName : String) →
            ConfMorphism P_bare P_dressed

/-- Composition of confinement morphisms. Deferred: categorical
    identity/assoc laws require an equational theory on the
    inductive above. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
opaque ConfMorphism.comp {P Q R : ConfinedParticle}
    (g : ConfMorphism Q R) (f : ConfMorphism P Q) : ConfMorphism P R

/-- Identity law axiom — not derivable without inductive `comp` def. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
axiom ConfMorphism.id_comp {P Q : ConfinedParticle}
    (f : ConfMorphism P Q) :
    ConfMorphism.comp (ConfMorphism.id Q) f = f

/-- Associativity axiom — not derivable without inductive `comp` def. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
axiom ConfMorphism.assoc {P Q R S : ConfinedParticle}
    (f : ConfMorphism P Q) (g : ConfMorphism Q R) (h : ConfMorphism R S) :
    ConfMorphism.comp h (ConfMorphism.comp g f) =
    ConfMorphism.comp (ConfMorphism.comp h g) f

/-- Right identity law axiom — not derivable without inductive `comp` def. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
axiom ConfMorphism.comp_id {P Q : ConfinedParticle}
    (f : ConfMorphism P Q) :
    ConfMorphism.comp f (ConfMorphism.id P) = f

/-- **Confinement category `Conf`.** The category of confined
    particles with {identity, unfolding, folding, dressing}
    morphisms, associative composition, identity laws. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
noncomputable instance : CategoryTheory.Category ConfinedParticle where
  Hom := ConfMorphism
  id P := ConfMorphism.id P
  comp := ConfMorphism.comp
  id_comp := ConfMorphism.id_comp
  comp_id := ConfMorphism.comp_id
  assoc := ConfMorphism.assoc

end QOU.BraidKnot
