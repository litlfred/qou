---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-008-2-quantum-mechanics-and-quantum-computation
section_title: "Quantum Mechanics and Quantum Computation"
section_number: 2
pages: 11-13
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
tation
We shall quickly indicate the basic principles of quantum mechanics.
The
quantum information context encapsulates a concise model of quantum theory:
The initial state of a quantum process is a vector |v⟩in a complex vector
space H. Measurement returns basis elements β of H with probability
|⟨β |v⟩|2/⟨v |v⟩
where ⟨v |w⟩= v†w with v† the conjugate transpose of v. A physical process oc-
curs in steps |v⟩−→U |v⟩= |Uv⟩where U is a unitary linear transformation.
Note that since ⟨Uv |Uw⟩= ⟨v |U†U|w⟩= ⟨v |w⟩= when U is unitary, it
follows that probability is preserved in the course of a quantum process.
One of the details for any speciﬁc quantum problem is the nature of the
unitary evolution. This is speciﬁed by knowing appropriate information about
the classical physics that supports the phenomena. This information is used
to choose an appropriate Hamiltonian through which the unitary operator is
constructed via a correspondence principle that replaces classical variables with
appropriate quantum operators. (In the path integral approach one needs a
Langrangian to construct the action on which the path integral is based.) One
needs to know certain aspects of classical physics to solve any speciﬁc quantum
problem.
A key concept in the quantum information viewpoint is the notion of the
superposition of states. If a quantum system has two distinct states |v⟩and
|w⟩, then it has inﬁnitely many states of the form a|v⟩+ b|w⟩where a and b
are complex numbers taken up to a common multiple. States are “really” in
the projective space associated with H. There is only one superposition of a
single state |v⟩with itself.
Dirac [21] introduced the “bra -(c)-ket” notation ⟨A |B⟩= A†B for the
inner product of complex vectors A, B ∈H. He also separated the parts of
the bracket into the bra < A | and the ket |B⟩. Thus
⟨A |B⟩= ⟨A | |B⟩
In this interpretation, the ket |B⟩is identiﬁed with the vector B ∈H, while the
bra < A | is regarded as the element dual to A in the dual space H∗. The dual
element to A corresponds to the conjugate transpose A† of the vector A, and
the inner product is expressed in conventional language by the matrix product
A†B (which is a scalar since B is a column vector). Having separated the bra
and the ket, Dirac can write the “ket-bra” |A⟩⟨B | = AB†. In conventional
notation, the ket-bra is a matrix, not a scalar, and we have the following
formula for the square of P = |A⟩⟨B | :
P 2 = |A⟩⟨B ||A⟩⟨B | = A(B†A)B† = (B†A)AB† = ⟨B |A⟩P.
The standard example is a ket-bra P = |A ⟩⟨A| where ⟨A |A⟩= 1 so that
P 2 = P. Then P is a projection matrix, projecting to the subspace of H that
is spanned by the vector |A⟩. In fact, for any vector |B⟩we have
P|B⟩= |A⟩⟨A | |B⟩= |A⟩⟨A |B⟩= ⟨A |B⟩|A⟩.
If {|C1⟩, |C2⟩, · · · |Cn⟩} is an orthonormal basis for H, and
Pi = |Ci ⟩⟨Ci|,
then for any vector |A⟩we have
|A⟩= ⟨C1 |A⟩|C1⟩+ · · · + ⟨Cn |A⟩|Cn⟩.
Hence
⟨B |A⟩= ⟨B |C1⟩⟨C1 |A⟩+ · · · + ⟨B |Cn⟩⟨Cn |A⟩
One wants the probability of starting in state |A⟩and ending in state |B⟩.
The probability for this event is equal to |⟨B |A⟩|2. This can be reﬁned if we
have more knowledge. If the intermediate states |Ci⟩are a complete set of
orthonormal alternatives then we can assume that ⟨Ci |Ci⟩= 1 for each i and
that Σi|Ci⟩⟨Ci| = 1. This identity now corresponds to the fact that 1 is the
sum of the probabilities of an arbitrary state being projected into one of these
intermediate states.
If there are intermediate states between the intermediate states this for-
mulation can be continued until one is summing over all possible paths from
A to B. This becomes the path integral expression for the amplitude ⟨B|A⟩.
