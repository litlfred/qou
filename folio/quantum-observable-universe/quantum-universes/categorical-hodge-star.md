Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$ with higher differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)). The **categorical Hodge star** is the involution $\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by

$$
  \alpha \wedge \star \beta
  = \int_A\!\bigl(\alpha^* \cdot \beta\bigr) \mathrm{vol},
$$

```tex
\begin{equation}\label{eq:categorical-hodge-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\star"] \ar[d, "\star"']
  & \Omega^{n-k}(A) \ar[d, "\star"] \\
  \Omega^{n-k}(A) \ar[r, equal]
  & \Omega^{n-k}(A)
\end{tikzcd}
\qquad (\star^2 = \mathrm{id})
\end{equation}
```

where $\int_A \colon A \to \mathbf{1}$ is the Frobenius form, $\alpha^* = S(\alpha)$ is the antipode-conjugate, and $\mathrm{vol} \in \Omega^n(A)$ is the volume form (the unique invariant top form normalised by $\int_A(\mathrm{vol}) = 1$).
