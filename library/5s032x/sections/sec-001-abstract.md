---
doc_id: 5s032x
doc_title: "The standard model symmetry and qubit entanglement"
section_id: sec-001-abstract
section_title: "Abstract"
section_number: null
pages: 1-5
source_pdf: 5S032X.pdf
source_sha256: 17761383781f7bdc
doc_brief: "The standard model symmetry and qubit entanglement — quantum description."
---
Indeed, the links appear so deep that Susskind has proposed to generalize ER =EPR , the conjecture that quantum
entanglement is equivalent to wormholes in spacetime [6], to GR = QM, proposing that ‘where there is quantum
mechanics, there is also gravity’ [7]. Hence, a quantum system does not merely come equipped with a geometry, but
that geometry is dynamical, approximating general relativistic spacetimes in a classical limit.
The origin of this idea can be traced to work of Jacobson, who has shown that Einstein’s equations can be recovered
from thermodynamics in the presence of black hole horizons [8] (see also [9, 10]). These arguments rely essentially
on the area law-scaling of the Bekenstein-Hawking entropy of black holes [11]. This scaling is also observed, in many
cases, for the entanglement entropy of quantum systems—indeed, it has been proposed to explain black hole entropy
as the entanglement entropy of degrees of freedom across the horizon [12, 13].
Along a different thread, van Raamsdonk has suggested that entanglement may be responsible for spacetime connec-
tivity [14, 15]. In the AdS/CFT correspondence, the Ryu-Takayanagi formula [16] relates the entanglement between
different patches of the conformal field theory on the boundary of Anti-de Sitter space with the area of a surface
partitioning the AdS-space; if the entanglement between both goes to zero, the space partitions into two disconnected
regions.
Combining these perspectives, the linearized Einstein equations follow from ‘entanglement thermodynamics’ for
perturbations of the AdS-spacetime [17, 18]. While the bulk of this work assumes the AdS/CFT-correspondence,
Jacobson has shown that a derivation of the full Einstein equations is possible without assuming an AdS-background,
given a condition of entanglement equilibrium [19].
A way to think about this is in terms of a graph, each node of which is itself an abstract element of quantum
information—a qubit, or perhaps more generally, some finite-dimensional Hilbert space—that carries no spatial in-
∗ Jochen.Szangolies@gmx.de
https://doi.org/10.32388/5S032X
2
formation itself, with the edges encoding the entanglement structure of the whole system. Geometry, then, must be
reconstructed from this basic picture.
This is, essentially, the proposal made by Cao and Carroll [20] (see also [21]). Starting from a graph as described
above, they show that the metric structure of spacetime, as well as the linearized Einstein equations, can be obtained,
using an argument closely related to that of Jacobson.
Intriguingly, there appears a natural bipartitioning of the entanglement degrees of freedom in proposals such as the
one in Ref. [20]. Recall that the area-law scaling of entanglement entropy plays a crucial role in recovering spacetime.
Such a scaling is typically only observed in a very special class of states, such as the ground states of local gapped
many-body systems [22]. In Ref. [20], a generalized notion termed ‘redundancy-constrained (RC) states’ is used, which
correspond to graphs such that the entanglement entropy can be computed by summing over all the contributions of
nearest-neighbor links over a given bipartition of the system into a region R and its complement, ¯R. Explicitly,
SRC(R) = 1
2
X
i∈R,j∈ ¯R
I(i :j), (1)
where I(i :j) is the quantum mutual information between nodes i and j (see Fig. 1).
R ¯R ∂R
FIG. 1. The entanglement entropy of a region R across its boundary ∂R is computed by summing up the contributions of
entanglement ‘links’ cut by the boundary. For a state with ‘short-range’ entanglement, this yields an area law.
One can now consider states that only approximately satisfy this constraint. Then, the entanglement entropy
receives a subleading correction
S(R) =SRC(R) +Ssub(R), (2)
which can be associated with long-range entanglement or excited degrees of freedom over and above the vacuum. This
subleading correction may then be associated to the entanglement entropy of an emergent gauge theory [23].
Along similar lines, Cao [24], following work by Harlow [25], has proposed to interpret the splitting of contributions
to the entanglement entropy in terms of quantum error correcting codes (QECC)—specifically, QECC protecting
against subsystem erasure. There, the information in some state ρ is nonlocally encoded into ˜ρ in such a way as to
be protected against erasure of the subsystem ¯R. Thus, there exists a decoding unitary on R
UR ˜ρU†
R =ρ⊗χ, (3)
whereχ is the generically entangled state of the remaining degrees of freedom, that restores the encoded information
ρ. Thus, the full information encoded on RS ¯R can be recovered from R alone. This yields for the entropy of
˜ρR = Tr¯R(˜ρ):
S(˜ρR) =S(χ) +S(ρ), (4)
3
R ¯R ∂R
FIG. 2. A state with additional long-range entanglement, or entanglement due to a state ‘encoded’ into it in the sense of
quantum error correction, receives subleading corrections to the entanglement entropy from these additional terms.
where S(χ) can be interpreted as the geometric, area-law contribution to the entropy, and S(ρ) in turn as stemming
from the emergent matter fields.
It is here that our investigation begins. If dynamical spacetime emerges from the area-law contribution to the
entanglement, it seems a natural proposal to investigate the emergence of matter degrees of freedom, together with
their symmetries, from the entanglement yielding subleading corrections to the entropy—the ‘logical’, encoded state
ρ, on the above view. However, we stress that this motivation is, at this point, heuristic; the discussion in the sequel
is independent of this interpretation.
Our main result is then to show how to use a construction of Dubois-Violette and Todorov [26, 27], as extended and
clarified by Krasnov [28], to derive the exact symmetry and degrees of freedom of (half a generation of) Standard Model
fermions from the entanglement properties of a three-qubit state. This proceeds by means of a kind of ‘dimensional
reduction’: a three-qubit state can be interpreted as yielding a 9 + 1-dimensional spacetime, which can be broken
down to 3 + 1 dimensions in a way left invariant by precisely the group transformation of SU (3)×SU (2)×U(1)/Z6,
the exact gauge symmetry of the Standard Model.
One can think of this in the following way. Standard, complex quantum mechanics can, as noticed long ago by
von Weizs¨ acker [29] (whose ‘ur-theory’ [30] might be considered the first example of a ‘quantum first’-approach), be
associated with 3 + 1-dimensional spacetime. In more modern times, it has been shown that the three-dimensionality
of position space and the state-space of elementary quantum systems, and the necessity of their correspondence, follow
from information-theoretical considerations [31, 32], and indeed, even the Lorentz transformations can be obtained
by considering the relation between different experimenters’ descriptions [33].
These arguments can be generalized to quantum theory over the quaternions H, leading to a 5 + 1-dimensional
spacetime. Furthermore, extending to the octonions O, we obtain 9 + 1 dimensions [34] (which are, not coincidentally,
precisely the dimensions in which a supersymmetric Lagrangian exists [35, 36]).
These spacetimes can then be broken down to 3+1 dimensions by simply singling out a preferred complex structure—
that is, fixing a split of H into C⊕ C and O into C⊕ C3. It is then the observation of Dubois-Violette, Todorov,
and Krasnov [26–28] that these splits are left invariant by SU (2)×U(1)/Z2 for the quaternionic case and SU (3)×
SU (2)×U(1)/Z6 for the octonionic one. This is then a ‘quantum first’ realization of the proposal due to Kaluza [37]
and Klein [38, 39] that higher-dimensional spacetime theories can lead to gauge fields in lower dimension.
The appeal to higher division-algebraic generalizations of quantum theory has a long and distinguished history.
Of note, Finkelstein, Jauch, Schiminovich and Speiser provided the first example of quaternionic quantum theory in
1962/1963 [40, 41]—the latter of which is remarkable for introducing a mass-generating mechanism for an SU (2)-
gauge theory by means of a quaternion-imaginary dynamical field playing much the same role as the Higgs field in
the later explanation of electroweak symmetry breaking.
Applications of the octonions to particle physics date back to work by G¨ unaydin and G¨ ursey, who first proposed
using them to model the strong force [42]. The attractivity of appealing to the (normed) division algebras C, H
4
and O comes from the observation that the unit complex numbers form the group U(1), the electromagnetic gauge
group, while the unit quaternions form SU (2), the gauge group of the weak interaction. Of course, due to their non-
associative nature, the unit octonions form no group at all—but still, their automorphism group is the exceptional
G2, which containsSU (3) (the gauge group of the strong interaction) as a subgroup—in fact, the subgroup preserving
one octonion imaginary direction, and thus, singling out a preferred complex structure.
This has led to an alternative, algebraic approach to models of particle physics. Dixon, for instance, focuses on the
algebra D = R⊗ C⊗ H⊗ O (where the factor of R is technically redundant and only included for aesthetic purposes),
and uses it to build a model incorporating the complete matter and force content of the Standard Model [43]. More
recently, Furey [44, 45] has proposed her unified theory of ideals, drawing on actions of the Dixon algebra D on itself.
Stoica [46] has proposed a construction in which the Standard Model emerges from the complex Clifford algebra Cℓ6,
with the color- and electromagnetic symmetry appearing in the same way as in the model of Furey. Also of note
here is the model of Morita [47–49], giving a quaternionic version of the theory of electroweak interactions, and an
octonionic QCD. For a more thorough review of this ‘algebraic’ approach to the Standard Model, see [46].
The final piece of the puzzle then is the origin of quaternionic/octonionic quantum theory. Here, we appeal
to work by Mosseri and Dandoloff [50, 51] and Bernevig and Chen [52]: entangled states of two qubits can be
written in terms of quaternionic spinors—more accurately, the state space of a two-qubit system is given by the
quaternionic Hopf fibration (just as the state space of a single qubit, the Bloch sphere, is the complex Hopf fibration).
Likewise, three-qubit systems can be considered as octonionic spinors, whose state space is given by the octonionic
Hopf fibration. This also provides the point of origin for the emergence of the Standard Model gauge group: the
equivariance group of the octonionic Hopf fibration is Spin(9), whose subgroup respecting the splitting O≃ C⊕ C3
is just SU (3)×SU (2)×U(1)/Z6 [28].
Furthermore, the Hopf maps in each case are entanglement sensitive—disentangling each qubit results in the space
decomposing into a product of individual qubit state spaces. The information within separable states is then fully
representable within ordinary, empty 3 + 1-dimensional spacetime; but entanglement introduces additional. ‘internal’
degrees of freedom. The heuristic picture we propose then is one where 3+1 dimensional spacetime with its dynamics
emerges from the area-law contribution to the entanglement of a quantum state, while area-law violating corrections
can be viewed as ‘bubbles’ of higher-dimensional spacetime, which, upon reduction to 3 + 1 dimensions, which can be
interpreted as singling out a preferred tensor product decomposition, add matter and gauge degrees of freedom.
The origin of the Standard Model symmetry and its attendant idiosyncrasies has been an active topic of research
since its inception. Grand Unified Theories (GUTs) have proposed to embed its gauge group into a larger one, re-
covering its phenomenology after appropriate symmetry breaking; however, there is a large number of such schemes
conceivable, with little guidance for choosing among them. The division algebraic approach reduces this embar-
rassment of riches somewhat, but even here, finding a unique model has been challenging, and the reason for their
appearance—what, if anything, singles them out as relevant to the description of elementary particles—is not well
understood.
Our main aim here is then to provide a physical picture that one might hope to offer some guidance. In particular,
as we will see, the division algebraic description is singled out by the geometry of qubit Hilbert spaces, potentially
significantly reducing the search space for theory-building. Furthermore, by building a bridge between the ‘quantum
first’ and division algebraic programs, we hope that the insights of each may help stimulate research within the other,
in particular by introducing the possibility of emergent matter (and gauge) degrees of freedom, but more generally
by providing a unified framework for both.
The remainder of this article is structured as follows. In Sec. II, we introduce the basic template the subsequent
three sections will follow. First, we give a brief introduction to the scenario, starting with a single qubit; then, in
Sec. II A, we present the connection of complex quantum mechanics with 3+1-dimensional spacetime. In the following
Sec. II B, we introduce the complex Hopf fibration, and show its relation to the state space of single qubits. Then, in
Sec. II C, we illustrate the importance of the group Spin(3) as the complex Hopf map’s equivariance group.
In Sec. III, the construction is generalized to two qubits, and quaternions, showing the connection to 5 + 1-
dimensional spacetime (III A), and the quaternionic Hopf fibration (III B). In Sec. III C, then, it is illustrated how the
groupSU (2)×U(1)/Z2 emerges from the subgroup of Spin(5) leaving a quaternion imaginary direction invariant. In
Sec. IV, the construction is analogously generalized to the octonions and three qubits, 9 + 1-dimensional spacetime
(IV A), the octonionic Hopf fibration and its relevance for three-qubit entanglement (IV B), and finally, the emergence
of SU (3)×SU (2)×U(1)/Z6 as leaving a choice of complex structure invariant (IV C).
In Sec. V, we will then speculate about an extension of the model to incorporate a full generation of Standard
Model fermions by generalizing to the four-qubit case, which will also allow us to include massive states in our model,
and yield a possible natural explanation for the chirality of the weak force. Finally, we conclude in Sec. VI, and
propose some directions of further development, such as the incorporation of a Higgs mechanism by taking account
of the non-triviality of the embedding of the fibre in the Hopf fibration.
5
