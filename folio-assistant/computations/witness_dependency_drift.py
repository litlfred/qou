#!/usr/bin/env python3
"""
Witness dependency-drift validator.

Walks every `*.witness.json` under `folio-assistant/computations/` and,
for each that carries `derivation_inputs.upstream_witness_hashes`,
verifies each recorded entry's sha256 against the current bytes of
the named upstream file on disk.

Drift means: an upstream witness changed since this witness was last
regenerated.  The downstream witness is stale and must be re-run
before its contents can be trusted.

Why this exists
───────────────
`.github/workflows/witness-pipeline.yml` re-runs a hardcoded list of
validator scripts and `git diff`s their outputs.  Scripts not on the
runlist are never re-executed in CI, so the workflow cannot detect
when a downstream witness has been left behind by an upstream change.
See `docs/audits/2026-05-16-stale-witness-infra-gap.md` for the full
write-up.

Adoption pattern (for downstream scripts):

    import hashlib, json
    from pathlib import Path

    def _load_upstream(path: Path) -> tuple[dict, dict]:
        raw = path.read_bytes()
        w   = json.loads(raw.decode("utf-8"))
        return w, {
            "path":            path.name,
            "sha256":          hashlib.sha256(raw).hexdigest(),
            "size_bytes":      len(raw),
            "commitSha":       w.get("commitSha"),
            "scriptCommitSha": w.get("scriptCommitSha"),
            "computedAt":      w.get("computedAt"),
        }

    # later, in the output witness dict:
    "derivation_inputs": {
        ...,
        "upstream_witness_hashes": [hash_record_1, hash_record_2, ...],
    }

Usage
─────
    python3 folio-assistant/computations/witness_dependency_drift.py
        # warn-only by default; exit code = number of stale downstreams

    python3 folio-assistant/computations/witness_dependency_drift.py --strict
        # exit code 1 on any drift (suitable for CI)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def _sha256_of(path: Path) -> str | None:
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_witness(witness_path: Path) -> tuple[list[dict], bool]:
    """Return (drift_records, has_deps).

    drift_records is empty when the witness is clean.  has_deps is
    True iff the witness declared `upstream_witness_hashes` (used by
    the caller to count covered witnesses without re-reading the
    file).
    """
    try:
        w = json.loads(witness_path.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        return [{
            "downstream":  witness_path.name,
            "kind":        "unreadable",
            "detail":      str(e),
        }], False
    # Two canonical locations for the hash array:
    #   1. derivation_inputs.upstream_witness_hashes — hand-rolled
    #      witnesses that embed a derivation_inputs block (e.g.
    #      low-isotope-mass-table)
    #   2. data.upstream_witness_hashes — WitnessBuilder-backed
    #      witnesses (the standard slot for builder.add_upstream)
    upstream_hashes = (
        w.get("derivation_inputs", {}).get("upstream_witness_hashes")
        or w.get("data", {}).get("upstream_witness_hashes")
    )
    if not upstream_hashes:
        return [], False  # no declared dependencies, nothing to check
    drifts: list[dict] = []
    for entry in upstream_hashes:
        ups_name = entry.get("path")
        if not ups_name:
            continue
        ups_path = HERE / ups_name
        recorded_sha = entry.get("sha256")
        current_sha = _sha256_of(ups_path)
        if current_sha is None:
            drifts.append({
                "downstream":      witness_path.name,
                "upstream":        ups_name,
                "kind":            "upstream_missing",
                "recorded_sha256": recorded_sha,
                "recorded_at":     entry.get("computedAt"),
            })
        elif current_sha != recorded_sha:
            drifts.append({
                "downstream":      witness_path.name,
                "upstream":        ups_name,
                "kind":            "sha256_mismatch",
                "recorded_sha256": recorded_sha,
                "current_sha256":  current_sha,
                "recorded_at":     entry.get("computedAt"),
            })
    return drifts, True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 on any drift (CI mode)")
    args = parser.parse_args()

    witnesses = sorted(HERE.glob("*.witness.json"))
    n_checked = 0
    n_with_deps = 0
    all_drifts: list[dict] = []
    for w in witnesses:
        n_checked += 1
        drifts, has_deps = check_witness(w)
        if drifts:
            all_drifts.extend(drifts)
        if has_deps:
            n_with_deps += 1

    print(f"Checked {n_checked} witnesses; "
          f"{n_with_deps} declare upstream_witness_hashes; "
          f"{len(all_drifts)} drift records.")
    if all_drifts:
        print("\nDrift detail:")
        for d in all_drifts:
            print(f"  - {d['downstream']} → {d.get('upstream', '?')}: "
                  f"{d['kind']}")
            if "recorded_sha256" in d:
                print(f"      recorded: {d['recorded_sha256']}")
            if "current_sha256" in d:
                print(f"      current:  {d['current_sha256']}")
            if "recorded_at" in d and d["recorded_at"]:
                print(f"      recorded_at: {d['recorded_at']}")

    # Signal failure by default when drifts are detected so CI catches
    # inconsistencies; --strict is preserved for back-compat but yields
    # the same exit code (gemini #663: avoid silent-success regression).
    return 1 if all_drifts else 0


if __name__ == "__main__":
    sys.exit(main())
