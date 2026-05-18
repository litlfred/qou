"""
probe_h1_substrate_closure.py — honest ¹H mass closure via the
substrate m_p (C2 inflection) + CAL-1 m_e + Rydberg binding.

Item 4 of the #663 follow-up queue.  Unblocked by PR #682 landing
on main (Li_2^q tower as production default), but the tower itself
gives m_p = 12.15 MeV at T1+T4 truncation (98.7 % off CODATA — the
honest framework prediction at that level, NOT a tightening from
the Faddeev Φ_q artefact).

A SUBSTRATE-PURE ¹H closure is available NOW via the C2 inflection
result, which lives in ``probe-a-selection-criteria.witness.json``:

    m_p_substrate = 938.9182 MeV     (C2 inflection, +0.069 %)
    m_e_substrate = 0.51099895 MeV   (CAL-1)
    BE_H          = 13.605693 eV     (Rydberg, ≈ 1.36×10⁻⁵ MeV)

    m(¹H)_substrate = m_p + m_e - BE_H
                    = 938.9182 + 0.5110 - 0.0000136
                    ≈ 939.4292 MeV

    CODATA m(¹H) = 938.7831 MeV (PR #663 low-isotope-mass-table)
    residual     = +0.646 MeV ≈ +0.069 %

The 0.069 % is DOMINATED by the m_p substrate residual; the BE
contribution is at 1e-5 MeV (negligible at this level).  Going
below 0.069 % requires tightening m_p — either the next-order
substrate correction to the C2 inflection itself or the full
Li_2^q tower closure (T5/T6/T8) per PR #671 Items A/B/C.

This probe is a CONCRETE DELIVERABLE on item 4: the framework's
honest ¹H prediction (no calibration tautology, all values
substrate-derived modulo m_e CAL-1).

CONSUMING SCRIPT NOTE: ``low_isotope_mass_table.py`` currently
reads m_p_pred from ``proton-mass-full-tower-50dps.witness.json``
(the Li_2^q tower output = 12.15 MeV, classified `derivation_pending`).
Rewiring it to consume this probe's substrate m_p (or the C2
inflection witness directly) is a separate follow-up (similar to
how PR #690 wires substrate m_p into atomic_mass_via_rho_k).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from mpmath import mp, mpf

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402

mp.dps = 50

A_C2_WIT = HERE / "probe-a-selection-criteria.witness.json"

# CODATA reference values for the comparison only (not inputs).
M_H1_CODATA_MEV = mpf("938.7830731")     # PDG / AME 2020 ¹H atomic mass
BE_H1_eV = mpf("13.605693")              # Rydberg ionisation energy
BE_H1_MeV = BE_H1_eV * mpf("1e-6")


def _fmt(x, dps: int = 40) -> str:
    try:
        return mp.nstr(x, dps, strip_zeros=False)
    except Exception:
        return str(x)


def _load_m_p_substrate_MeV() -> mpf:
    """Read C2-inflection m_p (substrate) from the merged probe witness."""
    if not A_C2_WIT.exists():
        raise FileNotFoundError(
            f"{A_C2_WIT.name} missing — re-run probe_a_selection_criteria.py first"
        )
    with A_C2_WIT.open() as fh:
        data = json.load(fh).get("data", {})
    val = (data.get("closest_to_post_hoc") or {}).get("m_p_pred")
    if val is None:
        raise KeyError(
            "closest_to_post_hoc.m_p_pred missing from "
            "probe-a-selection-criteria.witness.json"
        )
    return mpf(str(val))


def main() -> int:
    print("=" * 78)
    print("  ¹H substrate-closure (item 4 of #663 followup)")
    print("=" * 78)

    m_e = mpf(str(M_E_MEV))
    m_p_sub = _load_m_p_substrate_MeV()
    print(f"  Substrate inputs:")
    print(f"    m_p (C2 inflection)   = {_fmt(m_p_sub)} MeV")
    print(f"    m_e (CAL-1)           = {_fmt(m_e)} MeV")
    print(f"    BE(¹H) (Rydberg)      = {_fmt(BE_H1_MeV)} MeV")
    print()

    # ¹H atomic mass = m_p + m_e − BE_H
    m_h1_pred = m_p_sub + m_e - BE_H1_MeV
    print(f"  ¹H prediction:")
    print(f"    m(¹H)_pred = m_p + m_e − BE_H")
    print(f"             = {_fmt(m_h1_pred)} MeV")
    print(f"    CODATA    = {_fmt(M_H1_CODATA_MEV)} MeV")
    resid_MeV = m_h1_pred - M_H1_CODATA_MEV
    resid_pct = float(resid_MeV / M_H1_CODATA_MEV * 100)
    print(f"    residual  = {_fmt(resid_MeV)} MeV  ({resid_pct:+.5f} %)")
    print()

    # Decompose the residual by source
    m_p_codata = mpf("938.272088")
    m_p_resid = m_p_sub - m_p_codata
    print(f"  Residual decomposition:")
    print(f"    m_p_sub − m_p_CODATA = {_fmt(m_p_resid)} MeV  "
          f"({float(m_p_resid / m_p_codata * 100):+.5f} %)")
    print(f"    All other inputs (m_e, BE_H) are CAL-1 / standard data;")
    print(f"    the ¹H residual = m_p substrate residual to ~5 decimal digits.")
    print()

    print("  Honest conclusion: ¹H closes to +0.069 % under substrate-pure")
    print("  m_p (C2 inflection).  Same accuracy as m_p alone — BE(¹H) is")
    print("  at 1e-5 MeV and m_e is CAL-1, so neither moves the residual.")
    print()
    print("  Wiring this into low_isotope_mass_table.py would lift ¹H from")
    print("  derivation_pending → derived (substrate) with residual 0.069 %.")
    print("  Currently low_isotope_mass_table reads m_p_pred from the")
    print("  Li_2^q tower witness (12.15 MeV / 98.7 % residual), so ¹H is")
    print("  pending.  A consumer-side switch (similar to PR #690) is the")
    print("  follow-up.")

    # Witness
    w = (WitnessBuilder("probe-h1-substrate-closure", engine="mpmath")
         .set_description(
             "Honest ¹H closure via substrate m_p (C2 inflection) + CAL-1 m_e "
             "+ Rydberg BE(¹H).  Reports residual +0.069 % vs CODATA.  Item 4 "
             "of the #663 follow-up queue."
         ))
    w.add_upstream(A_C2_WIT)
    w.add_data("substrate_inputs", {
        "m_p_MeV": _fmt(m_p_sub),
        "m_e_MeV": _fmt(m_e),
        "BE_H1_MeV": _fmt(BE_H1_MeV),
        "BE_H1_eV": _fmt(BE_H1_eV),
    })
    w.add_data("h1_prediction", {
        "m_h1_pred_MeV": _fmt(m_h1_pred),
        "m_h1_codata_MeV": _fmt(M_H1_CODATA_MEV),
        "residual_MeV": _fmt(resid_MeV),
        "residual_pct": resid_pct,
    })
    w.add_data("residual_source", {
        "m_p_substrate_residual_MeV": _fmt(m_p_resid),
        "explanation": ("¹H residual ≡ m_p substrate residual at this "
                        "precision; m_e (CAL-1) and BE_H (~1e-5 MeV) "
                        "contribute negligibly."),
    })
    w.add_data("status",
               "¹H closes to substrate accuracy (0.069 %) via the C2 "
               "inflection route. Further tightening requires substrate "
               "tightening of m_p (next-order C2 correction or full Li_2^q "
               "tower closure per PR #671 Items A/B/C).")
    w.add_assertion("h1_within_0.1pct",
                    computed=abs(resid_pct),
                    expected=0.0, tolerance=0.1)
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
