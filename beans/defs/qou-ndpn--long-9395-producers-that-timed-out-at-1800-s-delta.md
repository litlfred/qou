---
# qou-ndpn
title: 'Long #9395 producers that timed out at 1800 s: delta_lambda_fr_identity_phase5c, lr_fusion_self_conj_test'
status: in-progress
type: task
priority: normal
created_at: 2026-11-24T21:01:22Z
updated_at: 2026-11-25T01:49:48Z
parent: qou-s028
---

## 2026-11-24
delta_lambda_fr_identity_phase5c: in the refresh, 4He FULL alone took 1163 s, and it then timed out in 4He CONSTIT at 1800 s. Re-launched with a 7000 s budget and a timestamped log. lr_fusion_self_conj_test: n=20 LR decomposition took 60.7 s, and it timed out in n=28. LR coefficient growth makes n=28 likely hours; not re-run (disk ~2-4 GB, shared).

## 2026-11-25 measured (agent, session 01Eucf)
delta_lambda_fr_identity_phase5c ran to completion: 1639 s wall (4He FULL 1044 s, 4He CONSTIT 594 s, everything else under 2 s), exit 0, 2/2 assertions pass. Log: /tmp/claude-0/-home-user/ab2f8fab-d324-5bfe-8e05-335069a715bd/scratchpad/a7-dlfr.log (scratchpad, may not survive). The payload is byte-identical to main; the ONLY diffs are scriptHash d943d514543d -> 2549f6b0416a and framework_doc content/ -> folio/ (the tree rename). NOT committed: that run used system mpmath 1.3.0 without clarabel, so the environment record would degrade (the witness guard warns). A refresh needs only a re-run under mpmath 1.4.1 + clarabel 0.11.1 (~28 min). The 1800 s timeout in #9395 was a margin problem (1639 s here vs >1800 s under load there), not a hang.
lr_fusion_self_conj_test: NOT re-run. n=20 LR self-fusion took 60.7 s, and n=28 (lambda=[6,6,5,5,4,2]) is far larger; expected hours. Not attempted with 1.6 GB of disk free in a shared container. Needs a dedicated session with a 2-4 h budget, or a cap at n<=20.

## 2026-11-25
delta_lambda_fr_identity_phase5c refreshed under mpmath 1.4.1 + clarabel (1233 s, 2/2 pass), committed in #9404 (bef562673db). lr_fusion_self_conj_test is still not run (expected hours at n=28).
