
Let $(\mathbf{C}, A, \tau)$ be a quantum universe with
connection $\nabla$ ([categorical connection](#def:categorical-connection)).
Then $J^1(A)$ ([categorical jet](#def:categorical-jet)) inherits a
Frobenius--Hopf structure from $A$, and the quadruple
$(\mathbf{C}, J^1(A), \tau', q)$ --- where $\tau'$ is
the induced fibre functor --- is again a quantum universe.

```tex
\begin{equation}\label{eq:jet-prolongation-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  (\mathbf{C}, A, \tau) \ar[r, "\nabla"]
  & (\mathbf{C}, J^1(A), \tau') \\
  A \ar[u, phantom, "\ni"] \ar[r, hook, "j^1"']
  & J^1(A) \ar[u, phantom, "\ni"]
\end{tikzcd}
\qquad\text{(jet prolongation)}
\end{equation}
```
