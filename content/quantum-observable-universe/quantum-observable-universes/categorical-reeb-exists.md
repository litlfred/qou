Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
[maximal torus](#def:maximal-torus) $T$ and
[weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$.
Then there exists a
[categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \theta_A)$ on $A$ satisfying:

1. **Vertical generator:** $\pi_V \circ d = \iota_\xi d\theta_A$.
2. **Normalisation:** $\xi \mathbin{;} \theta_A = \theta_A$
   (categorically: $\theta_A(\xi) = \mathrm{id}_{\mathbf{1}}$).

```tex
\begin{equation}\label{eq:reeb-exists-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\xi"] \ar[d, "d"']
  & A \ar[d, "\theta_A"] \\
  \Omega^1(A) \ar[r, "\iota_\xi"']
  & A
\end{tikzcd}
\qquad (\theta_A(\xi) = \mathrm{id}_{\mathbf{1}})
\end{equation}
```
