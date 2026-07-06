The Feynman--Stueckelberg interpretation identifies the [positron](#def:positron-knot) as an electron traveling backward in time. In the QOU framework, "time reversal" of a particle means chirality reversal of its constituent knots. It replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$. This operation requires infinite energy in the observable sector for all stable particles.

**Elementary fermions (electron).**
The electron is the left trefoil $T_{2,3}$. No continuous deformation connects $T_{2,3}$ to $T_{2,3}^{\sigma}$ ([trefoil vortex chirality flip](#rem:trefoil-vortex-chirality-flip)). They lie in different connected components of knot space, distinguished by the Jones polynomial. In the observable sector ($q \in \mathbb{R}$, $q \geq 1$), crossing a topological barrier between connected components requires energy

$$
  \mathfrak{E}_{\text{flip}}(e^-) =  +\infty.
$$

No finite-energy process can convert a single electron into a single positron. The only accessible process is [pair creation](#rem:pair-creation-energy) at the exceptional divisor. This creates a new pair at a cost of $2m_e \approx 1.022$ MeV while leaving the original electron unchanged.

**Composite fermions (proton, neutron).**
The proton is a [Borromean baryon](#def:borromean-baryon): $\mathfrak{p} = [\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]_p \oplus \mathcal{L}_H$. It is built from trefoils linked by the Hopf link. Its antiparticle $\mathfrak{p}^{\sigma}$ replaces every $T_{2,3}$ with $T_{2,3}^{\sigma}$ ([chirality remark](#rem:chirality-trefoil-electron-positron)).

The topological protection is equally strong for composites:

1. **Link type is a topological invariant.** The Borromean link $\mathcal{B}_3$ and its mirror $\mathcal{B}_3^{\sigma}$ are distinguished by the Milnor triple linking number $\bar{\mu}(123) = \pm 1$. No Reidemeister sequence connects them.
2. **Each constituent is independently protected.** Every quark trefoil in the proton would need to flip chirality independently. Each flip costs infinite energy.
3. **The Hopf linking is chirality-sensitive.** The Hopf link $\mathcal{L}_H$ binding the quarks has linking number $+1$. Its mirror has $-1$. Reversing this requires destroying and recreating the link.

Therefore:

$$
  \mathfrak{E}_{\text{flip}}(\mathfrak{p}) =  +\infty, \qquad
  \mathfrak{E}_{\text{flip}}(\mathfrak{n}) =  +\infty.
$$

The only way to produce $\mathfrak{p}^{\sigma}$ is pair creation at the exceptional divisor. This costs $2m_p \approx 1876.5$ MeV. Similarly, antineutron creation costs $2m_n \approx 1879.1$ MeV.

**Beta decay is not chirality reversal.**
A neutron can convert to a proton via $\mathfrak{n} \to \mathfrak{p} + e^- + \bar{\nu}_e^{\sigma}$, but this is not time reversal. Beta decay changes the crossing orientation partition of the Borromean link (from $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ to $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$). This is an R-I embedding move that alters binding energy while preserving both the Borromean link type and the chirality of each constituent trefoil. No trefoil flips from left to right. Instead, one quark flavor changes ($\mathfrak{d} \to \mathfrak{u}$) within the same chirality sector.

**Summary.**

| Particle | Chirality reversal energy | Pair creation threshold |
|----------|--------------------------|----------------------|
| Electron $e^-$ | $\infty$ | $2m_e \approx 1.022$ MeV |
| Proton $\mathfrak{p}$ | $\infty$ | $2m_p \approx 1876.5$ MeV |
| Neutron $\mathfrak{n}$ | $\infty$ | $2m_n \approx 1879.1$ MeV |
| Neutrino $\nu$ | $\infty$ | $\approx 0$ (massless to leading order) |

Sending a particle backward in time is indistinguishable from chirality reversal. The infinite energy barrier applies universally to all particles built from trefoil generators. The only physical process that produces the time-reversed partner is pair creation. This creates a new pair from the vacuum at the exceptional divisor without reversing the original particle.
