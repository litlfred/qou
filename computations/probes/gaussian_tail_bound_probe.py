#!/usr/bin/env python3
"""The Gaussian tail outside a window — bean `qou-fybg`, step 13.

Checks `QOU/MathlibExt/GaussianTailBound.lean`:

  hasSum_int_geometric        sum_{n in Z} q^|n| = 1 + 2q/(1-q)
  tsum_gaussian_sub_sum_Icc_le
      sum_{n in Z} e^{-a(n-c)^2} - sum_{|n|<=W} e^{-a(n-c)^2}
        <= e^{a c^2} e^{-a(W+1)^2/4} (1 + 2 sigma/(1-sigma)),  sigma = e^{-a/4}

Part (iv) is the one with content beyond validity: it measures the tail bound
AGAINST the main term `sqrt(pi/a)` at the Kashaev parameters, for several
window exponents `W = N^p`.  There is a genuine tradeoff, and this bound is
what makes it visible:

  * the tail wants `p` LARGE -- it decays like `exp(-a W^2/4) ~ exp(-1.36 N^{2p-1})`;
  * step 10's cubic remainder `M pi^2 |u|^3/(3N^2) ~ N^{3p-2}` wants `p` SMALL.

Both hold on `1/2 < p < 2/3`, and `p = 0.6` is the BALANCED choice: tail
exponent `N^{0.2}` against cubic `N^{-0.2}`.  Neither end of the range is
comfortable -- at `p = 0.55` the tail bound is still 8.6x the main term at
N = 1e6 (the crossover is near 1e10), and at `p = 0.65` the cubic decays only
like `N^{-0.05}`.  My first guess was that larger `p` is simply better; the
numbers say otherwise, which is why they are here.

Run:  python3 computations/probes/gaussian_tail_bound_probe.py
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


def gauss_tsum(a, c):
    hw = int(sqrt(mpf(130) * log(10) / a)) + int(abs(c)) + 20
    lo = int(c) - hw
    return sum(exp(-a * (mpf(n) - c) ** 2) for n in range(lo, lo + 2 * hw + 1))


def window_sum(a, c, W):
    return sum(exp(-a * (mpf(n) - c) ** 2) for n in range(-W, W + 1))


def tail_bound(a, c, W):
    sigma = exp(-a / 4)
    return (exp(a * c ** 2) * exp(-a * (mpf(W) + 1) ** 2 / 4)
            * (1 + 2 * sigma / (1 - sigma)))


print("=== (i) the two-sided geometric series over Z ===")
for q in (mpf('0.1'), mpf('0.5'), mpf('0.9'), mpf('0.99')):
    # truncate adaptively: a fixed +-400 is nowhere near enough at q = 0.99
    # (0.99^400 = 0.018), and a fixed window silently reports a wrong sum.
    M = int(mpf(45) * log(10) / (-log(q))) + 10
    S = sum(q ** abs(n) for n in range(-M, M + 1))
    closed = 1 + 2 * q / (1 - q)
    check(abs(S - closed) <= closed * mpf('1e-30') + TOL,
          f"geometric series wrong at q={q}: {S} vs {closed} (M={M})")
print("  q in {0.1, 0.5, 0.9, 0.99}, adaptive truncation: ok")

print()
print("=== (ii) the tail bound ===")
print(f"{'a':>8} {'c':>7} {'W':>4} {'true tail':>16} {'bound':>16} "
      f"{'slack x':>12} {'ok':>4}")
for a in (mpf('1.0'), mpf('0.3')):
    for c in (mpf(0), mpf('0.83'), mpf('-2')):
        for W in (2, 5, 10):
            true = gauss_tsum(a, c) - window_sum(a, c, W)
            b = tail_bound(a, c, W)
            ok = true <= b + TOL
            slack = b / true if true > 0 else mpf('inf')
            print(f"{float(a):8.2f} {float(c):7.2f} {W:4d} {float(true):16.6e} "
                  f"{float(b):16.6e} {float(slack):12.3e} "
                  f"{'ok' if ok else 'FAIL':>4}")
            check(ok, f"tail bound violated at a={a}, c={c}, W={W}: "
                      f"{true} > {b}")

print()
print("=== (iii) how crude the bound is -- stated, not hidden ===")
# The file's docstring calls the bound deliberately crude.  Quantify it, so the
# claim is checkable rather than an assertion.
a, c, W = mpf('1.0'), mpf(0), 5
true = gauss_tsum(a, c) - window_sum(a, c, W)
b = tail_bound(a, c, W)
sharp = exp(-a * (mpf(W) + 1) ** 2)          # what a sharp bound would keep
print(f"  a=1, c=0, W=5:  true = {float(true):.4e},  this bound = {float(b):.4e},"
      f"  e^-a(W+1)^2 = {float(sharp):.4e}")
print(f"  overshoot factor: {float(b / true):.4e}")
check(b / true > 1,
      "the bound would have to be at least the truth")
check(b / true > mpf('1e3'),
      f"the docstring calls this bound crude; if the overshoot were small the "
      f"description would be wrong (got {float(b/true)})")

print()
print("=== (iv) at the Kashaev parameters: the window-exponent tradeoff ===")
# a, c, L exactly as steps 10/12 produce them; W = N^p.
#
# tail/main ~ 1.93 sqrt(N) exp(-1.36 N^{2p-1})   [this bound]
# cubic     ~ N^{3p-2}                            [step 10's remainder]
#
# The tail is super-polynomially small once p > 1/2 -- but only ONCE
# 1.36 N^{2p-1} beats the 1/(1-sigma) ~ N/1.36 prefactor, and at p barely
# above 1/2 that crossover is astronomically far out.  The cubic needs
# p < 2/3 and decays only like N^{3p-2}.
print(f"{'N':>9} {'p':>5} {'W':>8} {'tail/sqrt(pi/a)':>18} {'cubic ~ N^(3p-2)':>18}")
tail06 = {}
for N in (10 ** 4, 10 ** 5, 10 ** 6):
    ks = 5 * N // 6
    th = mpf(ks) * pi / N
    a = pi * abs(cos(th) / sin(th)) / mpf(N)
    L = log(2 * sin(th))
    c = L / a
    main = sqrt(pi / a)
    for p in (mpf('0.55'), mpf('0.60'), mpf('0.65')):
        W = int(mpf(N) ** p)
        rel = tail_bound(a, c, W) / main
        cubic = mpf(N) ** (3 * p - 2)
        if p == mpf('0.60'):
            tail06[N] = (rel, cubic)
        print(f"{N:9d} {float(p):5.2f} {W:8d} {float(rel):18.4e} "
              f"{float(cubic):18.4e}")

# p = 0.6 is the balanced choice: tail exponent N^{0.2}, cubic N^{-0.2}.
Ns = sorted(tail06)
check(all(tail06[Ns[i + 1]][0] < tail06[Ns[i]][0] for i in range(len(Ns) - 1)),
      f"at p=0.6 the tail/main ratio is not decreasing: "
      f"{[float(tail06[n][0]) for n in Ns]}")
check(all(tail06[Ns[i + 1]][1] < tail06[Ns[i]][1] for i in range(len(Ns) - 1)),
      f"at p=0.6 the cubic is not decreasing: "
      f"{[float(tail06[n][1]) for n in Ns]}")
check(tail06[10 ** 5][0] < mpf('1e-3'),
      f"at p=0.6, N=1e5 the tail should already be under 1e-3 of the main "
      f"term; got {float(tail06[10**5][0])}")
print("  p = 0.6 balances them: tail exponent N^0.2, cubic N^-0.2, both -> 0.")

# p = 0.55 is asymptotically valid and USELESS at these N -- record it, since
# a first reading of this file's docstring suggested `p large is better`, and
# the opposite end is the trap.
ks = 5 * (10 ** 6) // 6
th = mpf(ks) * pi / (10 ** 6)
a55 = pi * abs(cos(th) / sin(th)) / mpf(10 ** 6)
c55 = log(2 * sin(th)) / a55
rel55 = tail_bound(a55, c55, int(mpf(10 ** 6) ** mpf('0.55'))) / sqrt(pi / a55)
check(rel55 > 1,
      f"p=0.55 at N=1e6 was expected to give a USELESS tail bound (>1x the "
      f"main term); got {float(rel55)}. If it is already small, the crossover "
      f"claim here is wrong.")
print(f"  p = 0.55 at N=1e6: tail/main = {float(rel55):.2f} -- still useless.")
print("    (1.36 N^0.1 = 5.4 has not yet beaten the 0.5 log N = 6.9 from the")
print("     sqrt(N) prefactor; that crossover is near N ~ 1e10.)")
print("  p = 0.65: tail is negligible but the cubic only decays like N^-0.05,")
print("    so it is WORSE overall than p = 0.6, not better.")

print()
if FAILURES:
    print(f"FAILED ({len(FAILURES)}):")
    for f in FAILURES[:20]:
        print("  -", f)
    raise SystemExit(1)
print("all assertions pass")
