#!/usr/bin/env python3
"""80-dps mpmath probe for Round 85 theorems (qou-9nnz, qou-cdx1, qou-ijoi, qou-l2vh, qou-qqyb).

Verifies:
1. step_add_prev_eq_mul (qou-9nnz):
   step(c, a, b) + a == c * b
2. trace_eq_of_rank_eq (qou-cdx1):
   for idempotent matrices P, Q of equal rank r, trace(P) == trace(Q) == r
3. bounded_two_order_sum_le (qou-ijoi):
   |a1*c*h2 + a2*c*h2| <= (B1 + B2)*c*h2 when |a1| <= B1, |a2| <= B2, c >= 0, h2 >= 0
4. eigen_first_sq_of_product_ratio (qou-l2vh):
   if a * b == -1 and a / b == -(q**2), then a**2 == q**2
5. unit_modulus_lt_real_gt_one (qou-qqyb):
   |exp(i * theta)| < q for real theta and q > 1
"""

import hashlib
import pathlib
from mpmath import mp

mp.dps = 80


def run_checks():
    tol = mp.mpf("1e-70")
    results = []

    # 1. qou-9nnz: step_add_prev_eq_mul
    max_err_1 = mp.mpf(0)
    for c_i, a_i, b_i in [(7, -3, 11), (-13, 5, 19), (23, 17, -8)]:
        c_v = mp.mpf(c_i) / mp.mpf(5)
        a_v = mp.mpf(a_i) / mp.mpf(7)
        b_v = mp.mpf(b_i) / mp.mpf(9)
        step_v = c_v * b_v - a_v
        err = abs((step_v + a_v) - (c_v * b_v))
        if err > max_err_1:
            max_err_1 = err
    results.append({
        "id": "step_add_prev_eq_mul",
        "bean": "qou-9nnz",
        "maxAbsError": mp.nstr(max_err_1, 25),
        "passed": bool(max_err_1 <= tol),
    })

    # 2. qou-cdx1: trace_eq_of_rank_eq
    # Construct two distinct rank-1 idempotent 2x2 matrices P and Q and check P^2=P, Q^2=Q, tr(P)==tr(Q)==1
    P = mp.matrix([[mp.mpf(3) / mp.mpf(5), mp.mpf(6) / mp.mpf(25)],
                   [mp.mpf(1), mp.mpf(2) / mp.mpf(5)]])
    Q = mp.matrix([[mp.mpf(1) / mp.mpf(3), mp.mpf(2) / mp.mpf(9)],
                   [mp.mpf(1), mp.mpf(2) / mp.mpf(3)]])
    P2 = P * P
    Q2 = Q * Q
    tr_P = P[0, 0] + P[1, 1]
    tr_Q = Q[0, 0] + Q[1, 1]
    max_err_2 = max(
        abs(tr_P - tr_Q),
        abs(tr_P - mp.mpf(1)),
        max(abs(P2[i, j] - P[i, j]) for i in range(2) for j in range(2)),
        max(abs(Q2[i, j] - Q[i, j]) for i in range(2) for j in range(2)),
    )
    results.append({
        "id": "trace_eq_of_rank_eq",
        "bean": "qou-cdx1",
        "maxAbsError": mp.nstr(max_err_2, 25),
        "passed": bool(max_err_2 <= tol),
    })

    # 3. qou-ijoi: bounded_two_order_sum_le
    c_val = mp.mpf(297) / mp.mpf(1000)
    h2_val = mp.mpf(437062) / mp.mpf(10000000)
    B1 = mp.mpf(2)
    B2 = mp.mpf(3)
    max_viol_3 = mp.mpf(0)
    for a1_n, a2_n in [(-19, 27), (15, -29), (-20, -30), (20, 30)]:
        a1 = mp.mpf(a1_n) / mp.mpf(10)
        a2 = mp.mpf(a2_n) / mp.mpf(10)
        lhs = abs(a1 * c_val * h2_val + a2 * c_val * h2_val)
        rhs = (B1 + B2) * c_val * h2_val
        viol = max(mp.mpf(0), lhs - rhs)
        if viol > max_viol_3:
            max_viol_3 = viol
    results.append({
        "id": "bounded_two_order_sum_le",
        "bean": "qou-ijoi",
        "maxAbsError": mp.nstr(max_viol_3, 25),
        "passed": bool(max_viol_3 <= tol),
    })

    # 4. qou-l2vh: eigen_first_sq_of_product_ratio
    max_err_4 = mp.mpf(0)
    for num, den in [(111, 100), (7, 5), (-13, 9), (29, 17)]:
        q_val = mp.mpf(num) / mp.mpf(den)
        for sign in [1, -1]:
            a_val = mp.mpf(sign) * q_val
            b_val = -mp.mpf(sign) / q_val
            err = max(
                abs(a_val * b_val + mp.mpf(1)),
                abs(a_val / b_val + (q_val ** 2)),
                abs((a_val ** 2) - (q_val ** 2)),
            )
            if err > max_err_4:
                max_err_4 = err
    results.append({
        "id": "eigen_first_sq_of_product_ratio",
        "bean": "qou-l2vh",
        "maxAbsError": mp.nstr(max_err_4, 25),
        "passed": bool(max_err_4 <= tol),
    })

    # 5. qou-qqyb: unit_modulus_lt_real_gt_one
    min_gap_5 = None
    max_mod_err_5 = mp.mpf(0)
    for th_n, th_d in [(0, 1), (3, 7), (-11, 5), (23, 9)]:
        theta = mp.mpf(th_n) / mp.mpf(th_d)
        mod_val = abs(mp.expj(theta))
        mod_err = abs(mod_val - mp.mpf(1))
        if mod_err > max_mod_err_5:
            max_mod_err_5 = mod_err
        for q_n, q_d in [(111, 100), (3, 2), (5, 3)]:
            q_val = mp.mpf(q_n) / mp.mpf(q_d)
            gap = q_val - mod_val
            if min_gap_5 is None or gap < min_gap_5:
                min_gap_5 = gap
    results.append({
        "id": "unit_modulus_lt_real_gt_one",
        "bean": "qou-qqyb",
        "minGap": mp.nstr(min_gap_5, 25),
        "maxAbsError": mp.nstr(max_mod_err_5, 25),
        "passed": bool(min_gap_5 > mp.mpf(0) and max_mod_err_5 <= tol),
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
