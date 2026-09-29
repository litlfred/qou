import QOU.MathlibExt.TemperleyLiebClosure

/-!
# Block structure of a normal-form word — and a cost of the `(I,J)` encoding

**Bean `qou-cds1`.** `TemperleyLiebClosure` proved the mechanism behind the
measured δ rule:

    e_k · (pre ++ k :: post)  =  δ · (pre ++ k :: post)      when pre is far from k

and left one thing to do — **instantiate it at the normal-form index**, i.e.
derive "`pre` is far from `k`" from the measured condition `k ∈ I ∧ k-1 ∉ I`.

This file takes the list-level steps that instantiation needs, and records a
gap that attempting it exposed.

## 🛑 The gap, which is a cost of a choice made two tranches back

`NormalIdx` states domination as a **threshold count**

    ∀ x,  |I ∩ [0,x]|  ≤  |J ∩ [0,x]|

rather than pointwise `j_r ≤ i_r`. That was deliberate and is documented in
`TemperleyLiebNormalForm`: the threshold form needs no sorting, is decidable,
and is what makes `Fintype.card` fall to `decide` — seven cardinalities came out
of it, up to `catalan 7 = 429`.

**The cost was not priced.** `descRun_eq_cons` — that a block's word begins with
its top index — needs `j_r ≤ i_r`, the **pointwise** form. The two are
equivalent (checked for every pair at `m ≤ 7` before the encoding was adopted),
but that equivalence is **not proved in Lean**, and the word construction cannot
proceed without the direction threshold ⟹ pointwise.

So the encoding that made the *count* cheap makes the *word* expensive, and the
missing bridge is a theorem, not a definition unfolding. Recorded because the
trade was made knowingly in one direction and its other side only appeared when
the word was needed.

The bridge to prove: for equal-size `I, J`, the threshold condition gives
`|J ∩ [0, i_r]| ≥ r+1` (since `|I ∩ [0, i_r]| = r+1`), hence `j_r ≤ i_r`.

## What is proved here

* `mem_elems` — `elems` lists exactly the members.
* `elems_sorted` — and lists them strictly increasing, inherited from
  `List.finRange` by `Sublist`. No sorting algorithm and no sortedness proof of
  its own, which is the point of defining `elems` by `filter`.
* `descRun_le` — every letter of a block is at most its top index. This is the
  half of the block structure the δ rule actually consumes: it is what makes an
  earlier block "far from `k`" once its top is known to be `≤ k-2`.
* `descRun_eq_cons` — a block's word begins with its top index, given `j ≤ i`.

`descRun_le` is independent of the gap above. `descRun_eq_cons` takes `j ≤ i` as
a hypothesis, so it is usable the moment the bridge lands, and is not blocked on
it.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebWordBlocks

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebNormalForm

variable {m : ℕ}

/-- `elems` lists exactly the members of `s`. -/
theorem mem_elems {s : Finset (Fin m)} {x : Fin m} : x ∈ elems s ↔ x ∈ s := by
  simp [elems, List.mem_filter, List.mem_finRange]

/-- **`elems` is strictly increasing** — inherited from `List.finRange` through
`Sublist`, with no sorting step and no sortedness proof of its own. That is the
whole reason `elems` is a `filter` rather than a `Finset.sort`. -/
theorem elems_sorted (s : Finset (Fin m)) : (elems s).Sorted (· < ·) :=
  (List.pairwise_lt_finRange m).sublist List.filter_sublist

/-- **Every letter of a block is at most the block's top index.**

This is the half of the block structure the δ rule consumes: an earlier block
whose top is `≤ k-2` has *all* its letters `≤ k-2`, hence all far from `k`. -/
theorem descRun_le {i j t : Fin m} (h : t ∈ descRun i j) : t ≤ i := by
  simp only [descRun, List.mem_map, List.mem_range] at h
  obtain ⟨u, _, rfl⟩ := h
  exact Fin.le_def.mpr (Nat.sub_le _ _)

/-- **A block's word begins with its top index.**

Takes `j ≤ i` as a hypothesis rather than deriving it, so it is usable the
moment the threshold-to-pointwise bridge lands and is not blocked on it. -/
theorem descRun_eq_cons {i j : Fin m} (h : j ≤ i) :
    ∃ rest, descRun i j = i :: rest := by
  have hij : j.val ≤ i.val := h
  refine ⟨(List.range (i.val - j.val)).map
      fun t => (⟨i.val - (t + 1), lt_of_le_of_lt (Nat.sub_le _ _) i.isLt⟩ : Fin m), ?_⟩
  simp only [descRun, show i.val + 1 - j.val = (i.val - j.val) + 1 from by omega,
    List.range_succ_eq_map, List.map_cons, List.map_map]
  refine congrArg₂ _ (Fin.ext (by simp)) rfl

end QOU.MathlibExt.TemperleyLiebWordBlocks
