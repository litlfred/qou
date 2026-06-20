*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe satisfying
the
([categorical volume constraint](#eq:categorical-volume-constraint)), so that
$G_q = \mathrm{Aut}^{\otimes}(\tau) \cong \mathrm{SU}_q(2)$
([$\mathrm{SU}(2)$ emergence](#thm:su2-emergence)). Then the inner-automorphism
$2$-group $\mathrm{INN}(G_q)$ is the unique strict $2$-group whose
quantum flatness condition $F_A = B$ reproduces the
instanton equation $F_A^{-} = 0$ under the simplicity constraint.

```tex
\begin{equation}\label{eq:emergence-to-quantum-flat-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  F_A \ar[r, equal, "\text{instanton}"]
    \ar[d, "F_A = B"']
  & F_A^+ \ar[d, equal, "\text{simplicity}"] \\
  B \ar[r, equal]
  & F_A^+
\end{tikzcd}
\qquad\text{(derived quantum flatness)}
\end{equation}
```

:defterm[Quantum flatness]{#quantum-flatness} is not an independent assumption: it is a *derived
consequence* of the instanton axiom. The instanton condition
$F_A = F_A^+$ (self-dual curvature) combined with the simplicity
constraint $B = F_A^+$ gives $F_A = B$ automatically. The $2$-group
language is a descriptive overlay that makes the higher-categorical
structure manifest, not an additional physical constraint.
