---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-3
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
Introduction
3
2.
Structure Types
4
2.1.
Categoriﬁcation of
N and
N[[z]]
4
3.
Structure Types and the Harmonic Oscillator
8
3.1.
The Quantum Harmonic Oscillator
9
3.2.
Structure Types and the Weyl Algebra
11
4.
StuﬀTypes
14
4.1.
Groupoids
14
4.2.
StuﬀTypes as a Generalization of Structure Types
20
4.3.
StuﬀTypes As Power Series
24
4.4.
Forgetful Functors: Properties, Structure, and Stuﬀ
27
5.
StuﬀTypes And Quantum Mechanics
30
5.1.
Inner Product of StuﬀTypes
30
5.2.
StuﬀOperators
34
5.3.
Feynman Diagrams and StuﬀOperators
38
6.
M-StuﬀTypes And Quantum Mechanics
43
6.1.
M-StuﬀTypes
44
6.2.
Quantum Mechanics: M = U(1)
50
7.
Conclusions
56
7.1.
Categoriﬁed Quantum Mechanics
56
7.2.
Other Generalizations
58
8.
Acknowledgements
60
Appendix A.
A Little Higher-Dimensional Algebra
61
Appendix B.
Slice Categories and 2-Categories
62
B.1.
2-Categories of StuﬀTypes and StuﬀOperators
62
Appendix C.
Categorical Approaches to Generalizing Species
66
C.1.
Generalized Species
66
References
68
CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS
3
1. Introduction
One reason for the success of category theory has been its ability to describe rela-
tions between seemingly separate areas of mathematics. Here, we will describe how
category theory can be used to see relationships between enumerative combinatorics
and quantum mechanics. Speciﬁcally, we examine an approach to understanding
the quantum harmonic oscillator by “categorifying” the Fock representation of the
Weyl algebra - which is the algebra of operators on states of the oscillator. This
builds on work described by Baez and Dolan[1]. Since we do not expect readers to
be expert in both quantum mechanics and category theory, we have tried to make
this paper as self-contained as possible. Many deﬁnitions and explanations will be
well-known to the experts in each ﬁeld, and are arranged by section as much as
possible to allow readers to skip familiar material.
Categoriﬁcation is best understood as the reverse of “decategoriﬁcation”. This
is a process which begins with some category, and produces a structure for which
isomorphisms in the original category appear as equations between objects instead.
Categoriﬁcation is the reverse process, replacing equations in some mathematical
setting with isomorphisms in some category in a consistent - but possibly non-
unique - way.
One example is the way we can treat the category of ﬁnite sets
as a categoriﬁcation of the natural numbers
N. The set
N can be seen as a set of
cardinalities indexing isomorphism classes of ﬁnite sets, and which get their addition
and multiplication from the categorical coproduct and product on the category of
ﬁnite sets. We will see further examples of a connection between decategoriﬁcation
and cardinality.
