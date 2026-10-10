import QOU.MathlibExt.TemperleyLiebThresholdBridge

/-!
# The δ rule, proved at the normal-form index

**Bean `qou-cds1`.** `computations/tl_closure_rule_probe.py` measured, on all
3456 products at `n = 2..7`:

    loops = 1   ⟺   k ∈ I  ∧  k-1 ∉ I

`TemperleyLiebClosure` proved the *mechanism* — `e_mul_prod_eq_smul`: on a word
`pre ++ k :: post` whose prefix is far from `k`, left multiplication by `e_k`
returns the same word scaled by `δ`. What was missing was the step from the
measured condition to that hypothesis. This file supplies it.

    e_mul_elt_eq_smul :  k ∈ I  →  (∀ j ∈ I, j+1 ≠ k)  →
                         e_k * elt(I,J)  =  δ • elt(I,J)

So the δ half of the closure rule is now **proved as stated**, not merely
observed on 3456 rows and explained by a sketch.

## Why the condition is what it is

`k ∈ I` puts `k` at the top of some block, so the word has `k` in it. `k-1 ∉ I`
forces every *earlier* block's top to be `≤ k-2` — an earlier top is `< k` by
sortedness, and cannot be `k-1` by hypothesis — and `descRun_le` carries that
bound to every letter of those blocks. Two or more below `k` is exactly
"far from `k`" in `e_farCommute`'s sense. That is the whole content of
`word_split`.

Every step of the chain is now closed: the bound is `descRun_le`
(`TemperleyLiebWordBlocks`), the block-top ordering is `elems_sorted`, and the
`j_r ≤ i_r` that `descRun_eq_cons` needs is `threshold_to_pointwise`
(`TemperleyLiebThresholdBridge`) — the gap recorded two tranches ago.

## 🛑 What is NOT proved

* **The `loops = 0` branch remains open** — 2378 of the 3456 products, no
  candidate formula fits, and `|I'| - |I|` moves in both directions. Nothing
  here touches it, and it is what still blocks `dim TL_n = catalan n`.
* **`card (NormalIdx m) = catalan (m+1)` is still `decide` at `m ≤ 6`**, not a
  theorem at general `m`.
* The converse of `threshold_to_pointwise` is still unproved and still
  unneeded.

No class, axiom or `sorry` stands in for any of this.

## A note on `subst`

`word_split` substitutes `k := A[r]` rather than rewriting with `A[r] = k`. That
is not cosmetic: `A[r]` carries its bounds proof, so `rw` finds no syntactic
occurrence and silently fails to fire. Recorded because the failure looks like a
missing lemma and is not one.

-- Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.MathlibExt.TemperleyLiebDeltaRule

open QOU.MathlibExt.TemperleyLieb
open QOU.MathlibExt.TemperleyLiebNormalForm
open QOU.MathlibExt.TemperleyLiebWordBlocks

variable {m : ℕ} {γ : Type*}


/-- Being two or more below `k` is exactly "far from `k`" in the sense
`e_farCommute` wants. -/
theorem far_of_le_sub_two {k t : Fin m} (h : t.val + 2 ≤ k.val) :
    ¬ adjFin k t ∧ k ≠ t := by
  constructor
  · rintro (h1 | h2)
    · omega
    · omega
  · intro he
    rw [he] at h
    omega

/-- If `i < k` and `i ≠ k-1` then `i ≤ k-2`. The arithmetic step behind
"`k-1 ∉ I` makes every earlier block far from `k`". -/
theorem le_sub_two_of_lt_of_ne {k i : Fin m} (hlt : i.val < k.val)
    (hne : i.val + 1 ≠ k.val) : i.val + 2 ≤ k.val := by
  omega


theorem zipWith_split {α β γ : Type*} (f : α → β → γ) (A : List α) (B : List β)
    (r : ℕ) (hA : r ≤ A.length) (hB : r ≤ B.length) :
    List.zipWith f A B
      = List.zipWith f (A.take r) (B.take r) ++ List.zipWith f (A.drop r) (B.drop r) := by
  rw [← List.zipWith_append (by simp [hA, hB]), List.take_append_drop, List.take_append_drop]

theorem flatten_zipWith_split {α β : Type*} (f : α → β → List γ) (A : List α) (B : List β)
    (r : ℕ) (hA : r < A.length) (hB : r < B.length) :
    (List.zipWith f A B).flatten
      = (List.zipWith f (A.take r) (B.take r)).flatten
        ++ (f (A[r]'hA) (B[r]'hB)
            ++ (List.zipWith f (A.drop (r+1)) (B.drop (r+1))).flatten) := by
  rw [zipWith_split f A B r hA.le hB.le, List.flatten_append,
    List.drop_eq_getElem_cons hA, List.drop_eq_getElem_cons hB,
    List.zipWith_cons_cons, List.flatten_cons]


theorem mem_zipWith_exists {α β γ' : Type*} {f : α → β → γ'} {A : List α} {B : List β}
    {c : γ'} (h : c ∈ List.zipWith f A B) : ∃ a ∈ A, ∃ b ∈ B, c = f a b := by
  induction A generalizing B with
  | nil => simp at h
  | cons a t ih =>
      cases B with
      | nil => simp at h
      | cons b u =>
          rw [List.zipWith_cons_cons, List.mem_cons] at h
          rcases h with rfl | h
          · exact ⟨a, by simp, b, by simp, rfl⟩
          · obtain ⟨a', ha', b', hb', rfl⟩ := ih h
            exact ⟨a', by simp [ha'], b', by simp [hb'], rfl⟩

theorem mem_take_lt_getElem {A : List (Fin m)} (hs : A.Sorted (· < ·)) {r : ℕ}
    (hr : r < A.length) {a : Fin m} (ha : a ∈ A.take r) : a < A[r] := by
  obtain ⟨s, hs', rfl⟩ := List.getElem_of_mem ha
  have hsr : s < r := by
    have := List.length_take (l := A) (i := r); omega
  have hsA : s < A.length := lt_trans hsr hr
  rw [List.getElem_take]
  exact (List.pairwise_iff_getElem.mp hs) s r hsA hr hsr


open QOU.MathlibExt.TemperleyLiebThresholdBridge in
/-- **The instantiation.** If `k ∈ I` and no element of `I` is `k-1`, the word
of `(I,J)` splits as `pre ++ k :: post` with every letter of `pre` far from
`k` — exactly the hypothesis of `e_mul_prod_eq_smul`. -/
theorem word_split (p : NormalIdx m) {k : Fin m}
    (hk : k ∈ p.1.1) (hk1 : ∀ j ∈ p.1.1, j.val + 1 ≠ k.val) :
    ∃ pre post, p.word = pre ++ k :: post ∧ ∀ t ∈ pre, ¬ adjFin k t ∧ k ≠ t := by
  classical
  set A := elems p.1.1 with hA
  set B := elems p.1.2 with hB
  have hkA : k ∈ A := mem_elems.mpr hk
  obtain ⟨r, hr, hkr⟩ := List.getElem_of_mem hkA
  subst hkr
  have hlen : A.length = B.length := by
    rw [hA, hB, elems_length, elems_length, p.2.1]
  have hrB : r < B.length := hlen ▸ hr
  have hBr : B[r] ≤ A[r] := threshold_to_pointwise p.2.2 r hr hrB
  obtain ⟨rest, hrest⟩ := descRun_eq_cons hBr
  refine ⟨(List.zipWith descRun (A.take r) (B.take r)).flatten,
    rest ++ (List.zipWith descRun (A.drop (r+1)) (B.drop (r+1))).flatten, ?_, ?_⟩
  · rw [NormalIdx.word, ← hA, ← hB, flatten_zipWith_split descRun A B r hr hrB,
      hrest, List.cons_append]
  · intro t ht
    rw [List.mem_flatten] at ht
    obtain ⟨blk, hblk, htblk⟩ := ht
    obtain ⟨a, ha, b, _, rfl⟩ := mem_zipWith_exists hblk
    have hta : t ≤ a := descRun_le htblk
    have hak : a < A[r] := mem_take_lt_getElem (hA ▸ elems_sorted p.1.1) hr ha
    have haI : a ∈ p.1.1 := mem_elems.mp (List.mem_of_mem_take ha)
    exact far_of_le_sub_two (by
      have h1 : a.val + 1 ≠ (A[r] : Fin m).val := hk1 a haI
      have h2 : a.val < (A[r] : Fin m).val := hak
      have h3 : t.val ≤ a.val := hta
      omega)


open QOU.MathlibExt.TemperleyLiebClosure in
/-- **The measured δ rule, proved at the normal-form index.** -/
theorem e_mul_elt_eq_smul {R : Type*} [CommRing R] (δ : R) (p : NormalIdx m) {k : Fin m}
    (hk : k ∈ p.1.1) (hk1 : ∀ j ∈ p.1.1, j.val + 1 ≠ k.val) :
    e R δ (adjFin (n := m)) k * p.elt δ = δ • p.elt δ := by
  obtain ⟨pre, post, hw, hfar⟩ := word_split p hk hk1
  rw [NormalIdx.elt, hw]
  exact e_mul_prod_eq_smul δ k pre post hfar


end QOU.MathlibExt.TemperleyLiebDeltaRule
