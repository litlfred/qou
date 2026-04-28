"""Unit conversions for QOU organic-chemistry computations.

Conversions
-----------
This module provides explicit, traceable conversions between the
energy units that appear in the chapter:

    1 eV       = 96.48533212331… kJ/mol     (CODATA 2018)
    1 eV       = 23.060547830619… kcal/mol  (derived; 1 cal = 4.184 J)
    1 Hartree  = 27.211386245988… eV        (CODATA 2018)
    1 kcal/mol = 4.184 kJ/mol                (defined: 1 cal ≡ 4.184 J)

All constants are taken from CODATA 2018 (the latest fully published
recommended values; CODATA 2022 supersedes a small subset, none of
which affect the conversions used here to 8 significant figures).

References
----------
CODATA 2018: P. J. Mohr, D. B. Newell, B. N. Taylor, E. Tiesinga,
    "CODATA recommended values of the fundamental physical constants:
    2018", Rev. Mod. Phys. 93, 025010 (2021).
NIST: https://physics.nist.gov/cuu/Constants/

@module folio-assistant/computations/lib/units
"""

from __future__ import annotations

# ── Source constants (CODATA 2018) ───────────────────────────────

EV_TO_KJ_PER_MOL = 96.48533212331  # CODATA 2018 (eV·N_A in kJ/mol)
EV_TO_KJ_PER_MOL_REF = "CODATA 2018"

HARTREE_TO_EV = 27.211386245988    # CODATA 2018
HARTREE_TO_EV_REF = "CODATA 2018"

CAL_TO_J = 4.184                   # exact, by definition
CAL_TO_J_REF = "thermochemical-calorie definition"


# ── Derived conversion factors ───────────────────────────────────

EV_TO_KCAL_PER_MOL = EV_TO_KJ_PER_MOL / CAL_TO_J  # ≈ 23.060547…
KJ_PER_MOL_TO_KCAL_PER_MOL = 1.0 / CAL_TO_J       # ≈ 0.23900574…
HARTREE_TO_KJ_PER_MOL = HARTREE_TO_EV * EV_TO_KJ_PER_MOL  # ≈ 2625.499…


# ── Bidirectional conversion API ─────────────────────────────────

def ev_to_kj_per_mol(x: float) -> float:
    """Convert energy from eV to kJ/mol."""
    return x * EV_TO_KJ_PER_MOL


def kj_per_mol_to_ev(x: float) -> float:
    """Convert energy from kJ/mol to eV."""
    return x / EV_TO_KJ_PER_MOL


def ev_to_kcal_per_mol(x: float) -> float:
    """Convert energy from eV to kcal/mol."""
    return x * EV_TO_KCAL_PER_MOL


def kcal_per_mol_to_ev(x: float) -> float:
    """Convert energy from kcal/mol to eV."""
    return x / EV_TO_KCAL_PER_MOL


def kj_per_mol_to_kcal_per_mol(x: float) -> float:
    """Convert energy from kJ/mol to kcal/mol."""
    return x * KJ_PER_MOL_TO_KCAL_PER_MOL


def kcal_per_mol_to_kj_per_mol(x: float) -> float:
    """Convert energy from kcal/mol to kJ/mol."""
    return x * CAL_TO_J


def hartree_to_ev(x: float) -> float:
    """Convert energy from Hartree to eV."""
    return x * HARTREE_TO_EV


def ev_to_hartree(x: float) -> float:
    """Convert energy from eV to Hartree."""
    return x / HARTREE_TO_EV


def hartree_to_kj_per_mol(x: float) -> float:
    """Convert energy from Hartree to kJ/mol."""
    return x * HARTREE_TO_KJ_PER_MOL


def kj_per_mol_to_hartree(x: float) -> float:
    """Convert energy from kJ/mol to Hartree."""
    return x / HARTREE_TO_KJ_PER_MOL


# ── Provenance dictionary for witness output ─────────────────────

CONVERSION_REFERENCES: dict[str, str] = {
    "eV->kJ/mol":      f"{EV_TO_KJ_PER_MOL} ({EV_TO_KJ_PER_MOL_REF})",
    "Hartree->eV":     f"{HARTREE_TO_EV} ({HARTREE_TO_EV_REF})",
    "cal->J":          f"{CAL_TO_J} ({CAL_TO_J_REF})",
    "eV->kcal/mol":    f"{EV_TO_KCAL_PER_MOL:.10f} (derived)",
    "Hartree->kJ/mol": f"{HARTREE_TO_KJ_PER_MOL:.6f} (derived)",
}


__all__ = [
    "EV_TO_KJ_PER_MOL",
    "EV_TO_KCAL_PER_MOL",
    "HARTREE_TO_EV",
    "HARTREE_TO_KJ_PER_MOL",
    "KJ_PER_MOL_TO_KCAL_PER_MOL",
    "CAL_TO_J",
    "CONVERSION_REFERENCES",
    "ev_to_kj_per_mol",
    "kj_per_mol_to_ev",
    "ev_to_kcal_per_mol",
    "kcal_per_mol_to_ev",
    "kj_per_mol_to_kcal_per_mol",
    "kcal_per_mol_to_kj_per_mol",
    "hartree_to_ev",
    "ev_to_hartree",
    "hartree_to_kj_per_mol",
    "kj_per_mol_to_hartree",
]
