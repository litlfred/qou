Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
[maximal torus](#def:maximal-torus) $T$ and
[weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$.
Then there exists a
[categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \varTheta_A)$ on $A$ satisfying:

1. **Vertical generator:** $\pi_V \circ d = \iota_\xi d\varTheta_A$.
2. **Normalisation:** $\xi \mathbin{;} \varTheta_A = \varTheta_A$
   (categorically: $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$).

```tex
\begin{equation}\label{eq:reeb-exists-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\xi"] \ar[d, "d"']
  & A \ar[d, "\varTheta_A"] \\
  \Omega^1(A) \ar[r, "\iota_\xi"']
  & A
\end{tikzcd}
\qquad (\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}})
\end{equation}
```
