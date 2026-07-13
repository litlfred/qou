<!-- FILE_START: mass-geometric-face-intro.md -->
The mass endomorphism's geometric face links the algebraic Markov trace to the hyperbolic volume of the knot complement. Thurston's volume additivity decomposes the mass of a composite knot into a sum over its JSJ pieces. The mass-volume factorisation conjecture establishes the categorical mass endomorphism as the product of this topological volume and the Frobenius-packing density.

The crossing-graded expansion organizes the mass hierarchically by crossing count, with each layer governed by the lifted crossing locality conjecture. The jet-tower bound secures geometric convergence for the brane-tower sum, while Jucys-Murphy reindexing connects the tower explicitly to standard Young tableaux in the Hecke algebra.
<!-- FILE_END: mass-geometric-face-intro.md -->

<!-- FILE_START: thurston-volume-additivity.md -->
## Thurston volume additivity

Every hyperbolic knot complement admits an ideal triangulation by tetrahedra with vertices on the sphere at infinity. A single complex shape parameter $z_i$ determines each tetrahedron up to isometry.

**Proposition.**
*The hyperbolic volume of the knot complement $S^3 \setminus \mathcal{K}$ is the sum of its tetrahedral volumes:*

$$
  V(\mathcal{K})
  \;=\;
  \sum_{i = 1}^N D(z_i),
$$

*where $D(z_i)$ is the Bloch-Wigner dilogarithm evaluated at the shape parameter. Flat tetrahedra ($z_i \in \mathbb{R}$) contribute zero volume.*

## Braid-theoretic consequence

A knot diagram induces an ideal triangulation containing one tetrahedron per crossing. Consequently, the volume sums additively over crossings:

$$
  V(\mathcal{K}) \;=\; \sum_{\text{crossings } c} D(z_c).
$$

Torus knots project entirely onto a surface, forcing every $z_c$ to be real. Their hyperbolic volume vanishes identically.

## Extremality

The Bloch-Wigner function reaches its maximum at the regular shape $z = e^{i\pi/3}$, yielding the Lobachevsky constant $v_3 \approx 1.01494$. The figure-eight knot $4_1$ comprises exactly two such tetrahedra, producing the minimum hyperbolic volume $V(4_1) = 2 v_3 \approx 2.02988$. This extremality pins the substrate parameter $q_0$ by calibrating the quantum of action $\hbar_q^2$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: thurston-volume-additivity.md -->

<!-- FILE_START: mass-volume-factorization.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md).

## Mass-volume factorization

At the particle-mass scale, the formula $\mathfrak{m} = \mathrm{Vol}/\hbar_q^2$ applies the universal categorical density $\rho_q$. At the much lower nuclear-binding scale, the formula refines to use the physical Frobenius packing density $\rho_F$.

**Conjecture.**
*Let $\mathcal{K}$ be the atomic braid of a derived atom. The categorical mass endomorphism factorizes as:*

$$
  \mathfrak{m}_{\mathcal{K}}(q)
  \;=\;
  \rho(q, \mathcal{K}) \cdot V_{\mathrm{hyp}}(\overline{\mathcal{K}}).
$$

*The Frobenius packing density $\rho(q, \mathcal{K})$ is determined by the specific Wedderburn blocks populated by the braid within the Hecke algebra.*

## JSJ refinement

Under the Jaco-Shalen-Johannson decomposition, the factorization restricts to a sum over the hyperbolic pieces $P_i$:

$$
  B(Z, N) \;=\; \sum_{P_i \text{ hyperbolic}}
  \rho_F(P_i) \cdot V_{\mathrm{hyp}}(P_i).
$$

Seifert-fibered torus-knot nucleons contribute zero volume. The hyperbolic pieces containing the closed-shell Borromean links carry the binding energy.

The density $\rho_F(P_i)$ adopts one of two values depending on CPT saturation: $m_e$ for single-chirality configurations, and $2m_e$ when the antiparticle channel activates.

## Supporting evidence

Assigning specific geometric knots and local densities reproduces doubly-magic binding energies within 6.2%. However, the precise assignment map from atom to geometric link requires a per-isotope phenomenological fit. The map remains a conjecture pending rigorous derivation of the atom-to-link translation and local density rules from first principles.
<!-- FILE_END: mass-volume-factorization.md -->

<!-- FILE_START: frobenius-packing-density.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the structurally-wrong leading-order ansatz per [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md).

## Frobenius packing density

The framework distinguishes two scale-dependent densities. The dimensionless substrate drag $\rho_q \approx 102$ governs the particle-mass scale. The physical Frobenius packing density $\rho_F \in \{m_e, 2m_e\}$ governs the nuclear-binding scale.

The Plancherel weights partition the Markov trace across the simple Wedderburn blocks of the Hecke algebra. The atomic link populates a specific subset of these blocks: the symmetric particle channel, the standard propagator channel, and the alternating antiparticle channel.

## The two-density rule

The topological entanglement of the link dictates block activation. The Frobenius density evaluates to:

$$
  \rho_F(\mathcal{K})
  \;=\;
  \begin{cases}
    m_e & \text{single-chirality (alt block empty)}, \\
    2 m_e & \text{CPT-saturated (alt block populated)}.
  \end{cases}
$$

Populating the alt block mandates its antiparticle partner by CPT symmetry, doubling the density.

Topological saturation triggers this threshold. Simple two-body links suppress the alt block. Three-body Borromean entanglement forces cyclic interaction, activating the alt channel. Closed-shell clusters saturate all blocks internally, while two-body inter-cluster bonds revert to the single-chirality density.

Mass computes as the geometric volume scaled by the discrete fractional volume occupied within the Wedderburn module. This categorical structure derives the $\{m_e, 2m_e\}$ threshold directly from the Frobenius pairing without phenomenological tuning.
<!-- FILE_END: frobenius-packing-density.md -->

<!-- FILE_START: crossing-graded-mass-expansion.md -->
## Crossing-graded mass expansion

**Conjecture.**
*Let $\mathcal{K}$ be an atomic braid of $c$ crossings. Fix the universal shape parameter $z_q$ from the Descartes elliptic curve and define the depth scalar $\xi(q) = D(z_q)/\hbar_q^2$. The categorical mass endomorphism admits the crossing-graded expansion:*

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^{c(\mathcal{K})} \xi(q)^n \cdot
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K}).
$$

*The coefficient $\mathfrak{m}^{(n)}_{\mathrm{GB}}$ sums the Gröbner-Shirshov masses over all configurations where exactly $n$ crossings carry volume (lifted) and the remainder are flat.*

## Locality corollary

If lifted-crossing contributions factorize independently—the locality hypothesis—the graded sum collapses exponentially:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  (1 + \xi(q))^{c(\mathcal{K})}.
$$

Each added crossing multiplies the mass. Geometric knots grow exponentially heavier. The expansion formalizes the semiclassical limit of the quantum dilogarithm operator acting at each Hecke generator, ordered by the quantum Planck constant. Taking the classical limit $\xi \to 0$ recovers the baseline Gröbner-Shirshov reduction.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: crossing-graded-mass-expansion.md -->

<!-- FILE_START: lifted-crossing-locality.md -->
## Lifted-crossing locality hypothesis

**Conjecture.**
*The joint mass contribution of lifted crossings factorizes into independent local evaluations:*

$$
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted}})
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in S} \eta(c).
$$

*The local factor $\eta(c)$ depends strictly on the individual crossing $c$, its sign, and the substrate parameter $q$, completely independent of the broader configuration.*

Locality requires that parallel transport of the shape parameter around multiple crossings accumulates zero phase. This vanishing holonomy is guaranteed at the generic physical substrate $q_0$ where the Knizhnik-Zamolodchikov connection is flat. The property fails at roots of unity or at the golden-ratio degeneration threshold, identifying $q_0$ as the distinguished regime supporting exact exponential mass scaling.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It applies $q$-deformation identities over an abstract coefficient ring and specializes them to real-valued observables at $q_0$.
<!-- FILE_END: lifted-crossing-locality.md -->

<!-- FILE_START: mass-categorical-descent.md -->
**Proposition.**
*The mass identity decomposes under the descent involution into a descended component and a transient component:*

$$
  B(Z,N) = B^{\mathrm{desc}}(Z,N) + B^{\mathrm{trans}}(Z,N).
$$

*The descended component resides in the center of the Hecke algebra. The transient component localizes to the exceptional divisors of the brane blow-up.*

**Descended terms.**
The descended elements are Casimir operators corresponding to the volume, pairing, and Wigner terms of the liquid-drop model. They evaluate purely via quantum factorials scaled by Plancherel weights.

**Transient terms.**
The transient elements isolate corrections from the surface boundary, the Coulomb charge locus, the exchange parity locus, and magic-number shell closures. Each corresponds to a specific geometric blow-up evaluated by a quantum dilogarithm correction based on its Schur-Weyl magnetic quantum number. The descent decomposition universally structures both the mass endomorphism and the electromagnetic coupling.
<!-- FILE_END: mass-categorical-descent.md -->

<!-- FILE_START: descended-level-zero.md -->
**Proposition.**
*For every jet level $n \ge 0$, the descended component of the mass integrand equals the invariant base-level holonomy:*

$$
  \bigl\lVert \mathrm{tr}\!\bigl(\hat\tau_n(\alpha^{(n+1)})\bigr) \bigr\rVert
  \;=\;
  \mathfrak{m}(\varrho_0).
$$

*The descended term enters the tower sum exclusively at level 0. All higher levels contribute strictly transient divisor modes.*

The descent involution is idempotent and factors recursively through lower levels. Iterating the trace reduction consistently recovers the base-level cycle mass. Summing the descended component at each subsequent jet level constitutes an invalid double-count of the foundational holonomy.
<!-- FILE_END: descended-level-zero.md -->
