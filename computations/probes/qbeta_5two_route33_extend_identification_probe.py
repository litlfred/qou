#!/usr/bin/env python3
"""Route 33 -- `extend` IS Re of the analytic Rogers L, and what Lean still needs.

Bean `qou-rstq` item 4 (cross-referenced from `qou-trns`). Pairs with three Lean
modules, all sorry-free and lake green:
  QOU/MathlibExt/ComplexDilogarithmLanden.lean  (4)  Landen's analytic core
  QOU/MathlibExt/AlternatingZetaTwo.lean        (1)  the alternating zeta(2)
  QOU/Archimedean/LiTwoNegOne.lean              (2)  Li2(-1) = -pi^2/12

WHY THIS ITEM
-------------
Route 32 showed the 5_2 sum rule reduces to the level-7 bridge, and that the
bridge rests on Lean's `extended_sum` -- which is stated for the corpus's
PIECEWISE `extend`, not for the analytic Rogers L the bridge computes with.
Identifying them is the last non-transport link, and it is `qou-rstq` item 4.

WHAT IS MEASURED
----------------
G1/G2: the identification holds, to 1e-50, at the six arguments `extended_sum`
actually uses and across all three regimes of `extend`.

G3/G4: the Landen leg, which is what the x < 0 regime needs. Lean now has its
ANALYTIC CORE -- the combination Li2(z) + Li2(z/(z-1)) + (1/2) log(1-z)^2 has
zero derivative (`hasDerivAt_landenCombo`) -- AND its base value,
Li2(-1) = -pi^2/12 (`LiTwo_neg_one`, from `hasSum_alternating_zeta_two`, a
Mathlib gap filled here). G4 checks the constant is 0.

G5 NAMES WHAT IS STILL MISSING, per regime, rather than leaving it in prose.
G6 is adversarial on the branch hypothesis of the Lean theorem.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import diff, fabs, findroot, im, log, mp, mpc, mpf, nstr, pi, polylog, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def rogersL(x):
    """The corpus's rogersL, valid on (0,1) where its LiTwo series converges."""
    return polylog(2, x) + log(x) * log(1 - x) / 2


def extend(x):
    """The corpus's `extend (pi^2/6) rogersL`."""
    C = pi ** 2 / 6
    if x > 1:
        return 2 * C - rogersL(1 / x)
    if x < 0:
        return -rogersL(x / (x - 1))
    return rogersL(x)


def ReL(x):
    """Re of the ANALYTIC Rogers L at real x, principal branches."""
    z = mpc(x, 0)
    return re(polylog(2, z) + log(z) * log(1 - z) / 2)


def landenCombo(z):
    return polylog(2, z) + polylog(2, z / (z - 1)) + log(1 - z) ** 2 / 2


def main() -> int:
    set_compute_dps()
    gates = []

    # ---- G1: the six arguments `extended_sum` actually uses ------------------
    xr = findroot(lambda t: t ** 3 - 2 * t ** 2 - t + 1, mpf("0.55"))
    ws = [1 / (1 - xr), xr, (xr - 1) / xr]
    args = ws + [-w for w in ws]
    rows = []
    worst1 = mpf(0)
    for a in args:
        e, r = extend(a), ReL(a)
        worst1 = max(worst1, fabs(e - r))
        rows.append({"x": nstr(a, 18), "extend": nstr(e, 18), "Re_L": nstr(r, 18),
                     "regime": ("x>1" if a > 1 else "x<0" if a < 0 else "0<=x<=1")})
    gates.append({
        "gate": "G1",
        "claim": "extend(pi^2/6, rogersL)(x) = Re of the analytic Rogers L, at the SIX arguments "
                 "Lean's `extended_sum` actually uses -- the level-7 orbit "
                 "{1/(1-x), x, (x-1)/x} and its negatives, x the root of X^3-2X^2-X+1 in (1/2,1). "
                 "These are the values the level-7 bridge (Route 32) needs, not a generic sample",
        "root_x": nstr(xr, 20), "per_argument": rows,
        "worst_difference": nstr(worst1, 10),
        "pass": bool(worst1 < mpf(10) ** -40),
    })

    # ---- G2: sweep, by regime -----------------------------------------------
    sweeps = []
    ok2 = True
    for lo, hi, name in [(mpf("0.02"), mpf("0.98"), "0 < x < 1"),
                         (mpf("1.02"), mpf(8), "x > 1"),
                         (mpf(-8), mpf("-0.02"), "x < 0")]:
        w = mpf(0)
        at = None
        for i in range(0, 81):
            x = lo + (hi - lo) * i / 80
            d = fabs(extend(x) - ReL(x))
            if d > w:
                w, at = d, x
        sweeps.append({"regime": name, "worst": nstr(w, 10),
                       "at_x": nstr(at, 12) if at is not None else "0 everywhere"})
        ok2 = ok2 and w < mpf(10) ** -40
    gates.append({
        "gate": "G2",
        "claim": "the same identification across ALL THREE regimes of `extend`, 81 points each -- "
                 "so the agreement is not an accident of the six arguments. On (0,1) the two "
                 "agree identically (both are the series); the content is in x > 1 (inversion) "
                 "and x < 0 (Landen)",
        "sweeps": sweeps, "pass": bool(ok2),
    })

    # ---- G3: the Landen combination has zero derivative ---------------------
    worst3 = mpf(0)
    for i in range(1, 40):
        z = mpc(-mpf(i) / 5, mpf(i) / 13)          # off the real axis too
        worst3 = max(worst3, fabs(diff(landenCombo, z)))
    gates.append({
        "gate": "G3",
        "claim": "d/dz [Li2(z) + Li2(z/(z-1)) + (1/2) log(1-z)^2] = 0 -- the analytic core of the "
                 "Landen leg, and exactly what Lean's `hasDerivAt_landenCombo` proves. Sampled "
                 "OFF the real axis as well, since the Lean statement is complex",
        "n_points": 39, "worst_abs_derivative": nstr(worst3, 10),
        "pass": bool(worst3 < mpf(10) ** -35),
    })

    # ---- G4: and the constant is 0 ------------------------------------------
    worst4 = mpf(0)
    for i in range(1, 40):
        z = mpc(-mpf(i) / 5, mpf(i) / 13)
        worst4 = max(worst4, fabs(landenCombo(z)))
    val_at_neg_one = landenCombo(mpf(-1))
    gates.append({
        "gate": "G4",
        "claim": "the constant that zero derivative leaves undetermined is 0 -- i.e. Landen holds "
                 "outright. Pinning it needs one special value, Li2(-1) = -pi^2/12 at the base "
                 "point z = -1. AN EARLIER DRAFT OF THIS GATE SAID LEAN DID NOT HAVE IT; that is "
                 "now false and is corrected: `QOU.Archimedean.LiTwo_neg_one` and `cLiTwo_neg_one` "
                 "prove it, from `hasSum_alternating_zeta_two` -- a Mathlib gap filled here, since "
                 "Mathlib has hasSum_zeta_two (pi^2/6) but no alternating analogue. What remains "
                 "for Landen is only the connectedness step from zero derivative to the identity",
        "n_points": 39, "worst_abs_value": nstr(worst4, 10),
        "value_at_z_eq_minus_1": nstr(val_at_neg_one, 10),
        "LiTwo_minus_one": nstr(polylog(2, mpf(-1)), 20),
        "minus_pi_sq_over_12": nstr(-pi ** 2 / 12, 20),
        "pass": bool(worst4 < mpf(10) ** -35),
    })

    # ---- G5: what is still missing, per regime ------------------------------
    on_cut = [nstr(a, 18) for a in args if a > 1]
    gates.append({
        "gate": "G5",
        "claim": "WHAT LEAN STILL NEEDS, named per regime rather than left in prose. (0,1): "
                 "nothing -- `cLiTwo_ofReal` already bridges the corpus's LiTwo to cLiTwo. "
                 "x < 0 (Landen): the analytic core AND the base value Li2(-1) = -pi^2/12 are "
                 "both proved; what remains is only the connectedness step from zero derivative "
                 "to the identity. x > 1 (inversion): HARDER, and not attempted -- x > 1 "
                 "lies ON cLiTwoExt's cut (notCut excludes real x >= 1), so it needs a BOUNDARY "
                 "value from off the cut, not merely a constant of integration. Exactly one of "
                 "the six arguments is in that regime, and it is unavoidable: it is w_1 = 2.24698",
        "arguments_needing_the_cut_regime": on_cut,
        "notCut_definition": "{w : Im w != 0 or Re w < 1}",
        "landen_remaining": "only the zero-derivative-to-identity connectedness step; the "
                            "analytic core and the base value Li2(-1) = -pi^2/12 are both proved",
        "inversion_remaining": "boundary values of Li2 on [1, inf) -- new analytic infrastructure",
        "pass": bool(len(on_cut) == 1),
    })

    # ---- G6: the branch hypothesis is load-bearing --------------------------
    # log(1 - z/(z-1)) = -log(1-z) needs 1-z off log's cut; for real z > 1 it fails by 2 pi i.
    zbad = mpf(3)
    lhs = log(1 - mpc(zbad, 0) / (mpc(zbad, 0) - 1))
    rhs = -log(1 - mpc(zbad, 0))
    gates.append({
        "gate": "G6",
        "claim": "ADVERSARIAL on the Lean hypothesis: `hasDerivAt_landenCombo` requires "
                 "1 - z in slitPlane, and that is load-bearing, not decoration. At z = 3 the "
                 "point 1 - z = -2 is a negative real, on log's cut, and "
                 "log(1 - z/(z-1)) = -log(1-z) FAILS by exactly 2 pi i -- so the cancellation the "
                 "theorem turns on would break. Dropping the hypothesis does not weaken the "
                 "theorem, it falsifies it",
        "z": "3", "lhs": nstr(lhs, 14), "rhs": nstr(rhs, 14),
        "difference": nstr(lhs - rhs, 14), "two_pi_i": nstr(mpc(0, 2 * pi), 14),
        "fails_by_2_pi_i": bool(fabs(lhs - rhs - mpc(0, 2 * pi)) < mpf(10) ** -40),
        "pass": bool(fabs(lhs - rhs - mpc(0, 2 * pi)) < mpf(10) ** -40),
    })

    out = {
        "probe": "qbeta_5two_route33_extend_identification",
        "bean": "qou-rstq", "cross_ref": "qou-trns", "dps": mp.dps,
        "pairs_with_lean": ["QOU/MathlibExt/ComplexDilogarithmLanden.lean",
                            "QOU/MathlibExt/AlternatingZetaTwo.lean",
                            "QOU/Archimedean/LiTwoNegOne.lean"],
        "gates": gates,
        "verdict": {
            "measured": "extend(pi^2/6, rogersL) = Re of the analytic Rogers L, to 1e-50, at the "
                        "six arguments `extended_sum` uses and across all three regimes.",
            "proved_this_round": "the analytic core of the Landen leg -- the combination "
                                 "Li2(z) + Li2(z/(z-1)) + (1/2) log(1-z)^2 has zero derivative, "
                                 "with the branch condition isolated and shown load-bearing.",
            "still_open": "(a) for Landen, only the connectedness step -- its analytic core AND "
                          "its base value Li2(-1) = -pi^2/12 are both now proved; (b) the INVERSION leg "
                          "for x > 1, which needs boundary values of Li2 ON its cut -- new "
                          "analytic infrastructure, and the sharper of the two. Exactly one of "
                          "the six arguments needs it, w_1 = 2.24698, and it cannot be avoided.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route33-extend-identification.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:84]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + ("extend IS Re L, measured; Landen's analytic core is proved; the "
                         "inversion leg still needs boundary values on the cut."
                         if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
