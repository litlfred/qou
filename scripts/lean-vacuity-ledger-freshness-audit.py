#!/usr/bin/env python3
"""Check a ledger invariant the re-verify tool cannot: a verdict must not
predate the revision it cites.

WHY THIS EXISTS
---------------
`docs/audits/lean-vacuity-review-ledger.json` records, per candidate, an agent
`verdict` and the `file_sha` of the `.lean` at review time (a 12-char SHA-256
prefix of the WHOLE FILE).  `scripts/lean-vacuity-ledger-reverify.py` re-checks
a verdict by asking whether the DECLARATION text still matches what it was at
that `file_sha`.

That assumes `file_sha` names the revision the verdict was made against.  When
it does not, the re-verify compares post-fix text against post-fix text, reports
IDENTICAL, and RESTORES a verdict written against the pre-fix file.

Worked case (2026-09-14, `qou-9yt9`):

    TannakaKreinReconstruction
      reviewed_at            2026-09-07T09:55:00Z
      file_sha f5b88ba3250d -> 21bac468c6, authored 2026-09-07T19:23:34Z

The verdict is 9.5 h OLDER than the revision it cites, and its evidence names
`monoidal_equiv` -- a field commit 21bac468c6 had replaced with real data
(`equiv : C === RepCat`).  The re-verify reported IDENTICAL and restored it.

THE INVARIANT
-------------
    reviewed_at  >=  authored-time of the earliest revision whose content
                     hashes to file_sha

AUTHOR date, not committer date: AGENTS.md rule 8 rebase-merges every branch,
which rewrites committer dates and would manufacture false positives.  Measured
both ways when this was written -- the counts were identical, so rebase-merge
does not explain the violations.

This script MEASURES.  It does not edit the ledger and does not fix the
re-verify tool; whether that tool should enforce the invariant is an owner call.
"""
import collections, datetime, hashlib, json, pathlib, subprocess, sys

LEDGER = pathlib.Path("docs/audits/lean-vacuity-review-ledger.json")


def revisions(path: str):
    """(sha, author-date) for each revision of `path`, oldest first."""
    out = subprocess.run(["git", "log", "--format=%H %aI", "--", path],
                         capture_output=True, text=True).stdout
    rows = [l.split(" ", 1) for l in out.splitlines() if l.strip()]
    return list(reversed(rows))


def content_hashes(path: str):
    """file_sha -> author-date of the EARLIEST revision with that content.

    Earliest, not newest: a file whose content returns to an earlier state
    would otherwise be dated by the later occurrence.
    """
    seen = {}
    for sha, when in revisions(path):
        blob = subprocess.run(["git", "show", f"{sha}:{path}"],
                              capture_output=True).stdout
        seen.setdefault(hashlib.sha256(blob).hexdigest()[:12], (sha, when))
    return seen


def utc(stamp: str):
    dt = datetime.datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    if dt.tzinfo is None:                      # date-only / naive: assume UTC
        dt = dt.replace(tzinfo=datetime.timezone.utc)
    return dt.astimezone(datetime.timezone.utc)


def main() -> int:
    entries = json.loads(LEDGER.read_text())["entries"]

    by_file = collections.defaultdict(list)
    for key, entry in entries.items():
        by_file[key.split("::")[0]].append((key, entry))

    fresh, stale, unmatched, undated = 0, [], [], 0
    for path, rows in sorted(by_file.items()):
        hashes = content_hashes(path)
        for key, entry in rows:
            reviewed, file_sha = entry.get("reviewed_at"), entry.get("file_sha")
            if not reviewed:
                undated += 1
                continue
            hit = hashes.get(file_sha)
            if hit is None:
                unmatched.append(key)
                continue
            sha, when = hit
            try:
                r = utc(reviewed)
            except ValueError:
                unmatched.append(key)
                continue
            c = utc(when)
            if r < c:
                stale.append((key, reviewed, sha, when,
                              round((c - r).total_seconds() / 3600, 1)))
            else:
                fresh += 1

    print(f"entries                                   : {len(entries)}")
    print(f"  invariant holds                         : {fresh}")
    print(f"  STALE (verdict predates the sha it cites): {len(stale)}")
    print(f"  file_sha matches no revision of the file : {len(unmatched)}")
    print(f"  no reviewed_at (freshness uncheckable)   : {undated}")

    if stale:
        print("\nby verdict:",
              dict(collections.Counter(entries[k]["verdict"] for k, *_ in stale)))
        print("\nworst 15 by lead time (verdict written N hours BEFORE the sha):")
        for key, reviewed, sha, when, hours in sorted(stale, key=lambda r: -r[4])[:15]:
            path, decl, _ = key.split("::")
            print(f"  {hours:8.1f}h  {decl:40.40s} {pathlib.Path(path).name}")

    if "--strict" in sys.argv and stale:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
