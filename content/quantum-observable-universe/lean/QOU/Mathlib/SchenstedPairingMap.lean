import QOU.Mathlib.SchenstedStandardGeneric

/-!
# The RSK pairing map `Sym n → Σ_λ SYT(λ)²`

**Brick 11.**  Packages the two standard tableaux of a permutation word — the
insertion tableau `P(w)` (`insertWordPSYT`, Brick 10) and the recording tableau
`Q̃(w)` (`insertWordSYT`, Brick 9b) — into a single dependent pair living in

    Σ μ : YoungDiagram, StandardYoungTableau μ × StandardYoungTableau μ,

the target `Σ_λ SYT(λ)²` of the Robinson–Schensted correspondence.  The pairing
is well-typed because `P(w)` and `Q̃(w)` share a *Young diagram*, not merely a
row-length list: `recordingShape_eq_pShape` lifts the row-length agreement
`insertWordRec_shape_eq_P` (through `shiftT_shape`) to an equality of
`YoungDiagram`s, so the recording tableau casts onto `P(w)`'s shape.

Two entry points:

* `rskPairWord` — for a *word* `w` whose content is `{1,…,n}` (a permutation
  word);
* `rskPair` — for a permutation `σ : Equiv.Perm (Fin n)`, via `wordOfPerm`.

This is the last structural brick before the RSK *inverse* (bumping reversal) and
the cardinality identity `Σ_{λ⊢n} (f^λ)² = n!` (`RSKBurnsideHolds n`) it feeds.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

open YoungDiagram Finset

/-- The **insertion shape** `pShape w`: the Young diagram of the insertion tableau
    `P(w)`, on its row-length shape. -/
noncomputable def pShape (w : List ℕ) : YoungDiagram :=
  ofRowLens (tableauShape (insertWord w)) (tableauShape_sorted (insertWord_colStrict w))

/-- **`Q̃(w)` and `P(w)` share a Young diagram.**  The recording shape equals the
    insertion shape: `insertWordRec_shape_eq_P` gives the row-length lists agree
    (`shiftT_shape` strips the `0→1` relabel), and `ofRowLens` of equal row-length
    lists is the same diagram (the `Sorted` proof is propositional). -/
theorem recordingShape_eq_pShape (w : List ℕ) : recordingShape w = pShape w := by
  have hL : tableauShape (shiftT (insertWordRec w).2) = tableauShape (insertWord w) := by
    rw [shiftT_shape, insertWordRec_shape_eq_P]
  unfold recordingShape pShape
  congr 1

/-- **The RSK pair of a permutation word.**  For a word `w` with content `{1,…,n}`,
    the insertion tableau `P(w)` and the recording tableau `Q̃(w)` — both standard,
    both of shape `pShape w` — packaged as a point of `Σ_λ SYT(λ)²`. -/
noncomputable def rskPairWord {w : List ℕ} {n : ℕ}
    (hw : (↑w : Multiset ℕ) = (↑(List.range n) : Multiset ℕ).map (· + 1)) :
    Σ μ : YoungDiagram, StandardYoungTableau μ × StandardYoungTableau μ :=
  ⟨pShape w, insertWordPSYT hw, recordingShape_eq_pShape w ▸ insertWordSYT w⟩

/-- The word read off a permutation `σ : Equiv.Perm (Fin n)`: `σ(0)+1, …, σ(n-1)+1`
    (values shifted into `{1,…,n}` so the insertion tableau is standard). -/
def wordOfPerm {n : ℕ} (σ : Equiv.Perm (Fin n)) : List ℕ :=
  (List.finRange n).map (fun i => (σ i : ℕ) + 1)

/-- **`wordOfPerm σ` is a permutation word.**  Its content is exactly `{1,…,n}`:
    `σ` permutes `Fin n`, so the underlying multiset of values is `range n`, and the
    `+1` shift lands it on `(range n).map (·+1)`. -/
theorem wordOfPerm_content {n : ℕ} (σ : Equiv.Perm (Fin n)) :
    (↑(wordOfPerm σ) : Multiset ℕ) = (↑(List.range n) : Multiset ℕ).map (· + 1) := by
  unfold wordOfPerm
  rw [Multiset.map_coe, Multiset.coe_eq_coe,
      show (fun i : Fin n => (σ i : ℕ) + 1)
        = (· + 1) ∘ (fun i : Fin n => (σ i : ℕ)) from rfl, ← List.map_map]
  -- `(finRange n).map (fun i => ↑(σ i))).map (·+1) ~ (range n).map (·+1)`
  refine List.Perm.map _ ?_
  -- `(finRange n).map (fun i => ↑(σ i)) ~ range n`
  refine (List.perm_ext_iff_of_nodup ?_ (List.nodup_range)).mpr (fun a => ?_)
  · exact (List.nodup_finRange n).map (fun x y h => σ.injective (Fin.val_injective h))
  · simp only [List.mem_map, List.mem_finRange, List.mem_range, true_and]
    constructor
    · rintro ⟨i, rfl⟩; exact (σ i).isLt
    · intro ha; exact ⟨σ.symm ⟨a, ha⟩, by simp⟩

/-- **The RSK pair of a permutation.**  `σ ↦ (P(wordOfPerm σ), Q̃(wordOfPerm σ))`,
    a point of `Σ_λ SYT(λ)²`.  The map underlying the Robinson–Schensted
    correspondence `Sym n ≃ Σ_λ SYT(λ)²`; bijectivity (via the bumping-reversal
    inverse) and the resulting `Σ_{λ⊢n} (f^λ)² = n!` are the remaining bricks. -/
noncomputable def rskPair {n : ℕ} (σ : Equiv.Perm (Fin n)) :
    Σ μ : YoungDiagram, StandardYoungTableau μ × StandardYoungTableau μ :=
  rskPairWord (wordOfPerm_content σ)

end QOU.Mathlib.Schensted
