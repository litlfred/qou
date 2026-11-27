---
# qou-9f1c
title: 'Issues-Cluster-1: Precision Gates, CODATA-2022 Pin Refresh & Retired Muon c3 (4 Open GitHub Issues)'
status: in-progress
type: task
priority: high
tags:
    - compute-accuracy
created_at: 2026-11-23T20:55:54Z
updated_at: 2026-11-27T14:18:23Z
parent: qou-xip2
---

Actionable GitHub Issues cluster (`4` open issues on `litlfred/qou`).

### Resolution & Closure Protocol
- Do NOT close any GitHub issue on partial progress (`Part of #...`); only close once 100% of stated deliverables have merged to `origin/main` with exact PR + commit SHA citations.
- **Special Guard on `#9154`:** Do NOT close `#9154` until BOTH Bilson-Thompson–Hackett–Kauffman 2009 `references.ts` registration (`#9157`) AND Chester–Arsiwalla–Kauffman 2025 (`arXiv:2501.03260`) library section ingestion have landed on `origin/main`.

### Open Issues in This Cluster
- **`#9104`**: Precision gates red on main: six blocking reds (q0 flip/drift, q0 refill, dps, reference-literal, value-copy) *(paired open PRs: #9105)*
- **`#8895`**: Retire muon c₃ = −2.0097 in 8 probes (qou-kt8o) *(paired open PRs: #8896)*
- **`#8010`**: Precision gates: 11 red ratchets on main
- **`#7589`**: rem-qstar-decay-sector-q0 quotes CODATA-2018 muon-pin figures *(paired open PRs: #7590)*


## 2026-11-23 — Worker 31 Issues-Cluster-1 Audit against origin/main (`e330ab6aa04`)

Verified all 4 open GitHub issues (plus guarded `#9154`) against `origin/main` (`e330ab6aa04`):
- **Closed now: 0/4** (none had 100% of deliverables already merged to `origin/main` at `e330ab6aa04`; strictly respected no-partial-close rule and `#9154` Special Guard).
- **Audited & linked with explicit status + tracking-bean comments on GitHub (4/4):**
  1. **`#9104`** (comment `#issuecomment-7118467548`): All 6 gates still red on `origin/main` `e330ab6aa04`; consolidated PR **#9237** turns 5/6 **GREEN** and drains `q0-anchor refill` `NEW: 63 -> 21`. Linked to `qou-9f1c`, `qou-1scg`, `qou-q0rf`, `qou-l7cy`.
  2. **`#8895`** (comment `#issuecomment-7118467931`): `qbeta_markov_trace_steps_4_5` `Q0_FLIP` fix is on `origin/main`; all 8 `c_3 = -2.0097` probes + witnesses are ported & full-dps upgraded in PR **#9237** (`Closes #8895` on merge). Linked to `qou-9f1c`, `qou-kt8o`, `qou-l7cy`.
  3. **`#8010`** (comment `#issuecomment-7118468322`): 5/11 ratchets (`import-time dps`, `raw-float64`, `CODATA stale-edition`, `docstring label carriers`, `mixed mpf/f64 -> serializer`) are **GREEN** on `origin/main`; remaining 6/11 match `#9104` (5/6 fixed in PR **#9237**). Linked to `qou-9f1c`, `qou-1scg`, `qou-q0rf`.
  4. **`#7589`** (comment `#issuecomment-7118468727`): `rem-qstar-decay-sector-q0.md` on `origin/main` still carries CODATA-2018 `80.3%` / `4.7e6` figures; paired PR `#7590` belongs to `PR-Drain-5` (`qou-i7r4`). Linked to `qou-9f1c`, `qou-iax1`, `qou-i7r4`.
  - **`#9154` Special Guard respected:** Kept open; PR **#9237** (`dd9498d6e10`, `Part of #9154`) registers BHK 2009 in `references.ts`, while CAK 2025 (`arXiv:2501.03260`) library ingestion awaits `#9095`.
