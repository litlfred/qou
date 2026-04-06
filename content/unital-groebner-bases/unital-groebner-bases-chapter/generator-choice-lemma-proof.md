Set $h := h_i$, $f := f_i$. Since $G$ is a Gröbner--Shirshov basis, write

$$
  h = \sum_{k \in K} \lambda_k\, u_k \cdot g_{\gamma_k} \cdot v_k
$$

with $\lambda_k \in R^*$, $u_k, v_k \in B$, $\gamma_k \in \Gamma$.
Set $\alpha := \mathrm{LM}(h)$.

Choose a representation with $\alpha$ minimal, and define
$T := \{k \in K \mid \mathrm{LM}(u_k \cdot g_{\gamma_k} \cdot v_k) = \alpha\}$.
Further choose so that $|T|$ is minimal. If $|T| = 1$, we are done.

Otherwise, let $k_1 \neq k_2 \in T$ and set
$c_{k_i} := \mathrm{LC}(u_{k_i} \cdot g_{\gamma_{k_i}} \cdot v_{k_i})$.
By unitality, $c_{k_i} \in R^\times$, so we may form the
$S$-polynomial

$$
  S := \lambda_{k_2}\,\frac{c_{k_2}}{c_{k_1}}\,
    u_{k_1} \cdot g_{\gamma_{k_1}} \cdot v_{k_1}
    - \lambda_{k_2}\, u_{k_2} \cdot g_{\gamma_{k_2}} \cdot v_{k_2}.
$$

Substituting back, either all terms with leading monomial $\alpha$
cancel (contradicting minimality of $\alpha$) or we reduce $|T|$ by
at least one (contradicting minimality of $|T|$). Thus $|T| = 1$.
