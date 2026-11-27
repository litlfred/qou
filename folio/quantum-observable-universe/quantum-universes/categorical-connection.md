Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$ with differential forms $\Omega^k(A)$ ([higher forms](#def:higher-forms)).

A **categorical connection** on $A$ is a morphism $\nabla \colon A \to A \otimes \Omega^1(A)$ in $\mathbf{C}$ satisfying the Leibniz rule $\nabla(\mu(a \otimes b)) = \nabla(a) \cdot b + a \cdot \nabla(b)$. The rule is expressed by the commutativity of the *Leibniz triangle*:

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

The **curvature** of $\nabla$ is the composition:

```tex
\begin{equation}\label{eq:curvature-composition}
\begin{tikzcd}[column sep=3em]
  A \ar[r, "\nabla"]
  & A \otimes \Omega^1(A) \ar[r, "\nabla"]
  & A \otimes \Omega^2(A)
\end{tikzcd}
\end{equation}
```

This composition is denoted $F_\nabla = \nabla^2$.
