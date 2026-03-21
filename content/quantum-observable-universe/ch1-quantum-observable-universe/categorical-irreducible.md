Let $(\mathcal{C}, A, \omega)$ be a quantum observable universe.
Any categorical instanton $\nabla$
([Definition](#def:categorical-instanton)) is irreducible:
$\operatorname{Hom}_{\mathcal{C}}(\mathbf{1},\,\mathrm{Ad}(A)) = 0$.

---

Suppose $s \colon \mathbf{1} \to \mathrm{Ad}(A)$ is a non-zero
invariant morphism.  The following diagram commutes:

```tex
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbf{1} \ar[r, "s"] \ar[dr, "0"']
  & \mathrm{Ad}(A) \ar[d, "\lambda|_{\mathrm{Ad}}"] \\
  & \mathbf{1}
\end{tikzcd}
```

Since $\mathrm{Ad}(A)$ is the trace-free part of $A \otimes A^*$,
the Frobenius form $\lambda$ vanishes on it:
$\lambda \circ s = 0$.  But $\lambda$ is non-degenerate by the
observability axiom, so $s = 0$.
