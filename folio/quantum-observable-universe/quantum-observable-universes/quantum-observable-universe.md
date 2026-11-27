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

The quotient in (5) is the **antisymmetric** one. The twist acts on $V$ by a unit scalar, $\theta_V = s \cdot \mathrm{id}_V$, and the braiding acts on the quotient by $-s^{-1}$:
$$
\pi \circ \beta_{V,V} = -s^{-1}\, \pi .
$$
This is the scalar the balancing axiom allows: since $\Lambda^2 V \cong \mathbf{1}$ and $\theta_{\mathbf{1}} = \mathrm{id}$, balancing forces $s^2 c^2 = 1$ for any braiding scalar $c$ on the quotient, and the antisymmetric choice is $c = -s^{-1}$. The Hecke eigenvalue $-q^{-1}$ together with $\theta_V = q^{1/2}$ would force $q = 1$, so the two cannot both hold. The pin excludes the trivial choice $V = \mathbf{1}$, $\Lambda^2 V = \mathbf{1} \otimes \mathbf{1}$: there $c = s = 1$, so $\pi = -\pi$, which makes $\pi$ zero whenever $2$ is invertible. Lean: `QOU/Core/ExteriorQuotientNormalisation.lean` (`exteriorSquare_balancing`, `hecke_halfTwist_forces_q_one`).
