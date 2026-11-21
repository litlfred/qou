import QOU.FluidDynamics.levi_growth_trichotomy

/-!
# QOU.FluidDynamics.levi_pair_channel_branch_b — linear growth forces exponent `1` (re-scoped)

## 🛑 Re-scoped 2026-10-13 — no Levi condition number, no branch verdict

Owner ruling Q1 (2026-10-13) re-scoped the Levi chain onto `Θ = f·ξ♭` on the
3D flow domain (`prop:core-levi-form`). The Levi datum is the single scalar
`ξ·curl ξ`; the Levi condition number `C_L`, its growth exponent `β` and regime
(C) are withdrawn as undefined, branch (A) is withdrawn, and branch (B) is an
open conjecture on the Levi scalar (`conj:levi-degeneracy`,
`LeviDegeneracyQ1.LeviDegeneracy`).

This file used to read the anti-parallel-pair lock as "the Levi condition
number grows linearly, hence `β = 1`, hence branch (B) fires for the pair
channel". Under the ruling:

* **Kept (re-scoped to a fluid-shape quantity):** `linear_seq_forces_beta_one`
  (formerly `linear_condNumber_forces_beta_one`, deprecated alias kept) — a
  positive sequence eventually bounded below by `A·κ` has growth exponent `1`.
  Its corpus application is the **inverse squared Townsend core aspect ratio**
  `1/κ²_lock = Γ/(π ν_q)` along the ladder `ν_q = (q-1)/(2q)`, which is
  exactly linear in `1/ε` (`ε := q - 1`): `1/κ²_lock = (2Γ/π)(1+ε)/ε`. That is
  a statement about core shape (`rem:hyperbolic-overlap-saturation`,
  `rem:townsend-biot-savart-strain`), conditional on the lock formula, which is
  a phenomenological model input and is not derived. The fitted `0.9963` in
  `qns-levi-lock-scaling-probe.witness.json` is a finite-window artefact
  (`qns_levi_lock_beta_exact_probe.py`, 50 dps: secant exponent `0.96293` over
  `[10⁻¹,10⁻²]`, `1.0` over `[10⁻¹⁹,10⁻²⁰]`); that record stands as a
  statement about the aspect ratio.
* **Withdrawn:** `linear_condNumber_degenerate` ("branch B fires"). It consumed
  the `branchB` field of the former carrier, which is removed
  (`levi_growth_trichotomy.lean`). A straight anti-parallel pair has Levi scalar
  `0` for every core shape, so the aspect-ratio exponent carries no Levi
  verdict.
* `linearTrichotomy` becomes `linearGrowthExponent` (witness that the linear
  case is realised, so the theorem is not about an empty class).

## Base ring (§7c)
Archimedean: `β` is a `limsup` of real log-ratios and `Real.rpow` is the
statement. `ℝ` is correct.

## References
- [leitner2026] fluid-dynamics/levi-degeneracy-conjecture (`conj:levi-degeneracy`),
  hyperbolic-overlap-saturation (the lock `κ² = πν/Γ`), townsend-biot-savart-strain
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

/-- **A linearly growing sequence has exponent `1`.**

    The dual of `bounded_seq_forces_beta_zero`.  If `a_κ ≥ A·κ` eventually
    with `A > 0`, then no exponent below `1` can be an upper exponent:
    `beta_upper` at `ε = (1 - β)/2` would give `A·κ ≤ κ^s` with
    `s = (1+β)/2 < 1`, i.e. `A·κ^(1-s) ≤ 1` — but `κ^(1-s)` is unbounded.
    No fit and no precision claim enters.  (Its former reading as "branch B
    for the pair channel" is withdrawn; file docstring.) -/
-- Ref: [leitner2026] fluid-dynamics/hyperbolic-overlap-saturation (the lock)
theorem linear_seq_forces_beta_one (T : GrowthExponent)
    (A : ℝ) (hA : 0 < A) (N₀ : ℕ)
    (hlin : ∀ κ : ℕ, N₀ ≤ κ → A * κ ≤ T.seq κ) :
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
  have hub : T.seq n ≤ (n : ℝ) ^ s := by
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

@[deprecated linear_seq_forces_beta_one (since := "2026-10-13")]
alias linear_condNumber_forces_beta_one := linear_seq_forces_beta_one

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

/-- A `GrowthExponent` with linearly growing sequence and `β = 1`.  `beta_upper` and `beta_lower` are the two halves of the
    limsup; both reduce to the rpow-growth lemmas after splitting
    `κ^(1±ε) = κ · κ^(±ε)`. -/
noncomputable def linearGrowthExponent (A : ℝ) (hA : 0 < A) :
    GrowthExponent where
  seq := fun κ => A * ((κ : ℝ) + 1)
  seq_pos := fun κ => by positivity
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

/-- The witness has exponent `1`, consistently with
    `linear_seq_forces_beta_one`. -/
example (A : ℝ) (hA : 0 < A) : (linearGrowthExponent A hA).beta = 1 :=
  linear_seq_forces_beta_one (linearGrowthExponent A hA) A hA 0
    (fun κ _ => by simp only [linearGrowthExponent]; nlinarith)

end QOU.FluidDynamics
