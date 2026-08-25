#!/usr/bin/env python3
"""log <4_1>_N absolutely — bean `qou-fybg`, step 7.

Checks `QOU/Knot/KashaevLogAsymptotic.lean`:

  argmax_angle_eq       th_{k*} = 5pi/6 - r pi/(6N),  r = 5N mod 6
  argmax_offset_le      |th_{k*} - 5pi/6| <= pi/N
  argmax_angle_mem      th_{k*} in [pi/6, 5pi/6]
  log_kashaevProd_argmax    the peak value with M = 4 substituted
  le_log_kashaev        log g* + log m - 1        <= log <4_1>_N
  log_kashaev_le        log <4_1>_N <= log g* + log C(N,w)

and, past what Lean states so far, what the bracket DELIVERS: the width of the
sandwich on `log <4_1>_N - N Vol/(2 pi)`, against the expected `(3/2) log N`.

The hypotheses of the last two are Nat-arithmetic side conditions, and a
statement whose hypotheses are never satisfiable is worthless.  Part (v)
therefore exhibits admissible `m` and `w` for a range of `N` and checks each
side condition explicitly rather than assuming they can be met.

Run:  python3 computations/probes/kashaev_log_asymptotic_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, exp, clsin, floor
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
    return clsin(2, 2 * th) / 2


def log_prod(N, k):
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def kashaev(N):
    """<4_1>_N = sum_{k<N} kashaevProd(N,k)."""
    tot = mpf(0)
    acc = mpf(1)          # kashaevProd(N,0) = empty product = 1
    tot += acc
    for k in range(1, N):
        acc *= (2 * sin(mpf(k) * pi / N)) ** 2
        tot += acc
    return tot


VOL = 4 * lob(pi / 6)                      # Vol(4_1)
V = -(2 / pi) * lob(5 * pi / 6)            # = Vol / (2 pi)

print("=== (i) the saddle angle: th_{k*} = 5pi/6 - r pi/(6N) ===")
print(f"{'N':>6} {'r=5N%6':>7} {'th_{k*}':>12} {'5pi/6 - r pi/6N':>17} "
      f"{'offset/(pi/N)':>14}")
for N in (6, 7, 11, 13, 25, 61, 240, 961):
    k = 5 * N // 6
    r = (5 * N) % 6
    th = mpf(k) * pi / N
    pred = 5 * pi / 6 - mpf(r) * pi / (6 * N)
    check(abs(th - pred) < mpf('1e-35'),
          f"argmax_angle_eq fails at N={N}: {th} != {pred}")
    off = abs(th - 5 * pi / 6)
    check(off <= pi / N + TOL, f"argmax_offset_le fails at N={N}")
    if N >= 6:
        check(pi / 6 - TOL <= th <= 5 * pi / 6 + TOL,
              f"argmax_angle_mem fails at N={N}: th={th}")
    print(f"{N:6d} {r:7d} {float(th):12.8f} {float(pred):17.8f} "
          f"{float(off / (pi / N)):14.4f}")
print("  offset/(pi/N) <= 5/6 always -- the floor undershoots, never overshoots")

print()
print("=== (ii) M = 4 is the sharp constant on [pi/6, 5pi/6] ===")
worst = max((1 / sin(pi / 6 + (5 * pi / 6 - pi / 6) * mpf(i) / 2000) ** 2, i)
            for i in range(2001))
print(f"  max of 1/sin^2 over 2001 samples of [pi/6, 5pi/6] = "
      f"{float(worst[0]):.10f}  (attained at the endpoints, where sin = 1/2)")
check(worst[0] <= 4 + mpf('1e-20'),
      f"1/sin^2 exceeds 4 on [pi/6, 5pi/6]: got {worst[0]}")
check(worst[0] > 4 - mpf('1e-6'),
      "M = 4 is not attained, so it is not the sharp constant the file claims")

print()
print("=== (iii) the peak value with M = 4 ===")
print(f"{'N':>6} {'|log g* - main|':>16} {'bound':>14} {'slack x':>9} {'ok':>4}")
for N in (6, 12, 13, 25, 60, 61, 120, 240, 241, 480):
    k = 5 * N // 6
    th = mpf(k) * pi / N
    main = (-(2 * mpf(N) / pi) * lob(5 * pi / 6)
            + log(2 * mpf(N) * sin(th))
            + (pi / (6 * mpf(N))) * (cos(th) / sin(th)))
    bound = (2 * (1 / (144 * mpf(k) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                  + (pi / N) ** 2 / (12 * sin(th) ** 2))
             + (2 * mpf(N) / pi) * (sqrt(3) * (pi / N) ** 2 / 2
                                    + 4 * (pi / N) ** 3 / 6))
    actual = abs(log_prod(N, k) - main)
    ok = actual <= bound + TOL
    print(f"{N:6d} {float(actual):16.6e} {float(bound):14.6e} "
          f"{float(bound / actual) if actual > 0 else float('inf'):9.2f} "
          f"{'ok' if ok else 'FAIL':>4}")
    check(ok, f"log_kashaevProd_argmax fails at N={N}: {actual} > {bound}")

print()
print("=== (iv) N^2 <= g_{k*}: the peak really is large ===")
for N in (6, 12, 60, 240):
    k = 5 * N // 6
    g = exp(log_prod(N, k))
    check(mpf(N) ** 2 <= g * (1 + TOL),
          f"sq_le_kashaevProd_argmax fails at N={N}: {N**2} > {g}")
print("  N in {6, 12, 60, 240}: ok")


def admissible_m(N):
    """Largest m with 1 <= m, m <= 5N/6, sqrt3 pi m^2 <= N."""
    m = int(floor(sqrt(mpf(N) / (sqrt(3) * pi))))
    while m >= 1 and sqrt(3) * pi * mpf(m) ** 2 > N:
        m -= 1
    return m if m >= 1 and m <= 5 * N // 6 else None


def admissible_w(N):
    """Smallest w with 2N+3 <= 3w, then check 6w <= 5N, w <= 5N/6, 2 <= 5N/6-w."""
    w = -(-(2 * N + 3) // 3)          # ceil((2N+3)/3)
    if 6 * w <= 5 * N and w <= 5 * N // 6 and 5 * N // 6 - w >= 2:
        return w
    return None


def upper_const(N, w):
    D = mpf(5 * N // 6 - w)
    return (mpf(w) / mpf(N) ** 2
            + mpf(w) * (sqrt(3) * mpf(N)) / (pi * D * (D - 1))
            + (2 + sqrt(sqrt(3) * mpf(N)) / 2)
            + (2 + sqrt(mpf(N) / sqrt(3)) / 2))


print()
print("=== (v-a) where the upper bound's hypotheses first become satisfiable ===")
# hw2 (2N+3 <= 3w) and hD (2 <= 5N/6 - w) pull against each other: the window
# boundary must be far enough right for the secant bound AND far enough left to
# leave two steps of gap.  Below some N there is no w at all.  This is a real
# restriction of `log_kashaev_le`, not a probe artefact -- record it.
first = min(N for N in range(6, 60) if admissible_w(N) is not None)
print(f"  smallest N with an admissible w: {first}")
for N in range(6, first):
    check(admissible_w(N) is None,
          f"admissible_w should be empty below N={first} but found one at {N}")
print(f"  N in [6, {first}) : none (e.g. N=12 needs w >= 9 but w <= 8)")
check(first == 18,
      f"the upper bound was expected to become usable at N=18; got {first}. "
      f"If this moved, `log_kashaev_le`'s hypotheses changed.")

print()
print("=== (v-b) the sandwich holds wherever the hypotheses are met ===")
print(f"{'N':>6} {'m':>5} {'w':>6} {'lower':>13} {'log<4_1>':>13} "
      f"{'upper':>13} {'width':>8} {'ok':>4}")
rows = []
for N in (18, 24, 48, 96, 192, 384, 768):
    m, w = admissible_m(N), admissible_w(N)
    if m is None or w is None:
        print(f"{N:6d}  -- no admissible m/w --")
        check(False, f"no admissible (m, w) at N={N}: m={m}, w={w}")
        continue
    # every Lean side condition, checked explicitly
    check(1 <= m <= 5 * N // 6, f"m out of range at N={N}")
    check(sqrt(3) * pi * mpf(m) ** 2 <= N, f"hsq fails at N={N}, m={m}")
    check(6 * w <= 5 * N, f"hw1 fails at N={N}, w={w}")
    check(2 * N + 3 <= 3 * w, f"hw2 fails at N={N}, w={w}")
    check(w <= 5 * N // 6, f"hwk fails at N={N}, w={w}")
    check(2 <= 5 * N // 6 - w, f"hD fails at N={N}, w={w}")

    lg = log_prod(N, 5 * N // 6)
    lower = lg + log(mpf(m)) - 1
    upper = lg + log(upper_const(N, w))
    truth = log(kashaev(N))
    ok = lower <= truth + TOL and truth <= upper + TOL
    print(f"{N:6d} {m:5d} {w:6d} {float(lower):13.6f} {float(truth):13.6f} "
          f"{float(upper):13.6f} {float(upper - lower):8.4f} "
          f"{'ok' if ok else 'FAIL':>4}")
    check(ok, f"sandwich violated at N={N}: {lower} <= {truth} <= {upper}")
    rows.append((N, lower, truth, upper))

print()
print("=== (vi) what the bracket delivers on log<4_1>_N - N Vol/(2 pi) ===")
print(f"{'N':>6} {'truth-NV':>12} {'(3/2)logN':>11} {'lower-NV':>11} "
      f"{'upper-NV':>11} {'width':>8}")
for N, lower, truth, upper in rows:
    nv = mpf(N) * V
    print(f"{N:6d} {float(truth - nv):12.5f} {float(mpf(3) / 2 * log(N)):11.5f} "
          f"{float(lower - nv):11.5f} {float(upper - nv):11.5f} "
          f"{float(upper - lower):8.4f}")
# the residual should track (3/2) log N with a bounded gap, and the sandwich
# width should stay bounded (it is log of a ratio of two O(sqrt N) constants)
res = [(truth - mpf(N) * V) - mpf(3) / 2 * log(N) for N, _, truth, _ in rows]
print(f"  residual - (3/2)logN : {[round(float(x), 4) for x in res]}")
check(max(res[1:]) - min(res[1:]) < mpf('0.05'),
      f"log<4_1>_N - N Vol/(2pi) - (3/2)log N is not settling to a constant: "
      f"spread {float(max(res[1:]) - min(res[1:]))}")
# THE TARGET.  That constant should be log c_sigma = log 3^(-1/4) = -(1/4)log 3.
target = -log(mpf(3)) / 4
print(f"  -> {float(res[-1]):.6f} at N={rows[-1][0]},  "
      f"target log(3^(-1/4)) = {float(target):.6f},  "
      f"gap = {float(abs(res[-1] - target)):.6f}")
check(abs(res[-1] - target) < mpf('0.002'),
      f"the residual is not converging to log(3^(-1/4)): got {float(res[-1])} "
      f"vs {float(target)}. This is the whole target of the arc -- if it does "
      f"not hold, c_sigma = 3^(-1/4) is wrong or the main term is misassembled.")
# and it should still be APPROACHING it, not sitting at a different constant
check(abs(res[-1] - target) < abs(res[1] - target),
      "the residual is moving away from log(3^(-1/4)) as N grows")
widths = [upper - lower for _, lower, _, upper in rows]
check(max(widths) < 10,
      f"the sandwich width is not bounded: {[float(x) for x in widths]}")
print(f"  sandwich width       : {[round(float(x), 3) for x in widths]}  "
      f"(bounded -- both constants are Theta(sqrt N), so the log of their "
      f"ratio is O(1))")
print(f"  c_sigma = exp(residual) would be in "
      f"[{float(exp(rows[-1][1] - mpf(rows[-1][0]) * V - mpf(3) / 2 * log(rows[-1][0]))):.4f}, "
      f"{float(exp(rows[-1][3] - mpf(rows[-1][0]) * V - mpf(3) / 2 * log(rows[-1][0]))):.4f}]"
      f"   (target 3^(-1/4) = {float(mpf(3) ** mpf('-0.25')):.6f})")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
