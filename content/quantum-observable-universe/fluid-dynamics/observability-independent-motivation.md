The [NS-singularity theorem](#thm:ns-singularity-descartes) deduces Navier--Stokes blowup from the QOU observability axiom $\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$. We must ask whether this axiom is independently motivated, or if assuming it merely amounts to assuming the NS conclusion.

**The axiom has six independent motivations.** None involve Navier--Stokes.

**1. Gauge irreducibility.**
In the archimedean realisation, observability becomes $H^0(M, \mathrm{Ad}(P)) = 0$. The gauge connection $A$ is irreducible (there are no nonzero gauge-equivariant sections of the adjoint bundle). Irreducibility constitutes the generic condition for connections on principal bundles over compact manifolds. The moduli space of irreducible connections is open and dense in the space of all connections. Reducible connections form a lower-dimensional stratum. This is a standard condition in gauge theory (Donaldson, Uhlenbeck, Atiyah--Bott).

**2. Contact non-integrability.**
Observability is equivalent to non-degeneracy of the Levi form $\mathcal{L}_\varTheta$ ([core-Levi equivalence](#prop:core-levi-form)). This is the defining property of a contact manifold. Contact manifolds are maximally non-integrable: the horizontal distribution $\ker(\varTheta)$ contains no integral submanifolds of dimension greater than half the contact dimension. Every odd-dimensional manifold admits a contact structure (Martinet 1971). The relevant question is whether the physical brane carries one. Bring's surface possesses a strictly pseudoconvex CR structure (positive definite Levi form). This condition is stronger than mere non-degeneracy, and it is a property of the specific manifold rather than an assumption about Navier--Stokes.

**3. Tannaka--Krein reconstruction.**
The fibre functor $\tau$ reconstructs $A$ as a Hopf algebra via Tannaka--Krein duality. For this reconstruction to yield a quantum group (rather than a quantum groupoid or a degenerate algebra), the representation category must be semisimple, and the forgetful functor must be faithful. Observability ensures the adjoint representation is simple (no trivial sub-representation). This simplicity is necessary for the semisimplicity of $\mathrm{Rep}(\mathrm{SU}_q(2))$. Without observability, the adjoint representation would contain a copy of $\mathbf{1}$. The Lie algebra $\mathfrak{su}(2)$ would acquire a centre, and the quantum group would degenerate to the reducible structure $\mathrm{U}(1) \times \mathrm{SU}(2)/\mathrm{U}(1)$.

**4. Mass non-degeneracy.**
The [mass identity](#def:mass-identity) $m \propto \oint_\varrho \|\nabla_A q\| \cdot \|L \wedge F^+\|$ is nonzero for a stable vortex $\varrho$ if and only if the integrand is nonzero. This requires $L \neq 0$ (a non-degenerate Levi form) at points of $\varrho$. If observability fails at $\varrho$, then $L = 0$ there. Consequently, $m = 0$, and the vortex becomes a massless gauge artifact rather than a particle.

**5. Particle existence.**
The [SU(2) emergence theorem](#thm:su2-emergence) deduces the gauge group $\mathrm{SU}(2)$ from the QOU axioms. If observability fails, the gauge group reduces to a proper subgroup (such as $\mathrm{U}(1)$). The representation theory can no longer produce the full particle spectrum.

**6. Measurability.**
Every degree of freedom of $A$ must be accessible to measurement via the fibre functor $\tau$. A failure of observability ($\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$) implies the existence of a nonzero morphism $\phi \colon \mathbf{1} \to \mathrm{Ad}(A)$. This constitutes a "hidden symmetry" that commutes with all measurements. The universe would contain a sector entirely invisible to experiment.

**Consequences of dropping observability.**

We define a quantum pre-universe (QPU) as a quantum universe $(\mathbf{C}, A, \tau)$ satisfying all QOU axioms except observability.

See [Table](#tbl:observability-independent-motivation-table-data).

The QPU provides a weaker framework. It does not force Navier--Stokes blowup because the contact structure can degenerate at collision points, permitting vortex cores to flatten.

**The relationship between observability and NS.**

We have the logical implication:

$$
  \text{Observability} \Longrightarrow \text{NS singular}
$$

The converse does not hold. Navier--Stokes blowup could occur through a different mechanism even without observability. Furthermore, NS regularity remains compatible with a QPU. If the physical universe is a QOU (observability holds), Navier--Stokes blows up. If it is only a QPU (observability fails), the Navier--Stokes question remains open, but particle physics loses mass, SU(2), and quarks. The observability axiom encodes a measurement principle with independent physical and geometric content. The Navier--Stokes consequence is a theorem, not an assumption.
