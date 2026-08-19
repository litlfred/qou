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

STEP 1 DONE (SincDeriv.lean, sorry-free): the Mathlib gap is closed —
hasDerivAt_sinc_zero (sinc'(0)=0, via slope + Real.sin_bound),
hasDerivAt_sinc (quotient rule off 0), differentiable_sinc. Stated in
Mathlib style, no QOU specifics, upstreamable. Next: step 2, the first
Euler-Maclaurin correction for C^1 f on a uniform grid.

STEP 2 DONE (EulerMaclaurinFirst.lean, sorry-free): Mathlib's missing first
Euler-Maclaurin correction, in the MONOTONE-DERIVATIVE form (which squeezes
and so pins the constant, instead of carrying an abstract modulus):
  cell_defect_bracket  — (h^2/2) f'(a+h) <= int_a^{a+h} (f(a+h) - f u) du
                          <= (h^2/2) f'(a),  for f' antitone on the cell
  grid_defect_bracket  — the summed form on the uniform grid x_i = i h
Both envelopes are (h/2) x a Riemann sum of f', so both -> (h/2)(f(nh)-f(0)).
Proof needs no Fubini and no modulus bookkeeping: MVT + antitonicity +
int_a^{a+h} (a+h-u) du = h^2/2. General f, Mathlib style, upstreamable.

STEP 3 REMAINING, and it is not just "apply": grid_defect_bracket needs
HasDerivAt f (f' x) x on the CLOSED [0, nh] including x = 0, but the corpus
phi = log(2 sin x) - log x has a junk value there. So step 3 must
 (a) define phiSinc x = log 2 + log (sinc x) (differentiable at 0 by STEP 1,
     since sinc 0 = 1 != 0), and prove phiSinc = phi on (0, pi);
 (b) prove phiSinc' antitone on [0, nh] -- true because phi'' = 1/x^2 -
     1/sin^2 x < 0 (sin x < x), but it needs proving;
 (c) then apply grid_defect_bracket and combine with the exact singular
     telescope (L4-1c-i) + Stirling (L4-1b) for L4-1's sharp statement.
