The archimedean specialisation of the categorical $q$-Lie bracket
([categorical $q$-Lie bracket](#def:categorical-q-lie-bracket)) to
the $q$-deformed Lie bracket ([$q$-Lie bracket](#ex:q-lie-bracket))
violates the Jacobi identity when $q \neq 1$.

Let $U, V, W \in \Gamma(H)$ be horizontal vector fields (i.e.
$\varTheta(U) = \varTheta(V) = \varTheta(W) = 0$). The *Jacobiator*

$$
  \mathrm{Jac}_q(U,V,W)
   :=  [[U,V]_q, W]_q + [[V,W]_q, U]_q + [[W,U]_q, V]_q
$$

is given by

$$
  \mathrm{Jac}_q(U,V,W)
  =  -q^{-1}(1-q^{-1})\!\sum_{\mathrm{cyc}}
        d\varTheta(V,W)\mathcal{L}_\xi U,
$$

where the sum is over cyclic permutations of $(U,V,W)$. In particular,
$\mathrm{Jac}_q = 0$ if and only if $q = 1$ (classical Jacobi identity)
or $d\varTheta|_{H \times H} = 0$ (integrable horizontal distribution).
Since $d\varTheta|_{H \times H}$ is the Levi form $L_\varTheta$, which is
non-degenerate by hypothesis, $[\cdot,\cdot]_q$ violates the Jacobi
identity for all $q \neq 1$. Thus $(\mathfrak{X}(M), [\cdot,\cdot]_q)$
is a *Leibniz algebra* (or a pre-Lie algebra), not a Lie algebra.

```tex
\begin{equation}\label{eq:q-jacobiator-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  {[\cdot,\cdot]_q} \ar[r, "\mathrm{Jac}_q"]
    \ar[d, "q{=}1"']
  & q^{-1}(1{-}q^{-1})d\varTheta \wedge \mathcal{L}_\xi \\
  {[\cdot,\cdot]} \ar[r, "\mathrm{Jac}"']
  & 0
\end{tikzcd}
\qquad\text{(Jacobiator)}
\end{equation}
```

The coefficient $q^{-1}(1-q^{-1})$ matches the $d_q^2$ obstruction
([archimedean $d_q^2$](#prop:dq-squared)), confirming that both
failures — of nilpotence and of the Jacobi identity — are driven by
the same geometric source: the non-degeneracy of the contact structure.
