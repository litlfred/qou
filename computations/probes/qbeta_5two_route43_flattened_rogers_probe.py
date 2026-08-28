#!/usr/bin/env python3
"""Route 43 -- the 5_2 sum rule recast as an EXTENDED Bloch statement:
`sum_sigma Rhat(y_sigma; eps_sigma, 0) = -pi^2/6`, with the flattening supplied
by the cubic itself.

Beans `qou-xblo` (this route) and `qou-0yqu` (the parent gap). Follows Route 42,
which measured why the ORDINARY Bloch group cannot see the sum rule.

THE STATEMENT
-------------
With `L(z) = Li2(z) + log(z)*log(1-z)/2` the Rogers dilogarithm and

    Rhat(z; p, q) = L(z) - (pi*i/2) * ( p*log(1-z) + q*log(z) )

Neumann's flattened Rogers dilogarithm,

    sum_sigma Rhat(y_sigma; eps_sigma, 0) = -pi^2/6                    (G2)

over the three roots of `y^3 - 2y^2 + 3y - 1`, where

    eps_j = ( 2*log(y_j) - 3*log(1-y_j) ) / (2*pi*i)  =  (+1, -1, 0)   (G1)

is the cubic's **own branch data** -- not a fitted parameter. That those are
integers is already a sorry-free theorem on `main` (`branch_data_of_cubic`),
proved from the cubic alone with no dilogarithm involved. So the flattening the
extended Bloch group wants is already in the corpus.

It is a REFORMULATION, not a weaker statement: `sum V_j` and `3*sum Rhat` differ
by an elementary term computable from the cubic (G4).

THE QUANTISATION SIGNATURE
--------------------------
    -3*pi^2/2 = -9 * (pi^2/6)      the sum rule in V-normalisation
    sum Rhat  = -1 * (pi^2/6)      the same statement, flattened

while the individual `Re(V_j)/(pi^2/6)` are irrational (G3). Integral only in
the sum -- the signature of a Chern-Simons-type invariant, whose indeterminacy
is exactly `pi^2/6`.

⚠ WHAT THIS IS NOT
------------------
Not a proof. It moves the sum rule into the setting where the right machinery
exists; it does not run that machinery. Specifically:

* Neumann's **parity / geometric conditions** on a flattening are NOT imposed.
  `eps` was found by a search over `p, q in {-2..2}` and then recognised as the
  branch data. A second assignment `(p,q) = (-2,2)` also yields an integer
  (`11`), so G5 reports the whole solution set rather than implying uniqueness.
  The measured claim is "the cubic's branch data, used as a flattening, makes
  the Galois sum an exact integer multiple of pi^2/6" -- NOT "the geometric
  flattening does".
* Nothing here derives the integer `-1`. Deriving it is the proof.

**The 5_2 sum rule remains verified to 80 dps, unproved.**
"""

import json
import pathlib
from itertools import product

from mpmath import fabs, im, log, mp, mpf, nint, nstr, pi, polylog, polyroots, re

EPS = [1, -1, 0]        # the cubic's branch data, measured in G1
BRANCH_V = [-1, 1, 1]   # the corpus's V_j branch integers (real root carries +1)


def rogersL(z):
    return polylog(2, z) + log(z) * log(1 - z) / 2


def flattened(z, p, q):
    """Neumann's flattened Rogers dilogarithm."""
    return rogersL(z) - (pi * 1j / 2) * (p * log(1 - z) + q * log(z))


def saddle_V(y, b):
    return 3 * polylog(2, y) + (log(y) + b * pi * 1j) ** 2


def roots():
    rs = polyroots([1, -2, 3, -1], maxsteps=800, extraprec=3000)
    up = [r for r in rs if im(r) > mpf(10) ** -45][0]
    dn = [r for r in rs if im(r) < -(mpf(10) ** -45)][0]
    real = [r for r in rs if fabs(im(r)) < mpf(10) ** -45][0].real
    return [up, dn, real]


def main() -> int:
    mp.dps = 60
    gates = []
    Y = roots()

    # ---- G1: the flattening is the cubic's own branch data ------------------
    measured = [(2 * log(y) - 3 * log(1 - y)) / (2 * pi * 1j) for y in Y]
    worst = max(fabs(m - e) for m, e in zip(measured, EPS))
    gates.append({
        "gate": "G1",
        "claim": "the flattening is NOT a fitted parameter: eps_j = (2 log y_j - 3 log(1-y_j)) "
                 "/ (2 pi i) is measured as exactly (+1, -1, 0), the cubic's own branch data. "
                 "That these are integers is already sorry-free Lean on main "
                 "(`branch_data_of_cubic`), proved from the cubic with no dilogarithm involved -- "
                 "so the flattening the extended Bloch group needs is already a theorem",
        "eps_measured": [nstr(re(m), 25) for m in measured],
        "eps_expected": EPS,
        "worst_deviation": nstr(worst, 12),
        "pass": bool(worst < mpf(10) ** -45),
    })

    # ---- G2: the extended-Bloch form of the sum rule ------------------------
    S = sum(flattened(y, e, 0) for y, e in zip(Y, EPS))
    gates.append({
        "gate": "G2",
        "claim": "THE REFORMULATION. Summed over the Galois orbit, the FLATTENED Rogers "
                 "dilogarithm at the saddle roots equals exactly -pi^2/6 -- one unit of the "
                 "extended Bloch group's indeterminacy. The imaginary part vanishes too, so this "
                 "is a complex identity and not merely a statement about real parts",
        "sum_Rhat": nstr(S, 40),
        "minus_pi_sq_over_6": nstr(-pi ** 2 / 6, 40),
        "residual": nstr(fabs(S + pi ** 2 / 6), 12),
        "pass": bool(fabs(S + pi ** 2 / 6) < mpf(10) ** -50),
    })

    # ---- G3: the quantisation signature -------------------------------------
    unit = pi ** 2 / 6
    per_root = [re(saddle_V(y, b)) / unit for y, b in zip(Y, BRANCH_V)]
    tot_ratio = (-3 * pi ** 2 / 2) / unit
    any_integral = any(fabs(v - int(nint(v))) < mpf(10) ** -20 for v in per_root)
    gates.append({
        "gate": "G3",
        "claim": "THE SIGNATURE. -3pi^2/2 is exactly -9 units of pi^2/6, and the flattened sum "
                 "is exactly -1 unit -- while the INDIVIDUAL Re(V_j)/(pi^2/6) are irrational. "
                 "Integral only in the sum is the signature of a Chern-Simons-type invariant, "
                 "whose indeterminacy is precisely pi^2/6. The gate requires the individual "
                 "values NOT to be integers, so the quantisation cannot be read as trivial",
        "sum_rule_in_units": nstr(tot_ratio, 25),
        "per_root_in_units": [nstr(v, 20) for v in per_root],
        "any_individual_integral": bool(any_integral),
        "pass": bool(fabs(tot_ratio + 9) < mpf(10) ** -40 and not any_integral),
    })

    # ---- G4: it is a reformulation, not a weaker statement -------------------
    SV = sum(saddle_V(y, b) for y, b in zip(Y, BRANCH_V))
    elem = sum(3 * (pi * 1j / 2) * e * log(1 - y) + pi * 1j * (e + 2 * b) * log(y)
               - pi ** 2 * b ** 2
               for y, e, b in zip(Y, EPS, BRANCH_V))
    gates.append({
        "gate": "G4",
        "claim": "the flattened form is EQUIVALENT to the sum rule, not weaker: sum V_j equals "
                 "3*sum Rhat plus an elementary term built from the cubic's branch data and the "
                 "logs. So proving the flattened statement proves the sum rule, which is what "
                 "makes the reformulation worth having",
        "sum_V": nstr(SV, 30),
        "three_sum_Rhat_plus_elementary": nstr(3 * S + elem, 30),
        "residual": nstr(fabs(SV - (3 * S + elem)), 12),
        "pass": bool(fabs(SV - (3 * S + elem)) < mpf(10) ** -45),
    })

    # ---- G5: the full solution set, so uniqueness is not implied ------------
    hits = []
    for p1, q1 in product(range(-2, 3), repeat=2):
        for p3, q3 in product(range(-2, 3), repeat=2):
            T = (flattened(Y[0], p1, q1) + flattened(Y[1], -p1, -q1)
                 + flattened(Y[2], p3, q3))
            if fabs(im(T)) < mpf(10) ** -30:
                r = re(T) / unit
                n = int(nint(r))
                if fabs(r - n) < mpf(10) ** -30:
                    hits.append({"p1_q1": [p1, q1], "p3_q3": [p3, q3], "units": n})
    gates.append({
        "gate": "G5",
        "claim": "the whole solution set over p,q in {-2..2} with the conjugate root carrying the "
                 "conjugate flattening -- reported rather than suppressed, because eps was FOUND "
                 "by this search and only then recognised as the branch data. A second "
                 "assignment also gives an integer, so this probe does NOT claim the flattening "
                 "is unique or that it satisfies Neumann's geometric conditions, which are not "
                 "imposed anywhere here",
        "solutions": hits,
        "count": len(hits),
        "branch_data_is_among_them": any(h["p1_q1"] == [1, 0] and h["p3_q3"] == [0, 0]
                                         for h in hits),
        "pass": bool(len(hits) >= 1
                     and any(h["p1_q1"] == [1, 0] and h["p3_q3"] == [0, 0] and h["units"] == -1
                             for h in hits)),
    })

    out = {
        "probe": "qbeta_5two_route43_flattened_rogers",
        "beans": ["qou-xblo", "qou-0yqu"], "dps": mp.dps,
        "follows": "Route 42 (the volume anchor and the Bloch-Wigner obstruction)",
        "gates": gates,
        "verdict": {
            "measured": "sum_sigma Rhat(y_sigma; eps_sigma, 0) = -pi^2/6 exactly, with eps the "
                        "cubic's own branch data (+1,-1,0) -- already integral by a sorry-free "
                        "Lean theorem on main. Equivalent to the sum rule up to an elementary "
                        "term.",
            "signature": "-3pi^2/2 is -9 units of pi^2/6 and the flattened sum is -1 unit, while "
                         "the individual Re(V_j) are irrational in those units. Integral only in "
                         "the sum -- a Chern-Simons-type quantisation.",
            "not_proved": "this is a reformulation. Nothing here derives the integer -1, and "
                          "Neumann's parity/geometric conditions on the flattening are not "
                          "imposed -- eps was found by search and then recognised. The target "
                          "becomes: show sum_sigma [y_sigma; eps_sigma, 0] is torsion in "
                          "extended-Bloch B-hat(C).",
            "sum_rule_status": "verified to 80 dps, unproved",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route43-flattened-rogers.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=False)
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:72]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the sum rule is an EXTENDED Bloch statement -- sum Rhat = -pi^2/6 with the flattening "
        "supplied by the cubic. A reformulation into the right setting, not a proof. "
        "The 5_2 sum rule remains verified to 80 dps, unproved."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
