#!/usr/bin/env python3
"""Bounded unit-anchor audit for the linear deuteron law B(²H) = 5·g_reeb [MeV].

The landed linear law (²H reeb-flow tier) produces the DIMENSIONLESS number
5·g_reeb ≈ 2.2336 and uses it as MeV directly — the unit anchor is implicit.
For the law to be a derivation, some canonical framework energy E_unit must
satisfy  B(²H) = 5·g_reeb · (E_unit / MeV)  with  E_unit ≈ 1 MeV.

This probe checks a FIXED, PREREGISTERED list of canonical framework
energies (no free combinations, no search beyond the list — Rule-14: a
wider scan would be shape-probing).  For each candidate we report
E_unit/MeV and the resulting B error vs AME.  Expected and honest outcome:
a NEGATIVE (no candidate ≈ 1.000 MeV), leaving the linear law's unit
anchor open.  Scope-(a): this constrains the listed candidates only.

Candidate list (canonical energies already in the corpus):
  m_e, 2·m_e, m_e·[2]_v, m_e·[2]_q, m_e·q, m_e·(q+1), m_e/ℏ_q²·(q−1)²,
  E₀ = m_e/(q(q−1)), E₀/[2]_v², Q_β (CODATA neutron Q-value).

-- Ref: categorical_q_decay_ba_low_isotopes.py (the landed 5g law);
reeb_g_structural_identity_probe.py (g structure);
docs/audits/2026-07-06-reeb-flow-pn-magnitude-provenance-and-1four-extension.md §3c.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
if str(_COMP) not in sys.path:
    sys.path.insert(0, str(_COMP))
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV, Q_NEUTRON_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

set_compute_dps()
COMP = str(_COMP)

AME_B_2H = AME_B_DEUTERON_MEV_VALIDATION
# neutron Q-value (CODATA-derived shared constant), the CAL-2 proxy
Q_BETA_MEV = mp.mpf(str(Q_NEUTRON_MEV))


def main() -> int:
    t0 = time.monotonic()
    q, _, _ = load_q_50dps()
    v = mp.sqrt(q)
    two_v = v + 1 / v
    two_q = q + 1 / q
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    hbar_q = 1 - 1 / q                       # ℏ_q = 1 − q⁻¹

    g = 1 / mp.sqrt(1 + two_v ** 2)          # landed magnitude (structural form)
    five_g = 5 * g
    # the unit the law would need to be exact on AME:
    e_needed = AME_B_2H / five_g

    candidates = {
        "m_e": m_e,
        "2*m_e": 2 * m_e,
        "m_e*[2]_v": m_e * two_v,
        "m_e*[2]_q": m_e * two_q,
        "m_e*q": m_e * q,
        "m_e*(q+1)": m_e * (q + 1),
        "m_e*(q-1)^2/hbar_q^2": m_e * (q - 1) ** 2 / hbar_q ** 2,
        "E0=m_e/(q(q-1))": E0,
        "E0/[2]_v^2": E0 / two_v ** 2,
        "Q_beta": Q_BETA_MEV,
    }

    rows = []
    best = None
    for name, val in candidates.items():
        dev_pct = 100 * (val - 1) / 1                       # vs the implicit 1 MeV
        b_pred = five_g * val
        err_pct = 100 * (b_pred - AME_B_2H) / AME_B_2H
        rows.append({"candidate": name, "E_unit_MeV": mp.nstr(val, 8),
                     "dev_from_1MeV_pct": mp.nstr(dev_pct, 5),
                     "B_pred_MeV": mp.nstr(b_pred, 8),
                     "err_vs_AME_pct": mp.nstr(err_pct, 5)})
        if best is None or abs(val - 1) < abs(best[1] - 1):
            best = (name, val)

    verdict = (
        f"NEGATIVE (scope-(a), preregistered list): no listed canonical energy "
        f"is ≈ 1 MeV — nearest is {best[0]} = {mp.nstr(best[1], 6)} MeV. The "
        f"linear law would need E_unit = {mp.nstr(e_needed, 8)} MeV for AME "
        f"exactness; no listed candidate matches it within 1 %. The 5·g law's "
        f"unit anchor remains open; the law stays classified ASSERTED."
    )

    payload = {
        "computation": "reeb-5g-unit-anchor-scan",
        "description": ("Bounded (preregistered 10-candidate) unit-anchor audit for "
                        "the linear deuteron law B = 5·g_reeb [MeV]. Honest negative; "
                        "no fit, no open-ended search. audit-only."),
        "tier": "exploratory (bounded audit; negative result)",
        "result": {
            "constants": {"g_reeb": mp.nstr(g, 12), "5g": mp.nstr(five_g, 10),
                          "B_AME_2H": mp.nstr(AME_B_2H, 8),
                          "E_unit_needed_MeV": mp.nstr(e_needed, 10)},
            "candidates": rows,
            "verdict": verdict,
        },
    }
    import platform
    wb = WitnessBuilder.wrap_legacy(
        "reeb-5g-unit-anchor-scan", payload,
        script_path=__file__, engine="python+mpmath",
        engine_version=f"python {platform.python_version()} + mpmath {mp.__version__}",
        output_dir=os.path.join(COMP, "probes"), start_time=t0,
    )
    wb.add_assertion("no_candidate_within_1pct_of_needed_unit",
                     computed=str(all(mp.fabs(1 - val / e_needed) > mp.mpf("0.01")
                                      for val in candidates.values())),
                     expected="True")
    wb.save(extra={"auditOnly": True})

    print("=== 5g unit-anchor bounded scan ===")
    print(f"  5g = {float(five_g):.6f}; needed E_unit = {float(e_needed):.6f} MeV")
    for r in rows:
        print(f"  {r['candidate']:>24}: {r['E_unit_MeV']:>10} MeV  "
              f"(err vs AME {r['err_vs_AME_pct']:>8} %)")
    print("  " + verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
