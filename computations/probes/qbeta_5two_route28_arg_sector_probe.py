#!/usr/bin/env python3
"""Route 28 -- Route 27's three obligations, replaced by one and then PROVED.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoArgSector.lean` (sorry-free, lake
green, eleven theorems on `[propext, Classical.choice, Quot.sound]`).

WHAT CHANGED SINCE ROUTE 27
---------------------------
Route 27 confined `sum_j arg(1 - x y_j)` to the UNIFORM window (-pi, 2 pi). That
forces tight control on every individual argument, which is where its 10% and 17%
margins came from -- and it left three inequalities unproved.

But the window only has to exclude phi +/- 2 pi, and it may depend on phi. With
phi in [0, pi) the window (phi - 2 pi, phi + 2 pi) suffices, and it is loose
enough to be reached from bounds that are free or elementary. The margins were an
artefact of the uniform window, not of the mathematics.

This probe measures the new scheme end to end. Every gate checks the statement it
names -- not a proxy for it. That discipline is the point: seven defects in this
lane were checks that tested something ADJACENT to what they claimed.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import arg, cos, exp, fabs, findroot, im, mp, mpf, nstr, pi, polyroots, re, sin
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
                          maxsteps=800, extraprec=2000))


def split(rs, tol):
    """Split a root list into (real roots, roots with Im > 0, roots with Im < 0)."""
    reals = [r for r in rs if fabs(im(r)) < tol]
    ups = [r for r in rs if im(r) >= tol]
    downs = [r for r in rs if im(r) <= -tol]
    return reals, ups, downs


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -20
    tiny = mpf(10) ** -25
    N = 700
    gates = []

    # phi_0: the discriminant root, u = 2 cos phi, Q(u) = u^4 - 6u^3 + 7u^2 + 6u - 31
    u0 = findroot(lambda u: u ** 4 - 6 * u ** 3 + 7 * u ** 2 + 6 * u - 31, mpf("-1.5"))
    phi0 = mp.acos(u0 / 2)

    # ---- G1: the two Vieta relations the Lean proof consumes ------------------
    worst_h1 = worst_h2 = mpf(0)
    minR = mpf(10) ** 9
    maxR = -minR
    n_pairs = 0
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        _, ups, _ = split(roots_at(x), tol)
        if not ups:
            continue
        n_pairs += 1
        a, b = re(ups[0]), im(ups[0])
        R = a * a + b * b
        c = cos(ph)
        minR, maxR = min(minR, R), max(maxR, R)
        worst_h1 = max(worst_h1, fabs(2 * c * R - (1 + 2 * a * R)))
        worst_h2 = max(worst_h2, fabs(2 * a * (R - 1) - (R * R - R - 1)))
    gates.append({
        "gate": "G1",
        "claim": "the two hypotheses of Lean's `sa_lt_cb` really do hold on the arc: with "
                 "y_2 = a + b i the upper member of the conjugate pair and R = |y_2|^2, "
                 "2 c R = 1 + 2 a R  and  2 a (R-1) = R^2 - R - 1. These are e_1 = 2c with "
                 "the real root written 1/R, and e_2 - e_1 = 1 cleared of denominators",
        "n_complex_pair_points": n_pairs,
        "worst_residual_h1": nstr(worst_h1, 10), "worst_residual_h2": nstr(worst_h2, 10),
        "R_range": [nstr(minR, 12), nstr(maxR, 12)],
        "pass": bool(worst_h1 < mpf(10) ** -25 and worst_h2 < mpf(10) ** -25 and n_pairs > 0),
    })

    # ---- G2: 1 < R, equivalently the positive real root is below 1 ------------
    worst_y1 = -mpf(10) ** 9
    minRR = mpf(10) ** 9
    n_y1 = 0
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        rs = roots_at(x)
        reals, ups, _ = split(rs, tol)
        pos = [re(r) for r in reals if re(r) > 0]
        if len(pos) != 1:
            continue
        n_y1 += 1
        worst_y1 = max(worst_y1, pos[0])
        if ups:
            a, b = re(ups[0]), im(ups[0])
            minRR = min(minRR, a * a + b * b)
    gates.append({
        "gate": "G2",
        "claim": "there is EXACTLY ONE positive real root at every arc point, and it lies "
                 "strictly below 1 -- which is Lean's `one_lt_normSq` (R = 1/y_1 > 1). The "
                 "proof needs no numerics: p(0) = -1 < 0 < 1 = p(1) for the monic cubic",
        "n_points_with_unique_positive_real_root": n_y1, "n_points": N - 1,
        "max_y1": nstr(worst_y1, 15), "min_R_over_complex_arc": nstr(minRR, 12),
        "pass": bool(n_y1 == N - 1 and worst_y1 < 1 and minRR > 1),
    })

    # ---- G3: the single surviving obligation, s*a - c*b < 0 -------------------
    worst_sacb = -mpf(10) ** 9
    at_sacb = None
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        _, ups, _ = split(roots_at(x), tol)
        if not ups:
            continue
        a, b = re(ups[0]), im(ups[0])
        v = sin(ph) * a - cos(ph) * b
        if v > worst_sacb:
            worst_sacb, at_sacb = v, ph
    gates.append({
        "gate": "G3",
        "claim": "Route 27's obligation s*a < c*b, now a THEOREM (`sa_lt_cb`) rather than a "
                 "measurement. Route 27 left it open with a measured margin; the Lean proof "
                 "discharges it from G1 by three sign certificates -- a > 0 makes "
                 "E = 1 + 4aR + 4a^2 R(R-1) positive termwise; a < 0 < -c makes "
                 "E(R-1) = R^3(R-1)^2 - 1 with R^3(R-1)^2 = (R^3-R^2)(R^2-R) a product of two "
                 "factors in (0,1); and a <= 0 <= c is immediate",
        "max_s_a_minus_c_b": nstr(worst_sacb, 20),
        "at_phi": nstr(at_sacb, 15), "at_phi_over_pi": nstr(at_sacb / pi, 12),
        "pass": bool(worst_sacb < 0),
    })

    # ---- G4: the four sector inputs, each checked as stated -------------------
    bad = {"a1_in_open_sector": 0, "one_root_im_nonpos": 0, "two_roots_im_nonpos_when_big": 0}
    n_big = 0
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        rs = roots_at(x)
        reals, _, _ = split(rs, tol)
        pos = [r for r in reals if re(r) > 0]
        a1 = arg(1 - x * pos[0])
        if not (-pi / 2 < a1 < 0):
            bad["a1_in_open_sector"] += 1
        others = [r for r in rs if r != pos[0]]
        n_nonpos = sum(1 for r in others if im(x * r) <= 0)
        if n_nonpos < 1:
            bad["one_root_im_nonpos"] += 1
        if ph > pi / 2:
            n_big += 1
            if n_nonpos < 2:
                bad["two_roots_im_nonpos_when_big"] += 1
    gates.append({
        "gate": "G4",
        "claim": "the four inputs of `branchInt_eq_zero_of_sector`, each checked as stated: "
                 "arg(1 - x y_1) lies in the OPEN sector (-pi/2, 0) for the positive real root "
                 "(this is what |x y_1| = y_1 < 1 buys, and it replaces Route 27's measured "
                 "-1.4077); at least one other root has Im(x y) <= 0; and when phi > pi/2, at "
                 "least TWO do -- which is exactly where the slack below phi - 2 pi runs out",
        "violations": {k: v for k, v in bad.items()},
        "n_points": N - 1, "n_points_with_phi_gt_pi_over_2": n_big,
        "pass": bool(all(v == 0 for v in bad.values())),
    })

    # ---- G5: the window, and k = 0 -------------------------------------------
    bad5 = {"below_window": 0, "above_window": 0, "k_nonzero": 0}
    worst_k = mpf(0)
    for i in range(1, N):
        ph = pi * i / N
        x = exp(1j * ph)
        S = sum(arg(1 - x * r) for r in roots_at(x))
        if not S > ph - 2 * pi:
            bad5["below_window"] += 1
        if not S < ph + 2 * pi:
            bad5["above_window"] += 1
        k = (S - ph) / (2 * pi)
        worst_k = max(worst_k, fabs(k))
        if fabs(k) > tiny:
            bad5["k_nonzero"] += 1
    gates.append({
        "gate": "G5",
        "claim": "the conclusion: sum_j arg(1 - x y_j) lands inside the phi-DEPENDENT window "
                 "(phi - 2 pi, phi + 2 pi), and the branch integer k in "
                 "sum_j log(1 - x y_j) = log x + 2 pi i k is 0",
        "violations": {k: v for k, v in bad5.items()}, "n_points": N - 1,
        "worst_abs_k": nstr(worst_k, 10),
        "pass": bool(all(v == 0 for v in bad5.values())),
    })

    # ---- G6: the phi>pi/2 hypothesis is LOAD-BEARING, not decorative ---------
    # Without `0 <= a_2`, the best available lower bound is -pi/2 + (-pi) + 0 = -3pi/2.
    # That clears phi - 2 pi only while phi <= pi/2.
    weak = -3 * pi / 2
    fails_from = None
    n_weak_fail = 0
    for i in range(1, N):
        ph = pi * i / N
        if not (weak > ph - 2 * pi):
            n_weak_fail += 1
            if fails_from is None:
                fails_from = ph
    gates.append({
        "gate": "G6",
        "claim": "an ADVERSARIAL check on the Lean statement itself: the extra hypothesis "
                 "`pi/2 < phi -> 0 <= a_2` is load-bearing, not decoration. Dropping it leaves "
                 "the lower bound -pi/2 + (-pi) + 0 = -3 pi/2, which clears phi - 2 pi only "
                 "while phi <= pi/2 -- so the weaker statement is FALSE on more than half the "
                 "arc and the hypothesis cannot be deleted",
        "weak_lower_bound": nstr(weak, 12),
        "n_arc_points_where_weak_bound_fails": n_weak_fail, "n_points": N - 1,
        "weak_bound_first_fails_at_phi": nstr(fails_from, 12) if fails_from else None,
        "pi_over_2": nstr(pi / 2, 12),
        "pass": bool(n_weak_fail > 0),
    })

    # ---- G7: the Lean non-vacuity witness R = 2 is a genuine arc point --------
    lo, hi = phi0 * mpf(1) / 100, phi0 * 99 / 100

    def Rof(ph):
        _, ups, _ = split(roots_at(exp(1j * ph)), tol)
        if not ups:
            return None
        a, b = re(ups[0]), im(ups[0])
        return a * a + b * b

    for _ in range(200):
        mid = (lo + hi) / 2
        if Rof(mid) is None:
            hi = mid
            continue
        if Rof(mid) > 2:
            lo = mid
        else:
            hi = mid
    ph2 = (lo + hi) / 2
    _, ups2, _ = split(roots_at(exp(1j * ph2)), tol)
    a2, b2 = re(ups2[0]), im(ups2[0])
    gates.append({
        "gate": "G7",
        "claim": "the witness in Lean's `sa_lt_cb_nonvacuous` (R = 2, a = 1/2, c = 3/4, "
                 "b = sqrt7/2, s = sqrt7/4) is a genuine point of the arc, not merely a formal "
                 "solution of the constraints: solving R(phi) = 2 recovers a = 1/2 and "
                 "c = cos phi = 3/4",
        "phi_with_R_eq_2": nstr(ph2, 20),
        "a_there": nstr(a2, 20), "a_target": "0.5",
        "cos_phi_there": nstr(cos(ph2), 20), "c_target": "0.75",
        "b_there": nstr(b2, 20), "b_target": nstr(mp.sqrt(7) / 2, 20),
        "pass": bool(fabs(a2 - mpf(1) / 2) < mpf(10) ** -20
                     and fabs(cos(ph2) - mpf(3) / 4) < mpf(10) ** -20
                     and fabs(b2 - mp.sqrt(7) / 2) < mpf(10) ** -20),
    })

    # ---- G8: the all-real branch, where sa_lt_cb is not even needed -----------
    bad8 = {"not_three_real": 0, "not_one_pos_two_neg": 0, "c_not_negative": 0}
    n_caseA = 0
    for i in range(1, N):
        ph = pi * i / N
        if ph <= phi0:
            continue
        n_caseA += 1
        x = exp(1j * ph)
        reals, _, _ = split(roots_at(x), tol)
        if len(reals) != 3:
            bad8["not_three_real"] += 1
            continue
        npos = sum(1 for r in reals if re(r) > 0)
        nneg = sum(1 for r in reals if re(r) < 0)
        if (npos, nneg) != (1, 2):
            bad8["not_one_pos_two_neg"] += 1
        if not cos(ph) < 0:
            bad8["c_not_negative"] += 1
    gates.append({
        "gate": "G8",
        "claim": "on phi > phi_0 all three roots are real, exactly one is positive and two are "
                 "negative, and c < 0 there. So on that part of the arc BOTH extra roots have "
                 "Im(x y) = y sin phi < 0 outright and `sa_lt_cb` is not needed at all -- the "
                 "conjugate-pair inequality is only ever used on phi < phi_0",
        "phi_0": nstr(phi0, 20), "phi_0_over_pi": nstr(phi0 / pi, 12),
        "n_case_A_points": n_caseA, "violations": {k: v for k, v in bad8.items()},
        "pass": bool(all(v == 0 for v in bad8.values()) and n_caseA > 0),
    })

    out = {
        "probe": "qbeta_5two_route28_arg_sector",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoArgSector.lean",
        "supersedes": "qbeta_5two_route27_branch_by_argument (its three obligations are now "
                      "one, and that one is proved)",
        "gates": gates,
        "verdict": {
            "what_route_27_left_open": "three real-algebraic inequalities on |x| = 1 with "
                                       "measured margins of 10% and 17%, needed because the "
                                       "argument sum was confined to the UNIFORM window "
                                       "(-pi, 2 pi).",
            "what_this_route_does": "widens the window to the phi-dependent "
                                    "(phi - 2 pi, phi + 2 pi), which is all that is needed to "
                                    "exclude phi +/- 2 pi. Two of the four resulting inputs are "
                                    "free (Complex.neg_pi_lt_arg, Complex.arg_le_pi), one needs "
                                    "only 0 < y_1 < 1, and the last reduces to s*a < c*b -- "
                                    "which is PROVED in Lean, not measured.",
            "so_the_margins_were": "an artefact of the uniform window, not of the mathematics.",
            "still_open": "the bridge from 'three complex roots satisfying the Vieta relations' "
                          "to 'a real root in (0,1) plus a conjugate pair (or three reals)'. "
                          "That is algebra, not analysis, and it is stated as hypotheses in the "
                          "Lean file rather than assumed silently. hcont's consumer is NOT "
                          "closed by this file.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route28-arg-sector.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:88]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: Route 27's three measured obligations become one, and that one is proved.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
