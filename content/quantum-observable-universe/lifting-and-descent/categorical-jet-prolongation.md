
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

## Proof (sketch)

The first jet $J^1(A)$ of a Frobenius--Hopf object $A$ inherits a
Frobenius--Hopf structure by transport along the connection $\nabla$,
the synthetic-differential-geometry construction of the jet bundle of an
algebra object (\cite{kock2004}, §1).

1. **Frobenius--Hopf transport.** The jet inclusion
   $j^1 \colon A \hookrightarrow J^1(A)$ is an algebra map, and $\nabla$
   splits $J^1(A) \cong A \oplus (\Omega^1 \otimes A)$. The
   multiplication, comultiplication, unit, counit and antipode of $A$
   extend to $J^1(A)$ through the Leibniz rule for $\nabla$, making
   $J^1(A)$ a Frobenius--Hopf object.

2. **Induced fibre functor.** With $\pi \colon J^1(A) \to A$ the jet
   projection, $\tau' = \tau \circ \pi$ is again monoidal, faithful and
   exact, so $(\mathbf{C}, J^1(A), \tau', q)$ satisfies the four
   quantum-universe axioms with the *same* braiding eigenvalue $q$.

The Lean sibling builds `ProlongedConnection` and `JetPreservesQU` and
states existence of the prolonged structure with `jet.original = fh`;
the construction is deferred there via `sorry`
(`-- Ref: [kock2004], [manuscript] §1`). $\square$
