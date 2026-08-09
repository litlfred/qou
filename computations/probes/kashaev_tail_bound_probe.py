#!/usr/bin/env python3
"""Gaussian decay away from the Kashaev saddle — bean `qou-fybg`, step 3.

Checks `QOU.Knot.FigureEightVolume.kashaevProd_right_tail`
(`QOU/Knot/KashaevTailBound.lean`):

    kashaevProd(N, k*+d) <= kashaevProd(N, k*) * exp(-sqrt3 pi d(d-1)/N)

with k* = floor(5N/6), and the pointwise bound it rests on,

    log(2 sin theta) <= -sqrt3 (theta - 5pi/6)      for theta in (0, pi)

which is the tangent line to a CONCAVE function at its zero.

The point of part (iii): the naive bound "every ratio is at most the first
one" gives only exp(-c d/N), which does NOT confine the sum to a sqrt(N)
window. The d^2 comes from the factors continuing to shrink.

Run:  python3 computations/probes/kashaev_tail_bound_probe.py
"""

from mpmath import mp, mpf, sin, log, pi, sqrt, exp

mp.dps = 40

FAILURES = []
TOL = mpf(10) ** (-30)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def log_prod(N, k):
    """log kashaevProd(N,k) = 2 sum_{j=1}^{k} log(2 sin(j pi / N))."""
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


TH = 5 * pi / 6

print("=== (i) the tangent bound log(2 sin th) <= -sqrt3 (th - 5pi/6) ===")
worst = None
for i in range(1, 400):
    th = mpf(i) * pi / 400
    lhs = log(2 * sin(th))
    rhs = -sqrt(3) * (th - TH)
    gap = rhs - lhs
    if worst is None or gap < worst[1]:
        worst = (float(th), float(gap))
    check(lhs <= rhs + TOL, f"tangent bound violated at theta={th}")
print(f"  400 sample angles in (0, pi): min slack = {worst[1]:.3e} at "
      f"theta = {worst[0]:.4f}   (touches 0 at 5pi/6 = {float(TH):.4f})")

print()
print("=== (ii) the right tail, against the Lean bound ===")
print(f"{'N':>6} {'d':>5} {'ratio g/g*':>14} {'exp(-c d(d-1)/N)':>18} {'ok':>4}")
for N in (60, 120, 240, 480):
    ks = 5 * N // 6
    base = log_prod(N, ks)
    for d in (0, 1, 2, 5, 10, 20, 40):
        if ks + d >= N:
            continue
        ratio = exp(log_prod(N, ks + d) - base)
        bound = exp(-sqrt(3) * pi * mpf(d) * (mpf(d) - 1) / N)
        ok = ratio <= bound + TOL
        print(f"{N:6d} {d:5d} {float(ratio):14.6e} {float(bound):18.6e} "
              f"{'ok' if ok else 'FAIL':>4}")
        check(ok, f"right tail violated at N={N}, d={d}: {ratio} > {bound}")

print()
print("=== (iii) d^2/N, not d/N: the naive first-factor bound is too weak ===")
print(f"{'N':>6} {'d':>5} {'true ratio':>14} {'d^2/N bound':>14} "
      f"{'first-factor^d':>16}")
for N in (240, 480):
    ks = 5 * N // 6
    base = log_prod(N, ks)
    first = exp(2 * log(2 * sin(mpf(ks + 1) * pi / N)))   # the largest ratio
    for d in (10, 20, 40, 60):
        if ks + d >= N:
            continue
        ratio = exp(log_prod(N, ks + d) - base)
        good = exp(-sqrt(3) * pi * mpf(d) * (mpf(d) - 1) / N)
        naive = first ** d
        print(f"{N:6d} {d:5d} {float(ratio):14.6e} {float(good):14.6e} "
              f"{float(naive):16.6e}")
        check(ratio <= good + TOL, f"quadratic bound failed at N={N}, d={d}")
        # the naive bound is valid but weaker — that is the point
        check(ratio <= naive + TOL, f"naive bound failed at N={N}, d={d}")
        check(good <= naive + TOL,
              f"at N={N}, d={d} the quadratic bound is NOT tighter than the "
              f"naive one — the file's claim would be wrong")

print()
print("=== (iv) the sqrt(N) window: where the bound crosses 1e-6 ===")
for N in (60, 240, 960, 3840):
    d = 1
    while exp(-sqrt(3) * pi * mpf(d) * (mpf(d) - 1) / N) > mpf('1e-6'):
        d += 1
    print(f"  N={N:5d}: bound < 1e-6 by d = {d:4d};  d/sqrt(N) = "
          f"{float(d / mpf(N) ** mpf('0.5')):.3f}")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
