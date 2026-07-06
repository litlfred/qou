Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe ([quantum observable universe](#def:quantum-observable-universe)). We define the **spatial realization** of $A$ as the space

$$
  M = \mathrm{Spec}(A) = \{ p \colon \mathbf{1} \to A \mid p \text{ is a categorical point} \}
$$

([categorical point](#def:categorical-point)). This functor realizes the algebra $A$ as a contact manifold. The target $M$ is an ordinary smooth manifold. The fibre functor $\tau$ recovers the function algebra $C^\infty(M)$ from $A$. Concretely, $M$ carries the following structures derived within $\mathbf{C}$:

1. **Local germs.** The augmentation ideal $\mathfrak{m}_p = \ker(p^* \colon A \to \mathbf{1})$ captures functions vanishing at $p$. The quotient $\mathfrak{m}_p / \mathfrak{m}_p^2$ is functorially dual to the tangent space $T_p M$. This yields the first-order germ decomposition

   $$
     A / \mathfrak{m}_p^2 \cong \mathbf{1} \oplus \mathfrak{m}_p / \mathfrak{m}_p^2.
   $$

2. **Kähler differentials.** The module $\Omega^1(A)$ of Kähler differentials maps under $\tau$ to sections of the cotangent bundle $\Gamma(T^* M)$.

3. **Contact form.** The Frobenius form $\int_A \colon A \to \mathbf{1}$ ([Frobenius pairing](#def:frobenius-pairing)) induces a canonical $1$-form $\varTheta_A \in \Omega^1(A)$ via pullback along the universal derivation $d \colon A \to \Omega^1(A)$.

4. **Reeb derivation.** The generator $\xi$ of the maximal torus action ([categorical Reeb](#def:categorical-reeb)) satisfies the Cartan relations $\iota_\xi \varTheta_A = \mathrm{id}_{\mathbf{1}}$ and $\iota_\xi d\varTheta_A = 0$.

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

Under $\tau$, the algebraic objects map to their geometric counterparts. The canonical $1$-form $\varTheta_A$ becomes the global contact $1$-form $\varTheta$. The generator $\xi$ becomes the Reeb vector field. The non-degeneracy of $\int_A$ guarantees that $d\varTheta$ is maximally non-degenerate on $\ker\varTheta$.
