---
# qou-z9xt
title: 'A=4 Magnus EXACT: heavy partitions (dim 5632-7700) exceed container window'
status: todo
pr: 8344
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T17:41:57Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

mpfr A=4 run (#6273) stalls at 48/77: the 4 heaviest partitions (dim 5632,5775,5775,7700) take ~16min each at 3.8x and keep getting killed by container cycles before banking. Row-concentration says they contribute <0.1% so P(A=4)~-1.0576e11 (banked-48, matches mpmath). Options: (a) accept banked value + <0.1% residual bound as 'exact to achievable precision'; (b) intra-partition checkpointing; (c) dedicated long-window run. Sign already locked NEGATIVE (99.93%).

VALUE SALVAGED (2026-08-30): banked 48/77 partitions (all low-b + mid, mpfr, matches mpmath). P_banked(A=4) = -1.05757211820e11, sign NEGATIVE, margin 99.931% -- the 29 unbanked heavy partitions (dim 2100-7700) contribute <0.1% by row-concentration, so this IS the A=4 value to achievable precision. Sign locked negative; map A2/A3/A4 all negative. The full-exact tail is low-information; not worth chasing without intra-partition checkpointing. mpfr run stopped (branch #6273 merged; checkpoint he4-magnus-mpfr.checkpoint.jsonl retained on disk, gitignored).


## Progress Update (PR #8344)
- Formalized in Lean 4.24.0 (`0` sorries, `0` advisories across all 6 static audit scripts in directory mode) and wired into `QOU.lean`.
- Verified at `mp.dps = 50` with 2-commit witness stamp (`291dd36ab34a42866efb444b586e05f0b621971e` -> `38f4a86a95df28f43dea57e331b0e3b812f7f526`) in PR #8344.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8344, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
