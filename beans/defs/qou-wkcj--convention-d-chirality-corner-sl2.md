---
# qou-wkcj
title: 'Convention-D chirality remark + corner sl2 persistence (n>=4): exclusive at n=4 only, weighted [3]_q:1'
status: in-progress
type: task
priority: normal
tags:
    - quark-state
    - chirality
    - weak
parent: qou-qs0e
blocking:
    - qou-hlx7
created_at: 2026-11-15T10:30:00Z
updated_at: 2026-11-15T10:30:00Z
---

Owner decisions relayed 2026-11-15 by coordinator session_01M5GA1LmsEf8tSMxFjMkmnn after #7855 merged:
(b) add one remark recording convention D's one-sidedness (observation; weak-chirality identification
stays scope (a)); (a) pursue the corner sl2 in H4 and beyond, headline that the n=4 exclusive
one-sidedness does not persist at n=5, and state what survives (weighted / limit version).

Session: https://claude.ai/code/session_01Qmmkt6RTXyN5gg3AQBGRy7
Branch: claude/conventionD-chirality-corner-sl2-2026-11-15

Result: exclusive one-sidedness is an n=4 accident. What survives at every n is a WEIGHTED bias
tau(P+) : tau(P-) = [3]_q : 1 (Lean ConventionDLineWeights.lean, n-independent, from tau(1)=1 and
tau(sigma)=z_D alone). The sl2-carrying parts of the two corners tend to the same ratio
(probe corner_sl2_weighted_persistence_probe.py, n=16: 3.0459 vs [3]_q0 = 3.0437). The bias is
bar-invariant in size and equals 3 at q = 1, so it belongs to convention D, not to |q|>1.
Remark rem:convention-d-chirality-side added in mass-theory (interprets
prop:markov-trace-frobenius-selection).
