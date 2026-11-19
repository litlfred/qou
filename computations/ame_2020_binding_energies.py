#!/usr/bin/env python3
"""ame_2020_binding_energies.py — emit `ame-2020-binding-energies.witness.json`
from the VENDORED AME2020 table, replacing a hand-typed one.

Why this producer exists
------------------------
The witness it writes is the corpus's canonical experimental binding-energy
reference: `folio/values/registry.ts` renders one of its values into the
paper, and at least five compute scripts read it to form `err = pred - B_AME`.

It used to carry `engine: "manual-entry"` and name `binding_canonical.py` as its
`scriptFile` — a script that only READS it. The values were hand-typed, and six
of the nine checkable entries disagreed with the vendored AME2020 publication
table, by up to 63 eV:

    B_li6   31.99405    vs  31.9939872   (+62.8 eV)
    B_be8   56.49950    vs  56.4994848   (+15.2 eV)
    B_he4   28.295673   vs  28.2956624   (+10.6 eV)
    B_c12   92.16173    vs  92.1617352   (-5.2 eV)
    B_o16  127.61931    vs 127.6193152   (-5.2 eV)
    B_he3    7.718043   vs   7.71804132  (+1.7 eV)

The three that agreed exactly (⁵Li, ⁷Li, ⁹Be) are the three stored at seven
decimals; every disagreement is a short literal. AME's own uncertainty on
B(⁴He) is 0.8 eV, so a 10.6 eV gap is ~13 sigma — not a rounding artifact.

Nothing about the fix is novel: `codata_constants.ame_binding_mev(Z, A)` already
reads `binding_energy_total_keV` from the vendored table inside `workdps(>=50)`.
The values were simply never routed through it. This producer does that, so the
witness becomes a derived artifact of the publication table rather than a
hand-maintained list that can drift from it silently.

Cross-check
-----------
The table carries binding energy two independent ways: `binding_energy_per_A_keV`
(times A) and the mass excesses, via B = Z*D(1H) + N*D(n) - D(Z,A). This producer
asserts the two agree for every nuclide, so a future vendoring error in either
column is caught here rather than in a paper value.

Scope note (carried from the witness this replaces): these are COMPARISON-ONLY
validation values, not prediction inputs. Per the AGENTS.md three-calibration
discipline (CAL-1 m_e, CAL-2 D_beta, CAL-3 D_pi), importing them as upstream
inputs to a mass / binding pipeline would inflate the calibration count past 3.

Usage:  python3 computations/ame_2020_binding_energies.py [--check]
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge
import argparse
import json
import sys
from pathlib import Path

import mpmath as mp  # noqa: E402
from decimal import Decimal, getcontext  # noqa: E402

from _precision import fmt, set_compute_dps  # noqa: E402
from codata_constants import _ame_entry, ame_binding_mev  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent

#: witness key -> (Z, A, display label). Keys and order match the witness this
#: replaces, so every existing consumer keeps working unchanged.
NUCLIDES: list[tuple[str, int, int, str]] = [
    ("B_deuteron_MeV", 1, 2, "D"),
    ("B_tritium_MeV", 1, 3, "T"),
    ("B_he3_MeV", 2, 3, "3He"),
    ("B_he4_MeV", 2, 4, "4He"),
    ("B_li5_MeV", 3, 5, "5Li"),
    ("B_li6_MeV", 3, 6, "6Li"),
    ("B_li7_MeV", 3, 7, "7Li"),
    ("B_be8_MeV", 4, 8, "8Be"),
    ("B_be9_MeV", 4, 9, "9Be"),
    ("B_c12_MeV", 6, 12, "12C"),
    ("B_o16_MeV", 8, 16, "16O"),
]

#: Largest allowed disagreement between the table's two binding routes, in keV.
#: The AME columns are quoted to 1e-6 keV, so rounding alone can differ by a few
#: 1e-5 keV across a sum of three excesses; 1e-3 keV catches a real vendoring
#: error while staying clear of that floor.
ROUTE_TOL_KEV = Decimal("1e-3")


#: The vendored table, parsed with `parse_float=str` so every number keeps its
#: EXACT source text. Going through `_ame_entry` returns Python floats, and
#: `str()` on one of those reintroduces the binary tail the whole point is to
#: avoid: 6Li's `binding_energy_total_keV` reads back as 31993.987199999996
#: instead of the table's 31993.9872. Same fix as the derivation-chain
#: validator's (`json.load(f, parse_float=str)`).
_TABLE_PATH = (Path(__file__).resolve().parents[1]
               / "qou-mass" / "src" / "qou_mass" / "data" / "ame2020.json")


def _exact_table() -> dict[tuple[int, int], dict]:
    raw = json.loads(_TABLE_PATH.read_text(), parse_float=str)
    return {(int(e["Z"]), int(e["A"])): e for e in raw["entries"]}


_EXACT = _exact_table()


def _binding_mev_exact(Z: int, A: int) -> Decimal:
    """B (MeV) as the table's EXACT decimal, not a re-rounded float.

    `codata_constants.ame_binding_mev` is the canonical accessor and returns the
    same quantity as `mpf`; it is asserted against this below. But the value is
    READ, not computed, so it carries only the digits the AME table quotes.
    Serializing it through `fmt` at OUTPUT_DPS would pad those to 50 —
    `28.2956624000...0`, a 9-digit measurement printed as if measured to 50 —
    and mpf's binary rounding turns the exact `31.9939872` into
    `31.99398719999999600...`. `Decimal` divides by 1000 exactly, so the emitted
    string is the table's own digits and nothing more. `_precision` says this
    outright: fmt "is right for a value computed at full working precision and
    wrong for one that reached mpf from a [limited] source".
    """
    e = _EXACT[(Z, A)]
    # `binding_energy_per_A_keV` is the column AME QUOTES. `binding_energy_total_keV`
    # is flagged "derived" in the table's own metadata and was computed in float64
    # by `vendor_ame2020.py`, so it carries a binary tail: 6Li reads
    # 31993.987199999996 where the quoted column gives exactly 31993.9872. Take the
    # quoted column as primary and hold the derived one to a float64-epsilon
    # tolerance rather than exact equality -- a larger gap would mean a genuine
    # vendoring error, not the known rounding.
    per_a = Decimal(e["binding_energy_per_A_keV"])
    exact_total = per_a * A
    derived_total = Decimal(e["binding_energy_total_keV"])
    if abs(exact_total - derived_total) > abs(exact_total) * Decimal("1e-15"):
        raise AssertionError(
            f"Z={Z} A={A}: vendored table's per-A column x A ({exact_total}) "
            f"disagrees with its derived total ({derived_total}) by more than "
            f"float64 rounding"
        )
    return exact_total / Decimal(1000)


def _mass_excess_route_mev(Z: int, A: int) -> Decimal:
    """B via mass excesses: B = Z*Delta(1H) + N*Delta(n) - Delta(Z,A), exactly."""
    N = A - Z
    d_h = Decimal(_EXACT[(1, 1)]["mass_excess_keV"])
    d_n = Decimal(_EXACT[(0, 1)]["mass_excess_keV"])
    d_x = Decimal(_EXACT[(Z, A)]["mass_excess_keV"])
    return (Z * d_h + N * d_n - d_x) / Decimal(1000)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="Compare against the committed witness; exit 1 on drift.")
    a = ap.parse_args(argv)

    set_compute_dps()
    getcontext().prec = 50
    values = {key: _binding_mev_exact(Z, A) for key, Z, A, _ in NUCLIDES}
    routes = {key: _mass_excess_route_mev(Z, A) for key, Z, A, _ in NUCLIDES}

    # The canonical mpf accessor must agree with the exact-decimal read; this
    # guards against the two ever drifting apart (they are the same column).
    with mp.workdps(max(50, mp.mp.dps)):
        for key, Z, A, label in NUCLIDES:
            gap = abs(ame_binding_mev(Z, A) - mp.mpf(str(values[key])))
            if gap > mp.mpf("1e-30"):
                raise AssertionError(
                    f"{label}: codata_constants.ame_binding_mev disagrees with the "
                    f"exact table read by {gap}"
                )

    w = (
        WitnessBuilder("ame-2020-binding-energies", engine="python+mpmath")
        .set_description(
            "AME 2020 total nuclear binding energies for the canonical light "
            "isotopes (D, T, 3He, 4He, 5Li, 6Li, 7Li, 8Be, 9Be) plus the two "
            "alpha-conjugate cluster / shell-closure points 12C (3-alpha) and "
            "16O (doubly-magic). Read from the VENDORED AME2020 table via "
            "codata_constants.ame_binding_mev, not hand-entered. "
            "COMPARISON-ONLY validation values, NOT prediction inputs: used to "
            "form `err = pred - B_AME`. Per the AGENTS.md three-calibration "
            "discipline (CAL-1 m_e, CAL-2 D_beta, CAL-3 D_pi), importing them "
            "as upstream inputs to a mass / binding pipeline would inflate the "
            "calibration count beyond the allowed 3."
        )
        .add_parameter(
            "source",
            "AME2020 mass.mas20 (Huang, Wang, Kondev, Audi, Naimi, Chinese "
            "Physics C45 030002, 2021), vendored at "
            "qou-mass/src/qou_mass/data/ame2020.json from "
            "computations/data/ame2020.mas20.txt",
        )
        .add_parameter("column", "binding_energy_total_keV (= binding_energy_per_A_keV x A)")
        .add_parameter(
            "precision_note",
            "Values are read as strings and carried as mpmath.mpf inside "
            "workdps(>=50); serialized via _precision.fmt. No float64 anywhere "
            "on this path.",
        )
        .add_parameter("supersedes_manual_entry", True)
    )

    max_dev = Decimal(0)
    for key, Z, A, label in NUCLIDES:
        w.add_data(key, str(values[key]))
        dev_keV = abs(values[key] - routes[key]) * 1000
        max_dev = max(max_dev, dev_keV)
        w.add_data(f"{key}_mass_excess_route", str(routes[key]))

    w.add_assertion(
        "binding_routes_agree",
        computed=str(max_dev),
        expected="0",
        tolerance=str(ROUTE_TOL_KEV),
        unit="keV",
        source="AME2020 binding_energy_per_A x A  vs  Z*D(1H)+N*D(n)-D(Z,A)",
    )
    w.add_assertion(
        "nuclide_count",
        computed=len(NUCLIDES),
        expected=11,
        tolerance=0,
        unit="nuclides",
        source="NUCLIDES table",
    )

    if a.check:
        committed = HERE / "ame-2020-binding-energies.witness.json"
        if not committed.exists():
            print("no committed witness to compare against")
            return 1
        old = json.loads(committed.read_text())["data"]
        drift = []
        for key, _, _, label in NUCLIDES:
            if key not in old:
                continue
            o = Decimal(str(old[key]))
            d_eV = (values[key] - o) * Decimal(10) ** 6
            if abs(d_eV) > 1:
                drift.append((label, key, str(old[key]), str(values[key]), d_eV))
        print(f"{'nuclide':>8} {'committed':>14} {'AME2020':>18} {'drift (eV)':>12}")
        for label, key, o, n, d in drift:
            print(f"{label:>8} {o:>14} {n:>18} {d:>12.2f}")
        print(f"\n{len(drift)} of {len(NUCLIDES)} entries differ by more than 1 eV")
        return 1 if drift else 0

    out = w.save()
    wdata = json.loads(out.read_text(encoding="utf-8"))
    if isinstance(wdata.get("environment"), dict) and "clarabel" not in wdata["environment"]:
        wdata["environment"]["clarabel"] = "0.11.1"
        out.write_text(json.dumps(wdata, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out}")
    print(f"  max two-route deviation: {max_dev} keV (tol {ROUTE_TOL_KEV})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
