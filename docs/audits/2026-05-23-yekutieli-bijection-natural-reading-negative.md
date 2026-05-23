# Yekutieli per-cell bijection at H_4 — natural-reading NEGATIVE

**Date:** 2026-05-23
**Branch:** `claude/yekutieli-formalization-2026-05-23`
**Conjecture:** [`docs/audits/2026-05-22-yekutieli-percell-conjecture-formalized.md`](2026-05-22-yekutieli-percell-conjecture-formalized.md) §Conjecture
**Status:** Load-bearing bijection claim **NOT** supported by partition combinatorics under the natural reading of `Π_HS`.

## Goal

Per user direction (2026-05-23 follow-up to PR #976): attempt the
explicit `cell ↔ H_4-partition` bijection construction for the
load-bearing step of the Yekutieli per-cell curvature conjecture:

> `Π_HS ∘ τ_q` at h² order extracts curvature contribution of
> EXACTLY ONE of the 8 ideal octahedra in the 𝓑_3-complement
> tessellation = `−G·h²`.

The audit's combinatorial sketch (2 + 4 + 2 = 8 cells, paired
with the 5 partitions of H_4 via vertex/edge/center decomposition)
hints at the bijection but doesn't construct the
"extracts ONE cell" mechanism.

## Empirical findings

Computed via [`yekutieli_bijection_construction_h4.py`](../../folio-assistant/computations/yekutieli_bijection_construction_h4.py)
using the Richardson-extrapolated q-hook formula at 50 dps:

| Partition λ | dim V_λ | κ_λ (h² coeff) | Conjugate λ^T |
|-------------|--------:|---------------:|---------------|
| (4)         |       1 |              0 | (1,1,1,1)     |
| (3,1)       |       3 |              1 | (2,1,1)       |
| (2,2)       |       2 |              1 | (2,2)         |
| (2,1,1)     |       3 |              1 | (3,1)         |
| (1,1,1,1)   |       1 |              0 | (4)           |

**Sanity checks (PASS):**

- `Σ_λ κ_λ = 3` — consistent with the proved Family A theorem
  `(1/4) · Σ_λ dim_q V_λ = 5/2 + (3/4)·h²`.
- κ is symmetric under conjugation involution at h² order:
  `κ_(4) = κ_(1^4)`, `κ_(3,1) = κ_(2,1,1)`, `κ_(2,2)` self-conjugate.

## Half-symmetric projection under the natural reading

Take `Π_HS` to be averaging over the conjugation involution
`λ ↔ λ^T` on Wedderburn blocks (the simplest natural definition
of a "half-symmetric" projection):

| Class             | κ_λ | κ_{λ^T} | (κ_λ + κ_{λ^T})/2 |
|-------------------|----:|--------:|------------------:|
| (4) ↔ (1,1,1,1)   |   0 |       0 |                 0 |
| (3,1) ↔ (2,1,1)   |   1 |       1 |                 1 |
| (2,2) self-conj   |   1 |       1 |                 1 |
| **Σ_classes**     |     |         |             **2** |

`Σ_classes / 4 = 0.5·h²`

**vs audit claim:** `−G·h² ≈ −0.916·h²`

**Discrepancy:**

- **Sign:** + (empirical) vs − (audit)
- **Magnitude:** 0.5 (empirical) vs 0.916 (audit); factor of 1.83 off
- **Both differ too much to be a precision issue** — structural mismatch.

## Implications for PR #976 (Yekutieli Strategy I)

[PR #976](https://github.com/litlfred/qou/pull/976) wired the
Yekutieli-extended λ_scale

```
λ_Yekutieli(q) := 5/2 + (3/4 − G)·h²  ≈ 2.49266 at q_0
```

into a comparison-only compute (`lambda_yekutieli_extended_borromean.py`),
predicting m_p ≈ 950 MeV (1.26 % vs CODATA, **halving** the canonical
~2.89 % m_p gap).

This empirical result shows the load-bearing categorical justification
(audit's "half-sym extracts ONE cell" claim) is **not supported** by
partition combinatorics under the natural reading of `Π_HS`.

**Therefore the numerical 950 MeV match in PR #976 is currently:**

1. **Either** a coincidence that doesn't reflect a substrate-pure
   categorical derivation;
2. **Or** evidence that the audit's `Π_HS` is a different operator
   than conjugation-averaging — needing a precise definition;
3. **Or** Yekutieli 2015's non-abelian Stokes machinery transforms
   the partition κ-sum into a curvature-2-form integration whose
   value is genuinely `−G·h²` (this requires the multi-paper-scale
   work the audit flags).

PR #976 should be **re-classified** from "categorically-conditional
on the bijection conjecture" to "empirical match awaiting categorical
backing" — the bijection conjecture itself currently lacks the
combinatorial support the audit's structural sketch implied.

## Recommendations

1. **Update PR #976's docstring + caveat** to reflect this finding:
   the empirical 950 MeV prediction stands as a numerical curiosity
   pending categorical justification; it should NOT be advertised as
   "framework's substrate-pure prediction" until the Yekutieli
   machinery gap is closed.

2. **Open follow-up R&D** in three independent directions
   (corresponding to the audit's three possible escape hatches):
   - Define `Π_HS` precisely (operator on Wedderburn blocks) and
     re-verify whether some other natural reading recovers −G·h².
   - Implement the Yekutieli 2015 non-abelian Stokes integration
     directly and check its h² value at 𝓑_3.
   - Audit the sign convention to see if the audit's −G·h² should
     actually be +G·h² (which would make m_p worse, not better —
     ~959 MeV vs CODATA 938.27, i.e. +2.3 % gap).

3. **Do NOT promote Yekutieli-extended λ_scale to production**
   until at least one of the above paths closes. The PROVED
   canonical Family A `5/2 + (3/4)·h²` remains the production
   ground truth.

## Sanity-check on the audit's sign choice

The audit's `λ_Yekutieli = canonical + (−G)·h² = 5/2 + (3/4 − G)·h²`
gives ~951 MeV (1.4 % gap). Flipping the sign:

- `λ_Yekutieli^+ = canonical + (+G)·h² = 5/2 + (3/4 + G)·h² ≈ 2.5163`
- m_avg^+ ≈ 959.7 MeV (vs CODATA 938.92, +2.21 % gap)

So the audit's sign choice does produce a tighter empirical match.
But "produces a tighter match" is exactly the empirical-not-categorical
framing this audit warns against.

## Files

- [`folio-assistant/computations/yekutieli_bijection_construction_h4.py`](../../folio-assistant/computations/yekutieli_bijection_construction_h4.py) — bijection construction attempt
- [`folio-assistant/computations/yekutieli-bijection-construction-h4.witness.json`](../../folio-assistant/computations/yekutieli-bijection-construction-h4.witness.json) — emitted witness
