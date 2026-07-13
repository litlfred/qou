Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with maximal torus $T$ and weight decomposition $\pi_H, \pi_V$. The **categorical Reeb derivation** is the endomorphism $\xi \colon A \to A$ generating the $T$-action. It acts as the infinitesimal generator of $T \subset G$ via the adjoint coaction. It satisfies three conditions. First, it generates vertical forms: $\pi_V \circ d = \iota_\xi d\varTheta_A$, where $\varTheta_A \in \Omega^1(A)$ is the canonical $1$-form dual to $\xi$. Second, it is normalized: $\varTheta_A(\xi) = \mathrm{id}_{\mathbf{1}}$. Third, horizontal forms are precisely the kernel of contraction: $\Omega^k_H(A) = \ker(\iota_\xi)$.

```tex
\begin{equation}\label{eq:reeb-decomposition-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\pi_H"] \ar[d, "\pi_V"']
  & \Omega^k_H(A) \ar[d, hook] \\
  \varTheta_A \wedge \Omega^{k-1}_H(A) \ar[r, hook]
  & \Omega^k(A)
\end{tikzcd}
\end{equation}
```
