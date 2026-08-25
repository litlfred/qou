/-
# L4-1c(i) — the singular part telescopes EXACTLY (bean qou-q8lc, epic qou-u1b5)

Third sub-brick of L4-1, and the one that reshapes the remaining work.

The cell-defect representation (L4-1a, `LogSineCellDefect.lean`) writes the
Riemann defect of the log-sine sums as `Σ_j ∫_{cell_j} (f(x_j) − f(u)) du`
with `f = log(2 sin ·)`.  Split the integrand at the singularity,

    log(2 sin x_j) − log(2 sin u) = (log x_j − log u) + (φ(x_j) − φ(u)),
    φ(x) := log(2 sin x / x)   — SMOOTH at 0 (removable, φ(0⁺) = log 2),

and the two halves have completely different characters:

* the **singular half** `Σ_j ∫_{cell_j} (log x_j − log u) du` telescopes to
  the *exact* closed form `−h·(n·log n − n − log(n!))` (`log_cell_telescope`
  below), which the Stirling brick (L4-1b) converts into
  `h·(½·log n + ½·log 2π + o(1))`;
* the **smooth half** `Σ_j ∫_{cell_j} (φ(x_j) − φ(u)) du` is an ordinary
  `C¹` Riemann-sum defect — no singularity anywhere in it.

**Consequence (recorded finding): no Euler–Maclaurin formula is needed for
L4-1.**  The scoping note in
`docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md` worried that the
endpoint singularity of `log(2 sin)` would defeat a summation formula and
that Mathlib has no Euler–Maclaurin to appeal to.  Both concerns dissolve:
the singular behaviour is captured *exactly* by the telescope + Stirling,
and what is left is smooth.  The remaining L4-1 work is a mean-value bound
on `φ'`, not a summation formula.

This file proves the exact telescope, sorry-free.  It is genuinely exact —
no asymptotics, no hypothesis on `n`, valid for every grid spacing `h > 0`.
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

import Mathlib.Analysis.SpecialFunctions.Integrals.Basic
import QOU.Knot.LogFactorialStirling

namespace QOU.Knot.FigureEightVolume

open Real

/-- The per-cell primitive difference, from Mathlib's hypothesis-free
    `integral_log` (which covers the first cell `[0, h]` through the
    singularity, `log 0 = 0` making the boundary term vanish). -/
theorem integral_log_cell {h : ℝ} (j : ℕ) :
    (∫ u in (((j : ℝ) - 1) * h)..((j : ℝ) * h), Real.log u)
      = (j : ℝ) * h * Real.log ((j : ℝ) * h)
        - ((j : ℝ) - 1) * h * Real.log (((j : ℝ) - 1) * h) - h := by
  rw [integral_log]
  ring

/-- **L4-1c(i) — the singular part telescopes exactly (sorry-free).**  For
    every grid spacing `h > 0` and every `n`,

        Σ_{j=1}^{n} ( ∫_{(j−1)h}^{jh} log u du − h·log(jh) )
          = h · ( n·log n − n − log(n!) ).

    The `log h` pieces cancel identically and the `log j` pieces telescope;
    the right-hand side is exactly the combination the Stirling brick
    (`tendsto_log_factorial_stirling`) evaluates. -/
theorem log_cell_telescope {h : ℝ} (hh : 0 < h) (n : ℕ) :
    ∑ j ∈ Finset.Icc 1 n,
        ((∫ u in (((j : ℝ) - 1) * h)..((j : ℝ) * h), Real.log u)
          - h * Real.log ((j : ℝ) * h))
      = h * ((n : ℝ) * Real.log n - (n : ℝ) - Real.log (n.factorial)) := by
  induction n with
  | zero => simp
  | succ m ih =>
      rw [Finset.sum_Icc_succ_top (by omega : 1 ≤ m + 1), ih]
      -- the new cell, with the primitive evaluated
      have hcast : (((m + 1 : ℕ) : ℝ) - 1) = (m : ℝ) := by push_cast; ring
      have hcast1 : ((m + 1 : ℕ) : ℝ) = (m : ℝ) + 1 := by push_cast; ring
      rw [integral_log_cell, hcast]
      -- the log h pieces cancel: m·h·log((m+1)h) − m·h·log(mh)
      --                        = m·h·(log(m+1) − log m)
      have hsplit : ((m : ℝ) + 1) * h * Real.log (((m : ℝ) + 1) * h)
            - (m : ℝ) * h * Real.log ((m : ℝ) * h)
            - h - h * Real.log (((m : ℝ) + 1) * h)
          = (m : ℝ) * h * (Real.log ((m : ℝ) + 1) - Real.log m) - h := by
        rcases Nat.eq_zero_or_pos m with hm0 | hm1
        · subst hm0
          norm_num
        · have hm : (0:ℝ) < m := by exact_mod_cast hm1
          rw [Real.log_mul (by positivity) hh.ne',
            Real.log_mul hm.ne' hh.ne']
          ring
      rw [hcast1, hsplit]
      -- the factorial step
      have hfac : ((m + 1).factorial : ℝ) = ((m : ℝ) + 1) * (m.factorial : ℝ) := by
        rw [Nat.factorial_succ]
        push_cast
        ring
      have hfacpos : (0:ℝ) < (m.factorial : ℝ) := by exact_mod_cast m.factorial_pos
      rw [hfac, Real.log_mul (by positivity) hfacpos.ne']
      rcases Nat.eq_zero_or_pos m with hm0 | hm1
      · subst hm0
        norm_num
      · have hm : (0:ℝ) < m := by exact_mod_cast hm1
        ring

end QOU.Knot.FigureEightVolume
