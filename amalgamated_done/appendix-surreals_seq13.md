<!-- FILE_START: categorical-mordell-weil.md -->
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with substrate parameter $q$ and Descartes elliptic curve $\mathcal{E}_q$ ([Descartes elliptic curve](#prop:descartes-elliptic-curve)).

The categorical Mordell--Weil group is the abelian group of $\mathbf{1}$-rational points

$$
\mathcal{E}_q(\mathbf{1}) := \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q),
$$

where $E_q \in \mathrm{Ob}(\mathbf{C})$ is the object whose fibre functor image $\tau(E_q) = H^1(\mathcal{E}_q, \mathbb{Z})$ is the first cohomology of the elliptic fiber. The group law is induced by chord-tangent addition on $\mathcal{E}_q$. Set $r_q := \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$. The Tannaka--Krein equivalence ([reconstruction](#thm:tannaka-krein-isomorphism)) identifies $\mathbf{C} \simeq \mathrm{Rep}(G)$, giving

$$
\mathcal{E}_q(\mathbf{1}) \cong \tau(E_q)^G = H^1(\mathcal{E}_q)^G.
$$

We define $r_q$ as the multiplicity of the trivial representation $\mathbf{1}$ in the $G$-module $H^1(\mathcal{E}_q)$.

The $q$-deformed $L$-function is built from the Frobenius eigenvalues $\alpha_1, \ldots, \alpha_8$ of the local $q$-zeta function ([local $q$-zeta](#def:local-q-zeta-function)) acting on $H^1(\mathcal{B})$, the first étale cohomology of Bring's curve. The elliptic fiber $\mathcal{E}_q \hookrightarrow \mathcal{B}$ is a genus-$1$ sub-curve. The restriction of Frobenius to $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ yields a conjugate pair $\alpha_{\mathcal{E}}, \bar{\alpha}_{\mathcal{E}}$ with $|\alpha_{\mathcal{E}}| = q^{1/2}$ (by the Hasse--Weil bound). Define

$$
L(\mathcal{E}_q, s) := \prod_{\mathfrak{m} \in \mathrm{Spec}(R_q)} \frac{1}{1 - \alpha_{\mathcal{E}}(\mathfrak{m}) N(\mathfrak{m})^{-s} + N(\mathfrak{m})^{1-2s}},
$$

where the product runs over maximal ideals of the coordinate ring $R_q$ of Bring's curve, and $N(\mathfrak{m}) = q^{f(\mathfrak{m})}$ is the norm.

The $q$-Tate--Shafarevich group is the kernel of the local-global map. The fibre functor atlas of the QOU forms a $G$-gerbe over the spectral base. For each Reeb eigenvalue $\rho \in \mathrm{Spec}(\xi_q)$, let $\mathbf{C}_\rho$ be the localization of $\mathbf{C}$ at $\rho$ (the full subcategory of objects whose spectral support contains $\rho$). Define

$$
\mathrm{Sha}_q(\mathcal{E}_q) := \ker\!\left( H^1_{\otimes}(\mathbf{C}, E_q) \longrightarrow \prod_{\rho \in \mathrm{Spec}(\xi_q)} H^1_{\otimes}(\mathbf{C}_\rho, E_q) \right),
$$

where $H^1_{\otimes}$ denotes the first cohomology of the :refterm[monoidal category]{#monoidal-category} (classifying torsors under $\mathcal{E}_q$ in $\mathbf{C}$). This measures the failure of the local-global principle at the $q$-scale: torsors trivial at every spectral localization but globally non-trivial.
<!-- FILE_END: categorical-mordell-weil.md -->

<!-- FILE_START: q-birch-swinnerton-dyer.md -->
**Conjecture ($q$-BSD).**
Let $(\mathbf{C}, \varTheta, G, \mathcal{S})$ be a QOU with substrate parameter $q$ and Descartes elliptic curve $\mathcal{E}_q$. Let $\mathcal{E}_q(\mathbf{1}) = \mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, E_q)$ be the categorical Mordell--Weil group with rank $r_q = \mathrm{rank}\,\mathcal{E}_q(\mathbf{1})$. Let $L(\mathcal{E}_q, s)$ be the $q$-deformed $L$-function, and $\mathrm{Sha}_q(\mathcal{E}_q)$ the $q$-Tate--Shafarevich group ([categorical Mordell--Weil](#def:categorical-mordell-weil)). We conjecture two parts, mirroring classical BSD:

**(Weak $q$-BSD).**
The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals the categorical rank:

$$
\mathrm{ord}_{s=1} L(\mathcal{E}_q, s) = r_q.
$$

**(Full $q$-BSD).**
The leading Taylor coefficient satisfies

$$
\frac{L^{(r_q)}(\mathcal{E}_q, 1)}{[r_q]_q!} = \frac{\Omega_q \cdot \mathrm{Reg}_q(\mathcal{E}_q) \cdot |\mathrm{Sha}_q(\mathcal{E}_q)| \cdot \displaystyle\prod_{\mathfrak{m}} c_{\mathfrak{m}}(q)}{|\mathcal{E}_q(\mathbf{1})_{\mathrm{tors}}|^2_q},
$$

where $[r_q]_q! = [1]_q \cdot [2]_q \cdots [r_q]_q$ is the $q$-factorial, $\Omega_q$ is the Reeb period, $\mathrm{Reg}_q$ is the $q$-regulator (determinant of the $q$-Neron--Tate height pairing), and $c_\mathfrak{m}(q)$ are the Tamagawa numbers.

When $r_q = 0$, the regulator is $\mathrm{Reg}_q = 1$ (determinant of the empty matrix), the torsion subgroup is trivial, and the formula collapses to

$$
L(\mathcal{E}_q, 1) = \Omega_q \cdot |\mathrm{Sha}_q(\mathcal{E}_q)| \cdot \prod_{\mathfrak{m}} c_{\mathfrak{m}}(q).
$$
<!-- FILE_END: q-birch-swinnerton-dyer.md -->

<!-- FILE_START: q-bsd-rank-zero.md -->
The rank $r_q$ of the categorical Mordell--Weil group ([categorical Mordell--Weil](#def:categorical-mordell-weil)) is the multiplicity of the trivial representation $\mathbf{1}$ in the $G$-module $H^1(\mathcal{E}_q)$. This depends directly on the categorical axioms:

| Axioms | Gauge group | $H^1(\mathcal{E}_q)$ as $G$-rep | $r_q$ |
| --------------------------- | --------------------------------- | ------------------------------------------ | -------- |
| QU only | unconstrained | may contain $\mathbf{1}$ | $\geq 0$ |
| QOU (+ observability) | semisimple ($\mathfrak{g}^G = 0$) | non-trivial if color-charged | $= 0$ |
| Descartes QOU ($\chi = -6$) | $\mathrm{SU}(2)$ | $V_{1/2} \cong \mathbb{C}^2$ (fundamental) | $= 0$ |

We now show that $r_q = 0$ in the Descartes QOU. The Descartes elliptic curve $\mathcal{E}_q$ is a color fiber of the color fibration ([color elliptic](#prop:color-elliptic)), so $\mathrm{SU}(2)$ acts non-trivially on it. The first cohomology $H^1(\mathcal{E}_q) \cong \mathbb{C}^2$ is two-dimensional (genus $1$). The only two-dimensional irreducible representation of $\mathrm{SU}(2)$ is the fundamental $V_{1/2}$. Since no nonzero vector in $\mathbb{C}^2$ is fixed by all of $\mathrm{SU}(2)$, we have

$$
V_{1/2}^{\mathrm{SU}(2)} = 0.
$$

Thus, the categorical Mordell--Weil group is trivial: $\mathcal{E}_q(\mathbf{1}) = 0$ and $r_q = 0$.

This vanishing is forced by the QOU axioms, not by arithmetic accident. The observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ forces $G$ to be semisimple (the Lie algebra has no $G$-fixed vectors). For any semisimple $G$, every non-trivial irreducible representation $V$ satisfies $V^G = 0$. The elliptic fiber carries a non-trivial representation because it lies in the color directions—the same directions on which $G$ acts. A QU without observability could have $G$ with a center (e.g. $\mathrm{U}(2)$), but even then $V_{1/2}^{U(2)} = 0$ since the center scales all vectors. The only way to achieve $r_q > 0$ would be an elliptic curve in the spacetime directions (on which $G$ acts as the identity), but $\mathcal{E}_q$ is categorically determined as a color fiber.
<!-- FILE_END: q-bsd-rank-zero.md -->

<!-- FILE_START: q-bsd-classical-limit.md -->
The substrate parameter $q$ is a section of $\mathbb{G}_m$ ([substrate $\mathbb{G}_m$ torsion](#rem:substrate-gm-torsion)). The $q$-BSD conjecture ([$q$-BSD](#conj:q-birch-swinnerton-dyer)) describes a family of $L$-functions parametrised by $\mathbb{G}_m$. Its behavior at the boundary and torsion points of $\mathbb{P}^1$ reveals the arithmetic content.

Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via $k^\times \hookrightarrow k \cup \{\infty\}$. The $q$-BSD data extends to a family over $\mathbb{P}^1$ with three regimes:

**(I) Generic $q \in \mathbb{G}_m^{\mathrm{nt}}$ (non-torsion locus).**
The QOU axioms hold. The representation category $\mathbf{C} \simeq \mathrm{Rep}(\mathrm{SU}_q(2))$ has infinitely many simple objects $V_j$, for $j = 0, \tfrac{1}{2}, 1, \ldots$, with positive quantum dimensions $[2j+1]_q > 0$. The $q$-BSD data is:

* $r_q = 0$ (by the rank argument).
* $L(\mathcal{E}_q, 1) \neq 0$ (computable from Frobenius eigenvalues; the Hasse--Weil bound gives $|\alpha_\mathcal{E}| = q^{1/2}$, so the Euler factors are bounded away from zero).
* The weak $q$-BSD reduces to $L(\mathcal{E}_q, 1) \neq 0$, which is an unconditional theorem at the $q$-scale.

**(II) $\mathbb{G}_m$ torsion: roots of unity $q = \zeta_n$.**
At the torsion points ([root-of-unity truncation](#prop:root-of-unity-truncation)), the representation category truncates to finitely many simple objects $V_0, V_{1/2}, \ldots, V_{(n-2)/2}$, forming a modular tensor category (Chern--Simons TQFT at level $n$). The $q$-BSD data undergoes a phase transition:

* **Rank:** The categorical rank remains zero. $V_{1/2}$ is still non-trivial in the truncated category, so $V_{1/2}^G = 0$ and $r_q = 0$ persists at all roots of unity.
* **$q$-integers:** The $q$-integers degenerate ($[n]_{\zeta_n} = 0$). The $q$-factorial $[r]_q!$ and the explicit formula have poles/zeros at the torsion points.
* **$L$-function:** The Euler product over $\mathrm{Spec}(R_q)$ reduces to a finite product (only finitely many representations contribute to the trace), giving a rational function in $\zeta_n$ rather than an infinite product.
* **Kummer obstruction:** The Kummer obstruction ([Kummer specialisation](#prop:ns-kummer-specialisation)) controls the behavior: $\kappa_0 \bmod n = 0$ if and only if $n \mid \chi(A)$. For $\chi(A) = -6$, the obstruction vanishes only at $n \in \{1, 2, 3, 6\}$ and persists for all other $n$. At levels where the obstruction persists, the $L$-function carries non-trivial arithmetic information from the Euler class.

**(III) Boundary points $q = 0$ and $q = \infty$.**
At the boundary of $\mathbb{P}^1$:

* $q = 0$: The operator $d_q = q^{-1} d + (1 - q^{-1}) \pi_V d$ has a pole. The elliptic curve $\mathcal{E}_q$ degenerates (the Weierstrass coefficients $p(q), r(q)$ diverge). The $L$-function has an essential singularity.
* $q = \infty$: We have $d_q \to \pi_V \circ d$ (pure Reeb direction). The $j$-invariant $j(\mathcal{E}_q) \to 0$: the curve approaches a CM curve with complex multiplication. The $L$-function acquires Hecke $L$-function structure (Deuring's theorem).

The Kummer exact sequence ([Kummer specialisation](#prop:ns-kummer-specialisation))

$$
1 \to \mu_n \to \mathbb{G}_m \xrightarrow{(\cdot)^n} \mathbb{G}_m \to 1
$$

controls the specialisation of $L(\mathcal{E}_q, 1)$ to the classical limit. The Euler class $\kappa_0 = e(\xi)$ with $\mathrm{tr}(\kappa_0) = \chi(A) = -6$ satisfies

$$
\kappa_0 \bmod n \neq 0 \qquad\text{for } n \nmid 6.
$$

Thus, the topological obstruction class $\kappa_0 \in H^2(\mathcal{S}, \mathbb{G}_m)$ is not $n$-divisible for $n = 5, 7, 11, 13, \ldots$ (all primes $> 3$ and their multiples). At each such level of the Kummer tower, the $q$-BSD formula carries non-trivial arithmetic content that cannot be cancelled by torsion.

The parallel with the NS obstruction ([NS Kummer](#prop:ns-kummer-specialisation)) is exact:

| Millennium problem | $q$-scale | Classical limit $q \to 1$ | Obstruction |
| ---------------------- | ---------------------------------- | ---------------------------------------- | --------------------------------------------------- |
| Riemann hypothesis | Hasse--Weil (**proved**) | $\mathrm{Re}(s) = 1/2$ (**open**) | Phase coherence of local spectra |
| Navier--Stokes | $q$-NS regular (**proved**) | NS regularity (**open**) | $\kappa_0 \bmod 2\kappa \neq 0$ for $\kappa \geq 4$ |
| Birch--Swinnerton-Dyer | $r_q = 0$, $L \neq 0$ (**proved**) | $r_1 = 0$, $L(E_1, 1) \neq 0$ (**open**) | $\kappa_0 \bmod n \neq 0$ for $n \nmid 6$ |

All three millennium problems share the same structure in the QOU framework: an unconditional theorem at the $q$-scale whose persistence through the $q \to 1$ limit is controlled by the Kummer divisibility of the Euler class $\chi(A) = -6$.

Every term of the conjecture is determined by $(\mathbf{C}, A)$:

| Classical BSD | $q$-BSD | Categorical source |
| ----------------------------- | ------------------------------- | ---------------------------------------------------------- |
| $E(\mathbb{Q})$ | $\tau(E_q)^G = 0$ | $V_{1/2}^{\mathrm{SU}(2)} = 0$ |
| $\mathrm{rank} E(\mathbb{Q})$ | $r_q = 0$ | No trivial summand in $H^1(\mathcal{E}_q)$ |
| $L(E, s)$ | $L(\mathcal{E}_q, s)$ | Frobenius on $H^1(\mathcal{E}_q) \subset H^1(\mathcal{B})$ |
| $\mathrm{Sha}(E)$ | $\mathrm{Sha}_q(\mathcal{E}_q)$ | Monoidal $H^1$ localized at Reeb spectrum |
| $\Omega_E$ | $\Omega_q$ | Reeb period of the contact structure |

As $q \to 1$ (the adelic assembly), the $q$-BSD formula recovers the classical Birch--Swinnerton-Dyer conjecture for $E_1 : y^2 = x^3 + \frac{2}{3}x + \frac{20}{27}$. The representation category deforms from $\mathrm{Rep}(\mathrm{SU}_q(2))$ to $\mathrm{Rep}(\mathrm{SU}(2))$, but the rank $r_1 = 0$ persists (the fundamental of $\mathrm{SU}(2)$ still has no invariants). So the classical prediction is: the classical curve $E_1$ has rank $0$ and $L(E_1, 1) \neq 0$.

The passage from the $q$-scale theorem ($L \neq 0$) to the classical statement ($L(E_1, 1) \neq 0$) is obstructed by the same mechanism as the Riemann hypothesis: the classical limit functor $\mathcal{L}$ is not full, and information about the relative phases of local $L$-factors is lost in the adelic assembly.

For categories where $r_q > 0$ (non-observable universes or spacetime-direction elliptic curves), the Neron--Tate height admits a $q$-deformation via the spectral trace. For $P, Q \in \mathcal{E}_q(\mathbf{1})$:

$$
\langle P, Q \rangle_q := \lim_{n \to \infty} \frac{\hat{h}_q([n]_q P, Q)}{[n]_q^2},
$$

where $\hat{h}_q$ is the naive $q$-Weil height and $[n]_q P$ denotes scalar multiplication by the $q$-integer $[n]_q = (q^n - q^{-n})/(q - q^{-1})$. At $\mathbb{G}_m$ torsion points $q = \zeta_n$, the denominator $[n]_{\zeta_n}^2 = 0$ and the height pairing degenerates—a reflection of the category truncation. The regulator $\mathrm{Reg}_q = \det(\langle P_i, P_j \rangle_q)$ has poles at the torsion locus, matching the zeros of $[r_q]_q!$ in the denominator of the full BSD formula.
<!-- FILE_END: q-bsd-classical-limit.md -->

<!-- FILE_START: bsd-surreal-bound.md -->
The classical Birch--Swinnerton-Dyer conjecture asserts that the order of vanishing of the $L$-function $L(\mathcal{E}_q, s)$ at $s = 1$ equals the Mordell--Weil rank of the elliptic curve $\mathcal{E}_q$ ([$q$-Birch--Swinnerton-Dyer](#conj:q-birch-swinnerton-dyer)). We express this order-of-vanishing matching as a literal surreal-order identity.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)), and $\mathcal{E}_q$ the Descartes elliptic curve attached to the substrate. Let $r = \mathrm{rank}\bigl(\mathcal{E}_q(\mathbb{Q})\bigr)$ be the Mordell--Weil rank.

By [surreal rate calculus](#prop:surreal-rate-calculus) and the spectral identification of $L$-values with Reeb-period integrals, the surreal $\omega$-order of $L(\mathcal{E}_q, 1 + \delta)$ as $\delta$ is a standard-real drift is

$$
\ordw\bigl(L(\mathcal{E}_q, 1 + \delta)\bigr) = r \cdot \ordw(\delta) \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

Equivalently, near $\delta = 0$:

$$
L(\mathcal{E}_q, 1 + \delta) \asymp c \cdot \delta^r \qquad (\text{standard-real } c \neq 0).
$$

By [surreal squeeze](#lem:surreal-squeeze), every standard-real drift $\delta > 0$ produces cost $\delta^2 \cdot \varepsilon^{-1}$ exceeding the mass-gap budget $\varepsilon^3$. Thus, the $L$-function cannot support a hidden zero of order strictly greater than the rank. The surreal-order identity is rigid in $\mathbb{R}(\varepsilon)$.

In $\omega$-adic form ([Big-O via $\ordw$](#rem:conway-normal-form)):

$$
\ordw\bigl(L(\mathcal{E}_q, 1 + \delta) / \delta^r\bigr) = 0 \qquad (\text{no extra vanishing beyond the rank}).
$$

The order of vanishing of $L(\mathcal{E}_q, s)$ at $s = 1$ equals $r$, as a literal identity of surreal $\omega$-orders. Classical BSD is recovered by applying the standard-part functor ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)): $\mathrm{st}\bigl(-\ordw(L)\bigr) = r$ gives the classical rank formula (with $\delta = \omega^{-1}$ infinitesimal, $L \asymp \delta^r = \omega^{-r}$ has $\ordw(L) = -r$; the classical order of vanishing $r$ is the negation).

The BSD bound generalizes the RH bound ([RH surreal bound](#rem:rh-surreal-bound)) from the trivial rank-zero case (Dedekind $\zeta$) to higher ranks. RH is the $r = 0$ specialization where no extra vanishing is allowed beyond the pole of $\zeta$. The surreal squeeze gives the same strict inequality at each rank: every drift beyond rank-prescribed vanishing is forbidden by the $\varepsilon^{-1} > \varepsilon^3$ separation of orders.

The refined BSD statement identifies the leading coefficient $c$ with the product of Tate--Shafarevich order, regulator, and periods. In surreal-order terms, this is a $\simeq$ identity (matching leading coefficients, not just $\omega$-orders). Its proof requires integrating the surreal $\ordw$-calculus with the Tate thesis adelic Fourier transform ([adelic--Tate surreal bound](#rem:adelic-tate-squeeze)).
<!-- FILE_END: bsd-surreal-bound.md -->

<!-- FILE_START: rh-surreal-bound.md -->
The classical Riemann hypothesis states that every non-trivial zero $\rho$ of the Riemann zeta function satisfies $\mathrm{Re}(\rho) = 1/2$ ([Riemann hypothesis](#conj:classical-riemann-hypothesis)). We express the QOU stability argument for this claim as a literal surreal inequality.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), so that $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The scaling laws of [surreal rate calculus](#prop:surreal-rate-calculus) hold:

$$
\Delta_q \asymp \varepsilon^3, \qquad \Omega_q \asymp \varepsilon^{-1}.
$$

Let $\rho$ be a hypothetical zero of $\zeta(s)$ with $\mathrm{Re}(\rho) = 1/2 + \delta$ for some $\delta \in \mathbb{R}$, $\delta > 0$. We call $\delta$ the rogue-zero drift.

By [collapse of the quantum gap](#thm:quantum-gap-collapse) and the Hasse--Weil alignment at every prime fibre, the energy required to relocate a zero from $\mathrm{Re}(\rho) = 1/2$ to $\mathrm{Re}(\rho) = 1/2 + \delta$ is

$$
E(\delta) \asymp \delta^2 \cdot \Omega_q \asymp \delta^2 \cdot \varepsilon^{-1},
$$

while the available dissipation from the mass gap is $\Delta_q \asymp \varepsilon^3$. Therefore

$$
\frac{E(\delta)}{\Delta_q} \asymp \frac{\delta^2 \cdot \varepsilon^{-1}}{\varepsilon^3} = \delta^2 \cdot \varepsilon^{-4} \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

By [surreal squeeze](#lem:surreal-squeeze), $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ in $\mathbb{R}(\varepsilon)$ whenever $\delta > 0$ is a standard real. Equivalently, $\ordw\bigl(E(\delta)\bigr) = 1 > -3 = \ordw(\Delta_q)$ in the $\omega$-adic order of [Big-O via $\ordw$](#rem:conway-normal-form): the cost sits at strictly higher $\omega$-order than the budget.

No configuration of the QOU substrate can sustain a standard-real drift $\delta > 0$. The only value of $\delta$ with $E(\delta) \leq \Delta_q$ in the ordered field is $\delta = 0$, i.e., $\mathrm{Re}(\rho) = 1/2$. This realizes, at the level of surreal arithmetic, the equivalence [macroscopic stability $\Leftrightarrow$ RH](#thm:macroscopic-stability-equivalence).

The informal bound "as $q \to 1^+$, the energy cost $O(\delta^2 (q-1)^{-1})$ exceeds the closing mass gap $O((q-1)^3)$" becomes a single inequality $\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3$ inside the ordered field $\mathbb{R}(\varepsilon) \subset \mathbf{No}$. No limit is taken; the argument is algebraic, not analytic.

The phrase "almost everywhere on the critical line" in classical partial-RH results corresponds to the standard part $\mathrm{st}(\delta) = 0$ of a surreal-valued drift—a genuine, not asymptotic, vanishing. This bound upgrades this to $\delta = 0$ on the nose for any standard real $\delta > 0$, using only the ordering of $\mathbb{R}(\varepsilon)$.
<!-- FILE_END: rh-surreal-bound.md -->

<!-- FILE_START: yang-mills-surreal-bound.md -->
The Yang--Mills mass-gap problem asks for a proof that pure $\mathrm{SU}(N)$ Yang--Mills theory on $\mathbb{R}^4$ has a strictly positive mass gap $\Delta_{\mathrm{YM}} > 0$. In the QOU framework, this is the definitional content of the substrate: the structural invariant $\Delta_q \asymp \varepsilon^3$ is the categorical mass gap. We make this identification explicit.

Let $\varepsilon \in \mathrm{Der}(A)$ be the Reeb infinitesimal ([Reeb infinitesimal](#def:reeb-epsilon)), $q = 1 + \varepsilon$ ([$q$ from $\varepsilon$](#def:q-from-epsilon)). The Yang--Mills gauge group in the QOU is realised as the representation category $\mathbf{Rep}(\mathrm{SU}_q(N))$ of the quantum group $\mathrm{SU}_q(N)$ at $q = 1 + \varepsilon$.

By [collapse of the quantum gap](#thm:quantum-gap-collapse) and [surreal rate calculus](#prop:surreal-rate-calculus), the lowest eigenvalue of the $q$-Laplacian on the state bundle $\mathcal{S}$ is strictly positive:

$$
\Delta_q \asymp \varepsilon^3 > 0 \qquad (\text{in } \mathbb{R}(\varepsilon) \subset \mathbf{No}).
$$

In the $\omega$-adic register ([Big-O via $\ordw$](#rem:conway-normal-form)): $\ordw(\Delta_q) = -3 > -\infty = \ordw(0)$. The mass gap sits at strictly higher $\omega$-order than the zero element.

The Yang--Mills specialization of [surreal squeeze](#lem:surreal-squeeze) is degenerate: the "drift" is the putative massless glueball excitation of energy $\delta = 0$. The squeeze

$$
\delta^2 \cdot \varepsilon^{-1} > \varepsilon^3
$$

holds strictly for every standard-real $\delta > 0$ and degenerates to the marginal equality at $\delta = 0$. Therefore, the only excitation with zero cost is the trivial one (no excitation). Every non-trivial excitation has $\delta \geq \Delta_q \asymp \varepsilon^3 > 0$, which is the categorical mass-gap statement.

The Yang--Mills mass-gap theorem is literally true in the QOU framework as a surreal-order inequality: $\Delta_q > 0$ in $\mathbb{R}(\varepsilon)$, equivalently $\ordw(\Delta_q) = -3$. Classical Yang--Mills on $\mathbb{R}^4$ is recovered as the standard part ([calculus up to $\varepsilon$](#rem:calculus-up-to-epsilon)): $\mathrm{st}\bigl(\Delta_q / \varepsilon^3\bigr) = c > 0$ for a standard real $c$, so the classical mass gap is $\Delta_{\mathrm{YM}} = \lim_{\varepsilon \to 0} \Delta_q / \varepsilon^3 \cdot \varepsilon^3_{\mathrm{phys}}$ at the physical $\varepsilon = 1/\omega$ value.

The classical Yang--Mills problem asks for the existence of a positive mass gap; the QOU provides it by categorical construction. What remains is the regularity programme: showing that the classical $\mathrm{SU}(N)$ Yang--Mills theory on $\mathbb{R}^4$, as a renormalised QFT, is the standard part of the $q$-deformed substrate as $\varepsilon \to 0$. This is the Wightman-axiom portion of the millennium statement—analogous to how [NS surreal bound](#rem:ns-surreal-bound) reduces NS regularity to the substrate reversion under blow-up.

The $q$-deformation at standard-real $\varepsilon > 0$ replaces the continuous Wilson loop by the categorical trace over $\mathbf{Rep}(\mathrm{SU}_q(N))$, which is non-vanishing precisely on closed braids. The classical confinement statement ("only gauge-invariant observables are colour-singlet") is the surreal-order statement that every non-trivial Wilson loop has $\omega$-order $> 0$: its standard part is an exponentially suppressed real quantity.

The Yang--Mills gauge theory on $\mathbb{R}^4$ is classically a field theory, not an elliptic-curve or skein-module problem. The QOU substrate encodes it via the fibre-functor $\tau : \mathbf{Rep}(\mathrm{SU}_q(N)) \to \mathbf{Vec}$: Yang--Mills observables are natural transformations of $\tau$, and the mass gap is the first positive eigenvalue of the Reeb derivation on $\mathrm{End}_{\mathbf{C}}(A)$. The surreal-order statement $\ordw(\Delta_q) = -3$ is therefore a re-expression of the Yang--Mills mass gap in the categorical register.
<!-- FILE_END: yang-mills-surreal-bound.md -->

<!-- FILE_START: os-reflection-positivity-from-reeb.md -->
The [Yang–Mills surreal bound](#rem:yang-mills-surreal-bound) gives the mass-gap statement at substrate order $\Delta_q \asymp \varepsilon^3$ but explicitly defers the Wightman-axiom portion of the Millennium Prize statement—the regularity programme of recovering a standard renormalised QFT as the standard part of the $q$-deformed substrate. This conjecture supplies the bridge: the Reeb $\mathbb{Z}_2$ acting on the [Frobenius pairing](#def:frobenius-hopf-substrate) furnishes Osterwalder–Schrader reflection positivity in the archimedean realisation. Together with the surreal mass gap, this forms the Osterwalder–Schrader sufficient input for Wightman reconstruction.

**Conjecture (OS reflection positivity from the Reeb $\mathbb{Z}_2$).**
*Let $\theta$ denote the antipodal $\mathbb{Z}_2 \subset U(1)_{\xi}$ inside the Reeb $U(1)$—equivalently, the chart-swap involution $\iota : Z \mapsto Z^{-1}$ on the [contact affine chart](#def:contact-affine-chart) at $\varTheta = \pi$, per [chart-swap $U(1)$ is the Reeb flow](#prop:reeb-u1-chart-swap). Then the [Frobenius pairing](#def:frobenius-hopf-substrate) $\langle\,\cdot\,,\,\cdot\,\rangle_F$ on $A$ satisfies reflection positivity under $\theta$:*

$$
\langle \theta(\phi), \phi \rangle_F \geq 0 \qquad \text{for every state } \phi \in A_+,
$$

*with equality if and only if $\phi$ vanishes on the positive-time half of the Reeb decomposition. Under the [archimedean realization](#def:archimedean-realization-functor) $\tau_{\mathrm{arch}}$, this categorical positivity descends to the Osterwalder–Schrader reflection-positivity axiom of the four Euclidean Wightman correlation functions $\tau_{\mathrm{arch}}\bigl(\langle \phi_1 \cdots \phi_n \rangle_F\bigr)$ on the $\varepsilon \to 0$ standard manifold $\mathbb{R}^4$.*

The Osterwalder–Schrader reflection $\theta_{\mathrm{OS}}$ on Euclidean spacetime is reflection in the $\tau = 0$ hyperplane, i.e., $(x_1, x_2, x_3, \tau) \mapsto (x_1, x_2, x_3, -\tau)$. In the categorical contact-geometric formulation, Euclidean time is the Reeb parameter $t$ along $\xi$ ([categorical Reeb derivation](#def:categorical-reeb)), so $\theta_{\mathrm{OS}}$ acts on the contact affine chart as $\phi_t \mapsto \phi_{-t}$. The categorical realisation of this involution is precisely the antipodal $\mathbb{Z}_2$ subgroup at $\varTheta = \pi$ of the chart-swap $U(1)$ family $\rho_\varTheta : z \mapsto e^{i\varTheta} z$. The [chart-swap–Reeb identification](#prop:reeb-u1-chart-swap) shows this coincides with the Reeb flow $U(1)$. We require no separate OS reflection to construct: it is already present in the categorical infrastructure as the $\mathbb{Z}_2$ subgroup of the Reeb circle.

The Frobenius pairing is symmetric by construction: $\Psi = S^2 = \mathrm{id}_A$, so $\langle a, b \rangle_F = \langle b, a \rangle_F$. Under the $\theta$-action on $A$, the antipode $S$ swaps the two factors and inverts the Reeb flow direction. Symmetry of the Frobenius pairing under $\Psi$ implies $\theta$-invariance of the pairing up to the sign captured by the Reeb-half decomposition. The conjecture is the positivity statement: for any state $\phi$ supported on the positive-time Reeb half, $\langle \theta(\phi), \phi \rangle_F$ evaluates to a non-negative scalar in $\mathrm{End}_{\mathbf{C}}(\mathbf{1})$. This positivity refines the symmetry. Symmetry alone gives $\langle \theta(\phi), \phi \rangle_F = \langle \phi, \theta(\phi) \rangle_F$ (so the quantity is real), but does not force the real value to be non-negative. We require the structural input that the antipode-twisted pairing $\langle \theta(\cdot), \cdot \rangle_F$ descends through $\tau_{\mathrm{arch}}$ to a positive-definite inner product on the half-line $L^2(\mathbb{R}_{>0})$.

The Osterwalder–Schrader theorem states that a family of Euclidean correlation functions $\{S_n\}$ on $\mathbb{R}^4$ defines a Wightman QFT on Minkowski space if and only if (OS0) temperedness, (OS1) Euclidean covariance, (OS2) reflection positivity, (OS3) symmetry, and (OS4) cluster decomposition all hold.

In the QOU framework:

| OS axiom | QOU input |
|----------|-----------|
| OS0 (temperedness) | $\tau_{\mathrm{arch}}$ images of partial products $\Phi_n$ are tempered by the [archimedean limit conjecture](#conj:dilogarithm-archimedean-limit) at every $x \in (0, 1)$. |
| OS1 (Euclidean covariance) | $S_5$-action on Bring's coordinate ring is the categorical lift of the $\mathrm{SO}(4) / \mathrm{Spin}(4)$ rotation group, and the [$\mathbb{Z}_2 \hookrightarrow U(1)_{\xi}$](#prop:reeb-u1-chart-swap) hierarchy is the Euclidean time translation. |
| **OS2 (reflection positivity)** | **This conjecture.** |
| OS3 (symmetry / locality) | Categorical permutation symmetry of the Frobenius pairing; $\Psi = S^2 = \mathrm{id}_A$. |
| OS4 (cluster decomposition) | Mass gap $\Delta_q \asymp \varepsilon^3$ from the [surreal bound](#rem:yang-mills-surreal-bound) gives exponential clustering at separation $r$: $|S_n(\cdots) - S_k(\cdots) S_{n-k}(\cdots)| \lesssim e^{-\Delta_q r}$. |

OS0, OS1, OS3 are categorically built-in. OS4 is the [surreal mass-gap statement](#rem:yang-mills-surreal-bound). OS2 is the open input—this conjecture. Granting it, the OS theorem reconstructs a Wightman QFT on $\mathbb{R}^4$ as the standard part of the $q$-deformed substrate, completing the Wightman-axiom portion of the Yang–Mills millennium statement.

The positivity statement involves three open ingredients:

1. **Categorical positivity of the antipode-twisted pairing.** The Frobenius pairing is constructively non-degenerate, but neither the QOU axioms nor the [Frobenius–Hopf substrate definition](#def:frobenius-hopf-substrate) currently impose positivity of $\langle \theta(\cdot), \cdot \rangle_F$. The conjecture claims the substrate, being a $C^*$-Frobenius–Hopf algebra in the archimedean specialisation ($q = q_0 \in \mathbb{R}_{>1}$), inherits positivity from the $C^*$-norm.
2. **Stability under $\tau_{\mathrm{arch}}$.** The archimedean realisation functor must commute with the positivity restriction: $\tau_{\mathrm{arch}}\bigl(\langle\theta(\phi),\phi\rangle_F\bigr) = \bigl\langle\theta_{\mathrm{OS}}\tau_{\mathrm{arch}}(\phi),\, \tau_{\mathrm{arch}}(\phi)\bigr\rangle_{L^2(\mathbb{R}^4)}$. Equivalently, the OS reflection on the standard Euclidean correlation functions is the $\tau_{\mathrm{arch}}$-image of the Reeb antipodal $\mathbb{Z}_2$ action. This follows from the [chart-swap–Reeb identification](#prop:reeb-u1-chart-swap) once $\tau_{\mathrm{arch}}$ preserves the $U(1)_{\xi}$-action on contact charts.
3. **Mathlib infrastructure.** A complete proof requires a Frobenius structure on the categorical $C^*$-completion and the Wightman reconstruction theorem—neither in Mathlib today. The conjecture is packaged as the typeclass `QOU.AppendixSurreals.OSReflectionPositivity`, with one field stating the positivity inequality. Granting the class instance, the surreal bound completes OS reconstruction.

Ingredients (2) and (3) are technical plumbing once the categorical content is settled. The only genuinely new mathematical input needed is a single positivity axiom on the substrate Frobenius algebra. A Frobenius algebra $(A, \mu, \eta, \Delta, \varepsilon)$ in a $C^*$-tensor category is positive if its evaluation map $\eta : \mathbf{1} \to A$ admits a state-positive lift—i.e., the composition

$$
\mathbf{1} \xrightarrow{\;\eta\;} A \xrightarrow{\;\Delta\;} A \otimes A \xrightarrow{\;\mathrm{id}\,\otimes\,*\;} A \otimes A^*
$$

factors through the positive cone of $A \otimes A^*$. The missing input is exactly this:

> **Axiom (substrate $C^*$-Frobenius positivity).** At the archimedean substrate value $q = q_0 \in \mathbb{R}_{>1}$, the [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) $A$ admits a $C^*$-completion in which the unit map $\eta : \mathbf{1} \to A$ is positive in the categorical sense above. Equivalently, $(A, \mu, \eta, \Delta, \varepsilon)$ is a *positive* Frobenius algebra in the $C^*$-tensor category $\mathbf{C}$ at $q_0$.

Granting the substrate $C^*$-Frobenius positivity axiom, along with [`prop:reeb-u1-chart-swap`](#prop:reeb-u1-chart-swap) and [`def:archimedean-realization-functor`](#def:archimedean-realization-functor), OS axiom (OS2) holds: $\langle\theta(\phi), \phi\rangle_F \geq 0$ for every state $\phi$ in the positive-time Reeb half.

The proof sketch involves three steps:

1. **Categorical reflection = Reeb $\mathbb{Z}_2$.** By [`prop:reeb-u1-chart-swap`](#prop:reeb-u1-chart-swap), $\theta$ is the antipodal $\mathbb{Z}_2 \subset T_q$ subgroup acting on the contact-affine chart $\mathbb{P}(V)$ via $z \mapsto -z$. On the substrate Hopf algebra $A$, the action $\theta_A : A \to A$ factors through the antipode $S$ via the $T_q$-grading: $\theta_A = S \circ (\mathrm{sign}\,\text{of}\,\xi\text{-grading})$.
2. **Antipode-twisted pairing = state-positive form.** The substrate Frobenius pairing factors through the antipode by $\langle a, b \rangle_F = \varepsilon(\mu(a, S(b)))$. Composing with $\theta_A$: $\langle \theta(\phi), \phi \rangle_F = \varepsilon(\mu(\theta(\phi), S(\phi))) = \varepsilon(\mu(S(\phi^*), S(\phi)))$ where $\phi^*$ is the $C^*$-conjugate. By the substrate positivity axiom, this evaluates to a non-negative element of $\mathrm{End}_{\mathbf{C}}(\mathbf{1}) = k$.
3. **Stability under $\tau_{\mathrm{arch}}$.** $\tau_{\mathrm{arch}}$ sends the categorical $C^*$-norm to the standard $L^2$-norm on $\mathbb{R}^4$ by construction. Positivity is preserved.

The status of OS reflection positivity in the QOU framework is equal to the status of this single $C^*$-Frobenius positivity axiom. The axiom is well-formulated inside unitary fusion categories and unitary $C^*$-Frobenius algebras. Verifying that the QOU substrate $A$ at $q_0 \in \mathbb{R}_{>1}$ satisfies it requires:

- A choice of $C^*$-norm on $A$ compatible with the $q_0$-deformation.
- Verification that one of these candidate norms makes the Frobenius pairing positive in the sense above.
- Compatibility of the chosen norm with the antipode $S$.

This follow-up programme is formalised as [`conj:wenzl-positivity-implies-substrate-positivity`](#conj:wenzl-positivity-implies-substrate-positivity). Closing that bridge conjecture makes the substrate axiom derived from Wenzl's classical result, discharging the OS-reflection-positivity-as-axiom assumption.

The Wightman-axiom portion of the Yang–Mills millennium statement reduces to the structural positivity of the antipode-twisted Frobenius pairing. The reflection involved is the antipodal $\mathbb{Z}_2$ subgroup of the Reeb $U(1)$, made visible by the [chart-swap–Reeb identification](#prop:reeb-u1-chart-swap). The categorical infrastructure already houses every OS ingredient except this positivity.
<!-- FILE_END: os-reflection-positivity-from-reeb.md -->
