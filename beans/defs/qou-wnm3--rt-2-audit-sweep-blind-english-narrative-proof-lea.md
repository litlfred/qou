---
# qou-wnm3
title: 'RT-2 (Audit Sweep): Blind `English Narrative Proof -> Lean Stmt/Skeleton` & `Lean Proof -> English Narrative` Semantic Equivalence'
status: in-progress
type: task
priority: critical
created_at: 2026-11-19T16:50:59Z
updated_at: 2026-11-20T08:05:00Z
parent: qou-ncxf
---

Independent 3-agent blind pipeline (`rt2-narrative-to-lean`, `rt2-lean-to-narrative`, `rt2-adjudicator`) catching bait-and-switch Lean proofs, missing cases, and mechanistic divergence between `.md` narrative proofs and `.lean` formal proofs.

## 2026-11-20 takeover (W11, session_01VQDpPdnjTBLBcPi6D5gj61 dispatch; branch claude/roundtrip-blind-audit-2026-11-20)
Stalled-claim takeover: last touch 2026-11-19T17:42Z (>3 h); no backing branch or PR found (searched open PRs and branch names for round/blind/rt-/ncxf). The tool named in the epic body, `folio/pipeline/roundtrip-blind-packets.ts`, does NOT exist on main 917b69399. W11 replaces it with `scripts/roundtrip-blind-sample.py` (deterministic sha256(label) sample, comment-stripped blind packets) and runs a first sampled pass; results go in docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.
