Let $(\mathcal{C}, A, \tau)$ be a quantum universe with
connection $\nabla$ ([categorical connection](#def:categorical-connection)).
Then $J^1(A)$ ([categorical jet](#def:categorical-jet)) inherits a
Frobenius--Hopf structure from $A$, and the quadruple
$(\mathcal{C},\, J^1(A),\, \tau',\, q)$ --- where $\tau'$ is
the induced fibre functor --- is again a quantum universe.
The following diagram commutes:

```tex
\begin{equation}\label{eq:jet-prolongation-cd}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  J^1(A) \ar[r, "\nabla'"] \ar[d, "j^1"']
  & J^1(A) \otimes \Omega^1(J^1(A)) \ar[d, "j^1 \otimes j^1"] \\
  A \ar[r, "\nabla"']
  & A \otimes \Omega^1(A)
\end{tikzcd}
\end{equation}
```

where $\nabla'$ is the prolonged connection and $\nabla$ the original.
