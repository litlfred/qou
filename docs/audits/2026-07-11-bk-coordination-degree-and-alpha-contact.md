# Binding multiplicity = coordination number of 𝓑_K — nucleon `z=A−1` and α-cluster contact graph

**Date:** 2026-07-11
**Branch:** `claude/bk-coordination-degree-derivation-2026-07-11`
**Compute:** [`computations/bk_coordination_contact_binding.py`](../../computations/bk_coordination_contact_binding.py)
**Witness:** [`computations/bk-coordination-contact-binding.witness.json`](../../computations/bk-coordination-contact-binding.witness.json)
**Follow-up to:** merged `rem:bk-coordination-multiplicity` (PR #3549), audit
[`2026-07-11-bk-crossing-coordination-multiplicity.md`](2026-07-11-bk-crossing-coordination-multiplicity.md).

## Task

Two follow-ups to the merged coordination-number reading: (1) *derive* the
`z=A−1` multiplicity structurally, and (2) fold in the α-cluster contact-graph
result forward. This audit records the honest derivation status of each.

## Part 1 — nucleon coordination `z = A−1` (A ≤ 4)

The merged result: the single-link weight `B = M(A)·m_e·Vol_n(K)` has multiplicity
`M(A=3) ≈ 2 = A−1` for the non-magic A=3 pair (fit-free, <3%).

**What is derivable (exact).** `z(A) = A−1` is the **vertex degree of the complete
graph `K_A`** — the fully-coordinated A-body cluster in which every nucleon is
bonded to every other. Equivalently the total bond count is `|E(K_A)| = C(A,2) =
A(A−1)/2`, and the average/uniform degree is `2·C(A,2)/A = A−1`. This is an exact
graph-theoretic fact, provable in Lean (Mathlib `SimpleGraph`, `⊤`/`completeGraph`).
The complete graph is **3D-realizable iff A ≤ 4** (a tetrahedron is the largest
all-mutually-adjacent point set in ℝ³), which is exactly the regime where the
single-link volume picture applies.

**What is NOT derived (conditional / empirical).** The identification
"single-link volume multiplier = coordination number `z`" is the **bond-extensive
hypothesis**: that binding is carried per-bond and each nucleon's `m_e·Vol_n(K)`
action is weighted by its coordination degree. Per the *formalize-first* discipline
and the *"axiomatization is not a proof"* rule, this is a **conditional structural
claim**, not a derivation from the 13 categorical drivers. It would be formalized as
a conditional class (`BondExtensiveBinding`) whose instance is the open input; the
graph-degree lemma is the proved part, the extensivity is the hypothesis. The
numerical match (`M_need ≈ 2 = z` for A=3) is the empirical support, not a
derivation.

> **Status: `z=A−1` is the coordination number (proved graph fact); "multiplier = z"
> is a conditional bond-extensive hypothesis, not derived.** Scope-limited (a).

## Part 2 — α-cluster contact coordination (A > 4), forward

For A>4 the coordination principle lifts to α-clusters. **Forward test:** fix the
per-bond energy `b_αα` from the two simplex clusters ¹²C/¹⁶O, then *predict* the
heavier α-conjugate nuclei from their standard Brink/Hafstad–Teller cluster
**contact geometries** — `B(n_α) = n_α·B(⁴He) + N_contacts·b_αα`:

| nucleus | n_α | N_contacts | geometry | B_pred | B_AME | err |
|---|--:|--:|---|--:|--:|--:|
| ⁸Be | 2 | 1 | dumbbell | 59.01 | 56.50 | +4.44% (unbound pair) |
| ¹²C | 3 | 3 | triangle (K₃) | 92.13 | 92.16 | −0.03% (calib) |
| ¹⁶O | 4 | 6 | tetrahedron (K₄) | 127.68 | 127.62 | +0.04% (calib) |
| ²⁰Ne | 5 | 8 | square pyramid | 160.80 | 160.64 | **+0.10%** |
| ²⁴Mg | 6 | 12 | octahedron | 198.76 | 198.26 | **+0.25%** |
| ⁴⁰Ca | 10 | 24 | fcc close-packed | 340.93 | 342.05 | **−0.33%** |

- **A single `b_αα ≈ 2.416 MeV` reproduces A=12–40 binding to <0.5%** (worst 0.33%
  on the forward set ²⁰Ne/²⁴Mg/⁴⁰Ca) from standard cluster geometries. ¹⁶O =
  tetrahedron (6 edges) and ²⁴Mg = octahedron (12 edges) are exact platonic edge
  counts.
- The **contact-graph edge count** replaces `C(n_α,2)` for n_α ≥ 5, because ≥5
  spheres cannot all mutually touch in 3D. The contact number grows ~linearly (each
  α has a bounded neighbour count — the kissing number ≤ 12), not quadratically.
- **⁸Be (n_α=2) is the unbound-pair exception:** the isolated α–α bond carries ≈0
  (⁸Be sits just above 2·⁴He), so the bond energy switches on only inside a 3+
  cluster — the triple-α gateway. Excluded from the forward-accuracy claim.

**Provenance / honesty.** This is the classical Brink α-cluster model; the QOU
content is the reading of `N_contacts` as the **α-level coordination number of the
building-block link 𝓑_K**, unifying with the Part-1 nucleon coordination `z=A−1`.
`b_αα` is a **single empirical residual constant, NOT derived** from the 13 drivers,
and the α-geometry per nucleus is the standard cluster assignment (a modelling
choice, not derived). Its derivation is coordinated with **#3548** (connected
two-α braid `tr_M`, PROBE 2), not attempted here.

## Verdict (critical-distance, scope-limited (a))

> The binding multiplicity is the **coordination number of 𝓑_K** at the relevant
> level — nucleon `z=A−1` for A≤4, α-cluster contact number for A>4. The
> coordination *numbers* are exact combinatorial/geometric facts; the *identification*
> with the binding multiplier is bond-extensive (conditional) and the per-bond
> energy `b_αα` is empirical. Not a closure — a structural organization of the open
> multiplicity with one fit-free integer per level.

**Open:** (1) derive "multiplier = coordination number" (bond-extensivity) from the
categorical/connected-cluster structure; (2) derive `b_αα` (→ #3548); (3) derive the
α-cluster geometry selection (why square-pyramid for ²⁰Ne, octahedron for ²⁴Mg)
rather than assigning it.
