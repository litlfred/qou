---
# qou-58zq
title: main is red on 11 precision ratchets under the FULL precision-gates family (measured 2026-09-16 at 67f52ddf58); --changed on a branch cannot see it
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-16T02:43:56Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

Measured by the merge-coordinator agent during the 2026-09-16 pass (its report, verified against the gate names in AGENTS.md): the FULL scripts/precision-gates.sh family run in a fresh worktree at origin/main 67f52ddf58 exits 1 in 324 s with 11 red ratchets — Q0_FLIP 1; q0-anchor refill NEW 188; float64-padding NEW 63; module-const LOSSY 1; raw-float64 976 witnesses; q0-drift NEW 5; mixed-arith over-baseline 4; plus import-time-dps, never-raises-dps, reference-literal, witness-value-copy. The PR heads of #7430/#7429/#7432 gave the identical line and counts with no PR file named, so the three merges did not move it. Contrast: every 'precision-gates.sh --changed' run in this session on a branch exited 0 — the --changed scope covers only the branch's touched files and cannot see main's own state, so 'gates exit 0' on a branch is not evidence that main is green. The discriminator is the full family in a worktree at origin/main. Related: qou-v0t8 (the regenerated-audit-witness trap, completed), qou-mnrd / qou-82ur (dirty witnesses reaching main). Nothing changed here (ask-first: fix at the producers, never widen a baseline).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8280, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
