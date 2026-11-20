---
# qou-zqno
title: 'RT-1 (Audit Sweep): Blind `Lean -> English -> Lean` Statement Round-Trip & Paper Statement Equivalence Across Provable Claims'
status: in-progress
type: task
priority: critical
created_at: 2026-11-19T16:50:59Z
updated_at: 2026-11-20T08:05:00Z
parent: qou-ncxf
---

Independent 3-agent blind pipeline (`rt1-lean-to-english` -> `rt1-english-to-lean` -> `rt1-adjudicator`) verifying whether stripped Lean declarations survive `Lean -> English -> Lean` round-trip without vacuity, ring weakening, or finite-case collapse, and match `.md` statements.

## 2026-11-20 takeover (W11, session_01VQDpPdnjTBLBcPi6D5gj61 dispatch; branch claude/roundtrip-blind-audit-2026-11-20)
Stalled-claim takeover: last touch 2026-11-19T17:42Z (>3 h); no backing branch or PR found (searched open PRs and branch names for round/blind/rt-/ncxf). The tool named in the epic body, `folio/pipeline/roundtrip-blind-packets.ts`, does NOT exist on main 917b69399. W11 replaces it with `scripts/roundtrip-blind-sample.py` (deterministic sha256(label) sample, comment-stripped blind packets) and runs a first sampled pass; results go in docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.
