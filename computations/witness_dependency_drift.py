#!/usr/bin/env python3
"""
Witness staleness validator — both directions.

Walks every `*.witness.json` (recursively from this script's dir) and
checks TWO independent staleness directions:

  1. UPSTREAM (transitive): for each witness that declares
     `upstream_witness_hashes`, verify each recorded sha256 against the
     current bytes of the named upstream file. Drift ⇒ an upstream
     changed since this witness was regenerated ⇒ this witness is stale.

  2. SELF: compare each witness's recorded `scriptHash` to the current
     hash of its producer file (resolved from `scriptFile`). Mismatch ⇒
     the producer changed since the witness was generated ⇒ stale, even
     if no upstream witness changed. (Added 2026-06-16 after the
     hadron-knot-table witness sat self-stale on a branch with a
     downstream binding regression that no check caught — see
     docs/audits/2026-06-16-hadron-knot-table-stale-witness-regression.md
     and the closure plan in
     docs/design/2026-06-16-witness-staleness-propagation.md.)

Together these cover the full propagation: a child producer change
flips SELF on that child, and once the child is regenerated its bytes
change, flipping UPSTREAM on every parent that recorded its hash.

Drift means: the witness is stale and must be re-run before its
contents can be trusted.

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
    python3 computations/witness_dependency_drift.py
        # report upstream drift + self-staleness + adoption %.
        # exit 1 on any UPSTREAM drift; self-staleness is WARN-only.

    python3 computations/witness_dependency_drift.py --self-strict
        # also exit 1 on self-staleness (scriptHash drift).

    python3 computations/witness_dependency_drift.py --strict
        # exit 1 on any drift (upstream or self) — full CI gate.

    python3 computations/witness_dependency_drift.py --no-self
        # upstream-only (the pre-2026-06-16 behaviour).
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
    if not isinstance(w, dict):
        # Some *.witness.json files hold a top-level JSON array (data
        # dumps, not builder witnesses) — no dependency block to check.
        return [], False
    # Two canonical locations for the hash array:
    #   1. derivation_inputs.upstream_witness_hashes — hand-rolled
    #      witnesses that embed a derivation_inputs block (e.g.
    #      low-isotope-mass-table)
    #   2. data.upstream_witness_hashes — WitnessBuilder-backed
    #      witnesses (the standard slot for builder.add_upstream)
    # Guard: some witnesses carry `data`/`derivation_inputs` as a LIST
    # (not a dict), so `.get` would raise — treat those as "no deps".
    di = w.get("derivation_inputs")
    dat = w.get("data")
    upstream_hashes = (
        (di.get("upstream_witness_hashes") if isinstance(di, dict) else None)
        or (dat.get("upstream_witness_hashes") if isinstance(dat, dict) else None)
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


def _file_hash12(path: Path) -> str | None:
    """sha256 12-char prefix of a file's bytes (matches WitnessBuilder's
    `file_content_hash`), or None if absent."""
    if not path.exists():
        return None
    return hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def _build_producer_index(roots: list[Path]) -> dict[str, list[Path]]:
    """Map each producer `*.py` basename to the path(s) that bear it.

    Used to resolve a witness's `scriptFile` back to its producer so we
    can recompute the current `scriptHash`. Ambiguous (multi-path) names
    are reported rather than guessed.
    """
    index: dict[str, list[Path]] = {}
    for root in roots:
        if not root.is_dir():
            continue
        for py in root.rglob("*.py"):
            if "_deprecated" in py.parts or "/.lake/" in str(py):
                continue
            index.setdefault(py.name, []).append(py)
    return index


def check_self_staleness(
    witness_path: Path,
    producer_index: dict[str, list[Path]],
) -> dict | None:
    """Compare a witness's recorded `scriptHash` to the current hash of
    its producer file.  A mismatch = the producer changed since the
    witness was last generated (self-staleness) — the witness must be
    re-run.  Returns a record, or None when fresh/unverifiable.

    Producer resolution (#5): when several files share the basename in
    `scriptFile`, prefer the candidate in the SAME directory as the
    witness, then the shallowest path — this resolves most of the
    name-collision "ambiguous" cases instead of giving up.

    This is the complement of `check_witness` (which checks UPSTREAM
    witness edges).  Together they cover both staleness directions:
    self (my producer changed) and transitive (an upstream changed).
    """
    try:
        w = json.loads(witness_path.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    if not isinstance(w, dict):
        return None
    recorded = w.get("scriptHash")
    script_file = w.get("scriptFile")
    if not recorded or not script_file:
        return {"downstream": witness_path.name, "kind": "self_unverifiable",
                "detail": "witness lacks scriptHash/scriptFile"}
    candidates = producer_index.get(script_file, [])
    if len(candidates) == 0:
        return {"downstream": witness_path.name, "kind": "producer_unresolved",
                "scriptFile": script_file}
    producer = _resolve_producer(candidates, witness_path)
    current = _file_hash12(producer)
    if current != recorded:
        return {"downstream": witness_path.name, "kind": "self_stale",
                "scriptFile": script_file, "producer": str(producer),
                "recorded_scriptHash": recorded, "current_scriptHash": current}
    return None


def _resolve_producer(candidates: list[Path], witness_path: Path) -> Path:
    """Pick the most likely producer among same-basename candidates (#5):
    prefer one in the witness's own directory, else the shallowest path."""
    if len(candidates) == 1:
        return candidates[0]
    same_dir = [c for c in candidates if c.parent == witness_path.parent]
    if len(same_dir) == 1:
        return same_dir[0]
    pool = same_dir or candidates
    return min(pool, key=lambda c: (len(c.parts), str(c)))


def _upstream_edges(witness_path: Path) -> list[str]:
    """Return the list of upstream witness basenames this witness records."""
    try:
        w = json.loads(witness_path.read_text())
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []
    if not isinstance(w, dict):
        return []
    di = w.get("derivation_inputs")
    dat = w.get("data")
    arr = (
        (di.get("upstream_witness_hashes") if isinstance(di, dict) else None)
        or (dat.get("upstream_witness_hashes") if isinstance(dat, dict) else None)
        or []
    )
    return [e.get("path") for e in arr if isinstance(e, dict) and e.get("path")]


def _propagate_transitive(
    edges: dict[str, list[str]], directly_stale: set[str]
) -> set[str]:
    """Close `directly_stale` upward over the edge DAG: a node is stale if
    any upstream it records is (directly or transitively) stale. Memoised
    DFS with cycle guard."""
    memo: dict[str, bool] = {}

    def stale(node: str, seen: frozenset) -> bool:
        if node in memo:
            return memo[node]
        if node in directly_stale:
            memo[node] = True
            return True
        if node in seen:  # cycle — don't recurse
            return False
        res = any(stale(up, seen | {node}) for up in edges.get(node, []))
        memo[node] = res
        return res

    return {n for n in edges if stale(n, frozenset())}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 on any upstream OR self drift (CI gate)")
    parser.add_argument("--self-strict", action="store_true",
                        help="exit 1 on self-staleness too (else warn-only)")
    parser.add_argument("--no-self", action="store_true",
                        help="skip the self-staleness (scriptHash) check")
    args = parser.parse_args()

    witnesses = sorted(HERE.rglob("*.witness.json"))
    repo_root = HERE.parent
    producer_index = (
        {} if args.no_self
        else _build_producer_index([HERE, repo_root / "tools"])
    )

    n_checked = n_with_deps = 0
    all_drifts: list[dict] = []
    self_records: list[dict] = []
    edges: dict[str, list[str]] = {}      # witness name -> upstream names
    directly_stale: set[str] = set()      # self-stale OR has upstream drift
    for w in witnesses:
        n_checked += 1
        drifts, has_deps = check_witness(w)
        all_drifts.extend(drifts)
        if has_deps:
            n_with_deps += 1
        if drifts:
            directly_stale.add(w.name)
        edges[w.name] = _upstream_edges(w)
        if not args.no_self:
            rec = check_self_staleness(w, producer_index)
            if rec is not None:
                self_records.append(rec)
                if rec["kind"] == "self_stale":
                    directly_stale.add(w.name)

    # #6 — transitive (Merkle-style) propagation: a witness is stale if any
    # upstream it records is itself (directly or transitively) stale, even
    # when its own recorded hashes still match. One memoised pass over the
    # on-disk DAG; only as deep as the recorded `upstream_witness_hashes`.
    transitively_stale = _propagate_transitive(edges, directly_stale)
    n_transitive_only = len(transitively_stale - directly_stale)

    n_self_stale = sum(1 for r in self_records if r["kind"] == "self_stale")
    pct = (100.0 * n_with_deps / n_checked) if n_checked else 0.0
    print(f"Checked {n_checked} witnesses.")
    print(f"  upstream edges:   {n_with_deps} declare upstream_witness_hashes "
          f"({pct:.1f}% adoption); {len(all_drifts)} drift records.")
    if not args.no_self:
        print(f"  self-staleness:   {n_self_stale} self-stale "
              f"(scriptHash != current producer); "
              f"{len(self_records) - n_self_stale} unverifiable/unresolved.")
    print(f"  transitive:       {n_transitive_only} additionally stale via "
          f"upstream propagation (recorded edges only).")

    if all_drifts:
        print("\nUpstream drift detail:")
        for d in all_drifts:
            print(f"  - {d['downstream']} → {d.get('upstream', '?')}: {d['kind']}")
            if "recorded_sha256" in d:
                print(f"      recorded: {d['recorded_sha256']}")
            if "current_sha256" in d:
                print(f"      current:  {d['current_sha256']}")
    if n_self_stale:
        print("\nSelf-stale detail (producer changed since witness generated):")
        for r in self_records:
            if r["kind"] == "self_stale":
                print(f"  - {r['downstream']} (producer {r['scriptFile']}): "
                      f"{r['recorded_scriptHash']} -> {r['current_scriptHash']}")

    # Exit semantics: upstream drift fails by default (existing CI contract,
    # gemini #663). Self-staleness is WARN-only unless --self-strict / --strict,
    # because self-staleness is widespread until adoption + regeneration catch
    # up, and we don't want to red-wall every PR on day one.
    fail = bool(all_drifts) or (bool(n_self_stale) and (args.self_strict or args.strict))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
