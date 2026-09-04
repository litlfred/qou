#!/usr/bin/env python3
"""M_1>0: the +/- cancellation, and why `Sum h` is the special combination.

Gap qou-k5r5, bean qou-t6hc. The gap records the obstruction as

    "M_1 = Cov(S|c|,Sc2)[+] + Cov(S_c h^2,Sc2)[-], partial cancellation of two
     ~n^{5/2} terms, ratio -> -0.62; need ratio > -1 uniformly."

This probe re-derives that split from the Plancherel GROWTH process, tests a
prediction about it, records the prediction's FAILURE, and measures whether the
"ratio > -1" worry is live.

FINDING 1: the split, from the growth chain, and its collapse to one diagram
-----------------------------------------------------------------------------
Adding a box at row r, column s raises Sum_cells h by exactly 1 + r + s: the new
cell has hook 1, and every cell left of it in its row and above it in its column
gains exactly one. Summing along a standard Young tableau,

    Sum_cells h = n + Sum_k (r_k + s_k) = Sum_k |c_k| + 2 Sum_k D_k - n

with c_k = s_k - r_k the content and D_k = min(r_k,s_k) + 1 the diagonal length
at the added corner. Checked here against a direct hook computation on every
sample. That reproduces the gap's [+]/[-] split: Sum|c_k| is the positive part,
Sum D_k the negative one.

But a path sum that equals a function of the final shape must be
path-INDEPENDENT, and the reason is that it collapses:

    Sum_cells h = Sum_cells (i + j + 1)

verified here on all 914 partitions of n <= 16 with a control, and formalised
sorry-free as QOU.BraidKnot.M1EdgeCalculus.sum_hookLen_eq_sum_coords. So the
growth-chain split is a statement about one diagram after all.

FINDING 2 (PREDICTION FALSIFIED): the split terms are NOT single-mode
---------------------------------------------------------------------
..._M1_kappa_structure.py derived that Sum c^2 is a SINGLE Kerov mode (m = 3),
and measured rho(Sum h, Sum c^2) -> 1. The natural prediction is that each half
of the split is single-mode too, which would turn the -0.62 cancellation from a
functional inequality into a comparison of two explicit constants.

It is false. rho(Sum|c_k|, Sum c^2) is FLAT at 0.979 across n = 100..1600 -- not
drifting to 1 -- and rho(Sum D_k, Sum c^2) sits near -0.95. Yet their
combination Sum h reaches 0.9975. So the off-mode components of Sum|c_k| and
2 Sum D_k CANCEL EACH OTHER, and Sum h is close to a pure m = 3 statistic while
neither of its parts is. That is a sharper statement of why Sum h is the special
combination than "it is conjugation-symmetric", and it is the reason the
cancellation cannot be reduced to two constants.

FINDING 3: the "ratio > -1" worry is not live on any accessible scale
----------------------------------------------------------------------
Measured 2 Cov(Sum D, Sum c^2) / Cov(Sum|c|, Sum c^2) = -0.648, -0.653, -0.656,
-0.655, -0.658 over n = 100..1600. It does drift more negative, but by ~0.01
per 16x in n; at that rate -1 is unreachable. And the quantity that matters,
kappa itself, is FLAT at ~0.058 over the same range while the ratio drifts --
the drift is absorbed by a compensating drift in Cov(Sum|c|, Sum c^2). A
cancellation heading for -1 would show as kappa decaying; it does not.

MEASURED, NOT PROVED, and the sampling is the weak point at n = 1600.
"""
import json
import random
import time
from bisect import bisect_right
from fractions import Fraction as F
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 30


def qf(x):
    return mpf(x.numerator) / mpf(x.denominator)


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def hook_sum(lam):
    if not lam:
        return 0
    conj = [sum(1 for l in lam if l >= j + 1) for j in range(lam[0])]
    return sum((l - j - 1) + (conj[j] - i - 1) + 1
               for i, l in enumerate(lam) for j in range(l))


def coord_sum(lam, off=1):
    return sum(i + j + off for i, l in enumerate(lam) for j in range(l))


def growth(N, rnd):
    """RSK-insert a uniform permutation. Returns per-step (content, diagonal
    length) and the final shape. The shape after k steps is Plancherel(k) and
    the chain is the Plancherel growth process."""
    perm = list(range(N))
    for i in range(N - 1, 0, -1):
        j = rnd.randrange(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    rows = []
    cs = []
    ds = []
    for x in perm:
        r = 0
        while True:
            if r == len(rows):
                rows.append([x])
                s = 0
                break
            row = rows[r]
            k = bisect_right(row, x)
            if k == len(row):
                row.append(x)
                s = k
                break
            row[k], x = x, row[k]
            r += 1
        cs.append(s - r)
        ds.append(min(r, s) + 1)
    return cs, ds, tuple(len(r) for r in rows)


def main():
    t0 = time.monotonic_ns()
    checks = []

    # ---- FINDING 1a: the one-diagram identity, exact ------------------------
    bad = ctrl = tot = 0
    for n in range(1, 17):
        for lam in partitions(n):
            tot += 1
            if hook_sum(lam) != coord_sum(lam, 1):
                bad += 1
            if hook_sum(lam) == coord_sum(lam, 0):
                ctrl += 1
    checks.append({
        "name": "FINDING 1: sum_cells h = sum_cells (i + j + 1)",
        "pass": bad == 0 and ctrl == 0,
        "detail": (
            f"Exact on all {tot} partitions of n = 1..16, {bad} violations. "
            f"CONTROL: dropping the +1 holds for {ctrl}/{tot} -- 0, so the "
            f"check can fail. Formalised sorry-free as QOU.BraidKnot."
            f"M1EdgeCalculus.sum_hookLen_eq_sum_coords, on [propext, "
            f"Classical.choice, Quot.sound]. This is why the growth-chain path "
            f"sum below is path-independent."),
    })

    # ---- FINDING 1b + 2 + 3: the growth chain -------------------------------
    plan = [(100, 20000), (200, 12000), (400, 6000), (800, 3000), (1600, 1400)]
    rows = []
    idbad = 0
    for n, ns in plan:
        rnd = random.Random(777 + n)
        sH = sY = sX = sZ = 0
        sHH = sYY = sXX = sZZ = 0
        sHY = sXY = sZY = 0
        for _ in range(ns):
            c, d, lam = growth(n, rnd)
            Y = sum(t * t for t in c)
            X = sum(abs(t) for t in c)
            Z = sum(d)
            H = X + 2 * Z - n
            if H != hook_sum(lam):
                idbad += 1
            sH += H; sY += Y; sX += X; sZ += Z
            sHH += H * H; sYY += Y * Y; sXX += X * X; sZZ += Z * Z
            sHY += H * Y; sXY += X * Y; sZY += Z * Y
        EH, EY, EX, EZ = F(sH, ns), F(sY, ns), F(sX, ns), F(sZ, ns)
        vH = qf(F(sHH, ns) - EH * EH); vY = qf(F(sYY, ns) - EY * EY)
        vX = qf(F(sXX, ns) - EX * EX); vZ = qf(F(sZZ, ns) - EZ * EZ)
        cHY = qf(F(sHY, ns) - EH * EY)
        cXY = qf(F(sXY, ns) - EX * EY)
        cZY = qf(F(sZY, ns) - EZ * EY)
        p = mpf(n) ** mpf("2.5")
        rows.append({
            "n": n, "nsamp": ns,
            "rho_h": nstr(cHY / (mp.sqrt(vH) * mp.sqrt(vY)), 6),
            "rho_abs": nstr(cXY / (mp.sqrt(vX) * mp.sqrt(vY)), 6),
            "rho_D": nstr(cZY / (mp.sqrt(vZ) * mp.sqrt(vY)), 6),
            "kappa": nstr(cHY / p, 6),
            "cov_abs": nstr(cXY / p, 6),
            "ratio": nstr(2 * cZY / cXY, 6),
        })
    checks.append({
        "name": "FINDING 1b CONTROL: sum h = sum|c_k| + 2 sum D_k - n on every sample",
        "pass": idbad == 0,
        "detail": (
            f"Checked against a direct hook computation on all "
            f"{sum(ns for _, ns in plan)} sampled diagrams, {idbad} mismatches. "
            f"This is the growth-chain form of the gap's [+]/[-] split: adding a "
            f"box at (r,s) raises sum h by exactly 1 + r + s."),
    })
    rho_abs = [mpf(r["rho_abs"]) for r in rows]
    rho_h = [mpf(r["rho_h"]) for r in rows]
    spread = max(rho_abs) - min(rho_abs)
    checks.append({
        "name": "FINDING 2 (PREDICTION FALSIFIED): the split terms are NOT single-mode",
        "pass": spread < mpf(1) / 100 and max(rho_abs) < mpf(99) / 100
                and rho_h[-1] > max(rho_abs),
        "detail": (
            f"PREDICTED, from sum c^2 being a single Kerov mode (m = 3): each "
            f"half of the split is single-mode too, so |rho| -> 1 for both and "
            f"the cancellation becomes a ratio of two constants. FALSE. "
            f"rho(sum|c_k|, sum c^2) = {[r['rho_abs'] for r in rows]} -- FLAT, "
            f"total spread {nstr(spread, 3)} over a 16x range in n, and nowhere "
            f"near 1. rho(sum D_k, sum c^2) = {[r['rho_D'] for r in rows]}. Yet "
            f"the combination reaches rho(sum h, sum c^2) = "
            f"{[r['rho_h'] for r in rows]}. So the OFF-MODE parts of sum|c_k| "
            f"and 2 sum D_k cancel each other: sum h is nearly a pure m = 3 "
            f"statistic while neither of its parts is. That is why the "
            f"cancellation does not reduce to two constants -- and a sharper "
            f"account of why sum h is the special combination than "
            f"'it is conjugation-symmetric'."),
    })
    ratios = [mpf(r["ratio"]) for r in rows]
    kappas = [mpf(r["kappa"]) for r in rows]
    drift = abs(ratios[-1] - ratios[0])
    checks.append({
        "name": "FINDING 3: 'ratio > -1' is not live -- kappa is flat while the ratio drifts",
        "pass": max(ratios) < 0 and min(ratios) > -1
                and max(kappas) - min(kappas) < mpf(1) / 100,
        "detail": (
            f"2 Cov(sum D, sum c^2)/Cov(sum|c|, sum c^2) = "
            f"{[r['ratio'] for r in rows]} over n = 100..1600: drifting more "
            f"negative by {nstr(drift, 3)} across a 16x range, so -1 is "
            f"unreachable at that rate. Meanwhile kappa = "
            f"{[r['kappa'] for r in rows]} is flat (spread "
            f"{nstr(max(kappas) - min(kappas), 3)}, against sqrt(2)/24 = "
            f"{nstr(mp.sqrt(2) / 24, 7)}) because Cov(sum|c|, sum c^2) = "
            f"{[r['cov_abs'] for r in rows]} drifts to compensate. A "
            f"cancellation heading for -1 would show as kappa DECAYING; it does "
            f"not. Weakest point: n = 1600 uses only {plan[-1][1]} samples."),
    })

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-kappa-cancellation.witness.json").write_text(
        json.dumps({
        "q0Anchor": "independent",
        "q0AnchorReason": "No substrate pin enters this computation: neither the producer nor its transitive import cone inside computations/ references q_at, q_muon_at, Q_50_DIGIT_STR, q_parameter or resolve_q0_anchor outside comments (AST import-cone walk, 2026-09-03). The probe computes: M_1>0: the +/- cancellation, and why `Sum h` is the special combination.",
            "probe": "m1_kappa_cancellation", "bean": ["qou-t6hc", "qou-k5r5"],
            "identity_partitions": tot, "growth": rows, "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: sum_cells h = sum_cells (i+j+1) -- the growth split collapses to")
    print("RESULT:   one diagram, and is Lean-proved.")
    print("RESULT: PREDICTION FALSIFIED -- the split terms are not single-mode; their")
    print("RESULT:   OFF-MODE parts cancel, which is what makes sum h special.")
    print("RESULT: the 'ratio > -1' worry is not live: kappa is flat while it drifts.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    ok = all(c["pass"] for c in checks)
    print("EXIT: 0" if ok else "EXIT: 1")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
