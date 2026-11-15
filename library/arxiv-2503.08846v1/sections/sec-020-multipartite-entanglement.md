---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-020-multipartite-entanglement
section_title: "Multipartite Entanglement"
section_number: null
pages: 43-44
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Multipartite Entanglement
In section 4.2 we reviewed classification of bipartite entanglement and showed that a classification similar
to SLOCC is possible in terms of the number of connections (Wilson lines) held by the two subsystems.
How does this classification works for multipartite systems?
For a 3-qubit system the SLOCC classification expects four distinct classes, two of which are bisep-
arable (either all three qubits are separable, or two of them in the Bell-type entanglement). The other
two classes correspond to genuinely tripartite entanglement: the GHZ class and the W class [95]. We
can try to use the same idea as in section 4.2 and draw all possible “connectome diagrams” of three S2
boundaries with four punctures [59]:
.
(173)
The first diagram clearly depicts a completely separable state of three qubits, but also diagrams number
two, three and four, since in those diagrams parties are connected with other parties by at most two lines.
In such a case the lines can be cut, as explained in section 4.2. Similarly, diagrams number five and six
are biseparable, corresponding to a Bell pair and a separable qubit. The last diagram expresses the state
= |000⟩+
1
√
d2 −1
|111⟩,
(174)
which is not exactly the GHZ state, but a state in the GHZ class. No connectome diagram exists to
represent the W class.
The SLOCC classification points to existence of some properties of entanglement that are not captured
by the “classical” connectome diagrams. (Recall that in the classical limit the connectomes label large
43
classes of diagrams.) Perhaps, a more refined topological classification exists, and there is a diagram
representing a genuine W state. See some suggestions in [71], although those apply to higher dimensional
Hilbert spaces, where SLOCC does not work. Note that W state certainly exists as a linear combination
of diagrams, but there is no single diagram that would reduce to it in the classical limit.
Classical limit was also essential in the derivation of entanglement inequalities in section 4.4. The
above observation reminds that one should not take them for granted in the full quantum regime. The
study of connectome inequalities in [102] showed that many known inequalities for entanglement entropy
can be reproduced by the simple counting of the connectome method, although in some cases the latter
produces identities, which saturate the inequalities. This is the case of monogamy of mutual information,
which reads
S(A + B) + S(B + C) + S(A + C) ≥S(A + B + C) + S(A) + S(B) + S(C) .
(175)
and a family of similar relations studied in [109], for example. It is not hard to check, that counting
connections indeed saturates this inequality.
Are there quantum states that violate the connectome inequalities? As in the example of the W state,
inaccessible to connectomes, such state would have to be “more quantum” then the semiclassical states
satisfying the connectome inequalities.
