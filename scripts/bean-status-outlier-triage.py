#!/usr/bin/env python3
"""Triage input for beans whose `status:` is outside beans' own vocabulary.

`check-beans.sh` shape 6 reports these; it deliberately does not fix them. This
supplies what an adjudicator needs to fix them one at a time: for each bean, the
lines in its own body that bear on whether the work is finished.

## Why this reports EVIDENCE and not a verdict

The tempting repair is `done -> completed`, `open -> todo`. It is wrong, and the
counter-example is why shape 6 is advisory: `qou-argp` carries `status: done`
over a body reading

    "Everything the converse zero locus needs is proved EXCEPT ONE NAMED LEMMA."

That is a live gap. Rewriting it to `completed` would close open work, which
AGENTS.md rule 13a forbids outright ("Don't close beans with open
conjectures!!!", owner directive). So the status field is not trustworthy on
exactly the population being triaged, and a classifier keyed on it -- or on any
single keyword -- would launder that unreliability into a bulk edit.

What this does instead is quote the bean back at you, both ways, and leave the
call to a reader. The `lean` column is a hint with a stated basis, never an
instruction: where the two kinds of evidence disagree it says MIXED, which is
the case that most needs a human and the one a keyword classifier would
silently resolve.

## Reading the output

    id  status  lean  title
        + <line>    evidence the work FINISHED
        - <line>    evidence something REMAINS

`lean` is `closed` / `open` / `MIXED` / `none`, from which kinds of evidence
were found. MIXED and none are the interesting rows.

One line can appear under BOTH `+` and `-`, and that is the point rather than a
bug. `qou-argp`'s "proved except one named lemma" matches a finished pattern
(`proved`) and a remains pattern (`except one`) at once, so the row shows it
twice. A line that is evidence both ways is exactly the line an adjudicator
needs to see, and it is the shape a single-keyword classifier resolves wrongly
and silently.

Measured on the 46 as of 2026-09-07: MIXED 24, closed 10, none 11, open 1. So
only 10 of 46 lean cleanly finished, which is the quantitative reason shape 6
is advisory -- a bulk `done -> completed` would have been wrong on most of the
population, not on an unlucky one.

A row can also invert its own status: `fwr6` is `status: open` over a body
saying "Item 2 is closed, and this bean was wrong about it".

Usage:  scripts/bean-status-outlier-triage.py [--markdown]
Exit:   0 always -- this is triage input, not a gate.
"""
from __future__ import annotations

import argparse
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BEANS = ROOT / "beans/defs"

#: beans' own accepted values (`beans update --help`).
CANONICAL = {"in-progress", "todo", "draft", "completed", "scrapped"}

#: Evidence the work finished. Deliberately narrow: each pattern names a
#: concrete artifact or outcome, not a mood. "done" is NOT here -- it is the
#: very word whose reliability is in question.
CLOSED_RE = re.compile(
    r"\b(CLOSED|RESOLVED|DRAINED|RETRACTED|SUPERSEDED|"
    r"merged as #\d+|landed in #?\d+|fixed in [0-9a-f]{7,}|"
    r"PROVED|proved sorry-free|all (?:checks|assertions) pass)\b", re.I)

#: Evidence something remains. Also narrow, and note `except` -- it is what
#: `qou-argp` turns on, and a generic "open" scan would have drowned it.
OPEN_RE = re.compile(
    r"\b(GAP:|STILL OPEN|remains open|not yet|except one|"
    r"is left|left open|unresolved|blocked on|needs a|"
    r"open question|TODO)\b", re.I)


def _front_matter(text: str) -> str:
    return text.split("---")[1] if text.startswith("---") else ""


def _field(fm: str, name: str) -> str:
    m = re.search(rf"^{name}:\s*(.*)$", fm, re.M)
    return m.group(1).strip().strip("'\"") if m else ""


def _evidence(body: str, pattern: re.Pattern, limit: int = 2):
    """Up to `limit` matching lines, trimmed. Skips the front-matter."""
    out = []
    for line in body.splitlines():
        s = line.strip().lstrip("#-*> ").strip()
        if not s or len(s) < 12:
            continue
        if pattern.search(s):
            out.append(s[:104])
            if len(out) >= limit:
                break
    return out


def scan():
    rows = []
    for p in sorted(BEANS.glob("*.md")):
        text = p.read_text(errors="replace")
        fm = _front_matter(text)
        status = _field(fm, "status")
        if not status or status in CANONICAL:
            continue
        body = text.split("---", 2)[-1]
        closed = _evidence(body, CLOSED_RE)
        opened = _evidence(body, OPEN_RE)
        lean = ("MIXED" if closed and opened
                else "closed" if closed
                else "open" if opened else "none")
        bid = re.search(r"^#\s+([A-Za-z0-9-]+)$", fm, re.M)
        rows.append({
            "id": bid.group(1) if bid else p.stem,
            "status": status,
            "lean": lean,
            "title": _field(fm, "title"),
            "closed_evidence": closed,
            "open_evidence": opened,
        })
    return rows


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args()
    rows = scan()

    by_lean = {}
    for r in rows:
        by_lean[r["lean"]] = by_lean.get(r["lean"], 0) + 1

    if args.markdown:
        print("| id | status | lean | title |")
        print("|---|---|---|---|")
        for r in rows:
            print(f"| `{r['id']}` | {r['status']} | **{r['lean']}** | "
                  f"{r['title'][:70]} |")
        return 0

    print(f"  beans with a status outside {sorted(CANONICAL)}: {len(rows)}")
    print(f"  lean: " + "  ".join(f"{k}={v}" for k, v in sorted(by_lean.items())))
    print("\n  MIXED and none are the rows that most need a human — the two the\n"
          "  status field cannot settle and a keyword rule would settle wrongly.\n")
    for r in rows:
        print(f"  {r['id']:<12} {r['status']:<6} lean={r['lean']:<7} "
              f"{r['title'][:58]}")
        for e in r["closed_evidence"]:
            print(f"      + {e}")
        for e in r["open_evidence"]:
            print(f"      - {e}")
    print("\n  + finished-evidence   - remains-evidence.  Neither is a verdict:\n"
          "  `qou-argp` is `status: done` over 'proved EXCEPT ONE NAMED LEMMA'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
