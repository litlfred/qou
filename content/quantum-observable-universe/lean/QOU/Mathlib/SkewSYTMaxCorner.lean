import QOU.BraidKnot.YoungTableauStandard

/-!
# `QOU.Mathlib.SkewSYTMaxCorner` — the erase-max step of the skew branching rule

Bean `qou-b21r` reduces `RSKIdentitiesContext.branching_two_one` to ONE open input: the skew
branching rule

    f^{λ/μ} = ∑_{c a corner of λ with c ∉ μ}  f^{(λ ∖ c)/μ},

i.e. "remove the largest entry of a skew standard Young tableau".  Its other two inputs are in
hand — `QOU.Mathlib.upSum_eq` is proved, and the transposition is the `Finset.sum_comm`
manoeuvre `pairTerm` already performs there.

This file supplies the **erase** direction's geometry, sorry-free.  It does not close the
branching rule: the bijection with `(λ ∖ c)/μ` tableaux, and the sum, are still to do.

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
- [manuscript] bean `qou-b21r`
-/

namespace QOU.BraidKnot.YoungTableauStandard
open Finset

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

end QOU.BraidKnot.YoungTableauStandard
