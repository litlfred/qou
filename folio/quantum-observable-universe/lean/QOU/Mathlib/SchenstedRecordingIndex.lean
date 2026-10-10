import QOU.Mathlib.SchenstedWordRecovery
import QOU.Mathlib.SchenstedRecording

/-!
# QOU.Mathlib.SchenstedRecordingIndex — the recording tableau *is* the row-index record

Brick 4 of epic `qou-nrex` (RSK inverse).

Brick 3 showed the word is recoverable from the insertion tableau **plus** the list of rows each
step appended to (`rowIndices`). That list looked like extra data. It is not: it is exactly what
the recording tableau `Q(w)` holds. This file proves the identification, at both levels.

* `qAppend Q i s` — write timestamp `s` at the end of `Q`'s row `i`. This is precisely the
  bookkeeping `insertRec` performs on its `Q` argument, extracted as a function of the row index.
* **`insertRec_snd_eq_qAppend`** — one step: `(insertRec P Q x s).2 = qAppend Q (newRowIndex P x) s`.
  So the row `insertRec` writes into is the row `insert` appends to — the same `newRowIndex` brick
  2 defined, with no separate notion of "where `Q` grew".
* `qAppendSteps` / **`insertWordRecAux_snd_eq_qAppendSteps`** — the whole fold:
  `Q(w)` is `qAppend`ed along `rowIndices`, timestamps counting up from the start index.
* **`insertWordRec_snd_eq_qAppendSteps`** — at the empty tableau, the form the inverse consumes.

## What this closes

Brick 3's `word_eq_of_insertWord_eq` needed equal insertion tableaux **and** equal index records.
The index record is now a function of `Q` rather than side information, so the pair `(P, Q)` alone
determines the word — the injectivity half of the RSK bijection, modulo reading `rowIndices` back
off `Q` (which is where the timestamps' `Nodup`/`range` content from `SchenstedRecording` enters).

## Scope

The forward identification only: `Q` is built by these appends. Recovering `rowIndices` *from* a
given `Q` — inverting `qAppendSteps` — is the next step, and `rskPair` bijectivity and
`RSKBurnsideHolds` are past it. Nothing here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- **Write a timestamp at the end of a row.** `qAppend Q i s` appends `s` to `Q`'s row `i`,
reading rows with `headD`/`tail` exactly as `insertRec` does — so a row index past the end creates
the row rather than failing. -/
def qAppend : List (List ℕ) → ℕ → ℕ → List (List ℕ)
  | Q, 0, s => (Q.headD [] ++ [s]) :: Q.tail
  | Q, i + 1, s => Q.headD [] :: qAppend Q.tail i s

@[simp] theorem qAppend_zero (Q : List (List ℕ)) (s : ℕ) :
    qAppend Q 0 s = (Q.headD [] ++ [s]) :: Q.tail := rfl

@[simp] theorem qAppend_succ (Q : List (List ℕ)) (i s : ℕ) :
    qAppend Q (i + 1) s = Q.headD [] :: qAppend Q.tail i s := rfl

/-- **One step: the recording write happens at the insertion row.**

`insertRec`'s `Q`-bookkeeping is `qAppend` at `newRowIndex P x` — the very index brick 2 defined
from `insert`'s recursion. The two notions of "which row grew" are the same notion. -/
theorem insertRec_snd_eq_qAppend :
    ∀ (P Q : List (List ℕ)) (x s : ℕ), tableauShape P = tableauShape Q →
      (insertRec P Q x s).2 = qAppend Q (newRowIndex P x) s
  | [], [], _, _ => fun _ => rfl
  | [], _ :: _, _, _ => fun h => by simp [tableauShape] at h
  | _ :: _, [], _, _ => fun h => by simp [tableauShape] at h
  | prow :: prest, qrow :: qrest, x, s => by
      intro h
      simp only [tableauShape_cons] at h
      injection h with _ hqs
      rw [insertRec, newRowIndex]
      cases hb : (rowInsert prow x).2 with
      | none => rfl
      | some y =>
          simp only [List.headD_cons, List.tail_cons]
          rw [qAppend_succ, List.tail_cons, insertRec_snd_eq_qAppend prest qrest y s hqs,
            List.headD_cons]

/-- Iterated `qAppend`: write timestamps `s, s+1, …` at the given rows, in order. -/
def qAppendSteps : List (List ℕ) → List ℕ → ℕ → List (List ℕ)
  | Q, [], _ => Q
  | Q, i :: rest, s => qAppendSteps (qAppend Q i s) rest (s + 1)

@[simp] theorem qAppendSteps_nil (Q : List (List ℕ)) (s : ℕ) : qAppendSteps Q [] s = Q := rfl

theorem qAppendSteps_cons (Q : List (List ℕ)) (i : ℕ) (rest : List ℕ) (s : ℕ) :
    qAppendSteps Q (i :: rest) s = qAppendSteps (qAppend Q i s) rest (s + 1) := rfl

/-- **The whole fold.** `Q` is grown by appending each timestamp at its step's insertion row. -/
theorem insertWordRecAux_snd_eq_qAppendSteps :
    ∀ (w : List ℕ) (s : ℕ) (P Q : List (List ℕ)), tableauShape P = tableauShape Q →
      (insertWordRecAux w s P Q).2 = qAppendSteps Q (rowIndices P w) s
  | [], _, _, _ => fun _ => rfl
  | x :: rest, s, P, Q => by
      intro h
      rw [insertWordRecAux, rowIndices_cons, qAppendSteps_cons,
        insertWordRecAux_snd_eq_qAppendSteps rest (s + 1) _ _
          (insertRec_shape P Q x s h).symm,
        insertRec_snd_eq_qAppend P Q x s h, insertRec_fst_eq_insert]

/-- **At the empty tableau** — the form the RSK inverse consumes: `Q(w)` is the result of appending
`0, 1, …, |w|-1` at the rows `rowIndices [] w`. -/
theorem insertWordRec_snd_eq_qAppendSteps (w : List ℕ) :
    (insertWordRec w).2 = qAppendSteps [] (rowIndices [] w) 0 :=
  insertWordRecAux_snd_eq_qAppendSteps w 0 [] [] rfl

end QOU.Mathlib.Schensted
