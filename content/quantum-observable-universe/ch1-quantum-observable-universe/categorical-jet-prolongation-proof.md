
The Frobenius--Hopf structure on $J^1(A)$ is inherited from $A$ via the
jet prolongation functor. The induced fibre functor $\tau'$ is defined
by composition with the canonical projection $J^1(A) \to A$, and the
substrate parameter $q$ carries over unchanged. The commutativity of
the diagram

```tex
\begin{equation}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  J^1(A) \ar[r, "\nabla'"] \ar[d, "j^1"']
  & J^1(A) \otimes \Omega^1(J^1(A)) \ar[d, "j^1 \otimes j^1"] \\
  A \ar[r, "\nabla"']
  & A \otimes \Omega^1(A)
\end{tikzcd}
\end{equation}
```

follows from the universal property of the jet bundle: $j^1$ is the
universal first-order differential operator, so any connection $\nabla$
on $A$ lifts uniquely to $\nabla'$ on $J^1(A)$ making the square
commute.
