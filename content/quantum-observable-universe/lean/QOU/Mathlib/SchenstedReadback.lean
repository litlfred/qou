import QOU.Mathlib.SchenstedRecordingIndex

/-!
# QOU.Mathlib.SchenstedReadback — reading the row indices back off `Q` (RSK inverse, brick 5)

Brick 4 showed `Q(w)` is built by `qAppend`ing timestamp `s` at row `rowIndices[s]`. This file
reads that back: **`qRowOf Q t`** locates the row of `Q` holding `t`, and the two lemmas below say
`qAppend` puts the new timestamp exactly where brick 4 says and disturbs nothing else.

* `qRowOf` — the row index of `t` in `Q`, as an `Option`.
* **`qRowOf_qAppend_self`** — `qRowOf (qAppend Q i s) s = some i`, when `s` is fresh for `Q`.
* **`qRowOf_qAppend_of_ne`** — for `t ≠ s`, appending `s` does not move `t`.

## The freshness hypothesis is not bookkeeping

`qRowOf` returns the *first* row containing `t`, so if `t` already occurs in `Q` the append cannot
be located by looking for `t` — an earlier copy shadows it. Freshness is what makes the read-back a
function of `Q` instead of a search with ties. In the RSK setting it is supplied by
`SchenstedRecording.insertWordRec_snd_content`: the recording content is exactly `range |w|`, each
timestamp occurring **once**, so every append is fresh at the moment it happens. That theorem was
proved a while ago with no consumer; this is what it was for.

## Scope

The single-step read-back. Threading it along `qAppendSteps` to recover the whole index list — and
thence `rskPair` injectivity, surjectivity, and `RSKBurnsideHolds` — is brick 6 and beyond. Nothing
here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- **Locate a timestamp.** The index of the first row of `Q` containing `t`, if any. -/
def qRowOf : List (List ℕ) → ℕ → Option ℕ
  | [], _ => none
  | r :: T, t => if t ∈ r then some 0 else (qRowOf T t).map (· + 1)

@[simp] theorem qRowOf_nil (t : ℕ) : qRowOf [] t = none := rfl

theorem qRowOf_cons (r : List ℕ) (T : List (List ℕ)) (t : ℕ) :
    qRowOf (r :: T) t = if t ∈ r then some 0 else (qRowOf T t).map (· + 1) := rfl

/-- A timestamp absent from every row is not located. -/
theorem qRowOf_eq_none : ∀ (Q : List (List ℕ)) (t : ℕ), (∀ r ∈ Q, t ∉ r) → qRowOf Q t = none
  | [], _, _ => rfl
  | r :: T, t, h => by
      rw [qRowOf_cons, if_neg (h r (List.mem_cons_self ..)),
        qRowOf_eq_none T t (fun s hs => h s (List.mem_cons_of_mem r hs))]
      rfl

/-- **The append is where brick 4 says it is.** A fresh timestamp lands in the row it was written
to. -/
theorem qRowOf_qAppend_self : ∀ (Q : List (List ℕ)) (i s : ℕ), (∀ r ∈ Q, s ∉ r) →
    qRowOf (qAppend Q i s) s = some i
  | Q, 0, s, _ => by
      rw [qAppend_zero, qRowOf_cons, if_pos (by simp)]
  | [], i + 1, s, _ => by
      rw [qAppend_succ, qRowOf_cons]
      simp only [List.headD_nil, List.not_mem_nil, if_false, List.tail_nil]
      rw [qRowOf_qAppend_self [] i s (by simp)]
      rfl
  | r :: T, i + 1, s, h => by
      rw [qAppend_succ, qRowOf_cons, List.headD_cons, List.tail_cons,
        if_neg (h r (List.mem_cons_self ..)),
        qRowOf_qAppend_self T i s (fun q hq => h q (List.mem_cons_of_mem r hq))]
      rfl

/-- **Appending disturbs nothing else.** Timestamps other than the one written keep their rows. -/
theorem qRowOf_qAppend_of_ne : ∀ (Q : List (List ℕ)) (i s t : ℕ), t ≠ s →
    qRowOf (qAppend Q i s) t = qRowOf Q t
  | [], 0, s, t, hts => by
      rw [qAppend_zero, qRowOf_cons]
      simp [hts]
  | r :: T, 0, s, t, hts => by
      rw [qAppend_zero, qRowOf_cons, qRowOf_cons, List.headD_cons, List.tail_cons]
      by_cases hr : t ∈ r
      · rw [if_pos hr, if_pos (List.mem_append_left _ hr)]
      · rw [if_neg hr, if_neg (by simp [hr, hts])]
  | [], i + 1, s, t, hts => by
      rw [qAppend_succ, qRowOf_cons]
      simp only [List.headD_nil, List.not_mem_nil, if_false, List.tail_nil]
      rw [qRowOf_qAppend_of_ne [] i s t hts]
      simp
  | r :: T, i + 1, s, t, hts => by
      rw [qAppend_succ, qRowOf_cons, qRowOf_cons, List.headD_cons, List.tail_cons]
      by_cases hr : t ∈ r
      · rw [if_pos hr, if_pos hr]
      · rw [if_neg hr, if_neg hr, qRowOf_qAppend_of_ne T i s t hts]

end QOU.Mathlib.Schensted
