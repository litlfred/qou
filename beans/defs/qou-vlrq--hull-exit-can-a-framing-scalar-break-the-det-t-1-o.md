---
# qou-vlrq
title: 'Hull exit: can a framing scalar break the det T = -1 obstruction?'
status: completed
type: task
priority: normal
created_at: 2026-09-02T20:52:19Z
updated_at: 2026-11-15T10:10:00Z
---


RESOLVED 2026-09-01 -- computations/probes/the_hull_exit_is_a_fractional_twist_probe.py,
6/6. YES -- and the exponent it needs is FRACTIONAL, which makes the missing
ingredient TWIST rather than writhe.

THE OBSTRUCTION WAS NEVER ABOUT d. A framed bond carries an overall factor c --
the corpus's own mu_eff = mu (1-h)^(e/2). A scalar multiplies BOTH block ratios,
so it scales the det T = -1 obstruction by c^2:

    |mu_sym * mu_anti| = c^2 |det(T + dI)|

|det| >= 1 blocks every d in the hull, but c = 0.95 already drops the product to
0.912 < 1. No stranger offset is needed; a scalar exits the hull by construction.

WINDOW, CLOSED FORM. With u = -log c at beta = 0: L(T=0) = u + log q and
L(T=1) = u - log q, so T=1 stays unbound iff u < log q:

    c in (1/q, 1]      <=>      e in [0, 0.8897722518)

and ratio(u) = (u + log q)/(log q - u) rises from 1 to unbounded across it. One
continuous parameter lifts the cap that no crossing count could (qou-o8ww).

THE EXPONENT MUST BE FRACTIONAL -- the whole point:

    e        c = (1-h)^(e/2)   in window?   ratio
    0        1.00000000        yes          1.0000
    1/2      0.94305244        yes          3.5656
    e*       0.90635175        yes         33.7055
    e_max    0.90091828        no          T=1 BINDS
    1        0.88934791        no          T=1 BINDS
    2        0.79093970        no          T=1 BINDS

e = 1 -- ONE FULL CROSSING'S WRITHE -- gives c = 0.8893479079 against threshold
1/q = 0.9009182840, outside by 0.011570. A full crossing's framing is TOO STRONG
and the T=1 channel binds. Every integer e >= 1 fails the same way.

CALUGAREANU: Lk = Tw + Wr. The writhe Wr is a signed crossing count, an INTEGER
for a braid word, and exactly what this construction carries. The twist
Tw = (1/2pi) int tau ds is CONTINUOUS, a property of the framed curve rather than
its diagram. The admissible window excludes every integer and admits a continuum
below 0.88977, so what it asks for is TWIST -- the ingredient the bond graph
structurally lacks, and precisely the one the writhe-normalised convention
divides out (qou-6pt7).

This is also where the owner's side reading lands. A serpenoid curve's
osculating circles rho = 1/kappa are the CURVATURE half of the Frenet data; the
TORSION tau is the other half and is what integrates to Tw. A description that
counts crossings sees Wr and is blind to tau. "What exits the convex hull" and
"what does a curvature description add" have the same answer.

MATCHING NATURE IS A FIT, SAID PLAINLY. 2.224566/0.066 = 33.7055 requires
u* = 0.0983278069, c* = 0.9063517467, e* = 0.838496742899 -- 94.24 % across the
window. Scanned against 22 corpus constants the nearest is 4h = 0.8362411952 at
0.27 %, which at an arc quoting agreements at 1e-13 is NOT a match. e* is a
measurement of what would be required, not a derivation.

ESTABLISHED: the obstruction is broken by a framing scalar and by nothing else
the construction contains; the window is c in (1/q, 1] in closed form; every
integer writhe is excluded so the ingredient is continuous twist.
NOT ESTABLISHED: any value for it. No substrate mechanism producing a fractional
twist is exhibited anywhere.

The gap has moved from "impossible" to "one unexplained continuous parameter".
That is progress and it is not a theory.

SCOPE: n=2 interface, |mu| < 1 binding convention inherited from qou-m896. The
A1/A2 determinant scaling is independent of that convention; the ratio and
window numbers are not. Lifting to 3-strands-per-nucleon is qou-r1yj.

## 2026-11-15 — OWNER RULING (PR #7823): the 33.7 comparison is ILL-POSED
A one-crossing coupling ratio (gl_N frame 1; SU(N) frame (N+1)/(N-1) <= 3) compared to B_d / E_virtual(1S0) = 2.224566/0.066 is a coupling-vs-energy category mismatch across the bound/virtual threshold, not a 33.7x miss. The 0.066 MeV itself is correct (effective-range np 1S0 pole, 0.0657 MeV). Probes quoting 33.7 left unedited (scriptHash). Follow-up: a derived coupling -> two-body binding step. See docs/audits/2026-11-15-quark-equals-strand-implications.md §4.
