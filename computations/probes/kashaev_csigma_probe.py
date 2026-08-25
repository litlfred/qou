#!/usr/bin/env python3
"""`hc` derived — bean `qou-fybg`, step 20.

Checks `QOU/Knot/KashaevCSigma.lean`:

  cSigma_sq_mul_abs_cot     c_sigma(th)^2 |cot th| = (2 sin th)^2      <- `hc`
  stirling_mul_gaussWidth   (2N sin th) sqrt(pi/(pi|cot th|/N))
                              = c_sigma(th) N^{3/2}
  cSigma_saddle             c_sigma(5pi/6) = 1/sqrt(sqrt 3)
  cSigma_saddle_pow_four    c_sigma(5pi/6)^4 = 1/3
  k_sq_eq_half              k = c_sigma sqrt(|cot|/2)  =>  k^2 = 1/2

`hc` was a HYPOTHESIS of `OneLoopPrefactorInvariance`.  It is an identity for
the `c_sigma` the analysis actually produces, because that `c_sigma` has the
shape "Stirling factor over square-rooted Hessian" -- so squaring it and
multiplying by the Hessian cancels the Hessian.  Part (i) checks that at many
angles, not just the saddle, since nothing about `4_1` enters.

Part (iv) closes the loop: the value `c_sigma(5pi/6)` must agree with the
empirical limit of `<4_1>_N / (N^{3/2} e^{N Vol/2pi})` measured in steps 18-19.

Run:  python3 computations/probes/kashaev_csigma_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, exp, clsin
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
TOL = mpf(10) ** (-35)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def c_sigma(th):
    return 2 * sin(th) / sqrt(abs(cos(th) / sin(th)))


print("=== (i) `hc` holds at every angle with cot != 0, not just the saddle ===")
worst = mpf(0)
for i in range(1, 200):
    th = mpf(i) * pi / 200
    if abs(cos(th)) < mpf('1e-20'):
        continue
    lhs = c_sigma(th) ** 2 * abs(cos(th) / sin(th))
    rhs = (2 * sin(th)) ** 2
    rel = abs(lhs - rhs) / rhs
    worst = max(worst, rel)
    check(rel < mpf('1e-40'), f"hc fails at theta={th}: {lhs} vs {rhs}")
print(f"  199 angles in (0, pi), worst relative error {float(worst):.2e}")
print("  -- nothing about 4_1 enters; it is `Stirling / sqrt(Hessian)` squared.")

print()
print("=== (ii) the link back to the analysis ===")
print(f"{'th':>8} {'N':>7} {'(2N sin)*sqrt(pi/a)':>22} {'c_sigma * N^1.5':>18}")
for th in (mpf('2.0'), 5 * pi / 6, mpf('2.9')):
    for N in (100, 10000):
        a = pi * abs(cos(th) / sin(th)) / mpf(N)
        lhs = (2 * mpf(N) * sin(th)) * sqrt(pi / a)
        rhs = c_sigma(th) * (mpf(N) * sqrt(mpf(N)))
        check(abs(lhs - rhs) <= abs(rhs) * mpf('1e-40'),
              f"the link fails at theta={th}, N={N}")
        print(f"{float(th):8.4f} {N:7d} {float(lhs):22.10f} {float(rhs):18.10f}")

print()
print("=== (iii) at the saddle ===")
cs = c_sigma(5 * pi / 6)
print(f"  c_sigma(5pi/6)   = {float(cs):.14f}")
print(f"  1/sqrt(sqrt 3)   = {float(1 / sqrt(sqrt(3))):.14f}")
print(f"  3^(-1/4)         = {float(mpf(3) ** mpf('-0.25')):.14f}")
print(f"  c_sigma^4        = {float(cs ** 4):.14f}   (target 1/3 = "
      f"{float(mpf(1)/3):.14f})")
check(abs(cs - 1 / sqrt(sqrt(3))) < TOL, "c_sigma(5pi/6) != 1/sqrt(sqrt 3)")
check(abs(cs - mpf(3) ** mpf('-0.25')) < TOL, "c_sigma(5pi/6) != 3^(-1/4)")
check(abs(cs ** 4 - mpf(1) / 3) < TOL, "c_sigma(5pi/6)^4 != 1/3")
# and k^2 = 1/2, with the Hessian cancelling before it is evaluated
kk = cs * sqrt(abs(cos(5 * pi / 6) / sin(5 * pi / 6)) / 2)
print(f"  k = c_sigma sqrt(|cot|/2) = {float(kk):.14f},  k^2 = "
      f"{float(kk ** 2):.14f}")
check(abs(kk ** 2 - mpf(1) / 2) < TOL, "k^2 != 1/2")

print()
print("=== (iv) closing the loop against the measured asymptotics ===")
# The value derived here must be the one steps 18-19 measured.
lobv = clsin(2, 2 * (5 * pi / 6)) / 2
VCOEFF = -(2 / pi) * lobv


def log_prods(N):
    out, acc = [mpf(0)], mpf(0)
    for k in range(1, N):
        acc += 2 * log(2 * sin(mpf(k) * pi / N))
        out.append(acc)
    return out


print(f"{'N':>7} {'<4_1>_N/(N^1.5 e^{NV})':>24} {'c_sigma(5pi/6)':>17} "
      f"{'gap':>12}")
gaps = []
for N in (961, 3841, 15361):
    lp = log_prods(N)
    ks = 5 * N // 6
    tot = sum(exp(lp[k] - lp[ks]) for k in range(N))   # <4_1>_N / g_{k*}
    val = tot * exp(lp[ks] - mpf(N) * VCOEFF) / mpf(N) ** mpf('1.5')
    gaps.append((N, abs(val - cs)))
    print(f"{N:7d} {float(val):24.14f} {float(cs):17.14f} "
          f"{float(abs(val - cs)):12.4e}")
check(all(gaps[i + 1][1] < gaps[i][1] for i in range(len(gaps) - 1)),
      f"the measured asymptotic constant is not converging to c_sigma(5pi/6): "
      f"{[float(g[1]) for g in gaps]}")
check(gaps[-1][1] < mpf('1e-4'),
      f"the measured constant is {float(gaps[-1][1])} from c_sigma(5pi/6) at "
      f"N={gaps[-1][0]} -- the derived value and the measured one would not "
      f"agree")
print("  the DERIVED c_sigma and the MEASURED asymptotic constant agree.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
