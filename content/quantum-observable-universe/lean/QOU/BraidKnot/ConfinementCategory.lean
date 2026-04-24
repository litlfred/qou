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

/-- Identity law for the confinement category. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
theorem ConfMorphism.id_comp {P Q : ConfinedParticle}
    (f : ConfMorphism P Q) :
    ConfMorphism.comp (ConfMorphism.id Q) f = f := by
  -- NOT PROVABLE: `ConfMorphism.comp` is `opaque`.
  -- STRUCTURAL FIX: replace the opaque declaration with an inductive
  -- definition by cases on `f` (id, unfold, fold, dress).  Example:
  --
  --   def ConfMorphism.comp : ConfMorphism P Q → ConfMorphism Q R →
  --                           ConfMorphism P R
  --     | .id _, g => g
  --     | .unfold _ _ h, .id _ => .unfold _ _ h
  --     | .unfold _ _ h, .unfold _ _ h' => .unfold _ _ (by omega)
  --     | ...  -- enumerate the 16 constructor combinations
  --
  -- Then identity/associativity laws follow by `rfl` or small case work.
  -- Ref: [manuscript] braids-and-knots/confinement-category
  sorry

/-- Associativity for the confinement category. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
theorem ConfMorphism.assoc {P Q R S : ConfinedParticle}
    (f : ConfMorphism P Q) (g : ConfMorphism Q R) (h : ConfMorphism R S) :
    ConfMorphism.comp h (ConfMorphism.comp g f) =
    ConfMorphism.comp (ConfMorphism.comp h g) f := by
  -- NOT PROVABLE: same root cause as id_comp — `comp` is opaque.
  -- See the fix sketch above.  Once `comp` is inductively defined,
  -- associativity is ~16 cases on the morphism constructors.
  -- Ref: [manuscript] braids-and-knots/confinement-category
  sorry

/-- **Confinement category `Conf`.** The category of confined
    particles with {identity, unfolding, folding, dressing}
    morphisms, associative composition, identity laws. -/
-- Ref: [manuscript] braids-and-knots/confinement-category
noncomputable instance : CategoryTheory.Category ConfinedParticle where
  Hom := ConfMorphism
  id P := ConfMorphism.id P
  comp := ConfMorphism.comp
  id_comp := ConfMorphism.id_comp
  comp_id f := by
    -- NOT PROVABLE: same root cause (`comp` is opaque).  Once `comp`
    -- is inductively defined, `comp_id` is a single-case rewrite:
    --   comp f (id _) = f  by definition of comp on (_, .id _)
    -- Ref: [manuscript] braids-and-knots/confinement-category
    sorry
  assoc := ConfMorphism.assoc

end QOU.BraidKnot
