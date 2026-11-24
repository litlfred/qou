#!/usr/bin/env python3
"""Post-merge bean reconciler for landed PRs and Merge Trains (`cat/cat-harness/beans`).

Why this tool exists
--------------------
In `litlfred/qou`, the flat-file `beans` tracker lives on the orphan branch
`origin/cat/cat-harness/beans` (typically checked out at `/private/tmp/qou-beans-latest`
and symlinked from `<qou>/beans`), NOT on `origin/main`. Consequently, merging a PR or
a `Process_MergeTrain` batch onto `origin/main` never updates bean statuses unless an
explicit post-merge step closes the completed leaf beans and pushes `cat/cat-harness/beans`.

This script implements the mandatory post-merge work-item closure step required by:
  - `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-to-main.md` (`Task_Report`),
  - `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-queue.md` (`Process_MergeTrain`),
  - `folio-assistant/cat-harness/sdlc/skills/sdlc-core/merge-manager-watcher.md` (`merge-steward`),
  - `.claude/skills/local/prepare-merge-auto.md` & `.claude/skills/local/integration-watcher.md`.

Precision & Anti-False-Closure Discipline (STRICT)
--------------------------------------------------
1. Verifies `state == "MERGED"` via GitHub CLI and `git merge-base --is-ancestor <oid> origin/main`
   after a targeted refspec fetch (`+refs/heads/main:refs/remotes/origin/main`; never bare `git fetch`).
2. Extracts primary target beans from PR titles, explicit closure/summary clauses, and single-purpose
   commit subjects — ignoring incidental `aggregating` / `linked` / `companion to` / `parent` mentions
   and multi-bean `(Lean only)` / `prereg` / `beans:` commits.
3. Enforces eight safety guards before closing any bean (unless `--force-bean <id>` is explicitly passed):
   - Skips beans already `completed` or `scrapped`;
   - Skips standing umbrella epics/milestones (`NEVER_CLOSE`, `type == milestone`, or `open_children > 0`,
     including prose `Child Beans` lists on epics without YAML `parent:` links);
   - Skips beans with open `blocked_by` dependencies or hold tags (`needs-owner-ok`, `8f-open`, `hold`);
   - Skips `OWNER CALL` / `OWNER DECISION` / `must never be closed` / `do not close` beans and corpus-wide
     multi-file sweep trackers;
   - Skips any bean whose PR-body mention, commit subject, or own bean-body tail (`[-2500:]`) carries an
     open caveat (`remains open`, `stays open`, `kept in-progress`, `open / next:`, `closed now: 0/`,
     `gated on owner`, `partial`, `done-partial`, `left open`, `deferred`, `until ... discharged`);
   - Skips any bean when a PR-touched `.lean` file introduces an uninstantiated `Conjecture` /
     `Hypothesis` class (`Rule 13a` / `§3b-cond` guard);
   - Re-evaluates parent `epic`s after leaf closures and closes an epic ONLY when `children > 0`,
     `open_children == 0`, not in `NEVER_CLOSE`, and its body carries zero open caveats.

Usage
-----
  python3 scripts/close-merged-pr-beans.py --pr 9282
  python3 scripts/close-merged-pr-beans.py --prs 9245,9247,9273,9278,9282
  python3 scripts/close-merged-pr-beans.py --prs 9238,9240,9241 --dry-run
  python3 scripts/close-merged-pr-beans.py --selftest
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

NEVER_CLOSE: frozenset[str] = frozenset({
    "qou-s028",
    "qou-xip2",
    "qou-anx0",
    "qou-lref",
    "qou-10v9",
    "qou-qhcr",
    "qou-u2al",
    "b9cj",
})

OPEN_STATUSES: frozenset[str] = frozenset({"in-progress", "todo", "open", "draft"})
CLOSED_STATUSES: frozenset[str] = frozenset({"completed", "scrapped"})

# Words on a PR-body or commit line indicating the bean is NOT completed by this PR.
OPEN_CAVEAT_RE = re.compile(
    r"\b("
    r"remains?\s+open|stays?\s+open|remain(?:s)?\s+in[- ]progress|stays?\s+in[- ]progress|"
    r"kept\s+`?in[- ]progress`?|stays?\s+todo|not\s+(?:yet\s+)?closed|partial(?:ly)?|done[- ]partial|"
    r"left\s+open|leave\s+open|keep(?:s)?\s+.*open|deferred|out\s+of\s+scope|"
    r"until\s+.*discharged|rule\s+13a|do\s+not\s+close|must\s+never\s+be\s+closed|"
    r"follow[- ]?up\s+to|omitted|narrowed"
    r")\b",
    re.I,
)

# Tail-of-bean-body markers indicating the worker who last updated the bean intentionally left it open.
BEAN_TAIL_OPEN_RE = re.compile(
    r"(?:"
    r"\b(?:remains?\s+open|stays?\s+open|remain(?:s)?\s+in[- ]progress|stays?\s+in[- ]progress)\b|"
    r"\bkept\s+`?in[- ]progress`?\b|"
    r"^\s*open\s*/\s*next\s*:|"
    r"\bclosed\s+now\s*:\s*0/\d+\b|"
    r"\bgated\s+on\s+owner\b|"
    r"\bno\s+instance\s+exists;\s*none\s+should\s+be\s+added\b"
    r")",
    re.I | re.M,
)

GUARD_TAGS: frozenset[str] = frozenset({
    "needs-owner-ok",
    "8f-open",
    "owner-decision",
    "hold",
})

# Clauses where linked/umbrella/gap/partial-seam beans are cited for context rather than closed.
CONTEXT_ONLY_LINE_RE = re.compile(
    r"\b("
    r"aggregat(?:es|ing)|companion\s+to|linked\s+(?:parent|goal|beans?|legacy)|"
    r"parent\s+epic|under\s+epic|advancing\s+linked|gap\s+`?qou-|stacked\s+on|"
    r"leaf\s+deliverables\s+of|algebraic\s+seams\s+of|diagnostics\s+for"
    r")\b",
    re.I,
)

# Bean title/body markers requiring explicit human/steward override.
# Note: "(owner decision 3)" appears in 2026-10-04 claim-reset boilerplate and is NOT an owner gate.
OWNER_GATE_TITLE_RE = re.compile(r"\b(OWNER\s+CALL|OWNER\s+DECISION)\b", re.I)
OWNER_GATE_BODY_RE = re.compile(
    r"\b(must\s+never\s+be\s+closed|do\s+not\s+close\s+while\s+open|owner\s+decision\s+\d+:\s*group,\s*do\s+not\s+close)\b",
    re.I,
)

# Corpus-wide multi-file sweep titles that should not auto-close from a small (<10 file) PR unless forced.
CORPUS_SWEEP_TITLE_RE = re.compile(
    r"(?:^SCREEN:|\b(?:[2-9]\d|\d{3,4})\s+(?:Lean\s+files|witnesses|producers|COMPUTED|non-integral|blocks|beans)\b)",
    re.I,
)

# Explicit PR-body lines that target a bean for delivery/closure.
PRIMARY_BODY_LINE_RE = re.compile(
    r"(?:"
    r"^\s*(?:closes?|fixes?|resolves?|completes?|beans?\s+closed|beans?)\s*[:\s]|"
    r"^\s*##+\s+summary\b|"
    r"ready\s+for\s+`?completed`?|"
    r"^\s*[-*]\s+\*\*`?[a-z0-9_-]{4,24}`?"
    r")",
    re.I,
)

NON_CLOSING_COMMIT_PREFIX_RE = re.compile(
    r"^(?:beans?\b|docs\(prereg\)|prereg\b|record\(|audit\(ns-)",
    re.I,
)

CONJECTURE_CLASS_DECL_RE = re.compile(
    r"^\s*class\s+([A-Za-z0-9_']*(?:Conjecture|Hypothesis)[A-Za-z0-9_']*)\b",
    re.M,
)

TOKEN_RE = re.compile(r"\b[a-zA-Z0-9_-]{4,24}\b")


@dataclass
class BeanRecord:
    bean_id: str
    status: str
    bean_type: str
    title: str
    parent: str
    body: str
    path: pathlib.Path
    children: list[str] = field(default_factory=list)
    blocked_by: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)


@dataclass
class BeanDecision:
    bean_id: str
    action: str  # "CLOSE" or "SKIP_*"
    reason: str
    pr_number: int
    merge_sha: str


def parse_frontmatter(md_text: str) -> tuple[dict[str, object], str]:
    if not md_text.startswith("---"):
        return {}, md_text
    parts = md_text.split("---", 2)
    if len(parts) < 3:
        return {}, md_text
    fm_raw, body = parts[1], parts[2]
    fm: dict[str, object] = {}
    id_match = re.search(r"^#\s+(\S+)\s*$", fm_raw, re.M)
    if id_match:
        fm["id"] = id_match.group(1).strip()
    cur_list_key: str | None = None
    for line in fm_raw.splitlines():
        if re.match(r"^\s*-\s+", line) and cur_list_key:
            lst = fm.setdefault(cur_list_key, [])
            if isinstance(lst, list):
                lst.append(line.strip()[1:].strip().strip('"').strip("'"))
            continue
        cur_list_key = None
        if ":" in line and not line.lstrip().startswith("#"):
            k, v = line.split(":", 1)
            k = k.strip()
            v = v.strip()
            if not v:
                cur_list_key = k
                fm[k] = []
            elif v.startswith("[") and v.endswith("]"):
                inner = v[1:-1].strip()
                fm[k] = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
            else:
                fm[k] = v.strip('"').strip("'")
    return fm, body.strip()


def load_beans_from_defs(defs_dir: pathlib.Path) -> dict[str, BeanRecord]:
    records: dict[str, BeanRecord] = {}
    children_map: dict[str, list[str]] = defaultdict(list)
    for md_path in sorted(defs_dir.glob("*.md")):
        txt = md_path.read_text(errors="replace")
        fm, body = parse_frontmatter(txt)
        bid = str(fm.get("id") or "").strip()
        if not bid:
            continue
        status = str(fm.get("status") or "").strip()
        btype = str(fm.get("type") or "task").strip()
        title = str(fm.get("title") or "").strip()
        parent_val = fm.get("parent", "")
        if isinstance(parent_val, list):
            parent = str(parent_val[0]).strip() if parent_val else ""
        else:
            parent = str(parent_val).strip()
        raw_blocked = fm.get("blocked_by", [])
        blocked_by = [str(x).strip() for x in raw_blocked] if isinstance(raw_blocked, list) else ([str(raw_blocked).strip()] if raw_blocked else [])
        raw_tags = fm.get("tags", [])
        tags = [str(x).strip() for x in raw_tags] if isinstance(raw_tags, list) else ([str(raw_tags).strip()] if raw_tags else [])
        records[bid] = BeanRecord(
            bean_id=bid,
            status=status,
            bean_type=btype,
            title=title,
            parent=parent,
            body=body,
            path=md_path,
            blocked_by=blocked_by,
            tags=tags,
        )
        if parent:
            children_map[parent].append(bid)
    for pid, kids in children_map.items():
        if pid in records:
            records[pid].children = sorted(kids)
    return records


def _match_known_beans_in_text(text: str, known_ids: set[str]) -> set[str]:
    """Match qou-XXXX / underscored bean IDs directly; require backticks for bare-word legacy IDs (e.g. `five`)."""
    hits: set[str] = set()
    for tok in TOKEN_RE.findall(text):
        if tok not in known_ids:
            continue
        if tok.startswith("qou-") or "_" in tok or any(ch.isdigit() for ch in tok):
            hits.add(tok)
        elif f"`{tok}`" in text:
            hits.add(tok)
    return hits


def extract_primary_beans_from_pr(
    pr_title: str,
    pr_body: str,
    commit_subjects: Iterable[str],
    known_ids: set[str],
) -> tuple[set[str], dict[str, list[str]]]:
    """Return (primary_candidate_ids, all_mention_lines_by_id)."""
    mention_lines: dict[str, list[str]] = defaultdict(list)
    primary: set[str] = set()

    # 1. PR title
    title_ids = _match_known_beans_in_text(pr_title, known_ids)
    is_lean_only_port = "(lean only)" in pr_title.lower()
    for tid in title_ids:
        mention_lines[tid].append(f"TITLE: {pr_title}")
        if not is_lean_only_port or len(title_ids) == 1:
            primary.add(tid)

    # 2. PR body lines
    for raw_line in (pr_body or "").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line_ids = _match_known_beans_in_text(line, known_ids)
        if not line_ids:
            continue
        for lid in line_ids:
            mention_lines[lid].append(f"BODY: {line}")
        if PRIMARY_BODY_LINE_RE.search(line):
            m_ctx = CONTEXT_ONLY_LINE_RE.search(line)
            if m_ctx:
                # Only beans appearing strictly before a context/sub-seam clause
                # (e.g. "resolves qou-6moa, qou-fadg, and leaf deliverables of qou-qint...")
                # or before a parenthetical "(parent epic ..., aggregating ...)" are primary targets.
                cut = m_ctx.start()
                paren = line.find("(")
                if 0 <= paren < cut and "resolves" not in line[paren:cut].lower():
                    cut = paren
                prefix = line[:cut]
                for lid in _match_known_beans_in_text(prefix, known_ids):
                    primary.add(lid)
            else:
                primary.update(line_ids)

    # 3. Commit subjects
    for subj in commit_subjects:
        s = subj.strip()
        if not s:
            continue
        c_ids = _match_known_beans_in_text(s, known_ids)
        for cid in c_ids:
            mention_lines[cid].append(f"COMMIT: {s}")
        if "(lean only)" in s.lower() or NON_CLOSING_COMMIT_PREFIX_RE.search(s):
            continue
        if len(c_ids) == 1:
            primary.update(c_ids)

    return primary, mention_lines


def evaluate_pr_beans(
    pr_number: int,
    merge_sha: str,
    pr_title: str,
    pr_body: str,
    commit_subjects: Iterable[str],
    uninstantiated_conjecture_classes: Iterable[str],
    records: dict[str, BeanRecord],
    force_beans: set[str] | None = None,
) -> list[BeanDecision]:
    """Pure classification core (unit-tested by --selftest)."""
    force_beans = force_beans or set()
    known_ids = set(records.keys())
    primary_ids, mention_lines = extract_primary_beans_from_pr(
        pr_title, pr_body, commit_subjects, known_ids
    )
    all_mentioned = set(mention_lines.keys()) | (force_beans & known_ids)
    conj_classes = list(uninstantiated_conjecture_classes)
    decisions: list[BeanDecision] = []

    for bid in sorted(all_mentioned):
        rec = records[bid]
        forced = bid in force_beans

        if rec.status in CLOSED_STATUSES:
            decisions.append(BeanDecision(bid, "SKIP_ALREADY_CLOSED", f"already {rec.status}", pr_number, merge_sha))
            continue

        if not forced and bid not in primary_ids:
            decisions.append(
                BeanDecision(bid, "SKIP_CONTEXT_ONLY", "mentioned only as context/parent/aggregated gap", pr_number, merge_sha)
            )
            continue

        open_kids = [k for k in rec.children if k in records and records[k].status in OPEN_STATUSES]
        if rec.bean_type == "epic" and not rec.children:
            # Also check prose `Child Beans` lists on epics whose children lack YAML `parent:` links.
            for body_line in rec.body.splitlines():
                if "child beans" in body_line.lower():
                    for cand in re.findall(r"\bqou-[a-z0-9]{4}\b", body_line):
                        if cand != bid and cand in records and records[cand].status in OPEN_STATUSES and cand not in open_kids:
                            open_kids.append(cand)
        open_blockers = [b for b in rec.blocked_by if b in records and records[b].status in OPEN_STATUSES]
        guard_tag_hits = sorted(set(rec.tags) & GUARD_TAGS)
        if not forced:
            if bid in NEVER_CLOSE:
                decisions.append(BeanDecision(bid, "SKIP_PROTECTED", "in NEVER_CLOSE standing-umbrella set", pr_number, merge_sha))
                continue
            if rec.bean_type == "milestone":
                decisions.append(BeanDecision(bid, "SKIP_MILESTONE", "milestone beans require manual closure", pr_number, merge_sha))
                continue
            if open_kids:
                decisions.append(
                    BeanDecision(
                        bid,
                        "SKIP_OPEN_CHILDREN",
                        f"{len(open_kids)} open child bean(s): {', '.join(open_kids[:5])}",
                        pr_number,
                        merge_sha,
                    )
                )
                continue
            if open_blockers:
                decisions.append(
                    BeanDecision(
                        bid,
                        "SKIP_BLOCKED_BY",
                        f"blocked_by open bean(s): {', '.join(open_blockers[:5])}",
                        pr_number,
                        merge_sha,
                    )
                )
                continue
            if guard_tag_hits:
                decisions.append(
                    BeanDecision(
                        bid,
                        "SKIP_TAG_GUARD",
                        f"guarded tag(s): {', '.join(guard_tag_hits)}",
                        pr_number,
                        merge_sha,
                    )
                )
                continue
            if OWNER_GATE_TITLE_RE.search(rec.title) or OWNER_GATE_BODY_RE.search(rec.body):
                decisions.append(
                    BeanDecision(bid, "SKIP_OWNER_GATED", "OWNER CALL / DECISION / do-not-close guard in bean", pr_number, merge_sha)
                )
                continue
            if CORPUS_SWEEP_TITLE_RE.search(rec.title):
                decisions.append(
                    BeanDecision(bid, "SKIP_CORPUS_SWEEP", "corpus-wide multi-file tracker title; verify 0 remaining before --force-bean", pr_number, merge_sha)
                )
                continue

            # Caveats in PR mentions
            caveat_hits = [ln for ln in mention_lines.get(bid, []) if OPEN_CAVEAT_RE.search(ln)]
            if caveat_hits:
                decisions.append(
                    BeanDecision(bid, "SKIP_OPEN_CAVEAT", f"caveat in PR: {caveat_hits[0][:120]}", pr_number, merge_sha)
                )
                continue

            # Caveats in the bean's own body tail (e.g. "Kept in-progress", "Bean stays open", "Open / next:")
            tail_m = BEAN_TAIL_OPEN_RE.search(rec.body[-2500:])
            if tail_m:
                snippet = " ".join(tail_m.group(0).split())
                decisions.append(
                    BeanDecision(bid, "SKIP_BEAN_BODY_OPEN", f"bean body tail notes still open: {snippet!r}", pr_number, merge_sha)
                )
                continue

            # Rule 13a: uninstantiated conjecture/hypothesis class introduced in PR's Lean files
            if conj_classes:
                decisions.append(
                    BeanDecision(
                        bid,
                        "SKIP_RULE_13A_CONJECTURE",
                        f"PR Lean declares 0-instance conjecture/hypothesis class: {', '.join(conj_classes[:3])}",
                        pr_number,
                        merge_sha,
                    )
                )
                continue

        decisions.append(BeanDecision(bid, "CLOSE", "verified completed on origin/main", pr_number, merge_sha))

    return decisions


def find_drained_parent_epics(
    newly_closed_ids: set[str],
    records: dict[str, BeanRecord],
    pr_number: int,
    merge_sha: str,
) -> list[BeanDecision]:
    """Check if closing `newly_closed_ids` drained the last open child of any parent epic."""
    parent_candidates = {
        records[bid].parent
        for bid in newly_closed_ids
        if bid in records and records[bid].parent in records
    }
    epic_decisions: list[BeanDecision] = []
    for pid in sorted(parent_candidates):
        prec = records[pid]
        if prec.status in CLOSED_STATUSES or pid in NEVER_CLOSE or prec.bean_type != "epic":
            continue
        if not prec.children:
            continue
        remaining_open = [
            k for k in prec.children
            if k in records and k not in newly_closed_ids and records[k].status in OPEN_STATUSES
        ]
        if remaining_open:
            continue
        if OWNER_GATE_TITLE_RE.search(prec.title) or OWNER_GATE_BODY_RE.search(prec.body) or OPEN_CAVEAT_RE.search(prec.body[-600:]):
            epic_decisions.append(
                BeanDecision(pid, "SKIP_EPIC_CAVEAT", "all children closed, but epic body carries open caveat", pr_number, merge_sha)
            )
            continue
        epic_decisions.append(
            BeanDecision(pid, "CLOSE", f"all {len(prec.children)} child bean(s) completed/scrapped", pr_number, merge_sha)
        )
    return epic_decisions


def detect_uninstantiated_conjecture_classes(main_wt: pathlib.Path, changed_files: Iterable[str]) -> list[str]:
    uninstantiated: list[str] = []
    for rel in changed_files:
        if not rel.endswith(".lean"):
            continue
        p = main_wt / rel
        if not p.exists():
            continue
        txt = p.read_text(errors="replace")
        for cls_name in CONJECTURE_CLASS_DECL_RE.findall(txt):
            # Check if any `instance ... : <cls_name>` exists in folio/
            grep = subprocess.run(
                ["git", "-C", str(main_wt), "grep", "-E", rf"\binstance\b.*:\s*.*{re.escape(cls_name)}\b", "origin/main", "--", "folio/"],
                capture_output=True,
                text=True,
            )
            if grep.returncode != 0 or not grep.stdout.strip():
                uninstantiated.append(cls_name)
    return sorted(set(uninstantiated))


def resolve_paths(args: argparse.Namespace) -> tuple[pathlib.Path, pathlib.Path, pathlib.Path]:
    script_repo = pathlib.Path(__file__).resolve().parent.parent
    main_wt = pathlib.Path(args.main_worktree).resolve() if args.main_worktree else script_repo

    if args.beans_cwd:
        beans_cwd = pathlib.Path(args.beans_cwd).resolve()
    elif pathlib.Path("/Users/litlfred/space_cats/qou/.beans.yml").exists():
        beans_cwd = pathlib.Path("/Users/litlfred/space_cats/qou")
    else:
        beans_cwd = main_wt

    if args.beans_worktree:
        beans_wt = pathlib.Path(args.beans_worktree).resolve()
    elif os.environ.get("QOU_BEANS_WORKTREE"):
        beans_wt = pathlib.Path(os.environ["QOU_BEANS_WORKTREE"]).resolve()
    elif (beans_cwd / "beans").exists():
        beans_dir_resolved = (beans_cwd / "beans").resolve()
        # Usually /private/tmp/qou-beans-latest/beans -> git root is parent
        beans_wt = beans_dir_resolved.parent if (beans_dir_resolved.parent / ".git").exists() else beans_dir_resolved
    else:
        beans_wt = pathlib.Path("/private/tmp/qou-beans-latest")

    return main_wt, beans_cwd, beans_wt


def parse_pr_numbers(pr_list: list[int] | None, prs_csv: str | None) -> list[int]:
    nums: list[int] = []
    for n in pr_list or []:
        nums.append(int(n))
    if prs_csv:
        for tok in re.split(r"[,\s]+", prs_csv.strip()):
            tok = tok.lstrip("#").strip()
            if tok:
                nums.append(int(tok))
    seen: set[int] = set()
    ordered: list[int] = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            ordered.append(n)
    return ordered


def _selftest() -> int:
    fails: list[str] = []

    def check(name: str, cond: bool) -> None:
        print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
        if not cond:
            fails.append(name)

    dummy_path = pathlib.Path("/tmp/dummy.md")
    recs = {
        "qou-leaf": BeanRecord("qou-leaf", "in-progress", "task", "Fix leaf bug", "qou-epic", "Clean leaf body.", dummy_path),
        "qou-done": BeanRecord("qou-done", "completed", "task", "Already done", "qou-epic", "Done.", dummy_path),
        "qou-epic": BeanRecord("qou-epic", "in-progress", "epic", "Batch Epic", "", "Clean epic.", dummy_path, ["qou-leaf", "qou-done"]),
        "qou-open": BeanRecord("qou-open", "in-progress", "task", "GAP: open item", "", "Open gap.", dummy_path),
        "qou-aggr": BeanRecord("qou-aggr", "todo", "task", "GAP: legacy aggregated", "", "Open legacy.", dummy_path),
        "qou-ownr": BeanRecord("qou-ownr", "in-progress", "task", "OWNER CALL: pick chart", "", "Needs owner.", dummy_path),
        "qou-s028": BeanRecord("qou-s028", "in-progress", "epic", "Umbrella", "", "Standing.", dummy_path),
    }

    # 1. Clean leaf closes, aggregated/context & caveat & protected & owner-call skip
    decs = evaluate_pr_beans(
        pr_number=9999,
        merge_sha="abcdef1234567890abcdef1234567890abcdef12",
        pr_title="feat(test): land leaf fix (qou-leaf, qou-open, qou-ownr)",
        pr_body=(
            "## Summary (`qou-leaf`, parent epic `qou-s028`, aggregating `qou-aggr`)\n"
            "- **qou-leaf**: Delivered complete fix.\n"
            "- `qou-open` remains open per Rule 13a.\n"
        ),
        commit_subjects=["feat: implement qou-leaf"],
        uninstantiated_conjecture_classes=[],
        records=recs,
    )
    by_id = {d.bean_id: d for d in decs}
    check("clean leaf marked CLOSE", by_id["qou-leaf"].action == "CLOSE")
    check("open-caveat bean skipped", by_id["qou-open"].action == "SKIP_OPEN_CAVEAT")
    check("aggregated legacy gap skipped as context-only", by_id["qou-aggr"].action == "SKIP_CONTEXT_ONLY")
    check("OWNER CALL bean skipped", by_id["qou-ownr"].action == "SKIP_OWNER_GATED")
    check("NEVER_CLOSE standing epic skipped", by_id["qou-s028"].action == "SKIP_CONTEXT_ONLY")

    # 2. Drained parent epic closes once its last open child (`qou-leaf`) closes
    epic_decs = find_drained_parent_epics({"qou-leaf"}, recs, 9999, "abcdef1234567890abcdef1234567890abcdef12")
    check("100%-drained parent epic marked CLOSE", len(epic_decs) == 1 and epic_decs[0].bean_id == "qou-epic" and epic_decs[0].action == "CLOSE")

    # 3. Rule 13a 0-instance conjecture class blocks auto-closure
    decs_13a = evaluate_pr_beans(
        pr_number=9998,
        merge_sha="abcdef1234567890abcdef1234567890abcdef12",
        pr_title="feat: conditional horizon theorem (qou-leaf)",
        pr_body="## Summary (`qou-leaf`)\nProves theorem conditional on conjecture.",
        commit_subjects=["feat: qou-leaf"],
        uninstantiated_conjecture_classes=["LCQHorizonPunctureAreaConjecture"],
        records=recs,
    )
    check("Rule 13a conjecture class blocks CLOSE", decs_13a[0].action == "SKIP_RULE_13A_CONJECTURE")

    # 4. Multi-bean `(Lean only)` port commit does NOT auto-close Python/research beans
    decs_lean_port = evaluate_pr_beans(
        pr_number=9997,
        merge_sha="abcdef1234567890abcdef1234567890abcdef12",
        pr_title="port #8311 (Lean only): theorems for qou-leaf, qou-open",
        pr_body="Ports Lean file only.",
        commit_subjects=["port #8311 (Lean only): theorems for qou-leaf, qou-open"],
        uninstantiated_conjecture_classes=[],
        records=recs,
    )
    check("multi-bean (Lean only) port skipped", all(d.action != "CLOSE" for d in decs_lean_port))

    # 5. Blocked-by, guarded tags, prose epic Child Beans, bean-body tail caveats, and bare English word `five`
    recs2 = dict(recs)
    recs2["five"] = BeanRecord("five", "completed", "task", "Legacy word bean", "", "Done.", dummy_path)
    recs2["qou-blkd"] = BeanRecord("qou-blkd", "todo", "task", "Blocked leaf", "", "Clean.", dummy_path, blocked_by=["qou-open"])
    recs2["qou-tagd"] = BeanRecord("qou-tagd", "in-progress", "task", "Tagged leaf", "", "Clean.", dummy_path, tags=["needs-owner-ok"])
    recs2["qou-tail"] = BeanRecord("qou-tail", "in-progress", "task", "Partial delivery", "", "Delivered clasp. Kept `in-progress` on quantitative gap.", dummy_path)
    recs2["qou-pepc"] = BeanRecord("qou-pepc", "in-progress", "epic", "Prose epic", "", "**Child Beans (2):** `qou-open`, `qou-done`", dummy_path)
    decs_extra = evaluate_pr_beans(
        pr_number=9996,
        merge_sha="abcdef1234567890abcdef1234567890abcdef12",
        pr_title="feat: test five guards (qou-blkd, qou-tagd, qou-tail, qou-pepc)",
        pr_body="Closes five items.",
        commit_subjects=[],
        uninstantiated_conjecture_classes=[],
        records=recs2,
    )
    by_id2 = {d.bean_id: d for d in decs_extra}
    check("bare English word 'five' not matched as bean ID", "five" not in by_id2)
    check("blocked_by open bean skipped", by_id2["qou-blkd"].action == "SKIP_BLOCKED_BY")
    check("needs-owner-ok tag skipped", by_id2["qou-tagd"].action == "SKIP_TAG_GUARD")
    check("bean-body tail 'Kept in-progress' skipped", by_id2["qou-tail"].action == "SKIP_BEAN_BODY_OPEN")
    check("prose Child Beans epic skipped while child open", by_id2["qou-pepc"].action == "SKIP_OPEN_CHILDREN")

    # 6. Sub-deliverable clause ("resolves qou-leaf, and leaf deliverables of qou-open") closes only qou-leaf
    decs_sub = evaluate_pr_beans(
        pr_number=9995,
        merge_sha="abcdef1234567890abcdef1234567890abcdef12",
        pr_title="feat(batch): backlog drain",
        pr_body="Beans: resolves `qou-leaf`, and leaf deliverables of `qou-open`.",
        commit_subjects=[],
        uninstantiated_conjecture_classes=[],
        records=recs,
    )
    by_id3 = {d.bean_id: d for d in decs_sub}
    check("sub-deliverable clause closes full bean and skips partial leaf-deliverable bean",
          by_id3["qou-leaf"].action == "CLOSE" and by_id3["qou-open"].action == "SKIP_CONTEXT_ONLY")

    print(f"\nselftest: {len(fails)} failure(s)")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pr", type=int, action="append", help="Merged PR number (repeatable)")
    ap.add_argument("--prs", type=str, help="Comma-separated merged PR numbers, e.g. 9245,9247,9282")
    ap.add_argument("--repo", default="litlfred/qou", help="GitHub owner/repo (default: litlfred/qou)")
    ap.add_argument("--main-worktree", help="Path to qou git worktree for origin/main ancestor checks")
    ap.add_argument("--beans-cwd", help="Directory containing .beans.yml for `beans` CLI")
    ap.add_argument("--beans-worktree", help="Git worktree of cat/cat-harness/beans")
    ap.add_argument("--force-bean", action="append", default=[], help="Explicitly force-close a verified bean ID")
    ap.add_argument("--dry-run", action="store_true", help="Inspect and classify without mutating or pushing")
    ap.add_argument("--no-push", action="store_true", help="Update beans locally without committing/pushing")
    ap.add_argument("--selftest", action="store_true", help="Run built-in precision & safety guard unit tests")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    pr_numbers = parse_pr_numbers(args.pr, args.prs)
    if not pr_numbers:
        ap.error("Provide at least one --pr <N> or --prs <N1,N2,...> (or --selftest).")

    main_wt, beans_cwd, beans_wt = resolve_paths(args)
    defs_dir = beans_wt / "beans" / "defs"
    if not defs_dir.is_dir():
        print(f"ERROR: beans defs directory not found at {defs_dir}", file=sys.stderr)
        return 2

    # Targeted refspec fetch of origin/main (never bare `git fetch origin`).
    subprocess.run(
        ["git", "-C", str(main_wt), "fetch", "--no-tags", "origin", "+refs/heads/main:refs/remotes/origin/main"],
        check=True,
    )
    if not args.dry_run:
        subprocess.run(
            ["git", "-C", str(beans_wt), "pull", "--rebase", "origin", "cat/cat-harness/beans"],
            check=True,
        )

    records = load_beans_from_defs(defs_dir)
    force_set = set(args.force_bean)
    all_to_close: list[BeanDecision] = []
    closed_so_far: set[str] = set()

    for pr_num in pr_numbers:
        gh_res = subprocess.run(
            [
                "gh", "pr", "view", str(pr_num), "-R", args.repo,
                "--json", "number,title,body,state,mergedAt,mergeCommit,commits,files",
            ],
            capture_output=True,
            text=True,
            check=True,
        )
        pr_data = json.loads(gh_res.stdout)
        state = pr_data.get("state")
        merge_oid = (pr_data.get("mergeCommit") or {}).get("oid", "")
        if state != "MERGED" or not merge_oid:
            print(f"ERROR: PR #{pr_num} is {state!r} (not MERGED on GitHub); refusing bean closure.", file=sys.stderr)
            return 1

        anc = subprocess.run(
            ["git", "-C", str(main_wt), "merge-base", "--is-ancestor", merge_oid, "origin/main"],
            capture_output=True,
        )
        if anc.returncode != 0:
            print(
                f"ERROR: PR #{pr_num} mergeCommit {merge_oid[:11]} is not an ancestor of origin/main!",
                file=sys.stderr,
            )
            return 1

        commit_subjects = [
            (c.get("messageHeadline") or "") for c in (pr_data.get("commits") or [])
        ]
        changed_files = [(f.get("path") or "") for f in (pr_data.get("files") or [])]
        conj_classes = detect_uninstantiated_conjecture_classes(main_wt, changed_files)

        decisions = evaluate_pr_beans(
            pr_number=pr_num,
            merge_sha=merge_oid,
            pr_title=pr_data.get("title") or "",
            pr_body=pr_data.get("body") or "",
            commit_subjects=commit_subjects,
            uninstantiated_conjecture_classes=conj_classes,
            records=records,
            force_beans=force_set,
        )
        print(f"=== PR #{pr_num} ({merge_oid[:11]}): {pr_data.get('title','')} ===")
        if not decisions:
            print("  (no bean IDs referenced)")
        for d in decisions:
            print(f"  [{d.action:24s}] {d.bean_id:10s} — {d.reason}")
            if d.action == "CLOSE" and d.bean_id not in closed_so_far:
                closed_so_far.add(d.bean_id)
                all_to_close.append(d)
                records[d.bean_id].status = "completed"

        epic_decisions = find_drained_parent_epics(closed_so_far, records, pr_num, merge_oid)
        for ed in epic_decisions:
            print(f"  [{ed.action:24s}] {ed.bean_id:10s} (parent epic) — {ed.reason}")
            if ed.action == "CLOSE" and ed.bean_id not in closed_so_far:
                closed_so_far.add(ed.bean_id)
                all_to_close.append(ed)
                records[ed.bean_id].status = "completed"

    if not all_to_close:
        print("\n0 beans eligible for automatic closure.")
        return 0

    if args.dry_run:
        print(f"\n[DRY-RUN] Would mark {len(all_to_close)} bean(s) completed: {[d.bean_id for d in all_to_close]}")
        return 0

    for d in all_to_close:
        note = f"Closed post-merge: landed on origin/main in PR #{d.pr_number} ({d.merge_sha[:11]})."
        subprocess.run(
            ["beans", "update", d.bean_id, "--status", "completed", "--body-append", note],
            cwd=str(beans_cwd),
            check=True,
        )

    subprocess.run(["beans", "check"], cwd=str(beans_cwd), check=True)
    check_sh = main_wt / "scripts" / "check-beans.sh"
    if check_sh.exists():
        subprocess.run(["bash", str(check_sh), "--quiet"], cwd=str(beans_cwd), check=True)

    if args.no_push:
        print(f"\nUpdated {len(all_to_close)} bean(s) locally (--no-push): {[d.bean_id for d in all_to_close]}")
        return 0

    status_out = subprocess.run(
        ["git", "-C", str(beans_wt), "status", "--porcelain"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    if not status_out:
        print("\nBeans worktree already clean; nothing to commit.")
        return 0

    subprocess.run(["git", "-C", str(beans_wt), "add", "beans/defs"], check=True)
    pr_tag = ",".join(f"#{n}" for n in pr_numbers)
    bean_tag = ", ".join(d.bean_id for d in all_to_close[:12])
    if len(all_to_close) > 12:
        bean_tag += f" (+{len(all_to_close) - 12} more)"
    commit_msg = f"chore(beans): close merged PR beans ({pr_tag}): {bean_tag}"
    subprocess.run(
        [
            "git", "-C", str(beans_wt),
            "-c", "user.name=litlfred",
            "-c", "user.email=litlfred@users.noreply.github.com",
            "commit", "-m", commit_msg,
        ],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(beans_wt), "pull", "--rebase", "origin", "cat/cat-harness/beans"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(beans_wt), "push", "origin", "HEAD:cat/cat-harness/beans"],
        check=True,
    )
    print(f"\nClosed & pushed {len(all_to_close)} bean(s) to origin/cat/cat-harness/beans.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
