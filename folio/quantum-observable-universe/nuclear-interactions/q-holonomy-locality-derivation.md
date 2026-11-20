## Locality from flatness of the KZ connection

The lifted-crossing locality hypothesis reduces to a statement about the holonomy of the Knizhnik-Zamolodchikov (KZ) connection at generic $q$. Cross-talk between two lifted crossings measures the curvature of a flat connection. Flatness implies factorization.

## Setup — the KZ connection

Let $X_n$ be the configuration space of $n$ distinct complex points. The quantum KZ connection on $X_n$ is flat. The monodromy representation coincides with the quantum-group R-matrix representation.

## Applying to the mass endomorphism

Model each crossing of an atomic braid as a puncture in $X_n$. A lifted crossing inserts $\Phi_q(z_c)$; an unlifted crossing inserts the identity. The mass contribution is the trace of the braid-word operator, computed via parallel transport.

**Claim.**
*At generic $q$, the parallel transport factorizes over disjoint punctures:*

$$
  \mathrm{Tr}\!\left[
    \prod_{c \in S} \Phi_q(z_c) \cdot \rho(\beta)
  \right]
  \;=\;
  \mathrm{Tr}[\rho(\beta)] \cdot \prod_{c \in S}
  \eta(c),
$$

*where $\eta(c)$ is the single-crossing expectation value.*

**Proof sketch.**
By flatness, closed loops encircling separated subsets have commuting holonomies. Simultaneous diagonalization decomposes the trace. The $\Phi_q$ insertions act by scalar on each eigenstrand. Thus, the multi-crossing expectation is a product of single-crossing expectations. The scalar obstruction requires non-abelian monodromy, which flatness rules out. $\square$

## Failure of flatness

Flatness is equivalent to semisimplicity of the braided tensor category. At generic $q$, representations are semisimple and locality holds. At roots of unity, non-semisimple subquotients appear and locality fails.

## The substrate as the locality window

The KZ connection is flat at every level (the infinitesimal braid relations are homogeneous), so flatness does not single out the pinned parameter $q_0 \approx 1.11$; what does is that $q_0$ is not a root of unity, so the monodromy target $H_n(q_0)$ is semisimple and the locality statement is about the generic Hecke representation. The soft confinement level is far from the first non-trivial root of unity, so locality holds to high order.

## Corollary — exponential mass scaling

Combining locality with the crossing-graded expansion gives, at the homogeneous fixed point, $\mathfrak{m}(\mathcal{K}; q_0) = \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot (1 + \xi(q_0))^{c(\mathcal{K})}$. Each crossing multiplies mass by $\approx 94$. Exponential scaling is the empirical signature of KZ flatness at the substrate.
