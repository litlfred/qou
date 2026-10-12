---
doc_id: arxiv-2104.04941v2
doc_title: "Fock–Goncharov Coordinates for Semisimple Lie Groups"
section_id: sec-001-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 2104.04941v2.pdf
source_sha256: 84426ed37754aa78
toc_source: outline
---
2
1.1.
Classical Teichmüller space
3
1.2.
Cluster ensemble structures
4
1.3.
Higher Teichmüller spaces
5
1.4.
Results
6
1.5.
Historical context
7
2.
Ingredients
8
2.1.
Root spaces and Weyl groups
8
2.2.
Unipotent subgroups
9
2.3.
Coxeter elements
9
2.4.
Generalized minors
9
2.5.
Factorization coordinates
11
2.6.
Quivers
11
2.7.
Cluster ensembles
12
3.
Key identities
13
3.1.
Actions of σG
13
3.2.
Grid exchange relations
14
4.
Coordinates on generically-decorated representations
15
4.1.
Conﬁgurations and gluings
16
4.2.
Triangular quivers and Fock–Goncharov coordinate structures
17
4.3.
From coordinates to representations
21
4.4.
Regarding 3-manifolds
23
5.
Main Result: Fock–Goncharov coordinate structures for non-An
23
5.1.
Overview
23
5.2.
Building the rectangle Q0
24
5.3.
Construction of µrot
25
5.4.
The A• edge
26
5.5.
Construction of µﬂip
27
5.6.
The map M
29
5.7.
The signiﬁcance of the “twisting” mutations
31
6.
Construction for An
32
E-mail address: sgilles@sgilles.net.
Date: 2021-03-24.
1
7.
Proof of Theorem 4.19 for simple G
33
7.1.
Overview
33
7.2.
Ordering mutations
34
7.3.
Rotation mutations
36
7.4.
Flip mutations
40
8.
Proof of Theorem 4.19 for semisimple G
43
9.
Examples
44
9.1.
A5
44
9.2.
B3
45
9.3.
D5
46
9.4.
G2
47
9.5.
E6
48
9.6.
E7
50
9.7.
E8
51
9.8.
D2 = A1 × A1
51
9.9.
A3 × C2
51
References
53
Acknowledgements
I owe thanks to far too many people to list them all by name. My professors have shared their time and
expertise with me, my oﬃce-mates have put up with me for multiple semesters, and my employers have given
me ﬂexibility to complete my research. I am grateful to them all.
My advisor, Professor Zickert, has provided me with expert guidance and mentoring over the years. He
has helped me to achieve the goal for which I began my study, and words cannot express my appreciation.
Finally, I would like to thank S. Kane, who taught me the meaning of work, and whom I am unable to
repay.
Soli Deo Gloria.
1. Introduction
The program of Fock–Goncharov, starting with [FG06b], aims to describe representation spaces of hyper-
bolic surfaces into Lie groups by moduli spaces deﬁned by polynomial equations. These moduli spaces carry
a positive structure (see Deﬁnition 4.23), and in the case of the Lie group PSL2(R), the associated positive
spaces can be identiﬁed with Teichmüller space and decorated Teichmüller space. For more complicated Lie
groups, these positive spaces give (decorated) higher Teichmüller spaces.
Our result regards an additional structure, a cluster ensemble structure (see Section 2.7), which allows
manipulating these moduli spaces eﬃciently via quivers.
(a) Cutting Σ into a fundamental domain.
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
· · ·
(b) Embedding a fundamental domain for Σ
into the disk model for hyperbolic space.
Figure 1. Putting a hyperbolic structure on Σ.
2
