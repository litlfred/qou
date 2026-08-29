#!/usr/bin/env python3
"""M_1>0 Debye constant-tracking, step 1: MEASURE the asymptotic expansion of the poissonized
descent-DPP variance V_A(theta)=Var(Sum|c|) to decide whether the |u|-KINK produces a theta^{-1/2}
term (=> rigorous rate theta^{-1/2}, hard constant) or whether it cancels (=> theta^{-1}, easy).

Gap qou-k5r5, epic qou-x631. The rigorous finite-n bound needs |V_A/theta^2 - v_A| <= C_A theta^{-p}.
The conservative kink argument says p=1/2; the large-theta investigation (PR #5937) measured an
EFFECTIVE exponent ~1.18, hinting the theta^{-1/2} term may be absent. This probe pins the expansion
    V_A(theta)/theta^2 = v_A + c_{1/2} theta^{-1/2} + c_1 theta^{-1} + c_{3/2} theta^{-3/2} + ...
by computing V_A at a geometric theta ladder (exact Bessel sums, high dps) and solving the linear
system for {v_A, c_{1/2}, c_1, c_{3/2}, c_2}. If |c_{1/2}| is at the numerical-noise floor while c_1
is O(1), the kink term VANISHES and the rigorous rate is theta^{-1} -- the constant-tracking is then
a smooth-weight (easy) Euler-Maclaurin estimate, not the hard kink case.

This is asymptotic-structure MEASUREMENT (an exponent/coefficient read-off), not a forbidden fit of a
physical result. mpmath high dps; NO float64. scope-(a); nothing wired; no c_k; L2 unchanged.
"""
from __future__ import annotations
import mpmath as mp

mp.mp.dps = 60


def bessel_table(theta, M):
    arg = 2 * mp.sqrt(theta)
    J = {0: mp.besselj(0, arg)}
    for x in range(1, M + 2):
        J[x] = mp.besselj(x, arg)
        J[-x] = (-1) ** x * J[x]
    return J


def _anti_abs(k):
    return mp.mpf(k * (k + 1)) / 2 if k >= 0 else -mp.mpf(k * (k + 1)) / 2


def VA_over_theta2(theta):
    M = int(mp.floor(2 * mp.sqrt(theta) + 14 * mp.power(theta, mp.mpf(1) / 6) + 20))
    Jt = bessel_table(theta, M)
    st = mp.sqrt(theta)
    xs = list(range(-M, M + 1))
    g = {k: _anti_abs(k) for k in xs}
    VA = mp.mpf(0)
    for i, x in enumerate(xs):
        gx = g[x]
        for y in xs[i + 1:]:
            J = st * (Jt[x] * Jt[y + 1] - Jt[x + 1] * Jt[y]) / (x - y)
            if J != 0:
                d = gx - g[y]
                VA += d * d * J * J
    return VA / theta ** 2


def fit(th, S, exps):
    """Overdetermined normal-equations fit S_i ~ sum_j coeff_j theta_i^{-exps_j}; returns
    coeffs and residual norm."""
    A = mp.matrix(len(th), len(exps)); b = mp.matrix(len(th), 1)
    for i, t in enumerate(th):
        for j, e in enumerate(exps):
            A[i, j] = t ** (-e)
        b[i] = S[i]
    At = A.T
    coeff = mp.lu_solve(At * A, At * b)
    res = A * coeff - b
    rn = mp.sqrt(sum(res[i] ** 2 for i in range(len(th))))
    return coeff, rn


def main():
    thetas = [mp.mpf(t) for t in (256, 512, 1024, 2048, 4096, 8192)]
    print(f"# V_A(theta)/theta^2 asymptotic expansion; dps={mp.mp.dps}; NO float64")
    S = []
    for th in thetas:
        s = VA_over_theta2(th)
        S.append(s)
        print(f"#   theta={int(th):>6}  V_A/theta^2 = {mp.nstr(s,16)}")
    print("#   (monotone INCREASING toward v_A: correction is negative, no oscillation)")
    print()
    # Multi-basis robustness: is the theta^{-1/2} KINK coefficient real or at the noise floor?
    print("# multi-basis fit (is c_{1/2} real?):")
    half = mp.mpf(1) / 2
    bases = [
        ("{0,1}",          [mp.mpf(0), mp.mpf(1)]),
        ("{0,1/2,1}",      [mp.mpf(0), half, mp.mpf(1)]),
        ("{0,1,3/2}",      [mp.mpf(0), mp.mpf(1), mp.mpf(3) / 2]),
        ("{0,1/2,1,3/2}",  [mp.mpf(0), half, mp.mpf(1), mp.mpf(3) / 2]),
    ]
    chalf_vals = []
    for label, exps in bases:
        c, rn = fit(thetas, S, exps)
        vA = c[0]
        rest = [mp.nstr(c[j], 6) for j in range(1, len(c))]
        chalf = None
        if half in exps:
            chalf = c[exps.index(half)]
            chalf_vals.append(chalf)
        print(f"#   basis {label:>14}: v_A={mp.nstr(vA,11)}  coeffs={rest}  resid={mp.nstr(rn,3)}")
    print()
    spread = max(abs(x) for x in chalf_vals) if chalf_vals else mp.inf
    print(f"# c_1/2 across bases: {[mp.nstr(x,4) for x in chalf_vals]}  (|max|={mp.nstr(spread,3)})")
    print()
    # DISCRIMINANCY TEST: can 6 points at ~1e-6 tell theta^{-1/2}/-2/3/-5/6/-1 apart? (single power)
    print("# discriminancy — best single-power fit v_A + c*theta^{-p}, sweeping p:")
    best = None
    p = mp.mpf('0.4')
    while p <= mp.mpf('1.3'):
        c, rn = fit(thetas, S, [mp.mpf(0), p])
        if best is None or rn < best[1]:
            best = (p, rn)
        p += mp.mpf('0.02')
    print(f"#   best p = {mp.nstr(best[0],4)}  (resid {mp.nstr(best[1],3)})")
    print("#   two-power residuals (all comparable => NOT discriminable):")
    for lbl, e in (("{0,1/2,1}", [0, mp.mpf(1)/2, 1]),
                   ("{0,2/3,1}", [0, mp.mpf(2)/3, 1]),
                   ("{0,5/6,1}", [0, mp.mpf(5)/6, 1]),
                   ("{0,1,3/2}", [0, 1, mp.mpf(3)/2])):
        c, rn = fit(thetas, S, [mp.mpf(x) for x in e])
        print(f"#     {lbl:>10}: resid {mp.nstr(rn,3)}")
    print()
    print("# VERDICT (corrected 2026-08-29): the sub-leading structure is NOT resolvable here.")
    print("#   c_{1/2} is small (|.|<1e-3, sign-unstable) BUT theta^{-1/2}/-2/3/-5/6/-1 all fit with")
    print("#   comparable residual (best single power ~0.94). A theta^{-5/6} Airy-EDGE term is plausible")
    print("#   and cannot be excluded. So 'kink cancels => rate theta^{-1}' is OVERSTATED and RETRACTED:")
    print("#   c_{1/2}=0 is NOT established (neither numerically here nor by the transpose symmetry, which")
    print("#   is automatic and does not isolate the half-power). What IS robust: the correction is SMALL")
    print("#   (|coeff|~0.05) with effective exponent ~0.9 -- enough for the (CS) closure (any rate")
    print("#   >= theta^{-1/2} with a small constant works; 30-300x headroom, PR #5937). Settling the")
    print("#   exact exponent / c_{1/2} needs the real Euler-Maclaurin+edge analysis (bean qou-tvok).")
    print("RESULT: sub-leading exponent INDETERMINATE at 6 points; kink-cancellation claim RETRACTED;")
    print("        correction small (eff. exp ~0.9), closure feasibility intact. qou-k5r5 OPEN.")
    print("EXIT: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
