The left trefoil $T_{2,3}$ and right trefoil $T_{2,3}^{\sigma}$ represent the electron and positron. The chirality assignment is conventional. The physical content is their mirror relationship: $T_{2,3}^{\sigma}$ is $T_{2,3}$ with all crossings reversed.

**Antiparticles from crossing reversal.**

Constructing an antihadron requires replacing every $T_{2,3}$ with $T_{2,3}^{\sigma}$ in the knot formula. Mirroring yields the antiproton:

$$
  \mathfrak{p}^{\sigma}
  = 
  [u^{\sigma}, u^{\sigma}, d^{\sigma}]_p \oplus \mathcal{L}_H
$$

where $u^{\sigma} = T_{2,3}^{\sigma}$ and $d^{\sigma} = (T_{2,3}^{\sigma})^{\sigma} = T_{2,3}$. The crossing energy of $\mathfrak{p}^{\sigma}$ reverses sign, yielding Coulomb charge $Q(\mathfrak{p}^{\sigma}) = -1$.

**Time reversal and the exceptional divisor.**

Traversing the exceptional divisor of the brane tower may reverse the chirality of a trefoil, mapping $T_{2,3}$ to $T_{2,3}^{\sigma}$. This corresponds to a particle traveling backward in time via the Feynman--Stueckelberg interpretation. The fiber adjoint involution ([fiber adjoint involution](#prop:fiber-adjoint-involution)) acts on the weight decomposition and reverses the Reeb flow. Extending this involution to the exceptional divisor provides a mechanism for chirality reversal: the vortex tube reverses winding orientation as it passes through the blow-up.

**Open questions.**

1. **Vortex inversion**: Can a vortex tube in the brane fluid reverse circulation? Classical fluid dynamics results on vortex reconnection require translation to the categorical setting.

2. **Information transfer**: A double chirality reversal (electron $\to$ positron $\to$ electron) constitutes a round-trip through the time-reversed sector. The fiber adjoint involution satisfies $\sigma^2 = \mathrm{id}$, returning the system to its original state. Information preservation across this round-trip depends on the exceptional divisor's monodromy.

3. **The imaginary part**: In the Archimedean realization over $\mathbb{C}$, the substrate parameter $q$ can be complex. The observability axiom restricts $q$ to positive reals. A nonzero imaginary part would contribute a phase to the crossing energy, distinguishing particles from antiparticles without mirror reflection. The full theory may exhibit chirality reversal as a continuous rotation rather than a discrete flip.

4. **CPT from the categorical algebra**: The combined CPT operation (charge conjugation $\sigma$, parity reflection, Reeb flow reversal) should derive from the fiber adjoint involution and the Frobenius structure. The CPT theorem then follows from the QOU involutive axiom.
