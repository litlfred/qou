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

STEP 3 LANDED (LogSineSharpConstant.lean, sorry-free), with a ROUTE
CORRECTION worth recording:
  hasDerivAt_phiDeriv   — phi'' = 1/x^2 - 1/sin^2 x on (0,pi)
  phiDeriv_antitoneOn   — phi' antitone on any [a,b] subset (0,pi); this is
                          the hypothesis the E-M bracket needs, and it is
                          just sin x < x. It went through cleanly -- the
                          piece I had flagged as the likely surprise did not
                          surprise.
  phi_interior_bracket  — the E-M bracket applied to phi on the interior
                          cells i = 1..n-1 (covering [h, nh]).

ROUTE CORRECTION: the planned (a) -- define phiSinc = log 2 + log(sinc) so
phi is differentiable at the CLOSED endpoint 0 -- proved UNNECESSARY. The
i=0 cell never needs a derivative: smooth_defect_squeeze already brackets it
between h(phi(h) - log 2) and 0, and that collapses as h -> 0. So E-M is
applied only on [h, nh] where phi is honestly smooth. STEP 1's sinc infra is
therefore NOT a dependency of this file; it stands on its own as
upstreamable Mathlib material. Recorded so no false chain of necessity is
inferred.

STEP 3 CONVERGENCE LANDED (same file, sorry-free) — the sharp statement:

  phi_smooth_defect_sharp
    | sum_{i=1..n-1} int_cell (phi(x_{i+1}) - phi(u)) du
        - (h/2)(phi(nh) - phi(h)) |   <=   (h^2/2)(phi'(h) - phi'(nh))

for every 0 < h and every n >= 1 with nh < pi. This IS van der Veen's
missing 1/2, now identified rather than merely bracketed, and it is
EFFECTIVE: no limit is taken, no modulus of continuity is carried.

How the two envelopes collapsed onto the term (the step that was open):
 - phi_sub_cell_bracket   — the SAME antitone MVT bracket, applied to phi
                            instead of to the cell defect, gives
                            h phi'(x_{i+1}) <= phi(x_{i+1}) - phi(x_i)
                                            <= h phi'(x_i).
 - phi_riemann_sum_bracket— summing + telescoping: phi(nh) - phi(h) is
                            trapped between h*R and h*L, i.e. between the
                            VERY SAME two Riemann sums that bracket the
                            defect sum S. That common trapping is what
                            turns two envelopes into one identified term.
 - sum_phiDeriv_telescope — L - R = phi'(h) - phi'(nh) exactly, so the
                            residual is O(h^2), not O(h).
 - sum_Ico_one_telescope  — the Ico-1-n telescope helper both use.

ROUTE NOTE: no integral comparison and no monotone-convergence argument
was needed after all. I had scoped this step as "monotone Riemann
convergence" (integrate phi' over each cell, FTC, sum). The shorter route
is to never integrate phi' at all: apply the ALREADY-PROVED
sub_bracket_of_antitoneOn_deriv a second time, to phi rather than to the
defect. Recording it because it is the fourth time on this front that a
step I flagged as the hard analytic one turned out to be a reuse of
machinery already in hand (cf. the E-M / Lipschitz / sinc corrections
above). The pattern is real: on this front my difficulty estimates run
high whenever the target is a BOUND that a monotonicity argument already
supplies, and only bite when the target is a genuine LIMIT.

REMAINING for L4-1's full sharp statement (do not overclaim): add the
collapsing i=0 cell (already bracketed by smooth_defect_squeeze between
h(phi(h) - log 2) and 0) and combine with L4-1c(i)'s exact singular
telescope + L4-1b's Stirling. The smooth half itself is now DONE.

RETRACTION (2026-08-19) -- THE INFRA GAP THIS BEAN CHASED WAS NOT A CORPUS GAP.

Everything above about "Mathlib has no E-M formula => genuine infra gap,
owner-authorised to add" is half wrong, and it is the half that mattered.
Mathlib indeed has none.  THIS CORPUS HAS HAD ONE SINCE 2026-08-10:

  QOU/MathlibExt/CompositeEulerMaclaurin.lean   abs_integral_sub_composite_le_osc
  QOU/MathlibExt/TrapezoidRule.lean
  QOU/Knot/LogSincNearZero.lean                 abs_sum_logSinc_sub_euler_maclaurin
                                                hasDerivAt_logSinc
                                                hasDerivAt_logSinc_deriv
                                                antitoneOn_logSinc_deriv

nine days before step 2 was written.  logSinc x = log(sin x) - log x, and
phi x = log 2 + logSinc x, so phiDeriv = logSinc' IDENTICALLY -- the three
phi lemmas of step 3 duplicate the three logSinc lemmas outright, and
abs_sum_logSinc_sub_euler_maclaurin IDENTIFIES the O(h) coefficient as
(h/12)(g'(b) - g'(a)) where phi_smooth_defect_sharp only BOUNDS it, by a
factor of exactly 6.

The 6 was measured by my own verification probe and misread:
logsine_sharp_constant_check.py reports bound/residual = 6.0008, 5.9988,
6.0007, 6.0010 across N = 200..1600, and the commit message called that
"headroom".  A ratio constant to four digits over a decade of h is the true
coefficient (1/2 divided by 1/12), not slack.

ROOT CAUSE, and it is not the estimate-calibration story recorded above:
AGENTS.md requires the corpus-grep checklist before declaring a gap in a
durable artifact.  Only the Mathlib inventory was run.
  grep -rln "EulerMaclaurin" content/
finds it at once.  Not covered by the parallel-exploration relaxation: the
corpus work was LANDED on main, not in flight, and settled infrastructure
has one right answer.

WHAT STANDS: SincDeriv.lean (Real.sinc differentiability -- absent from both
Mathlib and this corpus; LogSincNearZero deliberately avoids Real.sinc by
starting the grid at h).  EulerMaclaurinFirst.lean needs only f' antitone
where the composite rule needs a continuous f'', so it is kept as
weaker-hypothesis material -- but not as a gap closure.

NEXT: assemble L4-1's smooth half from abs_sum_logSinc_sub_euler_maclaurin.
Before writing any of it, grep what LogSincNearZero + KashaevEndpointSplit +
the qou-mlgp lane have already assembled -- the same failure twice would be
much worse than once.
Audit: docs/audits/2026-08-19-qou-shrp-duplicated-corpus-euler-maclaurin.md

REDUNDANT (2026-08-19) -- L4-1's target was ALREADY PROVED ON MAIN, stronger,
since 2026-08-10 19:24 UTC, one day BEFORE the L4-1 feasibility pass that
opened this bean.

  QOU/Knot/KashaevAsymptotic.lean :: kashaev_log_sum_asymptotic
    | sum_{j=1}^{k} log(2 sin(j pi/N))
        - ( -(N/pi) Lob(k pi/N) + (1/2) log(2N sin(k pi/N))
            + (pi/(12N)) cot(k pi/N) ) |
      <= 1/(144 k^2) + (7/12)(pi/N)^2 + (pi/N)^2/(12 sin^2(k pi/N))

Verified: 17-module cone ok=17, axioms [propext, Classical.choice, Quot.sound],
no sorryAx.  It is STRICTLY STRONGER than the L4-1 target: it identifies the
O(1/N) term as (pi/12N)cot, and its error is effective (explicit constants).
The two (1/2)log terms differ by exactly (1/2)log(2pi) -- the Stirling constant
the L4-1 route was going to produce.

Nothing is deleted; the work here is correct and sorry-free.  Downstream
consumers should cite kashaev_log_sum_asymptotic instead.
Audit: docs/audits/2026-08-19-l41-was-already-proved-on-main.md
