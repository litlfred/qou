#!/usr/bin/env python3
"""Categorize the derivation-chain gap into actionable tiers.

`derivation_chain_validator.py` reports ONE number — how many witnesses have no
derivation chain. After the recursive-scan fix (#5269) that number is ~2.6k, which
is true but not actionable: it says nothing about *what kind* of work each witness
needs, and it mixes together objects with entirely different obligations.

This tool splits the gap by the work each witness actually requires:

  A  audit-only ...... the witness declares `auditOnly` / `audit_only` (it records a
                       QA/audit tool's finding, not a derivation of a physical
                       target). Requiring a first-principles chain for the output of
                       a sorry-counter is a category error. EXEMPT — reported
                       separately, never silently dropped.
  B  probe ........... exploratory scope-(a) compute under `probes/`. A chain is
                       meaningful but low priority; these are not production.
  C  family .......... production witness whose producer emits MANY witnesses. One
                       chain claims the whole family (the audit matches by producer
                       BASENAME), so these are the high-yield authoring targets.
  D  singleton ....... production witness with its own producer. Genuinely needs a
                       per-compute chain authored by someone who understands that
                       derivation. This is the irreducible bulk.
  E  orphan .......... no producer script on disk. Provenance is gone; a chain
                       cannot honestly be authored until it is recovered or the
                       witness is retired.

Read-only: prints the tiering and (with --json) emits it for downstream use. It
does not modify witnesses, chains, or the validator's own counts.
"""
from __future__ import annotations

import argparse
import collections
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
#: Repo root. Producers do NOT all live under `computations/` -- some sit in
#: `docs/audits/scripts/`, and some are `.sage` or `.lean` rather than `.py`.
#: Scanning only ROOT for only `*.py` reported those witnesses as tier-E
#: orphans ("provenance is gone") when their producer was on disk the whole
#: time, which is the worst direction for this tool to be wrong in: the
#: recommended disposition for an orphan is to retire it.
REPO = ROOT.parent
#: Extensions a `scriptFile` may legitimately name.
PRODUCER_SUFFIXES = (".py", ".sage", ".lean", ".sh")
AUDIT_WITNESS = "derivation-chain-audit.witness.json"
SCRIPT_RE = re.compile(r"script:\s*([^\s,;]+)")
FAMILY_MIN = 2  # a producer emitting >= this many witnesses is a "family"


def _scan(pattern: str) -> list[pathlib.Path]:
    return sorted(p for p in ROOT.rglob(pattern) if "_deprecated" not in p.parts)


def _referenced_producers() -> set[str]:
    """Producer basenames already claimed by some chain's `script:` note."""
    out: set[str] = set()
    for cp in _scan("*.derivation.json"):
        try:
            data = json.loads(cp.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        for step in data.get("steps", []):
            for m in SCRIPT_RE.finditer(step.get("notes") or ""):
                out.add(pathlib.Path(m.group(1)).name)
    return out


def _guess_producer(witness_name: str, on_disk: set[str] | None = None) -> str:
    """Same convention the validator falls back on: foo-bar.witness.json -> foo_bar.py.

    A witness with no `scriptFile` is guessed by this name convention, and the
    guess used to assume `.py`.  Sage producers (`computations/substrate/*.sage`)
    therefore came back as tier-E orphans with the producer sitting right next to
    the witness.  When `on_disk` is supplied, prefer whichever suffix actually
    exists; fall back to `.py` so the reported name stays stable when none does.
    """
    stem = witness_name.replace(".witness.json", "").replace("-", "_")
    if on_disk:
        for suf in PRODUCER_SUFFIXES:
            if stem + suf in on_disk:
                return stem + suf
    return stem + ".py"


def categorize() -> dict:
    referenced = _referenced_producers()
    # `.claude/worktrees/` holds checkouts of OTHER branches; a producer that
    # exists only there is not on disk for THIS checkout, so it must not count.
    on_disk = {
        p.name
        for suf in PRODUCER_SUFFIXES
        for p in REPO.rglob("*" + suf)
        if ".claude" not in p.parts and "_deprecated" not in p.parts
    }

    records = []
    for wp in _scan("*.witness.json"):
        if wp.name == AUDIT_WITNESS:
            continue
        try:
            data = json.loads(wp.read_text())
        except (json.JSONDecodeError, OSError):
            continue
        if isinstance(data, dict):
            script_file = data.get("scriptFile")
            audit_only = bool(
                data.get("auditOnly") or data.get("audit_only") or data.get("auditOnlyDoc")
            )
        elif isinstance(data, list):
            script_file = next(
                (e.get("scriptFile") for e in data if isinstance(e, dict) and e.get("scriptFile")),
                None,
            )
            audit_only = False
        else:
            continue
        producer = pathlib.Path(script_file).name if script_file else _guess_producer(wp.name, on_disk)
        records.append({
            "witness": str(wp.relative_to(ROOT)),
            "producer": producer,
            "backed": producer in referenced,
            "audit_only": audit_only,
            "producer_on_disk": producer in on_disk,
            "probe": "probes" in wp.parts,
        })

    gap = [r for r in records if not r["backed"]]
    fam_size = collections.Counter(
        r["producer"] for r in gap
        if not r["audit_only"] and r["producer_on_disk"] and not r["probe"]
    )

    tiers: dict[str, list[dict]] = collections.defaultdict(list)
    for r in gap:
        if not r["producer_on_disk"]:
            tier = "E-orphan"
        elif r["audit_only"]:
            tier = "A-audit-only"
        elif r["probe"]:
            tier = "B-probe"
        elif fam_size[r["producer"]] >= FAMILY_MIN:
            tier = "C-family"
        else:
            tier = "D-singleton"
        r["tier"] = tier
        tiers[tier].append(r)

    families = collections.Counter(
        r["producer"] for r in tiers["C-family"]
    )
    return {
        "witnesses_in_scope": len(records),
        "already_backed": len(records) - len(gap),
        "gap_total": len(gap),
        "tier_counts": {k: len(v) for k, v in sorted(tiers.items())},
        "actionable_gap": len(tiers["C-family"]) + len(tiers["D-singleton"]),
        "families_ranked": families.most_common(),
        "tiers": {k: [r["witness"] for r in v] for k, v in tiers.items()},
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true", help="emit the full tiering as JSON")
    ap.add_argument("--tier", help="list the witnesses in one tier")
    args = ap.parse_args()

    res = categorize()
    if args.json:
        print(json.dumps(res, indent=2))
        return 0
    if args.tier:
        for w in res["tiers"].get(args.tier, []):
            print(w)
        return 0

    print(f"witnesses in scope : {res['witnesses_in_scope']}")
    print(f"already backed     : {res['already_backed']}")
    print(f"GAP                : {res['gap_total']}\n")
    labels = {
        "A-audit-only": "audit/tool output — EXEMPT (category error to chain)",
        "B-probe":      "exploratory probe — low priority",
        "C-family":     "production, shared producer — ONE chain drains the family",
        "D-singleton":  "production, own producer — needs per-compute authoring",
        "E-orphan":     "no producer on disk — provenance triage first",
    }
    for tier, n in sorted(res["tier_counts"].items()):
        print(f"  {n:5d}  {tier:14s} {labels.get(tier,'')}")
    print(f"\nACTIONABLE (C+D)   : {res['actionable_gap']}")
    print("\nTop families (witnesses drained per chain authored):")
    for prod, n in res["families_ranked"][:12]:
        print(f"  {n:5d}  {prod}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
