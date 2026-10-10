Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) with differential calculus $\Omega^1(A)$. The **higher differential forms** are the graded $A$-bimodule:

$$
  \Omega^k(A) =  \bigwedge\nolimits_A^k \Omega^1(A), \qquad k = 0, 1, 2, \ldots
$$

Here $\Omega^0(A) = A$. For an object $V$, $\Lambda^k V$ denotes its $k$-th exterior power. The differential $d \colon \Omega^k(A) \to \Omega^{k+1}(A)$ extends the universal derivation by the graded Leibniz rule and satisfies $d^2 = 0$:

```tex
\begin{equation}\label{eq:de-rham-complex}
\begin{tikzcd}[column sep=2.5em]
  A = \Omega^0(A) \ar[r, "d"]
  & \Omega^1(A) \ar[r, "d"]
  & \Omega^2(A) \ar[r, "d"]
  & \cdots
\end{tikzcd}
\qquad (d^2 = 0)
\end{equation}
```
