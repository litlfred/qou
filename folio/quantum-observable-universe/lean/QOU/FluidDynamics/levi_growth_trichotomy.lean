import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Archimedean
import Mathlib.Order.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

/-!
# QOU.FluidDynamics.levi_growth_trichotomy — Levi condition-number trichotomy

Refines the `conj:levi-degeneracy` **dichotomy** into an exhaustive **trichotomy**
on the growth exponent of the Levi condition number, per the q-NS gap audit
Finding 3
([`docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md`](../../../../../../docs/audits/2026-07-18-q-ns-classical-gap-decomposition.md)).

**Scope discipline (owner directive 2026-07-24).** *Given a QOU*, `C_L(κ)` is the
Levi condition number of the QOU's own vortex-core geometry along its
root-of-unity ladder, and "NS-singular / NS-regular" below mean the QOU's
**internal** `q = 1` flow. This is a statement about QOUs; it does not decide the
classical `ℝ³` Navier–Stokes problem.

## The problem with the dichotomy

`conj:levi-degeneracy` states "*exactly one* of (A) `C_L(κ) = O(1)` / (B)
`C_L(κ) ~ κ`". These are **not complementary**: an intermediate rate
`C_L(κ) ~ κ^β` with `0 < β < 1` satisfies neither, so as written the conjecture
could be vacuously false. The `LeviDegeneracy` class in
`fluid-dynamics/levi-degeneracy-conjecture.lean` encodes the degeneracy *set*,
not the growth *rate*, so it does not capture the dichotomy at all.

## The fix

Introduce the growth exponent `β = limsup_κ (log C_L(κ) / log κ) ∈ [0, 1]` and
state the exhaustive trichotomy:

* **β = 0** — `C_L = O(1)`, Levi non-degenerate ⇒ (categorically) NS-singular
  (branch A);
* **β = 1** — `C_L ~ κ`, Levi degenerates / core → sheet ⇒ NS-regular (branch B);
* **0 < β < 1** — marginal `C_L ~ κ^β`, **undetermined** (the window the
  dichotomy silently dropped).

## Rewritten 2026-08-30 — the structure did not tie `beta` to `condNumber`

The previous `LeviGrowthTrichotomy` carried `condNumber : ℕ → ℝ` and `beta : ℝ`
with **no field relating them**, and `leviNonDegenerate : Prop` as a free field
the instance chose for itself. Two instances were built against the old
definition to measure what it asserted, and both type-check:

* `condNumber = fun _ => 0`, `beta = 1/2`, `leviNonDegenerate = True` — a
  "condition number" that is identically zero, an exponent unrelated to it, and
  both branch fields vacuous because `1/2` is neither `0` nor `1`;
* `condNumber = fun _ => 1` (so `C_L = O(1)`, true exponent `0`) with `beta = 1`
  — the *opposite* branch of the conjecture, accepted without complaint.

So `condNumber` was decoration and `beta` was a free real: assuming
`LeviGrowthTrichotomy` bought nothing about a Levi condition number. And the
three theorems below used only `beta_mem`, which made them facts about a real in
`[0,1]` dressed as facts about a Levi trichotomy — the inversion AGENTS.md
§"Conditional-proved ≠ premise-established" warns about, and the same defect
`appendix-surreals/surreal-squeeze.lean` records in its own history.

Both are fixed:

* `beta` is pinned to `condNumber` by a two-sided `limsup` characterisation
  stated without `Filter` — for every `ε > 0`, `condNumber κ ≤ κ^(β+ε)`
  eventually, and `κ^(β-ε) ≤ condNumber κ` infinitely often. Together these say
  exactly `limsup_κ log C_L(κ) / log κ = β`.
* `leviNonDegenerate` is a **parameter**, not a field, so an instance can no
  longer choose the proposition its own branch fields are about.
* The elementary trichotomy facts are restated on a bare real `β`, where their
  unconditional character is visible; the structure-level corollaries are kept
  for consumers.

The tie has a payoff beyond hygiene: `bounded_condNumber_forces_beta_zero`
**derives** the `.md`'s identification of branch A with `C_L = O(1)`, which was
previously an unstated coincidence between two unrelated fields.

## Honest scope

This formalises the **classification structure** — that the correct statement is
a trichotomy and that the marginal window is a genuine third case. It does
**not** compute the actual `β` (which branch the real `C_L(κ)` growth falls
into): that value is the open content of `conj:levi-degeneracy` and, via
Bridge B, the Clay problem.

## Base ring (§7c)
Archimedean: `β` and `C_L` are real (a `limsup` of real log-ratios, an order
comparison). `ℝ` is correct — this block is on the archimedean side of the wall.

## References
- [manuscript] fluid-dynamics/levi-degeneracy-conjecture (`conj:levi-degeneracy`),
  core-levi-form, ns-obstruction-tower
-/

namespace QOU.FluidDynamics

/-! ### The elementary facts, stated where they live

`conj:levi-degeneracy` asserts that the three regimes are mutually exclusive and
exhaustive on `β ∈ [0,1]`. That assertion is **true and unconditional** — it is
ordered-field trichotomy — and it is stated here on a bare real so that nothing
about it looks conjectural. The structure-level corollaries follow. -/

/-- **The trichotomy is exhaustive on `[0, 1]`.** Every bounded-rate exponent
    falls into one of `β = 0`, `0 < β < 1`, `β = 1` — so the original two-branch
    dichotomy (`β = 0` xor `β = 1`) is *not* a valid partition; the marginal
    window `0 < β < 1` is the missing third case. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (Finding 3)
theorem beta_trichotomy {β : ℝ} (h0 : 0 ≤ β) (h1 : β ≤ 1) :
    β = 0 ∨ (0 < β ∧ β < 1) ∨ β = 1 := by
  rcases eq_or_lt_of_le h0 with h | h
  · exact Or.inl h.symm
  · rcases eq_or_lt_of_le h1 with h' | h'
    · exact Or.inr (Or.inr h')
    · exact Or.inr (Or.inl ⟨h, h'⟩)

/-- **The marginal window is a genuine third case.** When `0 < β < 1`, neither
    `β = 0` nor `β = 1` holds, so neither branch is triggered. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (Finding 3)
theorem beta_marginal_undetermined {β : ℝ} (h : 0 < β ∧ β < 1) :
    β ≠ 0 ∧ β ≠ 1 :=
  ⟨ne_of_gt h.1, ne_of_lt h.2⟩

/-! ### The conjectural structure

Everything below is conditional. Assuming `LeviGrowthTrichotomy` is assuming an
open conjecture, and the fields are chosen so that the assumption has content. -/

/-- Growth-rate data for the Levi condition number `C_L(κ)` along the
    root-of-unity ladder `q_κ = e^{iπ/κ}`, refining `conj:levi-degeneracy`.

    The proposition `leviNonDegenerate` — "the Levi form is non-degenerate along
    the ladder", both eigenvalues positive — is a **parameter**: the branch
    fields are claims about a *given* non-degeneracy predicate, not about one the
    instance is free to invent.

    `beta` is the growth exponent `limsup_κ log C_L(κ) / log κ`, and
    `beta_upper` / `beta_lower` are that `limsup` written out without `Filter`.
    They are what makes `condNumber` load-bearing rather than decorative; see the
    file docstring for the two instances that satisfied the previous definition
    with no content at all. -/
structure LeviGrowthTrichotomy (leviNonDegenerate : Prop) where
  /-- The Levi condition number `C_L(κ)` at ladder step `κ`. -/
  condNumber : ℕ → ℝ
  /-- A condition number is positive — without this `log C_L` is meaningless and
      the exponent below is not about anything. -/
  condNumber_pos : ∀ κ : ℕ, 0 < condNumber κ
  /-- Growth exponent `β = limsup_κ log C_L(κ) / log κ`. -/
  beta : ℝ
  /-- **Bounded-rate regime:** `0 ≤ β ≤ 1` (`C_L` grows no faster than `κ`). -/
  beta_mem : 0 ≤ beta ∧ beta ≤ 1
  /-- **`beta` is an upper exponent for `condNumber`:** for every `ε > 0`,
      `C_L(κ) ≤ κ^(β+ε)` for all large `κ`. -/
  beta_upper : ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ κ : ℕ, N ≤ κ →
    condNumber κ ≤ (κ : ℝ) ^ (beta + ε)
  /-- **…and it is attained:** for every `ε > 0`, `κ^(β-ε) ≤ C_L(κ)` for
      infinitely many `κ`.  Upper and lower together say exactly
      `limsup_κ log C_L(κ) / log κ = β`; the upper bound alone would be satisfied
      by any exponent at least the true one. -/
  beta_lower : ∀ ε : ℝ, 0 < ε → ∀ N : ℕ, ∃ κ : ℕ, N ≤ κ ∧
    (κ : ℝ) ^ (beta - ε) ≤ condNumber κ
  /-- **Branch A:** `β = 0` (`C_L = O(1)`) ⇒ Levi non-degenerate (NS-singular). -/
  branchA : beta = 0 → leviNonDegenerate
  /-- **Branch B:** `β = 1` (`C_L ~ κ`) ⇒ Levi degenerates (NS-regular). -/
  branchB : beta = 1 → ¬ leviNonDegenerate

/-- Structure-level form of `beta_trichotomy`. -/
theorem levi_trichotomy_exhaustive {P : Prop} (T : LeviGrowthTrichotomy P) :
    T.beta = 0 ∨ (0 < T.beta ∧ T.beta < 1) ∨ T.beta = 1 :=
  beta_trichotomy T.beta_mem.1 T.beta_mem.2

/-- Structure-level form of `beta_marginal_undetermined`. -/
theorem levi_marginal_undetermined {P : Prop} (T : LeviGrowthTrichotomy P)
    (h : 0 < T.beta ∧ T.beta < 1) : T.beta ≠ 0 ∧ T.beta ≠ 1 :=
  beta_marginal_undetermined h

/-- **Branches A and B are mutually exclusive.**  Stated honestly: the content is
    `(0 : ℝ) ≠ 1`, so the hypotheses are jointly unsatisfiable and no instance is
    consulted.  It is kept because the `.md` asserts exclusivity, not because the
    structure supplies it. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture
theorem levi_branches_exclusive {β : ℝ} (hA : β = 0) (hB : β = 1) : False := by
  rw [hA] at hB; exact zero_ne_one hB

/-! ### The tie earns its keep

`conj:levi-degeneracy` branch (A) reads "*β = 0: bounded growth,
`C_L(κ) = O(1)`*" — it treats the exponent and the boundedness as the same
condition.  Under the previous definition that identification was unstated and
unprovable, since nothing connected `beta` to `condNumber`; the file docstring's
second measurement is a counterexample to it.  With `beta_lower` in place one
direction is a theorem. -/

/-- **A bounded condition number forces `β = 0`.**  If `C_L` is bounded then no
    positive exponent survives `beta_lower`, because `κ^(β/2) → ∞` overtakes any
    bound.  This is the `.md`'s branch-(A) identification, derived rather than
    assumed. -/
-- Ref: [manuscript] fluid-dynamics/levi-degeneracy-conjecture (branch A)
theorem bounded_condNumber_forces_beta_zero {P : Prop}
    (T : LeviGrowthTrichotomy P) (hb : ∃ M : ℝ, ∀ κ : ℕ, T.condNumber κ ≤ M) :
    T.beta = 0 := by
  obtain ⟨M, hM⟩ := hb
  have hMpos : 0 < M := lt_of_lt_of_le (T.condNumber_pos 0) (hM 0)
  by_contra hne
  have hpos : 0 < T.beta := lt_of_le_of_ne T.beta_mem.1 (Ne.symm hne)
  have hhalf : 0 < T.beta / 2 := by linarith
  -- `c` is the threshold past which `κ^(β/2)` exceeds `M`
  set c : ℝ := M ^ (2 / T.beta) with hc
  have hcnn : 0 ≤ c := Real.rpow_nonneg hMpos.le _
  obtain ⟨N, hN⟩ := exists_nat_gt (max c 1)
  have hcN : c < (N : ℝ) := lt_of_le_of_lt (le_max_left _ _) hN
  have h1N : (1 : ℝ) ≤ (N : ℝ) := le_of_lt (lt_of_le_of_lt (le_max_right _ _) hN)
  obtain ⟨κ, hκN, hκ⟩ := T.beta_lower (T.beta / 2) hhalf N
  have hNκ : (N : ℝ) ≤ (κ : ℝ) := Nat.cast_le.mpr hκN
  -- `M = c ^ (β/2)`
  have hcM : c ^ (T.beta / 2) = M := by
    rw [hc, ← Real.rpow_mul hMpos.le,
      show 2 / T.beta * (T.beta / 2) = 1 by field_simp, Real.rpow_one]
  have step1 : c ^ (T.beta / 2) < (N : ℝ) ^ (T.beta / 2) :=
    Real.rpow_lt_rpow hcnn hcN hhalf
  have step2 : (N : ℝ) ^ (T.beta / 2) ≤ (κ : ℝ) ^ (T.beta / 2) :=
    Real.rpow_le_rpow (by linarith) hNκ hhalf.le
  have hexp : T.beta - T.beta / 2 = T.beta / 2 := by ring
  rw [hexp] at hκ
  have : M < T.condNumber κ := by
    calc M = c ^ (T.beta / 2) := hcM.symm
    _ < (N : ℝ) ^ (T.beta / 2) := step1
    _ ≤ (κ : ℝ) ^ (T.beta / 2) := step2
    _ ≤ T.condNumber κ := hκ
  exact absurd (hM κ) (not_le.mpr this)

/-! ### Consistency and refutability

The carrier is inhabited, so assuming it is not assuming a contradiction; and the
tie is refutable, which is what the previous definition lacked. -/

/-- Inhabitedness: `C_L ≡ 1` with exponent `0` satisfies every field. -/
noncomputable example : LeviGrowthTrichotomy True where
  condNumber := fun _ => 1
  condNumber_pos := fun _ => one_pos
  beta := 0
  beta_mem := ⟨le_refl 0, zero_le_one⟩
  beta_upper := by
    intro ε hε
    refine ⟨1, fun κ hκ => ?_⟩
    have h1 : (1 : ℝ) ≤ (κ : ℝ) := by exact_mod_cast hκ
    calc (1 : ℝ) = (1 : ℝ) ^ (0 + ε) := (Real.one_rpow _).symm
    _ ≤ (κ : ℝ) ^ (0 + ε) := Real.rpow_le_rpow zero_le_one h1 (by linarith)
  beta_lower := by
    intro ε hε N
    refine ⟨max N 1, le_max_left _ _, ?_⟩
    have h1 : (1 : ℝ) ≤ ((max N 1 : ℕ) : ℝ) := by
      exact_mod_cast Nat.one_le_iff_ne_zero.mpr (by positivity)
    exact Real.rpow_le_one_of_one_le_of_nonpos h1 (by linarith)
  branchA := fun _ => trivial
  branchB := by intro h; exact absurd h (by norm_num)

/-- **The tie is refutable.**  A bounded `condNumber` can no longer coexist with
    `beta = 1`: that pair is the file docstring's second measurement, which the
    previous definition accepted.  Now it is impossible. -/
example {P : Prop} (T : LeviGrowthTrichotomy P)
    (h : T.condNumber = fun _ => 1) : T.beta ≠ 1 := by
  have : T.beta = 0 := bounded_condNumber_forces_beta_zero T ⟨1, by simp [h]⟩
  rw [this]; norm_num

end QOU.FluidDynamics
