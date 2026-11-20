---
# qou-da6d
title: 'RT-3 (Audit Sweep): Blind `Theorem Statement <-> English Narrative Proof` Bidirectional Mathematical Self-Consistency'
status: in-progress
type: task
priority: critical
created_at: 2026-11-19T16:50:59Z
updated_at: 2026-11-20T08:05:00Z
parent: qou-ncxf
---

Independent 3-agent blind pipeline (`rt3-proof-to-stmt`, `rt3-stmt-to-proof`, `rt3-adjudicator`) verifying pure mathematical equivalence between theorem statements (`741` provable blocks) and their narrative proofs (`437` explicit `prf:*` blocks + inline proofs): catching unproved directions/uniqueness, hidden hypotheses, dead hypotheses, and hand-waved steps.

## 2026-11-20 takeover (W11, session_01VQDpPdnjTBLBcPi6D5gj61 dispatch; branch claude/roundtrip-blind-audit-2026-11-20)
Stalled-claim takeover: last touch 2026-11-19T17:42Z (>3 h); no backing branch or PR found (searched open PRs and branch names for round/blind/rt-/ncxf). The tool named in the epic body, `folio/pipeline/roundtrip-blind-packets.ts`, does NOT exist on main 917b69399. W11 replaces it with `scripts/roundtrip-blind-sample.py` (deterministic sha256(label) sample, comment-stripped blind packets) and runs a first sampled pass; results go in docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.
