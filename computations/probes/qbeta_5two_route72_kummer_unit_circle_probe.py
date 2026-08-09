#!/usr/bin/env python3
"""Route 72 -- Kummer's identity on the unit circle, and the exact boundary of
what was proved.

Bean `qou-kmmr`. Companion to `QOU/Knot/KummerUnitCircle.lean`.

WHAT WAS PROVED IN LEAN (sorry-free, axioms [propext, Classical.choice, Quot.sound])
------------------------------------------------------------------------------------
`blochWigner_lob_exp` -- for theta in (0, pi),

    BlochWigner_lob(e^{i theta}) = Cl_2(theta)

i.e. Kummer's identity's Lambda-side on |z| = 1. On the unit circle the ideal
tetrahedron is ISOSCELES, angles (theta, (pi-theta)/2, (pi-theta)/2), so the
Lambda-sum is Lam(theta) + 2 Lam((pi-theta)/2), and that is exactly the Clausen
duplication formula the corpus already had.

WHAT THIS PROBE IS FOR
----------------------
Two jobs, and the second matters more.

1. Control on the statement: the angles really are isosceles, and the Lambda
   identity really is duplication.
2. **Mark the boundary.** A reader seeing "Kummer proved" could easily assume
   the whole identity, or assume it reaches Vol(5_2). It does neither. G3 shows
   the dilogarithm half is TRUE but NOT proved; G4 shows the 5_2 shape is off
   the unit circle entirely, so this file cannot reach the volume.

**The 5_2 sum rule is PROVED** (`FiveTwoComplexPentagon.fiveTwo_saddle_sum_rule`).
Kummer in general, and the 5_2 VOLUME, are NOT.
"""

import json
import pathlib

from mpmath import (arg, clsin, cos, exp, fabs, im, log, mp, mpc, mpf, nstr, pi,
                    polylog, polyroots, sin)


def lam(t):
    """Lobachevsky Lambda(t) = Cl_2(2t)/2, the corpus's `Lob`."""
    return clsin(2, 2 * t) / 2


def lobsum(z):
    a1, a2, a3 = arg(z), arg(1 / (1 - z)), arg(1 - 1 / z)
    return lam(a1) + lam(a2) + lam(a3), (a1, a2, a3)


def main() -> int:
    mp.dps = 60
    tol = mpf(10) ** -45
    gates = []
    thetas = [mpf(1) / 4, mpf(1), pi / 3, pi / 2, mpf(5) / 2, pi - mpf(1) / 8]

    # ---- G1: on |z| = 1 the tetrahedron is isosceles ------------------------
    worst_iso, worst_sum = mpf(0), mpf(0)
    rows = []
    for th in thetas:
        z = exp(mpc(0, 1) * th)
        _, (a1, a2, a3) = lobsum(z)
        worst_iso = max(worst_iso, fabs(a1 - th), fabs(a2 - (pi - th) / 2),
                        fabs(a3 - (pi - th) / 2))
        worst_sum = max(worst_sum, fabs(a1 + a2 + a3 - pi))
        rows.append({"theta": nstr(th, 12), "angles": [nstr(a, 12) for a in (a1, a2, a3)]})
    gates.append({
        "gate": "G1",
        "claim": "on |z| = 1 the ideal tetrahedron is ISOSCELES: the three angles of e^{i theta} "
                 "are (theta, (pi-theta)/2, (pi-theta)/2), and they sum to pi. This is what "
                 "collapses Kummer to a one-variable identity there",
        "samples": rows,
        "max_angle_deviation": nstr(worst_iso, 8),
        "max_sum_minus_pi": nstr(worst_sum, 8),
        "pass": bool(worst_iso < tol and worst_sum < tol),
    })

    # ---- G2: the Lambda identity IS Clausen duplication ---------------------
    worst_id, worst_dup = mpf(0), mpf(0)
    for th in thetas:
        worst_id = max(worst_id, fabs(lam(th) + 2 * lam((pi - th) / 2) - clsin(2, th)))
        # Cl_2(2t) = 2 Cl_2(t) - 2 Cl_2(pi - t)  -- the corpus's Cl_2_duplication
        worst_dup = max(worst_dup,
                        fabs(clsin(2, 2 * th) - (2 * clsin(2, th) - 2 * clsin(2, pi - th))))
    gates.append({
        "gate": "G2",
        "claim": "Lam(theta) + 2 Lam((pi-theta)/2) = Cl_2(theta), and it is exactly the Clausen "
                 "duplication formula Cl_2(2t) = 2 Cl_2(t) - 2 Cl_2(pi-t) halved -- which the "
                 "corpus already had as Cl_2_duplication, so the Lean proof is three lines",
        "max_lambda_identity_residual": nstr(worst_id, 8),
        "max_duplication_residual": nstr(worst_dup, 8),
        "pass": bool(worst_id < tol and worst_dup < tol),
    })

    # ---- G3: the dilogarithm half is TRUE but NOT PROVED --------------------
    worst_dilog = mpf(0)
    for th in thetas:
        z = exp(mpc(0, 1) * th)
        ls, _ = lobsum(z)
        D = im(polylog(2, z)) + log(abs(z)) * arg(1 - z)
        worst_dilog = max(worst_dilog, fabs(ls - D), fabs(im(polylog(2, z)) - clsin(2, th)))
    gates.append({
        "gate": "G3",
        "claim": "THE BOUNDARY. The dilogarithm half -- Im Li_2(e^{i theta}) = Cl_2(theta), so "
                 "that the Lambda-sum equals the Bloch-Wigner dilogarithm form -- is TRUE "
                 "numerically but is NOT proved in Lean for the corpus's cLiTwoExt. The Lean "
                 "theorem states its conclusion in terms of Cl_2 alone and makes NO dilogarithm "
                 "claim. This gate exists so that boundary is recorded, not blurred",
        "max_residual_lambda_vs_dilog": nstr(worst_dilog, 8),
        "numerically_true": bool(worst_dilog < tol),
        "proved_in_lean_for_cLiTwoExt": False,
        "pass": bool(worst_dilog < tol),
    })

    # ---- G4: scope -- the 5_2 shape is NOT on the unit circle ---------------
    y1 = [r for r in polyroots([1, -2, 3, -1], maxsteps=2000, extraprec=6000)
          if im(r) > mpf(10) ** -40][0]
    _, (b1, b2, b3) = lobsum(y1)
    iso_fail = max(fabs(b2 - b3), fabs(abs(y1) - 1))
    gates.append({
        "gate": "G4",
        "claim": "SCOPE: this file does NOT reach Vol(5_2). The 5_2 shape y_1 has |y_1| = 1.5236, "
                 "so it is off the unit circle; its tetrahedron is NOT isosceles and log|z| != 0. "
                 "The general-z case needs the genuine two-variable argument and is untouched",
        "y1": nstr(y1, 25),
        "abs_y1": nstr(abs(y1), 20),
        "y1_angles": [nstr(a, 20) for a in (b1, b2, b3)],
        "isosceles_failure_a2_minus_a3": nstr(fabs(b2 - b3), 8),
        "on_unit_circle": bool(fabs(abs(y1) - 1) < tol),
        "pass": bool(iso_fail > mpf(1) / 100),
    })

    out = {
        "probe": "qbeta_5two_route72_kummer_unit_circle",
        "beans": ["qou-kmmr"], "dps": mp.dps,
        "lean": "QOU/Knot/KummerUnitCircle.lean -- blochWigner_lob_exp",
        "gates": gates,
        "verdict": {
            "proved": "Kummer's Lambda-side on |z| = 1: BlochWigner_lob(e^{i theta}) = Cl_2(theta), "
                      "sorry-free, standard axioms. On the unit circle Kummer IS Clausen "
                      "duplication.",
            "not_proved": [
                "Kummer for general z (needs the two-variable differential argument)",
                "Im Li_2(e^{i theta}) = Cl_2(theta) for the corpus's cLiTwoExt",
                "Vol(5_2) -- y_1 is off the unit circle",
            ],
            "sum_rule_status": "PROVED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route72-kummer-unit-circle.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "Kummer on |z| = 1 is PROVED (it is Clausen duplication). General Kummer, the "
        "cLiTwoExt half, and Vol(5_2) are NOT -- the 5_2 shape is off the unit circle."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
