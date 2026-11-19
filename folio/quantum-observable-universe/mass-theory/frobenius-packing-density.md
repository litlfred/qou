> **Superseded.** The scalar aether density $\rho_q = 1/\hbar_q^2$ used below is the structurally-wrong leading-order ansatz; the operator-valued form supersedes it ([mass-endomorphism tower](mass-endomorphism-tower.md)).

## Frobenius packing density

The framework distinguishes two scale-dependent densities. The dimensionless aether drag $\rho_q \approx 102$ governs the particle-mass scale. The physical Frobenius packing density $\rho_F \in \{m_e, 2m_e\}$ governs the nuclear-binding scale.

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

Mass computes as the geometric volume scaled by the discrete fractional volume occupied within the Wedderburn module. This categorical structure is a *candidate* mechanism for the $\{m_e, 2m_e\}$ threshold; it is **not** an established derivation.

The mechanism is refuted under the canonical colour-weighted convention. In the canonical $^4$He decomposition the alternating channel carries zero Frobenius weight, $y_{[1^{12}]} = 0$, with exact two-row dominance — every block of nonzero weight has at most two rows. The CPT argument doubles the density by *populating* the alternating channel, so with that channel structurally empty there is nothing to double. The $\rho_F$ prefactor accordingly remains an open input hypothesis, consistent with [the doubly-magic binding context](magic-A-binding-formula-context.md).
