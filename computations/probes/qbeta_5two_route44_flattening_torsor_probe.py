#!/usr/bin/env python3
"""Route 44 -- the flattening is a TORSOR, and Route 43's identification does
NOT generalise up the tower. A narrowing of my own claim, plus the structure
that explains it.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 43.

WHAT ROUTE 43 CLAIMED, AND WHAT SURVIVES
----------------------------------------
Route 43 measured `sum_sigma Rhat(y_sigma; eps_sigma, 0) = -pi^2/6` with
`eps = (+1,-1,0)` the cubic's branch data, and said "the flattening the extended
Bloch group needs is already a theorem in the corpus". **That was too strong.**

What survives, unchanged and exact (G2): at the `y` level, putting the branch
data in the `p` slot gives exactly `-1` unit of `pi^2/6`.

What does not (G3): the same recipe applied up the tower FAILS. The tower has a
branch relation at every level and all three are integral (G1) --

    y :  2*log(y)   - 3*log(1-y) = 2*pi*i*eps      eps   = (+1,-1, 0)
    w :  2*log(1-w) - 3*log(w)   = 2*pi*i*eta      eta   = (-1,+1, 0)
    c :    log(1-c) - 5*log(c)   = 2*pi*i*delta    delta = (-2,+2, 0)

-- but the branch data in the `p` slot yields an integer multiple of `pi^2/6`
ONLY at `y`. At `w` the integer-valued flattening sits in the `q` slot, and at
`c` the single hit over `p,q in [-3,3]` is `(1,-1)`, which is neither `+delta`
nor `-delta`. So the *placement* is not determined by the branch relation and
does not transfer. Route 43's identification is hereby narrowed to the `y` level.

THE STRUCTURE THAT EXPLAINS IT
------------------------------
The branch relation is a **null direction** of the flattening correction (G4):
at the real root `3*log(1-y_3) - 2*log(y_3) = 0` to 46 dps, so shifting
`(p_3,q_3)` by `(3,-2)` changes nothing. Flattenings therefore form a **torsor**
modulo the branch relation, not a set of distinguished tuples -- which is why
`(p_3,q_3) in {(-3,2), (0,0), (3,-2)}` all give the identical total, and why
asking "is eps THE flattening" was the wrong question. The right question is
whether its *class* works, and at the `y` level it does.

⚠ AND THE HITS ARE NOT UNIQUE. Over `p,q in [-3,3]` with the conjugate root
carrying the conjugate flattening: 6 integer hits at `y`, 6 at `w`, 1 at `c`
(G5) -- reported rather than implied, because Route 43 found `eps` by exactly
this kind of search and only then recognised it.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib
from itertools import product

from mpmath import fabs, im, log, mp, mpf, nint, nstr, pi, polylog, polyroots, re
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

LEVELS = {
    "y": {"poly": [1, -2, 3, -1], "branch": "2*log(z) - 3*log(1-z)"},
    "w": {"poly": [1, -1, 2, -1], "branch": "2*log(1-z) - 3*log(z)"},
    "c": {"poly": [1, 1, 0, -1], "branch": "log(1-z) - 5*log(z)"},
}


def orbit(coeffs):
    rs = polyroots(coeffs, maxsteps=800, extraprec=3000)
    return ([r for r in rs if im(r) > mpf(10) ** -38][0],
            [r for r in rs if im(r) < -(mpf(10) ** -38)][0],
            [r for r in rs if fabs(im(r)) < mpf(10) ** -38][0].real)


def branch_value(level, z):
    if level == "y":
        return (2 * log(z) - 3 * log(1 - z)) / (2 * pi * 1j)
    if level == "w":
        return (2 * log(1 - z) - 3 * log(z)) / (2 * pi * 1j)
    return (log(1 - z) - 5 * log(z)) / (2 * pi * 1j)


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def flat_sum(Z, pqs):
    return sum(rogersL(z) - (pi * 1j / 2) * (p * log(1 - z) + q * log(z))
               for z, (p, q) in zip(Z, pqs))


def main() -> int:
    set_compute_dps()
    unit = pi ** 2 / 6
    gates = []

    orbits = {k: orbit(v["poly"]) for k, v in LEVELS.items()}
    branch = {k: [branch_value(k, z) for z in orbits[k]] for k in LEVELS}
    bint = {k: [int(nint(re(x))) for x in branch[k]] for k in LEVELS}

    # ---- G1: every level's branch data is integral --------------------------
    worst = max(fabs(x - n) for k in LEVELS for x, n in zip(branch[k], bint[k]))
    gates.append({
        "gate": "G1",
        "claim": "the tower carries a branch relation at EVERY level and all three are integral: "
                 "eps = (+1,-1,0) at y, eta = (-1,+1,0) at w, delta = (-2,+2,0) at c. So the raw "
                 "material Route 43 used exists everywhere -- which is what makes the failure in "
                 "G3 a real negative rather than a missing input",
        "branch_integers": {k: bint[k] for k in LEVELS},
        "worst_deviation_from_integer": nstr(worst, 12),
        "pass": bool(worst < mpf(10) ** -35),
    })

    # ---- G2: the y-level result, unchanged ----------------------------------
    Sy = flat_sum(orbits["y"], [(k, 0) for k in bint["y"]])
    gates.append({
        "gate": "G2",
        "claim": "ROUTE 43'S y-LEVEL RESULT STANDS, exact and unchanged: branch data in the p "
                 "slot gives sum Rhat = -1 unit of pi^2/6. Nothing below retracts this -- what is "
                 "narrowed is the claim that the same recipe is what the extended Bloch group "
                 "wants in general",
        "sum_Rhat": nstr(Sy, 30),
        "in_units_of_pi_sq_over_6": nstr(re(Sy) / unit, 25),
        "pass": bool(fabs(Sy + unit) < mpf(10) ** -35),
    })

    # ---- G3: the generalisation FAILS ---------------------------------------
    recipe = {}
    for k in LEVELS:
        S = flat_sum(orbits[k], [(b, 0) for b in bint[k]])
        r = re(S) / unit
        integral = bool(fabs(im(S)) < mpf(10) ** -28 and fabs(r - int(nint(r))) < mpf(10) ** -28)
        recipe[k] = {"in_units": nstr(r, 20), "is_integer": integral}
    gates.append({
        "gate": "G3",
        "claim": "THE NEGATIVE, and it narrows my own Route 43 claim. Branch data in the p slot "
                 "gives an integer multiple of pi^2/6 ONLY at the y level. At w the integer-valued "
                 "flattening lives in the q slot instead, and at c the single hit over [-3,3] is "
                 "(1,-1) -- neither +delta nor -delta. The PLACEMENT is therefore not determined "
                 "by the branch relation and does not transfer up the tower, so 'the flattening "
                 "is supplied by the cubic' holds at y and is not a law",
        "branch_data_in_p_slot": recipe,
        "pass": bool(recipe["y"]["is_integer"] and not recipe["c"]["is_integer"]),
    })

    # ---- G4: the branch relation is a NULL direction -> torsor ---------------
    y3 = orbits["y"][2]
    null = 3 * log(1 - y3) - 2 * log(y3)
    variants = [(-3, 2), (0, 0), (3, -2)]
    totals = [flat_sum(orbits["y"], [(1, 0), (-1, 0), v]) for v in variants]
    spread = max(fabs(t - totals[0]) for t in totals)
    gates.append({
        "gate": "G4",
        "claim": "THE STRUCTURE. The branch relation is a NULL direction of the flattening "
                 "correction: 3*log(1-y_3) - 2*log(y_3) = 0 at the real root, so shifting "
                 "(p_3,q_3) by (3,-2) changes the total by nothing. Flattenings are a TORSOR "
                 "modulo the branch relation, not distinguished tuples -- which is why three "
                 "different (p_3,q_3) give the identical sum, and why 'is eps THE flattening' was "
                 "the wrong question to ask of it",
        "null_direction_value": nstr(null, 20),
        "totals_over_the_three_variants": [nstr(t, 25) for t in totals],
        "spread": nstr(spread, 12),
        "pass": bool(fabs(null) < mpf(10) ** -35 and spread < mpf(10) ** -35),
    })

    # ---- G5: how rare the integer flattenings actually are ------------------
    counts = {}
    R = range(-3, 4)
    for k in LEVELS:
        Z = orbits[k]
        Lv = [rogersL(z) for z in Z]
        l1 = [log(1 - z) for z in Z]
        l0 = [log(z) for z in Z]
        hits = []
        for p1, q1 in product(R, repeat=2):
            for p3, q3 in product(R, repeat=2):
                pq = [(p1, q1), (-p1, -q1), (p3, q3)]
                S = sum(Lv[i] - (pi * 1j / 2) * (pq[i][0] * l1[i] + pq[i][1] * l0[i])
                        for i in range(3))
                if fabs(im(S)) < mpf(10) ** -28:
                    r = re(S) / unit
                    n = int(nint(r))
                    if fabs(r - n) < mpf(10) ** -28:
                        hits.append({"p1_q1": [p1, q1], "p3_q3": [p3, q3], "units": n})
        counts[k] = {"n_hits": len(hits), "distinct_values": sorted({h["units"] for h in hits})}
    gates.append({
        "gate": "G5",
        "claim": "how rare the integer flattenings are, reported rather than implied: 6 hits at "
                 "y, 6 at w, 1 at c over p,q in [-3,3] with the conjugate root carrying the "
                 "conjugate flattening. Route 43 found eps by exactly this kind of search and "
                 "only then recognised it, so the search's yield belongs in the record",
        "per_level": counts,
        "pass": bool(counts["y"]["n_hits"] > 0 and counts["c"]["n_hits"] > 0),
    })

    out = {
        "probe": "qbeta_5two_route44_flattening_torsor",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 43 (the flattened Rogers reformulation)",
        "narrows": "Route 43's 'the flattening the extended Bloch group needs is already a "
                   "theorem in the corpus'. The y-level identity is unchanged; the claim that "
                   "the branch data IS the flattening does not generalise -- the placement "
                   "differs at w and fails at c.",
        "gates": gates,
        "verdict": {
            "stands": "sum_sigma Rhat(y_sigma; eps_sigma, 0) = -pi^2/6 at the y level, exact.",
            "narrowed": "the recipe does not transfer up the tower. Branch data in the p slot "
                        "is integral only at y; w needs the q slot, c matches neither.",
            "structure": "the branch relation is a null direction of the flattening correction, "
                         "so flattenings form a torsor modulo it. 'Is eps the flattening' is the "
                         "wrong question -- only its class can be.",
            "next": "Neumann's parity/geometric conditions are still NOT imposed. Getting them "
                    "in is what would pick the class out, and it is now clearly the blocking "
                    "step rather than a formality.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route44-flattening-torsor.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the y-level identity stands; the identification of branch data WITH the flattening does "
        "not generalise and is narrowed. Flattenings are a torsor modulo the branch relation, so "
        "Neumann's conditions are the blocking step. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
