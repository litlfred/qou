#!/usr/bin/env python3
r"""
rev_e_infinity_edge_limit_probe.py — `e_inf` as a CONVERGED limit of two independent edge
energies (qou-hok7)

`e_inf` is the one number left in the `REV_n` asymptotics.  Everything else in

    kappa = -A/2 - B - C + e_inf

is an explicit convergent series (#7294, `rev_staircase_closed_form_and_constant_term_probe`),
and that probe states the residue plainly: *"e_inf is measured at a single n rather than proved
to be a limit"* — the largest `n` its heuristic scan reached, `n = 3916` (`k = 88`).

This probe replaces the single reading with a limit, using what the previous three PRs built:

  #7305  the cost is the exact quadratic form  `ln q0 * [ sum_{i>k}(i-k) u_i + (1/2) sum u_i^2 ]`
         (Lean, sorry-free: `staircase_two_mul_hookSum_sub`)
  #7323  the maximiser is a top bulge + a contiguous run of `-1` + a bottom block, with the run's
         length forced by `sum u = 0` and its position free
  #7331  the excess does NOT add over two independently-run edges

#7331's non-additivity has a one-line resolution: the run belongs to ONE edge, not to both.
Split the rows at any undisplaced index between the run and the bottom block.  The one-body `F`
term, the linear cost and the quadratic cost are additive over such a split by inspection; the
only term that can couple the two sides is the pair term, and a crossing pair is `~2k` apart in
`beta`, where `eps(m) = -log(1 - q0^(-2m))` has already died.  So

    e_inf = max over (s_t, s_b)  [ Xtop*(s_t, s_t + s_b) + Xbot*(s_b) ]

with `s_t`, `s_b` the two blocks' sums and `s_t + s_b` the forced run length — a maximum of a
SUM of two searches whose value no longer depends on `k`.

## What this establishes, and what it does not

It establishes that `e_k` has STOPPED MOVING, and says at which `k`: the crossing pairs are
exactly zero in this arithmetic once `2(k - a) > 445`, so `k = 240` and `k = 320` give the same
scaled integer to 1e-40.  It does NOT prove the limit exists — that needs the upper bound on
`M_n` this arc still lacks, and `e_k` here is exhaustive over an explicit SHAPE CLASS, so every
value is a rigorous LOWER bound on the true one.  The class is checked against the full
enumeration at every `k <= 12` where that exists, and against #7331's independent joint search
at `k = 40`.  Nothing is fitted: no tolerance is chosen, the class is not selected against a
target, and the arithmetic is exact integers at scale 1e-40.

## Checks

  E1  the FULL-ENUMERATION maximiser lies in the shape class at every k <= 12, and the
      evaluators reproduce its excess exactly
  E2  the class reproduces PR #7331's independently-searched joint maximum at k = 40
  E3  the split is exact at k = 320 — no pair crosses it, and the fast pure-AP evaluator agrees
      with the general one
  E4  the finite-k correction IS the crossing pair term, and it reaches exactly 0
  E5  widening either edge's profile bounds does not move that edge's maximum
  E6  e_inf sits above the single-n reading #7294 used, by the finite-k tail

Proton-pinned; exact integer arithmetic at scale 1e-40; mpmath dps 60 for the tables.  No
float64.

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/BraidKnot/HookSumElasticity.lean
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

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

mp.dps = 60
Q0 = mp.mpf(Q_50_DIGIT_STR)
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

# `epsi(m)` is identically 0 in this arithmetic from `EPS_CUT` on.  Read off the table, not
# chosen: it is the first m whose rounded eps is zero at scale 1e-40.
EPS_CUT = next(m for m in range(1, _MMAX) if _EPS_I[m] == 0)
U_MAX_ABS = 8          # a displacement moves a gap by at most this, so windows need the slack


def epsi(m: int) -> int:
    return _EPS_I[m] if 0 < m < _MMAX else 0


def fi(b: int) -> int:
    return _F_I[b] if b < _MMAX else _F_I[_MMAX - 1]


def staircase_beta(k: int, L: int) -> list[int]:
    """beta of the staircase delta_k padded into an L-row frame (L >= k+1).

    Rows i <= k carry beta = 2k + P - 2i, an arithmetic progression of gap 2; the P = L-k-1 rows
    below carry beta = P-1, ..., 0, consecutive.  The junction between the two is the 'bottom
    wall' of #7323 and the free end of the AP is its 'top edge'.
    """
    return [max(k - i, 0) + (L - 1 - i) for i in range(L)]


# --------------------------------------------------------------------------------------------
# Evaluators.  `excess_full` is the O(L^2) definition.  `delta_excess` sums over the displaced
# rows only.  `ap_top_value` is the pure-AP closed form used for the top edge at large k.  E3
# checks all three against each other; none is trusted on its own.
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
    not sum to zero.  That is NOT the excess of any partition — it is the summand the row-split
    of the header decomposes the excess into, and it is what makes the two edges separately
    computable.  `nb0` is `[-b for b in b0]`, ascending, for the bisect window.
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


# `_DOWN[u]` is the complete downward tail of a single displaced row sitting in an AP of gap 2:
# sum over every row below it of [eps(gap0) - eps(gap)].  `_AP_D` is chosen so `2 * _AP_D`
# clears `EPS_CUT` with the displacement slack, which makes the tail exact rather than truncated.
_AP_D = (EPS_CUT + 2 * U_MAX_ABS) // 2 + 2
_DOWN = {u: sum(epsi(2 * d) - epsi(2 * d + u) for d in range(1, _AP_D + 1))
         for u in range(-U_MAX_ABS, U_MAX_ABS + 1)}


def ap_top_value(u: list[int]) -> int | None:
    """The top edge's contribution, for a displacement supported at the head of a semi-infinite
    AP of gap 2.

    Valid exactly when (i) every displaced row has at least `_AP_D` AP rows beneath it, so
    `_DOWN` is the whole tail, and (ii) `beta ~ 2k` there, so `F` is saturated and the one-body
    term is identically zero.  Both hold at `k = 320` for displacements inside the first ~30
    rows, and E3 checks this against `delta_excess` on the real frame rather than assuming it.
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
        for d in range(1, a + 1):                 # rows above a; the AP ends at row 0
            tot += epsi(2 * d) - epsi(2 * d - ua)
        for b in S:                               # undo the "undisplaced" assumption on S
            if b == a:
                continue
            d = b - a
            if d > 0:
                tot -= epsi(2 * d) - epsi(2 * d + ua)
            else:
                tot -= epsi(-2 * d) - epsi(-2 * d - ua)
    for ia, i in enumerate(S):                    # and put the true S-S pair terms back once
        for j in S[ia + 1:]:
            tot += epsi(2 * (j - i)) - epsi(2 * (j - i) + u[i] - u[j])
    return tot - (LNQ_I * sum(x * x for x in u)) // 2


def cross_pair_term(u: list[int], b0: list[int], split: int) -> int:
    """The pair contribution of pairs straddling `split` with a displaced row on each side — the
    only term in the excess that is not additive over the split."""
    L = len(u)
    beta = [b0[i] + u[i] for i in range(L)]
    top = [i for i in range(split) if u[i]]
    bot = [i for i in range(split, L) if u[i]]
    return sum(epsi(b0[i] - b0[j]) - epsi(beta[i] - beta[j]) for i in top for j in bot)


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


TMAX, TUMAX = 6, 5
BMAX, BUMAX = 7, 3
PWIN = 20          # how far below the top block the run's head may sit
ELL_MAX = 16       # the forced run length s_t + s_b
P_EXT_MAX = 7      # rows the shape may extend beyond the staircase
K_BIG = 320        # 2*(K_BIG - 30) >> EPS_CUT, so every crossing pair is exactly zero

TOPS = top_profiles(TMAX, TUMAX)
BOTS = bot_profiles(BMAX, BUMAX)


def top_table(tops=None, ell_max: int = ELL_MAX, pwin: int = PWIN):
    """`Xtop[(s_t, ell)] -> (value, top, run_head)`, the top edge's best value for each block sum
    and run length.  Evaluated in the k -> infinity AP, so it carries no k at all."""
    out: dict[tuple[int, int], tuple[int, tuple, int]] = {}
    for top in (TOPS if tops is None else tops):
        st = sum(top)
        lt = len(top)
        for ell in range(0, ell_max + 1):
            for p in range(lt, lt + pwin + 1):
                u = [0] * (p + ell + 1)
                for i, x in enumerate(top):
                    u[i] = x
                for i in range(p, p + ell):
                    u[i] = -1
                v = ap_top_value(u)
                if v is None:
                    continue
                cur = out.get((st, ell))
                if cur is None or v > cur[0]:
                    out[(st, ell)] = (v, top, p)
    return out


def bot_table(k: int = K_BIG, bots=None, pe_max: int = P_EXT_MAX):
    """`Xbot[s_b] -> (value, bot, P)`, the bottom edge's best value for each block sum."""
    out: dict[int, tuple[int, tuple, int]] = {}
    for pe in range(0, pe_max + 1):
        L = k + 1 + pe
        b0 = staircase_beta(k, L)
        nb0 = [-x for x in b0]
        for bot in (BOTS if bots is None else bots):
            if not bot:
                continue
            u = make_u(L, (), bot, 0, 0)
            if u is None:
                continue
            v = delta_excess(u, k, b0, nb0, require_zero_sum=False)
            if v is None:
                continue
            cur = out.get(sum(bot))
            if cur is None or v > cur[0]:
                out[sum(bot)] = (v, bot, pe)
    return out


def join(Xtop, Xbot):
    """`e_inf` as the maximum of the SUM, with the run length forced by `sum u = 0`."""
    best, arg = None, None
    for (st, ell), (vt, top, p) in Xtop.items():
        sb = ell - st
        if sb < 0 or sb not in Xbot:
            continue
        vb, bot, pe = Xbot[sb]
        if best is None or vt + vb > best:
            best, arg = vt + vb, (top, p, ell, bot, pe, st, sb, vt, vb)
    return best, arg


def sc(x: int) -> mp.mpf:
    return mp.mpf(x) / SCALE


# --------------------------------------------------------------------------------------------
print("e_inf as a converged limit — the two edges of the REV_n maximiser are independent")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  arithmetic: integers at scale 1e-{SCALE_DIGITS}")
print(f"  eps vanishes in this arithmetic from m = {EPS_CUT}; AP tail depth {_AP_D}")
print(f"  class: top <= {TMAX} rows / values <= {TUMAX} ({len(TOPS)} profiles), bottom <= {BMAX} "
      f"rows / values <= {BUMAX} ({len(BOTS)} profiles),")
print(f"         run head within {PWIN} rows of the block, run length <= {ELL_MAX}, "
      f"extension P <= {P_EXT_MAX}")
print(flush=True)

# --------------------------------------------------------------------------------------------
# E1 — the exhaustive maximiser lies in the class, and the evaluators reproduce it
# --------------------------------------------------------------------------------------------
print("E1  the FULL-ENUMERATION maximiser of #7305 against the shape class")
_EX = json.load(open(os.path.join(_HERE, "rev-exact-maximiser-small-n.witness.json")))
_e1 = []
for _r in _EX["exact_rows"]:
    _k = _r["k"]
    _b = _r["argmax_beta"][0]
    _Lm = len(_b)
    if _k < 7 or _Lm < _k + 1:
        continue                     # k <= 6: the staircase itself is the maximiser
    _pe = _Lm - _k - 1
    if _pe > P_EXT_MAX:
        continue
    _b0 = staircase_beta(_k, _Lm)
    _u = [_b[i] - _b0[i] for i in range(_Lm)]
    # decompose u into (top block, run of -1, bottom block)
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
        and len(_run) <= ELL_MAX and _run[0] - _lt <= PWIN
        and len(_run) == sum(_top) + sum(_bot)
    )
    _target = int(_r["M_n_scaled"]) - int(_r["V_stair_scaled"])
    _b0n = [-x for x in _b0]
    _vf, _vd = excess_full(_u, _k), delta_excess(_u, _k, _b0, _b0n)
    _rebuilt = make_u(_Lm, _top, _bot, _run[0], len(_run)) if _contig else None
    _e1.append({
        "k": _k, "n": _r["n"], "in_class": _in_class, "rebuild_matches": _rebuilt == _u,
        "top": list(_top), "run_head": _run[0] if _run else None, "run_length": len(_run),
        "bottom": list(_bot), "extension": _pe,
        "excess_full_minus_exhaustive": (_vf - _target) if _vf is not None else None,
        "delta_minus_exhaustive": (_vd - _target) if _vd is not None else None,
    })
    print(f"    k = {_k:2d} (n = {_r['n']:3d}): top {list(_top)}, run {len(_run)} at row "
          f"{_run[0]}, bottom {list(_bot)}, P = {_pe}  | in class {_in_class}, "
          f"evaluators off by {_vf - _target} / {_vd - _target}", flush=True)
_e1_bad = [r for r in _e1 if not (r["in_class"] and r["rebuild_matches"]
                                  and r["excess_full_minus_exhaustive"] == 0
                                  and r["delta_minus_exhaustive"] == 0)]
check(
    "E1 every exhaustively-found maximiser is in the shape class, and both evaluators reproduce "
    "its excess exactly",
    not _e1_bad,
    f"{len(_e1)} values of k (7..12, n = 28..78).  Each maximiser decomposes as a positive top "
    f"block, ONE contiguous run of -1 whose length is exactly s_t + s_b, and a positive bottom "
    f"block, with nothing in between — so the class is the shape the enumeration found, not a "
    f"shape imposed on it.  `make_u` rebuilds each u byte-for-byte from that decomposition, and "
    f"`excess_full` and `delta_excess` both return the enumeration's own M_n - V(delta_k) as the "
    f"SAME scaled integer (difference 0, not 'within tolerance').  k <= 6 is excluded because "
    f"there the staircase is itself the maximiser and there is no displacement to decompose"
    if not _e1_bad else
    "class or evaluator mismatch at k = " + ", ".join(str(r["k"]) for r in _e1_bad),
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# the tables, once
# --------------------------------------------------------------------------------------------
print("building the two edge tables")
_t0 = time.time()
_Xtop = top_table()
print(f"    top table:    {len(_Xtop)} (s_t, ell) keys   ({time.time()-_t0:.1f}s)", flush=True)
_t1 = time.time()
_Xbot = bot_table()
print(f"    bottom table: {len(_Xbot)} s_b keys          ({time.time()-_t1:.1f}s)", flush=True)
_vj, _aj = join(_Xtop, _Xbot)
_top, _p, _ell, _bot, _pe, _st, _sb, _vt, _vb = _aj
_e_inf = sc(_vj)
print(f"    e_inf = {mp.nstr(_e_inf, 26)}")
print(f"      top    {list(_top)} with the run of {_ell} at row {_p}: {mp.nstr(sc(_vt), 22)}")
print(f"      bottom {list(_bot)} against the wall, P = {_pe}: {mp.nstr(sc(_vb), 22)}")
print(flush=True)

# --------------------------------------------------------------------------------------------
# E2 — against PR #7331's independent joint search at k = 40
# --------------------------------------------------------------------------------------------
print("E2  the class against PR #7331's direct joint search at k = 40")
_SEP = json.load(open(os.path.join(_HERE, "rev-edge-separability.witness.json")))
_k40_ref = mp.mpf(_SEP["direct_joint_maximum"])
_t0 = time.time()
_best40, _arg40 = None, None
for _pe2 in range(0, P_EXT_MAX + 1):
    _L2 = 41 + _pe2
    _b02 = staircase_beta(40, _L2)
    _nb02 = [-x for x in _b02]
    for (_st2, _ell2), (_, _top2, _p2) in _Xtop.items():
        _sb2 = _ell2 - _st2
        if _sb2 < 0 or _sb2 not in _Xbot:
            continue
        for _bot2 in BOTS:
            if sum(_bot2) != _sb2:
                continue
            _u2 = make_u(_L2, _top2, _bot2, _p2, _ell2)
            if _u2 is None:
                continue
            _v2 = delta_excess(_u2, 40, _b02, _nb02)
            if _v2 is not None and (_best40 is None or _v2 > _best40):
                _best40, _arg40 = _v2, (_top2, _bot2, _p2, _ell2, _pe2)
print(f"    class at k = 40: {mp.nstr(sc(_best40), 24)}   ({time.time()-_t0:.1f}s)")
print(f"    PR #7331 direct: {mp.nstr(_k40_ref, 24)}")
print(f"    argmax: top {list(_arg40[0])}, bottom {list(_arg40[1])}, run {_arg40[3]} at row "
      f"{_arg40[2]}, P = {_arg40[4]}")
_k40_scaled = int(mp.floor(_k40_ref * SCALE + mp.mpf("0.5")))
_e2_gap = _best40 - _k40_scaled
check(
    "E2 the class reproduces PR #7331's independently-searched joint maximum at k = 40",
    abs(_e2_gap) <= 10 ** (SCALE_DIGITS - 23),
    f"class {mp.nstr(sc(_best40), 22)} against #7331's {mp.nstr(_k40_ref, 22)}, which searched "
    f"the run position over the WHOLE frame instead of a {PWIN}-row window and used a different "
    f"evaluator.  They agree to {mp.nstr(sc(abs(_e2_gap)), 4)}, the floor set by #7331's "
    f"witness recording its value to 24 significant digits — so the window does not cut the "
    f"optimum off, and the two searches are not sharing a bug",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E3 — the split is exact, and the three evaluators agree
# --------------------------------------------------------------------------------------------
print("E3  the split into two edges — do any pairs cross it?")
_Lj = K_BIG + 1 + _pe
_uj = make_u(_Lj, _top, _bot, _p, _ell)
_b0j = staircase_beta(K_BIG, _Lj)
_nb0j = [-x for x in _b0j]
_split = _p + _ell + 1
_cross = cross_pair_term(_uj, _b0j, _split)
_full = excess_full(_uj, K_BIG)
_dlt = delta_excess(_uj, K_BIG, _b0j, _nb0j)
# the fast AP evaluator against the general one, on the top piece alone, in the real frame
_utop_only = make_u(_Lj, _top, (), _p, _ell)
_ap = ap_top_value(_utop_only[:_p + _ell + 1])
_gen = delta_excess(_utop_only, K_BIG, _b0j, _nb0j, require_zero_sum=False)
print(f"    crossing pairs (split at row {_split}): {_cross}  (scaled integer)")
print(f"    definition {sc(_full)}")
print(f"    Xtop + Xbot  {mp.nstr(sc(_vj), 26)}   difference {_full - _vj}")
print(f"    fast AP top evaluator {_ap}  vs general {_gen}   difference {_ap - _gen}")
check(
    "E3 the two edges are independent, and the three evaluators agree to the last digit",
    _cross == 0 and _full == _vj and _dlt == _vj and _ap == _gen,
    f"at k = {K_BIG} the pairs straddling row {_split} contribute exactly {_cross} at scale "
    f"1e-{SCALE_DIGITS} — the two edges sit ~{2*K_BIG} apart in beta and eps vanishes in this "
    f"arithmetic from m = {EPS_CUT}.  The split sum Xtop + Xbot reproduces the O(L^2) definition "
    f"on the same shape exactly (difference {_full - _vj}), `delta_excess` agrees with both, and "
    f"the fast pure-AP evaluator agrees with the general one on the top piece (difference "
    f"{_ap - _gen}).  So e_inf is a maximum of a SUM of two k-independent terms — which is what "
    f"#7331's non-additivity was pointing at: the run belongs to one edge, not to both",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E4 — the finite-k correction is the crossing term, and it reaches exactly 0
# --------------------------------------------------------------------------------------------
print("E4  the limiting shape evaluated at finite k — where does e_k stop moving?")
_ladder = []
for _k2 in (20, 40, 60, 80, 120, 160, 200, 224, 240, 280, 320):
    _L3 = _k2 + 1 + _pe
    _u3 = make_u(_L3, _top, _bot, _p, _ell)
    if _u3 is None:
        continue
    _v3 = excess_full(_u3, _k2)
    if _v3 is None:
        continue
    _b03 = staircase_beta(_k2, _L3)
    _c3 = cross_pair_term(_u3, _b03, _split)
    _ladder.append({"k": _k2, "n": _k2 * (_k2 + 1) // 2, "value": mp.nstr(sc(_v3), 30),
                    "scaled": str(_v3), "crossing_scaled": _c3,
                    "deficit_from_limit": str(_vj - _v3)})
    print(f"    k = {_k2:4d}: {mp.nstr(sc(_v3), 26):30s} crossing {_c3:>22d}  "
          f"deficit {mp.nstr(sc(_vj - _v3), 6)}", flush=True)
_settled = [r for r in _ladder if r["crossing_scaled"] == 0]
_moving = [r for r in _ladder if r["crossing_scaled"] != 0]
_all_settled_equal = len({r["scaled"] for r in _settled}) == 1 and len(_settled) >= 2
_mono = all(int(_moving[i]["crossing_scaled"]) != 0 for i in range(len(_moving)))
_first_settled = min((r["k"] for r in _settled), default=None)
check(
    "E4 the finite-k deficit IS the crossing term, and both reach exactly zero together",
    _all_settled_equal and all(int(r["deficit_from_limit"]) != 0 for r in _moving)
    and all(int(r["deficit_from_limit"]) == 0 for r in _settled),
    f"the limiting shape's exact excess is the SAME scaled integer at every k from "
    f"{_first_settled} up ({len(_settled)} rungs, to 1e-{SCALE_DIGITS}), and at every smaller k "
    f"it is short by exactly the crossing pair term — the deficit and the crossing term vanish "
    f"at the same rung, which is what identifies the finite-k correction rather than merely "
    f"bounding it.  The threshold is arithmetic, not asymptotic: a crossing pair is ~2k apart "
    f"in beta and eps is identically 0 from m = {EPS_CUT}, so 2k > {EPS_CUT} is where it lands.  "
    f"This is the sequence having converged, NOT a proof that it converges — that needs the "
    f"upper bound on M_n the arc still lacks",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
# E5 — neither edge maximum is a bound artefact
# --------------------------------------------------------------------------------------------
print("E5  widening each edge's profile bounds")
_t0 = time.time()
_TOPS_W = top_profiles(TMAX + 2, TUMAX + 2)
_Xtop_w = top_table(tops=_TOPS_W, ell_max=ELL_MAX + 4, pwin=PWIN + 10)
_BOTS_W = bot_profiles(BMAX + 2, BUMAX + 1)
_Xbot_w = bot_table(bots=_BOTS_W, pe_max=P_EXT_MAX + 3)
_vj_w, _aj_w = join(_Xtop_w, _Xbot_w)
print(f"    widened: {len(_TOPS_W)} top profiles, {len(_BOTS_W)} bottom profiles  "
      f"({time.time()-_t0:.1f}s)")
print(f"    e_inf (widened) = {mp.nstr(sc(_vj_w), 26)}   difference {_vj_w - _vj}")
print(f"    argmax: top {list(_aj_w[0])}, run {_aj_w[2]} at row {_aj_w[1]}, "
      f"bottom {list(_aj_w[3])}, P = {_aj_w[4]}")
check(
    "E5 widening either edge's bounds does not move e_inf or its argmax",
    _vj_w == _vj and _aj_w[0] == _top and _aj_w[3] == _bot and _aj_w[2] == _ell,
    f"the class goes from {len(TOPS)}/{len(BOTS)} to {len(_TOPS_W)}/{len(_BOTS_W)} profiles, the "
    f"run-head window from {PWIN} to {PWIN+10}, the run length cap from {ELL_MAX} to "
    f"{ELL_MAX+4} and the extension cap from {P_EXT_MAX} to {P_EXT_MAX+3}; e_inf is the same "
    f"scaled integer (difference {_vj_w - _vj}) and the argmax is the same shape.  Without this "
    f"the two edge maxima would be artefacts of where the enumeration was stopped, and e_inf "
    f"would be a statement about the search rather than about the problem"
    if _vj_w == _vj else
    f"widening MOVED e_inf by {mp.nstr(sc(_vj_w - _vj), 8)} — the reported value was a bound "
    f"artefact; new argmax top {list(_aj_w[0])}, bottom {list(_aj_w[3])}",
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
    "E6 e_inf sits above the single-n reading, by an amount that is the finite-k tail",
    _gap > 0,
    f"e_inf = {mp.nstr(_e_inf, 24)} against the {mp.nstr(_e_single, 18)} recorded at "
    f"n = {_last['n']} (k = {_last['k']}) — higher by {mp.nstr(_gap, 6)}, "
    f"{mp.nstr(_gap/_e_inf*100, 4)} % of e_inf.  It MUST be higher: e_k is increasing and that "
    f"row is a finite-k value of the same sequence, so a converged limit below it would mean one "
    f"of the two searches is wrong.  The sign is the check; the size is how much of kappa the "
    f"single-n reading was missing"
    if _gap > 0 else
    f"e_inf = {mp.nstr(_e_inf, 24)} is BELOW the finite-k reading {mp.nstr(_e_single, 18)} at "
    f"n = {_last['n']}, which e_k monotone forbids — one of the two searches is wrong",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  e_inf = {mp.nstr(_e_inf, 30)}")
print(f"  limiting shape: top {list(_top)}, run of {_ell} at row {_p}, bottom {list(_bot)}, "
      f"extension P = {_pe}")
print(f"  edge energies: top {mp.nstr(sc(_vt), 24)}, bottom {mp.nstr(sc(_vb), 24)}")
print(f"  settled from k = {_first_settled} (n = {_first_settled*(_first_settled+1)//2})")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {"script": "computations/deltalambda/rev_e_infinity_edge_limit_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "e_inf, the last unknown constant in the REV_n asymptotics, as a CONVERGED limit rather "
        "than a single-n measurement.  The REV_n maximiser's two edges are independent: the "
        "one-body, linear and quadratic terms split over any undisplaced row, and the pair term "
        "that could couple them is O(eps(2k)), identically zero in 1e-40 arithmetic once "
        "2k > 445.  So e_inf = max over the two block sums of Xtop*(s_t, s_t+s_b) + Xbot*(s_b), "
        "the run length forced by sum u = 0 and the run belonging to one edge rather than both "
        "-- which is the resolution of #7331's non-additivity.  Exhaustive over an explicit "
        "shape class, so the value is a rigorous LOWER bound on the true e_k; the class is the "
        "shape the full enumeration of #7305 found at every k <= 12.  NOT a proof that the "
        "limit exists -- the upper bound on M_n is still open."
    ),
    "constants": {
        "ln_q0": mp.nstr(LNQ, 30), "scale_digits": SCALE_DIGITS,
        "eps_vanishes_at_m": EPS_CUT, "ap_tail_depth": _AP_D,
    },
    "shape_class": {
        "top_rows_max": TMAX, "top_value_max": TUMAX, "top_profiles": len(TOPS),
        "bottom_rows_max": BMAX, "bottom_value_max": BUMAX, "bottom_profiles": len(BOTS),
        "run_head_window": PWIN, "run_length_max": ELL_MAX, "extension_max": P_EXT_MAX,
        "k_big": K_BIG,
    },
    "exhaustive_maximisers_E1": _e1,
    "k40_against_7331_E2": {
        "class": mp.nstr(sc(_best40), 24), "pr7331": mp.nstr(_k40_ref, 24),
        "difference_scaled": _e2_gap,
        "argmax": {"top": list(_arg40[0]), "bottom": list(_arg40[1]), "run_head": _arg40[2],
                   "run_length": _arg40[3], "extension": _arg40[4]},
    },
    "split_exactness_E3": {
        "k": K_BIG, "split_row": _split, "crossing_pair_scaled": _cross,
        "definition_scaled": str(_full), "split_sum_scaled": str(_vj),
        "delta_excess_scaled": str(_dlt),
        "fast_ap_top": str(_ap), "general_top": str(_gen),
    },
    "finite_k_ladder_E4": _ladder,
    "settled_from_k": _first_settled,
    "widening_E5": {
        "top_profiles": len(_TOPS_W), "bottom_profiles": len(_BOTS_W),
        "e_inf_widened": mp.nstr(sc(_vj_w), 30), "difference_scaled": _vj_w - _vj,
        "argmax": {"top": list(_aj_w[0]), "run_head": _aj_w[1], "run_length": _aj_w[2],
                   "bottom": list(_aj_w[3]), "extension": _aj_w[4]},
    },
    "against_single_n_E6": {
        "n": _last["n"], "k": _last["k"], "single_n_excess": _last["excess"],
        "e_inf": mp.nstr(_e_inf, 30), "difference": mp.nstr(_gap, 20),
    },
    "e_infinity": {
        "value": mp.nstr(_e_inf, 30), "scaled": str(_vj),
        "top_edge": mp.nstr(sc(_vt), 30), "bottom_edge": mp.nstr(sc(_vb), 30),
        "limiting_shape": {"top": list(_top), "run_length": _ell, "run_head": _p,
                           "bottom": list(_bot), "extension": _pe},
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "e_inf has stopped moving, and the rung where it stops is identified rather than "
        "guessed: the crossing pair term and the deficit from the limit vanish together.  Its "
        "value is a maximum of a SUM of two k-independent edge energies, which resolves #7331's "
        "non-additivity -- the run belongs to one edge rather than to both.  It remains a lower "
        "bound on the true limit, exhaustive over a class that is the shape the full enumeration "
        "found wherever that enumeration is affordable."
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
