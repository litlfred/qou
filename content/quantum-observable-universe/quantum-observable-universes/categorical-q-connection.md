Let $\nabla$ be a connection on $A$
([categorical connection](#def:categorical-connection)) and $\xi$ the Reeb
derivation ([categorical Reeb derivation](#def:categorical-reeb)).  The
**$q$-deformed connection** is

$$
  \nabla_q =  q^{-1}\nabla
  + (1 - q^{-1})(\iota_\xi \nabla)\varTheta_A.
$$

```tex
\begin{equation}\label{eq:q-connection-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\nabla"] \ar[dr, "\nabla_q"']
  & \Omega^1(A) \otimes A
    \ar[d, "q^{-1}\mathrm{id} + (1 - q^{-1})\varTheta_A \circ \iota_\xi"] \\
  & \Omega^1(A) \otimes A
\end{tikzcd}
\qquad\text{($q$-connection)}
\end{equation}
```

At $q = 1$, $\nabla_q = \nabla$.
