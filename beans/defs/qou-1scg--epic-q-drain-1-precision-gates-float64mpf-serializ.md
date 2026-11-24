---
# qou-1scg
title: 'EPIC [Q-Drain-1]: Precision Gates, Float64/mpf Serialization & Witness Provenance Hygiene'
status: in-progress
type: epic
priority: high
created_at: 2026-11-23T20:55:45Z
updated_at: 2026-11-24T00:12:27Z
parent: qou-hksc
blocking:
    - qou-xip2
---

**Theme:** Precision Gates, Float64/mpf Serialization & Witness Provenance Hygiene
**Rationale:** Fixes blocking precision/q0-anchor/provenance ratchets at producer level (>=50-80 dps mpmath, zero float64).
**Child Beans (13):** `qou-y7ek`, `qou-f64g`, `qou-ke35`, `qou-lz8f`, `qou-qrsp`, `qou-w3dm`, `qou-q0rf`, `qou-sogb`, `qou-j540`, `qou-5c64`, `qou-brkp`, `qou-jdrx`, `qou-w1u2`

### Prioritized Beans in This Batch
- **`qou-y7ek`** (`high`, `todo`) — PPQ-1 (L1): 80-dps Newton Anchor Round-Trip Polish (2.85 ppt -> < 1e-80 on m_p/m_e -> q_0, q_2t) *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-f64g`** (`high`, `in-progress`) — INFRA (gated + measured): float64 entry points in mpmath probes — 17546 hits, 4 prior beans, no gate until now
- **`qou-ke35`** (`high`, `todo`) — The mpf migration of the constant modules is HALF DONE, and a consumer that never raises mp.dps now records 15 digits where it used to record 17
- **`qou-lz8f`** (`high`, `in-progress`) — A producer that cannot serialize an mpf DESTROYS its witness on every run — 38 candidates, and qou-geqa's crash class refills
- **`qou-qrsp`** (`high`, `in-progress`) — PRODUCER FIX: 37 of 45 measured producers re-pad float64 on re-run (qou-gqt5 follow-up)
- **`qou-w3dm`** (`high`, `in-progress`) — MAIN-SIDE: ~508 of 2749 witnesses carry a drifted scriptHash (18%)
- **`qou-q0rf`** (`high`, `todo`) — The q0-anchor refill ratchet is RED on main (NEW 147) — and the arrival rate, not the backlog, is the thing to fix *(Rule 13a: 0-instance classes: `Stripped`)*
- **`qou-sogb`** (`high`, `todo`) — r5-full-canonical-knot-solver: scriptHash MATCHES and 733 fields move deterministically — the documented ''diff the producer first'' check says safe and is wrong *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-j540`** (`high`, `in-progress`) — prop:demand-stability is marked verified against a float64 witness blind at Z=82 — and its successor is not a drop-in replacement
- **`qou-5c64`** (`high`, `todo`) — binding-single-pipeline-comparison is 3 months stale and RED when re-run — 2 assertions flip, one column moves 69x, and the float64 drain is blocked behind it *(Rule 13a: Rule 13a `stays open`/conjecture guard)*
- **`qou-brkp`** (`high`, `todo`) — BUG (fixed) + stale witness: a dps remediation broke 2 producers, and its own gate reported them clean
- **`qou-jdrx`** (`high`, `todo`) — VS-2 (P0 Substrate & Facade): Export 50-dps q_2t Pin, Drain Muon/Proton Pin Straddle, and Excise Float64 Constants in Core Facades
- **`qou-w1u2`** (`high`, `todo`) — Regenerate Stale Upstream Dashboard Witnesses & Add add_upstream() Provenance

### Worker Protocol
- Claim individual child beans via `beans update <bean-id> --status in-progress --body-append "Claimed by <branch> (YYYY-MM-DD)"`.
- Never mark a bean `completed` while an uninstantiated conjecture `class` or explicit `stays open` item remains (AGENTS.md Rule 13a).
- Enforce single-thread CPU caps (`LEAN_NUM_THREADS=1`, `nice -n 15`), zero float64 (`mpmath` >= 50-80 dps), and zero fitting.
