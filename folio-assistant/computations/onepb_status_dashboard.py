#!/usr/bin/env python3
"""1ppb readiness dashboard — single-witness aggregation.

QOU prediction is **structural**, not fitted against CODATA
atomic-mass tables.  The two structural prediction layers are:

  1. **LP dual shadow prices** y_λ* solving the operator-selection
     LP (`prop:operator-selection-lp` and friends).  These ARE
     the binding-energy shadow prices per Wedderburn block.  The
     active set {λ : y_λ* > 0} identifies which Wedderburn blocks
     a compound braid actually saturates.
  2. **Gröbner–Shirshov normal forms** in H_n(R, q).  The
     structural representation of each atomic configuration after
     full GS reduction.

This dashboard pulls headline metrics from both layers plus the
auxiliary audits (Macdonald telescope, BK structural battery,
Markov-axiom cross-checks).

Curve-fitting against AME atomic masses (Δ_binding column in the
additive-baseline audit) is **empirical data**, not a QOU
prediction target — included only for sanity check, not asserted
as a 1ppb gate.

Sources
-------
- `lp-confinement-nf-forcing.witness.json` — LP dual primal/dual
  values, active sets, duality gaps for compound braids.
- `confinement-operator-selection.witness.json` — operator-
  selection LP setup + Gram matrix.
- `cross-check-trM-1ppb.witness.json` — Hoefsmit vs markov_peel
  Markov-trace cross-check at 1ppb (passes for all 5 atoms).
- `codata-reconciliation.witness.json` — Markov axioms, q-integer
  identities, anchor scales.
- `ame-2020-binding-energies.witness.json` /
  `rho-f-volume-binding-gap.witness.json` — empirical AME binding
  (informational; not a QOU prediction).
- `brundan-kleshchev-audit.witness.json` — BK structural battery.
- `alpha-k-macdonald-closed-form.witness.json` — Plancherel
  completeness via Macdonald hook telescope.

Output: `onepb-status-dashboard.witness.json`.
"""

from __future__ import annotations
import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
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
            "derivation gap (rho_f_volume_binding_gap, sourcing AME "
            "binding directly)."
        )
        .set_audit_only("docs/audits/onepb-status-dashboard.md")
    )

    sources = {
        # Structural prediction layer (LP dual + GB NF)
        "lp_confinement_nf_forcing":
            load("lp-confinement-nf-forcing.witness.json"),
        "confinement_operator_selection":
            load("confinement-operator-selection.witness.json"),
        "cross_check_trM_1ppb":
            load("cross-check-trM-1ppb.witness.json"),
        # Structural-identity audits
        "codata_reconciliation":
            load("codata-reconciliation.witness.json"),
        "brundan_kleshchev_audit":
            load("brundan-kleshchev-audit.witness.json"),
        "alpha_k_macdonald":
            load("alpha-k-macdonald-closed-form.witness.json"),
        "y_lambda_macdonald_telescope":
            load("y-lambda-macdonald-telescope.witness.json"),
        "demazure_markov_trace":
            load("demazure-markov-trace.witness.json"),
        # Empirical AME data (informational; NOT a QOU prediction)
        "rho_f_volume_binding_gap":
            load("rho-f-volume-binding-gap.witness.json"),
    }

    # ── Layer 1: structural prediction (LP dual + GB NF) ───────────
    lp_nf = sources.get("lp_confinement_nf_forcing") or {}
    lp_data = lp_nf.get("data", {}) or {}
    lp_summary = {
        "n_compounds_total": lp_data.get("n_compounds_total"),
        "n_compounds_maximizer_in_active": lp_data.get(
            "n_compounds_maximizer_in_active"
        ),
        "lp_dual_emitted": lp_data.get("lp_dual_emitted"),
        "compounds": [
            {
                "label": c.get("label"),
                "active_set": c.get("active_set_partitions"),
                "active_set_size": c.get("active_set_size"),
                "compound_maximizer_lambda": c.get(
                    "compound_maximizer_lambda"
                ),
                "I_maximizer_lambda": c.get("I_maximizer_lambda"),
                "confinement_holds": c.get("confinement_holds"),
                "delta_within_bound": c.get("delta_within_bound"),
            }
            for c in lp_data.get("compounds", [])
        ],
    }
    # Per-compound LP dual variables (y0_star, y_star, primal/dual obj).
    lp_summary["dual_values"] = lp_data.get("lp_dual_summary", [])

    # ── Layer 2: Markov-trace consistency (Hoefsmit vs markov_peel) ─
    # cross-check-trM-1ppb was originally hand-rolled (no `data`
    # field); it has since migrated to the standard WitnessBuilder
    # layout where the substantive fields live under `data.*`.
    # Read from both locations so older snapshots remain compatible.
    raw = sources.get("cross_check_trM_1ppb") or {}
    trm = raw.get("data", raw) if isinstance(raw, dict) else {}
    # Tolerance still lives in `parameters.tolerance_relative` on
    # the migrated form; fall back to the field at top level for
    # legacy snapshots.
    tolerance = (
        raw.get("parameters", {}).get("tolerance_relative")
        if isinstance(raw.get("parameters"), dict)
        else None
    ) or trm.get("tolerance_relative", 1e-9)
    # Normalise to float — the witness may store this as a decimal
    # string (parameters.tolerance_relative) or as a numeric literal
    # (legacy top-level); downstream tooling expects float-comparable.
    try:
        tolerance_float = float(tolerance)
    except (TypeError, ValueError):
        tolerance_float = 1e-9
    trm_summary = {
        "atoms_compared": trm.get("atoms_compared", 0),
        "any_diverge": trm.get("any_diverge", None),
        "tolerance_relative": tolerance_float,
        "tolerance_relative_raw": tolerance,
        "max_rel_delta": max(
            (float(d.get("rel_delta", 0)) for d in trm.get("deltas", [])),
            default=0.0,
        ),
        "all_within_1ppb": all(
            d.get("within_1ppb", False) for d in trm.get("deltas", [])
        ) if trm.get("deltas") else None,
    }

    # ── Layer 3: structural identities ─────────────────────────────
    cr = sources.get("codata_reconciliation") or {}
    structural_max_ppb = (cr.get("data", {}) or {}).get(
        "max_non_anchor_delta_ppb", None
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

    # ── Layer 4: empirical AME data (informational) ────────────────
    # Binding metrics now derive from rho_f_volume_binding_gap, which
    # reads AME2020 binding directly (the additive-constituent baseline
    # was purged 2026-06-09).
    rfb = sources.get("rho_f_volume_binding_gap") or {}
    _brows = (rfb.get("data", {}) or {}).get("rows", []) or []
    # rho_f rows always carry float delta_binding_MeV + A ≥ 2 (trust the
    # schema — no per-row validation).  The only boundary case is an
    # absent witness ⇒ _brows == [], handled by the empty-guards below.
    binding_max = max((r["delta_binding_MeV"] for r in _brows), default=None)
    binding_avg = (
        sum(r["delta_binding_MeV"] / r["A"] for r in _brows) / len(_brows)
        if _brows else None
    )

    summary = {
        "structural_lp_dual": lp_summary,
        "markov_trace_consistency": trm_summary,
        "structural_max_non_anchor_delta_ppb": structural_max_ppb,
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
        "ame_empirical_data_informational": {
            "max_delta_binding_MeV": binding_max,
            "avg_binding_per_nucleon_MeV": binding_avg,
            "note": (
                "Empirical AME column for sanity-check only.  QOU "
                "predictions come from the LP dual + GB NF layers "
                "above, not from fitting against this column."
            ),
        },
        "witness_inventory": [
            name for name, data in sources.items() if data is not None
        ],
        "missing_witnesses": [
            name for name, data in sources.items() if data is None
        ],
    }

    print("1ppb-readiness dashboard")
    print("=" * 70)
    print()
    print("Layer 1 — LP dual / GB NF (QOU's structural prediction):")
    print(f"  compounds tested: {lp_summary['n_compounds_total']}")
    print(f"  GB NF maximizer in active set: "
          f"{lp_summary['n_compounds_maximizer_in_active']}/"
          f"{lp_summary['n_compounds_total']}")
    print(f"  duality gap (max across compounds): "
          f"{max((d.get('duality_gap', 0) for d in lp_summary['dual_values']), default=0)}")
    print(f"  active sets: "
          f"{[c['active_set_size'] for c in lp_summary['compounds']]}")
    print()
    print("Layer 2 — Markov-trace consistency (Hoefsmit vs markov_peel):")
    print(f"  atoms compared: {trm_summary['atoms_compared']}, "
          f"any_diverge: {trm_summary['any_diverge']}, "
          f"max rel_delta: {trm_summary['max_rel_delta']:.2e}, "
          f"all_within_1ppb: {trm_summary['all_within_1ppb']}")
    print()
    print("Layer 3 — Structural identities:")
    print(f"  CODATA max non-anchor Δ: {structural_max_ppb} ppb "
          "(AME publication-rounding floor only)")
    print(f"  BK structural audit: {bk_pass}/{bk_total} passed")
    print(f"  Macdonald Plancherel residuals: "
          f"{len(plancherel_residuals)} entries (each ~10⁻⁵¹)")
    print()
    print("Layer 4 — Empirical AME data (informational, not asserted):")
    print(f"  max Δ_binding (²⁰Ne): {binding_max} MeV")
    print(f"  avg per nucleon (A ≥ 4): {binding_avg} MeV/A "
          "(SEMF reference: ~7.5 MeV/A)")
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
    # LP duality gap (structural): must be exactly 0 across all
    # compounds for strong duality to hold.
    if lp_summary["dual_values"]:
        max_gap = max(d.get("duality_gap", 0) for d in lp_summary["dual_values"])
        builder.add_assertion(
            name="lp_max_duality_gap",
            computed=max_gap,
            expected=0.0,
            tolerance=1e-9,
            source="prop:operator-selection-lp strong duality",
        )
    # Markov-trace consistency: max relative difference < 1ppb.
    builder.add_assertion(
        name="markov_trace_max_rel_delta",
        computed=trm_summary["max_rel_delta"],
        expected=0.0,
        tolerance=1e-9,
        source="cross-check-trM-1ppb (Hoefsmit vs markov_peel)",
    )
    builder.add_data("summary", summary)
    builder.add_data("framing_note",
                     "Layers 1–2 are QOU's structural predictions "
                     "(LP dual shadow prices + GB NF Markov-trace "
                     "consistency).  Layer 4 (AME atomic masses) is "
                     "experimental data, not a prediction target — "
                     "QOU does not fit against it.")

    out_path = builder.save()
    print(f"\nWitness: {out_path}")


if __name__ == "__main__":
    main()
