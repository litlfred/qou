---
doc_id: arxiv-2605.09605v2
doc_title: "Cocycle Actions on Hidden Quantum Markov Models:"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 2605.09605v2.pdf
source_sha256: 24496fb444a2b558
doc_brief: "Cocycle Actions on Hidden Quantum Markov Models: — We develop a symmetry action framework for hidden quantum Markov models (HQMMs) tailored to one-dimensional quantum spin systems and"
---
Symmetry-protected topological (SPT) phases provide a unifying framework for a broad class of
quantum spin systems in which global symmetries protect robust edge modes, quantized topolog-
ical invariants, and nontrivial entanglement structures, even in one-dimensional settings [1, 2, 3].
Within this picture, the Haldane phase of spin-1 chains and its paradigmatic representative, the
AKLT model, furnish canonical examples of bosonic SPT phases protected by spin-rotation and
related symmetries [1, 4, 5]. Building on the index-theoretic and group-cohomological classification
of 1D SPT phases, these systems are now understood in terms of projective edge representations
and cohomology classes such as [ω]∈H 2(G,U(1)), and they are increasingly viewed as resources
1
arXiv:2605.09605v2  [math-ph]  26 May 2026
for quantum information processing and computational power [6, 7, 8, 9, 10, 11]. Recent devel-
opments have extended this perspective to open and driven quantum systems, where SPT order
persists under symmetry-preserving noisy dynamics and gives rise to refined notions of order and
protected structure in non-equilibrium settings [12, 13, 14].
In parallel, hidden quantum Markov models (HQMMs) have emerged as a rigorous operator-algebraic
framework for modeling structured quantum dynamics with latent degrees of freedom, extend-
ing classical hidden Markov models to the noncommutative setting [15, 16]. In this formalism,
completely positive maps and quantum channels govern the virtual evolution, while projective or
generalized measurements define the observed output processes [18, 19, 17]. This point of view has
recently been revitalized by applications to quantum information and quantum machine learning,
where HQMMs support new paradigms for modeling and learning temporal quantum data, in-
cluding split HQMM architectures and the operational analysis of quantum memory [20, 21, 22].
Strikingly, it has been shown that paradigmatic many-body states such as finitely correlated states
and matrix product states can be realized as observation processes of HQMMs, thereby providing
a stochastic and channel-based perspective on tensor-network ground states [23, 24, 25]. In par-
ticular, the AKLT state—realizing the Haldane phase as an SO(3)-protected SPT phase—admits
such an HQMM representation, and more generally fits into a cohomological framework where
symmetry actions on the hidden layer encode the underlying topological order [4, 5, 25, 26].
The present work is motivated by this convergence between SPT order and HQMMs. On
the one hand, the modern classification of 1D SPT phases via indices, projective representa-
tions, and cohomology provides a robust conceptual and technical toolkit for understanding
phases such as the Haldane phase and its generalizations [6, 7, 8, 27]. On the other hand, the
operator-algebraic theory of quantum Markov processes and their cocycles suggests that HQMMs
naturally carry symmetry actions and cohomological data at the level of their hidden (virtual)
dynamics [15, 16, 28, 22]. Our aim is to systematically develop a symmetry-action framework
for HQMMs that (i) recovers known SPT features of the AKLT and related Haldane-type chains
and (ii) recasts SPT phases as equivalence classes of cocycle actions on quantum Markov models,
thereby establishing a new step towards a rigorous bridge between quantum stochastic processes,
tensor-network descriptions, and the topological order of quantum phases [9, 10, 11, 29, 25].
In the present paper, we develop a comprehensive algebraic framework of symmetry actions
on HQMMs, focusing on the interplay between projective representations of a symmetry group
and the causal structure of the underlying quantum Markov chain. LetGbe a locally compact
group. The hidden sector is described by a separable Hilbert spaceHcarrying a projective unitary
representationπ:G→U(H) with associated 2-cocycleω∈H 2(G,U(1)), while the observable
sector is described by a Hilbert spaceKcarrying a linear unitary representationρ:G→U(K)
corresponding to the trivial cocycle. The algebraic actions are implemented via adjoint actions
α(H)
g = Ad(π(g)) onA H =B(H) andβ g = Ad(ρ(g)) onA O =B(K), extended to the quasi-local
algebrasA H,N0 andA O,N0 by tensor product structure [19, 17].
The HQMM is defined by a generative triple (ϕ0,EH,EH,O), whereϕ 0 is an initial state onA H,
EH :A H⊗A H→A H is a completely positive unital map [18] governing the hidden transition,
andE H,O :A H⊗A O → AH is a completely positive unital map governing the emission of
observables. The symmetry action is encoded in three fundamental conditions: invariance of the
initial state, equivariance of the hidden transition map, and covariance of the emission map. The
latter constitutes the central structural relation, asserting thatE H,O intertwines the projective
G-action onA H with the linearG-action onA O, thereby absorbing the projective anomaly at the
interface between hidden and observable sectors.
We analyze two distinct causal structures arising from different orderings of the hidden tran-
sition and emission maps: the conventional structureT (conv) corresponding to a measurement-
then-evolution paradigm, and the causal structureT (caus) corresponding to an evolution-then-
measurement paradigm. For each structure, we introduce sliced mapsT (conv)
X,Y ,T (caus)
X,Y :A H→A H
that propagate the hidden state forward, and establish their covariance properties under the
symmetry action.
2
The main result, Theorem 2.3, demonstrates that under the symmetry conditions (6), (7),
and (8), the global HQMM statesφ (conv) andφ (caus) on the quasi-local algebraA N0—constructed
as projective limits of finite-volume states—are invariant under the combined projective-linear
action ofG. Consequently, the hidden marginals are invariant under the projective actionα (H),
and the observable marginals are invariant under the linear actionβ.
This result is particularly significant for the study of symmetry-protected topological order.
The AKLT state [4, 5]—a prototypical SPT phase protected by SO(3) symmetry [1, 13]—is
realized as the observation process of a causal HQMM [29], where the hidden spaceH 1/2 carries
the irreducible projective spin-1/2 representationπwith cocycle [ω]∈H 2(SO(3),U(1)) ∼= Z2,
and the observable spaceH 1 carries the linear spin-1 representationρ. The emission map is
based on the AKLT tensors, while the hidden transition is only required to be equivariant with
respect the representationπin particular it can be taken a partial trace. In this case however the
underlying entanglement structure is trivial, the process allows to reproduce the AKLT finitely
correlated state as observation state as shown in our previous work [29]. The initial state is
uniquely determined by symmetry as the normalized trace via Schur’s lemma [19]. Theorem
2.3 therefore implies global SO(3)-invariance of the associated HQMM state, with the nontrivial
cocycle [ω] serving as a topological invariant characterizing the SPT phase [2, 3, 8].
Beyond the AKLT example, our approach establishes a rigorous operator-algebraic foundation
for the classification of SPT phases within the HQMM framework [28, 22]. The two causal
structures analyzed are natural candidates for modeling distinct physical scenarios, and their
symmetry properties can be extended to more complex systems [19]. Moreover, the algebraic
framework extends naturally to higher dimensions through a convenient framework of hidden
quantum Markov fields, opening avenues for studying SPT order in general matrix product states
framework [13]. Further works will pursue a systematic hidden-memory approach to SPT order,
exploring their classification and applications to quantum memory and learning algorithms.
The remainder of this paper is organized as follows. Section 2 introduces projective symme-
try actions on HQMMs via a 2-cocycle, formulates the invariance, equivariance, and covariance
conditions, and proves that these imply global invariance of the HQMM state for both causal
structures (Theorem 2.3). Section 3 applies this framework to the AKLT state. Section 4 con-
cludes with perspectives on classification, higher dimensions, and applications. Appedix A recalls
the operator-algebraic construction of HQMMs and defines the two causal structures.
