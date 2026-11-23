> *Je pense, donc je suis.*
> — René Descartes, *Discours de la méthode* (1637)

The starting point is a collection of observations about how an
observer interacts with the world. Colours are seen, and three of them
mix to produce white. An observer moves around, rotates, and looks
from different angles, yet the things measured do not depend on where
the observer stands or which way it faces. Time flows in one
direction, and observers are carried along with it. Three-fold structure recurs throughout nature — three
colours, three generations of matter, three-fold chirality — too
insistently to be coincidence; it asks for explanation rather than
stipulation. Multiple observers share the same world; they do not
each illuminate a private universe but navigate a common landscape.

Some observations run deeper. Observers measure, record, and compare,
and the comparisons are consistent: there is a pairing between what is
observed and the instruments used. Smooth change is the rule across
scales, so linear approximation describes the world from planetary
orbits to particle scattering, with integration and differentiation
as its native operations. Things occupy space, and that space can be
measured — the universe has *volume*. There is the experience of
choice: an observer decides what to measure and when, and the decision
shapes what is recorded. Whether that experience reflects something in
the structure of the world, or only ignorance of it, is a question
rather than a premise; the paper returns to it when observation is
treated as a process inside the structure
([Measurement and Observation](#chap:measurement-observation)). Even
the capacity for computation — to reason, count, and calculate —
seems woven into the fabric rather than added on.

One assumption is deliberately left out: that the constants of nature
are constant. A physical theory usually takes its constants as fixed
numbers, measured once and then held still. If they are allowed to
vary — not arbitrarily, but in a controlled, algebraic way — how does
that change the mechanics, or more precisely the mechanics of
observation? That is the question the paper asks, and the
[substrate parameter](#sec:introduction-substrate-parameter) below is
the form it takes.

Einstein taught that geometry and mass are bound together: spacetime
is not a passive stage on which matter performs, but a participant
shaped by the matter it contains. The motivating hope here is that a
similar bond holds one level down, between the *algebra* of processes
and the mass and interactions of what those processes describe. The
algebraic counterpart of curvature is torsion — the failure of two
operations to commute — and the paper asks how much of the structure
of particles that failure can carry. Gravity itself is taken up in
its own chapter
([Gravity and Spacetime Emergence](#chap:gravity-spacetime-emergence)).

Heisenberg wrote that "what we observe is not nature in itself but nature exposed to our method of questioning" \cite{heisenberg1958}. So the question is not what
the universe *is* but what its mechanics *do* — how its processes
compose and transform. Wigner found the effectiveness of mathematics
in describing nature "unreasonable", a "wonderful gift which we neither understand nor deserve" \cite{wigner1960}. The approach of this paper is to take
that unreasonableness not as a mystery to be explained but as a
principle to be *axiomatised*: the paper posits that the observable universe
*is* the mathematical structure its own observations force, so that
the fit between mathematics and the world is built in rather than
discovered.

The natural home for such a structure is category theory, the study
of how processes combine. A category records objects and the
processes (morphisms) between them, and says how processes compose;
a :refterm[monoidal category]{#monoidal-category} also says how two
processes run side by side. The language describes structure and
transformation without committing to any picture of what the
underlying objects "really are". The guiding example is familiar from
a first course on Lie groups: the finite-dimensional representations
of $\mathrm{SU}(2)$, with their tensor products, duals, and the
forgetful map that remembers only the underlying vector space. From
that data alone the Tannaka–Krein theorem reconstructs the group
itself ([Tannaka–Krein reconstruction](#prop:tannaka-krein-reconstruction));
the symmetry is recovered from how its representations compose rather
than assumed in advance.

The central thesis is that the everyday observations above, once
stated carefully, single out one kind of structure: a category of
processes rich enough to integrate, to differentiate, and to be
measured against. Each observation becomes one ingredient. Duality —
every process has a reverse — is the rigidity of the category.
Consistent measurement is a *fibre functor* $\tau$, which sends each
object to the vector space an instrument reads. Integration is a
*trace*: on the $\mathrm{SU}(2)$ example it is exactly the Haar
integral over the group ([Frobenius pairing on $\mathrm{SU}(2)$](#ex:frobenius-pairing-su2)).
Volume is the requirement that this trace be non-degenerate. A
structure that meets all of these requirements, including that its
states be observable and its measurements consistent, is called
a **quantum observable universe** (QOU)
([definition](#def:quantum-observable-universe)). The force of the
thesis is that the observations *determine* the ingredients; nothing
else is added by hand.

The categorical language then recovers, as internal pieces of the
structure, the concepts that describe a universe's mechanics. The
Lagrangian is a trace and the action is an integral
([categorical action](#def:categorical-action)); curvature, the gauge
field, and the matter current are specific processes in the category;
the Dirac operator is a connection twisted by the system's own
internal time-flow ([categorical Dirac operator](#def:categorical-dirac-operator)).
Each is a construction the axioms allow, not an entry borrowed from
the classical dictionary.

Noether taught that every continuous symmetry of a physical system
yields a conserved quantity: invariance under rotation gives angular
momentum, under translation in time gives energy, under a change of
gauge gives charge. Her theorem is the bridge from the symmetries that are
*observed* to the quantities that are *measured*, and it suggests why a trace
should be the notion of integration here: a trace is a device for
extracting one number from a symmetric process. Once the structure is
deformed by the parameter of the next section, the bridge bends
rather than breaks: the conserved quantities acquire corrections, and
some identities that held exactly become approximate ones
([Noether's theorem in the $q$-deformed setting](#rem:noether-theorem-callout)).
