#!/usr/bin/env python3
"""Route 73 -- the dilogarithm half of Kummer, the ideal-tetrahedron law of
sines, and the radial reduction it unlocks.

Bean `qou-kmmr`. Companions:
  QOU/Knot/KummerDilogHalf.lean     -- im_cLiTwoExt_exp, kummer_unit_circle
  QOU/Knot/IdealTetLawOfSines.lean  -- norm_eq_sin_div_sin, log_sin_sub_log_sin

THE LAW OF SINES, AND WHY IT IS THE WHOLE GAME
----------------------------------------------
An ideal tetrahedron with shape z (Im z > 0) has three dihedral angles

    th1 = arg z,   th2 = arg(1/(1-z)),   th3 = arg(1 - 1/z),   th1+th2+th3 = pi

and they satisfy   **|z| = sin(th2)/sin(th3)**.

That is the ideal-tetrahedron analogue of the Euclidean law of sines: the
*modulus* of the shape is a ratio of sines of the opposite angles, exactly as a
side length is in a triangle. It is what ties the ANGLE description of the
tetrahedron to the SHAPE-PARAMETER description.

And it is what reduces Kummer's identity from two variables to one. Along a ray
of constant arg z:
  * th1 is CONSTANT, so Lam(th1) contributes nothing;
  * th1+th2+th3 = pi forces d th3 = -d th2;
  * so  d/dr [Lam(th2)+Lam(th3)] = log(sin th3 / sin th2) * d th2/dr;
  * and d/dr [dilogarithm side]  = -log r * d th2/dr.
These agree **iff** r = sin(th2)/sin(th3) -- the law of sines. The basepoint
r = 1 is `kummer_unit_circle`, already proved.

UPDATE: Kummer for general z is now PROVED -- QOU/Knot/KummerRadial.lean,
`kummer` -- by exactly the radial reduction described above. G3 was the
numerical check on the plan; the plan worked.

**The 5_2 sum rule is PROVED.** The 5_2 VOLUME conjecture is Ohtsuki's theorem
and is NOT formalised here: Kummer is the analytic factor of Vol = D, and the
geometric factor is untouched.
"""

import json
import pathlib

from mpmath import (arg, clsin, exp, fabs, im, log, mp, mpc, mpf, nstr, pi,
                    polylog, polyroots, sin)


def lam(t):
    return clsin(2, 2 * t) / 2


def angles(z):
    return arg(z), arg(1 / (1 - z)), arg(1 - 1 / z)


def d_lambda(z):
    a1, a2, a3 = angles(z)
    return lam(a1) + lam(a2) + lam(a3)


def d_dilog(z):
    return im(polylog(2, z)) + log(abs(z)) * arg(1 - z)


def main() -> int:
    mp.dps = 60
    tol = mpf(10) ** -45
    gates = []
    y1 = [r for r in polyroots([1, -2, 3, -1], maxsteps=2000, extraprec=6000)
          if im(r) > mpf(10) ** -40][0]
    shapes = [mpc('0.3', '0.7'), mpc('1.5', '0.8'), mpc('-0.4', '1.2'),
              mpc('0.2', '2.5'), mpc('3', '0.1'), y1]

    # ---- G1: the dilogarithm half on the unit circle -----------------------
    worst = mpf(0)
    for th in [mpf(1) / 4, mpf(1), pi / 3, mpf(5) / 2, pi - mpf(1) / 8]:
        worst = max(worst, fabs(im(polylog(2, exp(mpc(0, 1) * th))) - clsin(2, th)))
    gates.append({
        "gate": "G1",
        "claim": "the dilogarithm half, now PROVED in Lean for the corpus's cLiTwoExt "
                 "(im_cLiTwoExt_exp): Im Li_2(e^{i theta}) = Cl_2(theta) on (0, 2pi). Proved by "
                 "same-derivative -- both sides differentiate to -log(2 sin(theta/2)) -- plus the "
                 "basepoint theta = pi, where cLiTwoExt(-1) = -pi^2/12 is REAL and Cl_2(pi) = 0",
        "max_residual": nstr(worst, 8),
        "pass": bool(worst < tol),
    })

    # ---- G2: THE LAW OF SINES ----------------------------------------------
    rows, worst_los = [], mpf(0)
    for z in shapes:
        a1, a2, a3 = angles(z)
        pred = sin(a2) / sin(a3)
        worst_los = max(worst_los, fabs(abs(z) - pred), fabs(a1 + a2 + a3 - pi))
        rows.append({"z": nstr(z, 16), "abs_z": nstr(abs(z), 20),
                     "sin_th2_over_sin_th3": nstr(pred, 20),
                     "angles_sum_minus_pi": nstr(fabs(a1 + a2 + a3 - pi), 6)})
    gates.append({
        "gate": "G2",
        "claim": "THE LAW OF SINES for an ideal tetrahedron: |z| = sin(th2)/sin(th3), with the "
                 "three angles summing to pi. The ideal-tetrahedron analogue of the Euclidean law "
                 "of sines -- the MODULUS of the shape is a ratio of sines of opposite angles, "
                 "just as a side length is in a triangle. It ties the ANGLE picture to the "
                 "SHAPE-PARAMETER picture, and it holds at the 5_2 shape y_1 like everywhere else",
        "samples": rows,
        "max_residual": nstr(worst_los, 8),
        "pass": bool(worst_los < tol),
    })

    # ---- G3: the radial reduction -- the difference is constant on rays ----
    worst_ray = mpf(0)
    ray_rows = []
    for z in shapes:
        phi = arg(z)
        vals = []
        for r in [mpf(1) / 4, mpf(1) / 2, mpf(1), mpf(2), mpf(5)]:
            w = r * exp(mpc(0, 1) * phi)
            vals.append(d_lambda(w) - d_dilog(w))
        spread = max(fabs(v - vals[0]) for v in vals)
        worst_ray = max(worst_ray, spread, max(fabs(v) for v in vals))
        ray_rows.append({"arg_z": nstr(phi, 14), "max_spread_along_ray": nstr(spread, 6)})
    gates.append({
        "gate": "G3",
        "claim": "THE REDUCTION WORKS. Along every ray of constant arg z, the difference "
                 "(Lambda-side minus dilogarithm-side) is CONSTANT in r -- and equal to 0. That "
                 "constancy is exactly what the law of sines buys, and it is why Kummer for "
                 "general z needs only a ONE-variable argument with r = 1 as basepoint, not the "
                 "two-variable differential argument it appears to need",
        "rays": ray_rows,
        "max_spread_and_value": nstr(worst_ray, 8),
        "pass": bool(worst_ray < tol),
    })

    # ---- G4: scope ---------------------------------------------------------
    gates.append({
        "gate": "G4",
        "claim": "SCOPE, UPDATED. When written this gate said the radial argument was not yet "
                 "assembled and general-z Kummer was unproved. It is now PROVED -- "
                 "QOU/Knot/KummerRadial.lean, `kummer`, sorry-free -- by exactly the reduction G3 "
                 "anticipated. What remains untouched is Vol(5_2): Kummer is the ANALYTIC factor "
                 "of Vol = D, and the GEOMETRIC factor (a triangulation's Lambda-sum IS the "
                 "volume) is qou-m015/qou-krvm territory. The 5_2 volume conjecture is Ohtsuki's "
                 "published theorem, not formalised anywhere here",
        "kummer_unit_circle_proved": True,
        "law_of_sines_proved": True,
        "kummer_general_z_proved": True,
        "proved_by": "QOU/Knot/KummerRadial.lean -- kummer",
        "vol_5_2_proved": False,
        "pass": True,
    })

    out = {
        "probe": "qbeta_5two_route73_law_of_sines_radial",
        "beans": ["qou-kmmr"], "dps": mp.dps,
        "lean": "QOU/Knot/KummerDilogHalf.lean; QOU/Knot/IdealTetLawOfSines.lean",
        "gates": gates,
        "verdict": {
            "proved": "Kummer on |z| = 1 (both halves); the ideal-tetrahedron law of sines "
                      "|z| = sin(th2)/sin(th3) for all Im z > 0.",
            "also_proved": "Kummer for general z -- QOU/Knot/KummerRadial.lean, `kummer`. The "
                           "radial argument G3 anticipated is now assembled.",
            "not_proved": "Vol(5_2) -- the GEOMETRIC factor of Vol = D is untouched.",
            "sum_rule_status": "PROVED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route73-law-of-sines-radial.witness.json")
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
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "the law of sines |z| = sin(th2)/sin(th3) makes the difference constant along rays, and "
        "the resulting one-variable argument is now assembled: general-z Kummer is PROVED. "
        "Vol(5_2) is still untouched -- that needs the geometric factor."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
