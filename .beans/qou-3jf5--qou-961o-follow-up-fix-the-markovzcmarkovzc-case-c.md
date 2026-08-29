---
# qou-3jf5
title: 'qou-961o follow-up: fix the markovZC/markovZc case-collision the rename introduced'
status: todo
type: task
priority: normal
created_at: 2026-08-29T11:48:06Z
updated_at: 2026-08-29T11:48:06Z
---

qou-961o renamed 3 convention-C markovZ -> markovZC, which case-collided with the pre-existing lowercase markovZc (convention D, categorical-chain-convergence-mechanisms.lean:83). One letter's case, opposite conventions (0.4993 C vs 0.6127 D at proton q0). Convention-auditor caught it (5ed07e46), corrected my AGENTS.md 'no collision' claim, logged a TRAP. FIX: renamed the lowercase markovZc -> markovZD (body q³/(q²+1) is byte-identical to QOU.BraidKnot.markovZD). markovZc is local-only (no cross-file consumers). AGENTS.md + convention-auditor MEMORY.md TRAP both marked RESOLVED. Verification: lean-verifier agent running (lean-direct segfaulted on cache load in main session — env trap, not the source). Owner-authorized (option 1).
