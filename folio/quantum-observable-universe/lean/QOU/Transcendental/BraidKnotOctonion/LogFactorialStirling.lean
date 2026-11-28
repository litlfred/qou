/-
# L4-1b — the Stirling half-log (bean qou-itg0, epic qou-u1b5)

Second sub-brick of L4-1 (feasibility pass
`docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md`).  van der
Veen's refined `s_n` expansion carries the constant contribution
"`−½ log n − ½ log 2π` … from the Stirling series used in [Zheng] p. 7";
this file supplies that input in log form, sorry-free, from Mathlib's
`Stirling.tendsto_stirlingSeq_sqrt_pi`:

    log(n!) − ( n·log n − n + ½·log n + ½·log(2π) )  →  0.

Mathlib states Stirling multiplicatively — `stirlingSeq n =
n! / (√(2n)·(n/e)^n) → √π` — so the whole content here is taking logs
and bookkeeping the split; no new analysis.  The remaining L4-1 input is
the uniform second-order cell remainder (`qou-q8lc`), the genuinely new
estimate.
-/

/-
**REDUNDANT (2026-08-19) — L4-1's target was already proved on `main`, stronger,
before this file was written.**

`QOU.Knot.FigureEightVolume.kashaev_log_sum_asymptotic`
(`QOU/Knot/KashaevAsymptotic.lean`, on main since 2026-08-10, sorry-free) gives

    | ∑_{j=1}^{k} log(2 sin(jπ/N))
        − ( −(N/π)·Lob(kπ/N) + ½·log(2N·sin(kπ/N)) + (π/(12N))·cot(kπ/N) ) |
      ≤ 1/(144k²) + (7/12)(π/N)² + (π/N)²/(12·sin²(kπ/N))

— strictly stronger than the L4-1 target this file serves: it identifies the
`O(1/N)` term and its error is effective.  The decomposition L4-1 was organised
around is `KashaevEndpointSplit.sum_log_two_sin_split`, exact algebra with no
cell integrals and no telescope.

Kept, not deleted: the proofs here are correct and sorry-free.  **New
downstream work should cite `kashaev_log_sum_asymptotic`, not this file.**
Audit: `docs/audits/2026-08-19-l41-was-already-proved-on-main.md`.
-/

import Mathlib.Analysis.SpecialFunctions.Stirling
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace QOU.Knot.FigureEightVolume

open Real

/-- `log` of Mathlib's Stirling sequence, expanded for `1 ≤ n`:
    `log(stirlingSeq n) = log(n!) − ½·log 2 − ½·log n − n·log n + n`. -/
theorem log_stirlingSeq_eq {n : ℕ} (hn : 1 ≤ n) :
    Real.log (Stirling.stirlingSeq n)
      = Real.log (n.factorial) - Real.log 2 / 2 - Real.log n / 2
        - (n : ℝ) * Real.log n + (n : ℝ) := by
  have hn0 : (0:ℝ) < n := by exact_mod_cast hn
  have hfac : (0:ℝ) < (n.factorial : ℝ) := by
    exact_mod_cast n.factorial_pos
  have he : (0:ℝ) < Real.exp 1 := Real.exp_pos 1
  have hsq : (0:ℝ) < Real.sqrt (2 * n) := Real.sqrt_pos.mpr (by linarith)
  have hpow : (0:ℝ) < ((n : ℝ) / Real.exp 1) ^ n := by positivity
  unfold Stirling.stirlingSeq
  rw [Real.log_div hfac.ne' (by positivity),
    Real.log_mul hsq.ne' hpow.ne',
    Real.log_sqrt (by linarith), Real.log_pow,
    Real.log_mul (by norm_num) hn0.ne',
    Real.log_div hn0.ne' he.ne', Real.log_exp]
  ring

/-- **L4-1b — the Stirling half-log (sorry-free).**  The additive Stirling
    expansion in exactly the shape vdV's `s_n` refinement consumes. -/
theorem tendsto_log_factorial_stirling :
    Filter.Tendsto (fun n : ℕ => Real.log (n.factorial)
        - ((n : ℝ) * Real.log n - (n : ℝ) + Real.log n / 2
            + Real.log (2 * π) / 2))
      Filter.atTop (nhds 0) := by
  have hpi := Real.pi_pos
  have hsqrt_pos : (0:ℝ) < Real.sqrt π := Real.sqrt_pos.mpr hpi
  -- log ∘ stirlingSeq → log √π = log π / 2
  have hlog := (Real.continuousAt_log hsqrt_pos.ne').tendsto.comp
    Stirling.tendsto_stirlingSeq_sqrt_pi
  rw [Real.log_sqrt hpi.le] at hlog
  have hsub := hlog.sub_const (Real.log π / 2)
  rw [sub_self] at hsub
  refine hsub.congr' ?_
  filter_upwards [Filter.eventually_ge_atTop 1] with n hn
  simp only [Function.comp_apply]
  rw [log_stirlingSeq_eq hn, Real.log_mul (by norm_num) hpi.ne']
  ring

end QOU.Knot.FigureEightVolume
