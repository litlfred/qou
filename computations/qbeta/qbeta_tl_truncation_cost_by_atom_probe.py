#!/usr/bin/env python3
"""qbeta_tl_truncation_cost_by_atom_probe.py — how much of the Hecke tower does
convention D discard?  Catalan(n)/n!, i.e. 83 % retained at A=1 and 0.043 % at
A=4.

Bean `qou-cds1`.  Scope-(b): exact integer combinatorics.

## Why this exists

The companion probe (`qbeta_c_vs_d_are_different_algebras_probe.py`) established
that convention D is the Temperley-Lieb quotient, which keeps only partitions
with at most two rows, and I described the discarded part as "the overwhelming
majority of the tower".  That was an ADJECTIVE.  This replaces it with a number,
because the owner has a ruling to make between

  * 2026-08-15 -- convention D canonical, and
  * 2026-09-03 -- derivations on the FULL TOWER,

and an adjective is not something to rule on.

## Measured, exactly (hook-length formula; `sum_lambda (f^lambda)^2 = n!` asserted)

    n    A=n/3   dim H_n = n!            dim TL_n            retained
    3    1                  6                   5            83.3333 %
    6    2                720                 132            18.3333 %
    9    3            362,880               4,862             1.3398 %
    12   4        479,001,600             208,012             0.0434 %
    15   5  1,307,674,368,000           9,694,845             0.0007 %
    18   6  6,402,373,705,728,000     477,638,700             ~0 %

and `dim TL_n = Catalan(n)` exactly at every `n` checked -- verified here rather
than quoted, by summing `(f^lambda)^2` over the <=2-row partitions and comparing
to `C(2n,n)/(n+1)`.

## What the number actually says -- and it is NOT "D is wrong"

The cost of the truncation is **n-dependent, and the two rulings live at
different `n`**:

  * The Q_beta ladder is an `H_3` object (A=1).  There D retains **83 %**, and
    discards a single 1-dimensional block.  That is why the C-vs-D difference on
    `beta_Bor` shows up only in the 4th decimal (registry: 0.99836662 vs
    0.99856216).
  * The mass / binding work is at `n = 3A`.  At ⁴He (`n = 12`) D retains
    **0.043 %**; by ⁶Li it is 7e-6.

So "D canonical" and "use the full tower" may both be right in their own
domains, and the live question is not which ruling wins globally but WHERE the
crossover bites.  This probe measures; it does not adjudicate.

## Precision

Exact integer arithmetic throughout (`math.factorial`, `math.comb`, integer
hook-length products).  No floating point in any claim; the percentages are
display only.
"""
from __future__ import annotations

import json
import pathlib as _pl
import sys as _sys
from math import comb, factorial

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

from witness_base import WitnessBuilder                         # noqa: E402

RESULTS: list[dict] = []


def record(name, passed, detail):
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


def partitions(n, mx=None):
    mx = n if mx is None else mx
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hook_dims(n):
    """f^lambda for every partition of n, by the hook-length formula (exact)."""
    out = {}
    for lam in partitions(n):
        conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
        prod = 1
        for i, row in enumerate(lam):
            for j in range(row):
                prod *= (row - j) + (conj[j] - i) - 1
        out[lam] = factorial(n) // prod
    return out


rows = {}
burnside_ok, catalan_ok = True, True
for n in (3, 6, 9, 12, 15, 18):
    d = hook_dims(n)
    full = sum(f * f for f in d.values())
    tl = sum(f * f for lam, f in d.items() if len(lam) <= 2)
    cat = comb(2 * n, n) // (n + 1)
    burnside_ok &= (full == factorial(n))
    catalan_ok &= (tl == cat)
    rows[n] = {"A": n // 3, "dim_H_n": full, "dim_TL_n": tl,
               "catalan_n": cat, "retained_pct": f"{100*tl/full:.4f}"}

record(
    "burnside_check_sum_of_squares_is_n_factorial",
    burnside_ok,
    "sum_lambda (f^lambda)^2 = n! at every n in {3,6,9,12,15,18}, so the "
    "hook-length dimensions are right before anything is concluded from them.",
)

record(
    "two_row_sector_dimension_is_exactly_catalan",
    catalan_ok,
    "summing (f^lambda)^2 over the <=2-row partitions gives exactly "
    "C(2n,n)/(n+1) at every n checked — i.e. dim TL_n = Catalan(n), verified "
    "rather than quoted. This is the dimension convention D retains.",
)

record(
    "truncation_cost_is_n_dependent_83pct_at_A1_and_0.04pct_at_A4",
    rows[3]["dim_TL_n"] * 100 > 83 * rows[3]["dim_H_n"]
    and rows[12]["dim_TL_n"] * 10000 < 5 * rows[12]["dim_H_n"],
    "; ".join(f"n={n} (A={r['A']}): {r['dim_TL_n']:,}/{r['dim_H_n']:,} = "
              f"{r['retained_pct']} %" for n, r in rows.items())
    + ". So the cost is n-DEPENDENT: the Q_beta ladder is an H_3 object where D "
      "discards a single 1-dim block and keeps 83 %, which is why C-vs-D differs "
      "only in the 4th decimal on beta_Bor (0.99836662 vs 0.99856216); the mass "
      "work is at n = 3A, where ^4He retains 0.043 %.",
)

record(
    "this_replaces_an_adjective_and_adjudicates_nothing",
    True,
    "the companion PR called the discarded part 'the overwhelming majority of "
    "the tower' — an adjective, and not something an owner can rule on. The "
    "number says 'D canonical' (2026-08-15) and 'use the full tower' "
    "(2026-09-03) may BOTH be right in their own domains, and the live question "
    "is where the crossover bites. Measured, not adjudicated.",
)

out = {
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "how much of the Hecke tower does convention D discard?",
    "answer": "Catalan(n)/n! is retained: 83.3 % at n=3 (A=1), 0.043 % at n=12 "
              "(A=4). The cost is n-dependent, so the D-canonical and full-tower "
              "rulings may both hold in their own domains.",
    "scope": "(b) — exact integer combinatorics. Adjudicates neither ruling.",
    "table": rows,
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
WitnessBuilder.stamp_staleness_metadata(out, script_path=__file__, engine="python")
wp = _HERE.parent / "qbeta-tl-truncation-cost-by-atom.witness.json"
wp.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wp}\nallPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
