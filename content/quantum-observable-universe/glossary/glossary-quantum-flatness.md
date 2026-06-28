Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
gauge group $G_q = \mathrm{Aut}^{\otimes}(\tau)$
([quantum gauge group](#def:quantum-gauge-group)) and connection
$\nabla$ on $A$ ([categorical connection](#def:categorical-connection)).
Let $\mathrm{INN}(G_q)$ denote the inner-automorphism $2$-group of
$G_q$, with $2$-form datum $B \in \Omega^2(A) \otimes \mathrm{Ad}(A)$.

The connection $\nabla$ is *quantum flat* if the curvature $F_\nabla$
equals the $2$-form datum:

$$
  F_\nabla = B.
$$

This is not an independent axiom. It is a derived consequence of the
instanton condition ([categorical instanton](#def:categorical-instanton))
combined with the simplicity constraint
$B \in \Gamma(\Lambda^+ H^* \otimes \mathrm{Ad}(P))$:

```tex
\begin{equation}\label{eq:quantum-flatness-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  F_\nabla \ar[r, equal, "\text{instanton}"]
    \ar[dr, equal, "F_\nabla = B"']
  & F_\nabla^+ \ar[d, equal, "\text{simplicity}"] \\
  & B
\end{tikzcd}
\qquad\text{(quantum flatness)}
\end{equation}
```

1. The instanton equation $\star_q F_\nabla = F_\nabla$ forces
   $F_\nabla = F_\nabla^+$ (self-dual curvature).
2. The simplicity constraint restricts $B = F_\nabla^+$.
3. Combining: $F_\nabla = B$.

:refterm[Quantum flatness]{#quantum-flatness} therefore encodes the condition that the $2$-group
gauge theory of $\mathrm{INN}(G_q)$ admits no independent
$2$-connection — the $2$-form datum is fully determined by the
ordinary connection.
