*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $d_q$ be the categorical $q$-deformed exterior derivative
([categorical $q$-exterior derivative](#def:categorical-q-ext-deriv)).  The composition
$d_q^2 = d_q \circ d_q \colon \Omega^k(A) \to \Omega^{k+2}(A)$ is
given by

$$
  d_q^2\alpha
  =  q^{-1}(1 - q^{-1})\omega_V \wedge_q [\xi, \alpha],
$$

where $\omega_V \in \Omega^2(A)$ is the curvature of the weight
decomposition (the image of the unit $1_A$ under
$\pi_V \circ d \circ d$) and $[\xi, \alpha]$ is the Lie derivative
along the generator $\xi$ of the $T$-action
([weight decomposition](#def:weight-decomposition)).  The following diagram
displays the obstruction to nilpotence:

```tex
\begin{equation}\label{eq:dq-squared-cd}
\begin{tikzcd}[row sep=2.5em, column sep=2.5em]
  \Omega^k(A) \ar[r, "d_q"] \ar[dr, "d_q^2"']
  & \Omega^{k+1}(A) \ar[d, "d_q"] \\
  & \Omega^{k+2}(A)
\end{tikzcd}
\qquad
d_q^2 = 0 \Longleftrightarrow
q = 1  \text{ or } [\xi, \alpha] = 0.
\end{equation}
```

In particular, $d_q^2 \neq 0$ for generic $\alpha$ whenever
$q \neq 1$: the $q$-deformed de Rham complex is *not* a cochain
complex.  On $\xi$-invariant forms (the horizontal subcomplex
$\Omega^k_H(A)$), $d_q$ does reduce to $q^{-1} d$ and $d_q^2 = 0$.


While the case analysis resolving the vanishing conditions of $d_q^2$ relies on standard algebraic properties, identifying this specific $q$-curvature obstruction and demonstrating its explicit role in breaking the cochain property for generic non-invariant forms represents a mathematically novel application within the framework of categorical $q$-deformations.
