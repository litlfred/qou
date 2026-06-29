**Definition (curvature-rank).**
*For an element $T_w \in H_n(R, q)$ written as a word in
$\sigma_i^{\pm 1}$ of length $\ell(T_w)$, the **curvature-rank**
$r(T_w)$ is the smallest non-negative integer $r$ such that*

$$
  F^{\,r}(T_w) \;=\; F\bigl(F\bigl(\cdots F(T_w)\cdots\bigr)\bigr)
  \;\in\; J^{\,r}(q) \setminus J^{\,r+1}(q),
$$

*where $F$ is the Hecke curvature 2-cocycle
([def:hecke-curvature-2-cocycle](#def:hecke-curvature-2-cocycle)),
$F^{\,r}$ is the $r$-fold iterated curvature applied via
Leibniz extension, and $J^\bullet(q)$ is the GB confinement
filtration ([confinement level](#def:confinement-level)).
Equivalently, $r(T_w)$ counts the minimal number of times the
Hecke or Yang–Baxter relations must be applied to express $T_w$
in normal form starting from its free-algebra representative.*

*By construction $r(\mathbf{1}) = 0$, $r(\sigma_i) = 0$,
$r(\sigma_i^{\,2}) = 1$ (one Hecke reduction),
$r(\sigma_i \sigma_{i+1} \sigma_i) = 0$ in normal form but $1$ if
the YB relation must be applied.  In general,
$r(T_w) \leq \ell(T_w)$ with equality only for words requiring
maximal reduction.*
