import QOU.Mathlib.SYTInsertMax

/-!
# QOU.Mathlib.SYTBranchingBijection — the deletion/insertion maps are mutually inverse

`eraseMax` (delete the max-value corner) and `insertMax` (re-insert `|μ|` at a corner) are mutually
inverse.  Together with the structural counting bridge this is the Greene–Nijenhuis–Wilf branching
bijection `StandardYoungTableau μ ≃ ⨆_{corners c} StandardYoungTableau (μ ∖ c)`.

Pure combinatorics; nothing archimedean; no fit.
-/

namespace QOU.Mathlib

open YoungDiagram

variable {μ : YoungDiagram}

/-- Two standard tableaux of the same shape are equal when their entry maps agree (`bijOn` is a
`Prop`, hence proof-irrelevant). -/
theorem syt_ext {T1 T2 : StandardYoungTableau μ} (h : ∀ i j, T1.entry i j = T2.entry i j) :
    T1 = T2 := by
  have hs : T1.toSsyt = T2.toSsyt := SemistandardYoungTableau.ext (fun i j => h i j)
  cases T1; cases T2; cases hs; rfl

/-- **Roundtrip 1.** Deleting the max corner and re-inserting `|μ|` recovers `T`. -/
theorem insertMax_eraseMax (T : StandardYoungTableau μ) (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (hmax : T.entry c.1 c.2 = μ.cells.card) :
    insertMax c hc (eraseMax T c hc hmax) = T := by
  apply syt_ext
  intro i j
  show (if (i, j) = c then μ.cells.card else (eraseMax T c hc hmax).entry i j) = T.entry i j
  by_cases hij : (i, j) = c
  · rw [if_pos hij]
    obtain ⟨rfl, rfl⟩ := Prod.ext_iff.mp hij
    exact hmax.symm
  · rw [if_neg hij]
    show (if (i, j) ∈ (eraseCorner μ c hc).cells then T.entry i j else 0) = T.entry i j
    by_cases hijμ : (i, j) ∈ μ
    · rw [if_pos ((mem_cells _).mpr ((mem_eraseCorner μ c hc (i, j)).mpr ⟨hijμ, hij⟩))]
    · rw [if_neg (fun h => hijμ ((mem_eraseCorner μ c hc (i, j)).mp ((mem_cells _).mp h)).1)]
      exact (T.toSsyt.zeros hijμ).symm

/-- **The re-inserted tableau carries `|μ|` at the corner** (so it has a max corner there). -/
theorem entry_insertMax_corner (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) :
    (insertMax c hc S).entry c.1 c.2 = μ.cells.card := by
  show (if (c.1, c.2) = c then μ.cells.card else S.entry c.1 c.2) = μ.cells.card
  rw [if_pos rfl]

/-- **Roundtrip 2.** Re-inserting `|μ|` at `c` and deleting that corner recovers `S`. -/
theorem eraseMax_insertMax (c : ℕ × ℕ) (hc : IsCornerCell μ c)
    (S : StandardYoungTableau (eraseCorner μ c hc)) :
    eraseMax (insertMax c hc S) c hc (entry_insertMax_corner c hc S) = S := by
  apply syt_ext
  intro i j
  show (if (i, j) ∈ (eraseCorner μ c hc).cells then (insertMax c hc S).entry i j else 0)
    = S.entry i j
  by_cases hijν : (i, j) ∈ (eraseCorner μ c hc).cells
  · rw [if_pos hijν]
    have hijne : (i, j) ≠ c := ((mem_eraseCorner μ c hc (i, j)).mp ((mem_cells _).mp hijν)).2
    show (if (i, j) = c then μ.cells.card else S.entry i j) = S.entry i j
    rw [if_neg hijne]
  · rw [if_neg hijν]
    exact (S.toSsyt.zeros (fun h => hijν ((mem_cells _).mpr h))).symm

end QOU.Mathlib
