---
# qou-da6d
title: 'RT-3 (Audit Sweep): Blind `Theorem Statement <-> English Narrative Proof` Bidirectional Mathematical Self-Consistency'
status: in-progress
type: task
priority: critical
created_at: 2026-11-19T16:50:59Z
updated_at: 2026-11-21T13:00:00Z
parent: qou-ncxf
---

Independent 3-agent blind pipeline (`rt3-proof-to-stmt`, `rt3-stmt-to-proof`, `rt3-adjudicator`) verifying pure mathematical equivalence between theorem statements (`741` provable blocks) and their narrative proofs (`437` explicit `prf:*` blocks + inline proofs): catching unproved directions/uniqueness, hidden hypotheses, dead hypotheses, and hand-waved steps.

## 2026-11-20 takeover (W11, session_01VQDpPdnjTBLBcPi6D5gj61 dispatch; branch claude/roundtrip-blind-audit-2026-11-20)
Stalled-claim takeover: last touch 2026-11-19T17:42Z (>3 h); no backing branch or PR found (searched open PRs and branch names for round/blind/rt-/ncxf). The tool named in the epic body, `folio/pipeline/roundtrip-blind-packets.ts`, does NOT exist on main 917b69399. W11 replaces it with `scripts/roundtrip-blind-sample.py` (deterministic sha256(label) sample, comment-stripped blind packets) and runs a first sampled pass; results go in docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.

## 2026-11-20 pass 1 result (W11, PR #8528)
- Sample: 10 of 435 eligible blocks, first by sha256(label). Audit: docs/audits/2026-11-20-roundtrip-blind-audit-pass1.md.
- 8 of 10 carry a statement / narrative / Lean mismatch. Classes: A, Lean conclusion supplied by an assumption (4). B, Lean weaker than the .md claim (6). C, narrative does not prove its statement (6+).
- Calibration: the blind legs independently reproduced qou-vkm6 (B07).
- New beans: qou-27ys, qou-ni0g, qou-1iit, qou-n3xv, qou-tdhw, qou-zxuy, qou-xxa9, qou-5d0x, qou-k9tf, qou-pwo1.
- Remaining: 425 blocks. The adjudicator is not yet a separate agent. The sampler misses dotted decl names. Stays in-progress.

## 2026-11-21 honesty-audits (bean-drain wave 1, session_01Qmmkt97DGEiUfDvuBj8sVr; issue #8813, branch claude/honesty-audits-2026-11-21)
- Sampler improvements (commit 24c44167e): dotted written decl names now resolve (pass 1's parser miss on `QuantumObservableUniverse.exists_instance`); `--offset K` so pass 2 continues after pass 1's 15 candidates; `--ref-audit` (see qou-5d0x: 148 of 717 refs name no theorem).
- The 8 pass-1 findings were re-checked on main 2ae54ab40 (all hold) and disclosed as caveat authorNotes.
- Pass 2 (next 20 by hash, `--offset 15`, blind legs + separate adjudicator) NOT run; offered to the owner on a card. 425 blocks remain. Stays in-progress.
