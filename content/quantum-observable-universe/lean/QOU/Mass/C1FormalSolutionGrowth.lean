/-
Copyright (c) 2026 litlfred. All rights reserved.

# q-Gevrey growth of the C1 formal solution at ∞ (W2 Stokes signature)

W2 ∞-side brick (bean `qou-xufp`). The C1 module `L1 = (q²x−1)σ² − (q−1)σ − (q−1)` has, at
`∞`, the formal power-series solution `f(x) = ∑ cₙ x^{−n}` with (witness
`computations/qbeta/c3_w2_inf_formal_solution.witness.json`):

  `c_{m+1} = c_m·(1 + (q−1)q^m + (q−1)q^{2m})`,  `c_0 = 1`.

The ratio `c_{m+1}/c_m` has q-degree `2m+1`, so the q-degree of `cₙ` is
`d_n = ∑_{m<n}(2m+1)`. This file proves `d_n = n²` — i.e. the coefficients grow like
`q^{n²}`, the **q-Gevrey-½ divergence** that is the ∞ Stokes signature: the formal series
does not converge and must be q-Borel/Laplace summed; the sector-difference of the sums is
the Stokes multiplier datum `U ∈ ℂ²` (the RSZ-wild residual, beaned).

**Scope.** The growth-degree identity `∑_{m<n}(2m+1) = n²` (= `deg_q cₙ`) only. The Stokes
summation is NOT here. §7c: `ℕ` degrees. Sorry-free. No fit; nothing wired.

-- Ref: [manuscript] docs/audits/2026-08-01-c1-inf-slope-half-rsz-stokes.md (W2 ∞)
-- Ref: [ramis-sauloy-zhang-2013] https://arxiv.org/abs/0903.0853 (§4-5, summation/Stokes)
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

namespace QOU.Mass.C1FormalSolutionGrowth

open Finset

/-- **q-degree of the `n`-th C1 formal coefficient**, `d_n = ∑_{m<n}(2m+1)`, from the
ratio degree `deg_q(c_{m+1}/c_m) = 2m+1`. -/
def c1FormalDeg (n : ℕ) : ℕ := ∑ m ∈ range n, (2 * m + 1)

/-- **q-Gevrey-½ growth**: `deg_q(cₙ) = n²`. The C1 formal solution at ∞ has coefficients of
q-degree `n²`, i.e. growth `q^{n²}` — the divergent (q-Gevrey) behaviour that forces Stokes
summation. Proof: the sum of the first `n` odd numbers is `n²`. -/
theorem c1FormalDeg_eq_sq (n : ℕ) : c1FormalDeg n = n ^ 2 := by
  induction n with
  | zero => rfl
  | succ k ih =>
    rw [c1FormalDeg, Finset.sum_range_succ, ← c1FormalDeg, ih]
    ring

/-- The growth is strictly super-linear for `n ≥ 2` (`n² > c·n` eventually) — a divergent
formal series, confirming the ∞ singularity is irregular (not Fuchsian). Stated as the
per-step increment `d_{n+1} − d_n = 2n+1`, which is unbounded. -/
theorem c1FormalDeg_step (n : ℕ) : c1FormalDeg (n + 1) = c1FormalDeg n + (2 * n + 1) := by
  rw [c1FormalDeg, Finset.sum_range_succ, ← c1FormalDeg]

end QOU.Mass.C1FormalSolutionGrowth
