#!/usr/bin/env python3
"""Numerical check of the FINAL ASSEMBLY bound for bean `qou-mlgp` (A).

The Lean theorem `QOU.Knot.FigureEightVolume.kashaev_log_sum_asymptotic`
(`QOU/Knot/KashaevAsymptotic.lean`) asserts, with `h = pi/N`, `theta = k*h`:

    | L_k  -  ( -(N/pi)*Lob(theta) + (1/2)*log(2*N*sin theta)
                + (pi/(12N))*cot(theta) ) |
        <=  1/(144 k^2) + (7/12) h^2 + h^2/(12 sin^2 theta)

for `1 <= k < N` and `h <= 1`, where `L_k = sum_{j=1}^{k} log(2 sin(j pi/N))`.

This probe checks (i) the bound holds with room to spare, (ii) the residual is
genuinely O(1/N^2) so the bound is not vacuous, and (iii) each of the five
error terms the Lean proof bounds separately is inside its own bound.

Run:  python3 computations/probes/kashaev_assembly_bound_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, factorial, clsin, quad

mp.dps = 60


def Lob(t):
    """Lobachevsky Lambda(t) = Cl_2(2t)/2."""
    return clsin(2, 2 * t) / 2


def L(N, k):
    """sum_{j=1}^{k} log(2 sin(j pi / N))."""
    return sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def logSinc(x):
    return log(sin(x)) - log(x)


def target(N, k):
    h = pi / N
    th = k * h
    return (-(mpf(N) / pi) * Lob(th)
            + log(2 * N * sin(th)) / 2
            + (pi / (12 * N)) * (cos(th) / sin(th)))


def bound(N, k):
    h = pi / N
    th = k * h
    return (mpf(1) / (144 * mpf(k) ** 2)
            + mpf(7) / 12 * h ** 2
            + h ** 2 / (12 * sin(th) ** 2))


FAILURES = []


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


print("=== (i) the asserted bound, over a grid of (N, k) ===")
print(f"{'N':>6} {'k':>6} {'theta/pi':>10} {'residual':>14} {'bound':>14} {'slack':>9}")
for N in (8, 16, 32, 64, 128, 256, 512):
    for frac in (mpf(1) / 12, mpf(1) / 4, mpf(1) / 2, mpf(5) / 6, mpf(11) / 12):
        k = int(frac * N)
        if k < 1 or k >= N:
            continue
        res = abs(L(N, k) - target(N, k))
        bd = bound(N, k)
        slack = float(bd / res) if res > 0 else float('inf')
        print(f"{N:6d} {k:6d} {float(mpf(k)/N):10.4f} "
              f"{float(res):14.3e} {float(bd):14.3e} {slack:9.1f}x")
        check(res <= bd, f"bound violated at N={N}, k={k}: {res} > {bd}")

print()
print("=== (ii) the residual is O(1/N^2) at fixed theta = 5pi/6 ===")
print(f"{'N':>6} {'residual':>16} {'residual*N^2':>16}")
prev = None
for N in (60, 120, 240, 480, 960):
    k = 5 * N // 6
    res = abs(L(N, k) - target(N, k))
    print(f"{N:6d} {float(res):16.6e} {float(res * N ** 2):16.6e}")
    if prev is not None:
        # ratio of successive residuals should be ~1/4 or better
        check(res < prev * mpf('0.35'),
              f"residual not decaying like 1/N^2 at N={N}")
    prev = res

print()
print("=== (iii) the five error terms, each inside its own Lean bound ===")
for N in (16, 64, 256):
    k = 5 * N // 6
    h = pi / N
    th = k * h
    # rho: Robbins remainder of log(k!)
    rho = (log(factorial(k))
           - (k * log(k) - k + log(mpf(k)) / 2 + log(2 * pi) / 2))
    t1 = rho - mpf(1) / (12 * k)
    # delta: Lob near zero
    delta = Lob(h) - (h - h * log(2 * h))
    t2 = delta / h
    # logSinc(h)/2
    t3 = logSinc(h) / 2
    # -(h/12) * (cot h - 1/h)
    t4 = -(h / 12) * (cos(h) / sin(h) - 1 / h)
    # E_em: the Euler-Maclaurin remainder
    S = sum(logSinc(mpf(j) * h) for j in range(1, k + 1))
    integral = quad(logSinc, [h, th])
    g1 = lambda x: cos(x) / sin(x) - 1 / x
    E = S - ((1 / h) * integral + (logSinc(h) + logSinc(th)) / 2
             + (h / 12) * (g1(th) - g1(h)))
    g2 = lambda x: 1 / x ** 2 - 1 / sin(x) ** 2
    bounds = [mpf(1) / (144 * mpf(k) ** 2), h ** 2 / 3, h ** 2 / 6,
              h ** 2 / 12, h ** 2 / 12 * (g2(h) - g2(th))]
    terms = [t1, t2, t3, t4, E]
    names = ["rho-1/12k", "delta/h", "logSinc(h)/2", "-(h/12)g1(h)", "E_em"]
    print(f"  N={N}, k={k}")
    for nm, tm, bd in zip(names, terms, bounds):
        ok = abs(tm) <= bd
        print(f"    {nm:>14}: |{float(tm):11.4e}| <= {float(bd):11.4e}  {'ok' if ok else 'FAIL'}")
        check(ok, f"term {nm} exceeds its bound at N={N}")
    # and the exact decomposition L_k = target + sum(terms)
    recon = target(N, k) + sum(terms)
    check(abs(recon - L(N, k)) < mpf(10) ** (-40),
          f"decomposition identity broken at N={N}: {abs(recon - L(N, k))}")
    print(f"    decomposition residual: {float(abs(recon - L(N, k))):.3e}")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
