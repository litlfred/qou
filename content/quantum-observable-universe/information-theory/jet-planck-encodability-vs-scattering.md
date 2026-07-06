The per-step particle spectrum
([particle spectrum per Planck step](#rem:jet-planck-particle-spectrum))
describes **resolvability**, not creation. This distinction
governs when an actual scattering process can occur.

**Encodability versus scattering.**
The particle table describes **encodability**: which knot
types have enough polynomial degree to be *resolvable* at each
jet order. This is not a scattering process. Step 0 $\to$ Step 1
does not mean "$\gamma + \gamma \to \nu + \nu^{\sigma}$". It means
that the first application of $\nabla_q$ creates horizontal
transport, and the unknot $0_1$ — which requires one winding with
zero crossings — becomes encodable for the first time. The
neutrino is not *produced from* the photon; it becomes
*resolvable* once the jet structure supports winding.

Actual scattering processes require far more structure. Consider
$\gamma\gamma \to \nu\nu^{\sigma}$: in standard QFT this cannot
happen at tree level because neutrinos carry no electric charge,
It requires a box diagram with virtual charged particles and a
$Z^0$ mediator. In the QOU framework the same obstruction
appears accordingly:

1. Photons ($K = \mathbf{1}_{B_4}$ knot-trivial under Markov closure; see [confined-particle](#def:confined-particle)) have no nontrivial knot, hence no crossings
 to Skein-resolve — they cannot couple directly to neutrinos.
2. The process requires **virtual pairs** (trefoil + mirror
 trefoil at brane tower level $A_1$,
 [virtual particles](#rem:virtual-particles-exceptional-divisor))
 to create charged intermediaries that couple to both the
 photon's involutive structure and the weak mediator.
3. The weak mediator $T_{3,5}$
 ([force–knot identification](#rem:force-knot-identification))
 has crossing number $10$ — it first becomes resolvable at
 step 10.
4. The full box topology (two virtual $e^-e^+$ pairs at $A_1$
 plus one $T_{3,5}$ mediation) requires step $\sim 10$–$11$:
 the weak mediator is the bottleneck, and the virtual pair
 structure at $A_1$ may add one additional jet order of
 overhead.

More generally, a scattering process involving a force mediator
of crossing number $c_{\text{med}}$ cannot occur before step
$c_{\text{med}}$, regardless of when the external particles
themselves become encodable. The encodability table gives the
*spectrum*; the scattering step count gives the *interaction
onset*.
