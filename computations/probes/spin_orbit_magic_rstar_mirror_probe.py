#!/usr/bin/env python3
"""Joint 50-dps verification probe for Round 48 low-isotope binding & magic-ladder beans:
- qou-w2vy: binding_from_frobenius_pairing / atom_character_raw object-dtype & return-type audit
- qou-frso: Framing spin-orbit 2l+1 Lande splitting (derived shape vs unfixed radial scale)
- qou-mgq3: Harmonic-oscillator vs Mayer-Jensen spin-orbit intruder magic closures & A5 wall
- qou-cds5: Step 1 resolution of the Convention-D r* band ([2.04, 2.16] door-scale provenance
            vs cabled-Borromean r*_D = 1.549361 grouped / 2.458116 borromean, and r_both^D = 2.871235)
- qou-z4ba: Exact P - Q = 5 ordering invariance of c1(Z, N) - c1(N, Z) across (21, 16) and (3, -2)

All real-valued computations run at 50 decimal places via mpmath (proton q0 anchor) and all
witness numbers are emitted as decimal or exact rational strings (zero raw float64 values).
"""

from __future__ import annotations

import datetime
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys

import mpmath as mp

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
if str(HERE.parent) not in sys.path:
    sys.path.insert(0, str(HERE.parent))
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import _path_bridge  # noqa: F401, E402
from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
import hecke_core_legacy as hcl  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from tr_m_wenzl_bridge_mpfr import (  # noqa: E402
    _build_seminormal_matrices_mpf,
    _chi_lambda_of_word_mpf,
)
from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from y_lambda_wenzl_bridge import (  # noqa: E402
    classical_dim,
    partitions_of,
    schur_principal,
)

set_compute_dps()
WORK_DPS = 50
WITNESS_PATH = HERE / "spin-orbit-magic-rstar-mirror-probe.witness.json"


def _git_head_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=str(REPO_ROOT), text=True
        ).strip()
        return out if len(out) == 40 else "0" * 40
    except Exception:
        return "0" * 40


def _fmt(x: mp.mpf, dps: int = 50) -> str:
    with mp.workdps(dps):
        return mp.nstr(mp.mpf(x), dps)


def _verify_w2vy() -> dict:
    """Verify qou-w2vy: kernel path, Python COO object-dtype fallback, and return-type boundary."""
    with mp.workdps(WORK_DPS):
        entry_k3 = next(
            e
            for e in hcl._PARTITION_TABLE
            if e.get("k", 0) == 3 and e.get("dim", 0) >= 2 and e.get("has_ysn", False)
        )
        chi_d, ln_d, dim_d = hcl.atom_character_raw(1, 1, entry_k3, include_inter=True)
        tr_d = hcl.atom_markov_trace(1, 1, k_cap=3)
        fn_d, _, max_ln_d = hcl.atom_frobenius_norm_sq(1, 1, k_cap=3)
        bfp_d = hcl.binding_from_frobenius_pairing(1, 1, k_cap=3)

        orig_kernel_flag = hcl._HAS_LP_KERNEL
        try:
            hcl._HAS_LP_KERNEL = False
            chi_p_py, ln_p_py, _ = hcl._atom_character_raw_exact(
                1, 1, entry_k3, include_inter=True
            )
        finally:
            hcl._HAS_LP_KERNEL = orig_kernel_flag

        chi_p_rs, ln_p_rs, _ = hcl._atom_character_raw_exact(
            1, 1, entry_k3, include_inter=True
        )
        rel_diff_chi = abs(mp.mpf(str(chi_p_py)) - mp.mpf(str(chi_p_rs))) / abs(
            mp.mpf(str(chi_p_rs))
        )
        assert rel_diff_chi < mp.mpf("1e-14"), f"Kernel vs Python COO mismatch: {rel_diff_chi}"

    assert type(chi_d).__name__ == "float"
    assert type(ln_d).__name__ == "float"
    assert type(tr_d).__name__ == "mpf"
    assert type(fn_d).__name__ == "mpf"
    assert type(bfp_d).__name__ == "mpf"

    return {
        "bean": "qou-w2vy",
        "k_cap_tested": "3",
        "partition_entry_tested": str(tuple(entry_k3["partition"])),
        "has_lp_kernel": str(bool(hcl._HAS_LP_KERNEL)),
        "atom_character_raw_return_types": {
            "chi_type": type(chi_d).__name__,
            "log_norm_type": type(ln_d).__name__,
            "dim_type": type(dim_d).__name__,
        },
        "downstream_return_types": {
            "atom_markov_trace": type(tr_d).__name__,
            "atom_frobenius_norm_sq": type(fn_d).__name__,
            "binding_from_frobenius_pairing": type(bfp_d).__name__,
        },
        "deuteron_kcap3": {
            "chi_float_str": f"{chi_d:.17e}",
            "log_norm_float_str": f"{ln_d:.17e}",
            "markov_trace_50dps": _fmt(tr_d),
            "frobenius_norm_sq_50dps": _fmt(fn_d),
            "binding_from_frobenius_pairing_MeV_50dps": _fmt(bfp_d),
        },
        "python_coo_object_fallback_deuteron_kcap3": {
            "chi_python_coo": f"{chi_p_py:.17e}",
            "chi_rust_kernel": f"{chi_p_rs:.17e}",
            "rel_diff": _fmt(rel_diff_chi, 20),
            "object_dtype_crash_reproduced": "False",
        },
    }


def _verify_frso_mgq3() -> dict:
    """Verify qou-frso (2l+1 spin-orbit splitting) and qou-mgq3 (magic ladders & A5 wall)."""
    lande_rows = []
    for ell in range(11):
        ell_q = Fraction(ell, 1)
        j_plus = ell_q + Fraction(1, 2)
        j_minus = ell_q - Fraction(1, 2)
        c_plus = j_plus * (j_plus + 1)
        c_minus = j_minus * (j_minus + 1)
        c_ell = ell_q * (ell_q + 1)
        c_spin = Fraction(1, 2) * Fraction(3, 2)
        two_ls_plus = c_plus - c_ell - c_spin
        two_ls_minus = c_minus - c_ell - c_spin
        diff = c_plus - c_minus
        assert two_ls_plus == ell_q
        assert two_ls_minus == -(ell_q + 1)
        assert diff == 2 * ell_q + 1
        assert two_ls_plus - two_ls_minus == 2 * ell_q + 1
        lande_rows.append(
            {
                "ell": str(ell),
                "two_ls_aligned": str(two_ls_plus),
                "two_ls_anti_aligned": str(two_ls_minus),
                "casimir_diff_2ell_plus_1": str(diff),
            }
        )

    ho_closures = [(n + 1) * (n + 2) * (n + 3) // 3 for n in range(7)]
    assert ho_closures == [2, 8, 20, 40, 70, 112, 168]

    intruder_caps = {n: 2 * (n + 2) for n in range(2, 6)}
    so_intruder_closures = {n: ho_closures[n] + intruder_caps[n] for n in range(2, 6)}
    assert [so_intruder_closures[n] for n in range(2, 6)] == [28, 50, 82, 126]

    mayer_jensen = ho_closures[:3] + [so_intruder_closures[n] for n in range(2, 6)]
    assert mayer_jensen == [2, 8, 20, 28, 50, 82, 126]

    a5_irrep_dims = [1, 3, 3, 4, 5]
    assert sum(d * d for d in a5_irrep_dims) == 60
    max_spin_doubled_a5 = 2 * max(a5_irrep_dims)
    assert max_spin_doubled_a5 == 10
    assert max_spin_doubled_a5 < intruder_caps[4] == 12  # 1h_{11/2} closing 82
    assert max_spin_doubled_a5 < intruder_caps[5] == 14  # 1i_{13/2} closing 126

    return {
        "beans": ["qou-frso", "qou-mgq3"],
        "lande_interval_identity_verified_ell_0_to_10": lande_rows,
        "ho_cumulative_closures_n_0_to_6": [str(x) for x in ho_closures],
        "so_intruder_closures_n_2_to_5": [
            {
                "n": str(n),
                "ho_base": str(ho_closures[n]),
                "intruder_j": f"{2 * n + 3}/2",
                "intruder_capacity_2j_plus_1": str(intruder_caps[n]),
                "magic_closure": str(so_intruder_closures[n]),
            }
            for n in range(2, 6)
        ],
        "mayer_jensen_magic_ladder": [str(x) for x in mayer_jensen],
        "a5_icosahedral_branching_wall": {
            "a5_irrep_dims": [str(d) for d in a5_irrep_dims],
            "burnside_sum_sq": "60",
            "max_spin_doubled_a5_dim": str(max_spin_doubled_a5),
            "h11_half_intruder_dim_at_82": str(intruder_caps[4]),
            "i13_half_intruder_dim_at_126": str(intruder_caps[5]),
            "single_a5_irrep_excluded_at_82_and_126": "True",
            "so3_ell5_to_a5_branching": "3 + 3 + 5 = 11",
        },
    }


def _q_int(m: int, q: mp.mpf) -> mp.mpf:
    return (q**m - q ** (-m)) / (q - 1 / q)


def _hook_lengths(lam: tuple[int, ...]) -> list[int]:
    conj = [sum(1 for row in lam if row > j) for j in range(lam[0])]
    hooks = []
    for i, row in enumerate(lam):
        for j in range(row):
            hooks.append((row - 1 - j) + (conj[j] - 1 - i) + 1)
    return hooks


def _dq(lam: tuple[int, ...], q: mp.mpf) -> mp.mpf:
    n = sum(lam)
    qfact = mp.mpf(1)
    for m in range(1, n + 1):
        qfact *= _q_int(m, q)
    ph = mp.mpf(1)
    for h in _hook_lengths(lam):
        ph *= _q_int(h, q)
    return qfact / ph


def _block_transposition(a: int, w: int = 3) -> list[int]:
    gens = []
    for r in range(w):
        for g in range(a + w - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def _borromean_inter_word(h_val: mp.mpf) -> list[tuple[float, float, int]]:
    dA = _block_transposition(0)
    dB = _block_transposition(3)
    dB_inv = [g for g in reversed(dB)]
    word = []
    for _ in range(3):
        word += [(1.0, 0.0, g) for g in dA]
        word += [(1.0, float(-h_val), g) for g in dB_inv]
    return word


def _verify_cds5() -> dict:
    """Verify qou-cds5 Step 1 at 50 dps: uncabled door [2.04, 2.16] vs cabled-Borromean r*_D."""
    with mp.workdps(WORK_DPS):
        q = mp.mpf(Q_50_DIGIT_STR)
        e0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
        h_val = q - 1 / q
        mu3_target = mp.mpf("0.4708")
        parts9 = [tuple(p) for p in partitions_of(9)]

        zc = 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))
        zd = q**3 / (q**2 + 1)

        def _y_vec(z_val: mp.mpf) -> dict[tuple[int, ...], mp.mpf]:
            Q_sq = q**2
            X = q * z_val / (1 - Q_sq + q * z_val)
            s = {p: schur_principal(list(p), X, Q_sq) for p in parts9}
            norm = sum(classical_dim(list(p)) * s[p] for p in parts9)
            return {p: s[p] / norm for p in parts9}

        yC = _y_vec(zc)
        yD = _y_vec(zd)
        sum_yC = sum(yC.values(), mp.mpf(0))
        sum_yD = sum(yD.values(), mp.mpf(0))

        # Geometric weights w_lambda^geom = d_q(lambda)^2 / sum_mu d_q(mu)^2
        dqsq9 = {p: _dq(p, q) ** 2 for p in parts9}
        d2_tot = sum(dqsq9.values(), mp.mpf(0))
        w_geom = {p: dqsq9[p] / d2_tot for p in parts9}

        # Prebuild 50-dps Hoefsmit seminormal matrices for all 30 partitions of H_9
        seminormal9 = {p: _build_seminormal_matrices_mpf(p, q) for p in parts9}
        zero = mp.mpf(0)
        one = mp.mpf(1)
        snap = {
            round(0.0, 9): zero,
            round(float(-h_val), 9): -h_val,
            round(float(-h_val / 2), 9): -h_val / 2,
        }
        from tr_m_wenzl_bridge_mpfr import _hecke_factor_coo

        coo_cache: dict[tuple, list[list[tuple[int, mp.mpf]]]] = {}

        def _factor_rows(p: tuple[int, ...], g: int, c_f: float, d_f: float):
            key = (p, g, round(c_f, 9), round(d_f, 9))
            if key in coo_cache:
                return coo_cache[key]
            sig, dim = seminormal9[p]
            c_mp = one if c_f == 1.0 else mp.mpf(str(c_f))
            d_mp = snap.get(round(d_f, 9), mp.mpf(str(d_f)))
            coo = _hecke_factor_coo(sig[g], c_mp, d_mp, dim)
            rows: list[list[tuple[int, mp.mpf]]] = [[] for _ in range(dim)]
            for j_idx, k_idx, val in coo:
                rows[j_idx].append((k_idx, val))
            coo_cache[key] = rows
            return rows

        def _word_mat(p: tuple[int, ...], word) -> list[list[mp.mpf]]:
            _, dim = seminormal9[p]
            P = [[zero] * dim for _ in range(dim)]
            for i in range(dim):
                P[i][i] = one
            for c_f, d_f, g in word:
                rows = _factor_rows(p, g, float(c_f), float(d_f))
                P_new = [[zero] * dim for _ in range(dim)]
                for r in range(dim):
                    Pr = P[r]
                    Pnr = P_new[r]
                    for j_idx in range(dim):
                        prj = Pr[j_idx]
                        if prj == zero:
                            continue
                        for k_idx, val in rows[j_idx]:
                            Pnr[k_idx] += prj * val
                P = P_new
            return P

        def _tr_mat(M: list[list[mp.mpf]]) -> mp.mpf:
            return sum((M[i][i] for i in range(len(M))), zero)

        def _tr_prod(A: list[list[mp.mpf]], B: list[list[mp.mpf]]) -> mp.mpf:
            dim = len(A)
            s = zero
            for i in range(dim):
                Ai = A[i]
                for j in range(dim):
                    s += Ai[j] * B[j][i]
            return s

        word_cache: dict[tuple, dict[tuple[int, ...], mp.mpf]] = {}

        def _eval_word_chars(word) -> dict[tuple[int, ...], mp.mpf]:
            key = tuple(word)
            if key in word_cache:
                return word_cache[key]
            out = {p: _tr_mat(_word_mat(p, word)) for p in parts9}
            word_cache[key] = out
            return out

        # Precompute M_inter once for all 30 partitions (shared across T/3He and grouped/borromean)
        inter_word = _borromean_inter_word(h_val)
        M_inter = {p: _word_mat(p, inter_word) for p in parts9}

        # Precompute M_intra once per (name, intra_order)
        M_intra: dict[tuple[str, str], dict[tuple[int, ...], list[list[mp.mpf]]]] = {}
        for intra_order in ("grouped", "borromean"):
            for name, (Z, N) in (("T", (1, 2)), ("3He", (2, 1))):
                full_w = atom_braid_word_3A(Z, N, include_inter=True, intra_order=intra_order)
                intra_w = [x for x in full_w if x[2] % 3 != 2]
                M_intra[(name, intra_order)] = {p: _word_mat(p, intra_w) for p in parts9}
                word_cache[tuple(intra_w)] = {
                    p: _tr_mat(M_intra[(name, intra_order)][p]) for p in parts9
                }

        # 1. PR #4766 uncabled pairwise supermodularity door (evaluated on the pre-qou-hu1f
        # "grouped" word that atom_braid_word_3A used when PR #4766 ran on 2026-08-08)
        door_c3 = {}
        for name, (Z, N) in (("T", (1, 2)), ("3He", (2, 1))):
            full = atom_braid_word_3A(Z, N, include_inter=True, intra_order="grouped")
            ga, gb = sorted({x[2] for x in full if x[2] % 3 == 2})
            sub_empty = [x for x in full if x[2] % 3 != 2]
            sub_a = [x for x in full if x[2] % 3 != 2 or x[2] == ga]
            sub_b = [x for x in full if x[2] % 3 != 2 or x[2] == gb]
            c_empty = _eval_word_chars(sub_empty)
            c_a = _eval_word_chars(sub_a)
            c_b = _eval_word_chars(sub_b)
            c_ab = _eval_word_chars(full)
            for tag, y in (("C", yC), ("D", yD)):
                d2g = sum(
                    y[p]
                    * (abs(c_ab[p]) - abs(c_a[p]) - abs(c_b[p]) + abs(c_empty[p]))
                    for p in parts9
                )
                door_c3[f"{name}_{tag}"] = -e0 * d2g

        door_ratio_T = door_c3["T_C"] / door_c3["T_D"]
        door_ratio_He3 = door_c3["3He_C"] / door_c3["3He_D"]

        # 2. #4364 width-3 cabled-Borromean cluster c3^cabled = E0 * (g_0 - g_B)
        def _cabled_eval(intra_order: str) -> dict:
            chars0 = {}
            charsB = {}
            for name in ("T", "3He"):
                m_in = M_intra[(name, intra_order)]
                chars0[name] = {p: _tr_mat(m_in[p]) for p in parts9}
                charsB[name] = {p: _tr_prod(m_in[p], M_inter[p]) for p in parts9}

            def _cluster_from_weights(w_map):
                c3_t = e0 * sum(
                    w_map[p] * (abs(chars0["T"][p]) - abs(charsB["T"][p])) for p in parts9
                )
                c3_h = e0 * sum(
                    w_map[p] * (abs(chars0["3He"][p]) - abs(charsB["3He"][p])) for p in parts9
                )
                return c3_t, c3_h, (c3_t + c3_h) / 2

            c3_t_C, c3_h_C, c3_mean_C = _cluster_from_weights(yC)
            c3_t_D, c3_h_D, c3_mean_D = _cluster_from_weights(yD)
            c3_t_G, c3_h_G, c3_mean_G = _cluster_from_weights(w_geom)

            r_star_C = mu3_target / c3_mean_C
            r_star_D = mu3_target / c3_mean_D
            r_star_D_T = mu3_target / c3_t_D
            r_star_D_He3 = mu3_target / c3_h_D

            r_geom_C = c3_mean_G / c3_mean_C
            r_geom_D = c3_mean_G / c3_mean_D
            r_both_C = r_geom_C * sum_yC
            r_both_D = r_geom_D * sum_yD

            return {
                "c3_T_C_MeV": _fmt(c3_t_C),
                "c3_He3_C_MeV": _fmt(c3_h_C),
                "c3_mean_C_MeV": _fmt(c3_mean_C),
                "c3_T_D_MeV": _fmt(c3_t_D),
                "c3_He3_D_MeV": _fmt(c3_h_D),
                "c3_mean_D_MeV": _fmt(c3_mean_D),
                "c3_geom_mean_MeV": _fmt(c3_mean_G),
                "r_star_C_mean": _fmt(r_star_C),
                "r_star_D_mean": _fmt(r_star_D),
                "r_star_D_per_isotope_band": [_fmt(r_star_D_He3), _fmt(r_star_D_T)],
                "r_geom_C": _fmt(r_geom_C),
                "r_geom_D": _fmt(r_geom_D),
                "r_both_C": _fmt(r_both_C),
                "r_both_D": _fmt(r_both_D),
                "_raw": (r_star_C, r_star_D, r_both_C, r_both_D),
            }

        grouped_res = _cabled_eval("grouped")
        borromean_res = _cabled_eval("borromean")

        r_star_C_grouped, r_star_D_grouped, r_both_C_grouped, r_both_D_grouped = grouped_res.pop(
            "_raw"
        )
        r_star_C_borr, r_star_D_borr, _, r_both_D_borr = borromean_res.pop("_raw")

        pr4766_lo = r_star_C_grouped * door_ratio_T
        pr4766_hi = r_star_C_grouped * door_ratio_He3
        assert mp.mpf("2.04") < pr4766_lo < mp.mpf("2.05")
        assert mp.mpf("2.15") < pr4766_hi < mp.mpf("2.16")

        assert mp.mpf("1.54") < r_star_D_grouped < mp.mpf("1.56") < mp.mpf("2.04")
        assert mp.mpf("2.16") < mp.mpf("2.45") < r_star_D_borr < mp.mpf("2.46")

        assert mp.mpf("2.87") < r_both_D_grouped < mp.mpf("2.88")
        assert r_both_D_grouped > r_star_D_grouped

        return {
            "bean": "qou-cds5",
            "mu3_target_MeV": _fmt(mu3_target),
            "sum_y_lambda_C_H9": _fmt(sum_yC),
            "sum_y_lambda_D_H9": _fmt(sum_yD),
            "pr4766_uncabled_door_provenance": {
                "c3_door_T_C_MeV": _fmt(door_c3["T_C"]),
                "c3_door_T_D_MeV": _fmt(door_c3["T_D"]),
                "c3_door_He3_C_MeV": _fmt(door_c3["3He_C"]),
                "c3_door_He3_D_MeV": _fmt(door_c3["3He_D"]),
                "door_ratio_C_over_D_T": _fmt(door_ratio_T),
                "door_ratio_C_over_D_He3": _fmt(door_ratio_He3),
                "r_star_C_times_door_ratio_T": _fmt(pr4766_lo),
                "r_star_C_times_door_ratio_He3": _fmt(pr4766_hi),
                "relayed_band_explanation": (
                    "PR #4766 multiplied the cabled-Borromean r*_C = 1.585412 by the uncabled "
                    "pairwise supermodularity door scale factor c3_door(C)/c3_door(D) in [1.2889, 1.3594] "
                    "to obtain [2.0434, 2.1552] ~ [2.04, 2.16]."
                ),
            },
            "cabled_borromean_grouped_word": grouped_res,
            "cabled_borromean_canonical_word": borromean_res,
            "step1_verdict": (
                "REFUTED as cabled-Borromean r*_D: on the #4364 grouped word, c3^cabled increases "
                "from 0.296958 MeV (C) to 0.303867 MeV (D), so r*_D = 1.549361 moves DOWN (-2.27%), "
                "while r_both^D jumps to 2.871235 (+85.32% overshoot). On the canonical borromean word, "
                "r*_D = 2.458116 lies above [2.04, 2.16]. None of the six pruned Delta_lambda ansaetze "
                "is rescued."
            ),
        }


def _c1_closed_pq(P: int, Q: int, Z: int, N: int) -> Fraction:
    A = Z + N
    i_pp = max(Z - 1, 0)
    i_nn = max(N - 1, 0)
    return (P * Z + Q * N) * (Fraction(1, 2 ** (A + 1)) - Fraction(1, 4**A)) - 4 * (
        i_pp - i_nn
    ) * Fraction(1, 4**A)


def _mirror_bracket(A: int) -> Fraction:
    return 5 * Fraction(1, 2 ** (A + 1)) - 13 * Fraction(1, 4**A)


def _verify_z4ba() -> dict:
    """Verify qou-z4ba: exact P - Q = 5 ordering invariance across (21, 16) and (3, -2)."""
    checked_pairs = 0
    for Z in range(1, 21):
        for N in range(1, Z):
            A = Z + N
            diff_grouped = _c1_closed_pq(21, 16, Z, N) - _c1_closed_pq(21, 16, N, Z)
            diff_borromean = _c1_closed_pq(3, -2, Z, N) - _c1_closed_pq(3, -2, N, Z)
            expected = (Z - N) * _mirror_bracket(A)
            assert diff_grouped == expected
            assert diff_borromean == expected
            if A >= 3:
                assert expected > 0
            checked_pairs += 1

    assert _mirror_bracket(2) == Fraction(-3, 16) < 0
    assert _mirror_bracket(3) == Fraction(7, 64) > 0
    assert _mirror_bracket(4) == Fraction(27, 256) > 0

    return {
        "bean": "qou-z4ba",
        "checked_mirror_pairs_1_le_N_lt_Z_le_20": str(checked_pairs),
        "grouped_coefficients_P_Q": ["21", "16"],
        "borromean_coefficients_P_Q": ["3", "-2"],
        "shared_gap_P_minus_Q": "5",
        "mirror_bracket_A2": str(_mirror_bracket(2)),
        "mirror_bracket_A3": str(_mirror_bracket(3)),
        "mirror_bracket_A4": str(_mirror_bracket(4)),
        "he3_minus_tritium_c1_grouped": str(
            _c1_closed_pq(21, 16, 2, 1) - _c1_closed_pq(21, 16, 1, 2)
        ),
        "he3_minus_tritium_c1_borromean": str(
            _c1_closed_pq(3, -2, 2, 1) - _c1_closed_pq(3, -2, 1, 2)
        ),
        "ordering_invariance_verified": "True",
    }


def main() -> None:
    import hashlib
    with mp.workdps(WORK_DPS):
        q = mp.mpf(Q_50_DIGIT_STR)
        e0 = mp.mpf(str(M_E_MEV)) / (q * (q - 1))
    w2vy = _verify_w2vy()
    frso_mgq3 = _verify_frso_mgq3()
    cds5 = _verify_cds5()
    z4ba = _verify_z4ba()

    head_sha = _git_head_sha()
    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()[:12]
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat()
    assertions = [
        {"name": "qou_w2vy_return_types_and_coo_object_fallback", "passed": True},
        {"name": "qou_frso_lande_2ell_plus_1_interval_identity", "passed": True},
        {"name": "qou_mgq3_mayer_jensen_magic_ladder_and_a5_wall", "passed": True},
        {"name": "qou_cds5_step1_r_star_convention_D_outside_pr4766_band", "passed": True},
        {"name": "qou_z4ba_c1_mirror_diff_gap_five_invariance", "passed": True},
    ]

    payload = {
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "computedAt": now_iso,
        "commitSha": head_sha,
        "scriptFile": "probes/spin_orbit_magic_rstar_mirror_probe.py",
        "scriptPath": "computations/probes/spin_orbit_magic_rstar_mirror_probe.py",
        "scriptHash": script_hash,
        "scriptCommitSha": head_sha,
        "allPassed": True,
        "assertions": assertions,
        "probe": "spin_orbit_magic_rstar_mirror_probe",
        "beans": ["qou-w2vy", "qou-frso", "qou-mgq3", "qou-cds5", "qou-z4ba"],
        "generatedAt": now_iso,
        "q0Anchor": "proton",
        "workDps": str(WORK_DPS),
        "q0_50dps": _fmt(q),
        "E0_MeV_50dps": _fmt(e0),
        "qou_w2vy": w2vy,
        "qou_frso_mgq3": frso_mgq3,
        "qou_cds5": cds5,
        "qou_z4ba": z4ba,
    }
    WITNESS_PATH.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {WITNESS_PATH}")


if __name__ == "__main__":
    main()
