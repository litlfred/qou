In the VOA formalism ([vertex operator](#def:vertex-operator)),
each vertex volume $\hat{V}_i$ is the **correlation function** of a
single vertex operator insertion:

$$
  \hat{V}_i(q) = 
  \bigl\langle Y(\sigma_i, z_i) \bigr\rangle_{\mathrm{Markov}}.
$$

The product formula is the **factorization of the $n$-point
correlation function** into one-point functions:

$$
  \bigl\langle Y(\sigma_0, z_0) \cdots Y(\sigma_{n-2}, z_{n-2})
  \bigr\rangle
  = 
  \prod_{i=0}^{n-2}
  \bigl\langle Y(\sigma_i, z_i) \bigr\rangle.
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
  \xrightarrow{\text{Hecke quotient}}
  H_n(R, q)
  \xrightarrow{\text{chain reduction}}
  \prod_{i} (a_i \sigma_i + b_i)
  \xrightarrow{\text{Markov trace}}
  \prod_{i} \hat{V}_i(q)
  = 
  P_\beta(q)
$$

Each step preserves the link invariant.  The polynomial
$P_\beta(q)$ is a well-defined invariant of the link
$\hat{\beta}$ --- it does not depend on the braid representative
or the reduction path.
