**Definition.**
*Let $H_n(R, q)$ be the Hecke algebra at substrate parameter $q$. Fix a partition $\lambda \vdash k$, bounded by the interaction-strand cutoff $k \leq k_{\max}(K, q)$ ([confinement level](#def:confinement-level)). The **knot operator energy** of $\lambda$ at $q$ is the absolute value of its LP-dual shadow price ([prop:mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)):*

$$
  E(\lambda, q)
  \;:=\;
  \bigl| u_\lambda(q) \bigr|
  \;=\;
  \left|
    \frac{w_\lambda(q)}{d_\lambda(q)}
    \;-\;
    \frac{1}{[k]_q!}
  \right|.
$$

*Here $w_\lambda(q) = d_q(\lambda)^2 / [k]_q!$ is the Wedderburn weight and $d_\lambda(q) = \dim_q V_\lambda$ is the quantum dimension. The subtrahend $1/[k]_q!$ is the LP-dual variable of the normalisation constraint. It equals the minimum of $w_\lambda/d_\lambda$ across partitions of $k$, attained by the trivial $1$-dimensional $(k)$ and $(1^k)$ representations.*

**Values.**
*The absolute value depends on the base ring:*
- *$R = \mathbb{R}$: $E(\lambda, q) \in \mathbb{R}_{\geq 0}$.*
- *$\mathbb{Q}_p$: $E(\lambda, q) \in \{p^{-n} : n \in \mathbb{Z}\} \cup \{0\}$.*
- *$\mathbb{F}_p$: No absolute value exists. The energy filtration is undefined. Confinement relies on ILP feasibility ([stable atom](#def:stable-atom)).*
