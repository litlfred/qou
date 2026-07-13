Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. The **spatial realization** of $A$ is the space

$$
  M = \mathrm{Spec}(A) = \{ p \colon \mathbf{1} \to A \mid
  p \text{ is a categorical point} \}.
$$

This functor realises the algebra $A$ as a contact manifold. It sends the Frobenius form to the global contact $1$-form and the torus generator to the Reeb field. The target $M$ is an ordinary smooth manifold—the classical space whose function algebra $C^\infty(M)$ the fibre functor $\tau$ recovers from $A$. Concretely, $M$ is equipped with the following structures, derived purely within $\mathbf{C}$:

1. **Local germs.** For each point $p$, the *augmentation ideal* $\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$ captures the functions vanishing at $p$. The quotient $\mathfrak{m}_p / \mathfrak{m}_p^2$ is functorially dual to the tangent space $T_p M$. This gives the first-order germ decomposition

   $$
     A / \mathfrak{m}_p^2
      \cong 
     \mathbf{1} \oplus \mathfrak{m}_p / \mathfrak{m}_p^2.
   $$

2. **Kähler differentials.** The module $\Omega^1(A)$ of Kähler differentials exists in $\mathbf{C}$ by hypothesis. Under the fibre functor, $\tau(\Omega^1(A))$ maps to sections of the cotangent bundle $\Gamma(T^* M)$.

3. **The contact form.** The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces a canonical $1$-form $\varTheta_A \in \Omega^1(A)$ via pullback along the universal derivation $d \colon A \to \Omega^1(A)$.

4. **The Reeb derivation.** The generator $\xi$ of the maximal torus action satisfies the Cartan relations $\iota_\xi \varTheta_A = \mathrm{id}_{\mathbf{1}}$ and $\iota_\xi d\varTheta_A = 0$ within the non-commutative differential calculus.

```tex
\begin{equation}\label{eq:spatial-realization-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  A \ar[r, "\tau"] \ar[d, "d"']
  & C^{\infty}(M) \ar[d, "d"] \\
  \Omega^1(A) \ar[r, "\tau"']
  & \Gamma(T^* M)
\end{tikzcd}
\qquad
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \varTheta_A \ar[r, mapsto, "\tau"]
  & \varTheta \\
  \xi \ar[r, mapsto, "\tau"']
  & \xi_{\mathrm{Reeb}}
\end{tikzcd}
\qquad\text{(spatial realisation)}
\end{equation}
```

Under $\tau$, these algebraic objects map to their geometric counterparts. $\varTheta_A$ becomes the global contact $1$-form $\varTheta$. $\xi$ becomes the Reeb vector field. Non-degeneracy of $\int_A$ guarantees that $d\varTheta$ is maximally non-degenerate on $\ker\varTheta$, which defines a contact manifold.
