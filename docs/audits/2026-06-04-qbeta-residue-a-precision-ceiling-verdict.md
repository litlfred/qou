# Residue-A precision ceiling — verdict: A reaches only ~4 sig figs

**Date:** 2026-06-04
**PR:** [#1805](https://github.com/litlfred/qou/pull/1805) ([branch](https://github.com/litlfred/qou/tree/claude/qbeta-residue-a-precision-ceiling-2026-06-04))
**Status:** NEGATIVE (A cannot reach ≥30 — or even ≥15 — digits from current data)
**Plan:** [2026-06-04-qbeta-residue-a-precision-ceiling-plan.md](./2026-06-04-qbeta-residue-a-precision-ceiling-plan.md)

## Question

Can residue A be recomputed to ≥ 30 digits to unblock the PR #1804 D3
PSLQ period probe?

## Answer: NO — A is reliable to ≈ 4 significant figures only

Script:
[`qbeta_residue_a_precision_ceiling.py`](../../computations/qbeta/qbeta_residue_a_precision_ceiling.py)
· witness `qbeta-residue-a-precision-ceiling.witness.json`.

Notation: `x_k := c_k·u_subst^k`; `L := lim_k x_k ≈ 2.118e-13` (tail
limit); **residue `A := u_subst·L ≈ 1.804e-15`**. `u_subst` is exact, so
A and L share the same relative precision.

### 1. The spread is intrinsic, not compute noise

| compute dps | tail_mean (k=8,9,10) | rel_spread |
|---|---|---|
| 50 | 2.1179447222e-13 | 1.9553e-4 |
| 80 | 2.1179447222e-13 | 1.9553e-4 |
| 120 | 2.1179447222e-13 | 1.9553e-4 |

The tail spread is **stable** as compute precision rises 50→120 dps ⇒ it
is the **intrinsic asymptotic spread**, confirming arithmetic precision
is *not* the limiter (the c_k are already 50 dps).

### 2. Extrapolation cannot recover the digits

The k→∞ limit `L` via four estimators (120 dps):

| estimator | L |
|---|---|
| raw mean (8,9,10) | 2.11794472225e-13 |
| Aitken Δ² (8,9,10) | 2.11774424551e-13 |
| Aitken Δ² (7,8,9) | 2.11773229462e-13 |
| 3-pt geometric (8,9,10) | 2.11774424551e-13 |

The 3-point geometric solve gives `ρ = −0.0219` — **negative**, hence
**not a clean single-geometric** convergence (`x_k = L + B·ρ^k` with
ρ<0 means the 3 points don't lie on one decaying exponential; the fit
is unreliable). The estimators **disagree at 9.5×10⁻⁵ relative**, so:

> **achievable digits ≈ 4.0** — both for L and for the residue A = u_subst·L.

### Verdict

- **≥ 30 digits (period-search grade): NO.**
- **≥ 15 digits (12-constant PSLQ grade): NO.**
- A / L are reliable to **≈ 4 significant figures** from the canonical
  c_2…c_10.

The precision ceiling is set by having only **three rungs** (k=8,9,10) in
the asymptote, **not** by arithmetic precision. Bumping dps does nothing;
the D3 period reframe **cannot be tested** at this precision, and cannot
be unblocked by recomputation alone.

## The genuine unblock path

To raise A's precision one must **extend the asymptote with more rungs**:
a higher-order **canonical** extraction of c_11…c_15 — proved / near-match
closed forms per rung, extending the existing c_2…c_10 ladder. This is a
**separate research program**, NOT an ansatz fit (which the Step-1 method
note and CLAUDE.md forbid). With ~6 more rungs the asymptote tightens
geometrically and Aitken/Richardson could then reach period-search grade.

This reframes the standing recommendation: the residue-A structural
search (categorical *or* period) is gated not on "recompute A" but on
**deriving canonical higher-order c_k** — the same gap that blocked
Step 1 of PR #1727 from extending past c_10.

## Anti-pattern compliance

- ✅ No ansatz for c_11+; extrapolation used only canonical c_2…c_10.
- ✅ Extrapolated A/L reported with an explicit error bar (4 sig figs);
  no over-claiming.
- ✅ A-vs-L notation corrected (residue A = u_subst·L) per Gemini #1805.
- ✅ u_subst / c_k from canonical witnesses; diagnostic-only.

## Cross-references

- PR #1727 — residue A Step 1 (the c_k tail source).
- PR #1804 — D3 period reframe, gated on this precision question.
- [1ppQ master ledger](../coordination/1ppq-qbeta.md).
