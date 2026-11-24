import Mathlib.Logic.Relation
import Mathlib.Algebra.Group.Commute.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Algebra.Order.Group.Unbundled.Abs
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-!
# The γγ lepton pair word reduces by braid-group relations only

Thread "β-decay Gröbner–Shirshov reduction" (W5 of the L2 1-ppQ plan), 2026-11-23.
Pre-registration: `computations/probes/qbeta_gg_pair_gb/PREREGISTRATION.md`.

The six-strand γγ lepton pair word is `V₀V₁V₂V₀V₃`, with vertex letter `Vᵢ = σᵢσᵢ₊₁⁻¹`
(photon `γᵢ = 1 + φ₀σᵢ + φ₁σᵢ₊₁ + φ₀₁σᵢσᵢ₊₁⁻¹`, owner ruling 2026-11-20). Its closure is
`e⁻ ⊔ ν̄ ⊔ loop` (`six_strand_pair_probe`).

## What is proved

1. `pairWord_braidEq_reduced`: the 10-letter word and the 4-letter word `σ₀²σ₁⁻¹σ₄⁻¹` are
   related by free cancellation and far commutation alone. No Hecke quadratic relation is used.
2. `eval_pairWord`: so in **every** group carrying elements `g i` that satisfy the braid
   relations, the two words have the same value. The invertible Hecke generators
   (`σᵢ⁻¹ = σᵢ − (q − q⁻¹)`) are one such group, for every `q`, including `q = 1`. Every trace,
   module action or energy that factors through the element therefore agrees on the two words,
   and their difference is `0` identically.
3. `run_invariant`: the signed crossing count between each pair of strands is unchanged by every
   braid relation. Since each letter changes one pair's count by `±1`,
   `four_le_length`: every word for this braid has at least 4 letters, and
   `length_even`: every such word has even length.
4. `cancellation_count`: so any reduction of `V₀V₁V₂V₀V₃` to a shortest word cancels exactly
   `(10 − 4)/2 = 3` pairs, whichever order it cancels them in.

`V₀V₁V₂V₃V₀` is the same braid (`pairWord'_braidEq`).

## What is NOT claimed

* That the cancellation count carries energy. No energy per cancelled pair is derived anywhere
  in the corpus, and none is introduced here.
* Anything about a nucleon. These words have no nucleon strand.
-/

namespace QOU.QBeta.GammaGammaPairReduction

/-- A braid letter `(i, true) = σᵢ`, `(i, false) = σᵢ⁻¹`. -/
abbrev Letter := ℕ × Bool

/-- The defining relations of the braid groups, as rewrite pairs. -/
inductive Rel : List Letter → List Letter → Prop
  | cancel (i : ℕ) (s : Bool) : Rel [(i, s), (i, !s)] []
  | far (i j : ℕ) (s t : Bool) (h : i + 2 ≤ j ∨ j + 2 ≤ i) :
      Rel [(i, s), (j, t)] [(j, t), (i, s)]
  | braid (i : ℕ) :
      Rel [(i, true), (i + 1, true), (i, true)] [(i + 1, true), (i, true), (i + 1, true)]

/-- One rewrite inside a word. -/
def Step (w w' : List Letter) : Prop :=
  ∃ l m r r', w = l ++ r ++ m ∧ w' = l ++ r' ++ m ∧ Rel r r'

/-- Equality in the braid group: the equivalence closure of `Step`. -/
def BraidEq : List Letter → List Letter → Prop := Relation.EqvGen Step

lemma step_of_rel (l m : List Letter) {r r' : List Letter} (h : Rel r r') :
    Step (l ++ r ++ m) (l ++ r' ++ m) := ⟨l, m, r, r', rfl, rfl, h⟩

/-- A function constant along every `Step` is constant on braid-equivalence classes. -/
lemma BraidEq.of_step {β : Type*} (f : List Letter → β)
    (hf : ∀ w w', Step w w' → f w = f w') {w w' : List Letter} (h : BraidEq w w') :
    f w = f w' := by
  induction h with
  | rel x y h => exact hf x y h
  | refl => rfl
  | symm _ _ _ ih => exact ih.symm
  | trans _ _ _ _ _ ih1 ih2 => exact ih1.trans ih2

/-! ## 1. Group values -/

section Group

variable {G : Type*} [Group G] (g : ℕ → G)

/-- `g` satisfies the braid relations. -/
structure IsBraidRep : Prop where
  far : ∀ i j, (i + 2 ≤ j ∨ j + 2 ≤ i) → Commute (g i) (g j)
  braid : ∀ i, g i * g (i + 1) * g i = g (i + 1) * g i * g (i + 1)

/-- The value of a letter. -/
def letterVal (x : Letter) : G := if x.2 then g x.1 else (g x.1)⁻¹

/-- The value of a word. -/
def eval (w : List Letter) : G := (w.map (letterVal g)).prod

lemma eval_append (u v : List Letter) : eval g (u ++ v) = eval g u * eval g v := by
  simp [eval, List.map_append, List.prod_append]

lemma eval_rel (hg : IsBraidRep g) {r r' : List Letter} (h : Rel r r') :
    eval g r = eval g r' := by
  cases h with
  | cancel i s => cases s <;> simp [eval, letterVal]
  | far i j s t hij =>
    have hc := hg.far i j hij
    have hc' : Commute (letterVal g (i, s)) (letterVal g (j, t)) := by
      cases s <;> cases t <;> simp only [letterVal] <;>
        simp [hc, hc.inv_left, hc.inv_right, hc.inv_inv]
    simpa [eval] using hc'.eq
  | braid i => simpa [eval, letterVal, mul_assoc] using hg.braid i

lemma eval_step (hg : IsBraidRep g) {w w' : List Letter} (h : Step w w') :
    eval g w = eval g w' := by
  obtain ⟨l, m, r, r', rfl, rfl, hr⟩ := h
  simp only [eval_append, eval_rel g hg hr]

/-- Braid-equal words have equal values in every braid representation. -/
theorem eval_braidEq (hg : IsBraidRep g) {w w' : List Letter} (h : BraidEq w w') :
    eval g w = eval g w' :=
  BraidEq.of_step (eval g) (fun _ _ hs => eval_step g hg hs) h

end Group

/-! ## 2. The pair word -/

/-- The vertex letter `Vᵢ = σᵢσᵢ₊₁⁻¹`. -/
def V (i : ℕ) : List Letter := [(i, true), (i + 1, false)]

/-- The γγ lepton pair word `V₀V₁V₂V₀V₃`. -/
def pairWord : List Letter := V 0 ++ V 1 ++ V 2 ++ V 0 ++ V 3

/-- The second word `V₀V₁V₂V₃V₀`. -/
def pairWord' : List Letter := V 0 ++ V 1 ++ V 2 ++ V 3 ++ V 0

/-- The reduced word `σ₀²σ₁⁻¹σ₄⁻¹`. -/
def pairReduced : List Letter := [(0, true), (0, true), (1, false), (4, false)]

lemma braidEq_of_step {w w' : List Letter} (h : Step w w') : BraidEq w w' :=
  Relation.EqvGen.rel _ _ h

lemma braidEq_trans {a b c : List Letter} (h1 : BraidEq a b) (h2 : BraidEq b c) :
    BraidEq a c := Relation.EqvGen.trans _ _ _ h1 h2

lemma braidEq_symm {a b : List Letter} (h : BraidEq a b) : BraidEq b a :=
  Relation.EqvGen.symm _ _ h

/-- **`V₀V₁V₂V₀V₃ = σ₀²σ₁⁻¹σ₄⁻¹` in the braid group**, by three free cancellations and two far
commutations. -/
theorem pairWord_braidEq_reduced : BraidEq pairWord pairReduced := by
  -- σ₀ σ₁⁻¹ σ₁ σ₂⁻¹ σ₂ σ₃⁻¹ σ₀ σ₁⁻¹ σ₃ σ₄⁻¹
  -- cancel σ₁⁻¹σ₁
  have s1 := step_of_rel [(0, true)] [(2, false), (2, true), (3, false), (0, true), (1, false),
    (3, true), (4, false)] (Rel.cancel 1 false)
  -- cancel σ₂⁻¹σ₂
  have s2 := step_of_rel [(0, true)] [(3, false), (0, true), (1, false), (3, true), (4, false)]
    (Rel.cancel 2 false)
  -- σ₃⁻¹σ₀ → σ₀σ₃⁻¹
  have s3 := step_of_rel [(0, true)] [(1, false), (3, true), (4, false)]
    (Rel.far 3 0 false true (Or.inr (by norm_num)))
  -- σ₃⁻¹σ₁⁻¹ → σ₁⁻¹σ₃⁻¹
  have s4 := step_of_rel [(0, true), (0, true)] [(3, true), (4, false)]
    (Rel.far 3 1 false false (Or.inr (by norm_num)))
  -- cancel σ₃⁻¹σ₃
  have s5 := step_of_rel [(0, true), (0, true), (1, false)] [(4, false)] (Rel.cancel 3 false)
  simp only [List.cons_append, List.nil_append, List.append_nil, Bool.not_false] at s1 s2 s3 s4 s5
  exact braidEq_trans (braidEq_of_step s1) <| braidEq_trans (braidEq_of_step s2) <|
    braidEq_trans (braidEq_of_step s3) <| braidEq_trans (braidEq_of_step s4) <|
    braidEq_of_step s5

/-- **`V₀V₁V₂V₃V₀` is the same braid**, by three free cancellations and one far commutation. -/
theorem pairWord'_braidEq : BraidEq pairWord' pairReduced := by
  -- σ₀ σ₁⁻¹ σ₁ σ₂⁻¹ σ₂ σ₃⁻¹ σ₃ σ₄⁻¹ σ₀ σ₁⁻¹
  have s1 := step_of_rel [(0, true)] [(2, false), (2, true), (3, false), (3, true), (4, false),
    (0, true), (1, false)] (Rel.cancel 1 false)
  have s2 := step_of_rel [(0, true)] [(3, false), (3, true), (4, false), (0, true), (1, false)]
    (Rel.cancel 2 false)
  have s3 := step_of_rel [(0, true)] [(4, false), (0, true), (1, false)] (Rel.cancel 3 false)
  -- σ₄⁻¹σ₀ → σ₀σ₄⁻¹, then σ₄⁻¹σ₁⁻¹ → σ₁⁻¹σ₄⁻¹
  have s4 := step_of_rel [(0, true)] [(1, false)] (Rel.far 4 0 false true (Or.inr (by norm_num)))
  have s5 := step_of_rel [(0, true), (0, true)] [] (Rel.far 4 1 false false (Or.inr (by norm_num)))
  simp only [List.cons_append, List.nil_append, List.append_nil, Bool.not_false] at s1 s2 s3 s4 s5
  exact braidEq_trans (braidEq_of_step s1) <| braidEq_trans (braidEq_of_step s2) <|
    braidEq_trans (braidEq_of_step s3) <| braidEq_trans (braidEq_of_step s4) <|
    braidEq_of_step s5

/-- **The unreduced and reduced pair words have the same value in every braid representation.**
In particular their difference vanishes in the Hecke algebra for every `q`, including `q = 1`. -/
theorem eval_pairWord {G : Type*} [Group G] (g : ℕ → G) (hg : IsBraidRep g) :
    eval g pairWord = eval g pairReduced :=
  eval_braidEq g hg pairWord_braidEq_reduced

/-! ## 3. The signed crossing matrix -/

/-- Strand labels by position, and the signed crossing count of each label pair. -/
@[ext] structure St where
  pos : ℕ → ℕ
  M : ℕ → ℕ → ℤ

/-- `+1` for `σᵢ`, `−1` for `σᵢ⁻¹`. -/
def sgn (s : Bool) : ℤ := if s then 1 else -1

/-- Labels `u, v` are the two strands `a, b` (in either order). -/
abbrev cross (a b u v : ℕ) : Prop := (u = a ∧ v = b) ∨ (u = b ∧ v = a)

lemma cross_comm (a b u v : ℕ) : cross a b u v ↔ cross b a u v := Or.comm

/-- Apply one letter: the strands at positions `i, i+1` cross with sign `s` and swap. -/
def act (S : St) (x : Letter) : St where
  pos k := if k = x.1 then S.pos (x.1 + 1) else if k = x.1 + 1 then S.pos x.1 else S.pos k
  M u v := S.M u v + if cross (S.pos x.1) (S.pos (x.1 + 1)) u v then sgn x.2 else 0

lemma act_M (S : St) (x : Letter) (u v : ℕ) : (act S x).M u v =
    S.M u v + if cross (S.pos x.1) (S.pos (x.1 + 1)) u v then sgn x.2 else 0 := rfl

lemma act_pos_self (S : St) (i : ℕ) (s : Bool) : (act S (i, s)).pos i = S.pos (i + 1) := by
  simp [act]

lemma act_pos_succ (S : St) (i : ℕ) (s : Bool) : (act S (i, s)).pos (i + 1) = S.pos i := by
  simp [act]

lemma act_pos_other (S : St) (i k : ℕ) (s : Bool) (h1 : k ≠ i) (h2 : k ≠ i + 1) :
    (act S (i, s)).pos k = S.pos k := by
  simp [act, h1, h2]

/-- Run a word from a state. -/
def run (S : St) (w : List Letter) : St := w.foldl act S

lemma run_append (S : St) (u v : List Letter) : run S (u ++ v) = run (run S u) v := by
  simp [run, List.foldl_append]

lemma run_rel {r r' : List Letter} (h : Rel r r') (S : St) : run S r = run S r' := by
  cases h with
  | cancel i s =>
    ext k
    · simp only [run, List.foldl]
      by_cases h1 : k = i
      · subst h1; rw [act_pos_self, act_pos_succ]
      · by_cases h2 : k = i + 1
        · subst h2; rw [act_pos_succ, act_pos_self]
        · rw [act_pos_other _ _ _ _ h1 h2, act_pos_other _ _ _ _ h1 h2]
    · rename_i v
      simp only [run, List.foldl, act_M, act_pos_self, act_pos_succ,
        cross_comm (S.pos (i + 1)) (S.pos i)]
      split_ifs <;> cases s <;> simp [sgn]
  | far i j s t hij =>
    ext k
    · simp only [run, List.foldl, act]; split_ifs <;> first | rfl | omega
    · rename_i v
      simp only [run, List.foldl]
      rw [act_M, act_M, act_M, act_M, act_pos_other S i j s (by omega) (by omega),
        act_pos_other S i (j + 1) s (by omega) (by omega),
        act_pos_other S j i t (by omega) (by omega),
        act_pos_other S j (i + 1) t (by omega) (by omega)]
      ring
  | braid i =>
    ext k
    · simp only [run, List.foldl, act]; split_ifs <;> first | rfl | omega
    · rename_i v
      simp only [run, List.foldl]
      simp only [act_M]
      simp (disch := omega) only [act_pos_self, act_pos_succ, act_pos_other]
      ring

/-- **The crossing state is a braid invariant.** -/
theorem run_invariant (S : St) {w w' : List Letter} (h : BraidEq w w') : run S w = run S w' :=
  BraidEq.of_step (run S) (fun w w' hs => by
    obtain ⟨l, m, r, r', rfl, rfl, hr⟩ := hs
    simp only [run_append, run_rel hr]) h

/-- The starting state: strand `k` at position `k`, no crossings. -/
def init : St := ⟨id, fun _ _ => 0⟩

/-- The three label pairs that `σ₀²σ₁⁻¹σ₄⁻¹` crosses: `{0,1}`, `{1,2}`, `{4,5}`. -/
def Φ (S : St) : ℤ := |S.M 0 1| + |S.M 1 2| + |S.M 4 5|

lemma abs_ite_sgn (c : Prop) [Decidable c] (s : Bool) :
    |(if c then sgn s else 0 : ℤ)| = if c then 1 else 0 := by
  split_ifs <;> cases s <;> simp [sgn]

/-- One letter changes `Φ` by at most `1`: it crosses one label pair. -/
lemma Φ_act_le (S : St) (x : Letter) : Φ (act S x) ≤ Φ S + 1 := by
  set a := S.pos x.1
  set b := S.pos (x.1 + 1)
  have e : ∀ u v, (act S x).M u v = S.M u v +
      if (u = a ∧ v = b) ∨ (u = b ∧ v = a) then sgn x.2 else 0 := fun _ _ => act_M S x _ _
  simp only [Φ, e]
  have t1 := abs_add_le (S.M 0 1) (if (0 = a ∧ 1 = b) ∨ (0 = b ∧ 1 = a) then sgn x.2 else 0)
  have t2 := abs_add_le (S.M 1 2) (if (1 = a ∧ 2 = b) ∨ (1 = b ∧ 2 = a) then sgn x.2 else 0)
  have t3 := abs_add_le (S.M 4 5) (if (4 = a ∧ 5 = b) ∨ (4 = b ∧ 5 = a) then sgn x.2 else 0)
  rw [abs_ite_sgn] at t1 t2 t3
  have hsum : ((if (0 = a ∧ 1 = b) ∨ (0 = b ∧ 1 = a) then 1 else 0 : ℤ) +
      (if (1 = a ∧ 2 = b) ∨ (1 = b ∧ 2 = a) then 1 else 0) +
      (if (4 = a ∧ 5 = b) ∨ (4 = b ∧ 5 = a) then 1 else 0)) ≤ 1 := by
    split_ifs <;> omega
  linarith

lemma Φ_run_le (S : St) (w : List Letter) : Φ (run S w) ≤ Φ S + w.length := by
  induction w generalizing S with
  | nil => simp [run]
  | cons x w ih =>
    have := ih (act S x)
    have := Φ_act_le S x
    simp only [run, List.foldl_cons, List.length_cons] at *
    push_cast
    linarith

lemma Φ_init : Φ init = 0 := by simp [Φ, init]

lemma Φ_pairReduced : Φ (run init pairReduced) = 4 := by decide

/-- **Every word for the pair braid has at least 4 letters.** -/
theorem four_le_length {w : List Letter} (h : BraidEq w pairWord) : 4 ≤ w.length := by
  have hr := run_invariant init (braidEq_trans h pairWord_braidEq_reduced)
  have hb := Φ_run_le init w
  rw [hr, Φ_pairReduced, Φ_init] at hb
  omega

/-- Every relation preserves the parity of the length. -/
lemma length_mod_two_step {w w' : List Letter} (h : Step w w') : w.length % 2 = w'.length % 2 := by
  obtain ⟨l, m, r, r', rfl, rfl, hr⟩ := h
  cases hr <;> (simp only [List.length_append, List.length_cons, List.length_nil]; try omega)

/-- **Every word for the pair braid has even length.** -/
theorem length_even {w : List Letter} (h : BraidEq w pairWord) : w.length % 2 = 0 := by
  have := BraidEq.of_step (fun u => u.length % 2) (fun _ _ hs => length_mod_two_step hs) h
  simpa [pairWord, V] using this

/-- **Exactly three cancellations.** The shortest word for `V₀V₁V₂V₀V₃` has 4 letters, so any
reduction to a shortest word removes `(10 − 4)/2 = 3` pairs. -/
theorem cancellation_count :
    pairWord.length = 10 ∧ pairReduced.length = 4 ∧ BraidEq pairWord pairReduced ∧
    (∀ w, BraidEq w pairWord → 4 ≤ w.length) ∧ (pairWord.length - pairReduced.length) / 2 = 3 :=
  ⟨rfl, rfl, pairWord_braidEq_reduced, fun _ h => four_le_length h, rfl⟩

end QOU.QBeta.GammaGammaPairReduction
