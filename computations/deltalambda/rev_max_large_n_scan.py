#!/usr/bin/env python3
r"""
rev_max_large_n_scan.py — extend M_n = max_lambda (R_lambda - E_lambda) to larger n (qou-hok7)

`qou-hok7`'s remaining open question is whether the proved `O(n^{3/4})` upper bound on REV is
SHARP, against the proved `Omega(sqrt n)` lower bound. The obstruction recorded on that bean is
that the two candidate rates cannot be separated on the data available: at `n <= 44`,

    M_n / sqrt(n)      2.02  2.53  2.88  3.12  3.19    still RISING
    M_n / n^{3/4}      1.01  1.15  1.21  1.24  1.24    flattening, not flat

and slow convergence is established for this object (the staircase ratio is still 4.466 at n = 435
against its own limit 5.0959), so a rising `sqrt n` ratio is consistent with BOTH rates.

This probe extends `M_n` — the maximum alone, not the full free energy — to the largest `n` this
container can reach. `M_n` needs a full scan over `p(n)` partitions, so the cost is `~n * p(n)`:

    p(44) =    75,175        p(52) =   281,589
    p(48) =  147,273         p(56) =   526,823
    p(50) =  204,226         p(60) =   966,467

## What it computes, and what it does NOT

`M_n = max_lambda [ R_lambda - (H(lambda) - H_min(n)) ln q_0 ]`, with
`R_lambda = sum_c eps_{h(c)} - sum_{i<=n} eps_i` (identity (E), proved in #7010).

It does **not** compute `REV_n` itself, which needs the whole `logsumexp` over `p(n)` shapes and
carries the entropy term on top. `M_n` is a LOWER bound on `REV_n` and the term whose rate is in
question; the entropy adds at the same order (measured: `(REV - M)/sqrt(n)` rising 0.754 -> 1.146
over `n = 8..46`), so a rate for `M_n` does not by itself settle `REV_n`. Stated because conflating
the two is the obvious misreading.

## Arithmetic

mpmath throughout, no float64. The scan runs at `mp.dps = 30`, which is far more than the ~6
significant figures the ratios are read to, and every reported `M_n` is RECOMPUTED at
`mp.dps = 60` from its argmax shape before being printed — so the scan precision affects only which
shape is selected, never a reported number. A shape mis-selected at 30 dps would have to be within
1e-25 of the true maximum, which cannot move the third significant figure of the ratio.
"""

from __future__ import annotations

import argparse
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

from hmin_closed_form_and_rev_sublinearity_probe import H_min_closed  # noqa: E402


def partitions_desc(n, maxpart=None):
    """Partitions of n as weakly decreasing tuples."""
    if maxpart is None:
        maxpart = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, maxpart), 0, -1):
        for rest in partitions_desc(n - first, first):
            yield (first,) + rest


def hook_multiset(lam):
    """(sum of hook lengths, list of hook lengths) — pure integer arithmetic."""
    conj = [0] * (lam[0] + 1)
    for j in range(lam[0]):
        conj[j] = sum(1 for p in lam if p > j)
    hs = []
    tot = 0
    for i, row in enumerate(lam):
        for j in range(row):
            h = row - j + conj[j] - i - 1
            hs.append(h)
            tot += h
    return tot, hs


def scan(n, et, lnq, hmin, progress_every=200000):
    """Return (M_n at scan precision, argmax shape, count) by full enumeration."""
    sf = sum(et[i] for i in range(1, n + 1))
    best_val = None
    best_lam = None
    cnt = 0
    t0 = time.time()
    for lam in partitions_desc(n):
        cnt += 1
        H, hs = hook_multiset(lam)
        acc = et[0]
        for h in hs:
            acc += et[h]
        val = (acc - sf) - (H - hmin) * lnq
        if best_val is None or val > best_val:
            best_val = val
            best_lam = lam
        if progress_every and cnt % progress_every == 0:
            el = time.time() - t0
            print(f"      n={n}: {cnt:,} shapes, {el:.0f}s elapsed, "
                  f"best so far {mp.nstr(best_val, 8)}", flush=True)
    return best_val, best_lam, cnt, time.time() - t0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ns", default="44,48,50,52",
                    help="comma-separated n values to scan")
    ap.add_argument("--scan-dps", type=int, default=30)
    args = ap.parse_args()
    ns = [int(x) for x in args.ns.split(",") if x.strip()]

    print("=" * 78)
    print("M_n = max_lambda (R_lambda - E_lambda), extended   (qou-hok7)")
    print("=" * 78)

    rows = []
    for n in ns:
        # --- scan at reduced precision, purely to SELECT the argmax
        mp.dps = args.scan_dps
        Q0 = Q_MP
        lnq = mp.log(Q0)
        T = Q0 ** 2
        et = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, 4 * n + 400)]
        hmin = H_min_closed(n)
        print(f"\n  scanning n={n} (H_min={hmin}) at {args.scan_dps} dps ...", flush=True)
        _v, lam, cnt, el = scan(n, et, lnq, hmin)

        # --- RECOMPUTE the winner at full precision; only this number is reported
        mp.dps = 60
        Q0 = Q_MP
        lnq = mp.log(Q0)
        T = Q0 ** 2
        et60 = [mp.mpf(0)] + [-mp.log(1 - T ** (-m)) for m in range(1, 4 * n + 400)]
        sf = sum(et60[i] for i in range(1, n + 1))
        H, hs = hook_multiset(lam)
        M = (sum(et60[h] for h in hs) - sf) - (H - hmin) * lnq

        r = {"n": n, "M": mp.nstr(M, 16), "argmax": list(lam), "partitions": cnt,
             "seconds": round(el, 1),
             "M_over_sqrt_n": mp.nstr(M / mp.sqrt(n), 10),
             "M_over_n34": mp.nstr(M / (mp.mpf(n) ** mp.mpf("0.75")), 10)}
        rows.append(r)
        print(f"    n={n}: {cnt:,} shapes in {el:.0f}s | M={mp.nstr(M, 10)} "
              f"| M/sqrt(n)={r['M_over_sqrt_n']} | M/n^0.75={r['M_over_n34']}", flush=True)
        print(f"      argmax {lam}", flush=True)

    print()
    print("-" * 78)
    print(f"  {'n':>4} {'M_n':>12} {'M/sqrt n':>11} {'M/n^0.75':>11} {'p(n)':>10} {'sec':>7}")
    for r in rows:
        print(f"  {r['n']:>4} {r['M'][:11]:>12} {r['M_over_sqrt_n'][:10]:>11} "
              f"{r['M_over_n34'][:10]:>11} {r['partitions']:>10,} {r['seconds']:>7.0f}")
    print()
    print("  Read BOTH columns. A rising M/sqrt(n) alone does not imply n^{3/4}; the staircase")
    print("  ratio is still 4.466 at n=435 against its own limit 5.0959, so slow convergence to")
    print("  a constant looks identical to a higher power over any short range.")
    print("  M_n is a LOWER bound on REV_n and does not settle REV_n's own rate: the entropy")
    print("  term adds at the same order.")

    payload = {
        "probe": "rev_max_large_n_scan",
        "bean": "qou-hok7",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "q0_anchor": "physical_proton",
        "scan_dps": args.scan_dps,
        "report_dps": 60,
        "computes": "M_n = max over partitions of (R_lambda - E_lambda); NOT REV_n itself",
        "rows": rows,
    }
    out = os.path.join(_COMPUTATIONS, "rev-max-large-n-scan.witness.json")
    with open(out, "w") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(f"\nwitness -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
