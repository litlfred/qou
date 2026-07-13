# GAP-2b: the many-body residual decouples from the nucleon count — it is α-cluster-structural (GAP-4)

**Date:** 2026-07-11
**Branch:** `claude/gap2b-irreducible-demand-2026-07-11`
**Compute:** [`computations/gap2b_irreducible_demand.py`](../../computations/gap2b_irreducible_demand.py)
**Witness:** [`computations/gap2b-irreducible-demand.witness.json`](../../computations/gap2b-irreducible-demand.witness.json)
**Beans:** `qou-ooqh` (GAP-2) → `qou-3lsb` (GAP-4). **Follows:** GAP-1 (#3630), GAP-2 (#3633).

## The question

GAP-2 (#3633) pruned the 3-clique reading and localized `M₃(K)` as the Milnor-**irreducible**
(Borromean `μ̄₁₂₃≠0`) triple count. The natural next step is the **graph→framed-link promotion**
to count the irreducible triples — but choosing a specific link is an arbitrary model input (a
hidden fit) unless the data forces it. So this diagnostic asks first: **what many-body count does
the data demand, and can any nucleon-level deltahedral invariant supply it?**

## Method (diagnostic, not a fit)

Per-order energies pinned on D (`e₂`) and T (`e₃`, M₃=1). For each nucleus, invert the residual
after the GAP-1 max-contact 2-body backbone (à la #3545 Part 6's "#bonds implied"):

`residual(K) = B_strong(K) − e₂·(3A−6)`,  `demanded_M₃(K) = residual(K) / e₃`.

| iso | cluster | A | B_strong | 2-body | residual | dem_M₃ | 3-clique | #faces |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| T   | —       | 3 |  8.482 |  6.674 |  1.808 | 1.00 | 1 | 0 |
| ⁴He | α (core)| 4 | 29.203 | 13.347 | 15.855 | 8.77 | 4 | 4 |
| ⁵Li | α + p   | 5 | 28.857 | 20.021 |  8.836 | 4.89 | 7 | 6 |
| ⁶Li | α + d   | 6 | 34.371 | 26.695 |  7.677 | 4.25 | 8 | 8 |
| ⁷Li | α + t   | 7 | 41.503 | 33.368 |  8.135 | 4.50 | 10 | 10 |

## Result — the residual decouples from the nucleon count

- **Li many-body residual is roughly CONSTANT:** 8.84, 7.68, 8.13 MeV — mean 8.22, **CV 5.8%**.
- **Li nucleon 3-clique count GROWS +43%:** 7 → 8 → 10.
- **`demanded_M₃` ~4.2–4.9 matches NO nucleon invariant** (3-clique 7/8/10, faces 6/8/10).

The residual **decouples** from every nucleon-level deltahedral count: a universal-`e₃` × nucleon
count cannot supply it (it would grow +43%, the residual is flat).

## Reading — the many-body term is at the α-cluster level (GAP-4)

The near-constant residual is the **α-cluster signature**: ⁵Li = α+p, ⁶Li = α+d, ⁷Li = α+t all
share a common **α-core-plus-valence** many-body binding (~8 MeV, roughly independent of the
valence nucleons), **not** a monolithic nucleon deltahedron whose 3-body count grows with A.

⇒ The many-body term lives at the **α-cluster level** — the Brink deltahedra of α-particles
(#3551), not the nucleon-level μ̄-irreducible count. This **prunes the nucleon-link-promotion
route** and redirects GAP-2's remainder into **GAP-4**: the correct object is the α+valence
cluster structure, where the constant many-body residual is naturally built. It also confirms the
corpus reading that ⁶Li = α+d sits below nucleon max-contact (a cluster, not a compact deltahedron).

## What stays open (GAP-4)

The α-cluster contact structure (α + valence) and how the ~8 MeV constant α-core many-body term
arises. The nucleon-level graph→link promotion is the **wrong level**; GAP-4's Brink-deltahedra of
α's is where this belongs. The 2-body backbone (GAP-1) + this cluster-level redirect together
localize the remaining work.

## Discipline

Scope-(a) **diagnostic** — inverting the residual reads off the demanded count (Part-6 style);
`e₂,e₃` pinned on D,T (2 anchors); the conclusion is a **decoupling** (a structural fact), not a
tuned match or a closure. No fit, no production wiring.
