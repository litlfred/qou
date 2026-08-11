#!/usr/bin/env python3
"""Triage a convention-D regeneration journal into commit / revert sets.

The rule this enforces is the one the campaign kept relearning the hard way:

    Do NOT commit a witness whose producer exited non-zero, timed out, or
    whose own internal checks failed. Revert it.

A producer that writes its witness *and* exits non-zero is not a broken
script — it is a script reporting a real failure in the only channel it has.
`rho_k_h3a_refinement` returns 2 when its Schur-Weyl identity misses, and it
writes the witness anyway; its own header says the extraction below is
meaningless without that identity. So the exit code is the verdict on the
*numbers*, and a nonzero one disqualifies them from being committed even
though the file on disk parses cleanly and looks fresh.

Reverting is therefore the default for every non-`ok` status, and the
witness stays at its committed value until the underlying failure is fixed.

Usage:
    convention-d-sweep-triage.py <journal.jsonl> [--revert]

Without --revert it only reports. With --revert it runs `git checkout --`
on every witness in the revert set.
"""
from __future__ import annotations

import collections
import json
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent


def load(journal: pathlib.Path):
    return [json.loads(l) for l in journal.read_text().splitlines() if l.strip()]


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    do_revert = "--revert" in sys.argv
    if not args:
        print(__doc__)
        return 1
    recs = load(pathlib.Path(args[0]))

    keep, drop = [], []
    for r in recs:
        changed = [w["path"] for w in r["witnesses"] if w["changed"]]
        (keep if r["status"] == "ok" else drop).append((r, changed))

    by_status = collections.Counter(r["status"] for r in recs)
    kept_w = sorted({w for _, ws in keep for w in ws})
    drop_w = sorted({w for _, ws in drop for w in ws})
    # A witness touched by BOTH a clean and a failed producer is not safe:
    # the failed run may have written last.
    contested = sorted(set(kept_w) & set(drop_w))
    kept_w = [w for w in kept_w if w not in contested]

    print(f"journal      : {args[0]}")
    print(f"producers    : {len(recs)}  ({', '.join(f'{k}={v}' for k, v in sorted(by_status.items()))})")
    print(f"COMMIT       : {len(kept_w)} witnesses changed by a clean (exit 0) producer")
    print(f"REVERT       : {len(drop_w)} witnesses touched by a failed producer")
    if contested:
        print(f"CONTESTED    : {len(contested)} touched by both — reverted, cannot attribute")

    if drop:
        print("\nfailed producers, with the witnesses they touched:")
        for r, ws in drop:
            print(f"  {r['status']:>9}  {r['seconds']:7.1f}s  {r['producer']}")
            for line in r.get("tail", [])[-2:]:
                print(f"             | {line[:150]}")
            for w in ws:
                print(f"             -> touched {w}")

    revert = sorted(set(drop_w) | set(contested))
    if do_revert and revert:
        subprocess.run(["git", "checkout", "--", *revert], cwd=REPO, check=False)
        print(f"\nreverted {len(revert)} witness(es) to their committed values")
    elif revert:
        print(f"\n(dry run — pass --revert to restore {len(revert)} witness(es))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
