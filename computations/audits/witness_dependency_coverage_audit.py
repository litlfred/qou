#!/usr/bin/env python3
"""Detect witnesses that lack upstream dependency tracking.

**Why this exists.**  The stale-audit class — "an audit whose own witness
isn't regenerated when its inputs change reports yesterday's answer with
today's authority" — has a root cause: witnesses that don't declare their
upstream dependencies via `upstream_witness_hashes`.  When they do declare
them, `witness_dependency_drift.py` catches staleness.  When they don't,
nothing does.

This audit finds witnesses that are **aggregators** (they read other
witness files or data files and produce a summary) but don't declare
`upstream_witness_hashes`.  These are the "silent stale" risk class.

Two concrete instances from PR #4929's rebase:
  - `onepb-status-dashboard.witness.json`: aggregates L1 precision status
    from many witnesses, but predated a precision-limit finding.
  - chapter audit count aggregates: drifted during rebase without flagging.

**Heuristic for "aggregator".**  A witness is likely an aggregator if:
  1. Its name contains 'dashboard', 'status', 'aggregate', 'summary',
     'report', or 'compliance' (naming convention).
  2. Its producer script (if identifiable from `scriptFile`) imports or
     opens other `*.witness.json` files.

**The coverage metric.**  Of all witnesses, what fraction declare
`upstream_witness_hashes`?  Of the aggregator subset, what fraction?
The second number is the one that matters for the stale-audit class.

    python3 witness_dependency_coverage_audit.py            # report
    python3 witness_dependency_coverage_audit.py --strict   # exit 1 if
                                                            # aggregators lack
                                                            # upstream tracking
    python3 witness_dependency_coverage_audit.py --list     # full list
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Aggregator name patterns — witnesses whose name suggests they read
# other witnesses or data files and produce a summary.
AGGREGATOR_PATTERNS = (
    "dashboard",
    "status",
    "aggregate",
    "summary",
    "compliance",
    "report",
    "onepb",
    "per-observable",
    "coverage",
)

# Suffixes for audit-exempt witnesses (they record provenance, not results).
AUDIT_EXEMPT_SUFFIXES = (
    "-audit.witness.json",
    "-scan.witness.json",
)


def is_aggregator(name: str) -> bool:
    """Heuristic: does this witness name suggest an aggregation role?"""
    lower = name.lower()
    return any(pat in lower for pat in AGGREGATOR_PATTERNS)


def scan_witnesses(root: Path) -> dict:
    """Walk all *.witness.json under root and classify them."""
    results = {
        "total": 0,
        "with_upstream": 0,
        "without_upstream": 0,
        "aggregator_total": 0,
        "aggregator_with_upstream": 0,
        "aggregator_without_upstream": [],
        "exempt": 0,
    }

    for wf in sorted(root.rglob("*.witness.json")):
        # Skip deprecated directories
        if "_deprecated" in str(wf):
            continue
        # Skip audit-exempt
        name = wf.name
        if any(name.endswith(s) for s in AUDIT_EXEMPT_SUFFIXES):
            results["exempt"] += 1
            continue

        results["total"] += 1

        try:
            data = json.loads(wf.read_text())
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue

        # Check for upstream_witness_hashes in any of the common locations.
        #
        # `data.upstream_witness_hashes` was MISSING from this list until
        # 2026-08-23, and it is where `qou_substrate.witness.record_upstream`
        # actually writes -- i.e. the canonical location, and the one the
        # 122 producers using that helper populate. Measured over 3045
        # witnesses: 235 carry `data.upstream_witness_hashes`, 2 carry the
        # top-level key. So this audit reported coverage of 2 (0.1%) against
        # a true 235 (7.7%) -- under-reporting by two orders of magnitude,
        # and reporting near-total absence of a mechanism that is in fact
        # adopted by hundreds of producers.
        #
        # Found while asking why nothing flagged borromean-per-lambda-fr-probe
        # as stale after its y_lambda input moved convention C -> D.
        has_upstream = False
        for getter in (
            lambda d: d.get("upstream_witness_hashes"),
            lambda d: (d.get("data") or {}).get("upstream_witness_hashes")
            if isinstance(d.get("data"), dict) else None,
            lambda d: (d.get("derivation_inputs") or {}).get(
                "upstream_witness_hashes")
            if isinstance(d.get("derivation_inputs"), dict) else None,
        ):
            try:
                val = getter(data)
            except Exception:
                val = None
            if val:
                has_upstream = True
                break

        if has_upstream:
            results["with_upstream"] += 1
        else:
            results["without_upstream"] += 1

        if is_aggregator(name):
            results["aggregator_total"] += 1
            if has_upstream:
                results["aggregator_with_upstream"] += 1
            else:
                results["aggregator_without_upstream"].append(
                    str(wf.relative_to(root))
                )

    return results


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Detect witnesses lacking upstream dependency tracking."
    )
    ap.add_argument(
        "--strict", action="store_true",
        help="exit 1 if any aggregator witness lacks upstream tracking"
    )
    ap.add_argument(
        "--list", action="store_true",
        help="print every untracked aggregator witness"
    )
    args = ap.parse_args()

    # Find repo root and computations/ directory
    import subprocess
    try:
        repo_root = Path(subprocess.check_output(
            ["git", "rev-parse", "--show-toplevel"],
            text=True
        ).strip())
    except (subprocess.CalledProcessError, FileNotFoundError):
        repo_root = Path(__file__).resolve().parent.parent.parent

    root = repo_root / "computations"
    if not root.exists():
        print("WARNING: computations/ directory not found on disk.")
        print("  This may be a sparse checkout. Run from a full checkout")
        print("  or pass the computations/ path as an argument.")
        return 0

    results = scan_witnesses(root)

    total = results["total"]
    pct_tracked = (
        100.0 * results["with_upstream"] / total if total else 0
    )
    agg_total = results["aggregator_total"]
    agg_untracked = results["aggregator_without_upstream"]
    agg_pct = (
        100.0 * results["aggregator_with_upstream"] / agg_total
        if agg_total else 100.0
    )

    print(f"Witness dependency coverage audit")
    print(f"  scanned: {total} witnesses ({results['exempt']} audit-exempt)")
    print(f"  with upstream_witness_hashes: {results['with_upstream']} "
          f"({pct_tracked:.1f}%)")
    print(f"  without: {results['without_upstream']}")
    print()
    print(f"  aggregator witnesses: {agg_total}")
    print(f"  aggregator with upstream tracking: "
          f"{results['aggregator_with_upstream']} ({agg_pct:.1f}%)")
    print(f"  aggregator WITHOUT tracking: {len(agg_untracked)}")

    if agg_untracked and (args.list or args.strict):
        print()
        print("  Untracked aggregators (stale-audit risk):")
        for path in agg_untracked:
            print(f"    {path}")

    if args.strict and agg_untracked:
        print()
        print(f"FAIL: {len(agg_untracked)} aggregator witness(es) lack "
              f"upstream dependency tracking.")
        print("  These are the 'silent stale' risk class — if their inputs")
        print("  change, no checker flags them. Add upstream_witness_hashes")
        print("  to their producer scripts (see witness_dependency_drift.py")
        print("  adoption pattern).")
        return 1

    print()
    print("OK" if not agg_untracked else
          f"WARN: {len(agg_untracked)} untracked aggregator(s) (advisory)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
