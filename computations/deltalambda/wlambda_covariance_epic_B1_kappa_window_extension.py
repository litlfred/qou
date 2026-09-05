#!/usr/bin/env python3
"""B1: extend the EXACT kappa_n window past n <= 67.  Gap qou-k5r5, Track B.

WHY
---
`M_1 = Cov_Planch(Sum_h, Sum_c^2) = kappa_n * n^{5/2}`, and the arc's open nub is
the ONE-SIDED statement `kappa_n >= kappa` for `n >= 13`, with
`kappa = 128/(225 pi^2)` (derived, PR #5428).  Track A must prove the sign of the
genus-1 second-order correction; the ORDER of that correction is undetermined at
reachable n -- the measured effective exponent was still rising (~0.25 -> 0.36
over n = 40..64), so it is not yet clear whether the correction is `n^{-1/2}`
bulk, `n^{-2/3}` edge, or a mix.

This probe does NOT prove the sign.  Per the 2026-08-28 revised workplan, Track B
exists to *guide* Track A: a wider exact window sharpens the effective-exponent
measurement and so tells A which order to expect, de-risking A3.

WHAT IT COMPUTES
----------------
Exact `kappa_n` as a `Fraction`, for a requested range of `n`, by direct
Plancherel summation over every partition:

    M_1 = E[H . C2] - E[H] . E[C2],   E[X] = sum_lambda (f^lambda)^2 / n! . X

with `H = sum_cells hook`, `C2 = sum_cells content^2`.  Every quantity is an
exact integer or `Fraction`; the comparison against `kappa` is mpmath at 60 dps.
**No float64 anywhere.**

TWO CLOSED FORMS REPLACE TWO CELL WALKS
---------------------------------------
The committed `..._M1_onesided_kappa_bound.py` walks all `n` cells three times
per partition -- once for the hook product, once for `H`, once for `C2`.  The
last two have closed forms, verified against that script on all 507 partitions
of `n = 1..14` and on its own output for `n = 3..20`:

    H  = sum_i C(lambda_i, 2) + sum_j C(lambda'_j, 2) + n
    C2 = sum_i [ m(m-1)(2m-1)/6 - i.m(m-1) + i^2.m ],   m = lambda_i

`H` because `h = arm + leg + 1` and the arm/leg sums telescope per row/column.

Measured speedup: **1.31x** (n = 55: 8.1s against 10.6s).  Modest, and that is
the honest finding -- the hook product still needs its `O(n)` walk, and the cost
is Python loop overhead rather than big-integer arithmetic.  A beta-number
(first-column hook) formula for `f^lambda`, evaluated on whichever of
`lambda` / `lambda'` has fewer rows, was tried and is NOT faster (1.25x): the
`O(r^2)` pair product plus one big `n! * num // den` costs about what the
`O(n)` walk costs at these sizes.  Recorded so it is not re-attempted.

SCALING, MEASURED
-----------------
n = 50 -> 3.4s, 55 -> 8.1s, 60 -> 19.1s: a factor of ~2.35 per +5 in n.  So each
further step costs about 1.19x the last, and the window extends by brute force
alone.  `p(85) ~ 3e7` partitions is the practical wall for this approach in
Python; a materially wider window needs a different algorithm, not a faster loop.

Usage:  python3 <this> NMIN NMAX  [--out PATH]
scope-(a); no fit; nothing wired; no c_k; L2 unchanged.  Gap qou-k5r5 OPEN.
"""
from __future__ import annotations

import json
import os
import sys
import time
from fractions import Fraction as F

import mpmath as mp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

sys.path[:0] = [
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "substrate"),
]
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60


def partitions(n):
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for p in range(min(n, mx), 0, -1):
            for r in gen(n - p, p):
                yield (p,) + r
    yield from gen(n, n)


def factorial(n):
    r = 1
    for k in range(2, n + 1):
        r *= k
    return r


def conj(lam):
    if not lam:
        return ()
    c = [0] * lam[0]
    for part in lam:
        for j in range(part):
            c[j] += 1
    return tuple(c)


def exact_M1(n):
    """Cov_Planch(Sum_h, Sum_c^2), exact Fraction."""
    nf = factorial(n)
    sX = sY = sXY = 0
    for lam in partitions(n):
        cj = conj(lam)
        prod = 1
        for i, part in enumerate(lam):
            ci = i + 1
            for j in range(part):
                prod *= part - j + cj[j] - ci
        f = nf // prod
        w = f * f
        H = sum(p * (p - 1) for p in lam) // 2 + sum(c * (c - 1) for c in cj) // 2 + n
        C2 = 0
        for i, m in enumerate(lam):
            C2 += m * (m - 1) * (2 * m - 1) // 6 - i * m * (m - 1) + i * i * m
        sX += w * H
        sY += w * C2
        sXY += w * H * C2
    return F(sXY, nf) - F(sX, nf) * F(sY, nf)



def _derived(rows, kappa):
    """The analysis the witness records, recomputed from `rows` alone.

    Every field here was previously assembled OUTSIDE this script: the commit
    that added `b1-kappa-window-extension.witness.json` added no script at all,
    so its `scriptFile` named a file that writes no witness, the provenance
    audit reported it NOT_A_PRODUCER, and `run_pipeline` treated a witness
    nothing could regenerate as current. `durationMs: 53` on a ~28-minute
    compute is the other tell.

    Reconstructed and verified BEFORE being wired in: all 8
    `windowed_exponents` and `secant_over_new_window` reproduce the committed
    values to their recorded 8 significant digits, exactly — and again after,
    against a full 1919 s run.

    The exponent is the log-log secant of `kappa_n - kappa` against `n`: a
    two-point slope over each window, negated so a decaying difference reads as
    a positive order.
    """
    by_n = {int(r["n"]): r for r in rows}
    ns = sorted(by_n)

    def d(n):
        r = by_n[n]
        return (mp.mpf(int(r["M1_num"])) / int(r["M1_den"])
                / mp.power(n, mp.mpf(5) / 2) - kappa)

    def slope(lo, hi):
        return -(mp.log(d(hi)) - mp.log(d(lo))) / (mp.log(hi) - mp.log(lo))

    # `slope` takes log(kappa_n - kappa), so it is real only where that
    # difference is POSITIVE. The one-sided premise says it is for n >= 13, but
    # a range straddling the crossover makes the log complex and mpmath then
    # rejects its own `nstr` output on the way back in. Reported as an empty
    # analysis rather than crashing, or worse, emitting a complex number
    # dressed as an exponent.
    if any(d(n) <= 0 for n in ns):
        return {
            "kappa": mp.nstr(kappa, 26),
            "rows": rows,
            "windowed_exponents": {},
            "exponents_undefined_because":
                "kappa_n - kappa is not positive throughout this range, so its "
                "log-log slope is not real; the one-sided premise holds only "
                "for n >= 13",
        }
    windows = {f"{ns[i]}..{ns[i + 3]}": mp.nstr(slope(ns[i], ns[i + 3]), 8)
               for i in range(len(ns) - 3)}
    lo_key = min(windows, key=lambda k: mp.mpf(windows[k]))
    return {
        "kappa": mp.nstr(kappa, 26),
        "rows": rows,
        # The window's second point: the verdict reads "a minimum NEAR
        # n = 71-72", reported as one n rather than a 4-wide window.
        "local_exponent_min_near": int(lo_key.split("..")[0]) + 1,
        "windowed_exponents": windows,
        "secant_over_new_window": mp.nstr(slope(ns[0], ns[-1]), 8),
    }


def main() -> int:
    nmin = int(sys.argv[1]) if len(sys.argv) > 1 else 68
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 72
    out = None
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]

    kappa = mp.mpf(128) / (225 * mp.pi ** 2)
    rows = []
    t0 = time.time()
    print(f"# kappa = 128/(225 pi^2) = {mp.nstr(kappa, 20)}")
    print(f"# {'n':>4} {'seconds':>9} {'kappa_n':>22} {'kappa_n - kappa':>16} {'sign':>5}")
    for n in range(nmin, nmax + 1):
        t = time.time()
        cov = exact_M1(n)
        dt = time.time() - t
        kap = mp.mpf(cov.numerator) / cov.denominator / mp.power(n, mp.mpf(5) / 2)
        diff = kap - kappa
        sgn = "+" if diff > 0 else ("-" if diff < 0 else "0")
        rows.append({
            "n": n,
            "M1_num": str(cov.numerator),
            "M1_den": str(cov.denominator),
            "kappa_n": mp.nstr(kap, 25),
            "kappa_n_minus_kappa": mp.nstr(diff, 12),
            "sign": sgn,
            # integer ms, not float seconds: a witness carries no raw float64,
            # and this matches the WitnessBuilder's own `durationMs`.
            "ms": int(dt * 1000),
        })
        print(f"  {n:>4} {dt:>9.1f} {mp.nstr(kap, 20):>22} {mp.nstr(diff, 6):>16} {sgn:>5}")
        sys.stdout.flush()
        if out:                      # write incrementally: a long run stays usable
            # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
            # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
            # dump runs, so any exception in between leaves the committed witness
            # empty or partial -- the shape that emptied 22 witnesses to zero bytes
            # in one `producer_importability_audit` run. `os.replace` is atomic on
            # POSIX within a filesystem, hence a SIBLING temp file.
            _wpath_sidu = out
            _wtmp_sidu = str(_wpath_sidu) + ".tmp"
            with open(_wtmp_sidu, "w") as fh:
                json.dump({"rows": rows}, fh, indent=2)
                fh.write("\n")

            _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    allpos = all(r["sign"] == "+" for r in rows)

    if "--witness" in sys.argv and len(rows) >= 4:
        data = _derived(rows, kappa)
        exps = [mp.mpf(v) for v in data["windowed_exponents"].values()]
        if not exps:
            print("  (no real exponents on this range — witness not written)")
            return 0 if allpos else 1
        ordered = sorted(rows, key=lambda r: int(r["n"]))
        ns = [int(r["n"]) for r in ordered]
        kaps = [mp.mpf(int(r["M1_num"])) / int(r["M1_den"])
                / mp.power(int(r["n"]), mp.mpf(5) / 2) for r in ordered]
        w = (
            WitnessBuilder("b1-kappa-window-extension", engine="python+mpmath")
            .set_description(
                "B1 / gap qou-k5r5 Track B: exact kappa_n over an extended n "
                "window by direct Plancherel summation, Fraction throughout, "
                "compared against kappa = 128/(225 pi^2) at 60 dps."
            )
            .add_parameter("n_min", ns[0])
            .add_parameter("n_max", ns[-1])
            .add_parameter("elapsed_sec", round(time.time() - t0, 1))
        )
        for k, v in data.items():
            w.add_data(k, v)
        w.add_assertion("all_kappa_n_exceed_kappa", computed=int(allpos),
                        expected=1, tolerance=0,
                        source="B1_kappa_window_extension")
        w.add_assertion(
            "kappa_n_strictly_decreasing",
            computed=int(all(kaps[i] > kaps[i + 1] for i in range(len(kaps) - 1))),
            expected=1, tolerance=0, source="B1_kappa_window_extension")
        w.add_assertion("window_extended_to_78", computed=ns[-1], expected=78,
                        tolerance=0, source="B1_kappa_window_extension")
        w.add_assertion(
            "effective_exponent_is_NOT_monotone",
            computed=int(not (all(exps[i] <= exps[i + 1] for i in range(len(exps) - 1))
                              or all(exps[i] >= exps[i + 1] for i in range(len(exps) - 1)))),
            expected=1, tolerance=0, source="B1_kappa_window_extension")
        w.add_assertion("exponent_below_edge_order",
                        computed=int(max(exps) < mp.mpf(2) / 3), expected=1,
                        tolerance=0, source="B1_kappa_window_extension")
        w.save()

    print(f"\nall kappa_n > kappa on [{nmin}, {nmax}]: {allpos}")
    print(f"total {time.time() - t0:.1f}s")
    return 0 if allpos else 1


if __name__ == "__main__":
    raise SystemExit(main())
