The QOU asserts that universal computation is native to the substrate. This claim, articulated by [`conj:quantum-computational-universality`](#conj:quantum-computational-universality) and the [Skein–Turing correspondence](#rem:skein-turing-machine), admits a sharp geometric analogue. Cardona, Miranda, Peralta-Salas, and Presas \cite{cardona2021} prove a corresponding result for steady Euler flows.

**The classical result.**
Let $(M^3, g)$ be a closed Riemannian 3-manifold. Let $X$ be a divergence-free vector field on $M$ satisfying the steady Euler equation

$$
  \nabla_X X = -\nabla p, \qquad \mathrm{div}_g(X) = 0.
$$

By a theorem of Sullivan–Etnyre–Ghrist, a conformal change of metric $g \mapsto \tilde g$ maps any non-vanishing steady Euler field to the Reeb vector field $R_\alpha$ of a contact form $\alpha$ on $M$, up to rescaling. Cardona–Miranda–Peralta-Salas–Presas show that this Reeb field can be chosen to be strongly Turing complete. They construct a Reeb field whose first-return map on a Poincaré section simulates an arbitrary Turing machine. Consequently, determining whether a trajectory reaches a given open set is strictly undecidable.

**Translation to the QOU.**
The QOU's [categorical Reeb derivation](#def:categorical-reeb-derivation) $\xi_q \colon A \to A$ generates a flow on the state bundle $\mathcal{S}$. Its horizontal projection precisely yields the Reeb vector field of the contact form $\varTheta$ ([Cartan magic formula relation](#def:categorical-reeb-derivation)). This is exactly the dynamical object that achieves universal computation in the classical setting. Three structural identifications follow.

First, Reeb flow acts as the internal clock. The [discrete Planck step](#rem:discrete-planck-step) and the [Reeb iterations per Planck](#prop:reeb-operations-per-planck) cast the Reeb derivation as the universe's clock. Cardona et al. show this identical dynamical object can encode any computable function. The clock that drives the universe is simultaneously a universal computer.

Second, the first-return map serves as a Toffoli action. The classical construction places a Turing machine's tape on a horizontal disk in $M$, using the Reeb first-return map to update the head's state. In the QOU, the analogue is the [Toffoli transfer matrix](#prop:toffoli-transfer-matrix) acting on the [observable MTC](#def:observable-mtc). The horizontal distribution $\ker(\varTheta)$ carries the tape, and one Reeb period implements exactly one Toffoli gate.

Third, undecidability guarantees an observational horizon. The undecidable trajectory problem of \cite{cardona2021} (extended to stationary Beltrami fields in \cite{cardona2023}) represents the geometric face of the [computational horizon](#def:computational-horizon). No finite observer can predict whether a given Reeb orbit reaches a given open set. Correspondingly, no finite QOU observer can resolve every section of $\mathcal{S}$.

**Consequences for the QOU.**
The categorical Reeb derivation is occasionally dismissed as an axiomatised formalism rather than a geometric flow. The Cardona–Miranda–Peralta-Salas–Presas construction collapses this gap. The Reeb-on-contact structure posited algebraically by the QOU is classically proven to support Turing-complete dynamics in dimension three. Universal computation is not a late emergent property of the quantum substrate; it is native to every contact 3-manifold possessing a sufficiently rich periodic-orbit structure. The QOU inherits this property by construction.

Tao's programme on hydrodynamic universality \cite{tao2019} parallels this result. Any sufficiently expressive ODE system embeds in steady Euler flow on some manifold. The QOU's Reeb derivation constitutes one such embedding. The [Skein–Turing machine](#rem:skein-turing-machine), encoding a Turing machine as a braid whose Skein polynomial yields the output, is simply the discrete Hecke-algebra shadow of this geometric construction.

**Location of the conjectural part.**
Cardona–Miranda–Peralta-Salas–Presas establish universality at one fixed metric. The QOU extends this claim: universality survives the [q-deformation](#def:quantum-observable-universe) of the ambient differential geometry. We conjecture that the continuous family of substrate parameters $q \in (1, \infty)$ supports a continuous family of universal Reeb flows, where discrete roots-of-unity specialisations recover the [FKLW universal quantum computer](#conj:quantum-computational-universality). Thus, [`conj:quantum-computational-universality`](#conj:quantum-computational-universality) remains conjectural, while the classical $q = 1$ limit stands as a theorem.
