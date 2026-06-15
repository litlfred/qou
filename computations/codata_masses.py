#!/usr/bin/env python3
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.

CODATA proton/neutron/electron mass witness.

Re-exports the canonical CODATA-2022 / AME-2020 values from
`codata_constants` (M_E_MEV, M_P_MEV, M_N_MEV) into a witness JSON
so the values registry (`content/values/registry.ts`) and the
`:leanval` codemod can pin Lean and Markdown literals to a single
source of truth.

The Python side of the CODATA chain (every `m_e`/`m_p`/`m_n` use
inside a `.py` script) already imports from `codata_constants`;
this witness extends the same chain to `.lean` files and
`.md` content.

Source values are documented in `codata_constants.py`:

    M_E_MEV = 0.51099895        (CODATA 2022)
    M_P_MEV = 938.27208816      (CODATA 2022)
    M_N_MEV = 939.56542052      (CODATA 2022; M_P + M_E + Q_β by
                                 construction)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from witness_base import WitnessBuilder  # noqa: E402
from codata_constants import M_E_MEV, M_N_MEV, M_P_MEV  # noqa: E402


def main() -> int:
    # Convert mpf to plain string for storage; the registry lookup
    # consumes the string verbatim.
    m_e = str(M_E_MEV)
    m_p = str(M_P_MEV)
    m_n = str(M_N_MEV)

    # Sanity windows (fail-fast against accidental bit-rot of the
    # canonical constants).  Tightened to the 1-keV CODATA bands.
    e_in_window = float(M_E_MEV) > 0.510998 and float(M_E_MEV) < 0.511000
    p_in_window = float(M_P_MEV) > 938.27200 and float(M_P_MEV) < 938.27220
    n_in_window = float(M_N_MEV) > 939.56500 and float(M_N_MEV) < 939.56600

    w = WitnessBuilder("codata-masses", engine="codata-constants")
    w.set_description(
        "CODATA 2022 / AME 2020 proton, neutron, electron masses "
        "(MeV/c^2), re-exported from "
        "folio-assistant/computations/codata_constants.py so the "
        "values registry can pin Lean and Markdown literals via "
        ":leanval[m_e_MeV] / :leanval[m_p_MeV] / :leanval[m_n_MeV]."
    )
    w.set_content_block("prop:three-calibration-inputs")
    w.add_parameter("source", "CODATA 2022 (m_e, m_p); AME 2020 + Q_β (m_n)")

    w.add_assertion(
        name="m_e_in_codata_2022_window",
        computed=str(e_in_window),
        expected="True",
        source="codata_masses",
    )
    w.add_assertion(
        name="m_p_in_codata_2022_window",
        computed=str(p_in_window),
        expected="True",
        source="codata_masses",
    )
    w.add_assertion(
        name="m_n_in_codata_2022_window",
        computed=str(n_in_window),
        expected="True",
        source="codata_masses",
    )

    w.add_data("m_e_MeV", m_e)
    w.add_data("m_p_MeV", m_p)
    w.add_data("m_n_MeV", m_n)
    w.add_data(
        "source_module",
        "folio-assistant/computations/codata_constants.py",
    )
    w.save()

    ok = e_in_window and p_in_window and n_in_window
    print(
        f"codata_masses: {'PASS' if ok else 'FAIL'}  "
        f"m_e={m_e}  m_p={m_p}  m_n={m_n}"
    )
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
