#!/usr/bin/env python3
r"""
rev_optimal_gap_profile_probe.py — the maximiser's SHAPE, and a model of mine it refutes
(qou-hok7)

#7286 pinned the maximiser's MEAN beta-gap to `2 + O(1/sqrt n)` (rigidity), and #7294 made that
exact: `8H = sum_i (2 beta_i - a_i)^2 - sum_i a_i^2`, so the hook sum is a positive-definite
quadratic and the row deviations `d_i = 2 beta_i - a_i` satisfy `d_i - d_{i+1} = 2 g_i - 4` for
the gap `g_i = beta_i - beta_{i+1}`. A mean is a weak description of a shape. This probe reads
the ACTUAL gap profile of the best shape found at each n, out of #7286's committed witness.

## What the profiles show

The maximiser is not "mean gap 2 with unspecified structure". It is the staircase with a block
of **3-gaps at the top** (large beta) and a matching block of **1-gaps at the bottom** (small
beta), everything between them at 2 -- and **no gap ever exceeds 3**.

## The model this refutes, which was mine

Before reading the profiles I had a single-move estimate: widen ONE gap from 2 to `G` at fixed
`(n, l)`. With the rest at 2 only `d_0` deviates, so `Delta H = (G-2)^2 / 2` and the energy cost
is `ln q_0 (G-2)^2 / 2`, while the saving is the pair term row 0 no longer pays,
`sum_{j>=1} [eps(2j) - eps(2j + G - 2)]`. That peaks at **G = 5, gain ~ +0.93**, and it is
**wrong about the shape**: the measured optimum never uses a gap above 3.

It is wrong because it answers a different question. Holding `l` fixed forces the compensating
shift to spread uniformly over every row; the real optimum instead MOVES `l` (to `k + 3`) and
pays for its 3-gaps with explicit 1-gaps at the bottom. R4 records the refutation rather than
the model, because a plausible closed-form story about the maximiser is exactly the kind of
thing that otherwise ends up in a PR body unchecked.

## Checks

  R1  the profile is {1, 2, 3}-valued at every n -- no gap exceeds 3
  R2  the structure is monotone: 3s at the top, 1s at the bottom, 2s between
  R3  the deviation COUNT against n (what actually sets the excess's growth)
  R4  the single-widened-gap model, and its refutation by R1

Reads #7286's committed witness (`rev-energy-gap-rigidity.witness.json`); recomputes nothing
that probe already recorded, so the two cannot drift. Proton-pinned; no Markov parameter in
this cone; exact integers for the gaps; mpmath for the eps sums; no float64.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))
_COMPUTATIONS = os.path.dirname(_HERE)
if _COMPUTATIONS not in sys.path:
    sys.path.insert(0, _COMPUTATIONS)

from mpmath import mp  # noqa: E402

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402

mp.dps = 40
Q0 = Q_MP
LNQ = mp.log(Q0)
T = Q0 ** 2

_NEPS = 4000
EPS = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, _NEPS)]
A_CONST = sum(EPS[m] for m in range(1, _NEPS, 2))
E2_CONST = sum(EPS[m] for m in range(2, _NEPS, 2))


def eps(m: int) -> mp.mpf:
    return EPS[m] if 0 < m < _NEPS else mp.mpf(0)


CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'ok ' if ok else 'FAIL'}] {name}: {detail}")


_SRC = os.path.join(_HERE, "rev-energy-gap-rigidity.witness.json")
if not os.path.exists(_SRC):
    print(f"missing input witness {_SRC} — it is committed by PR #7286; nothing to do")
    sys.exit(1)
with open(_SRC, encoding="utf-8") as fh:
    _W = json.load(fh)

# --------------------------------------------------------------------------------------------
print("R1/R2  the gap profile of the best shape found at each n")
_rows = []
for row in _W["tradeoff_R2"]:
    best = max(row["by_l"], key=lambda x: mp.mpf(x["V"]))
    b = best["beta"]
    g = [b[i] - b[i + 1] for i in range(len(b) - 1)]
    hist = dict(sorted(Counter(g).items()))
    n3 = sum(1 for x in g if x == 3)
    n1 = sum(1 for x in g if x == 1)
    # "monotone" = the 3s all precede the 1s (top-heavy 3s, bottom-heavy 1s)
    last3 = max((i for i, x in enumerate(g) if x == 3), default=-1)
    first1 = min((i for i, x in enumerate(g) if x == 1), default=len(g))
    _rows.append({"n": row["n"], "k": row["k"], "l": best["l"], "hist": hist,
                  "n3": n3, "n1": n1, "ndev": n3 + n1, "ngaps": len(g),
                  "monotone": last3 < first1, "gaps": g})
    print(f"    n = {row['n']:5d}  k = {row['k']:3d}  l = {best['l']:3d}   {hist}   "
          f"3s={n3} 1s={n1}  3s-before-1s={last3 < first1}")

_maxgap = max(max(r["gaps"]) for r in _rows)
_mingap = min(min(r["gaps"]) for r in _rows)
check(
    "R1 every gap lies in {1, 2, 3} — none exceeds 3",
    _maxgap <= 3 and _mingap >= 1,
    f"min gap {_mingap}, max gap {_maxgap} across {len(_rows)} shapes. The maximiser is a "
    f"UNIT perturbation of the staircase, not a shape with a few wide gaps",
)
check(
    "R2 the 3-gaps all precede the 1-gaps (3s at large beta, 1s at small beta)",
    all(r["monotone"] for r in _rows),
    f"{sum(1 for r in _rows if r['monotone'])}/{len(_rows)} — the structure is a top block of "
    f"3s, a bulk of 2s, and a bottom block of 1s, at every n",
)
check(
    "R2 the 3-count and the 1-count are equal or near-equal",
    all(abs(r["n3"] - r["n1"]) <= 1 for r in _rows),
    "n3 vs n1: " + ", ".join(f"{r['n3']}/{r['n1']}" for r in _rows)
    + " — the 1s are what PAY for the 3s, so they come in matched blocks",
)

# --------------------------------------------------------------------------------------------
print()
print("R3  the deviation count against n — this is what sets the excess's growth")
print(f"    {'n':>6} {'gaps':>6} {'devs':>6} {'frac':>8} {'devs/n^.25':>11}")
for r in _rows:
    q4 = mp.mpf(r["n"]) ** mp.mpf("0.25")
    print(f"    {r['n']:6d} {r['ngaps']:6d} {r['ndev']:6d} "
          f"{mp.nstr(mp.mpf(r['ndev']) / r['ngaps'], 4):>8} "
          f"{mp.nstr(mp.mpf(r['ndev']) / q4, 5):>11}")
_first, _last = _rows[0], _rows[-1]
_grow_n = mp.mpf(_last["n"]) / _first["n"]
_grow_d = mp.mpf(_last["ndev"]) / _first["ndev"]
_alpha = mp.log(_grow_d) / mp.log(_grow_n)
print(f"    n grows {mp.nstr(_grow_n, 5)}x, deviation count grows {mp.nstr(_grow_d, 5)}x "
      f"=> exponent {mp.nstr(_alpha, 5)}  (n^{{1/4}} = 0.25, n^{{1/2}} = 0.5)")
check(
    "R3 the deviation count grows SUB-linearly in l — the perturbation stays sparse",
    _rows[-1]["ndev"] / _rows[-1]["ngaps"] < _rows[0]["ndev"] / _rows[0]["ngaps"],
    f"deviating fraction falls {mp.nstr(mp.mpf(_first['ndev']) / _first['ngaps'], 4)} -> "
    f"{mp.nstr(mp.mpf(_last['ndev']) / _last['ngaps'], 4)}; count exponent "
    f"{mp.nstr(_alpha, 4)}. Only 5 points — an exponent, not a proof",
)

# --------------------------------------------------------------------------------------------
print()
print("R4  the single-widened-gap model — mine, and refuted by R1")
print(f"    {'G':>3} {'energy cost':>13} {'pair saving':>13} {'net':>12}")
_model = []
for G in range(3, 10):
    cost = LNQ * mp.mpf((G - 2) ** 2) / 2
    # row 0's gaps to the rows below run 2,4,6,... at G=2 and G, G+2, G+4, ... after widening
    save = sum((eps(2 * j) - eps(2 * j + G - 2) for j in range(1, 600)), mp.mpf(0))
    _model.append((G, cost, save, save - cost))
    print(f"    {G:3d} {mp.nstr(cost, 8):>13} {mp.nstr(save, 8):>13} "
          f"{mp.nstr(save - cost, 8):>12}")
_bestG = max(_model, key=lambda t: t[3])[0]
print(f"    model's optimal single gap: G = {_bestG}")
print(f"    measured maximum gap in ANY optimal shape: {_maxgap}")
check(
    "R4 the single-widened-gap model is REFUTED by the measured profiles",
    _bestG > _maxgap,
    f"the model prefers G = {_bestG} (net +{mp.nstr(max(t[3] for t in _model), 4)}); no "
    f"measured optimum uses a gap above {_maxgap}. It holds l FIXED, which forces the "
    f"compensating shift uniformly across rows; the real optimum moves l instead and pays "
    f"with explicit 1-gaps. Recorded as refuted rather than published as a story",
)

# --------------------------------------------------------------------------------------------
print()
_n_ok = sum(1 for _, ok, _ in CHECKS if ok)
print(f"=== {_n_ok}/{len(CHECKS)} checks pass ===")
print()
print("VERDICT")
print("  The maximiser has a SHAPE, and it is sharper than 'mean gap 2': a top block of")
print("  3-gaps, a bulk of 2-gaps, a bottom block of 1-gaps, with the 3-count and 1-count")
print("  matched and NO gap above 3. It is a unit perturbation of the staircase on a sparse")
print("  set of positions, and the deviating fraction FALLS with n.")
print()
print("  That is what a pair-term lower bound now has to handle, and it is a much smaller")
print("  target than the general mean-gap-2 configuration: the pair term of a shape whose")
print("  gaps are all within 1 of 2 differs from the staircase's by a bounded amount per")
print("  deviating position.")
print()
print("  NOT established: a pair-term lower bound, and nothing here proves the {1,2,3}")
print("  structure is FORCED -- it is what a heuristic search found at five n. A shape with")
print("  a wide gap could exist and be missed. R4 is the honest companion: my own closed-form")
print("  model of the maximiser predicted G = 5 and the data say otherwise.")

_out = {
    "schema": "qou-witness/v1",
    "computedAt": datetime.now(timezone.utc).isoformat(),
    "computation": os.path.basename(__file__),
    "bean": "qou-hok7",
    "anchor": "physical_proton",
    # Canonical anchor key read by the q0 audits/ratchet (the "anchor" key above is
    # a near-miss spelling they cannot see), plus scriptFile provenance.
    "q0Anchor": "proton",
    "scriptFile": os.path.basename(__file__),
    "q0Value": Q_50_DIGIT_STR,
    "description": (
        "The gap profile of the best shape found at each n: a top block of 3-gaps, a bulk of "
        "2s, a bottom block of 1s, no gap above 3. Also refutes a single-widened-gap model "
        "(mine) that predicted an optimal gap of 5."
    ),
    "source_witness": "rev-energy-gap-rigidity.witness.json",
    "profiles": [
        {"n": r["n"], "k": r["k"], "l": r["l"], "gap_histogram": {str(a): b
                                                                  for a, b in r["hist"].items()},
         "n_three": r["n3"], "n_one": r["n1"], "n_deviations": r["ndev"],
         "n_gaps": r["ngaps"], "threes_before_ones": r["monotone"], "gaps": r["gaps"]}
        for r in _rows
    ],
    "deviation_count_exponent": mp.nstr(_alpha, 12),
    "single_gap_model_refuted": {
        "model_optimal_G": _bestG,
        "measured_max_gap": _maxgap,
        "table": [{"G": G, "energy_cost": mp.nstr(c, 12), "pair_saving": mp.nstr(s, 12),
                   "net": mp.nstr(nt, 12)} for (G, c, s, nt) in _model],
    },
    "constants": {"A": mp.nstr(A_CONST, 30), "E_2": mp.nstr(E2_CONST, 30),
                  "ln_q0": mp.nstr(LNQ, 30)},
    "checks": [{"name": n, "ok": ok, "detail": d} for (n, ok, d) in CHECKS],
    "verdict": (
        "The maximiser is a unit perturbation of the staircase: 3s at the top, 1s at the "
        "bottom, no gap above 3, deviating fraction falling with n. A single-widened-gap "
        "model predicting G=5 is refuted. No pair-term lower bound is claimed, and the "
        "{1,2,3} structure is measured, not proved forced."
    ),
}
_path = os.path.join(_HERE, "rev-optimal-gap-profile.witness.json")
with open(_path, "w", encoding="utf-8") as fh:
    json.dump(_out, fh, indent=2)
    fh.write("\n")
print()
print(f"witness -> {_path}")

sys.exit(0 if _n_ok == len(CHECKS) else 1)
