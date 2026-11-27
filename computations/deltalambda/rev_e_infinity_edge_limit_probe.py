#!/usr/bin/env python3
r"""
rev_e_infinity_edge_limit_probe.py — `e_inf` splits into THREE independent k-free pieces
(qou-hok7)

`e_inf` is the one number left in the `REV_n` asymptotics.  Everything else in

    kappa = -A/2 - B - C + e_inf

is an explicit convergent series (#7294, `rev_staircase_closed_form_and_constant_term_probe`),
and that probe states the residue plainly: *"e_inf is measured at a single n rather than proved
to be a limit"* — the largest `n` its heuristic scan reached, `n = 3916` (`k = 88`).

This probe replaces the single reading with a structure.  From the previous three PRs:

  #7305  the cost is the exact quadratic form  `ln q0 * [ sum_{i>k}(i-k) u_i + (1/2) sum u_i^2 ]`
         (Lean, sorry-free: `staircase_two_mul_hookSum_sub`)
  #7323  the maximiser is a top bulge + a contiguous run of `-1` + a bottom block, with the run's
         length forced by `sum u = 0` and its position free
  #7331  the excess does NOT add over two independently-run edges, and the residual is an
         interface count

The run's position being FREE is the load-bearing fact, and #7331 stopped one step short of it.
A displaced row interacts with another only through `eps(m) = -log(1 - q0^(-2m))`, which dies
geometrically, so a free position is a position that goes to infinity: at the optimum the run
sits far from both blocks, and the excess splits into **three** mutually non-interacting pieces —

    e_inf  =  max over (s_t, s_b)  [ Xblock(s_t)  +  Xrun(s_t + s_b)  +  Xbot(s_b) ]

with `s_t`, `s_b` the two blocks' sums and the run length forced by `sum u = 0`.  None of the
three carries a `k`.

That also explains #7331's residual exactly, and predicts its sign and rough size without any
new computation: two isolated single-edge shapes each carry their own run, so their sum is
`Xrun(s_t) + Xrun(s_b)` where the joint shape has `Xrun(s_t + s_b)` — one run's worth of
interface double-counted.  #7331 measured 0.516 to 0.617 and attributed it to exactly that.

## What this establishes, and what it does not

It establishes the decomposition as an exact identity at finite `k` (excess = the three pieces +
the pairs that cross between them), measures the crossing terms, and shows they reach identically
zero — so `e_k` has stopped moving, at a rung that is identified rather than guessed.

It does NOT prove the limit exists: that needs the upper bound on `M_n` this arc still lacks.
`e_k` here is exhaustive over an explicit SHAPE CLASS, so every value is a rigorous LOWER bound
on the true one.  The class is the shape the full enumeration of #7305 independently found at
every `k <= 12`, and E5 widens every one of its bounds to check none is binding.

## Checks

  E1  the FULL-ENUMERATION maximiser lies in the shape class at every k <= 12, and two
      independent evaluators reproduce its excess to the rounding budget
  E2  the class reproduces PR #7331's independently-searched joint maximum at k = 40
  E3  the three-piece split is an exact identity, and the crossing terms are zero at large k
  E3b the block and the run REPEL — the assumption the whole decomposition rests on
  E4  the finite-k shortfall vanishes exactly when the crossing term does, and never from above
      (they are not the same NUMBER — the shortfall also carries each piece's own truncation)
  E5  widening every bound of the class moves neither e_inf nor its argmax
  E6  e_inf sits above the single-n reading #7294 used, as e_k increasing requires
  E7  the two block energies are equal as exact integers — one edge energy, seen twice

Proton-pinned; exact integer arithmetic at scale 1e-40; mpmath dps 60 for the tables.  No
float64.

-- Ref: [manuscript] folio/quantum-observable-universe/lean/QOU/BraidKnot/HookSumElasticity.lean
"""

from __future__ import annotations

import bisect
import json
import os
import sys
import time
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 60
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

SCALE_DIGITS = 40
SCALE = mp.mpf(10) ** SCALE_DIGITS

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def eps(m: int) -> mp.mpf:
    return -mp.log(1 - T ** (-m)) if m > 0 else mp.mpf(0)


_MMAX = 8000
_EPS_I = [0] + [int(mp.floor(eps(m) * SCALE + mp.mpf("0.5"))) for m in range(1, _MMAX)]
_F_I = [0] * _MMAX
for _m in range(1, _MMAX):
    _F_I[_m] = _F_I[_m - 1] + _EPS_I[_m]
LNQ_I = int(mp.floor(LNQ * SCALE + mp.mpf("0.5")))

# `epsi(m)` is identically zero in this arithmetic from `EPS_CUT` on.  Read off the table, not
# chosen: it is the first m whose rounded eps rounds to zero at scale 1e-40.
EPS_CUT = next(m for m in range(1, _MMAX) if _EPS_I[m] == 0)
U_MAX_ABS = 10          # a displacement moves a gap by at most this, so windows need the slack


def epsi(m: int) -> int:
    return _EPS_I[m] if 0 < m < _MMAX else 0


def fi(b: int) -> int:
    return _F_I[b] if b < _MMAX else _F_I[_MMAX - 1]


def staircase_beta(k: int, L: int) -> list[int]:
    """beta of the staircase delta_k padded into an L-row frame (L >= k+1).

    Rows i <= k carry beta = 2k + P - 2i, an arithmetic progression of gap 2; the P = L-k-1 rows
    below carry beta = P-1, ..., 0, consecutive.  The junction is the 'bottom wall' of #7323 and
    the free end of the AP is its 'top edge'.
    """
    return [max(k - i, 0) + (L - 1 - i) for i in range(L)]


# --------------------------------------------------------------------------------------------
# Evaluators.  `excess_full` is the O(L^2) definition; `delta_excess` sums over displaced rows
# only; `ap_value` is the closed form in a pure AP of gap 2.  E1 and E3 check them against each
# other and against #7305's independent cell-by-cell enumeration; none is trusted alone.
# --------------------------------------------------------------------------------------------
def excess_full(u: list[int], k: int) -> int | None:
    """Exact scaled excess over the staircase, straight from the definition."""
    L = len(u)
    b0 = staircase_beta(k, L)
    if sum(u) != 0:
        return None
    beta = [b0[i] + u[i] for i in range(L)]
    if beta[-1] < 0 or any(beta[i] <= beta[i + 1] for i in range(L - 1)):
        return None

    def gain(bs: list[int]) -> int:
        tot = sum(fi(b) for b in bs)
        for a in range(L):
            ba = bs[a]
            for b in range(a + 1, L):
                tot -= epsi(ba - bs[b])
        return tot

    lin = sum((i - k) * u[i] for i in range(L) if i > k)
    return gain(beta) - gain(b0) - (LNQ_I * (2 * lin + sum(x * x for x in u))) // 2


def _beta_if_valid(b0: list[int], u: list[int]) -> list[int] | None:
    L = len(u)
    beta = [b0[i] + u[i] for i in range(L)]
    if beta[-1] < 0:
        return None
    for i in range(L - 1):
        if beta[i] <= beta[i + 1]:
            return None
    return beta


def delta_excess(u: list[int], k: int, b0: list[int], nb0: list[int],
                 require_zero_sum: bool = True) -> int | None:
    """The same number as `excess_full`, summed over the displaced rows only.

    With `require_zero_sum=False` this evaluates the same expression on a displacement that does
    not sum to zero.  That is NOT the excess of any partition — it is one summand of the split,
    and it is what makes the three pieces separately computable.  `nb0` is `[-b for b in b0]`,
    ascending, for the bisect window.
    """
    L = len(u)
    if require_zero_sum and sum(u) != 0:
        return None
    beta = _beta_if_valid(b0, u)
    if beta is None:
        return None
    S = [i for i in range(L) if u[i]]
    Sset = set(S)

    tot = 0
    for a in S:
        tot += fi(beta[a]) - fi(b0[a])
        lo = bisect.bisect_left(nb0, -(b0[a] + EPS_CUT + U_MAX_ABS))
        hi = bisect.bisect_right(nb0, -(b0[a] - EPS_CUT - U_MAX_ABS))
        ba0, ba = b0[a], beta[a]
        for b in range(lo, hi):
            if b == a or b in Sset:
                continue
            if b > a:
                tot += epsi(ba0 - b0[b]) - epsi(ba - beta[b])
            else:
                tot += epsi(b0[b] - ba0) - epsi(beta[b] - ba)
    for ia, i in enumerate(S):
        for j in S[ia + 1:]:
            tot += epsi(b0[i] - b0[j]) - epsi(beta[i] - beta[j])

    lin = sum((i - k) * u[i] for i in S if i > k)
    return tot - (LNQ_I * (2 * lin + sum(x * x for x in u))) // 2


# `_DOWN[u]` is the complete tail, over every AP row BELOW a single row displaced by u, of
# [eps(gap0) - eps(gap)]; `_UP[u]` is the same upward.  `_AP_D` is set so `2 * _AP_D` clears
# `EPS_CUT` with the displacement slack, which makes both tails exact rather than truncated.
_AP_D = (EPS_CUT + 2 * U_MAX_ABS) // 2 + 2
_DOWN = {u: sum(epsi(2 * d) - epsi(2 * d + u) for d in range(1, _AP_D + 1))
         for u in range(-U_MAX_ABS, U_MAX_ABS + 1)}
_UP = {u: _DOWN[-u] for u in range(-U_MAX_ABS, U_MAX_ABS + 1)}


def ap_value(u: list[int], bounded_above: bool) -> int | None:
    """A displacement's contribution inside an arithmetic progression of gap 2.

    `bounded_above=True` puts row 0 at the free top of the AP (the top edge of the staircase);
    `False` continues the AP infinitely in both directions (a run sitting in the bulk).  Valid
    exactly when every displaced row has at least `_AP_D` AP rows on each unbounded side, and
    `beta ~ 2k` there so `F` is saturated and the one-body term is identically zero — E3 checks
    both against `delta_excess` on the real frame rather than assuming them.
    """
    n = len(u)
    for i in range(n - 1):
        if 2 + u[i] - u[i + 1] <= 0:
            return None
    S = [i for i in range(n) if u[i]]
    if not S:
        return 0
    tot = 0
    for a in S:
        ua = u[a]
        tot += _DOWN[ua]
        if bounded_above:
            for d in range(1, a + 1):          # the AP stops at row 0
                tot += epsi(2 * d) - epsi(2 * d - ua)
        else:
            tot += _UP[ua]
        for b in S:                            # undo the "everything else undisplaced" premise
            if b == a:
                continue
            d = b - a
            if d > 0:
                tot -= epsi(2 * d) - epsi(2 * d + ua)
            else:
                tot -= epsi(-2 * d) - epsi(-2 * d - ua)
    for ia, i in enumerate(S):                 # and put the true S-S pair terms back, once each
        for j in S[ia + 1:]:
            tot += epsi(2 * (j - i)) - epsi(2 * (j - i) + u[i] - u[j])
    return tot - (LNQ_I * sum(x * x for x in u)) // 2


def cross_pairs(u: list[int], b0: list[int], groups: list[list[int]]) -> int:
    """Pair terms between DIFFERENT displaced groups — the only part of the excess that is not
    additive over the groups."""
    beta = [b0[i] + u[i] for i in range(len(u))]
    tot = 0
    for gi in range(len(groups)):
        for gj in range(gi + 1, len(groups)):
            for i in groups[gi]:
                for j in groups[gj]:
                    a, b = (i, j) if i < j else (j, i)
                    tot += epsi(b0[a] - b0[b]) - epsi(beta[a] - beta[b])
    return tot


# --------------------------------------------------------------------------------------------
# The shape class
# --------------------------------------------------------------------------------------------
def top_profiles(tmax: int, umax: int):
    """Leading positive blocks.  On an AP of gap 2, `beta` strictly decreasing permits
    `u_{i+1} <= u_i + 1`, so a profile may rise by one as well as fall."""
    out: list[tuple[int, ...]] = [()]

    def rec(cur: tuple[int, ...]):
        if len(cur) >= tmax:
            return
        hi = umax if not cur else min(umax, cur[-1] + 1)
        for x in range(1, hi + 1):
            nxt = cur + (x,)
            out.append(nxt)
            rec(nxt)

    rec(())
    return out


def bot_profiles(bmax: int, umax: int):
    """Trailing positive blocks.  Not monotone in the data (the k=35 maximiser ends
    1,1,1,2,1,1), so enumerate freely with a positive leading entry."""
    out: list[tuple[int, ...]] = [()]

    def rec(cur: tuple[int, ...]):
        if len(cur) >= bmax:
            return
        for x in range(0, umax + 1):
            nxt = (x,) + cur
            if nxt[0] == 0:
                continue
            out.append(nxt)
            rec(nxt)

    for x in range(1, umax + 1):
        out.append((x,))
        rec((x,))
    return sorted(set(out), key=lambda t: (len(t), t))


def make_u(L: int, top: tuple[int, ...], bot: tuple[int, ...], p: int, ell: int):
    """`u` with the top block at the head, the bottom block at the tail, and a run of `-1` of
    length `ell` starting at row `p`.  None when the three pieces would overlap."""
    if p < len(top) or p + ell > L - len(bot):
        return None
    u = [0] * L
    for i, x in enumerate(top):
        u[i] = x
    for j, x in enumerate(bot):
        u[L - len(bot) + j] = x
    for i in range(p, p + ell):
        u[i] = -1
    return u


TMAX, TUMAX = 8, 6
BMAX, BUMAX = 9, 3
ELL_MAX = 40
P_EXT_MAX = 8
K_BOT = 320          # frame for the bottom-edge table: >= _AP_D AP rows above the block
K_BIG = 760          # frame where all three pieces are >= _AP_D apart
SEP = 250            # rows between the top block and the run's head at K_BIG

TOPS = top_profiles(TMAX, TUMAX)
BOTS = bot_profiles(BMAX, BUMAX)


def block_table(tops):
    """`Xblock[s_t] -> (value, top)`: the top edge's best value, alone, in the k -> infinity AP.
    Carries no k."""
    out: dict[int, tuple[int, tuple]] = {}
    for top in tops:
        if not top:
            continue
        v = ap_value(list(top), bounded_above=True)
        if v is None:
            continue
        st = sum(top)
        cur = out.get(st)
        if cur is None or v > cur[0]:
            out[st] = (v, top)
    return out


def run_table(ell_max: int):
    """`Xrun[ell]`: a contiguous run of `-1` of length `ell` in the AP bulk.  Carries no k."""
    return {ell: ap_value([-1] * ell, bounded_above=False) for ell in range(1, ell_max + 1)}


def bot_table(bots, k: int = K_BOT, pe_max: int = P_EXT_MAX):
    """`Xbot[s_b] -> (value, bot, P)`: the bottom edge's best value, alone."""
    out: dict[int, tuple[int, tuple, int]] = {}
    for pe in range(0, pe_max + 1):
        L = k + 1 + pe
        b0 = staircase_beta(k, L)
        nb0 = [-x for x in b0]
        for bot in bots:
            if not bot:
                continue
            u = make_u(L, (), bot, 0, 0)
            if u is None:
                continue
            v = delta_excess(u, k, b0, nb0, require_zero_sum=False)
            if v is None:
                continue
            sb = sum(bot)
            cur = out.get(sb)
            if cur is None or v > cur[0]:
                out[sb] = (v, bot, pe)
    return out


def join(Xblock, Xrun, Xbot):
    """`e_inf` as the maximum of the three-piece SUM, run length forced by `sum u = 0`."""
    best, arg = None, None
    for st, (vt, top) in Xblock.items():
        for sb, (vb, bot, pe) in Xbot.items():
            ell = st + sb
            if ell not in Xrun:
                continue
            v = vt + Xrun[ell] + vb
            if best is None or v > best:
                best, arg = v, (top, bot, pe, st, sb, ell, vt, Xrun[ell], vb)
    return best, arg


def sc(x: int) -> mp.mpf:
    return mp.mpf(x) / SCALE


# --------------------------------------------------------------------------------------------
print("e_inf — the REV_n excess splits into three independent k-free pieces")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  arithmetic: integers at scale 1e-{SCALE_DIGITS}")
print(f"  eps vanishes in this arithmetic from m = {EPS_CUT}; AP tail depth {_AP_D}")
print(f"  class: top <= {TMAX} rows / values <= {TUMAX} ({len(TOPS)} profiles), bottom <= {BMAX} "
      f"rows / values <= {BUMAX} ({len(BOTS)} profiles), run <= {ELL_MAX}, P <= {P_EXT_MAX}")
print(flush=True)

# --------------------------------------------------------------------------------------------
# E1 — the exhaustive maximiser lies in the class, and the evaluators reproduce it
# --------------------------------------------------------------------------------------------
print("E1  the FULL-ENUMERATION maximiser of #7305 against the shape class")
_EX = json.load(open(os.path.join(_HERE, "rev-exact-maximiser-small-n.witness.json")))
# The upstream producer's reach is an ENVIRONMENT VARIABLE (`REV_EXACT_KMAX`, default 10), so a
# re-run without it silently narrows this calibration from k <= 12 to k <= 10 and nothing else
# in the chain notices.  Record the reach so the narrowing is visible in the witness.
_EX_KMAX = max(r["k"] for r in _EX["exact_rows"])
print(f"    upstream enumeration reaches k = {_EX_KMAX} (REV_EXACT_KMAX; default 10)", flush=True)
_e1 = []
for _r in _EX["exact_rows"]:
    _k = _r["k"]
    _b = _r["argmax_beta"][0]
    _Lm = len(_b)
    if _k < 7 or _Lm < _k + 1 or _Lm - _k - 1 > P_EXT_MAX:
        continue                     # k <= 6: the staircase itself is the maximiser
    _pe = _Lm - _k - 1
    _b0 = staircase_beta(_k, _Lm)
    _u = [_b[i] - _b0[i] for i in range(_Lm)]
    _lt = 0
    while _lt < _Lm and _u[_lt] > 0:
        _lt += 1
    _lb = 0
    while _lb < _Lm and _u[_Lm - 1 - _lb] > 0:
        _lb += 1
    _top, _bot = tuple(_u[:_lt]), tuple(_u[_Lm - _lb:])
    _run = [i for i in range(_Lm) if _u[i] == -1]
    _contig = bool(_run) and _run == list(range(_run[0], _run[0] + len(_run)))
    _rest_zero = all(_u[i] == 0 for i in range(_lt, _Lm - _lb) if i not in set(_run))
    _in_class = (
        _contig and _rest_zero
        and len(_top) <= TMAX and (not _top or max(_top) <= TUMAX)
        and len(_bot) <= BMAX and (not _bot or max(_bot) <= BUMAX)
        and len(_run) <= ELL_MAX and len(_run) == sum(_top) + sum(_bot)
    )
    _target = int(_r["M_n_scaled"]) - int(_r["V_stair_scaled"])
    _b0n = [-x for x in _b0]
    _vf, _vd = excess_full(_u, _k), delta_excess(_u, _k, _b0, _b0n)
    _rebuilt = make_u(_Lm, _top, _bot, _run[0], len(_run)) if _contig else None
    # The comparison floor is set by ROUNDING and is COUNTED, not chosen.  #7305 accumulates n
    # rounded phi values per cell-sum, twice; this probe accumulates one rounded eps per changed
    # pair, one per unit of |u| in the F differences (the shared prefixes of the cumulative table
    # cancel exactly in integer arithmetic), and one rounded ln q0 scaled by the cost argument.
    # Each rounded input can move the total by at most one unit at 1e-40, so their count is the
    # budget.  The two sums are mathematically equal and numerically grouped differently.
    _bta = [_b0[i] + _u[i] for i in range(_Lm)]
    _pairs_changed = sum(1 for i in range(_Lm) for j in range(i + 1, _Lm)
                         if _bta[i] - _bta[j] != _b0[i] - _b0[j])
    _cost_arg = 2 * sum((i - _k) * _u[i] for i in range(_Lm) if i > _k) + sum(x * x for x in _u)
    _ulp_bound = 2 * _r["n"] + _pairs_changed + sum(abs(x) for x in _u) + abs(_cost_arg)
    _e1.append({
        "k": _k, "n": _r["n"], "in_class": _in_class, "rebuild_matches": _rebuilt == _u,
        "top": list(_top), "run_head": _run[0] if _run else None, "run_length": len(_run),
        "bottom": list(_bot), "extension": _pe, "evaluators_agree": _vf == _vd,
        "excess_full_minus_exhaustive": _vf - _target, "rounding_ulp_bound": _ulp_bound,
    })
    print(f"    k = {_k:2d} (n = {_r['n']:3d}): top {list(_top)}, run {len(_run)} at row "
          f"{_run[0]}, bottom {list(_bot)}, P = {_pe}  | in class {_in_class}, evaluators agree "
          f"{_vf == _vd}, off #7305 by {_vf - _target} of {_ulp_bound} allowed", flush=True)
_e1_bad = [r for r in _e1 if not (
    r["in_class"] and r["rebuild_matches"] and r["evaluators_agree"]
    and abs(r["excess_full_minus_exhaustive"]) <= r["rounding_ulp_bound"])]
_e1_worst = max((abs(r["excess_full_minus_exhaustive"]) for r in _e1), default=0)
_e1_allow = min((r["rounding_ulp_bound"] for r in _e1), default=0)
check(
    "E1 every exhaustively-found maximiser is in the shape class, and two independent evaluators "
    "reproduce its excess",
    not _e1_bad,
    f"{len(_e1)} values of k ({_e1[0]['k']}..{_e1[-1]['k']}, n = {_e1[0]['n']}..{_e1[-1]['n']}) — "
    f"every k the committed enumeration covers above 6.  Each maximiser decomposes as a positive top "
    f"block, ONE contiguous run of -1 whose length is exactly s_t + s_b, and a positive bottom "
    f"block, with nothing in between — so the three-piece class is the shape the enumeration "
    f"FOUND, not a shape imposed on it, and `make_u` rebuilds each u byte-for-byte from that "
    f"decomposition.  The two evaluators agree with each other on the nose at every k, sharing "
    f"no code path (one is the O(L^2) definition, the other sums over displaced rows through a "
    f"bisect window).  Against #7305's own M_n - V(delta_k) the worst deviation is {_e1_worst} "
    f"units at 1e-{SCALE_DIGITS} against a budget of {_e1_allow}: #7305 accumulates rounded phi "
    f"per CELL while this probe accumulates rounded eps per PAIR, so two integer sums of the "
    f"same quantity agree only to their operation count, and that count is what the budget is.  "
    f"k <= 6 is excluded — there the staircase is itself the maximiser, with no displacement to "
    f"decompose"
    if not _e1_bad else
    "class membership, evaluator agreement or the rounding budget fails at k = "
    + ", ".join(str(r["k"]) for r in _e1_bad),
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# the three tables
# --------------------------------------------------------------------------------------------
print("building the three tables")
_t0 = time.time()
_Xblock = block_table(TOPS)
print(f"    top blocks:  {len(_Xblock)} s_t keys from {len(TOPS)} profiles "
      f"({time.time()-_t0:.1f}s)", flush=True)
_Xrun = run_table(ELL_MAX)
_t1 = time.time()
_Xbot = bot_table(BOTS)
print(f"    bottom blocks: {len(_Xbot)} s_b keys from {len(BOTS)} profiles "
      f"({time.time()-_t1:.1f}s)", flush=True)
_vj, _aj = join(_Xblock, _Xrun, _Xbot)
_top, _bot, _pe, _st, _sb, _ell, _vt, _vr, _vb = _aj
_e_inf = sc(_vj)
print(f"    e_inf = {mp.nstr(_e_inf, 26)}")
print(f"      top block  {list(_top)} (s_t = {_st}): {mp.nstr(sc(_vt), 22)}")
print(f"      run of {_ell}                      : {mp.nstr(sc(_vr), 22)}")
print(f"      bottom block {list(_bot)} (s_b = {_sb}, P = {_pe}): {mp.nstr(sc(_vb), 22)}")
print(flush=True)

# --------------------------------------------------------------------------------------------
# E2 — against PR #7331's independent joint search at k = 40
# --------------------------------------------------------------------------------------------
print("E2  the class against PR #7331's direct joint search at k = 40")
_SEP7331 = json.load(open(os.path.join(_HERE, "rev-edge-separability.witness.json")))
_k40_ref = mp.mpf(_SEP7331["direct_joint_maximum"])
_NKEEP = 8
_tops_by: dict[int, list[tuple]] = {}
for _t2 in TOPS:
    if _t2:
        _v = ap_value(list(_t2), bounded_above=True)
        if _v is not None:
            _tops_by.setdefault(sum(_t2), []).append((_v, _t2))
for _s in _tops_by:
    _tops_by[_s] = sorted(_tops_by[_s], reverse=True)[:_NKEEP]
_bots_by: dict[int, list[tuple]] = {}
_L320 = K_BOT + 1 + 2
_b0320 = staircase_beta(K_BOT, _L320)
_nb0320 = [-x for x in _b0320]
for _b2 in BOTS:
    if _b2:
        _u2 = make_u(_L320, (), _b2, 0, 0)
        if _u2 is not None:
            _v = delta_excess(_u2, K_BOT, _b0320, _nb0320, require_zero_sum=False)
            if _v is not None:
                _bots_by.setdefault(sum(_b2), []).append((_v, _b2))
for _s in _bots_by:
    _bots_by[_s] = sorted(_bots_by[_s], reverse=True)[:_NKEEP]

# #7331's own argmax, re-evaluated here.  This is the O(1) half of the check and the sharper
# one: it asks whether THIS probe's evaluator, on the shape #7331 reported, returns the number
# #7331 recorded — independent of whether either search is exhaustive.
_R7331 = _SEP7331["joint_argmax"] if "joint_argmax" in _SEP7331 else None
_top7331, _bot7331 = (3, 2, 1, 1), (1, 1, 1, 2, 1, 1)
_p7331, _pe7331 = 13, 2
_L7331 = 41 + _pe7331
_u7331 = make_u(_L7331, _top7331, _bot7331, _p7331, sum(_top7331) + sum(_bot7331))
_v7331 = excess_full(_u7331, 40) if _u7331 is not None else None
_in7331 = (len(_top7331) <= TMAX and max(_top7331) <= TUMAX
           and len(_bot7331) <= BMAX and max(_bot7331) <= BUMAX
           and sum(_top7331) + sum(_bot7331) <= ELL_MAX and _pe7331 <= P_EXT_MAX)
print(f"    #7331's own argmax re-evaluated here: "
      f"{mp.nstr(sc(_v7331), 24) if _v7331 is not None else 'INVALID'}   (in this class: "
      f"{_in7331})", flush=True)

# and a bounded joint search, to show this class reaches at least as high
_t0 = time.time()
_best40, _arg40 = None, None
_SUM_CAP_40 = 10
for _pe2 in range(0, P_EXT_MAX + 1):
    _L2 = 41 + _pe2
    _b02 = staircase_beta(40, _L2)
    _nb02 = [-x for x in _b02]
    for _st2, _tl in _tops_by.items():
        if _st2 > _SUM_CAP_40:
            continue
        for _sb2, _bl in _bots_by.items():
            if _sb2 > _SUM_CAP_40:
                continue
            _ell2 = _st2 + _sb2
            if _ell2 > ELL_MAX:
                continue
            for _vt2, _top2 in _tl[:4]:
                for _vb2, _bot2 in _bl[:4]:
                    if len(_top2) + _ell2 + len(_bot2) > _L2:
                        continue
                    for _p2 in range(len(_top2), _L2 - len(_bot2) - _ell2 + 1):
                        _u3 = make_u(_L2, _top2, _bot2, _p2, _ell2)
                        if _u3 is None:
                            continue
                        _v3 = delta_excess(_u3, 40, _b02, _nb02)
                        if _v3 is not None and (_best40 is None or _v3 > _best40):
                            _best40, _arg40 = _v3, (_top2, _bot2, _p2, _ell2, _pe2)
print(f"    class at k = 40: {mp.nstr(sc(_best40), 24)}   ({time.time()-_t0:.1f}s)")
print(f"    PR #7331 direct: {mp.nstr(_k40_ref, 24)}")
print(f"    argmax: top {list(_arg40[0])}, bottom {list(_arg40[1])}, run {_arg40[3]} at row "
      f"{_arg40[2]}, P = {_arg40[4]}")
_k40_scaled = int(mp.floor(_k40_ref * SCALE + mp.mpf("0.5")))
_e2_gap = _best40 - _k40_scaled
# #7331 recorded its joint maximum to 24 significant digits, so agreement can be asked for only
# to that many; the floor is the RECORDING, not this arithmetic.
_e2_floor = 10 ** (SCALE_DIGITS - 23)
_e2_repro = _v7331 is not None and abs(_v7331 - _k40_scaled) <= _e2_floor
check(
    "E2 this probe reproduces PR #7331's maximum on #7331's own shape, and its class reaches at "
    "least as high",
    _e2_repro and _in7331 and _e2_gap >= -_e2_floor,
    f"#7331 reported top {list(_top7331)}, bottom {list(_bot7331)}, run at row {_p7331}, P = "
    f"{_pe7331}.  That shape is inside this class, and `excess_full` here returns "
    f"{mp.nstr(sc(_v7331), 22)} against the {mp.nstr(_k40_ref, 22)} #7331's witness records — "
    f"agreeing to the 24 significant digits the witness carries, with two different evaluators.  "
    f"A bounded joint search over this class (block sums <= {_SUM_CAP_40}, 4 profiles per sum, "
    f"every run position) then reaches {mp.nstr(sc(_best40), 22)}, {mp.nstr(sc(_e2_gap), 4)} "
    f"relative to #7331 — so the class is at least as wide as the one #7331 searched"
    if (_e2_repro and _in7331 and _e2_gap >= -_e2_floor) else
    (f"#7331's own shape re-evaluates to {mp.nstr(sc(_v7331), 22) if _v7331 else 'INVALID'} "
     f"against its recorded {mp.nstr(_k40_ref, 22)} (in class: {_in7331}); the bounded search "
     f"reaches {mp.nstr(sc(_best40), 22)}, {mp.nstr(sc(_e2_gap), 6)} relative to #7331"),
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E3 — the three-piece split is an exact identity, and the crossings vanish
# --------------------------------------------------------------------------------------------
print("E3  the three-piece split at k = 760")
_Lj = K_BIG + 1 + _pe
_p_big = len(_top) + SEP
_uj = make_u(_Lj, _top, _bot, _p_big, _ell)
_b0j = staircase_beta(K_BIG, _Lj)
_nb0j = [-x for x in _b0j]
_groups = [list(range(len(_top))), list(range(_p_big, _p_big + _ell)),
           list(range(_Lj - len(_bot), _Lj))]
_cross = cross_pairs(_uj, _b0j, _groups)
_full = excess_full(_uj, K_BIG)


def _piece(rows):
    _uu = [0] * _Lj
    for _i in rows:
        _uu[_i] = _uj[_i]
    return delta_excess(_uu, K_BIG, _b0j, _nb0j, require_zero_sum=False)


_pt, _pr, _pb = (_piece(g) for g in _groups)
print(f"    definition                    {mp.nstr(sc(_full), 26)}")
print(f"    Xblock + Xrun + Xbot          {mp.nstr(sc(_vj), 26)}   difference {_full - _vj}")
print(f"    crossing pairs                {_cross}  (scaled integer)")
print(f"    pieces in the real frame:  top {_pt - _vt:+d}   run {_pr - _vr:+d}   "
      f"bottom {_pb - _vb:+d}   (vs their k-free values)")
check(
    "E3 the three pieces are independent at k = 760, and each equals its k-free value exactly",
    _cross == 0 and _full == _vj and (_pt, _pr, _pb) == (_vt, _vr, _vb),
    f"the top block, the run and the bottom block sit >= {SEP} rows apart, so every pair between "
    f"two different groups is >= {2*SEP} apart in beta where eps is identically zero from "
    f"m = {EPS_CUT}: the crossing term is exactly {_cross} at scale 1e-{SCALE_DIGITS}.  Each "
    f"piece re-evaluated in the real k = {K_BIG} frame by `delta_excess` returns the same scaled "
    f"integer as its k-free closed form (differences {_pt-_vt}, {_pr-_vr}, {_pb-_vb}), and the "
    f"three sum to the O(L^2) definition on the assembled shape (difference {_full - _vj}).  "
    f"That is the decomposition holding as an identity between three independent evaluators, not "
    f"an approximation with a tolerance",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E3b — the load-bearing assumption: the block-run interaction is REPULSIVE, so a free position
# runs to infinity and the split is the optimum rather than merely an evaluable configuration
# --------------------------------------------------------------------------------------------
print("E3b  is the block-run interaction repulsive?  (this is what sends the run to infinity)")
_sepscan = []
for _s2 in (0, 1, 2, 3, 5, 8, 12, 20, 40, 80, 160, 250):
    _p4 = len(_top) + _s2
    _u4 = [0] * (_p4 + _ell)
    for _i, _x in enumerate(_top):
        _u4[_i] = _x
    for _i in range(_p4, _p4 + _ell):
        _u4[_i] = -1
    _v4 = ap_value(_u4, bounded_above=True)
    if _v4 is None:
        continue
    _sepscan.append({"separation": _s2, "value": mp.nstr(sc(_v4), 26), "scaled": str(_v4),
                     "shortfall_from_split": str(_vt + _vr - _v4)})
    print(f"    separation {_s2:4d}: {mp.nstr(sc(_v4), 24):28s} shortfall from Xblock + Xrun "
          f"{mp.nstr(sc(_vt + _vr - _v4), 6)}", flush=True)
_mono = all(int(_sepscan[i]["scaled"]) <= int(_sepscan[i + 1]["scaled"])
            for i in range(len(_sepscan) - 1))
_reaches = int(_sepscan[-1]["shortfall_from_split"]) == 0
check(
    "E3b the block and the run repel, so the free position runs to infinity and the split is the "
    "supremum",
    _mono and _reaches,
    f"the combined top-block-plus-run value increases monotonically in their separation over "
    f"{len(_sepscan)} sampled separations and reaches Xblock + Xrun exactly (shortfall 0 at "
    f"separation {_sepscan[-1]['separation']}), having been short by "
    f"{mp.nstr(sc(int(_sepscan[0]['shortfall_from_split'])), 4)} when adjacent.  This is the "
    f"assumption the whole decomposition rests on and it is the one an agent would be tempted to "
    f"assert: if the interaction were ATTRACTIVE the optimum would put the run against the "
    f"block, the three pieces would not separate, and e_inf computed this way would be an "
    f"understatement.  It is repulsive, so 'the position is free' (#7323) means 'the position "
    f"goes to infinity', and the sup is attained in the limit rather than at any finite k"
    if (_mono and _reaches) else
    f"the separation scan is NOT monotone ({_mono}) or does not reach the split value "
    f"({_reaches}) — the run does not simply move away from the block, so the three-piece split "
    f"is not the optimum and e_inf from it understates the limit",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E4 — the finite-k deficit IS the crossing term
# --------------------------------------------------------------------------------------------
print("E4  the limiting shape at finite k — where does e_k stop moving?")
_ladder = []
for _k2 in (40, 60, 100, 160, 240, 320, 400, 460, 520, 600, 700, 760):
    _L3 = _k2 + 1 + _pe
    _lo = len(_top)
    _hi = _L3 - len(_bot) - _ell
    if _hi < _lo:
        continue
    _p3 = (_lo + _hi) // 2                      # the run midway between the two blocks
    _u3 = make_u(_L3, _top, _bot, _p3, _ell)
    _v3 = excess_full(_u3, _k2)
    if _v3 is None:
        continue
    _b03 = staircase_beta(_k2, _L3)
    _g3 = [list(range(len(_top))), list(range(_p3, _p3 + _ell)),
           list(range(_L3 - len(_bot), _L3))]
    _c3 = cross_pairs(_u3, _b03, _g3)
    _ladder.append({"k": _k2, "n": _k2 * (_k2 + 1) // 2, "run_head": _p3,
                    "value": mp.nstr(sc(_v3), 30), "scaled": str(_v3),
                    "crossing_scaled": _c3, "deficit_scaled": str(_vj - _v3)})
    print(f"    k = {_k2:4d}: {mp.nstr(sc(_v3), 26):30s} crossing {_c3:>26d}  "
          f"deficit {mp.nstr(sc(_vj - _v3), 6)}", flush=True)
_settled = [r for r in _ladder if r["crossing_scaled"] == 0]
_moving = [r for r in _ladder if r["crossing_scaled"] != 0]
_first_settled = min((r["k"] for r in _settled), default=None)
check(
    "E4 the finite-k shortfall vanishes exactly when the crossing term does, and never from "
    "above",
    len(_settled) >= 2 and len({r["scaled"] for r in _settled}) == 1
    and all(int(r["deficit_scaled"]) == 0 for r in _settled)
    and all(int(r["deficit_scaled"]) > 0 for r in _moving),
    f"the limiting shape's exact excess is the SAME scaled integer at every k from "
    f"{_first_settled} up ({len(_settled)} rungs, agreeing to 1e-{SCALE_DIGITS}), and at every "
    f"smaller k it falls short — always from BELOW, never above — exactly where the crossing "
    f"term is nonzero.  The two switch off TOGETHER, which is what ties the finite-k correction "
    f"to the crossing pairs.  They are NOT equal: at k = 460 the crossing term is 1 unit while "
    f"the shortfall is 6, because the shortfall also carries each piece's OWN truncation — the "
    f"top block's AP does not yet extend {_AP_D} rows, and neither does the run's.  Reading the "
    f"two columns as the same number would be wrong; what is measured is that they have the same "
    f"support.  The threshold is arithmetic rather than asymptotic: a crossing pair is "
    f"~2 * (separation) apart in beta and eps is identically 0 from m = {EPS_CUT}, and with the "
    f"run placed midway the binding separation is ~k/2, which is why this settles later than a "
    f"two-piece split would.  This is the sequence HAVING converged, not a proof that it "
    f"converges — that needs the upper bound on M_n the arc still lacks",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E5 — no bound of the class is binding
# --------------------------------------------------------------------------------------------
print("E5  widening every bound of the class")
_t0 = time.time()
_TOPS_W = top_profiles(TMAX + 2, TUMAX + 2)
_Xblock_w = block_table(_TOPS_W)
print(f"    widened tops: {len(_TOPS_W)} profiles ({time.time()-_t0:.1f}s)", flush=True)
_t1 = time.time()
_BOTS_W = bot_profiles(BMAX + 1, BUMAX)
_Xbot_w = bot_table(_BOTS_W, pe_max=P_EXT_MAX + 4)
print(f"    widened bottoms: {len(_BOTS_W)} profiles ({time.time()-_t1:.1f}s)", flush=True)
_Xrun_w = run_table(ELL_MAX + 20)
_vj_w, _aj_w = join(_Xblock_w, _Xrun_w, _Xbot_w)
print(f"    e_inf (widened) = {mp.nstr(sc(_vj_w), 26)}   difference {_vj_w - _vj}")
print(f"    argmax: top {list(_aj_w[0])}, bottom {list(_aj_w[1])}, P = {_aj_w[2]}, "
      f"run {_aj_w[5]}")
check(
    "E5 widening every bound of the class moves neither e_inf nor its argmax",
    _vj_w == _vj and _aj_w[0] == _top and _aj_w[1] == _bot and _aj_w[5] == _ell,
    f"top rows {TMAX} -> {TMAX+2} and values {TUMAX} -> {TUMAX+2} ({len(TOPS)} -> "
    f"{len(_TOPS_W)} profiles), bottom rows {BMAX} -> {BMAX+1} ({len(BOTS)} -> {len(_BOTS_W)}), "
    f"run length {ELL_MAX} -> {ELL_MAX+20}, extension {P_EXT_MAX} -> {P_EXT_MAX+4}: e_inf is the "
    f"same scaled integer (difference {_vj_w - _vj}) and the argmax is the same shape.  Without "
    f"this the maximum would be an artefact of where the enumeration stopped, and e_inf would be "
    f"a statement about the search rather than about the problem — which is exactly what the "
    f"first version of this probe was, with every one of its caps binding at the argmax"
    if _vj_w == _vj else
    f"widening MOVED e_inf by {mp.nstr(sc(_vj_w - _vj), 8)} — the value was a bound artefact.  "
    f"New argmax: top {list(_aj_w[0])}, bottom {list(_aj_w[1])}, run {_aj_w[5]}, P = {_aj_w[2]}",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E6 — against the single-n reading the corpus carries
# --------------------------------------------------------------------------------------------
print("E6  against the single-n measurement #7294 used for e_inf")
_SCAL = json.load(open(os.path.join(_HERE, "rev-excess-scaling-exponent.witness.json")))
_last = _SCAL["scaling_R2"][-1]
_e_single = mp.mpf(_last["excess"])
_gap = _e_inf - _e_single
print(f"    #7294 at n = {_last['n']} (k = {_last['k']}): {mp.nstr(_e_single, 22)}")
print(f"    e_inf (this probe, converged):        {mp.nstr(_e_inf, 22)}")
print(f"    difference:                           {mp.nstr(_gap, 10)}")
check(
    "E6 e_inf sits above the single-n reading, as e_k increasing requires",
    _gap > 0,
    f"e_inf = {mp.nstr(_e_inf, 24)} against the {mp.nstr(_e_single, 18)} recorded at "
    f"n = {_last['n']} (k = {_last['k']}) — higher by {mp.nstr(_gap, 6)}, "
    f"{mp.nstr(_gap/_e_inf*100, 4)} % of e_inf.  It MUST be higher: e_k is increasing and that "
    f"row is a finite-k value of the same sequence, so a converged limit below it would mean one "
    f"of the two searches is wrong.  The sign is the check; the size is how much of kappa the "
    f"single-n reading was missing"
    if _gap > 0 else
    f"e_inf = {mp.nstr(_e_inf, 24)} is BELOW the finite-k reading {mp.nstr(_e_single, 18)} at "
    f"n = {_last['n']}, which e_k increasing forbids — this class is missing the shape the "
    f"heuristic found, so the reported e_inf is an understatement",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E7 — one edge energy, seen twice
# --------------------------------------------------------------------------------------------
print("E7  the two block energies")
print(f"    top    {list(_top)} (s_t = {_st}): {mp.nstr(sc(_vt), 24)}")
print(f"    bottom {list(_bot)} (s_b = {_sb}): {mp.nstr(sc(_vb), 24)}")
print(f"    difference: {_vt - _vb}   (scaled integer)")
_conj_top = [sum(1 for x in _top if x > j) for j in range(max(_top))] if _top else []
print(f"    transpose of the top block: {_conj_top}   (NOT the bottom block — see E7)")
print(f"    e_inf = 2 * E_edge + Xrun(2 * {_st}) = 2 * {mp.nstr(sc(_vt), 20)} + "
      f"({mp.nstr(sc(_vr), 20)})")
# and the same question one level up: are the two tables the same FUNCTION of the block sum, or
# do they only happen to agree at the argmax?
_shared = sorted(set(_Xblock) & set(_Xbot))
_table_diff = [(s, _Xblock[s][0] - _Xbot[s][0]) for s in _shared]
_agree_upto = max((s for s in _shared if all(d == 0 for t, d in _table_diff if t <= s)),
                  default=0)
_first_split = next((s for s, d in _table_diff if d != 0), None)
print(f"    over {len(_shared)} shared block sums the two tables agree for s <= {_agree_upto}"
      + (f" and first differ at s = {_first_split} by {dict(_table_diff)[_first_split]}"
         if _first_split is not None else " (everywhere)"))
check(
    "E7 the two block energies are EQUAL as exact integers — one edge energy, seen twice",
    _vt == _vb and _st == _sb,
    f"the top block {list(_top)} and the bottom block {list(_bot)} are different shapes found by "
    f"two searches that share no code path — one closed-form in the AP, one `delta_excess` in a "
    f"real frame — and their energies agree to every one of {SCALE_DIGITS} decimal places "
    f"(difference exactly {_vt - _vb}), with equal sums s_t = s_b = {_st}.  #7331 saw the same "
    f"equality for its block-plus-run edges and it survives here to the k-free blocks.  The "
    f"likely mechanism is that the staircase is self-conjugate and the hook multiset is a "
    f"transpose invariant — but these two tuples are NOT literally conjugate partitions: "
    f"{list(_top)} transposes to {_conj_top}, which is not {list(_bot)}.  #7331's witness calls "
    f"its own pair \'that conjugate pair\' and this probe repeated the claim before checking "
    f"it; the EQUALITY is measured to the last digit, the transpose correspondence between "
    f"these particular tuples is NOT, and identifying it is open.  So e_inf collapses to ONE "
    f"edge energy and one run: e_inf = 2 * E_edge + Xrun(2 * s), with E_edge = "
    f"{mp.nstr(sc(_vt), 24)}, s = {_st}, and Xrun({_ell}) = {mp.nstr(sc(_vr), 24)}.  The "
    f"equality is also a check on the two evaluators, not only an observation about the shapes.  "
    f"One level up, the two TABLES agree as functions of the block sum for s <= {_agree_upto}"
    + (f" and first part at s = {_first_split}, where the top table is higher by "
       f"{mp.nstr(sc(dict(_table_diff)[_first_split]), 4)}.  WHY they part is not measured "
       f"here — a row cap on one side is the obvious candidate and has not been checked — and "
       f"it does not reach e_inf, whose argmax is at s = {_st}"
       if _first_split is not None else ", i.e. everywhere they are both defined")
    if (_vt == _vb and _st == _sb) else
    f"the two block energies DIFFER by {mp.nstr(sc(_vt - _vb), 8)} (s_t = {_st}, s_b = {_sb}) — "
    f"the transpose invariance of the hook multiset makes that unexpected, so either one of the "
    f"two evaluators is wrong or the correspondence is not what it looks like",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  e_inf = {mp.nstr(_e_inf, 30)}")
print(f"        = Xblock{list(_top)} + Xrun({_ell}) + Xbot{list(_bot)}  (P = {_pe})")
print(f"        = {mp.nstr(sc(_vt), 22)} + ({mp.nstr(sc(_vr), 22)}) + {mp.nstr(sc(_vb), 22)}")
print(f"  settled from k = {_first_settled} (n = {_first_settled*(_first_settled+1)//2})"
      if _first_settled else "  never settled")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {"script": "computations/deltalambda/rev_e_infinity_edge_limit_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "e_inf, the last unknown constant in the REV_n asymptotics, as a three-piece "
        "decomposition rather than a single-n measurement.  The maximiser's run of -1 has a FREE "
        "position (#7323), and a free position goes to infinity because displaced rows interact "
        "only through eps, which dies geometrically -- so at the optimum the run sits far from "
        "both blocks and the excess splits into three mutually non-interacting k-free pieces: "
        "e_inf = max over (s_t, s_b) of Xblock(s_t) + Xrun(s_t+s_b) + Xbot(s_b), the run length "
        "forced by sum u = 0.  That also explains #7331's non-additivity: two isolated edges "
        "each carry their own run, so their sum double-counts one run's interface.  Exhaustive "
        "over an explicit shape class -- a rigorous LOWER bound on the true e_k -- where the "
        "class is the shape #7305's full enumeration independently found at every k <= 12 and "
        "every one of its bounds is widened in E5.  NOT a proof that the limit exists: the "
        "upper bound on M_n is still open."
    ),
    "constants": {
        "ln_q0": mp.nstr(LNQ, 30), "scale_digits": SCALE_DIGITS,
        "eps_vanishes_at_m": EPS_CUT, "ap_tail_depth": _AP_D,
    },
    "shape_class": {
        "top_rows_max": TMAX, "top_value_max": TUMAX, "top_profiles": len(TOPS),
        "bottom_rows_max": BMAX, "bottom_value_max": BUMAX, "bottom_profiles": len(BOTS),
        "run_length_max": ELL_MAX, "extension_max": P_EXT_MAX,
        "k_bot": K_BOT, "k_big": K_BIG, "separation": SEP,
    },
    "exhaustive_maximisers_E1": _e1,
    "upstream_enumeration_kmax": _EX_KMAX,
    "k40_against_7331_E2": {
        "class": mp.nstr(sc(_best40), 24), "pr7331": mp.nstr(_k40_ref, 24),
        "difference_scaled": _e2_gap, "recording_floor_scaled": _e2_floor,
        "argmax": {"top": list(_arg40[0]), "bottom": list(_arg40[1]), "run_head": _arg40[2],
                   "run_length": _arg40[3], "extension": _arg40[4]},
    },
    "three_piece_identity_E3": {
        "k": K_BIG, "crossing_pairs_scaled": _cross,
        "definition_scaled": str(_full), "sum_of_pieces_scaled": str(_vj),
        "piece_in_frame_vs_k_free": {"top": _pt - _vt, "run": _pr - _vr, "bottom": _pb - _vb},
    },
    "separation_scan_E3b": _sepscan,
    "finite_k_ladder_E4": _ladder,
    "one_edge_energy_E7": {
        "top_block": list(_top), "bottom_block": list(_bot), "s_t": _st, "s_b": _sb,
        "difference_scaled": _vt - _vb, "E_edge": mp.nstr(sc(_vt), 30),
        "top_block_transpose": _conj_top,
        "transpose_correspondence_identified": False,
        "run": mp.nstr(sc(_vr), 30), "identity": "e_inf = 2 * E_edge + Xrun(2 * s)",
        "tables_agree_up_to_block_sum": _agree_upto, "tables_first_differ_at": _first_split,
        "table_difference_by_block_sum": {str(s): d for s, d in _table_diff},
    },
    "settled_from_k": _first_settled,
    "widening_E5": {
        "top_profiles": len(_TOPS_W), "bottom_profiles": len(_BOTS_W),
        "run_length_max": ELL_MAX + 20, "extension_max": P_EXT_MAX + 4,
        "e_inf_widened": mp.nstr(sc(_vj_w), 30), "difference_scaled": _vj_w - _vj,
        "argmax": {"top": list(_aj_w[0]), "bottom": list(_aj_w[1]), "extension": _aj_w[2],
                   "run_length": _aj_w[5]},
    },
    "against_single_n_E6": {
        "n": _last["n"], "k": _last["k"], "single_n_excess": _last["excess"],
        "e_inf": mp.nstr(_e_inf, 30), "difference": mp.nstr(_gap, 20),
    },
    "e_infinity": {
        "value": mp.nstr(_e_inf, 30), "scaled": str(_vj),
        "top_block": mp.nstr(sc(_vt), 30), "run": mp.nstr(sc(_vr), 30),
        "bottom_block": mp.nstr(sc(_vb), 30),
        "limiting_shape": {"top": list(_top), "run_length": _ell, "bottom": list(_bot),
                           "extension": _pe, "s_t": _st, "s_b": _sb},
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "The REV_n excess splits into three independent k-free pieces -- a top block, a run of "
        "-1 whose length is forced, and a bottom block -- because the run's free position runs "
        "to infinity.  e_inf is the maximum of their sum, and the rung where e_k stops moving is "
        "identified rather than guessed: the crossing pair term and the deficit from the limit "
        "vanish together.  It remains a lower bound on the true limit, exhaustive over a class "
        "whose every bound is checked non-binding."
    ),
}
_out = os.path.join(_HERE, "rev-e-infinity-edge-limit.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
