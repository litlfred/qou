*Let $K$ be an atom-knot ([atom](#def:atom-knot)) with normal form $T_w \in H_{n(K)}(q)$. Let $\mathrm{G}(q)$ be the Frobenius Gram matrix of the primitive Wedderburn-block operators $\{e_\lambda\}_{\lambda \vdash k,\;k \leq k_{\max}}$ ([mass-coefficient-shadow-price](#prop:mass-coefficient-shadow-price)). Decompose the normal form in the primitive basis:*

$$
  T_w
  \;=\;
  \sum_\lambda x_\lambda \cdot e_\lambda,
  \qquad
  x_\lambda \in \mathbb{Z}_{\geq 0}.
$$

*The coefficient vector $x(K, q) := (x_\lambda)_\lambda$ is determined by $T_w$. The atom $K$ is **stable at $q$** if and only if this vector is an integer point of the positivity cone:*

$$
  x(K, q) \in \mathbb{Z}_{\geq 0}^N
  \quad\text{and}\quad
  \mathrm{G}(q) \, x(K, q) \;\geq\; 0
  \;\text{coordinatewise.}
$$
