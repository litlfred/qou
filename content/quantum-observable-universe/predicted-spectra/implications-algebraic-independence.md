Assume the [algebraic independence
conjecture](#conj:hyperbolic-volume-transcendence) holds: no non-trivial
polynomial $P \in \mathbb{Q}[x, y, z]$ satisfies
$P(\mathrm{Vol}(4_1), \mathrm{Vol}(5_2),
\mathrm{Vol}(\mathcal{B}_3)) = 0$.

**Mathematical consequences.**

1. **Milnor's conjecture confirmed on this triple.** The knots
   $4_1$, $5_2$, and the Borromean link $\mathcal{B}_3$ have pairwise
   non-commensurable hyperbolic complements; algebraic
   independence is strictly stronger than the $\mathbb{Q}$-linear
   independence predicted by Milnor.

2. **Irrationality of each volume.** Each of
   $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$,
   $\mathrm{Vol}(5_2)$, and $\mathrm{Vol}(\mathcal{B}_3)$ is
   irrational.  Irrationality of a single hyperbolic $3$-manifold
   volume is open; algebraic independence settles the question for
   the whole triple.

3. **Bloch--Wigner dilogarithm transcendence.** Since each volume is
   $D(\xi)$ for an algebraic $\xi$ in a number field
   ($\mathbb{Q}(\sqrt{-3})$, the cubic field of $5_2$, and
   $\mathbb{Q}(i)$ respectively), algebraic independence gives the
   first provably transcendental values of the Bloch--Wigner
   dilogarithm at algebraic arguments.

**QOU-specific consequences.**

1. **Brane tower does not collapse.** By the bridge
   theorem ([Yekutieli transcendence
   shadow](#rem:yekutieli-transcendence-shadow)), independence is
   equivalent to non-vanishing of the obstruction classes
   $\kappa_n \neq 0$ for all $n \geq 0$.  The cosimplicial filtration
   of $\mathrm{SU}_q(2)$-gerbes is genuinely infinite.

2. **Confinement is categorically robust.** The hadronic binding
   energy $\mathfrak{E}_{\mathrm{bind}}$ admits no closed-form algebraic
   reduction: the infinite tower is the categorical signature of
   quark confinement.  The Borromean baryon interpretation of the
   proton rests on an irreducible obstruction.

3. **Injective specialisation.** The evaluation map
   $\iota \colon \mathbb{Q}[q, q^{-1}]
   [\mathrm{Vol}(4_1), \mathrm{Vol}(5_2), \mathrm{Vol}(\mathcal{B}_3)]
   \to \mathbb{R}$ at $q = q_0$ is injective.  The physical coefficient
   ring is as rich as the formal Laurent polynomial ring admits.

4. **Strong falsifiability.** The information-bandwidth bounds
   $\mathfrak{B}(q)$ are tight: any experimental evidence of
   algebraic relations among computed volumes would contradict the
   prediction.

**Lean status.** Independence is encoded as the class
`QOU.Archimedean.HyperbolicVolumeIndependence`; populating an instance
requires a Nesterenko-type arithmetic theorem for the quantum
dilogarithm $\mathrm{Li}_2^q$ at algebraic arguments --- open.
