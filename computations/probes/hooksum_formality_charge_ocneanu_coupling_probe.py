#!/usr/bin/env python3
"""80-dps mpmath and exact rational verification probe for Round 64 theorems:
  - qou-0ie7: six_mul_hminClosed, hminClosed_step_continuity (HookSumRowTangentBound.lean)
  - qou-2akx: additive_map_pow_and_mul_three (FormalityBridgeF1.lean)
  - qou-bn8e: octet_em_left_inverse_and_sigma_span (ChargeQuadraticSumRule.lean)
  - qou-bsec: markovWeights_three_sum_and_classical_values (OcneanuWeightMarkov3.lean)
  - qou-8274: isCoupling_of_ne_iff_boundary_strand, coupled_consecutive_pair (ContiguousCouplingGraph.lean)
"""

from fractions import Fraction
import mpmath as mp

mp.mp.dps = 80


def hmin_closed(k: int, r: int) -> int:
    return sum(d * d for d in range(k + 1)) + r * (k + 1)


def verify_hooksum_closed_and_continuity() -> dict:
    for k in range(0, 25):
        for r in range(0, k + 2):
            lhs = 6 * hmin_closed(k, r)
            rhs = k * (k + 1) * (2 * k + 1) + 6 * r * (k + 1)
            assert lhs == rhs
        assert hmin_closed(k, k + 1) == hmin_closed(k + 1, 0)
    return {
        "name": "six_mul_hminClosed_and_hminClosed_step_continuity",
        "bean": "qou-0ie7",
        "kMaxTested": "24",
        "hminClosed_4_2": str(hmin_closed(4, 2)),
        "passed": True,
    }


def verify_formality_bridge_additive_pow_mul3() -> dict:
    x = mp.mpf("17") / mp.mpf("11")
    y = mp.mpf("23") / mp.mpf("13")
    z = mp.mpf("29") / mp.mpf("19")
    tol = mp.mpf(10) ** (-75)
    max_err = mp.mpf("0")
    for n in range(0, 12):
        err_pow = abs(mp.log(x**n) - mp.mpf(n) * mp.log(x))
        if err_pow > max_err:
            max_err = err_pow
        assert err_pow < tol
    err_mul3 = abs(mp.log(x * y * z) - (mp.log(x) + mp.log(y) + mp.log(z)))
    assert err_mul3 < tol
    return {
        "name": "additive_map_pow_and_mul_three",
        "bean": "qou-2akx",
        "maxPowResidual80dps": mp.nstr(max_err, 25),
        "mul3Residual80dps": mp.nstr(err_mul3, 25),
        "passed": True,
    }


def verify_octet_em_left_inverse_and_sigma_span() -> dict:
    q_u = Fraction(2, 3)
    q_d = Fraction(-1, 3)
    q_s = Fraction(-1, 3)

    def charge_self(q1: Fraction, q2: Fraction, q3: Fraction) -> Fraction:
        return q1 * q1 + q2 * q2 + q3 * q3

    def charge_inter(q1: Fraction, q2: Fraction, q3: Fraction) -> Fraction:
        return q1 * q2 + q1 * q3 + q2 * q3

    def energy(a: Fraction, b: Fraction, q1: Fraction, q2: Fraction, q3: Fraction) -> Fraction:
        return a * charge_self(q1, q2, q3) + b * charge_inter(q1, q2, q3)

    for a_num in range(-5, 6):
        for b_num in range(-5, 6):
            a = Fraction(a_num, 7)
            b = Fraction(b_num, 11)
            em_plus = energy(a, b, q_u, q_u, q_s)
            em_zero = energy(a, b, q_u, q_d, q_s)
            em_minus = energy(a, b, q_d, q_d, q_s)
            assert 2 * (em_plus - em_zero) + (em_zero - em_minus) == a
            assert (em_plus - em_zero) - (em_zero - em_minus) == b
            assert em_plus - em_minus == (2 * a - b) / Fraction(3, 1)
    return {
        "name": "octet_em_left_inverse_and_sigma_span",
        "bean": "qou-bn8e",
        "gridPairsVerified": "121",
        "passed": True,
    }


def verify_ocneanu_markov3_weights() -> dict:
    def w0(q: Fraction, z: Fraction) -> Fraction:
        return (q * z + 1) * (q**3 * z + q * z + 1) / ((q**2 + 1) * (q**4 + q**2 + 1))

    def w1(q: Fraction, z: Fraction) -> Fraction:
        return q**2 * (z - q) * (z * (q**2 + 1) - q**3) / ((q**2 + 1) * (q**4 + q**2 + 1))

    def w2(q: Fraction, z: Fraction) -> Fraction:
        return -q * (z - q) * (q * z + 1) / (q**4 + q**2 + 1)

    for q in [Fraction(1, 1), Fraction(2, 3), Fraction(5, 4), Fraction(-3, 2)]:
        for z in [Fraction(0, 1), Fraction(1, 3), Fraction(3, 5), Fraction(-2, 7)]:
            assert w0(q, z) + 2 * w2(q, z) + w1(q, z) == Fraction(1, 1)

    assert (w0(Fraction(1, 1), Fraction(0, 1)), w1(Fraction(1, 1), Fraction(0, 1)), w2(Fraction(1, 1), Fraction(0, 1))) == (
        Fraction(1, 6),
        Fraction(1, 6),
        Fraction(1, 3),
    )
    assert (w0(Fraction(1, 1), Fraction(1, 3)), w1(Fraction(1, 1), Fraction(1, 3)), w2(Fraction(1, 1), Fraction(1, 3))) == (
        Fraction(10, 27),
        Fraction(1, 27),
        Fraction(8, 27),
    )
    return {
        "name": "markovWeights_three_sum_and_classical_values",
        "bean": "qou-bsec",
        "plancherel_1_0": ["1/6", "1/6", "1/3"],
        "values_1_oneThird": ["10/27", "1/27", "8/27"],
        "passed": True,
    }


def verify_contiguous_coupling_characterization() -> dict:
    def in_block(k: int, x: int) -> bool:
        return 3 * k <= x < 3 * k + 3

    def is_coupling(i: int, j: int, x: int) -> bool:
        return in_block(i, x) and in_block(j, x + 1)

    for i in range(0, 10):
        for j in range(0, 10):
            for x in range(0, 32):
                if i != j:
                    lhs = is_coupling(i, j, x)
                    rhs = (x == 3 * i + 2) and (j == i + 1)
                    assert lhs == rhs
        assert is_coupling(i, i + 1, 3 * i + 2)
    return {
        "name": "isCoupling_of_ne_iff_boundary_strand_and_coupled_consecutive_pair",
        "bean": "qou-8274",
        "nucleonsTested": "10",
        "strandsTested": "32",
        "passed": True,
    }


def main() -> dict:
    checks = [
        verify_hooksum_closed_and_continuity(),
        verify_formality_bridge_additive_pow_mul3(),
        verify_octet_em_left_inverse_and_sigma_span(),
        verify_ocneanu_markov3_weights(),
        verify_contiguous_coupling_characterization(),
    ]
    return {
        "probe": "hooksum_formality_charge_ocneanu_coupling_probe",
        "dps": 80,
        "allPassed": all(c["passed"] for c in checks),
        "checks": checks,
    }


if __name__ == "__main__":
    res = main()
    assert res["allPassed"]
    print(f"PASS: {len(res['checks'])} checks verified at 80 dps / exact Fraction.")
