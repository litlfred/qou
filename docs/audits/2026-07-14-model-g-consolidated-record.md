# Model G — consolidated audit record (promotion to content blocks deferred)

**Date:** 2026-07-14 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Status:** owner-directed audit-level record (2026-07-14): "recorded for audit
for now"; promotion to content blocks is **deferred**, not an open-question
block — tracked as bean `qou-hfiw` (promotion task) to be resolved later.
**Scope:** consolidates the rounds-4–7 results (#3780, #3784, #3786, #3789)
into one citable record with the epistemic tier of every ingredient.

## The model

For a light alpha-conjugate (or alpha + light-remainder) isotope with cluster
decomposition into `k` alpha clusters plus light remainders (⁶Li = α+d,
⁷Li = α+t, ⁸Be = 2α, ⁹Be = 2α+n, ¹²C = 3α, ¹⁶O = 4α):

```
B(isotope) ≈ Σ_clusters B(cluster)              [AME cluster bindings — INPUT]
           + b · A_light,   b = 0.78 MeV        [light-spectator channel]
           + g · C(k,2)·[k ≥ 3],  g = 2.4155 MeV [gated α·α pair term]
```

Residuals (% of B_AME): ⁶Li +0.28, ⁷Li −0.31, ⁸Be +0.16, ⁹Be −0.02,
¹²C −0.26, ¹⁶O −0.28. ¹²C and ¹⁶O are out-of-sample (constants fixed before
evaluation). Witness:
[`alpha-activation-brunnian.witness.json`](../../computations/deltalambda/alpha-activation-brunnian.witness.json)
(9/9), building on
[`alpha-cluster-volume-additivity.witness.json`](../../computations/deltalambda/alpha-cluster-volume-additivity.witness.json)
(7/7) and [`inter-cluster-bond-term.witness.json`](../../computations/deltalambda/inter-cluster-bond-term.witness.json)
(10/10).

**Honesty banner.** The cluster bindings enter at measured AME values: Model G
derives the *composite* structure, not the absolute base. The framework's
ab-initio piece for the clusters is the separate bond-count tower
(³H −0.16%; ⁴He open — the Vol₄ census gap,
[`2026-07-13-he4-vol4-prediction-test.md`](2026-07-13-he4-vol4-prediction-test.md)).

## Epistemic tiers (per the registry conventions)

| ingredient | tier | source |
|---|---|---|
| bond-count multiplicity `M_n = (n−1)` | **proved-lean** | `QOU/Mass/LinearChainBondCount.lean` |
| μ̄ sign-rep obstruction (coupling through \|μ̄\| only) | **proved-lean** | `QOU/Mass/MilnorSignRepObstruction.lean` |
| Milnor-indeterminacy gate (Hopf spectator ⇒ `Subsingleton (ZMod Δ)`; α-only activation) | **proved-lean** (+ cited literature input `[milnor1954]`) | `QOU/Mass/MilnorIndeterminacyGate.lean` |
| W-plane annihilation on Vol=0 bond channels; CAL-3 class selection | **proved-lean** / **conditional** (on the `B = m_e·Vol` ledger class) | `QOU/Mass/BondChannelClassSelection.lean` |
| ⁸Be ≈ 0, k≥3 activation, α-only gate (predicted the ⁹Be adjudication) | **conditional** on the Brunnian arrangement model input | [`2026-07-13-alpha-activation-brunnian-derive-or-refute.md`](2026-07-13-alpha-activation-brunnian-derive-or-refute.md) |
| `b = 0.78 MeV/nucleon` | **empirical** (calibrated on the 3 one-bond composites) | [`2026-07-13-inter-cluster-bond-term-derive-or-refute.md`](2026-07-13-inter-cluster-bond-term-derive-or-refute.md) |
| Boolean `C(k,2)` saturation counting | **data-selected** (idempotent \|μ̄\| reading consistent, not derived) | same |
| `g = 2.4155 ≈ 3·b` (−2.9%) | **guarded near-match** (channel count 3 post-hoc) | same |
| ¹¹B / ¹⁴N / ¹⁹F mixed multi-bond | **open** (−58/−33/−10% deficit-level) | round-8 target |

## Deferred item

Promotion of this record to content blocks (proposition for the Lean-proved
gate structure; conjecture for the Brunnian arrangement + counting; remarks
for ⁸Be/⁹Be) is deferred by owner direction — not an open-question block.
Tracked as a bean; to be resolved later.
