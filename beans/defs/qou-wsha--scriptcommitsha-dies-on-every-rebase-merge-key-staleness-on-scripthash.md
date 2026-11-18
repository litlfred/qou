---
# qou-wsha
title: 'Witness provenance: scriptCommitSha dies on every rebase-merge — key staleness detection on scriptHash instead'
status: in-progress
type: task
priority: low
tags:
    - reorg-2026-10-04
created_at: 2026-08-10T03:45:00Z
updated_at: 2026-10-04T15:26:04Z
parent: qou-5vkl
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

## Consumer audit — the code is already right; the DOCS are the defect

Ran item 1 above (agent pickup, 2026-08-10). The result narrows this bean
considerably: **every enforcement path already keys on `scriptHash` alone.**

| consumer | keys staleness on | verdict |
|---|---|---|
| [`computations/witness_dependency_drift.py`](../computations/witness_dependency_drift.py) `check_self_staleness` — the validator CI actually runs | `scriptHash` only | ✅ already correct |
| [`tools/qou-substrate/python/qou_substrate/witness.py`](../tools/qou-substrate/python/qou_substrate/witness.py) `_EPHEMERAL_META_FIELDS` | `scriptCommitSha` **masked** as ephemeral, with the rationale *"change on every commit; would trigger CI drift loops if comparison were exact"* | ✅ already correct |
| `scripts/check-sidecars.sh:136` | advisory hint text naming both | cosmetic |
| **`AGENTS.md` §idle-backlog item 4** | *"stale when `scriptCommitSha` … **or** `scriptHash` … drift"* | ❌ **the defect** |
| **`.claude/skills/local/integration-watcher.md` §0b** | same `(a)` **OR** `(b)` wording | ❌ **the defect** |

So `witness.py` had already diagnosed this mechanism — it just never propagated
to the agent-facing rule.

**Why the doc half matters more than it looks.** The two doc sites are the
*idle-time backlog policy*: they tell an agent that a `scriptCommitSha`
mismatch means the witness is stale and to **refresh by re-running the
producer**. Under rebase-merge that trigger is permanently true, so the policy
routes idle agents into long-compute producer re-runs that fix nothing and go
stale again at the next merge — while consuming the ≤ 3-witness-per-idle-pass
budget that real `scriptHash` staleness needs. The cost is not a wrong number
in a report; it is misdirected compute, forever.

## Corpus measurement — graft-aware, and the direction survives

The withdrawn 0/1089 (below) was right to withdraw, but the *direction* holds
under a measurement that filters the graft boundaries explicitly. This clone
has **five** graft boundaries, not one. Classifying every `*.witness.json` and
scoring only those whose `git log -1` result is **not** a graft commit:

    UNMEASURABLE (graft)   1718     <- what the withdrawn number silently scored
    no provenance fields    709
    scriptCommitSha unknown 606
    producer unresolved     118
    RELIABLE, stale           3
    RELIABLE, in sync         0

Three distinct `actual` SHAs among the three — so the "every actual identical"
tell that exposed the false alarm is **absent** here. Same three witnesses,
both fields:

| witness | `scriptHash` | `scriptCommitSha` |
|---|---|---|
| `markov-trace-recursive` | ✅ OK | ❌ stale |
| `canonical-ordering-dof` | ❌ stale | ❌ stale |
| `qbeta-decay-sdp-extended-ck` | ✅ OK | ❌ stale |

On this sample the commit-sha criterion contributes **two false positives and
zero true positives** beyond `scriptHash`. The one genuine staleness
(`canonical-ordering-dof`, a real producer edit) is caught by `scriptHash`
alone — filed separately as `qou-zv2l`.

Sample is small (n=3) and that is a hard ceiling of the shallow clone, not a
choice; it is reported as n=3 rather than inflated. The mechanism argument does
not rest on it.

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

**Amendment (pickup agent):** read `.git/shallow` rather than assuming a single
truncation point — a fresh clone of this repo carries **five** graft boundaries,
so a filter written against one boundary sha still lets the artifact through.
The graft-aware measurement above does this and is the reusable form.

## Links

* `qou-w3eg` / PR #4883 — where this surfaced
* `qou-zv2l` — the one genuine self-staleness the audit turned up
* `scripts/check-sidecars.sh` — the P30 / drift consumer (hint text only)
* `computations/witness_dependency_drift.py` — the validator CI runs; already `scriptHash`-only
* `computations/substrate/witness_base.py` — `WitnessBuilder.stamp_staleness_metadata`, which writes both fields
* `tools/qou-substrate/python/qou_substrate/witness.py` — `_EPHEMERAL_META_FIELDS`, which already masks `scriptCommitSha`
