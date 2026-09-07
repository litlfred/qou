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

THE QUEUE IS TWO POPULATIONS, and conflating them is the mistake this script
was one revision away from making. Measured over the 450:

  ARTIFACT beans (~285) name repo files. "Has the tree moved under it" is
  meaningful for these, and staleness ranking applies.

  RESEARCH beans (~165) name NO file at all — "prove algebraic commutativity
  of Murphy elements", "Burnside Sum_lambda f_lambda^2 via GNW hook length",
  "prove Cov(Planch, ln f, omega_3) = 0 via Ivanov". These cannot go stale by
  the tree moving; they go stale only when someone proves the thing. Reporting
  them as "not rankable" invites reading them as a tool defect. They are not.

MEASURED HIT RATE, 2026-09-06: 8 actionable findings from 14 ranked beans
checked. The rate is worth recording because it settles a caution stated above
in the OTHER direction. The "thirteen of fourteen already handled" figure came
from the owner-GATED subset and, as noted, does not generalise. On the ranked
ARTIFACT subset the picture is different and better: over half the checks
produced real work, and the work was of four distinct kinds —

  a real fix        qou-b7cf   LAUNDERED 3 -> 0, plus one site the gate cannot
                               see (sp.Float(str(Q), 40), 17 digits padded to 40)
                    qou-ghy5   32 fabricated-DOI citation sites drained at the
                               producer, 9 -> 8 keys / 48 -> 16 sites
                    qou-qcy6   a new carrier-vacuity detector, 17 candidates
  a stale artifact  qou-aj91   the audit's OWN witness was one producer-
                               generation behind; reader surface 86 -> 88
  a verdict         qou-47sx   the blocked producer should NOT be repaired: its
                               volumes come from a function documented wrong for
                               five of its six subjects
  a correction      qou-8iru   three siblings re-derived, overnight, a result
                               this bean proved in Lean four weeks earlier
                    qou-b9c3   a sibling's orphan mechanism explains 0 of 22

Six of the fourteen were healthy and needed nothing (qou-2tuv, qou-0c19,
qou-cds1, qou-p77d, qou-e9pp, qou-9ot5) — which is the ranking working, not
failing: it costs one check to establish that, and the check is the product.

TWO SELECTION EFFECTS, so the 8/14 is not quotable as a general rate. The
sample is the TOP of the ranking, i.e. maximum tree movement, and it was
checked by an agent that reads the bean before deciding — a cheaper triage
would find less. Re-measure rather than quote this.

THE RANKING CANNOT SEPARATE "resolved by someone else" FROM "actively worked",
and this is its sharpest limitation. Both produce a high commit count against
the bean's paths. Worked example from the run that introduced this note:
`qou-2tuv` ranks FIRST (103 commits over 38 paths) and is not stale at all —
it is a live convention-D question carrying recent substantive measurements.
So read a high rank as "spend a check here", never as "this is probably done".
Separating the two would need commit attribution per branch, which this does
not attempt.

An earlier revision recovered only 22 of 187 unrankable beans by resolving
paths written relative to `computations/` (e.g. `qbeta/foo.py`, `probes/bar.py`).
That resolution is kept — it is real — but it is 11%, not the fix, and finding
that out is what established the two-population split above.

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

# Beans routinely write paths relative to `computations/` — `qbeta/foo.py`,
# `probes/bar.py`, `audits/baz.py` — which PATH_RE cannot see because it
# demands a top-level prefix. Resolving those recovers 22 of 187 (11%).
REL_RE = re.compile(r"\b([\w-]+(?:/[\w.-]+)*\.(?:py|lean|ts|json))\b")
REL_PREFIXES = (
    "", "computations", "content", "scripts", "docs", "tools", "schemas",
    "computations/probes", "computations/audits", "computations/qbeta",
    "computations/sweeps", "computations/markov", "computations/alpha",
    "computations/deltalambda", "computations/schurweyl",
    "computations/a_operator",
)


def resolve_paths(text: str) -> list[str]:
    """Repo paths a bean names, absolute-style and `computations/`-relative."""
    hits = {p for p in PATH_RE.findall(text) if (ROOT / p).exists()}
    for cand in REL_RE.findall(text):
        if any(cand.startswith(f"{pre}/") for pre in REL_PREFIXES if pre):
            continue
        for pre in REL_PREFIXES:
            probe = (ROOT / pre / cand) if pre else (ROOT / cand)
            if probe.exists():
                hits.add(f"{pre}/{cand}" if pre else cand)
                break
    return sorted(hits)


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

        paths = resolve_paths(text)
        if not paths:
            # NOT a tool failure — see the docstring. A bean naming no file is
            # a research question, and the tree moving says nothing about it.
            rows.append({"bean": bean_id, "updated": updated[:10],
                         "paths": 0, "moved": 0, "commits": 0,
                         "kind": "research",
                         "note": "research bean — names no file; not rankable "
                                 "by tree movement, and that is correct"})
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
                     "commits": commits, "kind": "artifact", "note": ""})

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

    research = sum(1 for r in rows if r["kind"] == "research")
    artifact = len(rows) - research
    unmoved = sum(1 for r in rows
                  if r["kind"] == "artifact" and r["commits"] == 0)
    print(f"\n{artifact} ARTIFACT beans (name repo files) — rankable.")
    print(f"{research} RESEARCH beans (name none) — NOT rankable by tree "
          f"movement, and that is correct, not a gap. They go stale only when "
          f"someone proves the thing.")
    print(f"\nOf the {artifact} artifact beans, {unmoved} have paths that did "
          f"NOT move since the bean was updated. So 'moved at all' is "
          f"{100 * (artifact - unmoved) // max(artifact, 1)}% positive and is "
          f"useless as a filter — only the MAGNITUDE discriminates. Rank by "
          f"it; do not threshold on it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
