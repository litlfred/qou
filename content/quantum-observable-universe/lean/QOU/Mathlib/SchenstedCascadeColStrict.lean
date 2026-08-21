import QOU.Mathlib.SchenstedReverseRowIndex
import QOU.Mathlib.SchenstedReverseCascade
import QOU.Mathlib.SYTListCorner

/-!
# QOU.Mathlib.SchenstedCascadeColStrict — the reverse cascade keeps columns strict (brick 13)

Brick 11 proved that `RowsSorted` and `NoEmptyRows` survive the reverse cascade unconditionally,
and located the corner condition that `ColStrict` needs. Brick 12 built the index theory of
`rowUninsert`. This file finishes the job.

**It does not go through brick 12's `strictBelow_reverse_bump_step`, and that is worth saying
plainly** because brick 12 was written expecting it would. That lemma relates `upper` and `lower`
when *both* rows are `rowUninsert` images. In the cascade the row below the one being written is
not always such an image: at the target row it is a `dropLast`, or the row is deleted outright. So
the pair-of-rows step does not compose along the cascade, and the induction below does the four
column cases directly against the returned top row. What brick 12 actually supplies here is
`rowUninsert_spec`, `le_index_of_lt` and `reverse_bump_index_mono` — the index theory, not the
packaged step.

## The corner predicate

`IsCorner T i` says the row below row `i` is strictly shorter, so removing the last cell of row `i`
leaves a Young shape. Two conveniences fall out of reading out-of-range rows as `[]`:

* the **last** row of a tableau is automatically a corner (the row below reads `[]`, length `0`);
* an **out-of-range** index is automatically not one, so `IsCorner T i` already carries
  `i < T.length` and no separate range hypothesis is needed.

## Scope

The cascade-level `ColStrict` preservation. Word-level surjectivity and `RSKBurnsideHolds` for
general `n` are the remainder of epic `qou-nrex`. Nothing here claims them.

Pure combinatorics on `ℕ`; nothing archimedean.
-/

namespace QOU.Mathlib.Schensted

/-- **Row `i` is a corner**: the row below is strictly shorter. Out-of-range rows read as `[]`, so
the last row of a tableau is a corner and an out-of-range index is not. -/
def IsCorner (T : List (List ℕ)) (i : ℕ) : Prop :=
  (T.getD (i + 1) []).length < (T.getD i []).length

/-- Being a corner one row down is being a corner in the tail. -/
theorem isCorner_cons_succ (r : List ℕ) (T : List (List ℕ)) (i : ℕ) :
    IsCorner (r :: T) (i + 1) ↔ IsCorner T i := by
  simp [IsCorner]

/-- At the top row, the corner condition says the second row is strictly shorter. -/
theorem isCorner_cons_zero (r : List ℕ) (T : List (List ℕ)) :
    IsCorner (r :: T) 0 ↔ (T.headD []).length < r.length := by
  cases T <;> simp [IsCorner, List.headD]

/-- A corner index is in range. -/
theorem isCorner_lt_length {T : List (List ℕ)} {i : ℕ} (h : IsCorner T i) : i < T.length := by
  by_contra hcon
  rw [IsCorner, getD_row_past (Nat.not_lt.mp hcon)] at h
  simp at h

/-- `dropLast` agrees with the row on every index it keeps. -/
theorem getD_dropLast {r : List ℕ} {j : ℕ} (hj : j < r.dropLast.length) :
    r.dropLast.getD j 0 = r.getD j 0 := by
  rcases List.eq_nil_or_concat r with rfl | ⟨s, a, rfl⟩
  · simp at hj
  · rw [List.concat_eq_append, List.dropLast_concat] at hj ⊢
    exact (getD_append_lt hj).symm

/-- Consing onto a column-strict tableau, given the one new comparison. -/
theorem colStrict_cons {r : List ℕ} {T : List (List ℕ)} (hT : ColStrict T)
    (h : ∀ row ∈ T.head?, StrictBelow r row) : ColStrict (r :: T) := by
  cases T with
  | nil => exact colStrict_singleton r
  | cons row rest =>
      rw [ColStrict, List.isChain_cons_cons]
      exact ⟨h row (by simp), hT⟩

/-- An eligible entry forces reverse insertion to succeed — the contrapositive of
`forall_le_of_rowUninsert_none`. -/
theorem rowUninsert_isSome_of_lt {r : List ℕ} {y j : ℕ} (hj : j < r.length)
    (hjy : r.getD j 0 < y) : ∃ z, (rowUninsert r y).2 = some z := by
  cases hs : (rowUninsert r y).2 with
  | some z => exact ⟨z, rfl⟩
  | none =>
      exact absurd (forall_le_of_rowUninsert_none r y hs _ (getD_mem hj)) (by omega)

/-- The last entry of a row, read with `getD`. -/
theorem getD_length_sub_one {r : List ℕ} (h : r ≠ []) :
    r.getD (r.length - 1) 0 = r.getLast h := by
  have hlt : r.length - 1 < r.length := by
    have := List.length_pos_iff.mpr h
    omega
  rw [getD_eq_getElem_mem hlt, List.getLast_eq_getElem h]

/-- **What the reverse cascade guarantees about the tableau it returns**, relative to the one it
was handed. Three facts about the top row, each needed one level up:

* the ejected value `z` came from some index `k` of the *old* top row;
* the new top row is no longer, and none of its entries is smaller;
* `z` is strictly below every surviving entry from column `k` rightwards.

That last clause is what lets the row above write `z` into its own column without breaking the
comparison, and it is what unifies the cascade's three shapes at the target row — row deleted, row
shortened by `dropLast`, row written by `rowUninsert`. -/
def CascadeStep (T T' : List (List ℕ)) (z : ℕ) : Prop :=
  ∃ k, k < (T.headD []).length ∧ (T.headD []).getD k 0 = z ∧
    (T'.headD []).length ≤ (T.headD []).length ∧
    (∀ j, j < (T'.headD []).length → (T.headD []).getD j 0 ≤ (T'.headD []).getD j 0) ∧
    (∀ m, k ≤ m → m < (T'.headD []).length → z < (T'.headD []).getD m 0)

/-- The top-row comparison of a column-strict tableau, in `headD` form. -/
theorem strictBelow_head {r : List ℕ} {T : List (List ℕ)} (hc : ColStrict (r :: T))
    (hT : T ≠ []) : StrictBelow r (T.headD []) := by
  cases T with
  | nil => exact absurd rfl hT
  | cons row rest =>
      rw [ColStrict, List.isChain_cons_cons] at hc
      simpa using hc.1

/-- Membership in `head?` names the `headD`. -/
theorem eq_headD_of_mem_head? {T : List (List ℕ)} {row : List ℕ} (h : row ∈ T.head?) :
    row = T.headD [] := by
  cases T with
  | nil => simp at h
  | cons a rest =>
      simp only [List.head?_cons, Option.mem_def, Option.some.injEq] at h
      rw [← h]; simp

/-- **The reverse cascade keeps columns strict**, at a corner.

The statement carries `CascadeStep` alongside because the induction needs it: at row `i + 1` the
row above has to write the value that came up from below into its own column, and the only way to
know that write is safe is to know where the value came from and what became of the row it came
from. `CascadeStep` is exactly that bookkeeping.

Three shapes occur at the target row and the invariant absorbs all three:

* **row deleted** — and the corner condition forces this to be the *last* row, since a length-one
  row with anything below it is not a corner. So the tableau below is empty and every clause is
  vacuous. This is the one case that surprised me: `IsCorner` does not merely make the deletion
  safe, it makes it rare.
* **row shortened** by `dropLast` — the ejected cell sat at the far right, so its column index is
  at or past the end of the shortened row and the last clause is vacuous again.
* **row written** by `rowUninsert` — the substantive case, and the one brick 12 was built for. -/
theorem uninsert_colStrict_step : ∀ (T : List (List ℕ)) (i : ℕ),
    ColStrict T → NoEmptyRows T → IsCorner T i →
    ColStrict (uninsert T i).1 ∧
      ∃ z, (uninsert T i).2 = some z ∧ CascadeStep T (uninsert T i).1 z
  | [], i, _, _, hcorner => by rw [IsCorner] at hcorner; simp at hcorner
  | r :: T, 0, hc, hne, hcorner => by
      have hrne : r ≠ [] := hne r (List.mem_cons_self ..)
      have hrpos : 0 < r.length := List.length_pos_iff.mpr hrne
      rw [isCorner_cons_zero] at hcorner
      have hlast : r.getLast? = some (r.getLast hrne) := List.getLast?_eq_getLast hrne
      rw [uninsert_zero]
      simp only
      by_cases hshort : r.length ≤ 1
      · -- deleted: the corner condition forces `T = []`
        have hTnil : T = [] := by
          cases T with
          | nil => rfl
          | cons row rest =>
              exfalso
              have hrow : row ≠ [] := hne row (List.mem_cons_of_mem r (List.mem_cons_self ..))
              have := List.length_pos_iff.mpr hrow
              simp only [List.headD_cons] at hcorner
              omega
        subst hTnil
        rw [if_pos hshort, hlast]
        refine ⟨colStrict_nil, r.getLast hrne, rfl, 0, ?_, ?_, ?_, ?_, ?_⟩
        · show 0 < ((r :: []).headD []).length
          simp only [List.headD_cons]; omega
        · show ((r :: []).headD []).getD 0 0 = r.getLast hrne
          simp only [List.headD_cons]
          have hg := getD_length_sub_one hrne
          rwa [show r.length - 1 = 0 from by omega] at hg
        · simp
        · simp
        · simp
      · -- shortened: `dropLast` keeps every column it retains
        rw [if_neg hshort, hlast]
        have hdl : r.dropLast.length = r.length - 1 := List.length_dropLast
        have hcs : ColStrict (r.dropLast :: T) := by
          refine colStrict_cons (colStrict_tail hc) ?_
          intro row hrow
          have hTne : T ≠ [] := by intro h; rw [h] at hrow; simp at hrow
          rw [eq_headD_of_mem_head? hrow]
          obtain ⟨hl, hlt⟩ := strictBelow_head hc hTne
          refine ⟨by omega, fun jj hj => ?_⟩
          rw [getD_dropLast (by omega)]
          exact hlt jj hj
        refine ⟨hcs, r.getLast hrne, rfl, r.length - 1, ?_, ?_, ?_, ?_, ?_⟩
        · show r.length - 1 < ((r :: T).headD []).length
          simp only [List.headD_cons]; omega
        · show ((r :: T).headD []).getD (r.length - 1) 0 = r.getLast hrne
          simp only [List.headD_cons]
          exact getD_length_sub_one hrne
        · show ((r.dropLast :: T).headD []).length ≤ ((r :: T).headD []).length
          simp only [List.headD_cons]; omega
        · show ∀ jj, jj < ((r.dropLast :: T).headD []).length →
            ((r :: T).headD []).getD jj 0 ≤ ((r.dropLast :: T).headD []).getD jj 0
          intro jj hj
          simp only [List.headD_cons] at hj ⊢
          rw [getD_dropLast hj]
        · show ∀ m, r.length - 1 ≤ m → m < ((r.dropLast :: T).headD []).length →
            r.getLast hrne < ((r.dropLast :: T).headD []).getD m 0
          intro m hm hmlt
          simp only [List.headD_cons] at hmlt
          exact absurd hmlt (by omega)
  | r :: T, i + 1, hc, hne, hcorner => by
      rw [isCorner_cons_succ] at hcorner
      have hTne : T ≠ [] := by
        intro h
        rw [h] at hcorner
        exact absurd (isCorner_lt_length hcorner) (by simp)
      have hTc : ColStrict T := colStrict_tail hc
      have hTn : NoEmptyRows T := fun row hrow => hne row (List.mem_cons_of_mem r hrow)
      obtain ⟨hTcs, z, hz, k, hk, hgk, hlenle, hentries, hfrom⟩ :=
        uninsert_colStrict_step T i hTc hTn hcorner
      obtain ⟨hsbl, hsbe⟩ := strictBelow_head hc hTne
      -- `z` sits below `r` in column `k`, so `r` has an eligible entry and its reverse
      -- insertion succeeds
      have hkr : k < r.length := lt_of_lt_of_le hk hsbl
      have hrk : r.getD k 0 < z := by rw [← hgk]; exact hsbe k hk
      obtain ⟨zUp, hzUp⟩ := rowUninsert_isSome_of_lt hkr hrk
      obtain ⟨kUp, hkUp, hgUp, hsetUp, hltUp, hrightUp⟩ := rowUninsert_spec r z zUp hzUp
      have hmono : k ≤ kUp := reverse_bump_index_mono ⟨hsbl, hsbe⟩ hk hgk hrightUp
      obtain ⟨T'', w, hT⟩ : ∃ T'' w, uninsert T i = (T'', w) := ⟨_, _, rfl⟩
      obtain ⟨r', v, hru⟩ : ∃ r' v, rowUninsert r z = (r', v) := ⟨_, _, rfl⟩
      rw [hT] at hz hTcs hlenle hentries hfrom
      simp only at hz hTcs hlenle hentries hfrom
      rw [hru] at hzUp hsetUp
      simp only at hzUp hsetUp
      -- pin both option components before rewriting, or the `match` cannot reduce
      subst hz
      subst hzUp
      have hfull : uninsert (r :: T) (i + 1) = (r' :: T'', some zUp) := by
        rw [uninsert_succ, hT]
        simp only
        rw [hru]
      rw [hfull]
      simp only
      refine ⟨colStrict_cons hTcs ?_, zUp, rfl, kUp, ?_, ?_, ?_, ?_, ?_⟩
      · intro row hrow
        rw [eq_headD_of_mem_head? hrow, hsetUp]
        refine ⟨by simp only [List.length_set]; exact le_trans hlenle hsbl, fun jj hj => ?_⟩
        have hjT : jj < (T.headD []).length := lt_of_lt_of_le hj hlenle
        by_cases hjU : jj = kUp
        · subst hjU
          rw [getD_set_self hkUp]
          exact hfrom jj hmono hj
        · rw [getD_set_ne (fun h => hjU h.symm)]
          exact lt_of_lt_of_le (hsbe jj hjT) (hentries jj hj)
      · show kUp < ((r :: T).headD []).length
        simp only [List.headD_cons]; exact hkUp
      · show ((r :: T).headD []).getD kUp 0 = zUp
        simp only [List.headD_cons]; exact hgUp
      · show ((r' :: T'').headD []).length ≤ ((r :: T).headD []).length
        simp only [List.headD_cons, hsetUp, List.length_set]
        omega
      · show ∀ jj, jj < ((r' :: T'').headD []).length →
          ((r :: T).headD []).getD jj 0 ≤ ((r' :: T'').headD []).getD jj 0
        intro jj hj
        simp only [List.headD_cons, hsetUp] at hj ⊢
        simp only [List.length_set] at hj
        by_cases hjU : jj = kUp
        · subst hjU
          rw [getD_set_self hkUp, hgUp]
          exact le_of_lt hltUp
        · rw [getD_set_ne (fun h => hjU h.symm)]
      · show ∀ m, kUp ≤ m → m < ((r' :: T'').headD []).length →
          zUp < ((r' :: T'').headD []).getD m 0
        intro m hm hmlt
        simp only [List.headD_cons, hsetUp] at hmlt ⊢
        simp only [List.length_set] at hmlt
        by_cases hmU : m = kUp
        · subst hmU
          rw [getD_set_self hkUp]
          exact hltUp
        · rw [getD_set_ne (fun h => hmU h.symm)]
          exact lt_of_lt_of_le hltUp (hrightUp m (lt_of_le_of_ne hm (fun h => hmU h.symm)) hmlt)

/-! ### The headline forms

`uninsert_colStrict_step` carries `CascadeStep` because the induction needs it. Callers do not. -/

/-- **The reverse cascade preserves column-strictness at a corner.** -/
theorem uninsert_colStrict {T : List (List ℕ)} {i : ℕ}
    (hc : ColStrict T) (hne : NoEmptyRows T) (hcorner : IsCorner T i) :
    ColStrict (uninsert T i).1 :=
  (uninsert_colStrict_step T i hc hne hcorner).1

/-- **And at a corner it always succeeds.** The `none` branch of `rowUninsert` is unreachable on a
genuine tableau: the value coming up from row `i + 1` sits strictly below the entry above it, so
the row above always has something eligible to displace. Worth stating separately — the definition
of `uninsert` has a `none` branch that a reader would otherwise have to reason about at every
call site. -/
theorem uninsert_isSome_of_isCorner {T : List (List ℕ)} {i : ℕ}
    (hc : ColStrict T) (hne : NoEmptyRows T) (hcorner : IsCorner T i) :
    ∃ z, (uninsert T i).2 = some z := by
  obtain ⟨-, z, hz, -⟩ := uninsert_colStrict_step T i hc hne hcorner
  exact ⟨z, hz⟩

/-! ### Relation to the shape-level corner predicate

`QOU.Mathlib.SYTEnum.IsCorner` (`SYTListCorner.lean`) is the same notion one level down, on the
shape list rather than the tableau. The two agree, and the bridge is recorded so this is not read
as a fourth duplication of corpus machinery.

The tableau-level form is the one the induction wants: `isCorner_cons_succ` is a one-line `simp`,
whereas the shape-level form would push `tableauShape` through every step. It also needs no
explicit `i < T.length` conjunct — out-of-range rows read as `[]`, so `0 < 0` fails and the range
condition is already implied (`isCorner_lt_length`). -/

/-- Shape lookup is row-length lookup, in range and out. -/
theorem getD_tableauShape (T : List (List ℕ)) (i : ℕ) :
    (tableauShape T).getD i 0 = (T.getD i []).length := by
  induction T generalizing i with
  | nil => simp [tableauShape]
  | cons r rest ih =>
      cases i with
      | zero => simp [tableauShape]
      | succ j => simpa [tableauShape] using ih j

/-- The tableau-level and shape-level corner predicates agree. -/
theorem isCorner_iff_shape (T : List (List ℕ)) (i : ℕ) :
    IsCorner T i ↔ QOU.Mathlib.SYTEnum.IsCorner (tableauShape T) i := by
  constructor
  · intro h
    exact ⟨by simpa [tableauShape] using isCorner_lt_length h,
      by rw [getD_tableauShape, getD_tableauShape]; exact h⟩
  · intro h
    rw [IsCorner, ← getD_tableauShape, ← getD_tableauShape]
    exact h.2

/-- **The last row is always a corner** — the RSK inverse's actual call site, since the cell
carrying the largest recording entry sits at the end of some row. -/
theorem isCorner_last {T : List (List ℕ)} (hne : NoEmptyRows T) (h : T ≠ []) :
    IsCorner T (T.length - 1) := by
  have hlen : 0 < T.length := List.length_pos_iff.mpr h
  rw [IsCorner, getD_row_past (by omega : T.length ≤ T.length - 1 + 1)]
  simp only [List.length_nil]
  refine List.length_pos_iff.mpr ?_
  rw [getD_row_eq (by omega : T.length - 1 < T.length)]
  exact hne _ (List.getElem_mem _)

end QOU.Mathlib.Schensted
