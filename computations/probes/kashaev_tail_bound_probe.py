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
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

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
print("=== (iv) the SECANT bound log(2 sin th) >= (5pi/6 - th)/sqrt3 ===")
worstsec = None
for i in range(0, 201):
    th = 2 * pi / 3 + mpf(i) * (5 * pi / 6 - 2 * pi / 3) / 200
    lhs = (5 * pi / 6 - th) / sqrt(3)
    rhs = log(2 * sin(th))
    gap = rhs - lhs
    if worstsec is None or gap < worstsec[1]:
        worstsec = (float(th), float(gap))
    check(lhs <= rhs + TOL, f"secant bound violated at theta={th}")
print(f"  201 sample angles in [2pi/3, 5pi/6]: min slack = {worstsec[1]:.3e} "
      f"at theta = {worstsec[0]:.4f}   (touches 0 at both ends)")
# Below 2pi/3 the bound eventually FAILS -- that is why the Lean statement
# carries the window. It is not tight: the bound survives a little past 2pi/3
# (concavity keeps it going for a while) and dies well before 0. Both shown,
# so the window is not read as sharp.
for th_bad in (mpf('1.9'), mpf('1.5'), mpf('1.0'), mpf('0.5')):
    lo = (5 * pi / 6 - th_bad) / sqrt(3)
    hi = log(2 * sin(th_bad))
    print(f"    theta = {float(th_bad):.4f}: secant claims {float(lo):9.6f} "
          f"<= {float(hi):9.6f}  -> {'holds' if lo <= hi else 'FAILS'}")
check((5 * pi / 6 - mpf('1.0')) / sqrt(3) > log(2 * sin(mpf('1.0'))),
      "the secant bound was expected to FAIL at theta = 1.0 (well below "
      "2pi/3); if it holds there the window in the Lean statement is "
      "mis-motivated")

print()
print("=== (v) the left tail, against the Lean bound ===")
print(f"{'N':>6} {'d':>5} {'ratio g/g*':>14} {'exp(-c d(d-1)/N)':>18} {'ok':>4}")
for N in (60, 120, 240, 480):
    ks = 5 * N // 6
    base = log_prod(N, ks)
    for d in (0, 1, 2, 5, 10, 20, 40):
        k = ks - d
        if k < 0 or 3 * k < 2 * N:      # the secant window
            continue
        ratio = exp(log_prod(N, k) - base)
        bound = exp(-pi * mpf(d) * (mpf(d) - 1) / (sqrt(3) * N))
        ok = ratio <= bound + TOL
        print(f"{N:6d} {d:5d} {float(ratio):14.6e} {float(bound):18.6e} "
              f"{'ok' if ok else 'FAIL':>4}")
        check(ok, f"left tail violated at N={N}, d={d}: {ratio} > {bound}")

print()
print("=== (vi) the sqrt(N) window: where the bound crosses 1e-6 ===")
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
