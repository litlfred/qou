*Holds over a generic commutative ring, with no archimedean input.*

**Proposition (channel algebra of the two-vortex interaction).** *Let $R$ be a commutative ring carrying elements $e_+, e_-, \sigma, q, u$ satisfying*

$$
  \underbrace{e_+ + e_- = 1}_{\text{partition of unity}}, \qquad
  \underbrace{e_+ e_- = 0}_{\text{orthogonality}}, \qquad
  \underbrace{q\,u = 1}_{\text{inverse witness}}, \qquad
  \underbrace{\sigma = q\,e_+ - u\,e_-}_{\text{spectral form}}.
$$

*These axioms imply*

$$
  \underbrace{e_+^2 = e_+,\ \ e_-^2 = e_-}_{\text{derived idempotency}}; \qquad
  \underbrace{\sigma^2 = q^2\,e_+ + u^2\,e_-}_{\text{spectral square, from partition + orthogonality}}; \qquad
  \underbrace{\sigma^2 = (q - u)\,\sigma + 1}_{\text{Hecke relation}}.
$$

These derivations combine into the proposition. The parallel identity $(-q^{-1})/q = -(q^2)^{-1}$ — defining the per-crossing eigenvalue ratio over any field without channel data — holds independently of the channel data.

The primary model assigns these elements to the commutant of $\sigma_1$ in the two-strand Hecke algebra $H_2(q)$. Here $\sigma$ represents the braid operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure). Setting $u = q^{-1}$ casts the spectral form as the eigenvalue decomposition of $\sigma_1$ supporting eigenvalues $q$ and $-q^{-1}$. The resulting Hecke relation proves that the abstract channel data logically forces the Skein relation without external topological presentation.
