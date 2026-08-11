---
# qou-shrp
title: 'L4-1 sharp constant: Riemann-defect refinement for phi (the 1/2 the antitone squeeze cannot pin)'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T12:00:00Z
updated_at: 2026-08-11T12:30:00Z
---

Reopens the sharp half of L4-1 after the correction recorded in
`docs/audits/2026-08-11-l41-sharp-constant-still-open.md`.

TARGET:
    sum_{j<=n} int_cell (phi(x_j) - phi(u)) du = (h/2)(phi(nh) - phi(0)) + O(h^2)
i.e. the LIMIT of the scaled defect, not the two-sided bound already proved
sorry-free by `smooth_defect_squeeze` (qou-ph2s, PR #5003).

WHY IT IS NEEDED: vdV Lemma 3's explicit `- (1/2) log 2N` is the N^{-1/2}
prefactor feeding Lemma 4's N^{(c+d+3)/2}. Measured evidence that the squeeze
cannot supply it: `computations/logsine_smooth_defect_constant.py` — the scaled
defect converges to the MIDPOINT of the proved interval, whose width is fixed
at 0.4516 and does not shrink with N.

ROUTE: per-cell, `int_{x-h}^{x} (phi(x) - phi(u)) du = (h^2/2) phi'(x) + O(h^3)`
by Taylor/MVT, then sum: `(h/2) sum_j phi'(x_j) h -> (h/2) int_0^{nh} phi'`.
So this DOES need `phi'` bounds — including near 0, where `phi' = cot x - 1/x`
is regular but its two terms are not. This is exactly the analysis qou-ph2s
found unnecessary FOR THE BOUND; it is necessary for the CONSTANT.

Candidate simplification: phi extends to an even analytic function of x on
(-pi, pi) (phi(x) = log(sinc x) + log 2 with sinc even, nonvanishing there), so
phi' is odd and phi'(0) = 0. If Mathlib carries analyticity of `sinc` or of
`sin x / x`, the first-cell difficulty may again evaporate — check before
hand-rolling a cot bound.

REFRAMED (LogSineRiemannForm.lean, sorry-free): the smooth half is EXACTLY a
right-endpoint Riemann-sum defect,
  sum_i int_cell (phi(x_{i+1}) - phi(u)) du = h sum_i phi(x_{i+1}) - int_0^{nh} phi,
so the missing 1/2 is precisely the FIRST EULER-MACLAURIN CORRECTION
(h/2)(phi(nh) - phi(0)). Mathlib has no E-M formula => genuine infra gap,
owner-authorised to add ("add mathlib infra if needed", 2026-08-11).

INFRA TO ADD (in order):
 1. Real.sinc differentiability — Mathlib has continuous_sinc + sinc_zero but
    NO deriv/analyticity. Needed so phi = log 2 + log(sinc) is C^1 at 0
    (phi' odd, phi'(0)=0). Route: HasDerivAt sinc 0 0 via |sin x - x| <= x^3/6
    (Real.sin_bound), and the quotient rule off 0.
 2. First E-M correction for C^1 f on a uniform grid:
    h*sum_{j=1}^n f(jh) - int_0^{nh} f = (h/2)(f(nh) - f(0)) + O(h^2 * modulus).
 3. Apply to phi; combine with the exact singular telescope + Stirling to get
    L4-1's sharp statement.
