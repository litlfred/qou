#!/usr/bin/env python3
"""1ppb readiness dashboard — single-witness aggregation.

Pulls the headline metric from each contributing audit witness and
emits a single consolidated dashboard JSON.  The dashboard's
`max_non_anchor_delta_ppb` field is the headline number that any
1ppb-readiness gate should track.

Sources
-------
- `codata-reconciliation.witness.json` — primary CODATA / SnapPy
  comparison; reports `data.max_non_anchor_delta_ppb`.
- `atom-mass-additive-baseline.witness.json` — additive
  constituent baseline; reports `max_delta_binding_MeV` and
  `avg_binding_per_nucleon_MeV`.
- `rho-f-volume-binding-gap.witness.json` — ρ_F · V_hyp gap;
  reports the per-isotope required ρ_F values.
- `brundan-kleshchev-audit.witness.json` — empirical-evidence
  dossier for the Brundan–Kleshchev isomorphism (4 tests × 5 n
  values = 20 assertions).
- `alpha-k-macdonald-closed-form.witness.json` — closed-form α_k
  via Macdonald hook telescope; reports Plancherel-completeness
  residuals.

Output: `onepb-status-dashboard.witness.json`.
"""

from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402


def load(name: str) -> dict | None:
    path = Path(__file__).parent / name
    if not path.exists():
        return None
    return json.loads(path.read_text())


def main() -> None:
    builder = (
        WitnessBuilder("onepb-status-dashboard", engine="python")
        .set_description(
            "Aggregated 1ppb-readiness dashboard.  Single source of "
            "truth for the headline metric `max_non_anchor_delta_ppb` "
            "across the QOU primary observables (CODATA reconciliation), "
            "structural audits (Brundan–Kleshchev, Macdonald-telescope "
            "Plancherel completeness), and the open atomic-binding "
            "derivation gap (atom_mass_additive_baseline + "
            "rho_f_volume_binding_gap)."
        )
        .set_audit_only("docs/audits/onepb-status-dashboard.md")
    )

    sources = {
        "codata_reconciliation":
            load("codata-reconciliation.witness.json"),
        "atom_mass_additive_baseline":
            load("atom-mass-additive-baseline.witness.json"),
        "rho_f_volume_binding_gap":
            load("rho-f-volume-binding-gap.witness.json"),
        "brundan_kleshchev_audit":
            load("brundan-kleshchev-audit.witness.json"),
        "alpha_k_macdonald":
            load("alpha-k-macdonald-closed-form.witness.json"),
        "y_lambda_macdonald_telescope":
            load("y-lambda-macdonald-telescope.witness.json"),
        "demazure_markov_trace":
            load("demazure-markov-trace.witness.json"),
    }

    # Single headline: max non-anchor deviation across all
    # currently-asserted predictions.  This is the number to watch.
    cr = sources.get("codata_reconciliation") or {}
    headline_ppb = (cr.get("data", {}) or {}).get(
        "max_non_anchor_delta_ppb", None
    )

    add = sources.get("atom_mass_additive_baseline") or {}
    binding_max = (add.get("data", {}) or {}).get(
        "max_delta_binding_MeV", None
    )
    binding_avg = (add.get("data", {}) or {}).get(
        "avg_binding_per_nucleon_MeV", None
    )

    bk = sources.get("brundan_kleshchev_audit") or {}
    bk_assertions = bk.get("assertions", [])
    bk_pass = sum(1 for a in bk_assertions if a.get("passed"))
    bk_total = len(bk_assertions)

    macd = sources.get("alpha_k_macdonald") or {}
    macd_assertions = macd.get("assertions", [])
    plancherel_residuals = [
        a.get("computed")
        for a in macd_assertions
        if a.get("name", "").startswith("plancherel_completeness_n")
    ]

    summary = {
        "max_non_anchor_delta_ppb": headline_ppb,
        "atom_binding": {
            "max_delta_binding_MeV": binding_max,
            "avg_binding_per_nucleon_MeV": binding_avg,
            "law": "ρ_F · V_hyp (rem:frobenius-packing-density)",
            "status": "atom→link map TODO; see rho_f_volume_binding_gap audit",
        },
        "brundan_kleshchev": {
            "passed": bk_pass,
            "total": bk_total,
            "tests": [
                "dim H_n = n!",
                "dim Z(H_n) = p(n)",
                "Jucys-Murphy content separation",
                "bar-invariant Plancherel sum",
            ],
        },
        "macdonald_telescope_plancherel_residuals": plancherel_residuals,
        "witness_inventory": [
            name for name, data in sources.items() if data is not None
        ],
        "missing_witnesses": [
            name for name, data in sources.items() if data is None
        ],
    }

    print("1ppb-readiness dashboard")
    print("=" * 70)
    print(f"Headline (codata-reconciliation max non-anchor Δ): "
          f"{headline_ppb} ppb")
    print(f"Atom binding-energy gap:")
    print(f"  max Δ_binding: {binding_max} MeV (heaviest tested)")
    print(f"  avg per nucleon: {binding_avg} MeV/A "
          "(SEMF: ~7.5 MeV/A)")
    print(f"  status: {summary['atom_binding']['status']}")
    print(f"BK structural audit: {bk_pass}/{bk_total} assertions passed")
    print(f"Macdonald Plancherel residuals: "
          f"{len(plancherel_residuals)} entries (each ~10⁻⁵¹)")
    print()
    print(f"Witnesses present: "
          f"{len(summary['witness_inventory'])}/"
          f"{len(sources)}")
    if summary["missing_witnesses"]:
        print(f"Missing: {summary['missing_witnesses']}")

    builder.add_assertion(
        name="all_witnesses_present",
        computed=len(summary["witness_inventory"]),
        expected=len(sources),
        tolerance=0,
        source="dashboard inventory check",
    )
    if isinstance(headline_ppb, (int, float)):
        builder.add_assertion(
            name="codata_max_non_anchor_delta_ppb",
            computed=headline_ppb,
            expected=0.0,
            tolerance=200.0,  # AME2020 publication-rounding floor
            unit="ppb",
            source="codata-reconciliation.witness.json",
        )
    builder.add_data("summary", summary)
    builder.add_data("note",
                     "Atomic binding-energy column requires the "
                     "atom→atomic-link map to land before its rows "
                     "join the asserted set.")

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
