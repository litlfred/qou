import QOU.Mathlib.SchenstedReadbackFold

/-!
# QOU.Mathlib.SchenstedRSKInjective — the RSK map is injective on words (brick 7)

Assembly. Bricks 1–6 built the inverse machinery; this file composes them into the statement they
were for:

> **`insertWordRec` is injective on words of a fixed length** — the pair `(P(w), Q(w))` determines
> `w`.

The chain, each link already proved:

1. brick 4 — `Q(w)` **is** `qAppendSteps [] (rowIndices [] w) 0`;
2. brick 6 — reading timestamp `k` off that recording tableau returns `(rowIndices [] w).getD k 0`;
3. so equal `Q`s (of equal length) force equal `rowIndices`;
4. brick 3 — equal `insertWord` **and** equal `rowIndices` force equal words.

## Why the length hypothesis

`qRowOf` locates timestamps `0, …, |w|-1`; nothing it says constrains indices past the end. Two
words of different lengths can therefore agree on every timestamp the shorter one has. In the RSK
application the length is fixed (`|w| = n` for a permutation of `Fin n`), so the hypothesis costs
nothing there — but it is a real hypothesis and is stated rather than hidden.

## Scope

Injectivity on the raw `List ℕ` layer. Lifting it to `SchenstedPairingMap.rskPair` (which is typed
in `StandardYoungTableau`) and proving surjectivity — and thence `RSKBurnsideHolds` — are the
remaining bricks of epic `qou-nrex`. Nothing here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- One row index per letter. -/
theorem rowIndices_length : ∀ (T : List (List ℕ)) (w : List ℕ),
    (rowIndices T w).length = w.length
  | _, [] => rfl
  | T, x :: rest => by
      rw [rowIndices_cons, List.length_cons, List.length_cons, rowIndices_length (insert T x) rest]

/-- **Equal recording tableaux force equal row-index records** (at equal word length). This is
brick 4 followed by brick 6: `Q` *is* the fold, and the fold is readable. -/
theorem rowIndices_eq_of_recording_eq (w w' : List ℕ) (hlen : w.length = w'.length)
    (hQ : (insertWordRec w).2 = (insertWordRec w').2) :
    rowIndices [] w = rowIndices [] w' := by
  have hl : (rowIndices [] w).length = (rowIndices [] w').length := by
    rw [rowIndices_length, rowIndices_length, hlen]
  refine List.ext_getElem hl (fun k hk hk' => ?_)
  have hkw : k < (rowIndices [] w).length := hk
  have hkw' : k < (rowIndices [] w').length := hk'
  have h1 := qRowOf_qAppendSteps_zero (rowIndices [] w) k hkw
  have h2 := qRowOf_qAppendSteps_zero (rowIndices [] w') k hkw'
  rw [← insertWordRec_snd_eq_qAppendSteps] at h1 h2
  rw [hQ, h2] at h1
  have hgd := Option.some.inj h1.symm
  simpa [List.getD_eq_getElem?_getD, List.getElem?_eq_getElem hkw,
    List.getElem?_eq_getElem hkw'] using hgd

/-- **The RSK map is injective on words of a fixed length.** The pair `(P(w), Q(w))` determines
`w`. -/
theorem word_eq_of_insertWordRec_eq (w w' : List ℕ) (hlen : w.length = w'.length)
    (h : insertWordRec w = insertWordRec w') : w = w' := by
  have hP : insertWord w = insertWord w' := by
    rw [← insertWordRec_fst, ← insertWordRec_fst, h]
  have hQ : (insertWordRec w).2 = (insertWordRec w').2 := by rw [h]
  exact word_eq_of_insertWord_eq w w' hP (rowIndices_eq_of_recording_eq w w' hlen hQ)

/-- Contrapositive form: distinct words of the same length have distinct `(P, Q)` pairs. -/
theorem insertWordRec_ne_of_ne (w w' : List ℕ) (hlen : w.length = w'.length) (hne : w ≠ w') :
    insertWordRec w ≠ insertWordRec w' :=
  fun h => hne (word_eq_of_insertWordRec_eq w w' hlen h)

end QOU.Mathlib.Schensted
