---
# qou-htsi
title: 'Convention C excision: sibling-found stale C sites and compute-closed gates to re-examine (owner 2026-09-06)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T09:38:55Z
updated_at: 2026-09-06T13:54:37Z
parent: qou-2akx
---

Owner, 2026-09-06 (verbatim): 'Be suspicious of closed gates based on compute. Lots of stale and sibling found convention C still around. Need to excise that.' Queued (not pivoted) behind the NZ derivation (qou-n2cl). Scope: (1) re-run scripts/convention-c-value-audit.py and scripts/convention-c-producer-audit.py on main; (2) list every 'closed' / 'refuted' / 'gate' verdict in docs/audits and .beans whose evidence is a computation run under convention C (z = sqrt(q)/(q+1)) and mark it C-conditional; (3) drain what qou-t9r1 / qou-pmkh have not. Value audit last measured 85 C bindings in computations/ (AGENTS.md R1 note).

2026-09-06 measured on main (scripts/convention-c-value-audit.py --all): 136 confirmed convention-C bindings, 25 BLOCKING (confirmed, unadjudicated) — up from the 85 / 21-unreported figures in AGENTS.md R1. First blocking row: computations/probes/two_channel_total_binding_floor_probe.py:108. Re-run before draining; quote the live number.



## 2026-09-06 takeover (convention-auditor subagent)
Claimed on worktree branch claude/convention-c-excision-2026-09-06 from HEAD 9b009da0e6. Plan: (1) re-measure value/producer/Lean audits on this HEAD; (2) drain BLOCKING value-audit sites where z_D substitution is a valid migration (excluding two-arm comparisons, qou-cds1-blocked ladder, qou-pmkh sites); (3) survey closed gates in docs/audits + .beans whose evidence is C-frame compute; write docs/audits/2026-09-06-convention-c-excision-and-c-conditional-gates.md.



## 2026-09-06 findings (convention-auditor subagent, branch claude/convention-c-excision-2026-09-06)
MEASURED on 9b009da0e6: value audit 137 confirmed C / 26 BLOCKING / 1 UNRESOLVED (509 D); shape audit 13 actionable + 113 deliberate; Lean 24 C defs -> 3 actionable / 21 deliberate.
STEP 2 — 0 of the 26 BLOCKING sites is a live Markov-trace computation that a z_D substitution would validly migrate: 12 are two-arm C-vs-D comparisons (the C binding is the subject), 14 are the convention-C c_k ladder investigated in its own frame (qou-cds1; includes the PRODUCER qbeta_precision_ladder_n5.py, whose witness is C-frame by its own docstring). No z was swapped, no witness regenerated; all 26 adjudicated into docs/audits/convention-c-comparison-ledger.json (12 comparison / 14 deliberate-c-frame). AFTER: 137 / 137 adjudicated / 0 BLOCKING / 0 UNRESOLVED, exit 0. Note --propose-ledger stubbed only 15 of 26 (D arm a call, D via sym_int, separate def scopes, or no D arm).
DETECTORS: (row 37) Lean RE_C_SQRTVAR false positive on coneCoordRow5 q := coneRow5Numerator q/(q^2+1)^2 — guarded, 24 -> 23 C defs; (row 38) value audit cannot see z_old = 1/(q0**0.5 + qi0**0.5) (nucleon-lp-convention-probe.py:87, z_C exactly, imported inverse) and had Q0 missing from _Q_VARS (1/(Q0+1/Q0) is 1/[2]_q, NOT C; was UNRESOLVED). Two Lean markov_parameter := sqrt q/(1+q) defs docstring-scoped as convention C (qou-cds1) — NOT lean-verified (no oleans in this container). Lean AFTER: 23 C defs, 0 actionable.
STEP 3 SURVEY (from the C surface outward, 147 C files -> 43 strong-verdict citing docs/beans read): outside the c_k ladder arc the corpus's refutations bind both conventions or rest on D (class i/iii); inside it they are C-conditional and the individual docs do not say so (class ii): 2026-06-24 lw2-c2 'does not reproduce'; 2026-07-19 c3 real-routes 'pruned' (also rests on the TR_M[5] bug, qou-dbau); 2026-07-03 eta-singularity 'refuted'; 2026-06-10 ck state-of-play (10x refuted); the c3-hypersensitivity docs' VALUES (the 1/u^3 argument itself is frame-independent); 2026-08-31 imq-elliptic numbers (its |q|>1 refutation is convention-independent); q-beta-cos-resummation numbers. Full table: docs/audits/2026-09-06-convention-c-excision-and-c-conditional-gates.md §4. Not re-scoped in place (dated records); follow-up should add the scoping sentence to each and to citing content blocks.
NOT TOUCHED: qou-cds1 ladder (not a z-swap, decayLadder_zC_threeRow_ne_zero), qou-pmkh 4 sites, qou-cds2 Gram pair, qou-mass/_internal (computations/ untouched), the shape audit's 13 (renaming to satisfy it is 1a audit-dodging).
precision-gates.sh --changed: RED on the tree-wide ratchets (q0-anchor flip=1 hadron-knot-table, refill, import-time dps, never-raises-dps, float64-padding, raw-float64, value-copy, q0-drift, hardcoded braid word, mixed mpf/f64); none of this branch's files is under computations/ or named in the output; regenerated audit witnesses reverted, no baseline widened.
