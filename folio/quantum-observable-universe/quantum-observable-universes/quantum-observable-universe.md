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
