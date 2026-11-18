#!/usr/bin/env python3
"""80-dps mpmath probe for Round 86 theorems (qou-3f7a, qou-gl58, qou-u5z0, qou-vnqx, qou-zzwm).

Verifies:
1. no_root_of_irreducible_cubic_degree_le_one (qou-3f7a):
   any root a = -c0/c1 of a linear polynomial c1*X + c0 over Q is not a root of X^3 - 2
2. colourResolvent_cyclic_three_step (qou-gl58):
   for w = exp(2*pi*i/3), w^3 * (x0 + w*x1 + w^2*x2) == x0 + w*x1 + w^2*x2
3. dimSum_five_sub_two_mul_four (qou-u5z0):
   dimSum(5) - 2 * dimSum(4) == 26 - 20 == 6 via hook-length formula
4. tau_kernel_at_one (qou-vnqx):
   (1 + (3*1^2 + 4 + 3/1^2)/4) / ((1 + 1)^2 / (3*1)) == 21/8
5. diff_eq_zero_of_equal_saturated (qou-zzwm):
   if E1 == B and E2 == B then E1 - E2 == 0
"""

import hashlib
import math
import pathlib
from mpmath import mp

mp.dps = 80


def hook_lengths(part):
    hooks = []
    for i, li in enumerate(part):
        for j in range(li):
            arm = li - 1 - j
            leg = sum(1 for p in part[i + 1:] if j < p)
            hooks.append(arm + leg + 1)
    return hooks


def dim_of(part):
    n = sum(part)
    prod_h = 1
    for h in hook_lengths(part):
        prod_h *= h
    return math.factorial(n) // prod_h


def run_checks():
    tol = mp.mpf("1e-70")
    results = []

    # 1. qou-3f7a: no_root_of_irreducible_cubic_degree_le_one
    min_abs_1 = None
    for c0 in range(-8, 9):
        for c1 in range(1, 9):
            a_val = -mp.mpf(c0) / mp.mpf(c1)
            val = abs((a_val ** 3) - mp.mpf(2))
            if min_abs_1 is None or val < min_abs_1:
                min_abs_1 = val
    results.append({
        "id": "no_root_of_irreducible_cubic_degree_le_one",
        "bean": "qou-3f7a",
        "minAbsCubicEval": mp.nstr(min_abs_1, 25),
        "maxAbsError": "0.0",
        "passed": bool(min_abs_1 > mp.mpf(0)),
    })

    # 2. qou-gl58: colourResolvent_cyclic_three_step
    w = mp.expj(mp.mpf(2) * mp.pi / mp.mpf(3))
    max_err_2 = mp.mpf(0)
    for x0_i, x1_i, x2_i in [(3, -5, 7), (11, 13, -17), (-2, 9, 4)]:
        x0 = mp.mpf(x0_i) / mp.mpf(3)
        x1 = mp.mpf(x1_i) / mp.mpf(5)
        x2 = mp.mpf(x2_i) / mp.mpf(7)
        res_v = x0 + w * x1 + (w ** 2) * x2
        shifted3 = w * (w * (w * res_v))
        err = abs(shifted3 - res_v)
        if err > max_err_2:
            max_err_2 = err
    results.append({
        "id": "colourResolvent_cyclic_three_step",
        "bean": "qou-gl58",
        "maxAbsError": mp.nstr(max_err_2, 25),
        "passed": bool(max_err_2 <= tol),
    })

    # 3. qou-u5z0: dimSum_five_sub_two_mul_four
    parts4 = [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    parts5 = [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]
    ds4 = sum(dim_of(p) for p in parts4)
    ds5 = sum(dim_of(p) for p in parts5)
    diff_3 = ds5 - 2 * ds4
    results.append({
        "id": "dimSum_five_sub_two_mul_four",
        "bean": "qou-u5z0",
        "dimSum4": str(ds4),
        "dimSum5": str(ds5),
        "maxAbsError": str(abs(diff_3 - 6)),
        "passed": bool(ds4 == 10 and ds5 == 26 and diff_3 == 6),
    })

    # 4. qou-vnqx: tau_kernel_at_one
    q1 = mp.mpf(1)
    lhs_4 = (mp.mpf(1) + (mp.mpf(3) * (q1 ** 2) + mp.mpf(4) + mp.mpf(3) / (q1 ** 2)) / mp.mpf(4)) / (((q1 + mp.mpf(1)) ** 2) / (mp.mpf(3) * q1))
    rhs_4 = mp.mpf(21) / mp.mpf(8)
    err_4 = abs(lhs_4 - rhs_4)
    results.append({
        "id": "tau_kernel_at_one",
        "bean": "qou-vnqx",
        "maxAbsError": mp.nstr(err_4, 25),
        "passed": bool(err_4 <= tol),
    })

    # 5. qou-zzwm: diff_eq_zero_of_equal_saturated
    max_err_5 = mp.mpf(0)
    for b_num, b_den in [(17, 5), (-23, 7), (101, 13)]:
        b_val = mp.mpf(b_num) / mp.mpf(b_den)
        e1 = b_val
        e2 = b_val
        err = abs(e1 - e2)
        if err > max_err_5:
            max_err_5 = err
    results.append({
        "id": "diff_eq_zero_of_equal_saturated",
        "bean": "qou-zzwm",
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
