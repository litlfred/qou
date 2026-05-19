#!/usr/bin/env python3
"""Parse AME 2020 mass.mas20 fixed-format file into a structured JSON
witness suitable for downstream consumption by the canonical
mass / β / Q / binding pipeline.

Source file: ``folio-assistant/computations/data/ame2020.mas20.txt``
  — uploaded via PR; copy of W.J.Huang, M.Wang, F.G.Kondev, G.Audi,
    S.Naimi, *The Ame2020 atomic mass evaluation (I)*, Chinese
    Physics C45, 030002 (March 2021); plus part II at 030003.

Fortran column spec (taken verbatim from the file header):

    a1, i3, i5, i5, i5, 1x, a3, a4, 1x, f14.6, f12.6, f13.5, 1x,
    f10.5, 1x, a2, f13.5, f11.5, 1x, i3, 1x, f13.6, f12.6
    cc  NZ   N    Z    A      el   o      mass      unc  binding unc
                                                            B  beta    unc
                                                              atomic_mass unc

Special markers:
  - ``#`` in place of decimal point → estimated (non-experimental)
  - ``*`` in place of value → not calculable

Output: ``folio-assistant/computations/data/ame2020.json``

CLI:
    python3 vendor_ame2020.py             # parse + emit
    python3 vendor_ame2020.py --check     # parse + print count, no write

Per repo-owner directive 2026-05-19: vendor AME 2020 into ``data/``.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "data" / "ame2020.mas20.txt"
DST = HERE / "data" / "ame2020.json"


def _parse_value(field: str) -> tuple[float | None, bool]:
    """Parse an AME numeric field; returns (value, estimated).

    Handles:
      - "      *  "       -> (None, False)   not calculable
      - "  100#    "      -> (100.0, True)   estimated (no decimal)
      - "8071.31806"      -> (8071.31806, False)  experimental
    """
    s = field.strip()
    if not s or s == "*":
        return None, False
    estimated = "#" in s
    s = s.replace("#", "")
    try:
        return float(s), estimated
    except ValueError:
        return None, estimated


def parse_line(line: str) -> dict | None:
    """Parse one data line of the AME mass table per the Fortran format.

    Returns None for header / comment lines.
    """
    if len(line) < 100:
        return None
    if not (line[0] in (" ", "0", "1")):
        return None
    # Use the Fortran field widths.
    # Spec: a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,1x,f10.5,1x,a2,
    #       f13.5,f11.5,1x,i3,1x,f13.6,f12.6
    try:
        cc = line[0:1]
        NZ = line[1:4].strip()
        N = line[4:9].strip()
        Z = line[9:14].strip()
        A = line[14:19].strip()
        el = line[20:23].strip()
        orig = line[23:27].strip()
        mass_excess_field = line[28:42]   # f14.6 keV (or "       *      ")
        mass_excess_unc_field = line[42:54]
        binding_field = line[54:67]       # f13.5 keV/A
        binding_unc_field = line[68:78]   # f10.5
        beta_type = line[79:81].strip()   # "B-" / "EC" / ...
        beta_energy_field = line[81:94]   # f13.5 keV
        beta_energy_unc_field = line[94:105]
        # Per Fortran spec: 1x, i3, 1x, f13.6, f12.6
        # idx 105 = 1x ; idx 106-108 = i3 (integer micro-u prefix);
        # idx 109 = 1x ; idx 110-122 = f13.6 (fractional micro-u);
        # idx 123-134 = f12.6 (atomic mass unc).
        atomic_mass_merged = line[106:123]
        atomic_mass_unc_field = line[123:135]
    except IndexError:
        return None

    # The N/Z/A fields are integers but might be blank for header.
    if not (N.lstrip("-").isdigit() and Z.lstrip("-").isdigit() and A.isdigit()):
        return None

    mass_excess, mass_excess_est = _parse_value(mass_excess_field)
    mass_excess_unc, _ = _parse_value(mass_excess_unc_field)
    binding_per_A, binding_est = _parse_value(binding_field)
    binding_per_A_unc, _ = _parse_value(binding_unc_field)
    beta_energy, beta_est = _parse_value(beta_energy_field)
    beta_energy_unc, _ = _parse_value(beta_energy_unc_field)

    # Atomic mass column: "int_micro_u fractional_micro_u" → full
    # value = int * 1e6 + fractional. Asterisks mark unmeasured.
    atomic_mass_micro_u = None
    atomic_mass_est = "#" in atomic_mass_merged
    cleaned = atomic_mass_merged.replace("#", "").strip()
    if cleaned and "*" not in cleaned:
        parts = cleaned.split()
        try:
            if len(parts) == 2:
                atomic_mass_micro_u = (
                    int(parts[0]) * 1_000_000 + float(parts[1])
                )
            elif len(parts) == 1:
                atomic_mass_micro_u = float(parts[0])
        except ValueError:
            atomic_mass_micro_u = None
    atomic_mass_unc, _ = _parse_value(atomic_mass_unc_field)

    return {
        "N": int(N),
        "Z": int(Z),
        "A": int(A),
        "element": el,
        "origin": orig if orig else None,
        "mass_excess_keV": mass_excess,
        "mass_excess_unc_keV": mass_excess_unc,
        "mass_excess_estimated": mass_excess_est,
        "binding_energy_per_A_keV": binding_per_A,
        "binding_energy_per_A_unc_keV": binding_per_A_unc,
        "binding_energy_per_A_estimated": binding_est,
        "binding_energy_total_keV": (
            binding_per_A * int(A) if binding_per_A is not None else None
        ),
        "beta_decay_type": beta_type if beta_type else None,
        "beta_decay_energy_keV": beta_energy,
        "beta_decay_energy_unc_keV": beta_energy_unc,
        "beta_decay_energy_estimated": beta_est,
        "atomic_mass_micro_u": atomic_mass_micro_u,
        "atomic_mass_unc_micro_u": atomic_mass_unc,
        "atomic_mass_estimated": atomic_mass_est,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="Parse and report counts; do not write JSON.")
    args = parser.parse_args(argv)

    if not SRC.exists():
        print(f"  ERROR: source not found at {SRC}")
        print(f"  Place the AME 2020 mass.mas20 file there first.")
        return 2

    entries: list[dict] = []
    skipped_header = 0
    with SRC.open("r", encoding="utf-8") as fh:
        for line in fh:
            r = parse_line(line)
            if r is None:
                skipped_header += 1
            else:
                entries.append(r)

    # Sort by (Z, N) for stable diffs.
    entries.sort(key=lambda e: (e["Z"], e["N"]))

    n_total = len(entries)
    n_experimental = sum(
        1 for e in entries
        if not (e["mass_excess_estimated"] or e["binding_energy_per_A_estimated"])
    )
    n_estimated = n_total - n_experimental

    # Z coverage histogram.
    by_Z: dict[int, int] = {}
    for e in entries:
        by_Z[e["Z"]] = by_Z.get(e["Z"], 0) + 1

    print(f"  parsed {n_total} entries ({skipped_header} header lines skipped)")
    print(f"  experimental: {n_experimental}, estimated: {n_estimated}")
    print(f"  Z coverage: Z={min(by_Z)}..{max(by_Z)}, "
          f"{len(by_Z)} elements")

    if args.check:
        return 0

    out = {
        "_metadata": {
            "source": (
                "uploads/mass_1.mas20.txt (AME2020 mass.mas20 from "
                "W.J.Huang, M.Wang, F.G.Kondev, G.Audi, S.Naimi, "
                "Chinese Physics C45, 030002, March 2021)"
            ),
            "source_path_in_repo": "folio-assistant/computations/data/ame2020.mas20.txt",
            "fortran_format": (
                "a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,1x,"
                "f10.5,1x,a2,f13.5,f11.5,1x,i3,1x,f13.6,f12.6"
            ),
            "units": {
                "mass_excess_keV": "keV",
                "binding_energy_per_A_keV": "keV per nucleon",
                "binding_energy_total_keV": (
                    "keV (binding_energy_per_A_keV × A; derived)"
                ),
                "beta_decay_energy_keV": "keV",
                "atomic_mass_micro_u": "micro-u (1u = 931.49410242 MeV)",
            },
            "markers": {
                "#": "estimated (non-experimental)",
                "*": "not calculable / measured",
            },
            "vendored_at": "2026-05-19",
            "vendored_by": (
                "folio-assistant/computations/vendor_ame2020.py — "
                "repo-owner directive: provide AME 2020 mass data "
                "as the canonical reference for the recursive "
                "atom-knot atlas across all isotopes"
            ),
            "n_entries": n_total,
            "n_experimental": n_experimental,
            "n_estimated": n_estimated,
        },
        "entries": entries,
    }

    DST.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"  Wrote: {DST}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
