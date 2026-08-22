import QOU.Mathlib.SchenstedAddable
import QOU.Mathlib.SchenstedReadback

/-!
# QOU.Mathlib.SchenstedStandardCount — the counting bridge from column-strictness (brick 23)

Brick 22 showed the shape an addable sequence builds is the **count shape**: row `i` holds exactly
the steps that landed in row `i`. So `IsAddable` at a step reduces to a comparison of counts, and
what the recording tableau has to supply is exactly that comparison.

This file proves it, from column-strictness alone:

> **`countLt_above`** — if an entry `k` sits at column `c` of row `r + 1`, then row `r` holds
> **strictly more** entries below `k`.

Read through brick 22, that inequality *is* the addability condition: the row above has more cells
placed before time `k` than the row the new cell goes into, which is what makes the new cell
addable.

## What it does not need

No truncation of the tableau. An earlier plan restricted `Q` to its entries below `s`, proved
`ColStrict` survived the filter and that the emptied rows formed a suffix — several hundred lines.
Counting per row replaces all of it, because brick 22 already phrased the shape as a count.

It also needs no notion of "standard" beyond what is written in the hypotheses: rows strictly
increasing and columns strictly increasing. There is no standardness predicate here, and none is
introduced — the third time on this arc that checking what the argument consumes turned out to
shrink the machinery.

## Scope

The counting fact. Producing the position sequence from a recording tableau — reading rows off `Q`
in timestamp order and assembling `AddableAlong` — is the next brick of epic `qou-nrex`. Nothing
here claims it, nothing here claims `rskPair` is bijective, and `RSKBurnsideHolds` for general `n`
stays open (proved for `n ≤ 12` by an unrelated route, `PartitionsOfBridge.rskBurnsideHolds_le12`,
with no RSK correspondence in it).

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- How many entries of a row lie strictly below `k`. -/
def countLt (row : List ℕ) (k : ℕ) : ℕ := (row.filter (· < k)).length

@[simp] theorem countLt_nil (k : ℕ) : countLt [] k = 0 := rfl

theorem countLt_cons (a : ℕ) (t : List ℕ) (k : ℕ) :
    countLt (a :: t) k = countLt t k + (if a < k then 1 else 0) := by
  rw [countLt, countLt, List.filter_cons]
  by_cases h : a < k <;> simp [h]

/-- **In a strictly increasing row, the entries below `row[c]` are exactly the first `c`.** -/
theorem countLt_getD : ∀ (row : List ℕ), row.Sorted (· < ·) → ∀ (c : ℕ), c < row.length →
    countLt row (row.getD c 0) = c
  | [], _, c, hc => by simp at hc
  | a :: t, hs, 0, _ => by
      rw [List.sorted_cons] at hs
      simp only [List.getD_cons_zero]
      rw [countLt_cons, if_neg (lt_irrefl a)]
      simp only [Nat.add_zero, countLt]
      -- every later entry is strictly greater, so nothing survives the filter
      rw [List.filter_eq_nil_iff.mpr]
      · rfl
      · intro b hb
        simp only [decide_eq_true_eq, Nat.not_lt]
        exact le_of_lt (hs.1 b hb)
  | a :: t, hs, c + 1, hc => by
      rw [List.sorted_cons] at hs
      simp only [List.getD_cons_succ]
      have hct : c < t.length := by simpa using hc
      have hmem : t.getD c 0 ∈ t := getD_mem hct
      rw [countLt_cons, if_pos (hs.1 _ hmem), countLt_getD t hs.2 c hct]

/-- An entry strictly below `k` at index `c` forces more than `c` entries below `k`. -/
theorem lt_countLt_of_getD_lt : ∀ (row : List ℕ), row.Sorted (· < ·) → ∀ (c k : ℕ),
    c < row.length → row.getD c 0 < k → c < countLt row k
  | [], _, c, _, hc, _ => by simp at hc
  | a :: t, hs, 0, k, _, hlt => by
      rw [List.sorted_cons] at hs
      simp only [List.getD_cons_zero] at hlt
      rw [countLt_cons, if_pos hlt]
      omega
  | a :: t, hs, c + 1, k, hc, hlt => by
      rw [List.sorted_cons] at hs
      simp only [List.getD_cons_succ] at hlt
      have hct : c < t.length := by simpa using hc
      have hmem : t.getD c 0 ∈ t := getD_mem hct
      have hak : a < k := lt_trans (hs.1 _ hmem) hlt
      have hih := lt_countLt_of_getD_lt t hs.2 c k hct hlt
      rw [countLt_cons, if_pos hak]
      omega

/-- **The bridge fact.** If an entry sits at column `c` of row `r + 1`, then row `r` holds strictly
more entries below it.

Column-strictness supplies both halves: the entry directly above is smaller, and — via the length
half of `StrictBelow` — that cell exists at all. Row `r` therefore has its first `c + 1` entries
below the threshold, against exactly `c` in row `r + 1`. -/
theorem countLt_above {Q : List (List ℕ)} (hcs : ColStrict Q)
    (hstrict : ∀ row ∈ Q, row.Sorted (· < ·)) {r c : ℕ}
    (hr : r + 1 < Q.length) (hcc : c < (Q.getD (r + 1) []).length) :
    countLt (Q.getD (r + 1) []) ((Q.getD (r + 1) []).getD c 0)
      < countLt (Q.getD r []) ((Q.getD (r + 1) []).getD c 0) := by
  obtain ⟨hlen, hlt⟩ := colStrict_adjacent hcs hr
  have hrowUp : Q.getD r [] ∈ Q := by
    rw [getD_row_eq (by omega)]; exact List.getElem_mem _
  have hrowDn : Q.getD (r + 1) [] ∈ Q := by
    rw [getD_row_eq hr]; exact List.getElem_mem _
  -- the row below contributes exactly `c`
  rw [countLt_getD _ (hstrict _ hrowDn) c hcc]
  -- the row above has a smaller entry at the same column, and is long enough to have it
  refine lt_countLt_of_getD_lt _ (hstrict _ hrowUp) c _ (lt_of_lt_of_le hcc hlen) ?_
  exact hlt c hcc

/-! ### The membership form

`countLt_above` is indexed by the column, but `qRowOf` — the corpus's timestamp locator — returns
only the **row**. Nothing in bricks 4-6 records the column, so the assembly cannot supply one.

It does not have to: in a strictly increasing row the column of an entry *is* its `countLt`, so the
column is recoverable rather than needing to be carried. `getD_countLt` below is that recovery, and
`countLt_above_mem` is `countLt_above` restated to take membership instead of a column index — the
form the assembly can actually reach. -/

/-- Nothing below the threshold means a count of zero. -/
theorem countLt_eq_zero {row : List ℕ} {k : ℕ} (h : ∀ b ∈ row, k ≤ b) : countLt row k = 0 := by
  rw [countLt, List.filter_eq_nil_iff.mpr]
  · rfl
  · intro b hb
    simp only [decide_eq_true_eq, Nat.not_lt]
    exact h b hb

/-- **The column of an entry is its `countLt`.** Both halves at once, since the induction is shared:
the count is a valid index, and reading there returns the entry. -/
theorem countLt_lt_length_and_getD : ∀ (row : List ℕ), row.Sorted (· < ·) → ∀ (k : ℕ), k ∈ row →
    countLt row k < row.length ∧ row.getD (countLt row k) 0 = k
  | [], _, k, hk => by simp at hk
  | a :: t, hs, k, hk => by
      rw [List.sorted_cons] at hs
      rcases List.mem_cons.mp hk with rfl | hkt
      · have h0 : countLt (k :: t) k = 0 := by
          rw [countLt_cons, if_neg (lt_irrefl k),
            countLt_eq_zero (fun b hb => le_of_lt (hs.1 b hb))]
        rw [h0]
        exact ⟨by simp, by simp⟩
      · have hak : a < k := hs.1 k hkt
        obtain ⟨hlen, hget⟩ := countLt_lt_length_and_getD t hs.2 k hkt
        rw [countLt_cons, if_pos hak]
        exact ⟨by simpa using hlen, by simpa using hget⟩

theorem countLt_lt_length {row : List ℕ} (hs : row.Sorted (· < ·)) {k : ℕ} (hk : k ∈ row) :
    countLt row k < row.length := (countLt_lt_length_and_getD row hs k hk).1

theorem getD_countLt {row : List ℕ} (hs : row.Sorted (· < ·)) {k : ℕ} (hk : k ∈ row) :
    row.getD (countLt row k) 0 = k := (countLt_lt_length_and_getD row hs k hk).2

/-- **The bridge fact, keyed on membership.** If `k` occurs in row `r + 1`, row `r` holds strictly
more entries below it. This is the form the assembly reaches: it needs only the row `qRowOf`
returns, never a column. -/
theorem countLt_above_mem {Q : List (List ℕ)} (hcs : ColStrict Q)
    (hstrict : ∀ row ∈ Q, row.Sorted (· < ·)) {r k : ℕ}
    (hr : r + 1 < Q.length) (hk : k ∈ Q.getD (r + 1) []) :
    countLt (Q.getD (r + 1) []) k < countLt (Q.getD r []) k := by
  have hrowDn : Q.getD (r + 1) [] ∈ Q := by
    rw [getD_row_eq hr]; exact List.getElem_mem _
  have hsd := hstrict _ hrowDn
  have hres := countLt_above hcs hstrict hr (countLt_lt_length hsd hk)
  rwa [getD_countLt hsd hk] at hres

/-! ### `qRowOf` correctness

The assembly reads a timestamp's row off `Q` with `qRowOf` (brick 5) and then feeds that row to
`countLt_above_mem`, which needs the timestamp to actually be **in** that row.

Nothing in bricks 4-6 says so. Every existing `qRowOf` lemma is about how `qAppend` and
`qAppendSteps` move things around — `qRowOf_qAppend_self`, `qRowOf_qAppend_of_ne`,
`qRowOf_qAppendSteps` — and none of them states that the located row is correct on its own terms.
For a `Q` that is simply given, rather than built by appending, there was nothing to appeal to.

Both facts below are short inductions on `qRowOf`'s own recursion. -/

/-- **The located row contains the timestamp.** -/
theorem mem_of_qRowOf : ∀ (Q : List (List ℕ)) (t r : ℕ), qRowOf Q t = some r → t ∈ Q.getD r []
  | [], t, r, h => by simp at h
  | row :: T, t, r, h => by
      rw [qRowOf_cons] at h
      by_cases hmem : t ∈ row
      · rw [if_pos hmem] at h
        have hr : r = 0 := (Option.some.inj h).symm
        subst hr
        simpa using hmem
      · rw [if_neg hmem] at h
        obtain ⟨r', hr', hEq⟩ := Option.map_eq_some_iff.mp h
        subst hEq
        simpa using mem_of_qRowOf T t r' hr'

/-- **The located row is a row.** -/
theorem qRowOf_lt_length : ∀ (Q : List (List ℕ)) (t r : ℕ), qRowOf Q t = some r → r < Q.length
  | [], t, r, h => by simp at h
  | row :: T, t, r, h => by
      rw [qRowOf_cons] at h
      by_cases hmem : t ∈ row
      · rw [if_pos hmem] at h
        have hr : r = 0 := (Option.some.inj h).symm
        subst hr
        simp
      · rw [if_neg hmem] at h
        obtain ⟨r', hr', hEq⟩ := Option.map_eq_some_iff.mp h
        subst hEq
        have := qRowOf_lt_length T t r' hr'
        simpa using this

/-- **The bridge fact, reached through `qRowOf`.** If `qRowOf` places `k` in row `r + 1`, then row
`r` holds strictly more entries below `k` — which, read through brick 22's count shape, is exactly
the addability of the cell `k` occupies. -/
theorem countLt_above_qRowOf {Q : List (List ℕ)} (hcs : ColStrict Q)
    (hstrict : ∀ row ∈ Q, row.Sorted (· < ·)) {r k : ℕ} (h : qRowOf Q k = some (r + 1)) :
    countLt (Q.getD (r + 1) []) k < countLt (Q.getD r []) k :=
  countLt_above_mem hcs hstrict (qRowOf_lt_length Q k (r + 1) h) (mem_of_qRowOf Q k (r + 1) h)

/-! ### `qRowOf` is total and exact, given distinct entries

Brick 24 gave one direction: the located row contains the timestamp. The counting step needs the
converse — if `t` sits in row `i`, `qRowOf` must *return* `i` — and that is where entries being
distinct across rows finally matters. `qRowOf` returns the **first** row containing `t`, so without
distinctness a repeated entry would be located in the wrong row.

Totality is separate and needs no distinctness. It matters because `qRowOf` returns an `Option`: a
counting argument that reads it with `.getD 0` would silently score every absent timestamp as row
`0`. -/

/-- **Totality.** A timestamp occurring anywhere in `Q` is located. -/
theorem qRowOf_isSome_of_mem_flatten : ∀ (Q : List (List ℕ)) (t : ℕ), t ∈ Q.flatten →
    ∃ r, qRowOf Q t = some r
  | [], t, h => by simp at h
  | row :: T, t, h => by
      by_cases hmem : t ∈ row
      · exact ⟨0, by rw [qRowOf_cons, if_pos hmem]⟩
      · rw [List.flatten_cons, List.mem_append] at h
        rcases h with hrow | htail
        · exact absurd hrow hmem
        · obtain ⟨r', hr'⟩ := qRowOf_isSome_of_mem_flatten T t htail
          exact ⟨r' + 1, by rw [qRowOf_cons, if_neg hmem, hr']; rfl⟩

/-- **Exactness.** With entries distinct across rows, membership in row `i` forces `qRowOf` to
return `i`. -/
theorem qRowOf_eq_some_of_mem : ∀ (Q : List (List ℕ)), Q.flatten.Nodup → ∀ (t i : ℕ),
    i < Q.length → t ∈ Q.getD i [] → qRowOf Q t = some i
  | [], _, t, i, hi, _ => by simp at hi
  | row :: T, hnd, t, i, hi, hmem => by
      rw [List.flatten_cons, List.nodup_append] at hnd
      cases i with
      | zero =>
          simp only [List.getD_cons_zero] at hmem
          rw [qRowOf_cons, if_pos hmem]
      | succ i' =>
          simp only [List.getD_cons_succ] at hmem
          have hiT : i' < T.length := by simpa using hi
          have htf : t ∈ T.flatten :=
            List.mem_flatten.mpr ⟨T.getD i' [], by rw [getD_row_eq hiT]; exact List.getElem_mem _,
              hmem⟩
          have hnot : t ∉ row := fun hc => (hnd.2.2 t hc t htf) rfl
          rw [qRowOf_cons, if_neg hnot, qRowOf_eq_some_of_mem T hnd.2.1 t i' hiT hmem]
          rfl

/-- **`qRowOf` locates exactly.** -/
theorem qRowOf_eq_some_iff_mem {Q : List (List ℕ)} (hnd : Q.flatten.Nodup) {t i : ℕ}
    (hi : i < Q.length) : qRowOf Q t = some i ↔ t ∈ Q.getD i [] :=
  ⟨mem_of_qRowOf Q t i, qRowOf_eq_some_of_mem Q hnd t i hi⟩

/-! ### The count equality

The step the whole Q-side reduces to. Brick 22 phrased the shape an addable sequence builds as a
count over the **position list**; `countLt` counts over the **rows of `Q`**. These are the same
number, and this is where that is proved.

The two sides genuinely count different things — timestamps on the left, entries on the right — so
the argument is a bijection, not a rewrite. Both filtered lists are duplicate-free and have the same
members, which is enough. -/

/-- A row of a tableau with distinct entries is itself duplicate-free. -/
theorem nodup_of_mem_of_flatten_nodup : ∀ (Q : List (List ℕ)), Q.flatten.Nodup →
    ∀ (row : List ℕ), row ∈ Q → row.Nodup
  | [], _, row, hr => by simp at hr
  | r :: T, hnd, row, hr => by
      rw [List.flatten_cons, List.nodup_append] at hnd
      rcases List.mem_cons.mp hr with rfl | hr'
      · exact hnd.1
      · exact nodup_of_mem_of_flatten_nodup T hnd.2.1 row hr'

/-- **The position list** of the timestamps `0, …, n-1`: for each, the row of `Q` that holds it. -/
def qPositions (Q : List (List ℕ)) (n : ℕ) : List ℕ :=
  (List.range n).map (fun t => (qRowOf Q t).getD 0)

/-- Locating a timestamp below the horizon returns its row, as a plain `ℕ`.

The `.getD 0` in `qPositions` is why totality had to be proved: without `hrange`, an absent timestamp
would read as row `0` and be counted there. -/
theorem getD_qRowOf_eq_iff {Q : List (List ℕ)} (hnd : Q.flatten.Nodup) {t i : ℕ}
    (hi : i < Q.length) (ht : t ∈ Q.flatten) :
    (qRowOf Q t).getD 0 = i ↔ t ∈ Q.getD i [] := by
  obtain ⟨r, hr⟩ := qRowOf_isSome_of_mem_flatten Q t ht
  rw [hr, Option.getD_some]
  constructor
  · intro hri
    subst hri
    exact mem_of_qRowOf Q t r hr
  · intro hmem
    have := qRowOf_eq_some_of_mem Q hnd t i hi hmem
    rw [hr] at this
    exact Option.some.inj this

/-- **The count equality.** The number of steps landing in row `i` equals the number of entries of
row `i` below the horizon. -/
theorem count_qPositions {Q : List (List ℕ)} (hnd : Q.flatten.Nodup) {k i : ℕ}
    (hi : i < Q.length) (hrange : ∀ t, t < k → t ∈ Q.flatten) :
    (qPositions Q k).count i = countLt (Q.getD i []) k := by
  classical
  have hrow : Q.getD i [] ∈ Q := by rw [getD_row_eq hi]; exact List.getElem_mem _
  have hrowNodup : (Q.getD i []).Nodup := nodup_of_mem_of_flatten_nodup Q hnd _ hrow
  -- rewrite both sides as lengths of filters
  rw [qPositions, List.count_eq_countP, List.countP_map, List.countP_eq_length_filter, countLt]
  -- the two filters are duplicate-free with the same members
  set L := List.filter ((fun x => x == i) ∘ fun t => (qRowOf Q t).getD 0) (List.range k) with hLdef
  set R := List.filter (fun x => decide (x < k)) (Q.getD i []) with hRdef
  have hLnd : L.Nodup := List.Nodup.filter _ List.nodup_range
  have hRnd : R.Nodup := List.Nodup.filter _ hrowNodup
  have hset : L.toFinset = R.toFinset := by
    ext x
    simp only [hLdef, hRdef, List.mem_toFinset, List.mem_filter, List.mem_range,
      Function.comp_apply, beq_iff_eq, decide_eq_true_eq]
    constructor
    · rintro ⟨hxk, hxi⟩
      exact ⟨(getD_qRowOf_eq_iff hnd hi (hrange x hxk)).mp hxi, hxk⟩
    · rintro ⟨hxrow, hxk⟩
      exact ⟨hxk, (getD_qRowOf_eq_iff hnd hi (hrange x hxk)).mpr hxrow⟩
  calc L.length = L.toFinset.card := (List.toFinset_card_of_nodup hLnd).symm
    _ = R.toFinset.card := by rw [hset]
    _ = R.length := List.toFinset_card_of_nodup hRnd

end QOU.Mathlib.Schensted
