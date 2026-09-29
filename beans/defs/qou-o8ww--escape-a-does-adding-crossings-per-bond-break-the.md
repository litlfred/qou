---
# qou-o8ww
title: 'Escape (a): does adding crossings per bond break the forced degeneracy?'
status: completed
type: task
priority: normal
created_at: 2026-09-01T08:27:18Z
updated_at: 2026-09-01T08:30:52Z
---


RESOLVED 2026-09-01 -- computations/probes/adding_crossings_cannot_break_the_degeneracy_probe.py,
6/6. NO -- and the reason subsumes the whole question.

THE OBSTRUCTION IS det T = -1. The Hecke relation T^2 = hT + 1 fixes the
eigenvalue product at q*(-1/q) = -1, so a crossing's two block ratios multiply to

    mu_sym * mu_anti = (q+d)(-1/q+d) = d^2 + d*h - 1 = det(T + dI)

On d in [-h,0] this is -1 at BOTH endpoints and -(1+h^2/4) at the vertex
d = -h/2, so |det| in [1, 1.010926552] -- ALWAYS >= 1, equality only at d = 0
and d = -h.

A bond built from k crossings is prod_i (T + d_i), whose block ratios multiply
factor by factor. Every factor has magnitude >= 1, so

    L(T=0) + L(T=1) = -log|mu_sym * mu_anti| <= 0   =>   ratio <= 1

FOR EVERY CROSSING COUNT. Adding crossings cannot break the degeneracy.
Verified on 200 random multi-crossing bonds (k = 2..6): det products all >= 1
(range 1.0124..1.0212 on the sample shown), best achievable ratio 0.927.

WHERE THE ESCAPE ACTUALLY IS. |d^2 + d*h - 1| < 1 <=> 0 < d(d+h) < 2. On the
interior d in (-h,0) the product d(d+h) is NEGATIVE, so the condition fails
everywhere inside. It holds only for

    d > 0  (beta < 0)     or     d < -h  (beta > 1)

beta=0 is sigma, beta=1 is sigma^-1, so: THE BOND OPERATOR MUST LEAVE THE CONVEX
HULL OF {sigma, sigma^-1}. No crossing count, no block grading, and no
convention does that -- one statement that subsumes both named escapes AND every
convention question this arc spent probes on (framing, writhe, colour weighting
all only move d within the hull).

WHAT NATURE WOULD COST, even outside the hull. Solving for the experimental
ratio 2.224566/0.066 = 33.7055 in the one-crossing family:

    d*        =  0.900918283896
    beta*     = -4.30937050        (4.31 outside the hull)
    |mu_sym|  =  2.0108968666
    |mu_anti| =  5.944e-11         <- T=0 within this of unbinding

and it is NOT robust: d* - 1e-4 gives ratio 13.19, d* - 1e-6 gives 19.78. So
33.7 is reachable only by tuning |mu_anti| to within 6e-11 of zero -- ten
digits, not a mechanism.

A FAIR WORD FOR THE OTHER SIDE. Near-threshold tuning is not by itself
unphysical: the real NN system is famously unnatural, with both S-wave channels
anomalously close to zero energy (a_np(3S1) = +5.419 fm, a_np(1S0) = -23.740 fm
against a force range ~1.4 fm), which is the basis of pionless EFT. A theory
reaching 33.7 by sitting near threshold is not automatically wrong. THE
STRUCTURAL PROBLEM IS THE OTHER HALF -- beta outside [0,1] is an operator that
is not a combination of the two crossings at all, and nothing in the
construction supplies one.

STATE OF THE TWO ESCAPES, both now closed under beta in [0,1]:
  (b) qou-m896 -- restores the SIGN pattern ungraded, caps the ratio at 1
  (a) here     -- cannot lift the cap at any crossing count
What remains is not a third escape of the same kind but a change of INGREDIENT:
a bond operator outside the convex hull of {sigma, sigma^-1}, whose meaning and
provenance are not supplied here.

SCOPE: closes escape (a) for bonds that are a PRODUCT of crossings (T + d_i)
with real d_i in [-h,0] -- what the construction uses and what the escape
proposed. Does NOT cover a bond that is a SUM of products, or one entangling the
two nucleons' internal strands rather than acting on a single interface
generator. The det-magnitude obstruction (A1-A3) is independent of the
|mu| < 1 binding convention; the A5 ratio numbers are not.
