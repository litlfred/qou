**Definition.**
*Let $H_n(R, q)$ be the Hecke algebra at substrate parameter $q$. For each Wedderburn block indexed by a partition $\lambda \vdash k$ ($k = 2, \ldots, k_{\max}(K, q)$, where $k_{\max}(K, q)$ is the per-atom truncation determined by the interaction-strand requirement of $K$ — see [confinement level](#def:confinement-level)), the **knot operator energy** of $\lambda$ at $q$ is the absolute value of its LP-dual shadow price:*

$$
  E(\lambda, q)
  \;:=\;
  \bigl| u_\lambda(q) \bigr|
  \;=\;
  \left|
    \frac{w_\lambda(q)}{d_\lambda(q)}
    \;-\;
    \frac{1}{[k]_q!}
  \right|,
$$

*where $w_\lambda(q) = d_q(\lambda)^2 / [k]_q!$ is the Wedderburn weight, $d_\lambda(q) = \dim_q V_\lambda$ is the quantum dimension, and $1/[k]_q!$ is $\min_\lambda\, w_\lambda/d_\lambda$, the minimum taken across partitions of $k$ and attained by the trivial $1$-dimensional $(k)$ and $(1^k)$ representations.*

**Values.**
*The energy takes values in:*
- *Archimedean realisation $R = \mathbb{R}$: $E(\lambda, q) \in \mathbb{R}_{\geq 0}$ (totally ordered).*
- *Non-archimedean $\mathbb{Q}_p$: $E(\lambda, q) \in \{p^{-n} : n \in \mathbb{Z}\} \cup \{0\}$ (totally ordered).*
- *Finite field $\mathbb{F}_p$: no archimedean absolute value exists. The energy filtration is undefined. Confinement falls back to ILP feasibility (see [stable atom](#def:stable-atom)), which *is* base-ring-independent.*
