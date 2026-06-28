The [NS-singularity theorem](#thm:ns-singularity-descartes) deduces
Navier--Stokes blowup from the QOU observability axiom
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$. This raises
the question: is the observability axiom independently motivated,
or does assuming it amount to assuming the NS conclusion?

**The axiom has six independent motivations, none involving NS.**

**1. Gauge irreducibility.**
In the archimedean realisation, observability becomes
$H^0(M, \mathrm{Ad}(P)) = 0$: the gauge connection $A$ is
**irreducible** (no nonzero gauge-equivariant sections of the
adjoint bundle). Irreducibility is the generic condition for
connections on principal bundles over compact manifolds — the
moduli space of irreducible connections is open and dense in the
space of all connections. Reducible connections form a lower-
dimensional stratum.

This is a standard condition in gauge theory (Donaldson,
Uhlenbeck, Atiyah--Bott) that predates QOU by decades.

**2. Contact non-integrability.**
Observability is equivalent to non-degeneracy of the Levi form
$\mathcal{L}_\varTheta$ ([core-Levi equivalence](#prop:core-levi-form)),
which is the defining property of a **contact manifold**.
Contact manifolds are maximally non-integrable: the horizontal
distribution $\ker(\varTheta)$ has no integral submanifolds of
dimension greater than half the contact dimension.

Every odd-dimensional manifold admits a contact structure
(Martinet 1971). The question is not whether one exists but
whether the physical brane carries one. The CR structure of
Bring's surface is strictly pseudoconvex (Levi form positive
definite), which is stronger than mere non-degeneracy. This is
a property of the specific manifold, not an assumption about NS.
Cf.\ \cite{nicolaescu2005, leitner-2018}.

**3. Tannaka--Krein reconstruction.**
The fibre functor $\tau$ reconstructs $A$ as a Hopf algebra via
Tannaka--Krein duality. For this reconstruction to yield a
**quantum group** (rather than a quantum groupoid or a degenerate
algebra), the representation category must be semisimple and the
forgetful functor must be faithful. Observability ensures that
the adjoint representation is **simple** (no trivial
sub-representation), which is necessary for semisimplicity of
$\mathrm{Rep}(\mathrm{SU}_q(2))$.

Without observability, the adjoint representation would contain
a copy of $\mathbf{1}$, the Lie algebra $\mathfrak{su}(2)$
would have a centre, and the quantum group would degenerate
to $\mathrm{U}(1) \times \mathrm{SU}(2)/\mathrm{U}(1)$ — a
reducible structure.

**4. Mass non-degeneracy.**
The [mass identity](#def:mass-identity) $m \propto
\oint_\varrho \|\nabla_A q\| \cdot \|L \wedge F^+\|$ is
nonzero for a stable vortex $\varrho$ iff the integrand is
nonzero, which requires $L \neq 0$ (Levi form non-degenerate)
at points of $\varrho$. If observability fails at $\varrho$,
then $L = 0$ there, $m = 0$, and the vortex is massless —
it is not a particle but a gauge artifact.

**5. Particle existence.**
The [SU(2) emergence theorem](#thm:su2-emergence) deduces the
gauge group $\mathrm{SU}(2)$ from the QOU axioms. If
observability fails, the gauge group reduces to a proper
subgroup (e.g. $\mathrm{U}(1)$), and the representation
theory cannot produce the full particle spectrum. No quarks,
no hadrons, no nuclear physics.

**6. Measurability.**
The word "observable" in "quantum observable universe" is
literal: every degree of freedom of $A$ is accessible to
measurement via the fibre functor $\tau$.
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) \neq 0$ would mean
there exists a nonzero morphism $\phi \colon \mathbf{1} \to
\mathrm{Ad}(A)$ — a "hidden symmetry" that commutes with all
measurements. The universe would contain a sector invisible
to any experiment.

**Consequences of dropping observability.**

Define a **quantum pre-universe** (QPU) as a quantum universe
$(\mathbf{C}, A, \tau)$ satisfying all QOU axioms **except**
observability. In a QPU:

See [Table](#tbl:observability-independent-motivation-table-data).

The QPU is a weaker framework. It does not force NS blowup
because the contact structure can degenerate at collision
points, allowing vortex cores to flatten.

**The relationship between observability and NS.**

The logical relationship is:

$$
  \text{Observability} \Longrightarrow \text{NS singular}
$$

but **not** the converse. NS blowup could occur even without
observability (through a different mechanism). And NS regularity
is **compatible** with a QPU (where observability fails).

The argument is:
- If the physical universe is a QOU (observability holds), then
 NS blows up.
- If the physical universe is only a QPU (observability fails),
 then the NS question is open — but so is particle physics
 (no mass, no SU(2), no quarks).

The observability axiom is not an encoding of NS blowup. It is
a measurement principle with independent gauge-theoretic,
contact-geometric, representation-theoretic, and physical
content. The NS consequence is a theorem, not an assumption.
