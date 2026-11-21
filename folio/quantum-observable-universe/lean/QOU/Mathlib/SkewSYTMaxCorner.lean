import QOU.BraidKnot.YoungTableauStandard
import QOU.Mathlib.YoungDiagramCorner

/-!
# `QOU.Mathlib.SkewSYTMaxCorner` — the erase-max step of the skew branching rule

Bean `qou-b21r` reduces `RSKIdentitiesContext.branching_two_one` to ONE open input: the skew
branching rule

    f^{λ/μ} = ∑_{c a corner of λ with c ∉ μ}  f^{(λ ∖ c)/μ},

i.e. "remove the largest entry of a skew standard Young tableau".  Its other two inputs are in
hand — `QOU.Mathlib.upSum_eq` is proved, and the transposition is the `Finset.sum_comm`
manoeuvre `pairTerm` already performs there.

This file supplies **both directions' constructions**, sorry-free — the corner extraction
(`exists_max_corner`), the diagram-level consequences, and the insertion (`skewInsertMax`).
It does **not** close the branching rule: proving the two are mutually inverse, and the sum
itself, are still to do.

## Why the skew case is not a transliteration of the straight one

`QOU/Mathlib/SYTEraseMax.lean` can lean on `StandardYoungTableau.bijOn`, which hands over
injectivity and surjectivity as separate directly-usable facts.  `SkewStandardYoungTableau`
instead certifies its filling with a Finset **image equality**

    (outer.cells \ inner.cells).image entry = Finset.range (outer.cells \ inner.cells).card

from which both halves must be re-derived.  `skew_injOn`, `skew_mem_range` and
`skew_exists_of_lt` do that once, so the rest of the development can cite them the way the
straight case cites `bijOn`.

Note also the skew entries are **0-based** (`range n`) where the straight ones are 1-based
(`Icc 1 n`); index arithmetic does not port.

## The one genuinely new obligation

`exists_max_corner` must show the maximal cell is a corner of `outer` **and lies outside
`inner`** — the second half has no counterpart in the straight case, and it is exactly what
makes `inner ≤ outer ∖ c` hold, so that the smaller skew shape is well-formed.

Pure combinatorics; nothing archimedean (§7c).

## References

- [stanley1999ec2] Enumerative Combinatorics I, §7.10 (skew tableaux)
- [leitner2026] bean `qou-b21r`
-/

namespace QOU.BraidKnot.YoungTableauStandard
open Finset QOU.Mathlib

variable {outer inner : YoungDiagram} {c : ℕ × ℕ}

/-- The skew cells of `outer / inner`. -/
abbrev skewCellsOf (outer inner : YoungDiagram) : Finset (ℕ × ℕ) :=
  outer.cells \ inner.cells

/-- **The entry map is injective on the skew region.**  `content` says the image is
`range |skew|`, and a set whose image has the same cardinality as itself is mapped
injectively.  Every step of a skew insert/erase construction needs this, and unlike the
straight case — where `StandardYoungTableau.bijOn` hands it over directly — it has to be
derived from the image equality. -/
theorem skew_injOn (T : SkewStandardYoungTableau outer inner) :
    Set.InjOn (fun c : ℕ × ℕ => T.entry c.1 c.2) (skewCellsOf outer inner) := by
  have hcard : (skewCellsOf outer inner).image (fun c => T.entry c.1 c.2)
      = Finset.range (skewCellsOf outer inner).card := T.content
  have : ((skewCellsOf outer inner).image (fun c => T.entry c.1 c.2)).card
      = (skewCellsOf outer inner).card := by
    rw [hcard, Finset.card_range]
  exact Finset.injOn_of_card_image_eq this

/-- **The entries on the skew region are exactly `0, …, |skew| − 1`.** -/
theorem skew_mem_range (T : SkewStandardYoungTableau outer inner)
    {c : ℕ × ℕ} (hc : c ∈ skewCellsOf outer inner) :
    T.entry c.1 c.2 < (skewCellsOf outer inner).card := by
  have : T.entry c.1 c.2 ∈ Finset.range (skewCellsOf outer inner).card := by
    rw [← T.content]
    exact Finset.mem_image_of_mem _ hc
  simpa using this

/-- **Every value below `|skew|` is attained.**  The surjective half of the same
`content` field. -/
theorem skew_exists_of_lt (T : SkewStandardYoungTableau outer inner)
    {v : ℕ} (hv : v < (skewCellsOf outer inner).card) :
    ∃ c ∈ skewCellsOf outer inner, T.entry c.1 c.2 = v := by
  have : v ∈ (skewCellsOf outer inner).image (fun c => T.entry c.1 c.2) := by
    rw [T.content]; simpa using hv
  simpa using Finset.mem_image.mp this

/-- A skew cell's right neighbour, if in `outer`, is also a skew cell: it cannot be in
`inner`, since `inner` is a lower set and the original cell is not in it. -/
theorem skew_right_mem (hc : c ∈ skewCellsOf outer inner)
    (h : (c.1, c.2 + 1) ∈ outer) : (c.1, c.2 + 1) ∈ skewCellsOf outer inner := by
  simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells] at hc ⊢
  refine ⟨h, fun hin => hc.2 ?_⟩
  exact inner.up_left_mem (le_refl c.1) (Nat.le_succ c.2) hin

/-- The downward neighbour, likewise. -/
theorem skew_down_mem (hc : c ∈ skewCellsOf outer inner)
    (h : (c.1 + 1, c.2) ∈ outer) : (c.1 + 1, c.2) ∈ skewCellsOf outer inner := by
  simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells] at hc ⊢
  refine ⟨h, fun hin => hc.2 ?_⟩
  exact inner.up_left_mem (Nat.le_succ c.1) (le_refl c.2) hin

/-- **The maximal entry sits on a removable corner of `outer` that is outside `inner`.**

This is the erase-max step of the skew branching rule, and the one place its geometry
differs from the straight case: the corner must additionally be shown to lie outside
`inner`, which is exactly what makes `outer ∖ c` still contain `inner`.

Both neighbours are ruled out the same way — if the neighbour were in `outer` it would be
a *skew* cell (`skew_right_mem` / `skew_down_mem`), its entry would strictly exceed the
maximum by `row_strict` / `col_strict`, and yet be bounded by it via `skew_mem_range`. -/
theorem exists_max_corner (T : SkewStandardYoungTableau outer inner) (n : ℕ)
    (hn : (skewCellsOf outer inner).card = n + 1) :
    ∃ c ∈ skewCellsOf outer inner,
      T.entry c.1 c.2 = n ∧ (c.1 + 1, c.2) ∉ outer ∧ (c.1, c.2 + 1) ∉ outer := by
  obtain ⟨c, hc, hval⟩ := skew_exists_of_lt T (v := n) (by omega)
  have hcin : c ∈ skewCellsOf outer inner := hc
  simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells] at hc
  refine ⟨c, hcin, hval, ?_, ?_⟩
  · intro hdown
    have hskew := skew_down_mem hcin hdown
    have hlt : T.entry c.1 c.2 < T.entry (c.1 + 1) c.2 :=
      T.col_strict (Nat.lt_succ_self c.1) hdown hc.2
    have hle := skew_mem_range T hskew
    simp only at hle
    omega
  · intro hright
    have hskew := skew_right_mem hcin hright
    have hlt : T.entry c.1 c.2 < T.entry c.1 (c.2 + 1) :=
      T.row_strict (Nat.lt_succ_self c.2) hright hc.2
    have hle := skew_mem_range T hskew
    simp only at hle
    omega

/-! ### The erased diagram

`exists_max_corner` gives a corner outside `inner`; these turn that into the diagram-level
facts the bijection will need. -/

/-- Deleting a corner that lies outside `inner` keeps `inner` inside the diagram. -/
theorem le_eraseCorner_of_notMem (hle : inner ≤ outer) (hc : IsCornerCell outer c)
    (hcn : c ∉ inner) : inner ≤ eraseCorner outer c hc := by
  intro x hx
  rw [YoungDiagram.mem_cells] at hx ⊢
  rw [mem_eraseCorner]
  exact ⟨hle hx, fun h => hcn (h ▸ hx)⟩

/-- Deleting that corner removes exactly it from the skew region.

Note this needs **no** hypothesis that `c ∉ inner` — set-difference-minus-a-cell is
`erase` on the difference either way.  (The unused binder was there until the linter
pointed out it does no work; carrying it would have implied the identity depends on the
corner being outside `inner`, which it does not.) -/
theorem skewCellsOf_eraseCorner (hc : IsCornerCell outer c) :
    skewCellsOf (eraseCorner outer c hc) inner = (skewCellsOf outer inner).erase c := by
  ext x
  simp only [skewCellsOf, Finset.mem_sdiff, Finset.mem_erase, YoungDiagram.mem_cells,
    mem_eraseCorner]
  constructor
  · rintro ⟨⟨hxo, hxc⟩, hxi⟩; exact ⟨hxc, hxo, hxi⟩
  · rintro ⟨hxc, hxo, hxi⟩; exact ⟨⟨hxo, hxc⟩, hxi⟩

/-- So the skew size drops by exactly one. -/
theorem card_skewCellsOf_eraseCorner (hc : IsCornerCell outer c)
    (hmem : c ∈ skewCellsOf outer inner) :
    (skewCellsOf (eraseCorner outer c hc) inner).card + 1
      = (skewCellsOf outer inner).card := by
  rw [skewCellsOf_eraseCorner hc, Finset.card_erase_of_mem hmem]
  have : 0 < (skewCellsOf outer inner).card := Finset.card_pos.mpr ⟨c, hmem⟩
  omega

/-! ### Toward the insert direction

Two facts the mirror construction needs.  The insert step itself (`skewInsertMax`) is NOT
here — see the file header and bean `qou-b21r` for what remains. -/

/-- A cell of `outer` other than the deleted corner survives the deletion. -/
theorem mem_eraseCorner_of_ne (hc : IsCornerCell outer c) {x : ℕ × ℕ}
    (hx : x ∈ outer) (hne : x ≠ c) : x ∈ eraseCorner outer c hc := by
  exact (mem_eraseCorner outer c hc x).mpr ⟨hx, hne⟩

/-- Off the skew region every entry is `0`, so a positive bound holds there too.  Needed
because the insert step must bound `S.entry` at cells it knows nothing about. -/
theorem entry_lt_card_of_pos (hc : IsCornerCell outer c)
    (S : SkewStandardYoungTableau (eraseCorner outer c hc) inner)
    (hpos : 0 < (skewCellsOf (eraseCorner outer c hc) inner).card) (i j : ℕ) :
    S.entry i j < (skewCellsOf (eraseCorner outer c hc) inner).card := by
  by_cases hm : (i, j) ∈ skewCellsOf (eraseCorner outer c hc) inner
  · exact skew_mem_range S hm
  · simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells, not_and, not_not] at hm
    by_cases hin : (i, j) ∈ eraseCorner outer c hc
    · rw [S.zeros (Or.inl (hm hin))]; exact hpos
    · rw [S.zeros (Or.inr hin)]; exact hpos

/-! ### The insert direction

`skewInsertMax` is the mirror of the erase step: put the new maximum at the corner and keep
`S` elsewhere.  Together with `exists_max_corner` these are the two halves of the branching
bijection — the bijection PROOF (that they are mutually inverse) and the resulting sum are
still to do.

The `content` field is where the skew case costs more than the straight one: it must show
`image entry (skew outer inner) = range (N+1)` from `S.content : image = range N`, by splitting
the skew region as `insert c (skew (outer ∖ c) inner)`.  `skewCellsOf` is an `abbrev`, so it
unfolds in the goal and `rw` cannot see it — the split is stated in the raw
`outer.cells \ inner.cells` form for that reason. -/

theorem entry_lt_of_skew (p q : ℕ) (hc : IsCornerCell outer (p, q))
    (S : SkewStandardYoungTableau (eraseCorner outer (p, q) hc) inner)
    {i j : ℕ} (hij : (i, j) ∈ outer) (hni : (i, j) ∉ inner) (hne : (i, j) ≠ (p, q)) :
    S.entry i j < (skewCellsOf (eraseCorner outer (p, q) hc) inner).card := by
  have h := skew_mem_range S (c := (i, j)) (by
    simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells]
    exact ⟨mem_eraseCorner_of_ne hc hij hne, hni⟩)
  simpa using h

/-- `(p, q)` being a corner rules out any cell strictly to its right in `outer`. -/
theorem not_mem_right_of_corner {p q j : ℕ} (hc : IsCornerCell outer (p, q))
    (hj : q < j) : (p, j) ∉ outer := by
  intro h
  exact hc.2.2 (outer.up_left_mem (le_refl p) (by omega) h)

/-- Likewise strictly below it. -/
theorem not_mem_below_of_corner {p q i : ℕ} (hc : IsCornerCell outer (p, q))
    (hi : p < i) : (i, q) ∉ outer := by
  intro h
  exact hc.2.1 (outer.up_left_mem (by omega) (le_refl q) h)

/-- **Insert the maximal entry at a corner outside `inner`** — the mirror of the erase step. -/
noncomputable def skewInsertMax (p q : ℕ) (hc : IsCornerCell outer (p, q))
    (hcn : (p, q) ∉ inner)
    (S : SkewStandardYoungTableau (eraseCorner outer (p, q) hc) inner) :
    SkewStandardYoungTableau outer inner where
  entry := fun i j =>
    if i = p ∧ j = q then (skewCellsOf (eraseCorner outer (p, q) hc) inner).card
    else S.entry i j
  row_strict := by
    intro i j₁ j₂ hlt hj₂ hj₁
    have hj₁o : (i, j₁) ∈ outer := outer.up_left_mem (le_refl i) (le_of_lt hlt) hj₂
    have hne1 : (i, j₁) ≠ (p, q) := by
      rintro h
      have hi : i = p := congrArg Prod.fst h
      have hjq : j₁ = q := congrArg Prod.snd h
      exact not_mem_right_of_corner hc (by omega) (hi ▸ hj₂)
    by_cases h2 : i = p ∧ j₂ = q
    · rw [if_pos h2, if_neg (by rintro ⟨-, h⟩; exact hne1 (by rw [h2.1, h]))]
      exact entry_lt_of_skew p q hc S hj₁o hj₁ hne1
    · have hne2 : (i, j₂) ≠ (p, q) := by
        rintro h
        exact h2 ⟨congrArg Prod.fst h, congrArg Prod.snd h⟩
      rw [if_neg h2, if_neg (by rintro ⟨h, h'⟩; exact hne1 (by rw [h, h']))]
      exact S.row_strict hlt (mem_eraseCorner_of_ne hc hj₂ hne2) hj₁
  col_strict := by
    intro i₁ i₂ j hlt hi₂ hi₁
    have hi₁o : (i₁, j) ∈ outer := outer.up_left_mem (le_of_lt hlt) (le_refl j) hi₂
    have hne1 : (i₁, j) ≠ (p, q) := by
      rintro h
      have hip : i₁ = p := congrArg Prod.fst h
      have hjq : j = q := congrArg Prod.snd h
      exact not_mem_below_of_corner hc (by omega) (hjq ▸ hi₂)
    by_cases h2 : i₂ = p ∧ j = q
    · rw [if_pos h2, if_neg (by rintro ⟨h, h'⟩; exact hne1 (by rw [h, h']))]
      exact entry_lt_of_skew p q hc S hi₁o hi₁ hne1
    · have hne2 : (i₂, j) ≠ (p, q) := by
        rintro h
        exact h2 ⟨congrArg Prod.fst h, congrArg Prod.snd h⟩
      rw [if_neg h2, if_neg (by rintro ⟨h, h'⟩; exact hne1 (by rw [h, h']))]
      exact S.col_strict hlt (mem_eraseCorner_of_ne hc hi₂ hne2) hi₁
  zeros := by
    intro i j h
    have hne : ¬ (i = p ∧ j = q) := by
      rintro ⟨rfl, rfl⟩
      rcases h with h | h
      · exact hcn h
      · exact h hc.1
    rw [if_neg hne]
    refine S.zeros ?_
    rcases h with h | h
    · exact Or.inl h
    · refine Or.inr (fun hm => h ?_)
      exact ((mem_eraseCorner outer (p, q) hc (i, j)).mp hm).1
  content := by
    have hcmem : (p, q) ∈ skewCellsOf outer inner := by
      simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells]
      exact ⟨hc.1, hcn⟩
    have hnotin : (p, q) ∉ skewCellsOf (eraseCorner outer (p, q) hc) inner := by
      simp only [skewCellsOf, Finset.mem_sdiff, YoungDiagram.mem_cells, mem_eraseCorner,
        not_and, not_not]
      intro h
      exact absurd rfl h.2
    have hsplit : outer.cells \ inner.cells
        = insert (p, q) (skewCellsOf (eraseCorner outer (p, q) hc) inner) := by
      show skewCellsOf outer inner = _
      rw [skewCellsOf_eraseCorner hc, Finset.insert_erase hcmem]
    have hagree : Set.EqOn
        (fun x : ℕ × ℕ =>
          if x.1 = p ∧ x.2 = q then (skewCellsOf (eraseCorner outer (p, q) hc) inner).card
          else S.entry x.1 x.2)
        (fun x : ℕ × ℕ => S.entry x.1 x.2)
        ↑(skewCellsOf (eraseCorner outer (p, q) hc) inner) := by
      intro x hx
      simp only [Finset.mem_coe] at hx
      refine if_neg (fun hxe => hnotin ?_)
      have hxpq : x = (p, q) := Prod.ext hxe.1 hxe.2
      exact hxpq ▸ hx
    rw [hsplit]
    rw [Finset.image_insert]
    rw [Finset.image_congr hagree]
    rw [S.content]
    rw [Finset.card_insert_of_notMem hnotin]
    rw [Finset.range_add_one]
    simp

end QOU.BraidKnot.YoungTableauStandard
