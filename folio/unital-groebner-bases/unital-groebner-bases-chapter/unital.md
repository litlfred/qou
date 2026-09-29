Let $R$, $A$, and $(B, <)$ be as in the
[Gröbner--Shirshov basis](#def:groebner-basis) definition, and let
$G = \{g_\gamma \mid \gamma \in \Gamma\}$ be a subset of $A$.

A subset $G \subseteq A$ is **unital** if:
1. For all $\gamma \in \Gamma$:
   $\mathrm{LC}(g_\gamma) \in R^\times$ (the units of $R$).
2. For all $\gamma \in \Gamma$ and $\alpha, \beta \in B$:
   $\mathrm{LC}(\alpha \cdot g_\gamma \cdot \beta) \in R^\times$
   whenever $\alpha \cdot g_\gamma \cdot \beta \neq 0$.

If the ground ring is a field, every Gröbner--Shirshov basis is automatically
unital. If $B$ is closed under multiplication, condition (b) follows
from (a).
