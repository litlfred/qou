#!/usr/bin/env python3
"""M_1>0: does the telescoping route's BUDGET close? Synthesis, no sampling.

Gap qou-k5r5, bean qou-t6hc leg A. This probe computes nothing itself. It reads
the two committed witnesses and does the arithmetic that decides the route:

  * `m1-kappa-large-n-sampler.witness.json`  -- infl (extrapolated), w_same
  * `m1-opp-sign-large-n.witness.json`       -- S_opp, B_opp

`N/P = S_same + S_opp + Q`, with `Q ~ 2.07/sqrt(n) -> 0`.

TWO SEPARATE QUESTIONS, and conflating them is the trap
-------------------------------------------------------
(1) DOES THE ACCOUNTING CLOSE? Asymptotically
        S_same -> 2 * w_same * infl * (1/pi)
    since E_omega[D(0)/lambda_1] -> 1/pi by VKLS. Adding the separately measured
    S_opp should reproduce the independently proved N/P -> 0.6605. It does, to
    well under a percent. That is a genuine cross-check: the two halves come
    from different measurements and the target from the Ivanov-Olshanski field,
    so agreement is evidence that the decomposition is right and nothing is
    double-counted or dropped.

(2) DO THE BOUNDS CLOSE IT? Entirely different question. The only DETERMINISTIC
    bound in hand for the opposite-sign half is the Lean one,
    `|slope| <= D(0)/g` (QOU.BraidKnot.M1EdgeCalculus.abs_diagLen_sub_transpose_le),
    whose omega-average is B_opp. Granting the same-sign half its MEASURED value
    for free -- which is not a bound, and is generous -- the total still lands
    ABOVE 1. So the route does not close on what is proved.

WHY THIS IS NOT A NEAR MISS
---------------------------
It is tempting to read "over by ~1%" as almost there. It is not, for one
measured reason: B_opp is still RISING with n across the whole grid. A gap that
would be closed by a slightly better constant is different from a gap whose
leading term is still growing, and this is the second kind. What the
opposite-sign half needs is an averaging argument of its own, not a tighter
constant in the same per-edge bound.

Honesty: pure arithmetic over committed witnesses; every input carries the error
quoted in its own witness and none of it is re-derived here. scope-(a); no fit;
nothing wired; gap qou-k5r5 stays OPEN.
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mpmath import mp, mpf, nstr, pi  # noqa: E402

mp.dps = 30

NP_LIMIT = mpf("0.6605")   # proved, modulo the cited Ivanov-Olshanski CLT


def main():
    t0 = time.monotonic_ns()
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    here = Path(__file__).parent
    samp = json.loads((here / "m1-kappa-large-n-sampler.witness.json").read_text())
    opp = json.loads((here / "m1-opp-sign-large-n.witness.json").read_text())

    infl = mpf(samp["infl_extrapolated"])
    srow = max(samp["rows"], key=lambda r: r["n"])
    orow = max(opp["rows"], key=lambda r: r["n"])
    nmax = srow["n"]
    w_same = mpf(srow["w_same"])
    S_opp = mpf(orow["S_opp"])
    B_opp = mpf(orow["B_opp"])
    Bs = [mpf(r["B_opp"]) for r in sorted(opp["rows"], key=lambda r: r["n"])]

    S_same = 2 * w_same * infl / pi
    total = S_same + S_opp

    print(f"# route budget, from the committed witnesses (n up to {nmax})")
    print(f"  infl (extrapolated)      = {nstr(infl, 6)}")
    print(f"  w_same                   = {nstr(w_same, 5)}")
    print(f"  S_same = 2 w_same infl/pi= {nstr(S_same, 6)}")
    print(f"  S_opp  (measured)        = {nstr(S_opp, 6)}   [still rising]")
    print(f"  Q                        -> 0")
    print(f"  sum                      = {nstr(total, 6)}   vs proved "
          f"N/P -> {nstr(NP_LIMIT, 5)}")
    print()
    print(f"  B_opp (the Lean bound)   = {nstr(B_opp, 5)}")
    print(f"  S_same + B_opp           = {nstr(S_same + B_opp, 6)}   vs 1")
    print()

    # (1) accounting. S_opp is still rising at the top of the grid, so the sum is
    # a LOWER bound on the limit; the check is that it does not OVERSHOOT and is
    # already close.
    rel = (NP_LIMIT - total) / NP_LIMIT
    check("ACCOUNTING: the two halves reproduce the proved limit N/P -> 0.6605",
          -mpf("0.02") < rel < mpf("0.12"),
          f"S_same {nstr(S_same, 5)} + S_opp {nstr(S_opp, 5)} = {nstr(total, 6)} "
          f"against {nstr(NP_LIMIT, 5)}, short by {nstr(rel * 100, 3)}%. S_opp is "
          f"still RISING at n = {orow['n']}, so the sum is a lower bound on the "
          f"limit and should sit slightly under -- overshooting would be the "
          f"failure. The two halves and the target come from three different "
          f"routes, so this is a real cross-check on the decomposition.")

    # (2) the bounds -- WITH THE UNCERTAINTY CARRIED THROUGH.
    #
    # An earlier version of this check reported "over 1 by 0.00076" and asked for
    # B_opp to fall by "0.114%". Both are overprecision: infl is an extrapolation
    # whose three independent seed refits span 1.012..1.050, which alone moves
    # S_same by about +-0.006 -- eight times the gap being quoted. A verdict the
    # precision cannot support is worse than no verdict, so this now propagates
    # the seed spreads and refuses to call it either way when they overlap 1.
    #
    # infl's per-seed refits are recomputed here from the sampler witness's
    # per-seed infl values, on the same top-three geometric grid it fitted.
    def seed_list(row):
        """`infl_per_seed` is a real list in witnesses written after the
        serialiser fix, and the single string "['a', 'b', 'c']" in ones written
        before it. Accept both rather than force a regeneration."""
        v = row["infl_per_seed"]
        if isinstance(v, list):
            return [mpf(x) for x in v]
        return [mpf(t.strip().strip("'\"")) for t in v.strip("[]").split(",")]

    fit = sorted(samp["rows"], key=lambda r: r["n"])[-3:]
    per_infl = []
    for k in range(len(seed_list(fit[0]))):
        x, y, z = (seed_list(r)[k] for r in fit)
        dd = x - 2 * y + z
        if dd != 0:
            per_infl.append((x * z - y * y) / dd)
    S_same_lo = 2 * w_same * min(per_infl) / pi
    S_same_hi = 2 * w_same * max(per_infl) / pi
    Bsp = mpf(orow.get("B_opp_spread", "0"))
    lo = S_same_lo + B_opp - Bsp
    hi = S_same_hi + B_opp + Bsp
    straddles = lo <= 1 <= hi

    check("BOUNDS: at this precision the total is INDISTINGUISHABLE from 1",
          straddles,
          f"granting S_same its measured value for free -- which is NOT a bound, "
          f"and is generous -- and adding the only deterministic opposite-sign "
          f"bound B_opp = {nstr(B_opp, 5)} +- {nstr(Bsp, 2)}, the total is "
          f"{nstr(S_same + B_opp, 6)} with a range of "
          f"[{nstr(lo, 6)}, {nstr(hi, 6)}] once infl's seed refits "
          f"({[nstr(v, 4) for v in per_infl]}) and B_opp's seed spread are carried "
          f"through. That range STRADDLES 1. So the honest verdict is not 'closes' "
          f"and not 'misses' -- the bounds land exactly on the boundary and the "
          f"precision in hand cannot separate them.")

    check("...and the tie-breaker is against us: B_opp is still RISING",
          Bs[-1] > Bs[0],
          f"B_opp across the grid = {[nstr(v, 4) for v in Bs]} at n = "
          f"{[r['n'] for r in sorted(opp['rows'], key=lambda r: r['n'])]}. Landing "
          f"on the boundary with the leading term still growing is not a near "
          f"miss that a better constant fixes -- extrapolating the rise puts the "
          f"total above 1. The opposite-sign half needs an averaging argument of "
          f"its own; the same-sign half got one from the telescoping density "
          f"reading, and that reading provably does not apply here.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    (here / "m1-route-budget.witness.json").write_text(json.dumps({
        "probe": "m1_route_budget",
        "bean": ["qou-t6hc", "qou-k5r5"],
        "inputs": {"infl": nstr(infl, 10), "w_same": nstr(w_same, 10),
                   "S_opp": nstr(S_opp, 10), "B_opp": nstr(B_opp, 10),
                   "n_sampler": nmax, "n_opp": orow["n"]},
        "S_same": nstr(S_same, 10), "sum": nstr(total, 10),
        "bound_total": nstr(S_same + B_opp, 10),
        "checks": checks, "passed": sum(1 for c in checks if c["pass"]),
        "total": len(checks), "ms": int(ms),
    }, indent=1) + "\n")
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print(f"RESULT: accounting closes ({nstr(total, 5)} vs {nstr(NP_LIMIT, 5)}); "
          f"the BOUNDS land on the boundary ({nstr(S_same + B_opp, 5)}, range "
          f"[{nstr(lo, 5)}, {nstr(hi, 5)}] vs 1) -- undecided at this precision.")
    print("RESULT: gap qou-k5r5 stays OPEN -- the opposite-sign half needs its own "
          "averaging argument.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
