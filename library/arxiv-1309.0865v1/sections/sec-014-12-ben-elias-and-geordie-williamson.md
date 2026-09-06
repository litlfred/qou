---
doc_id: arxiv-1309.0865v1
doc_title: "SOERGEL CALCULUS"
section_id: sec-014-12-ben-elias-and-geordie-williamson
section_title: "BEN ELIAS AND GEORDIE WILLIAMSON"
section_number: 12
pages: 12-13
source_pdf: 1309.0865v1.pdf
source_sha256: e610a4fa938a7cc9
doc_brief: "SOERGEL CALCULUS — The monoidal category of Soergel bimodules is an incarnati on of the Hecke category , a fundamental object in representation the ory ."
---
morphism can be thought of as a kind of rhombus (see section 6)
w
LLx,e
x
where the upper expression is always reduced.
Now let x and y be ﬁxed expressions. Following Libedinsky , we introduce th e
double leaves morphism
LLw,e,f
def=
y
LLy,f
w
LLx,e
x
where LLy,f denotes the vertical ﬂip of a light leaf morphism, and e (resp. f) is
a subexpression of x (resp. y) which expresses w. Hence LLw,e,f is a morphism
Bx →By. Consider the set
LLx,y
def=
⋃
w∈W
{LLw,e,f | e ∈M(x,w ), f ∈M(y,w )}
where,M(x,w ) denotes the set of subexpressions of x expressingw. Our main theo-
rem is then the following:
Theorem 1.1. LLx,y is anR-basis for HomD(Bx,B y).
The proof of this theorem is pure diagrammatic algebra. Unfo rtunately it is quite
convoluted. It has the following consequences:
(1) Under very general assumptions one has a functor D → SBim (we deﬁned
this functor earlier under the assumption that 2 was invertible). If the cate-
gory of Soergel bimodules is well-behaved (i.e. if the Soerg el Categoriﬁcation
Theorem holds) then this functor is an equivalence of monoid al categories.
(2) Soergel bimodules play an important role in modular repr esentation theory
[Soe00, Fie11]. Here it is desirable to have versions over ﬁe lds of positive
characteristic and local rings. One can deﬁne the diagramma tic category over
very general rings. For example, if W is crystallographic then one can deﬁne
the diagrammatic category over Z. Over a complete local ring the indecom-
posable objects in the diagrammatic category are parametri zed (up to shift)
byW , and the split Grothendieck group always categoriﬁes the He cke alge-
bra. This gives a new proof of Soergel’s Categoriﬁcation The orem whenever
Soergel bimodules are well-behaved, and suggests that the diagrammatic cat-
egory is the correct replacement when they are not.
SOERGEL CALCULUS 13
(3) The category of Bott-Samelson bimodules is a cellular ca tegory , with cells
parametrized by w ∈ W , and with cellular basis given by a ﬁxed choice of
light leaves morphisms. In particular, the endomorphism ri ng of any Bott-
Samelson bimodule is a cellular algebra.
1.6. Organization of the paper. This paper contains three parts.
Part 1: The ﬁrst two sections give background on the Hecke algebra an d Soergel
bimodules.
Section 2: We recall the Hecke algebra, Kazhdan-Lusztig basis and Deod -
har’s defect formula.
Section 3: We deﬁne standard and Soergel bimodules, state Soergel’s ca te-
goriﬁcation theorem and discuss realizations and localiza tion.
Part 2: In the next two sections, we deﬁne the diagrammatic categori es.
Section 4: We deﬁne the diagrammatic presentation of standard modules .
Section 5: We recall results of [Elib] and deﬁne the diagrammatic categ ory
of Soergel bimodules.
Part 3: In the last two sections we study the diagrammatic categorie s and prove
the equivalence to Soergel bimodules.
Section 6: We deﬁne Libedinsky’s light leaves and double leaves morphi sms
in the diagrammatic setting. We state the theorem that doubl e leaves
span, and deduce the main theorems of the paper.
Section 7: We prove that double leaves span.
