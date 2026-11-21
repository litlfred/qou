---
doc_id: arxiv-quant-ph-0606114v3
doc_title: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation"
section_id: sec-009-21-what-is-a-quantum-computer
section_title: "What is a Quantum Computer?"
section_number: 2.1
pages: 13-14
source_pdf: 0606114v3.pdf
source_sha256: a8e08c457b65c728
toc_source: inferred
doc_brief: "q - Deformed Spin Networks, Knot Polynomials and Anyonic Topological Quantum Computation — We review the q-deformed spin network approach to Topological Quantum Field Theory and apply these methods"
---
What is a Quantum Computer?
A quantum computer is, abstractly, a composition U of unitary transforma-
tions, together with an initial state and a choice of measurement basis. One
runs the computer by repeatedly initializing it, and then measuring the result
of applying the unitary transformation U to the initial state. The results of
these measurements are then analyzed for the desired information that the
computer was set to determine. The key to using the computer is the design
of the initial state and the design of the composition of unitary transforma-
tions. The reader should consult [65] for more speciﬁc examples of quantum
algorithms.
Let H be a given ﬁnite dimensional vector space over the complex numbers
C. Let {W0, W1, ..., Wn} be an orthonormal basis for H so that with |i⟩:= |Wi⟩
denoting Wi and ⟨i| denoting the conjugate transpose of |i⟩, we have
⟨i|j⟩= δij
where δij denotes the Kronecker delta (equal to one when its indices are equal
to one another, and equal to zero otherwise).
Given a vector v in H let
|v|2 := ⟨v|v⟩. Note that ⟨i|v is the i-th coordinate of v.
An measurement of v returns one of the coordinates |i⟩of v with probability
|⟨i|v|2. This model of measurement is a simple instance of the situation with a
quantum mechanical system that is in a mixed state until it is measured. The
result of measurement is to put the system into one of the basis states.
When the dimension of the space H is two (n = 1), a vector in the space
is called a qubit. A qubit represents one quantum of binary information. On
meausurement, one obtains either the ket |0⟩or the ket |1⟩. This constitutes
the binary distinction that is inherent in a qubit.
Note however that the
information obtained is probabilistic. If the qubit is
|ψ⟩= α|0⟩+ β |1⟩,
then the ket |0⟩is observed with probability |α|2, and the ket |1⟩is observed
with probability |β|2. In speaking of an idealized quantum computer, we do not
specify the nature of measurement process beyond these probability postulates.
In the case of general dimension n of the space H, we will call the vectors
in H qudits. It is quite common to use spaces H that are tensor products
of two-dimensional spaces (so that all computations are expressed in terms of
qubits) but this is not necessary in principle. One can start with a given space,
and later work out factorizations into qubit transformations.
A quantum computation consists in the application of a unitary transfor-
mation U to an initial qunit ψ = a0|0⟩+ ... + an|n⟩with |ψ|2 = 1, plus a
measurement of Uψ. A measurement of Uψ returns the ket |i⟩with probabil-
ity |⟨i|Uψ|2. In particular, if we start the computer in the state |i⟩, then the
probability that it will return the state |j⟩is |⟨j|U|i⟩|2.
It is the necessity for writing a given computation in terms of unitary
transformations, and the probabilistic nature of the result that characterizes
quantum computation. Such computation could be carried out by an idealized
quantum mechanical system. It is hoped that such systems can be physically
realized.
