---
# qou-6pd1
title: 'MERGE QUEUE: the four idle PRs measured CLEAN vs main (#6948 #6826 #6821 #6817) — prepare-merge-auto, rebase-merge, verify replay'
status: in-progress
type: task
created_at: 2026-09-07T18:16:29Z
updated_at: 2026-09-07T18:30:00Z
parent: qou-6g7j
---

Owner authorisation 2026-09-07: 'merge the clean PRs'. Measured CLEAN with git merge-tree against origin/main at session start: #6948 (qou-h2q6 conflict markers), #6826 (Phi_k not a trace retraction), #6821 (def:atomic-braid three strand counts), #6817 (Schur-Weyl surjection N=2 + 63 unlabelled sidecars). Pipeline per .claude/skills/local/prepare-merge-auto.md; sequential (a parallel rebase onto main races); verify each with scripts/verify-merge-replay.py; never delete branches. #7093 is deliberately NOT in this queue — bean qou-0ie7 is extending its branch; it merges after that agent finishes, as one PR.


2026-09-07 claimed by merge-coordinator sub-agent (worktree agent-a9a5286a51d4ee916). Order #6948 -> #6826 -> #6821 -> #6817, sequential; per-PR ledger appended below after each merge.

- #6948 (claude/stale-conflict-marker-bean-2026-09-06): its single commit 82813a9dc was ALREADY on main as 84b0cb1397 (git cherry: same patch-id; verify-merge-replay 1/1 replayed, 0 missing). Rebase onto origin/main 811839a3b skipped it as an applied cherry-pick; branch force-with-lease-pushed to 811839a3b (= main tip) so GitHub marks the PR merged. Checks: none applicable beyond merge-tree clean + replay (bean-only change). API 403 (session gate) -> no Copilot request, no PR-body edit; parent to confirm PR state.
