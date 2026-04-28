Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with
[weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$
and [categorical Reeb derivation](#def:categorical-reeb)
$(\xi, \varTheta_A)$. Then there exists a
[substrate parameter](#def:substrate-parameter)
$q \in \mathrm{End}(\mathbf{1}) \cong k$, with $q \notin \mu_\infty(k)$
(not a root of unity).  In the archimedean realisation this specialises
to a substrate field $q \colon M \to \mathbb{R}_{>0}$ with
$q(p) \ge 1$, such that the $q$-deformed differential

$$d_q = q^{-1} d + (1 - q^{-1}) \pi_V \circ d$$

interpolates between the full differential $d$ (at $q = 1$) and the
vertical projection $\pi_V \circ d$ (as $q \to \infty$).

```tex
\begin{equation}\label{eq:substrate-parameter-exists-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  d \ar[r, phantom, "\xleftarrow{q=1}"]
  & d_q \ar[r, phantom, "\xrightarrow{q \to \infty}"]
  & \pi_V \circ d
\end{tikzcd}
\qquad\text{(substrate interpolation)}
\end{equation}
```
