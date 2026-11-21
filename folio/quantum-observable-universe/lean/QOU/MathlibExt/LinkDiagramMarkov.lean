import QOU.MathlibExt.LinkDiagramStateSum
import Mathlib.Tactic.Abel

/-!
# Markov moves on braid closures

The easy direction of Markov's theorem at the level of link diagram codes: closures of braid words
related by a Markov move are Reidemeister equivalent.

**Conjugation** (`braidClosure_rotate`): the closures of `x :: w` and `w ++ [x]` are equivalent.
Relabelling the rows of the first closure (`rowRot`) moves the level of `x` to the bottom, just
after its closing arcs. The closing arcs carry one turn each, so the turns now sit on the edges
entering the level of `x`; `turnPast` moves them to the edges leaving it, which gives the second
closure. On the strands `x` does not touch this uses `merge` (`transferJoins`), on its two strands
`slide`. Together with the braid relations at word level this gives invariance under
`β ↦ σ β σ⁻¹`; those, and stabilisation, are not done here.

-- Ref: [kassel2008] Kassel–Turaev, "Braid Groups", GTM 247, §2.5 (closure and Markov moves)
-/

namespace QOU.MathlibExt.PL.Diagram

open Code

universe u

variable {E : Type u} [Fintype E] [DecidableEq E]

/-! ### Rearranging codes -/

omit [Fintype E] [DecidableEq E] in
theorem code_ext {D D' : Code E} (hx : D.xs = D'.xs) (hj : D.js = D'.js) : D = D' := by
  cases D; cases D'; simp_all

/-- Replace a code by an equal one on either side of a Reidemeister equivalence. -/
theorem ReidemeisterEquiv.of_eq {D₁ D₂ D₁' D₂' : Code E}
    (h : ReidemeisterEquiv ⟨E, D₁⟩ ⟨E, D₂⟩) (h₁ : D₁' = D₁) (h₂ : D₂ = D₂') :
    ReidemeisterEquiv ⟨E, D₁'⟩ ⟨E, D₂'⟩ := by
  subst h₁ h₂; exact h

omit [Fintype E] [DecidableEq E] in
theorem occurs_ofJs (js : Multiset (E × E × ℤ)) (e : E) :
    (Code.ofJs js).Occurs e ↔ ∃ j ∈ js, j.1 = e ∨ j.2.1 = e := by
  simp [Code.Occurs, Code.ofJs]

/-! ### Moving turns along a join -/

/-- **Turns move freely along a chain of two joins**: `(a, b, t), (b, c, t')` can be replaced by
`(a, b, t₁), (b, c, t₁')` when `t + t' = t₁ + t₁'`, if `b` occurs nowhere else. -/
theorem transferJoin (R : Code E) (a b c : E) (t t' t₁ t₁' : ℤ) (h : t + t' = t₁ + t₁')
    (hb : ¬ R.Occurs b) (hab : b ≠ a) (hcb : b ≠ c) :
    ReidemeisterEquiv ⟨E, R + Code.ofJs {(a, b, t), (b, c, t')}⟩
      ⟨E, R + Code.ofJs {(a, b, t₁), (b, c, t₁')}⟩ := by
  refine (ReidemeisterEquiv.of_move (Move.merge R a b c t t' hb hab hcb)).trans ?_
  rw [h]
  exact (ReidemeisterEquiv.of_move (Move.merge R a b c t₁ t₁' hb hab hcb)).symm

variable {P : Type*} [DecidableEq P]

/-- The joins `top p → mid p → bot p` with turns `t, t'`, over the positions `S`. -/
def chainJoins (top mid bot : P → E) (t t' : ℤ) (S : Finset P) : Multiset (E × E × ℤ) :=
  S.val.bind fun p => {(top p, mid p, t), (mid p, bot p, t')}

omit [Fintype E] [DecidableEq E] in
theorem chainJoins_insert (top mid bot : P → E) (t t' : ℤ) {S : Finset P} {p : P} (hp : p ∉ S) :
    chainJoins top mid bot t t' (insert p S) =
      {(top p, mid p, t), (mid p, bot p, t')} + chainJoins top mid bot t t' S := by
  rw [chainJoins, chainJoins, Finset.insert_val_of_notMem hp,
    Multiset.cons_bind]

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
theorem occurs_chainJoins (top mid bot : P → E) (t t' : ℤ) (S : Finset P) (e : E) :
    (Code.ofJs (chainJoins top mid bot t t' S)).Occurs e →
      ∃ p ∈ S, top p = e ∨ mid p = e ∨ bot p = e := by
  rw [occurs_ofJs]
  rintro ⟨j, hj, h⟩
  simp only [chainJoins, Multiset.mem_bind, Finset.mem_val, Multiset.insert_eq_cons,
    Multiset.mem_cons, Multiset.mem_singleton] at hj
  obtain ⟨p, hp, rfl | rfl⟩ := hj
  · exact ⟨p, hp, by tauto⟩
  · exact ⟨p, hp, by tauto⟩

/-- **Moving turns along many chains at once.** The middle edges must be distinct from each other
and from every top and bottom edge, and must not occur in `R`. -/
theorem transferJoins (top mid bot : P → E) (t t' t₁ t₁' : ℤ) (h : t + t' = t₁ + t₁')
    (hmid : Function.Injective mid) (htop : ∀ p q, mid p ≠ top q) (hbot : ∀ p q, mid p ≠ bot q)
    (S : Finset P) (R : Code E) (hR : ∀ p ∈ S, ¬ R.Occurs (mid p)) :
    ReidemeisterEquiv ⟨E, R + Code.ofJs (chainJoins top mid bot t t' S)⟩
      ⟨E, R + Code.ofJs (chainJoins top mid bot t₁ t₁' S)⟩ := by
  induction S using Finset.induction_on generalizing R with
  | empty => exact .refl _
  | @insert p S hp ih =>
    have hfresh : ∀ (u v : ℤ), ∀ q ∈ S,
        ¬ (Code.ofJs {(top p, mid p, u), (mid p, bot p, v)}).Occurs (mid q) := by
      intro u v q hq
      rw [occurs_ofJs_pair]
      have hpq : p ≠ q := fun h => hp (h ▸ hq)
      have := hmid.ne hpq
      have := htop q p
      have := hbot q p
      tauto
    -- First the positions in `S`, with the chain at `p` kept in the rest.
    have h₁ := ih (R + Code.ofJs {(top p, mid p, t), (mid p, bot p, t')}) fun q hq => by
      rw [occurs_add]
      exact not_or.2 ⟨hR q (Finset.mem_insert_of_mem hq), hfresh t t' q hq⟩
    -- Then the position `p`.
    have hp' : ¬ (R + Code.ofJs (chainJoins top mid bot t₁ t₁' S)).Occurs (mid p) := by
      rw [occurs_add]
      refine not_or.2 ⟨hR p (Finset.mem_insert_self p S), fun hoc => ?_⟩
      obtain ⟨q, hq, hq'⟩ := occurs_chainJoins top mid bot t₁ t₁' S _ hoc
      have hpq : p ≠ q := fun h => hp (h ▸ hq)
      rcases hq' with hq' | hq' | hq'
      · exact htop p q hq'.symm
      · exact hmid.ne hpq hq'.symm
      · exact hbot p q hq'.symm
    have h₂ := transferJoin (R + Code.ofJs (chainJoins top mid bot t₁ t₁' S)) (top p) (mid p)
      (bot p) t t' t₁ t₁' h hp' (htop p p) (hbot p p)
    have h₁' : ReidemeisterEquiv ⟨E, R + Code.ofJs (chainJoins top mid bot t t' (insert p S))⟩
        ⟨E, R + Code.ofJs (chainJoins top mid bot t₁ t₁' S) +
          Code.ofJs {(top p, mid p, t), (mid p, bot p, t')}⟩ := by
      refine h₁.of_eq ?_ ?_ <;> refine code_ext ?_ ?_ <;>
        simp only [ofJs, add_xs, add_js, chainJoins_insert top mid bot _ _ hp,
          Multiset.insert_eq_cons, ← Multiset.singleton_add, add_zero] <;> abel
    refine h₁'.trans (h₂.of_eq rfl ?_)
    refine code_ext ?_ ?_ <;>
      simp only [ofJs, add_xs, add_js, chainJoins_insert top mid bot _ _ hp,
        Multiset.insert_eq_cons, ← Multiset.singleton_add, add_zero] <;> abel

/-- **Moving one turn past a crossing.** On the left, every incoming edge of the crossing region
carries one turn: the two strands of the crossing on the joins `top u → mid o`, `top o → mid u`
(the two strands are exchanged by the relabelling of the closure), the strands in `S` on the joins
`top p → mid p`. On the right, the turn sits on the outgoing joins. -/
theorem turnPast (top mid bot : P → E) (hmid : Function.Injective mid)
    (htop : ∀ p q, mid p ≠ top q) (hbot : ∀ p q, mid p ≠ bot q)
    (u o : P) (huo : u ≠ o) (b : Bool) (S : Finset P) (hu : u ∉ S) (ho : o ∉ S)
    (R : Code E) (hR : ∀ p, ¬ R.Occurs (mid p)) :
    ReidemeisterEquiv
      ⟨E, R + (Code.ofXs {⟨mid o, bot o, mid u, bot u, b⟩} +
        Code.ofJs {(top u, mid o, 1), (top o, mid u, 1)} +
        Code.ofJs (chainJoins top mid bot 1 0 S))⟩
      ⟨E, R + (Code.ofXs {⟨top u, mid o, top o, mid u, b⟩} +
        Code.ofJs {(mid o, bot o, 1), (mid u, bot u, 1)} +
        Code.ofJs (chainJoins top mid bot 0 1 S))⟩ := by
  set X₁ : Code E := Code.ofXs {⟨mid o, bot o, mid u, bot u, b⟩} +
    Code.ofJs {(top u, mid o, 1), (top o, mid u, 1)}
  -- The strands not touched by the crossing.
  have h₁ := transferJoins top mid bot 1 0 0 1 (by norm_num) hmid htop hbot S (R + X₁)
    fun p hp => by
      rw [occurs_add]
      refine not_or.2 ⟨hR p, ?_⟩
      have hpu : p ≠ u := fun h => hu (h ▸ hp)
      have hpo : p ≠ o := fun h => ho (h ▸ hp)
      have := hmid.ne hpu
      have := hmid.ne hpo
      have := htop p u
      have := htop p o
      have := hbot p u
      have := hbot p o
      rw [occurs_add, occurs_ofJs_pair]
      simp only [Code.Occurs, Code.ofXs, Multiset.mem_singleton, exists_eq_left,
        Crossing.Mentions, Multiset.notMem_zero, false_and, exists_false, or_false]
      tauto
  -- The two strands of the crossing.
  have hfresh : ∀ x ∈ ({u, o} : Finset P),
      ¬ (R + Code.ofJs (chainJoins top mid bot 0 1 S)).Occurs (mid x) := by
    intro x hx
    rw [occurs_add]
    refine not_or.2 ⟨hR x, fun hoc => ?_⟩
    obtain ⟨q, hq, hq'⟩ := occurs_chainJoins top mid bot 0 1 S _ hoc
    have hxq : x ≠ q := by
      simp only [Finset.mem_insert, Finset.mem_singleton] at hx
      rintro rfl
      rcases hx with rfl | rfl <;> contradiction
    rcases hq' with hq' | hq' | hq'
    · exact htop x q hq'.symm
    · exact hmid.ne hxq hq'.symm
    · exact hbot x q hq'.symm
  have h₂ := ReidemeisterEquiv.of_move (Move.slide (R + Code.ofJs (chainJoins top mid bot 0 1 S))
    (top u) (bot o) (top o) (bot u) (mid o) (mid u) b 1 (hfresh o (by simp)) (hfresh u (by simp))
    (hmid.ne huo.symm) (by
      intro x hx
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hx
      rcases hx with rfl | rfl | rfl | rfl
      exacts [⟨(htop o u).symm, (htop u u).symm⟩, ⟨(hbot o o).symm, (hbot u o).symm⟩,
        ⟨(htop o o).symm, (htop u o).symm⟩, ⟨(hbot o u).symm, (hbot u u).symm⟩]))
  refine (h₁.of_eq ?_ rfl).trans (h₂.of_eq ?_ ?_)
  · refine code_ext ?_ ?_ <;> simp only [X₁, ofJs, ofXs, add_xs, add_js] <;> abel
  · refine code_ext ?_ ?_ <;> simp only [X₁, ofJs, ofXs, add_xs, add_js] <;> abel
  · refine code_ext ?_ ?_ <;> simp only [ofJs, ofXs, add_xs, add_js] <;> abel

/-! ### Splitting sums over `Fin` -/

section FinSplit

variable {α : Type*}

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
theorem univ_map_zero_succ {n : ℕ} (f : Fin (n + 1) → α) :
    (Finset.univ.val : Multiset (Fin (n + 1))).map f =
      f 0 ::ₘ (Finset.univ.val : Multiset (Fin n)).map fun j => f j.succ := by
  rw [Fin.univ_val_map, Fin.univ_val_map, List.ofFn_succ]
  rfl

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
theorem univ_map_castSucc_last {n : ℕ} (f : Fin (n + 1) → α) :
    (Finset.univ.val : Multiset (Fin (n + 1))).map f =
      (Finset.univ.val : Multiset (Fin n)).map (fun j => f j.castSucc) + {f (Fin.last n)} := by
  rw [Fin.univ_val_map, Fin.univ_val_map, List.ofFn_succ', List.concat_eq_append,
    ← Multiset.coe_add]
  rfl

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
theorem univ_bind_zero_succ {n : ℕ} (f : Fin (n + 1) → Multiset α) :
    (Finset.univ.val : Multiset (Fin (n + 1))).bind f =
      f 0 + (Finset.univ.val : Multiset (Fin n)).bind fun j => f j.succ := by
  rw [Multiset.bind, univ_map_zero_succ, Multiset.join_cons]
  rfl

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
theorem univ_bind_castSucc_last {n : ℕ} (f : Fin (n + 1) → Multiset α) :
    (Finset.univ.val : Multiset (Fin (n + 1))).bind f =
      (Finset.univ.val : Multiset (Fin n)).bind (fun j => f j.castSucc) + f (Fin.last n) := by
  rw [Multiset.bind, univ_map_castSucc_last, Multiset.join_add, Multiset.singleton_join]
  rfl

/-- The positions not touched by the letter `i`. -/
def untouched {m : ℕ} (i : Fin m) : Finset (Fin (m + 1)) :=
  Finset.univ.filter fun p => p ≠ i.castSucc ∧ p ≠ i.succ

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
theorem univ_map_untouched {m : ℕ} (i : Fin m) (f : Fin (m + 1) → α) :
    (Finset.univ.val : Multiset (Fin (m + 1))).map f =
      {f i.castSucc, f i.succ} + (untouched i).val.map f := by
  have hcs : i.castSucc ≠ i.succ := (Fin.castSucc_lt_succ i).ne
  have hrest : (Finset.univ.filter fun p : Fin (m + 1) => ¬ (p ≠ i.castSucc ∧ p ≠ i.succ)) =
      {i.castSucc, i.succ} := by
    ext p; simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert,
      Finset.mem_singleton]; tauto
  conv_lhs => rw [← Multiset.filter_add_not (fun p : Fin (m + 1) => p ≠ i.castSucc ∧ p ≠ i.succ)
    Finset.univ.val]
  rw [Multiset.map_add, add_comm, ← Finset.filter_val, ← Finset.filter_val, hrest,
    Finset.insert_val_of_notMem (by simpa using hcs)]
  simp [untouched]

end FinSplit

omit [Fintype E] [DecidableEq E] [DecidableEq P] in
/-- The joins of `chainJoins`, separated into the upper and the lower ones. -/
theorem chainJoins_eq (top mid bot : P → E) (t t' : ℤ) (S : Finset P) :
    chainJoins top mid bot t t' S =
      S.val.map (fun p => (top p, mid p, t)) + S.val.map (fun p => (mid p, bot p, t')) := by
  rw [chainJoins, ← Multiset.bind_singleton, ← Multiset.bind_singleton, ← Multiset.bind_add]
  rfl

/-! ### Merging chains of joins -/

/-- **Merging many chains at once**: `top p → mid p → bot p` becomes `top p → bot p`. -/
theorem mergeJoins (top mid bot : P → E) (t t' : ℤ)
    (hmid : Function.Injective mid) (htop : ∀ p q, mid p ≠ top q) (hbot : ∀ p q, mid p ≠ bot q)
    (S : Finset P) (R : Code E) (hR : ∀ p ∈ S, ¬ R.Occurs (mid p)) :
    ReidemeisterEquiv ⟨E, R + Code.ofJs (chainJoins top mid bot t t' S)⟩
      ⟨E, R + Code.ofJs (S.val.map fun p => (top p, bot p, t + t'))⟩ := by
  induction S using Finset.induction_on generalizing R with
  | empty => exact (ReidemeisterEquiv.refl _).of_eq rfl (by rfl)
  | @insert p S hp ih =>
    have h₁ := ih (R + Code.ofJs {(top p, mid p, t), (mid p, bot p, t')}) fun q hq => by
      rw [occurs_add, occurs_ofJs_pair]
      have hpq : p ≠ q := fun h => hp (h ▸ hq)
      have := hmid.ne hpq
      have := htop q p
      have := hbot q p
      have := hR q (Finset.mem_insert_of_mem hq)
      tauto
    have hp' : ¬ (R + Code.ofJs (S.val.map fun q => (top q, bot q, t + t'))).Occurs (mid p) := by
      rw [occurs_add, occurs_ofJs]
      refine not_or.2 ⟨hR p (Finset.mem_insert_self p S), ?_⟩
      rintro ⟨j, hj, h⟩
      obtain ⟨q, -, rfl⟩ := Multiset.mem_map.1 hj
      rcases h with h | h
      exacts [htop p q h.symm, hbot p q h.symm]
    have h₂ := ReidemeisterEquiv.of_move (Move.merge
      (R + Code.ofJs (S.val.map fun q => (top q, bot q, t + t'))) (top p) (mid p) (bot p) t t' hp'
      (htop p p) (hbot p p))
    have h₁' : ReidemeisterEquiv ⟨E, R + Code.ofJs (chainJoins top mid bot t t' (insert p S))⟩
        ⟨E, R + Code.ofJs (S.val.map fun q => (top q, bot q, t + t')) +
          Code.ofJs {(top p, mid p, t), (mid p, bot p, t')}⟩ := by
      refine h₁.of_eq ?_ ?_ <;> refine code_ext ?_ ?_ <;>
        simp only [ofJs, add_xs, add_js, chainJoins_insert top mid bot _ _ hp,
          Multiset.insert_eq_cons, ← Multiset.singleton_add, add_zero] <;> abel
    refine h₁'.trans (h₂.of_eq rfl ?_)
    refine code_ext ?_ ?_ <;>
      simp only [ofJs, add_xs, add_js, Finset.insert_val_of_notMem hp,
        ← Multiset.singleton_add, Multiset.map_add, Multiset.map_singleton, add_zero] <;> abel

omit [DecidableEq P] in
/-- The joins `e 0 → e 1 → ⋯ → e n`, without turns. -/
def chainOf {n : ℕ} (e : Fin (n + 1) → E) : Multiset (E × E × ℤ) :=
  (Finset.univ.val : Multiset (Fin n)).map fun j => (e j.castSucc, e j.succ, 0)

omit [Fintype E] [DecidableEq E] in
theorem occurs_chainOf {n : ℕ} (e : Fin (n + 1) → E) (x : E) :
    (Code.ofJs (chainOf e)).Occurs x → ∃ j, e j = x := by
  rw [occurs_ofJs]
  rintro ⟨_, hj, h⟩
  obtain ⟨j, -, rfl⟩ := Multiset.mem_map.1 hj
  rcases h with h | h
  exacts [⟨_, h⟩, ⟨_, h⟩]

/-- **Merging one long chain**: `a → e 0 → e 1 → ⋯ → e n` becomes `a → e n`, if the edges
`e 0, …, e (n - 1)` occur nowhere else. -/
theorem mergeChain (R : Code E) (a : E) (t : ℤ) :
    ∀ (n : ℕ) (e : Fin (n + 1) → E), Function.Injective e → (∀ j, e j ≠ a) →
      (∀ j : Fin n, ¬ R.Occurs (e j.castSucc)) →
      ReidemeisterEquiv ⟨E, R + Code.ofJs ({(a, e 0, t)} + chainOf e)⟩
        ⟨E, R + Code.ofJs {(a, e (Fin.last n), t)}⟩
  | 0, e, _, _, _ => (ReidemeisterEquiv.refl _).of_eq (by simp [chainOf]) rfl
  | n + 1, e, he, ha, hR => by
    have hrest : ¬ (R + Code.ofJs (chainOf fun k => e k.succ)).Occurs (e 0) := by
      rw [occurs_add]
      refine not_or.2 ⟨hR 0, fun h => ?_⟩
      obtain ⟨j, hj⟩ := occurs_chainOf _ _ h
      exact Fin.succ_ne_zero j (he hj)
    have h₁ := ReidemeisterEquiv.of_move (Move.merge (R + Code.ofJs (chainOf fun k => e k.succ))
      a (e 0) (e 1) t 0 hrest (ha 0) (he.ne (Fin.zero_ne_one)))
    have h₂ := mergeChain R a t n (fun k => e k.succ) (he.comp (Fin.succ_injective _))
      (fun j => ha _) (fun j => by
        show ¬ R.Occurs (e j.castSucc.succ)
        rw [Fin.succ_castSucc]
        exact hR j.succ)
    refine (h₁.of_eq ?_ (?_ : _ = R + Code.ofJs ({(a, e 1, t)} +
        chainOf fun k => e k.succ))).trans (h₂.of_eq (by simp) ?_)
    · refine code_ext ?_ ?_ <;> simp only [ofJs, add_xs, add_js, chainOf, univ_map_zero_succ,
        Multiset.insert_eq_cons, ← Multiset.singleton_add, add_zero]
      simp only [Fin.succ_zero_eq_one, Fin.castSucc_zero, Fin.succ_castSucc]
      abel
    · refine code_ext ?_ ?_ <;> simp only [ofJs, add_xs, add_js, add_zero]
      abel
    · simp [Fin.succ_last]

/-! ### Closures of words given as functions -/

/-- The closure of the braid word `g 0, g 1, …, g (n - 1)`. `braidClosure w` is `closureOf w.get`. -/
def closureOf {m n : ℕ} (g : Fin n → Fin m × Bool) : Code (Fin (n + 1) × Fin (m + 1)) where
  xs := (Finset.univ.val : Multiset (Fin n)).map fun k => letterCrossing k (g k).1 (g k).2
  js := (Finset.univ.val : Multiset (Fin n)).bind (fun k => letterJoins k (g k).1) +
    (Finset.univ.val : Multiset (Fin (m + 1))).map fun p => ((Fin.last _, p), (0, p), 1)

theorem braidClosure_eq_closureOf {m : ℕ} (w : List (Fin m × Bool)) :
    braidClosure w = closureOf w.get := rfl

/-- Closures of words that agree after identifying their lengths are equivalent. -/
theorem closureOf_congr {m n n' : ℕ} (h : n = n') (g : Fin n → Fin m × Bool)
    (g' : Fin n' → Fin m × Bool) (hg : ∀ k, g k = g' (Fin.cast h k)) :
    ReidemeisterEquiv ⟨_, closureOf g⟩ ⟨_, closureOf g'⟩ := by
  subst h
  obtain rfl : g = g' := funext fun k => by simpa using hg k
  exact .refl _

/-! ### Rotating the rows of a closure -/

section Rot

variable {Q : Type*}

/-- Move row `0` to the bottom and every other row up by one, permuting the positions of the row
that moves by `sw`. -/
def rowRot {n : ℕ} (sw : Equiv.Perm Q) : Fin (n + 1) × Q ≃ Fin (n + 1) × Q where
  toFun e := Fin.cases (Fin.last n, sw e.2) (fun j => (j.castSucc, e.2)) e.1
  invFun e := Fin.lastCases (0, sw.symm e.2) (fun j => (j.succ, e.2)) e.1
  left_inv := by
    rintro ⟨k, q⟩
    refine Fin.cases ?_ (fun j => ?_) k <;> simp
  right_inv := by
    rintro ⟨k, q⟩
    refine Fin.lastCases ?_ (fun j => ?_) k <;> simp

@[simp] theorem rowRot_zero {n : ℕ} (sw : Equiv.Perm Q) (q : Q) :
    rowRot (n := n) sw (0, q) = (Fin.last n, sw q) := rfl

@[simp] theorem rowRot_succ {n : ℕ} (sw : Equiv.Perm Q) (j : Fin n) (q : Q) :
    rowRot sw (j.succ, q) = (j.castSucc, q) := rfl

end Rot

section Letters

variable {m L : ℕ}

theorem letterCrossing_map_rowRot (sw : Equiv.Perm (Fin (m + 1))) (j : Fin L) (i : Fin m)
    (b : Bool) :
    (letterCrossing j.succ i b).map (rowRot sw) = letterCrossing j.castSucc i b := by
  cases b <;> simp [letterCrossing, Crossing.map]

theorem letterJoins_map_rowRot (sw : Equiv.Perm (Fin (m + 1))) (j : Fin L) (i : Fin m) :
    (letterJoins j.succ i).map (Prod.map (rowRot sw) (Prod.map (rowRot sw) id)) =
      letterJoins j.castSucc i := by
  simp [letterJoins, Multiset.map_map]

end Letters

/-! ### Conjugation -/

section Conj

variable {m L : ℕ}

/-- The part of a closure coming from the letters of `g`, placed at the first `L` levels of
`L + 1`. -/
def wordPart (g : Fin L → Fin m × Bool) : Code (Fin (L + 1 + 1) × Fin (m + 1)) where
  xs := (Finset.univ.val : Multiset (Fin L)).map fun j => letterCrossing j.castSucc (g j).1 (g j).2
  js := (Finset.univ.val : Multiset (Fin L)).bind fun j => letterJoins j.castSucc (g j).1

theorem wordPart_not_occurs (g : Fin L → Fin m × Bool) (p : Fin (m + 1)) :
    ¬ (wordPart g).Occurs (Fin.last (L + 1), p) := by
  have h1 : ∀ j : Fin L, (j.castSucc.castSucc : Fin (L + 1 + 1)) ≠ Fin.last (L + 1) := by
    intro j h; have := congrArg Fin.val h; simp at this; omega
  have h2 : ∀ j : Fin L, (j.castSucc.succ : Fin (L + 1 + 1)) ≠ Fin.last (L + 1) := by
    intro j h; have := congrArg Fin.val h; simp at this; omega
  simp only [Code.Occurs, wordPart, Multiset.mem_map, Multiset.mem_bind, Finset.mem_val,
    Finset.mem_univ, true_and, not_or, not_exists, not_and]
  constructor
  · rintro _ ⟨j, rfl⟩
    obtain ⟨i, b⟩ := g j
    cases b <;> simp [letterCrossing, Crossing.Mentions, h1, h2]
  · rintro _ ⟨j, hj⟩
    simp only [letterJoins, Multiset.mem_map, Finset.mem_val] at hj
    obtain ⟨q, -, rfl⟩ := hj
    simp [h1, h2]

/-- Edges of the closure on `L + 1` levels: the row above the last level, the bottom row, and the
top row. -/
abbrev topE (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1) × Fin (m + 1) := ((Fin.last L).castSucc, p)
abbrev midE (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1) × Fin (m + 1) := (Fin.last (L + 1), p)
abbrev botE (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1) × Fin (m + 1) := (0, p)

/-- The position the under strand of the letter `(i, b)` enters at. -/
def uPos (i : Fin m) (b : Bool) : Fin (m + 1) := if b then i.succ else i.castSucc
/-- The position the over strand of the letter `(i, b)` enters at. -/
def oPos (i : Fin m) (b : Bool) : Fin (m + 1) := if b then i.castSucc else i.succ

theorem letterCrossing_last (i : Fin m) (b : Bool) :
    letterCrossing (Fin.last L) i b =
      ⟨topE L (uPos i b), midE L (oPos i b), topE L (oPos i b), midE L (uPos i b), b⟩ := by
  cases b <;> simp [letterCrossing, uPos, oPos]

/-- The closure with the letter `(i, b)` last, split into the word part and the last level. -/
theorem closureOf_snoc_eq (g : Fin L → Fin m × Bool) (i : Fin m) (b : Bool) :
    closureOf (Fin.snoc g (i, b) : Fin (L + 1) → Fin m × Bool) =
      wordPart g + (Code.ofXs {letterCrossing (Fin.last L) i b} +
        Code.ofJs {(midE L (oPos i b), botE L (oPos i b), 1),
          (midE L (uPos i b), botE L (uPos i b), 1)} +
        Code.ofJs (chainJoins (topE L) (midE L) (botE L) 0 1 (untouched i))) := by
  refine code_ext ?_ ?_
  · simp only [closureOf, wordPart, ofXs, ofJs, add_xs, add_zero]
    rw [univ_map_castSucc_last]
    simp
  · simp only [closureOf, wordPart, ofXs, ofJs, add_js, zero_add]
    rw [univ_bind_castSucc_last, univ_map_untouched, chainJoins_eq]
    simp only [Fin.snoc_castSucc, Fin.snoc_last, letterJoins, untouched, Fin.succ_last]
    cases b <;> simp only [uPos, oPos, Multiset.insert_eq_cons, ← Multiset.singleton_add,
      if_true, if_false, Bool.false_eq_true] <;> abel

theorem swap_untouched (i : Fin m) {p : Fin (m + 1)} (hp : p ∈ (untouched i).val) :
    Equiv.swap i.castSucc i.succ p = p := by
  simp only [untouched, Finset.mem_val, Finset.mem_filter, Finset.mem_univ, true_and] at hp
  exact Equiv.swap_apply_of_ne_of_ne hp.1 hp.2

theorem letterJoins_zero_map (i : Fin m) :
    (letterJoins (0 : Fin (L + 1)) i).map
        (Prod.map (rowRot (Equiv.swap i.castSucc i.succ))
          (Prod.map (rowRot (Equiv.swap i.castSucc i.succ)) id)) =
      (untouched i).val.map fun p => (midE L p, botE L p, 0) := by
  rw [letterJoins, Multiset.map_map]
  refine Multiset.map_congr rfl fun p hp => ?_
  have := swap_untouched i hp
  simp only [Function.comp_apply, Prod.map, id]
  rw [show ((0 : Fin (L + 1)).castSucc : Fin (L + 1 + 1)) = 0 from rfl, rowRot_zero, rowRot_succ,
    this]
  rfl

theorem closingArc_map (i : Fin m) (p : Fin (m + 1)) :
    Prod.map (rowRot (Equiv.swap i.castSucc i.succ))
        (Prod.map (rowRot (Equiv.swap i.castSucc i.succ)) id)
        ((Fin.last (L + 1), p), ((0 : Fin (L + 1 + 1)), p), (1 : ℤ)) =
      (topE L p, midE L (Equiv.swap i.castSucc i.succ p), 1) := by
  simp only [Prod.map, id]
  rw [← Fin.succ_last, rowRot_succ, rowRot_zero]

theorem letterCrossing_zero_map (i : Fin m) (b : Bool) :
    (letterCrossing (0 : Fin (L + 1)) i b).map (rowRot (Equiv.swap i.castSucc i.succ)) =
      ⟨midE L (oPos i b), botE L (oPos i b), midE L (uPos i b), botE L (uPos i b), b⟩ := by
  have h1 : ((0 : Fin (L + 1)).succ, i.succ) = ((0 : Fin (L + 1)).succ, i.succ) := rfl
  cases b <;> simp only [letterCrossing, Crossing.map, uPos, oPos] <;>
    simp [-Fin.succ_zero_eq_one, -Fin.succ_zero_eq_one']

/-- The closure with the letter `(i, b)` first, with its rows rotated so that the first level
becomes the last. -/
theorem closureOf_cons_map (g : Fin L → Fin m × Bool) (i : Fin m) (b : Bool) :
    (closureOf (Fin.cons (i, b) g : Fin (L + 1) → Fin m × Bool)).map
        (rowRot (Equiv.swap i.castSucc i.succ)) =
      wordPart g + (Code.ofXs
          {⟨midE L (oPos i b), botE L (oPos i b), midE L (uPos i b), botE L (uPos i b), b⟩} +
        Code.ofJs {(topE L (uPos i b), midE L (oPos i b), 1),
          (topE L (oPos i b), midE L (uPos i b), 1)} +
        Code.ofJs (chainJoins (topE L) (midE L) (botE L) 1 0 (untouched i))) := by
  refine code_ext ?_ ?_
  · simp only [Code.map, closureOf, wordPart, ofXs, ofJs, add_xs, add_zero]
    rw [univ_map_zero_succ]
    simp only [Fin.cons_zero, Fin.cons_succ, Multiset.map_cons, Multiset.map_map,
      Function.comp_def, letterCrossing_map_rowRot, letterCrossing_zero_map]
    rw [← Multiset.singleton_add]
    exact add_comm _ _
  · simp only [Code.map, closureOf, wordPart, ofXs, ofJs, add_js, zero_add, Multiset.map_add]
    rw [univ_bind_zero_succ, chainJoins_eq, Multiset.map_add, Multiset.map_bind, Multiset.map_map,
      univ_map_untouched i]
    have hS : (untouched i).val.map
          (fun p => (topE L p, midE L (Equiv.swap i.castSucc i.succ p), (1 : ℤ))) =
        (untouched i).val.map fun p => (topE L p, midE L p, 1) :=
      Multiset.map_congr rfl fun p hp => by rw [swap_untouched i hp]
    simp only [Fin.cons_zero, Fin.cons_succ, letterJoins_map_rowRot, letterJoins_zero_map,
      Function.comp_def, closingArc_map, Equiv.swap_apply_left, Equiv.swap_apply_right, hS]
    cases b <;> simp only [uPos, oPos, Multiset.insert_eq_cons, ← Multiset.singleton_add,
      if_true, if_false, Bool.false_eq_true] <;> abel

/-- **Conjugation, one letter.** Moving the first letter of a braid word to the end does not change
the closure up to Reidemeister equivalence. -/
theorem closureOf_cons_equiv_snoc (g : Fin L → Fin m × Bool) (i : Fin m) (b : Bool) :
    ReidemeisterEquiv ⟨_, closureOf (Fin.cons (i, b) g : Fin (L + 1) → Fin m × Bool)⟩
      ⟨_, closureOf (Fin.snoc g (i, b) : Fin (L + 1) → Fin m × Bool)⟩ := by
  have hcs : i.castSucc ≠ i.succ := (Fin.castSucc_lt_succ i).ne
  have hmid : Function.Injective (midE (m := m) L) := fun p q h => (Prod.mk.inj h).2
  have hrow : (Fin.last (L + 1) : Fin (L + 1 + 1)) ≠ (Fin.last L).castSucc :=
    (Fin.castSucc_lt_last _).ne'
  have htop : ∀ p q : Fin (m + 1), midE L p ≠ topE L q := fun p q h => hrow (Prod.mk.inj h).1
  have hbot : ∀ p q : Fin (m + 1), midE L p ≠ botE L q := fun p q h =>
    Fin.last_pos.ne' (Prod.mk.inj h).1
  have huo : uPos i b ≠ oPos i b := by cases b <;> simp [uPos, oPos, hcs, hcs.symm]
  have hu : uPos i b ∉ untouched i := by cases b <;> simp [uPos, untouched]
  have ho : oPos i b ∉ untouched i := by cases b <;> simp [oPos, untouched]
  refine (ReidemeisterEquiv.of_equiv (rowRot (Equiv.swap i.castSucc i.succ)) _).trans ?_
  rw [closureOf_cons_map, closureOf_snoc_eq, letterCrossing_last]
  exact turnPast (topE L) (midE L) (botE L) hmid htop hbot (uPos i b) (oPos i b) huo b
    (untouched i) hu ho (wordPart g) (wordPart_not_occurs g)

/-- **Conjugation (cyclic rotation).** The closures of `x :: w` and `w ++ [x]` are Reidemeister
equivalent. -/
theorem braidClosure_rotate (x : Fin m × Bool) (w : List (Fin m × Bool)) :
    ReidemeisterEquiv ⟨_, braidClosure (x :: w)⟩ ⟨_, braidClosure (w ++ [x])⟩ := by
  obtain ⟨i, b⟩ := x
  have h₁ := closureOf_congr (m := m) (rfl : ((i, b) :: w).length = w.length + 1) ((i, b) :: w).get
    (Fin.cons (i, b) w.get) fun k => by
      refine Fin.cases ?_ (fun j => ?_) k <;> simp
  have h₂ := closureOf_congr (m := m) (by simp : w.length + 1 = (w ++ [(i, b)]).length)
    (Fin.snoc w.get (i, b)) (w ++ [(i, b)]).get fun k => by
      refine Fin.lastCases ?_ (fun j => ?_) k
      · simp
      · simp [List.getElem_append_left]
  rw [braidClosure_eq_closureOf, braidClosure_eq_closureOf]
  exact h₁.trans ((closureOf_cons_equiv_snoc w.get i b).trans h₂)

end Conj

/-! ### Stabilisation -/

section Stab

variable {m L : ℕ}

/-- The crossings and pass-through joins of the closure of `g`, without the closing arcs. -/
def wordCode (g : Fin L → Fin m × Bool) : Code (Fin (L + 1) × Fin (m + 1)) where
  xs := (Finset.univ.val : Multiset (Fin L)).map fun k => letterCrossing k (g k).1 (g k).2
  js := (Finset.univ.val : Multiset (Fin L)).bind fun k => letterJoins k (g k).1

/-- Include a closure on `m + 1` strands and `L` levels into one with an extra strand and an extra
level. -/
def stabEmb : Fin (L + 1) × Fin (m + 1) ↪ Fin (L + 1 + 1) × Fin (m + 1 + 1) :=
  ⟨fun e => (e.1.castSucc, e.2.castSucc), fun e e' h => by
    simp only [Prod.mk.injEq, Fin.castSucc_inj] at h; exact Prod.ext h.1 h.2⟩

/-- The word `g` read on `m + 2` strands. -/
def liftWord (g : Fin L → Fin m × Bool) : Fin L → Fin (m + 1) × Bool :=
  fun j => ((g j).1.castSucc, (g j).2)

@[simp] theorem stabEmb_apply (e : Fin (L + 1) × Fin (m + 1)) :
    (stabEmb e : Fin (L + 1 + 1) × Fin (m + 1 + 1)) = (e.1.castSucc, e.2.castSucc) := rfl

theorem untouched_castSucc (i : Fin m) :
    untouched i.castSucc = insert (Fin.last (m + 1)) ((untouched i).map Fin.castSuccEmb) := by
  ext p
  refine Fin.lastCases ?_ (fun q => ?_) p
  · simp only [untouched, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert,
      true_or, iff_true]
    exact ⟨(Fin.castSucc_lt_last _).ne', by
      rw [Fin.succ_castSucc]; exact (Fin.castSucc_lt_last _).ne'⟩
  · simp only [untouched, Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_insert,
      Finset.mem_map, Fin.castSuccEmb_apply, Fin.castSucc_inj, (Fin.castSucc_lt_last q).ne,
      false_or, exists_eq_right]
    rw [Fin.succ_castSucc]
    simp only [ne_eq, Fin.castSucc_inj]

theorem letterCrossing_stab (j : Fin L) (i : Fin m) (b : Bool) :
    (letterCrossing j i b).map stabEmb = letterCrossing j.castSucc i.castSucc b := by
  cases b <;> simp only [letterCrossing, Crossing.map, stabEmb_apply, Fin.succ_castSucc] <;> rfl

theorem letterJoins_stab (j : Fin L) (i : Fin m) :
    letterJoins j.castSucc i.castSucc =
      {((j.castSucc.castSucc, Fin.last (m + 1)), (j.succ.castSucc, Fin.last (m + 1)), 0)} +
      (letterJoins j i).map (Prod.map stabEmb (Prod.map stabEmb id)) := by
  rw [letterJoins, letterJoins, ← untouched, ← untouched, untouched_castSucc,
    Finset.insert_val_of_notMem (by simp),
    Multiset.map_cons, Finset.map_val, Multiset.map_map, Multiset.map_map,
    ← Multiset.singleton_add, Fin.succ_castSucc]
  rfl

theorem wordPart_liftWord (g : Fin L → Fin m × Bool) :
    wordPart (liftWord g) = (wordCode g).map stabEmb +
      Code.ofJs (chainOf fun r : Fin (L + 1) => (r.castSucc, Fin.last (m + 1))) := by
  refine code_ext ?_ ?_
  · simp only [wordPart, wordCode, Code.map, liftWord, Code.ofJs, add_xs, add_zero,
      Multiset.map_map, Function.comp_def, letterCrossing_stab]
  · simp only [wordPart, wordCode, Code.map, liftWord, Code.ofJs, add_js, chainOf,
      Multiset.map_bind, letterJoins_stab]
    rw [Multiset.bind_add, Multiset.bind_singleton]
    exact add_comm _ _

theorem castSuccEmb_univ_eq :
    (Finset.univ.map Fin.castSuccEmb : Finset (Fin (m + 1 + 1))) =
      insert (Fin.last m).castSucc (untouched (Fin.last m)) := by
  ext p
  refine Fin.lastCases ?_ (fun q => ?_) p
  · simp only [Finset.mem_map, Finset.mem_univ, Fin.castSuccEmb_apply, true_and, untouched,
      Finset.mem_insert, Finset.mem_filter, Fin.succ_last, ne_eq, not_true_eq_false, and_false,
      or_false]
    constructor
    · rintro ⟨x, hx⟩; exact absurd hx (Fin.castSucc_lt_last x).ne
    · intro h; exact absurd h.symm (Fin.castSucc_lt_last _).ne
  · have hq : q.castSucc ∈ (Finset.univ.map Fin.castSuccEmb : Finset (Fin (m + 1 + 1))) :=
      Finset.mem_map_of_mem _ (Finset.mem_univ q)
    simp only [hq, true_iff, Finset.mem_insert, untouched, Finset.mem_filter, Finset.mem_univ,
      true_and, Fin.succ_last]
    by_cases h : q = Fin.last m
    · exact Or.inl (by rw [h])
    · exact Or.inr ⟨fun h' => h (Fin.castSucc_inj.1 h'), (Fin.castSucc_lt_last q).ne⟩

theorem kink_stab (b : Bool) :
    kink (topE L (Fin.last m).castSucc) (midE L (Fin.last m).castSucc)
        (midE L (Fin.last (m + 1))) (topE L (Fin.last (m + 1))) (!b) b =
      letterCrossing (Fin.last L) (Fin.last m) b := by
  rw [letterCrossing_last]
  cases b <;> simp [kink, uPos, oPos, Fin.succ_last]

/-- **Stabilisation.** Adding a strand and closing it with `σₘ^{±1}` does not change the closure up
to Reidemeister equivalence. -/
theorem closureOf_stab (g : Fin L → Fin m × Bool) (b : Bool) :
    ReidemeisterEquiv ⟨_, closureOf g⟩
      ⟨_, closureOf (Fin.snoc (liftWord g) (Fin.last m, b) : Fin (L + 1) → Fin (m + 1) × Bool)⟩ := by
  set W := (wordCode g).map stabEmb with hWdef
  set m' : Fin (m + 1 + 1) := (Fin.last m).castSucc with hm'
  set M : Fin (m + 1 + 1) := Fin.last (m + 1) with hM
  set U := untouched (Fin.last m) with hU
  have hmM : m' ≠ M := (Fin.castSucc_lt_last _).ne
  have hW : ∀ e, W.Occurs e → ∃ (k : Fin (L + 1)) (p : Fin (m + 1)), e = (k.castSucc, p.castSucc) := by
    intro e he
    obtain ⟨x, -, rfl⟩ := (occurs_map _ _ _).1 he
    exact ⟨x.1, x.2, rfl⟩
  have hWM : ∀ e, W.Occurs e → e.2 ≠ M := by
    intro e he
    obtain ⟨k, p, rfl⟩ := hW e he
    exact (Fin.castSucc_lt_last p).ne
  have hUM : ∀ p ∈ U, p ≠ M := by
    intro p hp
    simp only [hU, untouched, Finset.mem_filter, Finset.mem_univ, true_and, Fin.succ_last] at hp
    exact hp.2
  have hcU : ∀ e, (Code.ofJs (chainJoins (topE L) (midE L) (botE L) 0 1 U)).Occurs e → e.2 ≠ M := by
    intro e he
    obtain ⟨p, hp, h⟩ := occurs_chainJoins _ _ _ _ _ _ _ he
    rcases h with rfl | rfl | rfl <;> exact hUM p hp
  have hmid : Function.Injective (midE (m := m + 1) L) := fun p q h => (Prod.mk.inj h).2
  have hrow : (Fin.last (L + 1) : Fin (L + 1 + 1)) ≠ (Fin.last L).castSucc :=
    (Fin.castSucc_lt_last _).ne'
  have htop : ∀ p q : Fin (m + 1 + 1), midE L p ≠ topE L q := fun p q h => hrow (Prod.mk.inj h).1
  have hbot : ∀ p q : Fin (m + 1 + 1), midE L p ≠ botE L q := fun p q h =>
    Fin.last_pos.ne' (Prod.mk.inj h).1
  -- Step 1: embed.
  have hc : (closureOf g).map stabEmb = W + Code.ofJs
      ((Finset.univ.map Fin.castSuccEmb : Finset (Fin (m + 1 + 1))).val.map
        fun p => (topE L p, botE L p, (0 : ℤ) + 1)) := by
    refine code_ext ?_ ?_
    · simp [closureOf, wordCode, hWdef, Code.map, Code.ofJs]
    · simp only [closureOf, wordCode, hWdef, Code.map, Code.ofJs, add_js, Multiset.map_add,
        Finset.map_val, Multiset.map_map]
      congr 1
  have h1 := ReidemeisterEquiv.of_move (Move.embed stabEmb (closureOf g))
  rw [hc] at h1
  -- Step 2: split the closing arcs at the middle row.
  have h2 := (mergeJoins (topE L) (midE L) (botE L) 0 1 hmid htop hbot
    (Finset.univ.map Fin.castSuccEmb) W fun p _ h => by
      obtain ⟨k, q, hk⟩ := hW _ h
      exact (Fin.castSucc_lt_last k).ne' (Prod.mk.inj hk).1).symm
  rw [castSuccEmb_univ_eq, chainJoins_insert _ _ _ _ _ (by
    simp [hU, untouched, Fin.succ_last])] at h2
  -- Step 3: a kink on strand `m'`.
  set R1 := W + Code.ofJs {(midE L m', botE L m', (1 : ℤ))} +
    Code.ofJs (chainJoins (topE L) (midE L) (botE L) 0 1 U) with hR1
  have hR1M : ∀ e, R1.Occurs e → e.2 ≠ M := by
    intro e he
    simp only [hR1, occurs_add, occurs_ofJs_single] at he
    rcases he with (h | rfl | rfl) | h
    exacts [hWM e h, hmM, hmM, hcU e h]
  have h3 := ReidemeisterEquiv.of_move (Move.r1 R1 (topE L m') (midE L m') (midE L M) (topE L M)
    (!b) b (fun h => hR1M _ h rfl) (fun h => hR1M _ h rfl) (fun h => hrow (Prod.mk.inj h).1)
    (by
      intro x hx
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hx
      rcases hx with rfl | rfl <;>
        exact ⟨fun h => hmM (Prod.mk.inj h).2, fun h => hmM (Prod.mk.inj h).2⟩))
  -- Step 4: the new strand `M` becomes a chain through every level.
  set eM : Fin (L + 1) → Fin (L + 1 + 1) × Fin (m + 1 + 1) := fun r => (r.castSucc, M) with heM
  set R2 := W + Code.ofXs {kink (topE L m') (midE L m') (midE L M) (topE L M) (!b) b} +
    Code.ofJs {(midE L m', botE L m', (1 : ℤ))} +
    Code.ofJs (chainJoins (topE L) (midE L) (botE L) 0 1 U) with hR2
  have h4 := (mergeChain R2 (midE L M) 1 L eM
    (fun r s h => Fin.castSucc_inj.1 (Prod.mk.inj h).1)
    (fun j h => (Fin.castSucc_lt_last j).ne (Prod.mk.inj h).1)
    (fun j h => by
      simp only [hR2, occurs_add, occurs_ofJs_single, occurs_ofXs_kink] at h
      rcases h with ((h | (h | h) | (h | h)) | (h | h)) | h
      · exact hWM _ h rfl
      · exact hmM (Prod.mk.inj h).2
      · exact hmM (Prod.mk.inj h).2
      · exact (Fin.castSucc_lt_last _).ne (Prod.mk.inj h).1.symm
      · exact (Fin.castSucc_lt_last j).ne (Fin.castSucc_inj.1 (Prod.mk.inj h).1.symm)
      · exact hmM (Prod.mk.inj h).2
      · exact hmM (Prod.mk.inj h).2
      · exact hcU _ h rfl)).symm
  rw [castSuccEmb_univ_eq] at h1
  refine (h1.trans h2).trans ((h3.of_eq ?_
    (?_ : _ = R2 + Code.ofJs {(midE L M, eM (Fin.last L), (1 : ℤ))})).trans (h4.of_eq rfl ?_))
  · refine code_ext ?_ ?_ <;>
      simp only [hR1, ofJs, ofXs, add_xs, add_js, Multiset.insert_eq_cons,
        ← Multiset.singleton_add, add_zero, zero_add] <;> abel
  · have hk : kinkTurn (!b) b = 1 := by cases b <;> rfl
    rw [hk]
    refine code_ext ?_ ?_ <;>
      simp only [hR1, hR2, ofJs, ofXs, add_xs, add_js, Multiset.insert_eq_cons,
        ← Multiset.singleton_add, add_zero, zero_add] <;> abel
  · rw [closureOf_snoc_eq, wordPart_liftWord, ← kink_stab]
    cases b <;> refine code_ext ?_ ?_ <;>
      simp only [hR2, hWdef, hm', hM, hU, heM, ofJs, ofXs, add_xs, add_js,
        Multiset.insert_eq_cons, uPos, oPos, Fin.succ_last, Fin.castSucc_zero, Nat.succ_eq_add_one, if_true, if_false, Bool.false_eq_true, Bool.not_true, Bool.not_false,
        ← Multiset.singleton_add, add_zero, zero_add] <;> abel

/-- **Stabilisation (braid words).** The closure of `w` on `m + 1` strands is Reidemeister
equivalent to the closure, on `m + 2` strands, of `w` followed by `σₘ^{±1}`. -/
theorem braidClosure_stab (w : List (Fin m × Bool)) (b : Bool) :
    ReidemeisterEquiv ⟨_, braidClosure w⟩
      ⟨_, braidClosure (w.map (fun x => (x.1.castSucc, x.2)) ++ [(Fin.last m, b)])⟩ := by
  have h₂ := closureOf_congr (m := m + 1)
    (by simp : w.length + 1 = (w.map (fun x => (x.1.castSucc, x.2)) ++ [(Fin.last m, b)]).length)
    (Fin.snoc (liftWord w.get) (Fin.last m, b))
    (w.map (fun x => (x.1.castSucc, x.2)) ++ [(Fin.last m, b)]).get fun k => by
      refine Fin.lastCases ?_ (fun j => ?_) k
      · simp
      · simp [liftWord, List.getElem_append_left]
  rw [braidClosure_eq_closureOf, braidClosure_eq_closureOf]
  exact (closureOf_stab w.get b).trans h₂


end Stab

/-! ### Cancelling a letter against its inverse -/

section Cancel

variable {m L : ℕ}

/-- Include the rows of a closure with `L` levels into one with `L + 2` levels. -/
def rowEmb2 : Fin (L + 1) × Fin (m + 1) ↪ Fin (L + 1 + 1 + 1) × Fin (m + 1) :=
  ⟨fun e => (e.1.castSucc.castSucc, e.2), fun e e' h => by
    simp only [Prod.mk.injEq, Fin.castSucc_inj] at h; exact Prod.ext h.1 h.2⟩

@[simp] theorem rowEmb2_apply (e : Fin (L + 1) × Fin (m + 1)) :
    (rowEmb2 e : Fin (L + 1 + 1 + 1) × Fin (m + 1)) = (e.1.castSucc.castSucc, e.2) := rfl

theorem letterCrossing_row2 (k : Fin L) (i : Fin m) (b : Bool) :
    (letterCrossing k i b).map rowEmb2 = letterCrossing k.castSucc.castSucc i b := by
  cases b <;> simp only [letterCrossing, Crossing.map, rowEmb2_apply, Fin.succ_castSucc] <;> rfl

theorem letterJoins_row2 (k : Fin L) (i : Fin m) :
    (letterJoins k i).map (Prod.map rowEmb2 (Prod.map rowEmb2 id)) =
      letterJoins k.castSucc.castSucc i := by
  rw [letterJoins, letterJoins, Multiset.map_map]
  refine Multiset.map_congr rfl fun p _ => ?_
  simp only [Function.comp_apply, Prod.map, rowEmb2_apply, id, Fin.succ_castSucc]

/-- The rows of the last two levels. -/
abbrev rowA (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1 + 1) × Fin (m + 1) :=
  ((Fin.last L).castSucc.castSucc, p)
abbrev rowB (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1 + 1) × Fin (m + 1) :=
  ((Fin.last (L + 1)).castSucc, p)
abbrev rowC (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1 + 1) × Fin (m + 1) := (Fin.last (L + 1 + 1), p)
abbrev rowZ (L : ℕ) (p : Fin (m + 1)) : Fin (L + 1 + 1 + 1) × Fin (m + 1) := (0, p)

theorem letterCrossing_pair (i : Fin m) (b : Bool) :
    ({letterCrossing (Fin.last L).castSucc i b, letterCrossing (Fin.last (L + 1)) i (!b)} :
        Multiset (Crossing (Fin (L + 1 + 1 + 1) × Fin (m + 1)))) =
      bigonPar (rowA L (oPos i b)) (rowC L (oPos i b)) (rowA L (uPos i b)) (rowC L (uPos i b))
        (rowB L (uPos i b)) (rowB L (oPos i b)) b := by
  cases b <;> simp [letterCrossing, bigonPar, uPos, oPos, Fin.succ_castSucc, Fin.succ_last]

/-- The closure of a word ending in `(i, b), (i, !b)`, written out. -/
theorem closureOf_snoc_snoc_eq (g : Fin L → Fin m × Bool) (i : Fin m) (b : Bool) :
    closureOf (Fin.snoc (Fin.snoc g (i, b)) (i, !b) : Fin (L + 1 + 1) → Fin m × Bool) =
      (wordCode g).map rowEmb2 + Code.ofJs ((Finset.univ.val : Multiset (Fin (m + 1))).map
        fun p => (rowC L p, rowZ L p, (1 : ℤ))) +
        Code.ofJs (chainJoins (rowA L) (rowB L) (rowC L) 0 0 (untouched i)) +
        Code.ofXs (bigonPar (rowA L (oPos i b)) (rowC L (oPos i b)) (rowA L (uPos i b))
          (rowC L (uPos i b)) (rowB L (uPos i b)) (rowB L (oPos i b)) b) := by
  rw [← letterCrossing_pair]
  refine code_ext ?_ ?_
  · simp only [closureOf, wordCode, Code.map, ofXs, ofJs, add_xs, add_zero, zero_add]
    rw [univ_map_castSucc_last, univ_map_castSucc_last, Multiset.map_map]
    simp only [Fin.snoc_castSucc, Fin.snoc_last, Function.comp_def, letterCrossing_row2]
    rw [Multiset.insert_eq_cons, ← Multiset.singleton_add]
    exact add_assoc _ _ _
  · simp only [closureOf, wordCode, Code.map, ofXs, ofJs, add_js, add_zero, zero_add,
      Multiset.map_bind]
    rw [univ_bind_castSucc_last, univ_bind_castSucc_last, chainJoins_eq]
    simp only [Fin.snoc_castSucc, Fin.snoc_last, letterJoins_row2]
    have h₁ : letterJoins (L := L + 1 + 1) (Fin.last L).castSucc i =
        (untouched i).val.map fun p => (rowA L p, rowB L p, (0 : ℤ)) := by
      rw [letterJoins, untouched]
      refine Multiset.map_congr rfl fun p _ => ?_
      simp only [Fin.succ_castSucc, Fin.succ_last]
    have h₂ : letterJoins (L := L + 1 + 1) (Fin.last (L + 1)) i =
        (untouched i).val.map fun p => (rowB L p, rowC L p, (0 : ℤ)) := by
      rw [letterJoins, untouched]
      refine Multiset.map_congr rfl fun p _ => ?_
      simp only [Fin.succ_last]
    rw [h₁, h₂]
    abel

/-- **Cancellation.** Appending a letter followed by its inverse does not change the closure up to
Reidemeister equivalence (one Reidemeister II move). -/
theorem closureOf_cancel (g : Fin L → Fin m × Bool) (i : Fin m) (b : Bool) :
    ReidemeisterEquiv ⟨_, closureOf g⟩
      ⟨_, closureOf (Fin.snoc (Fin.snoc g (i, b)) (i, !b) : Fin (L + 1 + 1) → Fin m × Bool)⟩ := by
  set Wg := (wordCode g).map (rowEmb2 (m := m) (L := L)) with hWg
  set CL : Multiset ((Fin (L + 1 + 1 + 1) × Fin (m + 1)) × (Fin (L + 1 + 1 + 1) × Fin (m + 1)) × ℤ) :=
    (Finset.univ.val : Multiset (Fin (m + 1))).map fun p => (rowC L p, rowZ L p, 1) with hCL
  have hval : ∀ k : Fin (L + 1), (k.castSucc.castSucc : Fin (L + 1 + 1 + 1)).val ≤ L := by
    intro k; simp only [Fin.coe_castSucc]; omega
  have hW : ∀ e, Wg.Occurs e → e.1.val ≤ L := by
    intro e he
    obtain ⟨x, -, rfl⟩ := (occurs_map _ _ _).1 he
    exact hval x.1
  have vA : ∀ p : Fin (m + 1), (rowA L p).1.val = L := by intro p; simp
  have vB : ∀ p : Fin (m + 1), (rowB L p).1.val = L + 1 := by intro p; simp
  have vC : ∀ p : Fin (m + 1), (rowC L p).1.val = L + 2 := by intro p; simp
  have vZ : ∀ p : Fin (m + 1), (rowZ L p).1.val = 0 := by intro p; simp
  have rowne : ∀ (e e' : Fin (L + 1 + 1 + 1) × Fin (m + 1)), e.1.val ≠ e'.1.val → e ≠ e' := by
    rintro e e' h rfl; exact h rfl
  -- Step 1: embed.
  have hc : (closureOf g).map rowEmb2 = Wg + Code.ofJs
      ((Finset.univ.val : Multiset (Fin (m + 1))).map fun p => (rowA L p, rowZ L p, (0 : ℤ) + 1)) := by
    refine code_ext ?_ ?_
    · simp [closureOf, wordCode, hWg, Code.map, Code.ofJs]
    · simp only [closureOf, wordCode, hWg, Code.map, Code.ofJs, add_js, Multiset.map_add,
        Multiset.map_map]
      congr 1
  have h1 := ReidemeisterEquiv.of_move (Move.embed rowEmb2 (closureOf g))
  rw [hc] at h1
  -- Step 2: split the closing arcs at the last row.
  have h2 := (mergeJoins (rowA L) (rowC L) (rowZ L) 0 1 (fun p q h => (Prod.mk.inj h).2)
    (fun p q => rowne _ _ (by rw [vC, vA]; omega)) (fun p q => rowne _ _ (by rw [vC, vZ]; omega))
    Finset.univ Wg fun p _ h => by have := hW _ h; rw [vC] at this; omega).symm
  -- Step 3: route the untouched strands through the middle row.
  set R3 := Wg + Code.ofJs CL + Code.ofJs {(rowA L (oPos i b), rowC L (oPos i b), (0 : ℤ)),
    (rowA L (uPos i b), rowC L (uPos i b), 0)} with hR3
  have hR3v : ∀ e, R3.Occurs e → e.1.val ≠ L + 1 := by
    intro e he
    simp only [hR3, occurs_add] at he
    rcases he with (h | h) | h
    · have := hW _ h; omega
    · rw [occurs_ofJs] at h
      obtain ⟨_, hj, h⟩ := h
      obtain ⟨p, -, rfl⟩ := Multiset.mem_map.1 hj
      rcases h with rfl | rfl <;> simp
    · rw [occurs_ofJs_pair] at h
      rcases h with (rfl | rfl) | (rfl | rfl) <;> simp
  have h3 := (mergeJoins (rowA L) (rowB L) (rowC L) 0 0 (fun p q h => (Prod.mk.inj h).2)
    (fun p q => rowne _ _ (by rw [vB, vA]; omega)) (fun p q => rowne _ _ (by rw [vB, vC]; omega))
    (untouched i) R3 fun p _ h => hR3v _ h (vB p)).symm
  -- Step 4: Reidemeister II on the two strands of the letter.
  set R4 := Wg + Code.ofJs CL + Code.ofJs (chainJoins (rowA L) (rowB L) (rowC L) 0 0 (untouched i))
    with hR4
  have huo : uPos i b ≠ oPos i b := by
    have hcs : i.castSucc ≠ i.succ := (Fin.castSucc_lt_succ i).ne
    cases b <;> simp [uPos, oPos, hcs, hcs.symm]
  have hu : uPos i b ∉ untouched i := by cases b <;> simp [uPos, untouched]
  have ho : oPos i b ∉ untouched i := by cases b <;> simp [oPos, untouched]
  have hR4B : ∀ p, p = uPos i b ∨ p = oPos i b → ¬ R4.Occurs (rowB L p) := by
    intro p hp h
    simp only [hR4, occurs_add, occurs_ofJs, hCL, Multiset.mem_map, Finset.mem_val,
      Finset.mem_univ, true_and] at h
    rcases h with (h | ⟨_, ⟨q, rfl⟩, h | h⟩) | h
    · have := hW _ h; simp at this
    · simp [Fin.ext_iff] at h
    · simp [Fin.ext_iff] at h
    · obtain ⟨q, hq, h⟩ := occurs_chainJoins _ _ _ _ _ _ _ (by rwa [occurs_ofJs])
      rcases h with h | h | h
      · simp [Fin.ext_iff] at h
      · obtain rfl := (Prod.mk.inj h).2
        rcases hp with rfl | rfl
        exacts [hu hq, ho hq]
      · simp [Fin.ext_iff] at h
  have h4 := ReidemeisterEquiv.of_move (Move.r2par R4 (rowA L (oPos i b)) (rowC L (oPos i b))
    (rowA L (uPos i b)) (rowC L (uPos i b)) (rowB L (uPos i b)) (rowB L (oPos i b)) b
    (hR4B _ (Or.inl rfl)) (hR4B _ (Or.inr rfl)) (fun h => huo (Prod.mk.inj h).2) (by
      intro x hx
      simp only [Set.mem_insert_iff, Set.mem_singleton_iff] at hx
      rcases hx with rfl | rfl | rfl | rfl <;>
        exact ⟨rowne _ _ (by simp), rowne _ _ (by simp)⟩))
  refine (h1.trans h2).trans ((h3.of_eq ?_ ?_).trans (h4.of_eq rfl ?_))
  · rw [chainJoins_eq, univ_map_untouched i (fun p => (rowA L p, rowC L p, (0 : ℤ)))]
    refine code_ext ?_ ?_ <;>
      simp only [hR3, hCL, ofJs, ofXs, add_xs, add_js, add_zero, zero_add] <;>
      cases b <;> simp only [uPos, oPos, if_true, if_false, Bool.false_eq_true,
        Multiset.insert_eq_cons, ← Multiset.singleton_add] <;> abel
  · refine code_ext ?_ ?_ <;>
      simp only [hR3, hR4, hCL, ofJs, ofXs, add_xs, add_js, add_zero, zero_add] <;> abel
  · rw [closureOf_snoc_snoc_eq]

theorem braidClosure_cancel_end (w : List (Fin m × Bool)) (i : Fin m) (b : Bool) :
    ReidemeisterEquiv ⟨_, braidClosure w⟩ ⟨_, braidClosure (w ++ [(i, b), (i, !b)])⟩ := by
  have h₂ := closureOf_congr (m := m) (by simp : w.length + 1 + 1 = (w ++ [(i, b), (i, !b)]).length)
    (Fin.snoc (Fin.snoc w.get (i, b)) (i, !b)) (w ++ [(i, b), (i, !b)]).get fun k => by
      refine Fin.lastCases ?_ (fun j => ?_) k
      · simp
      · refine Fin.lastCases ?_ (fun j => ?_) j
        · simp
        · simp [List.getElem_append_left]
  rw [braidClosure_eq_closureOf, braidClosure_eq_closureOf]
  exact (closureOf_cancel w.get i b).trans h₂

theorem braidClosure_congr {w w' : List (Fin m × Bool)} (h : w = w') :
    ReidemeisterEquiv ⟨_, braidClosure w⟩ ⟨_, braidClosure w'⟩ := by
  subst h; exact .refl _

/-- **Rotation by a block.** The closures of `u ++ v` and `v ++ u` are Reidemeister equivalent. -/
theorem braidClosure_append_comm (u v : List (Fin m × Bool)) :
    ReidemeisterEquiv ⟨_, braidClosure (u ++ v)⟩ ⟨_, braidClosure (v ++ u)⟩ := by
  induction u generalizing v with
  | nil => exact braidClosure_congr (by simp)
  | cons x u ih =>
    exact (braidClosure_rotate x (u ++ v)).trans
      ((braidClosure_congr (by simp)).trans ((ih (v ++ [x])).trans (braidClosure_congr (by simp))))

/-- **Cancellation anywhere.** Deleting a letter next to its inverse does not change the closure. -/
theorem braidClosure_cancel (u v : List (Fin m × Bool)) (i : Fin m) (b : Bool) :
    ReidemeisterEquiv ⟨_, braidClosure (u ++ [(i, b), (i, !b)] ++ v)⟩ ⟨_, braidClosure (u ++ v)⟩ :=
  (braidClosure_append_comm (u ++ [(i, b), (i, !b)]) v).trans
    ((braidClosure_congr (by simp)).trans ((braidClosure_cancel_end (v ++ u) i b).symm.trans
      (braidClosure_append_comm v u)))

/-- **Conjugation by a letter.** The closures of `σ w σ⁻¹` and `w` are Reidemeister equivalent. -/
theorem braidClosure_conj (w : List (Fin m × Bool)) (i : Fin m) (b : Bool) :
    ReidemeisterEquiv ⟨_, braidClosure ((i, b) :: w ++ [(i, !b)])⟩ ⟨_, braidClosure w⟩ :=
  (braidClosure_append_comm [(i, b)] (w ++ [(i, !b)])).trans
    ((braidClosure_congr (by simp)).trans ((braidClosure_cancel w [] i (!b)).trans
      (braidClosure_congr (by simp))))

end Cancel

end QOU.MathlibExt.PL.Diagram
