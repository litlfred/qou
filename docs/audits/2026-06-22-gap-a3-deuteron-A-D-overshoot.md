# A(D) follow-up: the flat baseline overshoots the deuteron binding by ~2×

**Date:** 2026-06-22
**Branch:** `claude/binding-a-d-overshoot-followup-2026-06-22`
**Status:** Positive/quantitative follow-up to the GAP-A-3 §4 probe — quantifies how far the binding
P_λ must deviate from flat. No fit; no P_λ proposed.
**Bean:** [`cbnf`](../../.beans/cbnf--categorical-binding-wiring-no-fitting.md)
**Follows:** [`2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md`](2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md) (PR #2626)
**Script:** [`computations/gap_a3_deuteron_A_D_overshoot.py`](../../computations/gap_a3_deuteron_A_D_overshoot.py)

## The comparison the §4 probe flagged

The §4 probe computed the canonical flat baseline `tr_M(β_D) = Σ_λ y_λ χ^λ(β_D) = 0.38836` and noted
that the flat (P_λ≡1) baseline would need `A(D) = 11.21` to hit `−B(D)/m_e = 4.353`. The immediate
follow-up: what is the **Phase-4-derived** `A(D)`?

`A(K) = Vol_hyp(K)/[8]_q · [3]_q^{2(Z-1)} · (q^{1/2}+q^{-1/2})^{4N}` (gap-a3 scope, ≤2.5%
zero-parameter). For the deuteron (Z=1, N=1): `[3]_q^0 = 1`, `Vol_hyp(D) = 12.776` (PR #787 Phase-3,
Z=1 cluster):

| factor | value |
|--------|-------|
| `Vol_hyp(D)` | 12.776 |
| `[8]_q` | 8.9457 |
| `(q^{1/2}+q^{-1/2})^4` | 16.0873 |
| **`A(D)` derived** | **22.975** |

## Result — the flat baseline overshoots by ~2.05×

| quantity | value |
|----------|-------|
| flat baseline `A(D)·tr_M(β_D)` | **8.923** |
| target `|−B(D)/m_e|` | 4.353 |
| **overshoot factor** | **2.050** (band `[2.00, 2.10]` from A(D)'s ≤2.5%) |
| required `[Σ y_λ χ^λ P_λ]/tr_M` | **0.488** |

So the Phase-4 `A(D)` is **22.98, not 11.21** — the flat (`P_λ≡1`) baseline **overshoots** the deuteron
binding by `~2.05×`. The bar-even P_λ redistribution must therefore **suppress** the effective trace to
**~48.8% of flat**. Combined with the §4 finding that the flat trace is **bar-mixed**, the deuteron's
P_λ must do two things: **bar-symmetrise** the trace, and **roughly halve** its magnitude.

## Critical-distance note

The overshoot `≈ 2.05` is **consistent with exactly 2** within A(D)'s ≤2.5% uncertainty band
(`[2.00, 2.10]`) — but it is **not pinned to 2**. A clean "factor of ½" suppression (`P_λ` halving the
trace) is *suggestive* but **not forced**; asserting it — or any specific `P_λ` reproducing 0.488 —
would be a fit, which the Δ_λ gate forbids. Reported as `≈2.05`, no value proposed.

## Net (binding thread, this session)

Two concrete, non-fit results now characterise the deuteron Δ_λ redistribution:
1. **(#2626)** the flat trace is **bar-mixed**, so the bar-even P_λ must carry an O(1) symmetrising part;
2. **(here)** the flat baseline **overshoots by ~2.05×**, so P_λ must suppress the effective trace to ~49%.

The open derivation is unchanged: a **categorical** P_λ (in the dim-6 bar-even subspace) that
simultaneously bar-symmetrises and ~halves the flat trace — derived, not fitted. That is the genuine
GAP-A-3 research core; this follow-up bounds *what it must achieve* without proposing it.

No fit; nothing wired; `c_k`/`Δ_λ` cal-anchored.

## Cross-references

- [`2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md`](2026-06-22-gap-a3-deuteron-plambda-flat-baseline-bareven.md) — the §4 flat-baseline + bar-even probe this extends.
- [`2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — the A(K) formula + the §4 closure.
