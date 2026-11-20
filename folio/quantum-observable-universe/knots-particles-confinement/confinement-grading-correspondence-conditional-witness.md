## Conditional dependence on the upstream grading identification

The Brundan–Kleshchev isomorphism is proved in \cite{brundankleshchev2009} for abstract algebras over a field. What remains conjectural is the identification of the QOU shadow-price ordering on knot-operator energies with the KLR $\mathbb{Z}$-grading on the cyclotomic quotient. This identification is precisely the content of the upstream conjecture.

## Empirical witness

For every atomic knot $K$ at $k_{\max} \leq 7$, the LP/SDP active set $\{\lambda \mid y_\lambda^* > 0\}$ matches the KLR-graded support predicted by the conditional theorem.

| $k_{\max}$ | atomic knots tested | LP active set = KLR support? |
|---|---|---|
| 3 | $3_1$ | yes |
| 4 | $3_1, 4_1$ | yes |
| 5 | $3_1, 4_1, 5_1, 5_2$ | yes |
| 6 | $3_1, 4_1, 5_{1,2}, 6_{1,2,3}$ | yes |
| 7 | $3_1, 4_1, 5_{1,2}, 6_{1,2,3}, 7_{1,\ldots,7}$ | yes |

Witnesses:
`lp-confinement-nf-forcing.witness.json`,
`confined-knot-binding.witness.json`,
`confinement-operator-selection.witness.json`.

These computations provide empirical evidence for the upstream conjecture. Once the upstream conjecture is settled, this witness becomes an unconditional theorem.

## Computational corollary

The conditional theorem licenses the engine optimisation. We enforce the KLR grading bound before any crystal step. Given a target confinement level $\ell$, the engine restricts crystal traversal to the subgraph spanned by KLR-modules of degree $\leq \ell$. Any application of $\tilde f_i$ that pushes a state into degree $\ell + 1$ is geometrically forbidden. This justifies the heuristic confinement cutoff in the engine.

This reduces engine-side combinatorics to a Bruhat-prefix Demazure filtration. The Demazure-fiber Markov-trace functional $T^{\mathrm{Dem}}(\lambda;\, w)$ provides the explicit quantitative form of the resonance widths inside each KLR-graded layer.
