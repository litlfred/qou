#!/usr/bin/env python3
"""80-dps mpmath probe for Round 81 theorems (qou-6h6p, qou-e1dc, qou-l2ob, qou-p2d5, qou-ypc5).

Verifies:
1. binding_dressing_free_sub_bound_eq_qbeta_over_h (qou-6h6p):
   (m_e / (q*(q-1))) * net_p * (trFree - trBound) == Q_beta * (trFree - trBound) / h
2. whiteheadLinkPhase_arg_decomp_zero (qou-e1dc):
   -((0 - N/2)**2 * pi / (2*N)) + N * pi / 8 == 0 for N > 0
3. chainRatio_add_two_neutrons (qou-l2ob):
   chainRatio(Z, N+2) == chainRatio(Z, N) * fnn**2 for Z >= 1, N >= 1
4. solMu3_add_three_solMu2 (qou-p2d5):
   solMu3(m2, m3, m4) + 3 * solMu2(m2, m3, m4) == m3
5. weighted_deviation_eq_of_same_bond (qou-ypc5):
   sum_l y_l * dev(atom1)_l == sum_l y_l * dev(atom2)_l when trM(atom1) == trM(atom2) == trM(a)*trM(b)*bond
"""

from mpmath import mp

mp.dps = 80


def run_checks():
    tol = mp.mpf("1e-70")
    results = []

    # 1. qou-6h6p: binding_dressing_free_sub_bound_eq_qbeta_over_h
    m_e = mp.mpf("51099895") / mp.mpf("100000000")
    q_val = mp.mpf(3)
    h_val = mp.mpf(4)
    net_p = mp.mpf("6125") / mp.mpf("1000")
    E0 = m_e / (q_val * (q_val - mp.mpf(1)))
    Q_beta = E0 * h_val * net_p
    max_err_1 = mp.mpf(0)
    for tr_free_str, tr_bound_str in [("17/5", "11/4"), ("43/9", "19/7"), ("101/13", "29/8")]:
        tr_free = mp.mpf(tr_free_str.split("/")[0]) / mp.mpf(tr_free_str.split("/")[1])
        tr_bound = mp.mpf(tr_bound_str.split("/")[0]) / mp.mpf(tr_bound_str.split("/")[1])
        lhs = (m_e / (q_val * (q_val - mp.mpf(1)))) * net_p * (tr_free - tr_bound)
        rhs = Q_beta * (tr_free - tr_bound) / h_val
        err = abs(lhs - rhs)
        if err > max_err_1:
            max_err_1 = err
    results.append({
        "id": "binding_dressing_free_sub_bound_eq_qbeta_over_h",
        "bean": "qou-6h6p",
        "maxAbsError": mp.nstr(max_err_1, 25),
        "passed": bool(max_err_1 <= tol),
    })

    # 2. qou-e1dc: whiteheadLinkPhase_arg_decomp_zero
    max_err_2 = mp.mpf(0)
    for n_val in [1, 2, 5, 12, 37, 100]:
        N_mp = mp.mpf(n_val)
        lhs = -(((mp.mpf(0) - N_mp / mp.mpf(2)) ** 2) * mp.pi / (mp.mpf(2) * N_mp)) + N_mp * mp.pi / mp.mpf(8)
        err = abs(lhs)
        if err > max_err_2:
            max_err_2 = err
    results.append({
        "id": "whiteheadLinkPhase_arg_decomp_zero",
        "bean": "qou-e1dc",
        "maxAbsError": mp.nstr(max_err_2, 25),
        "passed": bool(max_err_2 <= tol),
    })

    # 3. qou-l2ob: chainRatio_add_two_neutrons
    fpp = mp.mpf(13) / mp.mpf(11)
    fpn = mp.mpf(17) / mp.mpf(13)
    fnn = mp.mpf(19) / mp.mpf(15)
    max_err_3 = mp.mpf(0)
    for Z_int in [1, 2, 4, 8]:
        for N_int in [1, 3, 6, 9]:
            cr_n = (fpp ** (Z_int - 1)) * fpn * (fnn ** (N_int - 1))
            cr_n2 = (fpp ** (Z_int - 1)) * fpn * (fnn ** (N_int + 2 - 1))
            rhs = cr_n * (fnn * fnn)
            err = abs(cr_n2 - rhs)
            if err > max_err_3:
                max_err_3 = err
    results.append({
        "id": "chainRatio_add_two_neutrons",
        "bean": "qou-l2ob",
        "maxAbsError": mp.nstr(max_err_3, 25),
        "passed": bool(max_err_3 <= tol),
    })

    # 4. qou-p2d5: solMu3_add_three_solMu2
    max_err_4 = mp.mpf(0)
    for m2_i, m3_i, m4_i in [(3, -7, 11), (14, 29, -5), (-8, 19, 41)]:
        m2 = mp.mpf(m2_i) / mp.mpf(5)
        m3 = mp.mpf(m3_i) / mp.mpf(7)
        m4 = mp.mpf(m4_i) / mp.mpf(9)
        sol_mu2 = m2
        sol_mu3 = m3 - mp.mpf(3) * m2
        lhs = sol_mu3 + mp.mpf(3) * sol_mu2
        err = abs(lhs - m3)
        if err > max_err_4:
            max_err_4 = err
    results.append({
        "id": "solMu3_add_three_solMu2",
        "bean": "qou-p2d5",
        "maxAbsError": mp.nstr(max_err_4, 25),
        "passed": bool(max_err_4 <= tol),
    })

    # 5. qou-ypc5: weighted_deviation_eq_of_same_bond
    y_weights = [mp.mpf(2) / mp.mpf(9), mp.mpf(3) / mp.mpf(9), mp.mpf(4) / mp.mpf(9)]
    tr_a = mp.mpf(7) / mp.mpf(3)
    tr_b = mp.mpf(11) / mp.mpf(5)
    bond = mp.mpf(23) / mp.mpf(19)
    tr_free = tr_a * tr_b
    tr_target = tr_free * bond
    # Choose free characters chi_free so sum y_l * chi_free_l == tr_free
    chi_free = [tr_free, tr_free, tr_free]
    # Choose two distinct composite character profiles atom1, atom2 with sum y_l * chi_l == tr_target
    chi_atom1 = [tr_target + mp.mpf(3), tr_target - mp.mpf(2), tr_target]
    chi_atom2 = [tr_target - mp.mpf(6), tr_target + mp.mpf(4), tr_target]
    dev1 = sum(y_weights[i] * (chi_atom1[i] - chi_free[i]) for i in range(3))
    dev2 = sum(y_weights[i] * (chi_atom2[i] - chi_free[i]) for i in range(3))
    max_err_5 = abs(dev1 - dev2)
    results.append({
        "id": "weighted_deviation_eq_of_same_bond",
        "bean": "qou-ypc5",
        "maxAbsError": mp.nstr(max_err_5, 25),
        "passed": bool(max_err_5 <= tol),
    })

    return {
        "dps": str(mp.dps),
        "allPassed": all(r["passed"] for r in results),
        "checks": results,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_checks(), indent=2))
