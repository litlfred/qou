The QOU's claim that universal computation is native to the
substrate — articulated by
[`conj:quantum-computational-universality`](#conj:quantum-computational-universality)
and the
[Skein–Turing correspondence](#rem:skein-turing-machine) —
admits a sharp classical/geometric analogue in the work of
Cardona, Miranda, Peralta-Salas, and Presas
\cite{cardona2021} on steady Euler flows.

**The classical result.**
Let $(M^3, g)$ be a closed Riemannian 3-manifold and let
$X$ be a divergence-free vector field on $M$ satisfying the
steady Euler equation
$$
  \nabla_X X = -\nabla p, \qquad \mathrm{div}_g(X) = 0.
$$
By a theorem of Sullivan–Etnyre–Ghrist, after a conformal
change of metric $g \mapsto \tilde g$, any non-vanishing steady
Euler field is — up to rescaling — the **Reeb vector field**
$R_\alpha$ of a contact form $\alpha$ on $M$. Cardona–Miranda–
Peralta-Salas–Presas show that this Reeb field can be chosen
to be **Turing complete** in the strong sense: there is an
explicit construction of a Reeb field whose first-return map on
a Poincaré section simulates an arbitrary Turing machine, and
hence the problem "does the trajectory through a given point
reach a given open set?" is undecidable.

**Translation to the QOU.**
The QOU's
[categorical Reeb derivation](#def:categorical-reeb-derivation)
$\xi_q \colon A \to A$ generates a flow on the state bundle
$\mathcal{S}$ whose horizontal projection is the Reeb vector
field of the contact form $\varTheta$
([Cartan magic formula relation](#def:categorical-reeb-derivation)).
This is exactly the dynamical object Cardona–Miranda–Peralta-
Salas–Presas show is capable of universal computation in the
classical setting. Three structural identifications follow.

1. **Reeb flow = internal clock.** The
   [discrete Planck step](#rem:discrete-planck-step) and the
   [Reeb iterations per Planck](#prop:reeb-operations-per-planck)
   make the Reeb derivation the universe's clock. Cardona et
   al. show this same dynamical object can encode any
   computable function — the clock that ticks the universe is
   also a universal computer.

2. **First-return map = Toffoli action.** Their construction
   places a Turing machine's tape as a horizontal disk in $M$
   and uses the Reeb first-return map to update the head's
   state. The QOU's analogue is the
   [Toffoli transfer matrix](#prop:toffoli-transfer-matrix)
   acting on the
   [observable MTC](#def:observable-mtc): the horizontal
   distribution $\ker(\varTheta)$ carries the tape, and one
   Reeb period implements one Toffoli gate.

3. **Undecidability = observational horizon.** The undecidable
   trajectory problem of \cite{cardona2021}
   is the geometric face of the
   [computational horizon](#def:computational-horizon): no
   finite observer can predict whether a given Reeb orbit
   reaches a given open set, just as no finite QOU observer
   can resolve every section of $\mathcal{S}$.

**What this buys the QOU.**
The categorical Reeb derivation is sometimes criticised as a
formal device — an axiomatised derivation rather than a
geometric flow. The Cardona–Miranda–Peralta-Salas–Presas
construction collapses that gap: the same Reeb-on-contact
structure that the QOU posits algebraically is *already known
classically* to support Turing-complete dynamics in dimension
three. Universal computation is not an emergent property of the
quantum substrate; it is a property of every contact 3-manifold
whose Reeb field admits a sufficiently rich periodic-orbit
structure. The QOU inherits the property from its substrate by
construction.

Tao's general programme on hydrodynamic universality
\cite{tao2019} sits alongside this result: any sufficiently
expressive ODE system embeds in steady Euler flow on some
manifold. The QOU's Reeb derivation is one such embedding, and
the [Skein–Turing machine](#rem:skein-turing-machine) — which
encodes a Turing machine as a braid whose Skein polynomial is
the output — is the discrete (Hecke-algebra) shadow of the
continuous geometric construction.

**Where the conjectural part still lives.**
Cardona–Miranda–Peralta-Salas–Presas prove universality at
*one* fixed metric. The QOU's stronger conjectural claim is
that universality is preserved under the
[q-deformation](#def:quantum-observable-universe) of the
ambient differential geometry — i.e. that the continuous family
of substrate parameters $q \in (1, \infty)$ supports a
continuous family of universal Reeb flows, with the discrete
roots-of-unity specialisations recovering the
[FKLW universal quantum computer](#conj:quantum-computational-universality).
[`conj:quantum-computational-universality`](#conj:quantum-computational-universality)
remains conjectural; the classical $q = 1$ point is now a
theorem.
