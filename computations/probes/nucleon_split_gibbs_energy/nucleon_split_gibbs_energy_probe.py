"""80-dps numbers for the nucleon split read as free energy F vs internal energy U.

Closed forms from QOU.QBeta.NucleonSplitGibbsEnergy (all orders in q; the common trace drops
out of log Z_n - log Z_p = -2 ln q for every common factor). Variants are pre-registered in
PREREGISTRATION.md; none is selected by CODATA. Proton q0 anchor (muon also printed).
Beans qou-myts / qou-99qc.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import _path_bridge  # noqa: F401, E402
from _precision import fmt, set_compute_dps  # noqa: E402

DPS = 80
set_compute_dps(DPS)

import mpmath as mp  # noqa: E402
from mpmath import mpf  # noqa: E402

mp.mp.dps = max(mp.mp.dps, DPS)

from qou_substrate import codata as _codata  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta import qbeta_e0  # noqa: E402

M_E = mpf(_codata.codata("electron mass energy equivalent in MeV").value_str)
M_P = mpf(_codata.codata("proton mass energy equivalent in MeV").value_str)
M_N = mpf(_codata.codata("neutron mass energy equivalent in MeV").value_str)
DM_NP = M_N - M_P            # comparison only
QBETA = DM_NP - M_E          # comparison only


def variants(q):
    lq = mp.log(q)
    e0 = 1 / (q * (q - 1))                       # SpectatorEnergyMap.e0 (units of m_e)
    e0t = e0 * q ** 2 / (2 * q - 1)              # tower_ratio
    # numerical cross-check of both E0 against the canonical producer
    assert abs(e0 * M_E - qbeta_e0.order_zero(q=q, m_e=M_E)) < mpf(10) ** -60
    e0t_canon = qbeta_e0.canonical(q=q, m_e=M_E) / M_E
    F0 = 2 * e0 * lq                              # dF, kT = E0       (m_e)
    Ft = 2 * e0t * lq                             # dF, kT = E0_tower (m_e)
    U_D = F0                                      # dictionary: dU = dF = 2 dict units
    U_nat = -2 * (q - 1) ** 2 / q / (q - 1) ** 2  # -2(q-1)^2/q natural units x c_q^2 = -2/q
    U_T0 = 2 / (q * (2 * q - 1))
    U_Tt = 2 * q / (2 * q ** 2 - 1)
    out = {
        "q0": q, "E0_ord0_MeV": e0 * M_E, "E0_tower_MeV": e0t * M_E,
        "E0_tower_closed_vs_canonical": e0t - e0t_canon,
        "dF_ord0": F0, "dF_tower": Ft,
        "dU_dictionary": U_D, "dU_natural": U_nat, "dU_CAL1_ord0": U_T0, "dU_CAL1_tower": U_Tt,
        "TdS_dictionary": U_D - F0, "TdS_natural": U_nat - F0,
        "TdS_CAL1_ord0": U_T0 - F0, "TdS_CAL1_tower": U_Tt - Ft,
    }
    return out


SPLITS = ["dF_ord0", "dF_tower", "dU_dictionary", "dU_natural", "dU_CAL1_ord0", "dU_CAL1_tower"]


def main():
    wb = WitnessBuilder("nucleon-split-gibbs-energy", engine="mpmath")
    wb.set_description(
        "Nucleon split under the Gibbs map read as free energy F vs internal energy U "
        "(QOU.QBeta.NucleonSplitGibbsEnergy), four corpus temperature parametrisations, "
        "order-zero and tower E0, 80 dps; CODATA comparison only."
    )
    ok = True
    res = {}
    for name, q in (("proton", mpf(q_at(DPS))), ("muon", mpf(q_muon_at(DPS)))):
        r = variants(q)
        mev = {k: r[k] * M_E for k in SPLITS + ["TdS_dictionary", "TdS_natural",
                                                "TdS_CAL1_ord0", "TdS_CAL1_tower"]}
        res[name] = {"q0": fmt(q), "E0_ord0_MeV": fmt(r["E0_ord0_MeV"]),
                     "E0_tower_MeV": fmt(r["E0_tower_MeV"]),
                     "E0_tower_closed_minus_canonical": fmt(r["E0_tower_closed_vs_canonical"]),
                     "MeV": {k: fmt(v) for k, v in mev.items()},
                     "vs_dm_np": {k: fmt(mev[k] / DM_NP - 1) for k in SPLITS},
                     "vs_qbeta": {k: fmt(mev[k] / QBETA - 1) for k in SPLITS}}
        print(f"\n[{name}] q0 = {mp.nstr(q, 20)}  E0 = {mp.nstr(r['E0_ord0_MeV'], 12)}  "
              f"E0_tower = {mp.nstr(r['E0_tower_MeV'], 12)}  "
              f"(closed-canonical {mp.nstr(r['E0_tower_closed_vs_canonical'], 3)})")
        for k in SPLITS:
            print(f"  {k:16s} {mp.nstr(mev[k], 12):>16s} MeV   vs dm_np "
                  f"{mp.nstr(100 * (mev[k] / DM_NP - 1), 6):>9s} %   vs Q_beta "
                  f"{mp.nstr(100 * (mev[k] / QBETA - 1), 6):>9s} %")
        for k in ("TdS_dictionary", "TdS_natural", "TdS_CAL1_ord0", "TdS_CAL1_tower"):
            print(f"  {k:16s} {mp.nstr(mev[k], 12):>16s} MeV")
        good = (abs(r["TdS_dictionary"]) < mpf(10) ** -70 and r["TdS_CAL1_ord0"] < 0
                and r["TdS_CAL1_tower"] < 0 and r["dU_natural"] < 0)
        wb.add_assertion(f"{name}_lean_signs_reproduced", computed=bool(good), expected=True)
        ok &= bool(good)
    wb.add_data("lean_module", "QOU.QBeta.NucleonSplitGibbsEnergy")
    wb.add_data("beans_referenced", ["qou-myts", "qou-99qc"])
    wb.add_data("tower_check", "tower_weight_symmetry_check.py: tr_mu == tr_-mu exact, n=3,5,7")
    wb.add_data("selection", "none; variants pre-registered, CODATA comparison only")
    wb.add_data("anchors", res)
    wb.add_data("codata_comparison_only", {"dm_np": fmt(DM_NP), "qbeta": fmt(QBETA)})
    path = wb.save({"q0Anchor": "comparison"})
    print(f"\nwitness: {path}\nALL CHECKS {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
