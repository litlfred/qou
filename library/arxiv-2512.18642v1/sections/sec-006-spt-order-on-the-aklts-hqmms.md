---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for"
section_id: sec-006-spt-order-on-the-aklts-hqmms
section_title: "SPT order on the AKLT,s HQMMs"
section_number: null
pages: 15-16
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
doc_brief: "A Hidden Quantum Markov model framework for — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af- fleck–Kennedy–Lieb–Tasaki (AKLT) state—a cornerstone example of a"
---
The AKLT state’s remarkable robustness stems from its symmetry-protected topological (SPT)
order, which manifests elegantly within its Hidden Quantum Markov Model (HQMM) descrip-
tion. To understand this protection mechanism, clarify how symmetries operate in the HQMM
framework.
LetGbe a symmetry group with unitary representationsπ:G→U(H 1/2) on the virtual
space andρ:G→U(H 1) on the physical space.
The heart of the matter lies in theemission transition expectationE O,H, which implements
the quantum-classical interface between hidden and observable sectors. This channel is built from
the AKLT tensorsA k through:
EO,H(Z⊗Y) =
∑
k,k′
⟨k′|Y|k⟩A kZA†
k′ (20)
The fundamental covariance condition [26, 29]:
∑
k′
ρ(g)kk′Ak′ =π(g)A kπ(g)†
ensures thatE O,H transforms covariantly, meaning that symmetry transformations commute with
the emission process. This covariance propagates to the composite transition mapE X,Y that
drives the HQMM dynamics:
EX,Y (Z) =E H(EO,H(X⊗Y)⊗Z)
The mapE X,Y inherits the symmetry property:
Eρ(g)Xρ(g) †,ρ(g)Yρ(g) †(π(g)Zπ(g)†) =π(g)E X,Y (Z)π(g)†
This hierarchical symmetry preservation—from individual channels to composite dynamics—
ensures that the AKLT state’s topological character remains protected throughout the quantum
Markov process. The HQMM framework thus reveals how SPT order emerges from the consistent
interplay between hidden dynamics and symmetry constraints across all scales of the system.
Theorem 5.1.LetGbe a symmetry group with unitary representationsρ:G→U(H 1)on the
physical space andπ:G→U(H 1
2
)on the virtual space. The emission transition expectation
EO,H :B(H 1
2
)⊗B(H 1)→B(H 1
2
)defined in(20)isG-equivariant. That is, for allg∈G,
EO,H
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g) †
)
=π(g)E O,H(X⊗Y)π(g) †,(21)
for allX∈B(H 1
2
)andY∈B(H 1).
Proof.Letg∈G,X∈B(H 1
2
), andY∈B(H 1) be arbitrary. We compute the left-hand side of
(21):
LHS =E O,H
(
π(g)Xπ(g)†⊗ρ(g)Yρ(g) †
)
=
∑
m,m′
⟨m|ρ(g)Yρ(g)†|m′⟩Am
(
π(g)Xπ(g)†
)
A†
m′.
Expanding the matrix element in the physical basis{|m⟩}yields:
⟨m|ρ(g)Yρ(g)†|m′⟩=
∑
k,k′
ρ(g)mk⟨k|Y|k′⟩(ρ(g)†)k′m′.
Substituting this back into the expression for LHS and reordering the finite sums gives:
LHS =
∑
k,k′
⟨k|Y|k′⟩

∑
m,m′
ρ(g)mk(ρ(g)†)k′m′Am
(
π(g)Xπ(g)†
)
A†
m′

.
15
LetS k,k′ denote the inner sum. We can factor it as follows:
Sk,k′ =
(∑
m
ρ(g)mkAm
)(
π(g)Xπ(g)†
)(∑
m′
(ρ(g)†)k′m′A†
m′
)
.
We now apply the covariance condition. The first factor is given directly by (5):
∑
m
ρ(g)mkAm =π(g)A kπ(g)†.
The third factor is the adjoint of the covariance condition for indexk ′:
∑
m′
(ρ(g)†)k′m′A†
m′ =
(∑
m′
ρ(g)m′k′Am′
)†
=
(
π(g)Ak′π(g)†
)†
=π(g)A†
k′π(g)†.
Substituting these expressions intoS k,k′ and using the unitarity ofπ(g) (π(g) †π(g) =I) gives:
Sk,k′ =
(
π(g)Akπ(g)†
)(
π(g)Xπ(g)†
)(
π(g)A†
k′π(g)†
)
=π(g)A kXA†
k′π(g)†.
SubstitutingS k,k′ back into the expression for LHS yields the final result:
LHS =
∑
k,k′
⟨k|Y|k′⟩π(g)A kXA†
k′π(g)†
=π(g)

∑
k,k′
⟨k|Y|k′⟩AkXA†
k′

π(g)†
=π(g)E O,H(X⊗Y)π(g) †.
This completes the proof of (21).
Theorem 5.1 provides a key understanding about the unique properties of AKLT state. It
shows that the emission map is a perfect symmetry bridge. The equation (21) guarantees that
the symmetry of the hidden spin-½particles is perfectly converted into the standard symmetry
of the physical spin-1 particles we observe.
The dual of this map, which governs how information flows back to the hidden level, must
also respect this symmetry. The covariance implies that for a virtual density matrixσ, the dual
action satisfies:
E∗
O,H
(
π(g)σπ(g)†
)
= (π(g)⊗ρ(g))E ∗
O,H(σ)
(
π(g)†⊗ρ(g)†
)
.
This means that any physical process acting on the spin-1 chain—like time evolution under a
symmetric Hamiltonian—will automatically induce a corresponding action on the hidden spin-½
that faithfully preserves their projective character.
