/-
# The smooth half IS a Riemann-sum defect — so the missing ½ is Euler–Maclaurin
# (bean qou-shrp, epic qou-u1b5)

`smooth_defect_squeeze` (L4-1c(ii)) bounds the smooth half of the log-sine
cell defect two-sidedly but cannot pin van der Veen's `½` (measured:
`computations/logsine_smooth_defect_constant.py` — the limit is the midpoint
of the proved interval).  This file identifies *what* the `½` is, by an exact
rewriting that needs no analysis at all:

    Σ_{i<n} ∫_{cell_i} (φ(x_{i+1}) − φ(u)) du  =  h·Σ_{i<n} φ(x_{i+1})  −  ∫_0^{nh} φ,

i.e. the smooth half is exactly the **right-endpoint Riemann sum minus the
integral**.  Its leading correction is therefore the classical first
Euler–Maclaurin term `(h/2)·(φ(nh) − φ(0))` — which is precisely the `½` that
is missing, and matches the measured value.

**This corrects the scope of the earlier "Euler–Maclaurin is not needed"
finding** (`docs/audits/2026-08-11-l41-euler-maclaurin-feasibility.md`
§UPDATE).  That finding is right about the *singular* half: it telescopes
exactly, so no summation formula touches the `log(2 sin)` endpoint
singularity.  It was wrong to conclude that E–M is unnecessary for L4-1 as a
whole — the *smooth* half needs exactly the first E–M correction, and
Mathlib has no Euler–Maclaurin formula.  So the infrastructure gap is real,
it is simply located one step later than first thought, and on a function
(`φ`, extendable via `Real.sinc`) that is regular where the original
integrand was not.

**CORRECTION (2026-08-19).**  The gap was real in *Mathlib* and NOT real in
this *corpus*: `QOU/MathlibExt/CompositeEulerMaclaurin.lean` has carried the
composite rule since 2026-08-10, already applied to `logSinc` (= `φ − log 2`)
in `QOU/Knot/LogSincNearZero.lean`.  The paragraph above, and the
"Mathlib inventory" note below, led to that rule being rebuilt.  Use
`abs_sum_logSinc_sub_euler_maclaurin`.  See
`docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md`.

Mathlib inventory relevant to closing it: `Real.sinc` exists with
`Real.continuous_sinc` and `Real.sinc_zero`, but **no** differentiability or
analyticity lemmas — those, plus the first E–M correction for `C¹` functions,
are what `qou-shrp` must supply.
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

import QOU.Knot.LogSineSmoothPart

namespace QOU.Knot.FigureEightVolume

open Real

/-- **The smooth half is a right-endpoint Riemann defect (sorry-free,
    exact).**  Each cell contributes `h·φ(x_{i+1}) − ∫_{cell} φ`, so the sum
    is the Riemann sum minus the integral over `[0, nh]`.  No hypotheses
    beyond integrability, which `φ` has everywhere. -/
theorem smooth_defect_eq_riemann_defect {h : ℝ} (hh : 0 < h) (n : ℕ) :
    (∑ i ∈ Finset.range n,
        ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phi u))
      = h * (∑ i ∈ Finset.range n, phi (((i : ℝ) + 1) * h))
        - ∫ u in (0 : ℝ)..((n : ℝ) * h), phi u := by
  -- per cell: ∫ (c − φ) = h·c − ∫ φ
  have hcell : ∀ i ∈ Finset.range n,
      (∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h),
          (phi (((i : ℝ) + 1) * h) - phi u))
        = h * phi (((i : ℝ) + 1) * h)
          - ∫ u in ((i : ℝ) * h)..(((i : ℝ) + 1) * h), phi u := by
    intro i _
    rw [intervalIntegral.integral_sub intervalIntegrable_const
      (intervalIntegrable_phi _ _), intervalIntegral.integral_const,
      smul_eq_mul]
    ring
  rw [Finset.sum_congr rfl hcell, Finset.sum_sub_distrib, ← Finset.mul_sum]
  congr 1
  -- the cell integrals telescope to the whole interval
  have hadd := intervalIntegral.sum_integral_adjacent_intervals
    (a := fun k : ℕ => (k : ℝ) * h) (n := n)
    (f := phi) (μ := MeasureTheory.volume)
    (fun k _ => intervalIntegrable_phi _ _)
  simp only [Nat.cast_zero, zero_mul] at hadd
  rw [← hadd]
  refine Finset.sum_congr rfl fun i _ => ?_
  norm_num

end QOU.Knot.FigureEightVolume
