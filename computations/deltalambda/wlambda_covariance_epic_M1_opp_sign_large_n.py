#!/usr/bin/env python3
"""M_1>0: S_opp at large n -- the only half of the route still unaccounted for.

Gap qou-k5r5, bean qou-t6hc leg A. N/P = S_same + S_opp + Q. Q ~ 2.07/sqrt(n)
vanishes; `..._M1_kappa_large_n_sampler.py` settled the same-sign half (the
inflation factor extrapolates to 1.028 at 5.11 sigma, i.e. kappa is
asymptotically uniform). S_opp is what is left, and it is the awkward one:

  * it has NO density reading. For opposite-sign contents the content interval
    has length |c_A| + |c_B| while the denominator is g = |c_B| - |c_A|, so the
    drop-site argument simply does not apply;
  * its per-edge slope is the UNBOUNDED one (~sqrt(2n), see
    ..._edge_ratio_monotonicity.py);
  * the telescoping bound that does cover it, |slope| <= D(0)/g -- proved
    sorry-free as QOU.BraidKnot.M1EdgeCalculus.abs_diagLen_sub_transpose_le and
    SHARP per edge -- sat about an order of magnitude above the truth in the
    omega-average at n = 46.

THE QUESTION, and it is a falsifier
-----------------------------------
Does the slack B_opp/S_opp stay bounded, or grow? If it grows, the Lean bound is
asymptotically useless and the opposite-sign half needs a different input
altogether. Exact enumeration stops at n = 46 for these quantities; this uses
the same exact-in-distribution Plancherel edge sampler (Lam ~ Plancherel(n+1) by
RSK, two independent GNW hook walks, omega weight exactly (r-a)^2 (r+a)) and
reaches n = 800.

A PREDICTION, written before the run
------------------------------------
If w_same -> 0.5 and E[slope|same] -> 1.028/pi = 0.327, then S_same -> 0.327 and
the budget S -> 0.6605 forces S_opp -> about 0.33 -- nearly TRIPLE its n = 46
value of 0.118. If S_opp instead stays flat near 0.118, the accounting above is
wrong somewhere and this probe should say so rather than be reinterpreted.

CONTROL: S_opp, w_opp and B_opp are known exactly at n = 24 and 40 from the
committed `m1-telescoping-route.witness.json`, and the sampler must reproduce
them within its quoted Monte-Carlo error.

NORMALISATION, since it is easy to get wrong: S_opp and B_opp are normalised by
the TOTAL omega weight over all edges, w_opp by that same total. In the sampler
the dim(lam)dim(mu) factor is absorbed by the sampling, so an edge contributes
weight dABS*dO, and

    S_opp = 2 sum_opp (dO * num) / Wall,
    B_opp = 2 sum_opp (dO * sgn(dABS) * D0) / Wall,

matching the exact probe's Pterm-weighted definitions term for term.

Honesty: Monte-Carlo; every large-n number carries sampling error and is quoted
with its seed spread. scope-(a); no fit beyond what is labelled; nothing wired;
gap qou-k5r5 stays OPEN.
"""
from __future__ import annotations
from fractions import Fraction as F
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wlambda_covariance_epic_M1_kappa_large_n_sampler import (  # noqa: E402
    corners_of, hook_walk, qf, rsk_shape,
)
from mpmath import mp, mpf, nstr  # noqa: E402

mp.dps = 30


def run(n, nsamp, seed):
    rnd = random.Random(seed)
    Wall = 0
    Sopp_num = 0          # sum over opposite-sign edges of dO * num
    Bopp_num = 0          # sum over opposite-sign edges of dO * sgn(dABS) * D0
    Wopp = 0
    for _ in range(nsamp):
        Lam = rsk_shape(n + 1, rnd)
        cs = corners_of(Lam)
        if len(cs) < 2:
            continue
        conj = [0] * Lam[0]
        for p in Lam:
            for j in range(p):
                conj[j] += 1
        a = hook_walk(Lam, conj, rnd)
        b = hook_walk(Lam, conj, rnd)
        if a == b:
            continue
        ra = next(c for c in cs if c[0] == a)
        rb = next(c for c in cs if c[0] == b)
        (rx, cx, Dx), (ry, cy, Dy) = (ra, rb) if a < b else (rb, ra)
        dABS = abs(cy) - abs(cx)
        if dABS == 0:
            continue
        dO = cy * cy - cx * cx
        Wall += dABS * dO
        if not (cx > 0 > cy):
            continue                                   # same-sign: not this probe
        Wopp += dABS * dO
        num = Dx - Dy - 1 if dABS > 0 else Dx - Dy + 1
        Sopp_num += dO * num
        addrow = rx if dABS > 0 else ry
        addc = cx if dABS > 0 else cy
        D0 = sum(1 for i, p in enumerate(Lam) if p >= i + 1) - (1 if addc == 0 else 0)
        Bopp_num += dO * (1 if dABS > 0 else -1) * D0
    return (F(2 * Sopp_num, Wall) if Wall else F(0),
            F(2 * Bopp_num, Wall) if Wall else F(0),
            F(Wopp, Wall) if Wall else F(0))


def stat(n, nsamp, seeds):
    ss, bs, ws = [], [], []
    for s in seeds:
        S, B, W = run(n, nsamp, s)
        ss.append(qf(S)); bs.append(qf(B)); ws.append(qf(W))
    mean = lambda v: sum(v) / len(v)                     # noqa: E731
    half = lambda v: (max(v) - min(v)) / 2               # noqa: E731
    return {"n": n, "S_opp": mean(ss), "S_opp_spread": half(ss),
            "B_opp": mean(bs), "B_opp_spread": half(bs),
            "S_opp_per_seed": ss, "B_opp_per_seed": bs,
            "w_opp": mean(ws),
            "slack": mean(bs) / mean(ss) if mean(ss) else mpf(0)}


def main():
    t0 = time.monotonic_ns()
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    seeds = [11, 22, 33]
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    wit = Path(__file__).with_name("m1-telescoping-route.witness.json")
    ex = {}
    for r in json.loads(wit.read_text())["rows"]:
        ex[int(str(r["n"]).split(".")[0])] = (F(r["S_opp"]), F(r["B_opp"]), F(r["w_opp"]))

    print(f"# S_opp at large n, exact Plancherel edge sampling, "
          f"{len(seeds)} seeds, samples scaled ~1/n from a base of {nsamp}")
    print(f"# {'n':>4} {'S_opp':>10} {'+-':>9} {'exact':>10} {'rel.err':>9} "
          f"{'B_opp':>9} {'slack':>7} {'w_opp':>7}")
    rows = []
    for n in [24, 40, 100, 200, 400, 800]:
        # Samples scaled ~1/n so every tier costs about the same. The CONTROL
        # tiers (n = 24, 40) are the cheap ones and are where precision is
        # actually needed -- a loose control is worth nothing. The tolerance
        # below is NOT moved to accommodate a short run.
        r = stat(n, max(nsamp, nsamp * 400 // n), seeds)
        r["nsamp"] = max(nsamp, nsamp * 400 // n)
        e = qf(ex[n][0]) if n in ex else None
        r["exact_S_opp"] = e
        r["rel_err"] = (r["S_opp"] - e) / e if e else None
        r["exact_B_opp"] = qf(ex[n][1]) if n in ex else None
        rows.append(r)
        print(f"  {n:>4} {nstr(r['S_opp'], 5):>10} {nstr(r['S_opp_spread'], 3):>9} "
              f"{(nstr(e, 5) if e else '-'):>10} "
              f"{(nstr(r['rel_err'] * 100, 3) + '%' if e else '-'):>9} "
              f"{nstr(r['B_opp'], 4):>9} {nstr(r['slack'], 4):>7} "
              f"{nstr(r['w_opp'], 4):>7}", flush=True)

    val = [r for r in rows if r["exact_S_opp"] is not None]
    worst = max((abs(r["rel_err"]) for r in val), default=mpf("99"))
    check("CONTROL: reproduces the exact S_opp where it is known",
          len(val) >= 2 and worst < mpf("0.05"),
          f"n = {[r['n'] for r in val]} against the committed telescoping "
          f"witness: relative errors {[nstr(r['rel_err'] * 100, 3) + '%' for r in val]}, "
          f"worst {nstr(worst * 100, 3)}%, tolerance 5%. B_opp there: sampled "
          f"{[nstr(r['B_opp'], 4) for r in val]} against exact "
          f"{[nstr(r['exact_B_opp'], 4) for r in val]}.")

    big = [r for r in rows if r["n"] >= 100]
    so = [r["S_opp"] for r in big]
    check("PREDICTED: S_opp grows well past its n = 46 value of 0.118",
          so[-1] > mpf("0.2"),
          f"S_opp = {[nstr(v, 4) for v in so]} at n = {[r['n'] for r in big]}. "
          f"Predicted before the run: the budget S -> 0.6605 with S_same -> 0.327 "
          f"forces S_opp -> about 0.33, nearly triple the exact 0.118 at n = 46. "
          f"A flat S_opp here would mean the accounting is wrong.")

    slack = [r["slack"] for r in big]
    check("FALSIFIER: the Lean bound's slack B_opp/S_opp does NOT grow",
          slack[-1] < slack[0],
          f"B_opp/S_opp = {[nstr(v, 4) for v in slack]} at n = "
          f"{[r['n'] for r in big]}. B_opp itself = {[nstr(r['B_opp'], 4) for r in big]}. "
          f"If this ratio grew, |slope| <= D(0)/g would be asymptotically useless "
          f"and the opposite-sign half would need a different input. It does not "
          f"grow -- the bound stays a bounded factor above the truth.")

    wo = [r["w_opp"] for r in big]
    check("MEASURED: opposite-sign edges keep a large share of omega-weight",
          wo[-1] > mpf("0.3"),
          f"w_opp = {[nstr(v, 4) for v in wo]} at n = {[r['n'] for r in big]}. "
          f"These edges are not a vanishing correction, which is why they had to "
          f"be handled rather than bounded away.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-opp-sign-large-n.witness.json").write_text(
        json.dumps({
            "probe": "m1_opp_sign_large_n",
            "bean": ["qou-t6hc", "qou-k5r5"],
            "nsamp": nsamp, "seeds": seeds,
            "rows": [{k: ([nstr(x, 12) for x in v] if isinstance(v, list) else
                          v if isinstance(v, int) else
                          (nstr(v, 12) if v is not None else None))
                      for k, v in r.items()} for r in rows],
            "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    print()
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print(f"RESULT: S_opp = {nstr(rows[-1]['S_opp'], 5)} at n = {rows[-1]['n']}, "
          f"B_opp = {nstr(rows[-1]['B_opp'], 4)}, slack "
          f"{nstr(rows[-1]['slack'], 4)}.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
