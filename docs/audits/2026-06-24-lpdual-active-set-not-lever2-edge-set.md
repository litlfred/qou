# The LP-dual active set (blocks) is NOT lever-2's binding edge-set (bonds)

**Date:** 2026-06-24
**Branch:** `claude/lever2-lpdual-blocks-vs-bonds-2026-06-24`
**Status:** NEGATIVE result — records a non-connection so lever-2 does not chase it. No fit.
**Probe:** [`computations/probes/lpdual_active_set_vs_edge_set_negative.py`](../../computations/probes/lpdual_active_set_vs_edge_set_negative.py)
**Witness:** [`computations/probes/lpdual-active-set-vs-edge-set-negative.witness.json`](../../computations/probes/lpdual-active-set-vs-edge-set-negative.witness.json)

## Question (binding-levers follow-up to PR #2661)

PR #2661 found the qbk2 Reeb-propagator correction is 94.9% supported on the 7
deuteron LP-dual **active channels** (Wedderburn blocks `λ ⊢ 6`, `y_star > 0`):
`{(6,), (5,1), (4,2), (4,1,1), (3,3), (2,2,2), (2,1,1,1,1)}`. Lever 2 of the
Δ_λ-gate ([three-lever status §Lever 2](2026-06-23-delta-lambda-three-lever-status.md);
[`PauliChannelBinding.lean`](../../content/quantum-observable-universe/lean/QOU/Hecke/PauliChannelBinding.lean);
bean `w5tg`) has an open **occupancy** gate. **Is the LP-dual active set the
edge-set lever-2 must derive?**

## Cross-tab (deuteron, `λ ⊢ 6`)

| block | rows | cols | n(λ) | chirality | y_star | active |
|-------|-----:|-----:|-----:|:---------:|-------:|:------:|
| [6] | 1 | 6 | 0 | + | 1.80 | YES |
| [5,1] | 2 | 5 | 1 | − | 0.69 | YES |
| [4,2] | 2 | 4 | 2 | + | 0.23 | YES |
| [4,1,1] | 3 | 4 | 3 | − | 0.10 | YES |
| [3,3] | 2 | 3 | 3 | − | 1.05 | YES |
| [3,2,1] | 3 | 3 | 4 | + | 0 | no |
| [3,1,1,1] | 4 | 3 | 6 | + | 0 | no |
| [2,2,2] | 3 | 2 | 6 | + | 3.04 | YES |
| [2,2,1,1] | 4 | 2 | 7 | − | 0 | no |
| **[2,1,1,1,1]** | **5** | **2** | **10** | + | **29.7** | **YES** |
| [1⁶] | 6 | 1 | 15 | − | 0 | no |

## Verdict — NO connection

1. **Different objects.** The LP-dual active set is **Wedderburn blocks**
   (partitions). Lever-2's edge-set is **nucleon bonds** — the Pauli result
   `−q⁻¹ < 0` proves p–p/n–n bonds (forced antisymmetric) are unbound, only p–n
   survive; the open gate is the **Z·N p–n occupancy count**. Bonds ≠ blocks.

2. **No clean block-level rule.** No simple statistic — rows
   (active {1,2,3,5} vs inactive {3,4,6}), cols, n(λ), or chirality — separates
   active from inactive; every range overlaps.

3. **Only the Pauli endpoints agree.** `[6]` (fully symmetric) is active and
   `[1⁶]` (fully antisymmetric) is inactive — consistent with Pauli. But the
   **interior breaks** any "symmetric binds / antisymmetric doesn't" gradient:
   `[2,1,1,1,1]` (5 rows, near-antisymmetric, n(λ)=10) is the **most**-active
   block (`y_star` 29.7), while the balanced self-conjugate `[3,2,1]` is
   **inactive** — the opposite of what a symmetry rule predicts.

4. **Moot anyway — the LP-dual is degenerate.** The deuteron raw LP-dual has
   `duality_gap ≈ 4.4×10⁴` (strong duality fails on the full space). The active
   *set* is robust (the gap-0 phase agrees on the 7 blocks), but the
   shadow-price *magnitudes* — including the 29.7 — are unreliable, so there is
   no solid block-level structure to map onto the edge-set even in principle.

## Consequence for lever 2

The block-active-set is **not** lever-2's bond-occupancy answer; they are
different-level objects. Only the two Pauli endpoints are consistent, and
lever-2 already has those from `PauliChannelBinding.lean`. This is a recorded
**negative** — it removes a candidate lead (floated in the binding-levers
triage) so the `w5tg` occupancy work is not spent re-checking it. The genuine
lever-2 gate (the Z·N p–n occupancy, owner-gated to the s5-so3 keystone) is
untouched by this finding.
