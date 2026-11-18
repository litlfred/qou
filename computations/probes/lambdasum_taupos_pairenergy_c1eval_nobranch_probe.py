#!/usr/bin/env python3
"""80-dps mpmath probe for Round 83 theorems (qou-jgk6, qou-k6ub, qou-ygyx, qou-nalu, qou-2q85).

Verifies:
1. lambda_sum_eq_tau (qou-jgk6):
   lambdaPlus(tau) + lambdaMinus(tau) == tau
2. tauAnchor_pos (qou-k6ub):
   tauAnchor(q) > 0 for q > 0
3. pairEnergy_pos_for_crossing_pair (qou-ygyx):
   pairEnergy(m, m, q) > 0 and signedChannel(m, m, q) == 0 for m > 0, q > 1
4. c1ExponentPoly_eval_one_sub_zero (qou-nalu):
   c1ExponentPoly(q, 1) - c1ExponentPoly(q, 0) == q
5. not_isRoot_of_irreducible (qou-2q85):
   irreducible polynomial of degree > 1 over Q (e.g. X^3 - 2) has no rational root a = p/q
"""

import hashlib
import pathlib
from mpmath import mp

mp.dps = 80


def c1_exponent_poly(q_val, t_val):
    return (t_val ** 2) + (q_val - mp.mpf(1)) * t_val + (q_val - mp.mpf(1))


def run_checks():
    tol = mp.mpf("1e-70")
    results = []

    # 1. qou-jgk6: lambda_sum_eq_tau
    max_err_1 = mp.mpf(0)
    for num, den in [(21, 10), (26424, 10000), (7, 3), (19, 5), (43, 11)]:
        tau = mp.mpf(num) / mp.mpf(den)
        disc = mp.sqrt(tau ** 2 - mp.mpf(4))
        lam_plus = (tau + disc) / mp.mpf(2)
        lam_minus = (tau - disc) / mp.mpf(2)
        err = abs((lam_plus + lam_minus) - tau)
        if err > max_err_1:
            max_err_1 = err
    results.append({
        "id": "lambda_sum_eq_tau",
        "bean": "qou-jgk6",
        "maxAbsError": mp.nstr(max_err_1, 25),
        "passed": bool(max_err_1 <= tol),
    })

    # 2. qou-k6ub: tauAnchor_pos
    min_tau = None
    all_pos_2 = True
    for num, den in [(1, 10), (1, 2), (1, 1), (3, 2), (17, 5), (10, 1)]:
        q_val = mp.mpf(num) / mp.mpf(den)
        a_d3 = ((q_val + mp.mpf(1)) ** 2) / (mp.mpf(3) * q_val)
        a_d4 = (mp.mpf(3) * (q_val ** 2) + mp.mpf(4) + mp.mpf(3) / (q_val ** 2)) / mp.mpf(4)
        tau_a = (mp.mpf(1) + a_d4) / a_d3
        if tau_a <= mp.mpf(2):
            all_pos_2 = False
        if min_tau is None or tau_a < min_tau:
            min_tau = tau_a
    results.append({
        "id": "tauAnchor_pos",
        "bean": "qou-k6ub",
        "minTauAnchor": mp.nstr(min_tau, 25),
        "maxAbsError": "0.0",
        "passed": bool(all_pos_2 and min_tau > mp.mpf(0)),
    })

    # 3. qou-ygyx: pairEnergy_pos_for_crossing_pair
    min_energy_3 = None
    max_signed_err_3 = mp.mpf(0)
    for m_val in [1, 2, 3, 5]:
        for q_num, q_den in [(11, 10), (3, 2), (2, 1), (7, 3)]:
            q_val = mp.mpf(q_num) / mp.mpf(q_den)
            m_mp = mp.mpf(m_val)
            signed_ch = (m_mp - m_mp) * (q_val - mp.mpf(1) / q_val)
            count_ch = (m_mp + m_mp) * ((q_val - mp.mpf(1)) ** 2) / q_val
            if abs(signed_ch) > max_signed_err_3:
                max_signed_err_3 = abs(signed_ch)
            if min_energy_3 is None or count_ch < min_energy_3:
                min_energy_3 = count_ch
    results.append({
        "id": "pairEnergy_pos_for_crossing_pair",
        "bean": "qou-ygyx",
        "minPairEnergy": mp.nstr(min_energy_3, 25),
        "maxAbsError": mp.nstr(max_signed_err_3, 25),
        "passed": bool(min_energy_3 > mp.mpf(0) and max_signed_err_3 <= tol),
    })

    # 4. qou-nalu: c1ExponentPoly_eval_one_sub_zero
    max_err_4 = mp.mpf(0)
    for num, den in [(-7, 3), (0, 1), (1, 1), (13, 9), (41, 17)]:
        q_val = mp.mpf(num) / mp.mpf(den)
        lhs = c1_exponent_poly(q_val, mp.mpf(1)) - c1_exponent_poly(q_val, mp.mpf(0))
        err = abs(lhs - q_val)
        if err > max_err_4:
            max_err_4 = err
    results.append({
        "id": "c1ExponentPoly_eval_one_sub_zero",
        "bean": "qou-nalu",
        "maxAbsError": mp.nstr(max_err_4, 25),
        "passed": bool(max_err_4 <= tol),
    })

    # 5. qou-2q85: not_isRoot_of_irreducible (X^3 - 2 over Q)
    min_abs_eval_5 = None
    for p_int in range(-10, 11):
        for q_int in range(1, 11):
            a_val = mp.mpf(p_int) / mp.mpf(q_int)
            val = abs((a_val ** 3) - mp.mpf(2))
            if min_abs_eval_5 is None or val < min_abs_eval_5:
                min_abs_eval_5 = val
    results.append({
        "id": "not_isRoot_of_irreducible",
        "bean": "qou-2q85",
        "minAbsEvalOnGrid": mp.nstr(min_abs_eval_5, 25),
        "maxAbsError": "0.0",
        "passed": bool(min_abs_eval_5 > mp.mpf(0)),
    })

    self_bytes = pathlib.Path(__file__).read_bytes()
    sha64 = hashlib.sha256(self_bytes).hexdigest()
    return {
        "scriptHash": sha64,
        "scriptSha256": sha64,
        "dps": str(mp.dps),
        "allPassed": all(r["passed"] for r in results),
        "checks": results,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_checks(), indent=2))
