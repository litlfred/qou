The [Descartes Reeb-bundle theorem](#thm:ns-singularity-descartes) and the internal obstruction reduction deduce the categorical singularity $\mathrm{NS}(A) = e(\xi) \neq 0 \in H^2(\mathcal{S}, \mathbb{Z})$ from the QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ (which the framework model correspondence associates with Navier--Stokes blowup). This mandates the question: does this axiom stand independently, or does it merely smuggle in the NS conclusion?

**The axiom carries five structural motivations independent of Navier--Stokes.** A sixth, contact non-integrability, is withdrawn (item 2).

**1. Gauge irreducibility.**
Within the archimedean realisation, observability translates to $H^0(M, \mathrm{Ad}(P)) = 0$: the gauge connection $A$ must be **irreducible** (no nonzero gauge-equivariant sections inhabit the adjoint bundle). Irreducibility is the standard generic condition governing connections over compact manifolds. Reducible connections collapse onto a lower-dimensional stratum. This serves as a core gauge-theory condition (Donaldson, Uhlenbeck, Atiyah--Bott) decades older than QOU.

**2. Contact non-integrability (withdrawn).**
This item formerly identified observability with non-degeneracy of a Levi form. That identification is withdrawn. The chapter's plane field lives on the three-dimensional flow domain, where its Levi datum is the single scalar $\xi\cdot\mathrm{curl}\,\xi$ of the vorticity direction $\xi$ ([core Levi form](#prop:core-levi-form)). No result in this monograph links that scalar to $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$.

**3. Tannaka--Krein reconstruction.**
The fibre functor $\tau$ reconstructs $A$ as a functional Hopf algebra using Tannaka--Krein duality. For this algebra to survive as a **quantum group** (avoiding degeneration into a quantum groupoid), its representation category must be semisimple. Observability ensures the adjoint representation remains **simple** (rejecting any trivial sub-representation), a strict requirement for $\mathrm{Rep}(\mathrm{SU}_q(2))$ semisimplicity.

**4. Mass non-degeneracy.**
The [mass identity](#def:mass-identity) $m \propto \oint_\varrho \|\nabla_A q\| \cdot \|L \wedge F^+\|$ yields a nonzero value for a stable vortex $\varrho$ strictly when $L \neq 0$ at the vortex points. If observability drops at $\varrho$, $L \to 0$ and $m \to 0$: the vortex becomes physically massless, reduced to a gauge artifact.

**5. Particle existence.**
The [SU(2) emergence theorem](#thm:su2-emergence) requires observability to extract the gauge group $\mathrm{SU}(2)$ from the QOU axioms. Stripping observability collapses the gauge group to a lesser subgroup (e.g., $\mathrm{U}(1)$). The stunted representation theory fails to produce the complete particle spectrum: hadronic physics vanishes.

**6. Measurability.**
The descriptor "observable" is absolute: every internal degree of freedom of $A$ responds to measurement through the fibre functor $\tau$. A non-trivial morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$ would introduce a hidden symmetry immune to measurement, hiding a sector of the universe from physical observation.

**Consequences of dropping observability.**

A **quantum pre-universe** (QPU) satisfies all QOU axioms **except** observability. The [comparison of observable universes and pre-universes](#tbl:observability-independent-motivation-table-data) summarises the structural differences.

The QPU supplies a fundamentally weaker framework, and it permits NS regularity.

**The relationship between observability and NS.**

The logic proceeds strictly one way:

$$
  \text{Observability} \Longrightarrow \text{NS singular}
$$

The converse fails. Classical NS blowup could trigger without observability via entirely unrelated PDE mechanics; conversely, categorical NS-regularity ($\mathrm{NS}(A) = e(\xi) = 0$, $\chi(A) = 0$) fits within a QPU. Within the QOU model, the observability axiom encodes a measurement principle spanning gauge theory, geometry, and representation theory, from which $\mathrm{NS}(A) = e(\xi) \neq 0$ follows as a downstream topological consequence; identifying that internal class with classical 3D PDE blowup is the separate model-to-PDE bridge ([NS-regular QOU](#def:ns-regular-qou)).
