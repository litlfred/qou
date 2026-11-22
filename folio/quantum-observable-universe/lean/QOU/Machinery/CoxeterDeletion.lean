import QOU.Machinery.CoxeterReflectionCocycle

/-!
# The deletion condition, and reduced subwords

`QOU.Machinery.CoxeterReflectionCocycle` proved the exchange property — `strong_exchange`,
for **any** word and **any** right inversion — sorry-free at every rank. This file takes the
next classical step, which nothing in the corpus had:

* **`exists_deletion`** (the *deletion condition*, Björner–Brenti Thm 1.4.4): a word that is
  not reduced has **two** letters whose deletion leaves the product unchanged.
* **`exists_reduced_sublist`**: hence every word contains a **reduced subword** with the same
  product — not merely *some* reduced word, which is Mathlib's `exists_reduced_word'`, but one
  sitting inside the given word.

## Why the second one is the interesting half

Mathlib already gives *a* reduced word for any `w`. The subword strengthening is what the
**Bruhat order** needs: `QOU.Machinery.CoxeterBruhat` defines `u ≤ w` by "some reduced word
for `w` has a subword multiplying to `u`" and records, deliberately, that transitivity,
antisymmetry, the subword property and the lifting property are *not* proved there because
"each needs the exchange condition". `exists_reduced_sublist` is the first of those inputs
delivered in the form they are consumed in.

## What this is a step toward, and what it is not

The chain to Matsumoto's theorem — any two reduced expressions for the same `w` are related
by braid moves — runs *exchange → deletion → Matsumoto*. The first was already here; this
file supplies the second.

✅ **The third landed the same day** (2026-09-06): `QOU.IwahoriHecke.Matsumoto`, via
`CoxeterRankTwo` and `CoxeterDihedralDescent`. It is hypothesis-free for every Coxeter system
as of 2026-09-07, `CoxeterRankTwo.DihedralExact` having been proved in
`CoxeterDihedralOrder`. The paragraph below saying "nothing here closes Matsumoto" is still an
accurate statement about *this file*.

The conditional that consumes it is `QOU.IwahoriHecke.TwMatsumoto.exists_Tw_of_matsumoto`.
Not `BraidWordInvariance.exists_Tw_of_braidEquiv`, which quantifies over *all* words and whose
hypothesis is therefore **false** on a Coxeter group — refuted in the same tranche by
`TwMatsumoto.not_braidEquiv_hypothesis`, since braid moves preserve word length while
`π [i,i] = π []`.

Nothing here closes Matsumoto, and nothing here should be read as closing it.

## The proof, and why it is short

Induction along the word from the right (`List.reverseRecOn`). Either the prefix is already
non-reduced, in which case the inductive deletion survives appending a letter; or the prefix
is reduced and the new letter must therefore be a right descent of its product — at which
point `strong_exchange` deletes one letter of the prefix, and the appended letter is the
second deletion. No case analysis on the Coxeter matrix, no rank restriction.

-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, Thm 1.4.4 (deletion)
-- Ref: [bourbaki1968] Lie IV §1
-- Ref: [leitner2026] bean qou-06h7
-/

namespace QOU.Machinery.CoxeterDeletion

open CoxeterSystem List
open QOU.Machinery.CoxeterParabolic

variable {B W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

/-- The product of a one-letter word. -/
private theorem wordProd_single (i : B) : π [i] = σ i := by simp

/-- **The deletion condition.** A word that is not reduced has two positions `a < b` whose
deletion leaves the product unchanged.

This is the classical companion of the exchange property, and it follows from the *strong*
form proved in `CoxeterReflectionCocycle` with one induction along the word. -/
theorem exists_deletion : ∀ ω : List B, ¬ cs.IsReduced ω →
    ∃ a b : ℕ, a < b ∧ b < ω.length ∧ π ω = π ((ω.eraseIdx b).eraseIdx a) := by
  intro ω
  induction ω using List.reverseRecOn with
  | nil =>
    intro h
    exact absurd (show cs.IsReduced ([] : List B) by simp [CoxeterSystem.IsReduced]) h
  | append_singleton ω' i ih =>
    intro h
    by_cases hred : cs.IsReduced ω'
    · -- The prefix is reduced, so the appended letter must be a right descent.
      have hdesc : cs.IsRightDescent (π ω') i := by
        by_contra hnd
        rw [cs.not_isRightDescent_iff] at hnd
        refine h ?_
        show ℓ (π (ω' ++ [i])) = (ω' ++ [i]).length
        rw [cs.wordProd_append, wordProd_single cs i, hnd, hred]
        simp
      have hinv : cs.IsRightInversion (π ω') (σ i) :=
        (cs.isRightInversion_simple_iff_isRightDescent (π ω') i).mpr hdesc
      obtain ⟨r, hr, hreq⟩ := strong_exchange cs ω' hinv
      refine ⟨r, ω'.length, hr, by simp, ?_⟩
      have hb : ((ω' ++ [i]).eraseIdx ω'.length) = ω' := by
        simp [List.eraseIdx_append_of_length_le]
      rw [hb, ← hreq, cs.wordProd_append, wordProd_single cs i]
    · -- The prefix is already non-reduced; its deletion survives the append.
      obtain ⟨a, b, hab, hb, heq⟩ := ih hred
      have hlen : (ω'.eraseIdx b).length = ω'.length - 1 := List.length_eraseIdx_of_lt hb
      have ha' : a < (ω'.eraseIdx b).length := by omega
      refine ⟨a, b, hab, by simp only [List.length_append, List.length_singleton]; omega, ?_⟩
      rw [List.eraseIdx_append_of_lt_length hb [i],
        List.eraseIdx_append_of_lt_length ha' [i],
        cs.wordProd_append, cs.wordProd_append, heq]

/-- **Every word contains a reduced subword with the same product.**

Stronger than Mathlib's `exists_reduced_word'`, which produces *a* reduced word for the
element; here the reduced word is a `List.Sublist` of the word one started with. That is the
form the Bruhat order's subword criterion consumes. -/
theorem exists_reduced_sublist : ∀ (n : ℕ) (ω : List B), ω.length = n →
    ∃ ω' : List B, ω' <+ ω ∧ cs.IsReduced ω' ∧ π ω' = π ω := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro ω hn
    by_cases hred : cs.IsReduced ω
    · exact ⟨ω, List.Sublist.refl ω, hred, rfl⟩
    · obtain ⟨a, b, hab, hb, heq⟩ := exists_deletion cs ω hred
      have hlb : (ω.eraseIdx b).length = ω.length - 1 := List.length_eraseIdx_of_lt hb
      have ha2 : a < (ω.eraseIdx b).length := by omega
      have hla : ((ω.eraseIdx b).eraseIdx a).length = (ω.eraseIdx b).length - 1 :=
        List.length_eraseIdx_of_lt ha2
      obtain ⟨ω', hsub, hred', hprod⟩ :=
        ih ((ω.eraseIdx b).eraseIdx a).length (by omega) _ rfl
      refine ⟨ω', hsub.trans (((ω.eraseIdx b).eraseIdx_sublist a).trans
        (ω.eraseIdx_sublist b)), hred', ?_⟩
      rw [hprod, ← heq]

/-- The convenient form: no explicit length bookkeeping. -/
theorem exists_reduced_sublist' (ω : List B) :
    ∃ ω' : List B, ω' <+ ω ∧ cs.IsReduced ω' ∧ π ω' = π ω :=
  exists_reduced_sublist cs ω.length ω rfl

end QOU.Machinery.CoxeterDeletion
