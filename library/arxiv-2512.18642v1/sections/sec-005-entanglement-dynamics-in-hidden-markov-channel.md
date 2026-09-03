---
doc_id: arxiv-2512.18642v1
doc_title: "A Hidden Quantum Markov model framework for"
section_id: sec-005-entanglement-dynamics-in-hidden-markov-channel
section_title: "Entanglement Dynamics in Hidden Markov Channel"
section_number: null
pages: 12-15
source_pdf: 2512.18642v1.pdf
source_sha256: c4c7f8b0a719aa2d
doc_brief: "A Hidden Quantum Markov model framework for — This paper introduces a hidden quantum Markov models (HQMMs) framework to the Af- fleck–Kennedy–Lieb–Tasaki (AKLT) state—a cornerstone example of a"
---
To analyze the entanglement properties of a quantum channel Λ :B(H in)→B(H out), we employ
the Choi–Jamio/suppress lkowski isomorphism:
J(Λ) = (id in⊗Λ)
(
|Ω⟩⟨Ω|
)
,
where|Ω⟩= 1√din
∑din
i=1|i⟩ref⊗|i⟩ in is a maximally entangled state between a reference system
Href∼=Hin and the input systemH in [39]. This construction provides a complete characterization
of the channel’s ability to preserve or generate entanglement. Our primary system is the spin-½
12
Hilbert spaceH 1
2
∼= C2, with the standard basis{|↑⟩,|↓⟩}representing spin-up and spin-down
states. We define two particular entangled states of two qubits:
|Ψ−⟩= 1√
2(|↑↓⟩−|↓↑⟩),|Ψ +⟩= 1√
2(|↑↓⟩+|↓↑⟩),
which are two of the four Bell states. The two-dimensional subspace spanned by these states is
denoted byS= span{|Ψ −⟩,|Ψ +⟩}⊂H 1
2
⊗H 1
2
.
The isometryV:H 1
2
→H 1
2
⊗H 1
2
encodes a single spin into a specific two-spin entangled
subspace:
V=|Ψ −⟩⟨↑|+|Ψ +⟩⟨↓|.
This map satisfiesV †V=I 2, confirming it preserves the inner product, and its image is precisely
S.
From this isometry, we naturally obtain two complementary quantum channels. Theencoding
channelE ∗
H :B(H 1
2
)→B(H 1
2
⊗H 1
2
) embeds a single-qubit state into the two-qubit space:
E∗
H(ρ) =VρV †.
The adjoint channelE H :B(H 1
2
⊗H 1
2
)→B(H 1
2
) acts as a decoder, extracting information from
the two-qubit system back to a single qubit:
EH(X) =V †XV.
Theorem 4.1.Consider the encoding channelE ∗
H defined above. Its Choi–Jamio/suppress lkowski state
J(E∗
H)is a pure state exhibiting maximal entanglement between the reference system and the
output subsystem. Concretely,
J(E∗
H) =|Ψ Choi⟩⟨ΨChoi|,|Ψ Choi⟩= 1√
2
(
|↑⟩ R⊗|Ψ−⟩B +|↓⟩ R⊗|Ψ +⟩B
)
,
whereRlabels the reference qubit andBthe output two-qubit system. The entanglement entropy
across theR|Bpartition is
S
(
ρR
)
=S
(
ρB
)
= 1ebit,
withρ R = TrBJ(E∗
H)andρ B = TrRJ(E∗
H). This shows thatE ∗
H perfectly preserves one ebit of
entanglement with a reference system, achieving the theoretical maximum for an encoding from
one qubit to two qubits restricted to the Bell subspaceS.
Proof.We proceed through a systematic construction and analysis of the Choi state. SinceE ∗
H
takes a single qubit as input, we haved in = 2. We identify the reference system basis with the
input basis:|↑⟩ R corresponds to|↑⟩ in and|↓⟩ R to|↓⟩ in. The maximally entangled state between
reference and input is therefore
|Ω⟩= 1√
2
(
|↑⟩ R|↑⟩ in +|↓⟩ R|↓⟩ in
)
.
Applying the identity on the reference and the channel on the input gives:
J(E∗
H) = 1
2
∑
i,j∈{↑,↓}
|i⟩⟨j|R⊗V|i⟩⟨j| inV†.
Using the defining action ofV, namelyV|↑⟩=|Ψ −⟩andV|↓⟩=|Ψ +⟩, we obtain:
J(E∗
H) = 1
2
(
|↑⟩⟨↑| R⊗|Ψ−⟩⟨Ψ−|B+|↑⟩⟨↓| R⊗|Ψ−⟩⟨Ψ+|B+|↓⟩⟨↑| R⊗|Ψ+⟩⟨Ψ−|B+|↓⟩⟨↓| R⊗|Ψ+⟩⟨Ψ+|B
)
.
13
This operator is precisely the projector onto the pure state|Ψ Choi⟩as stated in the theorem.
Since|Ψ Choi⟩is pure, we can compute the reduced states by partial tracing. For the reference
system:
ρR = TrB|ΨChoi⟩⟨ΨChoi|
= 1
2
(
⟨Ψ−|Ψ−⟩|↑⟩⟨↑|+⟨Ψ −|Ψ+⟩|↑⟩⟨↓|+⟨Ψ +|Ψ−⟩|↓⟩⟨↑|+⟨Ψ +|Ψ+⟩|↓⟩⟨↓|
)
The Bell states are orthonormal:⟨Ψ ±|Ψ±⟩= 1 and⟨Ψ −|Ψ+⟩= 0. Thus,
ρR = 1
2
(
|↑⟩⟨↑|+|↓⟩⟨↓|
)
= I2
2.
The von Neumann entropy of this completely mixed qubit state isS(ρ R) =−Tr(ρ R log2ρR) = 1
ebit.
For the output systemB:
ρB = TrR|ΨChoi⟩⟨ΨChoi|= 1
2
(
|Ψ−⟩⟨Ψ−|+|Ψ +⟩⟨Ψ+|
)
.
To express this in the computational basis, we write:
|Ψ−⟩= |↑↓⟩−|↓↑⟩√
2 ,|Ψ +⟩= |↑↓⟩+|↓↑⟩√
2 .
Then,
|Ψ−⟩⟨Ψ−|= 1
2
(
|↑↓⟩⟨↑↓|−|↑↓⟩⟨↓↑|−|↓↑⟩⟨↑↓|+|↓↑⟩⟨↓↑|
)
,
|Ψ+⟩⟨Ψ+|= 1
2
(
|↑↓⟩⟨↑↓|+|↑↓⟩⟨↓↑|+|↓↑⟩⟨↑↓|+|↓↑⟩⟨↓↑|
)
.
Adding these and dividing by 2 yields:
ρB = 1
2
(
|↑↓⟩⟨↑↓|+|↓↑⟩⟨↓↑|
)
.
This density matrix has eigenvalues{ 1
2, 1
2,0,0}, givingS(ρ B) = 1 ebit as well.
For a pure bipartite state, the entanglement entropy is given by the von Neumann entropy
of either reduced density matrix. Here,S(ρ R) =S(ρ B) = 1. Since the reference system is a
single qubit, the maximum possible entanglement entropy is log 2 2 = 1 ebit. Our calculated value
saturates this bound, confirming that|Ψ Choi⟩is maximally entangled across theR|Bpartition
given the dimension constraints.
Remark 4.2.The encoding channelE ∗
H maps a single qubit isometrically into the two-dimensional
Bell subspaceSof two qubits. The fact that its Choi state carries exactly one ebit of entangle-
ment means that the channel can perfectly transmit one qubit of quantum information—its co-
herent information is maximal. Moreover, it preserves the maximum possible entanglement with
a reference system, which is the hallmark of an optimal quantum encoding. The corresponding
decoding channelE H reverses this process on the subspaceS, and both channels share the same
entanglement capacity as quantified by their Choi states. This structure reflects the essential role
of such encodings in valence-bond solid models and quantum error correction schemes.
14
