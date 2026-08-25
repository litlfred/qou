import QOU.Mathlib.SchenstedStandardCount
import QOU.Mathlib.SchenstedRecordingIndex

/-!
# QOU.Mathlib.SchenstedRecordingTrunc — rebuilding a recording tableau from its positions

Bricks 30 and 31 of epic `qou-nrex` (RSK inverse).

Brick 4 showed a recording tableau is built by `qAppendSteps`: timestamp `t` written at the end of
row `p t`. Brick 24 read the positions back off a finished `Q` as `qPositions`. This file closes the
loop — the appends replay `Q` exactly:

**`qAppendSteps_qPositions`** — `qAppendSteps [] (qPositions Q n) 0 = qTrunc Q n`, and hence
**`qAppendSteps_qPositions_self`** — `= Q` once the horizon `n` clears every entry.

The intermediate object is the horizon truncation `qTrunc Q n`: the timestamps of `Q` below `n`,
with the rows that have emptied dropped. It is what the partial replay has built, and stating the
induction at it is what makes the step provable — the replay after `n` steps is *not* `Q`, and the
naive statement has nothing to induct on.

The step `qAppend_qTrunc` is where the tableau structure enters. Two facts do the work, and both
are consequences of column strictness rather than of the appends:

* the truncation's non-empty rows are an initial segment, so a row index means the same thing in
  `qTrunc Q t` as in `Q` (`exists_le_head` — an entry anywhere has a strictly smaller entry in the
  top row);
* a timestamp is written at the *end* of its row, because the row is strictly increasing and every
  smaller entry of that row is already present (`filter_lt_succ_mem`).

## Scope

The `Q` half of the correspondence's forward direction only: positions replay to the tableau. It
does not say the recovered *word* has these positions — that is brick 29 — and assembling both into
`insertWordRec w = (P, Q)` is the next brick. `rskPair` bijectivity and `RSKBurnsideHolds` for
general `n` are past that and are not claimed here.

Pure combinatorics on `ℕ`; nothing archimedean; no fit.
-/

namespace QOU.Mathlib.Schensted

/-- **The horizon truncation.** `qTrunc Q n` keeps the timestamps of `Q` below `n`, stopping at the
first row that has emptied. On a standard tableau the emptied rows are exactly the bottom ones, so
stopping at the first is the same as dropping them all — and it keeps the recursion structural. -/
def qTrunc : List (List ℕ) → ℕ → List (List ℕ)
  | [], _ => []
  | row :: rest, n =>
      if row.filter (· < n) = [] then [] else (row.filter (· < n)) :: qTrunc rest n

@[simp] theorem qTrunc_nil (n : ℕ) : qTrunc [] n = [] := rfl

theorem qTrunc_cons (row : List ℕ) (rest : List (List ℕ)) (n : ℕ) :
    qTrunc (row :: rest) n =
      if row.filter (· < n) = [] then [] else (row.filter (· < n)) :: qTrunc rest n := rfl

/-- Nothing is below a zero horizon. -/
theorem filter_lt_eq_nil : ∀ (row : List ℕ) {n : ℕ}, (∀ a ∈ row, n ≤ a) → row.filter (· < n) = []
  | [], _, _ => rfl
  | a :: t, n, h => by
      have ha : ¬ a < n := by have := h a (List.mem_cons_self ..); omega
      rw [List.filter_cons, if_neg (by simpa using ha)]
      exact filter_lt_eq_nil t (fun b hb => h b (List.mem_cons_of_mem a hb))

/-- Everything is below a horizon that clears the row. -/
theorem filter_lt_eq_self : ∀ (row : List ℕ) {n : ℕ}, (∀ a ∈ row, a < n) → row.filter (· < n) = row
  | [], _, _ => rfl
  | a :: t, n, h => by
      rw [List.filter_cons, if_pos (by simpa using h a (List.mem_cons_self ..)),
        filter_lt_eq_self t (fun b hb => h b (List.mem_cons_of_mem a hb))]

@[simp] theorem qTrunc_zero : ∀ (Q : List (List ℕ)), qTrunc Q 0 = []
  | [] => rfl
  | row :: rest => by
      rw [qTrunc_cons, if_pos (filter_lt_eq_nil row (fun a _ => Nat.zero_le a))]

/-- Past every timestamp the truncation is the tableau. -/
theorem qTrunc_of_all_lt : ∀ (Q : List (List ℕ)) {n : ℕ}, NoEmptyRows Q →
    (∀ a ∈ Q.flatten, a < n) → qTrunc Q n = Q
  | [], _, _, _ => rfl
  | row :: rest, n, hne, h => by
      have hrow : row.filter (· < n) = row :=
        filter_lt_eq_self row (fun a ha => h a (by
          rw [List.flatten_cons]; exact List.mem_append_left _ ha))
      have hrne : row ≠ [] := hne row (List.mem_cons_self ..)
      rw [qTrunc_cons, hrow, if_neg hrne,
        qTrunc_of_all_lt rest (fun r hr => hne r (List.mem_cons_of_mem row hr))
          (fun a ha => h a (by rw [List.flatten_cons]; exact List.mem_append_right _ ha))]

/-- Raising the horizon past a timestamp the row does not hold changes nothing. -/
theorem filter_lt_succ_not_mem : ∀ (row : List ℕ) {t : ℕ}, t ∉ row →
    row.filter (· < t + 1) = row.filter (· < t)
  | [], _, _ => rfl
  | a :: rest, t, h => by
      have hane : a ≠ t := fun hc => h (hc ▸ List.mem_cons_self ..)
      have hrest : t ∉ rest := fun hc => h (List.mem_cons_of_mem a hc)
      rw [List.filter_cons, List.filter_cons, filter_lt_succ_not_mem rest hrest]
      by_cases hlt : a < t
      · rw [if_pos (by simp only [decide_eq_true_eq]; omega),
          if_pos (by simp only [decide_eq_true_eq]; omega)]
      · rw [if_neg (by simp only [decide_eq_true_eq]; omega),
          if_neg (by simp only [decide_eq_true_eq]; omega)]

/-- **A timestamp joins its row at the end.** In a strictly increasing row every entry below `t`
precedes `t`, so raising the horizon past `t` appends it. This is why the replay can use `qAppend`,
which only ever writes at the end of a row. -/
theorem filter_lt_succ_mem : ∀ (row : List ℕ), row.Sorted (· < ·) → ∀ {t : ℕ}, t ∈ row →
    row.filter (· < t + 1) = row.filter (· < t) ++ [t]
  | [], _, t, h => by simp at h
  | a :: rest, hs, t, h => by
      rw [List.sorted_cons] at hs
      rw [List.mem_cons] at h
      rcases h with rfl | h
      · have h1 : rest.filter (· < t + 1) = [] :=
          filter_lt_eq_nil rest (fun b hb => by have := hs.1 b hb; omega)
        have h2 : rest.filter (· < t) = [] :=
          filter_lt_eq_nil rest (fun b hb => by have := hs.1 b hb; omega)
        rw [List.filter_cons, List.filter_cons, h1, h2,
          if_pos (by simp only [decide_eq_true_eq]; omega),
          if_neg (by simp only [decide_eq_true_eq]; omega)]
        rfl
      · have hlt : a < t := hs.1 t h
        rw [List.filter_cons, List.filter_cons,
          if_pos (by simp only [decide_eq_true_eq]; omega),
          if_pos (by simp only [decide_eq_true_eq]; omega),
          filter_lt_succ_mem rest hs.2 h, List.cons_append]

/-- Raising the horizon past a timestamp no row holds changes nothing. -/
theorem qTrunc_succ_of_not_mem : ∀ (Q : List (List ℕ)) {t : ℕ}, (∀ row ∈ Q, t ∉ row) →
    qTrunc Q (t + 1) = qTrunc Q t
  | [], _, _ => rfl
  | row :: rest, t, h => by
      rw [qTrunc_cons, qTrunc_cons, filter_lt_succ_not_mem row (h row (List.mem_cons_self ..)),
        qTrunc_succ_of_not_mem rest (fun r hr => h r (List.mem_cons_of_mem row hr))]

/-- A row entry witnesses a strictly smaller entry in the row above. -/
theorem exists_lt_of_strictBelow {u l : List ℕ} (h : StrictBelow u l) {a : ℕ} (ha : a ∈ l) :
    ∃ b ∈ u, b < a := by
  obtain ⟨hlen, hlt⟩ := h
  obtain ⟨j, hj, hja⟩ := List.mem_iff_getElem.mp ha
  refine ⟨u.getD j 0, getD_mem (by omega), ?_⟩
  have := hlt j hj
  rwa [getD_eq_getElem_mem hj, hja] at this

/-- Any row entry lies at or above an entry of the **top** row. Chaining the previous lemma down the
column-strict tower, this is what makes a truncation's non-empty rows an initial segment. -/
theorem exists_le_head : ∀ (r : ℕ) (Q : List (List ℕ)) (a : ℕ), ColStrict Q → a ∈ Q.getD r [] →
    ∃ b ∈ Q.getD 0 [], b ≤ a
  | 0, _, a, _, ha => ⟨a, ha, le_refl a⟩
  | _ + 1, [], _, _, ha => by simp at ha
  | r + 1, row :: rest, a, hc, ha => by
      simp only [List.getD_cons_succ] at ha
      obtain ⟨b, hb, hba⟩ := exists_le_head r rest a (colStrict_tail hc) ha
      have hrne : rest ≠ [] := by
        intro hnil; rw [hnil] at hb; simp at hb
      have hb' : b ∈ rest.headD [] := by
        cases rest with
        | nil => exact absurd rfl hrne
        | cons r0 rs => simpa using hb
      obtain ⟨c, hcmem, hcb⟩ := exists_lt_of_strictBelow (strictBelow_head hc hrne) hb'
      exact ⟨c, by simpa using hcmem, by omega⟩

/-- Row membership gives membership in the flattening. -/
theorem getD_mem_flatten {Q : List (List ℕ)} {r a : ℕ} (h : a ∈ Q.getD r []) : a ∈ Q.flatten := by
  by_cases hr : r < Q.length
  · exact List.mem_flatten.mpr ⟨Q.getD r [], by rw [getD_row_eq hr]; exact List.getElem_mem _, h⟩
  · rw [getD_row_past (Nat.not_lt.mp hr)] at h; simp at h

/-- **One step of the replay.** Writing timestamp `t` at the end of its row in `qTrunc Q t` produces
`qTrunc Q (t + 1)`.

The two cases at the top row are the whole content. When the top row holds nothing below `t` the
truncation is empty and `t` starts the tableau — and then no row below can hold anything below
`t + 1` either, because column strictness would put a smaller entry in the top row. Otherwise the
top row survives and `t` is appended to it, the rows below being untouched because `t` occurs once.
Below the top row the argument recurses, with `exists_le_head` supplying the fact that the top row
is still non-empty so the index has not shifted. -/
theorem qAppend_qTrunc : ∀ (Q : List (List ℕ)) (r t : ℕ), ColStrict Q →
    (∀ row ∈ Q, row.Sorted (· < ·)) → Q.flatten.Nodup → t ∈ Q.getD r [] →
    qAppend (qTrunc Q t) r t = qTrunc Q (t + 1)
  | [], r, t, _, _, _, ht => by rw [List.getD_nil] at ht; simp at ht
  | row :: rest, 0, t, hc, hst, hnd, ht => by
      simp only [List.getD_cons_zero] at ht
      rw [List.flatten_cons, List.nodup_append] at hnd
      have hnotrest : ∀ r' ∈ rest, t ∉ r' := fun r' hr' hmem =>
        hnd.2.2 t ht t (List.mem_flatten.mpr ⟨r', hr', hmem⟩) rfl
      have hfs : row.filter (· < t + 1) = row.filter (· < t) ++ [t] :=
        filter_lt_succ_mem row (hst row (List.mem_cons_self ..)) ht
      by_cases hempty : row.filter (· < t) = []
      · have hrestnil : qTrunc rest (t + 1) = [] := by
          cases rest with
          | nil => rfl
          | cons r0 rs =>
              refine (qTrunc_cons r0 rs (t + 1)).trans (if_pos (filter_lt_eq_nil r0 ?_))
              intro a ha
              obtain ⟨b, hb, hba⟩ :=
                exists_lt_of_strictBelow
                  (by simpa using strictBelow_head hc (by simp)) ha
              have hne : a ≠ t := fun hcon => hnotrest r0 (by simp) (hcon ▸ ha)
              by_contra hcon
              have hmem : b ∈ row.filter (· < t) := by
                rw [List.mem_filter]
                exact ⟨hb, by simp only [decide_eq_true_eq]; omega⟩
              rw [hempty] at hmem; simp at hmem
        rw [qTrunc_cons, if_pos hempty, qTrunc_cons, hfs, hempty,
          if_neg (by simp), hrestnil, qAppend_zero]
        simp
      · rw [qTrunc_cons, if_neg hempty, qTrunc_cons, hfs, if_neg (by simp), qAppend_zero,
          List.headD_cons, List.tail_cons, qTrunc_succ_of_not_mem rest hnotrest]
  | row :: rest, r + 1, t, hc, hst, hnd, ht => by
      simp only [List.getD_cons_succ] at ht
      rw [List.flatten_cons, List.nodup_append] at hnd
      have hnotrow : t ∉ row := fun hmem => hnd.2.2 t hmem t (getD_mem_flatten ht) rfl
      have hnonempty : row.filter (· < t) ≠ [] := by
        obtain ⟨b, hb, hbt⟩ := exists_le_head (r + 1) (row :: rest) t hc (by simpa using ht)
        simp only [List.getD_cons_zero] at hb
        have hblt : b < t := lt_of_le_of_ne hbt (fun hcon => hnotrow (hcon ▸ hb))
        intro hnil
        have hmem : b ∈ row.filter (· < t) := by
          rw [List.mem_filter]
          exact ⟨hb, by simp only [decide_eq_true_eq]; omega⟩
        rw [hnil] at hmem; simp at hmem
      rw [qTrunc_cons, if_neg hnonempty, qTrunc_cons, filter_lt_succ_not_mem row hnotrow,
        if_neg hnonempty, qAppend_succ, List.headD_cons, List.tail_cons,
        qAppend_qTrunc rest r t (colStrict_tail hc)
          (fun r' hr' => hst r' (List.mem_cons_of_mem row hr')) hnd.2.1 ht]

/-- A run of appends, one step peeled off the end. -/
theorem qAppendSteps_append : ∀ (is : List ℕ) (Q : List (List ℕ)) (j s : ℕ),
    qAppendSteps Q (is ++ [j]) s = qAppend (qAppendSteps Q is s) j (s + is.length)
  | [], Q, j, s => by simp [qAppendSteps]
  | i :: rest, Q, j, s => by
      have hs : s + 1 + rest.length = s + (i :: rest).length := by
        simp only [List.length_cons]; omega
      rw [List.cons_append, qAppendSteps_cons, qAppendSteps_cons,
        qAppendSteps_append rest (qAppend Q i s) j (s + 1), hs]

/-- **The replay is exact.** Appending the timestamps below `n` at the positions read off `Q`
rebuilds `Q`'s truncation at `n`. -/
theorem qAppendSteps_qPositions {Q : List (List ℕ)} (hc : ColStrict Q)
    (hst : ∀ row ∈ Q, row.Sorted (· < ·)) (hnd : Q.flatten.Nodup) :
    ∀ (n : ℕ), (∀ t, t < n → t ∈ Q.flatten) → qAppendSteps [] (qPositions Q n) 0 = qTrunc Q n
  | 0, _ => by simp [qPositions]
  | n + 1, hrange => by
      have hn : qAppendSteps [] (qPositions Q n) 0 = qTrunc Q n :=
        qAppendSteps_qPositions hc hst hnd n (fun t ht => hrange t (by omega))
      have hlen : (qPositions Q n).length = n := by simp [qPositions]
      obtain ⟨r, hr⟩ := qRowOf_isSome_of_mem_flatten Q n (hrange n (by omega))
      rw [qPositions_succ, qAppendSteps_append, hn, hlen, hr, Option.getD_some, Nat.zero_add]
      exact qAppend_qTrunc Q r n hc hst hnd (mem_of_qRowOf Q n r hr)

/-- **The recording tableau is determined by its positions.** Once the horizon clears every entry,
the replay is `Q` on the nose — the form the RSK inverse consumes. -/
theorem qAppendSteps_qPositions_self {Q : List (List ℕ)} (hc : ColStrict Q)
    (hst : ∀ row ∈ Q, row.Sorted (· < ·)) (hnd : Q.flatten.Nodup) (hne : NoEmptyRows Q) {n : ℕ}
    (hrange : ∀ t, t < n → t ∈ Q.flatten) (hlt : ∀ a ∈ Q.flatten, a < n) :
    qAppendSteps [] (qPositions Q n) 0 = Q :=
  (qAppendSteps_qPositions hc hst hnd n hrange).trans (qTrunc_of_all_lt Q hne hlt)

end QOU.Mathlib.Schensted
