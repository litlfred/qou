#!/usr/bin/env python3
# polynomial_q_not_applicable: aggregator only; no symbolic-q polynomial logic.
"""
CLASS-A acknowledged-anchor banner (per Workplan-0b/M_N):
This script imports M_*_MEV_VALIDATION constants from
`codata_constants.py` as production inputs (not just as
comparison targets).  M_N is currently a CLASS-A acknowledged-
stub anchor pending its own substrate derivation — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`
for the open spec.  Until that lands, the calibration-discipline
audit (`canonical-script-input-audit`) classifies this script
as "with-substrate-splitting" or "anchor-pending"; reviewers
should treat the M_*_MEV_VALIDATION usage as CAL-3-ish anchor,
NOT as an independent calibration input.
═══════════════════════════════════════════════════════════════

Canonical-derivation pipeline compliance aggregator.

Single-shot dashboard of the **compute-infra discipline** for the
canonical-derivation chain. Joins the four existing infra audits
into one current-state snapshot so reviewers can read one witness
instead of four.

Source audits joined here
-------------------------

1. ``compute-audit-scan.witness.json`` — static scanner for
   performance / discipline patterns P11/P14/P15/P16/P21/P30/P31
   (catalogue: ``.claude/skills/local/compute-audit.md``).

2. ``canonical-script-input-audit.witness.json`` — calibration-
   input scheme audit (3-input vs over-count vs vol-hyp-fitted vs
   m_p-only vs Q_β-only) per
   ``content/quantum-observable-universe/braids-and-knots/calibration-inputs.md``.

3. ``derivation-chain-audit.witness.json`` — per-chain validation
   + computational-trust audit per the QOU methodology directive
   (every numerical claim must trace back to first-principles
   axioms via a ``DerivationChain``).

4. ``codata-reconciliation.witness.json`` — CAL-3 ↔ CODATA
   ``m_n - m_p - m_e`` cross-check (anchors the calibration
   discipline to CODATA 2022 within combined σ).

Output
------

``canonical-derivation-pipeline-compliance.witness.json`` — one
witness with:

* ``contracts``: per-contract pass/warn/fail with the source-of-truth
  audit witness it draws from.
* ``infra_score``: ratio of in-compliance scripts vs total scanned.
* ``known_open_conflicts``: in-source escalations that are documented
  but not yet resolved (e.g. TR_M_AT_Q0 vs Frobenius-selected τ_M).
* ``recommended_next``: ranked Priority list from
  ``docs/audits/2026-05-12-canonical-derivation-compute-review.md §4``.

Usage
-----

    python computations/canonical_derivation_pipeline_compliance.py

Audit-only: results live in
``docs/audits/2026-05-12-canonical-derivation-compute-review.md``.
This script does NOT recompute the source audits; it loads their
emitted witnesses. Run them first if they are stale (the witness
records ``computedAt`` for each source so reviewers can spot
staleness directly).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent

# Source witness files joined into the single dashboard.
SOURCES = {
    "compute_audit_scan": _pb.witness_path("compute-audit-scan.witness.json", HERE),
    "canonical_script_input_audit": (
        _pb.witness_path("canonical-script-input-audit.witness.json", HERE)
    ),
    "derivation_chain_audit": _pb.witness_path("derivation-chain-audit.witness.json", HERE),
    "codata_reconciliation": _pb.witness_path("codata-reconciliation.witness.json", HERE),
    "witness_reproducibility": (
        _pb.witness_path("witness-reproducibility-check.witness.json", HERE)
    ),
    "witness_provenance": (
        _pb.witness_path("witness-provenance-audit.witness.json", HERE)
    ),
}


def _safe_load(path: Path) -> dict[str, Any] | None:
    """Load a witness JSON; return None if missing (caller decides)."""
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        return None


def _summarize_compute_audit(w: dict[str, Any] | None) -> dict[str, Any]:
    """Pattern counts + computedAt + ratio against scanned files."""
    if w is None:
        return {"status": "missing", "note": "compute-audit-scan.witness.json not found"}
    data = w.get("data", {})
    by_pattern = data.get("by_pattern_count", {})
    files_scanned = w.get("parameters", {}).get("files_scanned")
    return {
        "status": "loaded",
        "computedAt": w.get("computedAt"),
        "files_scanned": files_scanned,
        "by_pattern_count": by_pattern,
        "total_findings": sum(by_pattern.values()),
        "top_files": data.get("top_files", [])[:10],
    }


def _summarize_input_audit(w: dict[str, Any] | None) -> dict[str, Any]:
    """3-input scheme breakdown + ratio of canonical scripts."""
    if w is None:
        return {"status": "missing", "note": "canonical-script-input-audit.witness.json not found"}
    data = w.get("data", {})
    by_scheme = data.get("by_scheme", {})
    canonical = data.get("canonical_3input_count", 0)
    over_count = data.get("over_count_count", 0)
    vol_hyp = data.get("vol_hyp_fitted_count", 0)
    total_classified = sum(by_scheme.values()) if by_scheme else (
        canonical + over_count + vol_hyp
    )
    return {
        "status": "loaded",
        "computedAt": w.get("computedAt"),
        "by_scheme": by_scheme,
        "canonical_3input_count": canonical,
        "over_count_count": over_count,
        "vol_hyp_fitted_count": vol_hyp,
        "total_classified": total_classified,
        "canonical_ratio": (
            (canonical / total_classified) if total_classified else None
        ),
    }


def _summarize_chain_audit(w: dict[str, Any] | None) -> dict[str, Any]:
    """Per-chain pass/fail + assertion counts."""
    if w is None:
        return {"status": "missing", "note": "derivation-chain-audit.witness.json not found"}
    chain_results = w.get("data", {}).get("chain_results", [])
    assertions = w.get("assertions", [])
    failed = [a for a in assertions if not a.get("passed", True)]
    return {
        "status": "loaded",
        "computedAt": w.get("computedAt"),
        "chain_count": len(chain_results),
        "assertion_count": len(assertions),
        "all_passed": w.get("allPassed"),
        "failed_assertion_count": len(failed),
    }


def _summarize_codata_recon(w: dict[str, Any] | None) -> dict[str, Any]:
    if w is None:
        return {"status": "missing", "note": "codata-reconciliation.witness.json not found"}
    return {
        "status": "loaded",
        "computedAt": w.get("computedAt"),
        "all_passed": w.get("allPassed"),
        "assertion_count": len(w.get("assertions", [])),
    }


def _summarize_repro(w: dict[str, Any] | None) -> dict[str, Any]:
    """P32 byte-equality reproducibility check."""
    if w is None:
        return {
            "status": "missing",
            "note": "witness-reproducibility-check.witness.json not found",
        }
    data = w.get("data") or {}
    return {
        "status": "loaded",
        "computedAt": w.get("computedAt"),
        "by_status": data.get("by_status") or {},
        "pass_ratio": data.get("pass_ratio"),
    }


def _summarize_provenance(w: dict[str, Any] | None) -> dict[str, Any]:
    """I14 witness-provenance completeness."""
    if w is None:
        return {
            "status": "missing",
            "note": "witness-provenance-audit.witness.json not found",
        }
    counts = w.get("data", {}).get("counts", {})
    return {
        "status": "loaded",
        "computedAt": w.get("computedAt"),
        "total_scanned": counts.get("total_scanned"),
        "prov_ok": counts.get("prov_ok"),
        "prov_missing": counts.get("prov_missing"),
        "prov_audit_exempt": counts.get("prov_audit_exempt"),
        "completeness_ratio": counts.get("completeness_ratio"),
    }


# ── Contract definitions ──────────────────────────────────────────
# Each contract maps to a single source-of-truth witness and a
# threshold function that turns the source into pass/warn/fail.

def _contract_witness_builder(scan: dict[str, Any]) -> dict[str, Any]:
    """P30 measures WitnessBuilder adoption."""
    p30 = scan.get("by_pattern_count", {}).get("P30", 0)
    files = scan.get("files_scanned") or 0
    return {
        "name": "WitnessBuilder usage (P30)",
        "source": "compute-audit-scan.witness.json",
        "metric": f"{p30} of {files} files write witnesses without WitnessBuilder",
        "status": (
            "fail" if p30 > 50 else
            "warn" if p30 > 0 else
            "pass"
        ),
        "remediation": (
            "Batch-port hand-written .witness.json writers to "
            "witness_base.WitnessBuilder. Reference: "
            "docs/audits/2026-05-08-compute-audit-workplan.md §Tier 2."
        ),
    }


def _contract_codata_registry(scan: dict[str, Any]) -> dict[str, Any]:
    """P31 measures CODATA-literal-outside-registry leakage."""
    p31 = scan.get("by_pattern_count", {}).get("P31", 0)
    return {
        "name": "CODATA constants from registry only (P31)",
        "source": "compute-audit-scan.witness.json",
        "metric": f"{p31} hardcoded CODATA literals outside the allowlist",
        "status": (
            "fail" if p31 > 30 else
            "warn" if p31 > 0 else
            "pass"
        ),
        "remediation": (
            "Replace each hit with import from codata_constants "
            "(_VALIDATION aliases) or experimental_constants. Tag "
            "audit-only consumers with `# noqa: P31` and a "
            "justifying comment."
        ),
    }


def _contract_witness_reproducibility(repro: dict[str, Any]) -> dict[str, Any]:
    """P32 measures byte-equality reproducibility of *.derivation.json builders."""
    by_status = repro.get("by_status") or {}
    pass_n = by_status.get("pass", 0)
    drift_n = by_status.get("drift", 0)
    error_n = by_status.get("error", 0)
    timeout_n = by_status.get("timeout", 0)
    skip_n = by_status.get("skip", 0)
    total_checkable = pass_n + drift_n + error_n + timeout_n
    pass_ratio = repro.get("pass_ratio")
    return {
        "name": "Witness reproducibility (P32)",
        "source": "witness-reproducibility-check.witness.json",
        "metric": (
            f"{pass_n}/{total_checkable} builders byte-equal "
            f"(drift={drift_n}, error={error_n}, "
            f"timeout={timeout_n}, skip={skip_n})"
        ),
        # Drift = real non-determinism = fail.
        # Error / timeout = environment issue = warn (not the
        # builder's fault per se, but blocks coverage).
        "status": (
            "fail" if drift_n > 0 else
            "warn" if (error_n + timeout_n) > 0 else
            "pass" if pass_ratio == 1.0 or pass_n > 0 else
            "fail"
        ),
        "remediation": (
            "For drift: investigate non-determinism (PYTHONHASHSEED, "
            "timestamps, hand-edits to committed JSON not reproduced "
            "by the script). For error/timeout: install missing deps "
            "or bump PER_BUILDER_TIMEOUT_S. Reference: "
            "witness_reproducibility_check.py + "
            "docs/audits/2026-05-12-canonical-derivation-compute-review.md §4 P3.2."
        ),
    }


def _contract_three_input_scheme(inp: dict[str, Any]) -> dict[str, Any]:
    """canonical-script-input-audit: 3-input vs over-count balance."""
    canonical = inp.get("canonical_3input_count", 0)
    over_count = inp.get("over_count_count", 0)
    total_classified = inp.get("total_classified", 0)
    return {
        "name": "3-input canonical scheme (CAL-1/2/3)",
        "source": "canonical-script-input-audit.witness.json",
        "metric": (
            f"{canonical} canonical / {over_count} over-count / "
            f"{total_classified} classified"
        ),
        "status": (
            "fail" if over_count > 100 else
            "warn" if over_count > 0 else
            "pass"
        ),
        "remediation": (
            "Migrate over-count scripts (consume both m_p and m_n) "
            "to the 3-input scheme: m_n = m_p + Q_β + m_e, with "
            "m_p derived from |tr_M(p, q_0)| · E_0. Reference: "
            "docs/audits/2026-05-10-workplan-0b-script-rewire-handoff.md."
        ),
    }


def _contract_derivation_chains(chain: dict[str, Any]) -> dict[str, Any]:
    """derivation-chain-audit: every chain must pass."""
    failed = chain.get("failed_assertion_count", 0)
    return {
        "name": "Per-chain trust-basis validation",
        "source": "derivation-chain-audit.witness.json",
        "metric": (
            f"{chain.get('assertion_count', 0)} assertions across "
            f"{chain.get('chain_count', 0)} chains; "
            f"{failed} failed"
        ),
        "status": "fail" if failed > 0 else "pass",
        "remediation": (
            "Read derivation-chain-audit.witness.json `assertions` "
            "for failed chain IDs and trust-basis transitions. "
            "Each `script_cited` step that fails should be promoted "
            "to `derived` or `lean_proven`."
        ),
    }


def _contract_codata_reconciliation(recon: dict[str, Any]) -> dict[str, Any]:
    """codata-reconciliation: CAL-3 ↔ CODATA m_n - m_p - m_e."""
    return {
        "name": "CAL-3 ↔ CODATA cross-check",
        "source": "codata-reconciliation.witness.json",
        "metric": (
            f"{recon.get('assertion_count', 0)} reconciliation "
            f"assertions; allPassed={recon.get('all_passed')}"
        ),
        "status": (
            "missing" if recon.get("status") == "missing" else
            "pass" if recon.get("all_passed") else
            "fail"
        ),
        "remediation": (
            "Refresh codata_constants.py against CODATA 2022 "
            "and re-run codata_reconciliation.py."
        ),
    }


# ── Known open conflicts (in-source escalations) ─────────────────
KNOWN_OPEN_CONFLICTS = [
    {
        "id": "TR_M_AT_Q0_vs_frobenius_proof",
        "where": "computations/derivation_chain.py:68-93",
        "summary": (
            "Registry TR_M_AT_Q0 (Wenzl-bridge y_λ assembly) "
            "disagrees with Frobenius-selected τ_M (`from_scratch/` "
            "chain on commit 25a204efa). Two distinct canonical "
            "values for the same nominal quantity."
        ),
        "audit_doc": (
            "docs/audits/2026-05-11-why-individual-mass-residuals-fit-not-derive.md "
            "§\"Update 2026-05-11 — τ_M / τ_SW conflation diagnosis\""
        ),
        "blocks_fix": (
            "P2.1 schur-weyl-weight-* → tau-sw-weight-* rename"
        ),
    },
]


# ── Recommended-next list (ranked from §4 of the review) ─────────
# As items land they are removed from the list; the most recent
# closure is recorded in the witness as `closed_recently` for audit.
CLOSED_RECENTLY = [
    "P0.1 — aggregator compliance witness (this script)",
    "P1.1 — deuteron_delta_i_audit Conv-C audit-only banner",
    "P1.2 — content 'prediction' language audit (closed in-tree)",
    "P3.1 — P31 hardcoded-CODATA scanner",
    "P3.2 — witness reproducibility byte-equality check (P32 contract above)",
    "P31-triage Phase A — 12 m_e (CAL-1) and m_μ/m_e (CAL-2) module-constant migrations (40 → 28 hits, contract: fail → warn)",
]

RECOMMENDED_NEXT = [
    {
        "priority": "P31-triage Phase B",
        "summary": (
            "28 remaining P31 hits. Categorized: (a) ~9 mass-table dict "
            "literals for m_p/m_n in mass-prediction scripts — OVERLAPS "
            "with Workplan-0b (the right fix is to derive m_n from m_p "
            "+ Q_β, not import the literal); (b) ~6 docstring / print-"
            "format / json-data hits — add `# noqa: P31` with audit-"
            "only justification; (c) ~13 m_p/m_n module constants in "
            "non-prediction scripts (audits, comparisons) — replace "
            "with M_P_MEV_VALIDATION / M_N_MEV_VALIDATION imports."
        ),
        "blocked_on": None,
    },
    {
        "priority": "P30-triage",
        "summary": (
            "Port the 96 hand-written .witness.json writers to "
            "witness_base.WitnessBuilder. Some hand-written witnesses "
            "encode review-only metadata that needs a builder pattern "
            "extension; case-by-case judgement required."
        ),
        "blocked_on": None,
    },
    {
        "priority": "P2.1",
        "summary": (
            "Rename schur-weyl-weight-* → tau-sw-weight-* across "
            "21 derivation-JSONs + 8 Python consumers."
        ),
        "blocked_on": "TR_M_AT_Q0_vs_frobenius_proof (see open conflicts)",
    },
    {
        "priority": "Workplan-0b",
        "summary": (
            "112 over-count scripts to migrate to the 3-input scheme "
            "(derive m_n = m_p + Q_β instead of importing both). "
            "Largest-scope semantic change; needs per-script "
            "verification that downstream consumers still round-trip. "
            "Subsumes the (a) tranche of P31-triage Phase B."
        ),
        "blocked_on": None,
    },
]


def _contract_witness_provenance(prov: dict[str, Any]) -> dict[str, Any]:
    """I14 witness-provenance completeness — every witness must
    declare engine, scriptFile, commitSha."""
    if prov.get("status") != "loaded":
        return {
            "name": "Witness provenance completeness (I14)",
            "source": "witness-provenance-audit.witness.json",
            "metric": "audit witness missing — run witness_provenance_audit.py",
            "status": "warn",
            "remediation": (
                "Run `python3 computations/"
                "witness_provenance_audit.py` to emit the audit witness."
            ),
        }
    missing = prov.get("prov_missing") or 0
    total = prov.get("total_scanned") or 0
    ratio = prov.get("completeness_ratio") or 0.0
    return {
        "name": "Witness provenance completeness (I14)",
        "source": "witness-provenance-audit.witness.json",
        "metric": (
            f"{missing} of {total} witnesses missing "
            f"engine/scriptFile/commitSha (completeness "
            f"ratio {ratio:.3f})"
        ),
        "status": (
            "fail" if missing > 50 else
            "warn" if missing > 0 else
            "pass"
        ),
        "remediation": (
            "Wrap hand-written .witness.json writers in "
            "witness_base.WitnessBuilder. See PR #781 fixups for "
            "the pattern (mass_table_ppb.py, binding_canonical.py)."
        ),
    }


def main() -> int:
    sources_loaded = {key: _safe_load(path) for key, path in SOURCES.items()}

    # Per-source summaries
    scan_summary = _summarize_compute_audit(sources_loaded["compute_audit_scan"])
    input_summary = _summarize_input_audit(
        sources_loaded["canonical_script_input_audit"]
    )
    chain_summary = _summarize_chain_audit(
        sources_loaded["derivation_chain_audit"]
    )
    codata_summary = _summarize_codata_recon(
        sources_loaded["codata_reconciliation"]
    )
    repro_summary = _summarize_repro(
        sources_loaded["witness_reproducibility"]
    )
    prov_summary = _summarize_provenance(
        sources_loaded["witness_provenance"]
    )

    # Per-contract pass/warn/fail
    contracts = [
        _contract_witness_builder(scan_summary),
        _contract_codata_registry(scan_summary),
        _contract_three_input_scheme(input_summary),
        _contract_derivation_chains(chain_summary),
        _contract_codata_reconciliation(codata_summary),
        _contract_witness_reproducibility(repro_summary),
        _contract_witness_provenance(prov_summary),
    ]

    # Aggregate score: pass=1, warn=0.5, fail=0, missing=skip
    score_map = {"pass": 1.0, "warn": 0.5, "fail": 0.0}
    scored = [
        score_map[c["status"]] for c in contracts if c["status"] in score_map
    ]
    infra_score = sum(scored) / len(scored) if scored else None

    # Print human-readable summary
    print("Canonical-derivation pipeline compliance dashboard")
    print("=" * 60)
    for c in contracts:
        marker = {"pass": "✓", "warn": "⚠", "fail": "✗", "missing": "?"}[
            c["status"]
        ]
        print(f"  {marker}  {c['name']:48s}  {c['status']}")
        print(f"      {c['metric']}")
    print()
    if infra_score is not None:
        print(f"Infra score: {infra_score:.2f} (1.0 = all contracts pass)")
    print()
    if KNOWN_OPEN_CONFLICTS:
        print("Known open conflicts:")
        for k in KNOWN_OPEN_CONFLICTS:
            print(f"  • [{k['id']}] {k['summary']}")
    print()
    print("Recommended next:")
    for r in RECOMMENDED_NEXT:
        blocked = (
            f"  [BLOCKED on: {r['blocked_on']}]" if r["blocked_on"] else ""
        )
        print(f"  {r['priority']}  {r['summary']}{blocked}")

    # Emit witness
    try:
        from witness_base import WitnessBuilder
    except ImportError:
        sys.path.insert(0, str(HERE))
        from witness_base import WitnessBuilder

    w = (
        WitnessBuilder(
            "canonical-derivation-pipeline-compliance",
            engine="python",
        )
        .set_description(
            "Aggregator dashboard of compute-infra compliance for "
            "the canonical-derivation chain. Joins four upstream "
            "audit witnesses into one current-state snapshot. See "
            "docs/audits/2026-05-12-canonical-derivation-compute-"
            "review.md §3 for the contract definitions."
        )
        .set_audit_only(
            "docs/audits/2026-05-12-canonical-derivation-compute-review.md"
        )
        .add_parameter(
            "sources",
            {k: str(p.relative_to(HERE.parent.parent))
             for k, p in SOURCES.items()},
        )
        .add_data("source_summaries", {
            "compute_audit_scan": scan_summary,
            "canonical_script_input_audit": input_summary,
            "derivation_chain_audit": chain_summary,
            "codata_reconciliation": codata_summary,
            "witness_reproducibility": repro_summary,
        })
        .add_data("contracts", contracts)
        .add_data("infra_score", infra_score)
        .add_data("known_open_conflicts", KNOWN_OPEN_CONFLICTS)
        .add_data("closed_recently", CLOSED_RECENTLY)
        .add_data("recommended_next", RECOMMENDED_NEXT)
        .add_caveat(
            "Aggregator-only: this script does NOT re-run any of the "
            "four source audits. Stale source witnesses propagate "
            "stale results here. Each source's `computedAt` is "
            "preserved in `source_summaries` so reviewers can spot "
            "staleness directly."
        )
        .add_caveat(
            "Contract thresholds are heuristic (e.g. P30>50 = fail). "
            "They reflect 2026-05-12 baseline; tighten as the "
            "infra-discipline backlog drains."
        )
    )
    w.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
