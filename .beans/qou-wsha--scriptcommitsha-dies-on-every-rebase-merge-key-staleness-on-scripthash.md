---
# qou-wsha
title: 'Witness provenance: scriptCommitSha dies on every rebase-merge — key staleness detection on scriptHash instead'
status: todo
type: task
priority: low
created_at: 2026-08-10T03:45:00Z
updated_at: 2026-08-10T03:45:00Z
---

Small, verified, and cheap to act on. Found while landing PR #4883.

## The mechanism

A witness records two provenance fields for its producer:

| field | what it is | survives rebase-merge? |
|---|---|---|
| `scriptHash` | 12-char SHA-256 prefix of the **producer file content** | ✅ **yes** |
| `scriptCommitSha` | `git log -1 --format=%H -- <producer>` | ❌ **no** |

AGENTS.md §"Branch + PR workflow" rule 8 makes **rebase-merge the default**. A
rebase-merge replays the branch's commits onto `main` with **new SHAs**. So any
witness whose producer was committed on the branch records a commit that does
not exist in `main`'s history the moment it lands. The witness is stale on
arrival, through no fault of the producer.

**Measured on PR #4883 after merge** (producer 8 commits back, well inside the
fetched window, so this measurement is reliable):

    scriptHash      recorded=d8de0d12bda3  actual=d8de0d12bda3  -> OK
    scriptCommitSha recorded=fc88f01f01    actual=e1f63695cd    -> STALE

I refreshed the sha *once* mid-PR (after rebasing onto main) and it went stale
again at merge, because the merge itself is the rewrite. **There is no
branch-side fix.** Refreshing before merge cannot work.

## Why this is low priority, not a fire

`scriptHash` — the field that actually detects *producer drift*, i.e. the thing
staleness detection exists to catch — is **content-addressed and correct**. An
edited producer changes `scriptHash` whether or not anything was rebased. So
detection works; `scriptCommitSha` is the decorative half.

## What to do

1. **Anything keying staleness on `scriptCommitSha` should key on `scriptHash`.**
   Audit the consumers (`scripts/check-sidecars.sh` prints
   *"check scriptCommitSha/scriptHash drift"*, so at least its message implies
   both) and demote the commit-sha comparison to informational.
2. **Do not mass-refresh `scriptCommitSha` across the corpus.** It would be
   correct for exactly as long as it takes the next rebase-merge to land, and it
   would touch a very large number of files for no detection benefit.

## ⚠ Measurement trap — do not repeat mine

My first attempt to size this corpus-wide reported **0 in-sync / 1089 stale**,
which looks like a dramatic finding and **is not one**. This checkout is a
**shallow clone** (`git rev-list --count origin/main` = 79). For any file not
touched inside that window, `git log -1 -- <path>` returns the **graft boundary
commit** — here `5a4f6eb654`, which git reports as "46405 files changed" because
it is the truncation point, not a real commit that touched them.

So the corpus-wide number is **unmeasurable from a shallow clone** and I withdrew
it. Only files whose producer commit is inside the fetched window (like #4883's)
give a trustworthy answer. If someone wants the real corpus figure, do it on a
full clone, or `git fetch --unshallow` first, and sanity-check by confirming the
reported "actual" SHAs are not all identical.

## Links

* `qou-w3eg` / PR #4883 — where this surfaced
* `scripts/check-sidecars.sh` — the P30 / drift consumer
* `computations/substrate/witness_base.py` — `WitnessBuilder.stamp_staleness_metadata`, which writes both fields
