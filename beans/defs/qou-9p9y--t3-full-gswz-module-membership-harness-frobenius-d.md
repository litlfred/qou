---
# qou-9p9y
title: 'T3: full GSWZ module-membership harness (Frobenius + dilog + eps_m); candidate data format'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T18:29:31Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cv7z
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-01 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Round 84 Progress (`litlfred/qou#8309`)
- **Lean 4.24.0 Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/GSWZModuleHarnessAndKerovMomentStructuresBrick.lean` (`0` `sorry`, `0` `axiom`, `0` warnings; `0` CRITICAL, `0` major, `0` advisory across all 7 static audits).
- **80-dps Probe & Witness**: `computations/probes/gswz_module_harness_and_kerov_moment_structures_brick_probe.py` & `computations/probes/gswz-module-harness-and-kerov-moment-structures-brick.witness.json` (`scriptCommitSha = 843d4ad40be5ebf362ac9c1f33db1be9d81b604b`, HEAD `701af74a55bd4d1ae870ab66bcadecbda5438362`, `allPassed = true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8309, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-01: "chore(beans): qou-9p9y touch — dilog layer complete, eps_m remains"). The work may be partly or fully done. Read the bean before you close it.
