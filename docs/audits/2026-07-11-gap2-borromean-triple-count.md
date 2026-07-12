# GAP-2: the 3-clique count overshoots — the 3-body term is the Milnor-irreducible subset (qou-ooqh)

**Date:** 2026-07-11
**Branch:** `claude/gap2-borromean-triple-count-2026-07-11`
**Compute:** [`computations/gap2_borromean_triple_count.py`](../../computations/gap2_borromean_triple_count.py)
**Witness:** [`computations/gap2-borromean-triple-count.witness.json`](../../computations/gap2-borromean-triple-count.witness.json)
**Bean:** `qou-ooqh` (GAP-2, blocked-by GAP-1 `qou-lzoh` — now unblocked by #3630).
**Follows:** GAP-1 (#3630, the max-contact 2-body edge set), #3545 Part 7 (Milnor `μ̄`-tower).

## What GAP-2 asked

GAP-1 (#3630) fixed the 2-body edge set at A≥5 (max-contact deltahedra, `3A−6` contacts),
leaving a bounded ~1.2–1.8 MeV/nucleon residual = the many-body term. GAP-2 tests the **first
many-body order** (3-body): is the residual accounted for by a 3-body term, and is the right
count the bonded-triple (3-clique) count or the Milnor-**irreducible** (Borromean `μ̄₁₂₃≠0`) subset?

## Model — per-ORDER pinning (not per-isotope)

`B(K) = e₂·M₂(K) + e₃·M₃(K) + e₄·M₄(K)`, `eₙ = m_e·a_D^(n)·wₙ` the per-order energy. Pin each
`eₙ` on the **lightest** nucleus that first exhibits order `n` — D, T, ⁴He (3 anchors for 3
per-order energies, #3588's `w₂`-pin extended) — then **predict A≥5 from geometry** (the clique
counts of the deltahedral contact graph). `Mₙ` candidate = the `k`-clique count (mutually-bonded
`k`-subset). Graphs built explicitly (tri-bipyramid A=5, octahedron A=6, pentagonal bipyramid A=7).

| iso | A | M₂=#edges | M₃=#triangles | M₄=#tetrahedra |
|---|--:|--:|--:|--:|
| D   | 2 | 1  | 0 | 0 |
| T   | 3 | 3  | 1 | 0 |
| ⁴He | 4 | 6  | 4 | 1 |
| ⁵Li | 5 | 9  | 7 | 2 |
| ⁶Li | 6 | 12 | 8 | 0 |
| ⁷Li | 7 | 15 | 10 | 0 |

Pinned: `e₂ = 2.2246` (deuteron bond), `e₃ = 1.8081` (triton 3-body), `e₄ = 8.6230` MeV
(⁴He 4-body, doubly-magic).

## Result — the 3-clique count OVERSHOOTS (refutation)

| iso | B_strong | 2+3-body | ratio | +4-body | ratio |
|---|--:|--:|--:|--:|--:|
| ⁵Li | 28.857 | 32.678 | **1.132** | 49.924 | 1.730 |
| ⁶Li | 34.371 | 41.160 | **1.197** | 41.160 | 1.197 |
| ⁷Li | 41.503 | 51.449 | **1.240** | 51.449 | 1.240 |

- The **bonded-triple (3-clique) count overshoots** the A≥5 binding by a **growing** +13→24%.
- Adding the 4-clique×`e₄`(⁴He) reading is **worse** where a tetrahedron exists (⁵Li 1.73) —
  ⁴He's 4-body magic is a **non-transferable shell closure** (its `e₄` over-predicts ⁵Li's two
  tetrahedra); octahedron/pentagonal-bipyramid have no K₄, so 4-body is absent there.

## Reading — the 3-body term is the Milnor-irreducible (Borromean) subset

The overshoot **refutes** "every mutually-bonded triple is a 3-body term" and **confirms the
corpus Part-7 reading**: only the Milnor-**irreducible** (Borromean, `μ̄₁₂₃≠0`) triples count.
A mutually-bonded triple (3-clique) is **reducible to pairwise** (`μ̄=0`, corpus Part 7: a chain
of Hopf bonds), so the 2-body edges *already carry* it — counting all 3-cliques **double-counts**.
The overshoot magnitude **measures** the reducible-triple excess.

This is a scope-(a) **prune**: it removes the 3-clique reading and localizes `M₃(K)` as the
`μ̄₁₂₃`-irreducible triple count.

## What stays open (GAP-2, sharpened)

`M₃(K) = ` the `μ̄₁₂₃`-irreducible triple count — computing it needs the **contact-graph → framed-
link promotion** (assign crossings/framing so the deltahedral graph becomes a link) plus the
validated `μ̄`-tower (`binding_mn_milnor_linking.py`). This probe prunes the clique reading; the
irreducible count is the next step. The ⁴He 4-body magic (non-transferable) is a separate
shell-structure input (GAP-4 territory).

## Discipline

Scope-(a) **refutation** (an honest reported overshoot, not a tuned match). `eₙ` pinned per-order
on D/T/⁴He (the minimal nuclei of each order — not per-isotope fitting), clique counts from
geometry, A≥5 forward-predicted. No fit, no production wiring — the anti-fit checkpoint of bean
`qou-ooqh`. Per the "refuted ≠ ruled out" discipline: this is scope-(a) — the 3-*clique* reading
is excluded; the 3-*body* term itself is not, only re-identified as the irreducible subset.
