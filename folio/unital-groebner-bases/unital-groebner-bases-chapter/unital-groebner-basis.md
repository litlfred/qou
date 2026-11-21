Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which is free as an
$R$-module and without quasi-zeros, and let $(B, <)$ be an admissible system
on $A$.

Let $I$ be a two-sided ideal in $A$ with a set of generators
$G = \{g_\gamma \mid \gamma \in \Gamma\}$.

We say that $G$ is a **Gröbner--Shirshov basis** with respect to $(B, <)$ if for every
$h \in I$ we have a representation:

$$h = \sum_{k \in K} \lambda_k u_k \cdot g_{\gamma_k} \cdot v_k$$

for $K$ an index set, $\gamma_k \in \Gamma$, $\lambda_k \in R^*$ and $u_k, v_k \in B$
such that $\LM(u_k \cdot g_{\gamma_k} \cdot v_k) \leq \LM(f)$ whenever
$u_k \cdot g_{\gamma_k} \cdot v_k \neq 0$.

We call a subset $G \subseteq A$ **unital** if:

1. For all $\gamma \in \Gamma$: $\LC(g_\gamma) \in R^\times$ (the units of $R$).
2. For all $\gamma \in \Gamma$ and for all $\alpha, \beta \in B$:
   $\LC(\alpha \cdot g_\gamma \cdot \beta) \in R^\times$ whenever
   $\alpha \cdot g_\gamma \cdot \beta \neq 0$.

Here $\LC(a)$ is the coefficient, in the expansion of $a$ in the $R$-basis $B$, of the
$<$-greatest basis element occurring in $a$.

An **S-polynomial** about $f, f' \in A$ is constructible if there exist
$u, u', v, v' \in B$ and $\lambda, \lambda' \in R^*$ such that
$\lambda \LT(u \cdot \LT(f) \cdot v) = \lambda' \LT(u' \cdot \LT(f') \cdot v')$,
in which case:

$$S(f, f') := \lambda u \cdot f \cdot v - \lambda' u' \cdot f' \cdot v'$$

The extra conditions of a Gröbner--Shirshov basis being unital are not that strong: if the
ground ring is a field, then a Gröbner--Shirshov basis is automatically a unital Gröbner--Shirshov
basis.
