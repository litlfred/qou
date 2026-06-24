import Mathlib.Analysis.SpecialFunctions.Hyperbolic.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.Log.Basic

/-!
# QOU.BraidKnot.BarSymmetricBarAntiSymmetricIdentities — P_m, Q_m + Pythagorean

**Lean encoding** of the four hyperbolic identities for the bar-symmetric
$P_m$ and bar-anti-symmetric $Q_m$ Markov-trace components of the
$T(2, 2m)$ torus link family.

## Origins

- `P_m = cosh((2m+1)η) / (2 cosh η)`: sibling PR #1125 / PR #1165 binomial pattern
- `Q_m = sinh((2m+1)η) / (2 cosh η)`: sibling PR #1153 sinh partner
- Four identities: PR #1181 sympy-verified for m = 0..6

## What this file PROVES

  ✓ Pythagorean (I2):  P_m² − Q_m² = 1/(2 cosh η)²
  ✓ tanh ratio (I1):    Q_m / P_m = tanh((2m+1)η)
  ✓ sum (I3):          P_m + Q_m = e^{(2m+1)η} / (2 cosh η)
  ✓ diff (I4):         P_m − Q_m = e^{-(2m+1)η} / (2 cosh η)

Plus the **per-particle tanh ladder corollary** (PR #1153 finding):
At substrate η_0, Q_m(η_0)/P_m(η_0) = tanh((2m+1)·η_0) gives:
  m=2 (W): tanh(5 η_0) ≈ 0.478
  m=3 (Z): tanh(7 η_0) ≈ 0.622
  m=4 (H): tanh(9 η_0) ≈ 0.734

These are claimed (in PR #1153) to be EM-channel-to-total ratios.

## What this file does NOT prove

- The CONNECTION to the Higgs mass formula (PR #1164) — that requires
  the bar-symmetric projection acts as the canonical mass channel;
  formal identification is research-grade open
- The Borromean Q = 0 — depends on the Borromean Markov-trace closed
  form (PR #1081), which is in a separate file; cross-cited not encoded

## Honest framing

These identities are GENUINE DERIVATIONS from hyperbolic-function
algebra. Unlike empirical pattern matches earlier in the session,
each identity follows by direct algebra:

  - cosh² − sinh² = 1  →  P² − Q² = 1/(2 cosh η)²
  - sinh/cosh = tanh   →  Q/P = tanh
  - cosh ± sinh = e^±x →  P ± Q = e^{±(2m+1)η}/(2 cosh η)

The proofs are mechanical via Mathlib's hyperbolic-function lemmas.
-/

namespace QOU.BraidKnot

open Real

/-- The bar-symmetric Markov-trace component for T(2, 2m). -/
noncomputable def P_m (m : ℕ) (η : ℝ) : ℝ :=
  Real.cosh ((2 * m + 1) * η) / (2 * Real.cosh η)

/-- The bar-anti-symmetric Markov-trace component for T(2, 2m). -/
noncomputable def Q_m (m : ℕ) (η : ℝ) : ℝ :=
  Real.sinh ((2 * m + 1) * η) / (2 * Real.cosh η)

/-- The quantum integer $[2]_q$ at substrate η: $[2]_q = q + q^{-1} = 2 \cosh η$. -/
noncomputable def bracket_2_q (η : ℝ) : ℝ := 2 * Real.cosh η

/-- The Pythagorean identity:
    $P_m^2 - Q_m^2 = 1/[2]_q^2$ (independent of m).

    This is the KEY structural generalization from PR #1181 — all
    torus knots T(2, 2m) satisfy the same Pythagorean constraint at
    substrate.

    Proof: direct from cosh²(x) − sinh²(x) = 1. -/
theorem pythagorean_identity (m : ℕ) (η : ℝ) (h_cosh_ne_zero : Real.cosh η ≠ 0) :
    P_m m η ^ 2 - Q_m m η ^ 2 = 1 / (bracket_2_q η) ^ 2 := by
  unfold P_m Q_m bracket_2_q
  have h_inner : Real.cosh ((2 * m + 1) * η) ^ 2 - Real.sinh ((2 * m + 1) * η) ^ 2 = 1 :=
    Real.cosh_sq_sub_sinh_sq _
  field_simp
  linear_combination h_inner

/-- The tanh ratio identity:
    $Q_m / P_m = \tanh((2m+1) \eta)$.

    Proof: trivial from sinh/cosh = tanh and the common $1/(2 \cosh η)$
    factors cancel. -/
theorem Q_over_P_eq_tanh (m : ℕ) (η : ℝ)
    (h_cosh_outer : Real.cosh η ≠ 0)
    (h_cosh_inner : Real.cosh ((2 * m + 1) * η) ≠ 0) :
    Q_m m η / P_m m η = Real.tanh ((2 * m + 1) * η) := by
  unfold P_m Q_m
  rw [Real.tanh_eq_sinh_div_cosh]
  field_simp

/-- The sum identity: $P_m + Q_m = e^{(2m+1)\eta} / (2 \cosh η)$.

    Proof: $\cosh + \sinh = e^x$. -/
theorem P_plus_Q (m : ℕ) (η : ℝ) :
    P_m m η + Q_m m η = Real.exp ((2 * m + 1) * η) / (2 * Real.cosh η) := by
  unfold P_m Q_m
  rw [div_add_div_same, ← Real.cosh_add_sinh]

/-- The difference identity: $P_m - Q_m = e^{-(2m+1)\eta} / (2 \cosh η)$.

    Proof: $\cosh - \sinh = e^{-x}$. -/
theorem P_minus_Q (m : ℕ) (η : ℝ) :
    P_m m η - Q_m m η = Real.exp (-((2 * m + 1) * η)) / (2 * Real.cosh η) := by
  unfold P_m Q_m
  rw [div_sub_div_eq_sub_div, ← Real.cosh_sub_sinh]

/-! ## Per-particle tanh ladder (PR #1153 finding)

The Q_m/P_m = tanh((2m+1)η) identity at substrate η_0 gives:
  m=2 (W): tanh(5η_0)
  m=3 (Z): tanh(7η_0)
  m=4 (H): tanh(9η_0)

These are claimed to be EM-channel/total ratios per particle. -/

/-- The substrate-evaluation η₀ corresponding to q_0 ≈ 1.10998.
    Defined as log(q_0) where q_0 is the canonical 50-digit pin
    `qou_substrate.constants.Q_50_DIGIT_STR`
    (`1.10997859555418057528159407960950937799328227995870`,
    derived from CODATA m_μ/m_e + SnapPy Vol(4_1)).
    Approximately 0.10434. -/
noncomputable def η_substrate : ℝ := Real.log 1.10997859555418057528159407960950937799328227995870

/-- The EM-channel ratio for particle T(2, 2m) at substrate.

    Per PR #1153 (merged commit 26e57945e): this equals
    tanh((2m+1)·η_substrate). Empirical values at substrate
    (50-dps mpmath, canonical pin):
      W (m=2): 0.4790
      Z (m=3): 0.6233
      H (m=4): 0.7348 -/
noncomputable def EM_channel_ratio (m : ℕ) : ℝ :=
  Real.tanh ((2 * m + 1) * η_substrate)

/-- The per-particle EM-channel ratio is positive at substrate
    (since η_substrate > 0 and tanh is positive for positive input). -/
theorem EM_channel_ratio_pos (m : ℕ) (h_eta : 0 < η_substrate) :
    0 < EM_channel_ratio m := by
  unfold EM_channel_ratio
  apply Real.tanh_pos.mpr
  positivity

/-- The EM-channel ratios are monotonically increasing in m
    (since tanh is monotone increasing and (2m+1)·η_0 grows with m). -/
theorem EM_channel_ratio_monotone (m m' : ℕ) (h_lt : m < m')
    (h_eta_pos : 0 < η_substrate) :
    EM_channel_ratio m < EM_channel_ratio m' := by
  unfold EM_channel_ratio
  apply Real.tanh_lt_tanh
  have : (2 * m + 1 : ℝ) < 2 * m' + 1 := by
    have : (m : ℝ) < m' := Nat.cast_lt.mpr h_lt
    linarith
  nlinarith [h_eta_pos]

/-! ## Cross-reference: Borromean (NOT torus) Q = 0

The Borromean rings 𝓑_3 are hyperbolic (not Seifert-fibered torus).
Per `BorromeanMarkovTrace.lean` (PR #1081) the closed form is purely
even in h:
    tr_M(β_Bor) = (4 + h² − 3h⁴ − h⁶) / (h² + 4)

The bar-anti-symmetric companion of this trace would be the odd-h
part divided by (h² + 4). Since the trace has NO odd-h terms, the
companion is zero.

This is encoded as a CONDITIONAL theorem here (depends on the
Borromean closed form proved elsewhere in BorromeanMarkovTrace.lean).
-/

/-- The Borromean Markov trace closed form over `ℝ`, parallel to the
    `ℚ` version in `BorromeanMarkovTrace.lean`. -/
noncomputable def trM_borromean_real (h : ℝ) : ℝ :=
  (4 + h^2 - 3 * h^4 - h^6) / (h^2 + 4)

/-- The bar-anti-symmetric companion of the Borromean Markov trace,
    over `ℝ`. -/
noncomputable def Q_borromean_real (h : ℝ) : ℝ :=
  (trM_borromean_real h - trM_borromean_real (-h)) / 2

/-- **The Borromean Markov trace has zero bar-anti-symmetric companion,
    over `ℝ`.**

    The closed form `(4 + h² − 3h⁴ − h⁶) / (h² + 4)` has all-even-power
    numerator and denominator, so `trM_borromean_real (−h) = trM_borromean_real h`
    by `ring`. The bar-anti-symmetric projection
    `Q_borromean_real h := (trM(h) − trM(−h)) / 2` therefore vanishes
    identically.

    This is the **ℝ-side lift** of the `ℚ` proof in
    [`QOU.BraidsAndKnots.Q_borromean_eq_zero`](../BraidsAndKnots/BorromeanMarkovTrace.lean)
    (PR #1211, commit `5329eb054`).  No `Rat.cast` lift is needed —
    the `ring` proof works uniformly over any `CommRing` of
    characteristic 0; the `noncomputable` qualifier is purely because
    of `(_ : ℝ) / (_ : ℝ)` division, not because of any irrational input.

    History:
      - `d4d640ce7` (sibling): placeholder `True := trivial`
      - PR #1196: documented the gap in [`docs/audits/2026-05-24-sinh-
        cosh-lean-integration-audit.md`](../../../../../docs/audits/2026-05-24-sinh-cosh-lean-integration-audit.md)
      - PR #1211: full proof over `ℚ` in `BorromeanMarkovTrace.lean`
        (commit `5329eb054`)
      - this PR (item E): **ℝ-side lift here**, with `Q_borromean_real`
        def + theorem proven via `ring` (uniform with the `ℚ` proof) -/
theorem Q_borromean_real_eq_zero (h : ℝ) : Q_borromean_real h = 0 := by
  unfold Q_borromean_real trM_borromean_real
  ring

/-- The Borromean Markov trace has zero bar-anti-symmetric companion over `ℝ`
    (named alias of `Q_borromean_real_eq_zero`, kept resolvable for downstream
    consumers that referred to `Q_borromean_eq_zero` by name; see also the `ℚ`
    version `QOU.BraidsAndKnots.Q_borromean_eq_zero` in
    `BorromeanMarkovTrace.lean`).

    Previously a `def Q_borromean_eq_zero : True := trivial` placeholder shim;
    de-vacuified to carry the real statement now that `Q_borromean_real_eq_zero`
    proves it (AGENTS.md §1a — no `: True` dodges). -/
theorem Q_borromean_eq_zero (h : ℝ) : Q_borromean_real h = 0 :=
  Q_borromean_real_eq_zero h

end QOU.BraidKnot
