/-
# A groupoid has no distinguished terminal object

Scoping lemma for the Epstein–Penner / Ptolemy-groupoid route (issue #6941,
bean `qou-ptgd`).

A recurring proposal frames the canonical (Epstein–Penner) ideal decomposition
of a cusped hyperbolic 3-manifold as *the terminal object* of the groupoid whose
objects are ideal triangulations and whose morphisms are Pachner / flip moves.
This file shows the framing cannot carry that weight, whichever version of the
groupoid is meant, by proving a dichotomy:

* `QOU.Mass.isTerminal_of_isTerminal` — in a groupoid, if **one** object is
  terminal then **every** object is terminal.  So terminality singles out
  nothing, and in particular cannot express the canonicity of a distinguished
  decomposition.
* `QOU.Mass.isEmpty_isTerminal_of_ne_id` — contrapositive: if some object carries a
  non-identity endomorphism (a mapping-class-group element, or a symmetry of the
  manifold acting on its triangulations), then **no** object is terminal.

The mathematical content is one cancellation.  For `f g : X ⟶ Y`, both
`f ≫ t_Y` and `g ≫ t_Y` lie in `X ⟶ T`, which a terminal `T` makes a
subsingleton; in a groupoid `t_Y` is invertible, hence monic, so `f = g`.
Every hom-set is then a singleton and the groupoid is equivalent to the
one-object-one-morphism category.

The hypothesis `Groupoid` is essential and not decoration: a general category
may perfectly well have a terminal object alongside objects with non-trivial
automorphisms.  It is invertibility of `t_Y` that collapses the whole category.

Consequence for the route, stated so it is not over-read: this refutes the
*word*, not the *object*.  A canonical decomposition still exists and is still
unique; it is a distinguished choice natural under isometry — a section of a
forgetful functor, or the unique minimiser of the Epstein–Penner convex-hull
functional — and it is not a limit.  Nothing here says anything about whether a
cell decomposition can carry a many-body term.

Scope: this is a scope-(b) STRUCTURAL exclusion in the sense of AGENTS.md
§"Before declaring refuted"; the invariant cited is the proof below.
-/
import Mathlib.CategoryTheory.Groupoid
import Mathlib.CategoryTheory.Limits.Shapes.Terminal

namespace QOU.Mass

open CategoryTheory CategoryTheory.Limits

universe v u

variable {C : Type u} [Groupoid.{v} C]

/-- In a groupoid, a terminal object collapses *every* hom-set to at most one
morphism.  Right-cancel the invertible `hT.from Y`. -/
theorem hom_subsingleton_of_isTerminal {T : C} (hT : IsTerminal T) (X Y : C) :
    Subsingleton (X ⟶ Y) :=
  ⟨fun _ _ => (cancel_mono (hT.from Y)).mp (hT.hom_ext _ _)⟩

/-- In a groupoid with a terminal object, every hom-set is inhabited: compose
into `T` and back out again.  Together with
`hom_subsingleton_of_isTerminal` this makes every hom-set a singleton. -/
def homOfIsTerminal {T : C} (hT : IsTerminal T) (X Y : C) : X ⟶ Y :=
  hT.from X ≫ Groupoid.inv (hT.from Y)

/-- **First horn.**  In a groupoid, one terminal object makes every object
terminal.  Terminality therefore distinguishes no decomposition from any
other. -/
def isTerminal_of_isTerminal {T : C} (hT : IsTerminal T) (T' : C) : IsTerminal T' :=
  have inst : ∀ X : C, Unique (X ⟶ T') := fun X =>
    haveI : Subsingleton (X ⟶ T') := hom_subsingleton_of_isTerminal hT X T'
    { default := homOfIsTerminal hT X T'
      uniq := fun _ => Subsingleton.elim _ _ }
  @IsTerminal.ofUnique _ _ T' inst

/-- In a groupoid with a terminal object, every endomorphism is the identity. -/
theorem endo_eq_id_of_isTerminal {T : C} (hT : IsTerminal T) {X : C} (f : X ⟶ X) :
    f = 𝟙 X :=
  (hom_subsingleton_of_isTerminal hT X X).elim f (𝟙 X)

/-- **Second horn.**  A single non-identity endomorphism anywhere in a groupoid
rules out a terminal object everywhere.  This is the horn that applies to
Penner's Ptolemy groupoid, whose automorphism groups are mapping-class groups,
and to a Pachner groupoid on symmetry-orbits of triangulations of a manifold
with non-trivial symmetry group. -/
theorem isEmpty_isTerminal_of_ne_id {X : C} {f : X ⟶ X} (hf : f ≠ 𝟙 X) (T : C) :
    IsEmpty (IsTerminal T) :=
  ⟨fun hT => hf (endo_eq_id_of_isTerminal hT f)⟩

/-- The dichotomy in one statement: in a groupoid, either no object is terminal,
or every object is.  There is no middle case in which terminality picks out a
canonical object. -/
theorem terminal_dichotomy :
    (∀ T : C, IsEmpty (IsTerminal T)) ∨ (∀ T : C, Nonempty (IsTerminal T)) := by
  by_cases h : ∀ T : C, IsEmpty (IsTerminal T)
  · exact Or.inl h
  · refine Or.inr fun T' => ?_
    push_neg at h
    obtain ⟨T, hT⟩ := h
    exact ⟨isTerminal_of_isTerminal hT.some T'⟩

end QOU.Mass
