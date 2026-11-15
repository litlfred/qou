---
doc_id: arxiv-2503.08846v1
doc_title: "A Tutorial on Knots and Quantum Mechanics"
section_id: sec-015-inequalities-for-the-entanglement-entropy
section_title: "Inequalities for the Entanglement entropy"
section_number: null
pages: 36-38
source_pdf: A_Tutorial_on_Knots_and_Quantum_Mechanics.pdf
source_sha256: 18321b615ffc968b
toc_source: outline
doc_brief: "A Tutorial on Knots and Quantum Mechanics — These notes review a description of quantum mechanics in terms of the topology of spaces, basing on the axioms of Topological Quantum Field Theory and path"
---
Inequalities for the Entanglement entropy
In the previous parts of section 4 we discussed expression of quantum entanglement in terms of topology
and showed how a specific measure of entanglement – the von Neumann entropy – gets a topological
expression. In this part we will discuss the entropy a little further and explain some of its well-known
properties in topological terms. Specifically, we will consider inequalities satisfied by the entanglement
entropy. The discussion becomes the most simple if we restrict ourselves to the limit of large k and of
large Hilbert spaces (that is Hilbert spaces of very large numbers of points) as introduced in section 3.4.
We will refer to this as the connectome limit.
36
A
B
C
ℓAB
NA
NB
NC
A
C
B
D
Figure 3: Topological presentation of correlations can be used to illustrate subadditivity (left) and strong
subadditivity (right).
First, let us discuss the property of entanglement entropy called subadditivity. Let us assume that in a
given quantum system one can separate a subsystem A and another subsystem B. Then the subadditivity
of the entropy is the statement that the entropy of the union of A and B is not greater than the sum of
entropies of A and B:
SvN(A + B) ≤SvN(A) + SvN(B) .
(157)
Instead of trying to interpret this inequality right away, let us first produce its topological analog.
Consider a generic state in the connectome limit. Note that the union A + B does not necessarily
represent the whole system, so there is also a complement A + B = C. Thus, a generic state will have the
form shown in figure 3 (left), where lines between subsystems A, B and C illustrate generic correlations
between them.
In the limit that we are applying, the correlations are quantified by the number of
connections. Let NA, NB and NC be the numbers of connections of the respective subsystems to the
remaining parts. Let ℓAB be the number of connections exclusively between A and B. Then a simple
relation holds:
NA + NB = NC + 2ℓAB ≥NC .
(158)
Since the entanglement entropy is proportional to the number of connections, with log 2 coefficient, the
subadditivity property (157) follows.
With the connectivity quantification of entanglement it is not hard to give an interpretation to the
subadditivity. The correlation of A and B with the rest of the system cannot exceed the the amount of
correlations in A and B taken together, simply because there might exist correlations between A and B.
The amount of correlation between A and B, in this case, is
ℓAB = (NA + NB −NC)/2 .
(159)
This is the topological version of what is known in Information Theory as mutual information I(A, B),
I(A, B) := SvN(A) + SvN(B) −SvN(A + B) .
(160)
If the system A + B does not have a complement (isolated) then SvN(A + B) = 0, SvN(A) = SvN(B) and
mutual information is essentially the same as the entanglement entropy.
Another very-well known inequality is strong subadditivity. It is formulated for three subsystems A,
B and C. The inequality states
SvN(A + B + C) + SvN(B) ≤SvN(A + B) + SvN(B + C) .
(161)
In terms of connectivity this inequality can be proven using the diagram shown in figure 3 (right), where
D = A + B + C. Denoting the number of connections as in the previous case one finds that
ND = NA+B + NB+C −2ℓAC −NB ≤NA+B + NB+C −NB ,
(162)
37
Φ+
B
ψ
Φ+
A
ψ
b
a
H
Xb
Za
Φ+
A
Φ+
B
b
a
b
a
H
Xb
Za
