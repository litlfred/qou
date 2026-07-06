Let $\beta \in B_n$ be a braid on $n$ strands and let
$\rho(\beta) \in H_n(R, q)$ be its image under the Hecke quotient
([Jones--Markov trace](#thm:jones-markov-trace)).  After Hecke
reduction, the element $\rho(\beta)$ decomposes as a product of
**generator chains**: for each generator $\sigma_i$
($i = 0, \ldots, n-2$), the crossings at $\sigma_i$ reduce to a
linear combination $a_i \sigma_i + b_i$ with
$a_i, b_i \in \mathbb{Z}[q^{\pm 1}]$.

**Theorem.**  The Markov trace factors as a product over generators:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr)
  = 
  \prod_{i=0}^{n-2} \hat{V}_i(q),
  \qquad
  \hat{V}_i(q) =  z \cdot a_i + b_i,
$$

where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov trace parameter.
Each $\hat{V}_i$ is the **vertex volume** at generator $\sigma_i$
--- the evaluation of the vertex operator $Y(\sigma_i, z_i)$ at
the $i$-th insertion point on the exceptional divisor
([vertex operator](#def:vertex-operator)).
