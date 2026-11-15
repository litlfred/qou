import QOU.FluidDynamics.levi_growth_trichotomy

/-!
# QOU.FluidDynamics.levi_pair_channel_branch_b — the linear branch, and the pair channel

The dual of `bounded_condNumber_forces_beta_zero`
([`levi_growth_trichotomy.lean`](levi_growth_trichotomy.lean)): a **linearly
growing** Levi condition number forces `β = 1`, which is branch **B** of
`conj:levi-degeneracy`.

**Scope discipline.** Everything here is *given a QOU*, and everything about
the anti-parallel-pair channel is **conditional on the lock formula**
`C_L = Γ/(π ν_q)` — a model input, not derived. This is a per-channel
statement in the sense of the 2026-07-25 caveat on
`conj:levi-degeneracy`: it assigns a branch to **one** channel under a named
hypothesis. It does **not** decide the conjecture, and it says nothing about
channels the lock does not cover.

## Why this file exists

`conj:levi-degeneracy` is a trichotomy on `β = limsup_κ log C_L(κ)/log κ`:
`β = 0` is branch A (blow-up), `β = 1` is branch B (regular), and
`0 < β < 1` is the **marginal window C**, where the regularity verdict is
undetermined. The corpus records a *fitted* `β ≈ 0.9963` for the pair
channel (`qns-levi-lock-scaling-probe.witness.json`, field `beta_fit`).

**A fitted `0.9963` is exactly the shape that would put this channel in the
undetermined window C.** It does not: the fit is a finite-`ε` artifact and
the true exponent is `1` on the nose. Under the lock, with
`ν_q = (q-1)/(2q)` and `ε := q - 1`,

  `κ²_lock = π ν_q / Γ = (π/(2Γ)) · ε/(1+ε)`,  so  `C_L = 1/κ²_lock ∼ (2Γ/π)/ε`,

which is exactly linear in `1/ε`; the `(1+ε)` is the whole discrepancy.
Measured at 50 dps (`qns_levi_lock_beta_exact_probe.py`): the secant
exponent is `0.96293` over `[10⁻¹,10⁻²]`, `0.99999996` over `[10⁻⁷,10⁻⁸]`,
and `1.0` over `[10⁻¹⁹,10⁻²⁰]`. The recorded `0.9963` is a fit over a
finite window, not evidence of a marginal exponent.

`linear_condNumber_forces_beta_one` below is the statement that removes the
ambiguity: it does not measure `β`, it **derives** `β = 1` from linear
growth, so no fit precision is involved and window C is excluded for any
channel whose condition number is eventually linear.

## What is proved, and what is assumed

*Proved here:* linear growth ⟹ `β = 1` ⟹ branch B fires
(`¬ leviNonDegenerate`); and the linear case is realizable, so the theorem
is not vacuous (`linearTrichotomy`).

*Assumed, and named:* the lock formula itself, the identification of `C_L`
with `1/κ²_lock`, and that the ladder's `ε_κ` is `∼ c/κ`. Those are the
model inputs; this file is what follows from them.

## Base ring (§7c)
Archimedean: `β` is a `limsup` of real log-ratios and `Real.rpow` is the
statement. `ℝ` is correct — this is on the archimedean side of the wall.

## References
- [leitner2026] fluid-dynamics/levi-degeneracy-conjecture (`conj:levi-degeneracy`),
  hyperbolic-overlap-saturation (the Levi lock `κ² = πν/Γ`)
-/

namespace QOU.FluidDynamics

open Real

/-- **Every positive level is eventually exceeded by `n^e`, `e > 0`** — the
    one archimedean fact all three growth arguments below need, factored out
    so each of them is bookkeeping.  Returns an index that is also `≥ M`. -/
theorem exists_large_rpow (c : ℝ) (hc : 0 ≤ c) (e : ℝ) (he : 0 < e) (M : ℕ) :
    ∃ n : ℕ, M ≤ n ∧ c < (n : ℝ) ^ e := by
  obtain ⟨n, hn⟩ := exists_nat_gt (max (c ^ (1 / e)) (M : ℝ))
  have hMn : (M : ℝ) < (n : ℝ) := lt_of_le_of_lt (le_max_right _ _) hn
  have hMn' : M ≤ n := by exact_mod_cast hMn.le
  refine ⟨n, hMn', ?_⟩
  have hcn : c ^ (1 / e) < (n : ℝ) := lt_of_le_of_lt (le_max_left _ _) hn
  have hc0 : (0 : ℝ) ≤ c ^ (1 / e) := Real.rpow_nonneg hc _
  have hstep : (c ^ (1 / e)) ^ e < (n : ℝ) ^ e := Real.rpow_lt_rpow hc0 hcn he
  rwa [← Real.rpow_mul hc, show 1 / e * e = 1 by field_simp, Real.rpow_one] at hstep

/-- **A linearly growing condition number forces `β = 1`** — branch B.

    The dual of `bounded_condNumber_forces_beta_zero`, and the reason the
    marginal window C is not where this channel lives.  If `C_L(κ) = A·κ`
    eventually with `A > 0`, then no exponent below `1` can be an upper
    exponent: `beta_upper` at `ε = (1 - β)/2` would give `A·κ ≤ κ^s` with
    `s = (1+β)/2 < 1`, i.e. `A·κ^(1-s) ≤ 1` — but `κ^(1-s)` is unbounded.

    Note what is *not* needed: no lower bound on `β`, no fit, and no
    precision claim.  `beta_mem` supplies `β ≤ 1` and this supplies `β ≥ 1`. -/
-- Ref: [leitner2026] fluid-dynamics/levi-degeneracy-conjecture (branch B)
theorem linear_condNumber_forces_beta_one {P : Prop} (T : LeviGrowthTrichotomy P)
    (A : ℝ) (hA : 0 < A) (N₀ : ℕ)
    (hlin : ∀ κ : ℕ, N₀ ≤ κ → A * κ ≤ T.condNumber κ) :
    T.beta = 1 := by
  by_contra hne
  have hlt : T.beta < 1 := lt_of_le_of_ne T.beta_mem.2 hne
  set s : ℝ := (1 + T.beta) / 2 with hs
  have hs_lt_one : s < 1 := by rw [hs]; linarith
  have hε : 0 < s - T.beta := by rw [hs]; linarith
  obtain ⟨N, hN⟩ := T.beta_upper (s - T.beta) hε
  have hsum : T.beta + (s - T.beta) = s := by ring
  -- pick an index past both thresholds at which `n^(1-s)` already exceeds `1/A`
  have hinvA : (0 : ℝ) ≤ 1 / A := by positivity
  obtain ⟨n, hnM, hbig⟩ :=
    exists_large_rpow (1 / A) hinvA (1 - s) (by linarith) (max N N₀)
  have hnN : N ≤ n := le_trans (le_max_left _ _) hnM
  have hnN₀ : N₀ ≤ n := le_trans (le_max_right _ _) hnM
  have hn0 : (0 : ℝ) < (n : ℝ) := by
    by_contra h
    push_neg at h
    have : (n : ℝ) = 0 := le_antisymm h (Nat.cast_nonneg n)
    rw [this] at hbig
    rw [Real.zero_rpow (by linarith)] at hbig
    linarith
  -- the upper exponent, at this index
  have hub : T.condNumber n ≤ (n : ℝ) ^ s := by
    have := hN n hnN
    rwa [hsum] at this
  have hub : A * (n : ℝ) ≤ (n : ℝ) ^ s := le_trans (hlin n hnN₀) hub
  -- split `n = n^s · n^(1-s)` and cancel `n^s > 0`
  have hsplit : (n : ℝ) ^ s * (n : ℝ) ^ (1 - s) = (n : ℝ) := by
    rw [← Real.rpow_add hn0, show s + (1 - s) = 1 by ring, Real.rpow_one]
  have hps : (0 : ℝ) < (n : ℝ) ^ s := Real.rpow_pos_of_pos hn0 s
  have hcancel : A * (n : ℝ) ^ (1 - s) ≤ 1 := by
    have h2 : (n : ℝ) ^ s * (A * (n : ℝ) ^ (1 - s)) ≤ (n : ℝ) ^ s * 1 := by
      rw [mul_one]
      calc (n : ℝ) ^ s * (A * (n : ℝ) ^ (1 - s))
          = A * ((n : ℝ) ^ s * (n : ℝ) ^ (1 - s)) := by ring
        _ = A * (n : ℝ) := by rw [hsplit]
        _ ≤ (n : ℝ) ^ s := hub
    exact le_of_mul_le_mul_left h2 hps
  -- but the index was chosen so that `n^(1-s) > 1/A`
  have : 1 < A * (n : ℝ) ^ (1 - s) := by
    rw [mul_comm]; exact (div_lt_iff₀ hA).mp hbig
  linarith

/-- **Branch B fires**: under linear growth the Levi form degenerates.

    This is the payoff — `branchB` is a field of the carrier, and this is
    the first place in the corpus where its hypothesis is *derived* from the
    condition number rather than assumed. -/
-- Ref: [leitner2026] fluid-dynamics/levi-degeneracy-conjecture (branch B)
theorem linear_condNumber_degenerate {P : Prop} (T : LeviGrowthTrichotomy P)
    (A : ℝ) (hA : 0 < A) (N₀ : ℕ)
    (hlin : ∀ κ : ℕ, N₀ ≤ κ → A * κ ≤ T.condNumber κ) :
    ¬ P :=
  T.branchB (linear_condNumber_forces_beta_one T A hA N₀ hlin)

/-- **Eventually** `c < κ^e`, in the "for all large κ" form `beta_upper`
    needs — `exists_large_rpow` gives one index, monotonicity of `x ↦ x^e`
    in the base extends it. -/
theorem eventually_lt_rpow (c : ℝ) (hc : 0 ≤ c) (e : ℝ) (he : 0 < e) :
    ∃ N : ℕ, 1 ≤ N ∧ ∀ κ : ℕ, N ≤ κ → c < (κ : ℝ) ^ e := by
  obtain ⟨N, hN1, hNc⟩ := exists_large_rpow c hc e he 1
  refine ⟨N, hN1, fun κ hκ => ?_⟩
  have hle : (N : ℝ) ≤ (κ : ℝ) := by exact_mod_cast hκ
  exact lt_of_lt_of_le hNc (Real.rpow_le_rpow (Nat.cast_nonneg N) hle he.le)

/-! ### The linear case is realizable

Without this the theorem above could be about an empty class.  The witness
is `C_L(κ) = A·(κ+1)` — linear, and positive at every index including `κ = 0`,
which `A·κ` is not. -/

/-- A `LeviGrowthTrichotomy` with linearly growing condition number and
    `β = 1`.  `beta_upper` and `beta_lower` are the two halves of the
    limsup; both reduce to the rpow-growth lemmas after splitting
    `κ^(1±ε) = κ · κ^(±ε)`. -/
noncomputable def linearTrichotomy (A : ℝ) (hA : 0 < A) :
    LeviGrowthTrichotomy False where
  condNumber := fun κ => A * ((κ : ℝ) + 1)
  condNumber_pos := fun κ => by positivity
  beta := 1
  beta_mem := ⟨zero_le_one, le_refl 1⟩
  beta_upper := by
    intro ε hε
    obtain ⟨N, hN1, hNb⟩ := eventually_lt_rpow (2 * A) (by positivity) ε hε
    refine ⟨N, fun κ hκ => ?_⟩
    have hκ1 : 1 ≤ (κ : ℝ) := by exact_mod_cast le_trans hN1 hκ
    have hκ0 : (0 : ℝ) < (κ : ℝ) := by linarith
    have hsplit : (κ : ℝ) ^ (1 + ε) = (κ : ℝ) * (κ : ℝ) ^ ε := by
      rw [Real.rpow_add hκ0, Real.rpow_one]
    rw [hsplit]
    have hgrow : 2 * A < (κ : ℝ) ^ ε := hNb κ hκ
    calc A * ((κ : ℝ) + 1) ≤ A * (2 * (κ : ℝ)) := by nlinarith
      _ = (κ : ℝ) * (2 * A) := by ring
      _ ≤ (κ : ℝ) * (κ : ℝ) ^ ε := by nlinarith
  beta_lower := by
    intro ε hε N
    obtain ⟨κ, hκN, hbig⟩ :=
      exists_large_rpow (1 / A) (by positivity) ε hε (max N 1)
    refine ⟨κ, le_trans (le_max_left _ _) hκN, ?_⟩
    have hκ1 : 1 ≤ (κ : ℝ) := by
      exact_mod_cast le_trans (le_max_right _ _) hκN
    have hκ0 : (0 : ℝ) < (κ : ℝ) := by linarith
    have hsplit : (κ : ℝ) ^ (1 - ε) * (κ : ℝ) ^ ε = (κ : ℝ) := by
      rw [← Real.rpow_add hκ0, show 1 - ε + ε = 1 by ring, Real.rpow_one]
    have hpe : (0 : ℝ) < (κ : ℝ) ^ ε := Real.rpow_pos_of_pos hκ0 ε
    have hinv : 1 < A * (κ : ℝ) ^ ε := by
      rw [mul_comm]; exact (div_lt_iff₀ hA).mp hbig
    -- `κ^(1-ε) = κ / κ^ε ≤ A·κ ≤ A·(κ+1)`
    have hstep : (κ : ℝ) ^ (1 - ε) * (κ : ℝ) ^ ε ≤ (A * ((κ : ℝ) + 1)) * (κ : ℝ) ^ ε := by
      rw [hsplit]
      nlinarith
    exact le_of_mul_le_mul_right hstep hpe
  branchA := by intro h; norm_num at h
  branchB := fun _ => id

/-- The witness really is in branch B: `β = 1`, so `linear_condNumber_degenerate`
    applies to it. -/
example (A : ℝ) (hA : 0 < A) : (linearTrichotomy A hA).beta = 1 := rfl

end QOU.FluidDynamics
