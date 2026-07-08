<!-- FILE_START: topological-mass-galois-baryons-intro.md -->
The topological mass formula and its volume-tower transcendence shadow prompt two questions. What structure does the Galois action on this transcendence reveal? How does the bar-self-dual confinement band package the baryon-sector periods?

This section traces the Yekutieli transcendence shadow and the implications of algebraic dependence. It formulates the baryon-period conjecture. It describes the golden-quartet Galois orbit, the Möbius golden fixed points, and the bar-self-dual confinement band. This completes the baryon-sector description and prepares the algebro-geometric PL-SW duality sequence.
<!-- FILE_END: topological-mass-galois-baryons-intro.md -->

<!-- FILE_START: formal-chain-transcendence-remark.md -->
The formal proof chain operates in the Laurent polynomial ground ring $\mathbb{Z}[q, q^{-1}]$. It does not use real-number arithmetic. Hyperbolic volumes enter only through the specialisation $\iota \colon q \mapsto q_0$. They appear as computed invariants verified to $10^{-14}$ precision via SnapPy.

The topological mass formula $\mathfrak{m}(K) = \mathrm{Vol}(K)/\hbar_q^2$ mixes Laurent polynomials in $q$ with hyperbolic volumes. The categorical derivation uses the Hecke algebra, Skein relations, Gröbner--Shirshov normal forms, and transfer matrices. This derivation remains purely algebraic over $\mathbb{Z}[q, q^{-1}]$. It does not depend on whether $\mathrm{Vol}(K)$ is transcendental, algebraic, or irrational.

The algebraic independence conjecture describes the number-theoretic structure of the physical coefficient ring. No result requires this conjecture. If a polynomial relation holds among the volumes, the mass predictions and categorical structure remain valid. Only the algebraic structure of the coefficient ring simplifies. The conjecture asserts exactly that the specialisation map $\iota$ is injective on the extended ring $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)]$.
<!-- FILE_END: formal-chain-transcendence-remark.md -->

<!-- FILE_START: yekutieli-transcendence-shadow.md -->
The [quantum characteristic classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ obstruct lifting at every level of the [cosimplicial crossed groupoid](#prop:cosimplicial-crossed-groupoid). The classes $\kappa_n$ never vanish. The brane tower therefore never collapses to finite height ([Yekutieli lifting](#prop:yekutieli-lifting)).

Each hyperbolic volume $\mathrm{Vol}(K)$ is the classical limit ($q \to 1$) of the quantum dilogarithm sum across the brane tower. A polynomial relation $P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)) = 0$ over $\mathbb{Q}[q, q^{-1}]$ would algebraically constrain the Chern--Simons invariants of the complements $S^3 \setminus 4_1$, $S^3 \setminus 5_2$, and $S^3 \setminus \mathcal{B}_3$. By the Chern--Simons/volume correspondence, this constraint would force holonomy contributions at different tower levels to close up after finitely many levels.

The cosimplicial structure theorem guarantees an infinite tower. The obstruction classes $\kappa_n$ never simultaneously vanish. The crossed groupoid does not degenerate. This realizes [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction). The motivic Galois character of the substrate is non-trivial at every finite place $p \nmid \chi(A)$. The class $\kappa_n$ is the HKR image of that character at level $n$ ([Hochschild–Kummer connection](#rem:hochschild-kummer-connection)). Consequently, $\kappa_n$ cannot vanish at the corresponding cyclotomic levels. The algebraic independence of the volumes is the *transcendence shadow* of the non-vanishing motivic Galois character. The tower never terminates. No polynomial envelope binds the resulting volumes.

Rigorous proof requires controlling the arithmetic of the quantum dilogarithm at every tower level. This control demands new results analogous to Nesterenko's theorem on the algebraic independence of $E$-function values. These results must generalize to quantum dilogarithm series and the cosimplicial filtration of $\mathrm{SU}_q(2)$-gerbes.
<!-- FILE_END: yekutieli-transcendence-shadow.md -->

<!-- FILE_START: implications-algebraic-independence.md -->
Assume the [algebraic independence conjecture](#conj:hyperbolic-volume-transcendence) holds. No non-trivial polynomial $P \in \mathbb{Q}[x, y, z]$ satisfies $P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)) = 0$.

**Mathematical consequences.**

1. **Milnor's conjecture.** The knots $4_1$, $5_2$, and the Borromean link $\mathcal{B}_3$ have pairwise non-commensurable hyperbolic complements. Algebraic independence implies the $\mathbb{Q}$-linear independence predicted by Milnor.

2. **Irrationality.** The volumes $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, $\mathrm{Vol}(5_2)$, and $\mathrm{Vol}(\mathcal{B}_3)$ are individually irrational. 

3. **Bloch--Wigner transcendence.** Each volume takes the form $D(\xi)$ for an algebraic $\xi$ in distinct number fields ($\mathbb{Q}(\sqrt{-3})$, the cubic field of $5_2$, and $\mathbb{Q}(i)$). Independence yields provably transcendental values of the Bloch--Wigner dilogarithm at algebraic arguments.

**Framework consequences.**

1. **Tower non-collapse.** The [bridge theorem](#rem:yekutieli-transcendence-shadow) equates independence with the non-vanishing of all obstruction classes $\kappa_n \neq 0$. The cosimplicial filtration of $\mathrm{SU}_q(2)$-gerbes is strictly infinite.

2. **Confinement.** The hadronic binding energy $\mathfrak{E}_{\mathrm{bind}}$ has no closed-form algebraic reduction. The infinite tower supplies the categorical signature of quark confinement. 

3. **Specialisation.** The evaluation map $\iota \colon \mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)] \to \mathbb{R}$ at $q = q_0$ is injective. The physical coefficient ring equals the formal Laurent polynomial ring.

4. **Bandwidth bounds.** The information-bandwidth bounds $\mathfrak{B}(q)$ are tight.

**Lean formalisation.**
Independence populates the class `QOU.Archimedean.HyperbolicVolumeIndependence`. Constructing an instance requires an arithmetic theorem for the quantum dilogarithm $\mathrm{Li}_2^q$ at algebraic arguments.
<!-- FILE_END: implications-algebraic-independence.md -->

<!-- FILE_START: implications-algebraic-dependence.md -->
Suppose the [algebraic independence conjecture](#conj:hyperbolic-volume-transcendence) fails. A non-trivial polynomial $P \in \mathbb{Q}[x, y, z]$ satisfies $P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)) = 0$.

**Mathematical consequences.**

1. **Milnor's conjecture.** Algebraic dependence is weaker than $\mathbb{Q}$-linear dependence. A dependence polynomial of degree greater than one does not refute Milnor's prediction of $\mathbb{Q}$-linear independence for pairwise non-commensurable hyperbolic $3$-manifolds.

2. **Bloch--Wigner identities.** Each volume takes the form $D(\xi_K)$ for an algebraic $\xi_K$ in distinct number fields. An algebraic dependence yields a $\mathbb{Q}$-polynomial identity among Bloch--Wigner values across $\mathbb{Q}(\sqrt{-3})$, the cubic field of $5_2$, and $\mathbb{Q}(i)$.

3. **Transcendence chain.** The implication chain from independence to Borel--Zagier to single-volume irrationality breaks. Irrationality remains open for each volume. The categorical lever to prove it vanishes.

**Framework consequences.**

1. **Tower collapse.** The contrapositive of the [bridge theorem](#rem:yekutieli-transcendence-shadow) forces an obstruction class $\kappa_n$ to vanish. The cosimplicial filtration terminates at finite depth.

2. **Confinement.** The hadronic binding energy $\mathfrak{E}_{\mathrm{bind}}$ reduces to a finite polynomial expression in $q$. Confinement does not require the infinite-tower structure.

3. **Borromean baryon.** The distinction between the Borromean link $\mathcal{B}_3$ and a sum of Hopf pairs reduces to finite categorical data. The invariant identifying the proton as a three-body configuration is computable without the infinite tower.

4. **Coefficient ring.** The evaluation map $\iota$ is not injective. The physical ring $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)]$ is smaller than the formal Laurent ring admits.

5. **Bandwidth bounds.** The substrate satisfies the information-bandwidth bounds $\mathfrak{B}(q)$ with slack. The topological mass formula, the Gröbner--Shirshov construction, and the spectral predictions remain valid. They reside in $\mathbb{Z}[q, q^{-1}]$ (see [formal chain remark](#rem:formal-chain-transcendence)).

**Lean formalisation.**
Dependence implies the class `QOU.Archimedean.HyperbolicVolumeIndependence` is uninhabited. The conditional theorem `QOU.Archimedean.tower_noncollapse_implies_independence` remains vacuously true. Its hypothesis `QOU.Torsion.YekutieliLiftingCondition` is unsatisfiable.
<!-- FILE_END: implications-algebraic-dependence.md -->

<!-- FILE_START: baryon-product-from-alt.md -->
Let $F(z, c) \in R[z, c]$ be the color-tube cubic ([color-tube cubic](#rem:color-tube-cubic)) with roots $c_1(z), c_2(z), c_3(z)$ over the categorical base ring $R$. Let $\mathrm{S}_3$ act on the three color sheets by permutation. The canonical Wedderburn decomposition is

$$
  R[\mathrm{S}_3]
  \;\cong\;
  R \oplus R \oplus R^{2 \times 2}
  \quad
  (\text{trivial} \;\oplus\; \text{sign} \;\oplus\; \text{standard}).
$$

The integrand

$$
  \lambda_{\mathrm{baryon}}(z)
  \;:=\;
  \prod_{k=1}^{3} \frac{dc_k}{dz}
$$

is the projection onto the $\mathrm{Alt}^3$ (sign) isotype of the $\mathrm{S}_3$-module $\bigotimes_{k=1}^3 \,T_{c_k}\mathbf{C}$ generated by the color-sheet velocities. The sum $\sum_k dc_k/dz$ projects onto the trivial isotype. The sum $\sum_{k \neq l} (dc_k/dz)(c_l + z)$ projects onto the standard isotype.

This purely algebraic statement holds over $R$. It does not use the archimedean fibre functor $\tau \colon R \to \mathbb{R}$. The quark-color content of the baryon selects the $\mathrm{Alt}$ isotype. This selection fixes the integrand up to a scalar.
<!-- FILE_END: baryon-product-from-alt.md -->

<!-- FILE_START: golden-skew-dual-node.md -->
The Hecke bar involution $\sigma \leftrightarrow \sigma^{-1}$ acts on the substrate parameter as $q \leftrightarrow q^{-1}$. In terms of $s = \sqrt{q}$, this is $s \leftrightarrow 1/s$. This involution maps the golden-ratio node $q_{\mathrm{gold}} = 1/\varphi^2$ ([golden-ratio degeneration](#rem:golden-ratio-degeneration)) to the skew-dual golden node:

$$
  q^{*}_{\mathrm{gold}}
  =  \varphi^2
  =  \frac{3 + \sqrt{5}}{2}
   \approx  2.618.
$$

The minimal polynomial of $1/\varphi$ over $\mathbb{Q}$ is $s^2 + s - 1$. Applying $s \mapsto 1/s$ and clearing denominators yields the bar-involute:

$$
  s^2 - s - 1.
$$

This is the minimal polynomial of $\varphi$. The involution $s \leftrightarrow 1/s$ exchanges these quadratics up to sign. Their roots form the bar-paired set $\{1/\varphi, \varphi\}$ on the positive real axis.
<!-- FILE_END: golden-skew-dual-node.md -->

<!-- FILE_START: golden-skew-dual-node-interpretation.md -->
**Remark (Stability margin).** The reciprocal node bar-duality ($\varphi^{-2}$ and $\varphi^2$) functions as a two-sided stability margin. This margin provides a boundary condition for bounding spectral gaps.
<!-- FILE_END: golden-skew-dual-node-interpretation.md -->

