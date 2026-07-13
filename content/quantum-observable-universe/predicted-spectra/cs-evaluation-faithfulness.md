Let $\Phi_n(K)$ denote the tower-level volume contribution from the [tower decomposition](#prop:volume-tower-decomposition). Let $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ denote the $n$-th [quantum characteristic class](#def:quantum-characteristic-classes).

**Proposition.**
The Chern--Simons evaluation map is *faithful* at each tower level. For every hyperbolic knot or link $K$ in the Descartes spectrum,

$$
  \kappa_n \neq 0 \quad \Longrightarrow \quad \Phi_n(K) \neq 0.
$$

If $\kappa_n$ defines a non-trivial obstruction in $H^2(\mathcal{S}, \mathcal{B})$, the Chern--Simons period integral over the $n$-th twisted sector yields a non-zero real contribution to $\mathrm{Vol}(K)$.

**Corollaries.**

1. **No accidental cancellation.** The Peiffer identity in the crossed groupoid conjugates $a^{(n)}$ by $g^{(n)}$ but preserves the period. The $\mathrm{SU}_{q_n}(2)$-adjoint action functions as an automorphism of the band $\mathcal{B} = \mathcal{O}_M^{\times}$, not as a projection to zero.
2. **Infinite non-trivial contributions.** The [Yekutieli lifting](#prop:yekutieli-lifting) theorem guarantees $\kappa_n \neq 0$ for all $n$. Faithfulness therefore implies the volume receives new data at every tower level.
3. **Path to algebraic independence.** If each $\Phi_n(K)$ carries arithmetically independent data, the series $\mathrm{Vol}(4_1) = \sum_n \Phi_n(4_1)$, $\mathrm{Vol}(5_2) = \sum_n \Phi_n(5_2)$, and $\mathrm{Vol}(\mathcal{B}_3) = \sum_n \Phi_n(\mathcal{B}_3)$ satisfy no polynomial relation. A finite polynomial cannot absorb infinitely many independent contributions.

**Relation to Mostow rigidity.**
Mostow rigidity guarantees the total volume $\mathrm{Vol}(K)$ defines a topological invariant. This proposition refines the invariant into a graded series $\{\Phi_n(K)\}_{n \geq 0}$, controlled by cohomological obstructions. Rigidity ensures convergence. Faithfulness ensures non-degeneracy at each grade.
