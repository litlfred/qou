import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.GroupTheory.Perm.Basic
import Mathlib.Tactic

/-!
# Pairwise decomposition of a braided interaction

Every interaction among `n` strands in a braided monoidal category is a
composite of *elementary crossings*, each of which involves exactly two
adjacent strands.  There is no primitive `n`-ary interaction operator: the
braiding is a binary natural isomorphism, and the hexagon axioms determine
how it acts on composite objects.  This file records the three facts that
license the rest of the chapter to study two-particle interactions only.

1. `composite_crossing_eq_two_elementary` — passing a composite `X ⊗ Y` past
   `Z` is the composite of the two elementary crossings `c_{Y,Z}` and
   `c_{X,Z}` (the hexagon).
2. `triple_crossing_route_independent` — the two ways of resolving a triple
   crossing agree.  This is the Yang–Baxter equation, equivalently the
   Reidemeister move of type III.
3. `three_crossings_needed` — two elementary crossings never bring all three
   pairs of three strands into contact; three are required.

Parts 1 and 2 are the categorical content; part 3 is the counting statement
that fixes the *number* of pairwise events a genuine three-body interaction
costs.

## References

- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
- Ref: [turaev2010] https://doi.org/10.1515/9783110221848
-/

namespace QOU.Braiding

open CategoryTheory CategoryTheory.MonoidalCategory CategoryTheory.BraidedCategory

universe v u

variable {C : Type u} [Category.{v} C] [MonoidalCategory C] [BraidedCategory C]

/-! ### Part 1 — composite interactions reduce to pairwise ones -/

/-- **Composite reduction.**  Passing the composite system `X ⊗ Y` past `Z`
    is not a new ternary operation: it is the elementary crossing of `Y` past
    `Z` followed by the elementary crossing of `X` past `Z`, reassociated.

    In a strict monoidal category the associators drop out and the statement
    reads `c_{X⊗Y, Z} = (c_{X,Z} ⊗ id_Y) ∘ (id_X ⊗ c_{Y,Z})`. -/
theorem composite_crossing_eq_two_elementary (X Y Z : C) :
    (β_ (X ⊗ Y) Z).hom =
      (α_ X Y Z).hom ≫ X ◁ (β_ Y Z).hom ≫ (α_ X Z Y).inv ≫
        (β_ X Z).hom ▷ Y ≫ (α_ Z X Y).hom :=
  braiding_tensor_left_hom X Y Z

/-! ### Part 2 — the two resolutions of a triple crossing agree -/

/-- **Route independence (Yang–Baxter, Reidemeister III).**  A degenerate
    triple crossing has two perturbations into a triangle of three pairwise
    crossings — slide the third strand above, or below.  The two sequences
    are equal, so the decomposition into pairwise events is well defined
    even though the order of the events is not. -/
theorem triple_crossing_route_independent (X Y Z : C) :
    (α_ X Y Z).inv ≫ (β_ X Y).hom ▷ Z ≫ (α_ Y X Z).hom ≫
      Y ◁ (β_ X Z).hom ≫ (α_ Y Z X).inv ≫ (β_ Y Z).hom ▷ X ≫ (α_ Z Y X).hom =
    X ◁ (β_ Y Z).hom ≫ (α_ X Z Y).inv ≫ (β_ X Z).hom ▷ Y ≫
      (α_ Z X Y).hom ≫ Z ◁ (β_ X Y).hom :=
  yang_baxter X Y Z

/-- **Pairwise decomposition of a braided interaction.**  The conjunction of
    the two categorical facts: a composite interaction *reduces* to pairwise
    ones, and that reduction is *independent of the route taken*. -/
theorem pairwise_interaction_decomposition (X Y Z : C) :
    ((β_ (X ⊗ Y) Z).hom =
        (α_ X Y Z).hom ≫ X ◁ (β_ Y Z).hom ≫ (α_ X Z Y).inv ≫
          (β_ X Z).hom ▷ Y ≫ (α_ Z X Y).hom)
      ∧
    ((α_ X Y Z).inv ≫ (β_ X Y).hom ▷ Z ≫ (α_ Y X Z).hom ≫
        Y ◁ (β_ X Z).hom ≫ (α_ Y Z X).inv ≫ (β_ Y Z).hom ▷ X ≫ (α_ Z Y X).hom =
      X ◁ (β_ Y Z).hom ≫ (α_ X Z Y).inv ≫ (β_ X Z).hom ▷ Y ≫
        (α_ Z X Y).hom ≫ Z ◁ (β_ X Y).hom) :=
  ⟨composite_crossing_eq_two_elementary X Y Z,
   triple_crossing_route_independent X Y Z⟩

/-! ### Part 3 — a three-body interaction costs three pairwise events -/

/-- The `i`-th elementary crossing, read on three strands as the adjacent
    transposition exchanging strands `i` and `i + 1`. -/
def adj (i : Fin 2) : Equiv.Perm (Fin 3) :=
  Equiv.swap i.castSucc i.succ

/-- The permutation of three strands realised by a word in the elementary
    crossings. -/
def braidPerm : List (Fin 2) → Equiv.Perm (Fin 3)
  | [] => 1
  | i :: w => adj i * braidPerm w

/-- The strand pairs that have crossed: those pairs `i < j` whose order the
    word reverses.  Two strands interact exactly when their order is
    reversed. -/
def crossedPairs (σ : Equiv.Perm (Fin 3)) : Finset (Fin 3 × Fin 3) :=
  Finset.univ.filter fun p => p.1 < p.2 ∧ σ p.2 < σ p.1

/-- Three strands have three pairs, so a fully interacting three-body state
    needs `crossedPairs` of cardinality `3`. -/
theorem card_all_pairs :
    (Finset.univ.filter fun p : Fin 3 × Fin 3 => p.1 < p.2).card = 3 := by
  decide

/-- The empty word crosses nothing. -/
theorem crossedPairs_nil : (crossedPairs (braidPerm [])).card = 0 := by
  decide

/-- A single elementary crossing brings exactly one pair into contact. -/
theorem crossedPairs_one (a : Fin 2) : (crossedPairs (braidPerm [a])).card = 1 := by
  fin_cases a <;> decide

/-- **Two elementary crossings are not enough.**  Whichever two elementary
    crossings are chosen, at least one of the three strand pairs never
    crosses. -/
theorem crossedPairs_two_lt_three (a b : Fin 2) :
    (crossedPairs (braidPerm [a, b])).card < 3 := by
  fin_cases a <;> fin_cases b <;> decide

/-- **Three pairwise crossings are required.**  A word in the elementary
    crossings that brings all three pairs of three strands into contact has
    length at least three.

    This is the counting half of the pairwise-decomposition principle: a
    genuine three-body interaction is not two two-body interactions.  It is
    three. -/
theorem three_crossings_needed (w : List (Fin 2))
    (h : (crossedPairs (braidPerm w)).card = 3) : 3 ≤ w.length := by
  match w with
  | [] => simp [crossedPairs_nil] at h
  | [a] => rw [crossedPairs_one a] at h; exact absurd h (by decide)
  | [a, b] => exact absurd h (Nat.ne_of_lt (crossedPairs_two_lt_three a b))
  | _ :: _ :: _ :: _ => simp

end QOU.Braiding
