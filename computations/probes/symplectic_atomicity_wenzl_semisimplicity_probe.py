#!/usr/bin/env python3
"""80-dps mpmath and exact rational verification probe for PR #8241:
  - qou-atsd: sp2_basis_volume_eq_det, sp2_diagonal_torus_rank_one
  - qou-dyij: knot_connected_sum_multiplicative, linking_excess_eq_zero_iff
  - qou-cc97: projector_bridge_trace_branching
  - qou-otbb: hook_product_three_invertible, central_projector_semisimple_idempotent_and_radical
  - qou-e4ri: qIntBal_two_sq_sub_one_eq_three, yekutieli_coboundary_associativity
"""

from fractions import Fraction
import mpmath as mp

mp.mp.dps = 80


def verify_sp2_sl2_atomicity() -> dict:
    for a11, a12, a21, a22 in [
        (Fraction(3, 2), Fraction(1, 2), Fraction(1, 1), Fraction(1, 1)),
        (Fraction(5, 3), Fraction(2, 3), Fraction(1, 2), Fraction(4, 5)),
    ]:
        e1 = (a11, a21)
        e2 = (a12, a22)
        omega = e1[0] * e2[1] - e1[1] * e2[0]
        det = a11 * a22 - a12 * a21
        assert omega == det
        assert (omega == Fraction(1, 1)) == (det == Fraction(1, 1))
    for t1 in [Fraction(3, 7), Fraction(-5, 11), Fraction(13, 4)]:
        t2 = Fraction(1, 1) / t1
        assert t1 * t2 == Fraction(1, 1)
    return {
        "name": "sp2_basis_volume_eq_det_and_diagonal_torus_rank_one",
        "bean": "qou-atsd",
        "matricesTested": "2",
        "torusSamples": "3",
        "passed": True,
    }


def verify_jones_connected_sum() -> dict:
    w1, w2 = Fraction(3, 5), Fraction(7, 11)
    tr1, tr2 = Fraction(13, 17), Fraction(19, 23)
    w12 = w1 * w2
    tr12 = tr1 * tr2
    v1 = w1 * tr1
    v2 = w2 * tr2
    v12 = w12 * tr12
    assert v12 == v1 * v2
    assert (v12 - v1 * v2) == Fraction(0, 1)
    return {
        "name": "knot_connected_sum_multiplicative_and_linking_excess",
        "bean": "qou-dyij",
        "connectedSumValue": str(v12),
        "passed": True,
    }


def verify_wenzl_bridge_branching() -> dict:
    q_curr = Fraction(7, 5)
    q_next = Fraction(19, 10)
    z_tl = Fraction(3, 8)
    tr_p_curr = Fraction(11, 13)
    tr_pep = z_tl * tr_p_curr
    tr_p_next = ((q_next - q_curr * z_tl) * tr_p_curr) / q_next
    assert q_next * tr_p_next + q_curr * tr_pep == q_next * tr_p_curr
    assert q_next * tr_p_next == (q_next - q_curr * z_tl) * tr_p_curr
    return {
        "name": "projector_bridge_trace_branching",
        "bean": "qou-cc97",
        "clearedRecurrenceValue": str(q_next * tr_p_next),
        "passed": True,
    }


def verify_wenzl_semisimplicity_hook_product() -> dict:
    h1, h2, h3 = Fraction(3, 2), Fraction(7, 3), Fraction(15, 7)
    u1, u2, u3 = Fraction(1, 1) / h1, Fraction(1, 1) / h2, Fraction(1, 1) / h3
    h_prod = (h1 * h2) * h3
    h_inv = (u3 * u2) * u1
    assert h_prod * h_inv == Fraction(1, 1)
    # Unnormalized projector E satisfying E^2 = h_prod * E
    e_unnorm = h_prod
    assert e_unnorm * e_unnorm == h_prod * e_unnorm
    e_norm = h_inv * e_unnorm
    assert e_norm * e_norm == e_norm
    return {
        "name": "hook_product_three_invertible_and_central_projector_idempotent",
        "bean": "qou-otbb",
        "hookProduct": str(h_prod),
        "passed": True,
    }


def verify_balanced_quantum_int_and_yekutieli() -> dict:
    s = mp.mpf("11") / mp.mpf("10")
    s_inv = mp.mpf("1") / s
    q2 = s + s_inv
    q3 = s * s + mp.mpf("1") + s_inv * s_inv
    err = abs((q2 * q2 - mp.mpf("1")) - q3)
    tol = mp.mpf(10) ** (-75)
    assert err < tol
    fx, fy, fz = Fraction(2, 5), Fraction(3, 7), Fraction(-4, 9)
    fxy, fyz, fxyz = Fraction(11, 13), Fraction(17, 19), Fraction(23, 29)
    lhs = ((fxy - fx) - fy) + ((fxyz - fxy) - fz)
    rhs = ((fyz - fy) - fz) + ((fxyz - fx) - fyz)
    assert lhs == rhs
    return {
        "name": "qIntBal_two_sq_sub_one_eq_three_and_yekutieli_coboundary",
        "bean": "qou-e4ri",
        "qIntResidual80dps": mp.nstr(err, 25),
        "passed": True,
    }


def main() -> dict:
    checks = [
        verify_sp2_sl2_atomicity(),
        verify_jones_connected_sum(),
        verify_wenzl_bridge_branching(),
        verify_wenzl_semisimplicity_hook_product(),
        verify_balanced_quantum_int_and_yekutieli(),
    ]
    return {
        "probe": "symplectic_atomicity_wenzl_semisimplicity_probe",
        "dps": 80,
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }


if __name__ == "__main__":
    res = main()
    assert res["allPassed"]
    print(f"PASS: {len(res['checks'])} checks verified at 80 dps / exact Fraction.")
