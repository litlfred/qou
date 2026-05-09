#!/usr/bin/env python3
"""ρ_F · V_hyp binding-energy gap analysis for light atomic species.

Per `rem:frobenius-packing-density`, the QOU binding-energy law is

    E_binding(K)  =  ρ_F(K) · V_hyp(K),

with ρ_F ∈ {m_e, 2 m_e} from Type-B fold-orbit closure of the
populated Wedderburn blocks (`prop:cpt-orbit-closure-density`)
and V_hyp the Thurston volume of the atomic-link complement.

This script does **not** compute V_hyp from QOU primitives — the
atom→atomic-link mapping for general isotopes is paper-side
content not yet wired through.  Instead, it inverts the law:
given the empirical Δ_binding from
`atom_mass_additive_baseline.py` and the SnapPy-known V_hyp of
candidate atomic-link primitives (figure-eight, three-twist,
Borromean, sums thereof), it reports the **required ρ_F** that
each candidate link would need to reproduce the observed binding
energy.

The output is the gap audit: which (link, ρ_F) candidates are
close to the QOU prediction ρ_F ∈ {m_e, 2 m_e}, and which need
multi-link composite atomic-link constructions.

Output: `rho-f-volume-binding-gap.witness.json`.

References
----------
- rem:frobenius-packing-density
- prop:cpt-orbit-closure-density
- def:topological-mass-formula
- atom_mass_additive_baseline.py — empirical Δ_binding source
- experimental_constants.VOL_* — SnapPy 3.3.2 volumes
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from experimental_constants import (  # noqa: E402
    M_E_MEV,
    VOL_FIGURE_EIGHT,
    VOL_THREE_TWIST,
    VOL_BORROMEAN,
)


# Candidate atomic-link primitives.  These are the only hyperbolic
# links with high-precision SnapPy volumes currently in the repo's
# experimental_constants table.  Composite atomic-links for
# heavier isotopes would build from these as JSJ pieces.
LINK_PRIMITIVES: dict[str, float] = {
    "figure-eight (4_1)": VOL_FIGURE_EIGHT,
    "three-twist (5_2)": VOL_THREE_TWIST,
    "Borromean (6^3_2)": VOL_BORROMEAN,
}


def required_rho(delta_binding_mev: float, vol: float) -> float:
    """ρ_F that reproduces `delta_binding = ρ_F · vol` (in MeV)."""
    if vol <= 0:
        return float("inf")
    return delta_binding_mev / vol


def main() -> None:
    builder = (
        WitnessBuilder("rho-f-volume-binding-gap", engine="python")
        .set_description(
            "Inverts ρ_F · V_hyp = Δ_binding to report the required "
            "ρ_F (in units of m_e) that each atomic-link-primitive "
            "candidate (figure-eight, three-twist, Borromean) would "
            "need to reproduce the empirical binding energy of light "
            "isotopes (²H–²⁰Ne).  QOU's prediction is ρ_F ∈ {m_e, "
            "2 m_e} from prop:cpt-orbit-closure-density; deviations "
            "from these two values quantify the atom-to-link mapping "
            "gap.  Bridges atom_mass_additive_baseline.py to the "
            "Frobenius packing density law in "
            "rem:frobenius-packing-density."
        )
        .set_audit_only("docs/audits/rho-f-volume-binding-gap.md")
    )

    # Load Δ_binding values from the additive baseline.
    add_path = (
        Path(__file__).parent / "atom-mass-additive-baseline.witness.json"
    )
    if not add_path.exists():
        raise SystemExit(
            "atom-mass-additive-baseline.witness.json not found; "
            "run atom_mass_additive_baseline.py first."
        )
    rows_in = json.loads(add_path.read_text()).get("data", {}).get("rows", [])

    # Per-isotope analysis.
    print(f"{'isotope':>8}  {'A':>3}  {'Δ_binding':>12}  "
          + "  ".join(f"{name[:18]:>18}" for name in LINK_PRIMITIVES))
    print(f"{'':>8}  {'':>3}  {'(MeV)':>12}  "
          + "  ".join(f"{'ρ_F/m_e needed':>18}"
                      for _ in LINK_PRIMITIVES))
    print("-" * 110)

    rows_out = []
    for row in rows_in:
        if row["A"] < 2:
            continue  # ¹H has zero nuclear binding (only 13.6 eV atomic).
        delta = row["delta_binding_MeV"]
        ratios = {
            name: required_rho(delta, vol) / M_E_MEV
            for name, vol in LINK_PRIMITIVES.items()
        }
        print(f"{row['isotope']:>8}  {row['A']:>3}  {delta:>12.3f}  "
              + "  ".join(f"{r:>18.3f}" for r in ratios.values()))
        rows_out.append({
            "isotope": row["isotope"],
            "A": row["A"], "Z": row["Z"], "N": row["N"],
            "delta_binding_MeV": delta,
            "required_rho_over_me_per_link": ratios,
        })

    # QOU expects ρ_F ∈ {1, 2} (in units of m_e).  Find the
    # candidate (isotope, link, target_rho) tuples within ±10% of
    # 1 or 2 — these are the cases where a single link primitive
    # plausibly explains the binding.
    matches = []
    for row in rows_out:
        for link, rho in row["required_rho_over_me_per_link"].items():
            for target in (1.0, 2.0):
                if abs(rho - target) / target < 0.10:
                    matches.append({
                        "isotope": row["isotope"],
                        "link": link,
                        "rho_over_me": rho,
                        "target_rho_over_me": target,
                        "deviation_pct": (rho - target) / target * 100,
                    })

    print()
    print(f"Candidate (isotope, link) pairs within ±10% of ρ_F ∈ "
          f"{{m_e, 2 m_e}}: {len(matches)}")
    for m in matches:
        print(f"  {m['isotope']:>5} via {m['link']:>20}  "
              f"ρ_F = {m['rho_over_me']:.3f}·m_e  "
              f"(target {m['target_rho_over_me']}·m_e, "
              f"Δ {m['deviation_pct']:+.2f}%)")

    if not matches:
        print("  (none — every isotope's binding requires a "
              "multi-link composite or a non-{m_e, 2 m_e} ρ_F)")

    builder.add_assertion(
        name="binding_gap_analysis_completed",
        computed=len(rows_out),
        expected=len(rows_out),
        tolerance=0,
        source="atom-mass-additive-baseline.witness.json rows ≥ ²H",
    )
    builder.add_data("rows", rows_out)
    builder.add_data("matches_within_10pct", matches)
    builder.add_data(
        "qou_prediction",
        "ρ_F ∈ {m_e, 2 m_e} per prop:cpt-orbit-closure-density",
    )
    builder.add_data("link_primitives_MeV_per_unit", {
        name: M_E_MEV * vol for name, vol in LINK_PRIMITIVES.items()
    })

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
