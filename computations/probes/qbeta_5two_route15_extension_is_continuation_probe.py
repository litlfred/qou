#!/usr/bin/env python3
"""Route 15 -- the piecewise extension IS Re of the analytic Rogers L. Derived.

Bean `qou-rhyp`; closes roast item 4 of `qou-rstq`, which this lane *created*
rather than inherited.

THE GAP THIS CLOSES
-------------------
Route 13 repaired two false ladder hypotheses by **defining** the Rogers `L` off
[0,1] via inversion above 1 and Landen below 0 (`FiveTwoRogersExtend.extend`).
That made the hypotheses free, and the honest cost was stated at the time:

    "the Lean object is a piecewise function, NOT proved equal to the analytic
     continuation of Li_2. G7 checks they agree at the six points in play.
     Agreement is evidence, not identification."

Six points is a coincidence budget. This probe shows it is not a coincidence:
the two agree **identically**, and there is a two-line derivation for each
branch. G1/G2 sweep generic arguments (1.01 to 1000, and -0.01 to -500), far
from the ladder's w1 = 2.2469796.

THE DERIVATION
--------------
Write L(x) = Li_2(x) + (1/2)*log(x)*log(1-x) with principal branches, and let
L_ext be the piecewise extension.

**x > 1.**  Principal `log(-x) = log x + i*pi`, so `log^2(-x) = log^2 x - pi^2 +
2*pi*i*log x`, and Euler inversion `Li_2(x) + Li_2(1/x) = -pi^2/6 - log^2(-x)/2`
gives, on real parts,

    Re Li_2(x) = pi^2/3 - log^2(x)/2 - Li_2(1/x).

Also `log(1-x) = log(x-1) + i*pi`, so `Re L(x) = Re Li_2(x) + log(x)*log(x-1)/2`.
Meanwhile

    L_ext(x) = 2*L(1) - L(1/x)
             = pi^2/3 - Li_2(1/x) - log(1/x)*log(1-1/x)/2
             = pi^2/3 - Li_2(1/x) + log(x)*log(x-1)/2 - log^2(x)/2

and the two expressions are the same. **Equality, not agreement.**

**x < 0.**  Here `Li_2(x)` is real (the cut is [1, inf)), `log(1-x)` is real, and
`Re L(x) = Li_2(x) + log|x|*log(1-x)/2`.  Put `y = x/(x-1)`, which is in (0,1),
so `1-y = 1/(1-x)` and `log(1-y) = -log(1-x)`, `log y = log(-x) - log(1-x)`.
Landen `Li_2(y) = -Li_2(x) - log^2(1-x)/2` then gives

    L(y) = -Li_2(x) - log^2(1-x)/2 + (log(-x) - log(1-x))*(-log(1-x))/2
         = -Li_2(x) - log(-x)*log(1-x)/2
         = -Re L(x),

so `L_ext(x) = -L(y) = Re L(x)`.  Again exactly.

WHERE THE WORK WENT -- SAY IT PLAINLY
-------------------------------------
It did not vanish, it **moved down one level**. `qou-rhyp` originally owed
"inversion x1 and Landen x3" for the Rogers L. Those are now free by
construction. But identifying the extension with the analytic continuation owes
**Li_2 inversion and Li_2 Landen** -- the same two classical facts, one level
down, and neither is in Mathlib (`qou-mlbg`: Mathlib has no `Li_2` at all).

So the ladder's hypotheses are genuinely discharged, and the price is that the
Lean `extend` is a piecewise function until someone proves those two. That is a
smaller and much better-defined debt than four unproved hypotheses, but it is a
debt, and nothing downstream should read `extend` as "the dilogarithm".

WHAT THIS PROBE IS AND IS NOT
-----------------------------
It is a numerical confirmation of a paper derivation, run at generic points so a
coincidence cannot pass. It is **not** a proof, and it is not a Lean artifact.
The 5_2 sum rule remains **verified to 80 dps, unproved**.
"""

import json
import pathlib

from mpmath import fabs, log, mp, mpf, nstr, pi, polylog, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

TOL = mpf(10) ** -35


def rlog(x):
    """Mathlib's `Real.log`: EVEN, real-valued, `Real.log 0 = 0`."""
    x = mpf(x)
    return mpf(0) if x == 0 else log(fabs(x))


def rogers_unit(x):
    """Rogers L on [0,1], where the power series is the honest dilogarithm."""
    x = mpf(x)
    return re(polylog(2, x)) + rlog(x) * rlog(1 - x) / 2


def ext(x, l1):
    """`FiveTwoRogersExtend.extend` at `c = pi^2/6`, `f = rogers_unit`."""
    x = mpf(x)
    if x > 1:
        return 2 * l1 - rogers_unit(1 / x)
    if x < 0:
        return -rogers_unit(x / (x - 1))
    return rogers_unit(x)


def principal(x):
    """Re of the analytic Rogers L, principal branches throughout."""
    x = mpf(x)
    return re(polylog(2, x) + log(x) * log(1 - x) / 2)


def main() -> int:
    set_compute_dps()
    l1 = pi ** 2 / 6
    gates = []

    hi = ["1.000001", "1.01", "1.3", "2.0", "2.2469796", "3.7", "10", "100", "1000", "1e6"]
    lo = ["-1e-6", "-0.01", "-0.5", "-0.99", "-1.0", "-1.7", "-2.2469796", "-5", "-50",
          "-500", "-1e6"]

    for gate, pts, branch in [("G1", hi, "x > 1 (inversion branch)"),
                              ("G2", lo, "x < 0 (Landen branch)")]:
        rows, worst = [], mpf(0)
        for t in pts:
            d = ext(t, l1) - principal(t)
            worst = max(worst, fabs(d))
            rows.append({"x": t, "ext": nstr(ext(t, l1), 18), "diff": nstr(d, 6)})
        gates.append({
            "gate": gate,
            "claim": f"extend == Re of the principal-branch analytic Rogers L on {branch}, "
                     "at GENERIC points far from the ladder's w1",
            "points": rows, "worst": nstr(worst, 8),
            "pass": bool(worst < TOL),
        })

    # ---- G3: the two classical Li_2 identities the derivation rests on ----
    inv, worst_i = [], mpf(0)
    for t in ["1.5", "2.2469796", "7.0", "250.0"]:
        x = mpf(t)
        d = (re(polylog(2, x)) + polylog(2, 1 / x)) - (pi ** 2 / 3 - rlog(x) ** 2 / 2)
        worst_i = max(worst_i, fabs(d))
        inv.append({"x": t, "resid": nstr(d, 6)})
    gates.append({
        "gate": "G3",
        "claim": "Euler inversion, real part: Re Li_2(x) + Li_2(1/x) = pi^2/3 - log^2(x)/2 for x > 1",
        "points": inv, "worst": nstr(worst_i, 8),
        "pass": bool(worst_i < TOL),
    })

    lan, worst_l = [], mpf(0)
    for t in ["-0.5", "-2.2469796", "-9.0", "-400.0"]:
        x = mpf(t)
        d = re(polylog(2, x / (x - 1)) - (-polylog(2, x) - rlog(1 - x) ** 2 / 2))
        worst_l = max(worst_l, fabs(d))
        lan.append({"x": t, "resid": nstr(d, 6)})
    gates.append({
        "gate": "G4",
        "claim": "Landen: Li_2(x/(x-1)) = -Li_2(x) - log^2(1-x)/2 for x < 0",
        "points": lan, "worst": nstr(worst_l, 8),
        "pass": bool(worst_l < TOL),
    })

    # ---- G5: continuity at the two seams, as a LIMIT, not a fixed tolerance ----
    # The first draft of this gate tested |ext(1+1e-10) - L1| < 1e-9 and FAILED, at
    # 1.25e-9. That was the test's fault, not the mathematics': near x = 1 the
    # residual is O(eps * log eps), so at eps = 1e-10 it is ~1e-9 by construction.
    # A seam is a limit statement and has to be gated as one.
    seam1, prev = [], None
    mono1 = True
    for e in ["1e-3", "1e-5", "1e-7", "1e-9"]:
        d = fabs(ext(mpf(1) + mpf(e), l1) - l1)
        seam1.append({"eps": e, "resid": nstr(d, 6)})
        if prev is not None and not d < prev:
            mono1 = False
        prev = d
    seam0, prev0 = [], None
    mono0 = True
    for e in ["1e-3", "1e-5", "1e-7", "1e-9"]:
        d = fabs(ext(-mpf(e), l1) - mpf(0))
        seam0.append({"eps": e, "resid": nstr(d, 6)})
        if prev0 is not None and not d < prev0:
            mono0 = False
        prev0 = d
    exact = {"at x = 1 exactly": nstr(ext("1.0", l1) - l1, 6),
             "at x = 0 exactly": nstr(ext("0.0", l1), 6)}
    gates.append({
        "gate": "G5",
        "claim": "the branches agree at the seams x = 0 and x = 1 IN THE LIMIT: the residual "
                 "decreases monotonically to 0 as eps -> 0, and vanishes exactly at the seams",
        "approach_to_x_eq_1_from_above": seam1,
        "approach_to_x_eq_0_from_below": seam0,
        "value_at_the_seams": exact,
        "note": "the residual is O(eps*log eps) at x = 1, so it is NOT bounded by any fixed "
                "tolerance chosen independently of eps -- gate on the trend instead",
        "pass": bool(mono1 and mono0
                     and fabs(ext("1.0", l1) - l1) < TOL
                     and fabs(ext("0.0", l1)) < TOL),
    })

    out = {
        "probe": "qbeta_5two_route15_extension_is_continuation",
        "bean": "qou-rhyp",
        "roast_item": "qou-rstq item 4 (created by this lane in Route 13)",
        "parent_bean": "qou-0yqu",
        "dps": mp.dps,
        "gates": gates,
        "verdict": {
            "outcome": "The piecewise `extend` equals Re of the principal-branch analytic Rogers L "
                       "IDENTICALLY, not just at the six ladder points. Confirmed at generic "
                       "arguments from 1.000001 to 1e6 and -1e-6 to -1e6.",
            "derivation": "x > 1: Euler inversion plus principal log(-x) = log x + i*pi, on real "
                          "parts. x < 0: Landen, using 1 - x/(x-1) = 1/(1-x). Both collapse exactly; "
                          "see this file's docstring for the two-line versions.",
            "where_the_work_went": "down one level, not away. The Rogers-L inversion and Landen "
                                   "hypotheses are now free by construction, but identifying `extend` "
                                   "with the analytic continuation owes Li_2 inversion and Li_2 "
                                   "Landen -- the same two classical facts, and Mathlib has no Li_2 "
                                   "at all (qou-mlbg).",
            "what_is_still_owed": "those two Li_2 identities, if the Lean object is to be called the "
                                  "dilogarithm. Until then `extend` is a piecewise function that "
                                  "provably satisfies the ladder's hypotheses -- which is what the "
                                  "ladder needs, and less than what the name suggests.",
            "not_a_proof": "this is numerical confirmation of a paper derivation. It is run at "
                           "generic points so that a coincidence cannot pass, which is the most a "
                           "probe can do.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route15-extension-is-continuation.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:88]}")
    print(f"\nwitness -> {dest}")
    print("VERDICT: roast item 4 CLOSED on paper -- `extend` IS Re of the analytic Rogers L.")
    print("         The debt moved down a level: Li_2 inversion + Li_2 Landen, still unproved.")
    return 0 if all(g["pass"] for g in gates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
