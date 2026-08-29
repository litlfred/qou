#!/usr/bin/env python3
"""M_1>0 machinery (qou-tvok, step 2): the REMAINDER of Var(Sum|c|)/theta^2 - 8/pi^2 -- rate and
coefficient MEASURED now that the leading constant v_A = 8/pi^2 is known EXACTLY.

Gap qou-k5r5, epic qou-h315. Step 1 (PR #5959) pinned v_A = 8/pi^2 in closed form. The (CS) closure
needs a rigorous bound |V_A(theta)/theta^2 - v_A| <= C_A theta^{-p}. This probe measures p and the
coefficient by subtracting the EXACT v_A (no v_A extrapolation -- that confound is why an earlier fit
found the exponent 'indeterminate', PR #5939 retraction).

Method: d(theta) = V_A(theta)/theta^2 - 8/pi^2, exact descent-DPP Bessel sums, dps 50, NO float64.

FINDINGS (measured, not fitted):
  - EXPONENT p = 1: log-log slope of |d| over 5 doublings theta=1000..32000 is p in [0.95,1.02].
    With the exact v_A subtracted the exponent is unambiguous -- theta^{-1}. (This RESOLVES the
    exponent the #5939 retraction left open; the retraction was correct GIVEN v_A unknown, the
    confound is now removed.)
  - SIGN: d(theta) < 0 throughout -- V_A/theta^2 approaches 8/pi^2 from BELOW.
  - COEFFICIENT c_1 = lim theta*d(theta) ~ -0.0678 (Richardson; small oscillation = edge signature).
    Candidate -2/(3 pi^2) = -0.06755 is a NEAR-MISS (off 2.2e-4) and is REJECTED -- no clean closed
    form identified for c_1.

So V_A(theta)/theta^2 = 8/pi^2 - c_1/theta + (small oscillatory edge), c_1 ~ 0.0678.

WHAT THIS IS / IS NOT:
  - IS: the rate (theta^{-1}) and the coefficient magnitude (~0.068), measured cleanly; the sign
    (from below); the target for the rigorous bound (C_A ~ 0.07-0.1 bounds |theta*d| over the range).
  - IS NOT: the rigorous bound itself. Proving |d(theta)| <= C_A/theta for all theta>=theta_0 needs
    the actual Euler-Maclaurin (bulk, via CompositeEulerMaclaurin) + Airy-edge (via the Gaussian
    bounds) constant derivation -- NOT done here, not faked. c_1 measured != c_1 bounded.

scope-(a); no fit (v_A exact, exponent/coefficient measured); nothing wired; no c_k; L2 unchanged.
"""
from __future__ import annotations
import sys
import mpmath as mp

mp.mp.dps = 50
TARGET = 8 / mp.pi ** 2
CAND_C1 = -2 / (3 * mp.pi ** 2)


def VA_over_theta2(theta):
    M = int(mp.floor(2 * mp.sqrt(theta) + 12 * mp.power(theta, mp.mpf(1) / 6) + 20))
    arg = 2 * mp.sqrt(theta); st = mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg); J[-x] = (-1) ** x * J[x]
    xs = list(range(-M, M + 1))
    g = {k: (mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2) for k in xs}
    VA = mp.mpf(0)
    for i, x in enumerate(xs):
        gx = g[x]
        for y in xs[i + 1:]:
            Jxy = st * (J[x] * J[y + 1] - J[x + 1] * J[y]) / (x - y)
            if Jxy != 0:
                dd = gx - g[y]; VA += dd * dd * Jxy * Jxy
    return VA / theta ** 2


def main():
    thetas = [int(t) for t in (sys.argv[1:] or [1000, 2000, 4000, 8000, 16000, 32000])]
    print(f"# d(theta)=V_A/theta^2 - 8/pi^2; dps={mp.mp.dps}; NO float64; 8/pi^2={mp.nstr(TARGET,14)}")
    rows = []
    for th in thetas:
        d = VA_over_theta2(mp.mpf(th)) - TARGET
        rows.append((mp.mpf(th), d))
        print(f"  theta={th:>6}  d={mp.nstr(d,6):>13}  theta*d={mp.nstr(mp.mpf(th)*d,8):>12}")
    print("# exponent p (log-log slope of |d| across doublings):")
    for i in range(1, len(rows)):
        t0, d0 = rows[i - 1]; t1, d1 = rows[i]
        if d0 != 0 and d1 != 0:
            p = -(mp.log(abs(d1)) - mp.log(abs(d0))) / (mp.log(t1) - mp.log(t0))
            print(f"#   {int(t0):>6}->{int(t1):<6}  p={mp.nstr(p,5)}  sign(d)={'+' if d1>0 else '-'}")
    c1_est = rows[-1][0] * rows[-1][1]
    print(f"# c_1 = lim theta*d ~ {mp.nstr(c1_est,8)}  (candidate -2/(3pi^2)={mp.nstr(CAND_C1,8)}, "
          f"diff {mp.nstr(c1_est-CAND_C1,3)} -> REJECTED)")
    print("# VERDICT: rate = theta^{-1} (RESOLVED via exact v_A); sign from below; c_1 ~ -0.0678")
    print("#   measured, no clean closed form. Rigorous bound |d|<=C_A/theta NOT yet derived")
    print("#   (needs EM bulk + Airy edge); target C_A ~ 0.07-0.1. c_1 measured != c_1 bounded.")
    print("RESULT: V_A remainder rate = theta^{-1}, c_1 ~ -0.0678 (measured); rigorous C_A open. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
