Let $\mathfrak{H}_p = [K_1, \ldots, K_n]_p \oplus \mathcal{L}$ be a
[hadron](#def:hadron) at a brane point $p$
([localized hadron](#def:localized-hadron)), and let $\mathcal{S}_p$ be the
exceptional divisor at $p$
([exceptional divisor](#def:exceptional-divisor)).

A **categorical transfer matrix** for $\mathfrak{H}_p$ is the equivalence
class

$$
  \mathcal{T}(\mathfrak{H})
  = 
  \bigl[ T \bigr]_{\sim}
   \in 
  \mathrm{End}\bigl(H_n(R, q)\bigr) \big/ \sim
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
