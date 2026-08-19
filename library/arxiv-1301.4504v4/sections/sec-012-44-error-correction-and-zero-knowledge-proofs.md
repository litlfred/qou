---
doc_id: arxiv-1301.4504v4
doc_title: "Prepared for submission to JHEP DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center "
section_id: sec-012-44-error-correction-and-zero-knowledge-proofs
section_title: "Error Correction and Zero-Knowledge Proofs"
section_number: 4.4
pages: 37-41
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "DEDICATED TO JOHN PRESKILL ON THE OCCASION OF HIS 60 TH BIRTHDAY Quantum Computation vs. Firewalls Daniel Harlowa Patrick Haydenb aPrinceton Center for Theoretical Science, Princeton University, Princ"
---
We’ve seen that the known NP-hardness results about decoding quantum error correct-
ing codes, although suggestive, break down for technical reasons when k is order one
and thus unfortunately can’t be invoked directly to draw any ﬁrm conclusions about
UR in that case. Moreover one might worry that the appearance of the NP-complete
problem Coset Weights in the argument of [59] was a consequence of their particular
decoding strategy; perhaps some more exotic correction procedure could somehow do
the error correction without having an intermediate step that allowed solution of Coset
Weights. We ﬁnd this unlikely, but both of these concerns can be addressed somewhat
by observing that the diﬃculty of implementing UR is actually closely related to an-
other complexity class known as Quantum Statistical Zero-Knowledge ( QSZK). The
idea of a zero-knowledge proof is best explained by example.
– 36 –
Consider the problem of determining whether two graphs G1 = (V1,E 1) and G2 =
(V2,E 2) are isomorphic, that is, whether there exists a permutation π of the vertices
of G2 turning G2 intoG1. There is currently no polynomial time classical or quantum
algorithm known for the graph isomorphism problem. Suppose, however, that some
inventive computer scientist claimed to be able to solve the graph isomorphism but
jealously guarded his secret abilities. Would he be able to convince you that two G1
andG2 are isomorphic without revealing any information about the isomorphism? Yes!
The computer scientist begins by randomly permuting the vertices of G1, sending you
the resulting graph G3. At that point, you ﬂip a coin and, depending on the outcome,
challenge him to exhibit an isomorphism to either G1 orG2. He will be able to succeed
if the graphs really were isomorphic but will necessarily fail half the time otherwise.
After a few repetitions of the process, you will become convinced of the existence of the
isomorphism between G1 and G2 without learning anything at all about its structure.
There are diﬀerent ways to formalize the idea of a zero-knowledge proof, leading to
potentially diﬀerent complexity classes. The version relevant here is known as the class
Statistical Zero-Knowledge ( SZK) [63]. In the quantum mechanical analogue, the two
participants, usually known as the prover and the veriﬁer, would exchange qubits rather
than bits, with the resulting class called QSZK [64]. There is absolutely no constraint
on the computational power of the prover, but the veriﬁer can only perform polynomial
time quantum computations. Moreover, only a statistically negligible amount of infor-
mation should leak from the prover to the veriﬁer. QSZK is the set of computational
problems with yes/no answers for which such a prover can always convince the veriﬁer
of yes instances but will fail with high probability for no instances. It is known that the
quantum model is at least as powerful as the classical one: SZK⊆ QSZK [65]. QSZK
also trivially contains BQP, the class of problems that can be solved on a quantum
computer: for such problems, the veriﬁcation can be done directly using the computer
itself without any need for a clever discussions with a prover. QSZK should therefore
be understood as the set of problems whose yes instances can be reliably identiﬁed
using a quantum computer with the help of an all-powerful prover, albeit one who is
both secretive and dishonest. To assert that all the problems in QSZK can be solved in
quantum polynomial time, that QSZK = BQP, is to assert that the prover is ultimately
no help at all.
Given some arbitrary polynomial-sized quantum circuit Udyn acting on three sys-
temsB,H andR such that|ψ⟩BHR =Udyn|000⟩BHR with|ψ⟩BHR maximally entangled
between B and HR, determining whether maximal entanglement with B can be de-
coded from R is a well-deﬁned computational problem. Call it the Error Correctability
– 37 –
problem.32 Note that Error Correctability has a quantum statistical zero-knowledge
proof, which simply consists of having the prover implement the quantum error cor-
rection operation on R (not caring that it might take exponential time) and having
the veriﬁer check the result. In fact, the problem of determining whether noise is cor-
rectable in this sense is complete for QSZK, meaning that any other problem in QSZK
can be eﬃciently mapped onto a version of the error correction problem [66] (see also
section 7 of [67]).
Suppose now that, given a circuit for an arbitrary correctableUdyn, it were possible
to eﬃciently ﬁnd and implement the error correction procedure. In that case, the entire
zero-knowledge proof for Error Correctability described above could be implemented
eﬃciently on a quantum computer. In the case of yes instances, the procedure would
produce veriﬁable maximal entanglement with B. In the case of no instances, no
such entanglement could be produced regardless of the decoding procedure attempted.
Moreover, since Error Correctability is QSZK-complete, that means that every problem
in QSZK could be solved on a quantum computer: being able to eﬃciently decode noise
whenever it is correctable would imply thatQSZK = BQP. (It is important to remember,
however, that simply determining whether some errors are correctable could be much
easier than actually correcting them.)
Crucially, Error Correctability remains QSZK-complete even if B consists of only
a single qubit, unlike the NP-hardness result for stabilizer decoding discussed earlier.
The question at the core of this article is whether the decoding can be performed in
time polynomial in the size of the circuit for Udyn. We have seen that being able to do
so would imply that QSZK = BQP if Udyn represented arbitrary correctable noise.
Since the real Udyn describing black hole evaporation is very special, we could ask
whether its known properties are so unusual as to undermine the argument. Speciﬁcally,
for suﬃciently late times, we expect maximal entanglement between BH and R. It
is possible to a certain extent to achieve the same thing using arbitrary |ψ⟩BHR =
Unoise|000⟩BHR by simply working withk copies of|ψ⟩. The resulting state|ψ⟩⊗k rapidly
converges to one with near-maximal entropy concentrated in the “typical subspace” of
B⊗kH⊗k [68]. This property is similar to true maximal entanglement generated by
Udyn, albeit slightly weaker.
The conviction that P⁄= NP has developed over several decades of research in
algorithm design and complexity theory. The belief that QSZK-complete problems
cannot be solved eﬃciently on a quantum computer is admittedly less well-founded but
does have some algorithmic and complexity theoretic support.
32The channel constructed in the previous subsection shows how to relate this deﬁnition to more
conventional error correction.
– 38 –
Researchers have been working for twenty years on the design of eﬃcient quantum
algorithms and some problems have stubbornly resisted attack. In particular, Shor’s
factoring algorithm naturally extends to an eﬃcient quantum algorithm for the more
general Abelian Hidden Subgroup problem [69]. Researchers have been trying consis-
tently since then to attack the non-Abelian version of the problem but with only very
limited success [70–72]. (Note that the non-Abelian version includes the graph isomor-
phism problem discussed above as a special case [73].) Large classes of strategies based
on Shor’s Fourier-sampling approach are known to fail [74, 75].
Given all the fruitless eﬀort that has gone into trying to ﬁnd an eﬃcient quantum
algorithm for solving the non-Abelian Hidden Subgroup problem, researchers have begun
to suspect that no such algorithm exists. Moore, Russell and Vazirani (MRV) took
one step further and deﬁned a classical invertible function that is eﬃcient to evaluate
but hard to invert on a quantum computer under the assumption that there is no
eﬃcient quantum algorithm for non-Abelian Hidden Subgroup [76]. Their construction is
easily adapted to rule out eﬃcient quantum algorithms for decoding eﬃciently encoded
quantum error correcting codes under the same assumption. Structurally, the function
is parametrized by a list of m vectorsV over Fn
q . The MRV function fV takes a matrix
M∈ GLn(Fq) to MV , with the output returned as an unordered list. ( m is selected to
be only slightly larger than n, which is suﬃcient to ensure that the function is injective
with high probability.)
Instead of returning an unordered list, however, the output vectors could equiva-
lently be ordered but permuted by an unknown permutation π, which can be used to
deﬁne the following isometry:
U :|M⟩A↦→ 1√
m!
∑
π∈Sm
|π⟩H|π(MV )⟩R. (4.22)
Then (IB⊗U) acting on a state maximally entangled between A and B eﬃciently
generates a state maximally mixed on BH with the property that the puriﬁcation of B
can be recovered by a unitary acting onR alone, precisely mimicking the key properties
of ∑
b,h|b⟩B|h⟩HUR|bh0⟩R. If fV is hard to invert on a quantum computer, however,
the decoding unitary can’t be implemented in polynomial time. Under the assumption
that there is no eﬃcient algorithm for non-Abelian hidden subgroup , however,fV is hard
to invert, even for V chosen uniformly at random.
At the level of complexity theory, there is some evidence thatQSZK-complete prob-
lems cannot be solved using small quantum circuits. (An eﬃcient quantum algorithm
corresponds to a small circuit that can itself be laid out eﬃciently, a further requirement
that should arguably be relaxed in discussions of the AMPS paradox.) It is known that
determining whether a function is 1-to-1 or 2-to-1 requires exponentially many calls to
– 39 –
the function, even for a quantum computer [77]. It is easy to construct a statistical
zero-knowledge protocol for the problem, however, in the setting in which the prover
knows the function and the veriﬁer is making queries to try and distinguish the 1-to-1
and 2-to-1 cases. Since SZK⊆ QSZK, the protocol lifts to a quantum statistical zero-
knowledge proof as well. In this model, therefore, an exponentially large number of
queries is required to solve the problem using a quantum computer even though it has
a zero-knowledge protocol. Any demonstration that QSZK has small circuits would
somehow have to be reconciled with that fact, which essentially rules out any strategy
which just directly transforms a zero-knowledge protocol directly into a small circuit.
Instead, the demonstration would need to make essential use of some subtle internal
structure of the problems contained in QSZK.33
The conclusion of this section is that by recasting Alice’s problem as quantum error
correction, we have set it into a framework where there are general arguments that such
problems likely take exponential time to solve. Moreover the practical diﬃculties of
doing the experiment, in particular the problems associated with measuring gravitons,
further increase the diﬃculty of this computational task. We did not quite manage to
prove that her task is NP-hard at ﬁxed k, but it is almost certainly at least QSZK-hard
and there are strong reasons to believe that such problems can’t be solved in polynomial
time on a quantum computer. From the computer science point of view, it would be
extremely surprising if implementing U†
R did not require exponential time.
