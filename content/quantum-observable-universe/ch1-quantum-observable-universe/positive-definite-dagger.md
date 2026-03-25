Let $(\mathbf{C}, \dagger)$ be a rigid monoidal category with involutive
structure ([involutive structure](#def:involutive-structure)). The involution is
*positive-definite* if for every non-zero
morphism $f \colon \mathbf{1} \to X$ the composite

```tex
\begin{equation}\label{eq:positive-definite-cd}
\begin{tikzcd}[column sep=2.5em]
  \mathbf{1} \ar[r, "f"]
  & X \ar[r, "f^{\dagger}"]
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

is a positive element of $\mathrm{End}(\mathbf{1}) \cong R$.
Equivalently, the sesquilinear form
$$
  \langle g, h \rangle
  = g^{\dagger} \circ h
  \in \mathrm{End}(\mathbf{1})
$$
is positive-definite on $\mathrm{Hom}(\mathbf{1}, X)$ for every
object $X$. This replaces the analytic notion of "Hilbert-space inner
product" with a purely categorical condition.
