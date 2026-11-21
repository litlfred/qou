---
# qou-ncxf
title: 'EPIC: Three-Way Blind Multi-Agent Semantic Round-Trip Audits (RT-1 Lean<->English Stmt, RT-2 Narrative Proof<->Lean, RT-3 Thm Stmt<->Narrative Proof)'
status: in-progress
type: epic
priority: critical
created_at: 2026-11-19T16:50:58Z
updated_at: 2026-11-21T16:00:00Z
---

End-to-end blind multi-agent round-trip audit architecture across all 741 provable claims (and definitions/conjectures) in QOU, using strictly isolated, tool-free blind agents at every leg plus deterministic comment/spoiler scrubbing (`folio/pipeline/roundtrip-blind-packets.ts`).

## 2026-11-20 takeover (W11, session_01VQDpPdnjTBLBcPi6D5gj61 dispatch; branch claude/roundtrip-blind-audit-2026-11-20)
Stalled-claim takeover: last touch 2026-11-19T17:42Z (>3 h); no backing branch or PR found (searched open PRs and branch names for round/blind/rt-/ncxf). The tool named in the epic body, `folio/pipeline/roundtrip-blind-packets.ts`, does NOT exist on main 917b69399. W11 replaces it with `scripts/roundtrip-blind-sample.py` (deterministic sha256(label) sample, comment-stripped blind packets) and runs a first sampled pass; results go in docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.

## 2026-11-20 pass 1 result (W11, PR #8528)
- Sample: 10 of 435 eligible blocks, first by sha256(label). Audit: docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.
- 8 of 10 carry a statement / narrative / Lean mismatch. Classes: A, Lean conclusion supplied by an assumption (4). B, Lean weaker than the .md claim (6). C, narrative does not prove its statement (6+).
- Calibration: the blind legs independently reproduced qou-vkm6 (B07).
- New beans: qou-27ys, qou-ni0g, qou-1iit, qou-n3xv, qou-tdhw, qou-zxuy, qou-xxa9, qou-5d0x, qou-k9tf, qou-pwo1.
- Remaining: 425 blocks. The adjudicator is not yet a separate agent. The sampler misses dotted decl names. Stays in-progress.

## 2026-11-21 (honesty-audits sibling)

Pass 2 done (20 blocks, offset 15; PR #8888, docs/audits/2026-11-21-roundtrip-blind-audit-pass2.md). Class A in 9/20, tautology 2, genuine 9. New: C12 `wigner_coefficient_axiom` is an axiom carrying an empirical 3 % bound at the retired CODATA-2018 muon pin (see also qou-wg3c); C09 and C13 narrative proofs verified wrong; C19/C20 agent findings checked and rejected. Five decl-not-found refs in the window. Pass-1 restatements and the confinement sorry also landed in #8888. Next cursor: offset 40.
