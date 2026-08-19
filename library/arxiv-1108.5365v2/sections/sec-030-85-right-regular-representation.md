---
doc_id: arxiv-1108.5365v2
doc_title: "Representation of the Quantum Plane, its Quantum"
section_id: sec-030-85-right-regular-representation
section_title: "Right regular representation"
section_number: 8.5
pages: 85-87
source_pdf: 1108.5365v2.pdf
source_sha256: 000961ede2234231
doc_brief: "Representation of the Quantum Plane, its Quantum — We give complete detail of the description of the GNS represe ntation of the quantum plane A and its dual ˆA as a von Neumann algebra."
---
Similarly by applying the pairing to the right regular corepresentation we obtain
Theorem 8.14. The right regular corepresentation is equivalent to
L2(R,ds 1)⊗
∫
R
∫ ⊕
R+
Pλ,−s2/2|Sb(Q + 2iλ)|2dλds2.
Proof. We apply the pairing to (7.73) and get
K0 = e−πb s2
2 ,
K = eπbt2,
E = (−iq1/2)(−q2)e−πiQb
1−q2 e
πb
2 s2e−πbt2
(
eπb(2t1+2t2)e2πb(−pt1 +pt2 )+
Gb( Q
2−it1−it2)Gb( Q
2 +it1−it2)
Gb( Q
2−it1−it2−b)Gb( Q
2 +it1−it2−b)
e2πbpt2
)
= i
q−q−1e
πb
2 s2e−πbt2
(
eπb(−2pt1 +2t1+2pt2 +t2)+
q1/2(1 +q−1e2πb(t1+t2))(1 +q−1e2πb(−t1+t2))e2πbpt2
)
85
= i
q−q−1e
πb
2 s2
(
eπb(2pt2 −t2) +eπb(2pt2 +3t2) + (e2πbt1 +e−2πbt1 +eπb(−2pt1 +2t1))eπb(2pt2 +t2)
)
,
F = iq−1/2eπiQb
1−q2 e
πb
2 s2+πbt2e−2πbt2−πbs2e−2πbpt2
= i
q−q−1e− πb
2 s2e−πb(t2+2pt2 ).
Again by shifting pt1↦→pt1 +t1 as in the left representation, the action of E
becomes
E = i
q−q−1e
πb
2 s2
(
eπb(2pt2 −t2) +eπb(2pt2 +3t2) + Ceπb(2pt2 −t2)
)
.
Hence under the unitary transformation Φ, E becomes
E = i
q−q−1e
πb
2 s2
(
eπb(2pt2 −t2) +eπb(2pt2 +3t2) + (e2πbλ +e−2πbλ)eπb(2pt2 −t2)
)
.
Finally, the remaining transformation used in the left regular repres entation
doesn’t change these actions. In exactly the same way if we apply:
multiplication by G b(Q
2 +iλ−it2)−1,
◦t2↦→−t2 : t2↦→−t2,p t2↦→−pt2,
◦e−πit2λ : pλ↦→pλ− t2
2,p t2↦→pt2− λ
2,
◦e− πi
2 s2t2 : ps2↦→ps2 + t2
4,p t2↦→pt2 + s2
4 ,
that does not change the left representation either, it becomes:
K0 = e−πb s2
2
K = e−πbt2
E = i
q−q−1 (q
1
2eπb(t2−λ) +q− 1
2e−πb(t2−λ))e−2πbpt2
= [ Q
2b− i
b (t2−λ)]qe−2πbpt2
F = i
q−q−1 (q− 1
2eπb(t2+λ) +q
1
2e−πb(t2+λ))e2πbpt2
= [ Q
2b + i
b (t2 +λ)]qe2πbpt2
which is precisely the representation denoted by Pλ,−s2/2.
86
Combining Theorem 8.11 and 8.14, and note that all the transformat ions used
are unitary, we conclude the main theorem:
Theorem 8.15. As a representation of Uq(gl(2, R))L⊗Uq(gl(2, R))R,
L2(GL+
q (2, R))≃
∫ ⊕
R
∫ ⊕
R+
Pλ,s⊗P λ,−s|Sb(Q + 2iλ)|2dλds (8.21)
and the equivalence is unitary.
In particular, we proved Ponsot-Teschner’s claim in [31] for Uq(sl(2, R)) by set-
ting s2 = 0 which corresponds to the determinant element N =A ˆA, as well as the
action of the central element K0.
