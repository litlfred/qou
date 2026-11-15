import Mathlib.Data.Real.Basic
import Mathlib.Data.Real.Archimedean
import Mathlib.Order.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FieldSimp

/-!
# QOU.FluidDynamics.levi_growth_trichotomy — growth-exponent trichotomy (re-scoped)

## 🛑 Re-scoped 2026-10-13 — this file no longer carries Levi data

Owner ruling Q1 (2026-10-13) re-scoped the Levi chain onto `Θ = f·ξ♭`, with
`ξ = ω/|ω|` the vorticity direction on the 3D flow domain
(`prop:core-levi-form`). In dimension 3 the Levi form of a plane field is
`1 × 1`: its datum is the single scalar `ξ·curl ξ`. There is **no Levi
condition number**, so the quantity `C_L(κ)` this file used to be about, its
growth exponent `β`, and the marginal regime `0 < β < 1` (regime C) are
**withdrawn as undefined** (`conj:levi-degeneracy`). Branch (A) of that
conjecture — "`β = 0` ⇒ Levi non-degenerate ⇒ blow-up" — is **withdrawn**,
refuted under `Θ = f·ξ♭` by the Beltrami flow
(`LeviDegeneracyQ1.beltrami_refutes_branchA`). Branch (B) survives as an open
conjecture **on the Levi scalar**, carried by `LeviDegeneracyQ1.LeviDegeneracy`,
not here.

What changed in this file:

* The carrier `LeviGrowthTrichotomy (leviNonDegenerate : Prop)` is renamed
  `GrowthExponent`, its `condNumber` field is renamed `seq`, and its two branch
  fields are **removed**: `branchA : beta = 0 → leviNonDegenerate` encoded the
  withdrawn branch (A), and `branchB : beta = 1 → ¬ leviNonDegenerate` was a
  statement about the exponent of an undefined condition number. The
  `leviNonDegenerate` parameter goes with them.
* `levi_branches_exclusive` is removed: its content was `(0 : ℝ) ≠ 1` and it
  asserted exclusivity of two branches one of which is withdrawn.
* `bounded_condNumber_forces_beta_zero` becomes `bounded_seq_forces_beta_zero`
  (deprecated alias kept). Its mathematics is unchanged: a bounded positive
  sequence has `limsup log a_κ / log κ = 0`. What is withdrawn is its former
  reading as "the branch-(A) identification of `β = 0` with `C_L = O(1)`".

What remains is unconditional real analysis about the growth exponent of a
positive sequence, and it is stated as such. It is still used, by
`levi_pair_channel_branch_b.lean`, for a quantity that is well-defined: the
inverse squared core aspect ratio of the Townsend model
(`rem:townsend-biot-savart-strain`, `rem:hyperbolic-overlap-saturation`). That
is a fluid-shape quantity, not Levi data — for a straight anti-parallel pair the
Levi scalar is `0` for every core shape (`prop:core-levi-form`, Examples).

## History (kept as a record)

2026-07-18: the `conj:levi-degeneracy` dichotomy was refined to a trichotomy on
`β ∈ [0, 1]`, since `0 < β < 1` satisfied neither branch. 2026-08-30: the old
carrier had no field tying `beta` to `condNumber` (two degenerate instances
type-checked, one taking `C_L ≡ 1` with `β = 1`); the two-sided `limsup`
characterisation `beta_upper` / `beta_lower` below was added and is kept. Both
earlier forms are in git history.

## Base ring (§7c)
Archimedean: `β` and the sequence are real (a `limsup` of real log-ratios, an
order comparison). `ℝ` is correct.

## References
- [leitner2026] fluid-dynamics/levi-degeneracy-conjecture (`conj:levi-degeneracy`),
  core-levi-form, townsend-biot-savart-strain
-/

namespace QOU.FluidDynamics

/-! ### The elementary facts

Every exponent in `[0, 1]` is `0`, in the open window, or `1`. This is
ordered-field trichotomy, unconditional, stated on a bare real. -/

/-- **The trichotomy is exhaustive on `[0, 1]`.** Every exponent in `[0, 1]`
    is `0`, in `(0, 1)`, or `1`. -/
theorem beta_trichotomy {β : ℝ} (h0 : 0 ≤ β) (h1 : β ≤ 1) :
    β = 0 ∨ (0 < β ∧ β < 1) ∨ β = 1 := by
  rcases eq_or_lt_of_le h0 with h | h
  · exact Or.inl h.symm
  · rcases eq_or_lt_of_le h1 with h' | h'
    · exact Or.inr (Or.inr h')
    · exact Or.inr (Or.inl ⟨h, h'⟩)

/-- **The open window is a genuine third case.** When `0 < β < 1`, neither
    `β = 0` nor `β = 1` holds. -/
theorem beta_marginal_undetermined {β : ℝ} (h : 0 < β ∧ β < 1) :
    β ≠ 0 ∧ β ≠ 1 :=
  ⟨ne_of_gt h.1, ne_of_lt h.2⟩

/-! ### The growth-exponent carrier

Not a conjecture: `GrowthExponent a` is the data of a positive real sequence
together with its exponent `limsup_κ log a_κ / log κ`, assumed to lie in
`[0, 1]`. It carries no Levi or blow-up content. -/

/-- A positive real sequence `seq` with growth exponent
    `beta = limsup_κ log seq(κ) / log κ ∈ [0, 1]`, the `limsup` written out
    without `Filter` as `beta_upper` / `beta_lower`.

    Formerly `LeviGrowthTrichotomy`, with `seq` read as the Levi condition
    number and two branch fields; both readings and both fields are withdrawn
    (file docstring). -/
structure GrowthExponent where
  /-- The sequence `a_κ`. -/
  seq : ℕ → ℝ
  /-- Positivity — without it `log a_κ` is meaningless. -/
  seq_pos : ∀ κ : ℕ, 0 < seq κ
  /-- Growth exponent `β = limsup_κ log a_κ / log κ`. -/
  beta : ℝ
  /-- **Bounded-rate regime:** `0 ≤ β ≤ 1`. -/
  beta_mem : 0 ≤ beta ∧ beta ≤ 1
  /-- **`beta` is an upper exponent:** for every `ε > 0`, `a_κ ≤ κ^(β+ε)` for
      all large `κ`. -/
  beta_upper : ∀ ε : ℝ, 0 < ε → ∃ N : ℕ, ∀ κ : ℕ, N ≤ κ →
    seq κ ≤ (κ : ℝ) ^ (beta + ε)
  /-- **…and it is attained:** for every `ε > 0`, `κ^(β-ε) ≤ a_κ` for
      infinitely many `κ`. Upper and lower together say exactly
      `limsup_κ log a_κ / log κ = β`. -/
  beta_lower : ∀ ε : ℝ, 0 < ε → ∀ N : ℕ, ∃ κ : ℕ, N ≤ κ ∧
    (κ : ℝ) ^ (beta - ε) ≤ seq κ

/-- Structure-level form of `beta_trichotomy`. -/
theorem growthExponent_trichotomy (T : GrowthExponent) :
    T.beta = 0 ∨ (0 < T.beta ∧ T.beta < 1) ∨ T.beta = 1 :=
  beta_trichotomy T.beta_mem.1 T.beta_mem.2

/-- Structure-level form of `beta_marginal_undetermined`. -/
theorem growthExponent_marginal (T : GrowthExponent)
    (h : 0 < T.beta ∧ T.beta < 1) : T.beta ≠ 0 ∧ T.beta ≠ 1 :=
  beta_marginal_undetermined h

/-! ### A bounded sequence has exponent `0` -/

/-- **A bounded sequence has exponent `0`.**  If `a` is bounded then no
    positive exponent survives `beta_lower`, because `κ^(β/2) → ∞` overtakes any
    bound.  (Its former reading as the branch-(A) identification of `β = 0`
    with a bounded Levi condition number is withdrawn; file docstring.) -/
theorem bounded_seq_forces_beta_zero
    (T : GrowthExponent) (hb : ∃ M : ℝ, ∀ κ : ℕ, T.seq κ ≤ M) :
    T.beta = 0 := by
  obtain ⟨M, hM⟩ := hb
  have hMpos : 0 < M := lt_of_lt_of_le (T.seq_pos 0) (hM 0)
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
  have : M < T.seq κ := by
    calc M = c ^ (T.beta / 2) := hcM.symm
    _ < (N : ℝ) ^ (T.beta / 2) := step1
    _ ≤ (κ : ℝ) ^ (T.beta / 2) := step2
    _ ≤ T.seq κ := hκ
  exact absurd (hM κ) (not_le.mpr this)

@[deprecated bounded_seq_forces_beta_zero (since := "2026-10-13")]
alias bounded_condNumber_forces_beta_zero := bounded_seq_forces_beta_zero

@[deprecated growthExponent_trichotomy (since := "2026-10-13")]
alias levi_trichotomy_exhaustive := growthExponent_trichotomy

@[deprecated growthExponent_marginal (since := "2026-10-13")]
alias levi_marginal_undetermined := growthExponent_marginal

/-! ### Consistency and refutability -/

/-- Inhabitedness: `a ≡ 1` with exponent `0` satisfies every field. -/
noncomputable example : GrowthExponent where
  seq := fun _ => 1
  seq_pos := fun _ => one_pos
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

/-- **The tie is refutable.**  A bounded sequence cannot carry `beta = 1`. -/
example (T : GrowthExponent)
    (h : T.seq = fun _ => 1) : T.beta ≠ 1 := by
  have : T.beta = 0 := bounded_seq_forces_beta_zero T ⟨1, by simp [h]⟩
  rw [this]; norm_num

end QOU.FluidDynamics
