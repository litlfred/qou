# Q_β Wenzl-Habiro keystone — coordination ledger

**Branch:** `claude/qbeta-wenzl-habiro-keystone-2026-06-01`
**PR:** [#1642](https://github.com/litlfred/qou/pull/1642)
**Goal:** Identify the explicit Q_β Habiro element categorical formula by wiring the level-2 SU(2) Wenzl identification (PR #1625 merged) into a concrete ansatz that reproduces the known c_2 = −1 (Taylor-exact) and c_3 = −2 (near-match) coefficients and predicts c_4–c_7 Taylor-exactly. Closing this would flip Q_β / m_n / Δ_pn from `near-match` to `proved` and meet the 1ppQ goal.

## The Wenzl-Habiro ansatz hypothesis

Q_β-Habiro(X) = (Wenzl factor at ζ_8) · (pair-specific Δ from p, n)

The Wenzl factor encodes the level-2 SU(2) Verlinde annihilator (`[4]_q = 0` at q = ζ_8, partitions first-column ≥ 4 negligible). The pair-specific Δ encodes the proton-asymmetry observed in PR #1625 (Φ_8 cancellation present iff p NOT in pair).

## Three tracks in parallel

1. **Wenzl→Q_β ansatz construction** — the keystone formula. (this branch's main thread)
2. **α_EM-parallel retry with Wenzl factor** — apply the `[2]_q·(1−h²α)` template (PR #1511) to Q_β with the new Wenzl context.
3. **Extend canonical Habiro data to A=5,6,7** (⁵Li, ⁶Li, ⁷Li, ⁷Be) — more data for Habiro recursion + mirror-pair (⁷Li/⁷Be) Φ_1·Φ_2 test.

## Context from merged PRs

| PR | HEAD | Findings |
|---|---|---|
| #1579 | `57b5fa2d3a` | CAL-3 = m_π corroborated; Lean strand-doubling Φ_8 = Φ_4(X²) |
| #1618 | `e7872b8907` | Phase 5q convention test + canonical helium Habiro + Lean a_8 partition + strand-doubling FALSIFIED |
| #1625 | `a3f84cce8b` | Level-2 SU(2) Wenzl categorical witness IDENTIFIED + Lean ζ_8 lemmas + Wenzl tower FALSIFIED at higher ζ_n + Φ_8 proton-CONDITIONAL |

## Status

- **L1 (cross-method compute precision at q₀, target ≤ 1 ppQ)**: MET — `_precision.py` default 65 dps compute / 50 dps serialization, per AGENTS.md §Precision goals + [`docs/precision-goals.md`](../precision-goals.md).
- **L2 (per-observable accuracy, target σ_pred ≤ σ_exp/100)**: 3/7 met; Q_β, m_n, Δ_pn share c_k tier wall root; m_μ misses 963.6× (post-re-pin).
- c_2 = −1 Taylor-exact PROVED
- c_3 = −2 near-match SETTLED (J_Hopf(q=1))
- c_4-c_7 cal-anchored (note: the earlier "c_4-c_7 below CODATA resolution" framing was retracted on 2026-06-01 — it was a tautology of a recursive single-point fit, not a precision floor; see `docs/audits/2026-06-01-qbeta-wenzl-habiro-ansatz.md` correction)
- N=7 needed for 1ppQ per truncation-order math (commit `6ace8153e`)

## Master ledger

- [`1ppq-qbeta.md`](1ppq-qbeta.md) — 1ppQ Q_β authority
