#!/usr/bin/env python3
"""
Bulk-relabel existing witness JSONs with precision + truncation tags.

Per user directive: "track which is which" — every witness must
declare the precision regime it was computed under.  Existing
witnesses (pre-F1) used the f64 path and have no `precision` field.
This one-shot script adds `precision: "f64_numeric_fallback"` and
`truncation_eps: 0.0` to any witness JSON that doesn't have them.

Idempotent: running multiple times has no additional effect.

Usage:
    python3 relabel_witnesses.py [--dry-run]

Default: writes in place, prints a list of files modified.
@module computations/relabel_witnesses
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DEFAULT_PRECISION = "f64_numeric_fallback"
DEFAULT_TRUNCATION_EPS = 0.0


def relabel_one(path: Path, dry_run: bool = False) -> bool:
    """Add precision + truncation_eps tags to a witness JSON if missing.

    Returns True if the file was (would be) modified.
    """
    try:
        data = json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return False
    if not isinstance(data, dict):
        return False

    modified = False
    if "precision" not in data:
        data["precision"] = DEFAULT_PRECISION
        modified = True
    if "truncation_eps" not in data:
        data["truncation_eps"] = DEFAULT_TRUNCATION_EPS
        modified = True

    if modified and not dry_run:
        path.write_text(json.dumps(data, indent=2, default=str))
    return modified


def main(argv: list[str]) -> int:
    dry_run = "--dry-run" in argv
    witnesses = sorted(ROOT.glob("*.witness.json"))
    print(f"Scanning {len(witnesses)} witness JSONs in {ROOT}...")
    modified_count = 0
    for path in witnesses:
        if relabel_one(path, dry_run=dry_run):
            modified_count += 1
            verb = "would relabel" if dry_run else "relabeled"
            print(f"  {verb}: {path.name}")
    if not dry_run:
        print(f"\n{modified_count} witness file(s) updated.")
    else:
        print(f"\n[dry run] {modified_count} witness file(s) "
              f"would be updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
