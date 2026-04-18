Suppose instead that the [algebraic independence
conjecture](#conj:hyperbolic-volume-transcendence) fails: some
non-trivial $P \in \mathbb{Q}[x, y, z]$ satisfies
$P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)) = 0$.

**Mathematical consequences.**

1. **Refutation of Milnor's conjecture on this triple.** Since
   algebraic dependence over $\mathbb{Q}$ entails $\mathbb{Q}$-linear
   dependence whenever the polynomial has degree one in some variable,
   even a weak dependence forces a linear relation among volumes of
   pairwise non-commensurable hyperbolic $3$-manifolds, contrary to
   Milnor's prediction.

2. **Unexpected Bloch--Wigner identity.** Each volume is
   $D(\xi_K)$ for algebraic $\xi_K$ in distinct number fields.  A
   dependence would yield a non-trivial $\mathbb{Q}$-polynomial
   identity among Bloch--Wigner values across
   $\mathbb{Q}(\sqrt{-3})$, the cubic field of $5_2$, and
   $\mathbb{Q}(i)$ --- a new and surprising arithmetic identity.

3. **Collapse of the formal transcendence conjecture chain.** The
   implication chain
   (independence $\Rightarrow$ Borel--Zagier $\Rightarrow$
   single-volume irrationality) does not reverse; dependence leaves
   irrationality of each individual volume open but removes the
   categorical lever for proving it.

**QOU-specific consequences.**

1. **Yekutieli brane tower collapses at finite height.** By the
   contrapositive of [the bridge
   theorem](#rem:yekutieli-transcendence-shadow), some obstruction
   class $\kappa_n$ vanishes: the cosimplicial filtration terminates
   after finitely many levels.

2. **Confinement admits an algebraic closed form.** The hadronic
   binding energy $\mathbf{E}_{\mathrm{bind}}$ reduces to a finite
   polynomial expression in $q$; the infinite-tower interpretation of
   confinement is categorically inessential.

3. **Borromean baryon interpretation weakens.** The obstruction-theoretic
   basis for identifying the proton with the Borromean link
   $\mathcal{B}_3$ (which distinguishes it from a mere sum of Hopf
   pairs) loses its categorical teeth: the distinguishing invariant
   becomes computable from finite data.

4. **Coefficient ring simplifies.** The evaluation map
   $\iota$ is non-injective; the physical ring
   $\mathbb{Q}[q, q^{-1}][\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
   \mathrm{Vol}(\mathcal{B}_3)]$ is strictly smaller than the formal
   Laurent ring admits.

5. **Partial QOU falsification.** The Chapter 9 bandwidth bounds
   $\mathcal{B}(q)$ are satisfied with slack; the information-theoretic
   "hardness" of the substrate is weaker than the full conjecture
   predicts.  This is a falsification of the strong form but not of
   the topological mass formula, Gr\"obner--Shirshov construction, or
   experimental predictions --- those live entirely in
   $\mathbb{Z}[q, q^{-1}]$ and do not depend on transcendence (cf.
   [formal chain remark](#rem:formal-chain-transcendence)).

**Lean status.** Dependence would mean no instance of
`QOU.Descartes.HyperbolicVolumeIndependence` is populatable; the class
remains well-formed but uninhabited.  The conditional theorem
`QOU.Descartes.tower_noncollapse_implies_independence` is still valid
(vacuously), but its hypothesis
`QOU.Torsion.YekutieliLiftingCondition` becomes unsatisfiable.
