<!-- FILE_START: yekutieli-lifting-kummer-motivic-intro.md -->
We incorporate the motivic enrichment of the Yekutieli lifting condition. The Kummer-filtration obstruction identifies the *fermionic-twisted* lifts. The Kummer tower organises this filtration. The Hochschild–Kummer connection interfaces with cyclic-homology data. We define the motivic substrate and its Galois character. We establish the *motivic-perpetual-obstruction*.

This motivic-enriched Yekutieli machinery serves as the native Galois substrate for the $q$-geometric-Langlands chapter. The spectral side of the Langlands functor pairs against the Galois character. The motivic perpetual obstruction supplies the structural obstacle that the spectral pairing navigates. Readers focused on the substrate level may treat the obstruction class as a black box. We defer its archimedean specialisation to the Descartes-universe chapter.
<!-- FILE_END: yekutieli-lifting-kummer-motivic-intro.md -->

<!-- FILE_START: p3-blowup-yekutieli.md -->
> **Summary.** We identify finite-time Navier-Stokes (NS) blowup with a finite obstruction level $n^*$ in the brane tower. At this level, a velocity field ceases to lift. We encode a counter-example by the cohomological address $(v_0, T^*, \Sigma, n^*, \kappa_{n^*})$. The local cohomology at the unit defect $z=1$ controls the singular set $\Sigma$.

The [regularity breakdown](#conj:regularity-breakdown) at $q = 1$ is a **cohomological obstruction** in the [Yekutieli lifting](#prop:yekutieli-lifting) framework.

## Yekutieli tower and regularity

The [recursive brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$ with jet prolongations $A_n \hookrightarrow A_{n+1}$ produces a sequence of central extensions of gerbes:
$$
  1 \to \mathcal{B}
  \to \mathfrak{G}_{n+1}
  \to \mathfrak{G}_n
  \to 1.
$$
Each carries an obstruction class $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)). A velocity field $v$ on the state bundle $\mathcal{S}$ is **smooth** if and only if it lifts through the entire tower. It admits a compatible representative at every level $A_n$:
$$
  v \text{ smooth}
  \quad\Longleftrightarrow\quad
  \kappa_n(v) = 0  \forall n \geq 0.
$$

## Blowup as cohomological obstruction

**Blowup as obstruction.** At $q = 1$, the spectral decay is polynomial: $|\hat{v}_k(t)| \sim k^{-s}$ for some Sobolev exponent $s$. The obstruction class $\kappa_n(v_1(t))$ at level $n$ depends on the $n$-th jet of $v$, which requires derivatives of order $n$. If $v \in H^s$ with $s$ finite, the $n$-th jet is undefined for $n > s$. The lifting fails:
$$
  \kappa_n(v_1(t)) \neq 0
  \quad\text{for}\quad
  n > s(t),
$$
where $s(t)$ is the Sobolev regularity at time $t$.

**Finite-time blowup means finite obstruction level.** If a NS solution loses regularity at time $T^*$, its Sobolev exponent $s(t) \to s^*$ as $t \to T^{*-}$ for some finite $s^* \geq 0$. The **obstruction level** is:
$$
  n^* = \lfloor s^* \rfloor + 1.
$$
The velocity field ceases to lift at this level. The blowup localises here:
- **Below $n^*$**: the velocity is smooth and lifts perfectly.
- **At $n^*$**: the obstruction class $\kappa_{n^*}$ is nonzero. The twisted 2-cocycle condition ([:refterm[descent]{#descent} condition](#prop:descent-condition)) fails.
- **Above $n^*$**: the solution does not exist in those gerbes.
<!-- FILE_END: p3-blowup-yekutieli.md -->

<!-- FILE_START: blowup-cohomological-address.md -->
**Location of a counter-example: the cohomological address.**
A counter-example to NS regularity is a quintuple:
$$
  (v_0, T^*, \Sigma, n^*, \kappa_{n^*})
$$
consisting of:
1. **Initial data** $v_0 \in C^\infty(\mathbb{R}^3)$, divergence-free, finite energy.
2. **Blowup time** $T^* < \infty$.
3. **Singular set** $\Sigma \subset \mathbb{R}^3$ — the spatial locus where regularity fails.
4. **Obstruction level** $n^* \in \mathbb{N}$ — the brane tower level where lifting fails.
5. **Obstruction class** $\kappa_{n^*} \in H^2(\Sigma, \mathcal{B})$ — the nonzero cohomology class preventing the lift.

Sobolev embedding relates the Hausdorff dimension $d_H(\Sigma)$ and the obstruction level $n^*$:

| $d_H(\Sigma)$ | Blowup geometry | $n^*$    | Singular $H^s$ |
| ------------- | --------------- | -------- | -------------- |
| $0$           | Point           | $\geq 3$ | $s^* < 3/2$    |
| $1$           | Filament        | $\geq 2$ | $s^* < 2$      |
| $2$           | Sheet           | $\geq 1$ | $s^* < 5/2$    |
<!-- FILE_END: blowup-cohomological-address.md -->

<!-- FILE_START: blowup-regularity-as-lifting.md -->
**Regularity as lifting.**
The [q-NS solution](#thm:q-ns-wellposedness) $v_q(t)$ is smooth for $q > 1$. The exponential damping of high modes ensures $v_q$ has exponentially decaying Fourier coefficients. All Yekutieli obstruction classes vanish:
$$
  |\hat{v}_k(t)| \leq |\hat{v}_k(0)|e^{-\nu_q[k]_q^2 t}
  \quad\Longrightarrow\quad
  \kappa_n(v_q(t)) = 0  \foralln.
$$
The decay rate $\nu_q [k]_q^2 \sim \varepsilonq^{2k}$ exceeds any polynomial. The field $v_q$ lifts through the tower to all levels.
<!-- FILE_END: blowup-regularity-as-lifting.md -->

<!-- FILE_START: blowup-local-cohomology-origin.md -->
**The local cohomology connection.**
The [local cohomology group](#def:local-cohomology-group) $H^1_{\mathfrak{m}_1}(A)$ at the unit defect $z = 1$ measures the obstruction to extending sections across the singularity. At $q = 1$, the defect locus $\{z = 1\}$ is the entire base manifold. The substrate parameter is identically $1$. We have:
$$
  H^1_{\mathfrak{m}_1}(A)\big|_{q=1}
  = 
  R^1\Gamma_{\mathfrak{m}_1}(A)
   \neq  0.
$$
This nonvanishing isolates the algebraic origin of the blowup. The $\mathfrak{m}_1$-torsion functor has a nontrivial derived functor exactly at $q = 1$, corresponding to regularity failure.

For $q > 1$, the defect locus $\{z = q^{-1}\} \neq \{z = 1\}$ separates from the unit. We have $H^1_{\mathfrak{m}_1}(A) = 0$. The obstruction vanishes. Regularity holds.
<!-- FILE_END: blowup-local-cohomology-origin.md -->

<!-- FILE_START: blowup-topological-selection.md -->
**The :refterm[descent]{#descent} condition and vortex reconnection.**
The [twisted 2-cocycle condition](#prop:descent-condition)
$$
  d(g_{ijk}^{(n)}) = a_{ij}^{(n)} \cdot g_{ijk}^{(n)}
  \cdot (a_{jk}^{(n)})^{-1}
$$
fails at the singular set $\Sigma$ because the transition functions $g_{ij}^{(n)}$ develop discontinuities there. These discontinuities correspond to [vortex reconnection](#rem:vortex-reconnection) events where the divisor topology changes. The obstruction class $\kappa_{n^*}$ measures the total topological change at $\Sigma$. It acts as the net "reconnection charge": the signed count of reconnection events weighted by their fusion-rule multiplicities.

**Constraint from Berry phase.**
The obstruction class must align with $\mathrm{SU}_q(2)$ representation theory. The class $\kappa_{n^*}$ must lie in the image of the character map:
$$
  \chi \colon
  \mathrm{Rep}(\mathrm{SU}_q(2))
   \to 
  H^2(\Sigma, \mathcal{B}).
$$
This restricts the possible values of $\kappa_{n^*}$ to a discrete lattice. This forms a **topological selection rule** on the blowup. We permit only vorticity concentrations with cohomological charges compatible with the categorical structure.
<!-- FILE_END: blowup-topological-selection.md -->

<!-- FILE_START: fermionic-twisted-sectors.md -->
A non-vanishing Yekutieli obstruction class $\kappa_n$ obstructs the lift $\mathcal{S}_n \to \mathcal{S}_{n+1}$. The transition between brane levels acquires a non-trivial twist. Under the [algebraic filter](#rem:algebraic-filter), fermionic-type matter (the $q$-harmonic forms satisfying $[F_A, \alpha] \neq 0$) exists precisely at the loci where $\kappa_n \neq 0$. This obstruction class creates "twisted" sectors in the gauge flow. The holonomy around these sectors acquires a phase in $H^2(M, \mathcal{O}_M^{\times})$ that prevents the vortex filament from lifting smoothly. This forces the localisation of fermionic excitations at the monodromy fixed points of the brane tower.
<!-- FILE_END: fermionic-twisted-sectors.md -->

<!-- FILE_START: kummer-filtration-obstruction.md -->
The Yekutieli obstruction classes $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) reside in the second cohomology of the state bundle with coefficients in the band $\mathcal{B} = \mathcal{O}_M^\times$. In the archimedean realisation, $\mathcal{B} = \mathbb{G}_m$, the multiplicative group scheme. The torsion structure of $\mathbb{G}_m$ imposes a natural filtration on the obstruction space.

**The Kummer exact sequence.** For each integer $n \geq 1$, the $n$-th power map on $\mathbb{G}_m$ fits into a short exact sequence of sheaves on $\mathcal{S}$:
$$
  1  \longrightarrow  \mu_n
   \longrightarrow  \mathbb{G}_m
  \xrightarrow{(\cdot)^n}
  \mathbb{G}_m
   \longrightarrow  1.
$$
The group scheme $\mu_n = \{\zeta \in \mathbb{G}_m : \zeta^n = 1\}$ consists of the $n$-th roots of unity. The associated long exact sequence in cohomology provides a connecting homomorphism and a reduction map at every level $n$:
$$
  \cdots  \to 
  H^1(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{\partial}
  H^2(\mathcal{S}, \mu_n)
   \to 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{(\cdot)^n}
  H^2(\mathcal{S}, \mathbb{G}_m)
   \to  \cdots
$$
The **Kummer reduction** of an obstruction class $\kappa$ at level $n$ is its image under the quotient:
$$
  \kappa \bmod n
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \big/
  nH^2(\mathcal{S}, \mathbb{G}_m).
$$
This reduction measures whether $\kappa$ is $n$-divisible in the obstruction group.
<!-- FILE_END: kummer-filtration-obstruction.md -->

<!-- FILE_START: kummer-tower.md -->
Stacking the Kummer sequences for all $n$ gives the **Kummer tower**. This filters $\mathbb{G}_m$ by its torsion subgroups:
$$
  \mu_1 \subset \mu_2 \subset \mu_3
  \subset \cdots \subset
  \mu_\infty \subset \mathbb{G}_m.
$$
The subgroup $\mu_\infty = \bigcup_{n \geq 1} \mu_n$ contains all roots of unity. This filtration induces a descending filtration on the obstruction:
$$
  \kappa  \in 
  F^1 H^2 \supset F^2 H^2 \supset F^3 H^2
  \supset \cdots,
  \qquad
  F^n H^2 = nH^2(\mathcal{S}, \mathbb{G}_m).
$$
The class $\kappa$ lies in $F^n$ if and only if it is $n$-divisible ($\kappa \bmod n = 0$).

**The trace and divisibility.** The [QU-to-QOU theorem](#thm:qu-to-qou) establishes that the first Yekutieli obstruction is the Euler class of the Reeb bundle: $\kappa_0 = e(\xi)$, with trace $\mathrm{tr}(\kappa_0) = \chi(A)$. The divisibility of this trace controls the Kummer reduction at level $n$:
$$
  \kappa_0 \bmod n = 0
  \quad\Longleftrightarrow\quad
  n  \big|  \chi(A).
$$
The obstruction $\kappa_0$ vanishes at precisely the Kummer levels $n$ that divide $|\chi(A)|$. It persists at all others. For any non-zero Euler characteristic, this gives a finite set of vanishing levels and a density-$1$ set of persisting levels.

**Complementary subgroup structure.** The obstruction at level $n$ in the brane tower ([QU-to-QOU](#thm:qu-to-qou), item 3) decomposes as:
$$
  \kappa_n = \kappa_0 + \delta_n,
$$
where $\delta_n$ is the jet correction at level $n$. The classes $\kappa_0$ and $\delta_n$ live in complementary subgroups of $H^2(\mathcal{S}, \mathbb{G}_m)$. The Euler class $\kappa_0$ is a topological invariant. The class $\delta_n$ is an analytic correction. They cannot cancel. Their sum $\kappa_n$ is nonzero whenever $\kappa_0$ is non-torsion.

This establishes the **perpetual obstruction** phenomenon. A non-torsion Euler class $\kappa_0$ produces a non-vanishing obstruction at every level of the brane tower. Jet refinement cannot remove it.

**Summary.** For any quantum universe with non-zero Euler characteristic $\chi(A) \neq 0$:
1. The Yekutieli obstruction $\kappa_0$ is non-trivial.
2. The Kummer tower filters the obstruction space by divisibility.
3. The obstruction persists at all Kummer levels $n \nmid \chi(A)$.
4. The complementary subgroup structure prevents jet corrections from cancelling the topological obstruction.
5. Properties of $\mathbf{C}_q$ depending on the vanishing of $\kappa_0 \bmod n$ must contend with this arithmetic obstruction at each level.
<!-- FILE_END: kummer-tower.md -->

<!-- FILE_START: kummer-tower-motivic-galois.md -->
**Motivic-Galois reading.**
The Kummer filtration on $H^2(\mathcal{S}, \mathbb{G}_m)$ is the restriction to the cyclotomic Galois subgroup $\mathrm{Gal}(\mathbb{Q}(\mu_\infty)/\mathbb{Q})$ of the **motivic-Galois filtration** on the [motivic substrate](#def:motivic-substrate). At each finite place $p \nmid \chi(A)$ of $\mathbb{Q}$ ([adelic substrate](#def:adelic-substrate)), the realization $\rho_p$ projects $\kappa_0$ to a non-trivial Frobenius character in $H^1_{\mathrm{Gal}}(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p),\,\mu_n(1))$ through the cyclotomic ideal $\mathbb{Z}[q]/\Phi_n(q)$. The perpetual obstruction guarantees that the motivic-Galois character of the Frobenius–Hopf substrate is non-trivial in $\mathrm{Hom}(\chi_n, 1)$ for almost every $n$. This realises perpetuity at every cyclotomic place.

The Frobenius character of $\kappa_0$ is non-trivial at almost every finite place $p \nmid \chi(A)$. We establish this in the [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction). The divisibility properties of the [Kummer tower](#rem:kummer-tower) follow as corollaries at each adelic place.
<!-- FILE_END: kummer-tower-motivic-galois.md -->

<!-- FILE_START: hochschild-kummer-connection.md -->
The Kummer filtration of $H^2(\mathcal{S}, \mathbb{G}_m)$ maps to the Hochschild cohomology of the Frobenius–Hopf algebra $A$ via the Hochschild–Kostant–Rosenberg comparison:
$$
  HH^2(\mathcal{U}_q, \mathrm{Ad})
  \xrightarrow{ \mathrm{HKR}}
  H^2(\mathcal{S}, \mathbb{G}_m).
$$
The deformation-theoretic obstruction (Hochschild) and the gerbe-theoretic obstruction (Yekutieli) present two views of the same class. The Kummer filtration pulls back to a filtration on $HH^2$ measuring the $n$-divisibility of deformation obstructions \cite{yekutieli2010}.

**Motivic-Galois interpretation.** The Kummer filtration on $H^2(\mathcal{S}, \mathbb{G}_m)$ restricts the **motivic-Galois filtration** to the cyclotomic subgroup $\mathrm{Gal}(\mathbb{Q}(\mu_\infty)/\mathbb{Q})$. Under the [motivic substrate](#def:motivic-substrate) realization tower $\{\rho_v\}$, the Hochschild class $\kappa \in HH^2(\mathcal{U}_q, \mathrm{Ad})$ projects at each finite place $p$ to a motivic Chern class $\rho_p(\kappa) \in H^1_{\mathrm{Gal}}(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p), \mu_n(1))$ through the cyclotomic ideal $\mathbb{Z}[q]/\Phi_n(q)$. Perpetual non-vanishing of $\kappa_n$ at every finite place $p \nmid \chi(A)$ ([Kummer tower](#rem:kummer-tower), [Descartes Yekutieli](#ex:archimedean-yekutieli)) means the motivic Galois character of the Frobenius–Hopf substrate is non-trivial in $\mathrm{Hom}(\chi_n, 1)$ for almost every $n$. The HKR comparison bridges the gerbe (geometric) and Hochschild (deformation) realizations of this single motivic class.
<!-- FILE_END: hochschild-kummer-connection.md -->

<!-- FILE_START: motivic-substrate.md -->
The QOU framework's algebraic substrate appears through two faces: the [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) and the [adelic substrate](#def:adelic-substrate). Both realize a single underlying object: the **motivic substrate**, a Grothendieck-ring datum equipped with a tower of realization functors.

**Definition (motivic substrate, axiom).**
The **motivic substrate** of the QOU framework is the triple
$$
  \mathcal{S}_{\mathrm{mot}}
  \;:=\;
  \bigl(K_0(\mathrm{Var}_k),\; \mathbb{L},\; \{\rho_v\}_{v \in \mathrm{Pl}(\mathbb{Q})}\bigr),
$$
consisting of:
1. the **Grothendieck ring of varieties** $K_0(\mathrm{Var}_k)$ over the base field $k$. It is the free abelian group on isomorphism classes $[X]$ of $k$-varieties modulo the scissor relations $[X] = [Z] + [X \setminus Z]$ for closed $Z \subseteq X$, with product $[X] \cdot [Y] = [X \times_k Y]$.
2. the **Lefschetz motive** $\mathbb{L} := [\mathbb{A}^1_k] \in K_0(\mathrm{Var}_k)$, with the localized ring $\mathcal{M} := K_0(\mathrm{Var}_k)[\mathbb{L}^{-1}]$ and its dimension-completion $\widehat{\mathcal{M}}$ ([motivic mass measure](#def:motivic-mass-measure)).
3. a **realization tower** $\{\rho_v \colon \widehat{\mathcal{M}} \to \widehat{\mathcal{M}}_v\}$. We assign one realization functor per place $v$ of $\mathbb{Q}$ ([adelic substrate](#def:adelic-substrate)). The archimedean realization $\rho_\infty$ is the [archimedean realization functor](#def:archimedean-realization-functor), landing in $\mathbb{R}$. The non-archimedean realizations $\rho_p$ at a finite prime $p$ produce local cyclotomic data compatible with the Habiro-ring framework ([Habiro completion](#prop:full-pole-structure-mass-trace)).

**Canonicity of the substrate.** Three observations factor through $\mathcal{S}_{\mathrm{mot}}$ rather than any single realization:
- **Mass formulas.** The topological mass of a knot ([motivic mass measure](#def:motivic-mass-measure)) is a class $\mathfrak{m}_{\mathrm{mot}}(\beta) \in \widehat{\mathcal{M}}$, not a real number. The real-valued mass arises only after applying $\rho_\infty$.
- **Adelic factorisation.** The global zeta integral $\mathcal{Z}(s)$ of the [adelic substrate](#def:adelic-substrate) factorises as a restricted product $\prod_v \zeta_v(s)$. This is the realization-tower factorisation $\rho_{\mathrm{tot}} = \prod_v \rho_v$ applied to a single motivic class.
- **Habiro evaluation.** The Habiro ring $\widehat{\mathbb{Z}[q]}$ is the universal target of the non-archimedean realizations of $\mathcal{S}_{\mathrm{mot}}$. The functor $\rho_p$ evaluates a motivic class at the level-$p$ root of unity. The inverse limit over $p$ recovers the Habiro completion.

Every algebraic invariant taking values in $\mathbb{R}$, $\mathbb{Q}_p$, or the Habiro ring is the realization at some place $v$ of a single motivic class living in $\widehat{\mathcal{M}}$.

**Relation to existing blocks.**
- The [Frobenius–Hopf substrate](#def:frobenius-hopf-substrate) is the algebraic-place realization. It forms a finite-type structure on $\mathcal{S}_{\mathrm{mot}}$.
- The [adelic substrate](#def:adelic-substrate) is the place-decomposition $\mathbb{A} = \mathbb{R} \times \prod_p' \mathbb{Q}_p$ indexing the realization tower. The adelic decomposition of a motivic class is the restricted product $\rho_{\mathrm{tot}}([X]) = (\rho_v([X]))_v$.
- The [arc space](#def:arc-space) $\mathcal{L}(X)$ provides the measurable space for motivic integration into $\widehat{\mathcal{M}}$. We derive the Kontsevich–Denef–Loeser motivic measure \cite{kontsevich1995, denef-loeser2001} from this space.

**Out of scope (deferred).** We do not axiomatize mixed motives, Bloch–Kato exact sequences, or full motivic Galois groups. We present the realization tower purely as the family $\{\rho_v\}$ of place-indexed evaluations. The categorical relationships among $\rho_v$ remain implicit.

**Lean axiomatization.** The substrate is axiomatized as a Lean `class` (per AGENTS.md §3b). The fields encode $K_0(\mathrm{Var}_k)$, $\mathbb{L}$, the localization $\widehat{\mathcal{M}}$, and the realization functors. We treat the `sorry` in any concrete instance as a substrate axiom, not a missing proof. Downstream results take a `[MotivicSubstrate]` instance as a hypothesis.
<!-- FILE_END: motivic-substrate.md -->

<!-- FILE_START: motivic-galois-character.md -->
The motivic-Galois layer on the Yekutieli obstruction $\kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m)$ acts via a single character of the cyclotomic Galois group: the **motivic Galois character of the Frobenius–Hopf substrate**.

**Definition.**
Let $A$ be the Frobenius–Hopf substrate of a quantum observable universe. Let $[A] \in \widehat{\mathcal{M}}$ be its motivic class ([motivic substrate](#def:motivic-substrate)). The **motivic Galois character of $A$** is the homomorphism
$$
  \chi^{\mathrm{mot}}_A
  \;\colon\;
  \mathrm{Gal}\bigl(\mathbb{Q}(\mu_\infty)/\mathbb{Q}\bigr)
  \;\longrightarrow\;
  \mathrm{Aut}_{\widehat{\mathcal{M}}}\bigl([A]\bigr).
$$
This encodes the action of the cyclotomic Galois group on the realization tower $\{\rho_p\}_{p \in \mathrm{Pl}(\mathbb{Q})}$ ([adelic substrate](#def:adelic-substrate)) of $[A]$. At each finite place $p$, the local component
$$
  \chi^{\mathrm{mot}}_{A,\,p}
  \;\colon\;
  \mathrm{Gal}\bigl(\bar{\mathbb{Q}}_p/\mathbb{Q}_p\bigr)
  \;\longrightarrow\;
  \mathrm{Aut}\bigl(\rho_p([A])\bigr)
$$
is the Frobenius character on the cyclotomic projection $\rho_p \colon \widehat{\mathcal{M}} \twoheadrightarrow \mathbb{Z}[q]/\Phi_{p^k}(q)$. The Yekutieli obstruction $\kappa_n$ ([quantum characteristic classes](#def:quantum-characteristic-classes)) is the image of $\chi^{\mathrm{mot}}_A$ under the [HKR comparison](#rem:hochschild-kummer-connection) to $H^2(\mathcal{S}, \mathbb{G}_m)$.

**Choice of level.**
Working directly with $\chi^{\mathrm{mot}}_A$ replaces per-level Čech-cocycle non-vanishing arguments with a single non-vanishing statement about the character ([motivic perpetual obstruction](#conj:motivic-perpetual-obstruction)). The Čech-cocycle and Hochschild presentations of $\kappa_n$ become realizations of $\chi^{\mathrm{mot}}_A$ at the archimedean and Hochschild-deformation places. The [Hochschild–Kummer](#rem:hochschild-kummer-connection) duality corresponds to the duality between these two realizations.

**Lean axiomatization.**
The formal-chain class [`MotivicGaloisCharacter`](../../lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean) takes a `MotivicSubstrate K0 Mhat Target` instance as a hypothesis. It exposes the character $\chi^{\mathrm{mot}}_A$ and its compatibility with each local realization $\rho_p$. We treat the `sorry` in any concrete instance as a substrate axiom.
<!-- FILE_END: motivic-galois-character.md -->

<!-- FILE_START: motivic-perpetual-obstruction.md -->
We lift the Kummer-tower perpetuity result ([Kummer tower](#rem:kummer-tower)) to a single algebraic statement at the level of the [motivic Galois character](#def:motivic-galois-character).

**Conjecture (motivic perpetual obstruction).**
Let $A$ be a Frobenius–Hopf substrate with motivic class $[A] \in \widehat{\mathcal{M}}$ and motivic Galois character $\chi^{\mathrm{mot}}_A$. If $\chi(A) \neq 0$, then $\chi^{\mathrm{mot}}_A$ is non-trivial at every finite place $p$ of $\mathbb{Q}$ with $p \nmid \chi(A)$. Equivalently, the local Frobenius character $\chi^{\mathrm{mot}}_{A, p}$ has a non-trivial element in
$$
  H^1_{\mathrm{Gal}}\!\bigl(\mathrm{Gal}(\bar{\mathbb{Q}}_p/\mathbb{Q}_p),\, \mu_n(1)\bigr)
$$
for every $n$ coprime to $p\,\chi(A)$. The Yekutieli obstruction $\kappa_0$ projects to a non-trivial Frobenius character at every such place.

**Sketch (conditional on `[MotivicGaloisCharacter K0 Mhat Target motiveA]`).**
We apply [QU-to-QOU](#thm:qu-to-qou) to identify $\kappa_0$ with the Euler class $e(\xi)$ of the Reeb bundle, satisfying $\mathrm{tr}(\kappa_0) = \chi(A)$. Under the realization $\rho_p \colon \widehat{\mathcal{M}} \to \mathbb{Z}[q]/\Phi_{p^k}(q)$ ([motivic substrate](#def:motivic-substrate)), the Euler class projects to a Frobenius character whose trace equals $\chi(A) \bmod p$. Because $p \nmid \chi(A)$, this trace is non-zero modulo $p$. The character is non-trivial. The class $\kappa_0$ retains a non-trivial Galois-cohomological component at every such place. By [Hochschild–Kummer](#rem:hochschild-kummer-connection), gerbe non-vanishing in $H^2(\mathcal{S}, \mathbb{G}_m)$ and Galois non-vanishing in $H^1_{\mathrm{Gal}}(\dots, \mu_n(1))$ are HKR-equivalent.
$\square$

**Consequence.**
This lemma subsumes every prior argument for the non-vanishing of $\kappa_n$ in the brane tower. In particular:
- [`rem:kummer-tower`](#rem:kummer-tower) summary item 6
- [`ex:archimedean-yekutieli`](#ex:archimedean-yekutieli) "Motivic-Galois reading"
- [`ex:chi-minus-six-derivation`](#ex:chi-minus-six-derivation) Step 8
- [`rem:hochschild-kummer-connection`](#rem:hochschild-kummer-connection) "Motivic-Galois interpretation"
These all reduce to corollaries of this motivic perpetual obstruction.
<!-- FILE_END: motivic-perpetual-obstruction.md -->
