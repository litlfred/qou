#!/usr/bin/env python3
"""The tilted Gaussian sum — bean `qou-fybg`, step 12.

Checks `QOU/MathlibExt/GaussianTiltedSum.lean`:

  exp_quadratic_eq              e^{-a u^2 + 2 L u} = e^{L^2/a} e^{-a(u - L/a)^2}
  abs_tsum_tilted_gaussian_sub_le
      | sum_{n in Z} e^{-a n^2 + 2 L n}  -  e^{L^2/a} sqrt(pi/a) |
        <= e^{L^2/a} sqrt(pi/a) * 2q/(1-q),   q = e^{-pi^2/a}
  sum_le_tsum_tilted_gaussian   any finite part <= the whole

Part (iv) is the payoff of the whole arc so far: instantiate `a` and `L` with
what step 10 actually produces at the Kashaev saddle,

    a = pi |cot th_k*| / N,     L = log(2 sin th_k*),   k* = floor(5N/6),

and the model sum divided by sqrt(N) should converge to `3^(-1/4)` -- i.e. to
`c_sigma`.  That is the number the whole formalisation is aimed at, computed
here from the Lean statements' own ingredients rather than from the closed
form.

Run:  python3 computations/probes/gaussian_tilted_sum_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, exp
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


def tilted_sum(a, L, halfwidth=None):
    """sum_{n in Z} exp(-a n^2 + 2 L n), truncated well below working precision."""
    if halfwidth is None:
        halfwidth = int(sqrt(mpf(120) * log(10) / a)) + int(abs(2 * L / a)) + 20
    c = int(L / a)
    return sum(exp(-a * mpf(n) ** 2 + 2 * L * mpf(n))
               for n in range(c - halfwidth, c + halfwidth + 1))


def rel_bound(a):
    q = exp(-pi ** 2 / a)
    return 2 * q / (1 - q)


print("=== (i) completing the square ===")
for a in (mpf('0.3'), mpf('1'), mpf('2.5')):
    for L in (mpf('-1.7'), mpf(0), mpf('0.4')):
        for u in (mpf('-3'), mpf('0.25'), mpf('7')):
            lhs = exp(-a * u ** 2 + 2 * L * u)
            rhs = exp(L ** 2 / a) * exp(-a * (u - L / a) ** 2)
            check(abs(lhs - rhs) <= abs(lhs) * mpf('1e-40'),
                  f"completing the square fails at a={a}, L={L}, u={u}")
print("  27 (a, L, u) combinations: ok")

print()
print("=== (ii) the tilted sum against its tilted integral ===")
print(f"{'a':>8} {'L':>8} {'sum':>20} {'e^(L^2/a)sqrt(pi/a)':>21} {'rel gap':>12} "
      f"{'bound':>12} {'ok':>4}")
for a in (mpf('1.5'), mpf('0.6'), mpf('0.2')):
    for L in (mpf(0), mpf('0.5'), mpf('-2')):
        S = tilted_sum(a, L)
        I = exp(L ** 2 / a) * sqrt(pi / a)
        rel = abs(S - I) / I
        b = rel_bound(a)
        ok = rel <= b + TOL
        print(f"{float(a):8.3f} {float(L):8.3f} {float(S):20.12f} "
              f"{float(I):21.12f} {float(rel):12.4e} {float(b):12.4e} "
              f"{'ok' if ok else 'FAIL':>4}")
        check(ok, f"tilted bound violated at a={a}, L={L}: {rel} > {b}")

print()
print("=== (iii) the tilt is a SHIFT: the sum peaks at n ~ L/a ===")
for a, L in ((mpf('0.4'), mpf('3')), (mpf('0.4'), mpf('-2.2'))):
    best = max(range(-40, 41), key=lambda n: -a * mpf(n) ** 2 + 2 * L * mpf(n))
    predicted = L / a
    check(abs(mpf(best) - predicted) <= mpf('0.5') + TOL,
          f"the peak of the tilted sum is at n={best}, not near L/a="
          f"{float(predicted)}")
    print(f"  a={float(a):.2f}, L={float(L):5.2f}: peak at n={best:3d}, "
          f"L/a = {float(predicted):6.2f}")

print()
print("=== (iv) THE PAYOFF: the model sum / sqrt(N) -> 3^(-1/4) ===")
# a and L exactly as step 10 produces them at the Kashaev saddle.
print(f"{'N':>7} {'a':>11} {'L':>11} {'L^2/a':>10} {'model/sqrt(N)':>15} "
      f"{'gap to 3^-1/4':>15}")
target = mpf(3) ** mpf('-0.25')
gaps = []
for N in (241, 961, 3841, 15361, 61441):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    a = pi * abs(cos(th) / sin(th)) / mpf(N)
    L = log(2 * sin(th))
    model = exp(L ** 2 / a) * sqrt(pi / a)
    val = model / sqrt(mpf(N))
    gap = abs(val - target)
    gaps.append((N, gap))
    print(f"{N:7d} {float(a):11.7f} {float(L):11.7f} {float(L**2/a):10.6f} "
          f"{float(val):15.10f} {float(gap):15.3e}")
    check(abs(tilted_sum(a, L) / (exp(L ** 2 / a) * sqrt(pi / a)) - 1)
          <= rel_bound(a) + TOL,
          f"the Lean bound fails at the Kashaev instantiation, N={N}")
check(all(gaps[i + 1][1] < gaps[i][1] for i in range(len(gaps) - 1)),
      f"model/sqrt(N) is not converging to 3^(-1/4): gaps "
      f"{[float(g[1]) for g in gaps]}")
check(gaps[-1][1] < mpf('1e-4'),
      f"model/sqrt(N) is {float(gaps[-1][1])} away from 3^(-1/4) at "
      f"N={gaps[-1][0]}; c_sigma would not be 3^(-1/4)")
print(f"  3^(-1/4) = {float(target):.10f};  gap at N={gaps[-1][0]} is "
      f"{float(gaps[-1][1]):.3e}")
print(f"  gap x N: {[round(float(g * n), 4) for n, g in gaps]}  -- O(1/N)")

print()
print("=== (v) the theta correction is beyond irrelevant here ===")
for N in (241, 961, 3841):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    a = pi * abs(cos(th) / sin(th)) / mpf(N)
    print(f"  N={N:6d}: a = {float(a):.7f},  2q/(1-q) = {float(rel_bound(a)):.3e}")
    check(rel_bound(a) < mpf('1e-20'),
          f"the theta correction is not negligible at N={N}")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
