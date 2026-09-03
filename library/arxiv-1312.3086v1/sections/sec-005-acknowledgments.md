---
doc_id: arxiv-1312.3086v1
doc_title: "Quantum repeater with Rydberg blocked atomic ensembles in fiber-coupled cavities"
section_id: sec-005-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 9-9
source_pdf: 1312.3086v1.pdf
source_sha256: ff328e7c7cbdc70c
doc_brief: "Quantum repeater with Rydberg blocked atomic ensembles in fiber-coupled cavities — 7 sections: Introduction; The sequence; At the end of this sequence, the s"
---
E. B. thanks M. Raoult, Jean-Louis Le Gouet and F.
Prats for fruitful discussions.
Appendix A: Derivation of the expression of the
average number of steps in entanglement generation
As described in Sec. III, the entanglement generation
procedure is performed in two steps. During each of these
steps, K = N/2 subnodes are entangled by pairs. A pair
of subnodes is correctly entangled with the probability
P0.
Let us ﬁrst compute the probability pK (n) that K
pairs are correctly entangled within exactly n repetitions.
This means that, within the (n −1) ﬁrst steps, at least
one pair is not entangled. Considering all the possible
cases, one establishes the following recurrence formula
pK (n) = pK−1 (n) p1 (n) + pK−1 (n)
 n−1
X
m=1
p1 (m)
!
+
 n−1
X
m=1
pK−1 (m)
!
p1 (n)
= pK−1 (n)
 
n
X
m=1
p1 (m)
!
+
 n−1
X
m=1
pK−1 (m)
!
p1 (n)
and, noting that p1 (n) = P0 (1 −P0)n−1 one gets
pK (n) = pK−1 (n) [1 −(1 −P0)n]
(A1)
+
 n−1
X
m=1
pK−1 (m)
!
P0 (1 −P0)n−1 .(A2)
Setting SK (n) ≡Pn
m=1 pK (m), one derives from Eq.
(A1) the relation SK (n)
=
SK−1 (n) [1 −(1 −P0)n]
whence SK (n) = S1 (n) [1 −(1 −P0)n]
K−1 and, since
S1 (n) = [1 −(1 −P0)n], SK (n) = [1 −(1 −P0)n]
K.
One ﬁnally deduces the expression for pK (n) from
pK (n) = SK (n) −SK (n −1)
pK (n) = [1 −(1 −P0)n]K −
h
1 −(1 −P0)n−1iK
.
The average number of repetitions one needs to entangle
