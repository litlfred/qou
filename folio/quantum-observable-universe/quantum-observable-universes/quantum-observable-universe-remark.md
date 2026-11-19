A quantum universe is thus braided; a quantum observable universe is braided and rigid.

**On "non-degenerate epimorphism" in the volume constraint.** The phrase "non-degenerate
epimorphism" for $\epsilon$ admits two readings of unequal strength, and only the stronger one does the work the
framework asks of condition 5:

| reading of $\epsilon$ | dimension statement | forces |
|---|---|---|
| epimorphism onto $\mathbf{1}$ | $\binom{N}{2} \neq 0$ | $N \geq 2$ — admits the colour fibre $N = 3$ |
| **isomorphism** $\Lambda^2 V \cong \mathbf{1}$ | $\binom{N}{2} = 1$ | $\mathbf{N = 2}$ |

Both rows are proved formally
in the Lean formalisation. The
isomorphism is the intended reading: $\det(g)$ is the scalar by which $g$ acts
on the **top** exterior power $\Lambda^N V$, so a constraint imposed on
$\Lambda^2 V$ is a determinant constraint exactly when $2 = N$. Under the weak
reading $\epsilon$ constrains only the second elementary symmetric function of
the eigenvalues, and the step to $\det(g_V) = 1$ — the whole point of condition
5 — does not go through. Non-degeneracy is precisely what upgrades the
epimorphism to an isomorphism, so the diagram's $\twoheadrightarrow$ remains
correct, just no longer the strongest thing true of $\epsilon$.
