---
# qou-ncxf
title: 'EPIC: Three-Way Blind Multi-Agent Semantic Round-Trip Audits (RT-1 Lean<->English Stmt, RT-2 Narrative Proof<->Lean, RT-3 Thm Stmt<->Narrative Proof)'
status: in-progress
type: epic
priority: critical
created_at: 2026-11-19T16:50:58Z
updated_at: 2026-11-20T08:05:00Z
---

End-to-end blind multi-agent round-trip audit architecture across all 741 provable claims (and definitions/conjectures) in QOU, using strictly isolated, tool-free blind agents at every leg plus deterministic comment/spoiler scrubbing (`folio/pipeline/roundtrip-blind-packets.ts`).

## 2026-11-20 takeover (W11, session_01VQDpPdnjTBLBcPi6D5gj61 dispatch; branch claude/roundtrip-blind-audit-2026-11-20)
Stalled-claim takeover: last touch 2026-11-19T17:42Z (>3 h); no backing branch or PR found (searched open PRs and branch names for round/blind/rt-/ncxf). The tool named in the epic body, `folio/pipeline/roundtrip-blind-packets.ts`, does NOT exist on main 917b69399. W11 replaces it with `scripts/roundtrip-blind-sample.py` (deterministic sha256(label) sample, comment-stripped blind packets) and runs a first sampled pass; results go in docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.
