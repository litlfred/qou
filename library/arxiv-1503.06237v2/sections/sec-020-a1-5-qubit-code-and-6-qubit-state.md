---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-020-a1-5-qubit-code-and-6-qubit-state
section_title: "A.1 5-qubit code and 6-qubit state"
section_number: null
pages: 43-45
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
The ﬁve-qubit code is a [[5 , 1, 3]]2 perfect code with distance 3 encoding one logical
qubit in ﬁve physical qubits. It is a stabilizer code with a stabilizer subgroup given by
S =⟨S1,S 2,S 3,S 4⟩, where
S1 =X⊗Z⊗Z⊗X⊗I
S2 =I⊗X⊗Z⊗Z⊗X
S3 =X⊗I⊗X⊗Z⊗Z
S4 =Z⊗X⊗I⊗X⊗Z.
(A.1)
Note that S1S2S3S4 =Z⊗Z⊗X⊗I⊗X and hence the group is manifestly invariant
under cyclic permutations. As is the case in the stabilizer formalism, codes are char-
acterized by an abelian stabilizer subgroup ([Si,Sj] = 0) and codespace is the joint +1
eigenspace for this group, code states satisfy
Sj|ψ⟩ =|ψ⟩ j = 1,... 4. (A.2)
– 41 –
In this case, there are two orthogonal codeword states.
Logical operators are unitary operators which preserve the codeword space, but
may act non-trivially on it. They are given by
X =X⊗X⊗X⊗X⊗X Z =Z⊗Z⊗Z⊗Z⊗Z. (A.3)
One may see that both X and Z commute with all the stabilizer generators, so they
indeed preserves the codeword space. Yet, they anti-commute with each other, so they
characterize one logical qubit, andX andZ behave as logical Pauli-X and -Z operators
for a logical qubit. Namely, one can denote two codeword states by|˜0⟩ and|˜1⟩ such that
Z|˜0⟩ =|˜0⟩, Z|˜1⟩ =−|˜1⟩, X|˜0⟩ =|˜1⟩, X|˜1⟩ =|˜0⟩. Applications of stabilizer generators
to logical operators do not change the action on the codeword space, so representations
of logical operators are not unique. Then one can introduce the following equivalence
relations among logical operators
Z∼ZU X∼XU where U∈S (A.4)
as equivalent logical operators act in the same way on the codeword space. In particular,
one can conclude that on the codespace, ¯X ∼ −Z⊗X⊗Z⊗I⊗I or any cyclic
permutation thereof by multiplying eq. A.3 by stabilizer generators in eq. A.1. In the
ﬁve-qubit code, one can show that logical operators must act non-trivially on at least
three physical qubits (weight 3) and the reduced density matrices on any two physical
qubits is always maximally mixed.
One can convert the ﬁve-qubit code into a six-qubit perfect state. Imagine that we
add one extra qubit to the ﬁve-qubit code such that the new qubit is entangled with a
logical state of the ﬁve-qubit code. To be speciﬁc, we consider a six-qubit state whose
stabilized byS′ =⟨S′
1,S′
2,S′
3,S′
4,S′
5,S′
6⟩, with generators are given by
S′
1 =X⊗Z⊗Z⊗X⊗I⊗I
S′
2 =I⊗X⊗Z⊗Z⊗X⊗I
S′
3 =X⊗I⊗X⊗Z⊗Z⊗I
S′
4 =Z⊗X⊗I⊗X⊗Z⊗I
S′
5 =X⊗X⊗X⊗X⊗X⊗X =X⊗X
S′
6 =Z⊗Z⊗Z⊗Z⊗Z⊗Z =Z⊗Z.
(A.5)
Here we have “recycled” stabilizer generators S1,...,S 4 from the ﬁve-qubit code:
S′
j =Sj⊗I for j = 1,..., 4. (A.6)
– 42 –
We then constructed new stabilizer generators S′
5 and S′
6 from logical operators of the
ﬁve-qubit code as follows:
S′
5 =X⊗X S ′
6 =Z⊗Z (A.7)
where X and Z act on ﬁve qubits. One may easily check that stabilizer generators
commute with each other. The wavefunction is speciﬁed by
S′
j|ψ⟩ =|ψ⟩ j = 1,..., 6, (A.8)
and the six-qubit state is given by |ψ⟩ =|˜0⟩⊗| 0⟩ +|˜1⟩⊗| 1⟩. From the construction,
one can see that ρA∝IA if|A|≤ 3. It turns out that this conversion is generic. That
is, one can always convert a perfect code with 2n− 1 spins into a perfect state with 2n
spins.
