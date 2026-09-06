import QOU.BraidKnot.CompositionCosetExists

/-!
# Composition-shaped tableaux — and `IsDistinguished` IS row standardness

`TableauPerm.dOf` gives Mathas' `d(t)` for a **partition** shape (`Specht.Tableau` is
indexed by a `YoungDiagram`).  Mathas' Lemma 3.9 is about a **composition** `μ`, whose
rows need not decrease, so that map does not apply to it as stated.

This file supplies the missing shape, and the point of it is that almost nothing new has
to be proved: the row-standardness condition on a composition tableau turns out to be
`CompositionMinimal.IsDistinguished`, already proved to characterise the distinguished
coset representatives `D_μ`.

## The dictionary

The cells of a composition `c : Composition n` are `Fin n`, linearly ordered, with cell
`x` lying in row `c.index x` — because `Composition.index` is defined so that row `i`
occupies the consecutive positions `sizeUpTo i … sizeUpTo i + blocksFun i − 1`.  A
tableau is a bijection between entries and cells, and following `dOf`'s orientation we
carry it as `d : Perm (Fin n)` read **entry ↦ cell**, so `d.symm` is **cell ↦ entry**.

Row standardness is naturally stated on *cells* — "reading a row left to right, the
entries increase" (`IsRowStandard`) — while `IsDistinguished` is stated on *entries*.
`isRowStandard_iff_isDistinguished` is the (short) argument that a bijection is monotone
within a block exactly when its inverse is.

## What this buys

`existsUnique_rowStandard` restates Proposition 3.3 in the vocabulary Mathas uses:
**every right coset of `S_μ` contains exactly one row-standard `μ`-tableau.**  Nothing is
reproved — it is `CompositionCosetExists.existsUnique_isDistinguished_mem_coset` under
the dictionary — which is precisely the claim worth making mechanical rather than
asserting it in prose.
-/

namespace QOU.BraidKnot.CompositionTableau

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.Hecke.SymmetricCoxeter Equiv

variable {n : ℕ}

/-- **The entry in cell `x`**, for the tableau carried by `d` in the entry ↦ cell
orientation. -/
def entryAt (d : Perm (Fin n)) (x : Fin n) : Fin n := d.symm x

@[simp] theorem entryAt_apply (d : Perm (Fin n)) (a : Fin n) :
    entryAt d (d a) = a := d.symm_apply_apply a

/-- **The row of cell `x`.** -/
def rowAt (c : Composition n) (x : Fin n) : Fin c.length := c.index x

/-- **Row standardness**, stated on cells: along each row, taken in increasing cell
order, the entries increase. -/
def IsRowStandard (c : Composition n) (d : Perm (Fin n)) : Prop :=
  ∀ x y : Fin n, rowAt c x = rowAt c y → x < y → entryAt d x < entryAt d y

/-- **The dictionary.**  A tableau is row standard exactly when its carrying permutation
is distinguished — the cell-side and entry-side conditions are the same condition, because
a bijection is monotone within a block iff its inverse is. -/
theorem isRowStandard_iff_isDistinguished (c : Composition n) (d : Perm (Fin n)) :
    IsRowStandard c d ↔ IsDistinguished c d := by
  constructor
  · intro h a b hidx hab
    rcases lt_trichotomy (d a) (d b) with hlt | heq | hgt
    · exact hlt
    · exact absurd (d.injective heq) (ne_of_lt hab)
    · have := h (d b) (d a) (by simpa [rowAt] using hidx.symm) hgt
      simp only [entryAt_apply] at this
      exact absurd hab (by omega)
  · intro h x y hidx hxy
    rcases lt_trichotomy (entryAt d x) (entryAt d y) with hlt | heq | hgt
    · exact hlt
    · exact absurd (d.symm.injective heq) (ne_of_lt hxy)
    · have := h (entryAt d y) (entryAt d x)
        (by simpa [entryAt, rowAt] using hidx.symm) hgt
      simp only [entryAt, Equiv.apply_symm_apply] at this
      exact absurd hxy (by omega)

/-- **Mathas, Proposition 3.3, in tableau language.**  Every right coset of the Young
subgroup `S_μ` contains **exactly one row-standard `μ`-tableau**.

This reproves nothing: it is `existsUnique_isDistinguished_mem_coset` read through
`isRowStandard_iff_isDistinguished`. -/
theorem existsUnique_rowStandard (c : Composition (n + 1)) (w : Perm (Fin (n + 1))) :
    ∃! d, IsRowStandard c d ∧ d * w⁻¹ ∈ youngOfComp c := by
  obtain ⟨d, ⟨hd, hdm⟩, huniq⟩ :=
    QOU.BraidKnot.CompositionCosetExists.existsUnique_isDistinguished_mem_coset c w
  refine ⟨d, ⟨(isRowStandard_iff_isDistinguished c d).mpr hd, hdm⟩, ?_⟩
  rintro e ⟨hed, hem⟩
  exact huniq e ⟨(isRowStandard_iff_isDistinguished c e).mp hed, hem⟩

/-- **The reference tableau `t^μ` is row standard.**  It is the identity: entry `a` sits
in cell `a`. -/
theorem isRowStandard_one (c : Composition n) : IsRowStandard c (1 : Perm (Fin n)) := by
  intro x y _ hxy
  simpa [entryAt] using hxy

end QOU.BraidKnot.CompositionTableau
