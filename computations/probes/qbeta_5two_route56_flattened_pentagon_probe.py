#!/usr/bin/env python3
"""Route 56 -- flattening removes the two-variable failure: Neumann's pentagon,
measured.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 54,
which proved the complex five-term identity when ONE variable is real and
measured it failing when both are complex. This probe measures what replaces it.

THE MOVE
--------
The identity needs `log a_3 = log(1-x) - log(1-xy)` and four companions. Those
are branch conditions and they DO fail. But nothing forces the use of `log a_3`:
carry the EXPANSION as the logarithm instead. With

    flatRogers(z, L, L') = Li_2(z) + L*L'/2 + (log(1-z) - L')*log z

the derivative is `rogersDeriv(z, L, L') * z'` exactly -- the `log z` factor's
contribution cancels against the `L'` one -- so the flattened pentagon sum has
vanishing derivative under regularity ALONE, with no branch hypothesis anywhere.
That is `QOU/QBeta/FiveTwoFlattenedPentagon.lean`, sorry-free.

Equivalently, with `d = log z - L` and `d' = log(1-z) - L'`,

    flatRogers = L(z) + d'*log(z)/2 - d*log(1-z)/2 + d*d'/2

and writing `d = 2 pi i p`, `d' = 2 pi i q` this is Neumann's `R(z;p,q)` up to
normalisation. So what is measured below is the pentagon in `Bhat(C)`.

WHAT IS MEASURED
----------------
G1 -- at every two-variable point where Route 54's identity FAILS, by as much as
`(-0.447 + 0.354i)*pi^2`, the flattened sum is exactly `pi^2/2`.
G2 -- every `(p,q)` is an INTEGER, in `{0,+-1}`. Not asserted from theory: the
defects are computed as `(log z - expansion)/(2 pi i)` and their distance to the
nearest integer is reported.
G3 -- flattening changes nothing where the branch conditions already hold.
G4 -- the control: the UNflattened sum still fails at those same points, so G1 is
not measuring a tautology.

**The 5_2 sum rule remains verified to 80 dps, unproved.** Lean gets constancy on
a connected regular region and the value `pi^2/2` on a region reaching the real
square; it does NOT get a region joining the real square to `(y_1, conj y_1)`.
These points are evidence the identity holds there, not a proof a region exists.
"""

import json
import pathlib

from mpmath import (conj, fabs, im, log, mp, mpc, mpf, nint, nstr, pi, polylog,
                    polyroots, re)
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

TWO_VARIABLE = [("2.0", "0.5", "1.5", "-0.9"),
                ("-1.0", "0.3", "3.0", "2.0"),
                ("0.5", "3.0", "0.5", "-3.0"),
                ("2.0", "0.1", "2.0", "-0.1")]


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def pentagon_data(x, y):
    """(arguments, expansions of log a_i, expansions of log(1-a_i))."""
    d = 1 - x * y
    args = [x, y, (1 - x) / d, d, (1 - y) / d]
    lx, l1x, ly, l1y, lxy = log(x), log(1 - x), log(y), log(1 - y), log(d)
    lam = [lx, ly, l1x - lxy, lxy, l1y - lxy]
    lamp = [l1x, l1y, lx + l1y - lxy, lx + ly, ly + l1x - lxy]
    return args, lam, lamp


def flat_rogers(z, lam, lamp):
    return polylog(2, z) + lam * lamp / 2 + (log(1 - z) - lamp) * log(z)


def flat_pentagon(x, y):
    args, lam, lamp = pentagon_data(x, y)
    return sum(flat_rogers(z, a, b) for z, a, b in zip(args, lam, lamp))


def plain_pentagon(x, y):
    return sum(rogersL(z) for z in pentagon_data(x, y)[0])


def defect_integers(x, y):
    """(p, q) per argument, as complex numbers that should be integers."""
    two_pi_i = 2 * pi * mpc(0, 1)
    args, lam, lamp = pentagon_data(x, y)
    return [((log(z) - a) / two_pi_i, (log(1 - z) - b) / two_pi_i)
            for z, a, b in zip(args, lam, lamp)]


def int_distance(c):
    """Distance from a complex number to the nearest rational integer."""
    return fabs(c - int(nint(re(c))))


def main() -> int:
    set_compute_dps()
    tol = mpf(10) ** -30
    target = pi ** 2 / 2
    gates = []

    pts = [(mpc(a, b), mpc(c, d)) for a, b, c, d in TWO_VARIABLE]

    # ---- G1: flattening repairs every two-variable failure -----------------
    rows, flat_devs = [], []
    for x, y in pts:
        raw = plain_pentagon(x, y) - target
        flat = flat_pentagon(x, y) - target
        flat_devs.append(fabs(flat))
        rows.append({"x": nstr(x, 10), "y": nstr(y, 10),
                     "unflattened_dev_over_pi_sq": nstr(raw / pi ** 2, 14),
                     "flattened_abs_dev": nstr(fabs(flat), 8)})
    gates.append({
        "gate": "G1",
        "claim": "flattening removes the two-variable failure. At every point where Route 54's "
                 "identity misses pi^2/2 -- by as much as (-0.447 + 0.354i)*pi^2 -- the flattened "
                 "sum is exactly pi^2/2. This is the numerical shadow of "
                 "FiveTwoFlattenedPentagon.hasDerivAt_flatPentagonSum, which needs NO branch "
                 "hypothesis at all where the unflattened statement needed five",
        "cases": rows,
        "max_flattened_abs_deviation": nstr(max(flat_devs), 8),
        "pass": bool(max(flat_devs) < mpf(10) ** -25),
    })

    # ---- G2: the defects really are integers -------------------------------
    dists, seen = [], set()
    per_point = []
    for x, y in pts:
        pq = defect_integers(x, y)
        for p, q in pq:
            dists.extend([int_distance(p), int_distance(q)])
            seen.add(int(nint(re(p))))
            seen.add(int(nint(re(q))))
        per_point.append({"x": nstr(x, 8), "y": nstr(y, 8),
                          "pq": [[str(int(nint(re(p)))), str(int(nint(re(q))))]
                                 for p, q in pq]})
    gates.append({
        "gate": "G2",
        "claim": "the defects are INTEGERS, measured not assumed: each (log z - expansion)/(2 pi "
                 "i) is computed and its distance to the nearest rational integer reported. "
                 "Every value lands in {0,+-1}. Writing d = 2 pi i p and d' = 2 pi i q, "
                 "flatRogers is Neumann's R(z;p,q) up to normalisation, so this is the pentagon "
                 "in Bhat(C)",
        "max_distance_to_integer": nstr(max(dists), 8),
        "integers_seen": sorted(seen),
        "per_point": per_point,
        "pass": bool(max(dists) < tol and seen <= {-1, 0, 1}),
    })

    # ---- G3: flattening is inert where the branch conditions hold ----------
    inert = []
    for x, y in [(mpf("0.3"), mpf("0.4")), (mpf("0.3"), mpc("1.5", "0.8")),
                 (mpf("0.9"), mpc("-40.0", "-0.001"))]:
        inert.append(fabs(flat_pentagon(x, y) - plain_pentagon(x, y)))
    gates.append({
        "gate": "G3",
        "claim": "flattening changes nothing where the branch conditions already hold -- the real "
                 "square and Route 54's one-variable region. So the flattened statement extends "
                 "the earlier one rather than replacing it "
                 "(FiveTwoFlattenedPentagon.flatPentagonSum_eq_pentagonSum)",
        "max_abs_difference": nstr(max(inert), 8),
        "pass": bool(max(inert) < mpf(10) ** -25),
    })

    # ---- G4: the control -- the unflattened sum really does still fail -----
    raws = [fabs(plain_pentagon(x, y) - target) for x, y in pts]
    gates.append({
        "gate": "G4",
        "claim": "the control. The UNflattened sum still fails at exactly these points, so G1 is "
                 "not measuring a tautology: something was repaired. Without this gate a bug that "
                 "silently made both sums equal would read as success",
        "min_unflattened_abs_deviation": nstr(min(raws), 8),
        "pass": bool(min(raws) > mpf("0.1")),
    })

    # ---- G5: target unmoved -------------------------------------------------
    roots = polyroots([1, -2, 3, -1], maxsteps=900, extraprec=3500)
    y_up = [r for r in roots if im(r) > tol][0]
    flat_conj = flat_pentagon(y_up, conj(y_up)) - target
    A = re(sum(polylog(2, z) for z in roots))
    gates.append({
        "gate": "G5",
        "claim": "the target is unmoved. The flattened identity does hold at the 5_2 pair "
                 "(y_1, conj y_1) that Vol(5_2) needs -- but Lean reaches it only through a "
                 "connected regular region joining it to the real square, and NO such region is "
                 "exhibited. This is evidence, not a proof, and A = sum Li2(y_j) still has none",
        "flattened_abs_dev_at_conjugate_pair": nstr(fabs(flat_conj), 8),
        "A": nstr(A, 30),
        "region_exhibited": False,
        "pass": bool(fabs(A - mpf("0.9717306814686482591277741699")) < mpf(10) ** -25),
    })

    out = {
        "probe": "qbeta_5two_route56_flattened_pentagon",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 54 (the unconditional one-variable pentagon)",
        "lean": "QOU/QBeta/FiveTwoFlattenedPentagon.lean -- hasDerivAt_flatPentagonSum, "
                "flatPentagonSum_eq_pi_sq_div_two_of_region",
        "gates": gates,
        "verdict": {
            "proved": "the FLATTENED pentagon sum has vanishing derivative under regularity "
                      "alone -- no branch hypothesis anywhere, where the unflattened statement "
                      "needed five. Sorry-free in Lean, standard axioms.",
            "measured": "flattening repairs every two-variable failure of Route 54, and all ten "
                        "defects per point are integers in {0,+-1}.",
            "still_owed": "a connected regular region joining the real square to (y_1, conj y_1). "
                          "Without it the 5_2 volume is out of reach.",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route56-flattened-pentagon.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "flattening removes the two-variable failure: the flattened pentagon has vanishing "
        "derivative under regularity ALONE, no branch hypothesis, and repairs every point where "
        "Route 54's identity missed pi^2/2. All defects are integers in {0,+-1}. What is still "
        "owed is a connected regular region reaching (y_1, conj y_1). The 5_2 sum rule remains "
        "verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
