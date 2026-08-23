#!/usr/bin/env python3
"""Split the hardcoded-q0 literal SITES into defects and non-defects.

WHY THIS EXISTS
---------------
`hardcoded_q0_literal_families_audit.py` counts SITES and says so itself, in
its own `caveat_not_split_source_vs_doc`:

    "This count is SITES, not defects. ... The predecessor CODATA sweep made
     exactly this mistake and had to correct itself: its 'code that computes a
     wrong number' bullet was 'wrong for 87 % of its own count'. Do not quote
     65 as a defect count. The split is the next step."

This is that step. It does not re-scan: it reuses the families audit's own
`scan()`, so the two can never disagree about WHICH sites exist -- only about
what each one MEANS, which is the ledger's job.

THE FOUR CLASSES
----------------
  a  CODE THAT COMPUTES     the literal feeds arithmetic, or is published as a
                            q0 into a witness.  The real defects.
  b  DELIBERATE CLASSIFIER  the code must NAME a specific, superseded or
                            held-fixed value in order to detect, compare
                            against, or reproduce it.  MIGRATING ONE BREAKS
                            THE DETECTOR -- e.g. `MUON_OLD` in
                            q0_muon_population_partition.py, whose entire job
                            is to separate the two muon populations.  These
                            belong in the audit's EXCLUSION set, never in a
                            migration batch.
  c  DOCUMENTATION          docstring / comment only.
  d  TEST FIXTURE           a pinned expected value; migrating makes the
                            assertion tautological.

WHAT IT CHECKS
--------------
1. Every live divergent site is classified.  A new transcription cannot land
   unnoticed: it has no ledger row, and this exits 1.
2. Every ledger row still matches a live site.  A stale row (site migrated or
   deleted) is reported so the ledger drains with the corpus.
3. `class_counts` / `substate_counts` in the ledger agree with the entries.

Usage:
    python3 computations/audits/q0_literal_classification_audit.py
    python3 ... --strict     # exit 1 on any unclassified or orphan row

Output:
    computations/audits/q0-literal-classification.witness.json
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
import _path_bridge  # noqa: E402, F401

sys.path.insert(0, str(HERE.parents[1] / "tools" / "qou-substrate" / "python"))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

from hardcoded_q0_literal_families_audit import scan  # noqa: E402

_T0 = time.monotonic()

LEDGER = HERE / "q0-literal-classification.json"

#: The classes a ledger row may carry.
_CLASSES = ("a", "b", "c", "d")
#: Sub-states, meaningful only for class (a).
_SUBSTATES = ("a-migrated", "a-blocked")


def live_sites() -> set[tuple[str, str]]:
    """(file, literal) for every DIVERGENT site, from the families audit."""
    fams = scan()["families"]
    return {(e["file"], e["literal"])
            for at, entries in fams.items() if at is not None
            for e in entries}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on unclassified sites or orphan ledger rows")
    args = ap.parse_args(argv)

    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    rows = ledger["entries"]

    keyed: dict[tuple[str, str], dict] = {}
    dupes = []
    for r in rows:
        k = (r["file"], r["literal"])
        if k in keyed:
            dupes.append(k)
        keyed[k] = r

    live = live_sites()
    unclassified = sorted(live - set(keyed))
    orphans = sorted(set(keyed) - live)

    bad_class = [r for r in rows if r.get("class") not in _CLASSES]
    bad_sub = [r for r in rows
               if (r.get("class") == "a" and r.get("substate") not in _SUBSTATES)
               or (r.get("class") != "a" and "substate" in r)]
    no_reason = [r for r in rows if not r.get("reason", "").strip()]

    counts = Counter(r["class"] for r in rows)
    subs = Counter(r["substate"] for r in rows if r.get("class") == "a")

    print("=" * 78)
    print("Hardcoded-q0 literals: SITES split into defects and non-defects")
    print("=" * 78)
    print(f"  live divergent sites : {len(live)}")
    print(f"  ledger rows          : {len(rows)}")
    print()
    labels = {"a": "code that computes  (DEFECTS)",
              "b": "deliberate classifier constant",
              "c": "documentation / docstring / comment",
              "d": "test fixture"}
    for c in _CLASSES:
        print(f"    ({c}) {labels[c]:<38} {counts.get(c, 0):>3}")
    for s in _SUBSTATES:
        print(f"         └ {s:<36} {subs.get(s, 0):>3}")
    print()
    print(f"  DEFECT COUNT (class a)          : {counts.get('a', 0)} "
          f"of {len(rows)} sites")
    print(f"  NON-DEFECTS (b + c + d)         : "
          f"{sum(counts.get(c, 0) for c in 'bcd')}")

    for name, items in (("UNCLASSIFIED live sites", unclassified),
                        ("ORPHAN ledger rows", orphans),
                        ("DUPLICATE ledger keys", dupes)):
        if items:
            print(f"\n  {name}: {len(items)}")
            for f, lit in items[:12]:
                print(f"      {f}  {lit[:34]}…")
            if len(items) > 12:
                print(f"      … and {len(items) - 12} more")

    ok_complete = not unclassified
    ok_no_orphans = not orphans
    ok_shape = not (bad_class or bad_sub or no_reason or dupes)
    ok_counts = (dict(counts) | {"total": len(rows)}) == ledger["class_counts"] \
        and dict(subs) == ledger["substate_counts"]

    assertions = [
        {"name": "1_every_live_site_is_classified", "passed": ok_complete,
         "detail": f"{len(unclassified)} live divergent site(s) carry no ledger "
                   "row. A new transcription cannot land silently: it lands "
                   "here as unclassified."},
        {"name": "2_no_orphan_ledger_rows", "passed": ok_no_orphans,
         "detail": f"{len(orphans)} ledger row(s) no longer match a live site. "
                   "Expected transiently while a migration lands; drain them in "
                   "the same commit so the ledger shrinks with the corpus."},
        {"name": "3_every_row_is_well_formed", "passed": ok_shape,
         "detail": f"class in {_CLASSES}, substate in {_SUBSTATES} iff class a, "
                   f"non-empty reason, unique key. Offenders: "
                   f"{len(bad_class)} class, {len(bad_sub)} substate, "
                   f"{len(no_reason)} reason, {len(dupes)} duplicate."},
        {"name": "4_declared_counts_match_entries", "passed": ok_counts,
         "detail": f"entries give {dict(counts)} / {dict(subs)}; ledger declares "
                   f"{ledger['class_counts']} / {ledger['substate_counts']}."},
    ]
    all_passed = all(a["passed"] for a in assertions)

    payload = {
        "computation_method": (
            "Reuses hardcoded_q0_literal_families_audit.scan() -- it does NOT "
            "re-scan, so the two audits cannot disagree about which sites "
            "exist. Joins the live divergent set against the committed ledger "
            "q0-literal-classification.json on (file, literal) and checks "
            "completeness, orphans, row shape and declared counts. Pure string "
            "and set work; no arithmetic, no float64."),
        "description": (
            "The defect/non-defect split the families audit's own "
            "`caveat_not_split_source_vs_doc` asks for. Of its divergent SITES, "
            "only class (a) -- the literal feeds arithmetic or is published as "
            "a q0 -- are defects. Class (b) constants must NOT be migrated: the "
            "code names a superseded or held-fixed value in order to detect or "
            "reproduce it, and re-pinning one breaks the detector."),
        "audit_only": True,
        "tier": "empirical",
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "Reads no substrate value as an input. It joins two string sets and "
            "computes nothing from any q0."),
        "scope": (
            "scope-(a) MEASUREMENT plus a curated ledger. It classifies; it "
            "changes no literal and asserts nothing about which value a "
            "producer SHOULD carry -- that is the A-vs-C anchor question, an "
            "owner matter (ruled 2026-08-22, landing in PR #5500)."),
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "live_divergent_sites": len(live),
            "ledger_rows": len(rows),
            "class_counts": dict(counts),
            "substate_counts": dict(subs),
            "defect_count_class_a": counts.get("a", 0),
            "non_defect_count_bcd": sum(counts.get(c, 0) for c in "bcd"),
            "unclassified": [{"file": f, "literal": l} for f, l in unclassified],
            "orphans": [{"file": f, "literal": l} for f, l in orphans],
            "never_migrate_class_b": sorted(
                {r["file"] for r in rows if r["class"] == "b"}),
            "verdict": (
                "Quoting the families audit's divergent total as a defect count "
                "overstates it. The non-(a) classes are not tidiness debt: a "
                "class-(b) constant is load-bearing precisely BECAUSE it is a "
                "superseded value, and migrating one silently disables the "
                "check it powers."),
        },
        "context": {
            "parent_audit": "computations/audits/hardcoded_q0_literal_families_audit.py",
            "ledger": "computations/audits/q0-literal-classification.json",
            "beans": ["qou-o922", "qou-bred"],
            "anchor_ruling": (
                "Owner, 2026-08-22 (PR #5500): 'A --> CODATA 2022'. The families "
                "audit measures divergence against A, which that PR replaces "
                "with C = q_muon_at(). The char-13 family here is B (CODATA "
                "2018), which #5500 declares out of its own scope. So the "
                "DESTINATION of a class-(a) migration is in motion, which is why "
                "most class-(a) rows are `a-blocked` rather than fixed here: "
                "reading the anchor is right under A and under C, but retyping "
                "either is right under neither for long."),
        },
    }
    b = WitnessBuilder.wrap_legacy(
        "q0-literal-classification", payload, script_path=__file__,
        engine="python", output_dir=HERE, start_time=_T0)
    out = b.save()
    print(f"\nwitness -> {out}")

    if args.strict and not (ok_complete and ok_no_orphans and ok_shape):
        print("STRICT: ledger is not in sync with the live divergent set",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
