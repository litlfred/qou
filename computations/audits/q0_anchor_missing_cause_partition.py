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

The converse also bites, and is measured here as ``INERT_DECLARATION``: a
manifest entry on a producer that hand-rolls its JSON can never fire, because
the code that reads the manifest lives inside ``build()``.

Cause classes emitted
---------------------
``NO_PRODUCER``      no ``.py`` in the tree mentions this witness name. Nothing
                     can re-stamp it; it needs a producer or a deletion, not a
                     re-run.
``NOT_BUILDER``      a producer exists but writes its JSON by hand
                     (``json.dump`` / ``write_text``) without going through
                     ``WitnessBuilder``. The stamping code never executes.
``INERT_DECLARATION`` the same, EXCEPT the stem *is* declared in the manifest ---
                     so the declaration reads as done and does nothing. Split out
                     from ``NOT_BUILDER`` because it is the actively misleading
                     subset: a reader checking the manifest concludes the
                     producer is handled.
``UNDECLARED``       producer uses the builder, but its stem is absent from the
                     manifest, so the builder declines to stamp. **This is the
                     class the refill runs through.**
``DECLARED_STALE``   producer uses the builder AND is declared --- so a re-run
                     would stamp it. The committed witness simply predates the
                     declaration and has not been re-run.
``GENERATED_MIRROR`` lives in a generated tree (e.g. ``qou-mass/_internal``);
                     never hand-edit, fix the source instead.

Reads from git, not from the working tree
-----------------------------------------
Everything --- witnesses, producer sources, and the manifest --- is read at a
single named revision via ``git archive``. This is not fastidiousness: this repo
is worked by several agents at once, and a shared checkout can be switched to
another branch mid-measurement. That happened while this script was being
written, silently changing the manifest from 410 declared stems to 728 between
two reads and invalidating a partition computed in between. A rev-pinned
measurement is reproducible by anyone who names the same rev; a working-tree one
is not reproducible even by its own author.

Usage
-----
    python3 computations/audits/q0_anchor_missing_cause_partition.py
    python3 computations/audits/q0_anchor_missing_cause_partition.py --rev origin/main
    python3 computations/audits/q0_anchor_missing_cause_partition.py --json out.json
"""

from __future__ import annotations

import argparse
import io
import json
import re
import subprocess
import sys
import tarfile
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]

# Trees generated from a source elsewhere. Never hand-edit these.
GENERATED_PREFIXES = ("qou-mass/src/qou_mass/_internal/",)

# Suffixes the consistency audit exempts: witnesses emitted BY audits, whose
# subject is the anchor bookkeeping itself.
#
# IMPORTED from that audit rather than restated. A hand-copied list drifts, and
# the drift is silent: an earlier draft guessed ``("-audit", "-status")`` and
# reported 1689 unstamped against the audit's 1678 --- an 11-witness
# disagreement between two scripts measuring the same population, which reads as
# a finding rather than as a copy that fell behind.
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from q0_anchor_consistency_audit import AUDIT_SUFFIXES
except ImportError:  # running the file from outside the audits/ dir
    AUDIT_SUFFIXES = (
        "-audit.witness.json",
        "-scan.witness.json",
        "-compliance.witness.json",
    )

_BUILDER_HINTS = (
    "WitnessBuilder",
    "qou_substrate.witness",
    "witness_base",
    "build_witness",
)

# Which subtrees to read out of git. `library/` is ~20 GB of ingested sources
# and holds no producers; naming the roots keeps the archive stream small.
_ROOTS = ("computations/", "tools/", "scripts/")


def _archive(rev: str, paths: tuple[str, ...]):
    """Yield (name, bytes) for every file in `paths` at `rev`."""
    p = subprocess.Popen(
        ["git", "archive", "--format=tar", rev, *paths],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        cwd=str(REPO),
    )
    with tarfile.open(fileobj=p.stdout, mode="r|") as tf:
        for m in tf:
            if m.isfile():
                f = tf.extractfile(m)
                if f is not None:
                    yield m.name, f.read()
    p.wait()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rev", default="HEAD",
                    help="git revision to measure (default HEAD). The tree is "
                         "read from git, so the working directory is never "
                         "consulted and a concurrent branch switch cannot "
                         "corrupt the result.")
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

    sha = subprocess.run(["git", "rev-parse", "--short", args.rev],
                         capture_output=True, text=True, cwd=str(REPO)).stdout.strip()

    witnesses: dict[str, bytes] = {}
    sources: dict[str, bytes] = {}
    manifest_raw: bytes | None = None
    for name, body in _archive(args.rev, _ROOTS):
        if name.endswith(".witness.json"):
            witnesses[name] = body
        elif name.endswith(".py"):
            if "_deprecated" not in Path(name).parts:
                sources[name] = body
        elif name.endswith("q0_anchor_manifest.json"):
            manifest_raw = body

    declared: set[str] = set()
    if manifest_raw:
        man = json.loads(manifest_raw)
        for key in ("ideal_muon", "physical_proton", "ambiguous"):
            v = man.get(key)
            if isinstance(v, list):
                declared.update(str(x) for x in v)

    # Producer index: witness base name -> scripts that mention it. A producer
    # names its witness in the WitnessBuilder(name=...) call or in a hand-rolled
    # output path, so a literal search is a reliable and cheap join.
    index: dict[str, list[str]] = defaultdict(list)
    uses_builder: dict[str, bool] = {}
    name_re = re.compile(rb"[\"']([A-Za-z0-9][A-Za-z0-9._-]{3,})[\"']")
    for path, body in sources.items():
        uses_builder[path] = any(h.encode() in body for h in _BUILDER_HINTS)
        for m in name_re.finditer(body):
            tok = m.group(1).decode("utf-8", "replace")
            if tok.endswith(".witness.json"):
                tok = tok[: -len(".witness.json")]
            index[tok].append(path)

    unstamped: list[str] = []
    stamped = exempt = 0
    for name, body in sorted(witnesses.items()):
        parts = Path(name).parts
        if not args.include_deprecated and "_deprecated" in parts:
            continue
        if any(name.endswith(s) for s in AUDIT_SUFFIXES):
            exempt += 1
            continue
        try:
            d = json.loads(body)
        except json.JSONDecodeError:
            continue
        if not isinstance(d, dict):
            continue
        if d.get("q0Anchor"):
            stamped += 1
        else:
            unstamped.append(name)

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
        # Prefer a builder-using candidate: a witness is often mentioned by
        # consumers too, and a consumer must not be reported as the thing that
        # failed to stamp.
        pick = next((c for c in cands if uses_builder.get(c)), cands[0])
        producer_of[w] = pick
        stem = Path(pick).stem
        if not uses_builder.get(pick):
            causes["INERT_DECLARATION" if stem in declared else "NOT_BUILDER"].append(w)
        elif stem in declared:
            causes["DECLARED_STALE"].append(w)
        else:
            causes["UNDECLARED"].append(w)

    total = len(unstamped)
    scope = "incl. _deprecated" if args.include_deprecated else "live (audit scope)"
    print(f"rev {args.rev} ({sha})   scope: {scope}")
    print(f"  witnesses in tree    {len(witnesses)}")
    print(f"  audit-exempt         {exempt}")
    print(f"  stamped              {stamped}")
    print(f"  UNSTAMPED            {total}")
    print(f"  manifest declares    {len(declared)} stems")
    print()
    print("cause partition of the unstamped population")
    print("-" * 62)
    order = ["UNDECLARED", "NOT_BUILDER", "INERT_DECLARATION", "NO_PRODUCER",
             "DECLARED_STALE", "GENERATED_MIRROR"]
    for k in order:
        v = causes.get(k, [])
        pct = f"{100 * len(v) / total:5.1f}%" if total else "  n/a"
        print(f"  {k:19s} {len(v):5d}  {pct}")
        for s in v[: args.sample]:
            print(f"        {s}")
            print(f"            producer: {producer_of.get(s, '—')}")

    und = Counter(producer_of.get(w, "?") for w in causes.get("UNDECLARED", []))
    print()
    print(f"UNDECLARED spans {len(und)} distinct producers; top 8 by witness count:")
    for prod, n in und.most_common(8):
        print(f"    {n:4d}  {prod}")

    if args.json_out:
        Path(args.json_out).write_text(json.dumps({
            "rev": args.rev, "sha": sha,
            "totals": {"witnesses": len(witnesses), "exempt": exempt,
                       "stamped": stamped, "unstamped": total,
                       "declared_stems": len(declared)},
            "causes": {k: causes.get(k, []) for k in order},
            "producer_of": producer_of,
        }, indent=2), encoding="utf-8")
        print(f"\nwrote {args.json_out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
