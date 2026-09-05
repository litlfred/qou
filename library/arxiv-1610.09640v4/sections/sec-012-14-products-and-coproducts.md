---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-012-14-products-and-coproducts
section_title: "Products and Coproducts"
section_number: 1.4
pages: 27-28
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
of C indexed by a (small) setI, we mean a functionI→Ob(C),i↦→Ci. We usually
denote this collection using the curly brackets notation:{Ci}i∈I.
Given a collection{Ci}i∈I of objects of C, its product is a pair (C,{pi}i∈I)
consisting of an objectC∈C, and a collection{pi}i∈I of morphismspi :C→Ci,
called projections. The pair (C,{pi}i∈I) must have this universal property: given
an objectD and morphismsfi : D→Ci, there is a unique morphismf : D→C
s.t. fi = pi◦f. Of course if a product(C,{pi}i∈I) exists, then it is unique up to
a unique isomorphism; and we usually write∏
i∈ICi := C, leaving the projection
morphisms implicit.
27
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Example 1.4.1. In Set and ModA all products exist, and they are the usual
cartesian products.
For a collection{Ci}i∈I of objects of C, its coproduct is a pair (C,{ei}i∈I),
consisting of an objectC and a collection{ei}i∈I of morphismsei :Ci→C, called
embeddings. The pair (C,{ei}i∈I) must have this universal property: given an
object D and morphisms fi : Ci→D, there is a unique morphismf : C→D
s.t. fi =f◦ei. If a coproduct(C,{ei}i∈I) exists, then it is unique up to a unique
isomorphism; and we write∐
i∈ICi :=C, leaving the embeddings implicit.
Example1.4.2. In Setthecoproductisthedisjointunion. In ModAthecoproduct
is the direct sum.
Product and coproducts are very degenerate cases oflimits and colimits respec-
tively. In this book we will not need to use limits and colimits in their most general
form. All we shall need is inverse limits and direct limits indexed byN; and these
will be recalled in Subsection 1.8 below.
We do need to talk aboutﬁbered products. Let C be some category. Recall that
a commutative diagram
(1.4.3) E
g1

g2 //D2
f2

D1
f1 //C
in C is called cartesian if for every objectE′∈C, with morphismsg′
1 : E′→D1
and g′
2 : E′→D2 that satisfyf1◦g′
1 = f2◦g′
2, there exists a unique morphism
h :E′→E such thatg′
i =gi◦h. See commutative diagram below.
E′
g′
1

g′
2
  h
  
E
g1

g2 //D2
f2

D1
f1 //C
A cartesian diagram is also called apullback diagram, and the objectE is called
the ﬁbered productof D1 and D2 over C, with notation D1×C D2 := E. This
notation leaves the morphisms implicit. Of course if a ﬁbered product exists, than
it is unique up to a unique isomorphism that commutes with the given arrows.
There is a dual notion:ﬁbered coproduct. The input is morphismsC→D1 and
C→D2 in C, and the ﬁbered coproductD1⊔CD1 in C is just the ﬁbered product
in the opposite categoryCop.
