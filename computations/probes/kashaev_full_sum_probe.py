#!/usr/bin/env python3
"""The whole invariant against the closed form — bean `qou-fybg`, step 18.

Checks `QOU/Knot/KashaevFullSum.lean`:

  kashaev_split             range N = [0,w) + [w,k*-W) + [k*-W,k*+W] + (k*+W,N)
  abs_kashaev_sub_model_le  | <4_1>_N - g_{k*} e^{L^2/a} sqrt(pi/a) |
                              <= g_{k*} (window + below + left + right)

Part (iii) is the headline of the whole arc: `<4_1>_N / (g_{k*} sqrt N)` should
converge to `3^(-1/4)`.  Steps 12 and 15 reached that from the Gaussian model
and from the window sum respectively; this is the FULL Kashaev invariant, every
term of it.

Everything is normalised by `g_{k*}` (which is about `e^{0.323 N}`) and
accumulated in log space -- raw values overflow float64 and print as `inf`.

Run:  python3 computations/probes/kashaev_full_sum_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, exp

mp.dps = 60

FAILURES = []
TOL = mpf(10) ** (-30)


def check(cond, msg):
    if not cond:
        FAILURES.append(msg)
    return cond


def log_prods(N):
    """[log g_0, ..., log g_{N-1}], accumulated incrementally."""
    out = [mpf(0)]
    acc = mpf(0)
    for k in range(1, N):
        acc += 2 * log(2 * sin(mpf(k) * pi / N))
        out.append(acc)
    return out


def params(N, p=mpf('0.6')):
    ks = 5 * N // 6
    W = int(mpf(N) ** p)
    w = -(-2 * N // 3)                    # ceil(2N/3)
    return ks, W, w


def hyps_ok(N):
    ks, W, w = params(N)
    return (6 <= N and 6 * w <= 5 * N and 2 * N <= 3 * w and w <= ks
            and 2 <= ks - w and w <= ks - W and ks + W + 1 <= N
            and W <= ks and 1 <= ks - W)


print("=== (i) where every side condition of the full theorem holds ===")
first = next(N for N in range(6, 600) if hyps_ok(N))
print(f"  smallest N: {first}")
for N in range(6, first):
    check(not hyps_ok(N),
          f"the side conditions were expected to fail below N={first}, but "
          f"they hold at N={N}")
check(first <= 200, f"the full theorem should be usable by N=200; got {first}")

print()
print("=== (ii) the four-way split is exact ===")
for N in (241, 961):
    ks, W, w = params(N)
    lp = log_prods(N)
    base = lp[ks]
    tot = sum(exp(lp[k] - base) for k in range(N))
    pieces = (sum(exp(lp[k] - base) for k in range(0, w))
              + sum(exp(lp[k] - base) for k in range(w, ks - W))
              + sum(exp(lp[k] - base) for k in range(ks - W, ks + W + 1))
              + sum(exp(lp[k] - base) for k in range(ks + W + 1, N)))
    check(abs(tot - pieces) <= abs(tot) * mpf('1e-45'),
          f"the four-way split is not exact at N={N}")
print("  N in {241, 961}: the four regions reassemble exactly")

print()
print("=== (iii) THE HEADLINE: <4_1>_N / (g_{k*} sqrt N) -> 3^(-1/4) ===")
print(f"{'N':>7} {'<4_1>_N/(g* sqrtN)':>21} {'gap to 3^-1/4':>15} {'x N':>10}")
target = mpf(3) ** mpf('-0.25')
gaps = []
for N in (241, 961, 3841, 15361):
    ks, W, w = params(N)
    lp = log_prods(N)
    base = lp[ks]
    tot = sum(exp(lp[k] - base) for k in range(N))
    val = tot / sqrt(mpf(N))
    gap = abs(val - target)
    gaps.append((N, gap))
    print(f"{N:7d} {float(val):21.12f} {float(gap):15.4e} "
          f"{float(gap * N):10.4f}")
check(all(gaps[i + 1][1] < gaps[i][1] for i in range(len(gaps) - 1)),
      f"<4_1>_N/(g_* sqrt N) is not converging to 3^(-1/4): "
      f"{[float(g[1]) for g in gaps]}")
check(gaps[-1][1] < mpf('1e-4'),
      f"still {float(gaps[-1][1])} away from 3^(-1/4) at N={gaps[-1][0]}")
print(f"  3^(-1/4) = {float(target):.12f}")
print("  this is the FULL invariant -- every term of sum_{k<N} g_k.")

print()
print("=== (iv) the proved bound, and how far from sharp it is ===")
print(f"{'N':>7} {'true gap':>13} {'window':>12} {'below':>12} {'left':>12} "
      f"{'right':>12}")
for N in (961, 3841):
    ks, W, w = params(N)
    lp = log_prods(N)
    base = lp[ks]
    th = mpf(ks) * pi / N
    a = -(pi * (cos(th) / sin(th)) / mpf(N))
    L = log(2 * sin(th))
    lo, hi = mpf(ks - W) * pi / N, mpf(ks + W) * pi / N
    grid = [lo + (hi - lo) * mpf(i) / 200 for i in range(201)]
    M = max(1 / sin(x) ** 2 for x in grid)
    K = max(abs(cos(x) / sin(x)) for x in grid)

    def errt(kk):
        t = mpf(kk) * pi / N
        return 2 * (1 / (144 * mpf(kk) ** 2) + mpf(7) / 12 * (pi / N) ** 2
                    + (pi / N) ** 2 / (12 * sin(t) ** 2))
    B = max(errt(ks) + errt(kp)
            + M * pi ** 2 * abs(mpf(kp) - mpf(ks)) ** 3 / (3 * mpf(N) ** 2)
            + K * pi * abs(mpf(kp) - mpf(ks)) / mpf(N)
            + M * pi ** 2 * abs(mpf(kp) - mpf(ks)) / (6 * mpf(N) ** 2)
            for kp in range(ks - W, ks + W + 1))
    q, sig = exp(-pi ** 2 / a), exp(-a / 4)
    E = exp(L ** 2 / a) * (sqrt(pi / a) * (2 * q / (1 - q))
                           + exp(a * (L / a) ** 2)
                           * exp(-a * (mpf(W) + 1) ** 2 / 4)
                           * (1 + 2 * sig / (1 - sig)))
    model = exp(L ** 2 / a) * sqrt(pi / a)
    D = mpf(ks - w)
    e_win = (exp(B) - 1) * (model + E) + E
    e_bel = mpf(w) / mpf(N) ** 2 + mpf(w) * (sqrt(3) * mpf(N)) / (pi * D * (D - 1))
    e_lef = mpf(N) * exp(-(pi * (mpf(W) + 1) * mpf(W) / (sqrt(3) * mpf(N))))
    e_rig = mpf(N) * exp(-(sqrt(3) * pi * (mpf(W) + 1) * mpf(W) / mpf(N)))
    tot = sum(exp(lp[k] - base) for k in range(N))
    true = abs(tot - model)
    bound = e_win + e_bel + e_lef + e_rig
    check(true <= bound + TOL, f"the full bound is violated at N={N}")
    print(f"{N:7d} {float(true):13.4e} {float(e_win):12.4e} "
          f"{float(e_bel):12.4e} {float(e_lef):12.4e} {float(e_rig):12.4e}")
    # Absolute sizes do not say which term binds; only the ratio to the main
    # term does, since the main term GROWS like sqrt(N).
    print(f"        /model: {'':5} {float(e_win/model):12.4e} "
          f"{float(e_bel/model):12.4e} {float(e_lef/model):12.4e} "
          f"{float(e_rig/model):12.4e}")
    parts = {'window': e_win, 'below': e_bel, 'left': e_lef, 'right': e_rig}
    worst = max(parts, key=lambda kk: parts[kk])
    check(worst == 'window',
          f"at N={N} the dominant error is '{worst}', not the window -- the "
          f"claim that only the window matters would be wrong")
print("  The window dominates at both N.  Asymptotically it stays dominant:")
print("    window/model ~ B ~ M pi^2 W^3/(3N^2) ~ 13.2 N^-0.2   (cubic-limited)")
print("    below /model ~ (24 sqrt3/pi)/(3^-1/4 sqrt N) ~ 17.4 N^-0.5")
print("    left  /model ~ sqrt(N) exp(-1.81 N^0.2),  right likewise with 5.44")
print("  Note the BELOW bound is CONSTANT in N (24 sqrt3/pi = 13.2) in absolute")
print("  terms -- it vanishes only because the main term grows.  Its true size")
print("  is ~1e-47 (step 17 probe), so it is loose by ~48 orders; that costs")
print("  nothing only because the window is looser still.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
