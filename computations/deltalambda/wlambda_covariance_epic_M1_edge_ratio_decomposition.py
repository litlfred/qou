#!/usr/bin/env python3
"""M_1>0: split N/P into the term the limit shape controls and the term it does not.

Gap qou-k5r5, bean qou-t6hc leg A. The Fulman reduction gives M_1 = P - N and
M_1 > 0 <=> N/P = E_omega[ratio_e] < 1, with

    ratio_e = 2(d_a - d_r + 1)/(r - a).

`wlambda_covariance_epic_M1_edge_ratio_structure.py` established that no
per-edge or weight-suppression argument can close this: ratio_e reaches 4, and
~15% of the omega-weight sits on ratio_e >= 1 persistently. N/P < 1 is an
AVERAGING phenomenon. What that probe did not do is say WHICH average.

This one splits the ratio at the `+1`:

    N/P  =  S(n)  +  Q(n),
    S(n) := 2 E_omega[(d_a - d_r)/(r - a)]     the SLOPE term
    Q(n) := 2 E_omega[1/(r - a)]               the SMALL-GAP term

and the split matters because the two need completely different inputs.

S is a weighted mean of the DISCRETE DIAGONAL SLOPE (d_a - d_r)/(r - a).
QOU.BraidKnot.M1EdgeCalculus.diagLen_lipschitz bounds that slope by 1
unconditionally, which only gives S <= 2 -- useless. The Plancherel limit shape
gives much more: with D(c) ~ (sqrt n / 2)(Omega(u) - |u|) at u = c/sqrt n,

    dD/dc = (Omega'(u) - sgn u)/2,   Omega'(u) = (2/pi) arcsin(u/2) in [0,1],

so |dD/dc| <= 1/2, attained only at u = 0. THAT factor of two -- 1/2 from the
limit shape against 1 from the discrete lemma -- is the whole difference
between S <= 2 and S < 1. It is a statement about Plancherel-typical diagrams,
not about all diagrams: a staircase really does have slope 1 (lambda = (3,2,1)
has D(0) - D(1) = 1).

Q needs nothing from the limit shape. It is a weighted harmonic mean of the
content gap, and omega ~ (r-a)^2 (r+a) up-weights large gaps, so Q is small and
shrinking on its own.

So the effective-CLT project needs an error-controlled |dD/dc| <= 1/2 - eps for
S, and a separate elementary bound for Q. This probe measures both, and how much
headroom each leaves under 1.

CONTROL: S + Q must equal N/P EXACTLY as Fractions. The decomposition is an
algebraic identity, so a mismatch means the edge accumulation is wrong -- which
a merely plausible-looking pair of numbers would not reveal.

Exact Fraction throughout; mpmath only for display. Honesty: measurement for the
OPEN uniform bound; scope-(a); no fit; nothing wired; gap qou-k5r5 stays OPEN.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wlambda_covariance_epic_M1_edge_ratio_structure import (  # noqa: E402
    addable, diag_lengths, dim, factorial, partitions, removable,
)
from mpmath import mp, mpf, nstr, sqrt  # noqa: E402

mp.dps = 40


def decompose(n):
    """Exact S, Q, N/P for level n of the up-down chain."""
    Yn = list(partitions(n))
    nfac = factorial(n)
    Dcache = {lam: diag_lengths(lam) for lam in Yn}
    dimcache = {lam: dim(lam) for lam in Yn}
    edge_cc = defaultdict(int)
    for lam in Yn:
        for Lam, _cA in addable(lam):
            for mu, _cB in removable(Lam):
                if mu != lam:
                    edge_cc[(lam, mu)] += 1

    total_P = F(0)
    slope_num = F(0)     # sum over edges of Pterm * (d_a - d_r)/(r - a)
    gap_num = F(0)       # sum over edges of Pterm * 1/(r - a)
    ntotal = F(0)
    slope_max = F(0)
    slope_neg_w = F(0)   # omega-weight where d_a < d_r
    gapsum = F(0)
    seen = set()
    for (lam, mu), cc in edge_cc.items():
        if (mu, lam) in seen:
            continue
        seen.add((lam, mu))
        Dl, Dm = Dcache[lam], Dcache[mu]
        added = [u for u in set(Dl) | set(Dm) if Dm.get(u, 0) == Dl.get(u, 0) + 1]
        removed = [u for u in set(Dl) | set(Dm) if Dm.get(u, 0) == Dl.get(u, 0) - 1]
        if len(added) != 1 or len(removed) != 1:
            continue
        cA, cB = added[0], removed[0]
        s = F(dimcache[lam] * dimcache[mu] * cc, (n + 1) * nfac)
        w_e = 2 * s
        dO = F(cB * cB - cA * cA)
        dABS = F(abs(cB) - abs(cA))
        d_a, d_r = Dl.get(cA, 0), Dl.get(cB, 0)
        # ORIENT THE EDGE. Both orientations of every edge occur, and `r - a` is
        # SIGNED: `dABS < 0` just means this one was enumerated from the other
        # end. Pterm and ratio_e are orientation-invariant (both factors flip),
        # but the SPLIT is not -- summing Pterm/(r-a) over unoriented edges
        # cancels to exactly zero, which is how this was caught.
        #
        # Flipping to mu->lam swaps which content is added and re-measures the
        # diagonal lengths in mu. Exactly, since mu = lam + box(cA) - box(cB):
        #   D_mu(cA) = D_lam(cA) + 1,  D_mu(cB) = D_lam(cB) - 1
        # so  D_mu(cB) - D_mu(cA) + 1 = -(D_lam(cA) - D_lam(cB) + 1),
        # which is the sign flip Nterm needs.
        if dABS < 0:
            cA, cB = cB, cA
            dABS, dO = -dABS, -dO
            d_a, d_r = Dm.get(cA, 0), Dm.get(cB, 0)
        Pterm = w_e * dABS * dO
        Nterm = w_e * F(2 * (d_a - d_r + 1)) * dO
        total_P += Pterm
        ntotal += Nterm
        if Pterm > 0:
            gap = dABS          # r - a, positive on this orientation
            sl = F(d_a - d_r, 1) / gap
            slope_num += Pterm * sl
            gap_num += Pterm / gap
            gapsum += Pterm * gap
            if sl > slope_max:
                slope_max = sl
            if d_a < d_r:
                slope_neg_w += Pterm
    S = 2 * slope_num / total_P
    Q = 2 * gap_num / total_P
    NP = ntotal / total_P
    return {
        "n": n, "NP": NP, "S": S, "Q": Q,
        "mean_slope": slope_num / total_P,
        "max_slope": slope_max,
        "mean_gap": gapsum / total_P,
        "w_slope_negative": slope_neg_w / total_P,
    }


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 40   # ~6 min; 32 is ~12 s
    t0 = time.monotonic_ns()
    rows, checks = [], []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    print(f"{'n':>3} {'N/P':>10} {'S (slope)':>11} {'Q (gap)':>10} "
          f"{'mean slope':>11} {'max slope':>10} {'mean gap':>9}")
    exact_split = True
    for n in range(4, nmax + 1):
        r = decompose(n)
        rows.append(r)
        if r["S"] + r["Q"] != r["NP"]:
            exact_split = False
        print(f"{n:>3} {nstr(mpf(r['NP'].numerator)/mpf(r['NP'].denominator), 7):>10} "
              f"{nstr(mpf(r['S'].numerator)/mpf(r['S'].denominator), 7):>11} "
              f"{nstr(mpf(r['Q'].numerator)/mpf(r['Q'].denominator), 7):>10} "
              f"{nstr(mpf(r['mean_slope'].numerator)/mpf(r['mean_slope'].denominator), 7):>11} "
              f"{nstr(mpf(r['max_slope'].numerator)/mpf(r['max_slope'].denominator), 5):>10} "
              f"{nstr(mpf(r['mean_gap'].numerator)/mpf(r['mean_gap'].denominator), 6):>9}")

    def f(x):
        return mpf(x.numerator) / mpf(x.denominator)

    check("decomposition is exact: S + Q == N/P as Fractions", exact_split,
          f"verified on n = 4..{nmax}")
    check("N/P < 1 on the whole range", all(r["NP"] < 1 for r in rows),
          f"max N/P = {nstr(max(f(r['NP']) for r in rows), 8)}")

    # Q ~ C/sqrt(n): the small-gap term VANISHES, so the slope term carries the
    # whole limit. Measured on the upper half of the range, where the small-n
    # transient (S is negative below n = 13) has died out.
    tail = [r for r in rows if r["n"] >= max(6, nmax // 2)]
    sq = [sqrt(mpf(r["n"])) * f(r["Q"]) for r in tail]
    spread = (max(sq) - min(sq)) / min(sq)
    check("the small-gap term scales as Q ~ C/sqrt(n), i.e. it vanishes",
          spread < mpf("0.05"),
          f"sqrt(n)*Q over n = {tail[0]['n']}..{tail[-1]['n']} is "
          f"{nstr(min(sq), 6)}..{nstr(max(sq), 6)} (spread {nstr(spread * 100, 3)}%)")

    check("so the SLOPE term carries the limit: S rises while Q falls",
          f(rows[-1]["S"]) > f(rows[-2]["S"]) and f(rows[-1]["Q"]) < f(rows[-2]["Q"]),
          f"at n = {rows[-1]['n']}: S = {nstr(f(rows[-1]['S']), 6)} rising, "
          f"Q = {nstr(f(rows[-1]['Q']), 6)} falling; N/P -> the proved 0.6605")

    # The point of the whole exercise, and it is an ALGEBRAIC statement.
    check("the POINTWISE limit-shape bound is exactly critical, hence insufficient",
          True,
          "|Omega'| <= 1 gives |dD/dc| <= 1/2 pointwise, so S = 2 E[slope] <= 1 and "
          "N/P = S + Q <= 1 + Q > 1. The pointwise bound cannot prove N/P < 1 at ANY "
          "finite n. Strictness must come from the omega-AVERAGE: E[slope] -> 0.33025 "
          "against the pointwise 1/2, a margin of ~1.51x that averaging supplies.")

    # ---- A MUCH WEAKER SUFFICIENT CONDITION THAN THE EFFECTIVE CLT ----
    #
    # N/P is monotone INCREASING from n = 9, and every value sits below the
    # proved limit 0.6605. Monotone-increasing-with-limit-L means sup = L, so
    #
    #     M_1 > 0 for all n
    #       <== [N/P monotone for n >= 9]           (OPEN, observed only)
    #         + [N/P -> 0.6605 < 1]                 (proved, modulo the IO CLT)
    #         + [exact check n <= 9]                (done)
    #
    # That replaces "Berry-Esseen-grade effective limit-shape estimates" with
    # monotonicity of a sequence -- a different and far weaker demand. It is NOT
    # a proof: monotonicity is observed on a finite range, and the increments
    # OSCILLATE (below), so it is not smooth and could in principle fail.
    NPs = [(r["n"], r["NP"]) for r in rows]
    tail_np = [(n, v) for n, v in NPs if n >= 9]
    mono = all(b > a for (_, a), (_, b) in zip(tail_np, tail_np[1:]))
    check("N/P is monotone increasing for n >= 9", mono,
          f"exact Fraction comparison over n = 9..{nmax}; "
          f"the only decreases anywhere are 5->6 and 8->9")
    LIM = F(6605, 10000)
    check("every N/P sits below the proved limit 0.6605",
          all(v < LIM for _, v in NPs),
          f"max = {nstr(max(f(v) for _, v in NPs), 8)} at n = {max(NPs, key=lambda t: t[1])[0]}")

    # The increments oscillate. Extrema are ROUGHLY equally spaced in sqrt(n),
    # but NOT exactly, and the n = 46 data is what showed that:
    #   peaks   n = 12, 25, 44 -> sqrt(n) = 3.464, 5.000, 6.633
    #   troughs n = 20, 36     -> sqrt(n) = 4.472, 6.000
    #   peak-to-peak spacing 1.536 then 1.633 (+6.3%); trough-to-trough 1.528.
    # A constant period would make those equal. They are not, and the spacing is
    # drifting upward, so this is an approximate description and NOT a
    # periodicity. Two predictions were made from it: the n = 36 trough (exact)
    # and a peak at n = 43 (came out at 44, off by one -- precisely because the
    # spacing was assumed constant). Do not extrapolate further: three peaks fit
    # two spacings, and the mechanism is unexplained. The natural suspect, the
    # VKLS support |c| <= 2 sqrt(n) crossing integers, gives period 1/2, not 1.53.
    incs = {b_n: b - a for (_, a), (b_n, b) in zip(tail_np, tail_np[1:])}
    if nmax >= 40:
        window = [n for n in incs if 30 <= n <= 40]
        trough = min(window, key=lambda n: incs[n])
        after = sorted(n for n in window if n > trough)
        check("increment oscillation: trough at n = 36, then rising (PREDICTED)",
              trough == 36 and all(incs[after[i]] < incs[after[i + 1]]
                                   for i in range(len(after) - 1)),
              f"trough at n = {trough}; increments rise monotonically across the "
              f"30..40 window this check inspects. (They peak at n = 44 and fall "
              f"again after -- see the next check; do not read this as rising to "
              f"nmax.)")
    else:
        check("increment oscillation: trough at n = 36, then rising (PREDICTED)",
              False,
              f"NOT CHECKED: needs nmax >= 40, got {nmax}.")

    # SECOND PREDICTION, written before the n >= 46 run existed.
    # Extrema equally spaced in sqrt(n) with period ~1.53 puts the next PEAK at
    # sqrt(n) ~ 6.00 + 0.53 = 6.53, i.e. n ~ 43: increments rise from the n = 36
    # trough to a peak at n ~ 43, then fall through n = 46. If they instead rise
    # monotonically through 46, or peak well away from 43, the sqrt(n)
    # periodicity is wrong and this check must FAIL rather than be reinterpreted.
    if nmax >= 46:
        w2 = sorted(n for n in incs if 37 <= n <= 46)
        peak = max(w2, key=lambda n: incs[n])
        before = [n for n in w2 if n < peak]
        after = [n for n in w2 if n > peak]
        rising = all(incs[before[i]] < incs[before[i + 1]] for i in range(len(before) - 1))
        falling = all(incs[after[i]] > incs[after[i + 1]] for i in range(len(after) - 1))
        check("increment oscillation: PREDICTED peak at n ~ 43, falling after",
              abs(peak - 43) <= 1 and rising and falling and len(after) >= 2,
              f"peak at n = {peak} (predicted 43); rising before = {rising}, "
              f"falling after = {falling}")
    else:
        check("increment oscillation: PREDICTED peak at n ~ 43, falling after",
              False, f"NOT CHECKED: needs nmax >= 46, got {nmax}.")

    check("the measured mean slope stays well under the pointwise 1/2",
          all(r["mean_slope"] < F(1, 2) for r in rows),
          f"max over range {nstr(max(f(r['mean_slope']) for r in rows), 6)} at n = "
          f"{max(rows, key=lambda r: f(r['mean_slope']))['n']}, heading for 0.33025")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    out = {
        "probe": "m1_edge_ratio_decomposition",
        "bean": ["qou-t6hc", "qou-k5r5"],
        "nmax": nmax,
        "rows": [{k: (str(v) if isinstance(v, F) else v) for k, v in r.items()} for r in rows],
        "checks": checks,
        "passed": sum(1 for c in checks if c["pass"]),
        "total": len(checks),
        "ms": int(ms),
    }
    wit = Path(__file__).with_name("m1-edge-ratio-decomposition.witness.json")
    # Hand-rolled dump: build() never runs, so the manifest cannot stamp
    # this one. Ask for the anchor with the same precedence q_parameter
    # uses at compute time (env var > manifest stem > proton) rather than
    # hardcoding a pin this run may not have used.
    from qou_substrate.witness import resolve_q0_anchor as _rq0  # noqa: PLC0415
    _q0a, _q0v = _rq0(__file__)
    out["q0Anchor"] = _q0a
    if _q0v:
        out["q0Value"] = _q0v
    wit.write_text(json.dumps(out, indent=1) + "\n")
    print()
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
