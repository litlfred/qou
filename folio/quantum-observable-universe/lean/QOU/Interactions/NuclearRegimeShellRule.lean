import Mathlib.Data.Finset.Max
import Mathlib.Data.Fintype.Perm
import Mathlib.Algebra.BigOperators.Group.List.Defs
import Mathlib.Algebra.Order.Field.Basic

/-!
# The Regime-I "shell rule" of `prop:nuclear-operator-regimes`, as a hypothesis class

`prop:nuclear-operator-regimes` used to state a rule for Regime I: the
inter-nucleon operator selected at a shell-filling step is the torus knot
`T(2, n_s)`, with `n_s` the shell size. The only operator ever recorded for that
regime, `Φ = (σ₀σ₁)²σ₀`, was labelled `T(2,5)`, but its closure in `B₃` is a
two-component link, so the rule was withdrawn (PR #8739). This file states the
rule as a hypothesis, without assuming it holds, so that it can be tested.

## Contents

* §1 `wordPerm`: the strand permutation of a positive word in `B₃`. The orbits
  of this permutation are the components of the braid closure. We prove that
  `(σ₀σ₁)²σ₀` fixes strand 0 and therefore never sends it to strand 1, so its
  closure is not a knot, and in particular not the cinquefoil `T(2,5)`.
* §2 `StepSelection` / `IsSelected`: one step of an inductive construction that
  takes an operator of least cost from a finite candidate set. This works over
  any linearly ordered `R`.
* §3 `ShellRuleT2`: the withdrawn rule, stated as a class with content and with
  **no instance**. It says that on the Regime-I steps every selected operator
  closes to `T(2, shellSize k)`.
* §4 What can be proved about it, sorry-free:
  - a single counter-step refutes it (`not_shellRuleT2_of_counterStep`);
  - a candidate set whose torus indices are bounded by `M` cannot satisfy it at
    a Regime-I step whose shell is larger than `M`
    (`not_shellRuleT2_of_bounded_index`). The 2026-04 producer's candidate set
    contained torus-labelled words with indices only up to 5, so the rule could
    never have been tested on the `sd` (6) or `fp` (12) shells;
  - multiplying all costs at a step by `λ > 0` does not change which operator is
    selected (`isSelected_smul_iff`). The measurement in
    `computations/nuclear_regime_shell_rule_probe.py` relies on this when it
    rescales the running nucleus at each step.

Nothing in this file asserts that the rule holds.

## References

- [prop:nuclear-operator-regimes]
- docs/audits/2026-11-21-nuclear-regime-shell-rule.md
-/

namespace QOU.Interactions.NuclearRegimeShellRule

/-! ## §1  Strand permutations of positive words in `B₃` -/

/-- The image of the generator `σᵢ` (`i ∈ {0, 1}`) in `S₃`: the transposition of
strands `i` and `i+1`. -/
def genPerm : Fin 2 → Equiv.Perm (Fin 3)
  | 0 => Equiv.swap 0 1
  | 1 => Equiv.swap 1 2

/-- The strand permutation of a positive word `σ_{i₁} ⋯ σ_{iₗ}` in `B₃`. -/
def wordPerm (w : List (Fin 2)) : Equiv.Perm (Fin 3) :=
  (w.map genPerm).prod

/-- The word `(σ₀σ₁)²σ₀`, which the 2026-04 producer selected at the one
recorded Regime-I step and labelled `T_{2,5}`. -/
def phiWord : List (Fin 2) := [0, 1, 0, 1, 0]

/-- The strand permutation of `(σ₀σ₁)²σ₀` is the transposition `(1 2)`. -/
theorem wordPerm_phiWord : wordPerm phiWord = Equiv.swap 1 2 := by
  decide

/-- `(σ₀σ₁)²σ₀` fixes strand `0`. -/
theorem wordPerm_phiWord_fixes_zero : wordPerm phiWord 0 = 0 := by
  decide

/-- A permutation that fixes a point fixes it under every power. -/
theorem pow_apply_of_fixed {α : Type*} (p : Equiv.Perm α) (a : α) (h : p a = a) :
    ∀ n : ℕ, (p ^ n) a = a := by
  intro n
  induction n with
  | zero => rfl
  | succ n ih => rw [pow_succ, Equiv.Perm.mul_apply, h, ih]

/-- **The closure of `(σ₀σ₁)²σ₀` is not a knot.** No power of its strand
permutation sends strand `0` to strand `1`, so strands `0` and `1` lie on
different components of the closure. The torus knot `T(2,5)` has one
component, so this word does not close to `T(2,5)`. (That the components of a
braid closure are the orbits of its strand permutation is the standard closure
construction, used here only in this docstring.) -/
theorem phiWord_closure_not_connected :
    ∀ n : ℕ, (wordPerm phiWord ^ n) 0 ≠ 1 := by
  intro n
  rw [pow_apply_of_fixed _ 0 wordPerm_phiWord_fixes_zero n]
  decide

/-! ## §2  One step of an inductive operator selection -/

/-- The data of an inductive operator selection: a finite candidate set and,
at each step `k`, a cost on candidates. The cost is generic: the probe uses
the "demand" (total negative normal-form coefficient mass) of
`N_k · o · n_{k+1}` evaluated at `q₀`. -/
structure StepSelection (Op R : Type*) [LinearOrder R] where
  /-- The finite candidate set. -/
  cands : Finset Op
  /-- The cost of candidate `o` at step `k`. -/
  cost : ℕ → Op → R

variable {Op R : Type*} [LinearOrder R]

/-- `o` is selected at step `k`: it is a candidate of least cost (ties are
allowed, so several operators may be selected at one step). -/
def IsSelected (S : StepSelection Op R) (k : ℕ) (o : Op) : Prop :=
  o ∈ S.cands ∧ ∀ o' ∈ S.cands, S.cost k o ≤ S.cost k o'

/-- When the candidate set is nonempty, some candidate is selected at every
step. -/
theorem exists_isSelected (S : StepSelection Op R) (hne : S.cands.Nonempty)
    (k : ℕ) : ∃ o, IsSelected S k o := by
  obtain ⟨o, ho, hmin⟩ := S.cands.exists_min_image (S.cost k) hne
  exact ⟨o, ho, hmin⟩

/-! ## §3  The withdrawn rule, as a hypothesis class (no instance) -/

/-- **The Regime-I shell rule (withdrawn; a hypothesis, not a result).**

`torusIndex o = some n` records that the closure of candidate `o` is the torus
type `T(2, n)`, and `none` that it is not a `T(2, ·)` torus type. `regimeI` is
the set of shell-filling steps, and `shellSize k` is the size of the shell
being filled at step `k`. The rule says that on every Regime-I step, every
selected operator closes to `T(2, shellSize k)`.

The class has no instance in the corpus. The probe in
`computations/nuclear_regime_shell_rule_probe.py` measures, for fixed data, the
steps at which it fails. -/
class ShellRuleT2 (S : StepSelection Op R) (torusIndex : Op → Option ℕ)
    (regimeI : Set ℕ) (shellSize : ℕ → ℕ) : Prop where
  /-- Every operator selected at a Regime-I step closes to `T(2, shellSize k)`. -/
  selected_is_shell_torus :
    ∀ k ∈ regimeI, ∀ o, IsSelected S k o → torusIndex o = some (shellSize k)

/-! ## §4  What can be proved about the rule -/

/-- **Falsifier.** A single Regime-I step that selects an operator whose closure
is not `T(2, shellSize k)` refutes the rule. -/
theorem not_shellRuleT2_of_counterStep (S : StepSelection Op R)
    (torusIndex : Op → Option ℕ) (regimeI : Set ℕ) (shellSize : ℕ → ℕ)
    {k : ℕ} (hk : k ∈ regimeI) {o : Op} (hsel : IsSelected S k o)
    (hbad : torusIndex o ≠ some (shellSize k)) :
    ¬ ShellRuleT2 S torusIndex regimeI shellSize := by
  intro h
  exact hbad (h.selected_is_shell_torus k hk o hsel)

/-- **A bounded candidate set cannot reach a larger shell.** Suppose the
candidate set is nonempty, every candidate's torus index (if it has one) is at
most `M`, and some Regime-I step fills a shell of size greater than `M`. Then
the rule fails. -/
theorem not_shellRuleT2_of_bounded_index (S : StepSelection Op R)
    (torusIndex : Op → Option ℕ) (regimeI : Set ℕ) (shellSize : ℕ → ℕ)
    (hne : S.cands.Nonempty) (M : ℕ)
    (hbound : ∀ o ∈ S.cands, ∀ n, torusIndex o = some n → n ≤ M)
    {k : ℕ} (hk : k ∈ regimeI) (hbig : M < shellSize k) :
    ¬ ShellRuleT2 S torusIndex regimeI shellSize := by
  obtain ⟨o, hsel⟩ := exists_isSelected S hne k
  refine not_shellRuleT2_of_counterStep S torusIndex regimeI shellSize hk hsel ?_
  intro heq
  have := hbound o hsel.1 (shellSize k) heq
  omega

/-- **Selection is unchanged by positive rescaling of the costs at a step.**
The probe rescales the running nucleus by a positive scalar at each step, which
multiplies every candidate's demand at that step by the same positive scalar,
so the selected operator does not change. -/
theorem isSelected_smul_iff {K : Type*} [Field K] [LinearOrder K]
    [IsStrictOrderedRing K] (cands : Finset Op) (c : Op → K) (lam : K)
    (hlam : 0 < lam) (o : Op) :
    IsSelected (⟨cands, fun _ x => lam * c x⟩ : StepSelection Op K) 0 o ↔
      IsSelected (⟨cands, fun _ x => c x⟩ : StepSelection Op K) 0 o := by
  unfold IsSelected
  constructor
  · rintro ⟨ho, h⟩
    exact ⟨ho, fun o' ho' => le_of_mul_le_mul_left (h o' ho') hlam⟩
  · rintro ⟨ho, h⟩
    exact ⟨ho, fun o' ho' => mul_le_mul_of_nonneg_left (h o' ho') hlam.le⟩

end QOU.Interactions.NuclearRegimeShellRule
