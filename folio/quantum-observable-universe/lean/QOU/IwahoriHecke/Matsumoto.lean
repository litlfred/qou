import QOU.Machinery.CoxeterDihedralDescent
import QOU.IwahoriHecke.TwFromMatsumoto

/-!
# Matsumoto's theorem, and the `T_w` basis it unlocks

Two reduced words for the same element of a Coxeter group are related by braid moves. Mathlib
records this as an open TODO (`GroupTheory/Coxeter/Basic.lean`: *"State and prove Matsumoto's
theorem"*); `TwFromMatsumoto` records it as the one hypothesis standing between this corpus and a
`T_w : W → H(M,q)`. This file proves it, **for every Coxeter system, with no hypothesis**.

## The proof, and where each ingredient came from

Tits' induction on length. Strip the last letter of each reduced word.

* Same last letter — strip it, apply the induction hypothesis, put it back. Needs only that braid
  moves survive appending (`braidEquiv_append`).
* Different last letters `s ≠ t` — then **both** are right descents, and
  `CoxeterDihedralDescent.exists_reduced_alternating_tail` produces a reduced word for `w` whose
  tail is the alternating block of length `M s t`, in both spellings, with a common prefix. One
  braid move connects them; each is then matched to the corresponding input word by the induction
  hypothesis, because they share a last letter.

The chain of inputs beneath that one step is the whole arc: exchange (`CoxeterReflectionCocycle`,
already in the corpus) → deletion (`CoxeterDeletion`) → rank-two structure (`CoxeterRankTwo`) →
the descent lemma (`CoxeterDihedralDescent`).

## Nothing here is hypothetical

Earlier versions of this file carried two hypotheses — `DihedralExact cs` (that `s_i s_j` has
order exactly `M i j`) and `M i j ≠ 0` (no infinite bonds) — and were hypothesis-free only on
type `A`. `QOU.Machinery.CoxeterDihedralOrder` proves both from the geometric representation, and
`CoxeterDihedralDescent` spends them there, so `matsumoto` and `exists_Tw` below hold for **every**
Coxeter system: `Bₙ`, `Dₙ`, `E₆₇₈`, `F₄`, `H₃`, `H₄`, every `I₂(m)`, and the infinite-bond ones too.

-- Ref: [matsumoto1964] DOI 10.1090/S0002-9904-1964-11211-9
-- Ref: [tits1969] Le problème des mots dans les groupes de Coxeter
-- Ref: [bjornerbrenti2005] Combinatorics of Coxeter Groups, Thm 3.3.1
-- Ref: [leitner2026] beans qou-06h7, qou-1u90
-/

namespace QOU.IwahoriHecke.Matsumoto

open CoxeterSystem List
open QOU.IwahoriHecke.BraidWord
open QOU.Machinery.CoxeterRankTwo QOU.Machinery.CoxeterDihedralDescent

variable {B : Type*}

/-! ## Braid-equivalence is a congruence for concatenation, and is symmetric -/

variable (Mf : B → B → ℕ)

theorem braidMove_append {u v : List B} (h : BraidMove Mf u v) (l : List B) :
    BraidMove Mf (u ++ l) (v ++ l) := by
  cases h with
  | move l₁ l₂ i j =>
    simpa [List.append_assoc] using BraidMove.move (M := Mf) l₁ (l₂ ++ l) i j

theorem braidEquiv_append {u v : List B} (h : BraidEquiv Mf u v) (l : List B) :
    BraidEquiv Mf (u ++ l) (v ++ l) := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih => exact ih.tail (braidMove_append Mf hstep l)

theorem braidEquiv_symm {u v : List B} (h : BraidEquiv Mf u v) : BraidEquiv Mf v u := by
  induction h with
  | refl => exact Relation.ReflTransGen.refl
  | tail _ hstep ih =>
    exact Relation.ReflTransGen.head (braidMove_symm Mf hstep) ih

/-! ## The alternating-word bridge

`BraidMove` is stated with the corpus's `altWord` (which **starts** with its first index) while the
Coxeter machinery uses Mathlib's `alternatingWord` (which **ends** with its second). The two agree
up to swapping the indices in the odd case, so the unordered pair of spellings is the same either
way — which is all a braid move needs. -/

theorem altWord_eq_alternatingWord (i j : B) :
    ∀ n : ℕ, altWord i j n = if Even n then alternatingWord i j n else alternatingWord j i n := by
  intro n
  induction n generalizing i j with
  | zero => rfl
  | succ n ih =>
    rw [altWord_succ, ih j i]
    by_cases hn : Even n
    · rw [if_pos hn, if_neg (by simp [Nat.even_add_one, hn]), alternatingWord_succ']
      simp [hn]
    · rw [if_neg hn, if_pos (by simp [Nat.even_add_one, hn]), alternatingWord_succ']
      simp [hn]

/-! ## Matsumoto -/

variable {W : Type*} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W)

local prefix:100 "ℓ" => cs.length
local prefix:100 "π" => cs.wordProd
local prefix:100 "σ" => cs.simple

private theorem exists_concat_of_length_pos {l : List B} (h : 0 < l.length) :
    ∃ l' a, l = l' ++ [a] := by
  induction l using List.reverseRecOn with
  | nil => simp at h
  | append_singleton l' a _ => exact ⟨l', a, rfl⟩

/-- Stripping the last letter of a reduced word gives a reduced word for the product times that
letter. -/
private theorem wordProd_dropLast {l : List B} {c : B} :
    π l = π (l ++ [c]) * σ c := by
  rw [cs.wordProd_append, cs.wordProd_singleton, mul_assoc, cs.simple_mul_simple_self, mul_one]

/-- **Matsumoto's theorem**, conditional on the rank-two order data.

Any two reduced words for the same element are related by a finite chain of braid moves. -/
theorem matsumoto :
    ∀ (n : ℕ) (u v : List B), u.length = n → cs.IsReduced u → cs.IsReduced v →
      π u = π v → BraidEquiv (fun a b => M a b) u v := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro u v hulen hured hvred huv
    have hvlen : v.length = n := by
      have h1 : ℓ (π u) = u.length := hured
      have h2 : ℓ (π v) = v.length := hvred
      rw [huv] at h1
      omega
    rcases Nat.eq_zero_or_pos n with hn | hn
    · have hu0 : u = [] := List.length_eq_zero_iff.mp (by omega)
      have hv0 : v = [] := List.length_eq_zero_iff.mp (by omega)
      rw [hu0, hv0]
    obtain ⟨u', s, rfl⟩ := exists_concat_of_length_pos (l := u) (by omega)
    obtain ⟨v', t, rfl⟩ := exists_concat_of_length_pos (l := v) (by omega)
    have hured' : cs.IsReduced u' := QOU.Machinery.CoxeterParabolic.isReduced_of_isReduced_concat cs hured
    have hvred' : cs.IsReduced v' := QOU.Machinery.CoxeterParabolic.isReduced_of_isReduced_concat cs hvred
    have hu'len : u'.length = n - 1 := by simp at hulen; omega
    have hv'len : v'.length = n - 1 := by simp at hvlen; omega
    by_cases hst : s = t
    · subst hst
      have hprod : π u' = π v' := by
        rw [wordProd_dropLast cs (l := u') (c := s), wordProd_dropLast cs (l := v') (c := s), huv]
      exact braidEquiv_append _ (ih (n - 1) (by omega) u' v' hu'len hured' hvred' hprod) [s]
    · -- Different last letters: both are right descents, so the dihedral tail exists.
      have hlenn : ℓ (π (u' ++ [s])) = n := by
        have h2 : ℓ (π (u' ++ [s])) = (u' ++ [s]).length := hured
        omega
      have hds : cs.IsRightDescent (π (u' ++ [s])) s := by
        show ℓ (π (u' ++ [s]) * σ s) < ℓ (π (u' ++ [s]))
        rw [← wordProd_dropLast cs (l := u') (c := s)]
        have h1 : ℓ (π u') = u'.length := hured'
        omega
      have hdt : cs.IsRightDescent (π (u' ++ [s])) t := by
        show ℓ (π (u' ++ [s]) * σ t) < ℓ (π (u' ++ [s]))
        rw [huv, ← wordProd_dropLast cs (l := v') (c := t)]
        have h1 : ℓ (π v') = v'.length := hvred'
        have h2 : ℓ (π (v' ++ [t])) = (v' ++ [t]).length := hvred
        omega
      obtain ⟨hmpos, l₁, hPred, hPprod, hQred, hQprod⟩ :=
        exists_reduced_alternating_tail cs hst hds hdt
      -- `m ≥ 1`, so each alternating tail has a last letter.
      obtain ⟨m', hm'⟩ : ∃ m', M s t = m' + 1 := ⟨M s t - 1, by omega⟩
      -- `P` ends in `t`, `Q` ends in `s`.
      set P : List B := l₁ ++ alternatingWord s t (M s t) with hP
      set Q : List B := l₁ ++ alternatingWord t s (M s t) with hQ
      have hPsplit : P = (l₁ ++ alternatingWord t s m') ++ [t] := by
        rw [hP, hm', alternatingWord_succ, List.concat_eq_append, List.append_assoc]
      have hQsplit : Q = (l₁ ++ alternatingWord s t m') ++ [s] := by
        rw [hQ, hm', alternatingWord_succ, List.concat_eq_append, List.append_assoc]
      -- One braid move connects `P` and `Q`.
      have hPQ : BraidEquiv (fun a b => M a b) Q P := by
        have hMts : M t s = M s t := M.symmetric t s
        have hmove : BraidMove (fun a b => M a b)
            (l₁ ++ altWord s t (M s t) ++ []) (l₁ ++ altWord t s (M t s) ++ []) :=
          BraidMove.move (M := fun a b => M a b) l₁ [] s t
        rw [List.append_nil, List.append_nil, hMts, altWord_eq_alternatingWord,
          altWord_eq_alternatingWord] at hmove
        by_cases he : Even (M s t)
        · rw [if_pos he, if_pos he] at hmove
          exact Relation.ReflTransGen.single (braidMove_symm _ hmove)
        · rw [if_neg he, if_neg he] at hmove
          exact Relation.ReflTransGen.single hmove
      -- Match `u` to `Q` (both end in `s`) and `v` to `P` (both end in `t`).
      have hQred2 : cs.IsReduced ((l₁ ++ alternatingWord s t m') ++ [s]) := by
        rw [← hQsplit]; exact hQred
      have hPred2 : cs.IsReduced ((l₁ ++ alternatingWord t s m') ++ [t]) := by
        rw [← hPsplit]; exact hPred
      have hQred' := QOU.Machinery.CoxeterParabolic.isReduced_of_isReduced_concat cs hQred2
      have hPred' := QOU.Machinery.CoxeterParabolic.isReduced_of_isReduced_concat cs hPred2
      have hlenQ : (l₁ ++ alternatingWord s t m').length = n - 1 := by
        have h1 : ℓ (π Q) = Q.length := hQred
        rw [hQprod, hlenn, hQsplit] at h1
        simp only [List.length_append, List.length_singleton] at h1 ⊢
        omega
      have hlenP : (l₁ ++ alternatingWord t s m').length = n - 1 := by
        have h1 : ℓ (π P) = P.length := hPred
        rw [hPprod, hlenn, hPsplit] at h1
        simp only [List.length_append, List.length_singleton] at h1 ⊢
        omega
      have huQ : BraidEquiv (fun a b => M a b) (u' ++ [s]) Q := by
        have hstep : BraidEquiv (fun a b => M a b) u' (l₁ ++ alternatingWord s t m') := by
          refine ih (n - 1) (by omega) u' _ hu'len hured' hQred' ?_
          have e1 : π u' = π (u' ++ [s]) * σ s := wordProd_dropLast cs
          have e2 : π (l₁ ++ alternatingWord s t m')
              = π ((l₁ ++ alternatingWord s t m') ++ [s]) * σ s := wordProd_dropLast cs
          rw [e1, e2, ← hQsplit, hQprod]
        have hfin2 := braidEquiv_append (fun a b => M a b) hstep [s]
        rwa [← hQsplit] at hfin2
      have hvP : BraidEquiv (fun a b => M a b) (v' ++ [t]) P := by
        have hstep : BraidEquiv (fun a b => M a b) v' (l₁ ++ alternatingWord t s m') := by
          refine ih (n - 1) (by omega) v' _ hv'len hvred' hPred' ?_
          have e1 : π v' = π (v' ++ [t]) * σ t := wordProd_dropLast cs
          have e2 : π (l₁ ++ alternatingWord t s m')
              = π ((l₁ ++ alternatingWord t s m') ++ [t]) * σ t := wordProd_dropLast cs
          rw [e1, e2, ← hPsplit, hPprod, huv]
        have hfin2 := braidEquiv_append (fun a b => M a b) hstep [t]
        rwa [← hPsplit] at hfin2
      exact (huQ.trans hPQ).trans (braidEquiv_symm _ hvP)

/-- The convenient form: no explicit length bookkeeping. -/
theorem matsumoto'
    {u v : List B} (hu : cs.IsReduced u) (hv : cs.IsReduced v) (huv : π u = π v) :
    BraidEquiv (fun a b => M a b) u v :=
  matsumoto cs u.length u v rfl hu hv huv

/-! ## The payoff: `T_w` exists -/

variable {R : Type*} [CommRing R] (q : R)

/-- **The `T_w` basis map exists**, for every Coxeter system, with no hypothesis.

`TwFromMatsumoto.exists_Tw_of_matsumoto` was stated conditionally on Matsumoto; the condition is
now discharged. `Tw` agrees with the word product on every reduced word, which is what a basis
indexed by `W` through reduced expressions means. -/
theorem exists_Tw :
    ∃ Tw : W → QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q (fun a b => M a b),
      ∀ l : List B, cs.IsReduced l →
        Tw (cs.wordProd l) = heckeWord q (fun a b => M a b) l :=
  QOU.IwahoriHecke.TwMatsumoto.exists_Tw_of_matsumoto cs q
    (fun _ _ hu hv huv => matsumoto' cs hu hv huv)

/-! ## Type `Aₙ`: a concrete instantiation

Nothing above is conditional any more, so this section is no longer discharging a hypothesis — it
names the type-`A` specialisation the rest of the corpus cites, and exhibits a group carrying it.
The two entry bounds are kept because they are the facts a reader checks when asking whether the
symmetric group is in scope. -/

theorem An_le_three (n : ℕ) (i j : Fin n) : (CoxeterMatrix.Aₙ n) i j ≤ 3 := by
  simp only [CoxeterMatrix.Aₙ, Matrix.of_apply]
  split_ifs <;> omega

theorem An_ne_zero (n : ℕ) (i j : Fin n) (h : i ≠ j) : (CoxeterMatrix.Aₙ n) i j ≠ 0 := by
  simp only [CoxeterMatrix.Aₙ, Matrix.of_apply, if_neg h]
  split_ifs <;> omega

/-- **Matsumoto's theorem for type `A`.** -/
theorem matsumoto_An {n : ℕ} {W : Type*} [Group W] (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W)
    {u v : List (Fin n)} (hu : cs.IsReduced u) (hv : cs.IsReduced v)
    (huv : cs.wordProd u = cs.wordProd v) :
    BraidEquiv (fun a b => (CoxeterMatrix.Aₙ n) a b) u v :=
  matsumoto' cs hu hv huv

/-- **The `T_w` basis map for the type-`A` Hecke algebra.**

This is the arc's target: `H_n(q)` for the symmetric group, with `T_w` defined on every element of
`W` and agreeing with the word product on every reduced word. -/
theorem exists_Tw_An {n : ℕ} {W : Type*} [Group W] (cs : CoxeterSystem (CoxeterMatrix.Aₙ n) W)
    {R : Type*} [CommRing R] (q : R) :
    ∃ Tw : W → QOU.MathlibExt.IwahoriHecke.HeckeAlgebra R q
        (fun a b => (CoxeterMatrix.Aₙ n) a b),
      ∀ l : List (Fin n), cs.IsReduced l →
        Tw (cs.wordProd l) = heckeWord q (fun a b => (CoxeterMatrix.Aₙ n) a b) l :=
  exists_Tw cs q

/-- A witness that the type-`A` statements are inhabited: Mathlib's presented group is a Coxeter
system of that type. So `matsumoto_An` and `exists_Tw_An` are statements about something. -/
example (n : ℕ) : CoxeterSystem (CoxeterMatrix.Aₙ n) (CoxeterMatrix.Aₙ n).Group :=
  CoxeterMatrix.toCoxeterSystem _

end QOU.IwahoriHecke.Matsumoto
