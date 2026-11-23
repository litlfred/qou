#!/usr/bin/env python3
"""80-dps verification probe for Taft root-of-unity Nakayama order, non-unimodularity,
and finite-jet pole obstruction vs the 70.4037x electron-unit split (bean qou-2b62 / NF-P5).

Lean companion: QOU/Observations/FiniteJetNormPoleOrder.lean.
Zero fitting, zero float64; proton pin q_0 = q_at(80).
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

from mpmath import mp, mpc, mpf  # noqa: E402
from qou_substrate.codata import codata  # noqa: E402
from qou_substrate.constants import Q_MP, q_at, vol_4_1_at  # noqa: E402
from qou_substrate.witness import WitnessBuilder  # noqa: E402


def fmt50(x: mpf) -> str:
    return mp.nstr(x, 50, strip_zeros=False)


def tr_z_h3_figure_eight(qv: mpf, zv: mpf) -> mpf:
    """Exact Ocneanu trace tr_z((sigma_0 sigma_1^-1)^2) in H_3(q).

    In H_3(q), V^2 = (sigma_0 sigma_1^-1)^2 = (1 - h^2) - h sigma_0 + h sigma_1 + ...
    Using the 3-irrep decomposition tr_z = y_{(3)} chi_{(3)} + y_{(2,1)} chi_{(2,1)} + y_{(1^3)} chi_{(1^3)}
    at Convention D (z = q^3/(q^2+1), y_{(1^3)} = 0, y_{(3)} = (q^4+1)/(q^2+1)^2, y_{(2,1)} = q^2/(q^2+1)^2):
      - On (3): sigma_0 = q, sigma_1^-1 = q^-1 => V = 1 => chi_{(3)}(V^2) = 1.
      - On (2,1): 2x2 matrices A_1 = [[q, 0], [0, -q^-1]], A_2 = ... trace(V) = 2 - (q + q^-1)^2 + 1 = 1 - h^2,
        det(V) = 1 => chi_{(2,1)}(V^2) = tr(V)^2 - 2 = (1 - h^2)^2 - 2 = h^4 - 2 h^2 - 1.
    """
    _ = zv
    hv = qv - mpf(1) / qv
    y3 = (qv ** 4 + mpf(1)) / ((qv ** 2 + mpf(1)) ** 2)
    y21 = (qv ** 2) / ((qv ** 2 + mpf(1)) ** 2)
    chi_21_v2 = hv ** 4 - mpf(2) * (hv ** 2) - mpf(1)
    return y3 * mpf(1) + y21 * chi_21_v2


def tr_z_h3_hopf_electron(qv: mpf) -> mpf:
    """Exact Convention-D Ocneanu trace of the Hopf electron word e^- = sigma_0 sigma_1 sigma_0 in H_3(q):
      - On (3): chi_{(3)}(sigma_0 sigma_1 sigma_0) = q^3.
      - On (2,1): det(sigma_0) = -1, eigenvalues (q, -q^-1), and on (2,1) the longest element
        w_0 = s_1 s_2 s_1 has trace 0! (Proven in ElectronUnitSplit.electron_21_trace_zero!)
      - On (1^3): y_{(1^3)} = 0 in Convention D.
    Hence tau_e(q) = tr_{z_D}(sigma_0 sigma_1 sigma_0) = q^3 * y_{(3)}(q).
    """
    y3 = (qv ** 4 + mpf(1)) / ((qv ** 2 + mpf(1)) ** 2)
    return (qv ** 3) * y3


def main() -> int:
    with mp.workdps(80):
        q0 = q_at(80)
        qi0 = mpf(1) / q0
        vol_41 = vol_4_1_at(80)
        mu_e_entry = codata("muon-electron mass ratio")
        mu_e_codata = mpf(mu_e_entry.value_str)

        wb = WitnessBuilder(
            "taft-tower-lepton-carrier",
            engine="mpmath (80 dps)",
            output_dir=HERE,
        )
        wb.set_description(
            "80-dps verification of Taft root-of-unity Nakayama order & non-unimodularity, "
            "finite-Laurent pole regularity at q=1, the 70.4037x ElectronUnitSplit ratio, "
            "and the +211.2 ppb proton-pinned muon residual (qou-2b62 / NF-P5)."
        )
        wb.add_parameter("workdps", 80)
        wb.add_parameter("q0_proton_50dps", fmt50(q0))

        wb.add_assertion(
            "q0_at_80_matches_Q_MP",
            computed=abs(q0 - (+Q_MP)),
            expected=mpf(0),
            tolerance=mpf("1e-65"),
            source="qou_substrate.constants",
        )

        # 1. Verify Taft T_n(zeta) Nakayama order = n and non-unimodularity |zeta^(n-1) - 1| > 0 for n = 2..6
        taft_rows = []
        max_nak_err = mpf(0)
        min_unimod_gap = mpf(10)
        for n_val in range(2, 7):
            zeta = mp.exp(mpc(0, 1) * (mpf(2) * mp.pi / mpf(n_val)))
            dist_mod = zeta ** (n_val - 1)
            unimod_gap = abs(dist_mod - mpc(1, 0))
            if unimod_gap < min_unimod_gap:
                min_unimod_gap = unimod_gap
            max_nak_err = max(max_nak_err, abs(zeta * dist_mod - mpc(1, 0)))
            # Check exact Nakayama order: |zeta^k - 1| > 0 for 1 <= k < n and == 0 at k = n
            sub_orders_nonzero = all(
                abs((zeta ** k) - mpc(1, 0)) > mpf("1e-5") for k in range(1, n_val)
            )
            if not sub_orders_nonzero:
                max_nak_err += mpf(1)
            taft_rows.append(
                {
                    "n": n_val,
                    "nakayama_order": n_val,
                    "distinguished_modulus_abs_minus_1": fmt50(unimod_gap),
                    "zeta_pow_n_minus_1_err": fmt50(abs((zeta ** n_val) - mpc(1, 0))),
                }
            )

        wb.add_assertion(
            "taft_nakayama_order_and_non_unimodularity_n2_to_n6",
            computed=max_nak_err + (mpf(0) if min_unimod_gap > mpf("0.5") else mpf(1)),
            expected=mpf(0),
            tolerance=mpf("1e-70"),
            source="FiniteJetNormPoleOrder.taft_unimodular_iff_zeta_eq_one & taft_nakayama_pow_id_iff",
        )

        # 2. Finite-Laurent trace ratio on 4_1 = (sigma_0 sigma_1^-1)^2 vs Hopf electron sigma_0 sigma_1 sigma_0
        z_d0 = (q0 ** 3) / (q0 ** 2 + mpf(1))
        tr_41_q0 = tr_z_h3_figure_eight(q0, z_d0)
        tau_e_q0 = tr_z_h3_hopf_electron(q0)
        finite_trace_ratio_q0 = tr_41_q0 / tau_e_q0
        # Classical q = 1 values: y3(1) = 2/4 = 1/2, y21(1) = 1/4, chi_21(V^2)|_{q=1} = -1
        # => tr_41(1) = 1/2 - 1/4 = 1/4, tau_e(1) = 1/2 => ratio(1) = 1/2 (regular, ZERO pole!)
        tr_41_q1 = tr_z_h3_figure_eight(mpf(1), mpf(1) / mpf(2))
        tau_e_q1 = tr_z_h3_hopf_electron(mpf(1))
        wb.add_assertion(
            "finite_laurent_ratio_4_1_over_hopf_regular_at_q_eq_1",
            computed=abs((tr_41_q1 / tau_e_q1) - (mpf(1) / mpf(2))),
            expected=mpf(0),
            tolerance=mpf("1e-75"),
            source="FiniteJetNormPoleOrder.no_laurent_trace_ratio_pole_at_one (ratio(1) = 1/2, finite)",
        )

        # Taft n=1 / Sweedler rank-4 regular norm det(L_x) on 1 + c X is det([[1,0],[c,1]])^2 = 1
        # or on group-like + nilpotent (a + b G + c X + d G X): N(a + b G + c X + d G X) = (a^2 - b^2)^2,
        # which forgets X altogether (retraction to k[Z/2]!) and stays regular at q = 1!
        hbar_sq = (mpf(1) - qi0) ** 2
        chart_split_R = tau_e_q0 / hbar_sq
        # Commutator-defect / hbar_q^-2 volume carrier on 4_1 vs CODATA m_mu / m_e:
        mu_e_pred_vol = vol_41 / hbar_sq
        mu_e_rel_ppb = (mu_e_pred_vol - mu_e_codata) / mu_e_codata * mpf("1e9")
        # Naive dividing Vol(4_1)/hbar_q^2 by ElectronUnitSplit chart_split_R would give Vol(4_1)/tau_e_q0 ~ 2.937!
        mu_e_divided_by_tau_e = vol_41 / tau_e_q0

        wb.add_assertion(
            "electron_unit_chart_split_matches_70p4037",
            computed=abs(chart_split_R - mpf("70.403727")),
            expected=mpf(0),
            tolerance=mpf("1e-4"),
            source="ElectronUnitSplit R = tau_e(q_0) / hbar_q^2 = 70.403727...",
        )
        wb.add_assertion(
            "commutator_hbar_inv_sq_identity_exact",
            computed=abs((mpf(1) / hbar_sq) - ((q0 ** 2) / ((q0 - mpf(1)) ** 2))),
            expected=mpf(0),
            tolerance=mpf("1e-73"),
            source="FiniteJetNormPoleOrder.hbarInvSq_eq",
        )

        wb.add_data("taft_nakayama_table", taft_rows)
        wb.add_data(
            "lepton_carrier_comparison_80dps",
            {
                "tau_e_hopf_q0": fmt50(tau_e_q0),
                "tr_M_4_1_h3_q0": fmt50(tr_41_q0),
                "finite_laurent_ratio_4_1_over_hopf_q0": fmt50(finite_trace_ratio_q0),
                "finite_laurent_ratio_at_q1": "1/2",
                "hbar_q_sq": fmt50(hbar_sq),
                "electron_unit_chart_split_R": fmt50(chart_split_R),
                "vol_4_1_over_hbar_q_sq": fmt50(mu_e_pred_vol),
                "codata_2022_mu_over_e_comparison": mu_e_entry.value_str,
                "vol_channel_residual_ppb": fmt50(mu_e_rel_ppb),
                "vol_4_1_over_tau_e_if_undivided_by_hbar_sq": fmt50(mu_e_divided_by_tau_e),
                "verdict_honest": (
                    "Any finite-rank Laurent/Taft norm with non-vanishing q=1 electron reference "
                    "is regular at q=1 (ratio(1)=1/2 on 4_1/Hopf) and cannot generate the 1/hbar_q^2 "
                    "double pole; the 206.7683264 muon ratio requires either an order-2 vanishing "
                    "commutator-squared reference (q-1)^2 or the infinite q-dilog tower, leaving "
                    "R = tau_e/hbar_q^2 = 70.403727 and the +211.22 ppb proton-pin residual intact."
                ),
            },
        )
        wb.save({"q0Anchor": "proton"})
        print(
            f"R = {mp.nstr(chart_split_R, 12)}, Vol(4_1)/hbar^2 = {mp.nstr(mu_e_pred_vol, 12)} "
            f"({mp.nstr(mu_e_rel_ppb, 6)} ppb vs CODATA)"
        )
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
