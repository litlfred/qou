#!/usr/bin/env python3
"""
log_channel_does_not_rescue_simplex_basis_probe — I proposed the log channel as
the constructive fix for the basis-span failure, on a structural argument. The
argument is wrong at nuclear A and the fix does not work. This records the
negative, its reason, and one by-product that strengthens a separate result.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Fourth probe of PR #6393,
refuting a conjecture of mine made in the same PR.

## The conjecture, and why it looked right

The companion probe measures that the coordination basis `C(A,2), C(A,3),
C(A,4)` cannot span `rho_grad(A) = [A]_q!/[2]_q!` -- pinned on A = 2,3,4 it is
142x short by A = 8 -- because `rho_grad` grows factorially while the basis is
polynomial.

The obvious structural fix: `rho_grad` is a PRODUCT, `prod_{k=3..A} [k]_q`, so
its natural additive object is the log. And since `[k]_q = (q^k - 1)/(q - 1)`,
for large k one has `log [k]_q ~ k log q`, giving

    log rho_grad(A) = sum_{k=3..A} log [k]_q  ~  log q * sum k  ~  C(A,2) * log q

-- the bond count again, matching the tower height and the
`QOU.Mass.CoordinationSaturation` cap. Three independent routes to `C(A,2)` would
have been a strong result, and the binding producers already work in the log
channel (`eps = E_0 log(1/f)`, `L = log(tr_free/tr_atom)`), so it would have
aligned the decomposition with the channel the corpus already uses.

## It is refuted, twice over

**(i) The asymptotic identity does not hold at nuclear A.** `log [k]_q ~ k log q`
needs `k log q >> 1`. At the proton pin `log q0 = 0.10434`, so `k log q` does not
even reach 1 until `k = 1/log q0 = 9.58`.

That estimate is the *optimistic* one and should not be quoted as the crossover:
what matters is which of `k log q` and the naive `log k` the true `log [k]_q` is
nearer, and measured at this pin **`log k` wins all the way to k = 20**, with
`k log q` taking over only between k = 20 and k = 50. So the nuclear range is not
merely pre-asymptotic, it is pre-asymptotic by a wide margin. At k = 3,
`log [k]_q = 1.2066` sits far closer to `log k = 1.0986` than to
`k log q = 0.3130`.

The consequence is measured directly: `log rho_grad(A) / (C(A,2) log q)` is 4.40
at A = 4 and DECLINES to 3.34 at A = 12 -- moving away from 1, not toward it.

**(ii) In the simplex basis the log channel is not better, it is differently
bad.** Pinned on the same three points:

        A       linear pred/true     log pred/true
        5           0.5639              0.3741
        6           0.1901             -1.0401
        8           0.007037           -6.7800
       12           4.53e-7           -33.054

The linear channel collapses toward zero; the log channel inverts sign at A = 6
and diverges negative. Neither spans the object. A polynomial basis pinned at
three points fails on `A log A` growth much as it fails on factorial growth.

## The by-product, which strengthens a separate result

The log solve returns `g_2 = 0` EXACTLY, for the same reason the linear one does:
`log rho_grad(2) = log 1 = 0`. So the `mu_2 = 0` normalisation identity that the
`mu2_vanishing` probe on this PR analyses is **channel-independent** -- it
survives any monotone reparametrisation fixing `1 -> 0`, which is independent
confirmation that its vanishing carries no information about 2-body content.

## What rho_grad actually is at nuclear A -- worth recording

Between the two natural comparisons, at the proton pin:

        A     rho/(A!/2)     rho/q^C(A,2)
        4        1.31            8.42
        8        4.46         4845
       12       39.5             9.67e6

`rho_grad` sits far nearer the plain factorial `A!/2` (the permutation count,
i.e. the q -> 1 limit) than the asymptotic `q^C(A,2)`, and drifts away from both.
So at nuclear A the q-deformation is a SUBLEADING correction and the leading
content of the graded reference is the bare permutation count.

This does not disturb the companion probe: the tower's height `C(A,2)` and the
positivity of every coefficient are exact combinatorial facts, independent of q.
It does mean the `C(A,2)` coincidence between the tower height and the
saturation cap is about the DEGREE STRUCTURE, not about magnitudes, and it should
not be read as the two objects agreeing numerically.

Scope **(a)**: a refuted conjecture of mine, its reason, and two measurements.
Nothing wired; no replacement basis is offered, and after this probe I do not
have one.

NO FLOAT64: mpmath `mpf` at 50 dps, exact integer factorials and binomials.
`float` appears nowhere.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: E402, F401

from math import comb, factorial  # noqa: E402

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.mp.dps = 50
PIN = (2, 3, 4)


def q_int(n: int, q):
    return mp.fsum([q**k for k in range(n)])


def rho_grad(A: int, q):
    r = mp.mpf(1)
    for k in range(3, A + 1):
        r *= q_int(k, q)
    return r


def C(A: int, k: int):
    return mp.mpf(comb(A, k))


def solve(fn):
    return mp.lu_solve(mp.matrix([[C(A, 2), C(A, 3), C(A, 4)] for A in PIN]),
                       mp.matrix([fn(A) for A in PIN]))


def fmt(x, n=8):
    return mp.nstr(x, n)


def main() -> int:
    q0 = Q_MP
    lq = mp.log(q0)

    print("log_channel_does_not_rescue_simplex_basis_probe")
    print("=" * 78)
    print("MY CONJECTURE (made in this same PR, and refuted here):")
    print("  rho_grad is a PRODUCT, so its additive object is the log; and since")
    print("  log [k]_q ~ k log q for large k,")
    print("      log rho_grad(A) = sum_k log [k]_q ~ C(A,2) * log q")
    print("  -- the bond count a third time, aligning the decomposition with the")
    print("  log channel the binding producers already use.")
    print()

    print("REFUTATION (i) — the asymptotic identity fails at nuclear A")
    print("-" * 78)
    print(f"  log [k]_q ~ k log q needs k*log q >> 1.  log q0 = {fmt(lq, 8)},")
    print(f"  so k*log q does not even reach 1 until k = {fmt(1 / lq, 8)}.")
    print("  That is the OPTIMISTIC estimate.  The crossover that matters is which")
    print("  of k*log q and the naive log k the true log [k]_q is nearer -- and")
    print("  measured, log k wins to k = 20, with k*log q taking over only between")
    print("  k = 20 and k = 50.  Pre-asymptotic by a wide margin:")
    print(f"{'k':>5} {'log [k]_q':>12} {'k*log q':>11} {'log k':>10} {'nearer':>10}")
    for k in (3, 5, 8, 12, 20, 50, 200):
        lk = mp.log(q_int(k, q0))
        asym, naive = k * lq, mp.log(k)
        nearer = "k*log q" if abs(lk - asym) < abs(lk - naive) else "log k"
        print(f"{k:>5} {fmt(lk, 7):>12} {fmt(asym, 7):>11} {fmt(naive, 7):>10} "
              f"{nearer:>10}")
    print()
    print("  So at k = 3 the q-deformed log is nearer the NAIVE log k; the")
    print("  asymptotic form only takes over well above the nuclear range.")
    print(f"{'A':>3} {'log rho_grad':>15} {'C(A,2)*log q':>15} {'ratio':>10}")
    ratios = {}
    for A in range(3, 13):
        L = mp.log(rho_grad(A, q0))
        r = L / (C(A, 2) * lq)
        ratios[A] = r
        print(f"{A:>3} {fmt(L, 10):>15} {fmt(C(A, 2) * lq, 10):>15} {fmt(r, 8):>10}")
    print()
    print(f"  The ratio is {fmt(ratios[4], 6)} at A=4 and DECLINES to "
          f"{fmt(ratios[12], 6)} at A=12 --")
    print("  moving away from 1, not toward it.  The conjecture is refuted.")
    assert ratios[12] < ratios[4], "ratio must move away from 1, refuting the claim"
    assert ratios[12] > 2, "and it is nowhere near 1"
    print()

    print("REFUTATION (ii) — in the simplex basis, the log channel is not better")
    print("-" * 78)
    g_lin = solve(lambda A: rho_grad(A, q0))
    g_log = solve(lambda A: mp.log(rho_grad(A, q0)))
    print(f"  linear: g2={fmt(g_lin[0], 8)} g3={fmt(g_lin[1], 8)} "
          f"g4={fmt(g_lin[2], 8)}")
    print(f"  log   : g2={fmt(g_log[0], 8)} g3={fmt(g_log[1], 8)} "
          f"g4={fmt(g_log[2], 8)}")
    print()
    print(f"{'A':>4} {'linear pred/true':>19} {'log pred/true':>16}")
    log_ratios = {}
    for A in (5, 6, 8, 12):
        pl = (g_lin[0] * C(A, 2) + g_lin[1] * C(A, 3) + g_lin[2] * C(A, 4)) \
            / rho_grad(A, q0)
        pg = (g_log[0] * C(A, 2) + g_log[1] * C(A, 3) + g_log[2] * C(A, 4)) \
            / mp.log(rho_grad(A, q0))
        log_ratios[A] = pg
        print(f"{A:>4} {fmt(pl, 7):>19} {fmt(pg, 7):>16}")
    print()
    print("  The linear channel collapses toward zero; the log channel INVERTS")
    print("  SIGN at A=6 and diverges negative.  Neither spans the object -- a")
    print("  polynomial basis pinned at three points fails on A log A growth much")
    print("  as it fails on factorial growth.")
    assert log_ratios[6] < 0 and log_ratios[12] < -10, \
        "the log channel should invert sign and diverge"
    print()

    print("BY-PRODUCT — this strengthens the mu2 result on this PR")
    print("-" * 78)
    print(f"  The log solve returns g2 = {fmt(g_log[0], 6)} EXACTLY, for the same")
    print("  reason the linear one does: log rho_grad(2) = log 1 = 0.")
    assert g_log[0] == 0, "g2 must be exactly 0 in the log channel too"
    print("  So the mu_2 = 0 normalisation identity is CHANNEL-INDEPENDENT: it")
    print("  survives any monotone reparametrisation fixing 1 -> 0.  That is")
    print("  independent confirmation that its vanishing carries no information")
    print("  about 2-body content.")
    print()

    print("WHAT rho_grad ACTUALLY IS AT NUCLEAR A")
    print("-" * 78)
    print(f"{'A':>4} {'rho/(A!/2)':>14} {'rho/q^C(A,2)':>16}")
    for A in (4, 6, 8, 12):
        t = rho_grad(A, q0)
        print(f"{A:>4} {fmt(t / (mp.mpf(factorial(A)) / 2), 7):>14} "
              f"{fmt(t / q0 ** comb(A, 2), 9):>16}")
    print()
    print("  rho_grad sits far nearer the plain factorial A!/2 -- the permutation")
    print("  count, i.e. the q -> 1 limit -- than the asymptotic q^C(A,2), and")
    print("  drifts away from both.  At nuclear A the q-deformation is a")
    print("  SUBLEADING correction; the leading content is the bare permutation")
    print("  count.")
    print()
    print("  This does NOT disturb the companion probe: the tower's height C(A,2)")
    print("  and the positivity of every coefficient are exact combinatorial")
    print("  facts, independent of q.  It does mean the C(A,2) coincidence")
    print("  between tower height and saturation cap is about DEGREE STRUCTURE,")
    print("  not magnitudes, and must not be read as numerical agreement.")
    print()
    print("  No replacement basis is offered.  After this probe I do not have one.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
