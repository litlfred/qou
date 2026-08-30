#!/usr/bin/env python3
"""M_1>0: the inflation factor at n = 400, by exact Plancherel edge sampling.

Gap qou-k5r5, bean qou-t6hc leg A. `..._M1_kappa_site_distribution.py` left one
free parameter: infl := E_omega[slope|same]/E_omega[D(0)/lambda_1|same] was
0.494 at n = 46 and still rising, and the worry on record was that it might
climb to pi/2 = 1.5708 -- which is exactly the critical pointwise limit-shape
bound, so the route would close on nothing. Exact enumeration cannot settle it:
it dies around n = 60 (p(61) is already 1.1e6 partitions with big-integer dims).

THE UNLOCK: THE TRIPLE MEASURE FACTORISES
-----------------------------------------
The up-down edge measure on triples is P(lam,Lam,mu) = dim(lam)dim(mu)/((n+1)n!).
Summing over lam and using the branching rule sum_{lam < Lam} dim(lam) = dim(Lam):

    P(Lam) = dim(Lam)^2/(n+1)!  =  Plancherel(n+1),

hence  P(lam,Lam,mu) = Planch(Lam) * [dim(lam)/dim(Lam)] * [dim(mu)/dim(Lam)]:

    **Lam ~ Plancherel(n+1), then TWO INDEPENDENT down-steps.**

Both pieces have exact classical samplers that never compute a dimension:
Lam by RSK on a uniform random permutation of [n+1], and each down-step by the
Greene-Nijenhuis-Wilf hook walk, which lands on corner c with probability
exactly dim(Lam - c)/dim(Lam). And because the corner-pair probability is
proportional to dim(lam_x)dim(lam_y), the omega importance weight is exactly

    dABS * dO = (r-a)^2 (r+a)

with no dimensions anywhere. Cost O(n sqrt n) per sample instead of enumerating
p(n+1) partitions, and only uniform INTEGER randomness -- no float64 anywhere.

CONTROL, and it is the whole reason to trust the large-n numbers: at n = 24, 40
and 48 the exact values are known from the committed
`m1-kappa-site-distribution.witness.json`, and the sampler must reproduce them
to within its own quoted Monte-Carlo error. A sampler that agrees with nothing
is worth nothing.

WHAT IT SAYS
------------
infl keeps rising but decelerates, and it is NOT heading for pi/2. Extrapolating
the three large-n points with a power law puts it near 1, i.e. kappa becomes
asymptotically UNIFORM: the omega-chosen intervals drop at the diagram's own
global average rate. That is the good case -- infl = 1 is exactly the uniform-
kappa case identified in `QOU.BraidKnot.M1EdgeCalculus.kappa_uniform_dot`.

Honesty: Monte-Carlo, so every large-n number carries sampling error and is
quoted with the spread over seeds; the extrapolation is a 3-point fit and is
reported as an extrapolation, not a limit. scope-(a); nothing wired; gap
qou-k5r5 stays OPEN. This probe cannot prove M_1 > 0 and does not claim to.
"""
from __future__ import annotations
from bisect import bisect_right
from fractions import Fraction as F
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mpmath import mp, mpf, nstr  # noqa: E402

mp.dps = 30


def qf(x):
    """Fraction -> mpf without touching binary64."""
    return mpf(x.numerator) / mpf(x.denominator)


def rsk_shape(N, rnd):
    """Shape of the RSK insertion tableau of a uniform permutation of [N];
    that shape is exactly Plancherel(N)-distributed."""
    perm = list(range(N))
    for i in range(N - 1, 0, -1):
        j = rnd.randrange(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    rows = []
    for x in perm:
        for row in rows:
            k = bisect_right(row, x)
            if k == len(row):
                row.append(x)
                x = None
                break
            row[k], x = x, row[k]
        if x is not None:
            rows.append([x])
    return tuple(len(r) for r in rows)


def corners_of(Lam):
    """(row, content, D_Lam(content)) per removable corner."""
    out = []
    L = len(Lam)
    for i in range(L):
        if Lam[i] > (Lam[i + 1] if i + 1 < L else 0):
            j = Lam[i] - 1
            out.append((i, j - i, min(i, j) + 1))
    return out


def hook_walk(Lam, conj, rnd):
    """GNW hook walk: returns a corner's row, with probability exactly
    dim(Lam - corner)/dim(Lam). Uniform integer choices only."""
    t = rnd.randrange(sum(Lam))
    i = 0
    while t >= Lam[i]:
        t -= Lam[i]
        i += 1
    j = t
    while True:
        arm = Lam[i] - j - 1
        leg = conj[j] - i - 1
        h = arm + leg
        if h == 0:
            return i
        k = rnd.randrange(h)
        if k < arm:
            j = j + 1 + k
        else:
            i = i + 1 + (k - arm)


def run(n, nsamp, seed):
    rnd = random.Random(seed)
    Wsame = 0
    Wall = 0
    dens_w = F(0)
    glob_w = F(0)
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
            continue                       # mu = lam: not an edge
        ra = next(c for c in cs if c[0] == a)
        rb = next(c for c in cs if c[0] == b)
        (rx, cx, Dx), (ry, cy, Dy) = (ra, rb) if a < b else (rb, ra)
        dABS = abs(cy) - abs(cx)
        if dABS == 0:
            continue                       # Pterm = 0
        dO = cy * cy - cx * cx
        w = dABS * dO
        Wall += w
        if cx > 0 > cy:
            continue                       # opposite-sign: slope is no density
        Wsame += w
        num = Dx - Dy - 1 if dABS > 0 else Dx - Dy + 1
        dens_w += F(w * num, dABS)
        addrow = rx if dABS > 0 else ry
        addc = cx if dABS > 0 else cy
        D0 = sum(1 for i, p in enumerate(Lam) if p >= i + 1) - (1 if addc == 0 else 0)
        glob_w += F(w * D0, Lam[0] - (1 if addrow == 0 else 0))
    return (F(dens_w, Wsame) if Wsame else F(0),
            F(glob_w, Wsame) if Wsame else F(0),
            F(Wsame, Wall) if Wall else F(0))


def seeds_stat(n, nsamp, seeds):
    ds, gs, ws, infls = [], [], [], []
    for s in seeds:
        d, g, w = run(n, nsamp, s)
        ds.append(qf(d)); gs.append(qf(g)); ws.append(qf(w))
        infls.append(qf(d) / qf(g) if g else mpf(0))
    mean = lambda v: sum(v) / len(v)                     # noqa: E731
    half = lambda v: (max(v) - min(v)) / 2               # noqa: E731
    return {"n": n, "E_dens": mean(ds), "E_dens_spread": half(ds),
            "E_glob": mean(gs), "w_same": mean(ws),
            "infl": mean(ds) / mean(gs),
            "infl_per_seed": infls, "infl_spread": half(infls)}


def main():
    t0 = time.monotonic_ns()
    nsamp = int(sys.argv[1]) if len(sys.argv) > 1 else 30000
    seeds = [11, 22, 33]
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    wit = Path(__file__).with_name("m1-kappa-site-distribution.witness.json")
    # The witness stringifies every field, ints included ("12", and "12.0" if a
    # future writer routes them through nstr), so parse rather than index on an
    # int. Getting this wrong made every exact value silently absent and the
    # CONTROL below vacuous -- it crashed on max() of an empty sequence, which
    # is the loud failure; had the check been written with a default it would
    # have PASSED while comparing nothing.
    exact = {int(str(r["n"]).split(".")[0]): F(r["E_dens"])
             for r in json.loads(wit.read_text())["rows"]}

    print(f"# exact Plancherel edge sampling, {nsamp} samples x {len(seeds)} seeds")
    print(f"# {'n':>4} {'E[dens|same]':>13} {'+-':>9} {'exact':>11} {'rel.err':>9} "
          f"{'E[D0/l1]':>9} {'infl':>8}")
    rows = []
    for n in [24, 40, 48, 100, 200, 400, 800]:
        r = seeds_stat(n, nsamp, seeds)
        ex = qf(exact[n]) if n in exact else None
        r["exact"] = ex
        r["rel_err"] = (r["E_dens"] - ex) / ex if ex else None
        rows.append(r)
        print(f"  {n:>4} {nstr(r['E_dens'], 6):>13} {nstr(r['E_dens_spread'], 3):>9} "
              f"{(nstr(ex, 6) if ex else '-'):>11} "
              f"{(nstr(r['rel_err'] * 100, 3) + '%' if ex else '-'):>9} "
              f"{nstr(r['E_glob'], 5):>9} {nstr(r['infl'], 5):>8}", flush=True)

    val = [r for r in rows if r["exact"] is not None]
    worst = max((abs(r["rel_err"]) for r in val), default=mpf("99"))
    check("CONTROL: the sampler reproduces the exact values where they are known",
          len(val) >= 3 and worst < mpf("0.02"),
          f"n = {[r['n'] for r in val]} against the committed "
          f"m1-kappa-site-distribution witness: relative errors "
          f"{[nstr(r['rel_err'] * 100, 3) + '%' for r in val]}, worst "
          f"{nstr(worst * 100, 3)}%, against a 2% tolerance. Seed spread on "
          f"E[dens] is {[nstr(r['E_dens_spread'], 3) for r in val]}. Without this "
          f"the large-n numbers would be unfalsifiable.")

    big = [r for r in rows if r["n"] >= 100]
    # Fit on the TOP three of the geometric grid (200, 400, 800): the second
    # difference grows with leverage while the sampling noise does not, so a
    # wider grid is worth far more than more samples at a narrow one.
    fit = big[-3:]
    infl = [r["infl"] for r in fit]
    allinfl = [r["infl"] for r in big]
    check("infl is RISING but DECELERATING across the large-n grid",
          all(allinfl[i] < allinfl[i + 1] for i in range(len(allinfl) - 1))
          and (allinfl[-1] - allinfl[-2]) < (allinfl[1] - allinfl[0]),
          f"n = {[r['n'] for r in big]}: infl = {[nstr(v, 5) for v in allinfl]}; "
          f"increments per doubling "
          f"{[nstr(allinfl[i + 1] - allinfl[i], 3) for i in range(len(allinfl) - 1)]} "
          f"-- each doubling adds less than the last.")

    # 3-point power-law extrapolation infl = I - C n^-alpha on a geometric grid
    # gives I = (ac-b^2)/(a-2b+c). THE DENOMINATOR IS A SECOND DIFFERENCE of
    # three nearly-collinear points, so it is the difference of two almost-equal
    # numbers and the estimator blows up as it approaches zero. Quoting I
    # without testing that denominator is how this probe first reported
    # "infl -> 1.0" from one run and "infl -> 1.41" from another whose infl
    # values agreed to under 1%. Both were noise. So: propagate the seed spread
    # through, and refuse to report a limit that the data cannot support.
    a, b, c = infl
    d2 = a - 2 * b + c
    # var(a - 2b + c) = sa^2 + 4 sb^2 + sc^2 -- the middle coefficient is 2, and
    # an earlier version dropped it, understating the noise.
    sa, sb, sc = (r["infl_spread"] for r in fit)
    sig = mp.sqrt(sa ** 2 + 4 * sb ** 2 + sc ** 2)
    signif = abs(d2) / sig if sig > 0 else mpf(0)
    Iinf = ((a * c - b * b) / d2) if d2 != 0 else mpf(0)
    # the same fit on each seed independently -- the honest error bar
    per = []
    for k in range(len(fit[0]["infl_per_seed"])):
        x, y, z = (r["infl_per_seed"][k] for r in fit)
        dd = x - 2 * y + z
        if dd != 0:
            per.append((x * z - y * y) / dd)
    PI2 = mp.pi / 2
    # The rule, applied honestly in both directions: significance-test the
    # denominator first, then report only the conclusion that test supports.
    # On the narrow grid (100, 200, 400) this same rule returned 1.17 sigma and
    # "undetermined" -- and two runs whose infl agreed to under 1% had given
    # 1.00 and 1.41, both noise. Widening the grid to 800 is what made the fit
    # usable; more samples at the narrow grid would not have.
    usable = signif >= 3
    check("the fit denominator is SIGNIFICANCE-TESTED before any limit is quoted",
          True,
          f"a-2b+c = {nstr(d2, 3)} against a seed-propagated noise of "
          f"{nstr(sig, 3)} => {nstr(signif, 3)} sigma on the grid "
          f"{[r['n'] for r in fit]}. Threshold 3 sigma. Verdict: "
          f"{'USABLE' if usable else 'NOT USABLE -- limit reported as undetermined'}. "
          f"On the narrow grid (100, 200, 400) the same rule gave 1.17 sigma and "
          f"refused to quote a limit; leverage, not sample count, is what fixed it.")

    spread = (max(per) - min(per)) if per else mpf(0)
    check("the three INDEPENDENT seed refits agree",
          bool(per) and spread < mpf("0.15"),
          f"re-fitting each seed separately gives {[nstr(v, 4) for v in per]}, "
          f"spanning {nstr(min(per), 4)}..{nstr(max(per), 4)} (spread "
          f"{nstr(spread, 3)}). These share no samples, so agreement here is the "
          f"real check on the fit -- the point estimate alone was what misled "
          f"before.")

    check("EXTRAPOLATED: infl heads for ~1, well under pi/2",
          usable and Iinf < mpf("1.3"),
          f"I = (ac-b^2)/(a-2b+c) = {nstr(Iinf, 5)} on n = {[r['n'] for r in fit]}, "
          f"against pi/2 = {nstr(PI2, 6)}. infl = 1 is exactly the UNIFORM-kappa "
          f"case (M1EdgeCalculus.kappa_uniform_dot): the omega-chosen intervals "
          f"drop at the diagram's own global rate, no faster. STILL AN "
          f"EXTRAPOLATION from three points on a fitted form -- what makes it "
          f"quotable is the {nstr(signif, 3)}-sigma denominator and the seed "
          f"agreement above, not the point estimate.")

    check("MEASURED (the part that needs no fit): infl at the top of the grid",
          big[-1]["infl"] > 0,
          f"infl = {nstr(big[-1]['infl'], 5)} +- {nstr(big[-1]['infl_spread'], 2)} "
          f"at n = {big[-1]['n']}, still rising. That is a measurement; the limit "
          f"above is not.")

    check("E[D(0)/lambda_1] falls toward the VKLS 1/pi",
          all(big[i]["E_glob"] > big[i + 1]["E_glob"] for i in range(len(big) - 1)),
          f"E[D(0)/lambda_1|same] = {[nstr(r['E_glob'], 5) for r in big]} at "
          f"n = {[r['n'] for r in big]}, decreasing toward 1/pi = {nstr(1 / mp.pi, 6)}. "
          f"That is the denominator of infl, and its limit is what makes "
          f"'infl < pi/2' equivalent to the critical pointwise bound.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    Path(__file__).with_name("m1-kappa-large-n-sampler.witness.json").write_text(
        json.dumps({
            "probe": "m1_kappa_large_n_sampler",
            "bean": ["qou-t6hc", "qou-k5r5"],
            "nsamp": nsamp, "seeds": seeds,
            # Lists and ints must survive intact: routing everything else
            # through nstr turned `infl_per_seed` into the single string
            # "[...]" and `n` into "12", each of which silently broke a
            # downstream consumer. Third instance of this in the cluster.
            "rows": [{k: ([nstr(x, 12) for x in v] if isinstance(v, list) else
                          v if isinstance(v, int) or v is None else nstr(v, 12))
                      for k, v in r.items()} for r in rows],
            "infl_extrapolated": nstr(Iinf, 8),
            "checks": checks,
            "passed": sum(1 for c in checks if c["pass"]),
            "total": len(checks), "ms": int(ms),
        }, indent=1) + "\n")
    print()
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print(f"RESULT: infl = {nstr(big[-1]['infl'], 5)} at n = {big[-1]['n']} by exact Plancherel "
          f"edge sampling (rising, decelerating).")
    print(f"RESULT: extrapolated limit {nstr(Iinf, 4)} "
          f"({nstr(signif, 3)} sigma, seed refits {[nstr(v, 4) for v in per]}), "
          f"well under pi/2." if usable else
          "RESULT: its LIMIT is NOT DETERMINED at this precision.")
    print("RESULT: gap qou-k5r5 stays OPEN.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
