#!/usr/bin/env python3
"""classify-agent-docs — story S17 (bean qou-4gzy) of the migration epic.

CLASSIFY ONLY. Reads the agent docs and prints one TSV row per file; moves,
edits and deletes nothing (owner decision 10, 2026-10-04: audits are
classify-only). Deterministic: the same tree gives byte-identical output.

Scope (SKILLS2 report, S17): docs/coordination, docs/handoffs, docs/handover,
docs/handovers, docs/agent-briefs, .claude/validation-errors-handoff.md.

Classes follow the owner's docs/ split ruling of 2026-10-04 (recorded on
qou-pjfi / qou-fqbv / qou-4gzy):

  handoff              -> beans/notes      (session handover)
  coordination-ledger  -> beans/notes      (ledgers, rollout / watch logs)
  status-survey        -> beans/surveys    (status snapshots, censuses)
  outstanding-work     -> beans            (plans, queues, backlogs) — agent work
  math-note            -> HOLD             (waits for the working-notes graph
                                            kind, folio-assistant-8npa; never
                                            a todo — a finished derivation is
                                            not open work)
  live-registry        -> STAY             (validated JSON registries, their
                                            validators, catalogs — read by
                                            code and cited by AGENTS.md)
  unclear              -> owner-review

`inbound_refs` counts tracked files OUTSIDE the scope that name the file by
its basename (`git grep -l -F`). Any move of a file with inbound_refs > 0 must
update those references in the same commit.

`math_dollars` counts `$` in the body. A non-math class with a high count is
flagged `mixed=yes`: such a file still moves verbatim, but it must not be
summarised into a bean, because it carries mathematics.

Usage: python3 scripts/classify-agent-docs.py > <out.tsv>
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPE_DIRS = ["docs/coordination", "docs/handoffs", "docs/handover",
              "docs/handovers", "docs/agent-briefs"]
SCOPE_FILES = [".claude/validation-errors-handoff.md"]
MIXED_DOLLARS = 40
# This story's own analysis outputs list every file in scope; not a reference.
SELF_DIR = "docs/audits/2026-10-04-workplan-and-migration/"

# (class, destination, regex over "<path> <title>") — first match wins.
RULES = [
    ("live-registry", "STAY (live: validated data / validator / catalog)",
     r"registry|_validate\.py|\.json$|\.py$|catalog|benchmark-table|calibration-layers"),
    ("handoff", "beans/notes",
     r"hand-?over|hand-?off|docs/handovers?/|docs/handoffs/|agent-brief|\bbrief\b"),
    ("status-survey", "beans/surveys",
     r"survey|status|census|dashboard|audit-summary|inventory|snapshot|scorecard"),
    ("handoff", "beans/notes", r"session intent"),
    ("outstanding-work", "beans",
     r"pivot|opportunit|research.direction|follow-?ups|triage|scope|trio|expansion|fate|workplan|work-plan|queue|backlog|\bplan\b|-plan\b|plan-|todo|priority|tranche|follow-?ons?|next-threads|roadmap|strategy"),
    ("coordination-ledger", "beans/notes",
     r"ledger|coordination|cleanup|rollout|watch|sibling|\bci\b|fix-|bib-|verification|acceptances|misfetch|cheat-sheet-manager|services|consumer|docstring"),
    ("math-note", "HOLD:folio-assistant-8npa",
     r"derivation|deriv|proof|refut|falsif|cheat-?sheet|identity|lemma|closure|formula|rule|consistency|conjecture|theorem|categorical|substrate|lambda|q-beta|qbeta|mass|binding|hecke|wenzl|markov|knot|braid|chain|1pp[bq]"),
]


def title_of(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("#"):
            return line.lstrip("# ").strip()
    return ""


def classify(rel: str, text: str) -> tuple[str, str, str, str]:
    # Match the FILE NAME (plus the handover directories, which are themselves
    # the classification) and the title — never the parent path, or every file
    # under docs/coordination/ matches /coordination/.
    parent = rel.rsplit("/", 1)[0] + "/"
    name = rel.rsplit("/", 1)[-1]
    key = (parent if re.search(r"hand|brief", parent) else "") + name
    hay = f"{key} {title_of(text)}".lower()
    for cls, dest, rx in RULES:
        m = re.search(rx, hay)
        if m:
            conf = "h" if m.start() < len(key) else "m"  # name hit beats title hit
            return cls, dest, conf, f"/{m.group(0)}/"
    dollars = text.count("$")
    if dollars >= MIXED_DOLLARS:
        return "math-note", "HOLD:folio-assistant-8npa", "l", f"no name rule; {dollars} $"
    return "unclear", "owner-review", "l", "no rule fired"


def files() -> list[Path]:
    out = []
    for d in SCOPE_DIRS:
        p = ROOT / d
        if p.is_dir():
            out += [f for f in p.rglob("*") if f.is_file()]
    out += [ROOT / f for f in SCOPE_FILES if (ROOT / f).is_file()]
    return sorted(set(out))


def inbound_counts(scope: list[str]) -> dict[str, int]:
    """basename -> number of tracked files outside scope (and outside beans/) naming it.

    One `git grep -o -F -f` pass over the tree instead of one grep per file.
    """
    import subprocess
    import tempfile
    names = sorted({p.rsplit("/", 1)[-1] for p in scope})
    with tempfile.NamedTemporaryFile("w", suffix=".txt") as pat:
        pat.write("\n".join(names) + "\n"); pat.flush()
        out = subprocess.run(["git", "grep", "--null", "-F", "-f", pat.name], cwd=ROOT,
                             capture_output=True, text=True).stdout
    # A hit must not be the tail of a longer name (`1ppb.md` inside `x-1ppb.md`).
    rx = re.compile(r"(?<![A-Za-z0-9_.-])(" + "|".join(map(re.escape, names)) + r")")
    scoped, hits = set(scope), {}
    for rec in out.splitlines():
        path, _, text = rec.partition("\0")
        if path in scoped or path.startswith(("beans/", SELF_DIR)):
            continue
        for m in rx.finditer(text):
            hits.setdefault(m.group(1), set()).add(path)
    return {n: len(hits.get(n, ())) for n in names}


def main() -> int:
    w = sys.stdout.write
    w("path\tclass\tdestination\tconfidence\tmixed\tmath_dollars\tinbound_refs\tbytes\trule\ttitle\n")
    fs = files()
    scope = [f.relative_to(ROOT).as_posix() for f in fs]
    refs = inbound_counts(scope)
    for f in fs:
        rel = f.relative_to(ROOT).as_posix()
        text = f.read_text(errors="replace")
        cls, dest, conf, rule = classify(rel, text)
        dollars = text.count("$")
        mixed = "yes" if cls != "math-note" and dollars >= MIXED_DOLLARS else "no"
        title = title_of(text).replace("\t", " ")[:120]
        w(f"{rel}\t{cls}\t{dest}\t{conf}\t{mixed}\t{dollars}\t{refs[rel.rsplit('/', 1)[-1]]}\t{f.stat().st_size}\t{rule}\t{title}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
