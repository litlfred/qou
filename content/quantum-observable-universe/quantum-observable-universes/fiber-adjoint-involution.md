Let $(\mathbf{C}, A, \tau)$ be a
([quantum observable universe](#def:quantum-observable-universe)). The Frobenius form
$\int_A \colon A \to \mathbf{1}$ induces an isomorphism
$A \xrightarrow{ \sim } A^{\vee}$ (the Frobenius self-duality), under
which:

1. the projective line object $\mathbb{P}(V)$
   ([projective line object](#def:projective-line-object)) embeds in the adjoint
   object $\mathrm{Ad}(A)$ as the coadjoint orbit of a highest-weight
   vector;
2. the assignment $\sigma \colon \mathbb{P}(V) \hookrightarrow \mathrm{Ad}(A)$ is an involution in the sense that $\sigma$
   determines $\mathbb{P}(V)$ from $\mathrm{Ad}(A)$ and vice versa;
3. the non-degeneracy of the [Frobenius pairing](#def:frobenius-pairing) forces the
   observability condition:

   $$
     \mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0.
   $$

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
\qquad\text{(fibre--adjoint involution)}
\end{equation}
```


## Lean formalization

The companion Lean `fiber_adjoint_involution_exists` currently encodes an existence stub (`∃ inv, True`) pending a faithful statement; the proof above is the intended content, deferred via `sorry` (`-- Ref: [manuscript]`).
