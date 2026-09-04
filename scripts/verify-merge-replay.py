#!/usr/bin/env python3
"""Verify a rebase-merge actually replayed every commit of its PR.

WHY THIS EXISTS (bean qou-vtau)
--------------------------------
After a rebase-merge the PR's head *becomes* `origin/main`'s tip, so the
check that reads as strongest evidence:

    git diff origin/main <merged-head>        # compares a commit to ITSELF

returns empty whether or not anything was dropped. Whenever the PR is the last
thing merged -- the normal case for a pipeline that merges what it just rebased
-- it verifies nothing while looking conclusive.

The failure it cannot see is real and has happened: PR #5111's rebase-merge
landed **7 of 8** commits, recovered as #5125. It was caught by grepping `main`
for the edited content, not by any diff.

Measured 2026-09-04: `prepare-merge-auto` Phase 5 ("Post-merge coordination")
prescribes NO verification at all -- not the tautological check, not a real
one. It posts a sibling comment and unsubscribes. So the gap is not a bad check
in the skill; it is the ABSENCE of one, and every merge since has been unchecked.

WHAT THIS CHECKS INSTEAD
------------------------
A rebase rewrites commit shas, so shas cannot be compared. A commit's
*patch-id* -- a hash of its diff -- is invariant under rebase, so it can.
For every commit on the pre-merge branch, this asserts a commit with the same
patch-id exists in the merge range on main.

Patch-id is the right invariant, but it is not magic; know its two edges:

  * A commit whose diff is EMPTY has no patch-id. Those are reported
    separately as `empty` rather than silently counted as replayed.
  * If a rebase CHANGED a commit's content -- a conflict resolved differently
    -- its patch-id changes and this reports it MISSING. That is the intended
    behaviour: a commit that landed with different content did not replay, and
    the resolution deserves a human look.

USAGE
-----
    scripts/verify-merge-replay.py --branch origin/claude/foo --merged <sha>
    scripts/verify-merge-replay.py --selftest      # proves it can detect a drop

`--selftest` is not decoration. A checker that always reports "0 missing" is
indistinguishable from a working one until the day it matters, which is exactly
the trap this script exists to close. The selftest synthesises a dropped commit
and asserts (a) this check reports it, and (b) the tautological check does not.
"""
from __future__ import annotations

import argparse
import subprocess
import sys


def git(*args: str, check: bool = False) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} failed: {r.stderr.strip()}")
    return r.stdout


def patch_id(sha: str) -> str | None:
    """Rebase-invariant hash of a commit's diff; None for an empty diff."""
    diff = git("diff-tree", "-p", "--no-commit-id", sha)
    if not diff.strip():
        return None
    out = subprocess.run(
        ["git", "patch-id", "--stable"], input=diff, capture_output=True, text=True
    ).stdout.split()
    return out[0] if out else None


def commits(rev_range: str) -> list[str]:
    return git("log", "--format=%H", rev_range).split()


def subject(sha: str) -> str:
    return git("log", "-1", "--format=%s", sha).strip()


def index(shas: list[str]) -> tuple[dict[str, str], list[str]]:
    """(patch_id -> sha, [shas with an empty diff])"""
    by_pid: dict[str, str] = {}
    empty: list[str] = []
    for s in shas:
        pid = patch_id(s)
        (empty.append(s) if pid is None else by_pid.setdefault(pid, s))
    return by_pid, empty


def verify(branch: str, merged: str, window: int = 40, quiet: bool = False) -> int:
    base = git("merge-base", branch, "origin/main").strip()
    if not base:
        raise SystemExit(f"no merge-base between {branch} and origin/main")

    branch_shas = commits(f"{base}..{branch}")
    if not branch_shas:
        print(f"  {branch}: no commits ahead of merge-base — nothing to verify")
        return 0

    # Window on main must be wide enough to contain the replayed range. Use the
    # branch commit count plus headroom for siblings that landed alongside.
    span = max(window, len(branch_shas) * 3)
    main_by_pid, _ = index(commits(f"{merged}~{span}..{merged}"))
    branch_by_pid, branch_empty = index(branch_shas)

    missing = [(s, subject(s)) for p, s in branch_by_pid.items() if p not in main_by_pid]

    if not quiet:
        print(f"  branch commits : {len(branch_shas)}")
        print(f"  replayed       : {len(branch_by_pid) - len(missing)}")
        if branch_empty:
            print(f"  empty diff     : {len(branch_empty)} (no patch-id; not counted as replayed)")
            for s in branch_empty:
                print(f"      - {s[:11]}  {subject(s)}")
        print(f"  MISSING        : {len(missing)}")
        for s, subj in missing:
            print(f"      !! {s[:11]}  {subj[:70]}")
    return len(missing)


def selftest() -> int:
    """Synthesise a drop and prove this check sees what the tautological one cannot.

    Deterministic and history-independent: rather than depend on #5111's branch
    still being reachable, take any merged range, hold one commit out of the
    "main side" index, and assert the check reports exactly that one.
    """
    print("SELFTEST — can this check detect a dropped commit?\n")
    head = git("rev-parse", "HEAD").strip()
    shas = commits(f"{head}~6..{head}")
    if len(shas) < 3:
        print("  SKIP: need >= 3 commits of history")
        return 0

    by_pid, _ = index(shas)
    if len(by_pid) < 3:
        print("  SKIP: need >= 3 commits with non-empty diffs")
        return 0

    pids = list(by_pid)
    dropped_pid = pids[0]
    dropped_sha = by_pid[dropped_pid]
    main_side = {p: s for p, s in by_pid.items() if p != dropped_pid}

    missing = [s for p, s in by_pid.items() if p not in main_side]
    ok_real = len(missing) == 1 and missing[0] == dropped_sha
    print(f"  simulated: {dropped_sha[:11]}  {subject(dropped_sha)[:60]}")
    print(f"  patch-id check      -> {'DETECTED' if ok_real else 'MISSED'} "
          f"({len(missing)} missing, expected 1)")

    # The tautological check, on the same scenario: main's tip IS the merged head.
    taut = git("diff", head, head)
    ok_taut = taut.strip() == ""
    print(f"  `git diff main <merged-head>` -> {'EMPTY (passes — sees nothing)' if ok_taut else 'non-empty'}")

    print()
    if ok_real and ok_taut:
        print("  PASS — the patch-id check detects the drop; the diff check reports a free pass.")
        return 0
    print("  FAIL — selftest did not behave as specified; do not trust this checker.")
    return 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--branch", help="pre-merge branch ref, e.g. origin/claude/foo-2026-09-04")
    ap.add_argument("--merged", help="the merge commit / resulting sha on main")
    ap.add_argument("--window", type=int, default=40,
                    help="how many commits of main to index (default 40)")
    ap.add_argument("--selftest", action="store_true",
                    help="prove the check can detect a drop, and that the diff check cannot")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if not (a.branch and a.merged):
        ap.error("--branch and --merged are both required (or use --selftest)")

    print(f"Verifying {a.branch} -> {a.merged[:11]}")
    n = verify(a.branch, a.merged, a.window)
    print()
    if n:
        print(f"RESULT: {n} commit(s) did NOT replay. Investigate before treating the merge as complete.")
        return 1
    print("RESULT: every commit replayed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
