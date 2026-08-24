#!/usr/bin/env python3
"""The largest Kashaev term sits at k = floor(5N/6) — bean `qou-fybg`.

Checks `QOU.Knot.FigureEightVolume.kashaevProd_le_argmax`
(`QOU/Knot/KashaevArgmax.lean`) numerically:

    kashaevProd(N, k) <= kashaevProd(N, floor(5N/6))   for all k < N, N >= 6

with kashaevProd(N, k) = prod_{j=1}^{k} (2 sin(j pi/N))^2, worked in log space.

Also checks the three structural facts the Lean proof rests on:

  * the ratio kashaevProd(N,k+1)/kashaevProd(N,k) is exactly (2 sin((k+1)pi/N))^2,
    so the sequence rises exactly while 2 sin > 1;
  * the shape is DOWN-UP-DOWN, not unimodal — there is a genuine local max at
    k = 0 with a dip after it, which is why the Lean proof splits off
    k <= floor(N/6) and routes it through kashaevProd(N,0) = 1;
  * ties happen: when 6 | N the increment at j = N/6 and j = 5N/6 is exactly 1,
    so `<=` is the sharp statement and `<` would be false.

Run:  python3 computations/probes/kashaev_argmax_probe.py
"""

from mpmath import mp, mpf, sin, log, pi
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


def log_prod(N, k):
    """log kashaevProd(N,k) = 2 sum_{j=1}^{k} log(2 sin(j pi / N))."""
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


# `sin(5 pi / 6)` is exactly 1/2 but mpmath computes it from a truncated pi, so
# an increment that is exactly 0 in closed form lands at +-1e-(dps). Every
# comparison below is therefore made with a tolerance far above that noise and
# far below any real gap; the Lean statement is `<=` precisely because these
# exact ties are real (part iv).
TOL = mpf(10) ** (-30)

print("=== (i) argmax is floor(5N/6) ===")
print(f"{'N':>6} {'floor(5N/6)':>12} {'true argmax':>12} {'ties':>6}")
for N in list(range(6, 61)) + [72, 100, 128, 180, 240, 361, 512]:
    vals = [log_prod(N, k) for k in range(N)]
    mx = max(vals)
    argmaxes = [k for k, v in enumerate(vals) if v > mx - TOL]
    ks = 5 * N // 6
    ok = all(v <= vals[ks] + TOL for v in vals)
    if N <= 24 or N % 6 == 0 or not ok:
        print(f"{N:6d} {ks:12d} {str(argmaxes):>12} {len(argmaxes):6d}"
              + ("" if ok else "   <-- FAIL"))
    check(ok, f"argmax mismatch at N={N}: floor(5N/6)={ks}, argmaxes={argmaxes}")

print()
print("=== (ii) the exact ratio, and where it crosses 1 ===")
for N in (7, 12, 13, 30):
    bad = 0
    for k in range(N - 1):
        lhs = log_prod(N, k + 1) - log_prod(N, k)
        rhs = 2 * log(2 * sin(mpf(k + 1) * pi / N))
        if abs(lhs - rhs) > mpf(10) ** (-28):
            bad += 1
        # rises exactly while N <= 6(k+1) <= 5N
        rising = (N <= 6 * (k + 1)) and (6 * (k + 1) <= 5 * N)
        if rising:
            check(lhs >= -mpf(10) ** (-28),
                  f"N={N} k={k}: in rising window but term fell")
        else:
            check(lhs <= mpf(10) ** (-28),
                  f"N={N} k={k}: outside rising window but term rose")
    check(bad == 0, f"ratio identity failed {bad} times at N={N}")
    print(f"  N={N:3d}: ratio identity exact, rise/fall matches the window")

print()
print("=== (iii) DOWN-UP-DOWN, not unimodal ===")
for N in (12, 30, 60, 120):
    vals = [log_prod(N, k) for k in range(N)]
    kl = N // 6
    ks = 5 * N // 6
    dip = min(range(kl + 1), key=lambda k: vals[k])
    # A plateau, not a strict local minimum: when 6 | N the increment at
    # j = N/6 is exactly 1, so vals[N/6] == vals[N/6 - 1]. Test the SHAPE
    # (down to a dip, then up to the argmax), not strict local-minimality.
    print(f"  N={N:4d}: falls to k={dip} (floor(N/6)={kl}) at "
          f"{float(vals[dip]):.3f}, then rises to {float(vals[ks]):.3f} "
          f"at k={ks}; vals[0] = {float(vals[0]):.1f}")
    check(vals[dip] < vals[0] - 1,
          f"N={N}: expected a real dip after k=0 — the sequence is not unimodal")
    check(vals[dip] < vals[ks] - 1,
          f"N={N}: expected the sequence to rise from the dip to the argmax")
    check(all(vals[k] <= vals[0] + TOL for k in range(0, kl + 1)),
          f"N={N}: sequence not falling on [0, floor(N/6)]")

print()
print("=== (iv) ties are real: 6 | N makes `<` false ===")
for N in (12, 30, 60):
    ks = 5 * N // 6
    eq = abs(log_prod(N, ks) - log_prod(N, ks - 1)) < TOL
    print(f"  N={N:3d}: kashaevProd(N,{ks}) == kashaevProd(N,{ks - 1})? {bool(eq)}")
    check(bool(eq), f"N={N}: expected an exact tie at the saddle when 6 | N")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
