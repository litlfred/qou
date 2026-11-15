/-
Copyright (c) 2026 QOU contributors. All rights reserved.
Released under Apache 2.0 license.
-/
import QOU.SchurWeyl.WtraceRadicalTwoRowSubset
import QOU.SchurWeyl.SeminormalBlockEquality
import QOU.SchurWeyl.MarkovAssembly

/-!
# The tower comparison is an iff — the forward direction

`WtraceRadicalTwoRowSubset` proved **reflection** unconditionally: if `heckeIncl a` is
invisible to `wtrace` upstairs, `a` is invisible downstairs.  That needed only
`wtrace_incl`, because a test element could be restricted to the image.

The **forward** direction cannot be done that way — a test element of `H_{m+1}` need
not be in the image, which is exactly the obstruction `QBeta.TLTowerRadicalDescent`'s
docstring names and answers with an (open) conditional expectation.  This file gets it
instead from the *identification* of the radical, which #7461 supplied:

- downstairs, `a ∈ rad` **iff** every at-most-two-row block kills `a`;
- upstairs, the same;
- and along `heckeIncl` the two are related by **branching**.

So the forward direction reduces to a statement about diagrams, and the reduction is
where the work went; the diagram fact itself is three lines.

## The three ingredients

1. `rowLen_two_eq_zero_eraseCorner` — **erasing a corner cannot create a third row.**
   The whole content is that `eraseCorner` shrinks (`mem_eraseCorner`), so a cell in
   row 2 downstairs would have been one upstairs.  Note this is the *universal*
   statement over corners, and is not `YoungDiagramThreeRowCorner.youngPred`, which is
   existential and runs the other way (it *finds* one corner preserving ≥ 3 rows).
2. `eq_zero_of_blockPreserving_of_compress_eq_zero` — **a block-diagonal matrix all of
   whose diagonal blocks vanish is zero.**  Every entry `X T S` is either off-block
   (zero by `BlockPreserving`) or inside the block of `c = cellOf T`, where
   `exists_insertMax_of_cellOf_top` factors both `T` and `S` through `insertMax` and
   the entry *is* an entry of `compress c hc X`.  `isCornerCell_cellOf_card` is what
   makes `c` a corner, so the compression is defined at all.
3. `seminormalRep_heckeIncl_mem_blockSubalgebra` (already on `main`) — the upstairs
   matrix of an element **of the image** is block-preserving.  This is the one place
   the image hypothesis is used, and it is why the forward direction holds for
   `heckeIncl a` and not for an arbitrary element.

## What this closes

`incl_mem_rad_iff` — the tower inclusion **detects the radical exactly**, at the
concrete `wtrace` carrier, with no conditional expectation and no open class.  The
induced map `H_m / rad → H_{m+1} / rad` is therefore injective *and* well defined, i.e.
the Temperley–Lieb quotients form a tower rather than a sequence of algebras with maps
between them.

`QBeta.TLTowerRadicalDescent` proves the same shape abstractly and every statement
there is conditional on `HeckeConditionalExpectation`, an open class with no instance.
That conditionality is **not** removed by this file: it is a statement about an
arbitrary trace on an arbitrary tower, where the conditional expectation is the only
thing relating the two radicals.  What is shown here is that the *canonical* carrier
does not need it, because `wtrace` has a branching rule.

## Scope

Convention **D** (`z = q³/(q²+1)`), `ℝ`, and the genericity `wtrace` carries — the same
scope as the two halves it composes.
-/

namespace QOU.SchurWeyl.WtraceRadicalTwoRow

open YoungDiagram QOU.Mathlib QOU.SchurWeyl QOU.SchurWeyl.SeminormalRep
open QOU.SchurWeyl.HeckeInclusion
open QOU.SchurWeyl.TableauCells

/-- **Erasing a corner cannot create a third row.**

`eraseCorner` only removes a cell, so a cell in row 2 of the erasure was already one
upstairs — where `rowLen 2 = 0` forbids it. -/
theorem rowLen_two_eq_zero_eraseCorner {mu : YoungDiagram} (h : mu.rowLen 2 = 0)
    (c : ℕ × ℕ) (hc : IsCornerCell mu c) : (eraseCorner mu c hc).rowLen 2 = 0 := by
  by_contra hne
  have hmem : (2, 0) ∈ eraseCorner mu c hc :=
    mem_iff_lt_rowLen.mpr (Nat.pos_of_ne_zero hne)
  rw [mem_eraseCorner] at hmem
  have hup : (2, 0) ∈ mu := hmem.1
  rw [mem_iff_lt_rowLen, h] at hup
  omega

/-- **A block-diagonal matrix whose every diagonal block vanishes is zero.**

Off-block entries die by `BlockPreserving`; an on-block entry is literally an entry of
the corresponding compression, via `exists_insertMax_of_cellOf_top`. -/
theorem eq_zero_of_blockPreserving_of_compress_eq_zero {mu : YoungDiagram}
    (hpos : 0 < mu.cells.card)
    {X : Matrix (StandardYoungTableau mu) (StandardYoungTableau mu) ℝ}
    (hbp : BlockPreserving mu.cells.card X)
    (hcomp : ∀ (c : ℕ × ℕ) (hc : IsCornerCell mu c), compress c hc X = 0) :
    X = 0 := by
  ext T S
  by_cases h : cellOf T mu.cells.card = cellOf S mu.cells.card
  · have hc : IsCornerCell mu (cellOf T mu.cells.card) := isCornerCell_cellOf_card T hpos
    obtain ⟨T', hT'⟩ := exists_insertMax_of_cellOf_top _ hc T rfl
    obtain ⟨S', hS'⟩ := exists_insertMax_of_cellOf_top _ hc S h.symm
    have hz := congrFun (congrFun (hcomp _ hc) T') S'
    rw [← hT', ← hS']
    exact hz
  · exact hbp T S h

/-- **Forward: the inclusion carries the radical upstairs.**

If every at-most-two-row block kills `a` downstairs, then every at-most-two-row block
kills `heckeIncl a` upstairs — because each of its diagonal blocks IS a downstairs
block at an erased corner, and erasing a corner keeps the diagram at two rows. -/
theorem twoRow_blocks_vanish_incl {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (m : ℕ) (a : Hecke ℝ q q⁻¹ m)
    (ha : ∀ (d : YoungDiagram) (hd : d.cells.card = m + 1), d.rowLen 2 = 0 →
      seminormalRep q hq0 hq2 m hd a = 0)
    (L : YoungDiagram) (hL : L.cells.card = m + 2) (hrow : L.rowLen 2 = 0) :
    seminormalRep q hq0 hq2 (m + 1) hL (heckeIncl ℝ q q⁻¹ m a) = 0 := by
  refine eq_zero_of_blockPreserving_of_compress_eq_zero (by rw [hL]; omega) ?_ ?_
  · rw [hL]
    exact seminormalRep_heckeIncl_mem_blockSubalgebra hq0 hq2 m hL a
  · intro c hc
    have hNs : (eraseCorner L c hc).cells.card = m + 1 := by
      have hcard := card_eraseCorner L c hc
      rw [hL] at hcard
      omega
    rw [compress_seminormalRep_heckeIncl hq0 hq2 m hL c hc hNs a]
    exact ha _ hNs (rowLen_two_eq_zero_eraseCorner hrow c hc)

/-- **The tower inclusion detects the radical EXACTLY** — unconditionally, at the
concrete `wtrace` carrier.

Reflection is `mem_rad_of_incl_mem_rad` (one rewrite of `wtrace_incl`); the forward
direction routes through the radical identification and the branching rule.  Together:
`H_m / rad ↪ H_{m+1} / rad`, so the Temperley–Lieb quotients are a tower. -/
theorem incl_mem_rad_iff {q : ℝ} (hq0 : q ≠ 0)
    (hq2 : GenericParameter.NotRootOfUnity q) (hq21 : q ^ 2 + 1 ≠ 0)
    (hgen : ∀ k : ℕ, 0 < k → (q ^ 2 : ℝ) ^ k ≠ 1) (m : ℕ) (a : Hecke ℝ q q⁻¹ m) :
    (∀ x : Hecke ℝ q q⁻¹ (m + 1),
        wtrace q hq0 hq2 (m + 1) (heckeIncl ℝ q q⁻¹ m a * x) = 0)
      ↔ ∀ b : Hecke ℝ q q⁻¹ m, wtrace q hq0 hq2 m (a * b) = 0 := by
  refine ⟨mem_rad_of_incl_mem_rad hq0 hq2 hq21 hgen m a, fun hb => ?_⟩
  refine mem_rad_of_twoRow_blocks_vanish hq0 hq2 hq21 (m + 1) _ ?_
  intro L hL hrow
  exact twoRow_blocks_vanish_incl hq0 hq2 m a
    ((mem_rad_iff_twoRow_blocks_vanish hq0 hq2 hq21 hgen m a).mp hb) L hL hrow

end QOU.SchurWeyl.WtraceRadicalTwoRow
