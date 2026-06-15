#!/usr/bin/env python3
"""Molecular experimental reference values → witness.

Single source of truth for the experimental comparison literals that were
hard-coded inline in the molecular-construction `.md` blocks (organic-chem
WS-B B1: benzene bond lengths 1.40/1.54/1.34 Å, CO 11.09 eV, CO₂ 8.28 eV,
H₂ 4.478 eV, C–C 3.60 eV, benzene resonance 36 kcal/mol). Every value is
EXPERIMENTAL (NIST / standard refs) — NOT derived from q₀ — and is pulled
from `experimental_constants.py` so the `.md` blocks `:val`-pin against one
witness instead of repeating inline literals that can drift.
"""
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import _path_bridge  # noqa: F401  — substrate modules live in substrate/
from witness_base import WitnessBuilder
from experimental_constants import (
    D0_CO_EV, D0_CO2_DOUBLE_EV, D0_H2_EV, D0_CC_EV,
    BOND_LEN_BENZENE_ANG, BOND_LEN_CC_SINGLE_ANG, BOND_LEN_CC_DOUBLE_ANG,
    BENZENE_RESONANCE_KCAL,
)


def main() -> None:
    w = WitnessBuilder("molecular-experimental-refs", engine="python")
    w.set_description(
        "Experimental molecular comparison references (bond dissociation "
        "energies, benzene bond lengths, benzene resonance energy) — the "
        "single source of truth for the :val-pinned literals in the "
        "molecular-construction .md blocks. All values are experimental "
        "(NIST / standard), NOT derived from q₀. De-hardcodes the inline "
        "literals flagged in organic-chem-redo WS-B (B1)."
    )
    refs = {
        "d0_co_ev": D0_CO_EV,                       # CO triple bond (≈11.09)
        "d0_co2_double_ev": D0_CO2_DOUBLE_EV,       # CO₂ double-bond ref (≈8.28)
        "d0_h2_ev": D0_H2_EV,                       # H₂ bond (≈4.478)
        "d0_cc_ev": D0_CC_EV,                       # C–C single bond (≈3.60)
        "bond_len_benzene_ang": BOND_LEN_BENZENE_ANG,    # 1.40 Å
        "bond_len_cc_single_ang": BOND_LEN_CC_SINGLE_ANG,  # 1.54 Å
        "bond_len_cc_double_ang": BOND_LEN_CC_DOUBLE_ANG,  # 1.34 Å
        "benzene_resonance_kcal": BENZENE_RESONANCE_KCAL,  # 36 kcal/mol
    }
    for k, v in refs.items():
        w.add_data(k, float(v))
    w.add_data(
        "provenance",
        "All experimental (NIST Chemistry WebBook / standard organic-chemistry "
        "references); comparison targets only, not derivation inputs. Pulled "
        "from folio-assistant/computations/substrate/experimental_constants.py.",
    )
    w.save()
    for k, v in refs.items():
        print(f"  {k:>24} = {v}")
    print("Done. molecular-experimental-refs witness saved.")


if __name__ == "__main__":
    main()
