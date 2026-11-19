Let $\mathbb{P}(V)$ be the projective line object. Using the Reeb decomposition, every form splits as $\alpha = \alpha_H + \varTheta \wedge \iota_\xi \alpha$. The **contact affine chart** $U_\xi \subset \mathbb{P}(V)$ is the open dense subset where the Reeb component is non-vanishing:

$$
  U_\xi =  \bigl\{ [\alpha] \in \mathbb{P}(V)
   \big|  \iota_\xi\alpha \neq 0 \bigr\}.
$$

On $U_\xi$, the affine coordinate $Z$ is defined as the ratio of the horizontal component to the vertical Reeb component:

$$
  Z([\alpha]) =  \frac{\alpha_H}{\iota_\xi\alpha}.
$$

```tex
\begin{equation}\label{eq:contact-affine-chart-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  U_\xi \ar[r, hook] \ar[d, "Z"']
  & \mathbb{P}(V) \ar[d, "\cong"] \\
  H = \ker\varTheta \ar[r, hook]
  & \Omega^1_H(A)
\end{tikzcd}
\end{equation}
```

The coordinate $Z$ takes values in the horizontal distribution $H$.
