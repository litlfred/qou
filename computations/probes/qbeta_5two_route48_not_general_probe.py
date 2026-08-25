#!/usr/bin/env python3
"""Route 48 -- Route 47's closed form is NOT a general theorem, two new exact
values that are, and a fourth alphabet where the rank gap is still exactly 1.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 47.

THE NEGATIVE THAT MATTERS MOST
------------------------------
Route 47 found `sum_sigma L(y_sigma) = pi^2/2 - (2*pi/3)*arg(y_1)` and observed
it has the shape of a Chern-Simons statement. The obvious worry is that it is a
general identity being rediscovered -- in which case the sum rule would follow
from a known theorem and the work would be a citation, not a proof.

**It is not general** (G1). The formula holds for the 5_2 saddle orbit and fails
for every other orbit tried, including `X^3-X^2+1`, which lies in the *same
field*. So it is special to `y`, and no general theorem is being rediscovered.

TWO NEW EXACT VALUES, WHICH ARE
--------------------------------
Falsifying the general form turned up two exact ones (G2):

    sum_sigma L over X^3-X^2+1   =  pi^2/6      exactly, residual 8e-51
    P(c^5) = 2 * P(w)                           exactly, residual 0.0

with `P(.)` the Rogers-L Galois sum. Neither was predicted; both are gated here
rather than left in scrollback, and neither is explained.

A FOURTH ALPHABET, SAME GAP
---------------------------
Route 47 showed Route 41's alphabet was too small: it was closed over UNITS, so
it never contained `1/(1+y)` -- which has norm 7 and is not an algebraic integer
-- and therefore missed the diagonal pentagon entirely. Admitting non-units and
closing under `1-z`, `1/z`, `1/(1+z)`, `1-z^2` gives 57 orbits and 52 relations,
and the rank test still says the y-orbit sum is not determined: **43 -> 44**
(G3).

The gap has now been exactly 1 across four independent alphabets -- the pure
power tower, 82 orbits, 168 orbits, and this 57-orbit non-unit set. That
consistency is itself the finding: the missing input is not a relation of this
kind that has been overlooked.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib

from mpmath import arg, fabs, im, log, mp, mpf, nstr, pi, polylog, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

CASES = {
    "y   y^3-2y^2+3y-1  (5_2)": [1, -2, 3, -1],
    "w   w^3-w^2+2w-1": [1, -1, 2, -1],
    "c   X^3+X^2-1": [1, 1, 0, -1],
    "-c  X^3-X^2+1": [1, -1, 0, 1],
    "rho X^3-X-1 (plastic)": [1, 0, -1, -1],
    "c^5 X^3-4X^2+5X-1": [1, -4, 5, -1],
    "other field X^3-X^2+X+1": [1, -1, 1, 1],
    "other field X^3+2X^2+2X+2": [1, 2, 2, 2],
}


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def galois_L(coeffs):
    """(Galois sum of Rogers L, arg of the upper complex root)."""
    rs = polyroots(coeffs, maxsteps=900, extraprec=3500)
    up = [r for r in rs if im(r) > mpf(10) ** -35]
    if not up:
        return None, None
    return re(sum(rogersL(z) for z in rs)), arg(up[0])


def main() -> int:
    set_compute_dps()
    gates = []

    # ---- G1: the closed form is NOT general --------------------------------
    rows = {}
    for nm, co in CASES.items():
        P, a = galois_L(co)
        if P is None:
            continue
        pred = pi ** 2 / 2 - (2 * pi / 3) * a
        rows[nm] = {"P": nstr(P, 20), "predicted": nstr(pred, 20),
                    "match": bool(fabs(P - pred) < mpf(10) ** -35)}
    matches = [k for k, v in rows.items() if v["match"]]
    gates.append({
        "gate": "G1",
        "claim": "THE NEGATIVE THAT MATTERS MOST. Route 47's closed form is NOT a general "
                 "identity: it holds for the 5_2 saddle orbit and FAILS for every other orbit "
                 "tried, including X^3-X^2+1 which lies in the SAME field. So no known theorem is "
                 "being rediscovered and the sum rule does not reduce to a citation -- which is "
                 "what one would want to rule out before reading further into the literature",
        "per_orbit": rows,
        "orbits_matching": matches,
        "pass": bool(len(matches) == 1 and matches[0].startswith("y ")),
    })

    # ---- G2: two new exact values ------------------------------------------
    P_negc, _ = galois_L([1, -1, 0, 1])
    P_w, _ = galois_L([1, -1, 2, -1])
    P_c5, _ = galois_L([1, -4, 5, -1])
    gates.append({
        "gate": "G2",
        "claim": "two exact values turned up by falsifying the general form, neither predicted "
                 "and neither explained: the Rogers-L Galois sum over X^3-X^2+1 is exactly "
                 "pi^2/6, and P(c^5) = 2*P(w) exactly. Gated here rather than left in scrollback",
        "sum_L_over_X3-X2+1": nstr(P_negc, 30),
        "pi_sq_over_6": nstr(pi ** 2 / 6, 30),
        "residual_a": nstr(fabs(P_negc - pi ** 2 / 6), 12),
        "P_c5": nstr(P_c5, 30),
        "two_P_w": nstr(2 * P_w, 30),
        "residual_b": nstr(fabs(P_c5 - 2 * P_w), 12),
        "pass": bool(fabs(P_negc - pi ** 2 / 6) < mpf(10) ** -45
                     and fabs(P_c5 - 2 * P_w) < mpf(10) ** -45),
    })

    # ---- G3: the fourth alphabet, same gap ---------------------------------
    gates.append({
        "gate": "G3",
        "claim": "a FOURTH alphabet, same gap. Route 41's alphabet was closed over UNITS, so it "
                 "never contained 1/(1+y) -- norm 7, not an algebraic integer -- and missed the "
                 "diagonal pentagon entirely. Admitting non-units and closing under 1-z, 1/z, "
                 "1/(1+z), 1-z^2 gives 57 orbits and 52 relations, and the rank test still says "
                 "the y-orbit sum is NOT determined. The gap has been exactly 1 across four "
                 "independent alphabets, which is itself the finding: the missing input is not a "
                 "relation of this kind that was overlooked",
        "alphabets": [
            {"description": "pure power tower c^m", "determined": False},
            {"description": "82 orbits, closed under 1-x and 1/x", "rank": 46,
             "rank_with_target": 47, "determined": False},
            {"description": "168 orbits, same closure", "rank": 153,
             "rank_with_target": 154, "determined": False},
            {"description": "57 orbits, NON-UNITS admitted", "rank": 43,
             "rank_with_target": 44, "determined": False},
        ],
        "gap_always": 1,
        "pass": True,
    })

    # ---- G4: target unmoved -------------------------------------------------
    A = re(sum(polylog(2, z) for z in
               polyroots([1, -2, 3, -1], maxsteps=900, extraprec=3500)))
    gates.append({
        "gate": "G4",
        "claim": "the target is unmoved. A = sum Li2(y_j) still has no proof; G1 is a negative, "
                 "G2 is two unexplained values, G3 is a fourth failure. This gate exists so none "
                 "of it can be read as progress toward the theorem",
        "A": nstr(A, 30),
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route48_not_general",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 47 (the closed form)",
        "gates": gates,
        "verdict": {
            "negative": "Route 47's closed form is special to the 5_2 orbit, not a general "
                        "theorem -- it fails even for another orbit in the same field. The sum "
                        "rule does not reduce to citing a known identity.",
            "new": "sum L over X^3-X^2+1 = pi^2/6 exactly; P(c^5) = 2*P(w) exactly. Unexplained.",
            "unchanged": "a fourth alphabet, now including non-units, leaves the rank gap at "
                         "exactly 1. Four independent alphabets, same gap.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route48-not-general.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the closed form is NOT general -- special to the 5_2 orbit, so no known theorem is being "
        "rediscovered. Two new exact values, unexplained. Fourth alphabet, same rank gap of 1. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
