#!/usr/bin/env python3
"""80-dps numbers for the exact Gibbs n-p split with the Coulomb pair term (route 1 of item C1).

Lean: ``QOU.QBeta.NucleonSplitGibbsCoulomb`` -- m_n - m_p = 2E log q - lambda/3 with
E = k_B T_q = E0 (route T, ``SpectatorEnergyMap.kT_eq_e0``). Audit:
``docs/audits/2026-11-27-nucleon-split-gibbs-coulomb.md``. Bean ``qou-myts``.

lambda (Coulomb energy per unit charge product) is NOT derived. The probe evaluates the split for
the two on-record scale candidates alpha_em(q0)*E0 (order zero, the route-T temperature) and
alpha_em(q0)*E0_tower (``crossing_covariant_qed_probe.py``); alpha_em is the framework value
``alpha_em_inv_derived`` (conditional on the Witten-kappa Gram-determinant sorry). It also prints,
as a DIAGNOSTIC that adopts nothing, the lambda each CODATA reading would need
(``gibbs_coulomb_lambda_of_split``). CODATA enters only the comparison lines.

Run:  python3 -u computations/probes/nucleon_split_gibbs_coulomb_probe.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

set_compute_dps(80)

import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, 80)

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402
from meson_em_sinh_closed_form import alpha_em_inv_derived  # noqa: E402

DPS = 80
M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
M_P_EXP = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
M_N_EXP = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
DM_NP_EXP = M_N_EXP - M_P_EXP          # comparison only
QBETA_EXP = DM_NP_EXP - M_E            # comparison only


def split(E, q0, lam):
    return 2 * E * mp.log(q0) - lam / 3


def at_anchor(q0):
    E = qbeta_e0.order_zero(q=q0, m_e=M_E)          # route T: k_B T_q = E0
    E_twr = qbeta_e0.canonical(q=q0, m_e=M_E)
    alpha = 1 / mpf(alpha_em_inv_derived(q0))
    cell = 2 * E * mp.log(q0)
    out = {"q0": q0, "E0_ord0": E, "E0_tower": E_twr, "alpha_em_inv": 1 / alpha, "cell_c0": cell}
    for tag, lam in (("alphaE0_ord0", alpha * E), ("alphaE0_tower", alpha * E_twr)):
        s = split(E, q0, lam)
        out[f"lambda_{tag}"] = lam
        out[f"split_{tag}"] = s
        out[f"split_{tag}_vs_dm_np"] = s / DM_NP_EXP - 1
        out[f"split_{tag}_vs_qbeta"] = s / QBETA_EXP - 1
    out["diag_lambda_for_qbeta"] = 3 * (cell - QBETA_EXP)
    out["diag_lambda_for_dm_np"] = 3 * (cell - DM_NP_EXP)
    out["diag_lambda_for_qbeta_over_alphaE0"] = out["diag_lambda_for_qbeta"] * mpf(alpha_em_inv_derived(q0)) / E
    return out


def main():
    wb = WitnessBuilder("nucleon-split-gibbs-coulomb", engine="mpmath")
    wb.set_description(
        "80-dps evaluation of the exact Gibbs n-p split 2E0 log q - lambda/3 "
        "(QOU.QBeta.NucleonSplitGibbsCoulomb) for the on-record Coulomb scales alpha*E0 and "
        "alpha*E0_tower at both q0 anchors; the lambda each CODATA reading would need is a "
        "diagnostic only."
    )
    ok = True
    res = {}
    for name, q0 in (("proton", mpf(q_at(DPS))), ("muon", mpf(q_muon_at(DPS)))):
        r = at_anchor(q0)
        res[name] = {k: fmt(v) for k, v in r.items()}
        print(f"\n[{name}] q0 = {mp.nstr(q0, 20)}  alpha^-1 = {mp.nstr(r['alpha_em_inv'], 16)}")
        print(f"  cell 2E0 log q = {mp.nstr(r['cell_c0'], 12)} MeV")
        for tag in ("alphaE0_ord0", "alphaE0_tower"):
            print(f"  lambda = {tag}: {mp.nstr(1000 * r[f'lambda_{tag}'], 10)} keV -> split "
                  f"{mp.nstr(r[f'split_{tag}'], 12)} MeV "
                  f"[vs dm_np {mp.nstr(100 * r[f'split_{tag}_vs_dm_np'], 6)} %, "
                  f"vs Q_beta {mp.nstr(100 * r[f'split_{tag}_vs_qbeta'], 6)} %]")
        print(f"  DIAGNOSTIC lambda needed: Q_beta {mp.nstr(r['diag_lambda_for_qbeta'], 10)} MeV "
              f"(= {mp.nstr(r['diag_lambda_for_qbeta_over_alphaE0'], 8)} alpha E0), "
              f"dm_np {mp.nstr(r['diag_lambda_for_dm_np'], 10)} MeV (negative: attraction)")
        good = (r["split_alphaE0_ord0"] < r["cell_c0"]) and (r["split_alphaE0_ord0"] > 0) \
            and abs(split(r["E0_ord0"], q0, r["diag_lambda_for_qbeta"]) - QBETA_EXP) < mpf(10) ** -60
        wb.add_assertion(f"{name}_coulomb_lowers_and_inverse_consistent", computed=bool(good), expected=True)
        ok &= bool(good)
    wb.add_data("lean_module", "QOU.QBeta.NucleonSplitGibbsCoulomb")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("lambda_status", "not derived; alpha*E0 candidates are on-record scales, alpha_em conditional on the Witten-kappa Gram sorry")
    wb.add_data("anchors", res)
    wb.add_data("codata_comparison_only", {"dm_np": fmt(DM_NP_EXP), "qbeta": fmt(QBETA_EXP)})
    path = wb.save({"q0Anchor": "comparison"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
