import QOU.FluidDynamics.VortexLinkTopology

set_option autoImplicit false

/-!
# `QOU.FluidDynamics.VortexLinkMarkov` — component linking of a closed braid is a conjugacy invariant

NS attack vector 2 (bean `qou-p6tm`), follow-up to `VortexLinkTopology`. That
file proves the signed crossing matrix `C` of a braid word is invariant under the
braid relations (R2, R3, far commutation), and notes as open that **conjugation
(Markov I) invariance of component linking for non-pure braids is not proved**.
This file proves it.

## Set-up

Run a word `w` on `n + 1` strands from `init n` (labels = positions, `C = 0`).
Let `P = (run (init n) w).pos`: the strand label at final position `p` is `P p`.
In the closure, final position `p` is joined to start position `p`, whose label
is `p`. So the labels of one component of the closure are exactly an orbit of
`P`, and a function `κ` on labels is constant on components iff `κ ∘ P = κ`.

For such a `κ` (a "component assignment"; the orbit map itself is the finest
one) the **component crossing sum**

  `compSum κ C A B = Σₓ Σᵧ [κ x = A] [κ y = B] · C x y`

is the signed number of crossings between components `A` and `B`; for `A ≠ B`
it is twice the linking number `lk(A, B)`. For a pure braid and `κ = id` it is
the entry `C A B` of `VortexLinkTopology`.

## What is proved (all sorry-free, no axioms beyond Lean's core three)

1. `run_relabel` — running a word commutes with relabelling the strands by any
   permutation `e`.
2. `compSum_relabel`, `compSum_add`, `compSum_bump_zero` — the bookkeeping of
   `compSum` (reindexing, additivity, one crossing).
3. `rotate_letter` — **moving the first letter of the word to the end** (the
   elementary cyclic rotation, which does not change the closed braid) preserves
   every component crossing sum, with the component assignment transported by
   the transposition of that letter; and the transported assignment is again
   constant on the components of the rotated closure.
4. `rotate` — the same for moving any prefix `v` to the end.
5. `run_inv_append` — `g⁻¹ g` acts trivially on every state (R2, iterated).
6. `markovI_conj` — **Markov I.** For every conjugate `g w g⁻¹` there is a
   permutation `e` of strand labels such that for every component assignment `κ`
   of the closure of `g w g⁻¹`, `κ ∘ e` is a component assignment of the closure
   of `w` and every component crossing sum of `w` (under `κ ∘ e`) equals that of
   `g w g⁻¹` (under `κ`). So the component linking matrix is a conjugacy
   invariant, for non-pure braids too.

## What is NOT here

* Markov II (stabilisation, which changes the strand count) is not proved.
* No statement about Euler or Navier–Stokes; see `VortexLinkTopology` and the
  audit `docs/audits/2026-10-12-ns-v2-vortex-topology.md`.

-- Ref: [manuscript] fluid-dynamics, NS attack vector 2 (vortex-line linking)
Bean `qou-p6tm`.
-/

namespace QOU.FluidDynamics.VortexLink

open Finset

variable {n : ℕ}

/-! ### Relabelling strands -/

/-- Relabel the strands of a state by a permutation `e` of labels. -/
def relabel (e : Equiv.Perm (Fin (n + 1))) (s : St n) : St n :=
  ⟨e ∘ s.pos, fun x y => s.C (e.symm x) (e.symm y)⟩

lemma bump_relabel {m : ℕ} (e : Equiv.Perm (Fin m)) (C : Fin m → Fin m → ℤ)
    (a b : Fin m) (t : ℤ) :
    (fun x y => bump C a b t (e.symm x) (e.symm y))
      = bump (fun x y => C (e.symm x) (e.symm y)) (e a) (e b) t := by
  funext x y
  simp only [bump, Equiv.symm_apply_eq]

lemma step_relabel (e : Equiv.Perm (Fin (n + 1))) (s : St n) (l : Letter n) :
    step (relabel e s) l = relabel e (step s l) := by
  simp only [step, relabel, Function.comp_apply, St.mk.injEq]
  exact ⟨rfl, (bump_relabel e s.C _ _ _).symm⟩

/-- Running a word commutes with relabelling. -/
theorem run_relabel (e : Equiv.Perm (Fin (n + 1))) (s : St n) (w : List (Letter n)) :
    run (relabel e s) w = relabel e (run s w) := by
  induction w generalizing s with
  | nil => rfl
  | cons l w ih => simp only [run_cons, step_relabel, ih]

/-! ### Component crossing sums -/

/-- Signed crossings between the strands that `κ` sends to `A` and those it sends
to `B`. -/
def compSum {K : Type*} [DecidableEq K] (κ : Fin (n + 1) → K)
    (C : Fin (n + 1) → Fin (n + 1) → ℤ) (A B : K) : ℤ :=
  ∑ x, ∑ y, if κ x = A ∧ κ y = B then C x y else 0

variable {K : Type*} [DecidableEq K]

lemma compSum_add (κ : Fin (n + 1) → K) (C D : Fin (n + 1) → Fin (n + 1) → ℤ) (A B : K) :
    compSum κ (C + D) A B = compSum κ C A B + compSum κ D A B := by
  simp only [compSum, ← Finset.sum_add_distrib, Pi.add_apply]
  refine Finset.sum_congr rfl fun x _ => Finset.sum_congr rfl fun y _ => ?_
  split_ifs <;> simp

lemma compSum_relabel (κ : Fin (n + 1) → K) (e : Equiv.Perm (Fin (n + 1)))
    (C : Fin (n + 1) → Fin (n + 1) → ℤ) (A B : K) :
    compSum κ (fun x y => C (e.symm x) (e.symm y)) A B = compSum (κ ∘ e) C A B := by
  simp only [compSum, Function.comp_apply]
  rw [← Equiv.sum_comp e]
  refine Finset.sum_congr rfl fun x _ => ?_
  rw [← Equiv.sum_comp e]
  simp

set_option linter.unnecessarySeqFocus false in
lemma compSum_bump_zero (κ : Fin (n + 1) → K) (a b : Fin (n + 1)) (t : ℤ) (A B : K) :
    compSum κ (bump 0 a b t) A B
      = (if κ a = A ∧ κ b = B then t else 0) + (if κ b = A ∧ κ a = B then t else 0) := by
  have h : ∀ x y : Fin (n + 1), (if κ x = A ∧ κ y = B then bump 0 a b t x y else 0)
      = (if x = a then (if y = b then (if κ x = A ∧ κ y = B then t else 0) else 0) else 0)
        + (if x = b then (if y = a then (if κ x = A ∧ κ y = B then t else 0) else 0) else 0) := by
    intro x y
    simp only [bump, Pi.zero_apply, zero_add]
    by_cases hxa : x = a <;> by_cases hyb : y = b <;> by_cases hxb : x = b <;>
      by_cases hya : y = a <;> simp_all <;> split_ifs <;> ring
  simp [compSum, h, Finset.sum_add_distrib]

lemma bump_eq_add {m : ℕ} (C : Fin m → Fin m → ℤ) (a b : Fin m) (t : ℤ) :
    bump C a b t = C + bump 0 a b t := by
  funext x y
  simp only [bump, Pi.add_apply, Pi.zero_apply]
  ring

/-! ### Cyclic rotation of the word -/

/-- The transposition of positions swapped by a letter. -/
def tr (l : Letter n) : Equiv.Perm (Fin (n + 1)) := Equiv.swap l.1.castSucc l.1.succ

lemma init_eq_relabel (e : Equiv.Perm (Fin (n + 1))) :
    (⟨e, 0⟩ : St n) = relabel e (init n) := rfl

lemma run_cons_init (l : Letter n) (u : List (Letter n)) :
    run (init n) (l :: u)
      = ⟨tr l ∘ (run (init n) u).pos,
         bump 0 l.1.castSucc l.1.succ (sgn l.2)
           + fun x y => (run (init n) u).C ((tr l).symm x) ((tr l).symm y)⟩ := by
  rw [run_cons]
  have hs : step (init n) l = ⟨tr l, bump 0 l.1.castSucc l.1.succ (sgn l.2)⟩ := rfl
  rw [hs, run_C_add, init_eq_relabel, run_relabel]
  rfl

lemma run_snoc_init (l : Letter n) (u : List (Letter n)) :
    run (init n) (u ++ [l])
      = ⟨(run (init n) u).pos ∘ tr l,
         (run (init n) u).C
           + bump 0 ((run (init n) u).pos l.1.castSucc) ((run (init n) u).pos l.1.succ)
               (sgn l.2)⟩ := by
  rw [run_append]
  simp only [run_cons, run_nil, step, St.mk.injEq]
  exact ⟨rfl, bump_eq_add _ _ _ _⟩

/-- **Elementary cyclic rotation.** Moving the first letter `l` of a word to the
end does not change the closed braid. Every component crossing sum is preserved,
with the component assignment transported by the transposition of `l`, and the
transported assignment is again constant on the components of the new closure. -/
theorem rotate_letter (l : Letter n) (u : List (Letter n)) (κ : Fin (n + 1) → K)
    (hκ : ∀ x, κ ((run (init n) (l :: u)).pos x) = κ x) :
    (∀ x, (κ ∘ tr l) ((run (init n) (u ++ [l])).pos x) = (κ ∘ tr l) x) ∧
    ∀ A B, compSum (κ ∘ tr l) (run (init n) (u ++ [l])).C A B
      = compSum κ (run (init n) (l :: u)).C A B := by
  rw [run_cons_init] at hκ
  simp only [Function.comp_apply] at hκ
  refine ⟨fun x => ?_, fun A B => ?_⟩
  · rw [run_snoc_init]
    simp only [Function.comp_apply]
    rw [hκ]
  · rw [run_snoc_init, run_cons_init]
    simp only
    rw [compSum_add, compSum_add, compSum_bump_zero, compSum_bump_zero,
      compSum_relabel]
    simp only [Function.comp_apply, hκ]
    ring

/-- **Cyclic rotation by a prefix.** Moving a prefix `v` to the end preserves
every component crossing sum, with the component assignment transported by a
permutation of labels. -/
theorem rotate (v u : List (Letter n)) :
    ∃ e : Equiv.Perm (Fin (n + 1)), ∀ (κ : Fin (n + 1) → K),
      (∀ x, κ ((run (init n) (v ++ u)).pos x) = κ x) →
      (∀ x, (κ ∘ e) ((run (init n) (u ++ v)).pos x) = (κ ∘ e) x) ∧
      ∀ A B, compSum (κ ∘ e) (run (init n) (u ++ v)).C A B
        = compSum κ (run (init n) (v ++ u)).C A B := by
  induction v generalizing u with
  | nil => exact ⟨1, fun κ hκ => by simpa using hκ⟩
  | cons l v ih =>
    obtain ⟨e, he⟩ := ih (u ++ [l])
    refine ⟨tr l * e, fun κ hκ => ?_⟩
    have h1 := rotate_letter l (v ++ u) κ (by simpa using hκ)
    rw [List.append_assoc] at h1
    have h2 := he (κ ∘ tr l) h1.1
    have hw : u ++ l :: v = u ++ [l] ++ v := by simp
    refine ⟨fun x => ?_, fun A B => ?_⟩
    · have := h2.1 x
      rw [hw]
      simpa [Equiv.Perm.coe_mul, Function.comp_assoc] using this
    · have := h2.2 A B
      rw [hw, List.cons_append]
      rw [show κ ∘ ⇑(tr l * e) = (κ ∘ tr l) ∘ e by
        simp [Equiv.Perm.coe_mul, Function.comp_assoc]]
      rw [this, h1.2 A B]

/-! ### Inverse words and Markov I -/

/-- The inverse braid word. -/
def inv (g : List (Letter n)) : List (Letter n) := (g.map fun l => (l.1, !l.2)).reverse

/-- `g⁻¹ g` acts trivially on every state. -/
theorem run_inv_append (g : List (Letter n)) (s : St n) : run s (inv g ++ g) = s := by
  induction g generalizing s with
  | nil => rfl
  | cons l g ih =>
    have : inv (l :: g) ++ l :: g = inv g ++ [(l.1, !l.2), (l.1, !!l.2)] ++ g := by
      simp [inv]
    rw [this, run_append, run_append, run_R2, ← run_append, ih]

/-- **Markov I (conjugation invariance of component linking).** For every
conjugate `g w g⁻¹`, some permutation `e` of strand labels carries every
component assignment `κ` of its closure to a component assignment `κ ∘ e` of the
closure of `w`, with every component crossing sum unchanged. -/
theorem markovI_conj (g w : List (Letter n)) :
    ∃ e : Equiv.Perm (Fin (n + 1)), ∀ (κ : Fin (n + 1) → K),
      (∀ x, κ ((run (init n) (g ++ w ++ inv g)).pos x) = κ x) →
      (∀ x, (κ ∘ e) ((run (init n) w).pos x) = (κ ∘ e) x) ∧
      ∀ A B, compSum (κ ∘ e) (run (init n) w).C A B
        = compSum κ (run (init n) (g ++ w ++ inv g)).C A B := by
  obtain ⟨e, he⟩ := rotate (K := K) g (w ++ inv g)
  have hw : run (init n) (w ++ inv g ++ g) = run (init n) w := by
    rw [List.append_assoc, run_append, run_inv_append]
  refine ⟨e, fun κ hκ => ?_⟩
  have := he κ (by simpa [List.append_assoc] using hκ)
  rw [hw] at this
  refine ⟨this.1, fun A B => ?_⟩
  rw [this.2 A B, List.append_assoc]

/-! ### Sanity checks -/

/-- The 2-strand twist `σ₁` closes to an unknot (one component); its single
crossing is a self-crossing of that component. The double sum counts the
symmetric matrix entries `C 0 1` and `C 1 0`, so with `κ` constant it is `2`. -/
theorem single_twist_one_component :
    compSum (fun _ : Fin 2 => ()) (run (init 1) [((0 : Fin 1), true)]).C () () = 2 := by
  decide

end QOU.FluidDynamics.VortexLink
