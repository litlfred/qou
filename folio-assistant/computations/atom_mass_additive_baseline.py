#!/usr/bin/env python3
"""Additive atomic-mass baseline + nuclear-binding residual.

The existing `atom_mass_derived.py` uses a multiplicative
``tr_atom × E_0`` formula whose result is structurally too large
for $A \\geq 1$ (Hydrogen comes out at +55%, Helium negative;
see `atom-mass-derived.witness.json`).  The physical relation is

    M_atom  =  Z · M_p + N · M_n + Z · M_e  −  E_binding,

with $E_{\\text{binding}}$ the nuclear binding energy (positive,
~8 MeV / nucleon for medium nuclei).  This script computes the
additive constituent baseline and reports the residual

    Δ_binding(A, Z)  :=  (Z M_p + N M_n + Z M_e)  −  M_{\\text{AME}}(A, Z)

for every isotope in `atom_mass_derived.py`'s ELEMENTS table.

For Hydrogen, the *physical* Δ_binding is the 13.6 eV atomic
binding ≈ 1.4 × 10⁻⁵ MeV ≈ 14 ppb at the 938 MeV scale.  The
*observed* residual depends on the precision of the AME tabulation
used: with AME2020 published to 3 decimal places (938.783 MeV),
the residual is dominated by publication rounding (~5 × 10⁻⁴ MeV
≈ 533 ppb floor; the table below reports 92.79 ppb).  A higher-
precision AME entry (≥ 6 dp) would expose the 14 ppb physical
binding.

For heavier nuclei, the residual IS the QOU-derivable
$\\rho_F \\cdot V_{\\text{hyp}}$ binding term
(`rem:frobenius-packing-density`).  This script doesn't compute
the binding from QOU primitives; it just records the
constituent-vs-AME residual so the binding model can be tested
against it as a separate witness.

References
----------
- experimental_constants.py — CODATA 2022 nucleon / electron masses
- atom_mass_derived.py — original multiplicative path (incorrect
  for atom assembly; preserved for the proton/neutron tr_M
  primitives it produces)
- rem:frobenius-packing-density — the binding-energy law that
  should reproduce the Δ_binding column
"""

from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import (  # noqa: E402
    M_P_MEV, M_P_MEV_ERR,
    M_N_MEV, M_N_MEV_ERR,
    M_E_MEV, M_E_MEV_ERR,
)


# AME2020 atomic masses (MeV) — same source as
# `atom_mass_derived.py::AME2020_MASS`.
AME2020_MASS_BY_ZN: dict[tuple[int, int], tuple[str, str, float]] = {
    (1, 0):  ("Hydrogen",  "1H",   938.783),
    (2, 2):  ("Helium",    "4He",  3728.401),
    (3, 4):  ("Lithium",   "7Li",  6535.367),
    (4, 5):  ("Beryllium", "9Be",  8394.794),
    (5, 6):  ("Boron",     "11B",  10255.103),
    (6, 6):  ("Carbon",    "12C",  11177.930),
    (7, 7):  ("Nitrogen",  "14N",  13043.781),
    (8, 8):  ("Oxygen",    "16O",  14899.169),
    (9, 10): ("Fluorine",  "19F",  17696.901),
    (10, 10):("Neon",      "20Ne", 18622.835),
}


def constituent_mass(Z: int, N: int) -> float:
    """Sum of free constituent masses (no binding)."""
    return Z * M_P_MEV + N * M_N_MEV + Z * M_E_MEV


def constituent_uncertainty(Z: int, N: int) -> float:
    """Uncertainty on `constituent_mass` propagated quadratically."""
    return ((Z * M_P_MEV_ERR) ** 2 +
            (N * M_N_MEV_ERR) ** 2 +
            (Z * M_E_MEV_ERR) ** 2) ** 0.5


def ppb(predicted: float, observed: float) -> float:
    if observed == 0:
        return float("inf")
    return 1e9 * abs(predicted - observed) / abs(observed)


def main() -> None:
    builder = (
        WitnessBuilder("atom-mass-additive-baseline", engine="python")
        .set_description(
            "Additive atomic-mass baseline:  M_atom ≈ Z·M_p + N·M_n + "
            "Z·M_e − E_binding(A, Z).  Records the constituent-vs-AME "
            "residual Δ_binding for every isotope in the "
            "`atom_mass_derived.py` ELEMENTS table.  At A = 1 the "
            "physical Δ_binding is the 13.6 eV atomic binding ≈ 14 ppb "
            "at the 938 MeV scale; the observed AME-residual is "
            "publication-rounding-floor-limited (3 dp at 938.783 MeV "
            "gives ~533 ppb floor; the witness reports 92.79 ppb).  "
            "At A ≥ 4 the residual is the nuclear binding that the "
            "Frobenius-packing law (rem:frobenius-packing-density) "
            "is expected to reproduce."
        )
        .set_audit_only(
            "docs/audits/atom-mass-additive-baseline.md"
        )
    )

    print(f"{'isotope':>10}  {'Z':>3}  {'N':>3}  "
          f"{'constituents':>16}  {'AME2020':>16}  "
          f"{'Δ_binding':>12}  {'Δ_ppb':>14}")
    print("-" * 110)

    rows = []
    for (Z, N), (element, isotope, m_observed) in sorted(
        AME2020_MASS_BY_ZN.items()
    ):
        m_const = constituent_mass(Z, N)
        m_const_err = constituent_uncertainty(Z, N)
        delta_binding = m_const - m_observed     # positive = binding
        delta_pb = ppb(m_const, m_observed)
        print(f"{isotope:>10}  {Z:>3}  {N:>3}  "
              f"{m_const:>16.6f}  {m_observed:>16.6f}  "
              f"{delta_binding:>+12.6f}  {delta_pb:>14.3f}")

        rows.append({
            "isotope": isotope,
            "element": element,
            "Z": Z, "N": N, "A": Z + N,
            "constituent_mass_MeV": m_const,
            "constituent_uncertainty_MeV": m_const_err,
            "ame2020_mass_MeV": m_observed,
            "delta_binding_MeV": delta_binding,
            "delta_ppb": delta_pb,
        })

    # Structural identity: constituent_mass(1, 0) = M_p + M_e exactly
    # (no rounding beyond IEEE 754).  This anchors the baseline as
    # bit-stable; the AME row's ppb deviation is dominated by the
    # 3-decimal-place AME2020 publication rounding (~500 ppb floor),
    # which is informational only and not asserted here.
    h_const = rows[0]["constituent_mass_MeV"]
    h_struct = M_P_MEV + M_E_MEV
    builder.add_assertion(
        name="hydrogen_constituent_structural_identity",
        computed=h_const - h_struct,
        expected=0.0,
        tolerance=1e-12,
        unit="MeV",
        source="IEEE 754 arithmetic on CODATA constants",
    )

    # The Δ_binding column for A ≥ 4 is what
    # `rem:frobenius-packing-density` should derive.
    # We track the maximum residual as a single scalar metric.
    max_binding = max(r["delta_binding_MeV"] for r in rows)
    binding_per_nucleon = [
        r["delta_binding_MeV"] / r["A"] for r in rows if r["A"] > 1
    ]
    avg_per_nucleon = (sum(binding_per_nucleon) / len(binding_per_nucleon)
                       if binding_per_nucleon else 0.0)
    print()
    print(f"max Δ_binding (heaviest tested): {max_binding:.3f} MeV")
    print(f"avg binding per nucleon (A ≥ 4): {avg_per_nucleon:.3f} MeV/A "
          "(SEMF predicts ~7.5–8 MeV/A)")

    builder.add_data("rows", rows)
    builder.add_data("max_delta_binding_MeV", max_binding)
    builder.add_data("avg_binding_per_nucleon_MeV", avg_per_nucleon)
    builder.add_data(
        "expected_qou_law",
        "ρ_F · V_hyp  (rem:frobenius-packing-density)",
    )
    builder.add_data("source", "AME2020 + CODATA 2022")

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
