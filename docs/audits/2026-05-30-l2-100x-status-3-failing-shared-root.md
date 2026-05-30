# 2026-05-30 — L2 100× status audit: 3 of 7 fail, shared root cause

**Trigger.** User-prioritised item 3 of the post-#1485 next-tranche queue ("L2 100× gaps for the missing 2 observables").

**Source.** [`folio-assistant/computations/per-observable-100x-status.witness.json`](../../folio-assistant/computations/per-observable-100x-status.witness.json) (`computedAt: 2026-05-30T03:44:59Z`, commit `3fda58749d`).

## Headline

The L2 dashboard tracks 7 observables — not 6 as stated in `CLAUDE.md §Precision goals` (the `m_K/m_π` meson ratio was added after that section was written; refresh PR pending). Current status:

| obs | role | 100× target met? | `miss_factor` | `err_ppb` | gating witness |
|---|---|:--:|---:|---:|---|
| `m_p` | CAL-2 anchor | ✓ | 0.1306 | 0.0004037 | `m-p-substrate-identity-50dps.witness.json` |
| `m_μ` | validation | ✓ | 1.6e−42 | 3.4e−43 | `m-p-borromean-verification-50dps.witness.json` |
| `m_e` | CAL-1 anchor | ✓ | N/A (anchor) | 0 | — |
| `m_K/m_π` | validation (meson) | ✓ | 0.08892 | 23.44 | merged PR #1455 |
| `Q_β` | **CAL-3 anchor** | ✗ | **159.9** | 1247. | `q-beta-operator-valued-N3.witness.json::Q_N2` |
| `m_n` | validation | ✗ | **180.8** | 1.039 | Path C: `m_p(substrate) + Q_β(N=5) + m_e`, no flavor-split |
| `Δ_pn` | validation (derived) | ✗ | **159.3** | 754.8 | Path C, same chain |

## Shared root cause

All three failing observables share **one** structural input: the τ_M Kashiwara derivation of `Q_β` truncated at k=2 with "k≥3 fitted rungs dropped as non-canonical" (per the `Q_N2` source-witness annotation). Specifically:

- `Q_β` directly consumes the truncated τ_M derivation → misses by ~160×.
- `m_n = m_p(substrate) + Q_β + m_e` propagates the `Q_β` miss → misses by ~180×.
- `Δ_pn = m_n − m_p` is a derived quantity → misses by ~160× (essentially equals `Q_β + m_e` modulo small reweighting).

The miss factors cluster tightly in the 160–180× band — a single underlying gap, not three independent calibration issues.

## Closure path

This is **not a Lean discharge or single-session foreground task.** The Δ_λ gate (per `CLAUDE.md §Precision goals → Δ_λ gate`) explicitly bars another fit-based ansatz; six closure ansätze (Frobenius co-Casimir, Demazure-fibre, LP-Plancherel, LP-Frobenius, crystal-graph, augmented Markov) have all failed on the deuteron. The productive directions are:

1. **GAP-A-3 / GAP-A-4** — categorical brane-tower level selection / ρ general rule.
2. **Option E** — Kashiwara crystal extension of the τ_M derivation to k ≥ 3 with canonical (non-fitted) rung-selection rule, displacing the current k=2 truncation. See [`docs/audits/2026-05-18-delta-lambda-gating-context.md`](2026-05-18-delta-lambda-gating-context.md).

Both are research-grade, multi-session, and currently active under the Phase 2 IwahoriHecke sprint (`57783eebb sprint2-iwahori`, etc.).

## Scope-of-this-audit

Audit only — no scripts re-run, no witnesses regenerated, no math advanced. Documents the **shared root cause** of the three failing observables so future agents stop pattern-matching on "two observables" (per `CLAUDE.md`) and recognise this as a single Q_β-derivation gap with two propagated derivatives.

## Sub-goal placement

- **Subgoal-1 path** (achievable, ≥ ~780 ppb CAL-2 floor): per-isotope Borromean-tower extension + operator-valued branching combiner. Owner-active. The 100× targets for `Q_β`, `m_n`, `Δ_pn` are all above the CAL-2 floor — Subgoal-1 closure would suffice.
- **Subgoal-2 path** (research-grade, < CAL-2 floor): not relevant for the three failing observables here; only relevant for absolute `m_p` / `m_n` / `m_⁴He` predictions.

## Sibling-PR coordination

The active Phase 2 IwahoriHecke sprint (sibling commits `57783eebb`, etc.) is the direct vehicle for Option E (Kashiwara crystal extension). Any new branch attacking the Q_β k=3 rung-selection should coordinate with that sprint via the `coordinate.md` skill — overlap at `lean/QOU/IwahoriHecke/*.lean` is near-certain.

## Status update for CLAUDE.md §Precision goals

The current section states "4/6 met". Actual current status is **4/7 met** (`m_p`, `m_μ`, `m_e`, `m_K/m_π`) — the discrepancy is the `m_K/m_π` meson ratio addition after `CLAUDE.md` was last refreshed. **Follow-up:** quick `CLAUDE.md` refresh PR to update the count + add a sentence pointing readers to this audit doc for the shared-root-cause analysis.
