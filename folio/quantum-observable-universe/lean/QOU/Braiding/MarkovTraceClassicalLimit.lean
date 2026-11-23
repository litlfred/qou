import Mathlib.GroupTheory.Perm.Cycle.Basic
import Mathlib.GroupTheory.Perm.Option
import Mathlib.Data.Fintype.Pi
import Mathlib.Data.Fintype.Quotient
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Group
import Mathlib.Tactic.LinearCombination
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

/-! ### The trace `z^{n − cyc(σ)}` and its value at `z_D(1) = 1/2`

The Ocneanu trace on `ℚ[Sₙ]` with Markov parameter `z` takes the value `z^{n − cyc(w)}` on a
permutation `w`. Here this is defined directly, for any commutative ring and any `z`, and shown to
be cyclic and to satisfy the Markov property, using only that the number of cycles is invariant under
conjugation and under the Markov move. Both invariances are read off the state count:
`#states = 2^{cyc}` and `2^a = 2^b → a = b`.

At convention D, `z_D = q³/(q²+1)`, which is `1/2` at `q = 1` (`zD_at_one`). There
`2ⁿ · z_D(1)^{n − cyc(σ)} = 2^{cyc(σ)}` (`two_pow_mul_trZ_half`), and the trace agrees with the
state count (`trZ_half_eq_trClassical`). With `def:mass-identity`,
`𝔪 = (1 + q²)ⁿ q^{−n−2w} tr_D`, the factor `(1 + q²)ⁿ q^{−n−2w}` is `2ⁿ` at `q = 1` for every
writhe `w`, so `𝔪(β)|_{q=1} = 2^{c(β)}`, where `c(β)` is the number of components of the closure.
That last substitution is the definition of the mass and is not restated in Lean here.
-/

/-- The number of cycles of `σ`, fixed points included (= components of the closure). -/
noncomputable def cycles (σ : Perm α) : ℕ := Nat.card (Quotient (SameCycle.setoid σ))

omit [DecidableEq α] in
theorem cycles_le_card (σ : Perm α) : cycles σ ≤ Fintype.card α := by
  unfold cycles
  rw [← Nat.card_eq_fintype_card]
  exact Nat.card_le_card_of_surjective _ Quotient.mk_surjective

/-- Two permutations with equally many states have equally many cycles. -/
theorem cycles_eq_of_card_states_eq {β : Type*} [Fintype β] [DecidableEq β]
    (σ : Perm α) (τ : Perm β) (h : Fintype.card (States σ) = Fintype.card (States τ)) :
    cycles σ = cycles τ := by
  rw [card_states_eq_two_pow_cycles, card_states_eq_two_pow_cycles] at h
  exact Nat.pow_right_injective le_rfl h

/-- The Markov move does not change the number of cycles. -/
theorem cycles_markovMove (σ : Perm α) (a : α) : cycles (markovMove σ a) = cycles σ :=
  cycles_eq_of_card_states_eq _ _ (Fintype.card_congr (statesMarkov σ a))

/-- Conjugation does not change the number of cycles. -/
theorem cycles_conj (σ τ : Perm α) : cycles (τ * σ * τ⁻¹) = cycles σ :=
  (cycles_eq_of_card_states_eq _ _ (Fintype.card_congr (statesConj σ τ))).symm

/-- **The trace `tr_z(σ) = z^{n − cyc(σ)}`**, for any `z` in any commutative ring. -/
noncomputable def trZ {R : Type*} [CommRing R] (z : R) (σ : Perm α) : R :=
  z ^ (Fintype.card α - cycles σ)

omit [DecidableEq α] in
theorem trZ_one_perm {R : Type*} [CommRing R] (z : R) (σ : Perm α) (h : cycles σ = Fintype.card α) :
    trZ z σ = 1 := by
  simp [trZ, h]

/-- **Cyclicity** of `tr_z`. -/
theorem trZ_mul_comm {R : Type*} [CommRing R] (z : R) (σ τ : Perm α) :
    trZ z (σ * τ) = trZ z (τ * σ) := by
  unfold trZ
  have h : τ * σ = τ * (σ * τ) * τ⁻¹ := by group
  rw [h, cycles_conj]

/-- **Markov property** of `tr_z` with parameter `z`: adding a strand and crossing it multiplies
the trace by `z`. -/
theorem trZ_markov {R : Type*} [CommRing R] (z : R) (σ : Perm α) (a : α) :
    trZ z (markovMove σ a) = z * trZ z σ := by
  unfold trZ
  rw [cycles_markovMove, Fintype.card_option,
    show Fintype.card α + 1 - cycles σ = (Fintype.card α - cycles σ) + 1 by
      have := cycles_le_card σ; omega, pow_succ, mul_comm]

/-- `z_D = q³/(q²+1)` is `1/2` at `q = 1`. -/
theorem zD_at_one {K : Type*} [Field K] : (1 : K) ^ 3 / ((1 : K) ^ 2 + 1) = 1 / 2 := by
  norm_num

/-- **`2ⁿ · tr_{1/2}(σ) = 2^{cyc(σ)}`.** -/
theorem two_pow_mul_trZ_half {K : Type*} [Field K] [CharZero K] (σ : Perm α) :
    (2 : K) ^ Fintype.card α * trZ (1 / 2 : K) σ = 2 ^ cycles σ := by
  unfold trZ
  have hle := cycles_le_card σ
  obtain ⟨d, hd⟩ : ∃ d, Fintype.card α = cycles σ + d := ⟨Fintype.card α - cycles σ, by omega⟩
  rw [hd, show cycles σ + d - cycles σ = d by omega, pow_add, mul_assoc, ← mul_pow]
  norm_num

/-- **The trace `z^{n − cyc}` at `z = 1/2` is the state count.** -/
theorem trZ_half_eq_trClassical (σ : Perm α) : trZ (1 / 2 : ℚ) σ = trClassical σ := by
  have h1 := two_pow_mul_trZ_half (K := ℚ) σ
  have h2 := two_pow_mul_trClassical σ
  have hne : (2 : ℚ) ^ Fintype.card α ≠ 0 := pow_ne_zero _ two_ne_zero
  apply mul_left_cancel₀ hne
  rw [h1, h2]
  rfl

/-! ### Remark: `𝔈 = 𝔪 · c_q²` is not a Landauer energy

Landauer's principle bounds an energy linearly in an entropy, so a Landauer-type energy would be
`E(q) · ln 𝔪` for some `E(q)` not depending on the braid. The definition `𝔈 := 𝔪 · c_q²` is linear
in `𝔪` itself, and no such `E` exists: the unknot has `𝔪 = [2]` and the two-component unlink has
`𝔪 = [2]²`, and matching both forces `[2] = 2`, i.e. `q = 1`.

The lemma below is that argument with the logarithm kept outside the algebra: `L` stands for
`ln [2]`, and the only property of the logarithm used is `ln([2]²) = 2 · ln [2]`, which is why the
second hypothesis reads `E · (2L)`. At `q = 1` the mass counts states (`2^{c}`), which is
exponential in the bit count `c`, while a Landauer energy counts bits. Bean `qou-078y`, result I3
(`qou-crossing-energy/result-info.md`).
-/

/-- **No braid-independent `E` makes `𝔪 · c = E · ln 𝔪` on the unknot and the 2-unlink, unless
`[2] = 2`.** Here `t = [2]_q`, `c = c_q² ≠ 0`, and `L = ln t`. -/
theorem not_landauer {K : Type*} [Field K] (t c E L : K) (ht : t ≠ 0) (hc : c ≠ 0)
    (h1 : t * c = E * L) (h2 : t ^ 2 * c = E * (2 * L)) : t = 2 := by
  have h : t * (t * c) = 2 * (t * c) := by linear_combination h2 - 2 * h1
  have htc : t * c ≠ 0 := mul_ne_zero ht hc
  exact mul_right_cancel₀ htc h

end QOU.Braiding.ClassicalTrace
