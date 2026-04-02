Let $\beta \in B_n$ be a braid on $n$ strands and let
$\rho(\beta) \in H_n(q)$ be its image under the Hecke quotient
([Jones--Markov trace](#thm:jones-markov-trace)).  After Hecke
reduction, the element $\rho(\beta)$ decomposes as a product of
**generator chains**: for each generator $\sigma_i$
($i = 0, \ldots, n-2$), the crossings at $\sigma_i$ reduce to a
linear combination $a_i \sigma_i + b_i$ with
$a_i, b_i \in \mathbb{Z}[q^{\pm 1}]$.

**Theorem.**  The Markov trace factors as a product over generators:

$$
  \mathrm{tr}_M\!\bigl(\rho(\beta)\bigr)
  \;=\;
  \prod_{i=0}^{n-2} \hat{V}_i(q),
  \qquad
  \hat{V}_i(q) \;=\; z \cdot a_i + b_i,

$$

where $z = 1/(q^{1/2} + q^{-1/2})$ is the Markov trace parameter.
Each $\hat{V}_i$ is the **vertex volume** at generator $\sigma_i$
--- the evaluation of the vertex operator $Y(\sigma_i, z_i)$ at
the $i$-th insertion point on the exceptional divisor
([vertex operator](#def:vertex-operator)).

**Proof.**  The Markov trace processes the product by peeling
generators from the right.  At each step, $\sigma_i$ is the
rightmost (largest-index) generator in the remaining word, and
the Markov property gives:

$$
  \mathrm{tr}_M(\cdots (a_i \sigma_i + b_i))
  \;=\;
  (z \cdot a_i + b_i) \cdot \mathrm{tr}_M(\cdots).

$$

This works because:

1. The chain at $\sigma_i$ reduces to $a_i \sigma_i + b_i$ (linear
   in $\sigma_i$ and the identity).
2. The Markov property
   $\mathrm{tr}_M(x \sigma_n) = z\,\mathrm{tr}_M(x)$ applies to
   the $\sigma_i$ term.
3. Generator $\sigma_i$ is the rightmost active generator, so the
   Markov property applies directly.
4. The remaining word involves only $\sigma_0, \ldots, \sigma_{i-1}$,
   independent of $\sigma_i$.

Applying this recursively from $i = n-2$ down to $i = 0$ gives the
product formula.  $\square$

## Connection to the vertex operator algebra

In the VOA formalism ([vertex operator](#def:vertex-operator)),
each vertex volume $\hat{V}_i$ is the **correlation function** of a
single vertex operator insertion:

$$
  \hat{V}_i(q) \;=\;
  \bigl\langle\, Y(\sigma_i, z_i) \,\bigr\rangle_{\mathrm{Markov}}.

$$

The product formula is the **factorization of the $n$-point
correlation function** into one-point functions:

$$
  \bigl\langle\, Y(\sigma_0, z_0) \cdots Y(\sigma_{n-2}, z_{n-2})
  \,\bigr\rangle
  \;=\;
  \prod_{i=0}^{n-2}
  \bigl\langle\, Y(\sigma_i, z_i) \,\bigr\rangle.

$$

This factorization is **not** an approximation --- it is an exact
consequence of the Markov property, which is the state-operator
correspondence of the VOA.  Each generator acts at a distinct
insertion point on $\mathcal{S}_p$, and the Markov property ensures that the
insertions are independent (they are at distinct points on
$\mathbb{P}^1(\mathbb{C})$, so their OPE is non-singular).

The degree bound $\deg P_\beta \leq n^2 - 1$ follows from the
conformal weight: each vertex volume has conformal weight
$\leq 2k_i + 1$ (where $k_i$ is the number of crossings at
$\sigma_i$), and the total conformal weight of the product is
bounded by $\sum_i (2k_i + 1) \leq (n-1)(n+1) = n^2 - 1$.

## The chain of invariant-preserving maps

$$
  \mathbb{Z}[B_n]
  \;\xrightarrow{\text{Hecke quotient}}\;
  H_n(q)
  \;\xrightarrow{\text{chain reduction}}\;
  \prod_{i} (a_i \sigma_i + b_i)
  \;\xrightarrow{\text{Markov trace}}\;
  \prod_{i} \hat{V}_i(q)
  \;=\;
  P_\beta(q)

$$

Each step preserves the link invariant.  The polynomial
$P_\beta(q)$ is a well-defined invariant of the link
$\hat{\beta}$ --- it does not depend on the braid representative
or the reduction path.
