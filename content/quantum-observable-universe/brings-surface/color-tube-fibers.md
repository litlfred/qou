Let $z \in \mathbb{P}^1(\mathbb{C})$.  The *color tube* at $z$ is the
affine curve defined over $\mathbb{Z}[z]$ by the color tube
cubic; we denote it $R_z$, $G_z$, or
$B_z$ according to which color tube coordinate $\mathbf{r}_z$,
$\mathbf{g}_z$, or $\mathbf{b}_z$ is used:

```tex
\begin{equation}\label{eq:color-tube-fiber-def}
  R_z  := 
  \bigl\{\mathbf{r}_z \in \mathbb{A}^1 :
    \mathbf{r}_z^{3} + (4z+1)\mathbf{r}_z^{2}
    + (6z^2+3z+1)\mathbf{r}_z
    + (4z^3+3z^2+2z+1) = 0\bigr\},
\end{equation}
```

and $G_z$, $B_z$ are defined by the same equation with coordinates
$\mathbf{g}_z$ and $\mathbf{b}_z$, respectively.  The coordinates
are related to the Lagrange resolvents by

$$
  \mathbf{r}_z = w_2 - z, \qquad \mathbf{g}_z = w_3 - z, \qquad
  \mathbf{b}_z = w_4 - z.
$$

As varieties, $R_z \cong G_z \cong B_z$ is isomorphic to the color
elliptic fiber $\mathcal{E}_z$ of [color elliptic curve](#prop:color-elliptic) via
the shift $X = \mathbf{c} + z$.
