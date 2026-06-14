The archimedean specialisation of the categorical $d_q^2$ formula
([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)) yields,
for the $q$-deformed exterior derivative
([$q$-exterior derivative](#ex:q-ext-deriv)) acting on
$\Omega^k(M)$:

$$
  d_q^2\alpha
  =  q^{-1}(1 - q^{-1})d\varTheta \wedge \mathcal{L}_\xi\alpha.
$$

```tex
\begin{equation}\label{eq:dq-squared-archimedean-diagram}
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  \Omega^k(M) \ar[r, "d_q"] \ar[rr, bend left=25, "d_q^2"]
  & \Omega^{k+1}(M) \ar[r, "d_q"]
  & \Omega^{k+2}(M)
\end{tikzcd}
\qquad\text{($d_q^2 \neq 0$ for $q \neq 1$)}
\end{equation}
```

Here the categorical curvature $\omega_V$ of the weight projection
specialises to $d\varTheta$ (the symplectic form on $H$) via the
([categorical--geometric correspondence](#prop:categorical-archimedean-bridge)),
and $[\xi, \alpha]$ becomes $\mathcal{L}_\xi\alpha$.

In particular, $d_q^2 = 0$ if and only if $q = 1$ (classical case) or
$\alpha$ lies in the kernel of $\mathcal{L}_\xi$ (Reeb-invariant forms).
On horizontal $\mathcal{L}_\xi$-invariant forms, $d_q$ *does*
define a cochain complex.

Though the proof utilises standard simplification over the obstruction product, framing the failure of the cochain complex condition geometrically—as proportional to the symplectic form and Reeb-invariant flow—constitutes a novel physical translation for the Quantum Observable Universe.
