#!/usr/bin/env python3
"""M_1>0: can the TELESCOPING identity replace the effective CLT? Measured.

Gap qou-k5r5, bean qou-t6hc leg A. The reduction stands at

    M_1 > 0  <=>  N/P = S + Q < 1,
    S = 2 E_omega[(d_a - d_r)/g],   Q = 2 E_omega[1/g],   g = r - a > 0.

`..._edge_ratio_decomposition.py` showed Q ~ 2.07/sqrt(n) -> 0, so S carries the
limit; and that the POINTWISE limit-shape bound |dD/dc| <= 1/2 gives exactly
S <= 1, i.e. it is critical and cannot prove N/P < 1 at any finite n.
`..._edge_ratio_monotonicity.py` then showed the per-edge worst case DIVERGES
(~sqrt(2n)), so averaging is forced.

THE IDEA BEING TESTED
---------------------
For SAME-SIGN contents the slope is not merely bounded, it is a DENSITY. Write
delta(t) := D(t) - D(t+1). On the positive axis D is non-increasing and
1-Lipschitz, so delta(t) in {0,1}; in fact delta(t) = #{i : lambda_i - i = t+1},
which is 0 or 1 because lambda_i - i is strictly decreasing (the beta-set /
Maya diagram). Hence for an interval [u,v) with 0 <= u < v,

    slope = (D(u) - D(v))/(v - u) = (1/(v-u)) sum_{t in [u,v)} delta(t)

is the FRACTION OF DROP SITES in the interval. And telescoping pins the total:

    sum_{t=0}^{lambda_1 - 1} delta(t) = D(0) - D(lambda_1) = D(0)   EXACTLY,

so the diagram's GLOBAL drop density is exactly D(0)/lambda_1 -- no limit shape,
no error term, just a telescoping sum. Under VKLS lambda_1/sqrt(n) -> 2 and
D(0)/sqrt(n) -> 2/pi, so the global density -> 1/pi and a uniform-average
S would be 2/pi = 0.63662, against the measured limit 0.6605. The HEADROOM is a
factor of exactly pi/2 = 1.5708: the omega-weighting may inflate the density by
57% and the bound still closes. That is the case for the route.

WHY THIS PROBE EXISTS RATHER THAN A PROOF
-----------------------------------------
Two things the pi/2 headroom argument quietly assumes, both of which are about
LIMITS and neither of which is obviously true at finite n:

  (1) OPPOSITE-SIGN EDGES. For c_A > 0 > c_B the content interval has length
      |c_A| + |c_B| while the denominator is g = |c_B| - |c_A|, so the slope is
      not a density and is exactly the unbounded one (~sqrt(2n)).

      I drafted this probe asserting the telescoping identity says NOTHING
      about those edges, and that the route therefore fails unless their weight
      vanishes. Both halves of that were wrong, and the run is what showed it.
      Their weight does NOT vanish -- it sits near 0.44 -- but the identity does
      reach them, because BOTH sides telescope to the SAME total D(0):

          D(+-u) = D(0) - N^sigma(u),   N^sigma(u) = #drop sites in [0,u) on side sigma
          => d_a - d_r = N^tau(v) - N^sigma(u),  a difference of two counts
             each in [0, D(0)]      =>   |slope| <= D(0)/g.

      The D(0) cancels. That bound is verified here with 0 violations and is
      SHARP: max |slope|*g/D(0) = 1 exactly. So the honest statement is not
      "outside the identity" but "inside it, at an order-of-magnitude cost".

  (2) THE INFLATION FACTOR. omega ~ (r-a)^2 (r+a) picks intervals; it does not
      pick them uniformly. What matters is
          infl := E_omega[slope | same] / E_omega[global density | same],
      i.e. how much more the omega-chosen intervals drop than the diagram's own
      average. The route needs infl bounded, ideally under pi/2.

Everything here is exact. The accumulation is INTEGER, which is not an
optimisation but the reason the split is trustworthy: with
Pterm = w * dABS * dO and slope = num/dABS,

    Pterm * slope   = w * dO * num          (integer)
    Pterm * (1/g)   = w * dO * sgn(dABS)    (integer)

so S and Q are ratios of integer sums with no rounding anywhere. CONTROL:
2*(S_num + Q_num) must equal N_num exactly, since num + sgn = Dx - Dy in both
orientations. A split that merely looks plausible is worth nothing -- an
earlier probe in this cluster had a term cancel to exactly zero and its
algebraic control passed straight through it.

WHAT THIS RUN SETTLED
---------------------
Three predictions written into the checks were REFUTED by the measurement and
are recorded as refuted rather than rewritten: opposite-sign weight does not
shrink (~0.44); S_opp is not negative (it crosses at n ~ 18 and saturates near
0.118, ~36% of S); and lambda_1 > 2 D(0) FAILS pointwise on ~10% of the
omega-weight, min margin -6. The last is the important one -- the pointwise
form of the pi/2 headroom argument is dead, because omega charges atypical
diagrams and a square has lambda_1 = D(0). Only the AVERAGED form survives,
E_omega[D(0)/lambda_1] < 1/2, which is measured here and holds with room.

What survives is worth having: an elementary, deterministic, two-case per-edge
bound where previously there was an appeal to Berry-Esseen-grade asymptotics.
What it does not do is close the gap -- the two bounds together still exceed 1,
so averaging is required on both sides.

Honesty: measurement deciding whether a ROUTE is viable; scope-(a); no fit;
nothing wired; gap qou-k5r5 stays OPEN. This probe cannot prove M_1 > 0 and
does not claim to.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wlambda_covariance_epic_M1_edge_ratio_monotonicity import (  # noqa: E402
    corners, dim, factorial, partitions,
)
from mpmath import mp, mpf, nstr  # noqa: E402

mp.dps = 40


def show(x, d=6):
    if isinstance(x, F):
        return nstr(mpf(x.numerator) / mpf(x.denominator), d)
    return nstr(mpf(x), d)


def durfee(Lam):
    """D_Lam(0): boxes on the main diagonal = #{i : Lam_i >= i+1}."""
    k = 0
    for i, p in enumerate(Lam):
        if p >= i + 1:
            k += 1
        else:
            break
    return k


def analyse(n):
    nfac = factorial(n)
    dimc = {lam: dim(lam, nfac) for lam in partitions(n)}

    Ptot = 0          # sum of Pterm            (integer)
    Ntot = 0          # sum of Nterm            (integer)
    S_num = {True: 0, False: 0}   # keyed by same-sign
    Q_num = {True: 0, False: 0}
    W = {True: 0, False: 0}       # omega-weight (= sum of Pterm) per class
    dens = defaultdict(int)       # (D0, lam1) -> omega-weight, SAME-sign only
    dens_all = defaultdict(int)   # (D0, lam1) -> omega-weight, all edges
    bnd_opp = defaultdict(int)    # (D0, g) -> omega-weight, OPP-sign: bounds S_opp
    sharp = F(0)                  # max over OPP edges of |slope|*g/D0 -- is the bound tight?
    bad_bound = 0                 # OPP edges violating |slope| <= D0/g
    bad_half = 0                  # ... and against the deliberately halved bound (control)
    max_slope = {True: None, False: None}
    bad_lipschitz = []            # same-sign edges violating |slope| <= 1
    viol_lam1 = 0                 # omega-weight where lambda_1 <= 2 D(0)
    margin_min = None             # min of lambda_1 - 2 D(0) over omega support

    for Lam in partitions(n + 1):
        cs = corners(Lam)
        k = len(cs)
        if k < 2:
            continue
        D0L = durfee(Lam)
        L1 = Lam[0]
        ds = [dimc[c[2]] for c in cs]
        # row index of each corner, needed for lambda_1 of the child
        rows = []
        Lc = len(Lam)
        for i in range(Lc):
            if Lam[i] > (Lam[i + 1] if i + 1 < Lc else 0):
                rows.append(i)
        for x in range(k):
            cx, Dx, _ = cs[x]
            for y in range(x + 1, k):
                cy, Dy, _ = cs[y]
                dABS = abs(cy) - abs(cx)
                if dABS == 0:
                    continue                      # Pterm = 0, carries no omega
                dO = cy * cy - cx * cx
                w = ds[x] * ds[y]
                Pt = w * dABS * dO                # >= 0, orientation-invariant
                Nt = w * 2 * (Dx - Dy) * dO
                Ptot += Pt
                Ntot += Nt
                # orientation: the box is ADDED at the content nearer the
                # diagonal. dABS > 0 means |c_y| > |c_x|, so c_x is the added one.
                if dABS > 0:
                    num, addc, addrow = Dx - Dy - 1, cx, rows[x]
                else:
                    num, addc, addrow = Dx - Dy + 1, cy, rows[y]
                same = not (cx > 0 > cy)
                S_num[same] += w * dO * num
                Q_num[same] += w * dO * (1 if dABS > 0 else -1)
                W[same] += Pt
                # the diagram the box is added to
                D0 = D0L - (1 if addc == 0 else 0)
                lam1 = L1 - (1 if addrow == 0 else 0)
                dens_all[(D0, lam1)] += Pt
                if same:
                    dens[(D0, lam1)] += Pt
                    sl = F(num, dABS)
                    if abs(sl) > 1:
                        bad_lipschitz.append((Lam, cx, cy, sl))
                sl = F(num, dABS)
                if not same:
                    bnd_opp[(D0, g_abs := abs(dABS))] += Pt
                    if D0:
                        if abs(sl) > F(D0, g_abs):
                            bad_bound += 1
                        r = abs(sl) * F(g_abs, D0)
                        if r > sharp:
                            sharp = r
                        if abs(sl) > F(D0, 2 * g_abs):
                            bad_half += 1
                if max_slope[same] is None or sl > max_slope[same]:
                    max_slope[same] = sl
                m = lam1 - 2 * D0
                if m <= 0:
                    viol_lam1 += Pt
                if margin_min is None or m < margin_min:
                    margin_min = m

    def wmean(acc, tot):
        if tot == 0:
            return F(0)
        return sum((F(v, tot) * F(D0, lam1) for (D0, lam1), v in acc.items()), F(0))

    Wt = W[True] + W[False]
    return {
        "n": n,
        "NP": F(Ntot, Ptot),
        "S": F(2 * (S_num[True] + S_num[False]), Ptot),
        "S_same": F(2 * S_num[True], Ptot),
        "S_opp": F(2 * S_num[False], Ptot),
        "Q": F(2 * (Q_num[True] + Q_num[False]), Ptot),
        "w_same": F(W[True], Wt),
        "w_opp": F(W[False], Wt),
        # E_omega[global drop density], conditioned on same-sign
        "dens_same": wmean(dens, W[True]),
        "dens_all": wmean(dens_all, Wt),
        # E_omega[slope | same]  =  S_same / (2 * w_same)
        "slope_same": F(S_num[True], W[True]) if W[True] else F(0),
        "slope_opp": F(S_num[False], W[False]) if W[False] else F(0),
        "max_slope_same": max_slope[True],
        "max_slope_opp": max_slope[False],
        "bad_lipschitz": len(bad_lipschitz),
        "w_lam1_viol": F(viol_lam1, Ptot),
        "margin_min": margin_min,
        # 2 * E_omega[D(0)/g ; opp] -- the telescoping bound ON S_opp
        "B_opp": sum((F(2 * v, Ptot) * F(D0, g) for (D0, g), v in bnd_opp.items()), F(0)),
        "sharp": sharp,
        "bad_bound": bad_bound,
        "bad_half": bad_half,
    }


def main():
    t0 = time.monotonic_ns()
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 46
    checks = []

    def check(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})

    rows = []
    print(f"# telescoping route: does the SAME-SIGN density argument survive? (n = 4..{nmax})")
    print(f"# {'n':>3} {'N/P':>9} {'S_same':>9} {'S_opp':>9} {'Q':>9} "
          f"{'w_opp':>8} {'E[slope|s]':>11} {'E[dens|s]':>10} {'infl':>7}")
    for n in range(4, nmax + 1):
        r = analyse(n)
        infl = (r["slope_same"] / r["dens_same"]) if r["dens_same"] else F(0)
        r["infl"] = infl
        rows.append(r)
        print(f"  {n:>3} {show(r['NP']):>9} {show(r['S_same']):>9} {show(r['S_opp']):>9} "
              f"{show(r['Q']):>9} {show(r['w_opp']):>8} {show(r['slope_same']):>11} "
              f"{show(r['dens_same']):>10} {show(infl):>7}", flush=True)

    # ---- CONTROL: the split is an identity, not a plausible-looking pair ----
    bad = [r["n"] for r in rows if r["S"] + r["Q"] != r["NP"]]
    check("CONTROL: S + Q = N/P exactly, and S_same + S_opp = S",
          not bad and not [r["n"] for r in rows if r["S_same"] + r["S_opp"] != r["S"]],
          f"exact Fraction identity at every n = 4..{nmax}, {len(bad)} mismatches. "
          f"Integer accumulation throughout, so there is no rounding to hide in.")

    prev = Path(__file__).with_name("m1-edge-ratio-decomposition.witness.json")
    pv = {r["n"]: (F(r["NP"]), F(r["S"]), F(r["Q"])) for r in json.loads(prev.read_text())["rows"]}
    sh = [r for r in rows if r["n"] in pv]
    mm = [r["n"] for r in sh if (r["NP"], r["S"], r["Q"]) != pv[r["n"]]]
    check("CONTROL: N/P, S and Q agree with the committed decomposition witness",
          sh and not mm,
          f"exact Fraction equality on n = {sh[0]['n']}..{sh[-1]['n']} ({len(sh)} levels), "
          f"{len(mm)} mismatches. This probe reaches S and Q by a different route "
          f"(Lam-centric, integer) than the witness did (pair-dict, Fraction).")

    # ---- THE TWO-CASE TELESCOPING BOUND (this is what the route actually gives) ----
    #
    # Both sides telescope. Writing N^sigma(u) for the number of drop sites in
    # [0,u) on side sigma, D(+-u) = D(0) - N^sigma(u), so for an edge with
    # |c_A| = u < v = |c_B|:
    #
    #   SAME sign:  d_a - d_r = N^sigma(v) - N^sigma(u) = #drops in [u,v)
    #               => 0 <= slope <= 1, and slope IS a density.
    #   OPP  sign:  d_a - d_r = N^tau(v) - N^sigma(u), a difference of two counts
    #               each in [0, D(0)]  => |slope| <= D(0)/g.
    #
    # The D(0) cancels in the opposite-sign case, which is why the identity DOES
    # reach those edges -- contrary to how this probe's own header framed them.
    check("TELESCOPING case 1 (same sign): slope is a DENSITY, 0 <= slope <= 1",
          all(r["bad_lipschitz"] == 0 for r in rows),
          f"0 violations over n = 4..{nmax}. delta(t) = D(t)-D(t+1) in {{0,1}}, so "
          f"the same-sign slope is the fraction of drop sites in [u,v). "
          f"max over range = {max(r['max_slope_same'] for r in rows)}.")

    check("TELESCOPING case 2 (opposite sign): |slope| <= D(0)/g",
          all(r["bad_bound"] == 0 for r in rows),
          f"0 violations over n = 4..{nmax}. The two side-telescopings share the "
          f"same total D(0), which cancels; what is left is a difference of two "
          f"drop-site counts, each in [0, D(0)]. This is the case the header "
          f"called out of reach of the identity, and it is not.")

    worst_sharp = max(r["sharp"] for r in rows)
    check("...and case 2 is SHARP: the bound is attained, not slack",
          worst_sharp == 1,
          f"max over opposite-sign edges of |slope|*g/D(0) = {worst_sharp} "
          f"(exactly 1) over n = 4..{nmax}. A bound one cannot improve per-edge; "
          f"everything further must come from averaging.")

    check("CONTROL: the case-2 detector fires against a halved bound D(0)/2g",
          sum(r["bad_half"] for r in rows) > 0,
          f"{sum(r['bad_half'] for r in rows)} violations of |slope| <= D(0)/2g "
          f"over the same edges, so the check above is comparing something.")

    # ---- THREE PREDICTIONS OF MINE, ALL REFUTED BY THIS RUN ----
    tail = rows[-8:]
    opp_w = [r["w_opp"] for r in tail]
    opp_s = [r["S_opp"] for r in tail]
    check("REFUTED (mine): omega-weight on opposite-sign edges does NOT shrink",
          not all(a > b for a, b in zip(opp_w, opp_w[1:])),
          f"w_opp over n = {tail[0]['n']}..{tail[-1]['n']}: {[show(v, 4) for v in opp_w]} "
          f"-- it peaks near n = 40 and sits around 0.44, not shrinking. I predicted "
          f"it would vanish. It does not, so the opposite-sign case had to be "
          f"handled rather than dismissed, which is what case 2 above does.")

    check("REFUTED (mine): S_opp is not negative -- it crosses zero and SATURATES",
          not all(v < 0 for v in opp_s),
          f"S_opp over the same range: {[show(v, 4) for v in opp_s]}. It is negative "
          f"below n ~ 18, crosses, and flattens near 0.118 -- about 36% of S at "
          f"n = {nmax}. I predicted it would subtract from S. For n >= 19 it adds.")

    check("REFUTED (mine): lambda_1 > 2 D(0) FAILS pointwise on the omega support",
          any(r["w_lam1_viol"] > 0 for r in rows),
          f"omega-weight on lambda_1 <= 2 D(0): {[show(r['w_lam1_viol'], 3) for r in tail]} "
          f"-- around 10%, not 0; min margin lambda_1 - 2 D(0) = "
          f"{min(r['margin_min'] for r in rows)}. Under VKLS the ratio -> pi/2, but "
          f"that is about TYPICAL diagrams and the omega-measure charges atypical "
          f"ones (a square has lambda_1 = D(0)). The pointwise form of the headroom "
          f"argument is DEAD; only an averaged form can survive.")

    # ---- WHAT SURVIVES ----
    infl = [r["infl"] for r in tail]
    PI2 = mp.pi / 2
    worst = max(r["infl"] for r in rows)
    # CORRECTED (see ..._M1_kappa_site_distribution.py). An earlier version of this
    # check called 0.494 against pi/2 "comfortable headroom". It is not headroom.
    # E_omega[D(0)/lambda_1] -> 1/pi, so asymptotically infl < pi/2 is the SAME
    # statement as E_omega[density] < 1/2 -- the pointwise limit-shape bound that
    # ..._edge_ratio_decomposition.py already showed to be EXACTLY CRITICAL. The
    # check still measures something real; it just is not independent evidence.
    check("inflation E[slope|same]/E[global density|same] < pi/2 (NOT independent)",
          mpf(worst.numerator) / mpf(worst.denominator) < PI2,
          f"max over n = 4..{nmax} is {show(worst)} against pi/2 = {nstr(PI2, 6)}; "
          f"last eight {[show(v, 4) for v in infl]} -- rising, and its limit is NOT "
          f"determined by this range. Below 1 throughout, i.e. the omega-chosen "
          f"intervals drop LESS than the diagram's own average. CAVEAT: "
          f"asymptotically this inequality IS the critical pointwise bound "
          f"E[density] < 1/2, not a margin on top of it. What does bear on the "
          f"route is WHERE kappa sits, measured in ..._M1_kappa_site_distribution.py: "
          f"infl -> pi/2 needs kappa at the origin, and kappa moves away from it.")

    # NOT scoped to the tail to make it pass: n = 4 genuinely violates it (25/48),
    # because lambda = (2,2) has lambda_1 = D(0). The exception is named, and the
    # check still fails if a violation appears anywhere at n >= 5.
    exc = [r["n"] for r in rows if r["dens_all"] >= F(1, 2)]
    check("SURVIVES: the AVERAGED form of the dead pointwise condition holds for n >= 5",
          exc == [4] or exc == [],
          f"E_omega[D(0)/lambda_1] < 1/2 uninterrupted on n = 5..{nmax}; the sole "
          f"exception anywhere is n = 4 at 25/48 = {show(F(25, 48), 4)}, where "
          f"lambda = (2,2) has lambda_1 = D(0). Last eight: "
          f"{[show(r['dens_all'], 4) for r in tail]}, heading for the VKLS "
          f"1/pi = {nstr(1 / mp.pi, 6)}. This is what must replace 'lambda_1 > 2 D(0) "
          f"pointwise', and effective Plancherel concentration for lambda_1 is where "
          f"it would come from.")

    # ---- HOW MUCH SLACK IS LEFT: the bound against the truth ----
    slack = [(r["n"], r["B_opp"], r["S_opp"]) for r in tail]
    r46 = rows[-1]
    check("MEASURED: the case-2 bound is ~an order of magnitude too weak as it stands",
          True,
          f"at n = {r46['n']}: bound B_opp = 2 E[D(0)/g ; opp] = {show(r46['B_opp'])} "
          f"against the true S_opp = {show(r46['S_opp'])}, a factor of "
          f"{show(r46['B_opp'] / r46['S_opp'] if r46['S_opp'] else F(0), 4)}. Combined "
          f"with the trivial same-sign bound 2*w_same = "
          f"{show(2 * r46['w_same'])} the total exceeds 1, so the per-edge bounds "
          f"ALONE do not close it. They are elementary and deterministic, which the "
          f"effective CLT is not -- but averaging is still required on BOTH sides.")

    ms = (time.monotonic_ns() - t0) // 1_000_000
    out = {
        "probe": "m1_telescoping_route",
        "bean": ["qou-t6hc", "qou-k5r5"],
        "nmax": nmax,
        "rows": [{k: (str(v) if isinstance(v, F) else v) for k, v in r.items()} for r in rows],
        "checks": checks,
        "passed": sum(1 for c in checks if c["pass"]),
        "total": len(checks),
        "ms": int(ms),
    }
    Path(__file__).with_name("m1-telescoping-route.witness.json").write_text(
        json.dumps(out, indent=1) + "\n")
    print()
    for c in checks:
        print(("  PASS  " if c["pass"] else "  FAIL  ") + c["name"] + " -- " + c["detail"])
    print()
    print("RESULT: telescoping route measured; see the three FALSIFIER checks.")
    print("RESULT: gap qou-k5r5 stays OPEN -- this probe cannot prove M_1 > 0.")
    print("EXIT: 0" if all(c["pass"] for c in checks) else "EXIT: 1")
    return 0 if all(c["pass"] for c in checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
