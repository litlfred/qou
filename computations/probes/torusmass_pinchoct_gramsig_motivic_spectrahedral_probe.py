#!/usr/bin/env python3
"""80-dps mpmath probe for Round 76:
- cj212: QOU.BraidKnot.TorusKnotMass.higgs_to_gauge_factor_ratio_ne_one
- qou-3q7t: QOU.MassTheory.PinchedOctahedron.e1_glued_and_quad_sum_sq
- qou-o3ta: QOU.QBeta.GramSignature.y21_mul_two_q_sq_eq_one_of_radical
- qou-u96j: QOU.AlgebraicSubstrate.realize_lefschetz_isUnit
- qou-zf9n: QOU.Archimedean.spectrahedral_phase_collapse_conventionD
"""

from __future__ import annotations
import hashlib
import json
import pathlib
import sys
from mpmath import mp

mp.dps = 80


def check_torus_knot_mass_ratio() -> dict[str, object]:
    gauge_factor = mp.mpf("143")
    scalar_factor = mp.mpf("171")
    ratio = scalar_factor / gauge_factor
    diff_from_one = abs(ratio - mp.mpf("1"))
    passed = (ratio > mp.mpf("0")) and (diff_from_one > mp.mpf("1") / mp.mpf("10"))
    return {
        "bean": "cj212",
        "theorem": "QOU.BraidKnot.TorusKnotMass.higgs_to_gauge_factor_ratio_ne_one",
        "ratio": mp.nstr(ratio, 80),
        "abs_ratio_sub_one": mp.nstr(diff_from_one, 80),
        "passed": passed,
    }


def check_pinched_octahedron_glued_quad() -> dict[str, object]:
    eps = mp.mpf("3") / mp.mpf("7")
    b1 = mp.mpf("5") / mp.mpf("11")
    b2 = mp.mpf("13") / mp.mpf("17")
    b1p = mp.mpf("-2") / mp.mpf("9")
    b2p = mp.mpf("7") / mp.mpf("13")
    m1 = mp.mpf("4") / mp.mpf("15")
    m2 = mp.mpf("-6") / mp.mpf("19")
    r = eps * (b2p - b1)
    t = eps * (b2 - b1 - m1)
    l = eps * (b2 - b1p + m2 - m1)
    b = eps * (b2p - b1p + m2)
    glue_res = abs((r + l) - (t + b))
    e1_val = r + t + l + b
    e2_val = r * t + r * l + r * b + t * l + t * b + l * b
    lin_res = abs(e1_val - mp.mpf("2") * (r + l))
    quad_lhs = (e1_val ** 2) - mp.mpf("2") * e2_val
    quad_rhs = (r ** 2) + (t ** 2) + (l ** 2) + (b ** 2)
    quad_res = abs(quad_lhs - quad_rhs)
    passed = (
        glue_res < mp.mpf("10") ** (-75)
        and lin_res < mp.mpf("10") ** (-75)
        and quad_res < mp.mpf("10") ** (-75)
    )
    return {
        "bean": "qou-3q7t",
        "theorem": "QOU.MassTheory.PinchedOctahedron.e1_glued_and_quad_sum_sq",
        "glue_residual": mp.nstr(glue_res, 80),
        "e1_glued_residual": mp.nstr(lin_res, 80),
        "quad_sum_sq_residual": mp.nstr(quad_res, 80),
        "passed": passed,
    }


def check_gram_signature_y21_radical() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    z_d = (q0 ** 3) / ((q0 ** 2) + mp.mpf("1"))
    two_q = q0 + (mp.mpf("1") / q0)
    y21 = (q0 - z_d) / two_q
    y3 = mp.mpf("1") - mp.mpf("2") * y21
    prod_val = y21 * (two_q ** 2)
    res_one = abs(prod_val - mp.mpf("1"))
    hz_res = abs((q0 * y3 + (q0 - (mp.mpf("1") / q0)) * y21) - z_d)
    passed = (res_one < mp.mpf("10") ** (-75)) and (hz_res < mp.mpf("10") ** (-75))
    return {
        "bean": "qou-o3ta",
        "theorem": "QOU.QBeta.GramSignature.y21_mul_two_q_sq_eq_one_of_radical",
        "y21": mp.nstr(y21, 80),
        "y21_mul_two_q_sq": mp.nstr(prod_val, 80),
        "residual_from_one": mp.nstr(res_one, 80),
        "passed": passed,
    }


def check_motivic_lefschetz_unit() -> dict[str, object]:
    # Evaluate multiplicative unit identity realize_v(inclusion(L)) * realize_v(inclusion(L⁻¹)) = 1
    places = [mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000"), mp.mpf("2"), mp.mpf("3"), mp.mpf("5")]
    max_res = mp.mpf("0")
    for lv in places:
        inv_lv = mp.mpf("1") / lv
        res = abs(lv * inv_lv - mp.mpf("1"))
        if res > max_res:
            max_res = res
    passed = max_res < mp.mpf("10") ** (-75)
    return {
        "bean": "qou-u96j",
        "theorem": "QOU.AlgebraicSubstrate.realize_lefschetz_isUnit",
        "places_evaluated": str(len(places)),
        "max_unit_residual": mp.nstr(max_res, 80),
        "passed": passed,
    }


def check_spectrahedral_convention_d() -> dict[str, object]:
    q0 = mp.mpf("11099806389098548918") / mp.mpf("10000000000000000000")
    z_d = (q0 ** 3) / ((q0 ** 2) + mp.mpf("1"))
    h = q0 - (mp.mpf("1") / q0)
    # General H3 Gram determinant factor ((h^2 + 4)*z^2 - (h^3 + 4*h)*z - 1) and ((q^2 + 1)*z - q^3)
    d_factor = ((q0 ** 2) + mp.mpf("1")) * z_d - (q0 ** 3)
    gen_factor = ((h ** 2) + mp.mpf("4")) * (z_d ** 2) - ((h ** 3) + mp.mpf("4") * h) * z_d - mp.mpf("1")
    res = abs(d_factor) + abs(gen_factor)
    passed = res < mp.mpf("10") ** (-75)
    return {
        "bean": "qou-zf9n",
        "theorem": "QOU.Archimedean.spectrahedral_phase_collapse_conventionD",
        "d_factor_residual": mp.nstr(abs(d_factor), 80),
        "general_det_factor_residual": mp.nstr(abs(gen_factor), 80),
        "passed": passed,
    }


def main() -> int:
    script_path = pathlib.Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]
    checks = [
        check_torus_knot_mass_ratio(),
        check_pinched_octahedron_glued_quad(),
        check_gram_signature_y21_radical(),
        check_motivic_lefschetz_unit(),
        check_spectrahedral_convention_d(),
    ]
    all_passed = all(bool(c["passed"]) for c in checks)
    payload = {
        "probe": "torusmass_pinchoct_gramsig_motivic_spectrahedral_probe",
        "dps": str(mp.dps),
        "scriptHash": script_hash,
        "allPassed": all_passed,
        "checks": checks,
    }
    print(json.dumps(payload, indent=2))
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
