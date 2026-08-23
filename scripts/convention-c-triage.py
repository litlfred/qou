#!/usr/bin/env python3
"""Triage the live convention-C sites into what may be migrated by machine.

The owner ruling (2026-08-15, reaffirmed 2026-08-23) is that convention D is
canonical and C is excised.  `convention-c-producer-audit.py` FINDS the sites and
`convention-c-producer-migrate.py` REWRITES them.  This script sits between: it
says, per site, whether a rewrite is a mechanical convention fix or a change to
recorded mathematics that needs a human.

Written after measuring that the automated path was 0-for-2 on the decay channel
(`computations/qbeta/qbeta_convention_c_migration_safety_probe.py`): one rewrite
broke a passing probe, the other silently moved 14 fields of a committed witness
while still exiting 0.  Both are now refused by guards G1/G2 in the migrate
script.  This extends the same reasoning to the rest of the corpus.

## The four blocking signals, in priority order

  B1  BLOCKED PATH.  Not ours to rewrite:
        * `tools/pyhecke/`           — registry `blocked_migrations`
        * `qou-mass/**/_internal/`   — GENERATED; edit the source and re-sync
                                       via scripts/sync-qou-mass-vendor.py
        * `q_pinning_50_digit.py`    — writes the ANCHOR-DEFINING witness;
                                       AGENTS rule 1 forbids re-pinning it
  B2  LADDER PHASE (migrate G2).  The bound name feeds `(z-1)*h/2`.  Substituting
      z_D there is the move `decayLadder_zC_threeRow_ne_zero` proves is not a
      migration — the ladder must be RE-DERIVED.
  B3  DELIBERATE COMPARISON (migrate G1).  The file references a C-named symbol,
      so the C value is probably an instrument, not a defect.
  B4  EMITS A COMMITTED WITNESS.  Rewriting changes numbers that are checked in.
      Not forbidden, but it is a value change and must be re-run, diffed and
      justified — never applied in a sweep.
  B4t TRANSITIVELY EMITS ONE.  The file itself writes no witness, but a module
      that IMPORTS it does.  Added after this script's first run called two
      sites MECHANICAL that are not: `per_braid_tower.py` and
      `substrate/hecke_core_symbolic.py` write no witness of their own, yet 5 of
      their 6 importers do.  A file-local witness test has exactly the
      import-cone blind spot AGENTS.md documents for witness staleness, and it
      had it here.  One hop is checked; deeper cones are not, so a MECHANICAL
      verdict remains a floor, not a guarantee.

A site with none of the four is MECHANICAL: a convention choice with no recorded
consequence, safe for `--apply`.

## What this is not

It is not a verdict that the MECHANICAL set is correct to migrate — only that
migrating it cannot silently change a committed number or break an instrument.
And a `B4` is a work item, not a refusal: those are the ones that actually carry
the excision, one at a time.

Usage:
    python3 scripts/convention-c-triage.py
    python3 scripts/convention-c-triage.py --json out.json
"""
from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parents[1]

BLOCKED_PATHS = (
    ("tools/pyhecke/", "registry blocked_migrations"),
    ("_internal/", "GENERATED — re-sync via scripts/sync-qou-mass-vendor.py"),
)
BLOCKED_FILES = {
    "computations/q_pinning_50_digit.py":
        "writes the ANCHOR-DEFINING witness — AGENTS rule 1, never re-pin",
}

WITNESS_MARKERS = re.compile(
    r"WitnessBuilder|witness\.json|add_parameter\(|add_assertion\(|write_witness",
)


def _importers(module_stem: str) -> list[str]:
    """One-hop: live .py files importing `module_stem`."""
    pat = re.compile(rf"^\s*(from|import)\s+.*\b{re.escape(module_stem)}\b", re.M)
    hits = []
    for p in REPO.rglob("*.py"):
        rel = str(p.relative_to(REPO))
        if "_deprecated" in rel or rel.endswith(f"/{module_stem}.py") \
                or ".lake" in rel or rel.startswith(".git"):
            continue
        try:
            if pat.search(p.read_text()):
                hits.append(rel)
        except Exception:
            continue
    return hits


def _importer_emits_witness(module_stem: str) -> list[str]:
    """Importers of `module_stem` that themselves emit a committed witness."""
    out = []
    for rel in _importers(module_stem):
        try:
            if WITNESS_MARKERS.search((REPO / rel).read_text()):
                out.append(rel)
        except Exception:
            continue
    return out


def _load(name: str, fname: str):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / fname)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def triage(recs, migrate):
    out = []
    for r in recs:
        path, target = r["path"], r["target"]
        reasons = []

        for pref, why in BLOCKED_PATHS:
            if pref in path:
                reasons.append(("B1", why))
                break
        if path in BLOCKED_FILES:
            reasons.append(("B1", BLOCKED_FILES[path]))

        src_path = REPO / path
        try:
            src = src_path.read_text()
            tree = ast.parse(src)
        except Exception:
            out.append({**r, "klass": "UNREADABLE", "reasons": ["could not parse"]})
            continue

        if target in migrate._ladder_phase_targets(tree):
            reasons.append(("B2", "feeds the ladder phase (z-1)*h/2 — re-derivation"))
        if r.get("deliberate") or migrate._file_has_c_reference(tree):
            reasons.append(("B3", "file references a C-named symbol — comparison"))
        if WITNESS_MARKERS.search(src):
            reasons.append(("B4", "emits a committed witness — value change"))
        else:
            downstream = _importer_emits_witness(src_path.stem)
            if downstream:
                shown = ", ".join(downstream[:3])
                more = f" (+{len(downstream) - 3} more)" if len(downstream) > 3 else ""
                reasons.append(("B4t",
                                f"imported by witness-emitting {shown}{more}"))

        klass = "MECHANICAL" if not reasons else reasons[0][0]
        out.append({**r, "klass": klass,
                    "reasons": [f"{c}: {w}" for c, w in reasons]})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    args = ap.parse_args()

    tmp = REPO / ".tmp-c-sites.json"
    subprocess.run(
        [sys.executable, str(REPO / "scripts" / "convention-c-producer-audit.py"),
         "--json", str(tmp)],
        cwd=REPO, capture_output=True,
    )
    recs = json.loads(tmp.read_text())
    tmp.unlink(missing_ok=True)

    migrate = _load("ccpm", "convention-c-producer-migrate.py")
    rows = triage(recs, migrate)

    order = ["MECHANICAL", "B4t", "B4", "B3", "B2", "B1", "UNREADABLE"]
    label = {
        "MECHANICAL": "MECHANICAL — safe for --apply (no witness, no phase, no comparison)",
        "B4": "B4 EMITS A COMMITTED WITNESS — value change, one at a time",
        "B4t": "B4t TRANSITIVELY EMITS ONE — an importer writes a witness",
        "B3": "B3 DELIBERATE COMPARISON — leave it; it measures the excision",
        "B2": "B2 LADDER PHASE — re-derivation, not substitution (qou-cds1)",
        "B1": "B1 BLOCKED PATH — not ours to rewrite",
        "UNREADABLE": "UNREADABLE",
    }
    for k in order:
        grp = [r for r in rows if r["klass"] == k]
        if not grp:
            continue
        print(f"\n{'=' * 74}\n{label[k]}  ({len(grp)})\n{'=' * 74}")
        for r in grp:
            print(f"  {r['path']}:{r['line']}  {r['target']}")
            for why in r["reasons"]:
                print(f"      {why}")

    print(f"\n{'=' * 74}\nSUMMARY")
    for k in order:
        n = sum(1 for r in rows if r["klass"] == k)
        if n:
            print(f"  {k:<12} {n:>4}")
    mech = sum(1 for r in rows if r["klass"] == "MECHANICAL")
    print(f"\n  machine-migratable now : {mech}")
    print(f"  needs a human          : {len(rows) - mech}")

    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(
            {"schema": "convention-c-triage/v1", "records": rows}, indent=2))
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
