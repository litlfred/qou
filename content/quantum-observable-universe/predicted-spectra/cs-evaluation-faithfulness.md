Let $\Phi_n(K)$ be the tower-level volume contribution from
[tower decomposition](#prop:volume-tower-decomposition) and let
$\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ be the $n$-th
[quantum characteristic class](#def:quantum-characteristic-classes).

**Proposition.**
The Chern--Simons evaluation map is *faithful* at each tower level:
for every hyperbolic knot or link $K$ in the Descartes spectrum,

$$
  \kappa_n \neq 0 \quad \Longrightarrow \quad \Phi_n(K) \neq 0.
$$

More precisely, if $\kappa_n$ is a non-trivial obstruction in
$H^2(\mathcal{S}, \mathcal{B})$, then the Chern--Simons period integral
over the $n$-th twisted sector produces a non-zero real contribution to
$\mathrm{Vol}(K)$.

**Corollaries.**

1. **No accidental cancellation.** The Peiffer identity in the crossed
   groupoid conjugates $a^{(n)}$ by $g^{(n)}$ but does not annihilate
   the period: the $\mathrm{SU}_{q_n}(2)$-adjoint action is an
   automorphism of the band $\mathcal{B} = \mathcal{O}_M^{\times}$,
   not a projection to zero.

2. **Infinite non-trivial contributions.** Combined with the
   [Yekutieli lifting](#prop:yekutieli-lifting) theorem, which
   guarantees $\kappa_n \neq 0$ for all $n$, faithfulness implies
   that the volume receives genuinely new data at every tower level.

3. **Path to algebraic independence.** If each $\Phi_n(K)$ carries
   arithmetically independent data (distinct from all lower levels),
   then the three sums $\mathrm{Vol}(4_1) = \sum_n \Phi_n(4_1)$,
   $\mathrm{Vol}(5_2) = \sum_n \Phi_n(5_2)$,
   $\mathrm{Vol}(\mathcal{B}_3) = \sum_n \Phi_n(\mathcal{B}_3)$
   cannot satisfy a polynomial relation --- because no finite
   polynomial can absorb infinitely many independent contributions.

**Relation to Mostow rigidity.**
Mostow rigidity guarantees that the *total* volume $\mathrm{Vol}(K)$ is
a topological invariant.  This conjecture refines the invariant into a
graded series $\{\Phi_n(K)\}_{n \geq 0}$, with each grade controlled by
a cohomological obstruction.  The rigidity theorem ensures convergence;
the faithfulness conjecture ensures each grade is non-degenerate.
