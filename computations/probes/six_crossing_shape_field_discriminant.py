#!/usr/bin/env python3
"""Six-crossing shape-field discriminants — reproducibility witness for the 6₁/6₂
arithmetic fingerprints used by `QOU/QBeta/SixOneShapeDiscriminant.lean`.

The GGM state-integral saddle curve is worked explicitly only for 4₁ and 5₂
(`library/arxiv-2012.00062v3/2012.00062v3.pdf` §§5–6); 6-crossing knots appear there only as q-series.
The faithful 6-crossing datum is therefore taken from the hyperbolic geometry: the
shape parameter `z` of the knot's ideal triangulation generates the shape field,
whose minimal polynomial and discriminant are the arithmetic fingerprint (the
6-crossing analogue of the 5₂ trace-field discriminant −23).

SOURCE (documented, not re-run here so the witness stays CI-safe without SnapPy):
the shapes below were produced by `snappy.Manifold('6_1'/'6_2').tetrahedra_shapes(
'rect', dec_prec=90)[0]`; the minimal polynomials by PARI/GP `z.algdep(deg)`. This
probe re-verifies both facts from the hardcoded shapes with mpmath + sympy only:

  6₁ (Stevedore, 4 tet, Vol ≈ 3.16396): shape min poly x⁴ − 3x³ + 6x² − 5x + 2,
       discriminant 257 (prime).
  6₂ (5 tet, Vol ≈ 4.40083):            shape min poly x⁵ − 3x⁴ + 5x³ − 5x² + 4x − 1,
       discriminant 1777 (prime).

Verification: (a) |p(z)| < 10⁻⁶⁰ at 90-digit precision (z is a root); (b) the
sympy discriminant of p equals the stated prime. The Lean file formalizes the
discriminant identity `∏_{i<j}(yᵢ−yⱼ)² = disc(e₁,…)` and its evaluation at the 6₁
Vieta values → 257 (generic ring; independent of this numerical source).

No fit; nothing wired. Source of truth for the shapes: SnapPy; for the field
polynomials: PARI algdep.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 90

# SnapPy Manifold(...).tetrahedra_shapes('rect', dec_prec=90)[0] — documented source.
SHAPES = {
    "6_1": (
        "0.895123382259649768951389683483530603380678187368803279946947960017800428384974106582003640",
        "1.552491820061879622421467325938648110598017684729938741462977509770982377333251170722221137",
        [1, -3, 6, -5, 2],          # x⁴ − 3x³ + 6x² − 5x + 2
        257,
    ),
    "6_2": (
        "1.186078404604432119023133838267381038869218517215524094689551862512215348722082881607477366",
        "0.874646460526086917571759719443566706817853336200335414283150016682723602454116685605482036",
        [1, -3, 5, -5, 4, -1],      # x⁵ − 3x⁴ + 5x³ − 5x² + 4x − 1
        1777,
    ),
}


def run() -> dict:
    out: dict = {}
    x = sp.symbols("x")
    for name, (re_s, im_s, coeffs, disc_expected) in SHAPES.items():
        z = mp.mpc(mp.mpf(re_s), mp.mpf(im_s))
        pz = mp.polyval([mp.mpf(c) for c in coeffs], z)
        is_root = abs(pz) < mp.mpf(10) ** (-60)
        P = sum(c * x ** (len(coeffs) - 1 - i) for i, c in enumerate(coeffs))
        disc = int(sp.discriminant(P, x))
        out[name] = {
            "min_poly_coeffs": coeffs,
            "min_poly": str(sp.factor(P)),
            "shape_is_root": bool(is_root),
            "p_at_z_abs": mp.nstr(abs(pz), 3),
            "discriminant": disc,
            "discriminant_expected": disc_expected,
            "discriminant_matches": disc == disc_expected,
            "discriminant_is_prime": bool(sp.isprime(abs(disc))),
        }
    return out


def main() -> int:
    res = run()
    print("# Six-crossing shape-field discriminants (SnapPy shapes, PARI algdep polys)\n")
    ok = True
    for name, d in res.items():
        print(f"## {name}: {d['min_poly']}")
        print(f"   shape is a root (|p(z)| = {d['p_at_z_abs']}): {d['shape_is_root']}")
        print(f"   discriminant = {d['discriminant']} (expected {d['discriminant_expected']}, "
              f"prime={d['discriminant_is_prime']}): {d['discriminant_matches']}\n")
        ok = ok and d["shape_is_root"] and d["discriminant_matches"]

    w = WitnessBuilder("six-crossing-shape-field-discriminant", engine="mpmath+sympy")
    w.set_description(
        "Reproducibility witness for the 6-crossing shape-field arithmetic fingerprints "
        "formalized by QOU/QBeta/SixOneShapeDiscriminant.lean. Shapes from "
        "snappy.Manifold('6_1'/'6_2') (dec_prec=90), minimal polynomials from PARI algdep; "
        "re-verified here with mpmath+sympy only (no SnapPy at run time). 6_1: x^4-3x^3+6x^2-5x+2, "
        "disc 257 (prime); 6_2: x^5-3x^4+5x^3-5x^2+4x-1, disc 1777 (prime). Each shape is a root "
        "to |p(z)|<1e-60 at 90 digits; discriminants match and are prime. GGM works explicit "
        "saddle curves only for 4_1/5_2, so the 6-crossing datum is taken from the hyperbolic "
        "geometry (SnapPy) instead. No fit; nothing wired."
    )
    for name, d in res.items():
        w.add_data(name, d)
    w.add_assertion(
        "six_crossing_shape_discriminants_verified",
        computed=1 if ok else 0, expected=1, tolerance=0,
        source="Each SnapPy shape is a root of its PARI-algdep minimal polynomial to |p(z)|<1e-60 "
               "at 90 digits, and the sympy discriminant equals the stated prime (6_1: 257, "
               "6_2: 1777). Formalized (6_1) as ∏(yi-yj)^2 = 257 in SixOneShapeDiscriminant.lean.",
    )
    out = w.save()
    print(f"witness → {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
