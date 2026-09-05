#!/usr/bin/env python3
"""Rank in-progress beans by how much the tree moved under them since they were
last updated.

WHAT THIS MEASURES, exactly: for each bean, the repo paths it names, and how
many commits touched those paths AFTER the bean's `updated_at`. That is a
TRIAGE SIGNAL, not a verdict — a bean whose files moved may still be open, and
a bean whose files did not move may have been answered somewhere else entirely
(measured this session: `qou-t7mt`'s answer landed in a commit whose subject was
about something unrelated).

WHY IT EXISTS. On 2026-09-05, thirteen of fourteen beans on the owner-gated
queue turned out to be already handled. But that sample was selected BY the
owner-gate criterion — beans that sat blocked, and so had the most time to be
resolved by someone else while nobody updated them. The rate does not
generalise to all 450 in-progress beans, 83 of which were updated in the last
three days. This script exists to rank, so a human or an agent spends the
checking budget where the tree actually moved.

    python3 scripts/bean-staleness-triage.py            # top 25
    python3 scripts/bean-staleness-triage.py --all
    python3 scripts/bean-staleness-triage.py --json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BEANS = ROOT / ".beans"

# A path-shaped token inside a bean body. Deliberately narrow: it must look
# like a real repo path with an extension we care about, so prose does not
# generate phantom paths.
PATH_RE = re.compile(
    r"\b((?:computations|content|scripts|docs|tools|schemas)/[\w./-]+"
    r"\.(?:py|lean|ts|md|json))\b"
)


def git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        capture_output=True, text=True, check=False,
    ).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--limit", type=int, default=25)
    a = ap.parse_args()

    rows = []
    for f in sorted(BEANS.glob("*.md")):
        text = f.read_text(errors="replace")
        if not re.search(r"^status: in-progress\s*$", text, re.M):
            continue
        m = re.search(r"^updated_at: (\S+)", text, re.M)
        if not m:
            continue
        updated = m.group(1)
        bean_id = f.name.split("--")[0]

        paths = sorted({p for p in PATH_RE.findall(text)
                        if (ROOT / p).exists()})
        if not paths:
            rows.append({"bean": bean_id, "updated": updated[:10],
                         "paths": 0, "moved": 0, "commits": 0,
                         "note": "names no existing repo path"})
            continue

        out = git("log", "--oneline", f"--since={updated}", "--", *paths)
        commits = len([ln for ln in out.splitlines() if ln.strip()])
        moved = 0
        for p in paths:
            o = git("log", "--oneline", "-1", f"--since={updated}", "--", p)
            if o.strip():
                moved += 1
        rows.append({"bean": bean_id, "updated": updated[:10],
                     "paths": len(paths), "moved": moved,
                     "commits": commits, "note": ""})

    rows.sort(key=lambda r: (-r["commits"], -r["moved"], r["updated"]))
    if a.json:
        json.dump(rows, sys.stdout, indent=2)
        print()
        return 0

    shown = rows if a.all else rows[: a.limit]
    print(f"{len(rows)} in-progress beans; showing {len(shown)}, "
          f"ranked by commits touching their named paths since their own "
          f"updated_at.\n")
    print(f"{'bean':12} {'updated':11} {'paths':>5} {'moved':>5} "
          f"{'commits':>7}  note")
    for r in shown:
        print(f"{r['bean']:12} {r['updated']:11} {r['paths']:5d} "
              f"{r['moved']:5d} {r['commits']:7d}  {r['note']}")

    nopath = sum(1 for r in rows if r["paths"] == 0)
    unmoved = sum(1 for r in rows if r["paths"] and r["commits"] == 0)
    print(f"\n{nopath} name no existing repo path (not rankable this way).")
    print(f"{unmoved} name paths that have NOT moved since the bean was "
          f"updated — but see the docstring: an answer can land elsewhere.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
