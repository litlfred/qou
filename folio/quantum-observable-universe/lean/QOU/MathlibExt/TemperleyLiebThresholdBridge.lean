import QOU.MathlibExt.TemperleyLiebWordBlocks

/-!
# Threshold domination gives pointwise domination — the bridge `NormalIdx` needed

**Bean `qou-cds1`.** `TemperleyLiebWordBlocks` recorded a gap that was a cost of
a choice made two tranches earlier: `NormalIdx` states domination as a
**threshold count**

    ∀ x,  |I ∩ [0,x]|  ≤  |J ∩ [0,x]|

because that form needs no sorting and is decidable — which is what made
`Fintype.card` fall to `decide` for `m ≤ 6`. But `descRun_eq_cons`, and with it
the whole word construction, needs the **pointwise** form `j_r ≤ i_r`. The two
were verified equivalent for every pair at `m ≤ 7` before the encoding was
adopted; the equivalence was not *proved*.

This file proves the direction that was blocking: **threshold ⟹ pointwise.**

## The mechanism, in one lemma

Everything reduces to a single statement about a strictly sorted list:

    l[r] ≤ x   ↔   r + 1 ≤ (l.filter (· ≤ x)).length

Read left to right at `x = i_r` it says `I` has at least `r+1` elements `≤ i_r`;
the threshold hypothesis transports that to `J`; read right to left for `J` it
gives `j_r ≤ i_r`. So one iff, applied once in each direction, is the whole
bridge — no counting argument beyond it.

## Two things worth noting

**The equal-cardinality hypothesis is not needed.** `NormalIdx` carries
`J.card = I.card`, and the bridge does **not** use it. The threshold condition
alone forces pointwise domination wherever both lists have an `r`-th entry.
Stated without it, since a hypothesis that is not used should not be required.

**`elems` pays off again.** `elems_nodup`, `elems_length` and `elems_filter` all
come out of `elems` being a `filter` over `List.finRange` — nodup and sortedness
are inherited by `Sublist`, and `elems (s.filter p) = (elems s).filter p` is a
`List.filter_filter` away. None of this would be available from `Finset.sort`,
which is also the reason `decide` works on this type at all.

## 🛑 What this does NOT do

* **The converse is not proved.** Only threshold ⟹ pointwise is here, which is
  the direction the word construction needs. The other direction is true (both
  were checked at `m ≤ 7`) and is not required by anything yet.
* **The instantiation is still not finished.** This unblocks
  `descRun_eq_cons` at a normal-form index, but assembling
  `word (I,J) = pre ++ k :: post` with `pre` far from `k` — and hence
  discharging `e_mul_prod_eq_smul`'s hypothesis — is the next step and is not
  taken here.
* Nothing here bears on the `loops = 0` branch of the closure rule, which
  remains open.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebThresholdBridge

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebNormalForm
open QOU.MathlibExt.TemperleyLiebWordBlocks

variable {m : ℕ}

/-- `elems` has no duplicates — inherited from `List.finRange` by `Sublist`. -/
theorem elems_nodup (s : Finset (Fin m)) : (elems s).Nodup :=
  (List.nodup_finRange m).sublist List.filter_sublist

/-- `elems` has exactly `s.card` entries. -/
theorem elems_length (s : Finset (Fin m)) : (elems s).length = s.card := by
  classical
  have h : (elems s).toFinset = s := by
    ext x; simp [List.mem_toFinset, mem_elems]
  have hc := List.toFinset_card_of_nodup (elems_nodup s)
  rw [h] at hc
  exact hc.symm

/-- Filtering commutes with `elems`. Both sides are one `filter` over
`List.finRange`, so this is `List.filter_filter` plus commutativity of `∧`. -/
theorem elems_filter (s : Finset (Fin m)) (p : Fin m → Prop) [DecidablePred p] :
    elems (s.filter p) = (elems s).filter (fun x => decide (p x)) := by
  simp only [elems, List.filter_filter]
  congr 1
  ext x
  simp [Finset.mem_filter, and_comm]

/-- **The one lemma the bridge rests on.** For a strictly sorted list, "the
`r`-th entry is `≤ x`" is exactly "at least `r+1` entries are `≤ x`".

The `¬ (a ≤ x)` branch is where sortedness is used: if the head already exceeds
`x` then so does everything after it, so the filter is empty and both sides are
false. -/
theorem sorted_getElem_le_iff :
    ∀ (l : List (Fin m)), l.Sorted (· < ·) → ∀ (x : Fin m) (r : ℕ) (hr : r < l.length),
      (l[r]'hr ≤ x ↔ r + 1 ≤ (l.filter (fun y => decide (y ≤ x))).length) := by
  intro l
  induction l with
  | nil => intro _ _ r hr; simp at hr
  | cons a t ih =>
      intro hs x r hr
      have hst : t.Sorted (· < ·) := hs.of_cons
      have hlt : ∀ y ∈ t, a < y := fun y hy => (List.sorted_cons.mp hs).1 y hy
      by_cases hax : a ≤ x
      · simp only [List.filter_cons, decide_eq_true_eq, if_pos hax, List.length_cons]
        cases r with
        | zero => simpa using hax
        | succ r' =>
            have hr' : r' < t.length := by simpa using hr
            simpa using ih hst x r' hr'
      · have hnone : ∀ y ∈ t, ¬ y ≤ x := by
          intro y hy hyx
          exact hax (le_of_lt (lt_of_lt_of_le (hlt y hy) hyx))
        have hfil : ((a :: t).filter (fun y => decide (y ≤ x))) = [] := by
          rw [List.filter_cons_of_neg (by simpa using hax)]
          exact List.filter_eq_nil_iff.mpr (by intro y hy; simpa using hnone y hy)
        rw [hfil]
        simp only [List.length_nil]
        constructor
        · intro hle
          exfalso
          cases r with
          | zero => exact hax (by simpa using hle)
          | succ r' =>
              have hr' : r' < t.length := by simpa using hr
              exact hnone _ (List.getElem_mem hr') (by simpa using hle)
        · intro h; omega

/-- **Threshold domination gives pointwise domination.**

The gap `TemperleyLiebWordBlocks` recorded, closed. Note that
`J.card = I.card` — which `NormalIdx` does carry — is **not** needed: the
threshold condition alone forces the pointwise inequality wherever both lists
have an `r`-th entry. -/
theorem threshold_to_pointwise {I J : Finset (Fin m)}
    (hdom : ∀ x : Fin m, (I.filter (· ≤ x)).card ≤ (J.filter (· ≤ x)).card)
    (r : ℕ) (hI : r < (elems I).length) (hJ : r < (elems J).length) :
    (elems J)[r] ≤ (elems I)[r] := by
  classical
  set x := (elems I)[r] with hx
  have h1 : r + 1 ≤ (I.filter (fun y => y ≤ x)).card := by
    rw [← elems_length, elems_filter]
    exact (sorted_getElem_le_iff (elems I) (elems_sorted I) x r hI).mp le_rfl
  have h2 : r + 1 ≤ (J.filter (fun y => y ≤ x)).card := le_trans h1 (hdom x)
  rw [← elems_length, elems_filter] at h2
  exact (sorted_getElem_le_iff (elems J) (elems_sorted J) x r hJ).mpr h2

end QOU.MathlibExt.TemperleyLiebThresholdBridge
