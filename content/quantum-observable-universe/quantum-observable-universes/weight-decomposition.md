Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)) with maximal torus
$T$ ([maximal torus](#def:maximal-torus)) and higher differential forms
$\Omega^k(A)$ ([higher forms](#def:higher-forms)). The $T$-action on
$\Omega^k(A)$ induces a $\mathbb{Z}$-grading by weights. Denoting by
$\pi_H, \pi_V$ the projections onto the weight-$0$ and non-zero-weight
summands, every $\alpha \in \Omega^k(A)$ decomposes uniquely:

```tex
\begin{equation}\label{eq:weight-decomposition-cd}
\begin{tikzcd}[row sep=2em, column sep=3em]
  & \Omega^k(A) \ar[dl, "\pi_H"'] \ar[dr, "\pi_V"] & \\
  \Omega^k_H(A) \ar[rr, hook, "\oplus"']
  & & \Omega^k_V(A)
\end{tikzcd}
\qquad \alpha = \alpha_H + \alpha_V.
\end{equation}
```

Here $\alpha_H = \pi_H(\alpha)$ is the **horizontal component**
(weight-$0$ under $T$) and $\alpha_V = \pi_V(\alpha)$ is the
*vertical component* (non-zero weight). A form is *purely
horizontal* if and only if $\alpha_V = 0$.
