#!/usr/bin/env python3
"""80-dps mpmath and exact rational verification probe for Round 67 theorems:
  - qou-ales: classical_values_at_one (DiprotonResponseClosedForm.lean)
  - qou-edt7: bind_three_and_four_ursell_reconstruct (CoordinationWeightDifferences.lean)
  - qou-gr3t: trace_bond_pair_eq_prod_single_bonds (MarkovBondFactor.lean)
  - qou-qve5: bondSum_mirror_diff_cut_invariant (BondCutSymmetry.lean)
  - qou-vwu3: parityRatioSlope_at_one_and_cayley (BondChannelTzParity.lean)
"""

from fractions import Fraction
import mpmath as mp

mp.mp.dps = 80


def verify_diproton_classical_at_one() -> dict:
    q = Fraction(1, 1)
    nuc_poly = (
        q**18 - 3 * q**16 + 7 * q**14 - 8 * q**12 + 10 * q**10
        - 9 * q**8 + 10 * q**6 - 6 * q**4 + 3 * q**2 - 1
    )
    resp_poly = q**10 - q**8 + 4 * q**6 - 4 * q**4 + 2 * q**2 - 1
    resp_coeff = (q**2 * (q**4 + q**2 + 1) * resp_poly) / ((q**2 + 1) * nuc_poly)
    resp_pp = ((q**2 - 1) ** 2 * (q**4 + q**2 + 1) * resp_poly) / ((q**2 + 1) * nuc_poly)
    nuc_tr = ((q**4 + 1) * nuc_poly) / (4 * q**9 * (q**2 + 1) ** 2)
    assert nuc_poly == Fraction(4, 1)
    assert resp_poly == Fraction(1, 1)
    assert resp_coeff == Fraction(3, 8)
    assert resp_pp == Fraction(0, 1)
    assert nuc_tr == Fraction(1, 2)
    return {
        "name": "classical_values_at_one",
        "bean": "qou-ales",
        "responseCoeff_1": "3/8",
        "nucleonTrace_1": "1/2",
        "passed": True,
    }


def verify_coordination_ursell_reconstruct() -> dict:
    w1, w2, w3 = Fraction(11, 5), Fraction(17, 7), Fraction(29, 9)
    bind2 = 1 * w1
    bind3 = 3 * w2
    bind4 = 6 * w3
    b3 = bind3 - 3 * bind2
    b4 = bind4 - 4 * bind3 + 6 * bind2
    assert bind3 == 3 * w1 + b3
    assert bind4 == 6 * w1 + 4 * b3 + b4
    return {
        "name": "bind_three_and_four_ursell_reconstruct",
        "bean": "qou-edt7",
        "bind3": str(bind3),
        "bind4": str(bind4),
        "passed": True,
    }


def verify_markov_bond_pair_product() -> dict:
    z_param = Fraction(8, 13)
    c1, d1 = Fraction(3, 5), Fraction(-2, 7)
    c2, d2 = Fraction(5, 9), Fraction(4, 11)
    tr1 = c1 * z_param + d1
    tr2 = c2 * z_param + d2
    tr_pair = (c1 * c2) * (z_param * z_param) + (c1 * d2 + d1 * c2) * z_param + d1 * d2
    assert tr_pair == tr1 * tr2
    return {
        "name": "trace_bond_pair_eq_prod_single_bonds",
        "bean": "qou-gr3t",
        "pairTrace": str(tr_pair),
        "passed": True,
    }


def verify_bond_cut_mirror_diff() -> dict:
    epp, epn, enn = Fraction(7, 5), Fraction(9, 4), Fraction(8, 5)
    k = Fraction(6, 1)
    z, n = Fraction(8, 1), Fraction(6, 1)
    for npn in [Fraction(3, 1), Fraction(11, 2), Fraction(19, 3)]:
        b_zn = epp * (k * z - npn) + epn * (2 * npn) + enn * (k * n - npn)
        b_nz = epp * (k * n - npn) + epn * (2 * npn) + enn * (k * z - npn)
        assert b_zn - b_nz == k * (epp - enn) * (z - n)
    return {
        "name": "bondSum_mirror_diff_cut_invariant",
        "bean": "qou-qve5",
        "mirrorDiff": str(k * (epp - enn) * (z - n)),
        "passed": True,
    }


def verify_parity_ratio_slope_cayley() -> dict:
    assert (Fraction(1, 1) ** 4 - 1) / (Fraction(1, 1) ** 4 + 1) == Fraction(0, 1)
    q = mp.mpf("110998") / mp.mpf("100000")
    s = (q**4 - 1) / (q**4 + 1)
    err1 = abs((1 + s) * (q**4 + 1) - 2 * q**4)
    err2 = abs((1 - s) * (q**4 + 1) - 2)
    tol = mp.mpf(10) ** (-75)
    assert err1 < tol
    assert err2 < tol
    return {
        "name": "parityRatioSlope_at_one_and_cayley",
        "bean": "qou-vwu3",
        "cayleyResidual80dps": mp.nstr(max(err1, err2), 25),
        "passed": True,
    }


def main() -> dict:
    checks = [
        verify_diproton_classical_at_one(),
        verify_coordination_ursell_reconstruct(),
        verify_markov_bond_pair_product(),
        verify_bond_cut_mirror_diff(),
        verify_parity_ratio_slope_cayley(),
    ]
    return {
        "probe": "diproton_coordination_markov_cut_parity_probe",
        "dps": 80,
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }


if __name__ == "__main__":
    res = main()
    assert res["allPassed"]
    print(f"PASS: {len(res['checks'])} checks verified at 80 dps / exact Fraction.")
