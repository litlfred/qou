---
doc_id: arxiv-1810.11563v1
doc_title: "Three Lectures on Complexity and Black Holes Leonard Susskind"
section_id: sec-039-221-the-protocol
section_title: "The Protocol"
section_number: 22.1
pages: 73-75
source_pdf: 1810.11563v1.pdf
source_sha256: 8e17ac8b91bc3cc9
doc_brief: "Three Lectures on Complexity and Black Holes Leonard Susskind — This is the written version of three lectures on complexity and black holes given at PiTP 2018 summer program entitled ”From Qubits to"
---
Here is the circuit that accomplishes the task:
72
Figure 36
Let me explain ﬁgure 36. The initial state is,
|Ψ⟩ =|max⟩⊗| 0⟩ (22.91)
The single-qubit gates H are Hadamard gates, which have the following action,
H|0⟩ = 1√
2
(
|0⟩ +|1⟩
)
H|1⟩ = 1√
2
(
|0⟩−| 1⟩
)
(22.92)
The protocol begins with a Hadamard acting on the clean qubit to transform it to
(
|0⟩ +
|1⟩
)
.
Next, a “controlled” G operation acts. The dot at the bottom indicates a controlled
operation: if the clean qubit is in the state |0⟩ then the unitary operator G acts on the
remaining qubits; if the clean qubit is in state |1⟩ then G does not act and |max⟩ is left
undisturbed. The last element of the circuit is another Hadamard.
It is straightforward to follow the circuit and see that the ﬁnal state is,
|Ψ′⟩ = 1
2
(
G + 1
)
⊗| 0⟩
+ 1
2
(
G− 1
)
⊗| 1⟩ (22.93)
Finally we compute the expectation value of the Z Pauli operator for the clean qubit
(which by the way, is no longer clean).
⟨Z⟩ =⟨max|
(G† +G
2
)
|max⟩ (22.94)
We now make use of the fact that|max⟩ is maximally complex. A maximally complex
73
state is Haar-random, which allows us to replace the expectation value by the normalized
trace,
⟨Z⟩ = Tr
(G† + G
2
)
(22.95)
Thus the circuit transforms the initial state to a ﬁnal state that indeed has information
about TrG. Of course that is not the end of the story; we still have to measureZ and repeat
the procedure enough times to determine the ⟨Z⟩ but that is not part of the reversible
process that we deﬁne to be the computational work.
It is also possible to determine Tr
(
G†−G
2
)
by a similar method which I will leave to
you.
