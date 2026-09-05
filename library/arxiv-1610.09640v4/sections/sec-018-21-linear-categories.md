---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-018-21-linear-categories
section_title: "Linear Categories"
section_number: 2.1
pages: 33-33
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Deﬁnition 2.1.1.Let K be a commutative ring. A K-linear categoryis a cat-
egory M, endowed with aK-module structure on each of the sets of morphisms
HomM(M0,M 1). The condition is this:
•For allM0,M 1,M 2∈M the composition function
HomM(M1,M 2)×HomM(M0,M 1)→HomM(M0,M 2)
(φ1,φ0)↦→φ1◦φ0
isK-bilinear.
IfK =Z, we say thatM is alinear category.
As already mentioned in Convention 1.2.4, in our book all linear categories are
K-linear.
Proposition 2.1.2. Let M be aK-linear category.
(1) For every objectM∈M, the setEndM(M) := HomM(M,M ), with its given
addition operation, and with the operation of composition, is a centralK-
ring.
(2) For every two objectsM0,M 1∈M, the setHomM(M0,M 1), with its given
addition operation, and with the operations of composition, is a left module
over the ring EndM(M1), and a right module over the ring EndM(M0).
Furthermore, these left and right actions commute with each other.
Exercise 2.1.3. Prove Proposition 2.1.2.
This result can be reversed:
Example 2.1.4. Let A be a centralK-ring. Deﬁne a categoryM like this: there
is a single objectM, and its set of morphisms isHomM(M,M ) :=A. Composition
in M is the multiplication ofA. Then M is aK-linear category.
For a centralK-ring A, the opposite ringAop has the sameK-module structure
as A, but the multiplication is reversed.
Exercise 2.1.5. Let A be a nonzero ring. Let P,Q ∈ModA be distinct free
A-modules of rank1.
(1) Prove that there is a ring isomorphismEndModA(P )∼= Aop. Is this ring
isomorphism canonical?
(2) Let M be the full subcategory ofModA on the set of objects{P,Q}. Com-
pare the linear categoryM to the ring of matricesMat2(Aop).
