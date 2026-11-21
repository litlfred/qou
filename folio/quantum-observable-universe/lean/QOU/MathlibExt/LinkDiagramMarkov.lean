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

end QOU.MathlibExt.PL.Diagram
