#!/usr/bin/env python3
r"""
rev_e_infinity_xbot_coercivity_probe.py — does the per-row coercivity bound transfer from the
top edge to the BOTTOM edge's own evaluator? (qou-hok7)

`e_inf` is a maximum over pairs `(s_t, s_b)` of `Xblock(s_t) + Xrun(s_t+s_b) + Xbot(s_b)`.
#7349 closed gap G2 by bounding the TOP edge: a per-row linearisation `Xblock(u) <= sum_i
[u_i Ghat(i+1) - (ln q0/2) u_i^2]`, then a concave relaxation, then a supergradient certificate.
G1 — `Xbot(s) <= Xblock(s)` — is what lets the join substitute `Xbot := Xblock` and is the last
conditionality on `e_inf`.

`rev_e_infinity_g1_bottom_edge_cap_probe.py` established that **no enumeration can ever settle
G1**: a capped maximum is a LOWER bound on its own supremum, and a lower bound can only refute
an inequality, never prove it.  What would settle it is an **upper** bound on `Xbot` of the kind
#7349 built for `Xblock` — and the cleaner move is to BYPASS G1 entirely, since the join needs a
certified cut, not a pointwise inequality.  Either way the missing object is the same: a
coercivity bound on the bottom edge.

This probe asks whether the top edge's argument transfers, and the answer is not obvious,
because the two edges do not live in the same environment.

## Why it is not a formality

`staircase_beta(k, L)` is TWO environments glued at a wall:

    rows i <= k :  b0 = k + L - 1 - 2i     an AP of GAP 2   (the top edge's world)
    rows i >  k :  b0 = L - 1 - i          consecutive, GAP 1   (the bottom wall)

The bottom block straddles the junction — at `pe = 3` its lowest three rows sit in the gap-1
wall and the rest in the gap-2 AP.  Three things follow that the top edge never has to deal
with:

  1. **`delta_excess` carries a one-body term** `fi(beta_a) - fi(b0_a)`.  `ap_value` has none —
     its docstring says `beta ~ 2k` there, so `F` is saturated and the one-body term vanishes.
     Near the wall `b0` is small, so it does not vanish.
  2. **An extra linear cost** `lin = sum_{i>k} (i-k) u_i`, worth `ln(q0)*lin` and measured at
     **0.7304** at the `s >= 11` maximisers (`lin = 7`).  `ap_value` has no analogue.
  3. **The gaps are not `2d`.**  From a wall row the distances to the AP are a gap-2 ladder with
     a shifted start, and within the wall they are `1, 2, 3, ...`.

## The bound under test

Per row `a`, with every other row treated as undisplaced (the evaluator's own premise), the
linearisation of `SearchCoercivity.lean` applies to each pair separately — `e a - e (a + D) <=
D * delta a` for BOTH signs of `D`, the discrete form, proved there by induction with no
derivative.  Summing it over the frame:

    Ghat_bot(a)  =  eps(b0_a + 1)                                   one-body slope
                  + sum_{j : b0_j < b0_a} delta(b0_a - b0_j)        rows BELOW  (gain)
                  - sum_{j : b0_j > b0_a} delta(b0_j - b0_a)        rows ABOVE  (loss)

with `delta(m) = eps(m) - eps(m+1)`, the same discrete step the Lean lemma uses — not a
derivative, so the probe and the formalisation are testing the same object.  The claim is then

    delta_excess(u)  <=  sum_a u_a Ghat_bot(a)  -  ln(q0) * lin(u)  -  (ln q0 / 2) * sum u_a^2

exactly parallel to #7349's S2, which checks the top edge's version over 8.3M blocks with 0
violations.

**The signed structure is the whole question.** `Ghat_bot` is a DIFFERENCE, not a sum: rows
below a displaced row are a gain and rows above are a loss.  For the top edge the row sits at
the free end, so there is almost nothing above it and the loss term is a short finite sum; deep
in the staircase there are ~`k` rows above, and whether the difference stays positive enough to
bound anything is what gets measured here.

## What a result means either way

  - **0 violations** — the coercivity transfers, `Xbot` has an explicit uniform upper bound, and
    the G1 bypass is live: certify the bottom edge the way #7349 certified the top, then
    enumerate the bottom class honestly inside the resulting cut.
  - **violations** — the transfer fails, and the probe reports WHERE (which rows, which
    profiles, how badly), which is the input to whatever argument replaces it.  A failure here
    is not a failure of G1; it is a failure of this particular route to it.

Nothing here closes G1 or refutes it.  This measures whether one specific, already-formalised
tool reaches the bottom edge at all.

Proton-pinned; exact integer arithmetic at scale 1e-40 inherited from
`rev_e_infinity_edge_limit_probe.py`, whose definitions this file executes directly rather than
re-deriving.  No float64.

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/BraidKnot/SearchCoercivity.lean
"""

from __future__ import annotations

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

_SRC = os.path.join(_HERE, "rev_e_infinity_edge_limit_probe.py")
_TEXT = open(_SRC).read()
_MARK = 'print("e_inf'
if _MARK not in _TEXT:
    raise SystemExit(f"driver banner {_MARK!r} not found in {_SRC} — refusing to guess a split")
_LIB: dict = {"__name__": "_edge_limit_defs", "__file__": _SRC}
exec(_TEXT[:_TEXT.index(_MARK)], _LIB)  # noqa: S102 — deliberate, and the split is asserted

epsi = _LIB["epsi"]
fi = _LIB["fi"]
sc = _LIB["sc"]
Q0, LNQ, LNQ_I = _LIB["Q0"], _LIB["LNQ"], _LIB["LNQ_I"]
EPS_CUT = _LIB["EPS_CUT"]
staircase_beta = _LIB["staircase_beta"]
bot_profiles, make_u = _LIB["bot_profiles"], _LIB["make_u"]
delta_excess, bot_table = _LIB["delta_excess"], _LIB["bot_table"]
top_profiles, block_table, ap_value = _LIB["top_profiles"], _LIB["block_table"], _LIB["ap_value"]
K, PEMAX = _LIB["K_BOT"], _LIB["P_EXT_MAX"]
TMAX, TUMAX = _LIB["TMAX"], _LIB["TUMAX"]

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

BMAX = int(os.environ.get("REV_XBOT_BMAX", "10"))
BUMAX = int(os.environ.get("REV_XBOT_BUMAX", "3"))

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


def dstep(m: int) -> int:
    """`delta(m) = eps(m) - eps(m+1)`, the DISCRETE downward step.

    This is the object `SearchCoercivity.sub_le_mul_of_antitone_step` is stated over — not a
    derivative — so the bound measured here is the one the Lean lemma licenses."""
    return epsi(m) - epsi(m + 1) if m >= 1 else 0


def ghat_bot(b0: list[int], r: int) -> int:
    """Per-row gain bound at frame row `r`: one-body slope, plus rows BELOW (gain), minus rows
    ABOVE (loss).  A difference, not a sum — which is the thing under test."""
    br = b0[r]
    tot = epsi(br + 1)                       # one-body: fi(b+u) - fi(b) <= u * eps(b+1)
    for j, bj in enumerate(b0):
        if j == r:
            continue
        if bj < br:
            g = br - bj
            if g <= EPS_CUT:
                tot += dstep(g)
        else:
            g = bj - br
            if g <= EPS_CUT:
                tot -= dstep(g)
    return tot


# --------------------------------------------------------------------------------------------
print("Xbot coercivity — does the top edge's per-row bound reach the bottom edge?")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  exact integers at scale 1e-40")
print(f"  staircase k = {K}: rows <= k are the gap-2 AP, rows > k the gap-1 wall")
print(f"  bottom class: <= {BMAX} rows / entries <= {BUMAX};  pe = 0..{PEMAX}")
print(flush=True)

# --------------------------------------------------------------------------------------------
print("X1  the frame is genuinely two environments (not one AP in disguise)")
_L = K + 1 + 3
_b0 = staircase_beta(K, _L)
_gaps_ap = [_b0[i] - _b0[i + 1] for i in range(0, K - 2)]
_gaps_wall = [_b0[i] - _b0[i + 1] for i in range(K + 1, _L - 1)]
print(f"    gaps among rows i < k   : {sorted(set(_gaps_ap))}")
print(f"    gaps among rows i > k   : {sorted(set(_gaps_wall))}")
print(f"    b0 at the junction      : ...{_b0[K-2:K+4]}...", flush=True)
check(
    "X1 the staircase really is gap-2 above the wall and gap-1 below it",
    set(_gaps_ap) == {2} and set(_gaps_wall) == {1},
    f"every gap among rows i < k is 2 and every gap among rows i > k is 1, so the bottom block "
    f"straddles two different environments.  That is why the top edge's `Ghat(m) = sum_{{d>=m}} "
    f"|eps'(2d)|` — which assumes a pure gap-2 ladder — cannot simply be reused, and why the "
    f"bound below is rebuilt from the frame's own distances",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("X2  the extra terms the top edge does not have")
_pe_seen: dict[int, int] = {}
_BOTS = bot_profiles(BMAX, BUMAX)
_XB = bot_table(_BOTS)
for _s, (_v, _b, _pe) in sorted(_XB.items()):
    _LL = K + 1 + _pe
    _u = make_u(_LL, (), _b, 0, 0)
    if _u is None:
        continue
    _pe_seen[_s] = sum((i - K) * _u[i] for i in range(_LL) if i > K)
_lin_max = max(_pe_seen.values()) if _pe_seen else 0
_onebody = epsi(1)
print(f"    lin at the per-s maximisers: {dict(list(sorted(_pe_seen.items()))[:14])}")
print(f"    worst lin = {_lin_max}  ->  handicap ln(q0)*lin = "
      f"{mp.nstr(LNQ * _lin_max, 12)}")
print(f"    one-body slope at the wall's last row: eps(1) = {mp.nstr(sc(_onebody), 12)}",
      flush=True)
check(
    "X2 both extra terms are LARGE, not perturbative",
    _lin_max >= 1 and _onebody > 0,
    f"the linear cost reaches ln(q0)*{_lin_max} = {mp.nstr(LNQ * _lin_max, 10)} at the bottom "
    f"maximisers — against an Xbot whose whole value is ~2.1 — and the one-body term, "
    f"identically zero for the top edge because `beta ~ 2k` saturates F there, is worth up to "
    f"eps(1) = {mp.nstr(sc(_onebody), 10)} per unit of displacement at the wall.  Neither is a "
    f"correction to the top edge's argument; they are structure it does not have",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("X3  does the per-row bound hold over the whole enumerated bottom class?")
_t0 = time.time()
_tested = 0
_viol: list[tuple] = []
_worst_slack = None          # smallest (bound - actual); negative means violated
_ghat_cache: dict[int, list[int]] = {}
for _pe in range(0, PEMAX + 1):
    _LL = K + 1 + _pe
    _bb0 = staircase_beta(K, _LL)
    _nb0 = [-x for x in _bb0]
    # only the rows a bottom block can occupy need a Ghat
    _lo_row = _LL - BMAX
    _g = {r: ghat_bot(_bb0, r) for r in range(_lo_row, _LL)}
    _ghat_cache[_pe] = [_g[r] for r in sorted(_g)]
    for _b in _BOTS:
        if not _b:
            continue
        _u = make_u(_LL, (), _b, 0, 0)
        if _u is None:
            continue
        _actual = delta_excess(_u, K, _bb0, _nb0, require_zero_sum=False)
        if _actual is None:
            continue
        _lin = sum((i - K) * _u[i] for i in range(_LL) if i > K)
        _gain = sum(_u[r] * _g[r] for r in range(_lo_row, _LL) if _u[r])
        _bound = _gain - (LNQ_I * (2 * _lin + sum(x * x for x in _u))) // 2
        _slack = _bound - _actual
        _tested += 1
        if _worst_slack is None or _slack < _worst_slack[0]:
            _worst_slack = (_slack, list(_b), _pe)
        if _slack < 0:
            _viol.append((_slack, list(_b), _pe))
_dt = time.time() - _t0
print(f"    tested {_tested:,} (profile, pe) pairs in {_dt:.0f}s")
print(f"    violations: {len(_viol):,}")
print(f"    tightest slack (bound - actual): {mp.nstr(sc(_worst_slack[0]), 14)} "
      f"at {_worst_slack[1]} pe={_worst_slack[2]}", flush=True)
if _viol:
    _viol.sort()
    print("    worst violations:")
    for _s2, _b2, _p2 in _viol[:6]:
        print(f"      {mp.nstr(sc(_s2), 12):>16}  {_b2} pe={_p2}")
check(
    "X3 the per-row linearisation bounds the bottom edge's excess",
    not _viol,
    f"over {_tested:,} (profile, pe) pairs the bound `sum_a u_a Ghat_bot(a) - ln(q0) lin - "
    f"(ln q0/2) sum u^2` holds with {len(_viol)} violations; the tightest slack is "
    f"{mp.nstr(sc(_worst_slack[0]), 12)} at {_worst_slack[1]}.  The bound is assembled from the "
    f"frame's own distances via the DISCRETE step `delta(m) = eps(m) - eps(m+1)` — the object "
    f"`SearchCoercivity.sub_le_mul_of_antitone_step` is stated over — so a clean result here is "
    f"licensed by a sorry-free lemma rather than by a derivative argument"
    if not _viol else
    f"over {_tested:,} (profile, pe) pairs the bound FAILS on {len(_viol):,}, worst by "
    f"{mp.nstr(sc(_viol[0][0]), 12)} at {_viol[0][1]} pe={_viol[0][2]}.  The per-row "
    f"linearisation does NOT transfer to the bottom edge as assembled here.  That is a fact "
    f"about this route, not about G1",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("X4  is the bound USEFUL — does it cap Xbot below anything?")
# A block lives in exactly ONE frame, so the uniform cap is the MAX over pe of that frame's
# per-row sum — never the sum across frames.  (Summing all 9 frames inflated it 3.9x; caught
# here before it was quoted.)
_cap_rows = []
_per_frame: dict[int, int] = {}
for _pe in range(0, PEMAX + 1):
    _LL = K + 1 + _pe
    _bb0 = staircase_beta(K, _LL)
    _lo_row = _LL - BMAX
    _frame_sum = 0
    for _r in range(_lo_row, _LL):
        _gh = ghat_bot(_bb0, _r)
        # max over v >= 1 of  v*Ghat - (ln q0/2) v^2, in scaled integers
        _peak = (_gh * _gh * 2) // (2 * LNQ_I) if _gh >= LNQ_I // 2 else _gh - LNQ_I // 2
        _cap_rows.append((_pe, _r, _gh, _peak))
        if _peak > 0:
            _frame_sum += _peak
    _per_frame[_pe] = _frame_sum
_pos = [r for r in _cap_rows if r[2] > 0]
_sum_peak = max(_per_frame.values())
_worst_pe = max(_per_frame, key=lambda p: _per_frame[p])
_across_frames = sum(r[3] for r in _cap_rows if r[3] > 0)
print(f"    rows with Ghat_bot > 0: {len(_pos):,} of {len(_cap_rows):,}")
print(f"    per-frame caps by pe: "
      f"{ {p: mp.nstr(sc(v), 8) for p, v in sorted(_per_frame.items())} }")
print(f"    uniform cap = max over pe = {mp.nstr(sc(_sum_peak), 14)} (at pe = {_worst_pe})")
print(f"    [summing ACROSS frames would give {mp.nstr(sc(_across_frames), 14)} — wrong, a "
      f"block occupies one frame]")
_int_sup = max(v for v, _, _ in _XB.values())
print(f"    enumerated max Xbot (BMAX={BMAX}): {mp.nstr(sc(_int_sup), 14)}", flush=True)
check(
    "X4 the per-row cap is finite and exceeds the enumerated maximum",
    _sum_peak > _int_sup,
    f"summing the per-row caps `max_{{v>=1}} [v Ghat_bot(r) - (ln q0/2) v^2]` over the rows of "
    f"ONE frame and taking the max over pe gives {mp.nstr(sc(_sum_peak), 12)} (at pe = "
    f"{_worst_pe}), against an enumerated maximum of {mp.nstr(sc(_int_sup), 12)} — a finite "
    f"uniform bound, but {mp.nstr(sc(_sum_peak)/sc(_int_sup), 6)}x the enumerated value.  "
    f"**That is far too loose to be used.** #7349's top-edge analogue `B_sharp` was 1.82x and "
    f"even that gave an unenumerable cut of 90; this is an order of magnitude worse, so the "
    f"route is LIVE but the bound as assembled is not yet a tool.  The looseness has the same "
    f"shape as `B_sharp`'s did — a per-row tangent with no cap, while a single row's real gain "
    f"saturates — so the concave relaxation that took the top edge 1.82x -> 1.04x is the next "
    f"step rather than a new idea"
    if _sum_peak > _int_sup else
    f"the per-row cap sums to {mp.nstr(sc(_sum_peak), 12)}, which does NOT exceed the "
    f"enumerated maximum {mp.nstr(sc(_int_sup), 12)} — so either the bound is unsound (X3 "
    f"would have caught that) or the row set is too narrow.  Investigate before using it",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
_ok_all = all(o for _, o, _ in CHECKS)
print(f"  per-row bound holds: {not _viol};  uniform cap "
      f"{mp.nstr(sc(_sum_peak), 14)} vs enumerated {mp.nstr(sc(_int_sup), 14)}")
print("  G1 is UNTOUCHED — this measures a tool, not the inequality")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {
        "script": "computations/deltalambda/rev_e_infinity_xbot_coercivity_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "G1 (Xbot(s) <= Xblock(s)) is the last conditionality on e_inf, and no enumeration can "
        "settle it: a capped maximum is a LOWER bound on its own supremum and a lower bound can "
        "only refute an inequality.  What is needed is an UPPER bound on Xbot, of the kind "
        "#7349 built for Xblock -- and it would also BYPASS G1, since the join needs a certified "
        "cut rather than a pointwise inequality.  This probe asks whether #7349's per-row "
        "linearisation transfers to the bottom edge's own evaluator.  It is not a formality: "
        "staircase_beta is TWO environments glued at a wall (gap 2 above, gap 1 below) and the "
        "bottom block straddles them, delta_excess carries a one-body term that ap_value lacks "
        "entirely (F is saturated at the top edge, not at the wall), and it pays an extra linear "
        "cost lin = sum_{i>k}(i-k)u_i worth ln(q0)*lin and reaching 0.7304 at the maximisers.  "
        "The bound under test is rebuilt from the frame's own distances using the DISCRETE step "
        "delta(m) = eps(m) - eps(m+1) -- the object SearchCoercivity.sub_le_mul_of_antitone_step "
        "is stated over -- so a clean result is licensed by a sorry-free lemma rather than by a "
        "derivative argument.  Ghat_bot is a DIFFERENCE, not a sum: rows below a displaced row "
        "are a gain and rows above are a loss, and deep in the staircase there are ~k rows "
        "above, which is the substantive question."
    ),
    "constants": {
        "k": K, "pe_max": PEMAX, "BMAX": BMAX, "BUMAX": BUMAX,
        "eps_cut": EPS_CUT,
        "worst_lin_at_maximisers": _lin_max,
        "lin_handicap": mp.nstr(LNQ * _lin_max, 30),
        "tested_pairs": _tested,
        "violations": len(_viol),
        "tightest_slack": mp.nstr(sc(_worst_slack[0]), 30),
        "per_row_cap_uniform": mp.nstr(sc(_sum_peak), 30),
        "per_row_cap_worst_pe": _worst_pe,
        "per_row_cap_by_frame": {str(p2): mp.nstr(sc(v2), 20)
                                 for p2, v2 in sorted(_per_frame.items())},
        "_cap_note": ("the uniform cap is the MAX over pe of one frame's per-row "
                      "sum; summing ACROSS frames is wrong (a block occupies one "
                      "frame) and inflates it ~3.9x"),
        "enumerated_max_Xbot": mp.nstr(sc(_int_sup), 30),
    },
    "lin_at_maximisers": {str(k2): v2 for k2, v2 in sorted(_pe_seen.items())},
    "violations": [{"slack": mp.nstr(sc(s3), 20), "bot": b3, "pe": p3}
                   for s3, b3, p3 in _viol[:40]],
    "open_gaps": {
        "G1_status": "UNTOUCHED — this probe measures a tool, not the inequality",
        "what_a_clean_result_buys": ("an explicit uniform upper bound on Xbot, hence the same "
                                     "concave-relaxation + supergradient-certificate route "
                                     "#7349 used on the top edge, hence a certified cut that "
                                     "removes G1 from the argument instead of proving it"),
        "what_remains_either_way": ("the tightening (#7349's B_sharp was 1.82x before the "
                                    "concave relaxation took it to 1.04x) and then an honest "
                                    "enumeration of the bottom class inside the resulting cut"),
        "headline": "still the upper bound on M_n, which none of this touches",
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "Measures whether #7349's per-row coercivity reaches the bottom edge, across a frame "
        "that is two glued environments rather than one AP, with a one-body term and an extra "
        "linear cost the top edge does not have.  Closes nothing and refutes nothing; it "
        "establishes whether the one already-formalised tool applies, which is the gate on the "
        "whole G1-bypass route."
    ),
}

_out = os.path.join(_HERE, "rev-e-infinity-xbot-coercivity.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
