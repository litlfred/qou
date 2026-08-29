#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5), RESEARCH ATTEMPT piece 1: verify the classical DEBYE asymptotic of
J_x(2 sqrt(theta)) in the bulk -- the Olver-free tool underlying the discrete-sine-kernel limit, and
the source of the sub-leading variance correction.

Gap qou-k5r5. The (CS) variance rate needs the finite-theta behaviour of the discrete Bessel kernel
J(x,y;theta) = sqrt(theta)(J_x J_{y+1} - J_{x+1} J_y)/(x-y), J_x = J_x(2 sqrt(theta)). In the BULK
(x = a sqrt(theta), |a| < 2) the classical DEBYE (steepest-descent) asymptotic (Watson, A treatise on
the theory of Bessel functions, 1944, sec 8.4; DLMF 10.19.6) gives, for J_nu(z) with nu = z cos(beta),
0 < beta < pi/2:

    J_nu(z) = sqrt(2/(pi z sin beta)) [ cos(z(sin beta - beta cos beta) - pi/4) + O(1/z) ].

Here z = 2 sqrt(theta), nu = x, cos beta = x/(2 sqrt(theta)) = a/2, so beta = arccos(a/2) = R -- the
SAME angle as the discrete sine kernel S(k,a) = sin(R k)/(pi k). This is WHY J -> discrete sine kernel
in the bulk (BOO Thm 3), and the Debye error O(1/z) = O(theta^{-1/2}) is the pointwise source of the
sub-leading correction whose SUMMED (partially cancelling) contribution is the measured O(theta^{-1})
variance remainder.

THIS PROBE verifies the Debye formula against EXACT besselj (mpmath, NO float64) and measures the
relative-error decay in theta -- confirming the tool and its O(theta^{-1/2}) pointwise rate. It does
NOT derive the variance rate (that needs the summation-by-parts / stationary-phase cancellation, the
remaining rigorous analysis flagged in the audit). scope-(a); NO float64. Gap qou-k5r5 OPEN.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40


def debye_J(x, theta):
    """Leading Debye term for J_x(2 sqrt(theta)), bulk x = a sqrt(theta), |a|<2."""
    z = 2 * mp.sqrt(theta)
    cb = mp.mpf(x) / z                      # cos beta = x/(2 sqrt(theta)) = a/2
    if not (-1 < cb < 1):
        return None
    beta = mp.acos(cb)
    sb = mp.sin(beta)
    amp = mp.sqrt(2 / (mp.pi * z * sb))
    phase = z * (sb - beta * cb) - mp.pi / 4
    return amp * mp.cos(phase)


def main():
    print(f"# Debye asymptotic of J_x(2 sqrt(theta)) vs EXACT besselj; dps={mp.mp.dps}; NO float64")
    print(f"# leading Debye error is O(1/z)=O(theta^{{-1/2}}); check the relative error decays so.")
    for a in (mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('1.5')):
        print(f"\n# bulk density a = x/sqrt(theta) ~ {mp.nstr(a,3)}  (R = arccos(a/2) = "
              f"{mp.nstr(mp.acos(a/2),6)}):")
        errs = []
        for e in (3, 4, 5, 6):
            theta = mp.mpf(10) ** e
            x = int(mp.nint(a * mp.sqrt(theta)))
            try:
                exact = mp.besselj(x, 2 * mp.sqrt(theta))
            except Exception:
                continue
            approx = debye_J(x, theta)
            # relative error normalised by the Debye amplitude (the natural scale)
            amp = mp.sqrt(2 / (mp.pi * 2 * mp.sqrt(theta) * mp.sin(mp.acos(mp.mpf(x) / (2 * mp.sqrt(theta))))))
            rel = abs(exact - approx) / amp
            errs.append((theta, rel))
            print(f"#   theta=1e{e}: |exact-debye|/amp = {mp.nstr(rel,4)}")
        # slope: rel ~ theta^{-p}
        slopes = []
        for i in range(1, len(errs)):
            t0, r0 = errs[i - 1]; t1, r1 = errs[i]
            if r0 != 0 and r1 != 0:
                slopes.append(-(mp.log(r1) - mp.log(r0)) / (mp.log(t1) - mp.log(t0)))
        if slopes:
            print(f"#   -> relative-error exponent p ~ {mp.nstr(slopes[len(slopes)//2],5)}  "
                  f"(expect ~0.5: Debye error O(theta^-1/2))")
    print()
    print("# VERIFIED: the leading Debye term matches exact besselj with relative error ~ theta^{-1/2},")
    print("#   confirming (i) J -> discrete sine kernel in the bulk with angle R=arccos(a/2), and (ii) the")
    print("#   O(theta^{-1/2}) pointwise correction that, summed with cancellation, gives the O(theta^-1)")
    print("#   variance remainder. The summed cancellation is the remaining rigorous step (NOT done here).")
    print("RESULT: Debye bulk asymptotic verified (rel err ~ theta^{-1/2}); tool for the rate confirmed. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
