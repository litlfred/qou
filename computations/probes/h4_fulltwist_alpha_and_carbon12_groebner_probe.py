#!/usr/bin/env python3
"""h4_fulltwist_alpha_and_carbon12_groebner_probe.py — 80-dps Multi-Crossing H_4(q)
Full-Twist Delta_4^2 Singlet Cell, GPMT Casimir Completion & Inductive Transfer-Matrix
Groebner-Shirshov Light/Medium Nuclear Compute (Lane N1, Bean qou-ki22 / Epic qou-8ffl).

Companion to Lean 4 formalization:
  `folio/quantum-observable-universe/lean/QOU/Nuclear/H4FullTwistAlphaCellAndGroebnerBridge.lean`
  (`namespace QOU.Nuclear.H4FullTwistAlphaCellAndGroebnerBridge`).

STRICT ANTI-FITTING & PRECISION DISCIPLINE
------------------------------------------
1. ZERO fitting to AME2020 binding energies or empirical separation energies.
   AME2020 (`codata_constants.ame_binding_mev`) is read strictly as an external
   validation reference (`delta_MeV = B_pred - B_AME`).
2. ZERO knot-volume hunting: never uses or revives the retired dead-exploratory
   `alpha_cluster_recursion.py` heuristic `64 m_e G + C(n_alpha, 2) m_e Vol(7^2_1)`.
3. ZERO binary64 (`float64`) arithmetic, ZERO `math` or `numpy` imports, ZERO raw
   JSON floats in the emitted witness (`witness_raw_float64_audit` = 0).
4. Evaluates every parameter-free algebraic branch at 80 decimal places (`mpmath`)
   at BOTH the 1-term proton pin `q_0` and the consistent 2-term Borromean pin `q_2t`
   (plus live CODATA-2022 muon pin `q_muon` for cross-anchor comparison stamping).
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

os.environ.setdefault("QOU_OUTPUT_DPS", "80")
os.environ.setdefault("QOU_COMPUTE_DPS", "95")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
for _p in (str(ROOT), str(ROOT / "substrate"), str(ROOT / "audits")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

from canonical_mass import (  # noqa: E402
    e0_hadronic_tower_mev,
    nucleon_mass_mev,
    two_term_lagrangian_proton_mass_mev,
    two_term_proton_neutron_mass_mev,
)
from codata_constants import M_E_MEV, _ame_entry, ame_binding_mev  # noqa: E402
from coulomb_energy import coulomb_energy_mev  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    q_at,
    q_muon_at,
    q_two_term_borromean_at,
)
from qou_substrate.witness import (  # noqa: E402
    WitnessBuilder,
    q0_comparison,
    record_upstream,
)

_UPSTREAM_RECORDS: list = []

TARGET_NUCLEI: list[tuple[str, int, int]] = [
    ("2H", 1, 1),
    ("3H", 1, 2),
    ("3He", 2, 1),
    ("4He", 2, 2),
    ("6Li", 3, 3),
    ("8Be", 4, 4),
    ("12C", 6, 6),
    ("16O", 8, 8),
    ("24Mg", 12, 12),
    ("40Ca", 20, 20),
]

AMU_MEV_CODATA2022_STR = "931.49410372"


# ── Pure-integer combinatorics (zero `math` module imports) ──────────────────
def _int_comb(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k_use = k if k <= n - k else n - k
    acc = 1
    for i in range(1, k_use + 1):
        acc = (acc * (n - k_use + i)) // i
    return acc


def _int_factorial(n: int) -> int:
    acc = 1
    for k in range(2, n + 1):
        acc *= k
    return acc


def _partitions_descending(n: int) -> list[tuple[int, ...]]:
    def _gen(rem: int, max_part: int):
        if rem == 0:
            yield ()
            return
        for part in range(min(rem, max_part), 0, -1):
            for tail in _gen(rem - part, part):
                yield (part,) + tail

    return list(_gen(n, n))


def _partition_count_dp(n: int) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1
    for part in range(1, n + 1):
        for s in range(part, n + 1):
            dp[s] += dp[s - part]
    return dp[n]


def _hook_length(shape: tuple[int, ...], r: int, c: int) -> int:
    arm = shape[r] - c - 1
    leg = sum(1 for r2 in range(r + 1, len(shape)) if shape[r2] > c)
    return arm + leg + 1


def _syt_dim(shape: tuple[int, ...]) -> int:
    n = sum(shape)
    prod = 1
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            prod *= _hook_length(shape, r, c)
    return _int_factorial(n) // prod


def _content_sum(shape: tuple[int, ...]) -> int:
    total = 0
    for r, row_len in enumerate(shape):
        for c in range(row_len):
            total += c - r
    return total


# ── Simplicial f-vectors matching AlphaSimplexCoordinationDerivation.lean ────
def _f1_simplex(A: int) -> int:
    if A <= 1:
        return 0
    if A == 2:
        return 1
    return 3 * A - 6


def _f2_simplex(A: int) -> int:
    if A <= 2:
        return 0
    return 3 * A - 8


def _f3_simplex(A: int) -> int:
    if A <= 3:
        return 0
    return A - 3


def _intra_alpha_edges(A: int) -> int:
    return 6 * (A // 4) + _int_comb(A % 4, 2)


def _intra_alpha_triangles(A: int) -> int:
    return 4 * (A // 4) + _int_comb(A % 4, 3)


def _intra_alpha_tetrahedra(A: int) -> int:
    return A // 4


def _cluster_nodes(A: int) -> int:
    return (A // 4) + (0 if (A % 4 == 0) else 1)


def _inter_cluster_edges(A: int) -> int:
    return _f1_simplex(_cluster_nodes(A))


def _inter_cluster_triangles(A: int) -> int:
    return _f2_simplex(_cluster_nodes(A))


def _total_cluster_edges(A: int) -> int:
    return _intra_alpha_edges(A) + _inter_cluster_edges(A)


# ── Section 1 & 2: H_4(q) Full-Twist & GPMT Closed Forms (Lean-mirrored) ─────
def _eval_h4_invariants(q: mp.mpf, nucleon_mode: str) -> dict[str, mp.mpf]:
    with mp.workdps(90):
        one = mp.mpf(1)
        qi = one / q
        h = q - qi
        hbar_q = (q - one) / q
        me = mp.mpf(str(M_E_MEV))
        e0_bare = me / (q * (q - one))
        e0_tower = mp.mpf(str(e0_hadronic_tower_mev(q=q)))
        z_d = (q ** 3) / (q ** 2 + one)
        z_gg = z_d - h / mp.mpf(2)
        z_nn = z_d - h

        q2_1 = q ** 2 + one
        q4_1 = q ** 4 + one
        q4_2_1 = q ** 4 + q ** 2 + one
        h4_mod_denom = (q2_1 ** 3) * q4_1 * q4_2_1

        # Convention-D surviving 2-row weights on H_4(q)
        w4_d = (q ** 8 + q ** 6 + q ** 4 + q ** 2 + one) / (q2_1 ** 4)
        w31_d = (q ** 2) * q4_2_1 / (q2_1 ** 4)
        w22_d = (q ** 4) / (q2_1 ** 4)

        # GPMT modified quantum dimensions on H_3(q) and H_4(q)
        d_mod_111 = -(q ** 3) / (q2_1 * q4_2_1)
        d_mod_211 = -(q ** 3) * q4_2_1 / ((q2_1 ** 3) * q4_1)
        d_mod_1111 = (q ** 7) / h4_mod_denom

        mu3_gpmt = -d_mod_111
        s_row3_h4_4 = -mp.mpf(3) * d_mod_211 + d_mod_1111
        mu4_gpmt_h4 = s_row3_h4_4 - mp.mpf(4) * mu3_gpmt

        # Direct H_4(Delta_4^+-2) definitions vs Lean closed-form rational expressions
        tr_d_pos_def = w4_d * (q ** 12) + mp.mpf(3) * w31_d * (q ** 4) + mp.mpf(2) * w22_d
        tr_d_pos_closed = (
            (q ** 4)
            * q4_1
            * (q ** 8 - q ** 6 + q ** 4 - q ** 2 + mp.mpf(2))
            / (q2_1 ** 2)
        )
        tr_d_neg_def = (
            w4_d * (q ** (-12)) + mp.mpf(3) * w31_d * (q ** (-4)) + mp.mpf(2) * w22_d
        )
        tr_d_neg_closed = (
            q4_1
            * (mp.mpf(2) * (q ** 8) - q ** 6 + q ** 4 - q ** 2 + one)
            / ((q ** 12) * (q2_1 ** 2))
        )

        casimir_d_def = mp.mpf(12) * w4_d + mp.mpf(12) * w31_d
        casimir_d_closed = mp.mpf(12) * q4_1 / (q2_1 ** 2)

        gpmt_ft_pos_def = (-mp.mpf(3) * d_mod_211) * (q ** (-4)) + d_mod_1111 * (q ** (-12))
        gpmt_ft_pos_closed = (
            mp.mpf(3) * (q ** 12)
            + mp.mpf(6) * (q ** 10)
            + mp.mpf(9) * (q ** 8)
            + mp.mpf(6) * (q ** 6)
            + mp.mpf(3) * (q ** 4)
            + one
        ) / ((q ** 5) * h4_mod_denom)

        gpmt_ft_neg_def = (-mp.mpf(3) * d_mod_211) * (q ** 4) + d_mod_1111 * (q ** 12)
        gpmt_ft_neg_closed = (
            (q ** 7)
            * (
                q ** 12
                + mp.mpf(3) * (q ** 8)
                + mp.mpf(6) * (q ** 6)
                + mp.mpf(9) * (q ** 4)
                + mp.mpf(6) * (q ** 2)
                + mp.mpf(3)
            )
            / h4_mod_denom
        )

        casimir_gpmt_def = (-mp.mpf(3) * d_mod_211) * mp.mpf(4) + d_mod_1111 * mp.mpf(12)
        casimir_gpmt_closed = (
            mp.mpf(12)
            * (q ** 3)
            * (q ** 8 + mp.mpf(2) * (q ** 6) + mp.mpf(4) * (q ** 4) + mp.mpf(2) * (q ** 2) + one)
            / h4_mod_denom
        )

        wigner_singlet_pos_def = d_mod_1111 * (q ** (-12))
        wigner_singlet_pos_closed = one / ((q ** 5) * h4_mod_denom)

        # Energy scales & bond / cell terms (bare E_0^(0) and tower E_0^(tower))
        b2_log_d_bare = e0_bare * mp.log(one / z_d)
        b2_log_gg_bare = e0_bare * mp.log(one / z_gg)
        b2_log_d_tower = e0_tower * mp.log(one / z_d)
        b2_log_gg_tower = e0_tower * mp.log(one / z_gg)

        w3_bare = e0_bare * mu3_gpmt
        w4_bare = e0_bare * mu4_gpmt_h4
        w3_tower = e0_tower * mu3_gpmt
        w4_tower = e0_tower * mu4_gpmt_h4

        # Intra-alpha K_4 cell energies across parameter-free H_4(q) branches:
        #   - Cell A_logD: 6 * b2_log_D + 4 * w3 + w4  (1-crossing simplex baseline)
        #   - Cell A_logGG: 6 * b2_log_gg + 4 * w3 + w4 (1-crossing gg simplex baseline)
        #   - Cell B1_gg_gpmtCas: 6 * b2_log_gg + E0 * casimirGPMTRow3(q)
        #       (6 achiral edges + H_4 GPMT >=3-row full-twist Casimir <-2*kappa>_{GPMT,>=3})
        #   - Cell B2_hopf2_logD_sRow3: 12 * b2_log_D + E0 * sRow3GPMT_H4(4)
        #       (length-12 full twist = 2 crossings on each of 6 K_4 edges + GPMT >=3-row sum)
        #   - Cell B3_unfactored_word: E0 * (-ln(tr_D(Delta_4^-2)) + gpmtRow3FullTwistPos(q))
        #       (single global 4-strand word without 6-edge pair decomposition)
        cell_a_logd_bare = mp.mpf(6) * b2_log_d_bare + mp.mpf(4) * w3_bare + w4_bare
        cell_a_loggg_bare = mp.mpf(6) * b2_log_gg_bare + mp.mpf(4) * w3_bare + w4_bare
        cell_b1_bare = mp.mpf(6) * b2_log_gg_bare + e0_bare * casimir_gpmt_closed
        cell_b1_tower = mp.mpf(6) * b2_log_gg_tower + e0_tower * casimir_gpmt_closed
        cell_b2_bare = mp.mpf(12) * b2_log_d_bare + e0_bare * s_row3_h4_4
        cell_b2_tower = mp.mpf(12) * b2_log_d_tower + e0_tower * s_row3_h4_4
        cell_b3_bare = e0_bare * (mp.log(one / tr_d_neg_closed) + gpmt_ft_pos_closed)

        if nucleon_mode == "two_term":
            mp_2t, mn_2t = two_term_proton_neutron_mass_mev(weighting="plain", q=q)
            m_p = mp.mpf(str(mp_2t))
            m_n = mp.mpf(str(mn_2t))
            m_p_lagr = mp.mpf(str(two_term_lagrangian_proton_mass_mev(q=q)))
        else:
            m_p = mp.mpf(str(nucleon_mass_mev("p")))
            m_n = mp.mpf(str(nucleon_mass_mev("n")))
            m_p_lagr = m_p

        return {
            "q": q,
            "qi": qi,
            "h": h,
            "hbar_q": hbar_q,
            "m_e_MeV": me,
            "m_p_MeV": m_p,
            "m_n_MeV": m_n,
            "m_p_lagrangian_check_MeV": m_p_lagr,
            "E0_bare_MeV": e0_bare,
            "E0_tower_MeV": e0_tower,
            "z_D": z_d,
            "z_gg": z_gg,
            "z_nn": z_nn,
            "w4_D": w4_d,
            "w31_D": w31_d,
            "w22_D": w22_d,
            "dMod111": d_mod_111,
            "dMod211": d_mod_211,
            "dMod1111": d_mod_1111,
            "mu3GPMT_H4": mu3_gpmt,
            "sRow3GPMT_H4_4": s_row3_h4_4,
            "mu4GPMT_H4": mu4_gpmt_h4,
            "trConventionDFullTwistPos": tr_d_pos_closed,
            "trConventionDFullTwistPos_identity_gap": abs(tr_d_pos_def - tr_d_pos_closed),
            "trConventionDFullTwistNeg": tr_d_neg_closed,
            "trConventionDFullTwistNeg_identity_gap": abs(tr_d_neg_def - tr_d_neg_closed),
            "casimirConventionD": casimir_d_closed,
            "casimirConventionD_identity_gap": abs(casimir_d_def - casimir_d_closed),
            "gpmtRow3FullTwistPos": gpmt_ft_pos_closed,
            "gpmtRow3FullTwistPos_identity_gap": abs(gpmt_ft_pos_def - gpmt_ft_pos_closed),
            "gpmtRow3FullTwistNeg": gpmt_ft_neg_closed,
            "gpmtRow3FullTwistNeg_identity_gap": abs(gpmt_ft_neg_def - gpmt_ft_neg_closed),
            "casimirGPMTRow3": casimir_gpmt_closed,
            "casimirGPMTRow3_identity_gap": abs(casimir_gpmt_def - casimir_gpmt_closed),
            "wignerSingletGPMTFullTwistPos": wigner_singlet_pos_closed,
            "wignerSingletGPMTFullTwistPos_identity_gap": abs(
                wigner_singlet_pos_def - wigner_singlet_pos_closed
            ),
            "b2_logD_bare_MeV": b2_log_d_bare,
            "b2_logGG_bare_MeV": b2_log_gg_bare,
            "b2_logD_tower_MeV": b2_log_d_tower,
            "b2_logGG_tower_MeV": b2_log_gg_tower,
            "w3_bare_MeV": w3_bare,
            "w4_bare_MeV": w4_bare,
            "w3_tower_MeV": w3_tower,
            "w4_tower_MeV": w4_tower,
            "cell_A_logD_bare_MeV": cell_a_logd_bare,
            "cell_A_logGG_bare_MeV": cell_a_loggg_bare,
            "cell_B1_gg_gpmtCas_bare_MeV": cell_b1_bare,
            "cell_B1_gg_gpmtCas_tower_MeV": cell_b1_tower,
            "cell_B2_hopf2_logD_sRow3_bare_MeV": cell_b2_bare,
            "cell_B2_hopf2_logD_sRow3_tower_MeV": cell_b2_tower,
            "cell_B3_unfactored_word_bare_MeV": cell_b3_bare,
        }


# ── Section 4: Inductive 2x2 Transfer-Matrix Groebner-Shirshov Reduction ─────
def _tm_step(
    h: mp.mpf, c_val: mp.mpf, d_val: mp.mpf, a_vec: mp.mpf, b_vec: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    """Exact 2x2 transfer-matrix step `tmGeneral h c d *v ![a, b]` from Lean §4."""
    a_next = (c_val * h + d_val) * a_vec + c_val * b_vec
    b_next = c_val * a_vec + d_val * b_vec
    return a_next, b_next


def _inductive_tm_groebner_nucleus(
    Z: int, N: int, q: mp.mpf, color_weighted_pn: bool = True
) -> dict[str, mp.mpf]:
    """O(A^2) inductive transfer-matrix Groebner-Shirshov normal-form evaluation
    (`tm-inductive-construction.md:9-49` & Lean `crossingChain_eq_tmProduct_nf`).

    Nucleon ordering `[p, ..., p, n, ..., n]` (`A = Z + N` nucleons, generators
    `sigma_0 .. sigma_{A-2}`). At generator `sigma_i`, each downstream nucleon
    `j in {i+1 .. A-1}` multiplies `(a_i, b_i)` by `tmGeneral(h, c_{ij}, d_{ij})`,
    requiring ZERO Yang-Baxter and ZERO far-commutativity steps.
    """
    with mp.workdps(90):
        one = mp.mpf(1)
        h = q - one / q
        z_d = (q ** 3) / (q ** 2 + one)
        delta_flavour = ((q - one) ** 2) * (one - q ** (-4)) / mp.mpf(3)
        d_pp = mp.mpf(0)
        d_nn = -h
        if color_weighted_pn:
            d_pn = -h * (mp.mpf(1) / mp.mpf(2) - delta_flavour / mp.mpf(4))
        else:
            d_pn = -h / mp.mpf(2)

        A = Z + N
        if A <= 1:
            return {
                "skein_prod_abs": one,
                "neg_ln_skein_prod": mp.mpf(0),
                "demand_l1_norm": mp.mpf(0),
                "crossing_count": mp.mpf(0),
            }

        skein_prod = one
        demand_l1 = mp.mpf(0)
        total_crossings = 0
        for i in range(A - 1):
            a_i = mp.mpf(0)
            b_i = one
            tau_i_is_p = i < Z
            for j in range(i + 1, A):
                tau_j_is_p = j < Z
                if tau_i_is_p and tau_j_is_p:
                    d_ij = d_pp
                elif (not tau_i_is_p) and (not tau_j_is_p):
                    d_ij = d_nn
                else:
                    d_ij = d_pn
                a_i, b_i = _tm_step(h, one, d_ij, a_i, b_i)
                total_crossings += 1
            v_hat_i = a_i * z_d + b_i
            skein_prod *= v_hat_i
            demand_l1 += abs(a_i)

        abs_prod = abs(skein_prod)
        return {
            "skein_prod_abs": abs_prod,
            "neg_ln_skein_prod": -mp.log(abs_prod),
            "demand_l1_norm": demand_l1,
            "crossing_count": mp.mpf(total_crossings),
        }


# ── Section 5: Exact 80-dps H_12(q) Wedderburn + GPMT Comparison ─────────────
def _ocneanu_weight_exact(shape: tuple[int, ...], q: mp.mpf, z: mp.mpf) -> mp.mpf:
    with mp.workdps(90):
        one = mp.mpf(1)
        num = one
        den = one
        for r, row_len in enumerate(shape):
            for c in range(row_len):
                num *= (q ** (2 * r)) * (q ** 2 - one - q * z) + (q ** (2 * c + 1)) * z
                h_rc = _hook_length(shape, r, c)
                den *= (q ** (2 * h_rc)) - one
        return num / den


def _ocneanu_gpmt_deriv_at_zd(
    shape: tuple[int, ...], q: mp.mpf
) -> tuple[int, mp.mpf]:
    """Compute the exact root multiplicity `m_{z_D}(shape)` of `(z - z_D)` in
    `w_{shape}(q, z)` and the exact m-th order GPMT residue
    `w_{shape}(q, z) / (z - z_D)^m |_{z = z_D}`.

    In cell `(r, c)`, evaluating the numerator linear factor at `z_D = q^3 / (q^2 + 1)` gives
      `q^{2r}(q^2 - 1 - q z_D) + q^{2c + 1} z_D = (q^{2c + 4} - q^{2r}) / (q^2 + 1)`,
    which vanishes if and only if `r - c = 2` (content `c - r = -2`).
    On every cell with `r - c = 2`, the factor simplifies identically to
      `(q^{2c + 1} - q^{2r + 1}) * (z - z_D) = -q^{2r - 3} * (q^4 - 1) * (z - z_D)`.
    """
    with mp.workdps(90):
        one = mp.mpf(1)
        z_d = (q ** 3) / (q ** 2 + one)
        zero_mult = 0
        num_reg = one
        den = one
        for r, row_len in enumerate(shape):
            for c in range(row_len):
                h_rc = _hook_length(shape, r, c)
                den *= (q ** (2 * h_rc)) - one
                if r - c == 2:
                    zero_mult += 1
                    # Exact linear coefficient in (z - z_D): q^{2c + 1} - q^{2r + 1}
                    num_reg *= (q ** (2 * c + 1)) - (q ** (2 * r + 1))
                else:
                    num_reg *= (
                        (q ** (2 * r)) * (q ** 2 - one - q * z_d)
                        + (q ** (2 * c + 1)) * z_d
                    )
        return zero_mult, num_reg / den


def _evaluate_h12_comparison(q: mp.mpf, check_upstream_witness: bool) -> dict[str, object]:
    with mp.workdps(90):
        one = mp.mpf(1)
        z_d = (q ** 3) / (q ** 2 + one)
        shapes12 = _partitions_descending(12)

        two_row_rows = []
        sum_dim_w = mp.mpf(0)
        tr_ft_pos = mp.mpf(0)
        tr_ft_neg = mp.mpf(0)
        casimir_2row = mp.mpf(0)

        mult_counts = {0: 0, 1: 0, 2: 0, 3: 0}
        simple_zero_sum_abs = mp.mpf(0)
        rect_3333_info: dict[str, str] = {}

        wit_map: dict[tuple[int, ...], mp.mpf] = {}
        max_wit_diff = mp.mpf(0)
        h12_wit_path = ROOT / "alpha" / "alpha-k-jones-markov-h12.witness.json"
        if check_upstream_witness and h12_wit_path.exists():
            h12_doc = record_upstream(h12_wit_path, _UPSTREAM_RECORDS)
            for item in h12_doc.get("data", {}).get("y_lambda_table", []):
                wit_map[tuple(item["partition"])] = mp.mpf(str(item["y_lambda"]))

        for sh in shapes12:
            d_lam = _syt_dim(sh)
            kappa = _content_sum(sh)
            mult, coeff = _ocneanu_gpmt_deriv_at_zd(sh, q)
            mult_counts[mult] = mult_counts.get(mult, 0) + 1

            if len(sh) <= 2:
                w_lam = _ocneanu_weight_exact(sh, q, z_d)
                sum_dim_w += mp.mpf(d_lam) * w_lam
                tr_ft_pos += mp.mpf(d_lam) * w_lam * (q ** (2 * kappa))
                tr_ft_neg += mp.mpf(d_lam) * w_lam * (q ** (-2 * kappa))
                casimir_2row += mp.mpf(d_lam) * w_lam * mp.mpf(2 * kappa)
                row_entry: dict[str, object] = {
                    "partition": list(sh),
                    "syt_dim": d_lam,
                    "content_sum": kappa,
                    "full_twist_exponent": 2 * kappa,
                    "w_convention_D": fmt(w_lam),
                }
                if sh in wit_map:
                    diff = abs(w_lam - wit_map[sh])
                    if diff > max_wit_diff:
                        max_wit_diff = diff
                    row_entry["h12_witness_abs_diff"] = fmt(diff)
                two_row_rows.append(row_entry)
            elif mult == 1:
                simple_zero_sum_abs += mp.mpf(d_lam) * abs(coeff)

            if sh == (3, 3, 3, 3):
                rect_3333_info = {
                    "partition": [3, 3, 3, 3],
                    "syt_dim": str(d_lam),
                    "content_sum": str(kappa),
                    "zD_root_multiplicity": str(mult),
                    "second_order_gpmt_coeff_w_over_z_minus_zD_sq": fmt(coeff),
                    "explanation": (
                        "Rectangular 4-row SU(4)-singlet cabled shape (3,3,3,3) contains TWO "
                        "cells of content -2: (2,0) and (3,1), giving a second-order zero "
                        "(z - z_D)^2 under Convention D and requiring the 2nd-order GPMT trace."
                    ),
                }

        # Borromean multiplicative vs H_12 check at 80 dps
        h = q - one / q
        tr_bor = (mp.mpf(4) + h ** 2 - mp.mpf(3) * (h ** 4) - (h ** 6)) / (h ** 2 + mp.mpf(4))
        tr_he4_disjoint_bor4 = tr_bor ** 4

        out: dict[str, object] = {
            "total_partitions_of_12": len(shapes12),
            "surviving_two_row_partitions_count": len(two_row_rows),
            "killed_three_plus_row_partitions_count": len(shapes12) - len(two_row_rows),
            "zD_root_multiplicity_histogram": {str(k): v for k, v in sorted(mult_counts.items())},
            "two_row_sum_dim_mul_weight": fmt(sum_dim_w),
            "two_row_normalization_residual": fmt(abs(sum_dim_w - one)),
            "tr_H12_conventionD_fullTwist_pos": fmt(tr_ft_pos),
            "tr_H12_conventionD_fullTwist_neg": fmt(tr_ft_neg),
            "casimir_H12_conventionD_two_row": fmt(casimir_2row),
            "gpmt_H12_first_order_simple_zero_weighted_sum_abs": fmt(simple_zero_sum_abs),
            "rectangular_3333_cabled_singlet_diagnostic": rect_3333_info,
            "disjoint_four_borromean_trM_fourth_power": fmt(tr_he4_disjoint_bor4),
            "two_row_table": two_row_rows,
        }
        if check_upstream_witness and wit_map:
            out["max_abs_diff_vs_f64_h12_witness"] = fmt(max_wit_diff)
        return out


# ── Evaluate all branches across the 10 target nuclei at a given q pin ───────
def _ame_sigma_total_mev(Z: int, A: int) -> mp.mpf:
    with mp.workdps(90):
        entry = _ame_entry(Z, A)
        unc_kev = entry.get("binding_energy_per_A_unc_keV")
        if unc_kev is None:
            return mp.mpf(0)
        return mp.mpf(str(unc_kev)) * mp.mpf(A) / mp.mpf(1000)


def _metrics(b_pred: mp.mpf, b_ame: mp.mpf, sigma_ame: mp.mpf) -> dict[str, str]:
    delta = b_pred - b_ame
    rel = delta / b_ame
    sig = (delta / sigma_ame) if sigma_ame > mp.mpf(0) else mp.mpf(0)
    return {
        "B_pred_MeV": fmt(b_pred),
        "delta_MeV": fmt(delta),
        "err_pct": fmt(rel * mp.mpf(100)),
        "err_ppQ": fmt(rel),
        "err_sigma": fmt(sig),
    }


def _evaluate_nuclear_table(inv: dict[str, mp.mpf]) -> dict[str, object]:
    with mp.workdps(90):
        q = inv["q"]
        e0_bare = inv["E0_bare_MeV"]
        e0_tower = inv["E0_tower_MeV"]
        b2_d_bare = inv["b2_logD_bare_MeV"]
        b2_gg_bare = inv["b2_logGG_bare_MeV"]
        b2_d_tower = inv["b2_logD_tower_MeV"]
        b2_gg_tower = inv["b2_logGG_tower_MeV"]
        w3_bare = inv["w3_bare_MeV"]
        w4_bare = inv["w4_bare_MeV"]
        w3_tower = inv["w3_tower_MeV"]
        w4_tower = inv["w4_tower_MeV"]

        cell_b1_bare = inv["cell_B1_gg_gpmtCas_bare_MeV"]
        cell_b1_tower = inv["cell_B1_gg_gpmtCas_tower_MeV"]
        cell_b2_bare = inv["cell_B2_hopf2_logD_sRow3_bare_MeV"]
        cell_b2_tower = inv["cell_B2_hopf2_logD_sRow3_tower_MeV"]

        m_p = inv["m_p_MeV"]
        m_n = inv["m_n_MeV"]
        m_e = inv["m_e_MeV"]

        rows: list[dict[str, object]] = []
        by_name_strong_b1_tower: dict[str, mp.mpf] = {}
        by_name_ec: dict[str, mp.mpf] = {}
        by_name_ame: dict[str, mp.mpf] = {}

        for name, Z, N in TARGET_NUCLEI:
            A = Z + N
            b_ame = ame_binding_mev(Z, A)
            sig_ame = _ame_sigma_total_mev(Z, A)
            e_c = coulomb_energy_mev(Z, A, q=q)

            f1_3t, f2_3t, f3_3t = _f1_simplex(A), _f2_simplex(A), _f3_simplex(A)
            n_alpha = _intra_alpha_tetrahedra(A)
            rem = A % 4
            f1_rem = _int_comb(rem, 2)
            f2_rem = _int_comb(rem, 3)
            f1_inter = _inter_cluster_edges(A)
            f2_inter = _inter_cluster_triangles(A)
            f1_cl = _total_cluster_edges(A)
            f2_cl = _intra_alpha_triangles(A)

            # (a) 1-crossing simplicial pair-trace baselines
            b_a1_3t_logd = (
                mp.mpf(f1_3t) * b2_d_bare + mp.mpf(f2_3t) * w3_bare + mp.mpf(f3_3t) * w4_bare - e_c
            )
            b_a2_3t_loggg = (
                mp.mpf(f1_3t) * b2_gg_bare + mp.mpf(f2_3t) * w3_bare + mp.mpf(f3_3t) * w4_bare - e_c
            )
            b_a3_cl_1cross_logd = (
                mp.mpf(f1_cl) * b2_d_bare + mp.mpf(f2_cl) * w3_bare + mp.mpf(n_alpha) * w4_bare - e_c
            )
            b_a4_cl_1cross_loggg = (
                mp.mpf(f1_cl) * b2_gg_bare + mp.mpf(f2_cl) * w3_bare + mp.mpf(n_alpha) * w4_bare - e_c
            )

            # (b) Multi-crossing H_4(Delta_4^2) + GPMT intra-alpha cells + inter-cell transfer bridges:
            # Remainder r = A mod 4 sub-simplex (A=2: D, A=3: T/3He, A=6: 6Li = alpha + d):
            rem_strong_gg_bare = mp.mpf(f1_rem) * b2_gg_bare + mp.mpf(f2_rem) * w3_bare
            rem_strong_gg_tower = mp.mpf(f1_rem) * b2_gg_tower + mp.mpf(f2_rem) * w3_tower
            rem_strong_d_bare = mp.mpf(f1_rem) * b2_d_bare + mp.mpf(f2_rem) * w3_bare
            rem_strong_d_tower = mp.mpf(f1_rem) * b2_d_tower + mp.mpf(f2_rem) * w3_tower

            # B1a: H_4 GPMT Casimir alpha-cells + Convention-D 1-crossing inter-cluster bridges
            strong_b1_interD_bare = (
                mp.mpf(n_alpha) * cell_b1_bare
                + rem_strong_gg_bare
                + mp.mpf(f1_inter) * b2_d_bare
                + mp.mpf(f2_inter) * w3_bare
            )
            strong_b1_interD_tower = (
                mp.mpf(n_alpha) * cell_b1_tower
                + rem_strong_gg_tower
                + mp.mpf(f1_inter) * b2_d_tower
                + mp.mpf(f2_inter) * w3_tower
            )
            # B1b: H_4 GPMT Casimir alpha-cells + achiral gg inter-cluster bridges
            strong_b1_interGG_tower = (
                mp.mpf(n_alpha) * cell_b1_tower
                + rem_strong_gg_tower
                + mp.mpf(f1_inter) * b2_gg_tower
                + mp.mpf(f2_inter) * w3_tower
            )
            # B2: H_4 double-crossing (length-12 full-twist = 2 crossings/edge) + GPMT sRow3(4) + logD bridges
            strong_b2_interD_bare = (
                mp.mpf(n_alpha) * cell_b2_bare
                + rem_strong_d_bare
                + mp.mpf(f1_inter) * b2_d_bare
                + mp.mpf(f2_inter) * w3_bare
            )
            strong_b2_interD_tower = (
                mp.mpf(n_alpha) * cell_b2_tower
                + rem_strong_d_tower
                + mp.mpf(f1_inter) * b2_d_tower
                + mp.mpf(f2_inter) * w3_tower
            )

            b_b1_interD_bare = strong_b1_interD_bare - e_c
            b_b1_interD_tower = strong_b1_interD_tower - e_c
            b_b1_interGG_tower = strong_b1_interGG_tower - e_c
            b_b2_interD_bare = strong_b2_interD_bare - e_c
            b_b2_interD_tower = strong_b2_interD_tower - e_c

            # B4: Pure O(A^2) 2x2 transfer-matrix Groebner-Shirshov block-ordered chain
            tm_res = _inductive_tm_groebner_nucleus(Z, N, q, color_weighted_pn=True)
            b_tm_chain_bare = e0_bare * tm_res["neg_ln_skein_prod"] - e_c

            by_name_strong_b1_tower[name] = strong_b1_interD_tower
            by_name_ec[name] = e_c
            by_name_ame[name] = b_ame

            # Nuclear & neutral atomic masses (MeV) for each key branch
            m_constit_nuc = mp.mpf(Z) * m_p + mp.mpf(N) * m_n
            m_constit_atom = m_constit_nuc + mp.mpf(Z) * m_e

            row_dict: dict[str, object] = {
                "nuclide": name,
                "Z": Z,
                "N": N,
                "A": A,
                "N_alpha": n_alpha,
                "A_rem": rem,
                "p_3A_partition_count": _partition_count_dp(3 * A),
                "B_AME_MeV": fmt(b_ame),
                "sigma_AME_MeV": fmt(sig_ame),
                "E_C_MeV": fmt(e_c),
                "constituent_nuclear_mass_MeV": fmt(m_constit_nuc),
                "constituent_neutral_atom_mass_MeV": fmt(m_constit_atom),
                "topology": {
                    "f1_3tree": f1_3t,
                    "f2_3tree": f2_3t,
                    "f3_3tree": f3_3t,
                    "f1_intra_alpha": _intra_alpha_edges(A),
                    "f1_inter_cluster": f1_inter,
                    "f2_inter_cluster": f2_inter,
                    "f1_total_cluster": f1_cl,
                },
                "transfer_matrix_groebner_nf": {
                    "crossing_count_C_A_2": int(tm_res["crossing_count"]),
                    "abs_skein_polynomial_P_N": fmt(tm_res["skein_prod_abs"]),
                    "neg_ln_abs_P_N": fmt(tm_res["neg_ln_skein_prod"]),
                    "generator_demand_l1_norm": fmt(tm_res["demand_l1_norm"]),
                },
                "branches": {
                    "A1_1cross_3tree_logD_GPMT_bare": _metrics(b_a1_3t_logd, b_ame, sig_ame),
                    "A2_1cross_3tree_logGG_GPMT_bare": _metrics(b_a2_3t_loggg, b_ame, sig_ame),
                    "A3_1cross_cluster_logD_GPMT_bare": _metrics(b_a3_cl_1cross_logd, b_ame, sig_ame),
                    "A4_1cross_cluster_logGG_GPMT_bare": _metrics(b_a4_cl_1cross_loggg, b_ame, sig_ame),
                    "B1a_H4_gg_GPMTCasimir_interLogD_bare": _metrics(b_b1_interD_bare, b_ame, sig_ame),
                    "B1b_H4_gg_GPMTCasimir_interLogD_tower": _metrics(b_b1_interD_tower, b_ame, sig_ame),
                    "B1c_H4_gg_GPMTCasimir_interLogGG_tower": _metrics(b_b1_interGG_tower, b_ame, sig_ame),
                    "B2a_H4_fulltwist2x_logD_sRow3_interLogD_bare": _metrics(
                        b_b2_interD_bare, b_ame, sig_ame
                    ),
                    "B2b_H4_fulltwist2x_logD_sRow3_interLogD_tower": _metrics(
                        b_b2_interD_tower, b_ame, sig_ame
                    ),
                    "B4_inductive_TM_groebner_block_chain_bare": _metrics(
                        b_tm_chain_bare, b_ame, sig_ame
                    ),
                },
            }

            if name == "12C":
                m12_ame_atom = mp.mpf(12) * mp.mpf(AMU_MEV_CODATA2022_STR)
                m12_ame_nuc_est = m_constit_nuc - b_ame
                row_dict["carbon12_mass_diagnostics"] = {
                    "CODATA2022_12u_neutral_atom_MeV": fmt(m12_ame_atom),
                    "constituent_minus_B_AME_nuclear_MeV": fmt(m12_ame_nuc_est),
                    "M_nuc_A1_1cross_3tree_logD_MeV": fmt(m_constit_nuc - b_a1_3t_logd),
                    "M_nuc_B1b_H4_GPMTCas_interLogD_tower_MeV": fmt(
                        m_constit_nuc - b_b1_interD_tower
                    ),
                    "M_nuc_B1c_H4_GPMTCas_interLogGG_tower_MeV": fmt(
                        m_constit_nuc - b_b1_interGG_tower
                    ),
                    "M_nuc_B2b_H4_fulltwist2x_tower_MeV": fmt(
                        m_constit_nuc - b_b2_interD_tower
                    ),
                    "M_atom_B1b_H4_GPMTCas_interLogD_tower_MeV": fmt(
                        m_constit_atom - b_b1_interD_tower
                    ),
                    "M_atom_B1c_H4_GPMTCas_interLogGG_tower_MeV": fmt(
                        m_constit_atom - b_b1_interGG_tower
                    ),
                }

            rows.append(row_dict)

        # Explicit 8Be vs 2*4He and 12C vs 3*4He threshold diagnostics (Lean §5)
        delta_ec_be8 = by_name_ec["8Be"] - mp.mpf(2) * by_name_ec["4He"]
        delta_ec_c12 = by_name_ec["12C"] - mp.mpf(3) * by_name_ec["4He"]
        be8_vs_2he4_ame = by_name_ame["8Be"] - mp.mpf(2) * by_name_ame["4He"]
        c12_vs_3he4_ame = by_name_ame["12C"] - mp.mpf(3) * by_name_ame["4He"]

        be8_diff_interD_bare = b2_d_bare - delta_ec_be8
        be8_diff_interD_tower = b2_d_tower - delta_ec_be8
        be8_diff_interGG_tower = b2_gg_tower - delta_ec_be8

        c12_diff_interD_bare = mp.mpf(3) * b2_d_bare + w3_bare - delta_ec_c12
        c12_diff_interD_tower = mp.mpf(3) * b2_d_tower + w3_tower - delta_ec_c12
        c12_diff_interGG_tower = mp.mpf(3) * b2_gg_tower + w3_tower - delta_ec_c12

        # Direct verification that B_alpha cancels identically in B(8Be) - 2*B(4He)
        b_he4_b1 = by_name_strong_b1_tower["4He"] - by_name_ec["4He"]
        b_be8_b1 = by_name_strong_b1_tower["8Be"] - by_name_ec["8Be"]
        cancellation_gap_be8 = abs((b_be8_b1 - mp.mpf(2) * b_he4_b1) - be8_diff_interD_tower)

        thresholds = {
            "Be8_minus_2xHe4": {
                "AME2020_threshold_MeV": fmt(be8_vs_2he4_ame),
                "AME2020_is_unbound": be8_vs_2he4_ame < mp.mpf(0),
                "inter_alpha_coulomb_jump_MeV": fmt(delta_ec_be8),
                "inter_bridge_count": 1,
                "pred_diff_interLogD_bare_MeV": fmt(be8_diff_interD_bare),
                "pred_unbound_interLogD_bare": be8_diff_interD_bare < mp.mpf(0),
                "pred_diff_interLogD_tower_MeV": fmt(be8_diff_interD_tower),
                "pred_unbound_interLogD_tower": be8_diff_interD_tower < mp.mpf(0),
                "pred_diff_interLogGG_tower_MeV": fmt(be8_diff_interGG_tower),
                "pred_unbound_interLogGG_tower": be8_diff_interGG_tower < mp.mpf(0),
                "intra_cell_cancellation_identity_gap_MeV": fmt(cancellation_gap_be8),
            },
            "C12_minus_3xHe4_Hoyle_threshold": {
                "AME2020_threshold_MeV": fmt(c12_vs_3he4_ame),
                "AME2020_is_bound": c12_vs_3he4_ame > mp.mpf(0),
                "inter_alpha_coulomb_jump_MeV": fmt(delta_ec_c12),
                "inter_bridge_count": 3,
                "inter_triangle_count": 1,
                "pred_diff_interLogD_bare_MeV": fmt(c12_diff_interD_bare),
                "pred_bound_interLogD_bare": c12_diff_interD_bare > mp.mpf(0),
                "pred_diff_interLogD_tower_MeV": fmt(c12_diff_interD_tower),
                "pred_bound_interLogD_tower": c12_diff_interD_tower > mp.mpf(0),
                "pred_diff_interLogGG_tower_MeV": fmt(c12_diff_interGG_tower),
                "pred_bound_interLogGG_tower": c12_diff_interGG_tower > mp.mpf(0),
            },
        }

        return {
            "nuclei": rows,
            "multi_alpha_thresholds": thresholds,
            "_raw_cancellation_gap_be8": cancellation_gap_be8,
            "_raw_be8_diff_interD_bare": be8_diff_interD_bare,
            "_raw_be8_diff_interD_tower": be8_diff_interD_tower,
            "_raw_c12_diff_interD_bare": c12_diff_interD_bare,
            "_raw_c12_diff_interD_tower": c12_diff_interD_tower,
        }


def main() -> int:
    set_compute_dps(80)
    with mp.workdps(95):
        q0 = q_at(95)
        q2t = q_two_term_borromean_at(95, k_weighted=False)
        q_mu = q_muon_at(95)

        inv_q0 = _eval_h4_invariants(q0, nucleon_mode="one_term")
        inv_q2t = _eval_h4_invariants(q2t, nucleon_mode="two_term")

        tab_q0 = _evaluate_nuclear_table(inv_q0)
        tab_q2t = _evaluate_nuclear_table(inv_q2t)

        h12_q0 = _evaluate_h12_comparison(q0, check_upstream_witness=True)
        h12_q2t = _evaluate_h12_comparison(q2t, check_upstream_witness=False)

        # Why L1 stopped at A <= 6: exact partition & dimension growth table
        l1_scaling = []
        for name, Z, N in TARGET_NUCLEI:
            A = Z + N
            n_str = 3 * A
            p_3a = _partition_count_dp(n_str)
            two_row_cnt = (n_str // 2) + 1
            fact_digits = len(str(_int_factorial(n_str)))
            l1_scaling.append({
                "nuclide": name,
                "A": A,
                "n_color_strands_3A": n_str,
                "p_3A_total_partitions": p_3a,
                "convention_D_surviving_2row_partitions": two_row_cnt,
                "dim_H_3A_factorial_decimal_digits": fact_digits,
                "tm_groebner_matrix_steps_C_A_2": _int_comb(A, 2),
            })

        wb = WitnessBuilder(
            "h4-fulltwist-alpha-and-carbon12-groebner",
            engine="mpmath-80dps",
            output_dir=HERE,
        )
        if _UPSTREAM_RECORDS:
            wb.add_upstream_records(_UPSTREAM_RECORDS)

        wb.set_description(
            "80-dps parameter-free evaluation of the H_4(q) 4-strand full-twist Delta_4^2 "
            "framing spectrum, Convention-D + GPMT modified-trace alpha-cell functionals, "
            "inductive 2x2 transfer-matrix Groebner-Shirshov reduction, 8Be vs 2*4He and "
            "12C vs 3*4He multi-alpha breakup thresholds, and exact 80-dps H_12(q) Wedderburn "
            "comparison across 2H..40Ca at both q_0 and q_2t (Bean qou-ki22 / Epic qou-8ffl)."
        )

        wb.add_parameter("precision_dps", 80)
        wb.add_parameter("q0_proton_1term", fmt(q0))
        wb.add_parameter("q2t_two_term_borromean", fmt(q2t))
        wb.add_parameter("q0_muon_codata2022", fmt(q_mu))
        wb.add_parameter("zero_fitting", True)
        wb.add_parameter("zero_knot_volume_hunting", True)
        wb.add_parameter(
            "lean_companion",
            "folio/quantum-observable-universe/lean/QOU/Nuclear/H4FullTwistAlphaCellAndGroebnerBridge.lean",
        )
        wb.add_parameter("bean_id", "qou-ki22")
        wb.add_parameter("epic_id", "qou-8ffl")

        wb.add_data(
            "h4_partition_combinatorics",
            [
                {
                    "partition": list(sh),
                    "syt_dim": _syt_dim(sh),
                    "row_count": len(sh),
                    "content_sum": _content_sum(sh),
                    "full_twist_exponent_2kappa": 2 * _content_sum(sh),
                }
                for sh in _partitions_descending(4)
            ],
        )
        wb.add_data(
            "l1_obstruction_and_tm_compression_scaling",
            {
                "diagnosis": (
                    "L1 (`cross-check-trM-1ppb.witness.json` and `binding_combiner_markov_peel_fallback.py`) "
                    "stopped at A <= 6 (`4He` at H_12 with p(12)=77, `6Li` at H_18 with p(18)=385) for two "
                    "coupled reasons: (1) unfactored Hoefsmit Specht matrices on H_{3A} scale as p(3A) "
                    "partitions and sum d_lambda^2 = (3A)! (reaching p(36)=17,977 and 36! ~ 3.72e41 at 12C), "
                    "while unblocked markov_peel branches exponentially on non-commuting triples; and "
                    "(2) raw 1D open-chain |tr_M(free)| - |tr_M(atom)| has only A-1 interfaces and "
                    "w_lambda(z_D) = 0 on all ell(lambda) >= 3 blocks, omitting both 3D K_4 coordination "
                    "and GPMT modified-trace cumulants. Block-ordered 2x2 transfer-matrix Groebner-Shirshov "
                    "reduction (`crossingChain_eq_tmProduct_nf`) compresses C(A,2) crossings to O(A^2) "
                    "steps, and H_4(q) + GPMT supplies the closed-shell K_4 cell algebra."
                ),
                "nuclide_scaling_table": l1_scaling,
            },
        )
        wb.add_data(
            "at_q0_proton_1term",
            {
                "h4_invariants": {k: fmt(v) for k, v in inv_q0.items()},
                "benchmark_nuclei": tab_q0["nuclei"],
                "multi_alpha_thresholds": tab_q0["multi_alpha_thresholds"],
                "h12_exact_80dps_comparison": h12_q0,
            },
        )
        wb.add_data(
            "at_q2t_two_term_borromean",
            {
                "h4_invariants": {k: fmt(v) for k, v in inv_q2t.items()},
                "benchmark_nuclei": tab_q2t["nuclei"],
                "multi_alpha_thresholds": tab_q2t["multi_alpha_thresholds"],
                "h12_exact_80dps_comparison": h12_q2t,
            },
        )

        # Assertions mirroring the Lean 4 theorems in H4FullTwistAlphaCellAndGroebnerBridge.lean
        # across BOTH q_0 (1-term proton pin) and q_2t (2-term Borromean proton pin).
        _gap_keys = (
            "trConventionDFullTwistPos_identity_gap",
            "trConventionDFullTwistNeg_identity_gap",
            "casimirConventionD_identity_gap",
            "gpmtRow3FullTwistPos_identity_gap",
            "gpmtRow3FullTwistNeg_identity_gap",
            "casimirGPMTRow3_identity_gap",
            "wignerSingletGPMTFullTwistPos_identity_gap",
        )
        max_h4_id_gap = max(
            inv[k] for inv in (inv_q0, inv_q2t) for k in _gap_keys
        )
        wb.add_assertion(
            name="h4_fulltwist_and_gpmt_closed_form_identities_80dps",
            computed=fmt(max_h4_id_gap),
            expected="0",
            tolerance="1e-75",
            source="H4FullTwistAlphaCellAndGroebnerBridge.lean §3 rational closed forms at q_0 and q_2t",
        )
        wb.add_assertion(
            name="h4_partition_burnside_sum_sq_eq_24",
            computed=str(sum(_syt_dim(s) ** 2 for s in _partitions_descending(4))),
            expected="24",
            tolerance="0",
            source="h4Partition_sum_sytDim_sq : sum d_lambda^2 = 24 = 4!",
        )
        max_h12_norm_resid = max(
            mp.mpf(str(h12_q0["two_row_normalization_residual"])),
            mp.mpf(str(h12_q2t["two_row_normalization_residual"])),
        )
        wb.add_assertion(
            name="h12_two_row_conventionD_weights_sum_to_one_80dps",
            computed=fmt(max_h12_norm_resid),
            expected="0",
            tolerance="1e-75",
            source="Exact 80-dps 7-partition 2-row Ocneanu normalization on H_12(q_0) and H_12(q_2t)",
        )
        max_be8_cancel_gap = max(
            tab_q0["_raw_cancellation_gap_be8"],
            tab_q2t["_raw_cancellation_gap_be8"],
        )
        wb.add_assertion(
            name="be8_intra_cell_cancellation_identity_exact",
            computed=fmt(max_be8_cancel_gap),
            expected="0",
            tolerance="1e-70",
            source="be8_two_alpha_threshold_diff : B(8Be) - 2*B(4He) = b_inter - (E_C(8Be) - 2*E_C(4He)) at q_0 and q_2t",
        )
        wb.add_assertion(
            name="be8_unbound_and_c12_bound_under_conventionD_inter_bridges",
            computed=(
                "1"
                if (
                    tab_q0["_raw_be8_diff_interD_bare"] < mp.mpf(0)
                    and tab_q0["_raw_be8_diff_interD_tower"] < mp.mpf(0)
                    and tab_q0["_raw_c12_diff_interD_bare"] > mp.mpf(0)
                    and tab_q0["_raw_c12_diff_interD_tower"] > mp.mpf(0)
                    and tab_q2t["_raw_be8_diff_interD_bare"] < mp.mpf(0)
                    and tab_q2t["_raw_be8_diff_interD_tower"] < mp.mpf(0)
                    and tab_q2t["_raw_c12_diff_interD_bare"] > mp.mpf(0)
                    and tab_q2t["_raw_c12_diff_interD_tower"] > mp.mpf(0)
                )
                else "0"
            ),
            expected="1",
            tolerance="0",
            source="be8_two_alpha_threshold_diff & c12_three_alpha_threshold_diff at q_0 and q_2t (bare and tower E_0)",
        )

        wb.add_caveat(
            "cell_B1 (`6 * b2_logGG + E_0 * casimirGPMTRow3(q)`) and cell_B2 "
            "(`12 * b2_logD + E_0 * sRow3GPMT_H4(4)`) are parameter-free candidate "
            "multi-crossing K_4 alpha-cell functionals constructed from the exact H_4(q) "
            "full-twist and GPMT modified-trace invariants in "
            "`H4FullTwistAlphaCellAndGroebnerBridge.lean` §3; deriving a unique canonical "
            "projection from the 12-quark algebra H_12(q) onto H_4(q) remains open (Lane N5, "
            "bean qou-ozdk)."
        )
        wb.add_caveat(
            "All binding energies `B_pred_MeV`, Coulomb energies `E_C_MeV`, H_4(q) invariants, "
            "and H_12(q) Wedderburn traces are evaluated at full 80-dps precision at both q_0 "
            "and q_2t. In `at_q0_proton_1term`, the auxiliary constituent nucleon mass "
            "diagnostics (`m_p_MeV`, `m_n_MeV`, `constituent_nuclear_mass_MeV`, "
            "`constituent_neutral_atom_mass_MeV`) read `canonical_mass.nucleon_mass_mev`, "
            "whose decimal strings originate from the 50-dps upstream witness "
            "`m-p-substrate-identity-50dps.witness.json`; in `at_q2t_two_term_borromean`, "
            "`m_p_MeV` and `m_n_MeV` are evaluated directly at full 80-dps precision from "
            "`two_term_proton_neutron_mass_mev(q=q2t)`."
        )

        stamp = q0_comparison(
            muon=q_mu,
            proton=q0,
            reason=(
                "Lane N1 probe evaluates H_4(q) full-twist + GPMT alpha-cell and inductive "
                "Groebner-Shirshov nuclear binding side-by-side at the 1-term proton pin q_0 "
                "and consistent 2-term Borromean proton pin q_2t, recording live CODATA-2022 "
                "muon q_0 for cross-anchor reference."
            ),
        )
        saved_path = wb.save(stamp)
        saved_doc = json.loads(saved_path.read_text(encoding="utf-8"))

        import witness_raw_float64_audit as _f64_audit

        n_raw_floats = _f64_audit.count_raw_floats(saved_doc)
        if n_raw_floats != 0:
            raise RuntimeError(f"Emitted witness contains {n_raw_floats} raw float64 values!")

        # Print transparent console summary at q_2t
        print("=" * 124)
        print(
            "  Lane N1 (qou-ki22): 80-dps H_4(q) Full-Twist + GPMT & Inductive Groebner-Shirshov Probe (@ q_2t)"
        )
        print("=" * 124)
        print(f"  q_0  (1-term proton) = {mp.nstr(q0, 24)}")
        print(f"  q_2t (2-term proton) = {mp.nstr(q2t, 24)}")
        print(
            f"  E0^(0) = {mp.nstr(inv_q2t['E0_bare_MeV'], 10)} MeV | "
            f"E0^(tower) = {mp.nstr(inv_q2t['E0_tower_MeV'], 10)} MeV | "
            f"E0*Casimir_GPMT_H4 = {mp.nstr(inv_q2t['E0_bare_MeV'] * inv_q2t['casimirGPMTRow3'], 10)} MeV"
        )
        print("-" * 124)
        hdr = (
            f"{'Nucl':<5} {'Z':>2} {'N':>2} {'A':>2} | "
            f"{'B_AME':>10} {'E_C':>8} | "
            f"{'A1_3t_D':>10} {'A2_3t_gg':>10} {'B1b_CasD':>10} {'B1c_CasGG':>10} "
            f"{'B2b_FT2x':>10} {'B4_TM_GS':>10}"
        )
        print(hdr)
        print("-" * len(hdr))
        for r in tab_q2t["nuclei"]:
            br = r["branches"]
            print(
                f"{r['nuclide']:<5} {r['Z']:>2} {r['N']:>2} {r['A']:>2} | "
                f"{mp.nstr(mp.mpf(r['B_AME_MeV']), 7):>10} "
                f"{mp.nstr(mp.mpf(r['E_C_MeV']), 6):>8} | "
                f"{mp.nstr(mp.mpf(br['A1_1cross_3tree_logD_GPMT_bare']['B_pred_MeV']), 7):>10} "
                f"{mp.nstr(mp.mpf(br['A2_1cross_3tree_logGG_GPMT_bare']['B_pred_MeV']), 7):>10} "
                f"{mp.nstr(mp.mpf(br['B1b_H4_gg_GPMTCasimir_interLogD_tower']['B_pred_MeV']), 7):>10} "
                f"{mp.nstr(mp.mpf(br['B1c_H4_gg_GPMTCasimir_interLogGG_tower']['B_pred_MeV']), 7):>10} "
                f"{mp.nstr(mp.mpf(br['B2b_H4_fulltwist2x_logD_sRow3_interLogD_tower']['B_pred_MeV']), 7):>10} "
                f"{mp.nstr(mp.mpf(br['B4_inductive_TM_groebner_block_chain_bare']['B_pred_MeV']), 7):>10}"
            )
        print("-" * 124)
        t8 = tab_q2t["multi_alpha_thresholds"]["Be8_minus_2xHe4"]
        t12 = tab_q2t["multi_alpha_thresholds"]["C12_minus_3xHe4_Hoyle_threshold"]
        print(
            f"  8Be - 2*4He : AME = {mp.nstr(mp.mpf(t8['AME2020_threshold_MeV']), 6)} MeV | "
            f"interLogD(bare) = {mp.nstr(mp.mpf(t8['pred_diff_interLogD_bare_MeV']), 6)} MeV | "
            f"interLogD(tower) = {mp.nstr(mp.mpf(t8['pred_diff_interLogD_tower_MeV']), 6)} MeV "
            f"(UNBOUND={t8['pred_unbound_interLogD_tower']})"
        )
        print(
            f"  12C - 3*4He : AME = +{mp.nstr(mp.mpf(t12['AME2020_threshold_MeV']), 6)} MeV | "
            f"interLogD+w3(bare) = +{mp.nstr(mp.mpf(t12['pred_diff_interLogD_bare_MeV']), 6)} MeV | "
            f"interLogGG+w3(tower) = +{mp.nstr(mp.mpf(t12['pred_diff_interLogGG_tower_MeV']), 6)} MeV"
        )
        print(f"  Saved 80-dps witness (0 raw float64) -> {saved_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
