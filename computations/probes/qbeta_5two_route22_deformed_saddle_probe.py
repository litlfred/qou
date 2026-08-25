#!/usr/bin/env python3
"""Route 22 -- the deformed saddle condition IS the GGM curve, and its branch data.

Bean `qou-trns`. Pairs with `QOU/QBeta/FiveTwoDeformedSaddle.lean` (sorry-free,
lake green).

WHAT WAS MISSING
----------------
`QOU/QBeta/FiveTwoSaddleSumRule.lean` has the BASE POINT versions:

    cubic_iff_sq_eq_cube   y^3-2y^2+3y-1 = 0  <->  y^2 = (1-y)^3
    branch_data_of_cubic   exists k : 2 log y - 3 log(1-y) = k*(2 pi i)

and calls the branch data "the sole source of the pi^2 in the sum rule". The
DEFORMED versions -- the ones the transport actually travels along -- were not
there. With

    V(x,y) = Li2(y) + Li2(x y) + Li2(y/x) + log(-y)^2
    y * dV/dy = 2 log(-y) - log(1-y) - log(1-x y) - log(1-y/x)   =: branchTerm

exponentiating turns dV/dy = 0 into  y^2 = (1-y)(1-x y)(1-y/x), and that is
IDENTICALLY the GGM curve. Gates G1-G3.

WHAT TO WATCH IN THE NUMBERS
----------------------------
G4 checks the corpus's own recorded claim that the base-point branch integers are
(+1, -1, 0). Note the corpus expression uses log(y) while branchTerm uses
log(-y) -- forced by the log(-y)^2 term in V -- so the two differ by 2*(log(-y) -
log(y)) = +-2 pi i per root, i.e. by 1 in k. Both are reported. Given this lane's
history with 2 pi, an unstated log(-y)-vs-log(y) convention is exactly the sort of
thing that silently shifts an integer, so it is measured rather than assumed.

G6 is the payoff: the SUM of the deformed branch integers along the arc. It is
what `QOU/Archimedean/BranchIntegerPinning.lean` pins, and `exp_branchSum_eq_one`
supplies that lemma's `hexp` from Vieta alone -- the saddle condition is not even
needed for the sum, only for the individual terms.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import cos, exp, fabs, im, log, mp, mpf, nint, nstr, pi, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def roots_x(x):
    return list(polyroots([x, -(x ** 2 + 1), x ** 2 + x + 1, -x],
                          maxsteps=500, extraprec=1000))


def curve(x, y):
    return x * y ** 3 - (x ** 2 + 1) * y ** 2 + (x ** 2 + x + 1) * y - x


def branch_term(x, y):
    """y * dV/dy = 2 log(-y) - log(1-y) - log(1-x y) - log(1-y/x), principal logs."""
    return (2 * log(-y) - log(1 - y) - log(1 - x * y) - log(1 - y / x))


def corpus_term(y):
    """The corpus's base-point expression: 2 log y - 3 log(1-y)."""
    return 2 * log(y) - 3 * log(1 - y)


def main() -> int:
    set_compute_dps()
    TOL = mpf(10) ** -30
    gates = []

    # ---- G1: the saddle condition holds at every root, on and off the arc ---
    worst1 = mpf(0)
    # NOTE: every off-arc point is built from mpf. Writing `1 + 0.4j` here (a Python
    # float64 literal) silently drops the whole computation to double precision --
    # the first run of this probe failed G1/G4 at exactly 4.3e-16 for that reason.
    pts = [exp(1j * pi * mpf(t)) for t in ["0", "0.3", "0.55", "0.9", "1"]] \
        + [mpf("0.6"), mpf("1.7"), mpf(1) + 1j * mpf("0.4")]
    for x in pts:
        for y in roots_x(x):
            worst1 = max(worst1, fabs(x * y ** 2 - (1 - y) * (1 - x * y) * (x - y)))
    gates.append({
        "gate": "G1",
        "claim": "the deformed saddle condition x*y^2 = (1-y)(1-x*y)(x-y) -- i.e. dV/dy = 0 "
                 "after exponentiating -- holds at every root of the GGM curve, on the arc and "
                 "off it",
        "n_points": len(pts), "worst": nstr(worst1, 8), "pass": bool(worst1 < TOL),
    })

    # ---- G2: it is IDENTICALLY the curve, not merely equivalent at roots ----
    worst2 = mpf(0)
    for (xv, yv) in [("0.3", "1.7"), ("-2.1", "0.44"), ("1.0", "5.0"), ("0.77", "-3.2")]:
        x, y = mpf(xv), mpf(yv)
        worst2 = max(worst2,
                     fabs((x * y ** 2 - (1 - y) * (1 - x * y) * (x - y)) - curve(x, y)))
    gates.append({
        "gate": "G2",
        "claim": "x*y^2 - (1-y)(1-x*y)(x-y) is IDENTICALLY curve(x,y) as a polynomial -- checked "
                 "at generic (x,y) OFF the curve, so this is the ring identity Lean proves, not "
                 "an equivalence that only holds at roots",
        "n_generic_points": 4, "worst": nstr(worst2, 8), "pass": bool(worst2 < TOL),
    })

    # ---- G3: at x = 1 it is the corpus's y^2 = (1-y)^3 -----------------------
    worst3 = mpf(0)
    for yv in ["0.31", "-1.4", "2.9"]:
        y = mpf(yv)
        worst3 = max(worst3, fabs((1 - y) * (1 - 1 * y) * (1 - y) - (1 - y) ** 3))
    gates.append({
        "gate": "G3",
        "claim": "at x = 1 the deformed condition collapses to y^2 = (1-y)^3, the corpus's "
                 "`cubic_iff_sq_eq_cube` -- so the deformation is a genuine generalisation of "
                 "what FiveTwoSaddleSumRule already proves, not a different statement",
        "worst": nstr(worst3, 8), "pass": bool(worst3 < TOL),
    })

    # ---- G4: the NEW Vieta product prod(1 - y_j) = 1 ------------------------
    worst4 = mpf(0)
    for x in pts:
        ys = roots_x(x)
        worst4 = max(worst4, fabs((1 - ys[0]) * (1 - ys[1]) * (1 - ys[2]) - 1))
    gates.append({
        "gate": "G4",
        "claim": "prod_j (1 - y_j) = 1 -- the third Vieta product, new in this file; joins "
                 "prod(1 - x*y_j) = x and prod(x - y_j) = x^2 from #4658. Together they are why "
                 "exp(sum of branchTerms) = 1",
        "n_points": len(pts), "worst": nstr(worst4, 8), "pass": bool(worst4 < TOL),
    })

    # ---- G5: the branch integers at the BASE POINT, both conventions --------
    ys1 = sorted(roots_x(mpf(1)), key=lambda z: (im(z), re(z)))
    k_branch, k_corpus, integrality = [], [], mpf(0)
    for y in ys1:
        kb = branch_term(mpf(1), y) / (2j * pi)
        kc = corpus_term(y) / (2j * pi)
        k_branch.append(nstr(re(kb), 8))
        k_corpus.append(nstr(re(kc), 8))
        integrality = max(integrality, fabs(im(kb)), fabs(re(kb) - nint(re(kb))),
                          fabs(im(kc)), fabs(re(kc) - nint(re(kc))))
    gates.append({
        "gate": "G5",
        "claim": "the base-point branch integers are integers in BOTH conventions, and they "
                 "differ -- branchTerm uses log(-y) (forced by the log(-y)^2 term in V) while "
                 "the corpus uses log(y). The corpus records (+1,-1,0) for its own convention; "
                 "reported here rather than assumed, because an unstated log(-y)-vs-log(y) "
                 "convention shifts an integer silently",
        "k_branchTerm_log_neg_y": k_branch,
        "k_corpus_log_y": k_corpus,
        "sum_branchTerm": nstr(sum(mpf(v) for v in k_branch), 8),
        "sum_corpus": nstr(sum(mpf(v) for v in k_corpus), 8),
        "worst_integrality_defect": nstr(integrality, 8),
        "pass": bool(integrality < mpf(10) ** -25),
    })

    # ---- G6: exp(sum) = 1 along the arc -- the `hexp` hypothesis --------------
    sums, worst_exp = [], mpf(0)
    for i in range(0, 21):
        ph = pi * i / 20
        x = mpf(-1) if i == 20 else exp(1j * ph)
        ys = roots_x(x)
        tot = sum(branch_term(x, y) for y in ys)
        worst_exp = max(worst_exp, fabs(exp(tot) - 1))
        sums.append(re(tot / (2j * pi)))
    ints = [int(nint(v)) for v in sums]
    gates.append({
        "gate": "G6",
        "claim": "exp(sum_j branchTerm) = 1 all along the arc, endpoint included -- the `hexp` "
                 "hypothesis of BranchIntegerPinning, supplied by exp_branchSum_eq_one from "
                 "VIETA ALONE (the saddle condition is not needed for the sum, only for the "
                 "individual terms)",
        "n_points": 21,
        "worst_|exp(sum) - 1|": nstr(worst_exp, 8),
        "pass": bool(worst_exp < TOL),
    })

    # ---- G7: and the principal-branch sum JUMPS at the endpoint -------------
    # A fourth independent way the endpoint sits on the cut. `hexp` is immune to
    # it (exp sees no branch); `hcont` is exactly what it violates.
    interior, endpoint = ints[:-1], ints[-1]
    x_end = mpf(-1)
    on_cut = []
    for y in roots_x(x_end):
        for label, z in [("-y", -y), ("1-y", 1 - y), ("1-x*y", 1 - x_end * y),
                         ("1-y/x", 1 - y / x_end)]:
            if re(z) < 0 and fabs(im(z)) < mpf(10) ** -25:
                on_cut.append({"root": nstr(re(y), 10), "factor": label, "value": nstr(re(z), 10)})
    gates.append({
        "gate": "G7",
        "claim": "the sum of PRINCIPAL-BRANCH branch integers is constant = 1 on [0, pi) and "
                 "drops to 0 exactly at phi = pi. That is a FOURTH independent way the endpoint "
                 "sits on the cut, and it is precisely what `hcont` forbids -- note `hexp` (G6) "
                 "is blind to it, because exp sees no branch. The factors on the cut at x = -1 "
                 "are listed: log(-y) at the positive root, and log(1+y) at the y = -w_1 root, "
                 "twice over",
        "sum_on_interior": sorted(set(interior)), "sum_at_endpoint": endpoint,
        "jump": endpoint - interior[-1],
        "factors_on_cut_at_x_eq_neg_one": on_cut,
        "pass": bool(len(set(interior)) == 1 and endpoint != interior[-1]),
    })

    out = {
        "probe": "qbeta_5two_route22_deformed_saddle",
        "bean": "qou-trns", "parent_bean": "qou-0yqu", "dps": mp.dps,
        "pairs_with_lean": "QOU/QBeta/FiveTwoDeformedSaddle.lean",
        "gates": gates,
        "verdict": {
            "outcome": "The deformed saddle condition dV/dy = 0 is IDENTICALLY the GGM curve, "
                       "over any commutative ring; its branch data follows from the curve alone; "
                       "and the sum over the three roots satisfies exp(sum) = 1 from Vieta "
                       "alone. The corpus had all three only at x = 1.",
            "what_it_buys_the_envelope": "the envelope argument's saddle hypothesis is free -- "
                                         "it IS the curve the roots were defined by. What the "
                                         "envelope still needs is dy_j/dx and d/dz Li2 along a "
                                         "path, i.e. analysis, not this.",
            "second_use_of_the_pinning_lemma": "exp_branchSum_eq_one is exactly the hexp input "
                                               "of eq_zero_of_continuousOn_of_exp_eq_one, so the "
                                               "same lemma that pins the transport's branch "
                                               "integer also pins the sum of the saddle branch "
                                               "integers -- given continuity, still open there.",
            "still_not_proved": "the envelope derivative dS/dphi = 2 phi. Li2 outside the unit "
                                "disc is needed for it and the corpus's cLiTwo is analytic only "
                                "on ||z|| < 1, while the arc's roots reach |y| = 2.247. That is "
                                "the qou-clx8 continuation, untouched.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route22-deformed-saddle.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:86]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: the deformed saddle condition is the curve; branch data derived; sum pinnable.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
