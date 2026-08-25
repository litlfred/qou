#!/usr/bin/env python3
"""The join: log(kashaevProd) asymptotics — bean `qou-fybg`, step 6.

Checks the two theorems in `QOU/Knot/KashaevPeakValue.lean`:

  (I)  log_kashaevProd_asymptotic

         |log g_k - (-(2N/pi) Lob(th_k) + log(2 N sin th_k)
                     + (pi/(6N)) cot th_k)|
           <= 2*(1/(144 k^2) + (7/12)(pi/N)^2 + (pi/N)^2/(12 sin^2 th_k))

       with th_k = k pi / N.  This is `kashaev_log_sum_asymptotic` doubled
       through `log g_k = 2 s_k`.

  (II) log_kashaevProd_saddle — the same with Lob(th_k) replaced by the exact
       saddle value Lob(5pi/6), paying

         (2N/pi) * (sqrt3 (pi/N)^2 / 2 + M (pi/N)^3 / 6)

       for the offset, where M dominates 1/sin^2 between th_k and 5pi/6.

The point of part (iii): that offset penalty is O(1/N), NOT O(1/N^2).  The
factor N in front of Lob amplifies the quadratic Taylor term back up.  If the
probe showed it decaying like 1/N^2 the Lean statement would be needlessly
weak; if it grew, the statement would be wrong.

Run:  python3 computations/probes/kashaev_peak_value_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, clsin
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


def lob(th):
    """Lobachevsky Lambda(th) = Cl_2(2 th) / 2."""
    return clsin(2, 2 * th) / 2


def log_prod(N, k):
    """log kashaevProd(N,k) = 2 sum_{j=1}^{k} log(2 sin(j pi / N))."""
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def main_term(N, k):
    th = mpf(k) * pi / N
    return (-(2 * mpf(N) / pi) * lob(th)
            + log(2 * mpf(N) * sin(th))
            + (pi / (6 * mpf(N))) * (cos(th) / sin(th)))


def err_bound(N, k):
    th = mpf(k) * pi / N
    return 2 * (1 / (144 * mpf(k) ** 2)
                + mpf(7) / 12 * (pi / N) ** 2
                + (pi / N) ** 2 / (12 * sin(th) ** 2))


print("=== (i) the join, at the saddle index k* = floor(5N/6) ===")
print(f"{'N':>6} {'k*':>6} {'|log g - main|':>16} {'bound':>14} "
      f"{'slack x':>9} {'ok':>4}")
for N in (12, 24, 60, 120, 240, 480, 960):
    k = 5 * N // 6
    actual = abs(log_prod(N, k) - main_term(N, k))
    bound = err_bound(N, k)
    ok = actual <= bound + TOL
    print(f"{N:6d} {k:6d} {float(actual):16.6e} {float(bound):14.6e} "
          f"{float(bound / actual) if actual > 0 else float('inf'):9.2f} "
          f"{'ok' if ok else 'FAIL':>4}")
    check(ok, f"(I) violated at N={N}, k={k}: {actual} > {bound}")

print()
print("=== (ii) the join, away from the saddle (k across the range) ===")
for N in (60, 240):
    for k in (1, 2, 5, N // 6, N // 3, N // 2, 2 * N // 3, 5 * N // 6, N - 1):
        if not (1 <= k < N):
            continue
        actual = abs(log_prod(N, k) - main_term(N, k))
        bound = err_bound(N, k)
        ok = actual <= bound + TOL
        check(ok, f"(I) violated at N={N}, k={k}: {actual} > {bound}")
    print(f"  N={N:4d}: all 9 sample indices ok")

print()
print("=== (iii) the saddle re-centring: O(1/N), and that is not slack ===")
# N NOT divisible by 6, so th_{k*} != 5pi/6 and the Taylor penalty is actually
# exercised.  (For 6 | N the offset is exactly 0 and this test is vacuous --
# see (iii-b).)
print(f"{'N':>6} {'offset |d|':>12} {'true cost':>13} {'penalty':>13} "
      f"{'penalty*N':>11} {'ok':>4}")
prev = None
for N in (13, 25, 61, 121, 241, 481, 961):
    k = 5 * N // 6
    th = mpf(k) * pi / N
    d = th - 5 * pi / 6
    check(abs(d) <= pi / N + TOL,
          f"the offset hypothesis |th_k - 5pi/6| <= pi/N fails at N={N}")
    # M dominating 1/sin^2 on the interval between th_k and 5pi/6
    lo, hi = min(th, 5 * pi / 6), max(th, 5 * pi / 6)
    M = max(1 / sin(lo + (hi - lo) * mpf(i) / 200) ** 2 for i in range(201))
    penalty = (2 * mpf(N) / pi) * (sqrt(3) * (pi / N) ** 2 / 2
                                   + M * (pi / N) ** 3 / 6)
    # what re-centring actually costs
    true_cost = (2 * mpf(N) / pi) * abs(lob(th) - lob(5 * pi / 6))
    actual = abs(log_prod(N, k) - (main_term(N, k)
                                   + (2 * mpf(N) / pi) * lob(th)
                                   - (2 * mpf(N) / pi) * lob(5 * pi / 6)))
    ok = actual <= err_bound(N, k) + penalty + TOL
    print(f"{N:6d} {float(abs(d)):12.6e} {float(true_cost):13.6e} "
          f"{float(penalty):13.6e} {float(penalty * N):11.4f} "
          f"{'ok' if ok else 'FAIL':>4}")
    check(ok, f"(II) violated at N={N}")
    check(true_cost <= penalty + TOL,
          f"the Taylor penalty does not cover the true re-centring cost at "
          f"N={N}: {true_cost} > {penalty}")
    prev = (N, penalty)

# penalty * N should approach a constant (sqrt3 * pi = 5.441), NOT decay
lastN, lastp = prev
check(float(lastp * lastN) > 5.0,
      f"the re-centring penalty is decaying faster than 1/N (penalty*N = "
      f"{float(lastp * lastN)}); the Lean statement's O(1/N) term would then "
      f"be needlessly weak")
check(float(lastp * lastN) < 6.0,
      f"the re-centring penalty is growing faster than 1/N (penalty*N = "
      f"{float(lastp * lastN)})")
print(f"  penalty*N -> {float(lastp * lastN):.4f}   "
      f"(sqrt3*pi = {float(sqrt(3) * pi):.4f}, plus the M(pi/N)^3 tail)")

print()
print("=== (iii-b) 6 | N: the offset is exactly 0, penalty is pure slack ===")
for N in (12, 60, 240, 960):
    k = 5 * N // 6
    th = mpf(k) * pi / N
    d = th - 5 * pi / 6
    check(abs(d) < mpf('1e-35'),
          f"for 6 | N the saddle index should hit 5pi/6 exactly; at N={N} the "
          f"offset is {d}")
    actual = abs(log_prod(N, k) - (main_term(N, k)
                                   + (2 * mpf(N) / pi) * lob(th)
                                   - (2 * mpf(N) / pi) * lob(5 * pi / 6)))
    check(actual <= err_bound(N, k) + TOL,
          f"(II) with zero offset should reduce to (I) at N={N}")
print("  N in {12, 60, 240, 960}: offset 0 to 35 digits, (II) collapses to (I)")

print()
print("=== (iv) sanity: the leading term is N*Vol(4_1)/(2 pi) ===")
# -(2N/pi) Lob(5pi/6) should be N * Vol(4_1) / (2 pi) with Vol = 4 Lob(pi/6)
vol = 4 * lob(pi / 6)
print(f"  4*Lob(pi/6)      = {float(vol):.12f}")
print(f"  -(2/pi)Lob(5pi/6)= {float(-(2 / pi) * lob(5 * pi / 6)):.12f}")
print(f"  Vol(4_1)/(2 pi)  = {float(vol / (2 * pi)):.12f}")
check(abs(vol - mpf('2.029883212819307250042405108549')) < mpf('1e-24'),
      f"4 Lob(pi/6) is not Vol(4_1): got {vol}")
check(abs(-(2 / pi) * lob(5 * pi / 6) - vol / (2 * pi)) < mpf('1e-30'),
      "the leading coefficient -(2/pi)Lob(5pi/6) does not equal Vol/(2 pi)")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
