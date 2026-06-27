Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$
([quantum universe](#def:quantum-universe)) with higher differential forms
$\Omega^k(A)$ ([higher forms](#def:higher-forms)). The
**categorical Hodge star** is the involution
$\star \colon \Omega^k(A) \to \Omega^{n-k}(A)$ defined by

$$
  \alpha \wedge \star \beta
  = \int_A\!\bigl(\alpha^* \cdot \beta\bigr) \mathrm{vol},
$$

```tex
\begin{equation}\label{eq:categorical-hodge-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(A) \ar[r, "\star"] \ar[d, "\star"']
  & \Omega^{n-k}(A) \ar[d, "\star"] \\
  \Omega^{n-k}(A) \ar[r, equal]
  & \Omega^{n-k}(A)
\end{tikzcd}
\qquad (\star^2 = \mathrm{id})
\end{equation}
```

where $\int_A \colon A \to \mathbf{1}$ is the Frobenius form,
$\alpha^* = S(\alpha)$ is the antipode-conjugate, and
$\mathrm{vol} \in \Omega^n(A)$ is the volume form
(the unique $G$-invariant top form normalised by
$\int_A(\mathrm{vol}) = 1$).
That $\star^2 = \mathrm{id}$ (i.e. $\star$ is an involution)
follows from the non-degeneracy of $\int_A$ and the involutivity of
the antipode. More precisely: $S^2 = \mathrm{id}$ holds on $A$
because a commutative Hopf algebra has involutive antipode (and our
Frobenius--Hopf axioms imply commutativity of $A$ via the faithfulness
of $\tau$ into $R\text{-}\mathrm{Mod}$). The extension to
$\Omega^k(A)$ follows from the graded Leibniz rule for $S$ on the
differential graded algebra.
