"""The e_inf join closes WITHOUT G1: a per-sum bound on the bottom edge, by Lagrange multiplier.

Bean `qou-as81`.  Follow-up to `rev_e_infinity_xbot_lnatural_probe.py`, which certifies
`sup Xbot = 2.159802376118285961604` over every frame and block length and so cuts the join's
window to `s_t + s_b <= 25` without G1.  That is not yet the closure.  The join over the window
(`rev_e_infinity_block_sup_relaxation_probe.py`, P9) scores the bottom block with the TOP
block's best value at the same sum, i.e. it still substitutes `Xbot(s) := Xblock(s)` inside
the window.  A single `sup` bound on `Xbot` is too weak there: at `(s_t, s_b) = (8, 8)`, where
`e_inf` is attained, it would add `2.1598 - 1.9654` and overshoot.  The window needs `Xbot(s)`
bounded for each `s` separately.

## The bound

For a multiplier `mu`, `G(u) - mu * sum_j u_j` is still L-natural-concave (a linear term), so
its integer maximum `h(mu)` is certified by the same min cut, and weak duality gives

    Xbot(s)  <=  h(mu) + mu * s        for every s and every mu.

Both lemmas of the L-natural probe carry over for `mu >= 0`: the tail bracket must stay below
`(ln q0)/2 + mu` (J2 measures it), and the wall inequality becomes `eps(1) - mu < ln q0 (pe + 1)`,
so frames beyond the first `pe*` where it holds add nothing (J3).

## Checks

  J1  per-multiplier certified maxima `h(mu)`: no `+-chi_S` move improves, support inside N
  J2  the tail lemma with the multiplier, at every frame and multiplier
  J3  the wall inequality fixes the last frame `pe*(mu)` that needs computing
  J4  the join over `s_t + s_b <= CUT`, with the exact top value and the per-sum bottom bound,
      never exceeds #7335's `e_inf`: the window's maximum is `e_inf`, and G1 is not used

`CUT` is read from the L-natural witness, which must be all-green.  Proton-pinned; mp.dps 25.

-- Ref: [murota2003] Discrete Convex Analysis, SIAM, 2003, Ch. 7 (L-natural optimality criterion)
"""

from __future__ import annotations

import functools
import json
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

# The L-natural probe's definitions (split, min cut, ascent), executed up to its banner.
_SRC = os.path.join(_HERE, "rev_e_infinity_xbot_lnatural_probe.py")
_TEXT = open(_SRC).read()
_MARK = "print(\"the bottom edge's INTEGER"
if _MARK not in _TEXT:
    raise SystemExit(f"banner not found in {_SRC} — refusing to guess a split")
_NS: dict = {"__name__": "_xbot_lnatural_defs", "__file__": _SRC}
exec(_TEXT[:_TEXT.index(_MARK)], _NS)  # noqa: S102 — deliberate; the split is asserted

mp = _NS["mp"]
# The relaxation probe's working precision, restated here because a prelude run
# through exec() is invisible to the import-time / never-raises dps audits. The
# assert keeps the two in step: change the relaxation probe and this fails.
assert mp.dps == 25, f"relaxation probe dps moved to {mp.dps}; update this probe"
mp.dps = 25
epsx, b0_of = _NS["epsx"], _NS["b0_of"]
LNQ, LNQ_HALF, TOL, GAIN_TOL = _NS["LNQ"], _NS["LNQ_HALF"], _NS["TOL"], _NS["GAIN_TOL"]
E_INF_7335, B_TOP_CERT = _NS["E_INF_7335"], _NS["B_TOP_CERT"]
NEG_INF = _NS["NEG_INF"]
Q_50_DIGIT_STR = _NS["Q_50_DIGIT_STR"]
NROWS = int(os.environ.get("REV_XBOTJ_N", "40"))
PECAP = 40                                   # J3 must land below this

# The block-sup probe's definitions, for the exact TOP value per sum (its P9 enumeration).
_BS = os.path.join(_HERE, "rev_e_infinity_block_sup_relaxation_probe.py")
_BTEXT = open(_BS).read()
_BMARK = 'print("the block value is concave'
if _BMARK not in _BTEXT:
    raise SystemExit(f"banner not found in {_BS} — refusing to guess a split")
_BNS: dict = {"__name__": "_block_sup_defs", "__file__": _BS}
exec(_BTEXT[:_BTEXT.index(_BMARK)], _BNS)  # noqa: S102

_LW = json.load(open(os.path.join(_HERE, "rev-e-infinity-xbot-lnatural.witness.json")))
if not all(c["ok"] for c in _LW["checks"]):
    raise SystemExit("the L-natural witness is not all-green; its cut cannot be used")
CUT = int(_LW["cut_M6"]["cut"])
B_BOT = mp.mpf(_LW["B_bot_integer"])

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}", flush=True)


# The multiplier enters only the one-body term, so patch `phi` in the L-natural namespace;
# `best_move`, `steepest_ascent` and `G_split` look it up there.
_BASE_PHI = _NS["phi"]
_MU = [mp.mpf(0)]


@functools.lru_cache(maxsize=None)
def _phi_mu(pe: int, n: int, j: int, x: int, mu) -> mp.mpf:
    v = _BASE_PHI(pe, n, j, x)
    return v if v == NEG_INF else v - mu * x


_NS["phi"] = lambda pe, n, j, x: _phi_mu(pe, n, j, x, _MU[0])


def pe_star(mu) -> int:
    """The first frame from which `eps(1) - mu < ln q0 (pe + 1)`: deeper frames add nothing."""
    e1 = epsx(mp.mpf(1))
    pe = 0
    while not (e1 - mu < LNQ * (pe + 1)):
        pe += 1
    return pe


def tail_bracket(pe: int, w, n: int) -> mp.mpf:
    bn = b0_of(pe, n)
    tot = epsx(mp.mpf(bn + 1))
    for x in range(n):
        wx = w[x] if x < len(w) else 0
        if x < pe or wx > 0:
            g = bn - b0_of(pe, x) - wx
            tot += epsx(mp.mpf(g - 1)) - epsx(mp.mpf(g))
    return tot


# The multipliers.  Any finite set gives a valid bound; these are the ones that are active on
# s = 1..24 in a wider scan (0.6 down to 0.0025), so the rest would only repeat them.
MUS = [mp.mpf(m) for m in ("0.4", "0.3", "0.2", "0.15", "0.12", "0.05", "0.045", "0.04",
                           "0.005", "0.0025", "0")]

print("the e_inf join without G1 — a per-sum bottom bound by Lagrange multiplier")
print(f"  q0 = {mp.nstr(mp.mpf(Q_50_DIGIT_STR), 20)} (proton pin);  mp.dps = {mp.dps}")
print(f"  window s_t + s_b <= {CUT} (L-natural M6);  N = {NROWS} rows")
print(flush=True)

print("J1-J3  certified h(mu) per multiplier")
H = {}
_j1, _j2, _j3 = True, mp.mpf("-inf"), 0
_rows = []
for mu in MUS:
    _MU[0] = mu
    ps = pe_star(mu)
    _j3 = max(_j3, ps)
    best = None
    for pe in range(ps + 1):
        u, st, gp, gm, mg = _NS["steepest_ascent"](pe, NROWS)
        supp = [j for j, x in enumerate(u) if x]
        _j1 = _j1 and gp <= GAIN_TOL and gm <= GAIN_TOL and (not supp or max(supp) < NROWS - 6)
        _j2 = max(_j2, tail_bracket(pe, u, NROWS) - (LNQ_HALF + mu))
        v = _NS["G_split"](u, pe)
        if best is None or v > best[0]:
            best = (v, pe, u)
    H[mu] = best[0]
    _rows.append({"mu": mp.nstr(mu, 6), "h": mp.nstr(best[0], 22), "pe_star": ps,
                  "argmax_pe": best[1], "argmax_sum": sum(best[2])})
    print(f"    mu = {mp.nstr(mu, 6):>7}: h = {mp.nstr(best[0], 22)}  frames 0..{ps}  "
          f"argmax sum {sum(best[2])}", flush=True)
check("J1 every h(mu) is a certified integer maximum", _j1,
      f"{len(MUS)} multipliers, every frame up to pe*(mu), N = {NROWS}: no +-chi_S move improves "
      f"(gain <= {mp.nstr(GAIN_TOL, 3)}) and every support ends below row {NROWS - 6}")
check("J2 the tail lemma holds with the multiplier", _j2 < 0,
      f"max over frames and multipliers of [eps(b_N + 1) + cbar_N] - [(ln q0)/2 + mu] = "
      f"{mp.nstr(_j2, 8)}")
check("J3 the wall inequality closes the frames", _j3 < PECAP,
      f"eps(1) - mu < ln q0 (pe + 1) from pe* <= {_j3} at every multiplier, so with the shift "
      f"identity (L-natural M8) frames beyond pe* add nothing")

print("J4  the join over the window")
S = CUT
SC = mp.mpf(10) ** (_BNS["TARGET_DIGITS"] - 2)
epsb, TAIL, LH, xrun = _BNS["epsx"], _BNS["TAIL"], _BNS["LNQ_HALF"], _BNS["xrun"]
_e2 = {}
for d in range(1, S + 1):
    for w in range(-(S - 1), S):
        if 2 * d + w >= 1:
            _e2[(d, w)] = int(mp.nint((epsb(2 * d) - epsb(2 * d + w)) * SC))
_tl = {(m, v): int(mp.nint(TAIL(m, v) * SC)) for m in range(1, S + 2) for v in range(1, S + 1)}
_ct = {v: int(mp.nint(LH * v * v * SC)) for v in range(1, S + 1)}
_best: dict[int, int] = {}


def _dfs(v, s, val):
    c = _best.get(s)
    if c is None or val > c:
        _best[s] = val
    if len(v) >= S:
        return
    p = len(v)
    lo = max(1, v[-1] - 1) if v else 1
    for vp in range(lo, S + 1):
        if s + vp > S:
            break
        dd = _tl[(p + 1, vp)] - _ct[vp]
        ok = True
        for j in range(p):
            e = _e2.get((p - j, vp - v[j]))
            if e is None:
                ok = False
                break
            dd += e
        if ok:
            v.append(vp)
            _dfs(v, s + vp, val + dd)
            v.pop()


_dfs([], 0, 0)
XTOP = {s: mp.mpf(v) / SC for s, v in _best.items() if s >= 1}
BOT = {s: min(H[mu] + mu * s for mu in MUS) for s in range(1, S)}
_worst, _arg = None, None
for st in range(1, S):
    for sb in range(1, S - st + 1):
        v = XTOP[st] + xrun(st + sb) + BOT[sb]
        if _worst is None or v > _worst:
            _worst, _arg = v, (st, sb)
_tight = [s for s in range(1, S) if abs(BOT[s] - XTOP[s]) < mp.mpf(10) ** -18]
for s in range(1, S):
    print(f"    s = {s:2d}: top {mp.nstr(XTOP[s], 14)}  bottom bound {mp.nstr(BOT[s], 14)}")
print(f"    max join {mp.nstr(_worst, 25)} at (s_t, s_b) = {_arg};  e_inf {mp.nstr(E_INF_7335, 25)}")
check("J4 the window's join is e_inf with no G1", _worst <= E_INF_7335 + TOL,
      f"over s_t + s_b <= {S} (s_t, s_b >= 1, as in block-sup P9), Xblock(s_t) + xrun(s_t + s_b) "
      f"+ min_mu [h(mu) + mu s_b] peaks at {mp.nstr(_worst, 25)} at {_arg}, against e_inf = "
      f"{mp.nstr(E_INF_7335, 25)} (difference {mp.nstr(_worst - E_INF_7335, 4)}).  Outside the "
      f"window the L-natural cut applies.  So e_inf is the maximum of the join with G1 nowhere "
      f"in the argument.  The bottom bound equals the top value at s = {_tight}")

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {"script": "computations/deltalambda/rev_e_infinity_xbot_join_probe.py"},
    "bean": "qou-as81",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key
    # above is a near-miss spelling they cannot see).
    "q0Anchor": "proton",
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "Per-sum upper bound on the bottom edge, Xbot(s) <= h(mu) + mu s, with h(mu) the "
        "certified integer maximum of the L-natural-concave G - mu sum u.  With the exact top "
        "value per sum, the join over the L-natural cut's window peaks at e_inf, so e_inf is "
        "the join's maximum without G1."),
    "params": {"N": NROWS, "cut": CUT, "B_bot": mp.nstr(B_BOT, 22)},
    "multipliers": _rows,
    "per_sum": [{"s": s, "top": mp.nstr(XTOP[s], 22), "bottom_bound": mp.nstr(BOT[s], 22)}
                for s in range(1, S)],
    "join": {"max": mp.nstr(_worst, 25), "at": list(_arg), "e_inf": mp.nstr(E_INF_7335, 30),
             "difference": mp.nstr(_worst - E_INF_7335, 6)},
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
}
_out = os.path.join(_HERE, "rev-e-infinity-xbot-join.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")
_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
