---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-005-5-combinatorial-descent-data
section_title: "Combinatorial Descent Data"
section_number: 5
pages: 25-28
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
We begin with a quick review of cosimplicial theory. Let∆ denote the simplex
category. The set of objects of∆ is the setN of natural numbers. Givenp,q∈N,
the morphismsα:p→q in ∆ are the order preserving functionsα:{0,...,p}→
{0,...,q}. We denote this set of morphisms by∆ q
p. An element of ∆ q
p may be
thought of as a sequencei = (i0,...,ip) of integers with 0≤i0≤···≤ip≤q.
We call∆ q :={∆ q
p}p∈N the q-dimensional combinatorial simplex, and an element
i∈∆ q
p is ap-dimensional face of∆ q.
Let C be some category. A cosimplicial object in C is a functorC : ∆ →C.
We shall usually writeCp := C(p) ∈Ob(C), and leave the morphisms C(α) :
C(p)→C(q), forα∈∆ q
p, implicit. Thus we shall refer to the cosimplicial object
C as{Cp}p∈N. The category of cosimplicial objects inC, where the morphisms are
natural transformations of functors∆ →C, is denoted by∆ (C).
If C is a category of sets with structure (i.e. there is a faithful functorC→Set),
then an object C ∈Ob(C) has elements c∈C. Let {Cp}p∈N be a cosimplicial
object of C. Given a facei∈∆ q
p and an elementc∈Cp, it will be convenient to
write
(5.1) ci :=C(i)(c)∈Cq.
The picture to keep in mind is of “the elementc pushed to the facei of the simplex
∆ q”. See Figure 2 for an illustration.
We shall be interested in cosimplicial crossed groupoids, i.e. in objects of the
category ∆ (CrGrpd). A cosimplicial crossed groupoid G ={Gp}p∈N has in each
simplicial dimensionp a crossed groupoidGp. The morphismsG(i) :Gp→Gq, for
i∈∆ q
p, are implicit, and we use notation (5.1).
Let us ﬁxp∈N. Then for anyω∈Ob(Gp) there is a group homomorphism (the
feedback) D : Gp
2(ω)→Gp
1(ω). And for every morphismg :ω→ω′in Gp
1 there is
a group isomorphism (the twisting)
AdGp
1 ↷Gp
2
(g) :Gp
2(ω)→Gp
2(ω′).
We shall often use the abbreviated expressionAd(g) to mean both AdGp
1 ↷Gp
2
(g)
and AdGp
1
(g); hopefully that will not cause confusion.
26 AMNON YEKUTIELI
Figure 2. Illustration of a combinatorial descent datum(ω,g,a)
in the cosimplicial crossed groupoidG ={Gp}p∈N.
Deﬁnition 5.2.LetG ={Gp}p∈N be a cosimplicial crossed groupoid. Acombina-
torial descent datumin G is a triple(ω,g,a) of elements of the following sorts:
(0) ω∈Ob(G0).
(1) g∈G1
1(ω(0),ω(1)), whereω(0),ω(1)∈Ob(G1) are the objects corresponding
to the vertices(0) and (1) in ∆ 1.
(2) a∈G2
2(ω(0)), whereω(0)∈Ob(G2)is the object corresponding to the vertex
(0) of ∆ 2.
The conditions are as follows:
(i) (Failure of1-cocycle)
g−1
(0,2)◦g(1,2)◦g(0,1) = D(a)
in the group G2
1(ω(0)). Here ω(i) ∈Ob(G2) and g(i,j) ∈G2
1(ω(i),ω(j))
correspond to the faces(i) and (i,j ) respectively of ∆ 2.
(ii) (Twisted 2-cocycle)
a−1
(0,1,3)◦a(0,2,3)◦a(0,1,2) = Ad(g−1
(0,1))(a(1,2,3))
in the group G3
2(ω(0)). Here ω(i) ∈Ob(G3), g(i,j) ∈G3
1(ω(i),ω(j)) and
a(i,j,k)∈G3
2(ω(i)) correspond to the faces(i), (i,j ) and (i,j,k ) respectively
of ∆ 3.
We denote byDesc(G) the set of all descent data inG.
See Figure 2 for an illustration.
Deﬁnition 5.3.Let (ω,g,a) and (ω′,g′,a′) be combinatorial descent data in the
cosimplicial crossed groupoidG. A gauge transformation(ω,g,a)→(ω′,g′,a′) is a
pair (f,b ) of elements of the following sorts:
(0) f∈G0
1(ω,ω′).
(1) b∈G1
2(ω(0)), whereω(0)∈Ob(G1) is the object corresponding to the vertex
(0) in ∆ 1.
These two conditions must hold:
(i)
g′=f(1)◦g◦D(b)◦f−1
(0)
TWISTED DEFORMATION QUANTIZATION 27
Figure 3. Illustration of a gauge transformation (f,b ) :
(ω,g,a)→(ω′,g′,a′) between descent data.
in the setG1
1(ω′
(0),ω′
(1)).
(ii)
a′= Ad(f(0))
(
b−1
(0,2)◦a◦Ad(g−1
(0,1))(b(1,2))◦b(0,1)
{
in the groupG2
2(ω′
(0)).
This is illustrated in Figure 3.
The gauge transformations form an equivalence relation on the setDesc(G); see
[Ye8, Proposition 1.6]. We call this relationgauge equivalence.
Let Φ : G→H be a morphism of cosimplicial crossed groupoids, i.e. a morphism
in ∆ (CrGrpd). Given a descent datum(ω,g,a)∈Desc(G), the tripleΦ(ω,g,a) :=
(Φ(ω), Φ(g), Φ(a)) is a descent datum in H. The resulting function Desc(Φ) :
Desc(G)→Desc(H) respects the gauge equivalence relations.
Deﬁnition 5.4.For a cosimplicial crossed groupoidG we write
Desc(G) := Desc(G)
gauge equivalence.
For a morphismΦ : G→H of cosimplicial crossed groupoids, we denote by
Desc(Φ) : Desc(G)→Desc(H)
the induced function.
Deﬁnition 5.5.A morphism Φ : G →H of cosimplicial crossed groupoids is
called aweak equivalenceif in every simplicial dimensionp the morphism of crossed
groupoids Φp :Gp→Hp is a weak equivalence (Deﬁnition 1.10).
The next result is proved in the companion paper [Ye8]. An alternative proof
(of a more general statement) can be found in M. Prasma’s paper [Pr].
Theorem 5.6 (Combinatorial Equivalence, [Ye8, Theorem 0.1]). Let Φ : G→H
be a weak equivalence between cosimplicial crossed groupoids. Then the function
Desc(Φ) : Desc(G)→Desc(H)
from Deﬁnition5.4 is bijective.
28 AMNON YEKUTIELI
Remark 5.7. If we view the cosimplicial crossed groupoid as a cosimplicial sim-
plicial set, then the set of descent dataDesc(G) becomes thetotal spaceof G. See
[BGNT2] and [Pr].
We discovered Theorem 5.6 while trying to understand, and possibly improve,
[BGNT1, Proposition 3.3.1] and the ideas in [CH]. The precise relation to [BGNT1,
Proposition 3.3.1] is explained in Remark 8.11. As for [CH]: there seems to be
an implicit assumption there that the nerveN(G) is a Reedy ﬁbrant cosimplicial
simplicial set. This might not be true – see [Pr].
