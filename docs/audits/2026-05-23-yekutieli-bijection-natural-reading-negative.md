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

Computed via [`yekutieli_bijection_construction_h4.py`](../../computations/yekutieli_bijection_construction_h4.py)
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

- [`computations/yekutieli_bijection_construction_h4.py`](../../computations/yekutieli_bijection_construction_h4.py) — bijection construction attempt
- [`computations/yekutieli-bijection-construction-h4.witness.json`](../../computations/yekutieli-bijection-construction-h4.witness.json) — emitted witness

## Addendum: Yekutieli under the upstream q-locality gate

The upstream q-locality discipline (commit `1a29b209b` on main, 2026-05-23,
[`docs/agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md`](../agent-briefs/2026-05-22-lambda-scale-qdilog-tower-direct.md))
retired 4 of 4 near-match λ candidates by measuring the slope of
`(λ_candidate(q) − λ_p_codata(q)) / λ_p_codata(q)` (ppm) across
`q ∈ [q_0 − 0.01, q_0 + 0.01]`. Candidates with slope > 10⁵ ppm/q
are classified as substrate-q_0 coincidences.

Applied to my Yekutieli prediction:

| Candidate                  | λ at q_0    | err at q_0 (ppm) | slope (ppm/q) |
|----------------------------|------------:|-----------------:|--------------:|
| Family A (production)      | 2.532779663 |        +29 604.99|      −1.69×10⁷|
| Yekutieli (PR #976)        | 2.492746271 |        +13 330.94|      −1.69×10⁷|
| closure-target λ_p_codata  | 2.459952788 |               0  |             0 |

**Both Family A AND Yekutieli have identical slopes of ≈ −1.69×10⁷
ppm/q** — and so do the 4 already-retired candidates.

Investigation: the slope is dominated by `d(λ_p_codata)/dq` =
`M_p/m_e · 2ℏ_q · (1/q²) / (8G)` ≈ 40 per unit q (in λ units),
which translates to ~1.6×10⁷ ppm/q via the `1e6 / λ_p_codata`
normalisation. ANY substrate-natural λ_scale with bounded
h-expansion has this slope — because λ_p_codata itself changes
rapidly via the ℏ_q² prefactor.

The only way to get slope = 0 is to set
`λ_candidate(q) = M_p/m_e · ℏ_q²(q) / (8G)` exactly — which is
the trivial-tautology choice (CODATA-implied function-form λ).

**Implication for the q-locality discipline:** the threshold of
10⁵ ppm/q would retire EVERY non-trivial λ candidate including
Family A. Either the discipline only applies to "candidates"
(not to PROVED structural identities) — in which case it doesn't
discriminate Yekutieli from Family A here — or it needs a
different metric (e.g. curvature instead of slope; or slope of
the m_p PREDICTION relative to some other anchor).

**Net effect on Yekutieli's status:** unchanged by the q-locality
gate. The natural-reading partition-combinatorics NEGATIVE finding
(above) remains the primary reason to reclassify the 950 MeV
prediction as "empirical match awaiting categorical backing".

The q-locality discipline as currently formulated is symmetric on
Family A vs Yekutieli — both are equally "non-q-local" in the
upstream slope metric. So either:

1. The discipline's threshold should be raised to >10⁷ ppm/q
   (which would mean ALL structural candidates pass, the test
   doesn't discriminate);
2. The discipline should be reformulated (e.g. slope of *residual
   in m_p prediction* normalised against the prefactor's natural
   slope, isolating the λ-curvature contribution);
3. The discipline should be applied only to "near-match" candidates
   (low err at q_0, like the 4 retired ones with ~5-1000 ppm err)
   — in which case Family A (29605 ppm err) and Yekutieli (13330
   ppm err) are not in the test population at all.

Reading (3) is the most consistent with the upstream commit's tally:
the 4 retired candidates all had small q_0 errors and were elevated
as "near-matches"; Family A and Yekutieli have order-of-magnitude
larger errors and are framework predictions (categorical identity
+ proposed substrate extension), not "near-match curve-fits".

Under reading (3), Yekutieli is **not** subject to the q-locality
retirement — but the natural-reading bijection NEGATIVE remains.

## Addendum 2: Reading A vs Reading B — which one matches CODATA?

The audit `2026-05-22-yekutieli-percell-conjecture-formalized.md`
identifies two readings of "Yekutieli per-cell curvature contributes
to λ_scale":

- **Reading A:** `λ = 5/2 − G·h²` (Yekutieli REPLACES Family A's
  `+(3/4)·h²` term)
- **Reading B:** `λ = 5/2 + (3/4 − G)·h²` (Yekutieli ADDED to
  Family A's structural h²)

The audit explicitly chose Reading B per "2026-05-23 user direction:
add, not replace". PR #976 implements Reading B.

**Empirical comparison against the closure-target:**

Compute what h² coefficient `κ` makes `5/2 + κ·h²` reproduce CODATA
m_p exactly at q_0:

```
λ_required = M_p / (m_e · Vol(𝓑_3) / ℏ_q²(q_0))
           = M_PE · ℏ_q²(q_0) / (8G)
           = 2.45995278…
           = 5/2 + κ · h²(q_0)
           ⇒ κ = (2.45995 − 2.5) / 0.04373…
           ⇒ κ ≈ −0.9166
```

This is `≈ −G` (off by 0.07 %). So **Reading A's `5/2 − G·h²`
matches CODATA almost exactly** at h² truncation; Reading B's
`5/2 + (3/4 − G)·h² = 5/2 − 0.166·h²` leaves the 1.26 % gap
because the +3/4 contribution pulls λ above the required value.

| Reading | total h² coeff | λ at q_0 | m_p pred | m_p err |
|---------|---------------:|---------:|---------:|--------:|
| Family A only (PROVED)  | +0.75       | 2.5328   | 966.05 MeV | +2.89 % |
| Reading B (PR #976)     | +(0.75 − G) | 2.4927   | 950.78 MeV | +1.26 % |
| Reading A (audit-rejected) | −G       | 2.4599   | 938.27 MeV |    0 % |
| Closure-target          | varies      | 2.45995  | 938.27 MeV |   ≡ 0 |

**Reading A gives exact CODATA match at h² truncation.** The user
direction "add, not replace" is therefore in tension with the
numerics. Three possibilities:

1. **Reading A is the correct framing**: a single Yekutieli per-cell
   curvature contribution `−G·h²` IS the categorical truth at h²
   order, replacing (not extending) Family A's `+3/4·h²`. The
   audit's "add, not replace" direction is empirically refuted.

2. **Reading B is correct + another mechanism cancels Family A's
   `+3/4·h²`**: there's a third categorical contribution `−3/4·h²`
   that exactly cancels Family A's structural h² term. The
   framework would then be Family A + this-mystery-term + Yekutieli
   = 0 + (−G·h²) = −G·h². Same numerical result as Reading A but
   structurally different.

3. **The numerical match is coincidental** at h² truncation, and
   the h⁴ and higher corrections (which Family A doesn't have but
   the closure-target does) distinguish Reading A from the closure-
   target at higher precision. This would mean Reading A only
   matches CODATA at h² order, not at h⁴ and beyond.

**Sanity check on possibility (3):** the closure-target's Taylor
coefficients grow rapidly: c_2 ≈ 62.6, c_4 ≈ −5057, c_6 ≈ 2.9×10⁷.
But these are coefficients of `λ_p_codata = M_PE·ℏ_q²/(8G)`, which
has c_2 = M_PE/(32G), NOT the same `c_2 = κ ≈ −0.9166` we'd get
from `5/2 + κ·h²` matching at q_0. The two "c_2" are different
expansions:

- closure-target's c_2 of `λ_p_codata(h) = c_0 + c_2·h² + …`:
  comes from Taylor at h=0 with `c_0 = 0` (since ℏ_q²(0) = 0).
- κ of `5/2 + κ·h²` matching at q_0: comes from imposing a
  CONSTANT `c_0 = 5/2`, which is structurally rigid (Family A
  proves this from S_4 dimension).

So the two "c_2" measure different things. Reading A's κ ≈ −G
is the local-match coefficient AT q_0 given a fixed c_0 = 5/2.
Whether κ ≈ −G holds at all orders (i.e. whether `5/2 − G·h²`
matches the full closure-target curve, not just at q_0) is an
open question — likely **no**, because closure-target has h⁴
corrections that pure `5/2 − G·h²` lacks.

**Implication for PR #976:** the choice of Reading B over Reading A
appears to be a STRUCTURAL choice (canonical Wedderburn theorem
must contribute) at the expense of NUMERICAL fit (Reading A
matches CODATA exactly at h² order). The 1.26 % gap in PR #976
is the price paid for structural orthodoxy.

If one trusts the user direction "add, not replace", PR #976 is
the right form and the residual 1.26 % gap reflects unmodelled
higher-order terms (Yekutieli per-cell + further curvature).
If one trusts the numerics, Reading A (rejected by the audit) is
the better match — but lacks structural justification.

Either way, the open question is **what categorical mechanism
produces κ ≈ −G** at h² order without invoking the
combinatorially-unsupported bijection. The closure-target's
algebraic form `M_PE · ℏ_q² / (8G)` suggests the answer involves
m_p/m_e directly (an empirical anchor), not a substrate-pure
derivation.
