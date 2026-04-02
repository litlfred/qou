Let $R$ be a commutative ring with unity, $A$ an $R$-algebra which
is free as an $R$-module and without quasi-zeros, $(B, <)$ an
[admissible system](#def:admissible-system), and $I$ a two-sided
ideal in $A$.

**Gröbner basis.** A set of generators
$G = \{g_\gamma \mid \gamma \in \Gamma\}$ for $I$ is a *Gröbner
basis* with respect to $(B, <)$ if for every $h \in I$ we have a
representation

$$
  h = \sum_{k \in K} \lambda_k\, u_k \cdot g_{\gamma_k} \cdot v_k

$$

for $K$ an index set, $\gamma_k \in \Gamma$, $\lambda_k \in R^*$,
$u_k, v_k \in B$, such that
$\mathrm{LM}(u_k \cdot g_{\gamma_k} \cdot v_k) \leq \mathrm{LM}(h)$
whenever $u_k \cdot g_{\gamma_k} \cdot v_k \neq 0$.

**Unital.** A subset $G \subseteq A$ is *unital* if:
1. For all $\gamma \in \Gamma$:
   $\mathrm{LC}(g_\gamma) \in R^\times$ (the units of $R$).
2. For all $\gamma \in \Gamma$ and $\alpha, \beta \in B$:
   $\mathrm{LC}(\alpha \cdot g_\gamma \cdot \beta) \in R^\times$
   whenever $\alpha \cdot g_\gamma \cdot \beta \neq 0$.

**$S$-polynomial.** For $f, f' \in A$, an *$S$-polynomial* is
constructible about $f$ and $f'$ if there exist
$u, u', v, v' \in B$, $\lambda, \lambda' \in R^*$ such that

$$
  \lambda\,\mathrm{LT}(u \cdot \mathrm{LT}(f) \cdot v)
  = \lambda'\,\mathrm{LT}(u' \cdot \mathrm{LT}(f') \cdot v').

$$

In this case,

$$
  S(f, f') := \lambda\, u \cdot f \cdot v
    - \lambda'\, u' \cdot f' \cdot v'.

$$

If the ground ring is a field, every Gröbner basis is automatically
unital. If $B$ is closed under multiplication, condition (b) follows
from (a).
