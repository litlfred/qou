#!/usr/bin/env python3
r"""
rev_e_infinity_block_sup_relaxation_probe.py — the block value is CONCAVE, so `sup_s Xblock`
is a concave program, and gap G2 shrinks from 1.82x to 1.04x (qou-hok7)

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

## What this does NOT do: G2 is REDUCED, not closed

Two things stand between this and an unconditional closure, and both are finite, specified
computations rather than open questions:

  **(a) A certificate for the concave maximisation.**  Coordinate ascent on a concave function
  reaches the global maximum, and the gradient at the reported optimum is tiny — but "tiny
  gradient in a numerical search" is not a proof.  What would settle it is the supergradient
  inequality `F(u) <= F(w) + grad F(w) . (u - w)` evaluated at the returned `w`, with the
  boundary coordinates (`u_i = 1`) carrying `grad <= 0` by KKT.

  **(b) A rigorous bound on the block length `T`.**  The measured `sup_u Xblock(u)` peaks at
  `T = 7` and falls monotonically after (2.25373, 2.25068, 2.23119, 2.20026, 2.16211, 2.11924
  at `T = 7..12`), but "falls in the range I measured" is not "falls forever".  The per-row
  bound does give a rigorous `T` cut: every row past index 5 contributes at most
  `Ghat(i+1) - ln q0/2`, which is negative there and tends to `-ln q0/2`, so the cumulative cap
  drops below `B_relax` at an explicit `T0` this probe computes.  `T0 = 40`, so `T = 13..40` —
  28 values — is simply unmeasured.

Until both are done the cut of 27 is not usable and the practical cut stays at 23 on the
measured `B`.  What has changed is the size of the remaining work: G2 was "tighten an explicit
series by a factor under two" and is now "certify a concave maximum and check ~30 values of T".

## Checks

  P1  `Xblock` at real `u` reproduces the integer enumeration at the known argmax
  P2  `Xblock` is concave in `u` — checked on random ordered triples, not assumed
  P3  Jensen is a valid upper bound on the exact value, and saturates where the linear one
      does not
  P4  the per-row bound's slack is concentrated in row 0 (73.8 % of `B_sharp`), and a single
      row's true maximum is 0.9297 against that row's 2.8936 budget
  P5  the relaxed sup `B_relax`, per `T`, with its peak and its argmax
  P6  the four bounds and the cut each one gives, with the enumeration cost of each cut
  P7  the rigorous `T0` past which no block length can reach `B_relax`

Proton-pinned; `mp.dps = 30`; the bulk tail uses the Lambert resummation of #7349 (verified
here against the direct sum) so a coordinate step costs `O(T + RMAX)` rather than
`O(T^2 + T*RMAX)`.  No float64.

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/BraidKnot/SearchCoercivity.lean
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
INT_SUP = mp.mpf("2.1598023761182859616035304")        # #7349's enumerated max, at [4,3,2,2,1,1,1]
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


T_KERNEL = [2 * epsx(2 * d) - epsx(2 * d - 1) - epsx(2 * d + 1) for d in range(1, DEPTH4)]


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
for _T in range(1, TMAX + 1):
    _v, _u = relaxed_sup(_T)
    _ordered = all(_u[k] >= _u[k + 1] - 1 for k in range(_T - 1))
    _p5.append({"T": _T, "sup": mp.nstr(_v, 22), "ordered": _ordered,
                "profile": [mp.nstr(x, 10) for x in _u]})
    if _best is None or _v > _best[0]:
        _best = (_v, _T, list(_u))
    print(f"    T = {_T:3d}: {mp.nstr(_v, 20):24s} ordering {'ok ' if _ordered else 'NO '} "
          f"[{', '.join(mp.nstr(x, 4) for x in _u[:7])}{'...' if _T > 7 else ''}]", flush=True)
B_RELAX, _T_STAR, _U_STAR = _best
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
# per-row bound: row i contributes at most max_{v>=1} [v Ghat(i+1) - (ln q0/2) v^2],
# which is Ghat^2/(2 ln q0) when the parabola peaks at v >= 1, else the value at v = 1.
def _row_cap(i: int) -> mp.mpf:
    gh = GHAT[i + 1]
    return gh ** 2 / (2 * LNQ) if gh >= LNQ else gh - LNQ_HALF


_run = mp.mpf(0)
_T0 = None
for _i in range(0, 400):
    _run += _row_cap(_i)
    if _run < B_RELAX and _i >= _T_STAR:
        _T0 = _i + 1
        break
_neg_from = next(i for i in range(400) if _row_cap(i) < 0)
print(f"    row caps turn negative from row {_neg_from} on "
      f"(Ghat({_neg_from+1}) = {mp.nstr(GHAT[_neg_from+1], 8)} < ln q0/2 = "
      f"{mp.nstr(LNQ_HALF, 8)})")
print(f"    cumulative per-row cap drops below B_relax at T0 = {_T0}", flush=True)
check(
    "P7 block length is rigorously bounded, and the unchecked window is explicit",
    _T0 is not None and _T0 < 400,
    f"every row past index {_neg_from - 1} contributes at most "
    f"`Ghat(i+1) - ln q0/2 < 0`, so the cumulative per-row cap falls below B_relax = "
    f"{mp.nstr(B_RELAX, 12)} at T0 = {_T0}: no block of length > {_T0} can reach it.  This "
    f"probe measured T <= {TMAX}, where the sup peaks at T = {_T_STAR} and falls monotonically "
    f"after.  So T = {TMAX + 1}..{_T0} is UNMEASURED — the gap between 'falls in the range I "
    f"looked at' and 'falls forever' is exactly {_T0 - TMAX} values of T, and closing it is "
    f"compute rather than insight",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  B_relax = {mp.nstr(B_RELAX, 22)} at T = {_T_STAR}   "
      f"({mp.nstr(B_RELAX / INT_SUP, 6)}x the integer maximum)")
print(f"  cut: s_t + s_b <= {_cut_relax}  ({blocks_with_sum_at_most(_cut_relax):,} blocks)")
print(f"  G2 remains OPEN: needs a concave-max certificate and T = {TMAX + 1}..{_T0}")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {
        "script": "computations/deltalambda/rev_e_infinity_block_sup_relaxation_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
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
        "enumerable.  Gap G2 is "
        "REDUCED, NOT CLOSED: an unconditional closure still needs a certificate for the "
        "concave maximum (a tiny numerical gradient is not a proof) and a check of the block "
        "lengths between this probe's measured range and the rigorous T0."
    ),
    "constants": {
        "ln_q0_half": mp.nstr(LNQ_HALF, 30), "mp_dps": mp.dps,
        "eps_depth": DEPTH2, "T_depth": DEPTH4, "lambert_depth": RMAX,
        "S_e_1": mp.nstr(S_E1, 30), "Ghat_1": mp.nstr(GHAT[1], 30),
        "integer_sup": mp.nstr(INT_SUP, 30), "B_sharp_7349": mp.nstr(B_SHARP, 30),
        "B_jensen_over_measured_T": mp.nstr(_jen_sup, 30),
        "B_relax_over_measured_T": mp.nstr(B_RELAX, 30),
        "T_star": _T_STAR, "T_measured_max": TMAX, "T0_rigorous": _T0,
        "_note": ("both suprema are over T <= T_measured_max, NOT over all T.  T0_rigorous is "
                  "the length past which the per-row cap forbids reaching B_relax; "
                  "T_measured_max+1 .. T0_rigorous is unchecked, which is why G2 is reduced "
                  "rather than closed."),
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
        "G2_status": "REDUCED, not closed",
        "G2_remaining_a": ("a certificate for the concave maximisation -- the supergradient "
                           "inequality at the returned point, with boundary coordinates "
                           "carrying a non-positive gradient by KKT"),
        "G2_remaining_b": (f"block lengths T = {TMAX + 1}..{_T0} are unmeasured; T0 = {_T0} is "
                           f"rigorous from the per-row cap turning negative at row "
                           f"{_neg_from}"),
        "G1": ("unchanged: Xbot(s) <= Xblock(s) for every s, measured equal for s <= 12 and "
               "top-higher by 0.01982 at s = 13"),
        "headline": "still the upper bound on M_n, which none of this touches",
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "Concavity of the block value turns sup_s Xblock from a search into a concave program "
        "and shrinks gap G2 from 1.82x to 1.04x, taking the e_inf cut from an unenumerable 90 "
        "to an enumerable 27.  It does not close G2: the concave maximum is numerical and the "
        "block-length window between the measured range and the rigorous T0 is unchecked.  "
        "Both are finite specified computations rather than open questions, which is the "
        "change."
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
