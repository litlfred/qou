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
