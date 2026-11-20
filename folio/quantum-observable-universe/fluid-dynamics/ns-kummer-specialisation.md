Let $(\mathbf{C}, A, \tau)$ isolate a valid QOU whose Reeb bundle $\xi$ over the closed surface $\mathcal{S}$ has class $[\xi] \in H^1(\mathcal{S}, \mathbb{G}_m)$ and first obstruction $\kappa_0 = c_1(\xi) = e(\xi) \in H^2(\mathcal{S}, \mathbb{Z})$, and suppose $\xi$ is the unit tangent bundle of $\mathcal{S}$. Then $\kappa_0[\mathcal{S}] = \chi_{\mathrm{eu}}(\mathcal{S})$ by Poincaré--Hopf ([QU-to-QOU](#thm:qu-to-qou), item 2). The hypothesis is not supplied by the [Reeb bundle](#def:reeb-bundle) $\mathcal{R}_p$, which is the Hopf fibration over the fibre $\mathcal{S}_p \cong S^2$ with Euler number $-1$. For the Descartes universe it holds for the link of the canonical cone over Bring's curve, $UT(\Sigma_4)$, with Euler number $-6$ ([the cone link](#lem:bring-cone-reeb-quaternionic-twist)). The integer that controls the Kummer tower is therefore $\chi_{\mathrm{eu}}(\mathcal{S})$, a topological Euler characteristic, and not the categorical trace $\mathrm{tr}(\mathrm{id}_A)$ ([the three Euler characteristics](#rem:three-euler-characteristics)).

The strict Kummer exact sequence evaluated at any integer $n \geq 1$:

$$
  1 \to \mu_n \to \mathbb{G}_m
  \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

forces a long exact sequence mapping through cohomology:

$$
  H^1(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\cdot n}
  H^1(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\partial_n}
  H^2(\mathcal{S}, \mu_n)
  \to H^2(\mathcal{S}, \mathbb{G}_m) = 0.
$$

On a closed surface $H^2(\mathcal{S}, \mathbb{G}_m) = 0$, so $\partial_n$ is surjective; its source modulo $n$ is $\mathbb{Z}/n$ via the degree (the degree-zero part of $H^1(\mathcal{S}, \mathbb{G}_m)$ is divisible), and $H^2(\mathcal{S}, \mu_n) \cong \mathbb{Z}/n$. The [specialisation driving $q = 1$](#rem:substrate-gm-torsion) projects cleanly:

$$
  \kappa_0 \mapsto
  \partial_n[\xi] = \kappa_0 \bmod n
   \in 
  H^2(\mathcal{S}, \mu_n) \cong \mathbb{Z}/n,
$$

which is the obstruction to an $n$-th root of $\xi$ ([QU-to-QOU](#thm:qu-to-qou), item 3).

The resulting class avoids zero if and only if $n \nmid \kappa_0$, that is, if and only if $\xi$ has no $n$-th root. Evaluated against any QOU with $\chi_{\mathrm{eu}}(\mathcal{S}) \neq 0$:

1. The exact specialisation $\kappa_0|_{q=1}$ avoids zero within $H^2(\mathcal{S}, \mu_n)$ for all integers $n \nmid \chi_{\mathrm{eu}}(\mathcal{S})$.
2. The integer set $\{n : n \nmid \chi_{\mathrm{eu}}(\mathcal{S})\}$ extends to infinity (encompassing all primes not dividing $\chi_{\mathrm{eu}}(\mathcal{S})$), so the obstruction remains **persistently nonzero**, piercing infinitely many levels of the Kummer tower.
3. The obstruction vanishes only at the finite, isolated Kummer levels $n \mid \chi_{\mathrm{eu}}(\mathcal{S})$, which align with the finite set of roots of unity where the category's truncation is compatible with the fixed Euler class.

**What persistence does and does not buy (the genericity caveat).** Items 2 and 3 say the set of surviving Kummer levels is *cofinite*. That measures how **cheap** the condition is, not how strong — and here the cofiniteness is elementary arithmetic: only $n \in \{1, 2, 3, 6\}$ divide $-6$, so the obstruction persists at every other level for no reason having to do with fluid dynamics. (The analogous statement for the substrate *parameter* $q$ — a nonzero polynomial obstruction has cofinite non-vanishing locus — is a parallel fact over a different index set, not the same one, and does not support the level-indexed claim.) A cheap condition cannot **by itself** be equivalent to a uniform statement without collapsing the equivalence.

Consequently "persistently nonzero" is **not** by itself evidence that the NS obstruction is a faithful regularity criterion. It is the Navier--Stokes instance of the barrier the $\mathrm{P}$ versus $\mathrm{NP}$ leg already records ([$\mathrm{P} \neq \mathrm{NP}$ at non-torsion $q$](#conj:qou-p-neq-np)) \cite{aaronsonwigderson2009,grochow2017}. The blow-up conclusion that consumes this proposition ([the Descartes universe is NS-singular](#thm:ns-singularity-descartes)) inherits the caveat — as that block already says for the separate categorical-to-classical bridge, the QOU-internal verdict is not a resolution of the classical regularity problem.

Note also that the divisibility structure is what makes the verdict level-dependent: at $\chi_{\mathrm{eu}}(\mathcal{S}) = -6$ the obstruction *vanishes* at levels $n \in \{1, 2, 3, 6\}$ while persisting at all others. Different restrictions of $\kappa_0$ therefore carry different verdicts at once, and the shared class transfers nothing between the Millennium legs.

The regularity content therefore sits in the filtration — whether the vortex-knot complexity stays bounded ([one length filtration, three problems](#rem:skein-filtration-trichotomy)) — not in the non-vanishing of the class alone.

**Proof.**

**(a) Divisibility of the Euler class.**

Constrained over a closed orientable surface $\Sigma_g$ anchored at genus $g$: $H^2(\Sigma_g, \mathbb{Z}) \cong \mathbb{Z}$. Under the hypothesis on $\xi$, the Euler class evaluates to $e(\xi)[\Sigma_g] = \chi_{\mathrm{eu}}(\Sigma_g) = 2 - 2g \in \mathbb{Z}$. Therefore:

$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n \mid \chi_{\mathrm{eu}}(\mathcal{S}).
$$

Applied to the Descartes universe at $\chi_{\mathrm{eu}}(\mathcal{S}) = -6$, the valid divisors restrict strictly to $\{1, 2, 3, 6\}$. $\kappa_0 \bmod n$ mathematically zeroes out only spanning $n \in \{1, 2, 3, 6\}$. It rigorously evades zero for all other $n$ (verifiably holding for $n = 5, 7, 11, 13, \ldots$).

**(b) Obstruction persistence.**

Evaluating at the root of unity $q = e^{i\pi/\kappa}$, the operating Kummer level isolates strictly to $n = 2\kappa$ (reflecting the exact order mapping $q$ inside $\mathbb{G}_m$). The functional obstruction $\kappa_0 \bmod 2\kappa$ reduces to:

$$
  \kappa_0 \bmod 2\kappa = 0
  \quad\Longleftrightarrow\quad
  2\kappa \mid \chi_{\mathrm{eu}}(\mathcal{S}).
$$

For $\chi_{\mathrm{eu}}(\mathcal{S}) = -6$, $2\kappa \mid 6$ permits exclusively $\kappa \in \{1, 3\}$, corresponding to $q = e^{i\pi}$ or $q = e^{i\pi/3}$. At every other valid $\kappa$ (universally capturing all $\kappa \geq 4$), the obstruction fundamentally **persists** squarely at that root of unity.

*Scope of (b).* The identification of the order of the root of unity $q$ with the Kummer level $n$ of the Reeb bundle is asserted, not derived; the arithmetic $2\kappa \nmid 6$ for $\kappa \notin \{1, 3\}$ holds independently of it. The class $\kappa_0 \bmod n$ is a global class on $\mathcal{S}$: its restriction to a one-dimensional locus lies in $H^2(\Sigma, \mu_n) = 0$.

**(c) The limit as kappa goes to infinity.**

Pushing $\kappa \to \infty$ ($q \to 1$) forces $2\kappa \to \infty$. Consequently, $2\kappa \nmid 6$ governs unconditionally for all $\kappa \geq 4$. The math yields:

$$
  \kappa_0 \bmod 2\kappa  \neq  0
  \qquad\text{for all } \kappa \geq 4.
$$

The topological component driving the NS obstruction **rigorously avoids vanishing** through the $q \to 1$ classical limit. Items 1–3 follow: the vanishing set is exactly $\{n : n \mid \chi_{\mathrm{eu}}(\mathcal{S})\}$, finite and complementary to the infinitely many levels where $\kappa_0 \bmod n \neq 0$.
