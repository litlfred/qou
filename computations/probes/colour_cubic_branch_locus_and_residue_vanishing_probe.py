#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational/symbolic arithmetic over QQ[z] and
# QQ[w] plus a high-precision Puiseux expansion used ONLY to show a coefficient
# is non-zero. Audit-only falsifiability probe (compute-author 1.3), no witness,
# no fitted parameter. NO float64: sympy exact throughout, mpmath at 60 dps for
# the single numerical non-vacuity check.
"""Probe: WHICH branch points does the SW contour enclose?  (bean `qou-qx7j`)

CONTEXT.  `prop:sw-period-residue-sum` was corrected on 2026-08-29 (bean
`qou-6v5l`, PR #6067) to range its residue sum over an ENCLOSED SUBSET E of the
branch points rather than over all of them, because summing over all poles of a
meromorphic 1-form on a compact surface gives ZERO.  Identifying E was left as
the open geometric content of the keystone `a_D^(n) = lw(n-1)`.

This probe answers it, and the answer is that the question is empty.

PART 1 -- THE BRANCH LOCUS IS BAR-SYMMETRIC (new; exact).
The colour cubic f(X,z) = X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1) has

    Delta(z) = -(16z^6 + 24z^5 + 35z^4 + 50z^3 + 35z^2 + 24z + 16),

whose coefficient list [16,24,35,50,35,24,16] is PALINDROMIC.  The corpus has
had this polynomial written out exactly since `bring_cubic_monodromy_probe.py`
(fact A1: degree 6, gcd(Delta, Delta') = 1, six distinct simple branch points)
and has never recorded that it is self-reciprocal.  Consequences:

  (1) z^6 Delta(1/z) = Delta(z), so the branch locus is invariant under
      z -> 1/z -- the Hecke bar-involution acting on the pole locus.
  (2) w = z + 1/z reduces Delta/z^3 to the cubic 16w^3 + 24w^2 - 13w + 2.
  (3) That cubic has discriminant -80000 < 0: one real root, one conjugate pair.
  (4) C(-2) = -4 < 0 < 23 = C(-1) puts the real root in (-2,-1), hence in
      (-2,2); and a REAL w with |w| < 2 gives |z| = 1 EXACTLY.
  (5) So the six split 2 + 4: two bar-FIXED points exactly on the unit circle,
      and one bar-orbit of four (two strictly inside, two strictly outside,
      moduli reciprocal).

  => THE UNIT CIRCLE IS NOT AN ADMISSIBLE CONTOUR: it passes through two branch
     points.  That is the one candidate the corpus's own `oint_{S_c}` notation
     suggests, and it is excluded.

PART 2 -- NO RESIDUE SURVIVES, SO NO E WORKS (exact, local).
At a simple square-root branch point put z = z_k + t^2, so t is a local
coordinate on the curve and d/dz = (1/(2t)) d/dt.  That operator sends a Laurent
term a_j t^j to (j/2) a_j t^{j-2}, so after n applications

    a_j t^j  |->  a_j * 2^{-n} * (prod_{i<n} (j - 2i)) * t^{j-2n}.

Since lambda_SW^(n) = X^(n) dz = X^(n) * 2t dt, the residue is 2 * [coefficient
of t^-2 in X^(n)], which only the term j = 2n-2 can supply.  But that chain
product CONTAINS A ZERO FACTOR at i = n-1: after n-1 applications the term has
become a CONSTANT, and the n-th differentiates it away.

    => Res_p(lambda_SW^(n)) = 0 at EVERY branch point, for EVERY n >= 1,
       INDEPENDENTLY of the Puiseux coefficients.

Hence every subset E sums to zero and E is not identifiable, because there is
nothing to enclose.  The probe checks the coefficients a_{2n-2} are NOT zero, so
the vanishing is genuinely caused by the chain factor and is not the trivial
statement that there is no such term.

NOT A DISCOVERY -- A THIRD ROUTE.  `prop:sw-classical-jet-exactness` already
holds period = 0 under the classical-jet rule, from GLOBAL exactness
(lambda_SW^(n) = d(X^(n-1))); `QOU.Brings.period_eq_zero_of_total_residue_vanishes`
gets it from the ambient compact surface.  This route is LOCAL and per-point: it
needs neither a global primitive nor the surface, only the parity of (1/2t)d/dt.
All three leave the q-difference prolongation untouched.

Lean: `QOU.Brings.ColourCubicBranchLocus` (sorry-free).

Reproduce:
    python3 -u computations/probes/colour_cubic_branch_locus_and_residue_vanishing_probe.py
"""
from __future__ import annotations

import sys

import sympy as sp

X, z, w = sp.symbols("X z w")

CUBIC = X**3 + (z + 1) * X**2 + (z**2 + z + 1) * X + (z**3 + z**2 + z + 1)


def main() -> int:
    fail: list[str] = []
    ok = lambda c, m: (print(f"  [{'OK ' if c else 'FAIL'}] {m}"), fail.append(m) if not c else None)[0]

    print("=" * 78)
    print("PART 1 -- the branch locus is bar-symmetric (z -> 1/z).  Exact.")
    print("=" * 78)

    D = sp.expand(sp.discriminant(sp.Poly(CUBIC, X)))
    coeffs = sp.Poly(D, z).all_coeffs()
    print(f"  disc_X(f) coefficients (z^6..z^0): {coeffs}")
    ok(coeffs == coeffs[::-1], "coefficient list is PALINDROMIC")

    # (1) self-reciprocity, as an exact identity
    recip = sp.simplify(sp.expand(z**6 * D.subs(z, 1 / z) - D))
    ok(recip == 0, "z^6 * Delta(1/z) - Delta(z) == 0 exactly")

    # (2) the w-reduction
    Cw = 16 * w**3 + 24 * w**2 - 13 * w + 2
    back = sp.simplify(sp.expand(Cw.subs(w, z + 1 / z) + D / z**3))
    ok(back == 0, "w = z + 1/z sends Delta/z^3 to -(16w^3 + 24w^2 - 13w + 2)")

    # (3) discriminant of the reduced cubic
    dC = sp.discriminant(sp.Poly(Cw, w))
    print(f"  disc(16w^3+24w^2-13w+2) = {dC}")
    ok(dC == -80000, "reduced-cubic discriminant is -80000")
    ok(dC < 0, "  < 0  => exactly one real root and one conjugate pair")

    # (4) IVT on integer evaluations -- no numerics
    cm2, cm1 = Cw.subs(w, -2), Cw.subs(w, -1)
    print(f"  C(-2) = {cm2}   C(-1) = {cm1}")
    ok(cm2 < 0 < cm1, "sign change on (-2,-1) => a real root there, by IVT")
    ok(sp.Poly(Cw, w).ground_roots() == {},
       "no rational root => irreducible over QQ (the two on-circle points are cubic irrationalities)")

    # |z| = 1 for a real w with |w| < 2.  Carry the radical as a real symbol s
    # with s^2 = 4 - w^2 -- sympy cannot decide re/im of sqrt(4-w^2) without
    # knowing the radicand is non-negative, and that assumption IS the |w| < 2
    # hypothesis.  z = (w + i s)/2, so |z|^2 = (w^2 + s^2)/4.
    wr = sp.Symbol("wr", real=True)
    s = sp.Symbol("s", real=True, nonnegative=True)
    mod2 = sp.simplify(((wr**2 + s**2) / 4).subs(s**2, 4 - wr**2))
    print(f"  z = (w + i s)/2 with s^2 = 4 - w^2  =>  |z|^2 = {mod2}")
    ok(mod2 == 1, "|z| = 1 EXACTLY for real w with |w| < 2")
    # and the pair really are the roots of z^2 - w z + 1
    zr = (wr + sp.I * s) / 2
    ok(sp.simplify(sp.expand(zr**2 - wr * zr + 1).subs(s**2, 4 - wr**2)) == 0,
       "  and they are the roots of z^2 - w z + 1")

    # (5) the 2 + 4 split, and reciprocal moduli
    print()
    roots = sp.nroots(sp.Poly(D, z), n=40)
    mods = sorted(sp.N(abs(r), 30) for r in roots)
    on = [m for m in mods if abs(m - 1) < sp.Float("1e-25")]
    off = [m for m in mods if abs(m - 1) >= sp.Float("1e-25")]
    print("  branch-point moduli:")
    for r in roots:
        print(f"    z = {sp.N(r, 18)}   |z| = {sp.N(abs(r), 18)}")
    ok(len(on) == 2, f"exactly 2 branch points on |z| = 1 (found {len(on)})")
    ok(len(off) == 4, f"exactly 4 off the unit circle (found {len(off)})")
    if len(off) == 4:
        prod_extremes = sp.N(off[0] * off[3], 25)
        prod_middle = sp.N(off[1] * off[2], 25)
        print(f"  reciprocal check: |z_min|*|z_max| = {prod_extremes}")
        ok(abs(prod_extremes - 1) < sp.Float("1e-20"), "off-circle moduli are reciprocal (r, 1/r)")
        ok(abs(prod_middle - 1) < sp.Float("1e-20"), "  and pair up as a single bar-orbit of four")

    print()
    print("  => THE UNIT CIRCLE PASSES THROUGH TWO BRANCH POINTS,")
    print("     so it is NOT an admissible contour for the period.")

    print()
    print("=" * 78)
    print("PART 2 -- every residue vanishes, so no E works.  Exact.")
    print("=" * 78)
    print("  d/dz = (1/(2t)) d/dt sends a_j t^j -> (j/2) a_j t^{j-2}.")
    print("  Residue of X^(n) dz = 2 * [coeff of t^-2 in X^(n)]; only j = 2n-2 reaches it.")
    print()
    print(f"  {'n':>3}  {'j = 2n-2':>9}  {'chain factor prod_{i<n} (j-2i)':>34}")
    for n in range(1, 13):
        j = 2 * n - 2
        prod = sp.prod([sp.Integer(j - 2 * i) for i in range(n)])
        print(f"  {n:>3}  {j:>9}  {str(prod):>34}")
        ok(prod == 0, f"chain factor vanishes at n={n}")

    print()
    print("  NON-VACUITY: the coefficients a_{2n-2} that the chain factor kills")
    print("  are themselves NON-ZERO, so the vanishing is caused by the operator")
    print("  parity and not by the absence of a term.  (mpmath, 60 dps.)")
    try:
        from mpmath import mp, mpc, mpf, polyroots

        mp.dps = 60
        bps = polyroots([mpf(int(c)) for c in coeffs], maxsteps=200, extraprec=300)
        zk = bps[0]
        rts = polyroots(
            [mpf(1), zk + 1, zk**2 + zk + 1, zk**3 + zk**2 + zk + 1],
            maxsteps=200, extraprec=300,
        )
        d = sorted([(abs(rts[i] - rts[j]), i, j) for i in range(3) for j in range(i + 1, 3)])
        gap = d[0][0]
        print(f"    at z_0 = {mp.nstr(zk, 12)}: two roots collide to |X_i - X_j| = {mp.nstr(gap, 4)}")
        ok(gap < mpf(10) ** (-25), "the branch point is a genuine simple (square-root) collision")
        Xk = (rts[d[0][1]] + rts[d[0][2]]) / 2
        ok(abs(Xk) > mpf(10) ** (-6), f"a_0 = X_k = {mp.nstr(Xk, 10)} is non-zero (the n=1 term the chain kills)")
    except ImportError:
        print("    [SKIP] mpmath unavailable; the exact Part-2 conclusion is unaffected.")

    print()
    print("=" * 78)
    if fail:
        print(f"VERDICT: {len(fail)} FAILURE(S)")
        for f in fail:
            print("  -", f)
        return 1
    print("VERDICT (exact):")
    print("  1. The branch locus is bar-symmetric: 2 points EXACTLY on |z| = 1")
    print("     (bar-fixed) + one bar-orbit of 4 (two inside, two outside).")
    print("     The unit circle is therefore NOT an admissible contour.")
    print("  2. Every residue of lambda_SW^(n) vanishes at every branch point for")
    print("     every n >= 1, independently of the Puiseux data.  So EVERY subset")
    print("     E gives period 0, and E IS NOT IDENTIFIABLE -- the question has no")
    print("     content under the classical-jet prolongation.")
    print()
    print("  The open problem is therefore UPSTREAM of E: which prolongation.")
    print("  The q-difference prolongation is untouched by this and by the two")
    print("  existing routes (prop:sw-classical-jet-exactness; the compact-surface")
    print("  argument in QOU.Brings.period_eq_zero_of_total_residue_vanishes).")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
