"""
chi_witness_completeness_audit.py — audit chi-*.witness.json files
for partition completeness (p(n) coverage).

Scope: currently scans only chi-*-at-q0-*.witness.json. Downstream
consumer staleness (binding-*.witness.json against current chi
witnesses) is documented in docs/audits/2026-06-09-binding-canonical-
default-depth-stratified.md §Prevention #3 (manual refresh routine)
but not yet automated by this script. Adding downstream-staleness
auditing is tracked as a follow-up.

Class of bug this catches (2026-06-09):
  A downstream compute (e.g. binding_depth_stratified_lr.py) consumes
  a cached chi-*.witness.json. If that cached witness is PARTIAL
  (missing partitions) when the downstream runs, the missing
  partitions get silently substituted as 0 in Φ_atom — Φ_free −
  Φ_atom over-counts — B inflates.

  Observed instance: ⁴He LR binding witness recorded B/AME = 2.089
  while Rust direct gave 0.497. Root cause: stale binding witness
  consumed a 24/77 partial cached ⁴He atom chi witness. The chi
  witness was later upgraded to 77/77, but the binding witness was
  not regenerated. Re-running binding_depth_stratified_lr.py against
  the now-complete chi witness gave 0.497, matching Rust exactly.

Discipline:
  - Every chi-*.witness.json should be COMPLETE: n_cached_partitions
    == p(n_strands).
  - Every downstream binding/τ_M witness that consumes chi witnesses
    must record the chi witness identities + their partition counts
    at consumption time, so we can detect later staleness.

Usage:
    python3 chi_witness_completeness_audit.py
    python3 chi_witness_completeness_audit.py --strict   # exit 1 on issues

Output: structured stdout report + chi-witness-completeness-audit.witness.json
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder

# Partition counts p(n) for relevant strand counts.
# H_3=3, H_6=11, H_9=30, H_12=77, H_15=176, H_18=385, H_21=792.
PARTITION_COUNTS = {3: 3, 6: 11, 9: 30, 12: 77, 15: 176, 18: 385, 21: 792}


def audit_chi_witness(path: Path) -> dict:
    """Audit a single chi-*.witness.json for partition completeness."""
    try:
        w = json.loads(path.read_text())
    except Exception as e:
        return {"path": str(path.name), "error": f"parse: {e}"}
    n_strands = int(w.get("n_strands", 0))
    n_cached = len(w.get("by_partition", []))
    expected = PARTITION_COUNTS.get(n_strands)
    complete = (n_cached == expected) if expected is not None else None
    return {
        "path": path.name,
        "n_strands": n_strands,
        "n_cached_partitions": n_cached,
        "expected_partitions": expected,
        "complete": complete,
        "coverage_pct": round(100 * n_cached / expected, 2) if expected else None,
    }


def chi_witnesses_in_dir(d: Path) -> list[Path]:
    """All chi-*-at-q0-*.witness.json files in a directory."""
    return sorted(set(list(d.glob("chi-*-at-q0-*.witness.json")) +
                      list(d.glob("chi-*-h*-at-q0-*.witness.json"))))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 if any chi witness is incomplete")
    args = parser.parse_args()

    builder = WitnessBuilder("chi-witness-completeness-audit")
    builder.set_description(
        "Audit chi-*.witness.json files for partition completeness "
        "(p(n) coverage). Catches the class of bug where a stale "
        "binding witness silently consumed a partial chi witness. "
        "See docs/audits/2026-06-09-binding-canonical-default-"
        "depth-stratified.md §(iii)."
    )

    chi_files = chi_witnesses_in_dir(HERE)
    audits = [audit_chi_witness(fp) for fp in chi_files]

    incomplete = [a for a in audits if a.get("complete") is False]
    unknown = [a for a in audits if a.get("complete") is None]

    print(f"{'witness':<60} {'n_str':>6} {'cached':>7} {'p(n)':>5} "
          f"{'cov%':>6} {'?':>3}")
    print("-" * 100)
    for a in audits:
        marker = ("YES" if a.get("complete") is True
                  else ("NO" if a.get("complete") is False else "?"))
        expected_val = a.get("expected_partitions")
        coverage_val = a.get("coverage_pct")
        expected_str = str(expected_val) if expected_val is not None else "?"
        coverage_str = str(coverage_val) if coverage_val is not None else "?"
        print(f"{a['path']:<60} "
              f"{a.get('n_strands', '?'):>6} "
              f"{a.get('n_cached_partitions', '?'):>7} "
              f"{expected_str:>5} "
              f"{coverage_str:>6} "
              f"{marker:>3}")

    print()
    print(f"=== SUMMARY ===")
    print(f"  total chi witnesses scanned: {len(audits)}")
    print(f"  complete:   {sum(1 for a in audits if a.get('complete') is True)}")
    print(f"  incomplete: {len(incomplete)}")
    print(f"  unknown:    {len(unknown)}")
    if incomplete:
        print("  INCOMPLETE:")
        for a in incomplete:
            print(f"    {a['path']}: {a['n_cached_partitions']}/"
                  f"{a['expected_partitions']} ({a['coverage_pct']}%)")

    builder.add_data("audits", audits)
    builder.add_data("incomplete", incomplete)
    builder.add_data("unknown_partition_count_strands", unknown)
    builder.add_data("total_scanned", len(audits))
    builder.add_data("total_complete",
                      sum(1 for a in audits if a.get("complete") is True))
    builder.add_data("total_incomplete", len(incomplete))
    builder.add_data("total_unknown", len(unknown))
    # `unknown` = couldn't verify (JSON parse error, or n_strands not in
    # PARTITION_COUNTS). It must NOT pass the audit: an unverifiable witness
    # is exactly the "partial/malformed chi consumed downstream" class of
    # bug this audit exists to catch.
    if not incomplete and not unknown:
        verdict = "PASS — all chi witnesses complete"
    elif incomplete:
        verdict = (
            f"FAIL — {len(incomplete)} chi witnesses incomplete"
            + (f" (+{len(unknown)} unverifiable)" if unknown else "")
            + "; downstream binding/tau_M computes that consume these will "
              "silently substitute 0 for missing partitions and OVER-COUNT "
              "binding."
        )
    else:
        verdict = (
            f"FAIL — {len(unknown)} chi witnesses could not be verified "
            "(JSON parse error or n_strands not in PARTITION_COUNTS); "
            "completeness is UNKNOWN, so downstream consumers are not safe."
        )
    builder.add_data("verdict", verdict)

    builder.add_assertion(
        "no_incomplete_chi_witnesses",
        computed=len(incomplete),
        expected=0,
        tolerance=0,
        unit="count",
        source="audit (this script)",
    )
    builder.add_assertion(
        "no_unverifiable_chi_witnesses",
        computed=len(unknown),
        expected=0,
        tolerance=0,
        unit="count",
        source="audit (this script)",
    )

    builder.save()

    # --strict fails on incomplete OR unverifiable witnesses.
    if args.strict and (incomplete or unknown):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
