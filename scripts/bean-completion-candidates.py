#!/usr/bin/env python3
"""Open beans that a later commit says were finished.

WHY THIS EXISTS
---------------
A bean left at `status: todo` after its work has landed is not a neutral
bookkeeping lapse -- it actively costs sessions. AGENTS.md §"Agent work-plan
policy" makes the bean list the agent's source of truth for "what next", so a
stale high-priority `todo` sends the next agent to re-derive something the
corpus already holds. That is the corpus-grep failure one level up: the grep
paths are clean because the work IS done; only the tracker disagrees.

Measured on 2026-09-04, before this script existed: of the first three
high-priority `todo` beans a session picked up, TWO had already been finished
(`qou-e4eu` closed by a sibling, `qou-w2vy` fixed by `d943f2acfac`), and a
third (`qou-1ucq`) had its headline claim fixed four days earlier by two
commits it had never absorbed. The session got several steps into a
re-derivation each time before `git log` stopped it.

WHAT THIS REPORTS -- AND WHAT IT DOES NOT
-----------------------------------------
For every bean still at `todo`, whether a commit SUBJECT naming it, dated after
the bean's own `updated_at`, carries a completion verb (`fix(...)`, `closed`,
`resolved`, `drained`, ...).

**These are CANDIDATES, never verdicts, and the false-positive rate is not
small.** Measured on the 12 high-priority candidates in the first run, at least
5 were visibly not done from the subject alone, in two distinct ways:

  * **Partial completion.** "ITEM 4 CLOSED" closes one item of a queue;
    "named failures drained, but the cascade class recurred" says outright that
    the bean survives; "item 3 fully closed; the remaining item is ..." names
    what is left.
  * **Verb attached to a DIFFERENT bean.** A subject like
    "qou-mfst is fixed on main -- close it, and name the pattern it shares with
    qou-lkrd" matches on `qou-lkrd` while the verb governs `qou-mfst`. This
    script cannot bind a verb to one of several ids in one subject.
  * **The verb is QUOTED or NEGATED -- it reports a REOPENING.** The worst class,
    because it inverts the meaning. `qou-hok7`'s later subject is
    "resurgence(qou-hok7): deuteron-wall 'resummation closed' is a wrong-transform
    artifact" -- the word `closed` appears in QUOTATION MARKS inside a subject
    whose whole point is that the closure was an artifact, and the bean was
    REOPENED by that very commit. A regex over a subject cannot see scare quotes.

**Reading the BODIES raises the rate further.** The ~4-in-10 above is what is
visible from subjects alone. Of the first four high-priority candidates whose
beans were actually opened and read, THREE were genuinely open and said so in
their own text ("Bean stays open on (1)-(4)"; "REOPENED. OPEN next step: ...").
n = 4 is small, but it points one way: treat the print-out as a list of beans
worth OPENING, and expect most of them to survive the read.

**Do not bulk-close from this output.** It is a read queue: it tells you which
beans are worth opening, and the reading is still yours.

The wider signal it deliberately does NOT print: 784 open beans have SOME
commit naming them after their own `updated_at`. That is an upper bound on
staleness and nothing more -- it catches progress, mentions and scope-widening
alike -- so it is not actionable and is not reported as staleness here.

USAGE
    scripts/bean-completion-candidates.py                # high priority only
    scripts/bean-completion-candidates.py --all          # every priority
    scripts/bean-completion-candidates.py --since 2026-08-01
"""
from __future__ import annotations

import argparse
import collections
import datetime
import pathlib
import re
import subprocess
import sys

_ID = re.compile(r"\bqou-[a-z0-9]{4,5}\b")
_DONE = re.compile(
    r"^(fix|fixes|fixed|close[sd]?|resolve[sd]?|complete[sd]?|drain|repair)\b"
    r"|\b(CLOSED|RESOLVED|COMPLETE|FIXED|drained|discharged)\b", re.I)
_ORDER = {"high": 0, "medium": 1, "low": 2}


def load_beans(root: pathlib.Path) -> dict:
    out = {}
    for f in sorted((root / ".beans").glob("*.md")):
        head = f.read_text(errors="replace")[:1200]
        g = {k: re.search(rf"^{k}: (.+)$", head, re.M) for k in
             ("status", "updated_at", "priority", "title")}
        bid = re.search(r"^# (\S+)", head, re.M)
        if not (bid and g["status"] and g["updated_at"]):
            continue
        out[bid.group(1)] = {
            "status": g["status"].group(1).strip(),
            "updated": g["updated_at"].group(1).strip(),
            "priority": g["priority"].group(1).strip() if g["priority"] else "?",
            "title": (g["title"].group(1).strip().strip("'\"") if g["title"] else ""),
            "file": f.name,
        }
    return out


def done_commits(since: str) -> dict:
    log = subprocess.run(
        ["git", "log", f"--since={since}", "--format=%H%x01%cI%x01%s"],
        capture_output=True, text=True).stdout.splitlines()
    hits = collections.defaultdict(list)
    for line in log:
        if line.count("\x01") != 2:
            continue
        sha, iso, subj = line.split("\x01", 2)
        ids = set(_ID.findall(subj))
        if not ids or not _DONE.search(subj):
            continue
        # Flag the ambiguous case rather than dropping it: a subject naming
        # several beans cannot say which one the verb governs.
        for b in ids:
            hits[b].append((sha, iso, subj, len(ids) > 1))
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="every priority, not just high")
    ap.add_argument("--since", default="2026-06-01", help="git log window (default 2026-06-01)")
    a = ap.parse_args()

    root = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                       capture_output=True, text=True).stdout.strip())
    beans = load_beans(root)
    hits = done_commits(a.since)

    rows = []
    for bid, b in beans.items():
        if b["status"] != "todo":
            continue
        try:
            upd = datetime.datetime.fromisoformat(b["updated"].replace("Z", "+00:00"))
        except ValueError:
            continue
        later = [h for h in hits.get(bid, [])
                 if datetime.datetime.fromisoformat(h[1]) > upd]
        if later:
            later.sort(key=lambda x: x[1])
            rows.append((b["priority"], bid, b, later[-1]))

    rows.sort(key=lambda r: (_ORDER.get(r[0], 3), r[2]["updated"]))
    shown = rows if a.all else [r for r in rows if r[0] == "high"]

    print(f"{len(beans)} beans, {sum(1 for b in beans.values() if b['status']=='todo')} open.")
    print(f"{len(rows)} open bean(s) have a completion-verb commit subject after their own "
          f"updated_at ({sum(1 for r in rows if r[0]=='high')} high priority).\n")
    for pri, bid, b, (sha, iso, subj, ambig) in shown:
        flag = "  [!! subject names >1 bean — the verb may govern another]" if ambig else ""
        print(f"  {bid}  ({pri}, last updated {b['updated'][:10]}){flag}")
        print(f"    bean : {b['title'][:100]}")
        print(f"    later: {sha[:11]} {iso[:10]} {subj[:100]}")
    print("\nCANDIDATES, NOT VERDICTS. From SUBJECTS alone the false-positive rate is "
          "~4 in 10; reading four\nof the bodies, THREE were still genuinely open. "
          "Three structural causes, all unfixable by regex:")
    print("  1. partial completion  -- 'ITEM 4 CLOSED', 'item 3 fully closed; the "
          "remaining item is ...'")
    print("  2. the verb governs a DIFFERENT bean named in the same subject "
          "(flagged above with !!)")
    print("  3. the verb is QUOTED or NEGATED and the commit REOPENED the bean -- "
          "e.g. qou-hok7's\n     \"deuteron-wall 'resummation closed' is a "
          "wrong-transform artifact\"")
    print("\nOpen each one and read it. Do NOT bulk-close from this output.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
