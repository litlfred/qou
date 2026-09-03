---
# qou-qx7j
title: 'E is not identifiable: every residue of lambda_SW^(n) vanishes locally, and the branch locus is bar-symmetric with two points exactly on |z|=1'
status: completed
type: task
priority: normal
created_at: 2026-09-03T04:11:10Z
updated_at: 2026-09-03T04:43:49Z
---

RESOLVED 2026-09-03, branch claude/enclosed-pole-set-E-2026-09-03.
Answers the question PR #6067 (bean qou-6v5l) left open.

ANSWER: E IS NOT IDENTIFIABLE -- the question is empty, not open. Under the
classical-jet rule lambda_SW^(n) = X^(n)dz, every residue vanishes
INDIVIDUALLY, so every subset E gives period zero.

The reason is local, and needs neither a global primitive nor the compact
surface. QOU.Brings.RamificationParityMonodromy already defines the right
operator for this setting: ddz f = fun e => ((e+2 : Z) : R) * f (e+2), the
coefficient form of d/dz = (1/2t)d/dt at z = z_c + t^2. That file uses the
shift's EVENNESS (ddz commutes with t -> -t). This uses the MULTIPLIER, at the
one exponent where it vanishes: (ddz f)(-2) = ((-2)+2)*f(0) = 0 for EVERY f.
The t^-2 coefficient of a z-derivative is always zero because the only input
that could reach it is the constant term. Depends on [propext] alone.

NEW AND EXACT: THE BRANCH LOCUS IS BAR-SYMMETRIC. disc coefficients
[16,24,35,50,35,24,16] are PALINDROMIC -- the corpus has had this polynomial
written out exactly since bring_cubic_monodromy_probe.py (fact A1) and never
recorded it. So z^6 Delta(1/z) = Delta(z): the locus is invariant under the
Hecke bar-involution z -> 1/z. Reducing by w = z+1/z gives 16w^3+24w^2-13w+2,
disc = -80000 < 0 (one real root, one conjugate pair); C(-2) = -4 < 0 < 23 =
C(-1) locates the real root in (-2,-1) by IVT on INTEGER evaluations; no
rational root, so it is a cubic irrationality; and a real w with |w| < 2 gives
|z| = 1 EXACTLY. Hence the six split 2 + 4: two bar-FIXED points exactly ON the
unit circle, one bar-orbit of four with reciprocal moduli (measured product
1.000000000000000000000000).

=> THE UNIT CIRCLE IS NOT AN ADMISSIBLE CONTOUR. It passes through two branch
points, and it is the candidate the corpus's own oint_{S_c} notation suggests.

NOT A DISCOVERY on the vanishing -- a THIRD route. prop:sw-classical-jet-exactness
has it from global exactness; period_eq_zero_of_total_residue_vanishes (#6067)
from the ambient compact surface. This one assumes least and is per-point. All
three leave the q-difference prolongation untouched.

RE-SCOPES THE TARGET: the open problem is UPSTREAM of E -- which prolongation.

TWO DEFECTS FOUND IN PASSING, both fixed here: sw_period_growth_probe.py does
not run on main (mpmath NoConvergence -- polyroots called at a branch point with
default maxsteps=50, and the colliding roots are the probe's own subject), and
it pushed exact integer discriminant coefficients through complex(), i.e.
float64. Verified pre-existing by running the origin/main version with correct
cwd and PYTHONPATH. Its closing claim that the residues are the per-block
Wedderburn dim_q is withdrawn -- they are zero.
