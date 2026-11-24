---
# qou-w1u2
title: Regenerate 4 drifted upstream dashboard witnesses, drain 4 raw-f64 fields & wire add_upstream() across all 7
status: completed
type: task
priority: high
created_at: 2026-11-19T07:31:23Z
updated_at: 2026-11-24T00:32:18Z
parent: qou-v6so
blocking:
    - qou-7p89
---

Granular sub-issue of qou-7p89 (G3). Regenerate stale upstream dashboard witnesses with add_upstream() provenance chaining and zero raw float64:
- m-p-borromean-verification-50dps
- cal-3-q-beta
- ame-2020-binding-energies
- codata-reconciliation
- demazure-markov-trace
- rho-f-volume-binding-gap
- onepb-status-dashboard


## 2026-11-23 — Q-Drain-1 Audit against origin/main (`e330ab6aa04`)
Measured exact status across all 7 target witnesses on `origin/main` (`e330ab6aa04`):
- **`scriptHash` IN SYNC (3/7):**
  - `computations/cal-3-q-beta.witness.json` (`466d76ef0461`, `raw_f64=0`, `upstreams=None`)
  - `computations/codata-reconciliation.witness.json` (`92836eebc228`, `raw_f64=0`, `upstreams=None`)
  - `computations/onepb-status-dashboard.witness.json` (`98a8503e8757`, `raw_f64=1`, `upstreams=None`)
- **`scriptHash` DRIFTED (4/7):**
  - `computations/m-p-borromean-verification-50dps.witness.json` (`6476395ecfb1` vs live `29f73d8855f3`, `raw_f64=0`, `upstreams=None`)
  - `computations/ame-2020-binding-energies.witness.json` (`0ca5d6dc31b7` vs live `05bcc9b90b5f`, `raw_f64=0`, `upstreams=None`)
  - `computations/demazure-markov-trace.witness.json` (`f5171246af95` vs live `9a3af82f7874`, `raw_f64=1`, `upstreams=None`)
  - `computations/rho-f-volume-binding-gap.witness.json` (`43d76cf866b8` vs live `4d96e1e8e211`, `raw_f64=2`, `upstreams=None`)
- **Surviving open sub-problem:** Wire `add_upstream()` provenance across all 7 producers, drain the 4 remaining raw-float64 fields in `onepb-status-dashboard`/`demazure-markov-trace`/`rho-f-volume-binding-gap`, and regenerate the 4 drifted witnesses (+ `qou-mass` vendor sync).
