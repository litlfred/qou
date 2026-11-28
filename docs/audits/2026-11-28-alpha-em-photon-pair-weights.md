# α_EM two-loop: what the photon form says about vertex-pair weights (2026-11-28)

Bean `qou-l4t2`. Mathematics only. Lean:
[`QOU/MassTheory/EmPhotonPairWeights.lean`](../../folio/quantum-observable-universe/lean/QOU/MassTheory/EmPhotonPairWeights.lean)
(lean-direct exit 0 with `-DautoImplicit=false`; axioms at most `propext`,
`Quot.sound`, `Classical.choice`; no `sorry`). Follows
[the classical-3 note](2026-11-28-alpha-em-theta-classical-three.md).

## Question

Form B and the θ-graph weight the four chiral two-vertex histories differently. Does
the ruled photon form `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` decide which weights are right?

## Result

At one convention-D generator, split the histories into mixed chirality
`M = σσ⁻¹ + σ⁻¹σ` and same chirality `S = σ² + σ⁻²`:

- `M = 2` and `S = 2 + h²` (`mixedPair_eq`, `samePair_eq`).
- Weights `a` on mixed and `b` on same give `(2a + 2b) + b h²` (`weightedPair_eq`).
- The classical part vanishes iff `a = −b` (`weightedPair_classical_zero_iff`, in a
  domain of characteristic zero). Form B's signed sum is `M − S = −h²`
  (`signed_eq_mixed_sub_same`).

| weighting | `(a, b)` | value |
|---|---|---|
| Form B (signed) | `(1, −1)` | `−h²` |
| θ-graph (unsigned, less singlet) | `(1, 1)`, then `−1` | `3 + h²` |
| photon form's own two-crossing term | `(1, 0)` | `2` |

The ruled photon form has the mixed-chirality term `σ₀σ₁⁻¹` and excludes the
same-chirality `σ₀σ₁`. So on its own degree-two term it carries weights `(1, 0)`,
which give a constant `2` and no `h²` (`photonTerm_weights_classical`). That matches
neither reading.

## Consequence (scope (a))

The photon form alone does not decide between Form B and the θ-graph. It fixes the
weights on its own two-crossing term, but a two-loop vertex pair is two **separate**
photon vertices on one fermion loop. The weights those carry need a propagator rule,
which the corpus does not yet state. Both readings stay as labelled fallbacks.

What would decide it: a stated rule for joining two copies of `γ` across a fermion
loop (for example the bar-Hermitian pairing `γ̄ · γ` restricted to the loop). That is
a definition, so it needs Carl's call before anything is built on it.
