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
3. `card_allPairs_le_length` — a word in elementary crossings whose net
   permutation reverses *every* one of the `C(n,2)` strand pairs has length
   at least `C(n,2)`.  For three strands that is three crossings; two never
   suffice.

Parts 1 and 2 are the categorical content and are inherited from Mathlib's
braided-category library.  Part 3 is the counting statement that fixes the
*number* of pairwise events a genuine many-body interaction costs; it is
proved here from scratch.

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

/-! ### Part 3 — an `n`-body interaction costs `C(n,2)` pairwise events

The braid word is read through its action on strand positions.  Two strands
have interacted when the word reverses their order; the elementary crossings
are the `n - 1` transpositions of adjacent positions.  The content of this
section is that each such crossing reverses at most one *new* pair, so the
number of interacting pairs is bounded by the length of the word. -/

variable {n : ℕ}

/-- An elementary crossing exchanges two strand positions adjacent in the
    order.  There are `n - 1` of these, the Artin generators. -/
structure AdjSwap (n : ℕ) where
  /-- The lower of the two exchanged positions. -/
  lo : Fin n
  /-- The upper of the two exchanged positions. -/
  hi : Fin n
  /-- The two positions are adjacent. -/
  adj : lo.val + 1 = hi.val

namespace AdjSwap

variable (s : AdjSwap n)

theorem lo_ne_hi : s.lo ≠ s.hi := by
  intro h; have := s.adj; rw [h] at this; omega

/-- The permutation realised by an elementary crossing. -/
def perm : Equiv.Perm (Fin n) := Equiv.swap s.lo s.hi

/-- **An elementary crossing can newly reverse only the pair it acts on.**
    If `u < v` but the crossing puts them in the opposite order, then `u` and
    `v` are precisely the two exchanged positions.

    This is the whole content of the counting bound: a crossing is a *local*
    event, so it cannot bring an arbitrary pair of strands into contact. -/
theorem eq_of_reverses {u v : Fin n} (huv : u < v)
    (h : s.perm v < s.perm u) : u = s.lo ∧ v = s.hi := by
  have hadj := s.adj
  have hvuv : u.val < v.val := huv
  simp only [perm] at h
  rcases eq_or_ne u s.lo with hu | hu
  · rcases eq_or_ne v s.hi with hv | hv
    · exact ⟨hu, hv⟩
    · exfalso
      have hvlo : v ≠ s.lo := by rw [← hu]; exact (ne_of_gt huv)
      rw [hu, Equiv.swap_apply_left, Equiv.swap_apply_of_ne_of_ne hvlo hv] at h
      have h1 : v.val < s.hi.val := h
      have h2 : u.val = s.lo.val := by rw [hu]
      omega
  · rcases eq_or_ne u s.hi with hu2 | hu2
    · exfalso
      have hvlo : v ≠ s.lo := by
        intro hc
        have h1 : u.val = s.hi.val := by rw [hu2]
        have h2 : v.val = s.lo.val := by rw [hc]
        omega
      have hvhi : v ≠ s.hi := by rw [← hu2]; exact (ne_of_gt huv)
      rw [hu2, Equiv.swap_apply_right, Equiv.swap_apply_of_ne_of_ne hvlo hvhi] at h
      have h3 : v.val < s.lo.val := h
      have h4 : u.val = s.hi.val := by rw [hu2]
      omega
    · exfalso
      rw [Equiv.swap_apply_of_ne_of_ne hu hu2] at h
      rcases eq_or_ne v s.lo with hv | hv
      · rw [hv, Equiv.swap_apply_left] at h
        have h3 : s.hi.val < u.val := h
        have h4 : v.val = s.lo.val := by rw [hv]
        omega
      · rcases eq_or_ne v s.hi with hv2 | hv2
        · rw [hv2, Equiv.swap_apply_right] at h
          have h3 : s.lo.val < u.val := h
          have h4 : v.val = s.hi.val := by rw [hv2]
          have h5 : u.val ≠ s.lo.val := fun hc => hu (Fin.ext hc)
          omega
        · rw [Equiv.swap_apply_of_ne_of_ne hv hv2] at h
          exact absurd h (not_lt.mpr (le_of_lt huv))

end AdjSwap

/-- All `C(n,2)` strand pairs `i < j`. -/
def allPairs (n : ℕ) : Finset (Fin n × Fin n) :=
  Finset.univ.filter fun p => p.1 < p.2

/-- There are exactly `C(n,2)` strand pairs. -/
theorem card_allPairs (n : ℕ) : (allPairs n).card = n.choose 2 := by
  classical
  have h1 : (allPairs n).card = ∑ b : Fin n, (b : ℕ) := by
    rw [allPairs, Finset.card_filter, Fintype.sum_prod_type, Finset.sum_comm]
    refine Finset.sum_congr rfl fun b _ => ?_
    rw [← Finset.card_filter]
    have h : (Finset.univ.filter fun a : Fin n => a < b) = Finset.Iio b := by
      ext a; simp
    rw [h, Fin.card_Iio]
  have h2 : (∑ b : Fin n, (b : ℕ)) = ∑ i ∈ Finset.range n, i :=
    Fin.sum_univ_eq_sum_range (fun i => i) n
  rw [h1, h2, Finset.sum_range_id, Nat.choose_two_right]

/-- The strand pairs whose order `σ` reverses.  Two strands have interacted
    exactly when their order is reversed. -/
def crossedPairs (σ : Equiv.Perm (Fin n)) : Finset (Fin n × Fin n) :=
  Finset.univ.filter fun p => p.1 < p.2 ∧ σ p.2 < σ p.1

/-- **One elementary crossing brings at most one new pair into contact.** -/
theorem card_crossedPairs_step (s : AdjSwap n) (σ : Equiv.Perm (Fin n)) :
    (crossedPairs (s.perm * σ)).card ≤ (crossedPairs σ).card + 1 := by
  have key : ∀ p ∈ crossedPairs (s.perm * σ) \ crossedPairs σ,
      σ p.1 = s.lo ∧ σ p.2 = s.hi := by
    intro p hp
    simp only [Finset.mem_sdiff, crossedPairs, Finset.mem_filter, Finset.mem_univ,
      true_and] at hp
    obtain ⟨⟨hlt, hrev⟩, hnot⟩ := hp
    have hne : σ p.1 ≠ σ p.2 := fun h => absurd (σ.injective h) (ne_of_lt hlt)
    have huv : σ p.1 < σ p.2 := by
      rcases lt_or_gt_of_ne hne with h | h
      · exact h
      · exact absurd ⟨hlt, h⟩ hnot
    exact s.eq_of_reverses huv hrev
  have hsub : (crossedPairs (s.perm * σ) \ crossedPairs σ).card ≤ 1 := by
    rw [Finset.card_le_one]
    intro p hp q hq
    obtain ⟨hp1, hp2⟩ := key p hp
    obtain ⟨hq1, hq2⟩ := key q hq
    exact Prod.ext (σ.injective (hp1.trans hq1.symm))
      (σ.injective (hp2.trans hq2.symm))
  calc (crossedPairs (s.perm * σ)).card
      ≤ (crossedPairs (s.perm * σ) \ crossedPairs σ).card + (crossedPairs σ).card :=
        Finset.card_le_card_sdiff_add_card
    _ ≤ (crossedPairs σ).card + 1 := by omega

/-- The permutation of strand positions realised by a word in elementary
    crossings. -/
def braidWordPerm : List (AdjSwap n) → Equiv.Perm (Fin n)
  | [] => 1
  | s :: w => s.perm * braidWordPerm w

@[simp] theorem crossedPairs_one : crossedPairs (1 : Equiv.Perm (Fin n)) = ∅ := by
  simp only [crossedPairs, Finset.filter_eq_empty_iff]
  rintro p - ⟨h1, h2⟩
  exact absurd h2 (not_lt.mpr (le_of_lt h1))

/-- **A word brings no more pairs into contact than it has letters.** -/
theorem card_crossedPairs_le_length (w : List (AdjSwap n)) :
    (crossedPairs (braidWordPerm w)).card ≤ w.length := by
  induction w with
  | nil => simp [braidWordPerm]
  | cons s w ih =>
      have := card_crossedPairs_step s (braidWordPerm w)
      simp only [braidWordPerm, List.length_cons]
      omega

/-- **Every pair must be paid for.**  A word in elementary crossings whose net
    permutation reverses *every* strand pair has length at least `C(n,2)`.

    For three strands this is three crossings.  Two will not do: after two
    elementary crossings one of the three pairs has never been adjacent.  A
    three-body interaction is not two two-body interactions. -/
theorem card_allPairs_le_length (w : List (AdjSwap n))
    (h : allPairs n ⊆ crossedPairs (braidWordPerm w)) :
    n.choose 2 ≤ w.length := by
  rw [← card_allPairs n]
  exact le_trans (Finset.card_le_card h) (card_crossedPairs_le_length w)

/-- The three-strand instance: a fully interacting triple costs three
    crossings. -/
theorem three_crossings_needed (w : List (AdjSwap 3))
    (h : allPairs 3 ⊆ crossedPairs (braidWordPerm w)) : 3 ≤ w.length := by
  have := card_allPairs_le_length w h
  norm_num at this
  exact this

/-! ### The proposition

`prop:pairwise-interaction-decomposition` states all three parts together.
This declaration is the content-block backlink: it is the conjunction of the
three theorems above, each proved separately. -/

/-- **Pairwise decomposition of a braided interaction.**  Three claims:

    1. a composite interaction *reduces* to pairwise ones (hexagon);
    2. that reduction is *independent of the route taken* (Yang–Baxter);
    3. a word bringing every one of the `C(n,2)` strand pairs into contact
       costs at least `C(n,2)` elementary crossings.

    Parts 1 and 2 say the many-body content of an interaction lives in the
    *sequence* of pairwise crossings rather than in an irreducible many-body
    vertex.  Part 3 says that sequence is not free. -/
theorem pairwise_interaction_decomposition (X Y Z : C) (n : ℕ) :
    ((β_ (X ⊗ Y) Z).hom =
        (α_ X Y Z).hom ≫ X ◁ (β_ Y Z).hom ≫ (α_ X Z Y).inv ≫
          (β_ X Z).hom ▷ Y ≫ (α_ Z X Y).hom)
      ∧
    ((α_ X Y Z).inv ≫ (β_ X Y).hom ▷ Z ≫ (α_ Y X Z).hom ≫
        Y ◁ (β_ X Z).hom ≫ (α_ Y Z X).inv ≫ (β_ Y Z).hom ▷ X ≫ (α_ Z Y X).hom =
      X ◁ (β_ Y Z).hom ≫ (α_ X Z Y).inv ≫ (β_ X Z).hom ▷ Y ≫
        (α_ Z X Y).hom ≫ Z ◁ (β_ X Y).hom)
      ∧
    (∀ w : List (AdjSwap n),
      allPairs n ⊆ crossedPairs (braidWordPerm w) → n.choose 2 ≤ w.length) :=
  ⟨composite_crossing_eq_two_elementary X Y Z,
   triple_crossing_route_independent X Y Z,
   fun w hw => card_allPairs_le_length w hw⟩

end QOU.Braiding
