Let $\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z$ be the color tube
coordinates at a point of Bring's surface
([colour tube fibres](#def:color-tube-fibers)).  The
:defterm[observed spacetime value]{#observed-value} is the element of $\mathbb{A}^1$
recovered from the color tube coordinates by the Vieta
identity:

```tex
\begin{equation}\label{eq:observed-value}
  \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z + 4z + 1 =  0.
\end{equation}
```

This identity defines the projection
$\pi_z \colon R_z \times G_z \times B_z \to \mathbb{A}^1$,
$(\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z) \mapsto z$,
which is a polynomial map over $\mathbb{Z}$.  At a branch
point $z_c$ where chiral sheets merge
([Bring's surface smoothness](#rem:brings-smoothness)), the exceptional divisor is
coordinatised by the limiting color vector; the observed spacetime
value reads off $z_c$ from the color data via the identity above,
providing a coordinate on the exceptional $\mathbb{P}^1(\mathbb{C})$.

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
