Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with $\chi(A) = -6$ and fiber genus $g(\Sigma_4) = 4$. Let $K$ be any knot type appearing as a component of a link produced by a finite sequence of Hopf linkings $\ell_H$, color-tube threadings $\ell_c$, and Skein crossing changes $\sigma$ applied to generators in $\mathcal{G}$. Then:
1. The Seifert genus of $K$ satisfies $g(K) \leq 4$.
2. $K$ admits a localized knot structure $(c, K) \in \mathrm{Hom}(\mathbf{1}, A^{\mathrm{co}T}) \times \mathrm{Knot}$ at some point $c$.
3. The localized knot $(c, K)$ descends under $\tau$ to an observable morphism in $\mathbf{C}$: every generated particle interacts with every other generated particle via the categorical braiding.

No generated knot is "dark"—the generation scheme is closed under observability.

*Hopf linking $\ell_H$ and Color-tube threading $\ell_c$* preserve each component's knot type and Seifert genus. The structures live in the total space and do not increase the genus of any individual component. 

*Skein crossing change $\sigma$* alters the Seifert genus by at most $± 1$:
$$
  |g(L_+) - g(L_-)| \leq 1, \qquad
  g(L_0) \leq \max\{g(L_+), g(L_-)\}.
$$
While a crossing change might produce a knot of genus $5$, Bring's surface imposes a spectral filter: only knots with $g(K) \leq 4$ admit localized knot structures. The physical state space $V_{\mathrm{phys}} = \varinjlim V^{\otimes n}$ vanishes for $g = 5$ descendants because the fibre functor $\tau$ cannot evaluate them.

This spectral filter acts directly at the level of the Skein resolution:
$$
  q  [L_+] - q^{-1} [L_-]
  = (q^{1/2} - q^{-1/2}) [L_0].
$$
Terms with $g > 4$ lie in the kernel of the mass functional $\mathfrak{m}$. The physical mass receives contributions only from embeddable terms. Every knot in the standard dictionary has $g(K) \leq 4$. Skein descendants like $4_1$ typically exhibit lower genus than their parent generators.
