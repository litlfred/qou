---
# qou-htsi
title: 'Convention C excision: sibling-found stale C sites and compute-closed gates to re-examine (owner 2026-09-06)'
status: todo
type: task
priority: normal
created_at: 2026-09-06T09:38:55Z
updated_at: 2026-09-06T10:05:22Z
parent: qou-2akx
---

Owner, 2026-09-06 (verbatim): 'Be suspicious of closed gates based on compute. Lots of stale and sibling found convention C still around. Need to excise that.' Queued (not pivoted) behind the NZ derivation (qou-n2cl). Scope: (1) re-run scripts/convention-c-value-audit.py and scripts/convention-c-producer-audit.py on main; (2) list every 'closed' / 'refuted' / 'gate' verdict in docs/audits and .beans whose evidence is a computation run under convention C (z = sqrt(q)/(q+1)) and mark it C-conditional; (3) drain what qou-t9r1 / qou-pmkh have not. Value audit last measured 85 C bindings in computations/ (AGENTS.md R1 note).

2026-09-06 measured on main (scripts/convention-c-value-audit.py --all): 136 confirmed convention-C bindings, 25 BLOCKING (confirmed, unadjudicated) — up from the 85 / 21-unreported figures in AGENTS.md R1. First blocking row: computations/probes/two_channel_total_binding_floor_probe.py:108. Re-run before draining; quote the live number.
