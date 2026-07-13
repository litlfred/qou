<!-- FILE_START: archimedean-condition-genus-intro.md -->
Having identified the lepton spectrum and chirality assignment, we now determine which closed-braid generators populate the maximally-descended genus, and establish the completeness of this generation system. This completeness serves as the anchor for the lepton-spectrum derivation.
<!-- FILE_END: archimedean-condition-genus-intro.md -->

<!-- FILE_START: torus-knot-generators.md -->
The Euler characteristic $\chi(A) = -6$ forces torus knots to serve as the generators of the particle spectrum. Because Bring's surface has genus $g = 4$, any $T_{m,n}$ whose Seifert genus exceeds $4$ cannot embed. This constraint selects a finite, enumerable generator set $\mathcal{G}$ whose cardinality is entirely determined by $\chi$.

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with $\chi(A) = -6$. The torus knot $T_{m,n}$ with $\gcd(m,n) = 1$ and $m < n$ embeds into the Seifert genus-$g$ surface only if:
$$
  g(T_{m,n}) =  \frac{(m-1)(n-1)}{2}  \leq  g(A) =  4.
$$
The constraint $(m-1)(n-1) \leq 8$ admits exactly six coprime pairs with $m \geq 2$. Together with the unknot $T_{1,0} = 0_1$, the generator set has $|\mathcal{G}| = 7$.
<!-- FILE_END: torus-knot-generators.md -->

<!-- FILE_START: torus-knot-generators-interpretation.md -->
1. **Lepton generations.** Charged leptons correspond to $T_{2,3}$ (electron), $T_{2,5}$ (muon), and $T_{2,7}$ (tau) at Reeb degrees $1, 2, 3$. Only the first two are $S_5$-equivariant; the tau embeds topologically but breaks its $\mathbb{Z}_7$ symmetry. $T_{2,9}$ saturates $g = 4$ (symmetry-broken), and $T_{2,11}$ is genus-excluded, precluding a fourth generation.
2. **Quark sector.** The $(3,n)$-family generators $T_{3,4}$ and $T_{3,5}$ act as $H^{0,1}$ force carriers. $T_{3,4}$ encodes Hopf-squared color binding, while $T_{3,5}$ mediates the weak interaction. The three-strand meridional winding resonantly threads the three color tubes.
3. **Saturation.** The seventh generator $T_{2,9}$ at genus $4$ exactly saturates Bring's surface. New particle types would require composite construction via linking operations.
4. **Hyperbolic knots.** The figure-eight $4_1$ and three-twist $5_2$ are not generators. They arise from Skein crossing changes applied to linked torus-knot configurations, inheriting nonzero hyperbolic volume and bare mass from the linking process.

The bound $N(\chi) = 1 - \chi = 7$ on the number of generators equals the number of handles ($g = 4$) plus the three independent Seifert genus values available within them. The recursive brane tower does not increase the genus, making the generator count stable across all levels.
<!-- FILE_END: torus-knot-generators-interpretation.md -->

<!-- FILE_START: embeddability-closure.md -->
Let $(\mathbf{C}, A, \tau)$ be the Descartes universe with $\chi(A) = -6$ and fiber genus $g(\Sigma_4) = 4$. Let $K$ be any knot type appearing as a component of a link produced by a finite sequence of Hopf linkings $\ell_H$, color-tube threadings $\ell_c$, and Skein crossing changes $\sigma$ applied to generators in $\mathcal{G}$. Then:
1. The Seifert genus of $K$ satisfies $g(K) \leq 4$.
2. $K$ admits a localized knot structure $(c, K) \in \mathrm{Hom}(\mathbf{1}, A^{\mathrm{co}T}) \times \mathrm{Knot}$ at some point $c$.
3. The localized knot $(c, K)$ descends under $\tau$ to an observable morphism in $\mathbf{C}$: every generated particle interacts with every other generated particle via the categorical braiding.

No generated knot is "dark"—the generation scheme is closed under observability.

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
Terms with $g > 4$ lie in the kernel of the mass functional $\mathcal{M}$. The physical mass receives contributions only from embeddable terms. Every knot in the standard dictionary has $g(K) \leq 4$. Skein descendants like $4_1$ typically exhibit lower genus than their parent generators.
<!-- FILE_END: embeddability-closure.md -->

<!-- FILE_START: embeddability-closure-interpretation.md -->
Because every knot type produced by generation remains embeddable in the genus-$4$ fiber, all fundamental particles interact. They all descend to the same base manifold and participate in categorical braiding. A hypothetical genus-$5$ particle would be unobservable and have zero coupling to other particles. The $\chi = -6$ constraint thus guarantees a self-consistent, fully interacting particle spectrum with no dark sectors.
<!-- FILE_END: embeddability-closure-interpretation.md -->

<!-- FILE_START: genus-from-hecke-completeness.md -->
The minimum genus at which the torus-knot evaluations span a $5$-dimensional Iwahori--Hecke representation $H_2(q) \oplus H_3(q)$ is $g_{\min} = 4$. Equivalently, the count of embeddable torus knots $T_{r,s}$ with $r \in \{2, 3\}$ first reaches or exceeds $5$ at genus $g = 4$.
<!-- FILE_END: genus-from-hecke-completeness.md -->

<!-- FILE_START: chebyshev-degree-genus.md -->
Let $a_n \in \mathbb{Z}[s]$ be the Hecke recurrence $a_{n+1} = s\,a_n + a_{n-1}$ with $a_0 = 0$, $a_1 = 1$, and let $u = s^2$. For odd $n = p$, $\deg_u a_p = (p-1)/2 = g(T_{2,p})$, and the leading coefficient of $a_p$ in $u$ is $1$.
<!-- FILE_END: chebyshev-degree-genus.md -->

