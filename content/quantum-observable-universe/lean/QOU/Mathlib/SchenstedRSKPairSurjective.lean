import QOU.Mathlib.SchenstedWordOfPermSurj
import QOU.Mathlib.SchenstedShapeOfPositions
import QOU.Mathlib.SchenstedRSKSurjective

/-!
# QOU.Mathlib.SchenstedRSKPairSurjective — `rskPair` hits every standard pair

Brick 38 of epic `qou-nrex` (RSK inverse), and the end of the arc that began at brick 10.

**`exists_rskPair_eq`** — for any Young diagram `μ` and any two standard Young tableaux of shape
`μ`, some permutation of `Fin |μ|` has that pair as its RSK image.

Everything it needs is proved: brick 32 recovers the word, brick 35 says the list representation is
faithful, brick 36 turns the word into a permutation, brick 37 supplies the shape hypothesis from
"the pair shares a shape". What is left is the plumbing, and the plumbing is dependent-type work:
`rskPairWord` is a `Σ` whose second component has already been transported along
`recordingShape_eq_pShape`, so comparing it with `⟨μ, S_P, S_Q⟩` means moving three things at once.

`sigma_pair_ext_entry` does it in the only way that stays honest: substitute the diagram equality,
then compare entries — and `entry_cast` says the transport does not move any entry, which is what
makes the second component comparable at all. Under the transport the recording tableau is
`shiftT` of the `0`-based one, so `shiftT_unshiftT` is what closes that leg — the down-shift of
brick 34 undone, on entries the content fact already knows are positive.

## Scope

Surjectivity. **Not** bijectivity: injectivity is `SchenstedRSKInjective`, stated for words, and
combining the two into an `Equiv` — and thence `RSKBurnsideHolds` for general `n` — is not done
here. `RSKBurnsideHolds` remains proved only for `n ≤ 12`, by `rskBurnsideHolds_le12`, a route with
no RSK correspondence in it.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Scope note superseded (2026-08-23).** The scope paragraph above records the state of the arc when
this brick landed. `RSKBurnsideHolds` is now proved for **every** `n`
(`QOU.Mathlib.rskBurnsideHolds`, brick 42), and `SnIsotypicSpechtSplit` is inhabited, so any
statement here that they "remain open" or hold "only for `n ≤ 12`" describes history rather than the
corpus. The per-brick scope is otherwise unchanged and still accurate.

-/

namespace QOU.Mathlib.Schensted

open YoungDiagram

/-- Transporting a standard tableau along an equality of diagrams does not move its entries. -/
theorem entry_cast {μ ν : YoungDiagram} (h : μ = ν) (S : QOU.Mathlib.StandardYoungTableau μ)
    (i j : ℕ) : (h ▸ S).entry i j = S.entry i j := by
  subst h; rfl

/-- Extensionality for a diagram carrying a *pair* of tableaux. -/
theorem sigma_pair_ext_entry {μ ν : YoungDiagram}
    {S₁ S₂ : QOU.Mathlib.StandardYoungTableau μ} {T₁ T₂ : QOU.Mathlib.StandardYoungTableau ν}
    (h : μ = ν) (h1 : ∀ i j, S₁.entry i j = T₁.entry i j)
    (h2 : ∀ i j, S₂.entry i j = T₂.entry i j) :
    (⟨μ, S₁, S₂⟩ : Σ ρ : YoungDiagram, QOU.Mathlib.StandardYoungTableau ρ ×
      QOU.Mathlib.StandardYoungTableau ρ) = ⟨ν, T₁, T₂⟩ := by
  subst h
  rw [QOU.Mathlib.StandardYoungTableau.ext_entry h1,
    QOU.Mathlib.StandardYoungTableau.ext_entry h2]

/-- Shifting a row down and back up is the identity on positive entries. -/
theorem map_pred_succ : ∀ (row : List ℕ), (∀ a ∈ row, 1 ≤ a) →
    (row.map (· - 1)).map (· + 1) = row
  | [], _ => rfl
  | a :: t, h => by
      have ha : 1 ≤ a := h a (List.mem_cons_self ..)
      simp only [List.map_cons]
      rw [map_pred_succ t (fun b hb => h b (List.mem_cons_of_mem a hb))]
      congr 1
      omega

/-- **`shiftT` undoes `unshiftT`** on a tableau of positive entries. -/
theorem shiftT_unshiftT {Q : List (List ℕ)} (h : ∀ a ∈ Q.flatten, 1 ≤ a) :
    shiftT (unshiftT Q) = Q := by
  rw [shiftT, unshiftT, List.map_map]
  refine List.ext_getElem (by simp) (fun i _ h2 => ?_)
  simp only [List.getElem_map, Function.comp_apply]
  exact map_pred_succ Q[i] (fun a ha => h a (List.mem_flatten.mpr ⟨Q[i], List.getElem_mem h2, ha⟩))

/-- **The RSK pair of a word that bridges to `(S_P, S_Q)` is `⟨μ, S_P, S_Q⟩`.** -/
theorem rskPairWord_eq_of_bridge {w : List ℕ} {n : ℕ}
    (hw : (↑w : Multiset ℕ) = (↑(List.range n) : Multiset ℕ).map (· + 1))
    {μ : YoungDiagram} (SP SQ : QOU.Mathlib.StandardYoungTableau μ)
    (hP : insertWord w = toListTableau SP)
    (hQ : (insertWordRec w).2 = toRecordingTableau SQ) :
    rskPairWord hw = ⟨μ, SP, SQ⟩ := by
  have hshapeP : pShape w = μ := by
    rw [pShape]
    exact (ofRowLens_congr _ μ.rowLens_sorted
      (by rw [hP, tableauShape_toListTableau])).trans ofRowLens_to_rowLens_eq_self
  refine sigma_pair_ext_entry hshapeP (fun i j => ?_) (fun i j => ?_)
  · show ((insertWord w).getD i []).getD j 0 = SP.entry i j
    rw [hP]
    exact getD_getD_toListTableau_all SP i j
  · rw [entry_cast]
    show ((shiftT (insertWordRec w).2).getD i []).getD j 0 = SQ.entry i j
    rw [hQ, toRecordingTableau, shiftT_unshiftT (pos_of_mem_flatten_toListTableau SQ)]
    exact getD_getD_toListTableau_all SQ i j

/-- **`rskPair` is surjective onto standard pairs.** Every pair of standard Young tableaux of a
common shape `μ` is the RSK image of a permutation of `Fin |μ|`. -/
theorem exists_rskPair_eq {μ : YoungDiagram} (SP SQ : QOU.Mathlib.StandardYoungTableau μ) :
    ∃ σ : Equiv.Perm (Fin μ.cells.card),
      rskPair σ = ⟨μ, SP, SQ⟩ := by
  set n := μ.cells.card with hn
  set P := toListTableau SP with hPdef
  set Q := toRecordingTableau SQ with hQdef
  have hrange : ∀ t, t < n → t ∈ Q.flatten :=
    fun t ht => (mem_flatten_toRecordingTableau SQ).mpr ht
  have hlt : ∀ a ∈ Q.flatten, a < n :=
    fun a ha => (mem_flatten_toRecordingTableau SQ).mp ha
  have hshape : tableauShape P = addCellSteps [] (qPositions Q n) := by
    rw [addCellSteps_qPositions (colStrict_toRecordingTableau SQ)
      (rows_strict_toRecordingTableau SQ) (nodup_flatten_toRecordingTableau SQ)
      (noEmptyRows_toRecordingTableau SQ) hrange hlt,
      tableauShape_toListTableau, tableauShape_toRecordingTableau]
  have hpair : insertWordRec (uninsertSteps P (qPositions Q n)).2 = (P, Q) :=
    insertWordRec_uninsertSteps_of_standard (rowsSorted_toListTableau SP)
      (colStrict_toListTableau SP) (noEmptyRows_toListTableau SP)
      (colStrict_toRecordingTableau SQ) (rows_strict_toRecordingTableau SQ)
      (nodup_flatten_toRecordingTableau SQ) (noEmptyRows_toRecordingTableau SQ)
      hrange hlt hshape
  have hfst : insertWord (uninsertSteps P (qPositions Q n)).2 = P := by
    rw [← insertWordRec_fst, hpair]
  have hsnd : (insertWordRec (uninsertSteps P (qPositions Q n)).2).2 = Q := by rw [hpair]
  have hwc : (↑(uninsertSteps P (qPositions Q n)).2 : Multiset ℕ)
      = (↑(List.range n) : Multiset ℕ).map (· + 1) := by
    rw [← insertWord_content, hfst, hPdef, content_toListTableau]
  obtain ⟨σ, hσ⟩ := exists_wordOfPerm_eq hwc
  refine ⟨σ, ?_⟩
  rw [rskPair]
  exact rskPairWord_eq_of_bridge _ SP SQ (by rw [hσ, hfst]) (by rw [hσ, hsnd])

end QOU.Mathlib.Schensted
