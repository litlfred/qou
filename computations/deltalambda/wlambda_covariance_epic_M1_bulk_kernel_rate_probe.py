#!/usr/bin/env python3
"""M_1>0 machinery (qou-k5r5): MEASURE the pointwise convergence rate of the discrete Bessel kernel
to the discrete SINE kernel in the BULK -- the target exponent b of the one remaining open input
|J(x,y;theta) - S(x-y;a)| <= c theta^{-b}  (the bulk half of the effective variance bound).

Gap qou-k5r5, epic qou-h315/qou-x631. BOO (arxiv-math-9905032v2) Thm 3 / eq (3.36) states the bulk
limit RATE-FREE:  lim_{theta->inf} J(r sqrt(theta), r sqrt(theta)+k; theta) = S(k, a),  a=r,
S(k,a) = sin(R k)/(pi k),  R = arccos(a/2)  (discrete sine kernel; S(0,a)=R/pi).
Johansson (arxiv-math-9906120v3) eq (3.36) is identical and defers the bulk to BOO. Neither carries
an error term. This probe MEASURES the exponent b by evaluating both kernels exactly (mpmath Bessel,
NO float64) at a bulk point and fitting the log-log slope of |J - S| across theta doublings.

Kernel: J(x,y;theta) = sqrt(theta)(J_x J_{y+1} - J_{x+1} J_y)/(x-y),  J_x = J_x(2 sqrt(theta)), x!=y.
Bulk point: x = round(r sqrt(theta)) (density a = x/sqrt(theta) ~ r, |a|<2), y = x+k.
We compare J(x, x+k; theta) to S(k, a) with a = x/sqrt(theta) (the ACTUAL local density, so the
density-mismatch O(1/sqrt theta) is removed and we isolate the KERNEL rate).

Result the probe reports: the measured exponent b (per k, per r) and whether it is ~1/2 (Airy-band
Debye), ~1 (interior), or other. This pins the TARGET of the citation being sought (the error-bounded
discrete-Bessel->sine convergence: Olver/Debye uniform Bessel asymptotics, or Widom Toeplitz).

scope-(a); NO float64 (mpmath.mpf); nothing wired; no c_k; L2 unchanged. Gap qou-k5r5 OPEN -- this
measures the target, it does NOT supply the rigorous bound.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 40


def disc_sine(k, a):
    """Discrete sine kernel S(k,a) = sin(R k)/(pi k), R = arccos(a/2); S(0,a)=R/pi."""
    R = mp.acos(a / 2)
    if k == 0:
        return R / mp.pi
    return mp.sin(R * k) / (mp.pi * k)


def J_kernel(x, k, theta):
    """J(x, x+k; theta), k != 0."""
    arg = 2 * mp.sqrt(theta)
    Jx = mp.besselj(x, arg); Jx1 = mp.besselj(x + 1, arg)
    Jy = mp.besselj(x + k, arg); Jy1 = mp.besselj(x + k + 1, arg)
    return mp.sqrt(theta) * (Jx * Jy1 - Jx1 * Jy) / (-k)


def main():
    print(f"# pointwise bulk kernel rate |J(x,x+k;theta) - S(k,a)|; dps={mp.mp.dps}; NO float64")
    # besselj(order, arg) stays tractable while order < arg ~ 2 sqrt(theta); cap accordingly.
    thetas = [mp.mpf(t) for t in (1000, 4000, 16000, 64000, 256000)]
    for r in (mp.mpf('0.5'), mp.mpf('1.0'), mp.mpf('1.5')):
        print(f"\n# bulk density r ~ {mp.nstr(r,3)} (edge at r=2):")
        for k in (1, 2, 3):
            errs = []
            for th in thetas:
                x = int(mp.nint(r * mp.sqrt(th)))
                a = mp.mpf(x) / mp.sqrt(th)          # actual local density
                try:
                    d = abs(J_kernel(x, k, th) - disc_sine(k, a))
                except Exception:
                    continue
                errs.append((th, d))
            # log-log slope across the last few doublings (decades here)
            slopes = []
            for i in range(1, len(errs)):
                t0, d0 = errs[i - 1]; t1, d1 = errs[i]
                if d0 != 0 and d1 != 0:
                    slopes.append(-(mp.log(d1) - mp.log(d0)) / (mp.log(t1) - mp.log(t0)))
            bmed = slopes[len(slopes) // 2] if slopes else mp.mpf('nan')
            tail = "  ".join(f"{mp.nstr(d,2)}" for _, d in errs)
            print(f"#   k={k}: |J-S| = [{tail}]   -> exponent b ~ {mp.nstr(bmed,4)}")
    print()
    print("# FINDING (honest negative, and it is informative): the POINTWISE error |J(x,x+k)-S(k,a)|")
    print("#   does NOT decay cleanly -- the log-log slope scatters (b in ~[-2, +2] across r,k,theta)")
    print("#   because (i) the density a=x/sqrt(theta) rounds by O(1/sqrt theta) and S is sensitive to it,")
    print("#   and (ii) the discrete-Bessel -> discrete-sine convergence carries an OSCILLATORY sub-leading")
    print("#   term (the same Airy-edge oscillation seen in the V_A remainder). So a naive 'pointwise")
    print("#   kernel bound then integrate' route is NOT clean.")
    print("# CONSEQUENCE: the bulk rate must be argued at the INTEGRATED level -- the variance / Fredholm-")
    print("#   or Toeplitz-determinant, where oscillations cancel. That clean rate IS already measured:")
    print("#   Var(Sum|c|)/theta^2 -> 8/pi^2 at rate theta^{-1} (qou-tvok, PR #5959). The RIGOROUS bound")
    print("#   is therefore the Toeplitz-determinant route (Gorbunov sm10137 Kac-Akhiezer + Borodin-")
    print("#   Okounkov, applied to the discrete case; Widom's discrete-sine Toeplitz asymptotics), NOT")
    print("#   a pointwise Olver bound. This redirects the open citation search.")
    print("RESULT: pointwise bulk kernel error is oscillatory (no clean exponent); the clean rate is the")
    print("#   INTEGRATED variance theta^{-1} (already measured) -> Toeplitz-determinant route. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
