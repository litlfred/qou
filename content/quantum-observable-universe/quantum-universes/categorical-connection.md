Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$ with
differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)).

A connection is the categorical device that lets one differentiate
sections and transport structure along $A$; it generalizes the
classical de Rham connection $d$ on differential forms, and the
$\mathrm{SU}(2)$ instance in [Example](#ex:categorical-connection-su2)
gives the reader's first concrete grip on it.

A **connection** on $A$ is a morphism
$\nabla \colon A \to A \otimes \Omega^1(A)$ in $\mathbf{C}$ satisfying
the Leibniz rule: $\nabla(\mu(a \otimes b)) = \nabla(a) \cdot b + a \cdot \nabla(b)$, expressed by the commutativity
of the *Leibniz triangle*:

```tex
\begin{equation}\label{eq:leibniz-triangle}
\begin{tikzcd}[row sep=2.5em, column sep=3.5em]
  A \otimes A
    \ar[r, "\mu"]
    \ar[dr, "{\nabla \otimes 1 + 1 \otimes \nabla}"']
  & A \ar[d, "\nabla"]
  \\
  & A \otimes \Omega^1(A)
\end{tikzcd}
\end{equation}
```

The **curvature** of $\nabla$ is the composition

```tex
\begin{equation}\label{eq:curvature-composition}
\begin{tikzcd}[column sep=3em]
  A \ar[r, "\nabla"]
  & A \otimes \Omega^1(A) \ar[r, "\nabla"]
  & A \otimes \Omega^2(A)
\end{tikzcd}
\end{equation}
```

denoted $F_\nabla = \nabla^2$, which is $A$-linear (a standard
consequence of the Leibniz rule).
