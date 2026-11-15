---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-019-21-linear-categories
section_title: "Linear Categories"
section_number: 2.1
pages: 33-33
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
Deﬁnition 2.1.1. Let K be a commutative ring. A K-linear category is a cat-
egory M, endowed with a K-module structure on each of the sets of morphisms
HomM(M0, M1). The condition is this:
• For all M0, M1, M2 ∈M the composition function
HomM(M1, M2) × HomM(M0, M1) →HomM(M0, M2)
(φ1, φ0) 7→φ1 ◦φ0
is K-bilinear.
If K = Z, we say that M is a linear category.
As already mentioned in Convention 1.2.4, in our book all linear categories are
K-linear.
Proposition 2.1.2. Let M be a K-linear category.
(1) For every object M ∈M, the set EndM(M) := HomM(M, M), with its given
addition operation, and with the operation of composition, is a central K-
ring.
(2) For every two objects M0, M1 ∈M, the set HomM(M0, M1), with its given
addition operation, and with the operations of composition, is a left module
over the ring EndM(M1), and a right module over the ring EndM(M0).
Furthermore, these left and right actions commute with each other.
Exercise 2.1.3. Prove Proposition 2.1.2.
This result can be reversed:
Example 2.1.4. Let A be a central K-ring. Deﬁne a category M like this: there
is a single object M, and its set of morphisms is HomM(M, M) := A. Composition
in M is the multiplication of A. Then M is a K-linear category.
For a central K-ring A, the opposite ring Aop has the same K-module structure
as A, but the multiplication is reversed.
Exercise 2.1.5. Let A be a nonzero ring.
Let P, Q ∈Mod A be distinct free
A-modules of rank 1.
(1) Prove that there is a ring isomorphism EndMod A(P) ∼= Aop. Is this ring
isomorphism canonical?
(2) Let M be the full subcategory of Mod A on the set of objects {P, Q}. Com-
pare the linear category M to the ring of matrices Mat2(Aop).
