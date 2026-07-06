**Remark (bar-symmetry class, categorical sectors, and the $c_5$ falsifiable prediction).**

> **Bar-symmetry class** (per [`def:bar-involution`](#def:bar-involution)):
> The function $c_5(q) = -b^2(q) - 1/2 = -3/2 + 1/[2]_q^2$ is bar-symmetric. The Hoefsmit–Quantum-2 identity $b^2 = 1 - 1/[2]_q^2$ is an algebraic theorem in the Lean sibling (`hoefsmit_b_squared_eq_one_minus_inv_quantum_two_squared`). The $-1/2$ piece is a q-independent commutative-QOU constant. The classical limit $c_5(1) = -5/4$ is proved as `c5_classical_limit_eq_neg_five_quarters`. The $c_5$ outlier at the silver ratio is the arithmetic sum of two clean bar-symmetric pieces landing on the inert prime $11 \in \mathbb{Z}[1+\sqrt 2]$. It is not a quantum-deformation artifact.

> **Pentagon-reduction cross-link.** The Leibniz expansion uses the q-dilogarithm pentagon identity. The algebraic identity holds in $\mathbb{Z}[q^{\pm 1}]$ for $|z| \ge q$ via duplication $u = v = i\sqrt{|z|}$, plus the post-$\tau$ $\log_q^2$ correction. This is formalised in [`pentagon_reduction_li2q.py`](../../../computations/pentagon_reduction_li2q.py) with audit documentation in [`-pentagon-reduction-li2q.md`](../../../docs/audits/-pentagon-reduction-li2q.md). The Pentagon coherence layer of $c_5$'s decomposition corresponds precisely to `pentagon_reduction_li2q.py`.

## Categorical interpretation

The $\mathfrak{Q}_\beta$ predictions partition into two distinct categorical sectors.

1. **Pure-$\sigma$ sector** ($c_3, c_4, c_6, c_7$). These contributions arise from positions in the braid that act as pure Hecke generators or their inverses. They live in the $\mathbb{Z}$-span of Hecke-quadratic eigenvalues. At the silver ratio, this span reduces to the Pell-Lucas extension $\mathbb{Z}[1 + \sqrt{2}]$.
2. **Bar-invariant fixed-point sector** ($c_5$). These contributions arise from averaged-crossing positions. They live in the bar-invariant subring, which intersects $\mathbb{Z}[1+\sqrt{2}]$ strictly on integer subspaces. The $1/2$ offset is the residual of this intersection.

These two sectors represent independent categorical inputs. The pure-$\sigma$ sector captures the Hecke-generator action. The bar-invariant fixed-point sector captures the involution-projector action. Both are required to reproduce $\mathfrak{Q}_\beta$ exactly via the precision ladder.

## Falsifiable prediction

Any future rung $c_k$ at $k \geq 8$ whose order $\hbar_q^{2k}$ coincides with an averaging-resonance position will manifest a similar $1/2$ fingerprint. An averaging-resonance position is a $k$-fold cyclic substructure containing at least one averaged crossing.

The proton braid has 11 typed crossings: 7 pure $\sigma_0$, 4 pure $\sigma_1$, 1 averaged $\sigma_0$, 1 averaged $\sigma_1$, and 3 inverted $\sigma_1^{-1}$. The averaging-resonance rungs are determined by the positions where two averaged crossings interact at order $\hbar_q^{2k}$.

Combinatorial counting of averaged-position pairs among the 11 typed crossings predicts the averaging-resonance rungs. These correspond to peaks in the combinatorial weight. The first peak occurs at $k = 5$. Subsequent peaks are predicted at $k = 8, 11, \ldots$, occurring every 3 rungs dictated by the 3-strand sub-braid combinatorics.

This prediction is testable by extending SDP-$T_\beta$ extraction to $k \geq 8$ and checking $c_8$ for the $1/2$ fingerprint. This probe is queued in [`computations/qbeta/qbeta_decay_sdp_extended_ck.py`](../../computations/qbeta/qbeta_decay_sdp_extended_ck.py).

## Discussion

This decomposition is a structural identification, not a first-principles derivation. The $-b^2$ and $-1/2$ summands are identified categorically. A complete proof requires two finite computations:

1. Explicit computation of the typed-$\mathbf{B}_3$ Markov-trace expansion at order $b^5 \hbar_q^{10}$.
2. Order-by-order separation of pure-$\sigma$ and averaged-position contributions.

Neither is yet executed in the framework. This proposition establishes the categorical grammar; the formal proof awaits the order-by-order Hecke expansion machinery.
