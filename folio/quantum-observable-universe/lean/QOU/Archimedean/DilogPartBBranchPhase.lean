import QOU.Archimedean.DilogarithmArchimedeanLimit
import Mathlib.Analysis.SpecialFunctions.Complex.Log

/-!
# Part B of `conj:dilogarithm-archimedean-limit` — the per-factor branch phase

Part A (fixed `x∈(0,1)`, `q→1⁻`) is closed sorry-free: `ArchimedeanLimit x` is
inhabited off `x=0` (`archimedeanLimit_Ioo`, `DilogPartAConvergence.lean`). The
remaining open content is **Part B** — the substrate continuation `q→1⁺` (to
`q₀≈1.11 > 1`) and the `x→1⁻` edge, where the factors `1 − x qᵏ` change sign and
the algebraic poles of `Φ_n` approach the `Li₂` branch cut.

For `k > k* = log_q(1/x)` a factor `1 − x qᵏ` is **negative**, so `log(1 − x qᵏ)`
on the principal branch acquires an imaginary `iπ` on top of the real
log-magnitude. This file formalizes that per-factor decomposition exactly — the
object the Part-B pole-cancellation audit subtracts with **no free parameter**:

* `clog_one_sub_of_gt_one` — the branch phase: for a negative real factor `1 − w`
  (`w > 1`), `Log(1 − w) = log(w − 1) + iπ` (principal complex log).
* `clog_one_sub_pole_phase_split` — combining the branch phase with the real
  algebraic split `log_neg_factor_split`, a negative factor decomposes into
  (i) the **algebraic pole** `log w` (with `w = x qᵏ`, linear-in-`k` divergence),
  (ii) the **convergent regularized piece** `log(1 − w⁻¹)`, and (iii) the
  **branch-cut phase** `iπ`.

This is a **formalize-first structural chip**, not a closure of Part B: it makes
the pole/phase bookkeeping exact, but the genuine Part-B content — the *uniform*
cancellation of the `iπ` tower and the linear pole across the cusp, yielding
`reg(x) = Li₂(x) − π²/3` — remains open (numerics:
`docs/audits/2026-07-17-dilog-archimedean-limit-partB-pole-cancellation.md`).

-- Ref: [leitner2026] conj:dilogarithm-archimedean-limit
-- Ref: [faddeev1994] https://doi.org/10.1142/S0217732394002793
-/

namespace QOU.QPochhammer

open Complex

/-- **Part B — the per-factor branch phase.**  For a negative real factor
    `1 − w` (`w > 1`), the principal complex logarithm picks up the `iπ`
    branch phase on top of the real log-magnitude:

    `Log(1 − w) = log(w − 1) + iπ`.

    This is the source of the branch-cut `iπ` tower in `(1−q)·log Φ_n` once
    `x qᵏ > 1` (i.e. `k > log_q(1/x)`), which the Part-A monotone-Riemann-sum
    argument does not see. -/
theorem clog_one_sub_of_gt_one (w : ℝ) (hw : 1 < w) :
    Complex.log ((1 - w : ℝ) : ℂ)
      = (Real.log (w - 1) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  have hneg : (1 - w : ℝ) < 0 := by linarith
  apply Complex.ext
  · -- real parts:  Real.log ‖↑(1−w)‖ = w−1 magnitude,  iπ contributes nothing
    rw [Complex.log_re, Complex.norm_real, Real.norm_eq_abs, abs_of_neg hneg, neg_sub]
    simp [Complex.add_re, Complex.mul_re, Complex.ofReal_re, Complex.ofReal_im,
      Complex.I_re, Complex.I_im]
  · -- imaginary parts:  arg of a negative real is π
    rw [Complex.log_im, Complex.arg_ofReal_of_neg hneg]
    simp [Complex.add_im, Complex.mul_im, Complex.ofReal_re, Complex.ofReal_im,
      Complex.I_re, Complex.I_im]

/-- **Part B — the exact per-factor pole + phase decomposition.**  Combining the
    branch phase with the real algebraic split `log_neg_factor_split`, a negative
    factor `1 − w` (`w = x qᵏ > 1`) decomposes into:

    `Log(1 − w) = log w + log(1 − w⁻¹) + iπ`,

    i.e. (i) the algebraic pole `log w` (linear-in-`k` divergence), (ii) the
    convergent regularized piece `log(1 − w⁻¹)`, (iii) the branch-cut phase `iπ`.
    This is exactly the per-factor object the Part-B pole-cancellation audit
    subtracts (no free parameter). -/
theorem clog_one_sub_pole_phase_split (w : ℝ) (hw : 1 < w) :
    Complex.log ((1 - w : ℝ) : ℂ)
      = (Real.log w : ℂ) + (Real.log (1 - w⁻¹) : ℂ) + (Real.pi : ℂ) * Complex.I := by
  rw [clog_one_sub_of_gt_one w hw, log_neg_factor_split w hw]
  push_cast
  ring

end QOU.QPochhammer
