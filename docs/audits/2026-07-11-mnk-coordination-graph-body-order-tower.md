# The nuclear coordination graph M_n(K) is a body-order tower, not a single graph (qou-v0yw)

**Date:** 2026-07-11
**Branch:** `claude/mnk-coordination-graph-selection-2026-07-11`
**Compute:** [`computations/mnk_coordination_graph_selection.py`](../../computations/mnk_coordination_graph_selection.py)
**Witness:** [`computations/mnk-coordination-graph-selection.witness.json`](../../computations/mnk-coordination-graph-selection.witness.json)
**Bean:** `qou-v0yw` (the confirmed single open binding keystone). **Reuses:** #3545's
validated Milnor machinery (`binding_mn_milnor_linking.py`).

## The open keystone

The Milnor `M_n` machinery is built and validated (Hopf `lk=1`, Borromean `μ̄_123=±1`,
chain `μ̄=0`), but *which* link/graph each nucleus is — the coordination topology — is
an un-derived MODEL INPUT. #3545's two routes failed: the ad-hoc chain undercounts
(~1 bond/nucleon vs data ~3, Part 8); the confinement-SDP is degenerate (Part 9). This
session's converged max-binding / max-contact result suggested a selection rule; this
probe tests it.

## Result — the natural selection rule is refuted; it's a tower

`B(K) = m_e·Σ_n a_D^(n)·w_n·M_n(K)`, all terms ≥ 0. The candidate "max-binding selects
the single link with the richest Milnor tower" **fails**:

| A=3 candidate | M₂ (pairwise) | M₃ (triple) | tower rank |
|---|--:|--:|--:|
| chain (Hopf×2, reducible) | 1 | 0 | 1 |
| Borromean (Brunnian, L6a4) | 0 | 1 | 1 |

The chain and the Borromean have **equal tower rank**: the Borromean is Brunnian, so it
*trades* the pairwise term (M₂=0) for the irreducible triple (M₃=1); the chain has the
opposite. Neither carries both orders, so max-binding does not select one graph — and
the choice would be weight-dependent.

## The correct reading — a body-order tower

The coordination is **not one graph** but the body-order **tower** `B = Σ_n B_n`
(ledger §0): M₂ from pairwise links, M₃ from Borromean triples, each order carrying its
own maximally-irreducible **Brunnian-n** sub-link. "chain vs Borromean" is a false
dichotomy — both contribute, at orders 2 and 3.

- **Refuted (scope-(a)):** "max-binding ⇒ single richest-tower graph."
- **Reframed:** qou-v0yw is a **per-order sub-link counting** problem, not a single-graph
  selection — aligning it with the framework's additive body-order series.
- **Explains #3545 Part 8's chain undercount:** a *pure* chain supplies only M₂ and is
  **missing the M₃ (and higher) term**, so it under-binds by exactly the 3-body
  contribution.

## Verdict (scope-limited (a))

> The coordination "graph" question dissolves into the body-order tower: each `M_n(K)`
> is the order-`n` Milnor invariant of its own maximally-irreducible (Brunnian-`n`)
> sub-link, not a single graph. The natural max-binding single-graph selection rule is
> refuted (equal tower rank, M₂↔M₃ trade). **qou-v0yw stays open**, now sharpened to a
> per-order sub-link **counting** problem (how many Borromean triples in ⁶Li, ¹²C, …)
> plus the M_n → w_n weights. A principled reframe, **not** a closure.

**Open (qou-v0yw, next):** the per-order sub-link counts (a combinatorial/topological
count over the isotope's link) and the M_n → w_n weight match. The reframe converts the
"which single graph" question into an order-by-order enumeration against the validated
Milnor tower.
