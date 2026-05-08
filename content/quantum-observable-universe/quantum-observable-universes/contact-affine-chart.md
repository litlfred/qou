Let $\mathcal{S}$ be the state bundle over $M$ whose fibres are the spaces of
$1$-forms, and let $\mathbb{P}(V)$ be the projective line object
([projective line object](#def:projective-line-object)). Using the
Reeb decomposition ([Reeb decomposition](#ex:reeb-decomposition)),
every form splits as
$\alpha = \alpha_H + \varTheta \wedge \iota_\xi \alpha$.

The *contact affine chart* $U_\xi \subset \mathbb{P}(V)$ is the open
dense subset of states with non-vanishing Reeb component:

$$
  U_\xi =  \bigl\{ [\alpha] \in \mathbb{P}(V)
   \big|  \iota_\xi\alpha \neq 0 \bigr\}.
$$

On $U_\xi$, the explicit *affine coordinate* is defined by the ratio
of horizontal spatial diffusion to vertical quantum spin:

$$
  Z([\alpha]) =  \frac{\alpha_H}{\iota_\xi\alpha}.
$$

```tex
\begin{equation}\label{eq:contact-affine-chart-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  U_\xi \ar[r, hook] \ar[d, "Z"']
  & \mathbb{P}(V) \ar[d, "\cong", "G/T"'] \\
  H = \ker\varTheta \ar[r, hook]
  & \Omega^1_H(A)
\end{tikzcd}
\end{equation}
```

The coordinate $Z$ takes values in the horizontal distribution
$H = \ker\varTheta$. The contact form $\varTheta$ and the Reeb vector field
$\xi$ thus automatically provide the stereographic projection for the
projective line fibres — no external coordinates are needed.
