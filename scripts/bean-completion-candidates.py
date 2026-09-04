#!/usr/bin/env python3
"""Open beans with recent related activity — worth OPENING, not a staleness list.

MEASURED PRECISION 2 IN 12. Read the caveat block below before quoting this.

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

  * **DELIBERATELY PARKED.** `qou-mln9` reads "Left `todo` deliberately ...
    Closing is the author's call." Not stale -- correctly parked, reason stated.
    No commit-message heuristic can tell a parked bean from a forgotten one,
    because the difference is intent and lives in the body.

**MEASURED PRECISION: 2 in 12, on the full high-priority list.** An earlier
version of this docstring said "~4 in 10 false positives" -- estimated from
subjects. Reading all twelve bodies gives TEN false positives: only `qou-vtau`
and `qou-w2vy` were genuinely stale, with `qou-c1ln` arguable.

So this is NOT a staleness list. It is a "beans with related recent activity,
worth opening" list. That is still worth twelve reads if it prevents one
re-derivation -- on the day it was written it would have prevented two -- but it
is a much smaller claim than the one this script shipped with.

**A better detector cannot be built from commit messages.** All four
false-positive classes are semantic and live in the bean body or the author's
intent. The check that works is an agent reading the bean.

THE OTHER QUESTION AN AGENT ACTUALLY HAS
----------------------------------------
"Is this done?" is only half of "can I pick this up?". The other half is
"is someone on it right now?", and that one a commit date DOES answer.

A bean whose id appears in any commit within the last few hours is presumed
CLAIMED, not stale, and is flagged `[ACTIVE ...]`. Measured case: `qou-bg3w`
("Which element is Delta?") carries three commits from the same day, the newest
hours old -- a live session mid-analysis. Taking it would have duplicated
settled work, which AGENTS.md permits only for open-outcome research and
explicitly not for work with one right answer.

This is a cheap signal and a reliable one, in contrast to the completion
heuristic above: it asks only WHEN, never WHAT, so none of the four semantic
failure classes touch it.

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
import functools
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
_ACTIVE_HOURS = 12  # a bean named by a commit this recently MAY be claimed — see _landed


@functools.lru_cache(maxsize=None)
def _landed(sha: str) -> bool:
    """Is this commit already an ancestor of origin/main?

    WHY THIS EXISTS. The `[ACTIVE]` flag was purely AGE-based and told the
    reader "presume CLAIMED, do not take". Age alone cannot tell a sibling
    HOLDING a bean from a sibling who FINISHED it, and the two want opposite
    actions: an in-flight branch should be left alone, while a landed one is
    at least FREE to take.

    🛑 LANDED IS A "WHERE", NOT A "WHAT" -- and this docstring got that wrong
    first. It read "landed work is precisely the bean most worth taking,
    because closing it is all that is left". That is an unsupported claim
    about the WORK, and it is false often enough to mislead: `_landed` tests
    only whether one COMMIT is an ancestor of origin/main. In a repo running
    ~40 commits/hour, LANDED is close to "someone touched this recently and
    their touch merged".

    Measured 2026-09-04, three LANDED bodies grepped for closure language:

        qou-6gf9   1 NOT CLOSED  1 not proved  2 open     1 still OPEN
        qou-k5r5   1 NOT DONE    1 NOT closed  1 NOT done  2 NOT proved
        qou-w3eg   1 NOT proved  2 OPEN        1 STILL OPEN 7 open

    All three are open research; a sibling PR (#6663) was actively working
    qou-6gf9 at the time. The agent that wrote the retracted sentence then
    repeated it in chat as "the LANDED beans are now a real, readable queue"
    and had to retract that too. The question "is the work done?" is the
    DEFAULT mode's, at a measured precision of 2 in 12 -- LANDED does not
    answer it and must not be printed as though it does.

    Measured 2026-09-04: `qou-9iwt` was flagged `[ACTIVE — commit 10h ago;
    presume CLAIMED, do not take]` on the strength of `1d75dfd31c3`, which was
    already MERGED TO MAIN. The flag suppressed the one bean whose work was
    demonstrably done. The session took it anyway and found two further defects
    the merged commit had not covered — so the flag would have cost that, and
    would have done it silently.
    """
    return subprocess.run(["git", "merge-base", "--is-ancestor", sha, "origin/main"],
                          capture_output=True).returncode == 0


_SHA = re.compile(r"[0-9a-f]{40}")


def newest_activity(entries, now):
    """(age_hours, sha, landed) for the newest commit naming a bean, or None.

    Factored out because BOTH modes need it and one of them got it wrong in a
    way no reader would see. `--active` unpacked the whole `(sha, iso, subj)`
    tuple and was correct; the default mode took `max()` over the TIMESTAMPS
    ALONE and then indexed `[0]` into the result — so it handed `_landed()` the
    single character `'2'` (the leading digit of an ISO date). `git merge-base
    --is-ancestor 2 origin/main` resolves nothing, returns non-zero, and
    `_landed` therefore answered False for EVERY bean. The `[IN FLIGHT — not on
    main]` flag was unconditionally on.

    Measured 2026-09-04 on the real tree: `qou-keu7`, `qou-f8lit` and `qou-cite`
    were all flagged "not on main" while their commits (`10eec50ef93`,
    `a28e4406490`, `f86729562a7`) had been verified on main the same hour. That
    is the exact failure `_landed` was added to fix, reproduced one function
    away in the same change that fixed it.

    The `_SHA` guard raises instead of silently answering False, because a
    False here is indistinguishable from a real in-flight commit.
    """
    newest = max(entries, key=lambda c: c[1], default=None)
    if not newest:
        return None
    sha, iso = newest[0], newest[1]
    if not _SHA.fullmatch(sha):
        raise ValueError(
            f"newest_activity expected a 40-hex sha, got {sha!r} — a caller is "
            "indexing into a max() taken over the wrong field")
    age_h = (now - datetime.datetime.fromisoformat(iso)).total_seconds() / 3600
    return age_h, sha, _landed(sha)


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


def any_commits(since: str) -> dict:
    """Every commit naming a bean — ALL REFS, not just merged history.

    `--all` is load-bearing and asymmetric with `done_commits` below, which
    deliberately stays on merged history. The two ask different questions:

      * done_commits — "has this bean's work LANDED?"  Only main can answer
        that, so an unmerged branch must NOT count.
      * any_commits  — "is a sibling WORKING on this?"  Only an UNMERGED
        branch can answer that, and a bare `git log` cannot see one.

    Measured 2026-09-04: a bare `git log` saw 500 commits in the last 12 h and
    `git log --all` saw 550, of which **50 were not on origin/main**. So the
    `[ACTIVE]` flag — which exists precisely to say "a live session holds this,
    do not take it" — was reading a population that BY CONSTRUCTION contains no
    in-flight work, and every bean it flagged was therefore landed. The flag was
    not merely imprecise; it could not be right.

    Note for a shallow clone: unfetched remote branches are invisible to `--all`
    too, so a clean IN FLIGHT bucket is weaker evidence than it looks. Fetch
    first if the answer matters.
    """
    """bean id -> [(sha, iso, subject)], ANY commit naming it. For the
    active-ownership signal, which does not care what the commit says."""
    log = subprocess.run(
        ["git", "log", "--all", f"--since={since}", "--format=%H%x01%cI%x01%s"],
        capture_output=True, text=True).stdout.splitlines()
    out = collections.defaultdict(list)
    for line in log:
        if line.count("\x01") != 2:
            continue
        sha, iso, subj = line.split("\x01", 2)
        for b in set(_ID.findall(subj)):
            out[b].append((sha, iso, subj))
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


def _selftest() -> int:
    """Exercise `newest_activity` in both directions and on the shipped bug.

    The bug this guards was invisible to every test that only asked "does the
    script run": it produced a plausible flag on every row, and a reader could
    not tell an always-on flag from a genuinely busy tree.
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    fails = []

    def check(name, cond):
        print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
        if not cond:
            fails.append(name)

    # origin/main's own tip is, by definition, an ancestor of origin/main.
    tip = subprocess.run(["git", "rev-parse", "origin/main"],
                         capture_output=True, text=True).stdout.strip()
    iso = now.isoformat()
    check("empty entries -> None", newest_activity([], now) is None)

    if _SHA.fullmatch(tip):
        got = newest_activity([(tip, iso, "tip")], now)
        check("origin/main tip reads LANDED", got is not None and got[2] is True)
        # A sha that cannot resolve must read NOT landed — the other direction,
        # which the old code answered correctly only by accident.
        dead = "0" * 40
        got = newest_activity([(dead, iso, "dead")], now)
        check("unresolvable sha reads NOT landed", got is not None and got[2] is False)
        # Newest wins, not first.
        older = (now - datetime.timedelta(hours=5)).isoformat()
        got = newest_activity([(dead, older, "old"), (tip, iso, "new")], now)
        check("picks the NEWEST entry", got is not None and got[1] == tip)
    else:
        check("origin/main resolves (skipped: no origin/main)", True)

    # The shipped bug: max() over timestamps alone, then [0]. Must RAISE, not
    # silently answer False.
    raised = False
    try:
        newest_activity([(iso[0], iso, "bug")], now)
    except ValueError:
        raised = True
    check("single-char sha RAISES instead of answering False", raised)

    print(f"\n{len(fails)} failure(s)")
    return 1 if fails else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true", help="every priority, not just high")
    ap.add_argument("--active", action="store_true",
                    help="instead: list open beans with a commit in the last "
                         f"{_ACTIVE_HOURS}h — presumed CLAIMED by a live session")
    ap.add_argument("--since", default="2026-06-01", help="git log window (default 2026-06-01)")
    ap.add_argument("--selftest", action="store_true",
                    help="check newest_activity against both directions of the "
                         "landed test, plus the shape bug that shipped once")
    a = ap.parse_args()

    if a.selftest:
        return _selftest()

    root = pathlib.Path(subprocess.run(["git", "rev-parse", "--show-toplevel"],
                                       capture_output=True, text=True).stdout.strip())
    beans = load_beans(root)
    hits = done_commits(a.since)
    allc = any_commits(a.since)
    now = datetime.datetime.now(datetime.timezone.utc)

    if a.active:
        act = []
        for bid, b in beans.items():
            if b["status"] not in ("todo", "in-progress"):
                continue
            newest = max((c for c in allc.get(bid, [])), key=lambda c: c[1], default=None)
            if not newest:
                continue
            age_h = (now - datetime.datetime.fromisoformat(newest[1])).total_seconds() / 3600
            if age_h < _ACTIVE_HOURS:
                act.append((age_h, bid, b, newest))
        act.sort()
        inflight = [x for x in act if not _landed(x[3][0])]
        landed   = [x for x in act if _landed(x[3][0])]
        print(f"Open beans with a commit in the last {_ACTIVE_HOURS}h: {len(act)}")
        print(f"  IN FLIGHT (not on origin/main) — presume CLAIMED, do NOT take: {len(inflight)}")
        print(f"  LANDED (already on origin/main) — nobody holds it, so it is FREE "
              f"to take: {len(landed)}")
        print("  LANDED says NOTHING about whether the WORK is done — only that one "
              "commit\n  naming the bean has merged. Read the body. See _landed().\n")
        act = inflight + landed
        for age_h, bid, b, (sha, iso, subj) in act:
            state = "IN FLIGHT — do NOT take" if not _landed(sha) else "LANDED — free to take"
            print(f"  {bid}  ({b['priority']}, {b['status']}, last commit {age_h:.0f}h ago)  [{state}]")
            print(f"    bean : {b['title'][:100]}")
            print(f"    last : {sha[:11]} {subj[:100]}")
        print("\nThis signal asks WHEN and WHERE, never WHAT, so none of the four "
              "semantic\nfailure classes below apply to it. WHERE is load-bearing: age "
              "alone cannot\ntell a sibling HOLDING a bean from one who FINISHED it, and "
              "those want opposite\nactions. Measured 2026-09-04 — qou-9iwt was flagged "
              "CLAIMED on a commit already\nMERGED to main, suppressing the one bean whose "
              "work was demonstrably done.\nAGENTS.md permits overlapping only open-outcome "
              "research — never work that has\none right answer.")
        return 0

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
        act = newest_activity(allc.get(bid, []), now)
        if act:
            age_h, _sha, landed = act
            if age_h < _ACTIVE_HOURS and not landed:
                flag += (f"  [IN FLIGHT — commit {age_h:.0f}h ago, not on main; presume CLAIMED, "
                         f"do not take]")
        print(f"  {bid}  ({pri}, last updated {b['updated'][:10]}){flag}")
        print(f"    bean : {b['title'][:100]}")
        print(f"    later: {sha[:11]} {iso[:10]} {subj[:100]}")
    print("\nCANDIDATES, NOT VERDICTS. MEASURED PRECISION 2 IN 12 on the full "
          "high-priority list\n(all twelve bodies read): only qou-vtau and qou-w2vy "
          "were genuinely stale.\nThis is a 'worth OPENING' list, NOT a staleness "
          "list. Four structural causes,\nall unfixable by regex because they are "
          "semantic:")
    print("  1. partial completion  -- 'ITEM 4 CLOSED', 'item 3 fully closed; the "
          "remaining item is ...'")
    print("  2. the verb governs a DIFFERENT bean named in the same subject "
          "(flagged above with !!)")
    print("  3. the verb is QUOTED or NEGATED and the commit REOPENED the bean -- "
          "e.g. qou-hok7's\n     \"deuteron-wall 'resummation closed' is a "
          "wrong-transform artifact\"")
    print("  4. the bean is DELIBERATELY PARKED and says so -- e.g. qou-mln9's "
          "'Left todo\n     deliberately ... Closing is the author's call.'")
    print("\nOpen each one and read it. Do NOT bulk-close from this output.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
