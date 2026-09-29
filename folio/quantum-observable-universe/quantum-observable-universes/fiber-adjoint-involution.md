The Frobenius form $\int_A \colon A \to \mathbf{1}$ induces an isomorphism $A \xrightarrow{ \sim } A^{\vee}$. Under this self-duality, the projective line object $\mathbb{P}(V)$ embeds into the adjoint object $\mathrm{Ad}(A)$ as the coadjoint orbit of a highest-weight vector. This assignment $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ is an involution, entirely determining $\mathbb{P}(V)$ from $\mathrm{Ad}(A)$ and vice versa. The non-degeneracy of the Frobenius pairing then forces the observability condition $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.

```tex
\begin{equation}\label{eq:fiber-adjoint-involution-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathbb{P}(V)
    \ar[r, hook, "\sigma"]
    \ar[d, "\cong"']
  & \mathrm{Ad}(A)
    \ar[d, "\cong", "\int_A"'] \\
  G/T
    \ar[r, hook, "\text{coadjoint orbit}"]
  & A^{\vee}
\end{tikzcd}
\end{equation}
```
