"""Corpus-side access to the NIST CODATA table.

The reader itself lives in the package, at
``tools/qou-substrate/python/qou_substrate/codata.py``, because
``qou_substrate.constants`` needs it and Layer 2a cannot import from
``computations/``. This module is a thin re-export so corpus scripts get the
same parser rather than a second copy — a vendored duplicate is exactly how
`qou-mass/_internal/` drifted on all 14 modules (AGENTS.md, §project
structure).

Usage
-----

    from codata_table import codata

    codata("muon-electron mass ratio").value  # mpf('206.7682827')

See the package module's docstring for the full contract.
"""

from __future__ import annotations

import sys
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent / "tools" / "qou-substrate" / "python"
if str(_PKG) not in sys.path:
    sys.path.insert(0, str(_PKG))

from qou_substrate.codata import (  # noqa: E402,F401
    CodataEntry,
    codata,
    table,
    uncertainty_str,
    value_str,
)

__all__ = ["CodataEntry", "codata", "table", "uncertainty_str", "value_str"]


if __name__ == "__main__":  # pragma: no cover - smoke check
    entries = table()
    print(f"parsed {len(entries)} CODATA-2022 entries")
    for q in (
        "muon-electron mass ratio",
        "proton-electron mass ratio",
        "electron mass energy equivalent in MeV",
        "proton mass energy equivalent in MeV",
        "neutron mass energy equivalent in MeV",
    ):
        e = codata(q)
        unc = "exact" if e.is_exact else f"{e.uncertainty_str} ({e.rel_ppb:.3g} ppb)"
        print(f"  {e.quantity:<48s} {e.value_str:>20s}  ± {unc}")
