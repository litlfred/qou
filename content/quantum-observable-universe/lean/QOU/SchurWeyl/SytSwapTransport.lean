import QOU.SchurWeyl.SytContentTuple

/-!
# QOU.SchurWeyl.SytSwapTransport — admissible-swap connectivity, transported

The connectivity half of SW-5 (bean `qou-jfr8`), carried across the same bridge
`SytContentTuple` used for separation.

`QOU.BraidKnot.JucysMurphy.syt_adjacentSwap_connected` proves, sorry-free, that any two standard
tableaux of one shape are joined by a chain of admissible adjacent swaps.  Reaching it from the
`SchurWeyl` side looked like it would need the two *swap constructions* matched —
`swapCellsSYT` against `swapTableau` — which is a much larger job than matching the label
conventions was.

**It does not, and the reason is worth stating.**  `AdjacentSwapStep` is defined purely in terms
of **content vectors**: `T'` is a step from `T` when their contents agree away from `{a, a+1}`,
are exchanged at `{a, a+1}`, and the gap `d` satisfies `d ≠ 0`, `d² ≠ 1`.  It never mentions how
`T'` is built.  So the transport needs only that `swapTableau T k` *has that content profile* —
which `cellOf_swapTableau_self` / `_succ` / `_of_ne` give — plus **separation**
(`syt_eq_of_cellContent_eq`), which says a content profile determines the tableau at most one way.
Separation, landed for the eigenvalue argument, turns out to do the structural matching too.

The admissibility conditions line up on the nose: `SwapAdmissible T k` asks that the cells of `k`
and `k+1` share neither row nor column, and in a standard tableau sharing a row forces `d = 1`
(`axialDist_of_sameRow`) while sharing a column forces `d = −1` (`axialDist_of_sameCol`) — so
`d² ≠ 1` is exactly admissibility.

LaTeX label: `lem:syt-swap-connected`
-/

namespace QOU.SchurWeyl

open QOU.Mathlib (StandardYoungTableau)
open TableauCells

variable {μ : YoungDiagram}

/-- **`d² ≠ 1` is admissibility.**  Sharing a row forces axial distance `1`, sharing a column
forces `−1`; so a gap that is neither is a genuine `2 × 2` swap. -/
theorem swapAdmissible_of_sq_axialDist_ne_one (T : StandardYoungTableau μ) {k : ℕ}
    (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) (hsq : (axialDist T k) ^ 2 ≠ 1) :
    SwapAdmissible T k := by
  have hkI : k ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨hk, by omega⟩
  have hkI' : k + 1 ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨by omega, hkn⟩
  have hmem : cellOf T k ∈ μ := (YoungDiagram.mem_cells _).mp (cellOf_mem T hkI)
  have hmem' : cellOf T (k + 1) ∈ μ := (YoungDiagram.mem_cells _).mp (cellOf_mem T hkI')
  have hent : T.entry (cellOf T k).1 (cellOf T k).2 = k := entry_cellOf T hkI
  have hent' : T.entry (cellOf T (k + 1)).1 (cellOf T (k + 1)).2 = k + 1 := entry_cellOf T hkI'
  -- name the two cells' coordinates so the row/column hypotheses can be substituted cleanly
  rcases hcc : cellOf T k with ⟨i₁, j₁⟩
  rcases hcc' : cellOf T (k + 1) with ⟨i₂, j₂⟩
  rw [hcc] at hmem hent
  rw [hcc'] at hmem' hent'
  unfold SwapAdmissible
  rw [hcc, hcc']
  refine ⟨fun hrow => ?_, fun hcol => ?_⟩
  · subst hrow
    have hone : axialDist T k = 1 := axialDist_of_sameRow T hmem hmem' hent hent'
    rw [hone] at hsq
    exact hsq (by norm_num)
  · subst hcol
    have hone : axialDist T k = -1 := axialDist_of_sameCol T hmem hmem' hent hent'
    rw [hone] at hsq
    exact hsq (by norm_num)

/-- **One admissible swap step**, in the `SchurWeyl` API: `T'` is `T` with the labels `k` and
`k+1` exchanged. -/
def SwapStep (T T' : StandardYoungTableau μ) : Prop :=
  ∃ (k : ℕ) (hk : 1 ≤ k) (hkn : k + 1 ≤ μ.cells.card) (hadm : SwapAdmissible T k),
    T' = swapTableau T k hk hkn hadm

/-- The two `cellContent`s — `QOU.SchurWeyl`'s and `QOU.BraidKnot.JucysMurphy`'s — are distinct
declarations with the same body `c.2 − c.1`, so they agree definitionally.  Named so the transport
below never silently relies on that. -/
theorem braidKnot_cellContent_eq (c : ℕ × ℕ) :
    QOU.BraidKnot.JucysMurphy.cellContent c = cellContent c := rfl

/-- **The transport.**  An `AdjacentSwapStep` between the `BraidKnot` images is a `swapTableau`
step here.  The proof never touches `swapCellsSYT`: `AdjacentSwapStep` constrains only content
vectors, `swapTableau` has the matching content profile, and separation
(`syt_eq_of_cellContent_eq`) does the rest. -/
theorem swapStep_of_adjacentSwapStep {T T' : StandardYoungTableau μ}
    (h : QOU.BraidKnot.JucysMurphy.AdjacentSwapStep μ T.toBraidKnot T'.toBraidKnot) :
    SwapStep T T' := by
  obtain ⟨a, b, hab, hT'a, hT'b, hother, hne0, hsq⟩ := h
  simp only [braidKnot_cellContent_eq, ← cellOf_eq_tableauCellEquiv] at hT'a hT'b hother hne0 hsq
  have hcard : QOU.BraidKnot.Specht.nOf μ = μ.cells.card := rfl
  have hbv : (b : ℕ) < μ.cells.card := by have := b.isLt; omega
  set k : ℕ := (a : ℕ) + 1 with hkdef
  have hk : 1 ≤ k := by omega
  have hkn : k + 1 ≤ μ.cells.card := by omega
  have hb1 : k + 1 = (b : ℕ) + 1 := by rw [hab]
  -- the gap in the step *is* `axialDist T k`
  have hd : (axialDist T k) ^ 2 ≠ 1 := by
    have hax : axialDist T k
        = cellContent (cellOf T ((b : ℕ) + 1)) - cellContent (cellOf T k) := by
      unfold axialDist axialDistance
      rw [hb1]
    rw [hax]
    exact hsq
  have hadm : SwapAdmissible T k := swapAdmissible_of_sq_axialDist_ne_one T hk hkn hd
  refine ⟨k, hk, hkn, hadm, ?_⟩
  -- both tableaux have the same content profile, and separation makes that enough
  refine syt_eq_of_cellContent_eq T' _ (fun j hj1 hjc => ?_)
  by_cases hjk : j = k
  · subst hjk
    rw [cellOf_swapTableau_self T hk hkn hadm, hb1]
    exact hT'a
  by_cases hjk' : j = k + 1
  · subst hjk'
    rw [cellOf_swapTableau_succ T hk hkn hadm, hb1]
    exact hT'b
  · have hjI : j ∈ Set.Icc 1 μ.cells.card := Set.mem_Icc.mpr ⟨hj1, hjc⟩
    rw [cellOf_swapTableau_of_ne T hk hkn hadm hjI hjk hjk']
    have hs : ((⟨j - 1, by omega⟩ : Fin (QOU.BraidKnot.Specht.nOf μ)) : ℕ) + 1 = j := by
      show j - 1 + 1 = j
      omega
    have hsa : (⟨j - 1, by omega⟩ : Fin (QOU.BraidKnot.Specht.nOf μ)) ≠ a := by
      intro hcon
      have hv : j - 1 = (a : ℕ) := congrArg Fin.val hcon
      exact hjk (by omega)
    have hsb : (⟨j - 1, by omega⟩ : Fin (QOU.BraidKnot.Specht.nOf μ)) ≠ b := by
      intro hcon
      have hv : j - 1 = (b : ℕ) := congrArg Fin.val hcon
      exact hjk' (by omega)
    have := hother ⟨j - 1, by omega⟩ hsa hsb
    rwa [hs] at this

/-- **Connectivity in the `SchurWeyl` API.**  Any two standard tableaux of one shape are joined by
a chain of admissible `swapTableau` steps — `syt_adjacentSwap_connected` carried across the bridge. -/
theorem syt_swapStep_connected (T T' : StandardYoungTableau μ) :
    Relation.ReflTransGen (SwapStep (μ := μ)) T T' := by
  have hbk := QOU.BraidKnot.JucysMurphy.syt_adjacentSwap_connected μ T.toBraidKnot T'.toBraidKnot
  have hlift := Relation.ReflTransGen.lift
    (r := QOU.BraidKnot.JucysMurphy.AdjacentSwapStep μ) (p := SwapStep (μ := μ))
    (fun S : QOU.BraidKnot.StandardYoungTableau μ => S.toMathlib)
    (fun A B hAB => swapStep_of_adjacentSwapStep
      (by rwa [QOU.BraidKnot.toBraidKnot_toMathlib, QOU.BraidKnot.toBraidKnot_toMathlib]))
    hbk
  have hlift' : Relation.ReflTransGen (SwapStep (μ := μ))
      (T.toBraidKnot.toMathlib) (T'.toBraidKnot.toMathlib) := hlift
  rwa [QOU.BraidKnot.toMathlib_toBraidKnot, QOU.BraidKnot.toMathlib_toBraidKnot] at hlift' 

end QOU.SchurWeyl

