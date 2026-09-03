#!/usr/bin/env python3
"""M_1>0: kappa_n EXACTLY, and where the n >= 13 threshold comes from.

Gap qou-k5r5, bean qou-t6hc. The gap reduces M_1 > 0 to two claims:

    (a) exact M_1 > 0 for n <= 12   [done, verified to n = 50]
    (b) kappa_n >= kappa for n >= 13,  kappa = 128/(225 pi^2)

with kappa_n = M_1(n)/n^{5/2}. Sampling cannot settle (b): the sampled kappa_n
wobbles by more than the quantity in dispute. M_1(n) is an exact rational
(sum over partitions of dim^2 X / n!), so this probe computes it exactly.

FINDING 1: 13 is not a convention -- it is the crossing point
--------------------------------------------------------------
kappa_n/kappa, exact: 0.723 (n=4), 0.946 (n=8), 0.99932 (n=12), 1.00234 (n=13).
kappa_n < kappa for n = 2..12 and kappa_n > kappa for every n from 13 up. So the
"n >= 13" in the gap statement is exactly where the sequence crosses its own
limit, and n = 13 is the BINDING case of claim (b) -- margin 0.23 %.

FINDING 2: the shape is rise, peak, fall -- not monotone either way
--------------------------------------------------------------------
I expected kappa_n decreasing to kappa from above, which would have made (b) a
corollary of monotonicity. WRONG. Exactly: kappa_n INCREASES from n = 3 to a
peak at n = 32 (kappa_32 = 1.026988 kappa), and decreases from n = 33 onward
(n = 33..42 all decreasing). Sampled continuation: 0.0590 at n = 50 falling to
0.0577 by n = 1600, i.e. back toward kappa from above.

So claim (b) splits into two genuinely different regimes, and only the first is
finite:

    n = 13..42   verified EXACTLY here, minimum margin 0.23 % at n = 13
    n >= 43      needs kappa_n decreasing with limit kappa -- an asymptotic
                 statement with an effective error bound, NOT a finite check

That is a sharper decomposition than "measured", and it says where the remaining
work is: an error term, not a monotonicity.

FINDING 3: claim (b) is STRONGER THAN THE GOAL NEEDS
-----------------------------------------------------
M_1(n) > 0 is equivalent to kappa_n > 0, since n^{5/2} > 0. So the tail does not
need kappa_n >= kappa; it needs only

    |kappa_n - kappa| < kappa                                            (b')

and the gap between what those two demand of an effective error bound is large
and measurable. Over the exactly-computed range n = 32..46, |kappa_n-kappa|/kappa
runs 0.0270 -> 0.0255, so

  * (b) asks the bound to resolve the SIGN of a quantity that is ~2.6 % of kappa
    -- relative accuracy better than 2.6 %;
  * (b') asks only |kappa_n - kappa| < kappa -- relative accuracy 100 %, a ~38x
    slacker demand, and any crude Kerov error term does it.

Formalised as QOU.BraidKnot.M1EdgeCalculus.pos_of_check_and_tail: a finite exact
check up to N plus the CRUDE tail bound past it gives positivity throughout. The
supporting lemma pos_of_abs_sub_lt needs no positivity hypothesis on kappa at
all -- |x - k| < k already forces both 0 < k and 0 < x, since the left side is
non-negative. Both sorry-free.

This does not close the gap. It replaces a demanding analytic requirement with
an undemanding one, and says so precisely.
"""
import json
import sys
import time
from fractions import Fraction as F
from math import factorial  # float64-ok: exact integer factorial, no float path
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 40


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def dim(lam, nf):
    if not lam:
        return 1
    conj = [sum(1 for l in lam if l >= j + 1) for j in range(lam[0])]
    p = 1
    for i, l in enumerate(lam):
        for j in range(l):
            p *= (l - j - 1) + (conj[j] - i - 1) + 1
    return nf // p


def main():
    t0 = time.monotonic_ns()
    # 34, not 30. FINDING 3 measures the TAIL, `rel[30:]`, i.e. n = 32 onward,
    # so a default below 32 leaves that slice empty. The committed witness was
    # produced at 34 (`"nmax": 34` in it) and cannot be reproduced by a bare
    # `python3 <this file>` while the default is 30. Costs 2 s.
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 34
    KAP = mpf(128) / (225 * mp.pi ** 2)
    checks = []
    rows = []
    for n in range(2, NMAX + 1):
        nf = factorial(n)
        EA = EB = EAB = F(0)
        for lam in partitions(n):
            d = dim(lam, nf)
            w = F(d * d, nf)
            A = (sum(i * l for i, l in enumerate(lam))
                 + sum(l * (l - 1) // 2 for l in lam) + n)
            B = sum((j - i) ** 2 for i, l in enumerate(lam) for j in range(l))
            EA += w * A; EB += w * B; EAB += w * A * B
        M1 = EAB - EA * EB
        kn = (mpf(M1.numerator) / mpf(M1.denominator)) / mpf(n) ** mpf("2.5")
        rows.append({"n": n, "M1": str(M1), "kappa_n": nstr(kn, 10),
                     "ratio": nstr(kn / KAP, 8)})
    ratios = [mpf(r["ratio"]) for r in rows]
    below = [r["n"] for r, x in zip(rows, ratios) if x < 1]
    above = [r["n"] for r, x in zip(rows, ratios) if x >= 1]
    checks.append({
        "name": "FINDING 1: kappa_n crosses kappa at exactly n = 13",
        "pass": below == list(range(2, 13)) and min(above) == 13,
        "detail": (
            f"Exact rational M_1(n) for n = 2..{NMAX}. kappa_n < kappa exactly "
            f"for n = {below[0]}..{below[-1]}, and kappa_n >= kappa for every "
            f"n from {min(above)} up. So the gap's 'n >= 13' is the crossing "
            f"point of the sequence with its own limit, not a convention. "
            f"kappa_13/kappa = {rows[11]['ratio']} -- a 0.23 % margin, and the "
            f"BINDING case of claim (b)."),
    })
    peak = max(range(len(rows)), key=lambda i: ratios[i])
    tail_dec = all(ratios[i] > ratios[i + 1] for i in range(peak, len(rows) - 1))
    checks.append({
        "name": "FINDING 2 (my expectation FALSIFIED): rise, peak, then fall",
        "pass": peak > 0 and (tail_dec or peak == len(rows) - 1),
        "detail": (
            f"I briefed the expectation that kappa_n DECREASES to kappa, which "
            f"would have made claim (b) a corollary of monotonicity. It does "
            f"not. Exactly: kappa_n rises to a peak at n = {rows[peak]['n']} "
            f"(ratio {rows[peak]['ratio']}) and falls thereafter"
            f"{' (monotone over the computed tail)' if tail_dec else ''}. "
            f"Sampled continuation from ..._kappa_derivation.py: 0.0590 at "
            f"n = 50 down to 0.0577 by n = 1600, i.e. back toward kappa from "
            f"above. So claim (b) is NOT one statement: n = 13..{NMAX} is a "
            f"finite exact check, and n > {NMAX} needs an effective error bound "
            f"on kappa_n - kappa. That is where the remaining work is."),
    })
    # ---- FINDING 3: the weaker sufficient claim ----------------------------
    rel = [abs(mpf(r["kappa_n"]) - KAP) / KAP for r in rows]
    # REFUSE rather than substitute. The old fallback was
    #     max(rel[30:]) if len(rel) > 30 else max(rel)
    # which, when the tail slice is empty, silently measured the max over the
    # WHOLE range (n = 2 up, where kappa_n/kappa is ~0.72 at n = 4) and then
    # reported it under this check's own label "over n = 32..{NMAX}". At the
    # then-default NMAX = 30 that printed the self-contradictory range
    # "n = 32..30", a worst_rel of 1.0, and a FAIL -- a wrong quantity under a
    # true-looking string, which is worse than an error.
    if len(rel) <= 30:
        raise SystemExit(
            f"FINDING 3 needs the tail n >= 32, i.e. NMAX >= 32; got NMAX = "
            f"{NMAX} ({len(rel)} rows). Re-run with a larger NMAX -- do not\n"
            f"read a whole-range maximum as a tail maximum.")
    worst_rel = max(rel[30:])
    n13 = next(r for r in rows if r["n"] == 13)
    checks.append({
        "name": "FINDING 3: (b') |kappa_n - kappa| < kappa suffices, with ~38x more room",
        "pass": worst_rel < mpf(1) / 10,
        "detail": (
            f"M_1(n) > 0 iff kappa_n > 0, since n^(5/2) > 0, so the tail needs "
            f"only |kappa_n - kappa| < kappa, not kappa_n >= kappa. Measured: "
            f"over n = 32..{NMAX} the ratio |kappa_n - kappa|/kappa is at most "
            f"{nstr(worst_rel, 6)}, i.e. an effective bound has a "
            f"{nstr(1 / worst_rel, 4)}x margin under (b'), against the ~2.6 % "
            f"relative accuracy (b) would need to resolve the sign. At the "
            f"binding n = 13 the (b) margin is only "
            f"{nstr((mpf(n13['ratio']) - 1) * 100, 3)} % -- but n = 13 is inside "
            f"the exact range, so that costs nothing. Formalised as "
            f"QOU.BraidKnot.M1EdgeCalculus.pos_of_check_and_tail. This does NOT "
            f"close the gap; it replaces a demanding analytic requirement with "
            f"an undemanding one."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-kappa-n-exact.witness.json").write_text(
        json.dumps({
        "q0Anchor": "independent",
        "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: M_1>0: kappa_n EXACTLY, and where the n >= 13 threshold comes from.",
            "probe": "m1_kappa_n_exact", "bean": ["qou-t6hc", "qou-k5r5"],
            "kappa": nstr(KAP, 15), "nmax": NMAX, "exact": rows,
            "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print(f"RESULT: kappa_n < kappa for n <= 12, >= kappa for n >= 13 -- exactly.")
    print(f"RESULT: the shape is rise / peak / fall, so claim (b) is a finite exact")
    print(f"RESULT:   check plus an ASYMPTOTIC error bound, not a monotonicity.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
