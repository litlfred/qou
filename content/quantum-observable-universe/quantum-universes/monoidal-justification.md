Before stating the formal definition, we pause to explain why a rigid
:refterm[monoidal category]{#monoidal-category} is the inevitable starting point for any theory of
quantum-geometric structure. Two independent lines of reasoning
converge on the same conclusion.

**Information-theoretic necessity.** Coecke and Kissinger
\cite{coecke2017} demonstrate that the tensor product $\otimes$ is
not an algebraic convenience but the *grammar* of any physical system
possessing inputs and outputs. The moment one demands a compositional
language — where composite systems are described by combining
subsystems, and processes compose both sequentially (via $\circ$) and
in parallel (via $\otimes$) — one is forced into a :refterm[monoidal category]{#monoidal-category}.
Rigidity (the existence of duals) then follows from the requirement
that every process be reversible at the level of type structure: a
system of type $V$ can always be "bent around" to become an input of
type $V^{\vee}$, which is precisely the content of the snake
identities.

**Physical reconstruction from superselection.** From an entirely
different direction, Haag's algebraic quantum field theory
\cite{haag1996} arrives at the same structure through the analysis of
superselection sectors. In the DHR (Doplicher--Haag--Roberts)
framework, the category of superselection sectors of any reasonable
quantum field theory is automatically a rigid braided monoidal
category: the tensor product encodes the composition of charges, the
braiding encodes the exchange statistics of sectors, and rigidity
encodes the existence of anticharges (conjugate sectors). The monoidal
structure is not imposed — it is *forced* by the locality and
covariance axioms of quantum physics.

These two perspectives — one from the logic of processes, the other
from the geometry of measurements — make the rigid monoidal framework
a uniquely well-motivated foundation. The definition that follows
captures exactly this structure.
