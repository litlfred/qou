Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which
is free as an $R$-module and without quasi-zeros, $(B, <)$ an
[admissible system](#def:admissible-system), and $I$ a two-sided
ideal in $A$.

A set of generators
$G = \{g_\gamma \mid \gamma \in \Gamma\}$ for $I$ is a
**Gröbner--Shirshov basis** with respect to $(B, <)$ if for every $h \in I$ we have a
representation

$$
  h = \sum_{k \in K} \lambda_k\, u_k \cdot g_{\gamma_k} \cdot v_k
$$

for $K$ an index set, $\gamma_k \in \Gamma$, $\lambda_k \in R^*$,
$u_k, v_k \in B$, such that
$\mathrm{LM}(u_k \cdot g_{\gamma_k} \cdot v_k) \leq \mathrm{LM}(h)$
whenever $u_k \cdot g_{\gamma_k} \cdot v_k \neq 0$.
