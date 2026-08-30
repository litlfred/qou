---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-011-42-computational-complexity-stabilizer-codes-and
section_title: "Computational Complexity, Stabilizer Codes, and NP-Hardness"
section_number: 4.2
pages: 32-37
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
One obvious source of computational hardness in the error correction procedure de-
scribed in the previous section is that in measuring the check operators and applying
corrections, we need to repeatedly use the encoding transformationUenc. If this unitary
is diﬃcult to implement as a quantum circuit, the error correction procedure will be
very time-consuming. In our discussion of the AMPS experiment below however, Uenc
will always be implementable with a small circuit. The rest of the correction procedure
seems straightforward, but there is one crucial point where after measuring the check
operators we need to pick a correction E†
α to apply. In general there are 2 2n possible
errors, out of which 2 n+k are consistent with any given result for the check operator
measurements. For a general channel it might be quite hard to decide which of these
2n+k corrections to apply. Since there are 2n−k possible results for measuring the check
operators, it is impractical to carry around a list of which correction to apply for each
syndrome. Without such a list however, it will generally take exponential time in n to
determine which check operator to apply since one will just have to go through the list
of 2n+k potential corrections and compute the probability for each that it is the correct
one to apply. In this section we sketch some known results about the hardness of this
step for a widely studied set of quantum error correcting codes, the stabilizer codes.
Stabilizer codes [57] are deﬁned by the property that the n−k check operators
in the computational basis are all just products of Pauli operators of the form (4.11).
Clearly both the Shor code and the trivial code are stabilizer codes. The reason for the
27Daniel Gottesman has suggested a simple “something else” to us, in the case where the matrix
Cαβ is diagonal. In that case the errors Eα inE send the code space to a set of mutually orthogonal
subspaces of the Hilbert space; this will typically be the case in the erasure channel if 2 l < n−k.
To do the correction we can just measure the projection operators onto each of these subspaces in
succession, stopping when the measurement returns one instead of zero. We can then just apply the
correction appropriate for that subspace. This procedure clearly takes an amount of time equal to the
number of possible errors, which in the erasure channel is 2 2l.
– 31 –
name is that the check operators generate a 2 n−k-element abelian subgroup S of the
full groupG of 22n products of Pauli operators, with the property that with respect to
the action ofG on the n-qubit Hilbert spaceS is the stabilizer subgroup of the k-qubit
code subspace. Thus rather than giving the codespace explicitly we can instead deﬁne
it by picking some Abelian subgroup of the Pauli group; in practice this is a much more
convenient way of deﬁning an error correcting code. Stabilizer codes are fairly easy to
encode: for any stabilizer code there is a relatively simple construction [57] of a circuit
of size O(n2) which implements Uenc exactly.
Stabilizer codes have the special property that we can expand the errors in Pauli
products of the form (4.11) in the computational basis instead of the logical basis
and still have each error commute or anticommute with each check operator. This
enables an elegant way of describing the relation of the errors to the results of the
check operator measurements. For each check operator we can deﬁne a 2 n component
row vector where the ﬁrst n components are its α’s from the parametrization (4.11)
and the last n are its β’s. We can then assemble these row vectors into an (n−k)× 2n
matrix H which is often called the parity check matrix. For each error we can make
a 2n-component column vector e whose ﬁrst n elements are the β’s for the error and
whose last n components are its α’s. Finally we can deﬁne the syndrome s of the error
as an n−k component column vector whose ith element is 0 if the error commutes
with the ith check operator and is 1 if it anticommutes. It is then not hard to check
thatHe =s, with the matrix multiplication done in the ﬁeld Z2. Thus the set of errors
e consistent with the syndrome s are just the solutions of this linear equation.
One simple channel in which one could study the hardness of stabilizer error correc-
tion is the erasure channel deﬁned in the previous subsection. In this case the possible
error vectors e are nonzero only for a known set of l out of the n qubits. We are then
free to remove the 2( n−l) columns from H which correspond to qubits which are
never erased, ﬁnding a new matrix H′ which is only (n−k)× 2l. When the inequality
2l <n−k is satisﬁed the matrix equation H′e′ =s is overdetermined and can always
be solved by Gaussian elimination in polynomial time unless no solution exists. Indeed
this inequality characterizes the channel capacity of the erasure channel, since it can be
shown that when it is violated it is impossible for the conditions (4.9) to be satisﬁed,
while when it is satisﬁed (4.9) will also be satisﬁed for a typical stabilizer code [42].
Thus stabilizer codes in the erasure channel can be corrected in polynomial time. We
emphasize however that this matrix structure is special to stabilizer codes, and that
for more general codes with polynomial size Uenc this procedure will not work. The
procedure described in the footnote at the end of the last section will work, but it
requires a time 2 2l which will be quite large when l is order n.
This result may not seem so promising from the point of view of the goal of this
– 32 –
article, but in fact there is a slightly more complicated channel in which it is possible
to show that stabilizer decoding is NP-complete [58, 59]. This is the gold standard
in evidence that a classical computation cannot be performed in polynomial time.
Good reviews of the basic properties of NP-completeness and its possible relevance for
physics are [23, 60]. Unfortunately the technical details of this argument restrict it
to showing NP-completeness only if k grows nontrivially with n, since the exponential
search which arises involves a search through 2 k things. This is an assumption we’d
like to drop in the context of Alice’s experiment, since we’d like her to be unable to
verify the entanglement even when k is order one, but the result is still indicative of
our main point since it shows quite convincingly how exponential time may be required
for error correction even when Unoise andUenc are both polynomial size. 28 The channel
studied by [59] is one in which X or Z errors can occur on any qubit with probability
p. The probability for a general error Eα is
Pr (Eα) =pwα(1−p)2n−wα, (4.14)
where wα is called the weight of the error and is deﬁned as as the number of αi’s and
βi’s in the parametrization (4.11) which are nonzero. 29 In order to correct this channel
one needs to ﬁnd the most likely set of errors, all ﬁxable by a single correction, which is
consistent with the syndromes. As explained in [59], the ability to answer this question
for general stabilizer codes in polynomial time in n would allow polynomial time in k
solution of the following question about matrices:
• Say we are given an integer w >0, an (n−k)×n matrixA, and a vector y with
n−k components, with the components of the latter two being elements of the
ﬁnite ﬁeld Z2. Is there a vector x with n components in Z2, of which at most w
are nonzero, with the property that Ax =y?
This problem is called the Coset Weights problem; it appears in classical coding theory
and was long ago shown to be NP-complete [58]. Since Coset Weights is NP-complete,
this then would allow polynomial time solution of any size k problem in the computa-
tional class NP. This is still not known to be impossible, but the very widely believed
28In more detail, the argument of [59] splits the error correction into two parts, one of which is
proven to be NP-complete for large k, and thus likely to require time exponential in k. The other part
appears to require exponential time in n, but they do not study its complexity in detail. We expect
stabilizer decoding in general to be hard even at ﬁxed k and large n.
29That Y is special is an undesirable asymmetry that is necessary for the proof of [59]. This seems
to be a technical problem, and we expect that correcting stabilizer codes is still NP-complete for the
“depolarizing channel”, where the probability for aY occuring is alsop. It seems unlikely that making
Y errors more likely would make the decoding easier but at the moment there is no proof.
– 33 –
conjecture P⁄= NP precludes it. For a discussion of the vast support for this conjecture,
see for example [61].
4.3 Alice’s Task as Error Correction
Having reviewed all this formalism we now see what it has to tell us about Alice’s
computing task. There is a straightforward way to recast what Alice is trying to do as
a quantum coding problem [3]. We can write the state (3.3) of the black hole as
|Ψ⟩ = 1√
|B|
∑
|b⟩B|¯b⟩, (4.15)
where
|¯b⟩≡ 1√
|H|
|h⟩HUR|bh0⟩R (4.16)
is a basis for a k dimensional subspace of HH⊗H R. We can obviously interpret this
subspace as a quantum code, with encoding transformation
Uenc≡URUmix,H. (4.17)
Here Umix,H is a simple entangling transformation analogous to Umix from equation
(3.25), but here entangling only the m qubits of H and the n + 1 ton +mth qubits of
R. For later convenience we will take Umix,H to act on each pair of qubits as
|b1b2⟩↦→ 1√
2
(
(−1)b1|b1b2⟩ +|b1 + 1,b 2 + 1⟩
)
, (4.18)
which is not quite the transformation given by the circuit in ﬁgure 3; to implement it
we need to act with an extra CNOT gate prior to the Hadamard transformation and
CNOT gates in ﬁgure 3. In this language, we can think of Alice not having access to
H as putting this code through an erasure channel that erases all qubits in H.
This simple recasting unfortunately does not allow us to learn anything about the
computational complexity of UR, since the state |Ψ⟩ has the special property that it
can be decoded just by acting with U†
R. The error correction is no harder than the
encoding, whose complexity we don’t know a priori. We can do better by recalling the
discussion of section 3.3, where we interpreted the state |Ψ⟩ as arising from the action
of a polynomial size circuit Udyn
Udyn|0⟩BHR = 1√
|B||H|
∑
bh
|b⟩B|h⟩HUR|bh0⟩R. (4.19)
We’d like to interpret Udyn as an encoding transformation and UR as a correction
operation, but this is not quite manifest here since Udyn always acts on the same state
– 34 –
so the code space appears one dimensional whereas we’d like it to be 2 k dimensional.
We can ﬁx this by introducing an additional systemB′, with the same number of qubits
as B, and then entangle it with B by acting with a transformation Umix,B′ which acts
as (4.18) on theith qubits ofB′ andB for alli∈ 1,...,k . We can then deﬁne ak-qubit
code subspace of this 2k +m +n qubit Hilbert space via the encoding transformation
Uenc≡Umix,B′Udyn such that
Uenc|b′⟩B′|0⟩BHR = 1√
|B||H|
∑
bh
Umix,B′|b′b⟩B′B|h⟩HUR|bh0⟩R. (4.20)
The errors introduced by the environment we again take to be erasures, now acting
on both B and H. With B and H erased, the only way to extract b′ and restore the
initial state is to unscramble the entanglement between B′ and R, which eﬀectively
requires being able to implement U†
R. More concretely, say that we have a polynomial
size circuit for UR. We may use it to act on the state (4.20) with U†
R. We may then act
with Umix,B′, now with the second element of each pair of qubits taken from the ﬁrst
k qubits of R instead of from B, which we no longer have access to. This produces a
state
|b′⟩ 1√
|B||H|
∑
bh
|b⟩B|h⟩H|bh0⟩R, (4.21)
so we have recovered the information b′. From here we can explicitly restore the initial
state in polynomial time by using ancilla to return BHR to the state|0⟩BHR and then
using Uenc to get back to the state (4.20) as desired. We may thus apply the lesson
of the previous section, which is that in general doing error correction for codes with
small encoding circuits requires exponential sized circuits. For stabilizer codes in the
erasure channel we saw that this was not true, but there is no reason to expect that the
encoding map (4.20) produces a stabilizer code. For more general Uenc the only known
correction procedure even in the erasure channel is the one described in the footnote at
the end of section 4.1, which takes a time 22l wherel is the number of erased qubits.3031
30By reshuﬄing factors between Uenc and Unoise we can turn erasures for a general code into a
more general channel for a stabilizer code, which for simplicity we can just take to be the trivial code.
The NP-completeness results of [59] strongly suggest that no general polynomial time error correction
algorithm exists for putting stabilizer codes through general channels, and essentially prove it when k
is large provided that P⁄= NP.
31It is interesting to note that since we here have l =k +m, the correction time 2 2(k+m) is actually
a bit faster than our estimate (3.22) which came from counting gates. This is because the correction
procedure from the footnote just mentioned involves doing quantum operations on B′, which is ﬁc-
titious and not available from the point of view of the original black hole problem. In other words,
any circuit for UR can be used to correct the channel just constructed but the converse is not true; a
generic correction procedure for this channel cannot be converted into a circuit for UR of comparable
complexity.
– 35 –
So far we have only discussed errors arising from Alice not having access to B and
H. There are of course other errors that can occur, having to do with the practical
diﬃculty of controlling the Hawking radiation. In particular an order one fraction of the
radiation will be gravitons, which are very hard to detect at all, never mind coherently
manipulate. It was shown long ago by Page [62] that the rate of Hawking radiation
into a ﬁeld of spin s decreases as s increases, so for Schwarzschild black holes in our
universe the fraction will be small. The question of how many bits can be lost without
losing the ability to error correct with high probability of success has been studied in
the literature, and as discussed in the previous subsection for the erasure channel the
number of bits which are lost must be less than n−k
2 . For a typical stabilizer code any
smaller number of erasures can be corrected with high probability of success [42]. This
will typically be true for more general codes like the one discussed here as well since
they should protect information at least as well as stabilizer codes. For the channel just
constructed, what was calledn in our general discussion of error correction is 2k+m+n
in terms of the parameters of our black hole model, so we can lose at most k+m+n
2 bits.
k +m have already been lost since Alice does not have access to B and H, so she can
lose n−k−m
2 more and still be able to error correct. Say that the fraction of the radiation
which is gravitons isα. Since α< 1
2, this means that if Alice waits long enough she can
lose all of the gravitons and still be able extract the entanglement accurately with room
to spare for correcting additional errors. Of course doing this error correction can be
an additional source of computational hardness, which will only make it even harder to
complete the decoding before the black hole evaporates. This discussion shows however
that without taking into account computational complexity, the diﬃculty of measuring
gravitons does not prevent the AMPS experiment from being done.
