---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-2
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
arXiv:1511.00400v2  [math.GT]  26 May 2016
Reidemeister torsion, hyperbolic three-manifolds,
and character varieties
Joan Porti∗
November 6, 2018
Abstract
This is a survey on Reidemeister torsion for hyperbolic three-manifolds
of ﬁnite volume. Torsions are viewed as topological invariants and also as
functions on the variety of representations in SL2(C). In both cases, the
torsions may also be computed after composing with ﬁnite dimensional
representations of SL2(C). In addition the paper deals with the torsion
of the adjoint representation as a function on the variety of PSLn+1(C)-
characters, using that the ﬁrst cohomology group with coeﬃcients twisted
by the adjoint is the tangent space to the variety of characters.
MSC: 57Q10; 57M27
Keywords: Reidemeister torsion; hyperbolic three-manifold; character va-
riety.
Contents
1
Introduction
2
2
Combinatorial and analytic torsions
4
2.1
Combinatorial torsion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.1.1
Torsion of a chain complex
. . . . . . . . . . . . . . . . . . . . . . . . . . .
4
2.1.2
Twisted chain complexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Geometric properties of combinatorial torsion . . . . . . . . . . . . . . . . . . . . .
7
2.2.1
Mayer-Vietoris . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.2
Polynomials
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
2.2.3
Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
2.3
Analytic torsion
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
3
Torsion of hyperbolic three-manifold with representations in SL2(C)
15
3.1
Torsions from lifts of the holonomy representation . . . . . . . . . . . . . . . . . .
16
3.1.1
Lifts of the holonomy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
3.1.2
Torsions for closed 3-manifolds . . . . . . . . . . . . . . . . . . . . . . . . .
17
3.1.3
Cusped hyperbolic 3-manifolds . . . . . . . . . . . . . . . . . . . . . . . . .
18
3.1.4
The twisted polynomial
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
3.2
Torsion on the variety of characters . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
3.2.1
The distinguished curve of characters . . . . . . . . . . . . . . . . . . . . .
19
3.2.2
Torsion on the distinguished curve of characters . . . . . . . . . . . . . . .
20
3.2.3
Dehn ﬁlling space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
3.2.4
Torsion for Dehn ﬁllings . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
3.2.5
Branched coverings on the ﬁgure eight . . . . . . . . . . . . . . . . . . . . .
25
∗Partially supported by Mineco through grant MTM2012-34834
1
4
Torsions for higher dimensional representations of hyperbolic three-manifolds 26
4.1
Representations of SL2(C) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
4.2
Higher torsions for closed manifolds . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
4.3
Functions on the variety of characters
. . . . . . . . . . . . . . . . . . . . . . . . .
29
4.3.1
Generic cohomology on the distinguished component . . . . . . . . . . . .
29
4.3.2
Higher torsions on the variety of characters . . . . . . . . . . . . . . . . . .
30
4.4
Evaluation at the holonomy
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
4.4.1
Cohomolgy at the character of the holonomy . . . . . . . . . . . . . . . . .
32
4.4.2
Torsion at the characters of the holonomy
. . . . . . . . . . . . . . . . . .
33
4.4.3
Dehn ﬁlling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
4.5
Quantum invariants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
35
5
Representations in PSLn+1(C) and the adjoint
36
5.1
Local parameters and change of curve
. . . . . . . . . . . . . . . . . . . . . . . . .
39
5.2
An example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
41
5.2.1
Computations for X(M3, PSL2(C)) . . . . . . . . . . . . . . . . . . . . . .
42
5.2.2
Computations for X(M3, PSL3(C)) . . . . . . . . . . . . . . . . . . . . . .
43
Appendix A Not approximating the trivial representation
44
Appendix B Cohomology on the variety or characters
45
B.1
The complete structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
B.1.1
The ﬁnite volume case . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
46
B.1.2
A basis in cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
B.2
Generic representations in the distinguished component. . . . . . . . . . . . . . .
49
