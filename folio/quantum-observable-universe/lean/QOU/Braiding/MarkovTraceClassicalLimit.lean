import Mathlib.GroupTheory.Perm.Cycle.Basic
import Mathlib.GroupTheory.Perm.Option
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Quotient
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Group
import Mathlib.SetTheory.Cardinal.Finite

/-!
# The Markov trace at `q = 1` counts bits: `𝔪 = 2^{components}`

At `q = 1` the Hecke algebra `H_n(q)` is the group algebra `ℚ[Sₙ]` and the
convention-D Markov parameter `z_D = q³/(q²+1)` is `1/2`. A braid enters only
through its permutation, and the components of its closure are the cycles of
that permutation (fixed points included).

This file builds the classical trace as a **state count**. A *state* of a
permutation `σ` of the strands is a two-valued colouring of the strands that is
invariant under `σ`, i.e. one bit per closed strand. Put

  `trClassical σ = #states(σ) / 2ⁿ`.

It is proved that

* `trClassical_one`: `trClassical 1 = 1`;
* `trClassical_mul_comm`: `trClassical (σ τ) = trClassical (τ σ)`;
* `trClassical_markov`: adding a strand and a crossing with it multiplies the
  trace by `1/2 = z_D(1)`;
* `card_states_eq_two_pow_cycles`: `#states(σ) = 2^{c(σ)}`, `c` = number of
  cycles of `σ`, fixed points included (= components of the closure).

So `2ⁿ · trClassical σ = 2^{c(σ)}`. These are the defining properties of a Markov
trace with parameter `1/2` on the tower `ℚ[S₁] ⊂ ℚ[S₂] ⊂ …` (evaluated on group
elements, then linearly), and by Jones' uniqueness of the Markov trace
(Jones 1987, Ann. Math. 126, Thm 5.1, cited, not formalized here) `trClassical`
is the Ocneanu trace at `q = 1`. With `def:mass-identity`,
`𝔪 = (1+q²)ⁿ q^(−n−2w) tr_D`, at `q = 1` this gives `𝔪 = 2ⁿ tr = 2^{c}`.

Information reading: `log₂ 𝔪(1) = c`, one bit per closed strand. Checked
independently by exact computation on 11 braids
(project file `qou-crossing-energy/result-info.md`, I1). Bean `qou-078y`.

Everything is combinatorics; the only division is by `2ⁿ` in `ℚ`.
-/

namespace QOU.Braiding.ClassicalTrace

open Equiv Equiv.Perm

variable {α : Type*} [Fintype α] [DecidableEq α]

/-- States of `σ`: two-valued colourings of the strands invariant under `σ`. -/
abbrev States (σ : Perm α) := {f : α → Bool // ∀ x, f (σ x) = f x}

/-- The classical trace: the number of states over `2ⁿ`. -/
noncomputable def trClassical (σ : Perm α) : ℚ :=
  (Fintype.card (States σ) : ℚ) / 2 ^ Fintype.card α

omit [Fintype α] [DecidableEq α] in
/-- An invariant colouring is invariant under every integer power. -/
theorem state_zpow {σ : Perm α} (f : States σ) (i : ℤ) (x : α) :
    f.1 ((σ ^ i) x) = f.1 x := by
  have hpos : ∀ (τ : Perm α), (∀ y, f.1 (τ y) = f.1 y) → ∀ (k : ℕ) y, f.1 ((τ ^ k) y) = f.1 y := by
    intro τ hτ k
    induction k with
    | zero => intro y; rfl
    | succ k ih => intro y; rw [pow_succ', Perm.mul_apply, hτ, ih]
  have hinv : ∀ y, f.1 (σ⁻¹ y) = f.1 y := by
    intro y
    have := f.2 (σ⁻¹ y)
    rw [Perm.apply_inv_self] at this
    exact this.symm
  cases i with
  | ofNat k => simpa using hpos σ f.2 k x
  | negSucc k =>
    rw [zpow_negSucc, ← inv_pow]
    exact hpos σ⁻¹ hinv (k + 1) x

/-- **States are colourings of the cycles.** -/
def statesEquivCycleColourings (σ : Perm α) :
    States σ ≃ (Quotient (SameCycle.setoid σ) → Bool) where
  toFun f := Quotient.lift f.1 (fun x y h => by
    obtain ⟨i, hi⟩ := h
    rw [← hi, state_zpow f i x])
  invFun h := ⟨fun x => h (Quotient.mk (SameCycle.setoid σ) x), fun x => by
    exact congrArg h
      (Quotient.sound (s := SameCycle.setoid σ) (sameCycle_apply_left.2 (SameCycle.refl σ x)))⟩
  left_inv f := by ext x; rfl
  right_inv h := by funext q; induction q using Quotient.inductionOn; rfl

/-- **`#states(σ) = 2^{c(σ)}`**, `c` the number of cycles, fixed points included. -/
theorem card_states_eq_two_pow_cycles (σ : Perm α) :
    Fintype.card (States σ) = 2 ^ Nat.card (Quotient (SameCycle.setoid σ)) := by
  rw [← Nat.card_eq_fintype_card, Nat.card_congr (statesEquivCycleColourings σ),
    Nat.card_fun, Nat.card_eq_fintype_card (α := Bool), Fintype.card_bool]

/-- `2ⁿ · trClassical σ = 2^{c(σ)}`: the classical mass counts bits. -/
theorem two_pow_mul_trClassical (σ : Perm α) :
    (2 : ℚ) ^ Fintype.card α * trClassical σ
      = 2 ^ Nat.card (Quotient (SameCycle.setoid σ)) := by
  unfold trClassical
  rw [card_states_eq_two_pow_cycles]
  push_cast
  field_simp

/-- The trivial braid has every colouring as a state. -/
theorem trClassical_one : trClassical (1 : Perm α) = 1 := by
  unfold trClassical
  have : Fintype.card (States (1 : Perm α)) = Fintype.card (α → Bool) :=
    Fintype.card_congr ⟨fun f => f.1, fun f => ⟨f, fun _ => rfl⟩, fun _ => rfl, fun _ => rfl⟩
  rw [this, Fintype.card_fun, Fintype.card_bool]
  push_cast
  exact div_self (pow_ne_zero _ two_ne_zero)

/-- Conjugation moves states by relabelling the strands. -/
def statesConj (σ τ : Perm α) : States σ ≃ States (τ * σ * τ⁻¹) where
  toFun f := ⟨fun y => f.1 (τ⁻¹ y), fun y => by
    simp only [Perm.mul_apply, Perm.inv_apply_self]
    exact f.2 _⟩
  invFun g := ⟨fun x => g.1 (τ x), fun x => by
    have := g.2 (τ x)
    simpa [Perm.mul_apply] using this⟩
  left_inv f := by ext x; simp
  right_inv g := by ext y; simp

/-- **Cyclicity** `tr(στ) = tr(τσ)`. -/
theorem trClassical_mul_comm (σ τ : Perm α) : trClassical (σ * τ) = trClassical (τ * σ) := by
  unfold trClassical
  have h : τ * σ = τ * (σ * τ) * τ⁻¹ := by group
  rw [h, Fintype.card_congr (statesConj (σ * τ) τ)]

/-- The Markov move: embed `σ` in one more strand (the new strand is `none`)
and cross strand `a` with the new one. -/
def markovMove (σ : Perm α) (a : α) : Perm (Option α) :=
  optionCongr σ * swap (some a) none

/-- States of the Markov move are states of `σ`: the new strand's bit is forced
to equal strand `a`'s. -/
def statesMarkov (σ : Perm α) (a : α) : States (markovMove σ a) ≃ States σ where
  toFun f := ⟨fun x => f.1 (some x), fun x => by
    by_cases hx : x = a
    · subst hx
      have h1 := f.2 (some x)
      have h2 := f.2 none
      simp only [markovMove, Perm.mul_apply, swap_apply_left, swap_apply_right,
        optionCongr_apply, Option.map_none, Option.map_some] at h1 h2
      show f.1 (some (σ x)) = f.1 (some x)
      rw [h2, h1]
    · have h := f.2 (some x)
      simp only [markovMove, Perm.mul_apply, optionCongr_apply] at h
      rwa [swap_apply_of_ne_of_ne (by simpa using hx) (by simp)] at h⟩
  invFun g := ⟨fun o => o.elim (g.1 a) g.1, fun o => by
    cases o with
    | none =>
      simp [markovMove, Perm.mul_apply, swap_apply_right, g.2 a]
    | some x =>
      by_cases hx : x = a
      · subst hx
        simp [markovMove, Perm.mul_apply, swap_apply_left]
      · simp only [markovMove, Perm.mul_apply, optionCongr_apply]
        rw [swap_apply_of_ne_of_ne (by simpa using hx) (by simp)]
        simp [g.2 x]⟩
  left_inv f := by
    ext o
    cases o with
    | none =>
      have h := f.2 (some a)
      simp only [markovMove, Perm.mul_apply, swap_apply_left, optionCongr_apply,
        Option.map_none] at h
      simpa using h.symm
    | some x => rfl
  right_inv g := by ext x; rfl

/-- **Markov property with parameter `1/2`.** -/
theorem trClassical_markov (σ : Perm α) (a : α) :
    trClassical (markovMove σ a) = (1 / 2) * trClassical σ := by
  unfold trClassical
  rw [Fintype.card_congr (statesMarkov σ a), Fintype.card_option]
  field_simp
  ring

end QOU.Braiding.ClassicalTrace
