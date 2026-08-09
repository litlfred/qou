#!/usr/bin/env python3
"""The window assembly — bean `qou-fybg`, step 15.

Checks `QOU/Knot/KashaevWindowAssembly.lean`:

  sum_window_model_eq        the model sum over the Nat window equals the model
                             sum over the Int window
  abs_sum_kashaevProd_window_sub_model_le
      | sum_{|k'-k|<=W} g_k'  -  g_k e^{L^2/a} sqrt(pi/a) |
        <= g_k ( (e^B - 1)(e^{L^2/a} sqrt(pi/a) + E) + E )

with `E = gaussWindowErr a L W` and `B` the sup over the window of step 10's
bound.

Everything is normalised by `g_k`: it is about `e^{0.323 N}`, so raw values
overflow float64's exponent range and print as `inf` while telling you nothing.
(That mistake was made once already, in the step-11 probe.)

Part (iii) is the payoff: the window sum divided by `g_k sqrt(N)` should
converge to `3^(-1/4)` -- this time from the Kashaev sum itself, not from the
Gaussian model alone as in step 12.

Run:  python3 computations/probes/kashaev_window_assembly_probe.py
"""

from mpmath import mp, mpf, sin, cos, log, pi, sqrt, exp

mp.dps = 60

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


def sup_over(N, k, k2, f, samples=120):
    a, b = sorted((theta(N, k), theta(N, k2)))
    if a == b:
        return f(a)
    return max(f(a + (b - a) * mpf(i) / samples) for i in range(samples + 1))


def step10_bound(N, k, kp):
    u = abs(mpf(kp) - mpf(k))
    M = sup_over(N, k, kp, lambda x: 1 / sin(x) ** 2)
    K = sup_over(N, k, kp, lambda x: abs(cos(x) / sin(x)))
    return (err_term(N, k) + err_term(N, kp)
            + M * pi ** 2 * u ** 3 / (3 * mpf(N) ** 2)
            + K * pi * u / mpf(N)
            + M * pi ** 2 * u / (6 * mpf(N) ** 2))


def gauss_window_err(a, L, W):
    q = exp(-pi ** 2 / a)
    sigma = exp(-a / 4)
    return exp(L ** 2 / a) * (sqrt(pi / a) * (2 * q / (1 - q))
                              + exp(a * (L / a) ** 2)
                              * exp(-a * (mpf(W) + 1) ** 2 / 4)
                              * (1 + 2 * sigma / (1 - sigma)))


def setup(N, p=mpf('0.6')):
    k = 5 * N // 6
    th = theta(N, k)
    a = pi * abs(cos(th) / sin(th)) / mpf(N)
    L = log(2 * sin(th))
    W = int(mpf(N) ** p)
    return k, a, L, W


print("=== (i) the model sum, Nat window vs Int window ===")
for N in (240, 960):
    k, a, L, W = setup(N)
    lhs = sum(exp(-a * (mpf(kp) - mpf(k)) ** 2 + 2 * L * (mpf(kp) - mpf(k)))
              for kp in range(k - W, k + W + 1))
    rhs = sum(exp(-a * mpf(n) ** 2 + 2 * L * mpf(n)) for n in range(-W, W + 1))
    check(abs(lhs - rhs) <= abs(lhs) * mpf('1e-45'),
          f"reindexing disagrees at N={N}")
    check(W <= k, f"the hypothesis W <= k fails at N={N}: W={W}, k={k}")
print("  N in {240, 960}: both windows agree, and W <= k holds")

print()
print("=== (ii) the assembly bound (everything over g_k) ===")
print(f"{'N':>7} {'W':>5} {'B':>9} {'|win/g - model|':>17} {'bound/g':>14} "
      f"{'ok':>4}")
rows = []
# N NOT divisible by 6.  For 6 | N the saddle index hits 5pi/6 exactly, so
# L = 0 and the model is 3^(-1/4) sqrt(N) BY CONSTRUCTION -- the tilt is never
# exercised and part (iii)'s model column is a tautology.  (Same trap as the
# step-6 probe, which also first used only 6 | N.)
for N in (241, 961, 3841):
    k, a, L, W = setup(N)
    win = [kp for kp in range(k - W, k + W + 1) if 1 <= kp < N]
    B = max(step10_bound(N, k, kp) for kp in win)
    # window sum divided by g_k, in log space so nothing overflows
    ratio = sum(exp(log_prod(N, kp) - log_prod(N, k)) for kp in win)
    model = exp(L ** 2 / a) * sqrt(pi / a)
    E = gauss_window_err(a, L, W)
    lhs = abs(ratio - model)
    bound = (exp(B) - 1) * (model + E) + E
    ok = lhs <= bound + TOL
    rows.append((N, k, W, B, ratio, model, E))
    print(f"{N:7d} {W:5d} {float(B):9.4f} {float(lhs):17.6e} "
          f"{float(bound):14.6e} {'ok' if ok else 'FAIL':>4}")
    check(ok, f"assembly bound violated at N={N}: {lhs} > {bound}")

print()
print("=== (iii) THE PAYOFF: window sum / (g_k sqrt(N)) -> 3^(-1/4) ===")
# Same target as step 12, but reached from the KASHAEV sum rather than from the
# Gaussian model.
print(f"{'N':>7} {'window/(g_k sqrtN)':>20} {'model/sqrtN':>14} "
      f"{'gap to 3^-1/4':>15}")
target = mpf(3) ** mpf('-0.25')
gaps = []
for N, k, W, B, ratio, model, E in rows:
    val = ratio / sqrt(mpf(N))
    gap = abs(val - target)
    gaps.append((N, gap))
    print(f"{N:7d} {float(val):20.10f} {float(model/sqrt(mpf(N))):14.10f} "
          f"{float(gap):15.4e}")
check(all(gaps[i + 1][1] < gaps[i][1] for i in range(len(gaps) - 1)),
      f"the window sum over g_k sqrt(N) is not converging to 3^(-1/4): "
      f"{[float(g[1]) for g in gaps]}")
print(f"  3^(-1/4) = {float(target):.10f}")
print("  (this is the Kashaev sum itself, not the Gaussian model of step 12.)")

print()
print("=== (iv) is the BOUND yet useful at these N? ===")
# Honest accounting: the assembly is proved, but at N a few thousand the bound
# is still larger than the quantity it bounds.  Report the ratio rather than
# implying the theorem is numerically sharp here.
print(f"{'N':>7} {'true gap':>13} {'bound':>13} {'bound/true':>12} "
      f"{'bound/model':>13}")
useful = []
for N, k, W, B, ratio, model, E in rows:
    true = abs(ratio - model)
    bound = (exp(B) - 1) * (model + E) + E
    useful.append((N, bound / model))
    print(f"{N:7d} {float(true):13.4e} {float(bound):13.4e} "
          f"{float(bound / true):12.3e} {float(bound / model):13.4e}")
check(all(useful[i + 1][1] < useful[i][1] for i in range(len(useful) - 1)),
      f"bound/model is not shrinking: {[float(u[1]) for u in useful]} -- the "
      f"assembly would never become informative")
check(useful[-1][1] > mpf('0.05'),
      f"bound/model at N={useful[-1][0]} is {float(useful[-1][1])}; if it were "
      f"already tiny the caveat below would be overstated")
print(f"  bound/model is shrinking fast but is still ~{float(useful[-1][1]):.0f}x")
print("  the main term at the largest N here: the assembly is PROVED and is")
print("  NOT yet numerically sharp at any N reachable by this probe.  What")
print("  pins c_sigma is the limit, which part (iii) exhibits; the finite-N")
print("  bound does not.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
