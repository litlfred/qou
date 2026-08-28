#!/usr/bin/env python3
"""Partition the `Q0_ANCHOR_MISSING` population by CAUSE, not by count.

`audits/q0_anchor_consistency_audit.py` reports *how many* witnesses carry no
top-level ``q0Anchor``. It deliberately does not fail on them --- its own header
calls ``Q0_ANCHOR_MISSING`` "pre-backfill; not a failure", and ``--strict`` exits
non-zero only on ``Q0_FLIP``. That is the right call for a *contradiction*
detector, but it means the missing population has never been attributed: a count
that mixes four unrelated defects cannot tell you which one to fix, and a drain
of any one of them is invisible against the other three.

This script answers the other question: *why* is each one unstamped?

The stamping contract, as implemented
-------------------------------------
``WitnessBuilder.build()`` writes ``q0Anchor`` in exactly two situations:

1. the producer put it in the payload itself (``w.save({"q0Anchor": ...})``); or
2. the producer's **stem is positively declared** in
   ``computations/q0_anchor_manifest.json`` (or ``QOU_Q0_ANCHOR`` is set).

Case 2 is the one that surprises people. Using ``WitnessBuilder`` is *not*
sufficient: an undeclared producer is left unstamped **on purpose**, because
defaulting a pin in would assert a pin nobody established. So "uses the
builder" and "gets stamped" are different properties, and the gap between them
is a cause class in its own right.

Cause classes emitted
---------------------
``NO_PRODUCER``      no ``.py`` in the tree mentions this witness name. Nothing
                     can re-stamp it; it is an orphan and needs a producer or a
                     deletion, not a re-run.
``NOT_BUILDER``      a producer exists but writes its JSON by hand
                     (``json.dump`` / ``write_text``) without going through
                     ``WitnessBuilder``. The stamping code never executes.
``UNDECLARED``       producer uses the builder, but its stem is absent from the
                     manifest, so the builder declines to stamp. **This is the
                     class the refill runs through.**
``DECLARED_STALE``   producer uses the builder AND is declared --- so a re-run
                     would stamp it. The committed witness simply predates the
                     declaration and has not been re-run.
``GENERATED_MIRROR`` lives in a generated tree (e.g. ``qou-mass/_internal``);
                     never hand-edit, fix the source instead.

Every class is reported with its count and a sample, so a drain can be scoped to
one cause and measured against that cause's denominator rather than the total.

Usage
-----
    python3 computations/audits/q0_anchor_missing_cause_partition.py
    python3 computations/audits/q0_anchor_missing_cause_partition.py --json out.json
    python3 computations/audits/q0_anchor_missing_cause_partition.py --rev origin/main

``--rev`` reads the tree out of git rather than the working directory, so a
producer run in progress cannot contaminate the measurement.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# Suffixes the consistency audit exempts: witnesses emitted BY audits, whose
# subject is the anchor bookkeeping itself.
#
# IMPORTED from the consistency audit rather than restated. A hand-copied list
# drifts, and the drift is silent: an earlier draft of this file guessed
# ``("-audit", "-status")`` and reported 1689 unstamped against the audit's
# 1678 --- an 11-witness disagreement between two scripts that are supposed to
# be measuring the same population, which reads as a real finding rather than
# as a copy that fell behind.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from q0_anchor_consistency_audit import AUDIT_SUFFIXES  # noqa: E402

# Trees that are generated from a source elsewhere. Never hand-edit these.
GENERATED_PREFIXES = ("qou-mass/src/qou_mass/_internal/",)

_BUILDER_HINTS = (
    "WitnessBuilder",
    "qou_substrate.witness",
    "witness_base",
    "from witness import",
    "import witness",
    "build_witness",
)
_HANDROLL_HINTS = ("json.dump", "write_text", "json.dumps")


def _run(cmd: list[str]) -> str:
    return subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(REPO), check=True
    ).stdout


def _witness_paths(rev: str | None) -> list[str]:
    if rev:
        out = _run(["git", "ls-tree", "-r", "--name-only", rev, "computations/"])
        return [p for p in out.splitlines() if p.endswith(".witness.json")]
    return sorted(
        str(p.relative_to(REPO))
        for p in (REPO / "computations").rglob("*.witness.json")
    )


def _read(path: str, rev: str | None) -> str | None:
    if rev:
        r = subprocess.run(
            ["git", "show", f"{rev}:{path}"],
            capture_output=True,
            text=True,
            cwd=str(REPO),
        )
        return r.stdout if r.returncode == 0 else None
    p = REPO / path
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return None


def _load_manifest() -> set[str]:
    """Stems the manifest positively declares (any bucket)."""
    try:
        man = json.loads(
            (REPO / "computations" / "q0_anchor_manifest.json").read_text(
                encoding="utf-8"
            )
        )
    except (OSError, json.JSONDecodeError):
        return set()
    declared: set[str] = set()
    for key in ("ideal_muon", "physical_proton", "ambiguous"):
        v = man.get(key)
        if isinstance(v, list):
            declared.update(str(x) for x in v)
    return declared


def _index_producers() -> dict[str, list[Path]]:
    """Map witness base name -> producer scripts that mention it.

    A producer names its witness in the ``WitnessBuilder(name=...)`` call (or in
    a hand-rolled output path), so a literal search for the base name is a
    reliable and cheap join. Indexed once rather than grepped per witness: the
    per-witness form is ~2000 greps over ~3000 files.
    """
    index: dict[str, list[Path]] = defaultdict(list)
    roots = [REPO / "computations", REPO / "tools", REPO / "scripts"]
    name_re = re.compile(r"[\"']([A-Za-z0-9][A-Za-z0-9._-]{3,})[\"']")
    for root in roots:
        if not root.is_dir():
            continue
        for py in root.rglob("*.py"):
            if "_deprecated" in py.parts:
                continue
            try:
                src = py.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for m in name_re.finditer(src):
                tok = m.group(1)
                if tok.endswith(".witness.json"):
                    tok = tok[: -len(".witness.json")]
                index[tok].append(py)
    return index


def _classify_producer(py: Path) -> str:
    try:
        src = py.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "NOT_BUILDER"
    if any(h in src for h in _BUILDER_HINTS):
        return "BUILDER"
    if any(h in src for h in _HANDROLL_HINTS):
        return "HANDROLL"
    return "NOT_BUILDER"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rev", help="read the tree at this git rev instead of the "
                                  "working directory")
    ap.add_argument("--json", dest="json_out", help="write the full partition here")
    ap.add_argument("--sample", type=int, default=6,
                    help="paths to show per cause class (default 6)")
    ap.add_argument("--include-deprecated", action="store_true",
                    help="also scan computations/_deprecated/. OFF by default, "
                         "to match q0_anchor_consistency_audit.py, which skips "
                         "it (line 280). A raw `computations/**` count is "
                         "therefore LARGER than the audit's Q0_ANCHOR_MISSING "
                         "for reasons that have nothing to do with stamping.")
    args = ap.parse_args()

    declared = _load_manifest()
    if not declared:
        print("WARNING: q0_anchor_manifest.json unreadable or empty — every "
              "producer will classify UNDECLARED.", file=sys.stderr)

    paths = _witness_paths(args.rev)
    if not args.include_deprecated:
        paths = [p for p in paths if "_deprecated" not in Path(p).parts]
    index = _index_producers()

    unstamped: list[str] = []
    stamped = 0
    exempt = 0
    for p in paths:
        if any(p.endswith(s) for s in AUDIT_SUFFIXES):
            exempt += 1
            continue
        raw = _read(p, args.rev)
        if raw is None:
            continue
        try:
            body = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not isinstance(body, dict):
            continue
        if body.get("q0Anchor"):
            stamped += 1
        else:
            unstamped.append(p)

    causes: dict[str, list[str]] = defaultdict(list)
    producer_of: dict[str, str] = {}
    for w in unstamped:
        if any(w.startswith(g) for g in GENERATED_PREFIXES):
            causes["GENERATED_MIRROR"].append(w)
            continue
        base = Path(w).name[: -len(".witness.json")]
        cands = index.get(base, [])
        if not cands:
            causes["NO_PRODUCER"].append(w)
            continue
        # Prefer a candidate that looks like a builder-using producer; a witness
        # is often mentioned by consumers too, and a consumer must not be
        # reported as the thing that failed to stamp.
        kinds = {c: _classify_producer(c) for c in cands}
        pick = next((c for c in cands if kinds[c] == "BUILDER"), None)
        if pick is None:
            pick = next((c for c in cands if kinds[c] == "HANDROLL"), cands[0])
        producer_of[w] = str(pick.relative_to(REPO))
        if kinds[pick] != "BUILDER":
            causes["NOT_BUILDER"].append(w)
        elif pick.stem in declared:
            causes["DECLARED_STALE"].append(w)
        else:
            causes["UNDECLARED"].append(w)

    total = len(unstamped)
    print(f"witnesses scanned      {len(paths)}")
    print(f"  audit-exempt         {exempt}")
    print(f"  stamped              {stamped}")
    print(f"  UNSTAMPED            {total}")
    print()
    print("cause partition of the unstamped population")
    print("-" * 62)
    order = ["UNDECLARED", "NOT_BUILDER", "NO_PRODUCER", "DECLARED_STALE",
             "GENERATED_MIRROR"]
    for k in order:
        v = causes.get(k, [])
        pct = f"{100 * len(v) / total:5.1f}%" if total else "  n/a"
        print(f"  {k:18s} {len(v):5d}  {pct}")
        for s in v[: args.sample]:
            prod = producer_of.get(s, "—")
            print(f"        {s}")
            print(f"            producer: {prod}")
    leftover = set(causes) - set(order)
    for k in sorted(leftover):
        print(f"  {k:18s} {len(causes[k]):5d}")

    # How concentrated is UNDECLARED? A handful of prolific producers would mean
    # a different fix than a long tail.
    und = Counter(producer_of.get(w, "?") for w in causes.get("UNDECLARED", []))
    print()
    print(f"UNDECLARED spans {len(und)} distinct producers; top 10 by witness count:")
    for prod, n in und.most_common(10):
        print(f"    {n:4d}  {prod}")

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(
                {
                    "rev": args.rev or "working-tree",
                    "totals": {
                        "scanned": len(paths),
                        "exempt": exempt,
                        "stamped": stamped,
                        "unstamped": total,
                    },
                    "causes": {k: causes.get(k, []) for k in order},
                    "producer_of": producer_of,
                },
                indent=2,
            ),
            encoding="utf-8",
        )
        print(f"\nwrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
