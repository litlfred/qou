Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with fundamental
object $V$ (the unique simple object of categorical dimension $2$;
see [spin labels](#prop:spin-labels) for the full labelling). The *weight
subcategory* $\langle V \rangle \subset \mathbf{C}$ is the full
subcategory whose objects are direct sums of weight spaces of $V$
(i.e. simultaneous eigenspaces of the Cartan subalgebra action).
The **maximal torus** of the gauge group is

$$
  T = \mathrm{Aut}^{\otimes}(\tau|_{\langle V \rangle}),
$$

the sub-group scheme of
$G = \mathrm{Aut}^{\otimes}(\tau)$
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)) consisting of those natural
automorphisms that act diagonally on each weight space of $V$.

```tex
\begin{equation}\label{eq:maximal-torus-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  T \ar[r, hook] \ar[d, "\mathrm{diag}"']
  & G = \mathrm{Aut}^{\otimes}(\tau) \ar[d] \\
  \mathrm{Aut}(\tau(V))
  & \mathrm{Aut}^{\otimes}(\tau) \ar[l]
\end{tikzcd}
\qquad\text{(maximal torus)}
\end{equation}
```

Equivalently, $T$ is the largest subgroup of $G$ for which every
object in $\langle V \rangle$ decomposes into one-dimensional
$T$-eigenspaces.
