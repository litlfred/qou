**Two times.**  The Reeb time $t$ must be distinguished from the
substrate parameter $q$, which plays the role of cosmological time
(Big Bang $q \to \infty$ to heat death $q \to 1$).  The $q$-heat
equation ([$q$-heat equation](#def:q-heat-equation)) lives at *fixed*
$q$ and evolves in $t$ along the Reeb flow — it is the dissipative
shadow of the Reeb endofunctor on $\mathbf{Rep}(\mathrm{SU}_q(2))$.

**Categorical formulation.**  The left-hand side $\partial_t$ is
the infinitesimal generator of the Reeb translation
$\phi_t^q \colon \mathcal{S} \to \mathcal{S}$, regarded as an
endomorphism of the identity functor on the slice category
$\mathbf{C}|_{\mathcal{S}}$.  The right-hand side $\Delta_q$ is the
$q$-deformed Hodge Laplacian
([three-term expansion of the $q$-Laplacian](#rem:q-laplacian-expansion)).
The $q$-heat equation asserts the equality of these two
endomorphisms on $u$, which is a purely categorical condition — no
choice of base field is required.

```tex
\begin{equation}\label{eq:q-heat-commutative}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \mathcal{S}
    \ar[r, "u(t)"]
    \ar[d, "\phi_\epsilon^q"']
  & \mathbf{1}_{\mathbf{C}}
    \ar[d, "\mathrm{id} - \epsilon\Delta_q"]
  \\
  \mathcal{S}
    \ar[r, "u(t + \epsilon)"']
  & \mathbf{1}_{\mathbf{C}}
\end{tikzcd}
\end{equation}
```

**Decomposition.**  Substituting the three-term expansion
([$q$-Laplacian expansion](#rem:q-laplacian-expansion)) gives

$$
  \partial_t u  =  -q^{-2}\Delta u
  - q^{-1}(1 - q^{-1})[\text{Coriolis}]u
  - (1 - q^{-1})^2\Delta_\xi u.
$$

The three terms correspond to:

1. **Classical diffusion** ($q^{-2}\Delta$): heat spreads across the
   base manifold.
2. **Reeb-spin diffusion** ($\Delta_\xi$): heat spreads along the
   internal Reeb fibre (the $\mathrm{SU}_q(2)$ direction).
3. **Coriolis cross-coupling**: interference between base-motion and
   Reeb-rotation.

At $q = 1$ only the classical term survives and one recovers the
ordinary heat equation $\partial_t u = \nabla^2 u$ (since
$-\Delta = \nabla^2$ on $0$-forms in the Hodge convention).  As
$q \to \infty$
the classical term is suppressed and diffusion is dominated by pure
Reeb-spin dynamics.

**Base-ring independence.**  Because $\Delta_q$ is a polynomial
operator in $q, q^{-1}$
([base-field independence](#rem:base-field-independence)), the
$q$-heat equation makes sense over any commutative ring in which
$q - 1$ is invertible — including $\mathbb{F}_p$ and $\mathbb{Q}_p$
(after specialising $q$ to a unit $\ne 1$), and the universal ring
$\mathbb{Z}[q, q^{-1}, (q - 1)^{-1}]$.  Convergent series
representations of its solutions (heat kernel, $q$-Gaussian) are
archimedean phenomena and require $\mathrm{char} = 0$.
