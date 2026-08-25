#!/usr/bin/env python3
"""Route 27 -- pinning the branch integer by an argument count, not continuity.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoBranchByArgument.lean` (sorry-free,
lake green).

THE TRADE
---------
After FiveTwoEnvelopeAssembly, `hcont` is the single open input to the envelope
step, and it is used for exactly one thing: forcing k = 0 in

    sum_j log(1 - x y_j) = log x + 2 pi i k .

Taking imaginary parts, sum_j arg(1 - x y_j) = phi + 2 pi k, so k is pinned by
BOUNDS: if the argument sum lies in (-pi, 2 pi) and phi in [0,pi), then k = 0.
That is arithmetic -- no continuity, no root tracking, no base point.

This probe measures what those bounds cost. The three facts G2-G4 replace
`hcont`, and they are real-algebraic statements on |x| = 1 of the same shape as
`xy_neg`, which this branch already proves by resultant elimination.

⚠ THE MARGINS ARE NOT GENEROUS, and that is the honest caveat: -1.4077 against
-pi/2 = -1.5708 is a 10% margin, and 1.3099 against pi/2 is 17%. The eliminations
will be tighter than xy_neg's was. Whether the trade is worth making is a
judgement; this probe supplies the numbers to make it on.

G6 records a route that FAILS, so it is not retried: Re(1 - x y_j) > 0 does NOT
hold on the arc -- it breaks near the endpoint, already at phi/pi = 0.9975.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import arg, conj, exp, fabs, log, mp, mpf, nstr, pi, polyroots, re
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


def main() -> int:
    set_compute_dps()
    N = 400
    gates = []

    # ---- G1: the argument sum IS phi -----------------------------------------
    worst1 = mpf(0)
    for i in range(0, N + 1):
        ph = pi * i / N
        x = exp(1j * ph)
        worst1 = max(worst1, fabs(sum(arg(1 - x * r) for r in roots_at(x)) - ph))
    gates.append({
        "gate": "G1",
        "claim": "sum_j arg(1 - x y_j) = phi EXACTLY along the whole arc, endpoint included. "
                 "Since the sum is congruent to phi mod 2 pi automatically (from the proved "
                 "Vieta product), this says the branch integer k is 0 -- which is what hcont is "
                 "used to establish",
        "n_points": N + 1, "worst": nstr(worst1, 10),
        "pass": bool(worst1 < mpf(10) ** -30),
    })

    # ---- G2, G3, G4: the three structural facts, with margins ---------------
    mn_arg = mpf(10) ** 9
    mx_second = -mpf(10) ** 9
    max_big = 0
    max_neg = 0
    for i in range(0, N):                      # OPEN arc [0, pi)
        ph = pi * i / N
        x = exp(1j * ph)
        ags = sorted((arg(1 - x * r) for r in roots_at(x)), reverse=True)
        mn_arg = min(mn_arg, ags[2])
        mx_second = max(mx_second, ags[1])
        max_big = max(max_big, sum(1 for a in ags if a > pi / 2))
        max_neg = max(max_neg, sum(1 for a in ags if a < 0))
    gates.append({
        "gate": "G2",
        "claim": "OBLIGATION 1 (replaces part of hcont): every arg(1 - x y_j) > -pi/2 on the "
                 "open arc. Measured minimum -1.4077 against -pi/2 = -1.5708 -- a 10% margin, "
                 "which is not generous",
        "min_arg": nstr(mn_arg, 12), "bound_minus_pi_over_2": nstr(-pi / 2, 12),
        "margin_fraction": nstr((mn_arg - (-pi / 2)) / (pi / 2), 8),
        "pass": bool(mn_arg > -pi / 2),
    })
    gates.append({
        "gate": "G3",
        "claim": "OBLIGATION 2: AT MOST ONE arg exceeds pi/2. Measured max count 1, and the "
                 "second-largest arg peaks at 1.3099 against pi/2 = 1.5708 -- a 17% margin. This "
                 "is what gives the upper bound sum < pi + pi/2 + pi/2 = 2 pi",
        "max_count_above_pi_over_2": max_big,
        "max_second_largest": nstr(mx_second, 12), "pi_over_2": nstr(pi / 2, 12),
        "margin_fraction": nstr((pi / 2 - mx_second) / (pi / 2), 8),
        "pass": bool(max_big <= 1 and mx_second < pi / 2),
    })
    gates.append({
        "gate": "G4",
        "claim": "OBLIGATION 3: at most TWO args are negative, i.e. at least one is >= 0. With "
                 "G2 this gives the lower bound sum > 2*(-pi/2) + 0 = -pi",
        "max_count_negative": max_neg, "pass": bool(max_neg <= 2),
    })

    # ---- G5: only ONE branch integer, not two -------------------------------
    worst5, at_end = mpf(0), None
    for i in range(0, N + 1):
        ph = pi * i / N
        x = exp(1j * ph)
        rs = roots_at(x)
        A = sum(log(1 - x * r) for r in rs)
        B = sum(log(1 - r / x) for r in rs)
        d = fabs(B - conj(A))
        if i < N:
            worst5 = max(worst5, d)
        else:
            at_end = d
    gates.append({
        "gate": "G5",
        "claim": "a structural simplification: on the OPEN arc the two log-sums are complex "
                 "CONJUGATES, because the roots are closed under conjugation (real cubic on "
                 "|x| = 1) and 1/x = conj x. Hence k_2 = -k_1 -- there is only ONE branch "
                 "integer, not two. It holds to 1e-40 on [0,pi) and also at the endpoint here, "
                 "though the argument for it breaks there since 1 - x y_1 sits on the cut",
        "max_on_open_arc": nstr(worst5, 10), "at_endpoint": nstr(at_end, 10),
        "pass": bool(worst5 < mpf(10) ** -30),
    })

    # ---- G6: a route that FAILS, recorded so it is not retried --------------
    worst6, at6 = -mpf(10) ** 9, None
    for i in range(0, N):
        ph = pi * i / N
        x = exp(1j * ph)
        for r in roots_at(x):
            v = re(x * r)
            if v > worst6:
                worst6, at6 = v, ph / pi
    gates.append({
        "gate": "G6",
        "claim": "RULED OUT, recorded so it is not retried: the tempting route 'Re(1 - x y_j) > 0 "
                 "on the arc, hence every |arg| < pi/2' is FALSE. max Re(x y_j) reaches 2.2468 "
                 "already at phi/pi = 0.9975, so Re(1 - x y_j) goes negative near the endpoint. "
                 "That is why G3 has to say 'at most one exceeds pi/2' rather than 'none does'",
        "max_Re_xy_on_open_arc": nstr(worst6, 12), "at_phi_over_pi": nstr(at6, 8),
        "min_Re_one_minus_xy": nstr(1 - worst6, 12),
        "route_fails": bool(worst6 > 1),
        "pass": bool(worst6 > 1),
    })

    out = {
        "probe": "qbeta_5two_route27_branch_by_argument",
        "bean": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoBranchByArgument.lean",
        "gates": gates,
        "verdict": {
            "the_trade": "hcont (continuity of the branch difference along the arc) is replaced "
                         "by three real-algebraic inequalities on |x| = 1 -- G2, G3, G4 -- of "
                         "the same shape as xy_neg, which this branch already proves by "
                         "resultant elimination. The arithmetic that turns those bounds into "
                         "k = 0 is Lean-proved (branchInt_eq_zero_of_arg_structure).",
            "what_it_costs": "the margins are not generous: -1.4077 vs -pi/2 is 10%, 1.3099 vs "
                             "pi/2 is 17%. The eliminations will be tighter than xy_neg's. "
                             "Whether the trade is worth making is a judgement, not a theorem.",
            "bonus": "G5: on the open arc the two log-sums are complex conjugates, so k_2 = -k_1 "
                     "and there is only ONE branch integer to pin, not two.",
            "ruled_out": "G6: Re(1 - x y_j) > 0 does NOT hold on the arc -- it fails near the "
                         "endpoint. Recorded so the route is not retried.",
            "still_open": "the three inequalities themselves. This probe does not prove them; it "
                          "measures them and prices the trade.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route27-branch-by-argument.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: hcont can be traded for three real-algebraic inequalities. Margins ~10-17%.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
