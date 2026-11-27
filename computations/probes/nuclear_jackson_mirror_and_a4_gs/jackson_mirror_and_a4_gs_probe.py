#!/usr/bin/env python3
"""Pre-registered 80-dps Thomae-Jackson mirror-nuclei Coulomb ladder (A = 3, 7, 11, 13, 15, 17)
and A = 4 Hecke GS ordering probe (bean qou-otet / NF-P3).

Pre-registration: PREREGISTRATION.md (committed prior to computing any number).
Lean companion: QOU/Nuclear/K2TensorSquareGGMGauge.lean.

Zero free parameters, zero CODATA alpha, zero float64. Uses proton-pinned q_0 = q_at(80),
Form-B derived alpha_q(q_0), CAL-1 m_e, derived m_p(q_0), and CAL-3 m_pi.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
for _p in ("computations", "computations/substrate", "tools/qou-substrate/python"):
    if str(ROOT / _p) not in sys.path:
        sys.path.insert(0, str(ROOT / _p))

from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

from codata_constants import (  # noqa: E402
    AME_B_HE4_MEV_VALIDATION,
    M_PI_PM_MEV_VALIDATION,
    ame_binding_mev,
)
from mpmath import mp, mpf  # noqa: E402
from qou_substrate.constants import (  # noqa: E402
    M_E_MEV_STR,
    Q_MP,
    q_at,
    q_int_at,
    vol_4_1_at,
)
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def alpha_form_b_at(qv: mpf, dps: int = 80) -> mpf:
    """Form-B Bring-surface derived alpha_q(q) = (q [9]_q [10]_q + 2/(3 pi))^-1."""
    q9 = q_int_at(9, q=qv, dps=dps)
    q10 = q_int_at(10, q=qv, dps=dps)
    alpha_inv = qv * q9 * q10 + mpf(2) / (mpf(3) * mp.pi)
    return mpf(1) / alpha_inv


def derived_mp_mev(qv: mpf, me: mpf, dps: int = 80) -> mpf:
    """Derived proton mass m_p(q) from the QOU proton substrate identity."""
    qi = mpf(1) / qv
    hv = qv - qi
    hbar_sq = (mpf(1) - qi) ** 2
    vol = vol_4_1_at(dps)
    tr_m = abs((mpf(4) + hv ** 2 - mpf(3) * (hv ** 4) - hv ** 6) / (hv ** 2 + mpf(4)))
    qf3 = (qv ** 2 + mpf(1) + qi ** 2) * (qv + qi)
    f_bor = tr_m * qf3 / (qv ** 3)
    return me * (mpf(2) * vol / hbar_sq * f_bor - mpf(12))


def flavor_split_leading_mpf(qv: mpf) -> mpf:
    """Canonical flavor_split_leading(q) used in atom_braid_word_3A p-n interface."""
    import _path_bridge  # noqa: F401
    from _li_2_q_util import flavor_split_leading

    return +flavor_split_leading(qv)


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        h0 = q0 - qi0
        me = mpf(M_E_MEV_STR)
        mpi = +M_PI_PM_MEV_VALIDATION
        mp_q0 = derived_mp_mev(q0, me, dps=80)
        alpha_q0 = alpha_form_b_at(q0, dps=80)

        wb = WitnessBuilder(
            "jackson-mirror-and-a4-gs",
            engine="mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "Pre-registered 80-dps evaluation of out-of-sample mirror-nuclei (A=3,7,11,13,15,17) "
            "Thomae-Jackson proper-time Coulomb + SU_q(6) magnetic recoil splits, K^x2 -> G "
            "recursion/gauge checks, and A=4 Hecke GS ordering (qou-otet / NF-P3)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))
        wb.add_parameter("alpha_FormB_inv_q0", fmt50(mpf(1) / alpha_q0))
        wb.add_parameter("m_p_derived_MeV", fmt50(mp_q0))
        wb.add_parameter("m_pi_CAL3_MeV", fmt50(mpi))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # ------------------------------------------------------------------
        # Control 0: Verify K2TensorSquareGGMGauge Lean recurrences at 80 dps
        # ------------------------------------------------------------------
        # 0a. (-1)^m parity twist intertwining on GGM recurrence y_{m+2} = (2 - q^{m+1}) y_{m+1} - y_m
        y_seq = [mpf(1), mpf(2) - q0]
        for m_idx in range(8):
            y_next = (mpf(2) - (q0 ** (m_idx + 1))) * y_seq[-1] - y_seq[-2]
            y_seq.append(y_next)
        z_seq = [((-mpf(1)) ** m_idx) * y_seq[m_idx] for m_idx in range(len(y_seq))]
        max_parity_res = max(
            abs(z_seq[m_idx + 2] + (mpf(2) - (q0 ** (m_idx + 1))) * z_seq[m_idx + 1] + z_seq[m_idx])
            for m_idx in range(8)
        )
        wb.add_assertion(
            "ggm_parity_twist_gauge_residual_zero",
            computed=max_parity_res,
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="K2TensorSquareGGMGauge.parityTwist_solves_plus_iff_minus",
        )

        # 0b. 3rd-order symmetric-square recurrence on [m+2]_q b_{m+2} = b_{m+1} + b_m
        # Note QDifferenceConfluentObstruction.qint is classical 1 + q + ... + q^{k-1}
        def qint_class(k: int) -> mpf:
            return (q0 ** k - mpf(1)) / (q0 - mpf(1))

        b1 = [mpf(1), mpf(1)]
        b2 = [mpf(2), -mpf(1)]
        for m_idx in range(8):
            b1.append((b1[-1] + b1[-2]) / qint_class(m_idx + 2))
            b2.append((b2[-1] + b2[-2]) / qint_class(m_idx + 2))
        w_prod = [b1[i] * b2[i] for i in range(len(b1))]
        max_sym2_res = max(
            abs(
                qint_class(m_idx + 2) * (qint_class(m_idx + 3) ** 2) * w_prod[m_idx + 3]
                - (
                    (mpf(1) + qint_class(m_idx + 2))
                    * (qint_class(m_idx + 2) * w_prod[m_idx + 2] + w_prod[m_idx + 1])
                    - w_prod[m_idx]
                )
            )
            for m_idx in range(7)
        )
        wb.add_assertion(
            "binding_sym2_third_order_recurrence_residual_zero",
            computed=max_sym2_res,
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="K2TensorSquareGGMGauge.binding_sym2_third_order",
        )

        # ------------------------------------------------------------------
        # Part 1: Mirror-nuclei ladder A = 3, 7, 11, 13, 15, 17
        # ------------------------------------------------------------------
        tau0 = mp.log(q0)
        mu_sq = q0 * (q0 ** 2 - mpf(1))
        mu = mp.sqrt(mu_sq)
        base_coul_mev = alpha_q0 * mpi

        step_factors = {
            "backward": mpf(1) - (qi0 ** 2),
            "symmetric_cayley": mpf(2) * (q0 ** 2 - mpf(1)) / (q0 ** 2 + mpf(1)),
            "symmetric_arith": (q0 ** 2 - (qi0 ** 2)) / mpf(2),
            "forward": q0 ** 2 - mpf(1),
        }

        quad_integrals_norm: dict[str, mpf] = {}
        quad_integrals_unnorm: dict[str, mpf] = {}
        # Sum geometric proper-time grid tau_j = tau0 * q0^(2j) until exp(-mu^2 tau_j) < 1e-95
        raw_grid_sum = mpf(0)
        for j in range(600):
            tau_j = tau0 * (q0 ** (2 * j))
            exponent = -mu_sq * tau_j
            if exponent < mpf("-230"):
                break
            term = (mpf(1) / mp.sqrt(mp.pi * tau_j)) * mp.exp(exponent) * tau_j
            raw_grid_sum += term

        for qname, sfac in step_factors.items():
            quad_integrals_unnorm[qname] = sfac * raw_grid_sum
            quad_integrals_norm[qname] = mu * sfac * raw_grid_sum

        cont_norm = mp.erfc(mu * mp.sqrt(tau0))
        cont_unnorm = cont_norm / mu
        quad_integrals_norm["continuum_erfc"] = cont_norm
        quad_integrals_unnorm["continuum_erfc"] = cont_unnorm

        # Verify ordering backward < continuum < forward on normalized kernel
        wb.add_assertion(
            "jackson_quadrature_brackets_continuum",
            computed=mpf(
                0
                if (
                    quad_integrals_norm["backward"]
                    < cont_norm
                    < quad_integrals_norm["forward"]
                )
                else 1
            ),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Monotone decreasing Schwinger integrand bracketed by backward/forward Jackson sums",
        )

        # Constituent SU(6) / SU_q(6) magnetic recoil factors
        recoil_sq = (mpi / (mpf(2) * mp_q0)) ** 2
        su6_ratio = mpf(3) / mpf(2)
        suq6_ratio = q_int_at(3, q=q0, dps=80) / q_int_at(2, q=q0, dps=80)
        recoil_branches = {
            "coulomb_only": mpf(1),
            "su6_minus": mpf(1) - su6_ratio * recoil_sq,
            "su6_plus": mpf(1) + su6_ratio * recoil_sq,
            "suq6_minus": mpf(1) - suq6_ratio * recoil_sq,
        }

        mirror_pairs = [
            (3, 1, 2, "3H-3He"),
            (7, 3, 4, "7Li-7Be"),
            (11, 5, 6, "11B-11C"),
            (13, 6, 7, "13C-13N"),
            (15, 7, 8, "15N-15O"),
            (17, 8, 9, "17O-17F"),
        ]

        mirror_table = []
        for A_val, z_low, z_high, label in mirror_pairs:
            b_low = ame_binding_mev(z_low, A_val)
            b_high = ame_binding_mev(z_high, A_val)
            delta_b_ame = b_low - b_high
            n_pair_diff = (A_val - 1) // 2
            vol_scale = (mpf(3) / mpf(A_val)) ** (mpf(1) / mpf(3))

            preds_vol_norm = {}
            preds_unscaled_norm = {}
            preds_vol_unnorm = {}
            for qname in ("backward", "symmetric_cayley", "symmetric_arith", "forward", "continuum_erfc"):
                e_pair_norm = base_coul_mev * quad_integrals_norm[qname]
                e_pair_unnorm = base_coul_mev * quad_integrals_unnorm[qname]
                preds_vol_norm[qname] = {
                    rname: fmt50(mpf(n_pair_diff) * vol_scale * e_pair_norm * rfac)
                    for rname, rfac in recoil_branches.items()
                }
                preds_unscaled_norm[qname] = {
                    rname: fmt50(mpf(n_pair_diff) * e_pair_norm * rfac)
                    for rname, rfac in recoil_branches.items()
                }
                preds_vol_unnorm[qname] = {
                    "coulomb_only": fmt50(mpf(n_pair_diff) * vol_scale * e_pair_unnorm),
                    "su6_minus": fmt50(
                        mpf(n_pair_diff) * vol_scale * e_pair_unnorm * recoil_branches["su6_minus"]
                    ),
                }

            entry = {
                "A": A_val,
                "mirror_pair": label,
                "Z_low": z_low,
                "Z_high": z_high,
                "normal_ordered_pair_diff": n_pair_diff,
                "AME2020_DeltaB_MeV_comparison": fmt50(delta_b_ame),
                "normalized_kernel_volume_R_A13_MeV": preds_vol_norm,
                "normalized_kernel_unscaled_pairs_MeV": preds_unscaled_norm,
                "unnormalized_kernel_volume_R_A13_MeV": preds_vol_unnorm,
            }
            mirror_table.append(entry)
            p_back = mpf(preds_vol_norm["backward"]["su6_minus"])
            p_sym = mpf(preds_vol_norm["symmetric_cayley"]["su6_minus"])
            p_fwd = mpf(preds_vol_norm["forward"]["su6_minus"])
            print(
                f"A={A_val:2d} ({label:7s}) AME={mp.nstr(delta_b_ame, 7):9s} MeV | "
                f"norm+R(A^1/3)+SU6-: back={mp.nstr(p_back, 7)} sym={mp.nstr(p_sym, 7)} fwd={mp.nstr(p_fwd, 7)} MeV"
            )

        # ------------------------------------------------------------------
        # Part 2: A = 4 (^4He) Pre-Registered Nucleon Ordering via Hecke GS Length
        # ------------------------------------------------------------------
        z_d = (q0 ** 3) / (q0 ** 2 + mpf(1))
        w_d = z_d - h0
        delta_fl = flavor_split_leading_mpf(q0)
        r_pn = z_d - h0 * (mpf(1) / mpf(2) - delta_fl / mpf(4))
        e0_full_mev = me / (q0 * (q0 - mpf(1)) * (mpf(1) - (mpf(1) - qi0) ** 2))
        ame_he4 = +AME_B_HE4_MEV_VALIDATION

        # Cross-check exact cut-bridge bond formula on deuteron (1 p-n bond) against tr_m_atom_zn(1, 1)
        from tr_m_atom_via_transfer import tr_m_atom_zn

        tr_d_atom, tr_d_free = tr_m_atom_zn(1, 1, q=q0)[:2]
        wb.add_assertion(
            "cut_bridge_pn_bond_matches_deuteron_transfer_matrix",
            computed=abs(mpf(str(tr_d_atom)) / mpf(str(tr_d_free)) - r_pn),
            expected=mpf(0),
            tolerance=mpf("1e-48"),
            source="mass_at_3A_proper cut-bridge factorization on H_6(q_0)",
        )

        a4_orderings = [
            "ppnn",
            "nnpp",
            "nppn",
            "pnnp",
            "pnpn",
            "npnp",
        ]
        ordering_rows = []
        for ord_str in a4_orderings:
            n_pp = sum(1 for k in range(3) if ord_str[k : k + 2] == "pp")
            n_nn = sum(1 for k in range(3) if ord_str[k : k + 2] == "nn")
            n_pn = sum(1 for k in range(3) if ord_str[k] != ord_str[k + 1])
            # Hecke GS normal-form expansion terms at the 3 bridges:
            # pp = sigma (1 basis word), nn = sigma - h (2 words), pn = sigma - c_pn h (2 words)
            gs_interface_terms = (1 ** n_pp) * (2 ** n_pn) * (2 ** n_nn)
            # Braid inverse-rewrite steps (sigma^-1 -> sigma - h on nn, fractional on pn)
            gs_nonpos_bridges = n_pn + n_nn
            ratio_atom_free = (z_d ** n_pp) * (r_pn ** n_pn) * (w_d ** n_nn)
            b_log_chain_mev = e0_full_mev * mp.log(mpf(1) / ratio_atom_free)
            leading_h_coeff = -(mpf(n_pn) * (mpf(1) / mpf(2) - delta_fl / mpf(4)) + mpf(n_nn))
            ordering_rows.append(
                {
                    "ordering": ord_str,
                    "n_pp": n_pp,
                    "n_pn": n_pn,
                    "n_nn": n_nn,
                    "gs_interface_expansion_terms": gs_interface_terms,
                    "gs_nonpositive_bridges": gs_nonpos_bridges,
                    "tr_atom_over_tr_free": fmt50(ratio_atom_free),
                    "B_log_chain_MeV": fmt50(b_log_chain_mev),
                    "leading_h_bond_shift": fmt50(leading_h_coeff),
                    "AME_He4_MeV_comparison": fmt50(ame_he4),
                }
            )
            print(
                f"A=4 {ord_str}: (pp,pn,nn)=({n_pp},{n_pn},{n_nn}) GS_terms={gs_interface_terms} "
                f"B_log_chain={mp.nstr(b_log_chain_mev, 10)} MeV"
            )

        min_gs_terms = min(r["gs_interface_expansion_terms"] for r in ordering_rows)
        selected_by_min_gs = [
            r["ordering"] for r in ordering_rows if r["gs_interface_expansion_terms"] == min_gs_terms
        ]
        wb.add_assertion(
            "minimal_gs_terms_selects_pp_containing_orderings_over_alternating_pnpn",
            computed=mpf(0 if ("ppnn" in selected_by_min_gs and "pnpn" not in selected_by_min_gs) else 1),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="Pre-registered Hecke GS interface expansion count (4 terms for ppnn/nnpp/nppn vs 8 for pnpn/npnp/pnnp)",
        )

        wb.add_data("quadrature_factors_norm", {k: fmt50(v) for k, v in quad_integrals_norm.items()})
        wb.add_data("recoil_factors", {k: fmt50(v) for k, v in recoil_branches.items()})
        wb.add_data("mirror_nuclei_A3_to_A17", mirror_table)
        wb.add_data(
            "a4_gs_ordering",
            {
                "rows": ordering_rows,
                "min_gs_interface_terms": min_gs_terms,
                "selected_by_min_gs_terms": selected_by_min_gs,
            },
        )
        wb.save({"q0Anchor": "proton"})
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
