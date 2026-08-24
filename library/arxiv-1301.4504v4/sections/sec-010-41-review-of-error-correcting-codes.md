---
doc_id: arxiv-1301.4504v4
doc_title: "Quantum Computation vs. Firewalls"
section_id: sec-010-41-review-of-error-correcting-codes
section_title: "Review of Error Correcting Codes"
section_number: 4.1
pages: 27-32
source_pdf: 1301.4504v4.pdf
source_sha256: 201acc5bb1d4b6a0
doc_brief: "Quantum Computation vs. Firewalls — In this paper we discuss quantum computational restrictions on the types of thought experiments recently used by Almheiri, Marolf, Polchinski, and Sully to argue"
---
Typically quantum systems cannot be isolated from their environment. It is interesting
to understand to what extent a system which began in an unknown state can be restored
to that state after it has interacted nontrivially with its environment. Usually this is
done by introducing another ancillary system and transferring the entanglement with
24This possibility was suggested to us by Raphael Bousso.
25A recent paper [52] also discussed the AMPS argument in the language of error correction; their
use of error correction was quite diﬀerent from that we discuss here.
– 26 –
U
E S A
U
noise
correct
Figure 5. Quantum error correction. Here S is the system whose state we want to restore,E
is the environment it becomes entangled with via the interaction Unoise, and A is the ancilla
it interacts with via Ucorrect. At the end the environment is entangled with the ancilla and
the system S is in the same quantum state it started in.
the environment from the system whose state we want to restore to the ancillary system.
We show this pictorially in ﬁgure 5.
Error correction is not always possible. For example, say that the transformation
Unoise from ﬁgure 5 is such that it results in the system S being maximally entangled
with the environment E. There is no information about its initial state remaining in
S, and no choice of Ucorrect will allow recovery. What is perhaps surprising is that
it is ever possible to restore the initial state after a nontrivial Unoise has acted. To
see that this can be done, following Shor [53] we consider an arbitrary superposition
|Ψ⟩ =a+|+⟩ +a−|−⟩ of the following two nine-qubit states:
|±⟩≡ 1
23/2 (|000⟩±| 111⟩) (|000⟩±| 111⟩) (|000⟩±| 111⟩). (4.1)
As a crude model of interaction with the environment, we can imagine that the state
|Ψ⟩ will be acted on randomly by a single Pauli operator X, Y , or Z on one of its
nine qubits. After this can we restore the state |Ψ⟩ without destroying it? As Shor
explained in [53], we can. The idea is to measure the following set of eight “check”
operators:
Z1Z2, Z 2Z3, Z 4Z5, Z 5Z6, Z 7Z8, Z 8Z9,
X1X2X3X4X5X6, and X4X5X6X7X8X9. (4.2)
Since the states|±⟩ are both eigenstates of eigenvalue one for all eight of these operators,
this measurement will do nothing to the state Ψ. Let’s say however that interaction
– 27 –
with the environment has caused the state to be acted on by X1. This commutes with
the last seven check operators, so their eigenvalues are unaﬀected, but it will change
the result of measuring Z1Z2 to from 1 to −1 for both states |±⟩. It is easy to see
that none of the other possible single-Pauli errors will give this signature as a result
of measuring the check operators. We can then “repair” the error up to an overall
irrelevant phase by acting withX1. Similarly say that the error acts with Z1. This will
now ﬂip the eigenvalue of X1X2X3X4X5X6 without aﬀecting any of the other check
operators. There are now two other single-Pauli errors with the same signature, Z2 and
Z3, but we can correct any of the three up to an overall phase by acting with Z1 on the
state. In this manner it is easy to see that any single-Pauli error can be corrected. 26
This protocol is called the Shor code, and it was the ﬁrst quantum error correcting
code to be discovered.
The Shor code works for two reasons. One is that it is redundant, meaning that
the number of bits of information it protects is signiﬁcantly fewer than the number
of physical bits present. This allows “room” for noise to creep in without disrupting
the message. The other reason is that it is nonlocal; the information is carried in the
entanglement between multiple qubits, which protects it against local decoherence and
depolarization. These observations motivate the general deﬁnition of a quantum code
as a code subspace - a k-qubit subspace of a larger n-qubit Hilbert space out of which
we can build states we wish to protect. In the Shor code the code subspace is spanned
by the states |±⟩. Given a code subspace HC⊆H we can always deﬁne an encoding
transformation Uenc with the property that
|¯c⟩ =Uenc|c1...c k, 0... 0|{z}
n−k zeros
⟩, (4.3)
with|¯c⟩ a complete basis forHC.
To describe error correction more generally, we ﬁrst need to say more about how to
understand the noise generated in a quantum systemS interacting with an environment.
In such a situation we can always write
Unoise|s0⟩ =
∑
s′,e
⟨s′e|Unoise|s0⟩|s′e⟩≡
∑
e
Me|se⟩, (4.4)
26It is not hard to describe this procedure in terms of unitary interaction Ucorrect with an ancillary
system. For example to measure Z1Z2 we introduce a single ancilla qubit in the state |0⟩anc and then
use two CNOT gates with the ﬁrst and second qubits being the control bits in the gate. This accom-
plishes|b1,b 2⟩|0⟩anc→|b1,b 2⟩|b1⟩anc→|b1,b 2⟩|b1 +b2⟩anc, which writes the result of the measurement
onto the ancillary qubit.
– 28 –
where|e⟩ is an orthonormal basis for the environment and the operators Me are called
Kraus operators [54]. They act only on the system S, have matrix elements
⟨s′|Me|s⟩ =⟨s′e|Unoise|s0⟩, (4.5)
and obey ∑
e
M†
eMe = 1. (4.6)
A set of operators Me obeying (4.6) is sometimes called a quantum channel , or occa-
sionally a superoperator.
The Kraus operators can be awkward to work with in practice because their deﬁni-
tion depends on the details of the interaction with the environment, which we usually
do not know. It is therefore convenient to expand them in a standard basis Eα of
operators such as the 2 2n distinct products of the Pauli operators
Me =
∑
α
CαeEα, (4.7)
and rewrite
Unoise|s⟩|0⟩ =
∑
α
Eα|s⟩|α⟩. (4.8)
Here we have deﬁned|α⟩≡ ∑
eCαe|e⟩, which are no longer necessarily orthonormal.
In this language there is a necessary and suﬃcient condition for when exact error
correction is possible for a given code [55, 56]. A setE of errorsEα is exactly correctable
if and only if
⟨¯c′|E†
αEβ|¯c⟩ =δcc′Cαβ (4.9)
for any |¯c⟩,|¯c′⟩ in some orthonormal basis for the code space, for any Eα,Eβ ∈E ,
and with the coeﬃcents Cαβ independent of c. If the Kraus operators produced by the
interaction with the environment can be written only in terms of Eα’s in a set E with
this property, then a generalization of the procedure described above for the Shor code
will always allow the state to be recovered perfectly.
To build some intuition for this criterion, consider the trivial code Uenc = 1. The
codespace is spanned by states of the form
|¯c⟩ =|c1...c k, 0... 0⟩. (4.10)
There is an obvious set of n−k “check” operators acting on this code space with
eigenvalue one; the spin Z operators acting on the last n−k qubits. As suggested
above we can take the Eα’s to be some subset of the 2 2n distinct products of Pauli
matrices, which in general we can write as
Xα1
1 Zβ1
1 ...X αn
n Zβn
n . (4.11)
– 29 –
The parameters α1,β 1,... take the values 0 or 1. This set of errors has the special
property that each element either commutes or anticommutes with each of the check
operators, so the condition (4.9) implies that the matrix Cαβ will be zero for any two
errorsEα,Eβ inE unless they commute with the same set of check operators. Moreover
it further implies that in the event that Cα,β⁄= 0 then the product E†
αEβ is equal to a
product of check operators. Now say we have a channel
∑
α
Eα|¯c⟩|α⟩, (4.12)
with allEα with|α⟩⁄ = 0 in a setE obeying (4.9). Channels with this property are called
exactly correctable. By measuring the check operators we can collapse this state to one
where all remainingEα’s commute with the same with the same set of check operators.
We may then pick any one of the remaining Eα’s and apply E†
α to restore the state|¯c⟩,
since in each term this produces some product of check operators which acts trivially
on the code space. This correction procedure is easily extended to the general case of
nontrivialUenc. We can simply take the set E of correctable errors for the trivial code
and conjugate it by Uenc to deﬁneE′ = UencEU†
enc. The check operators can be taken
to be UencZiU†
enc for the last n−k Pauli spin Z operators. This construction is not
unique since for a given code subspace there will be many Uenc’s which satisfy (4.3). Of
course channels are not always exactly correctable, and when they are not a would-be
quantum repair-person needs to look at the set of possible corrections consistent with
the result of the check operator measurements and then make her best guess about
which one to apply based on her understanding of which errors are most likely. This
procedure is sometimes called Maximal Likelihood Decoding.
The correction protocol just described is not necessarily the best one in general
situations. The transformation Uenc relates the “logical” basis in which the code is
trivial to the “computational” basis in which the interactions with the environment are
simple. The set of conjugated Pauli errors we just discussed is simple from the point
of view of the logical basis, but depending on the complexity of Uenc it could be quite
unnatural from the point of view of the computational basis. In particular we usually
expect the Kraus operators to be simple in the computational basis, and insisting on
expanding them in the conjugated Pauli basis will lead to more nonzero |α⟩’s than are
really necessary. A simple example of this that we will use below is the depolarizing
channel, which acts on a single qubit coupled to a 4-state environment as
Unoise :|Ψ⟩|0⟩↦−→ 1
2
[
|Ψ⟩|0⟩ +X|Ψ⟩|1⟩ +Y|Ψ⟩|2⟩ +Z|Ψ⟩|3⟩
]
. (4.13)
The Kraus operators for this channel areI/2,X/ 2,Y/ 2,Z/ 2, and it is not hard to verify
that it maximally entangles the qubit with the environment, erasing any information
– 30 –
about the initial state |Ψ⟩. More generally, the erasure channel is deﬁned as applying
this channel to some known set of l out of our n total qubits. The total set of errors
appearing in the channel is then 2 2l, but if we conjugate them by Uenc and re-expand
in the Pauli basis we in general ﬁnd more. Moreover even if the set of 2 2l erasures obey
the correctability condition (4.9), it will not in general be possible to ﬁnd some set of
conjugated Pauli’s that do. For stabilizer codes [57], a widely studied set of codes that
we review brieﬂy in the following subsection, the encoding transformation sends Pauli
errors to Pauli errors and we can use the check operator correction procedure described
above. For more general Uenc we need to do something else. 27
