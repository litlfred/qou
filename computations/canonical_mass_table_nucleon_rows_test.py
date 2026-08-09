#!/usr/bin/env python3
"""The extended mass table's free-nucleon rows must come from the facade.

Regression for `qou-7loj`: `lookup_nucleon_mass_borromean` used to read
`m-p-borromean-verification-50dps.witness.json` and return its
`m_p_pred_MeV = 965.384` — the `m_e·Vol(𝓑₃)/ℏ_q²·λ_A` form deprecated for
absolute mass on 2026-06-24 — so the p / n rows were +2.89 % high while
labelled `prediction_method=CANONICAL_TRACE`.

Nothing caught it: the value crossed as **data** (a `json.loads` of a witness
path, no import, no call), so the AST re-entry audit had no edge to find and
the prose guards had no text to read. A ppb-level assertion here is the check
that surface actually admits.

Run: python3 computations/canonical_mass_table_nucleon_rows_test.py
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402 — substrate path bridge

from canonical_mass_table_extended import (  # noqa: E402
    lookup_nucleon_mass_canonical,
)
from codata_constants import (  # noqa: E402
    M_N_MEV_VALIDATION,
    M_P_MEV_VALIDATION,
)

#: Generous vs the +1.35 / +2.39 ppb the canonical route actually achieves, and
#: ~21000× tighter than the +2.89 % (28.9 M ppb) the deprecated route returned.
#: Sized to catch a re-wiring, not to police the last digit.
TOLERANCE_PPB = 1_000.0

#: The values the deprecated Vol·ρ route returned, asserted absent.
DEPRECATED_MEV = {(1, 0): 965.38447552523690767, (0, 1): 966.71477359056614042}


def main() -> int:
    failures = 0
    for (Z, N), ref in (((1, 0), float(M_P_MEV_VALIDATION)),
                        ((0, 1), float(M_N_MEV_VALIDATION))):
        pred, origin = lookup_nucleon_mass_canonical(Z, N)
        label = "proton" if (Z, N) == (1, 0) else "neutron"

        if pred is None:
            print(f"  FAIL  {label}: no prediction returned")
            failures += 1
            continue

        err_ppb = (pred - ref) / ref * 1e9
        ok = abs(err_ppb) <= TOLERANCE_PPB
        print(f"  {'PASS' if ok else 'FAIL'}  {label} is canonical: "
              f"{pred:.9f} MeV vs CODATA {ref:.9f} ({err_ppb:+.2f} ppb)")
        if not ok:
            failures += 1
            print(f"        exceeds {TOLERANCE_PPB:.0f} ppb — has this been "
                  f"re-wired to a Vol·ρ route? (origin: {origin})")

        # Explicitly assert the deprecated magnitude is gone, so a regression
        # names itself instead of showing up as a bare tolerance failure.
        deprecated = DEPRECATED_MEV[(Z, N)]
        regressed = abs(pred - deprecated) < 1e-6
        print(f"  {'PASS' if not regressed else 'FAIL'}  {label} is not the "
              f"deprecated Vol·ρ value ({deprecated:.5f} MeV)")
        if regressed:
            failures += 1

    # Composite rows are binding energies and must not acquire a mass.
    ok = lookup_nucleon_mass_canonical(1, 1) == (None, None)
    print(f"  {'PASS' if ok else 'FAIL'}  composite (D) row unaffected")
    if not ok:
        failures += 1

    print(f"\n{'OK' if not failures else str(failures) + ' FAILURE(S)'} — 5 checks")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
