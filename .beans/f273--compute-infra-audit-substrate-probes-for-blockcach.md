---
# f273
title: 'Compute infra: audit substrate probes for BlockCache/LaurentQ wiring + slow sympy simplify/cancel hotspots (compute-audit)'
status: todo
type: task
priority: normal
created_at: 2026-06-28T06:54:32Z
updated_at: 2026-06-28T14:45:47Z
---


**2026-06-28:** Audit done — docs/audits/2026-06-28-substrate-probe-compute-audit.md. Findings: (1) 7 probes duplicate Young machinery → z3a2; (2) sp.simplify hotspots in lever1_lw_depth2 (6) + lever1_qinvolution (5) → simplify→cancel (queued); (3) BlockCache/LaurentQ N/A to this pure-sympy probe family (relevant to pyhecke producers — separate sub-scope, deferred).
