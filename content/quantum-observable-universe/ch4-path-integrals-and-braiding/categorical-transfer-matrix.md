Let $\mathfrak{H}_p = [K_1, \ldots, K_n]_p \bowtie \mathcal{L}$ be a
[hadron](#def:hadron) at a brane point $p$
([localized hadron](#def:localized-hadron)), and let $\mathcal{S}_p$ be the
exceptional divisor at $p$
([exceptional divisor](#def:exceptional-divisor)).

**Pointed knot variables.**
The constituent knots $K_i$ are simple objects in $\mathbf{C}$,
each factoring through a tensor power of $V$
([knot factorization](#rem:knot-factorization)):
$K_i \hookrightarrow V^{\otimes 2j_i}$ via the PawLei embedding
$\iota_{j_i}$.  The **pointed knot variables** of $\mathfrak{H}$ are the
formal variables $z_1, \ldots, z_n$ on $\mathcal{S}_p$, one for each
constituent, recording the insertion point of the
[vertex operator](#def:vertex-operator) $Y(K_i, z_i)$.

These variables are **not free** after the first crossing:
the link $\mathcal{L}$ encoding the internal entanglement
imposes algebraic relations among them.  Concretely, each
Hopf link between $K_i$ and $K_j$ constrains the pair
$(z_i, z_j)$ via the OPE singularity --- the Hecke relation
$(T - q)(T + q^{-1}) = 0$ evaluated at the collision
$z_i \to z_j$.  The relations are precisely the prior
entanglements of the constituents.

**Two levels of braiding operation.**
A braiding operation on $\mathfrak{H}$ can be described at two levels:

1. **Constituent level.**  Operate on the constituent
   variables $(z_1, \ldots, z_n)$ individually.  A crossing
   between $K_i$ and $K_j$ applies the vertex operator
   $Y(\sigma_k, z_k)$ at the relevant generator $\sigma_k$,
   producing a transfer matrix
   $T_{K_i, K_j}(q) \in \mathrm{M}_2(\mathbb{Z}[q^{\pm 1/2}])$
   that acts on the Hecke chain at $\sigma_k$.

2. **Composite level.**  Operate on the **hadron knot
   variable** $z_H$ --- the single formal variable of the
   composite knot $K_{\mathfrak{H}} = \hat{\beta}_{\mathfrak{H}}$ (the closure of the
   hadron braid word).  The Markov trace of the full braid
   word factors as a product of vertex volumes
   ([Markov trace product](#thm:markov-trace-product)):
   $\mathrm{tr}_M(\rho(\beta_{\mathfrak{H}})) = \prod_i \hat{V}_i(q)$.

**The categorical transfer matrix.**
A **categorical transfer matrix** for $\mathfrak{H}_p$ is the equivalence
class

$$
  \mathcal{T}(\mathfrak{H})
  \;=\;
  \bigl[\, T \,\bigr]_{\sim}
  \;\in\;
  \mathrm{End}\bigl(H_n(q)\bigr) \,\big/\, \sim

$$

where $T$ is any braiding operation on $\mathfrak{H}$ (at either level)
and the equivalence relation $\sim$ identifies two operations
$T_1 \sim T_2$ whenever they produce the same vertex volume:

$$
  T_1 \sim T_2
  \quad\Longleftrightarrow\quad
  \hat{V}(T_1, q) = \hat{V}(T_2, q)
  \quad\text{as polynomials in } q.

$$

This is well-defined because the vertex volume $\hat{V}_i(q)$
depends only on the Markov trace of the Hecke-reduced element
--- not on the specific braid representative, the
decomposition of $\mathfrak{H}$ into constituents, or the path of
braiding operations within $\mathcal{S}_p$.
