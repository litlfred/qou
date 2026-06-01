# Quantum Observable Universe — STATUS

> Always-current dashboard for the QOU folio. Each row links to the
> **master ledger** for that goal. Agents update relevant ledgers at
> session start (intent) + session end (results).

> Convention: see `.claude/skills/local/session-intent.md` (TBD)
> and `.claude/skills/local/coordinate.md` for the ledger discipline.

## Goals + ledgers

| Goal | Status | Ledger | Active PRs |
|------|--------|--------|------------|
| **L1: 1 ppb compute precision** | met (50 dps default, 10⁻⁵⁰ truncation) | `docs/coordination/1ppb.md` | — |
| **L2: per-observable 100× exp** | 3/7 met post-re-pin (m_p, m_e, m_K/m_π); m_μ is 209.8 ppb (NOT met — independent μ–p floor, not the Q_β chain) | `folio-assistant/computations/per-observable-100x-status.witness.json` | #1576 (m_K/m_π fix) |
| **1 ppQ — Q_β only (achievable)** | open; c_2 Taylor-exact, c_3 q_0-dependent (NOT Taylor); c_4–c_7 §3b-cond classes locked (PR #1587); eigenphase ≠ f falsified at u¹ (PR #1602) | [`1ppq-qbeta.md`](docs/coordination/1ppq-qbeta.md) | #1602 |
| **Δ_λ closure (Option-E)** | deuteron CLOSED; A=3 mirror pair at 0.11% near-match — (1+q)/2 NOT yet derived | [`option-e.md`](docs/coordination/option-e.md) | #1516 |
| **α_EM canonical derivation** | RT Phase 3 + Schwinger; Habiro element `[2]_q·(1-h²α)` derived (PR #1511); Bring residue → resolvent | [`alpha-em.md`](docs/coordination/alpha-em.md) | #1505, #1521, #1549, #1552 |
| **Q_β c_k flip-flop prevention** | enforcement live on main (PR #1577 merged: canonical-no-negative-result + ck-tiered-not-binary) | (lives in 1ppq-qbeta.md flip-flop history) | — |
| **Lean uniqueness wiring** | ~18% witness coverage | (per-PR) | #1572 |
| **Mass-sweep gap (A ≥ 4)** | mean abs err 4.25%; ⁶Li/⁷Li/⁹Be/¹¹B/¹⁴N/¹⁹F GAP (no atom→knot rule) | (lives in option-e.md) | — |

## Cross-cutting queues

| Queue | Purpose | Items |
|-------|---------|-------|
| [`todos/1ppq-qbeta-queue.json`](todos/1ppq-qbeta-queue.json) | Per-goal 1ppQ-Q_β work | 6 (3 done, 1 in_progress, 2 blocked) |
| [`todos/lean-discharge-queue.json`](todos/lean-discharge-queue.json) | Mechanical Lean sorry discharge (NOT §3b-cond) | 8 items + 1 registry of permanent sorries |
| [`todos/research-queue.json`](todos/research-queue.json) | Research-grade open items across goals | 7 items (Q_β Habiro, Φ_q×spectral, (1+q)/2, multi-nucleon A=4, atom→knot A≥5, fibre/observable doc, q_0 declined) |

## Active sessions

| Agent | Branch | Goal scope | Started | Status |
|-------|--------|------------|---------|--------|
| Claude (coord-infra) | `claude/coord-infra-1ppq-2026-05-31` | coord infrastructure + 1ppQ Q_β kickoff | 2026-05-31 | active |
| Claude (CAL-3 hunt) | `claude/brave-mendel-FPxFl` (PR #1579) | CAL-3 = m_π corroboration + parallel c_3 + v9 (1+q)/2 + L2 3-failing diagnosis | 2026-05-31 | active — see [`docs/coordination/2026-05-31-cal-3-m-pi-hunt.md`](docs/coordination/2026-05-31-cal-3-m-pi-hunt.md) |

## Conventions

- **Read this file first** at session start. Every agent.
- **Update the relevant ledger** with intent at session start; results at session end.
- **Watch main** continuously (per `.claude/skills/local/watch.md`); log relevant landings to ledger.
- **Coordinate with siblings** via `.claude/skills/local/coordinate.md`; cross-link active PRs in this table.
- **STATUS.md is a board, not a narrative.** Use master ledgers for chronology + open probes + retraction history.

## Last updated

2026-05-31 by Claude (coord-infra-1ppq-2026-05-31 session).
