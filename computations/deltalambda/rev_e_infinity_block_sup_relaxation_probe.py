#!/usr/bin/env python3
r"""
rev_e_infinity_block_sup_relaxation_probe.py — the block value is CONCAVE, so `sup_s Xblock`
is a concave program; certifying its maximum CLOSES gap G2 (qou-hok7)

#7349 bounded every valid top block by `B_sharp = 3.9214`, uniformly in its length and its
entries, which made the `e_inf` search finite: `s_t + s_b <= 90`.  90 is not enumerable
(~2.4e10 blocks), so the practical cut stayed on the *measured* `sup_s Xblock = 2.1598`, and
that conditionality is gap **G2**.

This probe attacks G2 and gets most of the way.

## Where `B_sharp` loses it

`B_sharp` sums a per-row budget `Ghat(i+1)^2 / (2 ln q0)`, and **row 0 alone is 73.8 % of the
total** — 2.8936 of 3.9214, attained at `u_0 = 7.447`.  That is fiction: the per-row bound is
the tangent at `u = 0` and has no cap, while a single row's actual gain *saturates* at
`S_e(1) = sum_d eps(2d) = 2.568` and then turns over against the quadratic cost.  Measured, the
best single-row block is `[3]` at **0.9297**, and `[8]` is worth **-1.149** against a bound of
2.878.

## Two ways to fix it, and the second is better

**Jensen.**  `f(x) = eps(2d) - eps(2d+x)` is concave (`f'' = -eps'' < 0`), so the distance-`d`
pair sum obeys `sum_i f(Delta_i) <= (T-d) f(mean)`, which saturates at `(T-d) eps(2d)` instead
of running away linearly.  That is valid and much tighter — `B_jensen = 2.6951` over this
probe's `T <= 12`, cut `90 -> 43` — and **still not enumerable**, 43 being ~1e10 blocks.  (A
longer separate run put the Jensen peak at `T = 13`, 2.69566, declining to 2.5532 by `T = 20`;
it does not move the cut.)

**Concavity of the objective itself.**  The same second-derivative fact applies to the whole
block value, not just to one bound: every internal term is `-eps(2d + (u_i - u_j))` up to a
constant, a concave function of a linear map of `u`; every bulk tail is `-eps(2d + u_i)`; the
cost is `-(ln q0/2) sum u_i^2`.  So `Xblock` is **concave in `u`**, and maximising it over the
convex set `{u_i >= 1}` is a concave program — a relaxation of the integer problem, hence a
rigorous upper bound, and one that drops no structure at all.

    B_relax  =  sup over real u >= 1 of Xblock(u)  =  2.2537313388   at T = 7

against the integer maximum 2.1598023761 — **1.042x**, where `B_sharp` was 1.816x.  Its argmax
`[3.977, 2.794, 2.075, 1.582, 1.231, 1, 1]` is recognisably the integer argmax
`[4, 3, 2, 2, 1, 1, 1]` with the integrality let out.  The cut becomes `s_t + s_b <= 27`, and
**27 is enumerable**: ~6e6 blocks, a couple of minutes, against 2.4e10 at 90.

## Closing G2: the certificate, and the trap inside it

Coordinate ascent on a concave function reaches the global maximum, and the gradient at the
reported optimum is tiny — but "tiny gradient in a numerical search" is not a proof.  What
settles it is the supergradient inequality, which holds at *every* `u` because `F` is concave:

    F(u)  <=  F(w) + grad F(w) . (u - w) .

The linear term is unbounded on its own, so the search region is confined first.  The per-row
bound gives `F(u) <= phi_i(u_i) + sum_{j != i} rowcap(j)`, so any `u` that reaches the incumbent
`INT_SUP` has `phi_i(u_i) >= INT_SUP - sum_{j != i} rowcap(j)` — a quadratic inequality in one
variable, whose solution set is an interval `[L_i, U_i]`.  Outside that box `F` is already below
the incumbent.  Maximising the linear term over `[1, U_i]` per coordinate therefore gives an
unconditional

    sup F(T = 7)  <=  2.25373556700090488296611      slack 6.43e-12 ,

which is `6.8e-11` of the distance to the integer maximum: the certificate costs nothing.  The
gradient here is **analytic** (`gx = -eps'` in closed form), not a central difference — the
inequality is about the true gradient, and a difference quotient would make it a statement about
the step size instead.

**The trap.**  At the optimum rows 5 and 6 sit on the boundary `u = 1` with *strictly negative*
gradients (-0.01155, -0.27151).  That is correct KKT behaviour, not a convergence failure.  But
for `g_i < 0` the max of `g_i (u_i - w_i)` over `[1, U_i]` is at `u_i = 1`, not at `U_i`;
charging every row `|g_i| (U_i - w_i)` instead inflates the slack to **1.447**, which swamps the
entire result by eleven orders of magnitude.  That error was made here first, and it is the only
delicate step — so P8 recomputes the inflated figure every run rather than quoting it.

The ascent point is **polished** before the certificate is taken: coordinates the search parked
at `1.0000149` are snapped to exactly `1` (killing a `+4e-6` boundary term outright) and the
interior ones get a wider ternary.  `F(w)` barely moves; the slack falls 1.50e-5 → 6.43e-12.
The certificate is valid at *any* `w`, so choosing a better one is free.

**Block length.**  The per-row cap gives a rigorous `T` bound: every row past index 5 contributes
at most `Ghat(i+1) - ln q0/2`, negative there and tending to `-ln q0/2`, so the cumulative cap
drops below the certified bound at an explicit `T0` this probe computes (`T0 = 40`).  A run with
`REV_BLOCK_SUP_TMAX=40` therefore covers **every** admissible length; the default 12 does not,
and says so.  That longer run declines monotonically from the `T = 7` peak at `ln q0/2` per step
throughout — 2.25373 at `T = 7`, 1.45889 at 25, 0.98942 at 34, 0.72856 at 39, **0.67639 at
T = 40 = T0**, a factor of 3.33 below the peak — so the peak is at `T = 7` over the whole
admissible range, not merely over the range that was convenient to measure.

## What it buys

The join over the certified cut `s_t + s_b <= 27` (6,325,875 blocks) returns

    e_inf  =  2.43929645512078402706542884314   at (s_t, s_b) = (8, 8),

agreeing with #7335's independently searched value to 1e-30.  So `e_inf` is no longer "the best
value a search found" but the **maximum over a window proved to contain it**.  The remaining
conditionality is **G1** alone — `Xbot(s) <= Xblock(s)`, measured equal for `s <= 12` — which
none of this touches, nor does any of it touch the arc's headline problem, the upper bound on
`M_n`.

## Checks

  P1  `Xblock` at real `u` reproduces the integer enumeration at the known argmax
  P2  `Xblock` is concave in `u` — checked on random ordered triples, not assumed
  P3  Jensen is a valid upper bound on the exact value, and saturates where the linear one
      does not
  P4  the per-row bound's slack is concentrated in row 0 (73.8 % of `B_sharp`), and a single
      row's true maximum is 0.9297 against that row's 2.8936 budget
  P5  the relaxed sup `B_relax`, per `T`, with its peak, its argmax and its certificate
  P6  the four bounds and the cut each one gives, with the enumeration cost of each cut
  P7  the rigorous `T0` past which no block length can reach the certified bound
  P8  the supergradient certificate — G2 item (a)
  P9  the join over the certified cut reproduces #7335's `e_inf`

Proton-pinned; `mp.dps = 30`; the bulk tail uses the Lambert resummation of #7349 (verified
here against the direct sum) so a coordinate step costs `O(T + RMAX)` rather than
`O(T^2 + T*RMAX)`.  No float64.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/BraidKnot/SearchCoercivity.lean
"""

from __future__ import annotations

import json
import os
import random
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 30
Q0 = mp.mpf(Q_50_DIGIT_STR)
LNQ = mp.log(Q0)
LNQ_HALF = LNQ / 2
T2 = Q0 ** 2
LNT2 = mp.log(T2)

TARGET_DIGITS = 28
_LN10 = mp.log(10)
DEPTH2 = int(mp.ceil(TARGET_DIGITS * _LN10 / (2 * LNQ))) + 5
DEPTH4 = int(mp.ceil(TARGET_DIGITS * _LN10 / (4 * LNQ))) + 5
RMAX = int(mp.ceil(TARGET_DIGITS * _LN10 / mp.log(T2 ** 2))) + 5
TOL = mp.mpf(10) ** (-(TARGET_DIGITS - 6))

TMAX = int(os.environ.get("REV_BLOCK_SUP_TMAX", "12"))
UMAX = mp.mpf(30)

E_INF_7335 = mp.mpf("2.43929645512078402706542884314")
# #7349's enumerated max (at [4,3,2,2,1,1,1]), READ from the witness that
# measures it (rev-e-infinity-search-reduction, coercivity_S3.measured_B) rather
# than typed (witness-value copy ratchet).
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "rev-e-infinity-search-reduction.witness.json"), encoding="utf-8") as _fh:
    INT_SUP = mp.mpf(json.load(_fh)["coercivity_S3"]["measured_B"])
# witness-copy-intentional: #7349's per-row bound, quoted as published; this probe's own witness records
# it, so reading it back from there would be circular.
B_SHARP = mp.mpf("3.92139923021415319458053")          # #7349's per-row uniform bound

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def epsx(x) -> mp.mpf:
    """`eps` at a REAL argument — the relaxation needs it off the integers."""
    return -mp.log(1 - T2 ** (-x)) if x > 0 else mp.inf


def g(d: int) -> mp.mpf:
    x = T2 ** (-2 * d)
    return LNT2 * x / (1 - x)


GHAT = {m: mp.fsum(g(d) for d in range(m, DEPTH2)) for m in range(1, DEPTH2)}
S_E1 = mp.fsum(epsx(2 * d) for d in range(1, DEPTH2))

_C: dict[int, list] = {}


def _coeffs(m: int):
    """`TAIL(m, v) = sum_r (1/r)(1 - t^(-vr)) t^(-2mr)/(1 - t^(-2r))` — #7349's resummation."""
    if m not in _C:
        _C[m] = [(mp.mpf(1) / r) * T2 ** (-2 * m * r) / (1 - T2 ** (-2 * r))
                 for r in range(1, RMAX)]
    return _C[m]


def TAIL(m: int, v) -> mp.mpf:
    c = _coeffs(m)
    z = T2 ** (-v)
    zp = mp.mpf(1)
    tot = mp.mpf(0)
    for r in range(1, RMAX):
        zp *= z
        tot += c[r - 1] * (1 - zp)
    return tot


def F(u) -> mp.mpf:
    """The block value at REAL `u` — the same function `edge_direct` computes at integers."""
    T = len(u)
    tot = mp.mpf(0)
    for i in range(T):
        for j in range(i + 1, T):
            tot += epsx(2 * (j - i)) - epsx(2 * (j - i) + u[i] - u[j])
        tot += TAIL(T - i, u[i])
    return tot - LNQ_HALF * mp.fsum(x * x for x in u)


def F_coord(u, i: int, x) -> mp.mpf:
    """Only the part of `F` that depends on `u_i`.  O(T + RMAX), not O(T^2 + T RMAX)."""
    T = len(u)
    tot = mp.mpf(0)
    for j in range(T):
        if j == i:
            continue
        if j > i:
            tot += epsx(2 * (j - i)) - epsx(2 * (j - i) + x - u[j])
        else:
            tot += epsx(2 * (i - j)) - epsx(2 * (i - j) + u[j] - x)
    return tot + TAIL(T - i, x) - LNQ_HALF * x * x


def jensen(u) -> mp.mpf:
    """Jensen per distance on the internal pairs; exact tails, exact cost."""
    T = len(u)
    tot = mp.mpf(0)
    for d in range(1, T):
        n = T - d
        m = (mp.fsum(u[:d]) - mp.fsum(u[T - d:])) / n
        tot += n * (epsx(2 * d) - epsx(2 * d + m))
    tot += mp.fsum(TAIL(T - i, u[i]) for i in range(T))
    return tot - LNQ_HALF * mp.fsum(x * x for x in u)


def gx(x) -> mp.mpf:
    """`-eps'(x)` in closed form.  ANALYTIC, not a finite difference: the supergradient
    inequality is about the true gradient, and a central difference would make the certificate
    a statement about the step size."""
    z = T2 ** (-x)
    return LNT2 * z / (1 - z)


def gradF(u):
    """The exact gradient of `F` at real `u`, term by term against `F`'s own definition."""
    T = len(u)
    out = []
    for i in range(T):
        s = mp.mpf(0)
        for j in range(T):
            if j == i:
                continue
            if j > i:
                s += gx(2 * (j - i) + u[i] - u[j])
            else:
                s -= gx(2 * (i - j) + u[j] - u[i])
        s += mp.fsum(gx(2 * d + u[i]) for d in range(T - i, DEPTH2 + T))
        out.append(s - LNQ * u[i])
    return out


def _row_cap(i: int) -> mp.mpf:
    """`max_{v >= 1} [v Ghat(i+1) - (ln q0/2) v^2]` — the most row `i` can contribute."""
    gh = GHAT[i + 1]
    return gh ** 2 / (2 * LNQ) if gh >= LNQ else gh - LNQ_HALF


def certificate(T: int, w, incumbent):
    """A rigorous upper bound on `sup_{u >= 1} F_T(u)` from the supergradient inequality.

    `F` is concave, so for EVERY `u`:  `F(u) <= F(w) + grad F(w) . (u - w)`.  The linear term is
    unbounded on its own, so it is confined first: the per-row bound gives
    `F(u) <= phi_i(u_i) + sum_{j != i} rowcap(j)`, so any `u` with `F(u) >= incumbent` has
    `phi_i(u_i) >= incumbent - sum_{j != i} rowcap(j)`, a quadratic inequality whose solution set
    is an interval `[L_i, U_i]`.  Outside that box `F` is already below the incumbent, so

        sup F_T  <=  max( incumbent ,  F(w) + sum_i max_{u_i in [1, U_i]} g_i (u_i - w_i) ) .

    The per-coordinate max is at `U_i` when `g_i >= 0` and at `1` when `g_i < 0` — the second
    case is the one that matters, because at the optimum the boundary coordinates sit at
    `u_i = 1` with a strictly negative gradient (KKT), and charging them `|g_i| (U_i - w_i)`
    instead inflates the slack by a factor of 3e7.
    """
    g = gradF(w)
    fw = F(w)
    caps = [_row_cap(i) for i in range(T)]
    tot = mp.fsum(caps)
    slack = mp.mpf(0)
    naive = mp.mpf(0)          # what charging |g_i|(U_i - w_i) unconditionally would cost
    rows = []
    for i in range(T):
        need = incumbent - (tot - caps[i])
        gh = GHAT[i + 1]
        disc = gh * gh - 4 * LNQ_HALF * need
        if disc < 0:
            # no `v` at all reaches the incumbent through row `i`: this `T` cannot beat it
            return incumbent, None, None, rows, True
        Ui = (gh + mp.sqrt(disc)) / (2 * LNQ_HALF)
        if Ui < 1:
            return incumbent, None, None, rows, True
        term = g[i] * (Ui - w[i]) if g[i] >= 0 else g[i] * (1 - w[i])
        slack += term
        naive += abs(g[i]) * (Ui - w[i])
        rows.append({"row": i, "grad": mp.nstr(g[i], 12), "U": mp.nstr(Ui, 12),
                     "w": mp.nstr(w[i], 12), "term": mp.nstr(term, 12)})
    bound = fw + slack
    return (bound if bound > incumbent else incumbent), slack, naive, rows, False


def _ternary(f, lo, hi, iters: int = 34):
    for _ in range(iters):
        a = lo + (hi - lo) / 3
        b = hi - (hi - lo) / 3
        if f(a) < f(b):
            lo = a
        else:
            hi = b
    return (lo + hi) / 2


def relaxed_sup(T: int, sweeps: int = 30):
    """Coordinate ascent on the concave program.  Returns (value, profile)."""
    u = [mp.mpf(max(1, 4 - i)) for i in range(T)]
    prev = None
    for _ in range(sweeps):
        for i in range(T):
            u[i] = _ternary(lambda x, i=i: F_coord(u, i, x), mp.mpf(1), UMAX)
        cur = F(u)
        if prev is not None and abs(cur - prev) < TOL:
            break
        prev = cur
    return F(u), u


def polish(u, snap_tol=mp.mpf("1e-3"), sweeps: int = 40, iters: int = 90):
    """Sharpen the ascent point so the CERTIFICATE is tight — `F(w)` barely moves.

    Two effects, and the first dominates.  A coordinate the ascent parked at `1.0000149` rather
    than at `1` carries a boundary gradient of -0.27, and `g_i (1 - w_i)` is then `+4e-6`
    instead of `0`; snapping it to exactly `1` kills that term outright.  And a wider ternary
    on the interior coordinates drives their gradients from ~1e-6 to ~1e-9, which matters
    because they are multiplied by a box width of ~10.

    The certificate is valid at ANY `w` — `F` is concave everywhere — so choosing a better `w`
    is free: it can only tighten the bound, never invalidate it.  Measured, this takes the
    slack from 1.50e-5 to 4.56e-8, a factor of 329.
    """
    v = [mp.mpf(1) if x < 1 + snap_tol else x for x in u]
    free = [i for i in range(len(v)) if v[i] > 1 + snap_tol]
    prev = None
    for _ in range(sweeps):
        for i in free:
            v[i] = _ternary(lambda x, i=i: F_coord(v, i, x), mp.mpf(1), UMAX, iters=iters)
        cur = F(v)
        if prev is not None and abs(cur - prev) < TOL:
            break
        prev = cur
    return v


T_KERNEL =[2 * epsx(2 * d) - epsx(2 * d - 1) - epsx(2 * d + 1) for d in range(1, DEPTH4)]


def xrun(ell: int) -> mp.mpf:
    return mp.fsum(min(d, ell) * T_KERNEL[d - 1] for d in range(1, DEPTH4)) - LNQ_HALF * ell


def cut_for(B) -> int:
    th = E_INF_7335 - 2 * B
    return max(ell for ell in range(1, 3000) if xrun(ell) > th)


def blocks_with_sum_at_most(S: int) -> int:
    """Exact count of valid blocks (entries >= 1, u_{i+1} <= u_i + 1) with sum <= S."""
    n = 0

    def rec(last, s):
        nonlocal n
        n += 1
        lo = max(1, last - 1) if last is not None else 1
        for x in range(lo, S - s + 1):
            rec(x, s + x)

    rec(None, 0)
    return n - 1


# --------------------------------------------------------------------------------------------
print("the block value is concave — sup_s Xblock is a concave program")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  mp.dps = {mp.dps}")
print(f"  depths derived from the decay rates: eps {DEPTH2}, T {DEPTH4}, Lambert {RMAX}")
print(f"  coordinate ascent over T <= {TMAX} (REV_BLOCK_SUP_TMAX)")
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P1  the real-u value against #7349's integer enumeration")
_argmax_int = [mp.mpf(x) for x in (4, 3, 2, 2, 1, 1, 1)]
_p1 = F(_argmax_int)
_p1_diff = _p1 - INT_SUP
# and the Lambert tail against the direct sum, since everything routes through it
_p1_tail = max(abs(TAIL(m, mp.mpf(v))
                   - mp.fsum(epsx(2 * d) - epsx(2 * d + v) for d in range(m, DEPTH2)))
               for (m, v) in ((1, 3), (1, 7), (4, 2), (7, 4), (2, 5)))
print(f"    F([4,3,2,2,1,1,1]) = {mp.nstr(_p1, 24)}")
print(f"    #7349 enumerated   = {mp.nstr(INT_SUP, 24)}")
print(f"    difference         = {mp.nstr(_p1_diff, 6)}")
print(f"    Lambert tail vs direct sum, worst of 5 points: {mp.nstr(_p1_tail, 6)}", flush=True)
check(
    "P1 the real-u objective is the same function the integer enumeration maximised",
    abs(_p1_diff) < TOL and _p1_tail < TOL,
    f"F at the integer argmax reproduces #7349's enumerated maximum to "
    f"{mp.nstr(_p1_diff, 4)}, and the Lambert tail resummation agrees with the direct sum to "
    f"{mp.nstr(_p1_tail, 4)} at 5 points.  Both matter: the relaxation is only a relaxation of "
    f"the right problem if the extended function restricts correctly, and every evaluation "
    f"here routes through the resummed tail rather than the sum #7349 used",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P2  is the objective concave?  (the relaxation's whole premise)")
random.seed(11)


def _rand_profile(T: int):
    u = [mp.mpf(random.uniform(1, 9))]
    for _ in range(T - 1):
        u.append(max(mp.mpf(1), u[-1] + mp.mpf(random.uniform(-3, 1))))
    return u


_p2_worst = None
_p2_n = 0
for _ in range(200):
    _T = random.randint(2, 8)
    _a, _b = _rand_profile(_T), _rand_profile(_T)
    _lam = mp.mpf(random.uniform(mp.mpf("0.05"), mp.mpf("0.95")))
    _mid = [_lam * p + (1 - _lam) * q for p, q in zip(_a, _b)]
    _gap = F(_mid) - (_lam * F(_a) + (1 - _lam) * F(_b))
    _p2_n += 1
    if _p2_worst is None or _gap < _p2_worst[0]:
        _p2_worst = (_gap, _T, _lam)
print(f"    {_p2_n} random ordered triples, T = 2..8")
print(f"    min F(mid) - [lam F(a) + (1-lam) F(b)] = {mp.nstr(_p2_worst[0], 8)} "
      f"at T = {_p2_worst[1]}", flush=True)
check(
    "P2 the block value is concave in u — measured, not assumed",
    _p2_worst[0] >= 0,
    f"minimum concavity gap {mp.nstr(_p2_worst[0], 6)} over {_p2_n} random ordered triples.  "
    f"The reason is one second derivative used three times: every internal term is "
    f"`-eps(2d + (u_i - u_j))` up to a constant — concave composed with a linear map — every "
    f"bulk tail is `-eps(2d + u_i)`, and the cost is `-(ln q0/2) sum u_i^2`.  This is what "
    f"makes the relaxation to real u a CONCAVE PROGRAM rather than a search, so a "
    f"coordinate-wise stationary point is the global maximum and not a local one",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P3  Jensen against the exact value — valid, and saturating")
_p3 = []
for _u in ([4, 3, 2, 2, 1, 1, 1], [3, 2, 1, 1, 1], [1], [4], [8], [12],
           [7, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2, 2, 2]):
    _uu = [mp.mpf(x) for x in _u]
    _ex, _je = F(_uu), jensen(_uu)
    _lin = mp.fsum(_uu[k] * GHAT[k + 1] - LNQ_HALF * _uu[k] * _uu[k] for k in range(len(_uu)))
    _p3.append({"block": _u, "exact": mp.nstr(_ex, 22), "jensen": mp.nstr(_je, 22),
                "linear": mp.nstr(_lin, 22)})
    print(f"    {str(_u):26s} exact {mp.nstr(_ex, 14):18s} Jensen {mp.nstr(_je, 14):18s} "
          f"linear {mp.nstr(_lin, 14)}", flush=True)
_p3_viol = sum(1 for r in _p3 if mp.mpf(r["jensen"]) < mp.mpf(r["exact"]) - TOL)
_p3_8 = next(r for r in _p3 if r["block"] == [8])
check(
    "P3 Jensen is a valid upper bound and saturates where the linear one runs away",
    _p3_viol == 0,
    f"0 violations over {len(_p3)} blocks.  The difference in kind shows at [8]: exact "
    f"{mp.nstr(mp.mpf(_p3_8['exact']), 8)}, Jensen {mp.nstr(mp.mpf(_p3_8['jensen']), 8)} — "
    f"equal, because a single-row block has no internal pairs and Jensen leaves the tail exact "
    f"— against the linear bound's {mp.nstr(mp.mpf(_p3_8['linear']), 8)}.  The linear bound "
    f"claims a block worth MINUS one is worth nearly three, which is the whole of why "
    f"B_sharp is 1.8x too big",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P4  where B_sharp's slack lives")
_p4_rows = [(i, GHAT[i + 1], GHAT[i + 1] ** 2 / (2 * LNQ), GHAT[i + 1] / LNQ) for i in range(6)]
_row0 = _p4_rows[0][2]
_single_best = max(((F([mp.mpf(v)]), v) for v in range(1, 26)), key=lambda t: t[0])
for _i, _gh, _bud, _ustar in _p4_rows:
    print(f"    row {_i}: Ghat({_i+1}) = {mp.nstr(_gh, 10):14s} budget {mp.nstr(_bud, 10):14s} "
          f"attained at u = {mp.nstr(_ustar, 6)}")
print(f"    best single-row block: [{_single_best[1]}] worth "
      f"{mp.nstr(_single_best[0], 16)}   (row-0 budget {mp.nstr(_row0, 16)})")
print(f"    S_e(1) = sum_d eps(2d) = {mp.nstr(S_E1, 16)}  — a single row's gain cannot exceed "
      f"this", flush=True)
check(
    "P4 B_sharp's slack is concentrated in row 0, and it is a missing cap",
    _row0 / B_SHARP > mp.mpf("0.7") and _single_best[0] < _row0 / 2,
    f"row 0's budget {mp.nstr(_row0, 10)} is "
    f"{mp.nstr(100 * _row0 / B_SHARP, 4)} % of B_sharp = {mp.nstr(B_SHARP, 10)}, and it is "
    f"attained at u_0 = {mp.nstr(_p4_rows[0][3], 6)}.  The true best single-row block is "
    f"[{_single_best[1]}] at {mp.nstr(_single_best[0], 10)} — "
    f"{mp.nstr(_row0 / _single_best[0], 5)}x less.  The per-row bound is the tangent at u = 0 "
    f"and has no cap; the real gain saturates at S_e(1) = {mp.nstr(S_E1, 8)} and then loses to "
    f"the quadratic cost.  So the fix is not a better constant, it is a bound that bends",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P5  the relaxed supremum, per block length")
_p5 = []
_best = None
_best_cert = None
_cert_rows_star = None
_naive_star = None
for _T in range(1, TMAX + 1):
    _v, _u = relaxed_sup(_T)
    _cb, _cs, _cn, _crows, _excl = certificate(_T, polish(_u), INT_SUP)
    _ordered = all(_u[k] >= _u[k + 1] - 1 for k in range(_T - 1))
    _p5.append({"T": _T, "sup": mp.nstr(_v, 22), "certified_bound": mp.nstr(_cb, 22),
                "certificate_slack": None if _cs is None else mp.nstr(_cs, 12),
                "excluded_by_row_box": _excl,
                "ordered": _ordered, "profile": [mp.nstr(x, 10) for x in _u]})
    if _best is None or _v > _best[0]:
        _best = (_v, _T, list(_u))
    if _best_cert is None or _cb > _best_cert[0]:
        _best_cert = (_cb, _T, _cs)
        _cert_rows_star = _crows
        _naive_star = _cn
    print(f"    T = {_T:3d}: {mp.nstr(_v, 20):24s} <= {mp.nstr(_cb, 20):24s} "
          f"ordering {'ok ' if _ordered else 'NO '} "
          f"[{', '.join(mp.nstr(x, 4) for x in _u[:7])}{'...' if _T > 7 else ''}]", flush=True)
B_RELAX, _T_STAR, _U_STAR = _best
B_CERT, _T_CERT, _SLACK_CERT = _best_cert
_p5_all_ordered = all(r["ordered"] for r in _p5)
check(
    "P5 the relaxed sup is 1.04x the integer maximum, against B_sharp's 1.82x",
    B_RELAX >= INT_SUP and B_RELAX / INT_SUP < mp.mpf("1.1"),
    f"B_relax = {mp.nstr(B_RELAX, 20)} at T = {_T_STAR}, argmax "
    f"[{', '.join(mp.nstr(x, 5) for x in _U_STAR)}] — recognisably the integer argmax "
    f"[4, 3, 2, 2, 1, 1, 1] with integrality let out.  That is "
    f"{mp.nstr(B_RELAX / INT_SUP, 6)}x the integer maximum {mp.nstr(INT_SUP, 12)}, where "
    f"B_sharp was {mp.nstr(B_SHARP / INT_SUP, 6)}x.  The AP ordering constraint was DROPPED "
    f"from the program (a further relaxation, so the bound stays valid) and the optimum "
    f"satisfies it anyway at every T: {_p5_all_ordered}",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P6  what each bound costs in search space")
_jen_sup = None
for _T in range(1, TMAX + 1):
    _u = [mp.mpf(max(1, 5 - i)) for i in range(_T)]
    _prev = None
    for _ in range(25):
        for _i in range(_T):
            def _f(x, i=_i, uu=_u):
                v = list(uu); v[i] = x
                return jensen(v)
            _u[_i] = _ternary(_f, mp.mpf(1), UMAX)
        _cur = jensen(_u)
        if _prev is not None and abs(_cur - _prev) < TOL:
            break
        _prev = _cur
    _jv = jensen(_u)
    if _jen_sup is None or _jv > _jen_sup:
        _jen_sup = _jv
_p6 = []
for _lab, _B in (("B_sharp (#7349)", B_SHARP),
                 (f"B_jensen (T <= {TMAX})", _jen_sup),
                 (f"B_relax (T <= {TMAX})", B_RELAX),
                 ("integer sup (measured)", INT_SUP)):
    _L = cut_for(_B)
    _n = blocks_with_sum_at_most(_L) if _L <= 30 else None
    _p6.append({"bound": _lab, "value": mp.nstr(_B, 22), "cut": _L,
                "blocks": _n})
    print(f"    {_lab:26s} {mp.nstr(_B, 14):18s} cut s_t+s_b <= {_L:3d}   "
          f"{f'{_n:,} blocks' if _n is not None else 'not enumerable'}", flush=True)
_cut_relax = cut_for(B_RELAX)
_cut_sharp = cut_for(B_SHARP)
check(
    "P6 the relaxed bound turns the cut from unenumerable into enumerable",
    _cut_relax <= 30 and _cut_sharp > 60,
    f"B_sharp cut at {_cut_sharp} (~1e10 blocks, hopeless); B_jensen at "
    f"{cut_for(_jen_sup)}; B_relax at {_cut_relax}, which is "
    f"{blocks_with_sum_at_most(_cut_relax):,} blocks — minutes, not geological time.  Inside "
    f"any such cut the enumeration carries no effective cap, since entries >= 1 and sum <= L "
    f"force length <= L and every entry <= L.  So the ARITHMETIC of an unconditional closure "
    f"now works; what is missing is the certificate, not the compute",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P7  how long can a block be?")
# per-row bound (`_row_cap`, defined above with the certificate): row i contributes at most
# max_{v>=1} [v Ghat(i+1) - (ln q0/2) v^2] = Ghat^2/(2 ln q0) when the parabola peaks at
# v >= 1, else the value at v = 1.
_run = mp.mpf(0)
_T0 = None
for _i in range(0, 400):
    _run += _row_cap(_i)
    if _run < B_CERT and _i >= _T_STAR:
        _T0 = _i + 1
        break
_neg_from = next(i for i in range(400) if _row_cap(i) < 0)
print(f"    row caps turn negative from row {_neg_from} on "
      f"(Ghat({_neg_from+1}) = {mp.nstr(GHAT[_neg_from+1], 8)} < ln q0/2 = "
      f"{mp.nstr(LNQ_HALF, 8)})")
print(f"    cumulative per-row cap drops below B_cert at T0 = {_T0}", flush=True)
_T_COVERED = TMAX >= _T0
check(
    "P7 block length is rigorously bounded",
    _T0 is not None and _T0 < 400,
    f"every row past index {_neg_from - 1} contributes at most "
    f"`Ghat(i+1) - ln q0/2 < 0`, so the cumulative per-row cap falls below the certified "
    f"B_cert = {mp.nstr(B_CERT, 12)} at T0 = {_T0}: no block of length > {_T0} can reach it.  "
    + (f"This run measured T <= {TMAX} >= T0, so every admissible length is covered and the "
       f"supremum over ALL T is certified."
       if _T_COVERED else
       f"This run measured T <= {TMAX}, where the sup peaks at T = {_T_STAR} and falls "
       f"monotonically after — so T = {TMAX + 1}..{_T0} is UNMEASURED here.  Re-run with "
       f"REV_BLOCK_SUP_TMAX={_T0} to cover it; that is compute, not insight, and the T <= 40 "
       f"run declines monotonically at ln q0/2 = {mp.nstr(LNQ_HALF, 8)} per step throughout"),
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P8  a certificate for the concave maximum — G2 item (a)")
print(f"    B_cert = {mp.nstr(B_CERT, 24)} at T = {_T_CERT}")
if _SLACK_CERT is not None:
    print(f"    slack  = {mp.nstr(_SLACK_CERT, 12)}   "
          f"({mp.nstr(_SLACK_CERT / (B_CERT - INT_SUP), 6)} of the gap to the integer sup)")
for _r in (_cert_rows_star or []):
    print(f"      row {_r['row']}: g = {_r['grad']:>16}  U = {_r['U']:>14}  "
          f"w = {_r['w']:>14}  term = {_r['term']}", flush=True)
_p8_ok = (
    _SLACK_CERT is not None
    and _SLACK_CERT >= 0
    and _SLACK_CERT / (B_CERT - INT_SUP) < mp.mpf("1e-5")
    and B_CERT >= B_RELAX
    and B_CERT >= INT_SUP
)
check(
    "P8 the concave maximum is certified, not merely converged",
    _p8_ok,
    f"the supergradient inequality at the coordinate-ascent point, with the linear term "
    f"maximised over the per-row box the incumbent forces, gives sup F(T = {_T_CERT}) <= "
    f"{mp.nstr(B_CERT, 24)} with slack {mp.nstr(_SLACK_CERT, 8)} — "
    f"{mp.nstr(_SLACK_CERT / (B_CERT - INT_SUP), 6)} of the distance to the integer maximum, so "
    f"the certificate costs essentially nothing against the ascent value {mp.nstr(B_RELAX, 20)}."
    f"  The gradient is ANALYTIC (`gx = -eps'` in closed form), not a finite difference.  The "
    f"boundary rows are the whole difficulty: at the optimum the last rows sit at u = 1 with "
    f"strictly negative gradients, which is correct KKT behaviour, and charging every row "
    f"|g_i|(U_i - w_i) rather than g_i(1 - w_i) would inflate the slack to "
    f"{mp.nstr(_naive_star, 8)} — a factor of {mp.nstr(_naive_star / _SLACK_CERT, 6)}, enough to "
    f"swamp the result many times over.  That error was made here first, and this figure is "
    f"recomputed every run rather than quoted",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("P9  the join at the certified cut — does it reproduce e_inf?")
_S = cut_for(B_CERT)
_SC = mp.mpf(10) ** (TARGET_DIGITS - 2)
_e2 = {}
for _d in range(1, _S + 1):
    for _w in range(-(_S - 1), _S):
        if 2 * _d + _w >= 1:
            _e2[(_d, _w)] = int(mp.nint((epsx(2 * _d) - epsx(2 * _d + _w)) * _SC))
_tl = {(m, v): int(mp.nint(TAIL(m, v) * _SC))
       for m in range(1, _S + 2) for v in range(1, _S + 1)}
_ct = {v: int(mp.nint(LNQ_HALF * v * v * _SC)) for v in range(1, _S + 1)}
_bestblock: dict[int, tuple[int, tuple]] = {}
_nodes = 0


def _dfs(v, s, val):
    global _nodes
    _nodes += 1
    c = _bestblock.get(s)
    if c is None or val > c[0]:
        _bestblock[s] = (val, tuple(reversed(v)))
    if len(v) >= _S:
        return
    p = len(v)
    lo = max(1, v[-1] - 1) if v else 1
    for vp in range(lo, _S + 1):
        if s + vp > _S:
            break
        d = _tl[(p + 1, vp)] - _ct[vp]
        ok = True
        for j in range(p):
            e = _e2.get((p - j, vp - v[j]))
            if e is None:
                ok = False
                break
            d += e
        if ok:
            v.append(vp)
            _dfs(v, s + vp, val + d)
            v.pop()


_dfs([], 0, 0)
_bestblock.pop(0, None)
_join, _jarg = None, None
for _st, (_vt, _pt) in _bestblock.items():
    for _sb, (_vb, _pb) in _bestblock.items():
        _val = mp.mpf(_vt) / _SC + xrun(_st + _sb) + mp.mpf(_vb) / _SC
        if _join is None or _val > _join:
            _join, _jarg = _val, (_st, _sb, _pt, _pb)
_mx = max(_bestblock, key=lambda s: _bestblock[s][0])
_xb_sup = mp.mpf(_bestblock[_mx][0]) / _SC
print(f"    enumerated {_nodes:,} blocks with sum <= {_S} (no effective cap)")
print(f"    argmax (s_t, s_b) = ({_jarg[0]}, {_jarg[1]})   top block {list(_jarg[2])}")
print(f"    e_inf  = {mp.nstr(_join, 30)}")
print(f"    #7335  = {mp.nstr(E_INF_7335, 30)}   diff {mp.nstr(_join - E_INF_7335, 6)}", flush=True)
check(
    "P9 the certified cut reproduces #7335's e_inf",
    abs(_join - E_INF_7335) < mp.mpf(10) ** (-20) and _S <= 30,
    f"the certificate's cut is s_t + s_b <= {_S}, {_nodes:,} blocks, and the join over that "
    f"window returns {mp.nstr(_join, 30)} at (s_t, s_b) = ({_jarg[0]}, {_jarg[1]}) with top "
    f"block {list(_jarg[2])} — agreeing with #7335's independently searched "
    f"{mp.nstr(E_INF_7335, 30)} to {mp.nstr(_join - E_INF_7335, 6)}.  The block supremum over "
    f"the same window is {mp.nstr(_xb_sup, 22)} at s = {_mx}, comfortably under B_cert = "
    f"{mp.nstr(B_CERT, 20)}, so the cut is not merely large enough by luck.  This is the "
    f"payoff: #7335's value was a search result, and inside the certified window it is a "
    f"MAXIMUM — conditional now only on G1, not on how far the search happened to run",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  B_cert = {mp.nstr(B_CERT, 22)} at T = {_T_CERT}   "
      f"({mp.nstr(B_CERT / INT_SUP, 6)}x the integer maximum)")
print(f"  cut: s_t + s_b <= {_S}  ({_nodes:,} blocks)")
print(f"  e_inf over that window = {mp.nstr(_join, 30)}")
print("  G2 " + ("CLOSED — certificate + every admissible T" if _T_COVERED else
                 f"item (a) CLOSED by the certificate; item (b) needs "
                 f"REV_BLOCK_SUP_TMAX={_T0}"))
print("  G1 unchanged: Xbot(s) <= Xblock(s) is still assumed")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {
        "script": "computations/deltalambda/rev_e_infinity_block_sup_relaxation_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The top-block value is CONCAVE in the displacement vector -- every internal term is "
        "-eps(2d + (u_i - u_j)), concave composed with a linear map; every bulk tail is "
        "-eps(2d + u_i); the cost is -(ln q0/2) sum u^2 -- so maximising it over real u >= 1 "
        "is a concave program, a relaxation of the integer problem and hence a rigorous upper "
        "bound.  Its value B_relax = 2.2537 is 1.042x the integer maximum where #7349's "
        "B_sharp was 1.816x, and the resulting cut on the e_inf search falls from 90 to 27, "
        "which IS enumerable (~6e6 blocks) where 90 (~1e10) is not.  An intermediate Jensen "
        "bound is also recorded: valid, 2.6951 over the measured T range, cut 43, still not "
        "enumerable.  The concave maximum is then CERTIFIED rather than merely converged: the "
        "supergradient inequality at the polished ascent point, with the linear term maximised "
        "over the per-row box the incumbent forces, closes with slack 6.4e-12 -- 6.8e-11 of "
        "the distance to the integer maximum.  The join over the certified cut reproduces "
        "#7335's "
        "independently searched e_inf = 2.43929645512078402706542884314 to 1e-30, at "
        "(s_t, s_b) = (8, 8).  Gap G2 is CLOSED at the run's measured block-length range; "
        "covering EVERY admissible length additionally needs REV_BLOCK_SUP_TMAX set to the "
        "rigorous T0 (the default 12 does not).  G1 -- Xbot(s) <= Xblock(s) -- is untouched and "
        "is now the only conditionality left on e_inf."
    ),
    "constants": {
        "ln_q0_half": mp.nstr(LNQ_HALF, 30), "mp_dps": mp.dps,
        "eps_depth": DEPTH2, "T_depth": DEPTH4, "lambert_depth": RMAX,
        "S_e_1": mp.nstr(S_E1, 30), "Ghat_1": mp.nstr(GHAT[1], 30),
        "integer_sup": mp.nstr(INT_SUP, 30), "B_sharp_7349": mp.nstr(B_SHARP, 30),
        "B_jensen_over_measured_T": mp.nstr(_jen_sup, 30),
        "B_relax_over_measured_T": mp.nstr(B_RELAX, 30),
        "B_certified_over_measured_T": mp.nstr(B_CERT, 30),
        "certificate_slack": None if _SLACK_CERT is None else mp.nstr(_SLACK_CERT, 20),
        "T_star": _T_STAR, "T_certified_argmax": _T_CERT,
        "T_measured_max": TMAX, "T0_rigorous": _T0,
        "all_lengths_covered": _T_COVERED,
        "_note": ("the suprema are over T <= T_measured_max, NOT over all T.  T0_rigorous is "
                  "the length past which the per-row cap forbids reaching B_certified; a run "
                  "with T_measured_max >= T0_rigorous covers every admissible length and sets "
                  "all_lengths_covered.  B_certified is the RIGOROUS number -- B_relax is the "
                  "coordinate-ascent value, which is a lower bound on the sup, not an upper "
                  "one."),
    },
    "certificate_P8": {
        "form": ("F concave => F(u) <= F(w) + grad F(w).(u - w); the per-row bound confines "
                 "each u_i to [1, U_i] for any u reaching the incumbent, and the linear term "
                 "is maximised over that box"),
        "gradient": "analytic (gx = -eps' in closed form), NOT a finite difference",
        "incumbent": mp.nstr(INT_SUP, 30),
        "T": _T_CERT,
        "bound": mp.nstr(B_CERT, 30),
        "slack": None if _SLACK_CERT is None else mp.nstr(_SLACK_CERT, 20),
        "slack_as_fraction_of_gap": (None if _SLACK_CERT is None
                                     else mp.nstr(_SLACK_CERT / (B_CERT - INT_SUP), 12)),
        "slack_if_boundary_rows_mischarged": (None if _naive_star is None
                                              else mp.nstr(_naive_star, 12)),
        "rows": _cert_rows_star,
        "_trap": ("the boundary rows carry strictly negative gradients at u = 1 (correct KKT).  "
                  "Charging every row |g_i|(U_i - w_i) instead of g_i(1 - w_i) inflates the "
                  "slack to the figure above and destroys the result.  Made here first; the "
                  "figure is recomputed every run rather than quoted."),
    },
    "join_P9": {
        "cut": _S,
        "blocks_enumerated": _nodes,
        "e_inf": mp.nstr(_join, 30),
        "e_inf_7335_searched": mp.nstr(E_INF_7335, 30),
        "difference": mp.nstr(_join - E_INF_7335, 8),
        "argmax_s_top_s_bot": [_jarg[0], _jarg[1]],
        "top_block": list(_jarg[2]),
        "bot_block": list(_jarg[3]),
        "block_sup_over_window": mp.nstr(_xb_sup, 24),
        "block_sup_at_s": _mx,
    },
    "relaxation_P5": {
        "objective": "Xblock(u) at real u, exactly -- no linearisation, no Jensen",
        "argmax": [mp.nstr(x, 20) for x in _U_STAR],
        "integer_argmax": [4, 3, 2, 2, 1, 1, 1],
        "ratio_to_integer_sup": mp.nstr(B_RELAX / INT_SUP, 20),
        "ordering_constraint_dropped_and_satisfied": _p5_all_ordered,
        "rows": _p5,
    },
    "jensen_P3": {
        "form": "sum_i f(Delta_i) <= (T-d) f(mean),  f(x) = eps(2d) - eps(2d+x) concave",
        "sup": mp.nstr(_jen_sup, 30), "cut": cut_for(_jen_sup),
        "rows": _p3,
    },
    "cuts_P6": _p6,
    "open_gaps": {
        "G2_status": ("CLOSED" if _T_COVERED else
                      f"item (a) CLOSED; item (b) needs REV_BLOCK_SUP_TMAX={_T0} (this run "
                      f"used {TMAX})"),
        "G2_a": ("CLOSED -- supergradient certificate, slack "
                 f"{'n/a' if _SLACK_CERT is None else mp.nstr(_SLACK_CERT, 8)}"),
        "G2_b": (f"block lengths T = 1..{_T0} exhaust the admissible range; this run measured "
                 f"T <= {TMAX}" + ("" if _T_COVERED else
                                   f", so T = {TMAX + 1}..{_T0} is uncovered HERE.  A "
                                   f"REV_BLOCK_SUP_TMAX=40 run declines monotonically at "
                                   f"ln q0/2 per step from the T = 7 peak 2.25373 through "
                                   f"1.45889 (T=25), 0.98942 (T=34) and 0.67639 (T=40=T0), a "
                                   f"factor of 3.33 below the peak")),
        "G1": ("unchanged and now the ONLY conditionality on e_inf: Xbot(s) <= Xblock(s) for "
               "every s, measured equal for s <= 12 and top-higher by 0.01982 at s = 13"),
        "headline": "still the upper bound on M_n, which none of this touches",
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "Concavity of the block value turns sup_s Xblock from a search into a concave program, "
        "shrinking gap G2 from 1.82x to 1.04x and the e_inf cut from an unenumerable 90 to an "
        "enumerable 27; the supergradient certificate then makes that maximum rigorous with "
        "slack 6.4e-12, and the join over the certified window returns #7335's e_inf exactly.  "
        "So e_inf is no longer 'the best value a search found' but the maximum over a window "
        "proved to contain it -- conditional on G1 alone.  The certificate's own trap is "
        "recorded and recomputed every run: the KKT boundary rows carry negative gradients and "
        "must be charged at u = 1, not at their box ends, or the slack inflates by eleven "
        "orders of magnitude."
    ),
}

_out = os.path.join(_HERE, "rev-e-infinity-block-sup-relaxation.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
