We show that if all $S$-polynomials reduce to zero and $f \in I$,
then $f$ has a Gröbner--Shirshov basis representation. Since $G$ generates $I$,
choose a representation

$$
  f = \sum_i h_i \cdot g_{\gamma_i} \cdot h_i', \qquad
  h_i, h_i' \in A,\; \gamma_i \in \Gamma.
$$

Expanding in the monomial basis $B$, write
$f = \sum_{i,k,k'} c_k c_{k'}' \beta_k \cdot g_i \cdot \beta_{k'}'$.

If for some representation all terms satisfy
$\mathrm{LM}(\beta_k \cdot g_i \cdot \beta_{k'}') \leq \mathrm{LM}(f)$,
we are done. Otherwise, define
$\alpha := \max\{\mathrm{LM}(h_i \cdot g_i \cdot h_i')\}$
with $\alpha > \mathrm{LM}(f)$; choose $\alpha$ minimal over all
representations.

Set $T := \{i \mid \mathrm{LM}(h_i \cdot g_i \cdot h_i') = \alpha\}$
and $g := \sum_{i \in T} \mathrm{LT}(h_i) \cdot g_i \cdot \mathrm{LT}(h_i')$.
By unitality, the leading coefficients are units, so
[Proposition ($S$-polynomial decomposition)](#prop:s-polynomial-decomposition)
applies:

$$
  g = \sum_{i \neq j \in T} d_{i,j}\, S_{i,j}.
$$

The $S_{i,j}$ are also $S$-polynomials about $g_i, g_j$; by
assumption they reduce to zero, i.e.\
$S_{i,j} = \sum_l \lambda_l^{i,j}\, u_l^{i,j} \cdot g_{l}^{i,j} \cdot v_l^{i,j}$
with $\mathrm{LM}(S_{i,j}) < \alpha$. Substituting back gives a new
representation of $f$ with strictly smaller maximal term —
contradiction.
