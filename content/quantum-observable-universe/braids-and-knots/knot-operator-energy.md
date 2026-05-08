**Definition.**
*Let $H_n(R, q)$ be the Hecke algebra at substrate parameter $q$.
For each Wedderburn block indexed by a partition $\lambda \vdash k$
($k = 2, \ldots, k_{\max}(K, q)$, where $k_{\max}(K, q)$ is the
per-atom truncation determined by the interaction-strand
requirement of $K$ — see [confinement level](#def:confinement-level)),
the **knot operator energy** of $\lambda$ at $q$ is the absolute
value of its LP-dual shadow price
([prop:bw-coefficient-shadow-price](#prop:bw-coefficient-shadow-price)):*

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

*where $w_\lambda(q) = d_q(\lambda)^2 / [k]_q!$ is the Wedderburn
weight, $d_\lambda(q) = \dim_q V_\lambda$ is the quantum dimension,
and $1/[k]_q!$ is the LP-dual variable of the normalisation
constraint (the smallest $w_\lambda/d_\lambda$ across partitions of
$k$, attained by the trivial $1$-dimensional $(k)$ and $(1^k)$
representations).*

**Values.**
*The energy takes values in:*
- *Archimedean realisation $R = \mathbb{R}$: $E(\lambda, q)
  \in \mathbb{R}_{\geq 0}$ (totally ordered).*
- *Non-archimedean $\mathbb{Q}_p$: $E(\lambda, q) \in
  \{p^{-n} : n \in \mathbb{Z}\} \cup \{0\}$ (also totally ordered).*
- *Finite field $\mathbb{F}_p$: no archimedean absolute value —
  the energy filtration is undefined, and confinement falls back
  to ILP feasibility (see [stable atom](#def:stable-atom)) which
  IS base-ring-independent.*

**Vanishing locus.**
*The set $\{q \in Q : E(\lambda, q) = 0\}$ is the **LP boundary**
for partition $\lambda$: at these $q$-values the operator
$\lambda$ becomes constraint-binding, and its inclusion or
exclusion in the LP-dual basis switches.  Crossing such a
$q$-value is a categorical phase transition for any atom whose
NF includes operator $\lambda$.*

**Cheap and expensive operators.**
*$1$-dimensional partitions $(k), (1^k)$ have
$w_\lambda/d_\lambda = 1/[k]_q!$, so $E(\lambda, q) = 0$
identically — these operators carry no shadow-price weight and
are always available.  Only mixing partitions ($d_\lambda \geq 2$)
have nonzero $E$ and contribute to the confinement filtration.*
