Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe
with volume form $\mathrm{vol} \in \Omega^n(A)$
([Definition](#def:q-hodge-star)).  Every connection $\nabla$
that is a critical point of the categorical Yang--Mills functional

$$
  S[\nabla] \;=\; \lambda\!\bigl(\star_q(F_\nabla) \cdot F_\nabla\bigr)
$$

is an instanton ([Definition](#def:categorical-instanton)).  That is,
the following diagram commutes:

```tex
\begin{equation}\label{eq:self-duality-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  \Omega^2(A) \ar[r, "\star_q"] \ar[d, "\lambda(\,\cdot\, {*}\, \cdot\,)"']
  & \Omega^2(A) \ar[d, "\lambda(\,\cdot\, {*}\, \cdot\,)"] \\
  \mathbf{1} \ar[r, "\mathrm{id}"']
  & \mathbf{1}
\end{tikzcd}
\qquad\Longrightarrow\qquad
F_\nabla \in \Omega^+(A).
\end{equation}
```

---

By the Bogomolny decomposition in the dagger category,

$$
  \lambda(F_\nabla^* \cdot F_\nabla)
  \;=\; 2\,\lambda({F_\nabla^-}^* \cdot F_\nabla^-)
        + \lambda(F_\nabla \wedge_q F_\nabla),
$$

where the second term is topological (determined by the class
$[F_\nabla] \in \Omega^2(A)/\mathrm{exact}$).  Minimising
$S[\nabla]$ forces $F_\nabla^- = 0$, which is exactly the
self-duality condition.
