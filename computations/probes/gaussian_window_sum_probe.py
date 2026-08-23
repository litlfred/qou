#!/usr/bin/env python3
"""The tilted Gaussian over a finite window, and the index bridge — step 14.

Checks `QOU/MathlibExt/GaussianWindowSum.lean`:

  sum_Icc_tilted_eq        sum_{|n|<=W} e^{-an^2+2Ln}
                             = e^{L^2/a} sum_{|n|<=W} e^{-a(n - L/a)^2}
  abs_sum_Icc_tilted_sub_le
      | sum_{|n|<=W} e^{-an^2+2Ln}  -  e^{L^2/a} sqrt(pi/a) |
        <= e^{L^2/a} ( sqrt(pi/a) * (theta error) + (tail beyond W) )

and `QOU/Knot/KashaevWindowIndex.lean`:

  sum_Icc_shift_int        sum_{j in [k-W, k+W]} F j
                             = sum_{n in [-W, W]} F((k + n).toNat)

Part (iv) exercises the bridge's hypothesis `W <= k`.  Without it BOTH sides
degrade silently -- Nat subtraction truncates `k - W` to 0 and `Int.toNat`
clamps -- so the two sides stop agreeing while neither errors.  The probe
exhibits a concrete disagreement, so the hypothesis is visibly load-bearing.

Run:  python3 computations/probes/gaussian_window_sum_probe.py
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


def window_tilted(a, L, W):
    return sum(exp(-a * mpf(n) ** 2 + 2 * L * mpf(n)) for n in range(-W, W + 1))


def window_shifted(a, c, W):
    return sum(exp(-a * (mpf(n) - c) ** 2) for n in range(-W, W + 1))


def theta_err(a):
    q = exp(-pi ** 2 / a)
    return 2 * q / (1 - q)


def tail_err(a, c, W):
    sigma = exp(-a / 4)
    return (exp(a * c ** 2) * exp(-a * (mpf(W) + 1) ** 2 / 4)
            * (1 + 2 * sigma / (1 - sigma)))


print("=== (i) the window sum, refactored through the shift ===")
for a in (mpf('1.2'), mpf('0.4')):
    for L in (mpf(0), mpf('0.7'), mpf('-1.5')):
        for W in (0, 3, 12):
            lhs = window_tilted(a, L, W)
            rhs = exp(L ** 2 / a) * window_shifted(a, L / a, W)
            check(abs(lhs - rhs) <= abs(lhs) * mpf('1e-40'),
                  f"shift refactor fails at a={a}, L={L}, W={W}")
print("  18 (a, L, W) combinations: ok")

print()
print("=== (ii) the window sum against the closed form ===")
print(f"{'a':>7} {'L':>7} {'W':>4} {'|window - closed|':>19} {'bound':>16} "
      f"{'ok':>4}")
for a in (mpf('1.2'), mpf('0.4')):
    for L in (mpf(0), mpf('-1.5')):
        for W in (2, 6, 15):
            lhs = abs(window_tilted(a, L, W) - exp(L ** 2 / a) * sqrt(pi / a))
            b = exp(L ** 2 / a) * (sqrt(pi / a) * theta_err(a)
                                   + tail_err(a, L / a, W))
            ok = lhs <= b + TOL
            print(f"{float(a):7.2f} {float(L):7.2f} {W:4d} {float(lhs):19.6e} "
                  f"{float(b):16.6e} {'ok' if ok else 'FAIL':>4}")
            check(ok, f"window bound violated at a={a}, L={L}, W={W}")

print()
print("=== (iii) which error dominates, at the Kashaev parameters ===")
# The two errors are of different kinds and the Lean statement keeps them
# apart.  Numerically, at these parameters one of them is not merely smaller
# but utterly absent -- worth saying, so nobody spends effort sharpening it.
# Printed as log10, not as the value: `float()` underflows below 1e-308 and
# would render the theta error as a flat 0.0000e+00 -- the same lie the
# window-sum probe's raw column told before it was normalised.  mpmath's
# comparison is exact either way.
print(f"{'N':>8} {'W=N^0.6':>9} {'log10 theta':>13} {'log10 tail':>12} "
      f"{'decades apart':>14}")
for N in (10 ** 4, 10 ** 5, 10 ** 6):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    a = pi * abs(cos(th) / sin(th)) / mpf(N)
    L = log(2 * sin(th))
    W = int(mpf(N) ** mpf('0.6'))
    te = sqrt(pi / a) * theta_err(a)
    ta = tail_err(a, L / a, W)
    lte, lta = log(te) / log(10), log(ta) / log(10)
    print(f"{N:8d} {W:9d} {float(lte):13.1f} {float(lta):12.1f} "
          f"{float(lta - lte):14.1f}")
    check(te < ta,
          f"at N={N} the theta error ({te}) was expected to be far BELOW the "
          f"tail ({ta}); if it is not, the balance described here is wrong")
print("  the sum-vs-integral error is astronomically below the tail here;")
print("  keeping them separate is about the STATEMENT, not about the numbers.")

print()
print("=== (iv) the bridge, and why `W <= k` is load-bearing ===")


def bridge_lhs(F, k, W):
    """sum over Nat Icc (k-W) (k+W), with Nat truncated subtraction."""
    lo = k - W if W <= k else 0
    return sum(F(j) for j in range(lo, k + W + 1))


def bridge_rhs(F, k, W):
    """sum over Int Icc (-W) W of F((k+n).toNat), with Int.toNat clamping."""
    return sum(F(max(0, k + n)) for n in range(-W, W + 1))


F = lambda j: mpf(1) / (mpf(j) + 7) ** 2      # anything injective enough
for k, W in ((100, 30), (50, 50), (7, 7)):
    check(abs(bridge_lhs(F, k, W) - bridge_rhs(F, k, W)) < TOL,
          f"the bridge fails at k={k}, W={W} even though W <= k")
print("  W <= k, three (k, W) pairs: both sides agree")
# now violate the hypothesis
bad = []
for k, W in ((3, 10), (0, 5), (2, 9)):
    lhs, rhs = bridge_lhs(F, k, W), bridge_rhs(F, k, W)
    if abs(lhs - rhs) > TOL:
        bad.append((k, W, float(lhs), float(rhs)))
check(len(bad) >= 1,
      "with W > k the two sides were expected to DISAGREE (Nat subtraction "
      "truncates, Int.toNat clamps); they did not, so the hypothesis W <= k "
      "would be decorative")
for k, W, l, r in bad:
    print(f"  W > k: k={k}, W={W} -> lhs={l:.6f}, rhs={r:.6f}  DISAGREE")
print("  so `W <= k` is load-bearing, and neither side errors without it.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
