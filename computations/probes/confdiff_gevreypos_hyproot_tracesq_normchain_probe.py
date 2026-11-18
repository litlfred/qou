#!/usr/bin/env python3
"""80-dps mpmath probe for Round 82 theorems (qou-lhsb, b9ms, qou-4mrb, qou-kyik, qou-j0j8).

Verifies:
1. additive_correction_diff_confined (qou-lhsb):
   |delta1 - delta2| <= 2 * eps when |m_pred + delta1 - m_obs| <= eps and |m_pred + delta2 - m_obs| <= eps
2. one_le_four_pow_mul_involution_sq (b9ms):
   1 <= 4**n * I(n)**2 for n >= 0
3. binding_kernel_eval_root (qou-4mrb):
   lam**2 - (lam + 1/lam)*lam + 1 == 0 for lam != 0
4. binding_trace_sq_eq_four_add_four_sinh_sq (qou-kyik):
   (2 * cosh(theta))**2 == 4 + 4 * sinh(theta)**2
5. normalizations_chain_rule (qou-j0j8):
   ((c / b2) / (c / b1)) * ((c / b3) / (c / b2)) == b1 / b3
"""

import hashlib
import pathlib
from mpmath import mp

mp.dps = 80


def involution_number(n: int) -> int:
    if n <= 1:
        return 1
    a, b = 1, 1
    for k in range(2, n + 1):
        a, b = b, b + (k - 1) * a
    return b


def run_checks():
    tol = mp.mpf("1e-70")
    results = []

    # 1. qou-lhsb: additive_correction_diff_confined
    m_pred = mp.mpf("938272088") / mp.mpf("1000000")
    m_obs = mp.mpf("938272081") / mp.mpf("1000000")
    eps = mp.mpf("1") / mp.mpf("10000")
    max_violation_1 = mp.mpf(0)
    for d1_num, d2_num in [(-8, 9), (7, -6), (-9, -9), (9, -9)]:
        delta1 = (m_obs - m_pred) + mp.mpf(d1_num) * eps / mp.mpf(10)
        delta2 = (m_obs - m_pred) + mp.mpf(d2_num) * eps / mp.mpf(10)
        assert abs(m_pred + delta1 - m_obs) <= eps
        assert abs(m_pred + delta2 - m_obs) <= eps
        diff = abs(delta1 - delta2)
        viol = max(mp.mpf(0), diff - mp.mpf(2) * eps)
        if viol > max_violation_1:
            max_violation_1 = viol
    results.append({
        "id": "additive_correction_diff_confined",
        "bean": "qou-lhsb",
        "maxAbsError": mp.nstr(max_violation_1, 25),
        "passed": bool(max_violation_1 <= tol),
    })

    # 2. b9ms: one_le_four_pow_mul_involution_sq
    all_ge_one = True
    min_val_2 = None
    for n_val in range(0, 15):
        inv_n = involution_number(n_val)
        val = (4 ** n_val) * (inv_n ** 2)
        if val < 1:
            all_ge_one = False
        if min_val_2 is None or val < min_val_2:
            min_val_2 = val
    results.append({
        "id": "one_le_four_pow_mul_involution_sq",
        "bean": "b9ms",
        "minValue": str(min_val_2),
        "maxAbsError": "0.0",
        "passed": bool(all_ge_one and min_val_2 >= 1),
    })

    # 3. qou-4mrb: binding_kernel_eval_root
    max_err_3 = mp.mpf(0)
    for num, den in [(3, 2), (7, 5), (-11, 4), (23, 17), (41, 13)]:
        lam = mp.mpf(num) / mp.mpf(den)
        lhs = lam ** 2 - (lam + mp.mpf(1) / lam) * lam + mp.mpf(1)
        err = abs(lhs)
        if err > max_err_3:
            max_err_3 = err
    results.append({
        "id": "binding_kernel_eval_root",
        "bean": "qou-4mrb",
        "maxAbsError": mp.nstr(max_err_3, 25),
        "passed": bool(max_err_3 <= tol),
    })

    # 4. qou-kyik: binding_trace_sq_eq_four_add_four_sinh_sq
    max_err_4 = mp.mpf(0)
    for num, den in [(0, 1), (3, 10), (78145, 100000), (-5, 7), (19, 11)]:
        theta = mp.mpf(num) / mp.mpf(den)
        lhs = (mp.mpf(2) * mp.cosh(theta)) ** 2
        rhs = mp.mpf(4) + mp.mpf(4) * (mp.sinh(theta) ** 2)
        err = abs(lhs - rhs)
        if err > max_err_4:
            max_err_4 = err
    results.append({
        "id": "binding_trace_sq_eq_four_add_four_sinh_sq",
        "bean": "qou-kyik",
        "maxAbsError": mp.nstr(max_err_4, 25),
        "passed": bool(max_err_4 <= tol),
    })

    # 5. qou-j0j8: normalizations_chain_rule
    max_err_5 = mp.mpf(0)
    for c_s, b1_s, b2_s, b3_s in [
        ("297/1000", "2224566/1000000", "380132/1000000", "4708/10000"),
        ("17/5", "13/7", "29/11", "43/19"),
        ("-23/9", "31/14", "-19/6", "37/8"),
    ]:
        c_v = mp.mpf(c_s.split("/")[0]) / mp.mpf(c_s.split("/")[1])
        b1_v = mp.mpf(b1_s.split("/")[0]) / mp.mpf(b1_s.split("/")[1])
        b2_v = mp.mpf(b2_s.split("/")[0]) / mp.mpf(b2_s.split("/")[1])
        b3_v = mp.mpf(b3_s.split("/")[0]) / mp.mpf(b3_s.split("/")[1])
        lhs = ((c_v / b2_v) / (c_v / b1_v)) * ((c_v / b3_v) / (c_v / b2_v))
        rhs = b1_v / b3_v
        err = abs(lhs - rhs)
        if err > max_err_5:
            max_err_5 = err
    results.append({
        "id": "normalizations_chain_rule",
        "bean": "qou-j0j8",
        "maxAbsError": mp.nstr(max_err_5, 25),
        "passed": bool(max_err_5 <= tol),
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
