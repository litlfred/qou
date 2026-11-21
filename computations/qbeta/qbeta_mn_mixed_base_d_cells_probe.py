#!/usr/bin/env python3
"""Production m_n uses a mixed Q_β base. This probe records the convention-D cells beside it.

WHAT THIS RECORDS (mass gap 5; owner chose "label retired base, fail loudly",
2026-11-16). Production m_n is ``m_p + Q_β + m_e`` with
``Q_β = derived_masses.q_beta_kashiwara_n2_mev()``. That function puts a
convention-D phase (``z_D = q³/(q²+1)``) on top of the published Form A base
``Q_A = m_e|q²−2q−1|(q+1)/(2q³)``, and Form A is the ``z = 1`` cell that the
2026-09-08 ruling retired as inadmissible. So the production value mixes two
bases, and its +501 ppb on m_n is a property of the retired base, not of
convention D.

This probe evaluates the convention-D cells consistently:
``Q_β = |tr_{z_D}(element)|·E₀`` with ZERO ``c_k`` rungs, for every candidate
element in ``qbeta-option-e-required-level.witness.json`` and both E₀ forms
(``qbeta_e0.canonical`` = tower-summed, ``qbeta_e0.order_zero``). It then
reports ``m_n = m_p + Q_β + m_e`` and the shift from production.

WHAT IT DOES NOT DO. It changes no production value and selects no element.
The element choice is open (bean ``qou-99qc``; SDP reading 3 rejects even
``nuc11_interleaved``), and no ``c_k`` ladder exists on an admissible base
(``qou-cds1``). The rows are NOT ranked by residual, because ranking by residual
is selection against the target.

PIN. The census traces ``tr_conv_D`` are recorded at the proton pin, so every
D cell is evaluated at the proton pin (``q_parameter.Q_MP``, 90 significant digits).
``derived_masses`` computed Q_β at the muon pin until 2026-11-20 (bean ``qou-aj91``); it now uses the proton pin;
the probe records that separately as a second straddle and does not mix it into
the D cells. ``Delta_S`` has a closed-form trace, so it is also evaluated at the
muon pin to measure how much the pin itself moves a cell.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.witness import q0_comparison  # noqa: E402

set_compute_dps()

from codata_constants import M_E_MEV  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from qbeta_e0 import canonical as e0_tower, order_zero as e0_order_zero  # noqa: E402
import derived_masses  # noqa: E402
from canonical_mass import proton_neutron_mass_mev  # noqa: E402

HERE = Path(__file__).resolve().parent
CENSUS = HERE / "qbeta-option-e-required-level.witness.json"

# CODATA 2022 neutron mass (MeV). Used ONLY in the error column, never in a value.
M_N_CODATA = mp.mpf("939.56542194")


def _delta_s_trace(q):
    z = q ** 3 / (q ** 2 + 1)
    return q ** 2 / 2 - q * z - 1 + z / q + 1 / (2 * q ** 2)


def _ppb(x):
    return (x - M_N_CODATA) / M_N_CODATA * mp.mpf(10) ** 9


def main() -> int:
    m_e = mp.mpf(str(M_E_MEV))
    m_p_prod, m_n_prod = (mp.mpf(str(v)) for v in proton_neutron_mass_mev())
    q_beta_prod = mp.mpf(derived_masses.q_beta_kashiwara_n2_mev())
    q_a = mp.mpf(derived_masses.q_beta_predicted_mev())
    # main's rename (_q_0 -> _q_0_muon) is the clearer name and the direction of
    # travel; both still exist, so this is not a break-fix.  The proton pin stays
    # Q_MP (90 significant digits) rather than main's Q_50_DIGIT_STR (50): the two
    # agree only to 1.9e-50, and with OUTPUT_DPS = 60 a 50-digit input pads digits
    # 51-60 of every serialized result -- the float64-padding defect one order up.
    q_muon = mp.mpf(derived_masses._q_0_muon())
    q_prot = Q_MP

    census = json.loads(CENSUS.read_text())["data"]["per_candidate"]
    rows = []
    for elem, rec in census.items():
        tr = mp.mpf(rec["tr_conv_D"])
        for e0_name, e0_fn in (("tower", e0_tower), ("order_zero", e0_order_zero)):
            qb = abs(tr) * e0_fn(q=q_prot, m_e=m_e)
            m_n = m_p_prod + qb + m_e
            rows.append({
                "element": elem,
                "E0_form": e0_name,
                "pin": "proton",
                "Q_beta_MeV": fmt(qb),
                "m_n_MeV": fmt(m_n),
                "m_n_err_ppb": fmt(_ppb(m_n), 8),
                "shift_from_production_ppb": fmt(_ppb(m_n) - _ppb(m_n_prod), 8),
            })
    # Delta_S closed form at the muon pin: how much the pin alone moves a cell.
    tr_mu = _delta_s_trace(q_muon)
    qb_mu = abs(tr_mu) * e0_tower(q=q_muon, m_e=m_e)
    qb_pr = abs(_delta_s_trace(q_prot)) * e0_tower(q=q_prot, m_e=m_e)
    pin_shift_rel = (qb_mu - qb_pr) / qb_pr

    # The production formula itself, evaluated at the proton pin instead of
    # derived_masses' muon pin: the size of the q0 straddle on the production value.
    def _prod_formula(q):
        qa = m_e * abs(q ** 2 - 2 * q - 1) * (q + 1) / (2 * q ** 3)
        z = q ** 3 / (q ** 2 + 1)
        h = q - 1 / q
        hb = (q - 1) / q
        b = mp.sqrt(1 - q ** 2 / (q ** 2 + 1) ** 2)
        return qa * mp.cos((z - 1) * h / 2 - b * hb ** 2 / 2) * (1 - b ** 2 * hb ** 4)
    qprod_mu = _prod_formula(q_muon)
    qprod_pr = _prod_formula(q_prot)
    straddle_ppb = (qprod_pr - qprod_mu) / M_N_CODATA * mp.mpf(10) ** 9

    ds_check = abs(mp.mpf(census["delta_S_short_normal_form"]["tr_conv_D"])
                   - _delta_s_trace(q_prot))

    wb = WitnessBuilder("qbeta-mn-mixed-base-d-cells")
    wb.set_description(
        "Production m_n = m_p + Q_beta + m_e uses derived_masses."
        "q_beta_kashiwara_n2_mev, which applies a convention-D phase to the "
        "retired z=1 Form A base. Records the production value as "
        "'retired-mixed-base' and every convention-D cell (zero c_k rungs, "
        "both E0 forms, every census element) beside it. No element is "
        "selected and no production value changes (owner, 2026-11-16).")
    wb.add_data("production", {
        "status": "retired-mixed-base",
        "Q_beta_MeV": fmt(q_beta_prod),
        "Q_A_form_A_MeV": fmt(q_a),
        "m_p_MeV": fmt(m_p_prod),
        "m_n_MeV": fmt(m_n_prod),
        "m_n_err_ppb": fmt(_ppb(m_n_prod), 8),
        "Q_beta_pin": "proton (derived_masses._q_0; muon straddle removed 2026-11-20, PR #8591, bean qou-aj91)",
        "why_mixed": "base Q_A is the z=1 cell retired 2026-09-08; the phase "
                     "alpha=(z-1)h/2 uses z_D",
    })
    wb.add_data("d_cells", rows)
    wb.add_data("delta_S_pin_effect", {
        "Q_beta_tower_muon_MeV": fmt(qb_mu),
        "Q_beta_tower_proton_MeV": fmt(qb_pr),
        "relative_shift": fmt(pin_shift_rel, 8),
    })
    wb.add_data("production_q0_straddle", {
        "Q_beta_production_formula_muon_pin_MeV": fmt(qprod_mu),
        "Q_beta_production_formula_proton_pin_MeV": fmt(qprod_pr),
        "matches_derived_masses_at_muon": fmt(abs(qprod_mu - q_beta_prod), 6),
        "Q_beta_relative_shift": fmt((qprod_pr - qprod_mu) / qprod_mu, 8),
        "m_n_shift_ppb": fmt(straddle_ppb, 8),
    })
    wb.add_data("open", {
        "element_choice": "qou-99qc (SDP reading 3 rejects nuc11_interleaved)",
        "ladder_on_admissible_base": "qou-cds1 (none exists)",
        "E0_tower_series": "qou-y3bm (canonical by ruling, not derived)",
    })
    wb.add_caveat("Rows are not ranked by residual. Choosing an element by "
                  "its m_n error would be selection against the target.")
    wb.add_assertion("delta_S_closed_form_matches_census",
                     computed=fmt(ds_check, 6), expected="0",
                     tolerance="1e-20",
                     source="tr_{z_D}(Delta_S) closed form vs census tr_conv_D")
    wb.add_upstream(CENSUS)
    # Both pins are read ON PURPOSE: the d_cells are at the proton pin, the
    # production value is derived_masses' muon pin, and delta_S_pin_effect /
    # production_q0_straddle measure the difference. Stamp the values this run
    # actually computed with, so the audit re-checks each leg.
    wb.save(q0_comparison(
        muon=q_muon, proton=q_prot,
        reason="records the production m_n (Q_beta at derived_masses._q_0, the "
               "muon pin) beside every convention-D cell at the proton pin "
               "(q_parameter.Q_MP), and measures the muon-vs-proton "
               "shift of both; both pins are read on purpose"))

    print(f"production m_n  {mp.nstr(m_n_prod, 15)}  err {mp.nstr(_ppb(m_n_prod), 6)} ppb  (retired mixed base)")
    for r in rows:
        print(f"  {r['element']:28s} {r['E0_form']:10s} Q_b {r['Q_beta_MeV'][:12]}  "
              f"err {r['m_n_err_ppb']} ppb  shift {r['shift_from_production_ppb']} ppb")
    print(f"Delta_S pin effect (muon vs proton, tower E0): {mp.nstr(pin_shift_rel, 6)}")
    print(f"production formula at proton pin: Q_b {mp.nstr(qprod_pr, 15)} (muon {mp.nstr(qprod_mu, 15)}); "
          f"m_n shift {mp.nstr(straddle_ppb, 6)} ppb; check vs derived_masses {mp.nstr(abs(qprod_mu - q_beta_prod), 3)}")
    print(f"Delta_S closed form vs census: {mp.nstr(ds_check, 3)}")
    return 0 if ds_check < mp.mpf("1e-20") else 1


if __name__ == "__main__":
    raise SystemExit(main())
