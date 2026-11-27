---
# qou-cfwx
title: Add the harness merge guard to qou (PR checks + merge-guard callers)
status: todo
type: feature
priority: normal
created_at: 2026-11-27T14:19:06Z
updated_at: 2026-11-27T14:19:06Z
---

Owner card 2026-11-27 ~14:17Z: "Yes, and plan full merge guard" (thread 'Get QOU site running on harness', PR #9440, ruling row in docs/coordination/owner-rulings.md). SCOPE ONLY until the owner picks a tier.

What fhir-harness has, and qou lacks:
1. .github/workflows/harness-pr-checks.yml -> cat-harness-tools layer-pr-checks.yml (typecheck, tests no-new-failures, gates no-new-failures, index gates), on pull_request + push main; draft-fast-tier.
2. .github/workflows/merge-guard-trigger.yml (pull_request signal, no token) and merge-guard.yml (workflow_run from main -> layer-merge-guard.yml, posts the merge-guard status). Both written by bun run cat workflow-pins --write.
3. merge-guard required status on main (branch protection; merge manager sets it).

Cost measured 2026-11-27: 679 qou PRs opened 2026-11-20..27 (~97/day), 100+ open. layer-pr-checks runs gates on main AND the PR per run, so a full tier per push is the expensive part.

Options to put to the owner: (a) guard + fast tier only (typecheck/prepare) on every PR, full tier only on label release/ready-to-merge; (b) full tier on ready_for_review; (c) guard only, judging local-verification evidence, no PR CI. Recommendation: (a).

## 2026-11-27 14:18Z — owner picked C, re-scoped
Verbatim: "but C -- i dont want to have slow merge times, no red gates (excpet json(ld) KG publication). all QA runs after. can be agent, does not need to be github action w/ runner queue issues." So NO PR-check workflow and NO Actions merge-guard callers. The guard is agent-run: bun run cat merge:guard <pr> (no --full-tier) + gen-block-jsonld --check; QA post-merge. Recorded: owner-rulings.md + AGENTS.md section "FAST MERGES" on PR #9440. Remaining: update prepare-merge-auto skill text to match; merge manager adopts it.
