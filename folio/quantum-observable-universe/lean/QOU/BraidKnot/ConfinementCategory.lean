import QOU.BraidKnot.ConfinedParticle
import Mathlib.CategoryTheory.Category.Basic

/-!
# Confinement Category

The category `Conf` has confined particles as objects and
{unfolding, folding, dressing} as morphisms. The Markov trace
extends to a functor `tr_M : Conf → R_q`.

## Design — list-based morphisms (Pattern 4 / no axioms)

A morphism `P → Q` is a list of *atomic* moves
(`unfold`, `fold`, `dress`) chained source-to-target. This
representation makes composition a transparent `cons`/`append`
operation, so the category laws (`id_comp`, `comp_id`, `assoc`) are
**proved by induction**, not asserted as axioms.

The earlier `opaque ConfMorphism.comp` + three category axioms have
been removed: making `comp` transparent eliminates the underlying
need for them.

## References

- [def:confinement-category]
- [def:confined-particle]
- [prop:level-sufficiency]
- [maclane1971] https://doi.org/10.1007/978-1-4757-4721-8 (Ch I)
-/

namespace QOU.BraidKnot

open QOU.Archimedean

/-- **Atomic confinement move.** A single generator of the
    confinement category — unfolding, folding, or dressing. The
    full morphism `P → Q` is a list (chain) of these. -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
inductive AtomicConfMove : ConfinedParticle → ConfinedParticle → Type where
  /-- Unfold `P` to a finer representation `P'`
      (`P.level = P'.level + 1`). -/
  | unfold : (P P' : ConfinedParticle) → P.level = P'.level + 1 →
             AtomicConfMove P P'
  /-- Fold `P` to a coarser representation `P'`
      (`P'.level = P.level + 1`). -/
  | fold : (P P' : ConfinedParticle) → P'.level = P.level + 1 →
           AtomicConfMove P P'
  /-- Dress `P_bare` with a named shell, producing `P_dressed`. -/
  | dress : (P_bare P_dressed : ConfinedParticle) → (shellName : String) →
            AtomicConfMove P_bare P_dressed

/-- **Confinement morphism.** A chain of atomic moves
    `P = X₀ → X₁ → ⋯ → X_n = Q`. The empty chain is the identity;
    composition is list concatenation (defined transparently below
    so the category laws are proved, not axiomatised). -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
inductive ConfMorphism : ConfinedParticle → ConfinedParticle → Type where
  /-- Empty chain — identity morphism on `P`. -/
  | nil : (P : ConfinedParticle) → ConfMorphism P P
  /-- Prepend an atomic move to an existing chain. -/
  | cons : {P Q R : ConfinedParticle} → AtomicConfMove P Q →
           ConfMorphism Q R → ConfMorphism P R

namespace ConfMorphism

/-- Identity morphism on `P` — alias for `nil`. -/
@[simp] def id (P : ConfinedParticle) : ConfMorphism P P := nil P

/-- Smart constructor: a single-step `unfold` morphism. -/
def unfold (P P' : ConfinedParticle) (h : P.level = P'.level + 1) :
    ConfMorphism P P' :=
  cons (AtomicConfMove.unfold P P' h) (nil P')

/-- Smart constructor: a single-step `fold` morphism. -/
def fold (P P' : ConfinedParticle) (h : P'.level = P.level + 1) :
    ConfMorphism P P' :=
  cons (AtomicConfMove.fold P P' h) (nil P')

/-- Smart constructor: a single-step `dress` morphism. -/
def dress (P_bare P_dressed : ConfinedParticle) (shellName : String) :
    ConfMorphism P_bare P_dressed :=
  cons (AtomicConfMove.dress P_bare P_dressed shellName) (nil P_dressed)

/-- **Composition** of confinement morphisms — concatenation of
    chains. Defined by recursion on the second (source-side)
    argument so that `comp_id` is `rfl` and `id_comp`/`assoc`
    follow by structural induction. -/
def comp : {P Q R : ConfinedParticle} →
    ConfMorphism Q R → ConfMorphism P Q → ConfMorphism P R
  | _, _, _, g, .nil _ => g
  | _, _, _, g, .cons a f => .cons a (comp g f)

/-- Unfold lemma for `comp` on a `cons` source — true by definition. -/
@[simp] theorem comp_cons {P P' Q R : ConfinedParticle}
    (g : ConfMorphism Q R) (a : AtomicConfMove P P') (f : ConfMorphism P' Q) :
    comp g (cons a f) = cons a (comp g f) := rfl

/-- **Right-identity law** — `g ∘ id = g`. By definition (`rfl`). -/
@[simp] theorem comp_id_def {P Q : ConfinedParticle}
    (g : ConfMorphism P Q) : comp g (nil P) = g := rfl

/-- **Right-identity law** for the public `id` alias. -/
theorem comp_id {P Q : ConfinedParticle} (f : ConfMorphism P Q) :
    comp f (id P) = f :=
  rfl

/-- **Left-identity law** — `id ∘ f = f`. By induction on `f`. -/
theorem id_comp {P Q : ConfinedParticle} (f : ConfMorphism P Q) :
    comp (id Q) f = f := by
  induction f with
  | nil _ => rfl
  | cons a f' ih => rw [comp_cons, ih]

/-- **Associativity** — `h ∘ (g ∘ f) = (h ∘ g) ∘ f`. By induction
    on the leftmost (source-side) factor `f`. -/
theorem assoc {P Q R S : ConfinedParticle}
    (f : ConfMorphism P Q) (g : ConfMorphism Q R) (h : ConfMorphism R S) :
    comp h (comp g f) = comp (comp h g) f := by
  induction f with
  | nil _ => rfl
  | cons a f' ih => simp [comp_cons, ih]

end ConfMorphism

/-- **Confinement category `Conf`.** The category of confined
    particles with chain-of-atomic-moves morphisms. The composition
    operator is transparent (list concatenation), so the category
    laws are proved theorems — no axioms required. -/
-- Ref: [leitner2026] braids-and-knots/confinement-category
-- Ref: [maclane1971] Mac Lane, "Categories for the Working Mathematician," Springer GTM 5, 1971
instance : CategoryTheory.Category ConfinedParticle where
  Hom := ConfMorphism
  id P := ConfMorphism.id P
  -- Mathlib's `≫` has source-target order `(X ⟶ Y) → (Y ⟶ Z) → (X ⟶ Z)`,
  -- whereas `ConfMorphism.comp` follows the Mac Lane convention
  -- `(Q ⟶ R) → (P ⟶ Q) → (P ⟶ R)`. Bridge by swapping.
  comp f g := ConfMorphism.comp g f
  -- `(𝟙 X) ≫ f = f` — instance's `comp (𝟙 X) f = ConfMorphism.comp f (𝟙 X)`,
  -- which is right-identity in Mac Lane order.
  id_comp f := ConfMorphism.comp_id f
  -- `f ≫ (𝟙 Y) = f` — instance's `comp f (𝟙 Y) = ConfMorphism.comp (𝟙 Y) f`,
  -- which is left-identity in Mac Lane order.
  comp_id f := ConfMorphism.id_comp f
  assoc f g h := ConfMorphism.assoc f g h

end QOU.BraidKnot
