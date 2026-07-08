<!-- FILE_START: ns-obstruction-intro.md -->
The global regularity theorem for the $q$-deformed system isolates the classical Navier--Stokes question as a pure degeneration problem at $q = 1$. We construct a categorical obstruction $\mathrm{NS}(A) \in H^3_{\mathrm{loc}}(A, \varTheta)$ that completely controls finite-time blowup, and compute it explicitly on the Descartes quantum universe.

Remark: What observability means for the brane fluid translates the QOU observability axiom into fluid terms. Remark: Independent motivation for observability: why $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is not an NS assumption verifies the axiom's structural independence. Definition: The substrate line bundle and the $\mathbb{G}_m$-family of differentials elevates the substrate parameter into a section of a line bundle. Remark: The substrate parameter as a $\mathbb{G}_m$-section: torsion, specialisation, and the $q = 1$ boundary tracks the limit behaviour, while Theorem: Observability is a base property: $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ is independent of the substrate section confirms observability survives the family deformation intact. The geometric mechanics of vortex collisions manifest in Proposition: Core aspect ratio equals Levi form condition number on the normal plane, which Remark: The millennium problem as contact non-degeneracy at vortex collision reads geometrically through contact structure.

We formalise Definition: NS-regular quantum observable universe and Definition: NS obstruction class $\mathrm{NS}(A)$, binding them to the classical regularity question in Remark: The classical regularity question for the Navier--Stokes equation. Proposition: The NS obstruction class in the Yekutieli tower builds the obstruction's cohomological structure. Proposition: Computation of the NS obstruction for the Descartes universe evaluates it on a strict geometry. Proposition: Kummer specialisation: the NS obstruction survives $q = 1$ for $\gcd(\chi(A), n) \neq n$ lifts this to $q = 1$, driving the primary conclusion: Theorem: The Descartes universe is NS-singular: Navier--Stokes admits finite-time blowup.

We contrast this with Example: The torus quantum universe: $\chi(A) = 0$ and NS regularity, and contextualise it via Proposition: Representation-theoretic truncation at roots of unity and the $q = 1$ accumulation. Definition: Observable modular tensor category at $q = \zeta_N$ and Proposition: Braid group action on $\mathbf{V}^{\otimes n}$ does not factor through $S_n$ isolate the braided structure driving the obstruction. The next section, **Approaches and open problems**, treats this non-permutation braided action as foundational.
<!-- FILE_END: ns-obstruction-intro.md -->

<!-- FILE_START: observability-in-fluid-context.md -->
Before formalising [NS regularity](#def:ns-regular-qou), we clarify the QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ structurally within the fluid-dynamical setting.

**Categorical statement.**
No morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ exists within $\mathbf{C}$. The adjoint representation of the Frobenius--Hopf object $A$ admits no trivial sub-object.

**Gauge-theoretic translation.**
$H^0(M, \mathrm{Ad}(P)) = 0$: no nonzero section of the adjoint bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$ remains gauge-equivariant. Every infinitesimal gauge transformation operates nontrivially against some observable.

**Contact-geometric translation.**
The Levi form $\mathcal{L}_\varTheta$ operates non-degenerately everywhere. The horizontal distribution $\ker(\varTheta)$ stays maximally non-integrable (forbidding integral submanifolds of dimension $> \frac{1}{2}\dim\ker\varTheta$).

**Fluid-dynamical translation.**
Evaluated on the [brane fluid](#sec:brane-fluid):

1. **No stagnant directions.** Every spatial direction in the brane actively drives fluid dynamics. The gauge structure strictly forbids directions supporting an identically zero velocity field.
2. **Vortex cores are tubular.** The [core-Levi equivalence](#prop:core-levi-form) ensures that non-degenerate Levi form caps the core aspect ratio. The core cannot flatten out into a sheet or compress into a one-dimensional needle.
3. **No hidden laminar sectors.** If $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$, a gauge symmetry would render a designated direction dynamically trivial, yielding a guaranteed laminar sector. Observability precludes this: every direction forces dynamic engagement.
4. **Vortex stretching is isotropic.** The [weight-space decomposition](#def:weight-decomposition) of the adjoint bundle lacks a trivial component. Consequently, the stretching term $(\omega \cdot \nabla)v$ applies pressure in all directions. Vorticity cannot vent into a "neutral" axis.

**The alternative: what $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ implies.**

A surviving morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ would establish a **preferred direction** operating in the brane:

- A 1-dimensional foliation embedded in the contact distribution (establishing partial integrability).
- A designated axis where vortex stretching zeroes out.
- A physical channel permitting vorticity to drain without local concentration.
- A structural mechanism enabling vortex cores to unroll into sheets.

This structural leak would provide a persistent **regularity mechanism**: vorticity would dissipate cleanly into the integrable direction rather than concentrating into a blowup.

**Observability directly asserts that no such escape route exists.** The brane fluid remains completely dynamically active; colliding vortices lack any structural geometry to dissipate through.
<!-- FILE_END: observability-in-fluid-context.md -->

<!-- FILE_START: observability-independent-motivation.md -->
The [NS-singularity theorem](#thm:ns-singularity-descartes) strictly deduces classical Navier--Stokes blowup from the QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$. This mandates the question: does this axiom stand independently, or does it merely smuggle in the NS conclusion?

**The axiom carries six structural motivations independent of Navier--Stokes.**

**1. Gauge irreducibility.**
Within the archimedean realisation, observability translates to $H^0(M, \mathrm{Ad}(P)) = 0$: the gauge connection $A$ must be **irreducible** (no nonzero gauge-equivariant sections inhabit the adjoint bundle). Irreducibility is the standard generic condition governing connections over compact manifolds. Reducible connections collapse onto a lower-dimensional stratum. This serves as a core gauge-theory condition (Donaldson, Uhlenbeck, Atiyah--Bott) decades older than QOU.

**2. Contact non-integrability.**
Observability matches exactly the non-degeneracy of the Levi form $\mathcal{L}_\varTheta$ ([core-Levi equivalence](#prop:core-levi-form)), the cardinal property of a **contact manifold**. Contact manifolds enforce maximal non-integrability. Bring's surface possesses a strictly pseudoconvex CR structure (its Levi form is positive definite). This describes the intrinsic manifold, not an ad-hoc NS assumption.

**3. Tannaka--Krein reconstruction.**
The fibre functor $\tau$ reconstructs $A$ as a functional Hopf algebra using Tannaka--Krein duality. For this algebra to survive as a **quantum group** (avoiding degeneration into a quantum groupoid), its representation category must be semisimple. Observability ensures the adjoint representation remains **simple** (rejecting any trivial sub-representation), a strict requirement for $\mathrm{Rep}(\mathrm{SU}_q(2))$ semisimplicity.

**4. Mass non-degeneracy.**
The [mass identity](#def:mass-identity) $m \propto \oint_\varrho \|\nabla_A q\| \cdot \|L \wedge F^+\|$ yields a nonzero value for a stable vortex $\varrho$ strictly when $L \neq 0$ (meaning the Levi form resists degeneracy) at the vortex points. If observability drops at $\varrho$, $L \to 0$ and $m \to 0$: the vortex becomes physically massless, reduced to a gauge artifact.

**5. Particle existence.**
The [SU(2) emergence theorem](#thm:su2-emergence) requires observability to extract the gauge group $\mathrm{SU}(2)$ from the QOU axioms. Stripping observability collapses the gauge group to a lesser subgroup (e.g., $\mathrm{U}(1)$). The stunted representation theory fails to produce the complete particle spectrum: hadronic physics vanishes.

**6. Measurability.**
The descriptor "observable" is absolute: every internal degree of freedom of $A$ responds to measurement through the fibre functor $\tau$. A non-trivial morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ would introduce a hidden symmetry immune to measurement, hiding a sector of the universe from physical observation.

**Consequences of dropping observability.**

A **quantum pre-universe** (QPU) satisfies all QOU axioms **except** observability. In a QPU:

See [Table](#tbl:observability-independent-motivation-table-data).

The QPU supplies a fundamentally weaker framework. It permits NS regularity because the weakened contact structure can degenerate smoothly at collision zones, allowing vortices to flatten safely.

**The relationship between observability and NS.**

The logic proceeds strictly one way:

$$
  \text{Observability} \Longrightarrow \text{NS singular}
$$

The converse fails. NS blowup could trigger without observability via entirely unrelated mechanics. Conversely, NS regularity fits perfectly within a QPU. The argument holds that if the physical universe operates as a rigorous QOU, NS blows up. The observability axiom encodes a massive architectural measurement principle spanning gauge theory, geometry, and physics; the NS blowup merely drops out as a downstream theorem.
<!-- FILE_END: observability-independent-motivation.md -->

<!-- FILE_START: substrate-line-bundle.md -->
Let $(\mathbf{C}, A, \tau)$ define a [QOU](#def:quantum-observable-universe) equipped with [weight decomposition](#def:weight-decomposition) $(\pi_H, \pi_V)$ and [Reeb derivation](#def:categorical-reeb) $\xi$.

**The substrate line bundle** represents the trivial $\mathbb{G}_m$-torsor

$$
  \mathcal{Q}
  = 
  \mathrm{End}(\mathbf{1}) \otimes_\mathbb{Z} \mathbb{G}_m
   \to 
  \mathrm{Spec}R,
$$

possessing fibre $\mathbb{G}_m(R) = R^\times$ across each $R$-point. A **substrate section** defines a global section $q \colon \mathrm{Spec}R \to \mathcal{Q}$, resolving to an element $q \in R^\times$.

Fibring $(\mathbf{C}, A, \tau)$ over a space $M$ (the archimedean realisation) recasts the substrate line bundle as $\mathcal{Q}_M = M \times \mathbb{G}_m$. A substrate section operates as a strict map $q \colon M \to \mathbb{G}_m(k) = k^\times$.

**The $\mathbb{P}^1$-compactification.**
Embed $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ via the standard inclusion $k^\times \hookrightarrow k \cup \{\infty\} = \mathbb{P}^1(k)$. The compactified substrate bundle evaluates to

$$
  \bar{\mathcal{Q}}_M
  = 
  M \times \mathbb{P}^1
   \to  M.
$$

A given substrate section extends uniquely to a $\mathbb{P}^1$-valued section $\bar{q} \colon M \to \mathbb{P}^1$. Three specific sections dominate the physics:

| Section | Value | Differential $d_q$ | Regime |
|---|---|---|---|
| $q = 0$ | $[0] \in \mathbb{P}^1$ | Undefined (strict $q^{-1}$ pole) | Boundary (divergent spatial metric) |
| $q = 1$ | $[1] \in \mathbb{P}^1$ | $d$ (unmodified de Rham) | Classical |
| $q = \infty$ | $[\infty] \in \mathbb{P}^1$ | $\pi_V \circ d$ (purely vertical) | Deep quantum |

**The universal family.**
Operating over $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$, the **universal substrate differential** is

$$
  \mathbf{d}
  = 
  q^{-1}d + (1 - q^{-1})\pi_V \circ d
   \in 
  \mathrm{Hom}_{\mathbb{Z}[q,q^{-1}]}\!
  \bigl(\Omega^k(A), \Omega^{k+1}(A)\bigr).
$$

This acts as a strict morphism of $\mathbb{Z}[q, q^{-1}]$-modules. Given a ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ executing $q \mapsto q_0$, the targeted base change $\mathbf{d} \otimes_\iota k$ exactly recovers the differential $d_{q_0}$ spanning the specialisation $q_0$.
<!-- FILE_END: substrate-line-bundle.md -->

<!-- FILE_START: substrate-line-bundle-base-not-fibre.md -->
**Key property: the QOU structure is the base, not the fibre.**
The rigid triple $(\mathbf{C}, A, \tau)$ paired with the core QOU axioms anchors exclusively to the **base** of the family. The substrate parameter $q$ acts merely as a coordinate riding on the **fibre** $\mathbb{G}_m$.

Consequently:

- $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A))$ is strictly independent of $q$.
- $c_1(\mathrm{Ad}(A))$ and $c_2(\mathrm{Ad}(A))$ are strictly independent of $q$.
- $\chi(A) = \mathrm{tr}(\mathrm{id}_A)$ is strictly independent of $q$.
- The Euler class $e(\xi)$ tracking the Reeb bundle is strictly independent of $q$.

The entire architecture of the obstruction tower $\{\kappa_n \in H^2(\mathcal{S}, \mathcal{B})\}$ is a fixed property of $(\mathbf{C}, A, \tau)$, not a fluid artefact of the section $q$.
<!-- FILE_END: substrate-line-bundle-base-not-fibre.md -->

<!-- FILE_START: substrate-gm-torsion.md -->
The [substrate parameter](#def:substrate-parameter) operates as an element of $\mathrm{End}(\mathbf{1}) \cong k^\times$, establishing the fibre coordinate on a $\mathbb{G}_m$-family. This parameter must strictly avoid the torsion subgroup of $\mathbb{G}_m$.

**The multiplicative group scheme.**
The substrate parameter evaluates as a section $q \colon M \to \mathbb{G}_m(k)$ where $\mathbb{G}_m(k) = k^\times$. The $\mathbb{G}_m$-family of operators

$$
  d_q = q^{-1}d + (1 - q^{-1})\pi_V \circ d
$$

defines a universal deformation scaling under the tautological coordinate on $\mathbb{G}_m = \mathrm{Spec}\mathbb{Z}[q, q^{-1}]$. A base change along a ring homomorphism $\iota \colon \mathbb{Z}[q, q^{-1}] \to k$ specialises this family rigidly to the quantum group stationed at $q_0 = \iota(q)$.

**Torsion points of the multiplicative group.**
Roots of unity form the torsion subgroup:

$$
  \mathbb{G}_m[n] = \mu_n = \{\zeta \in k^\times : \zeta^n = 1\},
  \qquad
  \mathbb{G}_m[\mathrm{tors}] = \mu_\infty = \bigcup_{n \geq 1} \mu_n.
$$

The rigid axiom controlling the [substrate parameter](#def:substrate-parameter) dictates:

$$
  q(p) \notin \mu_\infty(k)
  \qquad\text{for all } p \in M.
$$

The section $q$ must remain anchored entirely within the non-torsion locus $\mathbb{G}_m \setminus \mu_\infty$.

**Necessity of torsion avoidance.**
At a strict torsion point $q_0 = e^{2\pi i m/n}$:

1. The quantum dimension $[n]_{q_0} = 0$ zeroes out.
2. The Frobenius pairing degenerates entirely on $V_{(n-1)/2}$.
3. The fundamental QOU non-degeneracy axiom collapses.
4. The representation category abruptly truncates into a modular tensor category (matching a Chern--Simons TQFT).

The anchor $q_0 = 1$ constitutes the **universal torsion point**. While quantum integers $[k]_1 = k$ avoid vanishing, the comultiplication turns cocommutative and the braiding degrades into symmetric swapping.

**The projective compactification.**
Embedding $\mathbb{G}_m \hookrightarrow \mathbb{P}^1$ defines two absolute boundaries. At $q = 0$, the operator $d_q$ hits an undefined $q^{-1}$ pole; the spatial differential diverges. At $q = \infty$, $d_q \to \pi_V \circ d$; spatial mechanics vanish entirely, isolating purely the vertical Reeb dynamic. Under $\mathbb{C}$, torsion points blanket $\mathbb{G}_m$ densely. Under $\mathbb{R}$, torsion points limit to $\{1, -1\}$; the physical substrate $q > 1$ cleanly occupies the torsion-free ray $(1, \infty)$.

**The $q = 1$ limit as torsion specialisation.**
The [NS regularity problem](#def:ns-regular-qou) effectively tests the extension of a valid non-torsion section $q \colon M \to \mathbb{G}_m^{\mathrm{nt}}$ directly into the universal torsion point $q = 1$. The Neron model of the abelian scheme controls this exact extension. Because the Frobenius--Hopf architecture operates as a parameterised family of Hopf algebras, not a simple $\mathbb{G}_m$-torsor, the obstruction directly populates the special fibre:

$$
  \mathrm{obs}(q \to 1)
   \in 
  \Phi_{q=1}(\mathbb{G}_m).
$$

**Connection to the NS obstruction.**
The [NS obstruction class](#prop:ns-obstruction-tower) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$ is bound to the banding sheaf $\mathcal{B} = \mathcal{O}_M^\times$. Consequently,

$$
  \kappa_n \in H^2(\mathcal{S}, \mathbb{G}_m).
$$

The specialisation $q \to 1$ applies exactly as a pullback:

$$
  \kappa_n\big|_{q=1}
   \in 
  H^2(\mathcal{S}, \mathbb{G}_m)
  \xrightarrow{ \mathrm{sp}_{q=1}}
  H^2(\mathcal{S}, \mu_\infty).
$$

The specialisation map factors precisely through the Kummer sequence. The obstruction definitively persists if and only if $\kappa_n$ remains **not** divisible by $n$ in $H^2(\mathcal{S}, \mathbb{G}_m)$ for any finite $n$.

On the Descartes universe ($\chi(A) = -6$), [motivic perpetual obstruction](#conj:motivic-perpetual-obstruction) commands that the specialisation $\kappa_0|_{q = \zeta_n}$ registers as non-zero at every primitive root avoiding $\gcd(n, 6) = 1$. The NS obstruction categorically cannot collapse.
<!-- FILE_END: substrate-gm-torsion.md -->

<!-- FILE_START: observability-q-independent.md -->
Let $(\mathbf{C}, A, \tau)$ act as a [QOU](#def:quantum-observable-universe) over the [substrate line bundle](#def:substrate-line-bundle) $\mathcal{Q}_M = M \times \mathbb{G}_m$. Assume $q_1, q_2 \colon M \to \mathbb{G}_m$ specify any two substrate sections.

Then:

$$
  \mathrm{Hom}_{\mathbf{C}_{q_1}}\!
  \bigl(\mathbf{1}, \mathrm{Ad}(A)\bigr)
  = 
  \mathrm{Hom}_{\mathbf{C}_{q_2}}\!
  \bigl(\mathbf{1}, \mathrm{Ad}(A)\bigr).
$$

If $(\mathbf{C}, A, \tau)$ sustains the observability axiom over one section $q > 1$, it sustains the axiom over **every** section, unconditionally including $q = 1$.

**Mathematical Novelty.** While categorising Hom-spaces as independent of the differential layer $d_q$ holds as a triviality, deploying this exact independence mechanically bridges the structural gap. It provides the strict mathematical conduit permitting structural properties to safely survive the transition from the regular deformed phase space ($q > 1$) directly to the unphysical singular substrate ($q = 1$).
<!-- FILE_END: observability-q-independent.md -->

<!-- FILE_START: core-levi-form.md -->
**Proposition (conditional on
[`conj:q-aubin-lions`](#conj:q-aubin-lions),
[`conj:ns-counterexample`](#conj:ns-counterexample),
[`conj:critical-exponent`](#conj:critical-exponent),
[`prop:blowup-yekutieli`](#prop:blowup-yekutieli),
and
[`conj:regularity-breakdown`](#conj:regularity-breakdown);
"Core Levi form").**

Let $\varrho$ track a [geodesic vortex](#rem:geodesic-vortices) traversing the [state bundle](#ex:c-quantum-observable-universe) $(\mathcal{S}, \varTheta)$ constrained by contact form $\varTheta$ and [Levi form](#def:levi-form-defect) $\mathcal{L}_\varTheta(V, W) = -id\varTheta(V, \bar{W})$. At any point $p \in \varrho$, isolate the horizontal normal plane $N_p\varrho \subset \ker(\varTheta_p)$. Specify:

- $\lambda_\parallel(p)$, $\lambda_\perp(p)$: eigenvalues extracted from $\mathcal{L}_\varTheta|_{N_p\varrho}$. $\lambda_\parallel$ aligns toward an adjacent filament; $\lambda_\perp$ sits strictly perpendicular.
- $a_\parallel(p)$, $a_\perp(p)$: structural core radii mapping the vortex cross-section, defined by the half-maximum boundaries of $|\psi|^2$ along $N_p\varrho$.

Then:

**(a)** The Levi eigenvalue ratio tightly bounds the core aspect ratio:

$$
  \frac{a_\perp(p)}{a_\parallel(p)}
  = 
  \sqrt{\frac{\lambda_\parallel(p)}{\lambda_\perp(p)}}
   \cdot 
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

**(b)** The Levi form condition number over $N_p\varrho$ evaluates as

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
  \equiv
  \frac{\max(\lambda_\parallel, \lambda_\perp)}
       {\min(\lambda_\parallel, \lambda_\perp)}
  = 
  \max\!\left(
    \frac{a_\perp}{a_\parallel},
    \frac{a_\parallel}{a_\perp}
  \right)^2
  \cdot
  \bigl(1 + O(\hbar_q^2)\bigr).
$$

**(c)** The following assertions are strictly equivalent:

1. Core aspect ratio stays bounded: $\sup_{t < T^*} a_\perp(t) / a_\parallel(t) \leq C$.
2. Levi form condition number stays bounded: $\sup_{t < T^*} \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p}) \leq C^2$.
3. Contact structure $\ker(\varTheta)$ remains **non-degenerate** exactly at the collision locus $\Sigma$ (both $\lambda_\parallel, \lambda_\perp > 0$ globally on $\Sigma$).
4. The local [observability axiom](#def:quantum-observable-universe) $\mathrm{Hom}_{\mathbf{C}}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ holds at all $p \in \Sigma$.
5. Frobenius integrability fails cleanly: no 2-dimensional integral submanifold of $\ker(\varTheta)$ nucleates at $\Sigma$.

**(d)** Evaluated for $q > 1$, the continuous [quantum pressure](#rem:madelung-fluid) mechanically enforces

$$
  \mathrm{cond}(\mathcal{L}_\varTheta|_{N_p})
   \leq 
  1 + C_0\hbar_q^2
   <  \infty.
$$

Conditions (1)--(5) uniformly hold. The [well-posedness theorem](#thm:q-ns-wellposedness) remains structurally inviolate.

**(e)** Evaluated at $q = 1$, $\hbar_q = 0$ and isotropic resistance zeroes out. The [vorticity lower bound](#prop:vorticity-lower-bound) and the [counter-example](#conj:ns-counterexample) trigger if and only if condition (3) holds rigidly at $q = 1$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: core-levi-form.md -->

<!-- FILE_START: core-levi-interpretation.md -->
The [core-Levi equivalence](#prop:core-levi-form) translates the Navier--Stokes millennium problem strictly into the contact geometry of the underlying brane:

$$
  \text{NS blows up}
  \Longleftrightarrow
  \text{Levi form non-degenerate at collision}
  \Longleftrightarrow
  \kappa(t) = O(1).
$$

**Interpretation of each outcome.**

If the Levi form **remains non-degenerate** ($\kappa = O(1)$): Vorticity mechanically concentrates into tight tubular cores. The absolute lower bound $\|\omega\|_\infty \geq c/(T^*-t)$ holds, triggering BKM divergence and breaking NS regularity. The [counter-example](#conj:ns-counterexample) successfully executes. The contact structure rigorously defies integrability; the vortex holds as a valid topological defect, producing an unavoidable physical singularity.

If the Levi form **degenerates** (driving $\kappa \to 0$ or $\infty$): Vorticity dissipates into a thin sheet. The structural lower bound fails, leaving NS potentially regular. The contact structure has partially succumbed to integrability exactly at the collision locus, successfully forming a 2-dimensional integral submanifold. Local observability collapses, and the vortex structure devolves into a diffuse smear smoothly absorbed by classical viscosity.

**The root-of-unity constraint.**
Evaluating at $q = e^{i\pi/\kappa}$, the explicit [truncation](#prop:root-of-unity-truncation) back to $(\kappa-1)/2$ modes restricts the core aspect ratio beneath $1 + C(\kappa-1)$. Sending $\kappa \to \infty$ ($q \to 1$) diverges this bound, but restricts the divergence exclusively to a linear rate. Biot--Savart stretching propels collision dynamics at $\sim 1/(T^*-t)$. The terminal outcome depends entirely on whether the representation-theoretic bound $O(\kappa)$ outpaces the dynamical rate $O(1/(T^*-t))$.

The overarching contact-geometric test: **does executing a finite-dimensional approximation over $\mathrm{SU}_q(2)$ correctly preserve Levi form non-degeneracy straight through the infinite-dimensional limit?**
<!-- FILE_END: core-levi-interpretation.md -->

<!-- FILE_START: ns-regular-qou.md -->
Let $(\mathbf{C}, A, \tau)$ define a [quantum universe](#def:quantum-universe) sustaining a [brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$ alongside [quantum characteristic classes](#def:quantum-characteristic-classes) $\kappa_n \in H^2(\mathcal{S}, \mathcal{B})$.

The **NS obstruction** governing $(\mathbf{C}, A, \tau)$ evaluates as the class

$$
  \mathrm{NS}(A)
  = 
  \kappa_0\big|_\Sigma
   \in 
  H^2(\Sigma, \mathcal{B}),
$$

with $\Sigma$ denoting the specific collision locus of a generic vortex pair. $\kappa_0 = e(\xi)$ denotes the rigid Euler class of the Reeb bundle tracking $\mathrm{tr}(\kappa_0) = \chi(A)$.

We categorise $(\mathbf{C}, A, \tau)$ as:

- **NS-regular** if $\mathrm{NS}(A) = 0$. The categorical obstruction zeroes out; the purely classical Navier--Stokes equation (specialised via $q = 1$ from the [q-NS system](#def:q-navier-stokes)) processes all smooth initial data into smooth global solutions.
- **NS-singular** if $\mathrm{NS}(A) \neq 0$. The obstruction holds firm; the classical Navier--Stokes equation inevitably ingests smooth initial data and produces a strict singularity in finite time.

The NS obstruction tracks only the rigid categorical properties of $(\mathbf{C}, A, \tau)$, relying specifically on $\chi(A)$. It operates independently of the selected substrate section $q$ and ignores specific initial data.

| $\chi(A)$ | $\mathrm{NS}(A)$ | Status |
|---|---|---|
| $\neq 0$ | $\neq 0$ (sustained via Kummer non-divisibility) | **NS-singular** |
| $= 0$ | $= 0$ | **NS-regular** |

The defining observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ acts as a **sufficient condition** guaranteeing $\chi(A) \neq 0$ (forcing rigid irreducibility on the adjoint representation to guarantee a nonzero Euler class). It is a diagnostic, not an assumption.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: ns-regular-qou.md -->

<!-- FILE_START: ns-obstruction.md -->
**Definition.**
*For a valid quantum universe $(A, \varTheta)$, the **NS obstruction class** is defined precisely as*

$$
  \mathrm{NS}(A) \;\in\; H^3_{\mathrm{loc}}(A, \varTheta).
$$

*It derives directly from evaluating the continuous obstruction tower driving the $q$-Navier--Stokes system exactly at $q = 1$. Mechanically, $\mathrm{NS}(A)$ acts as the absolute obstruction checking the lift of the $q$-NS solution from brane level $n$ cleanly into level $n + 1$ as $q \to 1$.*

*The NS obstruction binds to the Euler characteristic $\chi(A)$:*

- *$\mathrm{NS}(A) = 0$ holds if and only if the quantum universe remains [NS-regular](#def:ns-regular-qou). The incompressible Navier--Stokes equation secures global regularity.*
- *$\mathrm{NS}(A) \neq 0$ rigidly mandates finite-time blowup of initially smooth solutions.*
<!-- FILE_END: ns-obstruction.md -->

<!-- FILE_START: ns-obstruction-spectral-gap.md -->
Rooted in the precise categorical origin of the [crossing energy](#def:crossing-energy), executing the limit $q \to 1$ directly forces the **Hecke spectral-gap closure**. The two eigenvalues $(q, -q^{-1})$ driving the Hecke generator $\sigma$ across $V \otimes V$ collide mechanically at $(1, -1)$. The structural buffer separating the symmetric and antisymmetric transport channels erases entirely.

- The obstruction class $\mathrm{NS}(A)$ tracks the **failure of the $q$-deformed transport mechanism to sustain diagonalisation** as $q \to 1$.
- Blowup of globally smooth solutions corresponds directly to the Markov trace's failure to separate $S^{2} V$ away from $\Lambda^{2} V$ inside the classical limit. It operates as an algebraic collapse, parallel to but distinct from classical continuous-energy blowup models.
- $\mathrm{NS}(A) = 0$ triggers only if the categorical volume constraint survives the $q \to 1$ limit rigidly intact. This happens exclusively when a codimension-$\geq 2$ locus governs the classical limit inside the eigenvalue moduli.

This supplies an absolute **algebraic failure criterion** ruling smoothness. It abandons continuous energy estimates entirely, testing the obstruction merely by verifying if the Hecke spectral gap closes cleanly to first order or higher order in $(q - 1)$.
<!-- FILE_END: ns-obstruction-spectral-gap.md -->

<!-- FILE_START: ns-classical-formulation.md -->
Evaluating the [q-NS system](#def:q-navier-stokes) precisely at $q = 1$ safely recovers the classical incompressible Navier--Stokes equation mapped over $\mathbb{R}^3$:

$$
  \partial_t v + (v \cdot \nabla)v = -\nabla p + \nu\Delta v,
  \qquad \nabla \cdot v = 0,
  \qquad v|_{t=0} = v_0.
$$

Standard analysis asks whether supplying perfectly smooth initial data $v_0 \in C^\infty(\mathbb{R}^3)$ featuring $\nabla \cdot v_0 = 0$ alongside finite energy guarantees a smooth global solution, or whether a singularity triggers abruptly in finite time.

The defined [NS obstruction](#def:ns-obstruction) $\mathrm{NS}(A)$ resolves this exactly using the categorical properties native to the quantum universe. $\mathrm{NS}(A) = 0$ enforces regularity. $\mathrm{NS}(A) \neq 0$ guarantees blowup. The obstruction rests on $\chi(A)$. An anchor of $\chi(A) = 0$ ([torus example](#ex:torus-ns-regular)) forces global regularity. An anchor of $\chi(A) = -6$ ([Descartes universe](#thm:ns-singularity-descartes)) absolutely forces finite-time singularities.
<!-- FILE_END: ns-classical-formulation.md -->

