---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for"
section_id: sec-002-hidden-quantum-markov-models
section_title: "Hidden Quantum Markov Models"
section_number: null
pages: 3-4
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
doc_brief: "A Hidden Quantum Markov model framework for — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af- fleck–Kennedy–Lieb–Tasaki (AKLT) state—a cornerstone example of a"
---
LetHandKbe two finite-dimensional Hilbert spaces and letB(H) andB(K) be the algebras
of bounded operators over the Hilbert spacesHandK, respectively. A map isEfromB(H) to
B(K) is said to becompletely positiveif all its matrix amplifications
E:M n(A)→M n(B),[a ij]↦→[Φ(aij)]
preserve positivity for everyn∈N. Aquantum channelis a completely positive, trace-preserving
map Φ :A→Bthat describes general physical transformations of quantum states. The funda-
mental duality between state and observable evolution is encoded in the dual map Φ∗ :B∗→A∗,
defined via the relation
Tr(Φ(ρ)X) = Tr(ρΦ∗(X)) for allρ∈A ∗, X∈B.
This establishes the precise correspondence between the Schr¨ odinger picture (state evolutionρ↦→
Φ(ρ)) and the Heisenberg picture (observable evolutionX↦→Φ∗(X)).
Atransition expectationE:A⊗B→Ais a completely positive, identity-preserving map
that generalizes the notion of conditional expectation to open quantum systems. The duality
between quantum channels and transition expectations manifests through the adjoint relationship:
ifEis a transition expectation, then its dualE ∗ :A ∗→(A⊗B) ∗ defines a quantum channel
when properly normalized. This framework provides the mathematical foundation for describing
emission, absorption, and general interaction processes in quantum information theory.
HQMM provides a generative description of quantum stochastic processes through a bipartite
structure separating hidden dynamics from observable outputs. Formally, an HQMM is defined
as a state on the quasi-local algebraA H,O = (B(H)⊗B(H 1))⊗N, representing an infinite bipar-
tite quantum system whereA H =B(H) ⊗N describes the hidden system andA O =B(H 1)⊗N
represents the observable output system [12]. The model is specified by agenerative triplet
Ξ = (ϕ0,EH,EO,H), where:
•ϕ 0 :B(H)→Cis an initial state on the hidden algebra;
•E H :B(H)⊗B(H)→B(H) is a CPIP map governing hidden system dynamics;
•E O,H :B(H)⊗B(H 1)→B(H) is a CPIP map encoding observable emission.
3
The conventional HQMM follows quantum causality where measurement precedes state evo-
lution. For sequencesX= ⨂n
m=0Xm andY= ⨂n
m=0Ym, the state is:
φH,O(X⊗Y) =ϕ 0◦EX0,Y0◦EX1,Y1◦···◦E Xn,Yn(h),(1)
where the forward transition map is defined as:
EX,Y (·) :=E H
(
EO,H(X⊗Y)⊗·
)
.(2)
This structure implements the causal sequence: at each stepm, the emission mapE O,H first
processes the observableY m with the current hidden state, followed by hidden state propagation
viaE H.
