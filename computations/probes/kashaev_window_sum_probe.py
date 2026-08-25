#!/usr/bin/env python3
"""Pointwise Gaussian -> Gaussian sum — bean `qou-fybg`, step 11.

Checks `QOU/Knot/KashaevWindowSum.lean`:

  kashaevProd_eq_mul_exp          g_k' = g_k exp(log g_k' - log g_k)
  kashaevProd_bounds_of_log_bound g_k e^{T-B} <= g_k' <= g_k e^{T+B}
  sum_kashaevProd_le_of_log_bound sum_s g_k' <= g_k e^B sum_s e^{T}
  le_sum_kashaevProd_of_log_bound g_k e^{-B} sum_s e^{T} <= sum_s g_k'
  sum_kashaevProd_window_sandwich |sum_s g_k' - g_k sum_s e^T|
                                    <= g_k (e^B - 1) sum_s e^T

with `T` and `B` abstract.  Here they are instantiated with step 10's tilted
Gaussian, which is the intended use:

    T(k') = 2u log(2 sin th_k) + (pi u^2/N) cot th_k,   u = k' - k
    B     = sup over the window of step 10's bound

Part (iv) is the one that matters for `c_sigma`: the sandwich is useful only if
`e^B - 1 -> 0`, i.e. only if the window's error budget shrinks.  It does, at
the `1/sqrt(N)` rate step 10 established -- so the model sum and the true sum
agree to a factor `1 + O(1/sqrt N)`.

Part (v) checks the claim in the file's docstring that no sign hypothesis on
`B` is needed, by exercising the algebraic step it rests on
(`e^B + e^{-B} >= 2`) at negative `B` as well.

Run:  python3 computations/probes/kashaev_window_sum_probe.py
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
TOL = mpf(10) ** (-25)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def theta(N, k):
    return mpf(k) * pi / N


def log_prod(N, k):
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def prod(N, k):
    return exp(log_prod(N, k))


def err_term(N, k):
    th = theta(N, k)
    return 2 * (1 / (144 * mpf(k) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                + (pi / N) ** 2 / (12 * sin(th) ** 2))


def sup_over(N, k, k2, f, samples=200):
    a, b = sorted((theta(N, k), theta(N, k2)))
    if a == b:
        return f(a)
    return max(f(a + (b - a) * mpf(i) / samples) for i in range(samples + 1))


def T_of(N, k, kp):
    """step 10's target: tilt + quadratic."""
    th = theta(N, k)
    u = mpf(kp) - mpf(k)
    return (2 * u * log(2 * sin(th))
            + (pi * u ** 2 / mpf(N)) * (cos(th) / sin(th)))


def B_of(N, k, kp):
    """step 10's bound for this pair."""
    u = abs(mpf(kp) - mpf(k))
    M = sup_over(N, k, kp, lambda x: 1 / sin(x) ** 2)
    K = sup_over(N, k, kp, lambda x: abs(cos(x) / sin(x)))
    return (err_term(N, k) + err_term(N, kp)
            + M * pi ** 2 * u ** 3 / (3 * mpf(N) ** 2)
            + K * pi * u / mpf(N)
            + M * pi ** 2 * u / (6 * mpf(N) ** 2))


print("=== (i) g_k' = g_k exp(log g_k' - log g_k) ===")
for N in (60, 240):
    for k, kp in ((5 * N // 6, 5 * N // 6 + 7), (10, 40), (1, N - 1)):
        lhs = prod(N, kp)
        rhs = prod(N, k) * exp(log_prod(N, kp) - log_prod(N, k))
        check(abs(lhs - rhs) <= abs(lhs) * mpf('1e-30') + TOL,
              f"exp identity fails at N={N}, k={k}, k'={kp}")
print("  N in {60, 240}, three index pairs each: ok")

print()
print("=== (ii) the exponentiated ratio brackets g_k' ===")
print(f"{'N':>6} {'u':>5} {'g_k e^(T-B)':>14} {'g_kp':>14} {'g_k e^(T+B)':>14} "
      f"{'ok':>4}")
for N in (240, 960):
    k = 5 * N // 6
    for u in (-15, -5, 5, 15):
        kp = k + u
        if not (1 <= kp < N):
            continue
        T, B = T_of(N, k, kp), B_of(N, k, kp)
        lo = prod(N, k) * exp(T - B)
        hi = prod(N, k) * exp(T + B)
        val = prod(N, kp)
        ok = lo <= val * (1 + TOL) and val <= hi * (1 + TOL)
        print(f"{N:6d} {u:5d} {float(lo):14.6e} {float(val):14.6e} "
              f"{float(hi):14.6e} {'ok' if ok else 'FAIL':>4}")
        check(ok, f"bracket fails at N={N}, u={u}")

print()
print("=== (iii) the window sum, both directions ===")
# Everything is divided by g_k.  Not cosmetic: g_k is about e^{0.323 N}, so at
# N = 3840 the raw numbers are ~1e539 and `float()` prints `inf` -- a column of
# `inf  inf  inf   ok` reads as a passing check while showing nothing.  mpmath
# itself is fine (arbitrary exponent range), so the comparison was always
# genuine; it is the display that had to change.
print(f"{'N':>6} {'W':>4} {'e^-B S':>15} {'sum g_kp/g_k':>15} {'e^B S':>15} "
      f"{'ok':>4}")
for N in (240, 960, 3840):
    k = 5 * N // 6
    W = int(sqrt(mpf(N)))
    window = [kp for kp in range(k - W, k + W + 1) if 1 <= kp < N]
    B = max(B_of(N, k, kp) for kp in window)
    S = sum(exp(T_of(N, k, kp)) for kp in window)
    ratio = sum(exp(log_prod(N, kp) - log_prod(N, k)) for kp in window)
    lo = exp(-B) * S
    hi = exp(B) * S
    ok = lo <= ratio * (1 + TOL) and ratio <= hi * (1 + TOL)
    print(f"{N:6d} {W:4d} {float(lo):15.6e} {float(ratio):15.6e} "
          f"{float(hi):15.6e} {'ok' if ok else 'FAIL':>4}")
    check(ok, f"window sum bounds fail at N={N}")

print()
print("=== (iv) the sandwich is USEFUL: e^B - 1 -> 0 ===")
# The sandwich says the true window sum and the model sum g_k * S agree to a
# relative factor e^B - 1.  If that did not go to 0 the whole construction
# would be vacuous.
print(f"{'N':>6} {'W':>4} {'B':>10} {'e^B - 1':>10} {'true/model - 1':>16} "
      f"{'x sqrt(N)':>10}")
rows = []
for N in (240, 960, 3840, 15360):
    k = 5 * N // 6
    W = int(sqrt(mpf(N)))
    window = [kp for kp in range(k - W, k + W + 1) if 1 <= kp < N]
    B = max(B_of(N, k, kp) for kp in window)
    S = sum(exp(T_of(N, k, kp)) for kp in window)
    true = sum(prod(N, kp) for kp in window)
    model = prod(N, k) * S
    rel = abs(true / model - 1)
    rows.append((N, B, rel))
    print(f"{N:6d} {W:4d} {float(B):10.5f} {float(exp(B) - 1):10.5f} "
          f"{float(rel):16.8f} {float(rel * sqrt(mpf(N))):10.5f}")
    check(rel <= exp(B) - 1 + TOL,
          f"the sandwich is violated at N={N}: relative gap {rel} exceeds "
          f"e^B - 1 = {exp(B) - 1}")
check(all(rows[i + 1][1] < rows[i][1] for i in range(len(rows) - 1)),
      f"B is not decreasing: {[float(r[1]) for r in rows]} -- the sandwich "
      f"would never tighten")
check(rows[-1][1] < mpf('0.35'),
      f"B is still {float(rows[-1][1])} at N={rows[-1][0]}; the model and the "
      f"true sum would not be within a small factor")
print(f"  B -> {float(rows[-1][1]):.5f} at N={rows[-1][0]}: model and true sum "
      f"agree to a factor 1 + O(1/sqrt N)")

print()
print("=== (v) no sign hypothesis on B is needed: e^B + e^-B >= 2 always ===")
for b in (mpf('-5'), mpf('-1'), mpf('-0.001'), mpf(0), mpf('0.001'), mpf(3)):
    check(exp(b) + exp(-b) >= 2 - TOL,
          f"e^B + e^-B >= 2 fails at B={b}")
print("  checked at B = -5, -1, -0.001, 0, 0.001, 3 -- holds at negative B too,")
print("  which is why `sum_kashaevProd_window_sandwich` carries no `0 <= B`.")
print("  (a negative B forces the window empty, since it would bound an")
print("   absolute value below zero; then both sides of the sandwich are 0.)")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
