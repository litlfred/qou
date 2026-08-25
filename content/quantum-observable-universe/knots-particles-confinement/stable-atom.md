**Definition.**
*Let $K$ be an atom-knot ([atom](#def:atom-knot)) with normal form $T_w \in H_{n(K)}(q)$. Let $\mathrm{G}(q)$ be the Frobenius Gram matrix of the primitive Wedderburn-block operators $\{e_\lambda\}_{\lambda \vdash k,\;k \leq k_{\max}}$ ([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)). Decompose the normal form in the primitive basis:*

$$
  T_w
  \;=\;
  \sum_\lambda x_\lambda \cdot e_\lambda,
  \qquad
  x_\lambda \in \mathbb{Z}_{\geq 0}.
$$

*The atom $K$ is **stable at $q$** if and only if this decomposition admits an **ILP** (integer linear program) solution:*

$$
  \exists\, x \in \mathbb{Z}_{\geq 0}^N
  \;\text{such that}\;
  \mathrm{G}(q) \, x \;\geq\; 0
  \;\text{coordinatewise.}
$$

*That is, the Frobenius positivity constraint $(Gx)_\gamma \geq 0$ holds for every primitive constraint $\gamma$ with $x$ a nonnegative integer vector.*
