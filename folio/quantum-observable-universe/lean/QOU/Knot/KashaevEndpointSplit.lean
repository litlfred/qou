/-
  The endpoint, split off exactly — bean `qou-mlgp` (A).

  THE OBSTRUCTION THIS REMOVES.  Every previous attempt at (A) foundered at
  `j = 0`, where `log(2 sin(jπ/N)) → −∞`.  Euler–Maclaurin does not apply to a
  singular integrand, and that endpoint is exactly where the `−½log N` and the
  additive constant of

      s_k = (N/π)·Λ(θ) − ½·log(2N sin θ) + O(1/N),      θ = kπ/N

  come from.  `KashaevProdEndpoint.lean` pinned the far endpoint and
  `KashaevReflectionTrapezoid.lean` disposed of the symmetric half; both left
  `j = 0` untouched, and the reflection provably cannot reach it (it pairs `k`
  with `N−1−k`, and both endpoints sit outside that pairing).

  THE MOVE.  Do not estimate the singularity — SUBTRACT it.  Writing
  `log(2 sin x) = log(2x) + logSinc x` with `logSinc x := log(sin x) − log x`,

      ∑_{j=1}^{k} log(2 sin(jπ/N)) = k·log(2π/N) + log(k!) + ∑_{j=1}^{k} logSinc(jπ/N)

  exactly, for every `N` and every `k < N` (`sum_log_two_sin_split`).  All three
  pieces are now benign:

    * `k·log(2π/N)` is closed form;
    * `log(k!)` is Stirling — `Real.Stirling.le_log_factorial_stirling` in
      Mathlib gives `k log k − k + ½log k + ½log(2π) ≤ log k!` effectively, for
      every `k ≠ 0`;
    * `∑ logSinc(jπ/N)` is a Riemann sum of a function that is CONTINUOUS at `0`
      (`logSinc → 0`) and EVEN (`logSinc_neg` below), hence has vanishing odd
      derivatives at `0`.  Euler–Maclaurin applies with no singular endpoint at
      all.

  THAT THE BOOKKEEPING CLOSES is checked in
  `computations/probes/kashaev_endpoint_split_probe.py` (5 assertions):
  the split is exact; the `logSinc` sum minus its Euler–Maclaurin approximant is
  `O(h³)` with `|·|·N³ = 0.0222` flat to 1.0001× across `N = 100…800`; and
  reassembling gives `s_k` to `O(1/N³)` with `|·|·N³ = 0.0669` flat to
  1.007× across `N = 400…1600`.  In the reassembly the
  `+1/(12k)` of Stirling and the `−(h/12)·(1/θ)` coming from
  `logSinc′(x) = cot x − 1/x` cancel identically, leaving exactly the measured
  `−(π/12N)·cot θ`.

  WHAT REMAINS, AND THE PRECISE MATHLIB GAP.  Two things.
    (1) Euler–Maclaurin for a smooth function on a compact interval — needed to
        turn `∑ logSinc(jh)` into `(1/h)∫₀^θ logSinc + ½logSinc(θ) + (h/12)·
        logSinc′(θ) + O(h³)`.  Mathlib has `Polynomial.bernoulli` and
        `sum_range_pow_eq_bernoulli` but no Euler–Maclaurin summation formula.
    (2) The `1/(12k)` term of Stirling.  Mathlib's own docstring on
        `le_log_factorial_stirling` says so: "Sharper bounds due to Robbins are
        available, but are not yet formalised. These would add lower order terms
        (beginning with `(12 * n)⁻¹`)."  Without it the reassembly proves the
        `O(1/N)` form of (A) but not the `−(π/12N)cot θ` refinement, because the
        cancellation above needs both halves.

  So (A) is no longer blocked on a singularity.  It is blocked on two standard,
  clearly-named pieces of analysis that Mathlib does not yet have.

  -- Ref: [leitner2026] QOU/Knot/KashaevProdEndpoint.lean
  -- Ref: [leitner2026] QOU/Knot/KashaevReflectionTrapezoid.lean
  -- Ref: [leitner2026] computations/probes/kashaev_endpoint_split_probe.py
  -- Ref: [leitner2026] computations/probes/kashaev_reflection_probe.py
-/
import QOU.Knot.KashaevReflectionTrapezoid

namespace QOU.Knot.FigureEightVolume

open Real

/-- `logSinc x = log(sin x) − log x`, i.e. `log(sin x / x)` where that is
defined.  The regular part of `log(2 sin)` after the `log(2x)` singularity is
subtracted. -/
noncomputable def logSinc (x : ℝ) : ℝ := Real.log (Real.sin x) - Real.log x

/-- `logSinc 0 = 0` — the singularity really is gone (`Real.log 0 = 0` in
Mathlib's convention, and `sin 0 = 0`, so both terms vanish).  The analytic
content is that `log(sin x / x) → 0` as `x → 0`; this is the value the
continuous extension takes. -/
@[simp] theorem logSinc_zero : logSinc 0 = 0 := by
  simp [logSinc]

/-- **`logSinc` is even.**  Hence every odd derivative vanishes at `0`, which is
why the Euler–Maclaurin expansion of `∑ logSinc(jh)` has no `h`-order endpoint
contribution at the left end — the reason the split works. -/
theorem logSinc_neg (x : ℝ) : logSinc (-x) = logSinc x := by
  simp [logSinc, Real.sin_neg, Real.log_neg_eq_log]

/-- **The endpoint split.**

    ∑_{j=1}^{k} log(2 sin(jπ/N)) = k·log(2π/N) + log(k!) + ∑_{j=1}^{k} logSinc(jπ/N)

exact, for every `N ≠ 0` and every `k < N`.  Each term is
`log(2 sin x) = log(2π/N) + log j + logSinc x` at `x = jπ/N`; summing the
`log j` gives `log(k!)`.

This is the step that removes the `j = 0` singularity from (A): the left side is
singular termwise as `j/N → 0`, the right side is a closed form plus a factorial
plus a sum of a function continuous at `0`. -/
theorem sum_log_two_sin_split {N k : ℕ} (hN : N ≠ 0) (hk : k < N) :
    ∑ j ∈ Finset.Ico 1 (k + 1), Real.log (2 * Real.sin ((j : ℝ) * π / N))
      = (k : ℝ) * Real.log (2 * π / N) + Real.log (Nat.factorial k)
        + ∑ j ∈ Finset.Ico 1 (k + 1), logSinc ((j : ℝ) * π / N) := by
  have hNR : (0 : ℝ) < N := by exact_mod_cast Nat.pos_of_ne_zero hN
  have hpi : (0 : ℝ) < π := Real.pi_pos
  -- `∑_{j=1}^{m} log j = log (m!)`
  have hfact : ∀ m : ℕ, ∑ j ∈ Finset.Ico 1 (m + 1), Real.log (j : ℝ)
      = Real.log (Nat.factorial m) := by
    intro m
    induction m with
    | zero => simp
    | succ n ih =>
      rw [Finset.sum_Ico_succ_top (by omega : 1 ≤ n + 1), ih, Nat.factorial_succ]
      have hne : ((Nat.factorial n : ℕ) : ℝ) ≠ 0 := by
        exact_mod_cast Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero n)
      push_cast
      rw [Real.log_mul (by positivity) hne]
      ring
  -- the termwise identity
  have hterm : ∀ j ∈ Finset.Ico 1 (k + 1),
      Real.log (2 * Real.sin ((j : ℝ) * π / N))
        = Real.log (2 * π / N) + Real.log (j : ℝ) + logSinc ((j : ℝ) * π / N) := by
    intro j hj
    rw [Finset.mem_Ico] at hj
    have hjR : (0 : ℝ) < (j : ℝ) := by exact_mod_cast hj.1
    have hx : (0 : ℝ) < (j : ℝ) * π / N := by positivity
    have hjlt : (j : ℝ) < (N : ℝ) := by exact_mod_cast (by omega : j < N)
    have hxlt : (j : ℝ) * π / N < π := by
      rw [div_lt_iff₀ hNR]; nlinarith
    have hsin : 0 < Real.sin ((j : ℝ) * π / N) :=
      Real.sin_pos_of_pos_of_lt_pi hx hxlt
    have h1 : Real.log ((j : ℝ) * π / N) = Real.log (j : ℝ) + Real.log (π / N) := by
      rw [show (j : ℝ) * π / N = (j : ℝ) * (π / N) by ring]
      exact Real.log_mul (ne_of_gt hjR) (by positivity)
    have h2 : Real.log (2 * π / N) = Real.log 2 + Real.log (π / N) := by
      rw [show (2 : ℝ) * π / N = 2 * (π / N) by ring]
      exact Real.log_mul (by norm_num) (by positivity)
    simp only [logSinc]
    rw [Real.log_mul (by norm_num) (ne_of_gt hsin), h1, h2]
    ring
  rw [Finset.sum_congr rfl hterm, Finset.sum_add_distrib, Finset.sum_add_distrib,
    Finset.sum_const, hfact k, Nat.card_Ico]
  simp only [Nat.add_sub_cancel, nsmul_eq_mul]

end QOU.Knot.FigureEightVolume
