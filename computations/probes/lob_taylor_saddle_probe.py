#!/usr/bin/env python3
"""Lambda at the saddle, to second order — bean `qou-fybg`, step 2.

Checks `QOU.Knot.FigureEightVolume.abs_Lob_taylor_saddle`
(`QOU/Knot/LobTaylorSaddle.lean`):

    | Lambda(theta) - ( Lambda(th*) + (sqrt3/2)(theta - th*)^2 ) |
        <= M |theta - th*|^3 / 6,     th* = 5 pi / 6

with M any bound on 1/sin^2 between the two points. Three things are checked:

  (i)   the LINEAR term is absent because Lambda'(th*) = -log(2 sin th*) = 0
        exactly — the saddle condition, not a dropped small term;
  (ii)  the quadratic coefficient is Lambda''(th*)/2 = -cot(th*)/2 = sqrt3/2,
        so the Hessian of the Kashaev exponent -(2N/pi)Lambda is -(2N/pi)sqrt3;
  (iii) the stated cubic bound holds, with the sharp constant 1/6.

Run:  python3 computations/probes/lob_taylor_saddle_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, clsin, quad
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


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def Lob(t):
    return clsin(2, 2 * t) / 2


TH = 5 * pi / 6

print("=== (i) the saddle condition is exact ===")
print(f"  2 sin(5pi/6)          = {mp.nstr(2 * sin(TH), 30)}")
print(f"  Lambda'(th*) = -log(2 sin th*) = {mp.nstr(-log(2 * sin(TH)), 5)}")
check(abs(2 * sin(TH) - 1) < mpf(10) ** (-45), "2 sin(5pi/6) != 1")
check(abs(log(2 * sin(TH))) < mpf(10) ** (-45), "Lambda'(5pi/6) != 0")

print()
print("=== (ii) the quadratic coefficient is the Hessian ===")
cot = cos(TH) / sin(TH)
print(f"  cot(5pi/6)            = {mp.nstr(cot, 30)}")
print(f"  -sqrt3                = {mp.nstr(-sqrt(3), 30)}")
print(f"  Lambda''(th*)/2 = -cot/2 = {mp.nstr(-cot / 2, 30)}")
print(f"  sqrt3/2               = {mp.nstr(sqrt(3) / 2, 30)}")
check(abs(cot + sqrt(3)) < mpf(10) ** (-45), "cot(5pi/6) != -sqrt3")
# Lambda'' by central difference, as an independent read on the sign/size
eps = mpf(10) ** (-12)
d2 = (Lob(TH + eps) - 2 * Lob(TH) + Lob(TH - eps)) / eps ** 2
print(f"  Lambda''(th*) numerically = {mp.nstr(d2, 12)}   (sqrt3 = "
      f"{mp.nstr(sqrt(3), 12)})")
check(abs(d2 - sqrt(3)) < mpf('1e-8'),
      f"numerical Lambda''(th*) = {d2}, expected sqrt3")

print()
print("=== (iii) the cubic bound, with the sharp constant 1/6 ===")
print(f"{'d':>10} {'|residual|':>16} {'M|d|^3/6':>16} {'ratio':>9}")
for d in [mpf(1) / 2, mpf(1) / 4, mpf(1) / 8, mpf(1) / 16, mpf(1) / 32,
          mpf(1) / 64, -mpf(1) / 4, -mpf(1) / 8, -mpf(1) / 16]:
    th = TH + d
    resid = abs(Lob(th) - (Lob(TH) + sqrt(3) * d ** 2 / 2))
    # M = sup of 1/sin^2 between the two points; sin is monotone on each side
    lo, hi = (min(TH, th), max(TH, th))
    M = max(1 / sin(lo) ** 2, 1 / sin(hi) ** 2)
    bound = M * abs(d) ** 3 / 6
    ratio = float(bound / resid) if resid > 0 else float('inf')
    print(f"{float(d):10.5f} {float(resid):16.6e} {float(bound):16.6e} "
          f"{ratio:9.2f}x")
    check(resid <= bound, f"cubic bound violated at d={d}: {resid} > {bound}")

print()
print("=== (iv) the residual really is Theta(|d|^3), so 1/6 is not slack ===")
print(f"{'d':>10} {'residual/|d|^3':>18}")
prev = None
for d in [mpf(1) / 8, mpf(1) / 16, mpf(1) / 32, mpf(1) / 64, mpf(1) / 128]:
    th = TH + d
    resid = abs(Lob(th) - (Lob(TH) + sqrt(3) * d ** 2 / 2))
    r = resid / abs(d) ** 3
    print(f"{float(d):10.6f} {float(r):18.10f}")
    if prev is not None:
        check(abs(r - prev) < mpf('0.05'),
              f"residual/|d|^3 not converging: {prev} -> {r}")
    prev = r
# the limit is |Lambda'''(th*)|/6 = (1/sin^2 th*)/6 = 4/6 = 2/3
print(f"  limit should be |Lambda'''(th*)|/6 = (1/sin^2(5pi/6))/6 = "
      f"{float(1 / sin(TH) ** 2 / 6):.10f}")
check(abs(prev - 1 / sin(TH) ** 2 / 6) < mpf('0.02'),
      f"residual/|d|^3 -> {prev}, expected {1 / sin(TH) ** 2 / 6}")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
