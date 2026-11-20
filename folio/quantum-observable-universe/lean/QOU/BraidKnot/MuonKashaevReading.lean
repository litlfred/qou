/-
Copyright (c) 2026 litlfred. All rights reserved.

# The muon carrier as the leading saddle of the 4₁ Kashaev series

Bean `qou-6gf9` (lepton self-energy front, owner 2026-11-20).
Audit: `docs/audits/2026-11-20-lepton-self-energy-front.md`.
Probe: `computations/probes/mu_kashaev_reading_probe.py`.

## The question

The CAL-2 relation `m_μ/m_e = Vol(4₁)/ℏ_q²` (with `ℏ_q = 1 − q⁻¹`) is
described in the corpus as "the Kashaev limit". If that is meant literally,
the relation is the **leading term** of the 4₁ Kashaev asymptotic series and
its first correction is **fixed by that series** — no free coefficient. This
file states what "literally" forces and proves what the forced correction does.

## The series (literature, cited — not proved here)

Andersen–Hansen (quoted in the held source `[murakami-h2011]` Thm 1.2):

  `J_N(4₁; e^{2πi/N}) ∼ 3^{-1/4} · N^{3/2} · exp(N·Vol(4₁)/2π)`,

with twisted Reidemeister torsion `2/√−3` and Chern–Simons invariant
`i·Vol(4₁)` (so `CS(4₁) = 0`: no phase term). The full Ohtsuki expansion is

  `log J_N = N·Vol/2π + (3/2)·log N − (1/4)·log 3 + Σ_{n ≥ 1} κ_n / N^n`,

with the corpus's exact identifications (`2026-07-12-ohtsuki-higher-rungs-exact`,
numerically exact, 19–36 digits; **not** Lean-proved):
`κ₁ = 11√3π/108`, `κ₂ = 2π²/27`, `κ₃ = 1081√3π³/21870`, `κ₄ = 98π⁴/729`.

## What this file proves (sorry-free)

1. `leading_match_forces_hbar_sq` (generic `[Field K]`): matching the leading
   term `Vol/ℏ_K` of the Kashaev exponent to `Vol/ℏ_q²` forces
   `ℏ_K = ℏ_q²` — the reading is not free. (With `ℏ_K = ℏ_q` the leading term
   would be `Vol/ℏ_q ≈ 20.5`, not `≈ 206.8`.)
2. `kashaevTrunc_sub_leading_ge`: for `N ≥ 1` and non-negative rungs, every
   finite truncation exceeds the leading term by at least the one-loop piece
   `(3/2)·log N + c₀`.
3. `one_loop_4_1_gt`: for the 4₁ constant `c₀ = −(1/4)·log 3` and `N ≥ 2`,
   the one-loop piece exceeds `log 2 > 0.693`; `two_thirds_lt_one_loop_4_1`.
4. `kappa_4_1_nonneg`: the four identified Ohtsuki rungs are positive.
5. `kashaev_reading_excluded` (capstone): if the measured ratio `r` lies
   **below** `Vol/ℏ_q²` — which is the measured sign of the μ–p residual at
   the proton pin (+211 ppb high) — then **no** finite truncation of the 4₁
   series with non-negative rungs can equal `r`; and the gap is at least
   `2/3` in absolute units (`kashaev_reading_gap`).

## Scope

(b) relative to the stated class: "`m_μ/m_e` is a finite truncation of the
4₁ Kashaev log-series at `N = 2π/ℏ_q²`, with non-negative Ohtsuki rungs".
Named invariant: the sign of the one-loop term (`log 3 < 6·log 2`). The
measured sign of the residual enters as the hypothesis `hr`, not as a fact
proved here. For the actual 4₁ rungs the hypothesis `hκ` is discharged at
`m ≤ 4` by `kappa_4_1_nonneg`; beyond `m = 4` it is carried.

Not covered: readings in which the relation is *not* the Kashaev exponent
(multiplicative-amplitude readings are covered by the monomial order window in
`MuPCarrierOrderWindow.lean`), and evaluations off the root of unity (the
Murakami `ξ = 2πi + u` deformation, `[murakami-h2011]` Thm 1.3).
-/
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Analysis.Complex.ExponentialBounds

namespace QOU.BraidKnot.MuonKashaev

open Real Finset

/-! ## §1  Generic: the leading-term identification is forced -/

/-- Matching the Kashaev leading exponent `V/ℏ_K` to the CAL-2 carrier `V/ℏ_q²`
forces `ℏ_K = ℏ_q²`. Generic over any field; no archimedean content. -/
theorem leading_match_forces_hbar_sq {K : Type*} [Field K] {V hK hq : K}
    (hV : V ≠ 0) (hK0 : hK ≠ 0) (hq0 : hq ≠ 0) (heq : V / hK = V / hq ^ 2) :
    hK = hq ^ 2 := by
  have hq2 : hq ^ 2 ≠ 0 := pow_ne_zero 2 hq0
  rw [div_eq_div_iff hK0 hq2] at heq
  exact (mul_left_cancel₀ hV heq).symm

/-- With `N := 2π/ℏ_K`, the Kashaev leading term `N·V/(2π)` is `V/ℏ_K`. -/
theorem leading_term_eq {V hK : ℝ} (hK0 : hK ≠ 0) :
    (2 * π / hK) * V / (2 * π) = V / hK := by
  have : (2 * π) ≠ 0 := by positivity
  field_simp

/-! ## §2  The truncated 4₁ Kashaev log-series -/

/-- Finite truncation at order `m` of the Kashaev log-series
`N·V/2π + (3/2)·log N + c₀ + Σ_{n=1}^{m} κ_n / N^n`. -/
noncomputable def kashaevTrunc (V c0 : ℝ) (κ : ℕ → ℝ) (m : ℕ) (N : ℝ) : ℝ :=
  N * V / (2 * π) + 3 / 2 * Real.log N + c0 + ∑ n ∈ Icc 1 m, κ n / N ^ n

/-- The 4₁ one-loop constant `c₀ = log 3^{-1/4} = −(1/4)·log 3`
(Andersen–Hansen prefactor). -/
noncomputable def c0_4_1 : ℝ := -(Real.log 3) / 4

/-- Every truncation with non-negative rungs sits at least the one-loop piece
above the leading term. -/
theorem kashaevTrunc_sub_leading_ge (V c0 : ℝ) (κ : ℕ → ℝ) (m : ℕ) {N : ℝ}
    (hN : 1 ≤ N) (hκ : ∀ n ∈ Icc 1 m, 0 ≤ κ n) :
    3 / 2 * Real.log N + c0 ≤ kashaevTrunc V c0 κ m N - N * V / (2 * π) := by
  unfold kashaevTrunc
  have hN0 : 0 < N := by linarith
  have hsum : 0 ≤ ∑ n ∈ Icc 1 m, κ n / N ^ n :=
    sum_nonneg fun n hn => div_nonneg (hκ n hn) (pow_nonneg hN0.le n)
  linarith

/-- `log 3 < 2·log 2` (since `3 < 4`). -/
theorem log_three_lt_two_log_two : Real.log 3 < 2 * Real.log 2 := by
  have h4 : Real.log 4 = 2 * Real.log 2 := by
    rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow]; norm_num
  rw [← h4]
  exact Real.log_lt_log (by norm_num) (by norm_num)

/-- **One-loop dominance.** For `N ≥ 2` the 4₁ one-loop piece exceeds `log 2`. -/
theorem one_loop_4_1_gt {N : ℝ} (hN : 2 ≤ N) :
    Real.log 2 < 3 / 2 * Real.log N + c0_4_1 := by
  unfold c0_4_1
  have hlogN : Real.log 2 ≤ Real.log N := Real.log_le_log (by norm_num) hN
  have h3 := log_three_lt_two_log_two
  have h2pos : 0 < Real.log 2 := Real.log_pos (by norm_num)
  linarith

/-- Numerical floor: the 4₁ one-loop piece exceeds `2/3` for every `N ≥ 2`. -/
theorem two_thirds_lt_one_loop_4_1 {N : ℝ} (hN : 2 ≤ N) :
    (2 : ℝ) / 3 < 3 / 2 * Real.log N + c0_4_1 := by
  have h := one_loop_4_1_gt hN
  have hl := Real.log_two_gt_d9
  linarith

/-! ## §3  The identified 4₁ Ohtsuki rungs are positive -/

/-- The four identified 4₁ Ohtsuki rungs (corpus PSLQ identifications,
19–36 confirmed digits; see the module docstring). Zero beyond `n = 4`. -/
noncomputable def kappa_4_1 : ℕ → ℝ
  | 1 => 11 * Real.sqrt 3 * π / 108
  | 2 => 2 * π ^ 2 / 27
  | 3 => 1081 * Real.sqrt 3 * π ^ 3 / 21870
  | 4 => 98 * π ^ 4 / 729
  | _ => 0

theorem kappa_4_1_nonneg (n : ℕ) : 0 ≤ kappa_4_1 n := by
  have hs : 0 ≤ Real.sqrt 3 := Real.sqrt_nonneg 3
  have hp : 0 ≤ π := Real.pi_pos.le
  match n with
  | 0 => simp [kappa_4_1]
  | 1 => simp only [kappa_4_1]; positivity
  | 2 => simp only [kappa_4_1]; positivity
  | 3 => simp only [kappa_4_1]; positivity
  | 4 => simp only [kappa_4_1]; positivity
  | n + 5 => simp [kappa_4_1]

/-! ## §4  Capstone: the Kashaev reading of CAL-2 moves m_μ the wrong way -/

/-- **The gap.** At `N = 2π/ℏ_q²` (with `N ≥ 2`), every finite truncation of
the 4₁ series with non-negative rungs exceeds the CAL-2 carrier `V/ℏ_q²` by more
than `2/3`. -/
theorem kashaev_reading_gap (V hq : ℝ) (κ : ℕ → ℝ) (m : ℕ) (hq0 : hq ≠ 0)
    (hN : 2 ≤ 2 * π / hq ^ 2) (hκ : ∀ n ∈ Icc 1 m, 0 ≤ κ n) :
    V / hq ^ 2 + 2 / 3 < kashaevTrunc V c0_4_1 κ m (2 * π / hq ^ 2) := by
  have hlead := leading_term_eq (V := V) (pow_ne_zero 2 hq0)
  have h1 := kashaevTrunc_sub_leading_ge V c0_4_1 κ m (N := 2 * π / hq ^ 2)
    (by linarith) hκ
  have h2 := two_thirds_lt_one_loop_4_1 hN
  linarith

/-- **Exclusion (scope (b) for the stated class).** If the measured ratio `r`
lies below the CAL-2 carrier `V/ℏ_q²` — the measured sign of the μ–p residual at
the proton pin, carried as the hypothesis `hr` — then no finite truncation of
the 4₁ Kashaev log-series at `N = 2π/ℏ_q²` with non-negative rungs equals `r`. -/
theorem kashaev_reading_excluded (V hq r : ℝ) (κ : ℕ → ℝ) (m : ℕ) (hq0 : hq ≠ 0)
    (hN : 2 ≤ 2 * π / hq ^ 2) (hκ : ∀ n ∈ Icc 1 m, 0 ≤ κ n)
    (hr : r < V / hq ^ 2) :
    r ≠ kashaevTrunc V c0_4_1 κ m (2 * π / hq ^ 2) := by
  have := kashaev_reading_gap V hq κ m hq0 hN hκ
  intro h
  linarith

/-- The same, instantiated on the identified 4₁ rungs at any order `m`. -/
theorem kashaev_reading_excluded_4_1 (V hq r : ℝ) (m : ℕ) (hq0 : hq ≠ 0)
    (hN : 2 ≤ 2 * π / hq ^ 2) (hr : r < V / hq ^ 2) :
    r ≠ kashaevTrunc V c0_4_1 kappa_4_1 m (2 * π / hq ^ 2) :=
  kashaev_reading_excluded V hq r kappa_4_1 m hq0 hN
    (fun n _ => kappa_4_1_nonneg n) hr

end QOU.BraidKnot.MuonKashaev
