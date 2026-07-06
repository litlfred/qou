"""I13 audit — incomplete upstream witness coverage.

A production witness file is "incompletely covered" if one or
more of its enumerated rows / entries records an error rather
than a derived value.  Common shape: a sweep across atoms /
partitions / Wedderburn blocks where some entries succeed and
others fail because the upstream producer's coverage is
incomplete.

The catalogue text in `local/compute-integration-watcher`:

  **I13. INCOMPLETE UPSTREAM WITNESS COVERAGE.** A consumer's
  witness records `error_kind: <X>` entries for some atoms /
  blocks because the upstream producer hasn't emitted those
  rows yet.  Fix: extend the producer's atom list; OR mark the
  consumer as a partial result with the missing atoms enumerated.

This audit walks every `computations/*.witness.json`,
collects every `error_kind` field anywhere in the JSON tree,
and surfaces a (witness, error_kind, count, sample-entries)
report.

Emits `incomplete-coverage-audit.witness.json`.

Usage:
    python3 computations/incomplete_coverage_audit.py [--strict]
"""



from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
from witness_base import WitnessBuilder  # noqa: E402

REPO_ROOT = HERE.parent.parent


def _collect_error_kinds(obj: Any,
                         results: list[dict[str, Any]],
                         path: list[str | int]) -> None:
    """Recursively walk a JSON object collecting every `error_kind`."""
    if isinstance(obj, dict):
        ek = obj.get("error_kind")
        if ek:
            # Capture the parent context: include sibling fields
            # that are scalars (these usually identify the failed
            # entry, e.g. `atom`, `label`, `partition`).
            siblings = {
                k: v for k, v in obj.items()
                if k != "error_kind"
                and isinstance(v, (str, int, float, bool))
            }
            results.append({
                "json_path": ".".join(str(p) for p in path),
                "error_kind": ek,
                "siblings": siblings,
            })
        for k, v in obj.items():
            _collect_error_kinds(v, results, path + [k])
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _collect_error_kinds(v, results, path + [i])


def _audit_witness(path: Path) -> dict[str, Any] | None:
    """Audit one witness file for error_kind entries."""
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return None

    results: list[dict[str, Any]] = []
    _collect_error_kinds(d, results, [])
    if not results:
        return None

    rel = path.relative_to(REPO_ROOT)
    kinds = Counter(r["error_kind"] for r in results)
    return {
        "witness": str(rel),
        "total_error_entries": len(results),
        "by_kind": dict(kinds),
        "sample_entries": results[:15],
    }


def main() -> int:
    strict = "--strict" in sys.argv

    # Skip the audit's own output to prevent recursive self-counting:
    # the witness this script emits stores every detected error_kind
    # under `data.rows[*].sample_entries[*].error_kind`, so re-scanning
    # it would re-classify those records as fresh errors each run,
    # inflating `total_error_entries` monotonically.
    SELF_OUTPUT = "incomplete-coverage-audit.witness.json"

    rows: list[dict[str, Any]] = []
    # Scan the whole compute tree's witnesses (reorg scan-root fix).
    for w in sorted((HERE.parent).rglob("*.witness.json")):
        if "_deprecated" in w.parts:
            continue
        if w.name == SELF_OUTPUT:
            continue
        result = _audit_witness(w)
        if result is None:
            continue
        rows.append(result)

    # Total error_kind counter across all witnesses.
    total_by_kind: Counter = Counter()
    for r in rows:
        for k, n in r["by_kind"].items():
            total_by_kind[k] += n

    print("=" * 80)
    print(f"I13 audit — incomplete upstream witness coverage  ({len(rows)} witnesses)")
    print("=" * 80)
    for r in sorted(rows, key=lambda x: -x["total_error_entries"]):
        bk = ", ".join(f"{k}={n}" for k, n in r["by_kind"].items())
        print(f"  {r['witness']:<70s}  {r['total_error_entries']} ({bk})")
    print()
    print(f"Error-kind totals across all witnesses:")
    for k, n in total_by_kind.most_common():
        print(f"  {k:<40s} {n}")
    print()
    print(f"Summary:")
    print(f"  witnesses with error_kind entries: {len(rows)}")
    print(f"  total error_kind entries:          {sum(r['total_error_entries'] for r in rows)}")

    b = (
        WitnessBuilder("incomplete-coverage-audit", engine="python")
        .set_description(
            "I13 audit per local/compute-integration-watcher: every "
            "computations/*.witness.json is walked for "
            "`error_kind` fields anywhere in the JSON tree.  Each hit "
            "records the per-entry failure mode + sibling fields (which "
            "typically identify the failing atom/partition/label), giving "
            "a follow-up agent the per-entry queue needed to extend the "
            "upstream producer's coverage."
        )
        .set_content_block(
            "I13 antipattern (compute-integration-watcher.md §antipatterns)"
        )
        .add_parameter("total_witnesses_with_errors", len(rows))
        .add_parameter("total_error_entries",
                       sum(r["total_error_entries"] for r in rows))
        .add_data("error_kind_totals", dict(total_by_kind))
        .add_data("rows", rows)
        .add_assertion(
            name="no_error_kind_entries",
            computed=1.0 if not rows else 0.0,
            expected=1.0, tolerance=0.0,
            unit="boolean (1.0 = every witness covers its enumerated scope)",
            source="Closure gate: when this passes, every production "
                   "witness has a complete row set for its declared "
                   "atom / partition / block scope.",
        )
    )
    out = b.save()
    print(f"\nWitness: {out}")

    if strict and rows:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
