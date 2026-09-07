---
# qou-6pd1
title: 'MERGE QUEUE: the four idle PRs measured CLEAN vs main (#6948 #6826 #6821 #6817) — prepare-merge-auto, rebase-merge, verify replay'
status: todo
type: task
created_at: 2026-09-07T18:16:29Z
updated_at: 2026-09-07T18:16:29Z
parent: qou-6g7j
---

Owner authorisation 2026-09-07: 'merge the clean PRs'. Measured CLEAN with git merge-tree against origin/main at session start: #6948 (qou-h2q6 conflict markers), #6826 (Phi_k not a trace retraction), #6821 (def:atomic-braid three strand counts), #6817 (Schur-Weyl surjection N=2 + 63 unlabelled sidecars). Pipeline per .claude/skills/local/prepare-merge-auto.md; sequential (a parallel rebase onto main races); verify each with scripts/verify-merge-replay.py; never delete branches. #7093 is deliberately NOT in this queue — bean qou-0ie7 is extending its branch; it merges after that agent finishes, as one PR.
