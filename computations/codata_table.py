"""Reader for the authoritative NIST CODATA table (`uploads/allascii.txt`).

**This module is the single source of truth for CODATA values.** Before it
existed, every CODATA constant in the corpus was a hand-transcribed literal,
which is how 138 sites came to carry the CODATA-**2018** muon-electron mass
ratio `206.7682830` under a "CODATA 2022" label while `codata_2022_source.py`
carried the correct 2022 value `206.7682827` — the same number, two editions,
no mechanism that could notice.

`uploads/allascii.txt` is NIST's *Fundamental Physical Constants — Complete
Listing*, 2022 CODATA adjustment, committed verbatim (366 lines,
`http://physics.nist.gov/constants`). Reading it is cheap and exact, so a
literal is never necessary.

Usage
-----

    from codata_table import codata

    r = codata("muon-electron mass ratio")
    r.value       # mpmath.mpf('206.7682827')
    r.uncertainty # mpmath.mpf('0.0000046')
    r.unit        # ''
    r.rel         # 2.2e-8

Values are returned as `mpmath.mpf` built from the table's digit string, so
they carry full table precision and never round-trip through float64 (see the
NO-FLOAT64 family in `scripts/precision-gates.sh`).

Table format (fixed-width, whitespace-grouped digits):

    muon-electron mass ratio            206.768 2827      0.000 0046
    alpha particle mass                 6.644 657 3450 e-27  0.000 000 0021 e-27  kg

An uncertainty of `(exact)` is returned as `None`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import mpmath as mp

# The table lives in uploads/ because it is an unmodified upstream artifact,
# committed as downloaded rather than transcribed into a source file.
_TABLE_PATH = Path(__file__).resolve().parent.parent / "uploads" / "allascii.txt"

_HEADER_RULE = "-" * 40  # the row of dashes that opens the data section

# Column starts are fixed-width in the NIST listing; taken from the header row
# rather than guessed, and asserted at parse time.
_COL_VALUE = 60
_COL_UNCERT = 85
_COL_UNIT = 110


@dataclass(frozen=True)
class CodataEntry:
    """One row of the NIST table."""

    quantity: str
    value: mp.mpf
    uncertainty: mp.mpf | None  # None for values the table marks "(exact)"
    unit: str
    value_str: str  # digits exactly as printed, whitespace removed
    uncertainty_str: str

    @property
    def is_exact(self) -> bool:
        return self.uncertainty is None

    @property
    def rel(self) -> float:
        """Relative standard uncertainty (0.0 when exact)."""
        if self.uncertainty is None or self.value == 0:
            return 0.0
        return float(abs(self.uncertainty / self.value))

    @property
    def rel_ppb(self) -> float:
        return self.rel * 1e9


def _clean_number(field: str) -> str:
    """`'206.768 2827'` -> `'206.7682827'`; `'6.644 657 e-27'` -> `'6.644657e-27'`.

    NIST groups digits in threes with spaces and separates the exponent with a
    space. Both are presentation only.
    """
    return re.sub(r"\s+", "", field.strip())


def _parse_table(path: Path = _TABLE_PATH) -> dict[str, CodataEntry]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")

    # Locate the dashed rule that opens the data section.
    start = None
    for i, line in enumerate(lines):
        if line.startswith(_HEADER_RULE):
            start = i + 1
            break
    if start is None:
        raise ValueError(f"{path}: no header rule found; is this the NIST listing?")

    entries: dict[str, CodataEntry] = {}
    for line in lines[start:]:
        if not line.strip():
            continue
        quantity = line[:_COL_VALUE].strip()
        value_field = line[_COL_VALUE:_COL_UNCERT]
        uncert_field = line[_COL_UNCERT:_COL_UNIT]
        unit = line[_COL_UNIT:].strip()
        if not quantity or not value_field.strip():
            continue

        value_str = _clean_number(value_field)
        uncert_str = _clean_number(uncert_field)

        # "(exact)" marks a defined constant (c, h, e, k, N_A, ...).
        if uncert_str.startswith("(exact"):
            uncertainty = None
        else:
            try:
                uncertainty = mp.mpf(uncert_str)
            except (ValueError, TypeError):
                uncertainty = None

        try:
            value = mp.mpf(value_str)
        except (ValueError, TypeError):
            # A handful of rows carry non-numeric values; skip rather than guess.
            continue

        entries[quantity.lower()] = CodataEntry(
            quantity=quantity,
            value=value,
            uncertainty=uncertainty,
            unit=unit,
            value_str=value_str,
            uncertainty_str=uncert_str,
        )

    return entries


_CACHE: dict[str, CodataEntry] | None = None


def table() -> dict[str, CodataEntry]:
    """The whole parsed table, keyed by lowercased quantity name."""
    global _CACHE
    if _CACHE is None:
        _CACHE = _parse_table()
    return _CACHE


def codata(quantity: str) -> CodataEntry:
    """Look up one quantity by its exact NIST name (case-insensitive).

    Raises `KeyError` with near-miss suggestions rather than returning a
    default — a silently-wrong constant is the failure mode this module exists
    to remove.
    """
    entries = table()
    key = quantity.strip().lower()
    if key in entries:
        return entries[key]

    words = [w for w in re.split(r"[\s\-]+", key) if len(w) > 2]
    near = [q for q in entries if all(w in q for w in words)][:8]
    hint = f"  Did you mean: {near}" if near else ""
    raise KeyError(f"{quantity!r} not in the CODATA table.{hint}")


def value_str(quantity: str) -> str:
    """The value's digit string exactly as NIST prints it (whitespace removed)."""
    return codata(quantity).value_str


if __name__ == "__main__":  # pragma: no cover - smoke check
    entries = table()
    print(f"parsed {len(entries)} CODATA-2022 entries from {_TABLE_PATH}")
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
