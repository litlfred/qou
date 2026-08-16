---
doc_id: arxiv-1103.2082v1
doc_title: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St)"
section_id: sec-007-2-ribbon-categories-and-traces
section_title: "Ribbon Categories and Traces"
section_number: 2
pages: 3-5
source_pdf: 1103.2082v1.pdf
source_sha256: 0ac5371486b38eac
doc_brief: "MODIFIED TRACES ON DELIGNE’S CATEGORY Rep(St) — Deligne has deﬁned a category which interpolates among the representations of the various symmetric groups."
---
The authors of [GKP10] deﬁne modiﬁed trace functions for ideals in ribbon categories. In
this section we give a brief overview of this theory but refer the reader to the above paper
for further details and proofs.
2.1. Ribbon Categories. For notation and the general setup of ribbon categories our ref-
erences are [Tur10] and [Kas95]. A tensor categoryC is a category equipped with a covariant
bifunctor
⊗ :C×C→C
called the tensor product, a unit object 1, an associativity constraint, and left and right
unit constraints such that the Triangle and Pentagon Axioms hold (see [Kas95, XI.2]). In
particular, for any V inC, 1⊗V and V⊗ 1 are canonically isomorphic to V .
3
A braiding on a tensor categoryC consists of a family of isomorphisms
{cV,W :V⊗W→W⊗V},
deﬁned for each pair of objects V,W which satisfy the Hexagon Axiom [Kas95, XIII.1 (1.3-
1.4)] as well as the naturality condition expressed in the commutative diagram [Kas95,
(XIII.1.2)]. We say a tensor category is braided if it has a braiding. We call the braiding
symmetric if
cW,V◦cV,W = IdV⊗W
for all V and W inC.
A tensor category C has duality if for each object V inC there exits an object V∗ and
coevaluation and evaluation morphisms 1
coevV : 1→V⊗V∗ and ev V :V∗⊗V→ 1
satisfying relations [Kas95, XIV.2 (2.1)].
A twist in a braided tensor category C with duality is a family
{θV :V→V}
of natural isomorphisms deﬁned for each object V ofC satisfying relations [Kas95, (XIV.3.1-
3.2)]. Let us point out that the existence of twists is equivalent to having functorial isomor-
phisms V
∼=− →V∗∗ for all V inC (cf. [BK01, Section 2.2]).
A ribbon category is a braided tensor category with duality and twists. A fundamental
feature of ribbon categories is the fact that morphisms in the category can be represented
diagrammatically and that isotopic diagrams correspond to equal morphisms. For the sake
of brevity, we do not give the graphical calculus here but encourage the interested reader to
refer to [Kas95].
In a ribbon category it is convenient to also deﬁne the morphisms
coev′
V : 1→V∗⊗V and ev′
V :V⊗V∗→ 1
which are given by
coev′
V = (IdV∗⊗θV )◦cV,V∗◦ coevV and ev′
V = evV◦cV,V∗◦ (θV⊗ IdV∗).
Finally, the ground ring of a ribbon category C is
K = EndC(1).
We assumeK is a ﬁeld, that the category isK-linear, and that the tensor product is bilinear.
Later references to linearity will always be with respect to K. Ultimately the ground ring
will be a ﬁxed ﬁeld F of characteristic zero and the categories in question will be F -linear.
2.2. Ideals inC. There are two closely related notions of an ideal within a ribbon category.
The ﬁrst we discuss is used in [GKP10] and deﬁned via objects. We discuss the second
notion in Section 2.4. Note that here and elsewhere if f andg are morphisms, then we write
fg for the composition f◦g.
Deﬁnition 2.1. We say a full subcategoryI of a ribbon categoryC is an ideal if the following
two conditions are met:
(1) If V is an object of I and W is any object of C, then V⊗W is an object of I.
1In [GKP10] these maps are denoted bV and dV , respectively.
4
(2)I is closed under retracts; that is, if V is an object of I, W an object of C, and if
there exists morphisms f :W→V , g :V →W such that gf = IdW , then W is an
object ofI.
Trivially, ifI consists of just the zero object or I =C, thenI is an ideal of the category.
We say an idealI is a proper ideal if it contains a nonzero object and is not all of C.
