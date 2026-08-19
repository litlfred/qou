import QOU.SchurWeyl.TableauCells
import QOU.BraidKnot.JucysMurphyOV
import QOU.BraidKnot.SytMathlibBridge

/-!
# QOU.SchurWeyl.SytContentTuple — the content tuple determines the tableau, in the `cellOf` API

**The separation input for general irreducibility** (SW-5, bean `qou-jfr8`).  Ram's Theorem 4.1
(`SeminormalRep.seminormalRep_qJM`) makes each `q`-Jucys–Murphy element act *diagonally* on the
SYT basis, with entry `q^{2·cellContent (cellOf T k)}` at `T`.  That alone does not separate the
basis: it separates it only if distinct tableaux of one shape have distinct **content tuples**.

That combinatorial fact is already proved in the corpus, sorry-free, as
`QOU.BraidKnot.JucysMurphy.syt_content_tuple_injective` — the Okounkov–Vershik stack under
`BraidKnot/`.  What is missing is only the translation, because the two halves of the repo use
**two different `StandardYoungTableau` types**:

| | type | cell-of-a-label |
|---|---|---|
| SchurWeyl (`TableauCells`) | `QOU.Mathlib.StandardYoungTableau` | `cellOf T k`, labels `1 … |μ|` |
| BraidKnot (Okounkov–Vershik) | `QOU.BraidKnot.StandardYoungTableau` | `tableauCellEquiv μ T s`, labels `0 … |μ|−1` |

`BraidKnot/SytMathlibBridge.lean` already carries the type conversion with both round trips
(`toBraidKnot`, `toMathlib`, `toBraidKnot_toMathlib`, `toMathlib_toBraidKnot`).  This file adds the
missing *label* correspondence — `cellOf T (s+1)` is `tableauCellEquiv μ T.toBraidKnot s`, the
one-down entry shift read on cells — and transports the separation statement across it.

> **Two `cellContent`s.** `QOU.SchurWeyl.cellContent` (`SchurWeyl/HoefsmitRep.lean`) and
> `QOU.BraidKnot.JucysMurphy.cellContent` (`BraidKnot/JucysMurphy.lean`) are *distinct
> declarations* with the same body `c.2 − c.1`.  They are definitionally equal, so the transport
> is free, but they are not the same symbol and this file is explicit about which is which — per
> AGENTS.md §"attributes do not transfer across overloaded symbols".  (The corpus carries five
> `cellContent` definitions in total; consolidating them is a separate cleanup, not attempted here.)

Refs:
- [okounkov1996] Okounkov–Vershik, *A new approach to the representation theory of the symmetric
  groups* — the content-tuple/Gelfand–Tsetlin separation.
- [ram1997] Ram, *Seminormal representations …* — the `q`-deformed eigenvalues.

LaTeX label: `lem:syt-content-tuple-separates`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells

variable {μ : YoungDiagram}

/-- **The label correspondence across the SYT bridge.**  `tableauCellEquiv` finds the cell of
`T.toBraidKnot` carrying label `s`; since `toBraidKnot` shifts every on-cell entry down by one,
that is the cell of `T` carrying `s + 1`, i.e. `cellOf T (s + 1)`. -/
theorem cellOf_eq_tableauCellEquiv (T : StandardYoungTableau μ) (s : Fin (QOU.BraidKnot.Specht.nOf μ)) :
    cellOf T (s.val + 1)
      = ((QOU.BraidKnot.JucysMurphy.tableauCellEquiv μ T.toBraidKnot s : ℕ × ℕ)) := by
  set c := ((QOU.BraidKnot.JucysMurphy.tableauCellEquiv μ T.toBraidKnot s : ℕ × ℕ)) with hc
  have hmem : c ∈ μ := QOU.BraidKnot.JucysMurphy.tableauCellEquiv_mem _ s
  have hcells : c ∈ μ.cells := (YoungDiagram.mem_cells c).mpr hmem
  -- the BraidKnot entry at `c` is `s`, and it is `T.entry c − 1` by definition of `toBraidKnot`
  have hentry : (T.toBraidKnot).entry c.1 c.2 = s.val :=
    QOU.BraidKnot.JucysMurphy.entry_tableauCellEquiv _ s
  have hshift : T.entry c.1 c.2 - 1 = s.val := hentry
  have hge : 1 ≤ T.entry c.1 c.2 := by
    have h := T.mapsTo_cells (Finset.mem_coe.mpr hcells)
    exact (Set.mem_Icc.mp h).1
  exact cellOf_unique T hcells (by omega)

/-- **Separation — the content tuple determines the tableau** (`cellOf` form).  Two standard
tableaux of the same shape that assign the same content to every label `1 ≤ k ≤ |μ|` are equal.

This is `QOU.BraidKnot.JucysMurphy.syt_content_tuple_injective` transported across the bridge.
The mathematical content is entirely there: entries increase strictly along diagonals, so the
*row* of the cell holding `k` is a function of the content tuple alone, and row + content gives
the column. -/
theorem syt_eq_of_cellContent_eq (T T' : StandardYoungTableau μ)
    (h : ∀ k : ℕ, 1 ≤ k → k ≤ μ.cells.card → cellContent (cellOf T k) = cellContent (cellOf T' k)) :
    T = T' := by
  have hbk : T.toBraidKnot = T'.toBraidKnot := by
    refine QOU.BraidKnot.JucysMurphy.syt_content_tuple_injective μ _ _ (fun s => ?_)
    have hs : s.val + 1 ≤ μ.cells.card := by
      have := s.isLt
      have hcard : QOU.BraidKnot.Specht.nOf μ = μ.cells.card := rfl
      omega
    have hk := h (s.val + 1) (by omega) hs
    rw [cellOf_eq_tableauCellEquiv T s, cellOf_eq_tableauCellEquiv T' s] at hk
    exact hk
  calc T = (T.toBraidKnot).toMathlib := (QOU.BraidKnot.toMathlib_toBraidKnot T).symm
    _ = (T'.toBraidKnot).toMathlib := by rw [hbk]
    _ = T' := QOU.BraidKnot.toMathlib_toBraidKnot T'

end QOU.SchurWeyl
