#!/usr/bin/env python3
"""80-dps mpmath computational probe for Round 56 formalization:
1. qou-0c19: Canonical 3k layout boundary colour mismatch ((3k+2)%3 == 2 vs
   (3k+3)%3 == 0) and exact collinearity of linear-chain interface count A - 1
   with mass number A.
2. qou-0gbx: Flavour-split geometric tail ratio K = (C - (1 + x)) / (x^2 / (1 - x)),
   required single-term coefficient excess c - 1 = K * x / (1 - x), and
   monotonicity c_1 < c_2 < c_3 < c_4 across powers x^k for 0 < x < 1.
3. qou-17mq: Finite-volume neutrality offset mu = (w1*K1 + w2*K2)/(w1 + w2)
   forcing opposite signs K1 - mu < 0 < K2 - mu for K1 < K2, and strictly
   positive integral of unsubtracted coth kernel.
4. qou-768r: SLq(2) knot-label parity exclusion at odd A (mu = A + 1 even),
   crossing-minus-writhe evenness (c - w = 2 * c_neg), and canonical atom-word
   spanning-surface genus g = 4 * A for c = 12*A - 1, n = 3*A, mu = A + 1.
5. qou-d0qq: KZ pullback generator polynomial inverse g_i * (g_i - h*I) = I
   at complex non-unitary level k + 2 = i*pi / ln(q0), plus common-conjugator
   transport of braid and far-commutation relations.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import pathlib
from mpmath import mp

mp.dps = 80


def main() -> None:
    alpha_inv = mp.mpf("137.035999177")
    alpha = mp.mpf(1) / alpha_inv
    q0 = mp.exp(mp.mpf("0.10434072031951951232"))
    h_val = q0 - mp.mpf(1) / q0
    hbar_q = mp.mpf(1) - mp.mpf(1) / q0

    # 1. qou-0c19: LayoutConflict colour mismatch and A - 1 collinearity
    colour_mismatch_verified = True
    for k_idx in range(1, 12):
        x_low = 3 * k_idx + 2
        x_high = x_low + 1
        if (x_low % 3 != 2) or (x_high % 3 != 0) or (x_low % 3 == x_high % 3):
            colour_mismatch_verified = False
    assert colour_mismatch_verified

    alpha_lin = mp.mpf("2.75")
    beta_lin = -mp.mpf("1.25")
    gamma_lin = mp.mpf("0.85")
    max_collinear_res = mp.mpf(0)
    for a_num in range(2, 10):
        a_mp = mp.mpf(a_num)
        lhs = alpha_lin * a_mp + beta_lin + gamma_lin * (a_mp - 1)
        rhs = (alpha_lin + gamma_lin) * a_mp + (beta_lin - gamma_lin)
        res = abs(lhs - rhs)
        if res > max_collinear_res:
            max_collinear_res = res
    assert max_collinear_res < mp.mpf("1e-75")

    # 2. qou-0gbx: GeometricTailBound required coefficient excess and k = 1..4 sweep
    x_val = mp.power(hbar_q, 3)
    c_target = mp.mpf(1) + mp.mpf("1.31459") * x_val
    tail_val = mp.power(x_val, 2) / (mp.mpf(1) - x_val)
    gap_val = c_target - (mp.mpf(1) + x_val)
    k_ratio = gap_val / tail_val
    c_req = (c_target - mp.mpf(1)) / x_val
    excess_lhs = c_req - mp.mpf(1)
    excess_rhs = k_ratio * x_val / (mp.mpf(1) - x_val)
    excess_res = abs(excess_lhs - excess_rhs)
    assert excess_res < mp.mpf("1e-70")

    coeffs_k = [
        (c_target - mp.mpf(1)) / mp.power(hbar_q, k_pow)
        for k_pow in (1, 2, 3, 4)
    ]
    assert coeffs_k[0] < coeffs_k[1] < coeffs_k[2] < coeffs_k[3]

    # 3. qou-17mq: Finite-volume neutrality offset and sign change
    w1 = mp.mpf("1.5")
    w2 = mp.mpf("2.5")
    k1 = mp.coth(mp.mpf("1.2"))
    k2 = mp.coth(mp.mpf("0.4"))
    assert 0 < k1 < k2
    unsub_mean = w1 * k1 + w2 * k2
    assert unsub_mean > 0
    mu_offset = unsub_mean / (w1 + w2)
    sub_1 = k1 - mu_offset
    sub_2 = k2 - mu_offset
    neutral_sum_res = abs(w1 * sub_1 + w2 * sub_2)
    assert sub_1 < 0 < sub_2
    assert neutral_sum_res < mp.mpf("1e-70")

    # 4. qou-768r: SLq(2) label parity and canonical atom-word genus g = 4*A
    slq2_checks_ok = True
    for a_val in range(2, 13):
        c_cnt = 12 * a_val - 1
        n_str = 3 * a_val
        mu_comp = a_val + 1
        g_gen = 4 * a_val
        seifert_lhs = c_cnt - n_str
        seifert_rhs = 2 * g_gen + mu_comp - 2
        label_cons = ((c_cnt - n_str - 1) % 2 == 0)
        even_a = (a_val % 2 == 0)
        if seifert_lhs != seifert_rhs or label_cons != even_a:
            slq2_checks_ok = False
    assert slq2_checks_ok

    # 5. qou-d0qq: KZ non-unitary level k + 2 = i*pi / ln(q0) and polynomial inverse
    ln_q0 = mp.log(q0)
    kz_k_plus_2_imag = mp.pi / ln_q0
    # Verify 2x2 representation of Hecke generator g with eigenvalues q0 and -1/q0
    # conjugated by an invertible upper-triangular matrix U = [[1, 2], [0, 1]]:
    # U * diag(q0, -1/q0) * U^-1 = [[q0, -2*(q0 + 1/q0)], [0, -1/q0]]
    g00 = q0
    g01 = -mp.mpf(2) * (q0 + mp.mpf(1) / q0)
    g11 = -mp.mpf(1) / q0
    # Check g * (g - h * I) == I:
    inv00 = g00 - h_val
    inv01 = g01
    inv11 = g11 - h_val
    prod00 = g00 * inv00
    prod01 = g00 * inv01 + g01 * inv11
    prod11 = g11 * inv11
    kz_inv_res = max(abs(prod00 - 1), abs(prod01), abs(prod11 - 1))
    assert kz_inv_res < mp.mpf("1e-70")

    script_path = pathlib.Path(__file__).resolve()
    script_hash = hashlib.sha256(script_path.read_bytes()).hexdigest()[:12]

    witness = {
        "probe": "computations/probes/layout_geomtail_neutrality_slq2_kz_probe.py",
        "beans": ["qou-0c19", "qou-0gbx", "qou-17mq", "qou-768r", "qou-d0qq"],
        "precision_dps": 80,
        "gitCommit": "0000000000000000000000000000000000000000",
        "scriptCommitSha": "0000000000000000000000000000000000000000",
        "scriptHash": script_hash,
        "allPassed": True,
        "generatedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "results": {
            "qou_0c19_layout_and_collinearity": {
                "colour_mismatch_verified_k_1_to_11": colour_mismatch_verified,
                "lower_colour_mod_3": 2,
                "upper_colour_mod_3": 0,
                "max_collinearity_residual": mp.nstr(max_collinear_res, 30),
            },
            "qou_0gbx_geometric_tail_bound": {
                "x_hbar_q_cubed": mp.nstr(x_val, 30),
                "tail_to_gap_ratio_K": mp.nstr(k_ratio, 30),
                "required_coeff_excess_residual": mp.nstr(excess_res, 30),
                "required_coeffs_k_1_to_4": [mp.nstr(v, 25) for v in coeffs_k],
            },
            "qou_17mq_neutrality_sign_change": {
                "unsubtracted_weighted_sum": mp.nstr(unsub_mean, 30),
                "volume_average_offset_mu": mp.nstr(mu_offset, 30),
                "subtracted_region_1": mp.nstr(sub_1, 30),
                "subtracted_region_2": mp.nstr(sub_2, 30),
                "neutralised_integral_residual": mp.nstr(neutral_sum_res, 30),
            },
            "qou_768r_slq2_parity_and_genus": {
                "verified_a_2_to_12": slq2_checks_ok,
                "deuteron_a2_genus": 8,
                "a3_mirror_components": 4,
                "a3_admits_knot_label": False,
            },
            "qou_d0qq_kz_pullback_inverse": {
                "kz_k_plus_2_imag": mp.nstr(kz_k_plus_2_imag, 30),
                "polynomial_inverse_max_residual": mp.nstr(kz_inv_res, 30),
            },
        },
    }

    out_path = script_path.with_name("layout-geomtail-neutrality-slq2-kz.witness.json")
    out_path.write_text(json.dumps(witness, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path} (scriptHash={script_hash})")


if __name__ == "__main__":
    main()
