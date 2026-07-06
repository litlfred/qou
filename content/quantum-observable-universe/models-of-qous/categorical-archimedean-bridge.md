Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with weight decomposition $\pi_H, \pi_V$ ([weight decomposition](#def:weight-decomposition)) and categorical $q$-exterior derivative $d_q$ ([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)). 

Under the fibre functor $\tau$, the categorical and geometric definitions of $d_q$ coincide. The categorical vertical derivative $\pi_V \circ d$ corresponds to the geometric operation of contracting with the Reeb vector field $\xi$ and wedging with the contact form $\varTheta$. This correspondence forms a commuting square:

```tex
\begin{equation}\label{eq:categorical-archimedean-bridge-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\pi_V \circ d"] \ar[d, "\tau"']
  & \Omega^{k+1}(A) \ar[d, "\tau"] \\
  \Omega^k(M) \ar[r, "\varTheta \wedge \mathcal{L}_\xi"']
  & \Omega^{k+1}(M)
\end{tikzcd}
\qquad\text{(categorical--geometric bridge)}
\end{equation}
```

This states that $\tau(\pi_V \circ d) = \varTheta \wedge \mathcal{L}_\xi$, where $\varTheta$ is the contact form and $\mathcal{L}_\xi$ is the Lie derivative along the Reeb vector field.
