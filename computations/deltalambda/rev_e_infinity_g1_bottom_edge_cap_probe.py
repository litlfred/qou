#!/usr/bin/env python3
r"""
rev_e_infinity_g1_bottom_edge_cap_probe.py — G1's only recorded counter-evidence is an
ENUMERATION ARTIFACT, and the two edge tables agree much further than anyone measured
(qou-hok7)

`e_inf` is a maximum over pairs `(s_t, s_b)` of `Xblock(s_t) + Xrun(s_t+s_b) + Xbot(s_b)`.
Every probe in this arc evaluates it with the substitution `Xbot := Xblock`, which is an upper
bound **only under G1**:

    G1:   Xbot(s)  <=  Xblock(s)   for every s.

The corpus records G1's evidence as: *the two tables are EQUAL for `s <= 12`, and the top is
higher by 0.01982 at `s = 13`.*  That sentence appears in #7335's E7, in three witness
`description`s, in two probe headers, in bean `qou-hok7` and in #7349's body, and the `s = 13`
half of it reads as a data point in G1's favour — the one place the inequality is strict and
strict in the right direction.

**It is not a data point. It is the bottom enumeration running out of ROWS.**

## What is actually going on

`Xblock` enumerates top profiles with `TMAX = 8` rows and entries `<= TUMAX = 6`.  `Xbot`
enumerates bottom profiles with `BMAX = 9` rows and entries `<= BUMAX = 3`.  Those caps are not
comparable, and the two tables have completely different maximiser *shapes*: at `s = 8` the top
winner is `[3, 2, 1, 1, 1]` (steep, 5 rows) and the bottom winner is `[1, 1, 1, 1, 2, 1, 1]`
(flat, 7 rows) — **and they are worth the same to all 40 digits.**  The bottom winner is not the
top winner reversed, and it needs more rows to get there.  So the bottom class exhausts its row
budget first, and from that point on `Xbot` is an UNDERestimate of its own supremum.

Vary the cap and the break point moves with it.  Four settings, and in **every one** the winning
profile at the break uses exactly `BMAX` rows:

| `BMAX` | `BUMAX` | equal through | breaks at | winner rows at the break |
|---|---|---|---|---|
| 8 | 6 | `s = 11` | 12 | 8 = cap |
| 9 | 3 | `s = 12` | 13 | 9 = cap |
| 10 | 3 | `s = 14` | 15 | 10 = cap |
| 11 | 3 | **`s = 17`** | 18 | 11 = cap |

The committed `BMAX = 9` row is the one the corpus quotes.  At `BMAX = 11` the tables are
**exactly equal at `s = 13`** — the 0.01982 does not exist.  `BUMAX` is irrelevant: raising it
3 -> 6 while dropping `BMAX` 9 -> 8 made the agreement *shorter*, not longer.

## 🛑 A prediction of mine that was REFUTED, recorded because it was wrong

From the first two rows I read off "break = `BMAX` + 4" and predicted `BMAX = 10` would break at
14 and `BMAX = 11` at 15.  **Both wrong**: they break at 15 and 18.  A two-point linear fit on
a cap effect is exactly the kind of thing this corpus tells agents not to trust, and the
refutation is the useful part — the break is not a fixed offset from the cap, because saturating
the cap is *necessary but not sufficient* to lose the maximum.  At `BMAX = 11` the winner
reaches 11 rows at `s = 15` and equality still survives to `s = 17`: for three further values
of `s` the capped class happens to still contain a maximiser.  What survives from the fit is
only the qualitative claim, which all four settings support: **the break is governed by `BMAX`,
saturates it, and recedes as `BMAX` grows.**

## What this does NOT do — G1 is still OPEN

Enumerating a larger class gives a better **lower** bound on `Xbot`.  A lower bound can only ever
*refute* `Xbot <= Xblock`; it can never prove it.  So this probe does not close G1 and does not
weaken it either.  What changes is the evidence:

  - the one recorded observation pointing *toward* G1 (`s = 13`) is withdrawn as an artifact;
  - the observations *consistent with* G1 extend from `s <= 12` to `s <= 17` — exact equality
    in 40-digit integer arithmetic at every one, across two different evaluators (`ap_value` in
    the `k -> infinity` AP for the top, `delta_excess` on a finite `k = 320` staircase frame
    with a `P` extension for the bottom) and two unrelated maximiser shapes;
  - `s <= 17` covers the certified join window's argmax `s_b = 8` with room to spare, though not
    the whole window `s_b <= 27`.

**What would actually close G1** is an upper bound on `Xbot` of the kind #7349 built for
`Xblock` — a per-row coercivity bound on the bottom edge's own evaluator, then a certificate.
That is not attempted here.  Alternatively G1 can be *bypassed*: the join needs a certified cut,
not a pointwise inequality, so a certified bound on `Xbot` plus an honest enumeration of the
bottom class inside that cut would remove G1 from the argument entirely rather than proving it.

## Checks

  G1a  the two tables are EXACTLY equal (integer arithmetic, no tolerance) wherever the bottom
       class is not row-capped
  G1b  at every cap setting, the winning bottom profile at the break point uses exactly `BMAX`
       rows — the break is cap saturation, not a property of the edge
  G1c  raising `BMAX` strictly extends the agreement:  11, 12, 14, 17
  G1d  the recorded `s = 13` violation is GONE at `BMAX >= 10`: the tables are equal there
  G1e  the maximisers are not reflections of one another — different lengths, different shapes,
       identical values

Proton-pinned; exact integer arithmetic at scale 1e-40 throughout, inherited from
`rev_e_infinity_edge_limit_probe.py` whose definitions this file executes directly rather than
re-deriving (the two tables must be THE committed tables, not lookalikes).  No float64.

-- Ref: [manuscript] computations/deltalambda/rev_e_infinity_edge_limit_probe.py
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

# --------------------------------------------------------------------------------------------
# Load the COMMITTED definitions.  `rev_e_infinity_edge_limit_probe.py` has no `__main__` guard
# and runs its whole driver at import, so take the source up to the first driver line.  Split on
# a literal banner rather than a line number so an edit upstream cannot silently shift it.
# --------------------------------------------------------------------------------------------
_SRC = os.path.join(_HERE, "rev_e_infinity_edge_limit_probe.py")
_TEXT = open(_SRC).read()
_MARK = 'print("e_inf'
if _MARK not in _TEXT:
    raise SystemExit(f"driver banner {_MARK!r} not found in {_SRC} — refusing to guess a split")
_LIB: dict = {"__name__": "_edge_limit_defs", "__file__": _SRC}
exec(_TEXT[:_TEXT.index(_MARK)], _LIB)  # noqa: S102 — deliberate, and the split is asserted

bot_profiles = _LIB["bot_profiles"]
bot_table = _LIB["bot_table"]
top_profiles = _LIB["top_profiles"]
block_table = _LIB["block_table"]
sc = _LIB["sc"]
Q0 = _LIB["Q0"]
TMAX, TUMAX = _LIB["TMAX"], _LIB["TUMAX"]
BMAX, BUMAX = _LIB["BMAX"], _LIB["BUMAX"]

from qou_substrate.constants import Q_50_DIGIT_STR  # noqa: E402

# the corpus's recorded figure, which this probe withdraws
RECORDED_S = 13
RECORDED_DIFF = mp.mpf("0.0198162676389039602300948111946348416306")

# cap settings to sweep.  (BMAX, BUMAX); the second row is the committed one.
SETTINGS = [(8, 6), (BMAX, BUMAX), (10, 3), (11, 3)]
if os.environ.get("REV_G1_BMAX12"):
    SETTINGS.append((12, 3))

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}", flush=True)


# --------------------------------------------------------------------------------------------
print("G1 — is the bottom edge really below the top, or is its enumeration just smaller?")
print(f"  q0 = {mp.nstr(Q0, 20)} (proton pin);  exact integers at scale 1e-40")
print(f"  committed class: top <= {TMAX} rows / entries <= {TUMAX};  "
      f"bottom <= {BMAX} rows / entries <= {BUMAX}")
print(flush=True)

_TOPS = top_profiles(TMAX, TUMAX)
XBLOCK = block_table(_TOPS)
print(f"  top table: {len(XBLOCK)} keys from {len(_TOPS):,} profiles", flush=True)
print()

# --------------------------------------------------------------------------------------------
print("G1a/G1b/G1c  vary the bottom row cap and watch the break point move")
ROWS = []
for _bm, _bu in SETTINGS:
    _t0 = time.time()
    _bots = bot_profiles(_bm, _bu)
    _xb = bot_table(_bots)
    _eq_to, _brk = None, None
    for _s in sorted(set(XBLOCK) & set(_xb)):
        if XBLOCK[_s][0] == _xb[_s][0]:
            if _brk is None:
                _eq_to = _s
        elif _brk is None:
            _brk = _s
    _wr = len(_xb[_brk][1]) if _brk in _xb else None
    ROWS.append({
        "BMAX": _bm, "BUMAX": _bu, "profiles": len(_bots), "keys": len(_xb),
        "equal_through": _eq_to, "breaks_at": _brk,
        "winner_rows_at_break": _wr, "cap_saturated_at_break": _wr == _bm,
        "winner_at_break": list(_xb[_brk][1]) if _brk in _xb else None,
        "diff_at_break": sc(XBLOCK[_brk][0] - _xb[_brk][0]).__str__() if _brk in _xb else None,
        "recorded_s_equal": (RECORDED_S in _xb
                             and XBLOCK[RECORDED_S][0] == _xb[RECORDED_S][0]),
        "seconds": round(time.time() - _t0),
    })
    print(f"    BMAX={_bm:3d} BUMAX={_bu}  {len(_bots):>9,} profiles  "
          f"equal through s = {_eq_to:3d}, breaks at {_brk:3d}  "
          f"winner there uses {_wr} rows (cap {_bm}) "
          f"{'SATURATED' if _wr == _bm else '*** NOT saturated ***'}", flush=True)
    if _bm == BMAX and _bu == BUMAX:
        _COMMITTED = (_xb, _eq_to, _brk)
    if _bm == max(s[0] for s in SETTINGS):
        _WIDEST = (_xb, _eq_to, _brk)

_bot_c, _eq_c, _brk_c = _COMMITTED
_bot_w, _eq_w, _brk_w = _WIDEST
_WIDEST_BM = max(s[0] for s in SETTINGS)

_exact = all(XBLOCK[s][0] == _bot_w[s][0] for s in range(1, _eq_w + 1))
check(
    "G1a the two tables agree EXACTLY, in integers, wherever the bottom class is not capped",
    _exact and _eq_w >= _eq_c,
    f"at BMAX = {_WIDEST_BM} the tables are equal for every s = 1..{_eq_w}, as exact integers "
    f"at scale 1e-40 — no tolerance is involved, the values are identical.  They come from "
    f"DIFFERENT evaluators (`ap_value` in the k -> infinity AP for the top; `delta_excess` on a "
    f"finite k = 320 staircase frame with a P extension for the bottom) and from different "
    f"maximiser shapes, so this is agreement, not a shared code path",
)

_all_sat = all(r["cap_saturated_at_break"] for r in ROWS)
check(
    "G1b every break point is the ROW cap saturating, at every setting tried",
    _all_sat,
    "at each of " + ", ".join(f"BMAX={r['BMAX']}" for r in ROWS) + " the winning bottom profile "
    "at the first disagreement uses exactly BMAX rows: "
    + "; ".join(f"{r['BMAX']} -> {r['winner_at_break']}" for r in ROWS)
    + ".  The bottom maximisers are FLAT and LONG (entries 1-3) where the top's are STEEP and "
      "SHORT, so the bottom class exhausts its row budget first and from there on Xbot "
      "understates its own supremum",
)

_mono = all(ROWS[i]["equal_through"] <= ROWS[i + 1]["equal_through"] for i in range(len(ROWS) - 1))
check(
    "G1c raising the row cap strictly extends the agreement",
    _mono and _eq_w > _eq_c,
    "equal-through runs "
    + " -> ".join(f"{r['equal_through']} (BMAX {r['BMAX']})" for r in ROWS)
    + f".  The committed cap {BMAX} gives {_eq_c}; {_WIDEST_BM} gives {_eq_w}.  BUMAX is not "
      f"the constraint — raising it 3 -> 6 while dropping BMAX 9 -> 8 made the agreement "
      f"SHORTER ({ROWS[0]['equal_through']}), which is the row cap talking, not the entry cap",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("G1d  the corpus's recorded counter-evidence")
_rec_gone = [r for r in ROWS if r["recorded_s_equal"]]
print(f"    recorded: 'top higher by {mp.nstr(RECORDED_DIFF, 8)} at s = {RECORDED_S}'")
for r in ROWS:
    print(f"      BMAX={r['BMAX']:3d}: s = {RECORDED_S} is "
          f"{'EQUAL' if r['recorded_s_equal'] else 'unequal'}")
_reproduced = any(r["BMAX"] == BMAX and not r["recorded_s_equal"] for r in ROWS)
check(
    "G1d the recorded s = 13 violation is an artifact and disappears when the cap is lifted",
    _reproduced and len(_rec_gone) >= 2,
    f"at the committed BMAX = {BMAX} the figure reproduces (that part of the record is "
    f"correct), and at BMAX >= {min(r['BMAX'] for r in _rec_gone)} the two tables are EXACTLY "
    f"EQUAL at s = {RECORDED_S}.  So the 0.01982 is the bottom enumeration running out of rows, "
    f"not the bottom edge being worth less.  It is quoted as a data point in G1's favour in "
    f"#7335's E7, in three witness descriptions, in two probe headers, in bean qou-hok7 and in "
    f"#7349's body; it is WITHDRAWN as evidence in either direction",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print("G1e  the two maximisers are not reflections of each other")
_shape = []
for _s in range(1, min(_eq_w, 12) + 1):
    _t = list(XBLOCK[_s][1])
    _b = list(_bot_w[_s][1])
    _shape.append({"s": _s, "top": _t, "bot": _b, "top_rows": len(_t), "bot_rows": len(_b),
                   "is_reverse": _b == _t[::-1], "equal_value": XBLOCK[_s][0] == _bot_w[_s][0]})
    print(f"    s = {_s:2d}: top {str(_t):28s} bot {str(_b):34s} "
          f"{'reverse' if _b == _t[::-1] else 'NOT a reverse'}")
_never_rev = sum(1 for r in _shape if not r["is_reverse"])
_all_eq = all(r["equal_value"] for r in _shape)
check(
    "G1e equal values, unrelated shapes — the agreement is not a symmetry of the profile",
    _all_eq and _never_rev >= len(_shape) - 2,
    f"{_never_rev} of {len(_shape)} maximiser pairs are not reverses of one another, and all "
    f"{len(_shape)} are worth exactly the same.  At s = 8 the top winner is "
    f"{list(XBLOCK[8][1])} ({len(XBLOCK[8][1])} rows) and the bottom winner is "
    f"{list(_bot_w[8][1])} ({len(_bot_w[8][1])} rows).  Whatever makes Xbot = Xblock, it is not "
    f"'read the block backwards' — which is why the row caps are not interchangeable and why "
    f"nobody noticed the bottom class was the smaller one",
)
print(flush=True)

# --------------------------------------------------------------------------------------------
print(f"  agreement extends from s <= {_eq_c} (committed cap) to s <= {_eq_w} (BMAX "
      f"{_WIDEST_BM})")
print(f"  the join's argmax s_b = 8 sits well inside it; the full window s_b <= 27 does not")
print("  G1 is STILL OPEN — a larger enumeration is a better LOWER bound on Xbot, and a lower")
print("  bound can only refute Xbot <= Xblock, never prove it")
print()

_wit = {
    "schema": "https://litlfred.github.io/qou/schemas/witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": {
        "script": "computations/deltalambda/rev_e_infinity_g1_bottom_edge_cap_probe.py"},
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "G1 -- Xbot(s) <= Xblock(s), the last conditionality on e_inf -- has one recorded "
        "observation in its favour: the corpus states the two edge tables are EQUAL for s <= 12 "
        "and the top is higher by 0.01982 at s = 13.  That figure is an ENUMERATION ARTIFACT.  "
        "The bottom class is capped at BMAX = 9 rows while its maximisers are flat and long "
        "(entries 1-3, one row per unit of s) where the top's are steep and short, so the "
        "bottom exhausts its row budget first; from there Xbot understates its own supremum.  "
        "Varying the cap moves the break point -- BMAX 8/9/10/11 give agreement through s = "
        "11/12/14/17 -- and at EVERY setting the winning profile at the break uses exactly "
        "BMAX rows.  At BMAX >= 10 the tables are exactly equal at s = 13 and the 0.01982 does "
        "not exist.  BUMAX is not the constraint: raising it 3 -> 6 while dropping BMAX 9 -> 8 "
        "made the agreement SHORTER.  A prediction of the agent's -- break = BMAX + 4, fitted "
        "to the first two settings -- was REFUTED by the other two (15 and 18, not 14 and 15); "
        "saturating the cap is necessary but not sufficient to lose the maximum.  G1 is NOT "
        "closed and is not weakened: a larger enumeration is a better LOWER bound on Xbot, "
        "which can only refute the inequality, never prove it.  What changed is the evidence -- "
        "the one observation pointing toward G1 is withdrawn, and the observations consistent "
        "with it extend from s <= 12 to s <= 17, in exact integer arithmetic, across two "
        "different evaluators and two unrelated maximiser shapes."
    ),
    "constants": {
        "recorded_s": RECORDED_S,
        "recorded_diff": mp.nstr(RECORDED_DIFF, 30),
        "committed_BMAX": BMAX, "committed_BUMAX": BUMAX,
        "committed_TMAX": TMAX, "committed_TUMAX": TUMAX,
        "agreement_committed_cap": _eq_c,
        "agreement_widest_cap": _eq_w,
        "widest_BMAX": _WIDEST_BM,
    },
    "cap_sweep": ROWS,
    "maximiser_shapes": _shape,
    "refuted_prediction": {
        "claim": "break point = BMAX + 4, read off the BMAX = 8 and 9 rows",
        "predicted": {"BMAX_10": 14, "BMAX_11": 15},
        "measured": {"BMAX_10": next(r["breaks_at"] for r in ROWS if r["BMAX"] == 10),
                     "BMAX_11": next(r["breaks_at"] for r in ROWS if r["BMAX"] == 11)},
        "status": "REFUTED",
        "what_survives": ("the break is governed by BMAX, saturates it, and recedes as BMAX "
                          "grows -- but not by a fixed offset, because cap saturation is "
                          "necessary and not sufficient to lose the maximum (at BMAX = 11 the "
                          "winner reaches 11 rows at s = 15 and equality survives to s = 17)"),
    },
    "open_gaps": {
        "G1_status": "STILL OPEN -- neither closed nor weakened",
        "why_this_cannot_close_it": ("enumerating a larger class bounds Xbot from BELOW; a "
                                     "lower bound can refute Xbot <= Xblock but never prove "
                                     "it"),
        "what_would_close_it": ("an upper bound on Xbot of the kind #7349 built for Xblock -- a "
                                "per-row coercivity bound on the bottom edge's own evaluator, "
                                "then a supergradient certificate"),
        "how_to_BYPASS_it": ("the join needs a certified cut, not a pointwise inequality.  A "
                             "certified bound on Xbot plus an honest enumeration of the bottom "
                             "class inside that cut removes G1 from the argument rather than "
                             "proving it"),
        "headline": "still the upper bound on M_n, which none of this touches",
    },
    "checks": [{"name": n, "ok": o, "detail": d} for n, o, d in CHECKS],
    "verdict": (
        "The single observation the corpus records in G1's favour is an artifact of the bottom "
        "edge's row cap, and it vanishes when the cap is lifted.  G1 itself is untouched -- "
        "still open, still the only conditionality on e_inf -- but its evidence base is now "
        "honest: exact agreement through s = 17 across two evaluators and two unrelated "
        "maximiser shapes, and nothing at all pointing the other way."
    ),
}

_out = os.path.join(_HERE, "rev-e-infinity-g1-bottom-edge-cap.witness.json")
with open(_out, "w") as fh:
    json.dump(_wit, fh, indent=2)
    fh.write("\n")
print(f"wrote {_out}")

_ok = sum(1 for _, o, _ in CHECKS if o)
print(f"{_ok}/{len(CHECKS)} checks pass")
sys.exit(0 if _ok == len(CHECKS) else 1)
