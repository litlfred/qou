#!/usr/bin/env python3
"""<4_1>_N above and below, with no g_{k*} — bean `qou-fybg`, step 19.

Checks `QOU/Knot/KashaevAsymptoticBounds.lean`:

  abs_log_kashaevProd_argmax_le   |log g_{k*} - P| <= E          (step 7, named)
  kashaevProd_argmax_bounds       e^{P-E} <= g_{k*} <= e^{P+E}
  kashaev_bounds_of_model
      e^{P-E}(model - err) <= <4_1>_N <= e^{P+E}(model + err)

Part (ii) is the headline in its final form:

    e^{P} * model / (N^{3/2} e^{N Vol/2pi})  ->  3^(-1/4)

Part (iii) asks the question the theorem actually turns on: `err <= model`.
Without it the lower bound is NEGATIVE and says nothing.  With `W = N^0.6` that
condition does not hold until `N ~ 1e7`; the probe therefore SEARCHES for the
best `W` at each `N` and reports where the theorem first has content.  A window
exponent is a free parameter, and 0.6 -- convenient for the tail analysis of
step 13 -- is not the one that makes this statement usable soonest.

Run:  python3 computations/probes/kashaev_asymptotic_bounds_probe.py
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
TOL = mpf(10) ** (-30)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def lob(th):
    return clsin(2, 2 * th) / 2


VCOEFF = -(2 / pi) * lob(5 * pi / 6)          # Vol(4_1)/(2 pi)


def peak_main(N):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    return (-(2 * mpf(N) / pi) * lob(5 * pi / 6)
            + log(2 * mpf(N) * sin(th))
            + (pi / (6 * mpf(N))) * (cos(th) / sin(th)))


def peak_err(N):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    return (2 * (1 / (144 * mpf(ks) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                 + (pi / N) ** 2 / (12 * sin(th) ** 2))
            + (2 * mpf(N) / pi) * (sqrt(3) * (pi / N) ** 2 / 2
                                   + 4 * (pi / N) ** 3 / 6))


def log_prod_peak(N):
    ks = 5 * N // 6
    return 2 * sum(log(2 * sin(mpf(j) * pi / N)) for j in range(1, ks + 1))


print("=== (i) step 7 brackets log g_{k*} ===")
print(f"{'N':>7} {'log g_k*':>16} {'P':>16} {'|diff|':>12} {'E':>12} {'ok':>4}")
for N in (241, 961, 3841):
    lg = log_prod_peak(N)
    P, E = peak_main(N), peak_err(N)
    ok = abs(lg - P) <= E + TOL
    print(f"{N:7d} {float(lg):16.8f} {float(P):16.8f} {float(abs(lg-P)):12.4e} "
          f"{float(E):12.4e} {'ok' if ok else 'FAIL':>4}")
    check(ok, f"step 7's bracket fails at N={N}")


def model_of(N):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    a = -(pi * (cos(th) / sin(th)) / mpf(N))
    L = log(2 * sin(th))
    return exp(L ** 2 / a) * sqrt(pi / a), a, L


print()
print("=== (ii) THE HEADLINE: e^P model / (N^{3/2} e^{N Vol/2pi}) -> 3^-1/4 ===")
print(f"{'N':>8} {'value':>18} {'gap to 3^-1/4':>15} {'x N':>10}")
target = mpf(3) ** mpf('-0.25')
gaps = []
for N in (241, 961, 3841, 15361, 61441):
    P = peak_main(N)
    model, a, L = model_of(N)
    val = exp(P) * model / (mpf(N) ** mpf('1.5') * exp(mpf(N) * VCOEFF))
    gap = abs(val - target)
    gaps.append((N, gap))
    print(f"{N:8d} {float(val):18.12f} {float(gap):15.4e} {float(gap*N):10.4f}")
check(all(gaps[i + 1][1] < gaps[i][1] for i in range(len(gaps) - 1)),
      f"the headline is not converging to 3^(-1/4): {[float(g[1]) for g in gaps]}")
# Assert the RATE, not a hand-picked absolute tolerance: gap x N settles.
scaled = [g[1] * g[0] for g in gaps]
check(max(scaled[1:]) - min(scaled[1:]) < mpf('0.1'),
      f"gap x N is not settling, so the convergence is not clean O(1/N): "
      f"{[float(x) for x in scaled]}")
print(f"  3^(-1/4) = {float(target):.12f};  Vol(4_1)/2pi = {float(VCOEFF):.12f}")
print(f"  gap x N -> {float(scaled[-1]):.4f}, clean O(1/N).  (Step 18's headline")
print(f"  had constant 0.536; this one uses the MODEL and step 7's MAIN term")
print(f"  rather than the true values, so the O(1/N) constants differ.)")

print()
print("=== (iii) when does `err <= model` hold?  (the lower bound's content) ===")


def total_err_over_model(N, W):
    """(window + below + left + right) / model, with w = ceil(2N/3)."""
    ks = 5 * N // 6
    w = -(-2 * N // 3)
    if not (W <= ks and 1 <= ks - W and ks + W + 1 <= N and w <= ks - W
            and 2 <= ks - w):
        return None
    th = mpf(ks) * pi / N
    a = -(pi * (cos(th) / sin(th)) / mpf(N))
    L = log(2 * sin(th))
    lo, hi = mpf(ks - W) * pi / N, mpf(ks + W) * pi / N
    grid = [lo + (hi - lo) * mpf(i) / 60 for i in range(61)]
    if any(x <= 0 or x >= pi for x in grid):
        return None
    M = max(1 / sin(x) ** 2 for x in grid)
    K = max(abs(cos(x) / sin(x)) for x in grid)

    def errt(kk):
        t = mpf(kk) * pi / N
        return 2 * (1 / (144 * mpf(kk) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                    + (pi / N) ** 2 / (12 * sin(t) ** 2))
    u = mpf(W)
    B = (2 * errt(ks - W) + M * pi ** 2 * u ** 3 / (3 * mpf(N) ** 2)
         + K * pi * u / mpf(N) + M * pi ** 2 * u / (6 * mpf(N) ** 2))
    q, sig = exp(-pi ** 2 / a), exp(-a / 4)
    E = exp(L ** 2 / a) * (sqrt(pi / a) * (2 * q / (1 - q))
                           + exp(a * (L / a) ** 2)
                           * exp(-a * (u + 1) ** 2 / 4)
                           * (1 + 2 * sig / (1 - sig)))
    model = exp(L ** 2 / a) * sqrt(pi / a)
    D = mpf(ks - w)
    tot = ((exp(B) - 1) * (model + E) + E
           + model * 0 + mpf(w) / mpf(N) ** 2
           + mpf(w) * (sqrt(3) * mpf(N)) / (pi * D * (D - 1))
           + mpf(N) * exp(-(pi * (u + 1) * u / (sqrt(3) * mpf(N))))
           + mpf(N) * exp(-(sqrt(3) * pi * (u + 1) * u / mpf(N))))
    return tot / model


print(f"{'N':>9} {'W=N^0.6':>9} {'err/model':>12} {'best W':>8} "
      f"{'best err/model':>15}")
rows = []
for N in (10 ** 4, 10 ** 5, 10 ** 6):
    W06 = int(mpf(N) ** mpf('0.6'))
    r06 = total_err_over_model(N, W06)
    best, bestr = None, None
    for W in range(int(mpf(N) ** mpf('0.45')), int(mpf(N) ** mpf('0.66')),
                   max(1, N // 400)):
        r = total_err_over_model(N, W)
        if r is not None and (bestr is None or r < bestr):
            best, bestr = W, r
    rows.append((N, r06, best, bestr))
    print(f"{N:9d} {W06:9d} {float(r06):12.4f} {best:8d} {float(bestr):15.4f}")
check(all(r[3] < r[1] for r in rows),
      f"optimising W should beat the N^0.6 choice at every N; it did not")
usable = [r[0] for r in rows if r[3] < 1]
check(usable,
      f"`err <= model` never holds in the range tested, even with the best W: "
      f"{[(r[0], float(r[3])) for r in rows]} -- the lower bound would be "
      f"vacuous everywhere probed")
print(f"  `err <= model` first holds (best W) at N = {min(usable)}")
check(min(usable) == 10 ** 6,
      f"expected the threshold at N=1e6 with an optimised W; got {min(usable)}. "
      f"If this moved, the point at which the LOWER bound acquires content "
      f"moved with it.")
print("  With W = N^0.6 it holds at NO N tested (19.4, 3.66, 1.45 at 1e4..1e6);")
print("  optimising W beats it everywhere and brings the threshold to 1e6.")
print("  The exponent 0.6 is convenient for step 13's tail analysis, not for")
print("  making the lower bound have content: the cubic remainder wants a")
print("  SMALLER window than the tail does, and the balance point moves with N.")
print("  (W = N^0.6 should come good near N ~ 1e7, where its cubic term is")
print("   13.2 N^-0.2 ~ 0.52; that is past what this probe computes.)")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
