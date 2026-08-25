#!/usr/bin/env python3
"""The sharp Laplace sum — bean `qou-fybg`, step 8 (gap B, first half).

Checks `QOU/MathlibExt/GaussianThetaBound.lean`:

  norm_jacobiTheta₂_sub_one_le
      |Re theta_2(-c, i pi/a) - 1|  <=  2q/(1-q),   q = exp(-pi^2/a)

  abs_tsum_gaussian_sub_sqrt_le
      | sum_{n in Z} exp(-a(n-c)^2)  -  sqrt(pi/a) |
          <=  sqrt(pi/a) * 2q/(1-q)

The claim that matters for `c_sigma` is not that this is A bound but that it
is the SHARP one: the discrete sum equals the Gaussian integral `sqrt(pi/a)`
with an error that is exponentially small in `1/a`, uniformly in the shift `c`.
`GaussianSumBound`'s `sum <= 1 + sqrt(pi/a)/2` is off by an additive `1` and
cannot see the constant at all.

Part (iii) is the point of contact with the Kashaev arc: at `a = sqrt3 pi/N`
the error is `exp(-pi N/sqrt3)`, so for the constant, replacing the sum over
`k` by a Gaussian integral is free.

Run:  python3 computations/probes/gaussian_theta_bound_probe.py
"""

from mpmath import mp, mpf, exp, pi, sqrt, cos, log

mp.dps = 60

FAILURES = []
TOL = mpf(10) ** (-45)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def gauss_sum(a, c, halfwidth=None):
    """sum_{n in Z} exp(-a (n-c)^2), truncated where terms fall below 1e-55."""
    if halfwidth is None:
        halfwidth = int(sqrt(mpf(60) * log(10) / a)) + 20
    lo = int(c) - halfwidth
    return sum(exp(-a * (mpf(n) - c) ** 2) for n in range(lo, lo + 2 * halfwidth + 1))


def theta_re(a, c, terms=40):
    """Re theta_2(-c, i pi/a) = sum_{m in Z} cos(2 pi m c) exp(-pi^2 m^2/a)."""
    return 1 + 2 * sum(cos(2 * pi * m * c) * exp(-pi ** 2 * mpf(m) ** 2 / a)
                       for m in range(1, terms + 1))


def bound(a):
    q = exp(-pi ** 2 / a)
    return 2 * q / (1 - q)


print("=== (i) the theta bound |Re theta_2 - 1| <= 2q/(1-q) ===")
print(f"{'a':>8} {'c':>6} {'|Re th - 1|':>14} {'2q/(1-q)':>14} {'ratio':>8} {'ok':>4}")
for a in (mpf(3), mpf(1), mpf('0.5'), mpf('0.2')):
    for c in (mpf(0), mpf('0.25'), mpf('0.5'), mpf('0.7')):
        actual = abs(theta_re(a, c) - 1)
        b = bound(a)
        ok = actual <= b + TOL
        print(f"{float(a):8.3f} {float(c):6.2f} {float(actual):14.6e} "
              f"{float(b):14.6e} {float(b/actual) if actual > 0 else 0:8.3f} "
              f"{'ok' if ok else 'FAIL':>4}")
        check(ok, f"theta bound violated at a={a}, c={c}: {actual} > {b}")
# at c = 0 every term is positive and the bound is essentially attained
a0 = mpf(1)
check(abs(theta_re(a0, 0) - 1) > mpf('0.4') * bound(a0),
      "at c = 0 the bound should be near-attained (within a factor ~2); if it "
      "is not, `2q/(1-q)` is far looser than claimed")
print(f"  at c=0, a=1: actual/bound = "
      f"{float(abs(theta_re(a0, 0) - 1) / bound(a0)):.4f}  -- near-attained, "
      f"so the bound is not loose")

print()
print("=== (ii) the Laplace sum against its integral ===")
# Below NOISE the computed difference is mp roundoff, not the theta
# correction, and comparing it to the bound is vacuous.  Such rows are marked
# `noise` and assert only that the sum is indistinguishable from the integral
# at working precision -- claiming `ok` there would be reporting a check that
# did not happen.
NOISE = mpf(10) ** (-50)
print(f"{'a':>8} {'c':>6} {'sum':>18} {'sqrt(pi/a)':>18} {'|diff|':>13} "
      f"{'bound':>13} {'ok':>6}")
for a in (mpf(3), mpf(1), mpf('0.5'), mpf('0.2'), mpf('0.05')):
    for c in (mpf(0), mpf('0.5')):
        s = gauss_sum(a, c)
        g = sqrt(pi / a)
        diff = abs(s - g)
        b = g * bound(a)
        if diff < NOISE and b < NOISE:
            verdict = 'noise'
            check(diff < NOISE,
                  f"at a={a}, c={c} the sum should be indistinguishable from "
                  f"the integral at working precision; got {diff}")
        else:
            verdict = 'ok' if diff <= b + TOL else 'FAIL'
            check(diff <= b + TOL,
                  f"Laplace bound violated at a={a}, c={c}: {diff} > {b}")
        print(f"{float(a):8.3f} {float(c):6.2f} {float(s):18.12f} "
              f"{float(g):18.12f} {float(diff):13.5e} {float(b):13.5e} "
              f"{verdict:>6}")

print()
print("=== (iii) c = 1/2 is the worst shift, and it is still exponentially "
      "small ===")
# the sum is smallest at c = 1/2 (lattice straddles the peak); the theta
# correction changes SIGN there.  Uniformity in c is what the Lean statement
# claims, so check the extreme.
for a in (mpf(1), mpf('0.5')):
    s0, sh = gauss_sum(a, mpf(0)), gauss_sum(a, mpf('0.5'))
    g = sqrt(pi / a)
    print(f"  a={float(a):5.2f}: sum(c=0) - integral = {float(s0 - g):+.6e},  "
          f"sum(c=1/2) - integral = {float(sh - g):+.6e}")
    check(s0 > g and sh < g,
          f"expected the c=0 sum above the integral and the c=1/2 sum below "
          f"it at a={a}; got {s0-g} and {sh-g}")
    check(abs(sh - g) <= g * bound(a) + TOL,
          f"the bound fails at the worst shift c=1/2, a={a}")

print()
print("=== (iv) the Kashaev regime a = sqrt3 pi / N ===")
print(f"{'N':>6} {'a':>12} {'sqrt(pi/a)':>13} {'rel. error bound':>18}")
for N in (12, 60, 240, 960):
    a = sqrt(3) * pi / N
    rel = bound(a)
    print(f"{N:6d} {float(a):12.6f} {float(sqrt(pi/a)):13.6f} "
          f"{float(rel):18.6e}")
    check(rel < mpf('1e-8') or N < 20,
          f"at N={N} the theta correction {rel} is not negligible")
    # sqrt(pi/a) = sqrt(N/sqrt3); THIS is where 3^(-1/4) comes from
    check(abs(sqrt(pi / a) - sqrt(mpf(N) / sqrt(3))) < mpf('1e-40'),
          f"sqrt(pi/a) != sqrt(N/sqrt3) at N={N}")
print(f"  sqrt(pi/a) = sqrt(N/sqrt3) = N^(1/2) * 3^(-1/4)   <-- the constant")
print(f"  3^(-1/4) = {float(mpf(3) ** mpf('-0.25')):.10f}")
check(abs(sqrt(1 / sqrt(3)) - mpf(3) ** mpf('-0.25')) < mpf('1e-40'),
      "sqrt(1/sqrt3) != 3^(-1/4) -- the identification of c_sigma is wrong")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
