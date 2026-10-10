import QOU.Mathlib.SchenstedReadback

/-!
# QOU.Mathlib.SchenstedReadbackFold — the whole index list, read back off `Q` (RSK inverse, brick 6)

Brick 5 read one append back. This file threads it along the fold, under the invariant that makes
the read-back well defined: **every timestamp already in `Q` is below the next one to be written**.
Timestamps count up, so the invariant is self-propagating, and each append is fresh for everything
before it.

* `AllLt Q s` — every entry of `Q` is `< s`.
* `mem_qAppend` / `allLt_qAppend` — an append adds only `s`, so the invariant survives with `s+1`.
* `qRowOf_qAppendSteps_of_lt` — later appends never move an earlier timestamp.
* **`qRowOf_qAppendSteps`** — `qRowOf (qAppendSteps Q is s) (s + k) = some (is.getD k 0)`:
  timestamp `s+k` sits in the row the `k`-th step wrote to.

Combined with brick 4 (`Q(w)` *is* `qAppendSteps [] (rowIndices [] w) 0`), the index list is a
function of `Q(w)` — which is what brick 3's `word_eq_of_insertWord_eq` needs to become injectivity
of the RSK map.

## Scope

The read-back. Assembling it into `rskPair` injectivity, then surjectivity, then
`RSKBurnsideHolds`, is the remainder of epic `qou-nrex`. Nothing here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- Every entry of `Q` is strictly below `s` — the freshness invariant, in the form that
propagates. -/
def AllLt (Q : List (List ℕ)) (s : ℕ) : Prop := ∀ r ∈ Q, ∀ t ∈ r, t < s

theorem allLt_nil (s : ℕ) : AllLt [] s := by intro _ h; simp at h

/-- `AllLt Q s` says in particular that `s` itself is absent — the freshness `qRowOf_qAppend_self`
wants. -/
theorem not_mem_of_allLt {Q : List (List ℕ)} {s : ℕ} (h : AllLt Q s) : ∀ r ∈ Q, s ∉ r :=
  fun r hr hs => absurd (h r hr s hs) (lt_irrefl s)

/-- **An append adds only its own timestamp.** -/
theorem mem_qAppend : ∀ (Q : List (List ℕ)) (i s : ℕ) (r' : List ℕ), r' ∈ qAppend Q i s →
    ∀ t ∈ r', (∃ r ∈ Q, t ∈ r) ∨ t = s
  | Q, 0, s, r', hr', t, ht => by
      rw [qAppend_zero, List.mem_cons] at hr'
      rcases hr' with rfl | hr'
      · rcases List.mem_append.mp ht with h | h
        · cases Q with
          | nil => simp at h
          | cons a T => exact Or.inl ⟨a, List.mem_cons_self .., h⟩
        · exact Or.inr (List.mem_singleton.mp h)
      · cases Q with
        | nil => simp at hr'
        | cons a T => exact Or.inl ⟨r', List.mem_cons_of_mem a hr', ht⟩
  | Q, i + 1, s, r', hr', t, ht => by
      rw [qAppend_succ, List.mem_cons] at hr'
      rcases hr' with rfl | hr'
      · cases Q with
        | nil => simp at ht
        | cons a T => exact Or.inl ⟨a, List.mem_cons_self .., ht⟩
      · rcases mem_qAppend Q.tail i s r' hr' t ht with ⟨r, hr, htr⟩ | h
        · cases Q with
          | nil => simp at hr
          | cons a T => exact Or.inl ⟨r, List.mem_cons_of_mem a hr, htr⟩
        · exact Or.inr h

/-- The invariant survives an append, with the counter bumped. -/
theorem allLt_qAppend {Q : List (List ℕ)} {s : ℕ} (h : AllLt Q s) (i : ℕ) :
    AllLt (qAppend Q i s) (s + 1) := by
  intro r' hr' t ht
  rcases mem_qAppend Q i s r' hr' t ht with ⟨r, hr, htr⟩ | rfl
  · exact Nat.lt_succ_of_lt (h r hr t htr)
  · exact Nat.lt_succ_self t

/-- **Later appends never move an earlier timestamp.** -/
theorem qRowOf_qAppendSteps_of_lt : ∀ (Q : List (List ℕ)) (is : List ℕ) (s t : ℕ), t < s →
    qRowOf (qAppendSteps Q is s) t = qRowOf Q t
  | _, [], _, _, _ => rfl
  | Q, i :: rest, s, t, hts => by
      rw [qAppendSteps_cons,
        qRowOf_qAppendSteps_of_lt (qAppend Q i s) rest (s + 1) t (Nat.lt_succ_of_lt hts),
        qRowOf_qAppend_of_ne Q i s t (Nat.ne_of_lt hts)]

/-- **The read-back.** Under the freshness invariant, timestamp `s + k` sits in the row that the
`k`-th step wrote to — so the index list is recoverable from the recording tableau. -/
theorem qRowOf_qAppendSteps : ∀ (Q : List (List ℕ)) (is : List ℕ) (s : ℕ), AllLt Q s →
    ∀ (k : ℕ), k < is.length → qRowOf (qAppendSteps Q is s) (s + k) = some (is.getD k 0)
  | _, [], _, _, k, hk => by simp at hk
  | Q, i :: rest, s, h, 0, _ => by
      rw [qAppendSteps_cons]
      simp only [Nat.add_zero, List.getD_cons_zero]
      rw [qRowOf_qAppendSteps_of_lt (qAppend Q i s) rest (s + 1) s (Nat.lt_succ_self s),
        qRowOf_qAppend_self Q i s (not_mem_of_allLt h)]
  | Q, i :: rest, s, h, k + 1, hk => by
      rw [qAppendSteps_cons, show s + (k + 1) = (s + 1) + k by omega,
        qRowOf_qAppendSteps (qAppend Q i s) rest (s + 1) (allLt_qAppend h i) k
          (by simpa using Nat.lt_of_succ_lt_succ hk)]
      rfl

/-- **At the empty tableau**, the form the RSK inverse consumes: reading timestamp `k` off `Q`
returns the row the `k`-th letter's insertion appended to. -/
theorem qRowOf_qAppendSteps_zero (is : List ℕ) (k : ℕ) (hk : k < is.length) :
    qRowOf (qAppendSteps [] is 0) k = some (is.getD k 0) := by
  have := qRowOf_qAppendSteps [] is 0 (allLt_nil 0) k hk
  simpa using this

end QOU.Mathlib.Schensted
