---
doc_id: malkin-2021-galois-action-on-motivic-fundamental-groups-thes
doc_title: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-7
source_pdf: malkin-2021-galois-action-on-motivic-fundamental-groups-thesis.pdf
source_sha256: 3bc30dc6a4a03a7f
toc_source: outline
doc_brief: "On the Galois action on motivic fundamental groups of punctured elliptic and rational curves — On the Galois Action on Motivic Fundamental Groups of Punctured Elliptic and Rational Curves Nikolay"
---
Abstract
On the Galois Action on Motivic Fundamental Groups
of Punctured Elliptic and Rational Curves
Nikolay Malkin
2021
The main motive of this thesis is to study the action of the motivic Galois group on the motivic fundamental
group of an algebraic curve 푋punctured at a ﬁnite set of points 푆:
GalMot ⟳휋Mot
1
(푋−푆, 푣0).
(1)
The algebraic, geometric, and analytic aspects of this action are examined in two cases: for 푋= P1 and for 푋
an elliptic curve.
To study this action, we rely on motivic correlators, canonical elements in the fundamental Lie coalgebra
of the category of mixed motives over a number ﬁeld. We trace three themes:
(1) The Lie coalgebra structure on the motivic correlators. Using combinatorial arguments with an injection
of Hodge theory, we ﬁnd general families of relations (double shuﬄe relations) on these elements.
(2) The Hodge realization of the structure in (1). The canonical real periods of the motivic correlators are
the Hodge correlator functions, functions of several 푋-valued variables that are computed as Feynman
integrals. We ﬁnd new functional equations on the Hodge correlator integrals. The proofs of results
related to themes (1) and (2) are closely intertwined.
(3) The geometry of modular manifolds. The phenomenon that the complex computing cohomology of some
locally symmetric space can be mapped to the standard cochain complex of the motivic Lie coalgebra had
been observed in several cases. Our work on Bianchi hyperbolic threefolds and the motivic fundamental
groups of CM elliptic curves is a variation on this theme.
On the Galois Action on Motivic Fundamental Groups
of Punctured Elliptic and Rational Curves
A Dissertation
Presented to the Faculty of the Graduate School
of
Yale University
in Candidacy for the Degree of
Doctor of Philosophy
by
Nikolay Malkin
Dissertation Director: A.B. Goncharov
June 2021
Copyright © 2021 by Nikolay Malkin
All rights reserved.
Contents
List of ﬁgures
v
Acknowledgments
vi
1
Introduction
1
1.1
Hodge and motivic correlators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.1.1
Hodge correlator integrals . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
2
1.1.2
Correlator coalgebra and fundamental group
. . . . . . . . . . . . . . . . . . . . .
4
1.2
Mixed Tate motives and correlators on rational curves . . . . . . . . . . . . . . . . . . . . .
10
1.2.1
Hodge correlators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
1.2.2
Motivic correlators . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
1.2.3
Multiple polylogarithms
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
2
Shuﬄe relations for Hodge and motivic correlators on P1
26
2.1
Introduction and main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
2.1.1
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
2.1.2
Hodge correlator integrals and shuﬄe relations . . . . . . . . . . . . . . . . . . . .
28
2.1.3
Quasidihedral Lie coalgebras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
33
2.1.4
Relations for Hodge and motivic correlators . . . . . . . . . . . . . . . . . . . . . .
36
2.2
Construction of the quasidihedral Lie coalgebra . . . . . . . . . . . . . . . . . . . . . . . .
37
2.2.1
Deﬁnitions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
37
2.2.2
Proof of Theorem 2.5 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
44
2.3
Specialization theorem for Hodge correlators
. . . . . . . . . . . . . . . . . . . . . . . . .
63
2.4
The second shuﬄe relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
68
2.4.1
Proofs of Theorems 2.1, 2.6, and 2.7 . . . . . . . . . . . . . . . . . . . . . . . . . .
68
2.4.2
Applications
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
3
Motivic 휋1 of CM elliptic curves and geometry of Bianchi hyperbolic threefolds
74
3.1
Introduction and main results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
3.1.1
Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
3.1.2
Relations for correlators
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
79
3.2
Motivic correlators on elliptic curves . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
3.2.1
Main properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
81
3.2.2
Symmetric correlators modulo depth . . . . . . . . . . . . . . . . . . . . . . . . . .
85
3.2.3
Second shuﬄe relations
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
92
3.3
Bianchi hyperbolic threefolds and modular complexes . . . . . . . . . . . . . . . . . . . . .
93
3.3.1
Bianchi tessellations and orbifolds . . . . . . . . . . . . . . . . . . . . . . . . . . .
93
3.3.2
Modular complexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
95
3.3.3
Relating the modular and Bianchi complexes to the Galois Lie coalgebra . . . . . . .
98
3.4
Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
101
3.4.1
The weight 4 case: Euler complexes . . . . . . . . . . . . . . . . . . . . . . . . . .
101
3.4.2
Degeneration to rational curves: Voronoi complexes and multiple 휁-values
. . . . .
104
References
112
