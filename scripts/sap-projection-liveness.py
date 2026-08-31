#!/usr/bin/env python3
"""Which `proof-no-self-assuming-projection` findings are STILL bare projections?

## Why this exists

The vacuity review ledger
([`docs/audits/lean-vacuity-review-ledger.json`](../docs/audits/lean-vacuity-review-ledger.json))
records an agent verdict per `(file, decl, criterion)`. A `genuine` verdict on
`proof-no-self-assuming-projection` means the declaration's body was, at review
time, the class field its type restates. It does **not** say whether that is
still true — the ledger is a record of adjudication, not of repair state.

So a drain needs a *liveness* measure, and the obvious one is wrong.

**TRAP, measured 2026-08-31.** Asking *"does the declaration name still occur
in the file?"* reports **81 of 81 files still live** immediately after a
tranche that repaired nine of them — because a repaired file keeps the name
(the ref points at it) and, worse, a *gutted* file mentions the name in the
docstring explaining what was removed. The check answers "is the string
present", which is not the question.

This script parses each declaration's body instead and asks whether it is a
bare projection: `:= ctx.field`, `:= inst.field arg …`, or
`:= by exact ctx.field`. Measured the same day on the same tree, that gives

    PROJECTION            46   (LIB 31, SIBLING 15)
    not-a-bare-projection 23
    GONE                  21   (declaration removed)

The `GONE` bucket is not a defect: it is the drain, and it names exactly the
declarations removed by the bucket-A gutting plus the two false classes.

## Units — say which one you are quoting

The ledger counts **declarations**; the arc's earlier framing counted
**classes**. `bucket C = 31` (library) happens to agree here, but `bucket
B = 6` was six vacuous *classes* in siblings while this reports fifteen
sibling *projections* — several of them in classes never scored vacuous.
They are different populations and neither number is a correction of the
other.

## Limits

The body parser is regex-based. It recognises the three spellings above and
nothing else, so a projection wrapped in `⟨…⟩`, `Iff.intro`, or a `by`-block
that does more than `exact` reads as `not-a-bare-projection`. That direction
is the safe one for a drain — it under-reports work rather than inventing it —
but it means a clean run is **not** proof that no projection remains.

USAGE
    python3 scripts/sap-projection-liveness.py           # summary + lists
    python3 scripts/sap-projection-liveness.py --json out.json
"""

from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "docs/audits/lean-vacuity-review-ledger.json"
CRITERION = "proof-no-self-assuming-projection"

# `:= ctx.field`, `:= inst.field a b`, optionally behind `by exact`.
_PROJ = re.compile(
    r":=\s*(?:by\s+exact\s+)?[A-Za-z_][\w'.]*\.[A-Za-z_][\w'₀-₉]*"
    r"\s*[a-zA-Z_₀-₉' ]*$"
)
_EXACT = re.compile(r"by\s+exact\s+[\w'.]+\.[\w'₀-₉]+[\w' ]*")

_NEXT_DECL = re.compile(
    r"\n(?=(?:/--|/-!|@\[|theorem |lemma |def |noncomputable |class "
    r"|structure |instance |example |end ))"
)


def body_of(text: str, decl: str) -> str | None:
    """The source of `decl`, from its header to the next top-level declaration."""
    short = decl.split(".")[-1]
    m = re.search(
        rf"^\s*(?:theorem|lemma|def|noncomputable def)\s+{re.escape(short)}\b",
        text,
        re.M,
    )
    if not m:
        return None
    rest = text[m.start():]
    n = _NEXT_DECL.search(rest[1:])
    return rest[: (n.start() + 1 if n else len(rest))]


def classify(path: str, decl: str) -> str:
    p = ROOT / path
    if not p.exists():
        return "MISSING"
    body = body_of(p.read_text(errors="replace"), decl)
    if body is None:
        return "GONE"
    tail = " ".join((body.split(":=", 1)[1] if ":=" in body else "").split())
    if _PROJ.search(":= " + tail) or (tail and _EXACT.fullmatch(tail)):
        return "PROJECTION"
    return "not-a-bare-projection"


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--json", help="write the full result set here")
    args = ap.parse_args()

    ledger = json.loads(LEDGER.read_text())
    rows = []
    for key, entry in ledger["entries"].items():
        if entry.get("category") != CRITERION or entry.get("verdict") != "genuine":
            continue
        path, decl, _ = key.split("::")
        rows.append({"file": path, "decl": decl, "status": classify(path, decl),
                     "tree": "LIB" if "/lean/QOU/" in path else "SIBLING"})

    counts = collections.Counter(r["status"] for r in rows)
    live = [r for r in rows if r["status"] == "PROJECTION"]
    print(f"genuine `{CRITERION}` entries: {len(rows)}")
    for k, v in counts.most_common():
        print(f"  {k:<22} {v}")
    print(f"\nstill projections by tree: "
          f"{dict(collections.Counter(r['tree'] for r in live))}")
    for tree in ("SIBLING", "LIB"):
        sel = sorted((r for r in live if r["tree"] == tree),
                     key=lambda r: (r["file"], r["decl"]))
        print(f"\n### {tree} ({len(sel)})")
        for r in sel:
            print(f"  {r['file']}::{r['decl']}")

    if args.json:
        Path(args.json).write_text(json.dumps(rows, indent=2))
        print(f"\nwrote {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
