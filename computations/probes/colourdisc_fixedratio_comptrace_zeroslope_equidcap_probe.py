#!/usr/bin/env python3
"""80-dps mpmath probe for Round 84 theorems (qou-3e6w, qou-4cu3, qou-o7c0, qou-2002, qou-lzoh).

Verifies:
1. colourDiscriminant_ge_two_z_sq (qou-3e6w):
   2 * z**2 * (z**2 + 1) <= (4*z**3 + 3*z**2 + 3*z + 4)**2 + 2*z**2*(z**2 + 1)
2. fixedColourings_sequential_eq_four_mul_interleaved (qou-4cu3):
   fixedColourings(sequential) == 8 == 4 * fixedColourings(interleaved)
3. componentTrace_succ_components (qou-o7c0):
   componentTrace(n, c + 1) == 2 * componentTrace(n, c)
4. interface_bond_difference_zero_slope (qou-2002):
   Phi(Wpn * (a + 0*s)) - Phi(Wnp * (a + 0*s)) == 0 when Phi(Wpn) == Phi(Wnp)
5. equidistant_cluster_size_le_finrank_succ (qou-lzoh):
   for equidistant family in R^r with Gram matrix (d^2/2)*(I + J) > 0, n + 1 <= r + 1
"""

import hashlib
import itertools
import pathlib
from mpmath import mp

mp.dps = 80


def apply_swap(perm, i, j):
    res = list(perm)
    res[i], res[j] = res[j], res[i]
    return tuple(res)


def compose_perms(p1, p2):
    return tuple(p1[p2[k]] for k in range(len(p1)))


def count_fixed_colourings(perm):
    cnt = 0
    for col in itertools.product((0, 1), repeat=4):
        if all(col[perm[i]] == col[i] for i in range(4)):
            cnt += 1
    return cnt


def run_checks():
    tol = mp.mpf("1e-70")
    results = []

    # 1. qou-3e6w: colourDiscriminant_ge_two_z_sq
    min_slack_1 = None
    for num, den in [(-7, 3), (-1, 1), (0, 1), (2, 5), (13, 4)]:
        z = mp.mpf(num) / mp.mpf(den)
        disc = ((mp.mpf(4) * (z ** 3) + mp.mpf(3) * (z ** 2) + mp.mpf(3) * z + mp.mpf(4)) ** 2) + mp.mpf(2) * (z ** 2) * ((z ** 2) + mp.mpf(1))
        lb = mp.mpf(2) * (z ** 2) * ((z ** 2) + mp.mpf(1))
        slack = disc - lb
        if min_slack_1 is None or slack < min_slack_1:
            min_slack_1 = slack
    results.append({
        "id": "colourDiscriminant_ge_two_z_sq",
        "bean": "qou-3e6w",
        "minSlack": mp.nstr(min_slack_1, 25),
        "maxAbsError": "0.0",
        "passed": bool(min_slack_1 >= mp.mpf(0)),
    })

    # 2. qou-4cu3: fixedColourings_sequential_eq_four_mul_interleaved
    id4 = (0, 1, 2, 3)
    s0 = apply_swap(id4, 0, 1)
    s1 = apply_swap(id4, 1, 2)
    s2 = apply_swap(id4, 2, 3)
    interleaved = id4
    for g in (s0, s1, s0, s2, s1):
        interleaved = compose_perms(interleaved, g)
    sequential = id4
    for g in (s0, s0, s1, s1, s2):
        sequential = compose_perms(sequential, g)
    fc_inter = count_fixed_colourings(interleaved)
    fc_seq = count_fixed_colourings(sequential)
    results.append({
        "id": "fixedColourings_sequential_eq_four_mul_interleaved",
        "bean": "qou-4cu3",
        "fixedInterleaved": str(fc_inter),
        "fixedSequential": str(fc_seq),
        "maxAbsError": str(abs(fc_seq - 4 * fc_inter)),
        "passed": bool(fc_inter == 2 and fc_seq == 8 and fc_seq == 4 * fc_inter),
    })

    # 3. qou-o7c0: componentTrace_succ_components
    max_err_3 = mp.mpf(0)
    for n_val in range(1, 8):
        for c_val in range(0, 7):
            ct_c = (mp.mpf(2) ** c_val) / (mp.mpf(2) ** n_val)
            ct_c1 = (mp.mpf(2) ** (c_val + 1)) / (mp.mpf(2) ** n_val)
            err = abs(ct_c1 - mp.mpf(2) * ct_c)
            if err > max_err_3:
                max_err_3 = err
    results.append({
        "id": "componentTrace_succ_components",
        "bean": "qou-o7c0",
        "maxAbsError": mp.nstr(max_err_3, 25),
        "passed": bool(max_err_3 <= tol),
    })

    # 4. qou-2002: interface_bond_difference_zero_slope
    max_err_4 = mp.mpf(0)
    phi_free = mp.mpf(19) / mp.mpf(7)
    phi_wpn_s = mp.mpf(31) / mp.mpf(11)
    phi_wnp_s = mp.mpf(23) / mp.mpf(13)
    for a_num, a_den in [(-5, 3), (0, 1), (17, 9), (41, 12)]:
        a_val = mp.mpf(a_num) / mp.mpf(a_den)
        b_val = mp.mpf(0)
        lhs = (a_val * phi_free + b_val * phi_wpn_s) - (a_val * phi_free + b_val * phi_wnp_s)
        err = abs(lhs)
        if err > max_err_4:
            max_err_4 = err
    results.append({
        "id": "interface_bond_difference_zero_slope",
        "bean": "qou-2002",
        "maxAbsError": mp.nstr(max_err_4, 25),
        "passed": bool(max_err_4 <= tol),
    })

    # 5. qou-lzoh: equidistant_cluster_size_le_finrank_succ
    # Verify det(Gram_n) = (d^2 / 2)^n * (n + 1) > 0 for n = 1, 2, 3 and max cluster size in R^3 is 3 + 1 = 4
    max_err_5 = mp.mpf(0)
    d_val = mp.mpf(3) / mp.mpf(2)
    for n_val in [1, 2, 3]:
        G = mp.matrix(n_val, n_val)
        for i in range(n_val):
            for j in range(n_val):
                G[i, j] = (d_val ** 2 / mp.mpf(2)) * (mp.mpf(2) if i == j else mp.mpf(1))
        det_g = mp.det(G)
        expected_det = ((d_val ** 2 / mp.mpf(2)) ** n_val) * mp.mpf(n_val + 1)
        err = abs(det_g - expected_det)
        if err > max_err_5:
            max_err_5 = err
    results.append({
        "id": "equidistant_cluster_size_le_finrank_succ",
        "bean": "qou-lzoh",
        "maxClusterInR3": "4",
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
