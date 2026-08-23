#!/usr/bin/env python3
"""Route 32 -- the sum rule IS S(0), and the bridge to the proved identity.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoLevelSevenBridge.lean` (9
theorems, sorry-free, `lake build QOU.QBeta.FiveTwoLevelSevenBridge` green).

WHAT THIS MAPS
--------------
The transport gives S(pi) - S(0) = pi^2. This route identifies both ends:

    S(0)  = -3 pi^2 / 2   <- THIS IS THE 5_2 SUM RULE          [G1]
    S(pi) = -  pi^2 / 2                                        [G2]

and S(pi) sits at x = -1, where the curve's cubic is the LEVEL-7 cubic
y^3 + 2y^2 - y - 1 and w_k = -y_j EXACTLY -- w_1 = 2.24698 is the very argument
that broke hinv1 in this branch's correction 1.                [G3]

There the already-proved cyclotomic identity gives sum_j Re[2L(-y_j) + L(y_j)]
= +pi^2/2, and what separates it from sum_j Re V(-1, y_j) is a log-bilinear
correction with NO DILOGARITHMS:                               [G4, G5]

    corr y = Re[ log(-y)^2 - log(-y) log(1+y) - (1/2) log(y) log(1-y) ]

which sums to exactly -pi^2. G6 shows why: the log-times-log part vanishes at
EVERY root because 2 log|y| = 2 log|1+y| + log(1-y) is the cubic itself, and the
whole -pi^2 is ONE argument at ONE root -- arg(-t) = pi at the unique positive
root. Same -t-on-the-cut that produced corrections 5 and 6; third appearance,
and this time it is the answer rather than a defect.

⚠ G9 RECORDS WHAT THIS DOES NOT CLOSE, and it is not a footnote: the numeric
bridge uses the ANALYTIC Rogers L, while Lean's `extended_sum` is stated for the
corpus's piecewise `extend`. Identifying them is `qou-rstq` item 4 -- open, on
paper only, and sitting directly on this bridge.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import (cos, exp, fabs, findroot, im, log, mp, mpc, mpf, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def roots_at(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=900, extraprec=2500))


def V(x, y):
    return polylog(2, y) + polylog(2, x * y) + polylog(2, y / x) + log(-y) ** 2


def S(ph):
    x = exp(1j * ph)
    return sum(re(V(x, r)) for r in roots_at(x))


def RogersL(z):
    """The ANALYTIC Rogers L, principal branches."""
    return polylog(2, z) + log(z) * log(1 - z) / 2


def corr(y):
    return re(log(-y) ** 2 - log(-y) * log(1 + y) - log(y) * log(1 - y) / 2)


def main() -> int:
    set_compute_dps()
    eps = mpf(10) ** -15
    gates = []

    # ---- G1: S(0) IS the sum rule -------------------------------------------
    S0 = S(eps)
    gates.append({
        "gate": "G1",
        "claim": "S(0) = sum_j Re V(1, y_j) equals -3 pi^2 / 2 -- i.e. S(0) IS the 5_2 sum rule. "
                 "The transport is therefore not a step TOWARDS the sum rule, it is a "
                 "reformulation OF it: S(pi) - S(0) = pi^2 turns the sum rule into a statement "
                 "about the endpoint x = -1",
        "S_at_0": nstr(S0, 24), "minus_3_pi_sq_over_2": nstr(-3 * pi ** 2 / 2, 24),
        "residual": nstr(fabs(S0 + 3 * pi ** 2 / 2), 10),
        "pass": bool(fabs(S0 + 3 * pi ** 2 / 2) < mpf(10) ** -25),
    })

    # ---- G2: S(pi) = -pi^2/2, and S(0) = 3 S(pi) -----------------------------
    Spi = S(pi - eps)
    exact = -pi ** 2 / 2 - 2 * pi * eps + eps ** 2   # S(pi-eps) = S(pi) - (2 pi eps - eps^2)
    gates.append({
        "gate": "G2",
        "claim": "S(pi) = -pi^2/2, checked against the EXACT eps-shifted value rather than a "
                 "rounded one. Note S(0) = 3 * S(pi) exactly -- the 3 in -3 pi^2/2 is the number "
                 "of saddles, which is the kind of structure the resurgence picture would explain",
        "S_at_pi_minus_eps": nstr(Spi, 24), "exact_expected": nstr(exact, 24),
        "residual": nstr(fabs(Spi - exact), 10),
        "S0_over_Spi": nstr(S0 / (-pi ** 2 / 2), 12),
        "pass": bool(fabs(Spi - exact) < mpf(10) ** -22),
    })

    # ---- G3: at x = -1 the cubic is level-7, and w = -y ----------------------
    rs = [re(r) for r in polyroots([1, 2, -1, -1])]
    ws = sorted([-r for r in rs], reverse=True)
    ws_direct = sorted([re(r) for r in polyroots([1, -2, -1, 1])], reverse=True)
    worst_w = max(fabs(a - b) for a, b in zip(ws, ws_direct))
    rs_curve = sorted([re(r) for r in roots_at(mpf(-1))])
    worst_c = max(fabs(a - b) for a, b in zip(sorted(rs), rs_curve))
    gates.append({
        "gate": "G3",
        "claim": "at x = -1 the curve's y-cubic IS the level-7 cubic y^3 + 2y^2 - y - 1, and the "
                 "ladder arguments are w_k = -y_j EXACTLY -- w_1 = 2.24698 is the same value that "
                 "left Li2's disc of convergence and falsified hinv1 (correction 1 of this branch)",
        "roots_y": [nstr(r, 18) for r in sorted(rs)],
        "w_from_minus_y": [nstr(w, 18) for w in ws],
        "w_as_roots_of_Y3_minus_2Y2_minus_Y_plus_1": [nstr(w, 18) for w in ws_direct],
        "worst_w_mismatch": nstr(worst_w, 10),
        "worst_curve_vs_levelSeven": nstr(worst_c, 10),
        "pass": bool(worst_w < mpf(10) ** -30 and worst_c < mpf(10) ** -30),
    })

    # ---- G4: the proved cyclotomic identity, in analytic form ---------------
    tot_R = sum(re(2 * RogersL(-r) + RogersL(r)) for r in rs)
    gates.append({
        "gate": "G4",
        "claim": "sum_j Re[2 L(-y_j) + L(y_j)] = +pi^2/2 with the ANALYTIC Rogers L. This is the "
                 "shape of Lean's `extended_sum`, with the multiplicities matching once w = -y. "
                 "⚠ Lean's theorem is about the corpus's piecewise `extend`, NOT this L -- see G9",
        "value": nstr(tot_R, 22), "pi_sq_over_2": nstr(pi ** 2 / 2, 22),
        "residual": nstr(fabs(tot_R - pi ** 2 / 2), 10),
        "pass": bool(fabs(tot_R - pi ** 2 / 2) < mpf(10) ** -25),
    })

    # ---- G5: the correction is exactly -pi^2 --------------------------------
    tot_V = sum(re(V(mpf(-1), r)) for r in rs)
    gap = tot_V - tot_R
    tot_corr = sum(corr(r) for r in rs)
    gates.append({
        "gate": "G5",
        "claim": "the gap between sum_j Re V(-1, y_j) and sum_j Re[2L(-y_j)+L(y_j)] is exactly "
                 "-pi^2, and it equals the log-bilinear sum_j corr(y_j) -- a quantity with NO "
                 "dilogarithms in it. That is the whole remaining arithmetic of the bridge, and "
                 "Lean's `corr_sum_eq_neg_pi_sq` proves it",
        "sum_Re_V": nstr(tot_V, 22), "sum_Re_Rogers": nstr(tot_R, 22),
        "gap": nstr(gap, 22), "minus_pi_sq": nstr(-pi ** 2, 22),
        "gap_residual": nstr(fabs(gap + pi ** 2), 10),
        "sum_corr": nstr(tot_corr, 22),
        "corr_matches_gap": nstr(fabs(tot_corr - gap), 10),
        "pass": bool(fabs(gap + pi ** 2) < mpf(10) ** -25
                     and fabs(tot_corr - gap) < mpf(10) ** -40),
    })

    # ---- G6: WHY it collapses -- per-root decomposition ---------------------
    rows = []
    worst_ll = mpf(0)
    tot_pp = mpf(0)
    for y in sorted(rs):
        a, ka = log(fabs(-y)), (mpf(0) if -y > 0 else mpf(1))
        b, kb = log(fabs(1 + y)), (mpf(0) if 1 + y > 0 else mpf(1))
        c, kc = log(fabs(y)), (mpf(0) if y > 0 else mpf(1))
        d, kd = log(fabs(1 - y)), (mpf(0) if 1 - y > 0 else mpf(1))
        ll = a * a - a * b - c * d / 2
        pp = -ka * ka + ka * kb + kc * kd / 2
        worst_ll = max(worst_ll, fabs(ll))
        tot_pp += pp
        rows.append({"y": nstr(y, 18), "log_log_part": nstr(ll, 10),
                     "pi_sq_coefficient": nstr(pp, 6)})
    gates.append({
        "gate": "G6",
        "claim": "WHY it collapses. Splitting corr into its log-times-log part and its pi^2 part: "
                 "the log-log part vanishes at EVERY root, because "
                 "2 log|y| = 2 log|1+y| + log(1-y) is equivalent to y^2 = (1+y)^2 (1-y), which IS "
                 "the cubic. The entire -pi^2 is the pi^2 coefficient -1 at the UNIQUE POSITIVE "
                 "root, from arg(-t) = pi. One argument, at one root. Lean: `sq_eq_of_root`, "
                 "`log_rel_of_root`, `corr_of_pos_root`, `corr_of_neg_root`",
        "per_root": rows,
        "worst_log_log_part": nstr(worst_ll, 10),
        "total_pi_sq_coefficient": nstr(tot_pp, 6),
        "pass": bool(worst_ll < mpf(10) ** -40 and fabs(tot_pp + 1) < mpf(10) ** -40),
    })

    # ---- G7: y^2 - (1+y)^2(1-y) IS the cubic, identically -------------------
    worst_id = mpf(0)
    for i in range(-30, 31):
        y = mpf(i) / 7
        worst_id = max(worst_id,
                       fabs((y ** 2 - (1 + y) ** 2 * (1 - y)) - (y ** 3 + 2 * y ** 2 - y - 1)))
    gates.append({
        "gate": "G7",
        "claim": "y^2 - (1+y)^2 (1-y) = y^3 + 2y^2 - y - 1 IDENTICALLY in y, not just at the "
                 "roots -- checked at 61 rational points off the roots, so the identity is not "
                 "being confirmed by the very thing it is used to prove. Lean: `sq_eq_of_root`",
        "n_points": 61, "worst_residual": nstr(worst_id, 10),
        "pass": bool(worst_id < mpf(10) ** -40),
    })

    # ---- G8: GAP A -- the real root never collides ---------------------------
    worst_dp = mpf(10) ** 9
    at = None
    for i in range(1, 400):
        ph = pi * i / 400
        x = exp(1j * ph)
        c = re(x)
        t = [re(r) for r in roots_at(x) if fabs(im(r)) < mpf(10) ** -20 and re(r) > 0][0]
        dp = fabs(3 * t ** 2 - 4 * c * t + (2 * c + 1))
        if dp < worst_dp:
            worst_dp, at = dp, ph
    gates.append({
        "gate": "G8",
        "claim": "GAP A, re-priced: |dp/dy| at the positive real root never drops below 1.75 on "
                 "the arc, so the REAL root never collides -- only the other two do, at phi_0. So "
                 "t(phi) is globally differentiable with NO exceptional point, and y_2 + y_3 = "
                 "2c - t and y_2 y_3 = 1/t are too. The obstruction is confined to splitting one "
                 "quadratic whose coefficients are smooth",
        "min_abs_dp_dy_at_real_root": nstr(worst_dp, 12),
        "at_phi_over_pi": nstr(at / pi, 10),
        "pass": bool(worst_dp > 1),
    })

    # ---- G9: the link this gate guarded is now CLOSED ------------------------
    # G9 previously asserted that the `extend` <-> analytic-L identification was
    # OPEN, with pass hardcoded True, and said it was "the one gate here that
    # would fail if the lane ever quietly closed it without saying so".
    # The lane has now closed it -- openly -- so the gate is REWRITTEN rather
    # than left passing on a claim that has drifted. It is also converted from a
    # hardcoded declaration into an actual MEASUREMENT.
    def rogersL_real(u):
        return polylog(2, u) + log(u) * log(1 - u) / 2

    def extend_piecewise(v):
        """The corpus's `extend (pi^2/6) rogersL`, all three branches."""
        C = pi ** 2 / 6
        if v > 1:
            return 2 * C - rogersL_real(1 / v)
        if v < 0:
            return -rogersL_real(v / (v - 1))
        return rogersL_real(v)

    def ReL_analytic(v):
        z = mpc(v, 0)
        return re(polylog(2, z) + log(z) * log(1 - z) / 2)

    xr = findroot(lambda t: t ** 3 - 2 * t ** 2 - t + 1, mpf("0.55"))
    ws = [1 / (1 - xr), xr, (xr - 1) / xr]
    six = ws + [-w for w in ws]
    rows9, worst9 = [], mpf(0)
    for a in six:
        d = fabs(extend_piecewise(a) - ReL_analytic(a))
        worst9 = max(worst9, d)
        rows9.append({"x": nstr(a, 18), "difference": nstr(d, 8),
                      "regime": ("x>1 inversion" if a > 1 else
                                 "x<0 Landen" if a < 0 else "0<=x<=1 identity")})
    gates.append({
        "gate": "G9",
        "claim": "THE LINK THIS GATE GUARDED IS NOW CLOSED, and the gate is rewritten rather than "
                 "left passing on a drifted claim. It used to assert that `extend` = Re of the "
                 "analytic Rogers L held ON PAPER ONLY (qou-rstq item 4), with pass hardcoded "
                 "True, and said it would fail if the lane closed it quietly. The lane closed it "
                 "openly: `extend_eq_re_cRogersL` in QOU/QBeta/FiveTwoExtendIdentification.lean "
                 "proves it for every real x != 0, 1 -- all three regimes, all six arguments. So "
                 "G4's use of the analytic L above is now backed by a Lean theorem, not by "
                 "Route 15's paper argument. This gate now MEASURES the identification at the six "
                 "arguments instead of declaring anything",
        "was": "assertion that the gap EXISTS, pass hardcoded True",
        "now": "measurement of the identification the Lean theorem states",
        "lean_theorem": "QOU.QBeta.FiveTwoExtendIdentification.extend_eq_re_cRogersL",
        "per_argument": rows9,
        "worst_difference": nstr(worst9, 10),
        "pass": bool(worst9 < mpf(10) ** -40),
    })

    # ---- G10: and what remains open, so the closure is not overread ----------
    gates.append({
        "gate": "G10",
        "claim": "WHAT ITEM 4's CLOSURE DOES NOT BUY, stated because the temptation to overread is "
                 "the reason G9 existed. Item 4 was ONE INPUT to this bridge. Still open: (a) GAP "
                 "A, a globally differentiable root labelling -- the one remaining hypothesis in "
                 "the transport, re-priced in G8; (b) ASSEMBLING S(pi) = sum_j Re V(-1, y_j) in "
                 "Lean and composing corr_sum_eq_neg_pi_sq with extended_sum, which item 4 "
                 "unblocks but does not perform. And the headline is untouched: S(0) = -3 pi^2/2 "
                 "IS the sum rule (G1), so the transport REFORMULATES it rather than approaching "
                 "it. Closing item 4 moved a link, not the headline",
        "still_open": ["Gap A -- global root labelling (qou-glbl)",
                       "assembling S(pi) and wiring the bridge to extended_sum (qou-asem)"],
        "headline_unchanged": "S(0) = -3 pi^2/2 IS the sum rule; the transport reformulates it",
        "pass": True,
    })

    out = {
        "probe": "qbeta_5two_route32_levelseven_bridge",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoLevelSevenBridge.lean",
        "gates": gates,
        "verdict": {
            "the_map": "S(0) = -3 pi^2/2 IS the sum rule; the transport turns it into S(pi) = "
                       "-pi^2/2; at x = -1 the cubic is the level-7 one with w = -y; the proved "
                       "cyclotomic identity gives +pi^2/2; and the difference is a log-bilinear "
                       "-pi^2 which is ONE argument at ONE root.",
            "what_is_proved_here": "corr_sum_eq_neg_pi_sq -- the -pi^2, from the cubic itself.",
            "closed_since_this_probe_was_written": "qou-rstq item 4 -- the identification of "
                                  "`extend` with Re of the analytic Rogers L, which sits ON this "
                                  "bridge, is now PROVED in Lean for all three regimes "
                                  "(extend_eq_re_cRogersL). G9 is rewritten accordingly.",
            "what_is_still_open": "(a) the global root labelling for the transport (Gap A, "
                                  "re-priced in G8, bean qou-glbl); (b) assembling S(pi) = sum_j "
                                  "Re V(-1, y_j) in Lean and composing corr_sum_eq_neg_pi_sq with "
                                  "extended_sum (bean qou-asem) -- unblocked by item 4, not "
                                  "performed by it.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route32-levelseven-bridge.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("the sum rule IS S(0); the bridge to the proved identity is one arg at "
                         "one root. The `extend` link (G9) is now CLOSED in Lean; Gap A and the "
                         "assembly (G10) remain."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
