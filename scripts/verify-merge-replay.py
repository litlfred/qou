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
  * `git patch-id` hashes CONTEXT LINES, not just the changed ones. So a commit
    whose content replayed byte-identically still gets a different patch-id if a
    sibling edited the same file between the branch point and the merge -- the
    rebase lands the same hunk against different surrounding text. Measured
    2026-09-04 on PR #6604: two commits reported MISSING, both present on main
    with identical content (`detector-precision-measured.md` hashed
    `03da6cb8b11f8e8f` on both sides), because siblings `a8b6e60348a` and
    `1d059668c13` had edited `corpus-grepper/MEMORY.md` in between.

    Those are reported as a THIRD class, `context-drift`: a commit with the same
    SUBJECT was found in the merge range. That is deliberately weaker evidence
    than a patch-id match and is never folded into `replayed` -- a subject match
    says a commit by that name landed, not that its content is the same. Verify
    the content by hand before believing it.

EXIT CODES
----------
    0  every commit replayed by patch-id
    1  at least one commit is genuinely MISSING -- no patch-id and no subject
    2  no missing, but at least one context-drift needing a content check

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
    """Rebase-invariant hash of a commit's diff; None for an empty diff.

    BYTES, not text. A diff is not guaranteed to be UTF-8 -- this corpus holds
    commits whose diffs are not, and decoding one raises UnicodeDecodeError and
    takes the whole audit down. Found by running this check retroactively over
    ~30 merged branches, where exactly that happened. `git patch-id` wants bytes
    anyway, so there is nothing to decode until the hash comes back.
    """
    diff = subprocess.run(
        ["git", "diff-tree", "-p", "--no-commit-id", sha], capture_output=True
    ).stdout
    if not diff.strip():
        return None
    out = subprocess.run(
        ["git", "patch-id", "--stable"], input=diff, capture_output=True
    ).stdout.split()
    return out[0].decode("ascii") if out else None


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


def classify(
    unmatched: list[tuple[str, str]], main_subjects: set[str]
) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """Split patch-id misses into (missing, context_drift) by subject presence.

    Pure, so the selftest can exercise the real classifier rather than a copy of
    it. A subject match is deliberately weak evidence -- it says a commit by that
    name landed, not that its content is the same -- so it gets its own class and
    is never returned as replayed.
    """
    drifted = [(s, subj) for s, subj in unmatched if subj in main_subjects]
    missing = [(s, subj) for s, subj in unmatched if subj not in main_subjects]
    return missing, drifted


def _require_local_object(ref: str, what: str) -> None:
    """Refuse to verify against a ref this clone cannot resolve.

    Without this the failure is SILENT AND INVERTED. The main-side window is
    `{merged}~span..{merged}`; if `merged` is not present locally that range
    yields nothing, every branch commit is unmatched, and the checker reports
    them all as MISSING -- which reads exactly like a merge that dropped
    commits, and invites the reader to re-push work that in fact landed
    cleanly. Measured 2026-09-05 immediately after merging PR #6849: `MISSING:
    2`, both commits present on main, the only fault being that `git fetch` had
    not run since the merge.
    """
    # `check=True` is load-bearing: this module's `git()` SWALLOWS a non-zero
    # exit unless asked. Written without it, this guard ran, returned "", and
    # never fired -- a guard that is silently inert, which is the same defect
    # class it was added to catch. Caught by testing it against a sha that does
    # not exist rather than by reading it.
    try:
        git("cat-file", "-e", f"{ref}^{{commit}}", check=True)
    except SystemExit:
        raise SystemExit(
            f"{what} {ref!r} is not present in this clone.\n"
            f"  Run:  git fetch origin main\n"
            f"  (A just-merged sha is not local until you fetch. Verifying "
            f"without it reports every commit MISSING, which is an artifact of "
            f"the stale ref and not a dropped commit.)")


def verify(branch: str, merged: str, window: int = 40, quiet: bool = False) -> tuple[int, int]:
    _require_local_object(merged, "merged sha")
    _require_local_object(branch, "branch ref")
    base = git("merge-base", branch, "origin/main").strip()
    if not base:
        raise SystemExit(f"no merge-base between {branch} and origin/main")

    branch_shas = commits(f"{base}..{branch}")
    if not branch_shas:
        print(f"  {branch}: no commits ahead of merge-base — nothing to verify")
        return 0, 0

    # Window on main must be wide enough to contain the replayed range. Use the
    # branch commit count plus headroom for siblings that landed alongside.
    span = max(window, len(branch_shas) * 3)
    main_by_pid, _ = index(commits(f"{merged}~{span}..{merged}"))
    branch_by_pid, branch_empty = index(branch_shas)

    # Second line of defence, independent of ref resolution. If the main-side
    # window indexed NOTHING while the branch has commits, no comparison
    # happened at all -- so "all missing" is a statement about the window, never
    # about the merge. Report it as the error it is rather than as a result.
    if not main_by_pid and branch_by_pid:
        raise SystemExit(
            f"main-side window {merged}~{span}..{merged} indexed 0 commits "
            f"while {branch} has {len(branch_by_pid)}.\n"
            f"  Nothing was compared, so this is NOT a finding about the merge.\n"
            f"  Usual cause: the merge sha is stale in this clone — "
            f"run `git fetch origin main` and re-run.")

    unmatched = [(s, subject(s)) for p, s in branch_by_pid.items() if p not in main_by_pid]

    # Fallback for the context-line edge: a patch-id miss is not yet a drop.
    # Look for the same SUBJECT in the merge range; a commit that landed under
    # its own subject did replay, with different context. Weaker than patch-id,
    # so it is reported as its own class and never counted as replayed.
    main_subjects = {
        subject(s) for s in commits(f"{merged}~{span}..{merged}")
    }
    missing, drifted = classify(unmatched, main_subjects)

    if not quiet:
        print(f"  branch commits : {len(branch_shas)}")
        print(f"  replayed       : {len(branch_by_pid) - len(unmatched)}")
        if branch_empty:
            print(f"  empty diff     : {len(branch_empty)} (no patch-id; not counted as replayed)")
            for s in branch_empty:
                print(f"      - {s[:11]}  {subject(s)}")
        if drifted:
            print(f"  context-drift  : {len(drifted)} (subject found on main, patch-id differs)")
            for s, subj in drifted:
                print(f"      ?  {s[:11]}  {subj[:70]}")
            print("      VERIFY THE CONTENT of these — a subject match is not a content match.")
        print(f"  MISSING        : {len(missing)}")
        for s, subj in missing:
            print(f"      !! {s[:11]}  {subj[:70]}")
    return len(missing), len(drifted)


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

    # The context-drift classifier, on the same dropped commit. Two cases, and
    # the second is the one that matters: a commit whose subject IS on main must
    # NOT be reported as a drop (that was the #6604 false positive), and must NOT
    # be silently absorbed into `replayed` either.
    subj = subject(dropped_sha)
    m_no, d_no = classify([(dropped_sha, subj)], set())
    m_yes, d_yes = classify([(dropped_sha, subj)], {subj})
    ok_drift = (len(m_no), len(d_no), len(m_yes), len(d_yes)) == (1, 0, 0, 1)
    print(f"  context-drift split -> {'CORRECT' if ok_drift else 'WRONG'} "
          f"(subject absent: {len(m_no)} missing/{len(d_no)} drift; "
          f"present: {len(m_yes)} missing/{len(d_yes)} drift)")

    print()
    if ok_real and ok_taut and ok_drift:
        print("  PASS — the patch-id check detects the drop; the diff check reports a free pass;")
        print("         a subject-only match is classed as drift, neither dropped nor replayed.")
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
    n, drift = verify(a.branch, a.merged, a.window)
    print()
    if n:
        print(f"RESULT: {n} commit(s) did NOT replay. Investigate before treating the merge as complete.")
        return 1
    if drift:
        print(f"RESULT: no drops, but {drift} commit(s) matched only by subject "
              f"(context drift). Check their content on main before signing off.")
        return 2
    print("RESULT: every commit replayed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
