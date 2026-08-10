---
# qou-pm48
title: 'prepare-merge + merge PRs #4873 (uniform spread) and #4876 (Wedderburn algebra rung)'
status: completed
type: task
created_at: 2026-08-10T02:20:00Z
updated_at: 2026-08-10T02:20:00Z
---

Owner granted explicit merge permission ("merge 4873/4876 after prepare").

Scope: run the /prepare-merge pipeline on both PRs (verify each Lean diff
against current `origin/main`, request Copilot review, dispose of comments),
then rebase-merge each per AGENTS.md rule 8.

Both PRs are Lean-only, so the content/witness/precision steps of the
pipeline are no-ops; the gate is `lean`-direct exit 0 on each changed
file's real import cone plus `#print axioms` showing no `sorryAx`.

Follow-on (owner picked option 3): attack residual item 1 of #4876 — the
division-ring collapse `𝔇 i ≃ R` for `k[S_n]` in char 0.
