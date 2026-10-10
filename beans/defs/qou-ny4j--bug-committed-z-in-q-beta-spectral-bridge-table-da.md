---
# qou-ny4j
title: 'BUG: committed z in q-beta-spectral-bridge-table-data is 73.6 ppQ off'
status: completed
type: bug
priority: high
created_at: 2026-08-06T22:36:24Z
updated_at: 2026-08-06T22:46:15Z
---

z = 0.499320334033598 committed in content/quantum-observable-universe/nuclear-interactions/q-beta-spectral-bridge-table-data.md. Exact value at 65 dps from the canonical 50-digit muon-pinned q0 is 0.4993203340335612717689664 -- relative discrepancy 7.36e-14 = 73.6 ppQ, exceeding the L1 <=1 ppQ internal-agreement goal by ~74x. CAUSE DIAGNOSED: not the proton/muon pin (that shifts z by 3e-10, ~4000x larger) and not float64 (float64 reproduces the exact value to 6.4e-17 and does NOT give the committed digits). The q0 that reproduces the committed z exactly is 1.10997859555420..., differing from canonical at the 12th digit -- i.e. a STALE / under-converged q0, the q0-repin staleness class. Fix: recompute z from the canonical q0 at 65 dps and refresh the table + any dependent witness. Found during T3h (qou-mcwm).
