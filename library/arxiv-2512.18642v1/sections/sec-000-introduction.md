---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
doc_brief: "A Hidden Quantum Markov model framework for — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af- fleck–Kennedy–Lieb–Tasaki (AKLT) state—a cornerstone example of a"
---
Hidden Markov models [1] are recognized as powerful stochastic processes due to their ability
to capture complex correlations, with broad applications across various domains [2]—especially
in machine learning tasks [3], where algorithmic implementations [4, 5] have achieved significant
success. Several proposals have been made to generalize hidden Markov models into the quantum
setting [7, 8, 9]. Namely, with the rising interest in quantum computing and quantum machine
learning [10] but a suitable generalized probabilistic picture is remained missing [11]. Recently,
an algebraic approach to HQMM within the framework of quantum probability has been sug-
gested [12], offering promising features such as entanglement [13] and the ability to represent an
important class of matrix product states as observations [14]. This approach defines a HQMM as
a hidden system—described by a Quantum Markov Chain (QMC) [15, 16], and an observation
system strongly correlated with it. Information is encoded through sequences of hidden transi-
tions and emission transition expectations, whose dual maps are quantum channels [17], these
represent the fundamental building blocks of the HQMMs framework. It is worth noting that
QMCs serve as the quantum generalization of classical Markov chains and offer a powerful frame-
work for describing the dynamics of quantum systems. They play a particularly foundational role
in the theory of finitely correlated states on quantum spin chains [18, 19, 20]. Beyond this core
1
arXiv:2512.18642v1  [quant-ph]  21 Dec 2025
application, QMCs find broad use in diverse areas such as quantum control [21], quantum informa-
tion theory [22], quantum software development [23], and quantum communication systems [24].
A particularly important subclass, quantum walks, has proven instrumental in developing novel
quantum algorithms [25].
The AKLT model, introduced in [26, 27], provides a paradigmatic example of a gapped spin-
1 system with an exactly solvable ground state described by a Matrix Product State (MPS)
[18]. It explicitly satisfies Haldane’s conjecture [28], which distinguishes integer-spin antiferro-
magnetic chains—possessing a gapped spectrum (the “Haldane gap”) and exponentially decaying
correlations—from their gapless, power-law-correlated half-integer counterparts. Beyond confirm-
ing Haldane’s conjecture, the AKLT state has emerged as a foundational model for SPT order
[29, 30]. This stems from its elegant construction, where each physical spin-1 site arises from
projecting two virtual spin-½degrees of freedom into the symmetric triplet subspace, revealing a
hidden layer of entanglement. At the virtual level, the system is constructed on auxiliary spin-½
spacesH 1
2
∼= C2, where the physicalSO(3) rotation symmetry is realized projectively through the
double-cover mapSU(2)→SO(3). Formally, a groupGof symmetry acts onH 1
2
via a projective
unitary representationπ:G→U(H 1
2
), characterized by a non-trivial 2-cocycleω:G×G→U(1).
Its cohomology class [ω]∈H 2(SO(3),U(1)) ∼= Z2 directly encodes theZ 2 topological index of
the SPT phase [31]. This algebraic structure arising from the mismatch between the virtual
projective representationπand the physical spin-1 representationρ:G→ U(H 1) acting on
H1∼= C3—underpins the robustness of fractionalized spin-½edge modes and defines the SPT
nature of the AKLT phase.
Previous works have shown a deep connection between quantum Markov chains on infinite
tensor product of matrix algebras and finitely correlated states including matrix product states
ansatz[18]. Moreover, recent algebraic approaches, framed within infinite tensor products of C*-
algebras [32], have been used to classify topological order in solid-state physics [33, 34, 35].
In this context, this work establishes a HQMM framework for the AKLT spin chain, capturing its
entanglement structure and SPT order within a quantum probabilistic formalism. We construct
the generative triplet ΞAKLT = (ϕ0,EH,EO,H), whereϕ 0 :B(H 1
2
)→Cinitializes the hidden spin-½
system,E H :B(H 1
2
)⊗B(H 1
2
)→B(H 1
2
) governs its hidden dynamics, andEO,H :B(H 1
2
)⊗B(H 1)→
B(H 1
2
) encodes theG-equivariant emission transition to the physical spin-1 space. The sequential
quantum dynamics is defined by the transition map
EXℓ,Yℓ(·) =E H
(
EO,H(Xℓ⊗Yℓ)⊗·
)
.
Within this framework, we demonstrate the following principal results: Theorem 3.4 pro-
vides an explicit HQMM decomposition of the AKLT state, determining virtual-physical cor-
relations within the model. We explicitly characterize the conditional dependency of physical
observations on the underlying Markov process through the AKLT quantum channel. Theo-
rem 4.1 studies the entanglement structure of the underlying Markov dynamics. It establishes
that the Choi–Jamio/suppress lkowski stateJ(E∗
H) of the encoding channelE ∗
H is a pure, maximally entan-
gled bipartite state between the reference and output spaces. The resulting entanglement entropy
S(ρR) =S(ρ B) = 1 ebit confirms that the hidden dynamics fully encode the chain’s entanglement
structure [39, 40]. Theorem 5.1 explicitly formulates theG-covariance of the emission process,
proving thatE O,H isG-equivariant. The covariance condition
EO,H
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g) †
)
=π(g)E O,H(X⊗Y)π(g) †
holds with respect to the projective virtual representationπ:G→ U(H 1
2
) and the physical
representationρ:G→U(H 1), thereby embedding the SPT index in the HQMM’s symmetry
structure.
This framework translates the topological and entanglement properties of the AKLT chain
into a well-defined quantum stochastic process. Our approach directly connects tensor network
2
states [41] to quantum models [42], with promising implications for quantum machine learning
and quantum computation architectures. Natural extensions include multi-dimensional general-
izations to cluster states and projected entangled pair states [37, 43], with promising implications
for measurement-based quantum computation [44, 45] makes them prime candidates for this
framework. The present work thus opens a pathway to investigating solid-state models through
hidden quantum Markov dynamics, namely with the increasing efficiency of algebraic methods in
understanding topological order [53, 34] .
We begin in Section 2 with the necessary background and definitions. Building on this foun-
dation, Section 3 is devoted to constructing the HQMM for the AKLT chain. With this model
established, we then explore the entanglement properties of its hidden dynamics in Section 4. Fur-
thermore, in Section 5, we reveal how this HQMM framework naturally encodes the Symmetry-
Protected Topological (SPT) order characteristic of the AKLT state. We synthesize our findings
and offer conclusions in Section 6.
