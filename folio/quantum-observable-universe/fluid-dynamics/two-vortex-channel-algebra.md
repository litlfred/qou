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

In addition, over any field with $q \neq 0$, the per-crossing eigenvalue ratio satisfies $(-q^{-1})/q = -(q^2)^{-1}$ independently of the channel projectors.

The primary model assigns these elements to the commutant of $\sigma_1$ in the two-strand Hecke algebra $H_2(q)$. Here $e_\pm$ represents the Wedderburn pair of the [Hopf channel](#def:van-der-waals-hopf-channel) and $\sigma$ represents the braid operator of the [$R$-matrix braiding](#prop:r-matrix-braiding-structure). Setting $u = q^{-1}$ casts the spectral form as the eigenvalue decomposition of $\sigma_1$ supporting eigenvalues $q$ and $-q^{-1}$. The resulting Hecke relation proves that the abstract channel data logically forces the Skein relation without external topological presentation.
