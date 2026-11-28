# α_EM two-loop placement count: `N₁ = 1`, and the θ-graph is `3 + one vertex pair` (2026-11-28)

Bean `qou-l4t2` (parent `qou-3l2l`). Mathematics only: no measured value enters any
statement below. Lean:
[`QOU/MassTheory/EmThetaGraphSkeinSplit.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/EmThetaGraphSkeinSplit.lean)
(lean-direct exit 0 with `-DautoImplicit=false`; axioms `propext`, `Quot.sound`,
`Classical.choice` only; no `sorry`). Builds on
[`EmVertexPairScalarChain.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/EmVertexPairScalarChain.lean)
and [the 2026-11-27 note](2026-11-27-alpha-em-two-loop-skein-scalar.md).

## Question

The 2026-11-27 note left `N₁`, the number of two-loop vertex-pair placements, as a
choice. The corpus already has a second two-loop reading: the θ-graph
([2026-07-14](2026-07-14-alpha-em-theta-graph-two-loop-candidate.md)), the unique 1PI
two-loop vacuum graph, with value `θ(1,1,2) = [3]_q` and term `−α²[3]_q/(8π)²`.
Form B has `−α² H h²` with `H = [2]_q/(8π)`. How do they relate?

## Result

With `h = q − q⁻¹`:

1. `[3]_q = 3 + h²` (`qInt3_eq_three_add_hsq`, any commutative ring with `q q⁻¹ = 1`).
2. `[3]_q = 3 − V`, where `V` is the chirality-summed vertex pair at any two
   convention-D generators (`qInt3_eq_three_sub_vertexPair`). So the θ-graph is a
   classical constant plus **exactly one** vertex pair.
3. `−[3]_q x² = −3x² + (−h²)x²` (`theta_two_loop_split`).
4. No integer `N` gives `N h² = [3]_q` (`qInt3_not_skein_multiple`). Every skein-chain
   coefficient vanishes at `q = 1`, while `[3]_1 = 3`.

**Consequence.** Both readings put one vertex pair at two loops, so `N₁ = 1` is what
the θ-graph gives, and Form B's `N₁ = 1` is consistent with it. The "same-position
plus cross-position, `N₁ = 2`" option has no support in the corpus's graph reading:
there is one 1PI two-loop topology (cited from the 2026-07-14 audit; that uniqueness
is not proved in Lean here).

The two readings still differ, in two places, neither of which is the placement count:

- **Classical part.** The θ-graph has a `3` that no skein chain can produce
  (result 4). Form B has none, so Form B's two-loop term vanishes as `q → 1`.
- **Measure.** The θ-graph carries `x² = (α/(8π))²`; Form B carries
  `H α² = [2]_q α²/(8π)`, one factor of `[2]_q·8π` apart on the shared `h²` piece.

So the open two-loop question is the measure and the classical constant, not `N₁`.
The measure question is being worked in a separate thread.

## Comparison (prose only; not in any proof)

The 2026-07-14 audit records the θ-graph ladder at −0.200 ppb (1.3σ) and Form B at
+0.313 ppb (2.1σ) at the proton pin. Both are far inside the ~80 ppb pin-tension
floor (`qou-2002`), and `qou-aemx` forbids choosing by residual, so these numbers
decide nothing.
