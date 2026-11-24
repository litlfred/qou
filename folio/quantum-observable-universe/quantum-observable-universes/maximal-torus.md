Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with fundamental object $V$. The weight subcategory $\langle V \rangle \subset \mathbf{C}$ is the full subcategory whose objects are direct sums of the weight spaces of $V$. The **maximal torus** $T$ of the gauge group is the subgroup of natural automorphisms that act diagonally on each weight space of $V$:

$$
  T = \mathrm{Aut}^{\otimes}(\tau|_{\langle V \rangle}) \subset G.
$$

```tex
\begin{equation}\label{eq:maximal-torus-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  T \ar[r, hook] \ar[d, "\mathrm{diag}"']
  & G \ar[d] \\
  \mathrm{Aut}(\tau(V))
  & \mathrm{Aut}^{\otimes}(\tau) \ar[l]
\end{tikzcd}
\end{equation}
```
