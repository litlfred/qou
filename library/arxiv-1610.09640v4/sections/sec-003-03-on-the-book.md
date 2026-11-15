---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-003-03-on-the-book
section_title: "On the Book"
section_number: 0.3
pages: 13-14
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
from the foundations, and going all the way to applications in commutative and
noncommutative algebra. The emphasis is on explicit constructions (with exam-
ples), as opposed to axiomatics. The most abstract concept we use is probably that
of an abelian category (which seems indispensable).
A special feature of this book is that most of the theory deals with the category
C(A, M) of DG A-modules in M, where A is a DG ring and M is an abelian category.
Here “DG” is short for “diﬀerential graded”, and our DG rings are more commonly
known as unital associative DG algebras.
See Subsections 3.3 and 3.8 for the
deﬁnitions.
The notion C(A, M) covers most important examples that arise in
algebra and geometry:
• The category C(A) of DG A-modules, for any DG ring A. This includes
unbounded complexes of modules over an ordinary ring A.
• The category C(M) of unbounded complexes in any abelian category M.
This includes M = Mod A, the category of sheaves of A-modules on a
ringed space (X, A).
13
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
The category C(A, M) is a DG category, and its DG structure determines the
homotopy category K(A, M) with its triangulated structure. We prove that every
DG functor F : C(A, M) →C(B, N) induces a triangulated functor
(0.3.1)
F : K(A, M) →K(B, N)
between the homotopy categories.
We can now reveal that in the previous subsections we were a bit imprecise (for
the sake of simplifying the exposition): what we referred to there as C(M) was
actually the strict subcategory Cstr(M), whose morphisms are the degree 0 cocycles
in the DG category C(M). For the same reason the homotopy category K(M) was
suppressed there.
The derived category D(A, M) is obtained from K(A, M) by inverting the quasi-
isomorphisms. If suitable resolutions exist, the triangulated functor (0.3.1) can be
derived, on the left or on the right, to yield triangulated functors
(0.3.2)
LF, RF : D(A, M) →D(B, N).
We prove existence of K-injective, K-projective and K-ﬂat resolutions in K(A, M)
in several important contexts, and explain their roles in deriving functors and in
presenting morphisms in D(A, M).
In the last six sections of the book we discuss a few key applications of derived
categories to commutative and noncommutative algebra.
