---
# qou-kvgn
title: 'Merge sweep 2026-09-07: rebase-merge every non-draft open PR whose mergeable_state is clean, verify replay per PR, report the table'
status: scrapped
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T18:25:28Z
updated_at: 2026-11-15T13:31:00Z
parent: qou-5vkl
---

Owner: 'merge the clean PRs' (2026-09-07). Rule: non-draft AND mergeable_state==clean at the moment of merge, rebase-merge, never delete branches, run scripts/verify-merge-replay.py after each. Drafts skipped. Delegated to a merge-coordinator agent; result table goes here.

## Sweep executed by the parent session 2026-09-07 ~18:50Z (the merge-coordinator subagent is API-gated: mcp__github__* is not exposed to subagents and REST /repos/* returns 403 'GitHub access is not enabled for this session'; recorded as a TRAP for later sessions).

Rule applied: non-draft, GitHub mergeable at merge time (405 'has merge conflicts' = not clean), rebase-merge, expectedHeadSha pinned, branches kept. Live sibling PRs (head updated within ~60 min: #7005 #7061 #7088 #7097 #7099 #7104 #7114 #7115 #7119 #7120 #7121 #7122 #7123 #7126 #7130 #7131) were NOT touched — their sessions own them.

MERGED (10), replay verified by patch-id (every commit replayed): #7118 2868d21288 · #7083 052ca0dc18 · #6853 bcc1ea1abe · #6818 8c646ed4c3 · #6816 23915bbd87 · #6804 ecd1ababaf · #6758 b9ac9c35ff · #6744 0c957c179b · #6355 709bfa9cf5 · #6353 4ff8a4b5eb.
CONFLICTS (8, not merged): #7093 #6807 #6361 #6359 #6358 #6357 #6350 #6342.
HELD — body says do-not-merge: #6307 (posted for review only), #5402 (audit branch), #5352 (survey; carries a sibling's only copy of 431def4877), #5861 (§6 escalation on pivotalOfBraided).
HELD — judgement, owner call: #6178 (404 files, 76 producers re-routed from an 8-day-stale tree, merge commits at tip) and #6025 (+419k-line witness, edits raw-float64-baseline.json — baselines drain, never grow).
Drafts skipped: #7124 #7101 #6878 #6681 #6233 #5338 #5330 #4845.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-07 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Closed 2026-11-15 (owner tap, ops bean triage)

Status set to `scrapped`: a one-off merge sweep from 2026-09-07; superseded by the 2026-11-15 idle-PR triage (project file qou-handover/idle-pr-triage.md), which dispositioned the open PRs again.
