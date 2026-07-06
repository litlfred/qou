Suppose the [algebraic independence conjecture](#conj:hyperbolic-volume-transcendence) fails. Then a non-trivial polynomial $P \in \mathbb{Q}[x, y, z]$ satisfies $P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)) = 0$.

**Mathematical consequences.**

1. **Milnor's conjecture.** Algebraic dependence is weaker than $\mathbb{Q}$-linear dependence. A dependence polynomial of degree greater than one does not refute Milnor's prediction of $\mathbb{Q}$-linear independence for pairwise non-commensurable hyperbolic $3$-manifolds.

2. **Bloch--Wigner identities.** Each volume takes the form $D(\xi_K)$ for algebraic $\xi_K$ in distinct number fields. An algebraic dependence yields a $\mathbb{Q}$-polynomial identity among Bloch--Wigner values across $\mathbb{Q}(\sqrt{-3})$, the cubic field of $5_2$, and $\mathbb{Q}(i)$.

3. **Transcendence chain.** The implication chain (independence $\Rightarrow$ Borel--Zagier $\Rightarrow$ single-volume irrationality) breaks. Irrationality remains open for each volume, but the categorical lever to prove it vanishes.

**Framework consequences.**

1. **Tower collapse.** The contrapositive of the [bridge theorem](#rem:yekutieli-transcendence-shadow) forces an obstruction class $\kappa_n$ to vanish. The cosimplicial filtration terminates at finite depth.

2. **Confinement.** The hadronic binding energy $\mathfrak{E}_{\mathrm{bind}}$ reduces to a finite polynomial expression in $q$. The infinite-tower structure is not required for confinement.

3. **Borromean baryon.** The distinction between the Borromean link $\mathcal{B}_3$ and a sum of Hopf pairs reduces to finite categorical data. The invariant identifying the proton as a three-body configuration is computable without the infinite tower.

4. **Coefficient ring.** The evaluation map $\iota$ is non-injective. The physical ring $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)]$ is smaller than the formal Laurent ring admits.

5. **Bandwidth bounds.** The substrate satisfies the information-bandwidth bounds $\mathfrak{B}(q)$ with slack. The topological mass formula, Gröbner--Shirshov construction, and spectral predictions remain valid, as they reside in $\mathbb{Z}[q, q^{-1}]$ (see [formal chain remark](#rem:formal-chain-transcendence)).

**Lean formalisation.**
Dependence implies the class `QOU.Archimedean.HyperbolicVolumeIndependence` is uninhabited. The conditional theorem `QOU.Archimedean.tower_noncollapse_implies_independence` remains vacuously true, but its hypothesis `QOU.Torsion.YekutieliLiftingCondition` is unsatisfiable.
