#!/usr/bin/env python3
"""Everything outside the window — bean `qou-fybg`, step 17.

Checks `QOU/Knot/KashaevBeyondWindow.lean`:

  mul_pred_le_of_le              d(d-1) >= (W+1)W once d >= W+1
  sum_kashaevProd_right_beyond_le
      sum_{k=k*+W+1}^{N-1} g_k <= N g_{k*} exp(-sqrt3 pi (W+1)W/N)
  sum_kashaevProd_left_beyond_le
      sum_{k=w}^{k*-W-1} g_k   <= N g_{k*} exp(-pi (W+1)W/(sqrt3 N)),  2N <= 3w

Parts (iii)-(iv) are the ones with content.  The main term is
`3^(-1/4) sqrt(N) g_{k*}`, so what has to be checked is not that the tails are
small but that they are small RELATIVE TO sqrt(N):

  * the right tail carries `sqrt3 pi = 5.441` in the exponent;
  * the left tail carries `pi/sqrt3 = 1.814` -- a factor 3 weaker, because the
    secant chord is shallower than the tangent one.  It still wins, later.
  * the region below `2N/3`, which neither covers, is bounded separately and
    is the one that has to be checked directly.

Run:  python3 computations/probes/kashaev_beyond_window_probe.py
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


def log_prod(N, k):
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, k + 1))


def ratio_to_peak(N, k, base):
    """g_k / g_{k*}, in log space."""
    return exp(log_prod(N, k) - base)


print("=== (i) d(d-1) >= (W+1)W for d >= W+1 ===")
for W in (0, 1, 5, 40):
    for d in (W + 1, W + 2, W + 17):
        check(mpf(d) * (mpf(d) - 1) >= (mpf(W) + 1) * mpf(W) - TOL,
              f"d(d-1) >= (W+1)W fails at W={W}, d={d}")
print("  12 (W, d) pairs: ok")

print()
print("=== (ii) the two tail bounds ===")
print(f"{'N':>6} {'W':>4} {'true right':>14} {'right bound':>14} "
      f"{'true left':>14} {'left bound':>14} {'ok':>4}")
for N in (241, 961, 3841):
    ks = 5 * N // 6
    base = log_prod(N, ks)
    W = int(mpf(N) ** mpf('0.6'))
    w = -(-2 * N // 3)                       # ceil(2N/3), so 2N <= 3w
    tr = sum(ratio_to_peak(N, k, base) for k in range(ks + W + 1, N))
    br = mpf(N) * exp(-(sqrt(3) * pi * (mpf(W) + 1) * mpf(W) / N))
    tl = sum(ratio_to_peak(N, k, base) for k in range(w, ks - W))
    bl = mpf(N) * exp(-(pi * (mpf(W) + 1) * mpf(W) / (sqrt(3) * N)))
    ok = tr <= br + TOL and tl <= bl + TOL
    print(f"{N:6d} {W:4d} {float(tr):14.4e} {float(br):14.4e} "
          f"{float(tl):14.4e} {float(bl):14.4e} {'ok' if ok else 'FAIL':>4}")
    check(tr <= br + TOL, f"right tail bound violated at N={N}")
    check(tl <= bl + TOL, f"left tail bound violated at N={N}")

print()
print("=== (iii) the tails against the MAIN term (3^-1/4 sqrt N) ===")
# Small is not enough; small compared with sqrt(N) is what matters.
print(f"{'N':>8} {'right bnd/sqrtN':>17} {'left bnd/sqrtN':>16}")
rr, ll = [], []
for N in (241, 961, 3841, 10 ** 5, 10 ** 6):
    W = int(mpf(N) ** mpf('0.6'))
    br = mpf(N) * exp(-(sqrt(3) * pi * (mpf(W) + 1) * mpf(W) / N)) / sqrt(mpf(N))
    bl = mpf(N) * exp(-(pi * (mpf(W) + 1) * mpf(W) / (sqrt(3) * N))) / sqrt(mpf(N))
    rr.append((N, br))
    ll.append((N, bl))
    print(f"{N:8d} {float(br):17.4e} {float(bl):16.4e}")
check(all(rr[i + 1][1] < rr[i][1] for i in range(len(rr) - 1)),
      f"the right tail is not shrinking relative to sqrt(N): "
      f"{[float(r[1]) for r in rr]}")
check(all(ll[i + 1][1] < ll[i][1] for i in range(len(ll) - 1)),
      f"the left tail is not shrinking relative to sqrt(N): "
      f"{[float(l[1]) for l in ll]}")
check(rr[-1][1] < mpf('1e-20'), f"right tail still {float(rr[-1][1])} at N=1e6")
check(ll[-1][1] < mpf('1e-6'), f"left tail still {float(ll[-1][1])} at N=1e6")
print(f"  the LEFT tail is the slower of the two by a factor 3 in the exponent")
print(f"  (pi/sqrt3 = {float(pi/sqrt(3)):.3f} against sqrt3 pi = "
      f"{float(sqrt(3)*pi):.3f}): the secant chord is shallower than the")
print(f"  tangent one, so the same window buys less on the left.")

print()
print("=== (iv) the region below 2N/3, which neither bound covers ===")
# `sum_kashaevProd_left_beyond_le` needs 2N <= 3k.  Everything below that is
# left to KashaevTailBound's cruder machinery -- so check directly that it is
# negligible against sqrt(N), which is all that is required of it.
print(f"{'N':>6} {'w=ceil(2N/3)':>13} {'sum_{k<w} g_k/g*':>18} {'/sqrt(N)':>12}")
below = []
for N in (241, 961, 3841):
    ks = 5 * N // 6
    base = log_prod(N, ks)
    w = -(-2 * N // 3)
    tot = sum(ratio_to_peak(N, k, base) for k in range(0, w))
    below.append((N, tot / sqrt(mpf(N))))
    print(f"{N:6d} {w:13d} {float(tot):18.4e} {float(tot/sqrt(mpf(N))):12.4e}")
check(all(below[i + 1][1] < below[i][1] for i in range(len(below) - 1)),
      f"the below-2N/3 region is not shrinking relative to sqrt(N): "
      f"{[float(b[1]) for b in below]}")
check(below[-1][1] < mpf('1e-3'),
      f"the below-2N/3 region is {float(below[-1][1])} of the main term at "
      f"N={below[-1][0]}; it needs to vanish for c_sigma to be readable")
print("  it vanishes relative to sqrt(N), which is all that is asked of it --")
print("  so KashaevTailBound's crude constants there cost nothing.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
