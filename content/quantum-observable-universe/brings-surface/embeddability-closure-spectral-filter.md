The [embeddability closure](#thm:embeddability-closure) rests on how each generation move acts on the Seifert genus, together with a spectral filter at genus $4$.

*Hopf linking $\ell_H$ and Color-tube threading $\ell_c$* preserve each component's knot type and Seifert genus. The structures live in the total space and do not increase the genus of any individual component. 

*Skein crossing change $\sigma$* alters the Seifert genus by at most $\pm 1$:
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
