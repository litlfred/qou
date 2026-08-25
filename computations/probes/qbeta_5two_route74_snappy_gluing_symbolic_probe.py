#!/usr/bin/env python3
"""Route 74 -- the 5_2 gluing equations, verified SYMBOLICALLY over the shape
field, and a wrong assumption of mine caught by SnapPy.

Beans `qou-m015`, `qou-mlgp`, `qou-kmmr`.

WHY SYMBOLIC AND NOT NUMERICAL
------------------------------
SnapPy's gluing equations are INTEGER exponent matrices -- exact combinatorial
data, not floating point. And the 5_2 shape is algebraic: a root of
y^3 - 2y^2 + 3y - 1 (discriminant -23). So the whole verification can be done
exactly, in Q[y]/(minpoly), with no floats anywhere: form the product
prod_j z_j^a (z'_j)^b (z''_j)^c - 1, clear denominators, and reduce modulo the
minimal polynomial. The residual is 0 or it is not.

That is strictly stronger than evaluating at 60 dps, and it is what this probe
does. mpmath appears here ONLY to identify which algebraic number SnapPy's
numerical shape is; every equation check is sympy over the number field.

THE CORRECTION THIS PROBE RECORDS
---------------------------------
`FiveTwoVolumeConstant.lean` previously defined the 5_2 triangulation as
`const 3 fiveTwoTet` -- three tetrahedra all of shape y_1. **That was wrong.**
SnapPy gives shapes (y_1, 1/(1-y_1), y_1): the middle tetrahedron carries the
SECOND EDGE PARAMETER of y_1, not y_1.

The volume claim Vol = 3 D(y_1) survives, but for a reason the earlier version
did not state: z -> 1/(1-z) cyclically permutes the three dihedral angles, so
Lam(th1)+Lam(th2)+Lam(th3) is unchanged. That is now a Lean theorem
(`IdealTetrahedron.rotate_angles`, `volume_rotate`) rather than an assumption,
and the triangulation is corrected to the real shapes.

**The 5_2 sum rule is PROVED; Kummer's identity is PROVED.** The 5_2 VOLUME
conjecture is Ohtsuki's theorem and is not formalised here, and no claim here is
about the topological manifold S^3 \\ 5_2.
"""

import json
import pathlib
import warnings

warnings.filterwarnings("ignore")

import sympy as sp
from mpmath import fabs, im, mp, mpc, mpf, nstr, polyroots
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

MINPOLY_COEFFS = [1, -2, 3, -1]          # y^3 - 2y^2 + 3y - 1


def main() -> int:
    set_compute_dps()
    gates = []
    y = sp.symbols("y")
    minpoly = y ** 3 - 2 * y ** 2 + 3 * y - 1

    try:
        import snappy
    except ImportError:
        print("snappy not installed -- cannot run"); return 1

    M = snappy.Manifold("5_2")
    N = M.num_tetrahedra()
    rows = [[int(x) for x in r] for r in M.gluing_equations()]
    snappy_shapes = [mpc(str(z.real()), str(z.imag())) for z in M.tetrahedra_shapes("rect")]

    y1 = [r for r in polyroots(MINPOLY_COEFFS, maxsteps=2000, extraprec=6000)
          if im(r) > mpf(10) ** -30][0]

    # ---- G1: identify SnapPy's shapes as exact algebraic numbers -----------
    expected = [y1, 1 / (1 - y1), y1]
    labels = ["y_1", "1/(1-y_1)", "y_1"]
    worst = max(fabs(a - b) for a, b in zip(snappy_shapes, expected))
    all_same = fabs(snappy_shapes[0] - snappy_shapes[1]) < mpf(10) ** -20
    gates.append({
        "gate": "G1",
        "claim": "THE CORRECTION. SnapPy's three 5_2 shapes are (y_1, 1/(1-y_1), y_1) -- they are "
                 "NOT all equal. An earlier version of FiveTwoVolumeConstant.lean modelled the "
                 "triangulation as `const 3 fiveTwoTet` (all shape y_1); that was wrong, and this "
                 "gate exists so the error cannot recur silently",
        "num_tetrahedra": N,
        "snappy_shapes": [nstr(z, 14) for z in snappy_shapes],
        "identified_as": labels,
        "max_identification_error": nstr(worst, 6),
        "all_three_shapes_equal": bool(all_same),
        "pass": bool(worst < mpf(10) ** -9 and not all_same),
    })

    # ---- G2: the gluing equations, EXACTLY over Q[y]/(minpoly) -------------
    shapes = [y, 1 / (1 - y), y]
    def params(z):
        return [z, 1 / (1 - z), (z - 1) / z]

    eq_rows, worst_sym = [], 0
    for k, row in enumerate(rows):
        expr = sp.Integer(1)
        for j in range(N):
            p = params(shapes[j])
            for tI in range(3):
                expr *= p[tI] ** row[3 * j + tI]
        num, _den = sp.fraction(sp.cancel(sp.together(expr - 1)))
        red = sp.simplify(sp.rem(sp.expand(num), minpoly, y))
        eq_rows.append({"kind": "edge" if k < N else "cusp", "exponents": row,
                        "residual_mod_minpoly": str(red)})
        worst_sym = max(worst_sym, 0 if red == 0 else 1)
    gates.append({
        "gate": "G2",
        "claim": "THE MAIN RESULT, AND IT IS SYMBOLIC. All 5 gluing equations -- 3 edge, 2 cusp -- "
                 "hold EXACTLY over the shape field Q[y]/(y^3-2y^2+3y-1). Each product minus 1, "
                 "with denominators cleared, reduces to 0 modulo the minimal polynomial. No "
                 "floating point is involved anywhere in this gate",
        "minimal_polynomial": str(minpoly),
        "discriminant": -23,
        "equations": eq_rows,
        "all_residuals_zero": bool(worst_sym == 0),
        "pass": bool(worst_sym == 0),
    })

    # ---- G3: why the volume still comes out 3 D(y_1) -----------------------
    ang = sp.simplify(sp.rem(sp.expand(sp.fraction(
        sp.cancel(sp.together(1 / (1 - (1 / (1 - y))) - (1 - 1 / y))))[0]), minpoly, y))
    gates.append({
        "gate": "G3",
        "claim": "why Vol = 3 D(y_1) SURVIVES the correction, as a reason rather than a "
                 "coincidence: z -> 1/(1-z) cyclically permutes the three dihedral angles, since "
                 "1/(1 - 1/(1-z)) = 1 - 1/z and 1 - 1/(1/(1-z)) = z. So Lam(th1)+Lam(th2)+Lam(th3) "
                 "is unchanged -- proved in Lean as IdealTetrahedron.rotate_angles / volume_rotate",
        "cycle_identity_residual": str(ang),
        "pass": bool(ang == 0),
    })

    # ---- G4: scope ---------------------------------------------------------
    gates.append({
        "gate": "G4",
        "claim": "SCOPE. Verified here: that the ALGEBRAIC shapes satisfy SnapPy's gluing "
                 "equations exactly. NOT verified, and not statable in Lean today: that this "
                 "triangulation is a triangulation OF the topological manifold S^3 \\ 5_2. That "
                 "is Thurston hyperbolisation plus Mostow rigidity and needs hyperbolic "
                 "3-manifolds, which neither Mathlib nor QOU has. Nor is the 5_2 volume "
                 "conjecture (Ohtsuki 2016) touched",
        "gluing_equations_verified_symbolically": True,
        "is_triangulation_of_the_manifold": "not statable in Lean today",
        "vol_conjecture_formalized": False,
        "pass": True,
    })

    out = {
        "probe": "qbeta_5two_route74_snappy_gluing_symbolic",
        "beans": ["qou-m015", "qou-mlgp", "qou-kmmr"],
        "snappy_version": snappy.version(),
        "gates": gates,
        "verdict": {
            "proved_symbolically": "the exact algebraic shapes (y_1, 1/(1-y_1), y_1) satisfy all "
                                   "5 of SnapPy's 5_2 gluing equations over Q[y]/(y^3-2y^2+3y-1), "
                                   "residual 0.",
            "corrected": "the triangulation is NOT three copies of y_1; the middle tetrahedron is "
                         "1/(1-y_1). Vol = 3 D(y_1) survives because the relabelling cycles the "
                         "angles -- now a theorem, not an assumption.",
            "not_established": "that this is a triangulation of S^3 \\ 5_2 (not statable in Lean).",
            "sum_rule_status": "PROVED", "kummer_status": "PROVED",
        },
    }
    dest = (pathlib.Path(__file__).resolve().parents[1]
            / "qbeta-5two-route74-snappy-gluing-symbolic.witness.json")
    dest.write_text(json.dumps(out, indent=2) + "\n")
    for g in gates:
        print(f"  {g['gate']}  pass={g['pass']}  {g['claim'][:70]}")
    print(f"\nwitness -> {dest}")
    ok = all(g["pass"] for g in gates)
    print("VERDICT: " + (
        "all 5 gluing equations hold EXACTLY over the shape field -- symbolic, no floats. And "
        "the triangulation is (y_1, 1/(1-y_1), y_1), NOT three copies of y_1: the earlier Lean "
        "model was wrong and is corrected."
        if ok else "FAILED -- see the gates above."))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
