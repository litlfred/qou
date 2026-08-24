import QOU.Mathlib.SchenstedRecordingOfSYT

/-!
# QOU.Mathlib.SchenstedSYTRoundTrip — the bridge is an inverse

Brick 35 of epic `qou-nrex` (RSK inverse).

Brick 10's `listStandardYT` turns a list tableau into a standard Young tableau; bricks 33–34 turn
one back. This file proves the composite is the identity:

**`sigma_listStandardYT_toListTableau`** — `⟨_, listStandardYT (toListTableau S) …⟩ = ⟨μ, S⟩`.

## Why the statement is a `Sigma`

`listStandardYT` lands on the diagram `ofRowLens (tableauShape T) …`, which is only *propositionally*
equal to `μ`. So the two tableaux do not have the same type and cannot be compared directly. Packing
the diagram alongside the tableau is what makes the equation statable, and it is the form
`rskPair`'s codomain takes anyway.

The dependent-type work is confined to two small lemmas — `ofRowLens_congr` (equal row-length lists
give equal diagrams, by `subst`, the sortedness proofs being irrelevant) and `sigma_ext_entry`
(substitute the diagram, then compare entries). Everything else is entrywise on `ℕ` and has no cast
in it: `getD_getD_toListTableau_all` says the list tableau reads back the tableau's entries at
*every* index, on the diagram and off it — off it both sides are `0`, one by `getD` past the end and
the other by the SSYT's own `zeros`.

## Scope

The bridge only. Two gaps remain between here and `rskPair` surjectivity, both named on the epic
bean: threading the `Σ`-equality through `rskPair`'s definition, and the fact that a recovered word
of content `{1, …, n}` comes from a permutation (`∃ σ, wordOfPerm σ = w`). `rskPair` bijectivity is
not claimed and `RSKBurnsideHolds` for general `n` remains open.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.StandardYoungTableau

variable {μ : YoungDiagram}

/-- **Extensionality by entries.** Two standard tableaux on the same diagram agreeing at every
index are equal — the `bijOn` fields are proofs, so they carry no extra data. -/
theorem ext_entry {S T : StandardYoungTableau μ} (h : ∀ i j, S.entry i j = T.entry i j) : S = T := by
  have hssyt : S.toSsyt = T.toSsyt := SemistandardYoungTableau.ext h
  cases S; cases T; cases hssyt; rfl

end QOU.Mathlib.StandardYoungTableau

namespace QOU.Mathlib.Schensted

open YoungDiagram

variable {μ : YoungDiagram}

/-- `content` is the flattening, as a multiset. -/
theorem content_eq_flatten : ∀ (Q : List (List ℕ)), content Q = (↑Q.flatten : Multiset ℕ)
  | [] => rfl
  | r :: T => by
      rw [content_cons, content_eq_flatten T, List.flatten_cons]
      simp

/-- **The content of the bridged tableau is `{1, …, |μ|}`** — the hypothesis `listStandardYT` takes,
in the multiset form it takes it. Both sides are duplicate-free with the same members. -/
theorem content_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    content (toListTableau S) = (↑(List.range μ.cells.card) : Multiset ℕ).map (· + 1) := by
  have hinj : Function.Injective (fun x : ℕ => x + 1) := fun a b h => by simpa using h
  rw [content_eq_flatten]
  refine (Multiset.Nodup.ext ?_ ?_).mpr (fun a => ?_)
  · rw [Multiset.coe_nodup]; exact nodup_flatten_toListTableau S
  · rw [Multiset.map_coe, Multiset.coe_nodup]; exact List.nodup_range.map hinj
  · rw [Multiset.mem_coe, mem_flatten_toListTableau_iff_Icc, Multiset.map_coe, Multiset.mem_coe,
      List.mem_map]
    constructor
    · rintro ⟨h1, h2⟩
      exact ⟨a - 1, List.mem_range.mpr (by omega), by omega⟩
    · rintro ⟨b, hb, rfl⟩
      rw [List.mem_range] at hb
      omega

/-- **The list tableau reads back every entry** — on the diagram by construction, off it because
both sides are `0`: the list runs out, and a semistandard tableau vanishes off its shape. -/
theorem getD_getD_toListTableau_all (S : QOU.Mathlib.StandardYoungTableau μ) (i j : ℕ) :
    ((toListTableau S).getD i []).getD j 0 = S.entry i j := by
  by_cases hj : j < μ.rowLen i
  · have hcell : (i, j) ∈ μ := mem_iff_lt_rowLen.mpr hj
    have hi : i < (toListTableau S).length := by
      rw [length_toListTableau, length_rowLens]
      exact mem_iff_lt_colLen.mp (μ.up_left_mem (le_refl i) (Nat.zero_le j) hcell)
    exact getD_getD_toListTableau S hi hj
  · have hz : S.entry i j = 0 :=
      S.toSsyt.zeros (fun hc => hj (mem_iff_lt_rowLen.mp hc))
    rw [hz]
    by_cases hi : i < (toListTableau S).length
    · rw [getD_row_eq hi, getElem_toListTableau S hi,
        getD_past (by simpa using Nat.not_lt.mp hj)]
    · rw [getD_row_past (Nat.not_lt.mp hi), List.getD_nil]

/-- Equal row-length lists give equal diagrams; the sortedness proofs are irrelevant. -/
theorem ofRowLens_congr {w w' : List ℕ} (hw : List.Sorted (· ≥ ·) w)
    (hw' : List.Sorted (· ≥ ·) w') (h : w = w') : ofRowLens w hw = ofRowLens w' hw' := by
  subst h; rfl

/-- The diagram the bridge lands on **is** `μ`. -/
theorem shape_toListTableau_eq (S : QOU.Mathlib.StandardYoungTableau μ) :
    ofRowLens (tableauShape (toListTableau S))
      (tableauShape_sorted (colStrict_toListTableau S)) = μ :=
  (ofRowLens_congr _ μ.rowLens_sorted (tableauShape_toListTableau S)).trans
    ofRowLens_to_rowLens_eq_self

/-- Comparing tableaux on *different* diagrams: substitute the diagram, then compare entries. -/
theorem sigma_ext_entry {ν : YoungDiagram} {S : QOU.Mathlib.StandardYoungTableau μ}
    {T : QOU.Mathlib.StandardYoungTableau ν} (h : μ = ν)
    (he : ∀ i j, S.entry i j = T.entry i j) :
    (⟨μ, S⟩ : Σ ρ : YoungDiagram, QOU.Mathlib.StandardYoungTableau ρ) = ⟨ν, T⟩ := by
  subst h
  rw [QOU.Mathlib.StandardYoungTableau.ext_entry he]

/-- **The bridge is an inverse.** Reading a standard Young tableau into the list representation and
realising it again returns the tableau — diagram and all. -/
theorem sigma_listStandardYT_toListTableau (S : QOU.Mathlib.StandardYoungTableau μ) :
    (⟨_, listStandardYT (rowsSorted_toListTableau S) (colStrict_toListTableau S)
        (content_toListTableau S)⟩ :
      Σ ρ : YoungDiagram, QOU.Mathlib.StandardYoungTableau ρ) = ⟨μ, S⟩ :=
  sigma_ext_entry (shape_toListTableau_eq S) (getD_getD_toListTableau_all S)

end QOU.Mathlib.Schensted
