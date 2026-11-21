#!/usr/bin/env python3
r"""
rev_e_infinity_search_reduction_probe.py — the `e_inf` search is COERCIVE, and the greedy
argument that would have closed it is REFUTED (qou-hok7)

PR #7335 reduced `e_inf` to a maximisation over three `k`-free pieces,

    e_inf  =  max over (s_t, s_b) of  [ Xblock(s_t) + Xrun(s_t + s_b) + Xbot(s_b) ] ,

and #7349 turned `Xblock` and `Xrun` into closed-form series.  What neither did is close the
**search**: `(s_t, s_b) = (8, 8)` and the block `[3,2,1,1,1]` are still outputs of an
enumeration over a capped shape class, and nothing proved the caps non-binding in principle.

This probe attacks that, and the first thing it produces is a **negative**.

## The obvious argument is unsound, and it is worth saying why

`Xrun` loses `ln q0 / 2 = 0.0521703...` per unit of run length, so the natural move is: find the
first `s` at which the block's marginal gain `Xblock(s+1) - Xblock(s)` drops below that, and
stop.  That is a greedy / first-crossing exchange argument, and it needs `Xblock` to have
decreasing increments.

**It does not.**  Measured, the marginal drops below `ln q0/2` at `s = 9` (0.02854) and
`s = 10` (0.03538), then comes back **above** at `s = 11` (0.07983) before falling for good at
`s = 12`.  A first-crossing rule stops at `s = 9` and misses `s = 11..14` entirely — including
`s = 14`, which is where `Xblock` actually peaks.  So `Xblock` is not discretely concave and no
greedy rule closes this search.  Recorded because the argument is the one a reader reaches for.

## What does work: coercivity

`eps(m) = -log(1 - q0^(-2m))` is convex and decreasing, so for **every** sign of `D`

    eps(2d) - eps(2d + D)  <=  |eps'(2d)| * D  =:  g(d) * D ,

the two cases being `int_a^{a+D}|eps'| <= D|eps'(a)|` for `D > 0` and
`-int_{a+D}^{a}|eps'| <= -|D||eps'(a)|` for `D < 0`, both because `|eps'|` is decreasing.  That
single inequality linearises the whole pair sum.  Summing it over pairs telescopes — the
distance-`d` pairs of a block contribute `(top d entries) - (bottom d entries)` — and with
`top_d <= sqrt(d * N)` (Cauchy-Schwarz, `N = sum v^2`), `bottom_d >= d`, and the bulk tails
bounded by `sum_j TAIL[j+1][v_j] <= sum_{m>=1} sum_{d>=m} eps(2d) = sum_d d eps(2d) =: S_1`:

    Xblock(u)  <=  S_1 - G_1 + G_half * sqrt(N)  -  (ln q0 / 2) * N ,

    G_1 = sum_d d g(d) ,   G_half = sum_d sqrt(d) g(d) .

The right side is a downward parabola in `sqrt(N)`, so it is **bounded above uniformly in the
block's length and entries** — which is what makes the search finite at all:

    Xblock(u)  <=  B_rig  :=  S_1 - G_1 + G_half^2 / (2 ln q0)   for EVERY valid block.

**Summing by ROW instead of by pair distance is 2.7x better, and more legible.**  The
Cauchy-Schwarz step above is applied once per distance `d`, so it charges the same top rows
again at every `d`.  Collect the linearisation by row and it telescopes to one coefficient per
row, with a reading: row `i` counted from the free top edge only ever sees distances `>= i + 1`
on its way down to the bulk, so the most it can gain per unit of displacement is

    Ghat(m)  :=  sum_{d >= m} |eps'(2d)| ,     coefficient of row i  =  Ghat(i + 1) .

Each row is then a downward parabola in its own `u_i` and the whole thing maximises termwise:

    Xblock(u)  <=  sum_i [ u_i Ghat(i+1) - (ln q0/2) u_i^2 ]  <=  B_sharp
    B_sharp    :=  sum_{m>=1} Ghat(m)^2 / (2 ln q0)  =  3.92139923021415319 .

Both bounds are checked; the per-row one is roughly 40x tighter at the argmax.  It is still
crude in absolute terms — 1.82x the measured maximum — and crudeness costs: the unconditional
cut it gives is `s_t + s_b <= 90`, finite but far past any feasible enumeration.  The practical
cut uses the measured `B` instead and is therefore conditional on it.

## What this establishes, and what it does not

**Establishes.** The maximisation is coercive: only finitely many `(s_t, s_b)` can win, by an
inequality chain with no fitted constant in it.  And within the *measured* cut the search is
genuinely exhaustive — at `s <= 23` a block with entries `>= 1` cannot have length `> 23` or an
entry `> 23`, so running the enumeration at `UMAX = TMAX = SMAX = 23` has **no cap at all**,
and the answer is `(8, 8)` with `Xbot` replaced by `Xblock`.

**Does not.** Two gaps, and they are now sharp enough to name:

  G1  `Xbot(s) <= Xblock(s)` for every `s`.  #7335's E7 measured the two tables EQUAL for
      `s <= 12` and the top higher by 0.01982 at `s = 13`; beyond that it is unmeasured, and
      nothing here proves it.  The join used below substitutes `Xblock` for `Xbot`, which is an
      upper bound only if G1 holds.

  G2  `sup_s Xblock(s) = 2.1598023761182859616035` (attained at `s = 14`).  Measured over
      `s <= 26` with the caps lifted to 24/12 and the argmax using at most length 18 and entry
      4 — non-binding — but not proved.  `B_sharp = 3.9214` bounds the sup rigorously at 1.82x,
      which is close enough to be interesting and not close enough to substitute: it cuts at
      `s_t + s_b <= 90` where the measured `B` cuts at 23, and 90 is not enumerable.  Closing
      G2 is therefore the same thing as tightening `B_sharp` by a factor under two — which is
      the most tractable-looking open item in this file.

Neither gap is the arc's headline open problem, which remains the upper bound on `M_n`.

## Checks

  S1  the per-term convexity inequality holds on a wide grid, both signs of `D`
  S2  both assembled bounds hold on every block of the enumerated class, and the per-row
      route is far tighter — which locates the loss in the Cauchy-Schwarz step
  S3  the uniform bound is finite and explicit, and gives an unconditional cut on `s_t + s_b`
  S4  the marginal is NOT monotone — it re-crosses `ln q0/2` upward at `s = 11`
  S5  `Xblock` peaks at `s = 14`, but the join's argmax is `s = 8`: the block gives up 0.194
      of its own maximum to shorten the run by 12
  S6  the join over the reduced space is `(8, 8)` and reproduces #7335's `e_inf` exactly
  S7  at `s <= 23` the enumeration carries no effective cap, and lifting the nominal caps to
      24/12 leaves every value at `s <= 23` unchanged
  S8  the scaled-integer tables the enumeration runs on agree with a direct mpmath evaluation

Proton-pinned; mpmath builds three tables, then the enumeration is exact integer arithmetic at
scale 1e-40.  No float64.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/BraidKnot/EdgeDecoupling.lean
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
LNQ = mp.log(Q0)
LNQ_HALF = LNQ / 2
T2 = Q0 ** 2
LNT2 = mp.log(T2)

SCALE_DIGITS = 40
SCALE = mp.mpf(10) ** SCALE_DIGITS

# Series depths derived from the decay rates, not chosen: eps(2d) ~ q^(-4d) and
# eps(m) ~ q^(-2m), so pushing a tail below 1e-55 needs these many terms.
TARGET_DIGITS = 55
_LN10 = mp.log(10)
DEPTH2 = int(mp.ceil(TARGET_DIGITS * _LN10 / (2 * LNQ))) + 5
DEPTH4 = int(mp.ceil(TARGET_DIGITS * _LN10 / (4 * LNQ))) + 5
TOL = mp.mpf(10) ** (-(TARGET_DIGITS - 5))

# The coercivity cut is taken against #7335's searched value, which this probe does not recompute.
# READ from the witness that searches it (rev-e-infinity-edge-limit, e_infinity.value)
# rather than typed (witness-value copy ratchet).
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "rev-e-infinity-edge-limit.witness.json"), encoding="utf-8") as _fh:
    E_INF_7335 = mp.mpf(json.load(_fh)["e_infinity"]["value"])

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def eps(m: int) -> mp.mpf:
    return -mp.log(1 - T2 ** (-m)) if m > 0 else mp.mpf(0)


def g(d: int) -> mp.mpf:
    """`|eps'(2d)| = (ln t) t^(-2d) / (1 - t^(-2d))`, `t = q0^2`.  Decreasing in `d`."""
    x = T2 ** (-2 * d)
    return LNT2 * x / (1 - x)


S_1 = mp.fsum(d * eps(2 * d) for d in range(1, DEPTH2))
G_1 = mp.fsum(d * g(d) for d in range(1, DEPTH2))
G_HALF = mp.fsum(mp.sqrt(d) * g(d) for d in range(1, DEPTH2))
N_STAR = (G_HALF / LNQ) ** 2
B_RIG = S_1 - G_1 + G_HALF ** 2 / (2 * LNQ)

T_KERNEL = [2 * eps(2 * d) - eps(2 * d - 1) - eps(2 * d + 1) for d in range(1, DEPTH4)]


def xrun(ell: int) -> mp.mpf:
    """#7349's closed form: `sum_d min(d, ell) T(d) - (ln q0 / 2) ell`."""
    return mp.fsum(min(d, ell) * T_KERNEL[d - 1] for d in range(1, DEPTH4)) - LNQ_HALF * ell


GHAT = {m: mp.fsum(g(d) for d in range(m, DEPTH2)) for m in range(1, DEPTH2)}
B_SHARP = mp.fsum(GHAT[m] ** 2 for m in range(1, DEPTH2)) / (2 * LNQ)


def bound_cs(u) -> mp.mpf:
    """`S_1 - G_1 + G_half sqrt(N) - (ln q0/2) N`, the Cauchy-Schwarz route."""
    N = sum(x * x for x in u)
    return S_1 - G_1 + G_HALF * mp.sqrt(N) - LNQ_HALF * N


def bound_row(u) -> mp.mpf:
    """`sum_i [ u_i Ghat(i+1) - (ln q0/2) u_i^2 ]`, the per-row route.

    Summing the linearisation by ROW rather than by pair distance telescopes to a single
    coefficient per row, and that coefficient has a reading: row `i` counted from the free top
    edge only ever sees distances `>= i + 1` on its way down to the bulk, so the most it can
    gain per unit of displacement is `Ghat(i+1) = sum_{d >= i+1} |eps'(2d)|`.  Each row is then
    a downward parabola in its own `u_i` and the whole thing maximises termwise.
    """
    return mp.fsum(u[i] * GHAT[i + 1] - LNQ_HALF * u[i] * u[i] for i in range(len(u)))


# --------------------------------------------------------------------------------------------
# the block enumeration, built BOTTOM-UP so every prefix is itself a complete block
#
# `v` runs bottom-to-top (`v_j = u_{T-1-j}`), which is what makes the value incremental: the
# bulk is BELOW the block, so extending upward leaves every existing row's distance to the bulk
# alone.  The AP ordering `u_{i+1} <= u_i + 1` becomes `v_{j+1} >= v_j - 1`.
# --------------------------------------------------------------------------------------------
def _tables(tmax: int, umax: int):
    e2 = {}
    for d in range(1, tmax + 1):
        for w in range(-(umax - 1), umax):
            if 2 * d + w >= 1:
                e2[(d, w)] = int(mp.nint((eps(2 * d) - eps(2 * d + w)) * SCALE))
    tail = {}
    for m in range(1, tmax + 2):
        for v in range(1, umax + 1):
            tail[(m, v)] = int(mp.nint(
                mp.fsum(eps(2 * d) - eps(2 * d + v) for d in range(m, DEPTH2)) * SCALE))
    cost = {v: int(mp.nint(LNQ_HALF * v * v * SCALE)) for v in range(1, umax + 1)}
    return e2, tail, cost


def block_table(tmax: int, umax: int, smax: int):
    """`Xblock[s] -> (scaled value, profile top-to-bottom)`, exhaustive over the class."""
    e2, tail, cost = _tables(tmax, umax)
    best: dict[int, tuple[int, tuple]] = {}
    nodes = 0

    def dfs(v: list, s: int, val: int):
        nonlocal nodes
        nodes += 1
        cur = best.get(s)
        if cur is None or val > cur[0]:
            best[s] = (val, tuple(reversed(v)))
        if len(v) >= tmax:
            return
        p = len(v)
        lo = max(1, v[-1] - 1) if v else 1
        for vp in range(lo, umax + 1):
            if s + vp > smax:
                break
            delta = tail[(p + 1, vp)] - cost[vp]
            ok = True
            for j in range(p):
                e = e2.get((p - j, vp - v[j]))
                if e is None:
                    ok = False
                    break
                delta += e
            if ok:
                v.append(vp)
                dfs(v, s + vp, val + delta)
                v.pop()

    dfs([], 0, 0)
    best.pop(0, None)
    return best, nodes


def sc(x: int) -> mp.mpf:
    return mp.mpf(x) / SCALE


# --------------------------------------------------------------------------------------------
print("the e_inf search is coercive — and the greedy route to it is refuted")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  mp.dps = {mp.dps}")
print(f"  ln q0 / 2 = {mp.nstr(LNQ_HALF, 24)}   (the run's marginal cost per unit)")
print(f"  series depths derived from the decay rates: eps {DEPTH2}, T {DEPTH4}")
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S1  eps(2d) - eps(2d + D) <= g(d) D, for EVERY sign of D")
_s1_worst = None
_s1_n = 0
for _d in range(1, 31):
    for _D in range(-(2 * _d - 1), 41):
        _s1_n += 1
        _slack = g(_d) * _D - (eps(2 * _d) - eps(2 * _d + _D))
        if _s1_worst is None or _slack < _s1_worst[0]:
            _s1_worst = (_slack, _d, _D)
print(f"    {_s1_n} (d, D) pairs, d <= 30, D from -(2d-1) to 40")
print(f"    minimum slack g(d)D - [eps(2d) - eps(2d+D)] = {mp.nstr(_s1_worst[0], 6)} "
      f"at d = {_s1_worst[1]}, D = {_s1_worst[2]}", flush=True)
check(
    "S1 the linearising inequality holds on both sides of D = 0",
    _s1_worst[0] >= 0,
    f"minimum slack {mp.nstr(_s1_worst[0], 6)} over {_s1_n} pairs, attained at D = "
    f"{_s1_worst[2]} where the two sides are equal by construction.  Both signs matter and they "
    f"are different arguments: for D > 0 it is `int_a^(a+D)|eps'| <= D|eps'(a)|`, for D < 0 it "
    f"is `-int_(a+D)^a |eps'| <= -|D||eps'(a)|`, and both hold because `|eps'|` is decreasing.  "
    f"Dropping the D < 0 case — keeping only `D^+` — is what makes the bound diverge: the "
    f"negative pair terms are exactly what stops a long alternating profile from collecting "
    f"g(1) per step at linear cost",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S2  the assembled bound, against the exact block value")
TMAX_C, UMAX_C, SMAX_C = 12, 8, 40
_tbl_c, _nodes_c = block_table(TMAX_C, UMAX_C, SMAX_C)
_e2c, _tailc, _costc = _tables(TMAX_C, UMAX_C)


def exact_block(u) -> mp.mpf:
    """The block value from the same tables the enumeration uses, as an mpf."""
    n = len(u)
    tot = 0
    for i in range(n):
        for j in range(i + 1, n):
            tot += _e2c[(j - i, u[i] - u[j])]
        tot += _tailc[(n - i, u[i])]
        tot -= _costc[u[i]]
    return sc(tot)


_s2_viol_cs = _s2_viol_row = 0
_s2_tight_cs = _s2_tight_row = None
for _s, (_val, _prof) in sorted(_tbl_c.items()):
    _v = sc(_val)
    _bc, _br = bound_cs(_prof), bound_row(_prof)
    if _v > _bc:
        _s2_viol_cs += 1
    if _v > _br:
        _s2_viol_row += 1
    if _s2_tight_cs is None or _bc - _v < _s2_tight_cs[0]:
        _s2_tight_cs = (_bc - _v, _s, _prof)
    if _s2_tight_row is None or _br - _v < _s2_tight_row[0]:
        _s2_tight_row = (_br - _v, _s, _prof)
print(f"    checked the argmax at each of {len(_tbl_c)} block sums (from {_nodes_c} enumerated "
      f"blocks)")
print(f"    Cauchy-Schwarz route: {_s2_viol_cs} violations, tightest slack "
      f"{mp.nstr(_s2_tight_cs[0], 8)} at {list(_s2_tight_cs[2])}")
print(f"    per-row route:        {_s2_viol_row} violations, tightest slack "
      f"{mp.nstr(_s2_tight_row[0], 8)} at {list(_s2_tight_row[2])}", flush=True)
check(
    "S2 both coercivity bounds hold, and the per-row one is far tighter",
    _s2_viol_cs == 0 and _s2_viol_row == 0 and _s2_tight_row[0] < _s2_tight_cs[0],
    f"0 violations of either bound over {len(_tbl_c)} per-sum maximisers drawn from "
    f"{_nodes_c} enumerated blocks.  Tightest slack {mp.nstr(_s2_tight_cs[0], 6)} for the "
    f"Cauchy-Schwarz route against {mp.nstr(_s2_tight_row[0], 6)} for the per-row one — a "
    f"factor {mp.nstr(_s2_tight_cs[0] / _s2_tight_row[0], 5)}, which locates the loss: it is "
    f"the Cauchy-Schwarz step `top_d <= sqrt(d N)`, applied once per distance, that counts the "
    f"same top rows over and over.  Summing by ROW instead never introduces it.  Both are "
    f"checked at the maximiser of each sum, which is where a bound is tightest",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S3  the rigorous uniform bounds and the unconditional cut")
print(f"    S_1     = sum_d d eps(2d)        = {mp.nstr(S_1, 24)}")
print(f"    G_1     = sum_d d g(d)           = {mp.nstr(G_1, 24)}")
print(f"    G_half  = sum_d sqrt(d) g(d)     = {mp.nstr(G_HALF, 24)}")
print(f"    Ghat(1) = sum_d g(d)             = {mp.nstr(GHAT[1], 24)}")
print(f"    B_rig   = S_1 - G_1 + G_half^2/(2 ln q0)  = {mp.nstr(B_RIG, 24)}")
print(f"    B_sharp = sum_m Ghat(m)^2 / (2 ln q0)     = {mp.nstr(B_SHARP, 24)}")
_thresh_rig = E_INF_7335 - 2 * B_RIG
_L_RIG = max(ell for ell in range(1, 4000) if xrun(ell) > _thresh_rig)
_thresh_sharp = E_INF_7335 - 2 * B_SHARP
_L_SHARP = max(ell for ell in range(1, 4000) if xrun(ell) > _thresh_sharp)
print(f"    unconditional cut, B_rig:   Xrun(ell) > {mp.nstr(_thresh_rig, 12):16s} "
      f"=>  s_t + s_b <= {_L_RIG}")
print(f"    unconditional cut, B_sharp: Xrun(ell) > {mp.nstr(_thresh_sharp, 12):16s} "
      f"=>  s_t + s_b <= {_L_SHARP}", flush=True)
# witness-copy-intentional: the measured maximum this probe computes later (_B_meas,
# stage G2); the S3 message quotes it before it is computed.
_G2_MEASURED_MAX = mp.mpf('2.1598023761182859616')
check(
    "S3 the maximisation is coercive: only finitely many (s_t, s_b) can win",
    mp.isfinite(B_SHARP) and _L_SHARP < _L_RIG,
    f"B_sharp = {mp.nstr(B_SHARP, 20)} bounds EVERY valid block, with no cap on its length or "
    f"its entries and no fitted constant anywhere in the chain.  Since Xrun falls linearly at "
    f"-ln q0/2 per unit, that forces s_t + s_b <= {_L_SHARP}.  This is the part that needs no "
    f"measurement: the search space is finite as a matter of the inequality, not of the table.  "
    f"The per-row route beats the Cauchy-Schwarz one by "
    f"{mp.nstr(B_RIG / B_SHARP, 5)}x ({mp.nstr(B_RIG, 8)} -> {mp.nstr(B_SHARP, 8)}, cut "
    f"{_L_RIG} -> {_L_SHARP}) and it is the more legible of the two: row i counted from the "
    f"free top edge only sees distances >= i+1 on its way to the bulk, so `Ghat(i+1)` is the "
    f"most it can gain per unit.  It is STILL NOT ENUMERABLE — {_L_SHARP} is far past any "
    f"feasible search, and {mp.nstr(B_SHARP / _G2_MEASURED_MAX, 4)}x the "
    f"measured maximum — so this settles finiteness and not the value",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S4  is the marginal monotone?  (the greedy argument's premise)")
_ss = sorted(_tbl_c)
_marg = [(s, sc(_tbl_c[s][0]) - sc(_tbl_c[s - 1][0])) for s in _ss if s - 1 in _tbl_c]
_below = [(s, m) for s, m in _marg if m < LNQ_HALF]
_first_below = _below[0][0] if _below else None
_re_cross = [(s, m) for s, m in _marg if _first_below is not None
             and s > _first_below and m >= LNQ_HALF]
for _s, _m in _marg:
    if 7 <= _s <= 14:
        print(f"    s = {_s:3d}  Xblock = {mp.nstr(sc(_tbl_c[_s][0]), 22):26s} "
              f"marginal {mp.nstr(_m, 16):20s} {'BELOW' if _m < LNQ_HALF else 'ABOVE'} "
              f"ln q0/2   {list(_tbl_c[_s][1])}", flush=True)
check(
    "S4 the marginal is NOT monotone — the greedy / first-crossing argument is refuted",
    len(_re_cross) > 0,
    f"the marginal first drops below ln q0/2 = {mp.nstr(LNQ_HALF, 12)} at s = {_first_below}, "
    f"then comes back ABOVE it at s = "
    f"{', '.join(str(s) for s, _ in _re_cross)} (largest re-crossing "
    f"{mp.nstr(max(m for _, m in _re_cross), 6)}, at s = "
    f"{max(_re_cross, key=lambda t: t[1])[0]}) before falling for good.  So Xblock is not "
    f"discretely concave, and a rule that stops at the first crossing stops at s = "
    f"{_first_below} and misses everything above it — including s = 14, where Xblock peaks.  "
    f"This is a REFUTATION of the natural argument, scope (a): it says the greedy route does "
    f"not close the search, not that no argument does",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S5  where Xblock peaks, and where the join puts it")
_s_peak = max(_ss, key=lambda s: _tbl_c[s][0])
_peak = sc(_tbl_c[_s_peak][0])
_at8 = sc(_tbl_c[8][0])
print(f"    Xblock peaks at s = {_s_peak}: {mp.nstr(_peak, 24)}  {list(_tbl_c[_s_peak][1])}")
print(f"    the join's argmax is at s = 8:  {mp.nstr(_at8, 24)}  {list(_tbl_c[8][1])}")
print(f"    the block gives up {mp.nstr(_peak - _at8, 16)} of its own maximum", flush=True)
check(
    "S5 the block does not sit at its own maximum — the run's cost moves it",
    _s_peak != 8 and _peak > _at8,
    f"Xblock peaks at s = {_s_peak} with {mp.nstr(_peak, 20)}, but the three-piece join puts "
    f"the top block at s = 8 with {mp.nstr(_at8, 20)} — {mp.nstr(_peak - _at8, 8)} below its "
    f"own best.  It buys that back on the run: s_t = 8 rather than {_s_peak} shortens ell by "
    f"{2 * (_s_peak - 8)} and Xrun by {mp.nstr(xrun(2 * _s_peak) - xrun(16), 8)}.  So neither "
    f"edge's shape can be read off its own table — which is the reason the search is over pairs "
    f"and not over each piece separately",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S6  the join over the reduced space, with Xbot := Xblock")
_B_meas = _peak
_thresh = E_INF_7335 - 2 * _B_meas
_L_CUT = max(ell for ell in range(1, 200) if xrun(ell) > _thresh)
print(f"    measured B = {mp.nstr(_B_meas, 24)} (s = {_s_peak})")
print(f"    cut: Xrun(ell) > e_inf - 2B = {mp.nstr(_thresh, 20)}  =>  s_t + s_b <= {_L_CUT}")
print(f"    Xrun({_L_CUT}) = {mp.nstr(xrun(_L_CUT), 20)},  "
      f"Xrun({_L_CUT + 1}) = {mp.nstr(xrun(_L_CUT + 1), 20)}")
# exhaustive inside the cut: sum <= L_CUT with entries >= 1 forces length <= L_CUT and
# entries <= L_CUT, so these caps are not caps.
_tbl_f, _nodes_f = block_table(_L_CUT, _L_CUT, _L_CUT)
_best_j, _arg_j = None, None
for _st, (_vt, _pt) in _tbl_f.items():
    for _sb, (_vb, _pb) in _tbl_f.items():
        _v = sc(_vt) + xrun(_st + _sb) + sc(_vb)
        if _best_j is None or _v > _best_j:
            _best_j, _arg_j = _v, (_st, _sb, _pt, _pb)
print(f"    enumerated {_nodes_f} blocks with no effective cap (TMAX = UMAX = SMAX = {_L_CUT})")
print(f"    argmax (s_t, s_b) = ({_arg_j[0]}, {_arg_j[1]});  "
      f"value = {mp.nstr(_best_j, 30)}")
print(f"    #7335 searched value = {mp.nstr(E_INF_7335, 30)}")
print(f"    difference = {mp.nstr(_best_j - E_INF_7335, 8)}", flush=True)
check(
    "S6 the upper-bound join is maximised at (8, 8) and equals #7335's e_inf",
    _arg_j[0] == 8 and _arg_j[1] == 8 and abs(_best_j - E_INF_7335) < mp.mpf("1e-28"),
    f"over every (s_t, s_b) surviving the cut, with Xbot replaced by Xblock, the maximum is "
    f"{mp.nstr(_best_j, 26)} at (8, 8) — #7335's value to {mp.nstr(_best_j - E_INF_7335, 4)}.  "
    f"Substituting Xblock for Xbot can only RAISE the join if Xbot <= Xblock (gap G1, measured "
    f"equal for s <= 12 and top-higher at s = 13), so under G1 this is an upper bound that is "
    f"ATTAINED at the incumbent — which closes the (s_t, s_b) search, conditional on G1 and on "
    f"B being the true supremum (gap G2).  It does not close it unconditionally, and the "
    f"conditionality is the whole of what is left here",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S7  are the caps binding?")
_tbl_w, _nodes_w = block_table(24, 12, 26)
_diff = [s for s in _tbl_f if s in _tbl_w and _tbl_w[s][0] != _tbl_f[s][0]]
_maxlen = max(len(_tbl_w[s][1]) for s in _tbl_w)
_maxent = max(max(_tbl_w[s][1]) for s in _tbl_w)
print(f"    widened run: TMAX = 24, UMAX = 12, SMAX = 26 ({_nodes_w} blocks)")
print(f"    argmax profiles use at most length {_maxlen} (cap 24) and entry {_maxent} (cap 12)")
print(f"    values differing from the uncapped run at s <= {_L_CUT}: {len(_diff)}", flush=True)
check(
    "S7 no cap is binding anywhere the answer depends on",
    len(_diff) == 0 and _maxlen < 24 and _maxent < 12,
    f"two independent enumerations agree at every s <= {_L_CUT}: one at TMAX = UMAX = SMAX = "
    f"{_L_CUT}, where the caps CANNOT bind (entries >= 1 and sum <= {_L_CUT} force length <= "
    f"{_L_CUT} and every entry <= {_L_CUT}), and one widened to 24/12.  The widened run's "
    f"argmax profiles reach length {_maxlen} and entry {_maxent}, both inside their caps.  "
    f"#7335's published caps were 8/6 and this is the check it could not make, since its "
    f"enumeration was over profiles rather than incremental",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("S8  the table evaluator against a direct mpmath one")


def exact_block_mpmath(u) -> mp.mpf:
    """The block value computed straight from `eps`, with no table and no rounding.

    Deliberately the slow route: every bulk tail is summed term by term to DEPTH2 in mpmath
    rather than looked up, and nothing passes through the 1e-40 integer scale.  It shares no
    code with the enumeration, so agreement checks the tables' construction — their truncation
    depth and their rounding — and not merely their use.
    """
    n = len(u)
    tot = mp.mpf(0)
    for i in range(n):
        for j in range(i + 1, n):
            tot += eps(2 * (j - i)) - eps(2 * (j - i) + u[i] - u[j])
        tot += mp.fsum(eps(2 * d) - eps(2 * d + u[i]) for d in range(n - i, DEPTH2))
    return tot - LNQ_HALF * sum(x * x for x in u)


_s8_probe = [_tbl_c[_s][1] for _s in (1, 2, 5, 8, 11, 14, 20)] + [(4, 3, 2, 2, 1, 1, 1)]
_s8 = []
for _u in _s8_probe:
    _a, _b = exact_block(_u), exact_block_mpmath(_u)
    _s8.append({"profile": list(_u), "table": mp.nstr(_a, 26), "direct": mp.nstr(_b, 26),
                "difference": mp.nstr(_a - _b, 6)})
    print(f"    {str(list(_u)):28s} table {mp.nstr(_a, 20):24s} diff {mp.nstr(_a - _b, 4)}",
          flush=True)
_s8_worst = max(abs(mp.mpf(r["difference"])) for r in _s8)
_scale_floor = mp.mpf(10) ** (-SCALE_DIGITS) * 200
check(
    "S8 the scaled-integer tables agree with a direct mpmath evaluation",
    _s8_worst < _scale_floor,
    f"{len(_s8)} profiles including the argmax {list(_tbl_c[8][1])} and the peak "
    f"{list(_tbl_c[14][1])}; worst difference {mp.nstr(_s8_worst, 4)} against a floor of "
    f"{mp.nstr(_scale_floor, 3)} — the 1e-{SCALE_DIGITS} integer scale times the number of "
    f"rounded table entries a profile of this size touches.  The enumeration is fast because it "
    f"looks values up and adds integers; this confirms the lookup tables were built right, "
    f"which the enumeration cannot check on its own since it uses them for everything",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  e_inf = {mp.nstr(_best_j, 30)}  at (s_t, s_b) = (8, 8)")
print(f"  reduced search space: s_t + s_b <= {_L_CUT} (measured B = {mp.nstr(_B_meas, 12)}), "
      f"<= {_L_SHARP} (rigorous B_sharp = {mp.nstr(B_SHARP, 12)}), "
      f"<= {_L_RIG} (B_rig = {mp.nstr(B_RIG, 12)})")
print(f"  remaining gaps: G1 Xbot <= Xblock;  G2 sup_s Xblock = {mp.nstr(_B_meas, 24)}")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {
        "script": "computations/deltalambda/rev_e_infinity_search_reduction_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The e_inf three-piece maximisation is COERCIVE -- eps convex decreasing linearises "
        "every pair term for both signs, the pair sum telescopes to top-minus-bottom, and the "
        "quadratic cost dominates, giving a uniform bound B_rig on every valid block with no "
        "cap on its length or entries.  So only finitely many (s_t, s_b) can win, as a matter "
        "of the inequality rather than of any table.  Separately and NEGATIVELY: the marginal "
        "of Xblock is NOT monotone -- it re-crosses ln q0/2 upward at s = 11 -- so the greedy / "
        "first-crossing exchange argument that would close the search is refuted.  Within the "
        "measured cut the enumeration carries no effective cap and the join is maximised at "
        "(8, 8), reproducing #7335's searched e_inf; that closure is CONDITIONAL on two named "
        "gaps, Xbot <= Xblock and B being the true supremum."
    ),
    "constants": {
        "ln_q0_half": mp.nstr(LNQ_HALF, 30), "mp_dps": mp.dps,
        "scale_digits": SCALE_DIGITS,
        "eps_depth": DEPTH2, "T_depth": DEPTH4,
        "S_1": mp.nstr(S_1, 30), "G_1": mp.nstr(G_1, 30), "G_half": mp.nstr(G_HALF, 30),
        "N_star": mp.nstr(N_STAR, 30), "B_rigorous": mp.nstr(B_RIG, 30),
        "Ghat_1": mp.nstr(GHAT[1], 30), "B_sharp": mp.nstr(B_SHARP, 30),
    },
    "coercivity_S3": {
        "per_term": "eps(2d) - eps(2d+D) <= g(d) D  for every sign of D,  g(d) = |eps'(2d)|",
        "assembled_cauchy_schwarz":
            "Xblock(u) <= S_1 - G_1 + G_half sqrt(N) - (ln q0/2) N,  N = sum v^2",
        "assembled_per_row":
            "Xblock(u) <= sum_i [ u_i Ghat(i+1) - (ln q0/2) u_i^2 ],  "
            "Ghat(m) = sum_{d>=m} |eps'(2d)|",
        "uniform_cauchy_schwarz": "B_rig = S_1 - G_1 + G_half^2 / (2 ln q0)",
        "uniform_per_row": "B_sharp = sum_m Ghat(m)^2 / (2 ln q0)",
        "B_rigorous": mp.nstr(B_RIG, 30),
        "B_sharp": mp.nstr(B_SHARP, 30),
        "unconditional_ell_cut": _L_SHARP,
        "unconditional_ell_cut_cauchy_schwarz": _L_RIG,
        "measured_B": mp.nstr(_B_meas, 30), "measured_B_at_s": _s_peak,
        "measured_ell_cut": _L_CUT,
        "crudeness_factor": mp.nstr(B_RIG / _B_meas, 10),
    },
    "greedy_refuted_S4": {
        "ln_q0_half": mp.nstr(LNQ_HALF, 30),
        "first_below": _first_below,
        "re_crossings": [{"s": s, "marginal": mp.nstr(m, 20)} for s, m in _re_cross],
        "marginals": [{"s": s, "marginal": mp.nstr(m, 20),
                       "Xblock": mp.nstr(sc(_tbl_c[s][0]), 26),
                       "profile": list(_tbl_c[s][1])} for s, m in _marg],
    },
    "join_S6": {
        "argmax_s_t": _arg_j[0], "argmax_s_b": _arg_j[1],
        "top_profile": list(_arg_j[2]), "bot_profile_as_top": list(_arg_j[3]),
        "value": mp.nstr(_best_j, 30),
        "searched_7335": mp.nstr(E_INF_7335, 30),
        "difference": mp.nstr(_best_j - E_INF_7335, 20),
        "blocks_enumerated": _nodes_f,
    },
    "evaluator_crosscheck_S8": {
        "worst_difference": mp.nstr(_s8_worst, 20),
        "floor": mp.nstr(_scale_floor, 10),
        "rows": _s8,
    },
    "open_gaps": {
        "G1": ("Xbot(s) <= Xblock(s) for every s.  #7335's E7 measured the two tables equal "
               "for s <= 12 and the top higher by 0.01982 at s = 13; unmeasured beyond."),
        "G2": ("sup_s Xblock(s) equals the measured maximum at s = 14.  Measured over s <= 26 "
               "with caps lifted and non-binding; bounded rigorously only by B_rig, which is "
               "too crude to substitute."),
        "headline": ("Neither is the arc's headline open problem, which remains the upper "
                     "bound on M_n."),
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "The search space is provably finite and the greedy route into it is refuted.  Within "
        "the measured cut the enumeration is genuinely uncapped and lands on (8, 8) at #7335's "
        "e_inf.  What is left is two named inequalities, G1 and G2, neither of which is the "
        "arc's headline open problem."
    ),
}

_out = os.path.join(_HERE, "rev-e-infinity-search-reduction.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
