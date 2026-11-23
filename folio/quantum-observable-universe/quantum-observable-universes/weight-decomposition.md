Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with maximal torus $T$. The $T$-action extends to the non-commutative de Rham forms $\Omega^k(A)$, inducing a $\mathbb{Z}$-grading by weights. Let $\pi_H$ and $\pi_V$ denote the projections onto the weight-zero and non-zero-weight summands, respectively. This gives the **weight decomposition**, where every form $\alpha$ splits uniquely:

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

The horizontal component $\alpha_H = \pi_H(\alpha)$ is invariant under $T$. The vertical component $\alpha_V = \pi_V(\alpha)$ carries non-zero weight. A form is *purely horizontal* if and only if $\alpha_V = 0$.
