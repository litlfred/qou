A quantum universe $(\mathbf{C}, A, \tau)$ over $R$ is a **quantum observable universe** if the forgetful functor $\tau$ is faithful and five conditions hold:

1. *(Rigidity)* Every object $V \in \mathbf{C}$ has a dual $V^{\vee}$, with evaluation $\mathrm{ev}_V \colon V \otimes V^{\vee} \to \mathbf{1}$ and coevaluation $\mathrm{coev}_V \colon \mathbf{1} \to V^{\vee} \otimes V$ satisfying the [snake identities](#def:snake-identity).
2. *(Non-degenerate integration)* The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces an isomorphism $A \xrightarrow{\sim} A^{\vee}$ via the pairing $(a, b) \mapsto \int_A ab$.
3. *(Observability)* There are no hidden global symmetries: $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.
4. *(Measurability)* The categorical Chern classes of the adjoint object vanish: $c_1(\mathrm{Ad}(A)) = 0$ and $c_2(\mathrm{Ad}(A)) = 0$.
5. *(Categorical volume constraint)* The exterior square of the fundamental object $V$ is a quotient $\pi \colon V \otimes V \twoheadrightarrow \Lambda^2 V$, and there is an **isomorphism** $\epsilon \colon \Lambda^2 V \xrightarrow{\ \sim\ } \mathbf{1}$ preserved by all tensor automorphisms:

```tex
\begin{equation}\label{eq:categorical-volume-constraint}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Lambda^2 V \ar[r, "\Lambda^2 g_V"]
              \ar[d, "\epsilon"', two heads]
  & \Lambda^2 V \ar[d, "\epsilon", two heads]
  \\
  \mathbf{1} \ar[r, "g_{\mathbf{1}} = \mathrm{id}"']
  & \mathbf{1}
\end{tikzcd}
\end{equation}
```

A quantum universe is thus braided; a quantum observable universe is braided and rigid.

**On "non-degenerate epimorphism" in condition 5.** The phrase "non-degenerate
epimorphism" for $\epsilon$ admits two readings of unequal strength, and only the stronger one does the work the
framework asks of condition 5:

| reading of $\epsilon$ | dimension statement | forces |
|---|---|---|
| epimorphism onto $\mathbf{1}$ | $\binom{N}{2} \neq 0$ | $N \geq 2$ — admits the colour fibre $N = 3$ |
| **isomorphism** $\Lambda^2 V \cong \mathbf{1}$ | $\binom{N}{2} = 1$ | $\mathbf{N = 2}$ |

Both rows follow from $\dim \Lambda^2 V = \binom{N}{2}$. The
isomorphism is the intended reading: $\det(g)$ is the scalar by which $g$ acts
on the **top** exterior power $\Lambda^N V$, so a constraint imposed on
$\Lambda^2 V$ is a determinant constraint exactly when $2 = N$. Under the weak
reading $\epsilon$ constrains only the second elementary symmetric function of
the eigenvalues, and the step to $\det(g_V) = 1$ — the whole point of condition
5 — does not go through. Non-degeneracy is precisely what upgrades the
epimorphism to an isomorphism, so the diagram's $\twoheadrightarrow$ remains
correct, just no longer the strongest thing true of $\epsilon$.
