The electron is the word $e^- = \sigma_0\sigma_1\sigma_0$ ([electron](#def:electron-knot)) and the positron is its mirror $e^+ = \sigma_0^{-1}\sigma_1^{-1}\sigma_0^{-1}$ ([positron](#def:positron-knot)), the same word with every crossing reversed. The mirror word is the inverse braid, $e^+ = (e^-)^{-1}$. The chirality assignment is conventional. The physical content resides in their mirror relationship.

**Where the chirality lives.** The closures are the positive and negative Hopf links. Unlike the trefoil (the backup electron, which is chiral as an unoriented knot), the Hopf link is amphichiral as an unoriented link: its mirror image is itself with one component reversed. So the electron and positron cannot be told apart by the unoriented link type of their closures. They are told apart by the braid itself and by the orientation of the closure. The writhe, a well-defined invariant of the braid, is $+3$ for $e^-$ and $-3$ for $e^+$, so $e^- \neq e^+$ in $B_3$ (`QOU.BraidKnot.ElectronPositronWrithe.electron_ne_positron`). The linking number of the oriented closure is $+1$ for $e^-$ and $-1$ for $e^+$.

**Antiparticles from crossing reversal.**

Antihadron construction reverses every crossing in the knot formula, $\sigma_i \mapsto \sigma_i^{-1}$. Mirroring yields the antiproton:

$$
  \mathfrak{p}^{\sigma}
  = 
  [u^{\sigma}, u^{\sigma}, d^{\sigma}]_p \oplus \mathcal{L}_H
$$

Each quark is an unknot strand carrying one crossing letter ([knot formula table](#rem:knot-formula-table)): $\sigma_i$ for $u$ and $\sigma_i^{-1}$ for $d$. Mirroring reverses the letter, so $u^{\sigma}$ carries $\sigma_i^{-1}$ and $d^{\sigma}$ carries $\sigma_i$. The crossing energy of $\mathfrak{p}^{\sigma}$ reverses sign. This yields Coulomb charge $Q(\mathfrak{p}^{\sigma}) = -1$.

**Time reversal and the exceptional divisor.**

Traversing the exceptional divisor of the brane tower reverses every crossing of the electron word. This maps $e^-$ to $e^+ = (e^-)^{-1}$. The Feynman--Stueckelberg interpretation maps this to a particle traveling backward in time. The fiber adjoint involution acts on the weight decomposition and reverses the Reeb flow. Extending this involution to the exceptional divisor provides a mechanism for chirality reversal. The vortex tube reverses winding orientation passing through the blow-up.

**Open questions.**

1. **Vortex inversion**: Reversing circulation of a vortex tube in the brane fluid requires translating classical fluid dynamics results on vortex reconnection to the categorical setting.

2. **Information transfer**: Double chirality reversal (electron $\to$ positron $\to$ electron) constitutes a round-trip through the time-reversed sector. The fiber adjoint involution satisfies $\sigma^2 = \mathrm{id}$. This returns the system to its original state. Information preservation across this round-trip depends on the exceptional divisor's monodromy.

3. **The imaginary part**: The Archimedean realization over $\mathbb{C}$ permits a complex substrate parameter $q$. The observability axiom restricts $q$ to positive reals. A nonzero imaginary part contributes a phase to the crossing energy. This phase distinguishes particles from antiparticles without mirror reflection. The full theory models chirality reversal as a continuous rotation rather than a discrete flip.

4. **CPT from the categorical algebra**: The fiber adjoint involution and the Frobenius structure derive the combined CPT operation (charge conjugation $\sigma$, parity reflection, Reeb flow reversal). The QOU involutive axiom implies the CPT theorem.
