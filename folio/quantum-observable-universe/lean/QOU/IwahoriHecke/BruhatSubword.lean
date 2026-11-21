import QOU.IwahoriHecke.Matsumoto
import QOU.Machinery.CoxeterBruhatOrder

/-!
# The subword property, and Bruhat transitivity

`QOU.Machinery.CoxeterBruhat` defines `u ≤ w` by "**some** reduced word for `w` has a subword
multiplying to `u`" and lists four properties it does not prove. `CoxeterBruhatOrder` closed
antisymmetry by a length squeeze. The remaining three all wait on the **subword property**:

> `u ≤ w` implies **every** reduced word for `w` has a subword multiplying to `u`.

That is a statement about all reduced words, so it needs Matsumoto — which
`QOU.IwahoriHecke.Matsumoto` now supplies. This file spends it and closes two more of the four.

## What closes

* **`subword_property`** — the statement above, and `bruhatLe_iff_forall_reduced`, which turns the
  existential definition into a universal one.
* **`bruhatLe_trans`** — hence **transitivity**, immediately: the witness for `v ≤ w` can be taken
  reduced (`bruhatLe_reduced_witness`), the subword property applies to *that* word, and
  `List.Sublist` is transitive.

## The argument

Matsumoto reduces everything to a **single braid move**, and a braid move only rewrites one
alternating block: a subword splits as `a ++ b ++ c` with `b` inside the block, and only `b` has to
be replaced. So the whole content is the rank-two lemma **`exists_subword_altWord_swap`**: a subword
of `altWord i j (M i j)` has a same-product subword of `altWord j i (M j i)`.

That in turn is `CoxeterRankTwo`'s structure theorem plus two list facts — the alternating word of
length `k ≤ n` is a **prefix** of the one of length `n` in the same spelling, and a **tail** of it in
the other spelling when `k < n`. The one case those miss is `k = n`, where the two spellings have
the same product outright: that is the braid relation (`wordProd_altWord_braid`).

## Scope — nothing here is conditional

`subword_property` and `bruhatLe_trans` used to carry `DihedralExact` and `M i j ≠ 0`, **solely
because they call Matsumoto**; `Matsumoto` no longer has them (`CoxeterDihedralOrder` proves both
from the geometric representation), so neither does this file. Everything below holds for every
Coxeter system.

`exists_subword_altWord_swap` and the braid-move transport were **already** unconditional before
that: the swap never needs to know the order of `σᵢσⱼ`, only that a reduced rank-two word is
alternating and that the two full-length spellings share a product. That was not the shape I
expected when writing it — the hypotheses were stated on the swap first and the compiler reported
them unused.

✅ **The lifting property landed the same day**, in `QOU.IwahoriHecke.BruhatReflection`, off the
subword property proved here — so all four of `CoxeterBruhat`'s deferred properties are now closed.

✅ **And the two Bruhat orders were shown to agree**, in `QOU.IwahoriHecke.BruhatConverse`:
`BruhatLe ↔ ReflLe` and its left-handed mirror `BruhatLe ↔ LeftReflLe`, which is what a consumer
citing Mathas' Prop 3.7 needs. `BruhatReflection` had supplied `ReflLe → BruhatLe`; the converse
was the open half.

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, Thm 2.2.2 (subword property)
-- Ref: [humphreys1990] Reflection Groups and Coxeter Groups, §5.10
-- Ref: [leitner2026] beans qou-06h7, qou-phir
-/

namespace QOU.IwahoriHecke.BruhatSubword

open CoxeterSystem List
open QOU.IwahoriHecke.BraidWord QOU.IwahoriHecke.Matsumoto
open QOU.Machinery.CoxeterParabolic QOU.Machinery.CoxeterRankTwo
open QOU.Machinery.CoxeterBruhat QOU.Machinery.CoxeterBruhatOrder

variable {B : Type*}

/-! ## Alternating words as lists -/

/-- Every letter of an alternating word is one of its two indices. -/
theorem mem_altWord : ∀ (n : ℕ) (i j l : B), l ∈ altWord i j n → l = i ∨ l = j := by
  intro n
  induction n with
  | zero => intro i j l hl; simp [altWord] at hl
  | succ n ih =>
    intro i j l hl
    rw [altWord_succ] at hl
    rcases List.mem_cons.mp hl with h | h
    · exact Or.inl h
    · exact (ih j i l h).symm

/-- **Same spelling: a prefix.** `altWord i j k` is a prefix of `altWord i j n` for `k ≤ n`. -/
theorem altWord_sublist_self :
    ∀ (k : ℕ) (i j : B) (n : ℕ), k ≤ n → altWord i j k <+ altWord i j n := by
  intro k
  induction k with
  | zero => intro i j n _; simp [altWord_zero]
  | succ k ih =>
    intro i j n h
    obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
    rw [altWord_succ, altWord_succ]
    exact (ih j i n' (by omega)).cons₂ i

/-- **Other spelling: a tail.** `altWord j i k` sits inside `altWord i j n` for `k < n` — drop the
leading letter and apply the prefix fact. -/
theorem altWord_swap_sublist (i j : B) {k n : ℕ} (h : k < n) :
    altWord j i k <+ altWord i j n := by
  obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
  rw [altWord_succ]
  exact (altWord_sublist_self k j i n' (by omega)).cons i

/-! ## The braid relation, in `altWord` form -/

variable {W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd

/-- **The braid relation.** The two alternating words of length `M i j` have the same product.
Mathlib states it for `alternatingWord`; the bridge carries it to `altWord`, in both parities. -/
theorem wordProd_altWord_braid (i j : B) :
    π (altWord i j (M i j)) = π (altWord j i (M i j)) := by
  have hbase : π (alternatingWord i j (M i j)) = π (alternatingWord j i (M i j)) := by
    have h := cs.prod_alternatingWord_eq_prod_alternatingWord_sub i j (M i j) (by omega)
    rwa [show M i j * 2 - M i j = M i j by omega] at h
  rw [altWord_eq_alternatingWord, altWord_eq_alternatingWord]
  by_cases he : Even (M i j)
  · rw [if_pos he, if_pos he]; exact hbase
  · rw [if_neg he, if_neg he]; exact hbase.symm

/-! ## The rank-two swap -/

/-- **The one piece of real content.** A subword of `altWord i j (M i j)` has a same-product
subword of `altWord j i (M j i)`.

The subword's product `v` lies in the rank-two parabolic and has length at most `M i j`; by
`CoxeterRankTwo` it has an **alternating** reduced word, of one spelling or the other. The prefix
and tail facts cover every case but `ℓ(v) = M i j` in the wrong spelling, and there the braid
relation says the whole target word already has product `v`. -/
theorem exists_subword_altWord_swap {i j : B}
    {b : List B} (hb : b <+ altWord i j (M i j)) :
    ∃ b' : List B, b' <+ altWord j i (M j i) ∧ π b' = π b := by
  classical
  have hMsym : M j i = M i j := M.symmetric j i
  set J : Set B := ({i, j} : Set B) with hJ
  have hbmem : ∀ l ∈ b, l ∈ J := by
    intro l hl
    have := mem_altWord (M i j) i j l (hb.mem hl)
    simpa [hJ] using this
  have hv : π b ∈ parabolic cs J := wordProd_mem_parabolic cs J hbmem
  obtain ⟨p, hp, hpred, hpv⟩ := exists_reducedWord_of_mem_parabolic cs hv
  have hpmem : ∀ l ∈ p, l = i ∨ l = j := by
    intro l hl; have := hp l hl; simpa [hJ] using this
  -- `p` is one of the two alternating words of its length.
  have hpalt : p = altWord i j p.length ∨ p = altWord j i p.length := by
    rcases isReduced_pair_eq_alternatingWord cs (i := i) (j := j) p hpred hpmem with h | h
    · by_cases he : Even p.length
      · left; rw [altWord_eq_alternatingWord, if_pos he]; exact h
      · right; rw [altWord_eq_alternatingWord, if_neg he]; exact h
    · by_cases he : Even p.length
      · right; rw [altWord_eq_alternatingWord, if_pos he]; exact h
      · left; rw [altWord_eq_alternatingWord, if_neg he]; exact h
  -- `|p| = ℓ(π b) ≤ |b| ≤ M i j`.
  have hple : p.length ≤ M i j := by
    have h1 : ℓ (π p) = p.length := hpred
    have h2 : ℓ (π b) ≤ b.length := cs.length_wordProd_le b
    have h3 : b.length ≤ (altWord i j (M i j)).length := hb.length_le
    rw [length_altWord] at h3
    rw [hpv] at h1
    omega
  rw [hMsym]
  rcases hpalt with hpa | hpa
  · -- `p = altWord i j |p|`: a tail of `altWord j i (M i j)` unless `|p| = M i j`.
    rcases Nat.lt_or_ge p.length (M i j) with hlt | hge
    · exact ⟨p, hpa ▸ altWord_swap_sublist j i hlt, hpv⟩
    · have hlen : p.length = M i j := by omega
      refine ⟨altWord j i (M i j), List.Sublist.refl _, ?_⟩
      rw [← wordProd_altWord_braid cs i j, ← hlen, ← hpa, hpv]
  · -- `p = altWord j i |p|`: a prefix of `altWord j i (M i j)`.
    exact ⟨p, hpa ▸ altWord_sublist_self p.length j i (M i j) hple, hpv⟩

/-! ## Transporting a subword along a braid move -/

/-- "`ω` has a subword multiplying to `u`". -/
def HasSubwordFor (u : W) (ω : List B) : Prop := ∃ ω' : List B, ω' <+ ω ∧ π ω' = u

/-- **A braid move preserves the property.** Outside the rewritten block nothing moves; inside it,
`exists_subword_altWord_swap` supplies the replacement. -/
theorem hasSubwordFor_of_braidMove
    {u : W} {ω₁ ω₂ : List B} (h : BraidMove (fun a b => M a b) ω₁ ω₂)
    (hs : HasSubwordFor cs u ω₁) : HasSubwordFor cs u ω₂ := by
  cases h with
  | move l₁ l₂ i j =>
    obtain ⟨ω', hsub, hprod⟩ := hs
    obtain ⟨x, c, rfl, hx, hc⟩ := List.sublist_append_iff.mp hsub
    obtain ⟨a, b, rfl, ha, hb⟩ := List.sublist_append_iff.mp hx
    obtain ⟨b', hb', hbprod⟩ := exists_subword_altWord_swap cs hb
    refine ⟨a ++ b' ++ c, ?_, ?_⟩
    · exact List.sublist_append_iff.mpr
        ⟨a ++ b', c, rfl, List.sublist_append_iff.mpr ⟨a, b', rfl, ha, hb'⟩, hc⟩
    · rw [cs.wordProd_append, cs.wordProd_append, hbprod, ← cs.wordProd_append,
        ← cs.wordProd_append]
      exact hprod

/-- Hence braid-**equivalence** preserves it. -/
theorem hasSubwordFor_of_braidEquiv
    {u : W} {ω₁ ω₂ : List B} (h : BraidEquiv (fun a b => M a b) ω₁ ω₂)
    (hs : HasSubwordFor cs u ω₁) : HasSubwordFor cs u ω₂ := by
  induction h with
  | refl => exact hs
  | tail _ hstep ih => exact hasSubwordFor_of_braidMove cs hstep ih

/-! ## The subword property -/

/-- **The subword property.** If `u ≤ w` then **every** reduced word for `w` has a subword
multiplying to `u` — not merely the one the definition happens to name. -/
theorem subword_property
    {u w : W} (h : BruhatLe cs u w) {ω : List B} (hred : cs.IsReduced ω) (hw : π ω = w) :
    ∃ ω' : List B, ω' <+ ω ∧ π ω' = u := by
  obtain ⟨ω₀, ω₀', hred₀, hw₀, hsub₀, hu₀⟩ := h
  have hequiv : BraidEquiv (fun a b => M a b) ω₀ ω :=
    matsumoto' cs hred₀ hred (by rw [hw₀, hw])
  exact hasSubwordFor_of_braidEquiv cs hequiv ⟨ω₀', hsub₀, hu₀⟩

/-- The existential definition of `BruhatLe` is equivalent to the universal one. -/
theorem bruhatLe_iff_forall_reduced {u w : W} :
    BruhatLe cs u w ↔
      ∀ ω : List B, cs.IsReduced ω → π ω = w → ∃ ω' : List B, ω' <+ ω ∧ π ω' = u := by
  constructor
  · intro h ω hred hw
    exact subword_property cs h hred hw
  · intro h
    obtain ⟨ω, hred, hw⟩ := cs.exists_reduced_word' w
    obtain ⟨ω', hsub, hu⟩ := h ω hred hw.symm
    exact ⟨ω, ω', hred, hw.symm, hsub, hu⟩

/-! ## Transitivity, immediately -/

/-- **Transitivity** — the second of `CoxeterBruhat`'s four, and a two-line consequence of the
subword property.

The obstruction `CoxeterBruhatOrder` recorded was that `u ≤ v` names *some* reduced word for `v`
while `v ≤ w` produces *another* one. The subword property removes the distinction. -/
theorem bruhatLe_trans
    {u v w : W} (h₁ : BruhatLe cs u v) (h₂ : BruhatLe cs v w) : BruhatLe cs u w := by
  obtain ⟨ω, ωv, hred, hw, hsub, hvred, hv⟩ := bruhatLe_reduced_witness cs h₂
  obtain ⟨ωu, hsubu, hu⟩ := subword_property cs h₁ hvred hv
  exact ⟨ω, ωu, hred, hw, hsubu.trans hsub, hu⟩

/-! ## Type `A`: the specialisation the rest of the corpus cites -/

theorem subword_property_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u w : W} (h : BruhatLe cs u w)
    {ω : List (Fin n)} (hred : cs.IsReduced ω) (hw : cs.wordProd ω = w) :
    ∃ ω' : List (Fin n), ω' <+ ω ∧ cs.wordProd ω' = u :=
  subword_property cs h hred hw

theorem bruhatLe_trans_An {n : ℕ} {W : Type*} [Group W]
    (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W) {u v w : W}
    (h₁ : BruhatLe cs u v) (h₂ : BruhatLe cs v w) : BruhatLe cs u w :=
  bruhatLe_trans cs h₁ h₂

end QOU.IwahoriHecke.BruhatSubword
