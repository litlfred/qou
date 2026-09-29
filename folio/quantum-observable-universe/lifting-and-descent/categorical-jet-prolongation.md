Let $(\mathbf{C}, A, \tau)$ be a quantum universe equipped with connection $\nabla$ ([categorical connection](#def:categorical-connection)). The space $J^1(A)$ ([categorical jet](#def:categorical-jet)) strictly inherits a Frobenius–Hopf structure from $A$. The quadruple $(\mathbf{C}, J^1(A), \tau', q)$, carrying the induced fibre functor $\tau'$, formally constitutes a quantum universe.

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

## Proof (sketch)

The first jet $J^1(A)$ of a Frobenius–Hopf object $A$ inherits its Frobenius–Hopf structure via transport along the connection $\nabla$. This relies on the synthetic-differential-geometry construction of the jet bundle for an algebra object (\cite{kock2004}, §1).

1. **Frobenius–Hopf transport.** The jet inclusion $j^1 \colon A \hookrightarrow J^1(A)$ forms an exact algebra map, and $\nabla$ strictly splits $J^1(A) \cong A \oplus (\Omega^1 \otimes A)$. The multiplication, comultiplication, unit, counit, and antipode of $A$ naturally extend to $J^1(A)$ through the Leibniz rule for $\nabla$, establishing $J^1(A)$ as a complete Frobenius–Hopf object.
2. **Induced fibre functor.** Defining $\pi \colon J^1(A) \to A$ as the jet projection, the functor $\tau' = \tau \circ \pi$ remains strictly monoidal, faithful, and exact. Consequently, $(\mathbf{C}, J^1(A), \tau', q)$ precisely satisfies the four quantum-universe axioms with the identical braiding eigenvalue $q$. $\square$
