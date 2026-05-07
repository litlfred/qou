#!/usr/bin/env python3
"""Bulk migration: rename `timestamp` and `timestamp_utc` keys in witness
JSON files to the canonical `computedAt` from ComputationWitness schema.

Per Copilot review on PR #433, the canonical schema field is
`computedAt` (folio-assistant/schemas/types.ts) but historical witnesses
use `timestamp` (244 files) or `timestamp_utc` (34 newer files from
PR #427). This script standardizes all to `computedAt`.

USAGE:
    python3 migrate_witness_timestamp_to_computedAt.py            # dry-run
    python3 migrate_witness_timestamp_to_computedAt.py --apply    # write
"""
from __future__ import annotations
import json
import sys
from pathlib import Path


def migrate_one(path: Path, apply: bool):
    """Migrate a single witness file. Returns (changed, key_seen).

    Returns (False, "skip:<reason>") on any I/O or parse failure so the
    bulk migration is resilient (caller logs and continues).
    """
    try:
        with open(path) as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return False, "skip:invalid-json"
    except OSError as e:
        # Permission denied, broken symlink, missing file, etc.
        return False, f"skip:io:{e.__class__.__name__}"
    if not isinstance(data, dict):
        return False, None
    key = None
    if "timestamp_utc" in data:
        key = "timestamp_utc"
    elif "timestamp" in data:
        key = "timestamp"
    if key is None:
        return False, None
    if "computedAt" in data:
        # Already has computedAt; just remove the duplicate
        if apply:
            data.pop(key)
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
        return True, f"{key} (dup)"

    # Rename: insert computedAt at the position of the old key
    new_data = {}
    for k, v in data.items():
        if k == key:
            new_data["computedAt"] = v
        else:
            new_data[k] = v
    if apply:
        with open(path, "w") as f:
            json.dump(new_data, f, indent=2)
    return True, key


def main():
    apply = "--apply" in sys.argv
    base = Path(__file__).parent

    counts = {"timestamp": 0, "timestamp_utc": 0,
              "timestamp (dup)": 0, "timestamp_utc (dup)": 0}
    n_files = 0
    n_unchanged = 0
    for path in sorted(base.glob("*.witness.json")):
        n_files += 1
        changed, key = migrate_one(path, apply)
        if changed:
            counts[key] = counts.get(key, 0) + 1
        else:
            n_unchanged += 1

    print(f"{'APPLIED' if apply else 'DRY-RUN'}:")
    print(f"  Total .witness.json files: {n_files}")
    print(f"  Unchanged (no timestamp key): {n_unchanged}")
    for k, v in counts.items():
        print(f"  Files with `{k}` key: {v}")
    if not apply:
        print()
        print("Run with --apply to write changes.")


if __name__ == "__main__":
    main()
