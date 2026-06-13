**Theorem (conditional on
[`conj:crystal-graph-realization`](#conj:crystal-graph-realization)
and the Brundan–Kleshchev isomorphism
\cite{brundankleshchev2009}).**
*Let $\mathsf{C}$ denote the upstream conjectural class
$[\mathrm{CrystalGraphRealization}]$ — an instance of which
provides the Kashiwara crystal $\mathrm{Cryst}(H_n(R, q))$ together
with the Brundan–Kleshchev isomorphism $H_n(R, q) \cong R_\alpha^{\Lambda}$
intertwining centres
\cite{khovanovlauda2009, brundankleshchev2009}. Then,
[**conditional on $\mathsf{C}$**], the
[confinement filtration](#def:confinement-level) $J^\bullet(q)$ on
$H_n(R, q)$ coincides with the filtration induced by the natural
$\mathbb{Z}$-grading on the KLR algebra: a closed braid $K$ with
normal form $T_w$ has confinement level $\ell(K, q)$ if and only
if its KLR-module lift $\mathfrak{M}_K$ has top non-zero graded
piece in degree $\ell(K, q)$,*

$$
  T_w \in J^\ell(q) \setminus J^{\ell+1}(q)
  \;\iff\;
  (\mathfrak{M}_K)_d = 0 \;\;\text{for}\;\; d > \ell.
$$
## Why the upstream class is a single conjecture

The Brundan–Kleshchev cyclotomic-Hecke / KLR isomorphism is proved
in \cite{brundankleshchev2009} for the abstract algebras over a
field; what remains conjectural in this manuscript is the
identification of the QOU LP/SDP **shadow-price ordering** on
knot-operator energies (`def:knot-operator-energy`) with the KLR
$\mathbb{Z}$-grading on the *cyclotomic quotient* relevant to
confinement.  This identification is precisely the content of
[`conj:crystal-graph-realization`](#conj:crystal-graph-realization);
the class-axiomatisation packages the corresponding compatibility
data into a single field.

## Empirical witness

For every atomic knot $K$ at $k_{\max} \leq 7$, the LP/SDP active
set $\{\lambda \mid y_\lambda^* > 0\}$ produced by
[`confinement-operator-selection.py`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/confinement_operator_selection.py)
matches the KLR-graded support predicted by the conditional
theorem.

| $k_{\max}$ | atomic knots tested | LP active set = KLR support? |
|---|---|---|
| 3 | $3_1$ | yes |
| 4 | $3_1, 4_1$ | yes |
| 5 | $3_1, 4_1, 5_1, 5_2$ | yes |
| 6 | $3_1, 4_1, 5_{1,2}, 6_{1,2,3}$ | yes |
| 7 | $3_1, 4_1, 5_{1,2}, 6_{1,2,3}, 7_{1,\ldots,7}$ | yes |

Witnesses:
[`lp-confinement-nf-forcing.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/lp-confinement-nf-forcing.witness.json),
[`confined-knot-binding.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/confined-knot-binding.witness.json),
[`confinement-operator-selection.witness.json`](https://github.com/litlfred/qou/blob/main/folio-assistant/computations/confinement-operator-selection.witness.json).

These are *empirical evidence* for the upstream conjecture
[`conj:crystal-graph-realization`](#conj:crystal-graph-realization),
not a proof of this conditional theorem.  Once the upstream
conjecture is settled (e.g. by an explicit construction of the
KLR-grading on the QOU cyclotomic quotient), the conditional
hypothesis will be discharged and this block becomes an
unconditional theorem.

## Computational consequence

The conditional theorem licenses the existing engine optimisation:
the KLR grading bound is enforced before any crystal step. Given a
target confinement level $\ell$, the engine restricts crystal
traversal of
[`conj:crystal-graph-realization`](#conj:crystal-graph-realization)
to the subgraph spanned by KLR-modules of degree $\leq \ell$. Any
application of $\tilde f_i$ that would push a state into degree
$\ell + 1$ is geometrically forbidden — the heuristic confinement
cutoff in the engine is justified up to the upstream conjecture.

This is symmetric-crystal shortcut #1 + #3 (CLAUDE.md §7b)
reducing engine-side combinatorics to a Bruhat-prefix Demazure
filtration.  The Demazure-fiber Markov-trace functional
$T^{\mathrm{Dem}}(\lambda;\, w)$ from
[`prop:demazure-fiber-markov-trace`](#prop:demazure-fiber-markov-trace)
provides the explicit quantitative form of the resonance widths
that arise inside each KLR-graded layer.
