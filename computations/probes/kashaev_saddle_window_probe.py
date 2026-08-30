#!/usr/bin/env python3
"""The assembly specialised at the saddle — bean `qou-fybg`, step 16.

Checks `QOU/Knot/KashaevSaddleWindow.lean`:

  kashaevGaussCoeff_pos     a = -pi cot(th_k)/N > 0 when th_k in (pi/2, pi)
  angle_mem_window          every window index's angle is in the window's range
  abs_sum_kashaevProd_saddle_window_le

The point of this probe is NOT the bound -- step 15's probe already exercised
it -- but the HYPOTHESES.  A specialisation whose hypotheses cannot be met is
worthless, and several of them are Nat-arithmetic conditions that interact:

    hW    : W <= k            hk1  : 1 <= k - W
    hkWN  : k + W < N         hlo  : pi/2 < th_k       hhi : th_k < pi

With `k = floor(5N/6)` and `W = floor(N^0.6)`, `hkWN` is the binding one:
`N^0.6 < N/6` needs `N^0.4 > 6`, i.e. `N > 6^2.5 = 88.2`.  Part (i) finds the
exact threshold rather than assuming it.

Run:  python3 computations/probes/kashaev_saddle_window_probe.py
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
TOL = mpf(10) ** (-30)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def theta(N, k):
    return mpf(k) * pi / N


def log_prod(N, k):
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def err_term(N, k):
    th = theta(N, k)
    return 2 * (1 / (144 * mpf(k) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                + (pi / N) ** 2 / (12 * sin(th) ** 2))


def hyps_hold(N, p=mpf('0.6')):
    """Every side condition of abs_sum_kashaevProd_saddle_window_le."""
    k = 5 * N // 6
    W = int(mpf(N) ** p)
    if not (4 <= N):
        return None
    if not (k < N and W <= k and 1 <= k - W and k + W < N):
        return None
    th = theta(N, k)
    if not (pi / 2 < th < pi):
        return None
    return k, W


print("=== (i) where the hypotheses first all hold (W = N^0.6) ===")
first = None
for N in range(4, 400):
    if hyps_hold(N) is not None:
        first = N
        break
print(f"  smallest N with every side condition satisfied: {first}")
for N in range(4, first):
    check(hyps_hold(N) is None,
          f"the side conditions were expected to FAIL below N={first}, but "
          f"they hold at N={N}")
check(first is not None and first <= 120,
      f"the hypotheses should become satisfiable by N=120; got {first}")
# the binding condition is k + W < N, i.e. N^0.4 > 6
k, W = 5 * (first - 1) // 6, int(mpf(first - 1) ** mpf('0.6'))
check(k + W >= first - 1,
      f"at N={first-1} the expected obstruction was k + W >= N; it was "
      f"something else, so the analysis in this probe is wrong")
print(f"  at N={first-1}: k={k}, W={W}, k+W={k+W} >= N -- `hkWN` is the binding one")
print(f"  (N^0.4 > 6 needs N > 6^2.5 = {float(mpf(6) ** mpf('2.5')):.1f})")

print()
print("=== (ii) the Gaussian coefficient is positive and equals pi|cot|/N ===")
print(f"{'N':>7} {'k':>7} {'th_k':>10} {'a':>13} {'pi|cot|/N':>13}")
for N in (121, 241, 961, 3841):
    k, W = hyps_hold(N)
    th = theta(N, k)
    a = -(pi * (cos(th) / sin(th)) / mpf(N))
    alt = pi * abs(cos(th) / sin(th)) / mpf(N)
    print(f"{N:7d} {k:7d} {float(th):10.6f} {float(a):13.9f} {float(alt):13.9f}")
    check(a > 0, f"kashaevGaussCoeff is not positive at N={N}: {a}")
    check(abs(a - alt) < TOL,
          f"a != pi|cot|/N at N={N} -- the two files disagree on the "
          f"coefficient")
    check(pi / 2 < th < pi, f"th_k out of (pi/2, pi) at N={N}")

print()
print("=== (iii) M, K and B on the window, and the conclusion ===")
print(f"{'N':>7} {'W':>5} {'M':>9} {'K':>8} {'B':>9} {'|win/g - model|':>17} "
      f"{'bound/g':>13} {'ok':>4}")
for N in (241, 961, 3841):
    k, W = hyps_hold(N)
    lo, hi = theta(N, k - W), theta(N, k + W)
    grid = [lo + (hi - lo) * mpf(i) / 300 for i in range(301)]
    check(all(0 < x < pi for x in grid),
          f"the window's angular range leaves (0, pi) at N={N}")
    M = max(1 / sin(x) ** 2 for x in grid)
    K = max(abs(cos(x) / sin(x)) for x in grid)
    B = max(err_term(N, k) + err_term(N, kp)
            + M * pi ** 2 * abs(mpf(kp) - mpf(k)) ** 3 / (3 * mpf(N) ** 2)
            + K * pi * abs(mpf(kp) - mpf(k)) / mpf(N)
            + M * pi ** 2 * abs(mpf(kp) - mpf(k)) / (6 * mpf(N) ** 2)
            for kp in range(k - W, k + W + 1))
    th = theta(N, k)
    a = -(pi * (cos(th) / sin(th)) / mpf(N))
    L = log(2 * sin(th))
    q = exp(-pi ** 2 / a)
    sig = exp(-a / 4)
    E = exp(L ** 2 / a) * (sqrt(pi / a) * (2 * q / (1 - q))
                           + exp(a * (L / a) ** 2)
                           * exp(-a * (mpf(W) + 1) ** 2 / 4)
                           * (1 + 2 * sig / (1 - sig)))
    model = exp(L ** 2 / a) * sqrt(pi / a)
    ratio = sum(exp(log_prod(N, kp) - log_prod(N, k))
                for kp in range(k - W, k + W + 1))
    lhs = abs(ratio - model)
    bound = (exp(B) - 1) * (model + E) + E
    ok = lhs <= bound + TOL
    print(f"{N:7d} {W:5d} {float(M):9.4f} {float(K):8.4f} {float(B):9.4f} "
          f"{float(lhs):17.6e} {float(bound):13.6e} {'ok' if ok else 'FAIL':>4}")
    check(ok, f"the specialised conclusion fails at N={N}")

print()
print("=== (iv) M and K stay bounded as N grows -- the window does not run out ===")
# If M blew up with N the single-interval hypothesis form would be useless.
# The window's angular half-width is `pi W/N ~ pi N^-0.4`, so M -> 4 and
# K -> sqrt3 only at rate `N^-0.4`.  That is SLOW: M is still 5.13 at
# N = 15361.  Report the rate rather than asserting a threshold I guessed.
print(f"{'N':>7} {'M':>9} {'(M-4) N^0.4':>13} {'K':>8} {'(K-sqrt3) N^0.4':>16}")
Ms = []
for N in (241, 961, 3841, 15361, 61441):
    k, W = hyps_hold(N)
    lo, hi = theta(N, k - W), theta(N, k + W)
    grid = [lo + (hi - lo) * mpf(i) / 200 for i in range(201)]
    M = max(1 / sin(x) ** 2 for x in grid)
    K = max(abs(cos(x) / sin(x)) for x in grid)
    r = mpf(N) ** mpf('0.4')
    Ms.append((N, M, K))
    print(f"{N:7d} {float(M):9.4f} {float((M - 4) * r):13.4f} "
          f"{float(K):8.4f} {float((K - sqrt(3)) * r):16.4f}")
check(all(Ms[i + 1][1] < Ms[i][1] for i in range(len(Ms) - 1)),
      f"M is not decreasing towards 4: {[float(m[1]) for m in Ms]}")
check(all(Ms[i + 1][2] < Ms[i][2] for i in range(len(Ms) - 1)),
      f"K is not decreasing towards sqrt3: {[float(m[2]) for m in Ms]}")
check(Ms[-1][1] < mpf('4.7'),
      f"M should be under 4.7 by N={Ms[-1][0]}; it is {float(Ms[-1][1])}")
check(Ms[-1][2] < mpf('1.95'),
      f"K should be under 1.95 by N={Ms[-1][0]}; it is {float(Ms[-1][2])}")
# The limit of the scaled column is not a fitted number:
#   sin(5pi/6 + eps) = 1/2 - (sqrt3/2) eps + ...,  so  1/sin^2 = 4(1 + 2 sqrt3 eps),
#   and eps = pi W/N = pi N^-0.4, giving (M - 4) N^0.4 -> 8 sqrt3 pi.
limM = 8 * sqrt(3) * pi
check(Ms[-1][1] - 4 < limM * mpf('1.3') / (mpf(Ms[-1][0]) ** mpf('0.4')),
      f"(M-4) should be approaching {float(limM)} N^-0.4; at N={Ms[-1][0]} it "
      f"is {float((Ms[-1][1] - 4) * mpf(Ms[-1][0]) ** mpf('0.4'))}")
print(f"  M -> 4 and K -> sqrt3 as the window shrinks onto the saddle in angle,")
print(f"  so ONE pair of angular bounds serves every N past the threshold.")
print(f"  The approach is only N^-0.4: (M-4) N^0.4 -> 8 sqrt3 pi = "
      f"{float(limM):.2f} (observed {float((Ms[-1][1]-4) * mpf(Ms[-1][0]) ** mpf('0.4')):.2f}),")
print(f"  so M is still 5.13 at N = 15361 and 4.59 at N = 61441.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
