---
doc_id: arxiv-1109.1919v3
doc_title: "COMBINATORIAL DESCENT DATA FOR GERBES AMNON YEKUTIELI"
section_id: sec-003-3-some-remarks
section_title: "Some Remarks"
section_number: 3
pages: 10-12
source_pdf: 1109.1919v3.pdf
source_sha256: 2b634edddf232047
doc_brief: "COMBINATORIAL DESCENT DATA FOR GERBES AMNON YEKUTIELI — We consider descent data in cosimplicial crossed groupoids."
---
To ﬁnish the note, here are a few remarks and clariﬁcations, to help place our
work in context.
Remark 3.1. Cosimplicial crossed groupoids arise naturally in the geometry of
gerbes. This is well-known – see [Gi, Br1, Br2, BGNT1]. Let us quickly indicate
how this occurs. Let G be a sheaf of groups on a topological spaceX, and let
Aut(G) be its sheaf of automorphism groups. There is an obvious sheaf of crossed
groups (i.e. crossed modules)
G =
(
D :G→Aut(G)
)
onX. Consider an open coveringU ={Uk}ofX. The Čech construction gives rise
to a cosimplicial crossed groupG := C(U, G). The setDesc(G) is an approximation
of the set of equivalence classes ofG-gerbes on X (the discrepancy is because we
may have to use reﬁnements and hypercoverings).
If everyG-gerbe totally trivializes on the coveringU (see [Ye1, Deﬁnition 9.16]),
then Desc(G) actually classiﬁesG-gerbes. IfV is another such covering, andV →
U is a reﬁnement, then there is an induced weak equivalence of cosimplicial crossed
groups C(U, G)→C(V, G).
More general gerbes (notG-gerbes as above) can sometimes be classiﬁed by a
sheaf of crossed groupoidsG – see next remark. For the full generality is it necessary
to invoke more complicated combinatorics – see Remark 3.6.
Remark 3.2. Theorem 0.1 is used to provetwisted deformation quantizationin
our paper [Ye1] (see also the survey article [Ye3]). We look at a smooth algebraic
varietyX over a ﬁeldK of characteristic 0. By parameter K-algebra we mean a
complete noetherian local commutative K-algebra R, with maximal ideal m and
residue ﬁeldR/m = K. The main example is R = K[[ℏ]], the algebra of power
series in a variableℏ.
Onthevariety X therearetwoimportantsheavesofDGLiealgebras: thealgebra
Tpoly,Xof poly derivations, and the algebraDpoly,Xof poly diﬀerential operators.
Consider the sheaves of pronilpotent DG Lie algebrasmˆ⊗Tpoly,Xand mˆ⊗Dpoly,X.
The Deligne crossed groupoidconstruction (see [Ge] or [Ye2]) gives rise to sheaves
of crossed groupoidsG := Del
(
mˆ⊗Tpoly,X
)
and H := Del
(
mˆ⊗Dpoly,X
)
.
Now letU be a ﬁnite aﬃne open covering ofX. Consider the cosimplicial crossed
groupoids G := C(U, G) and H := C(U, H). The sets Desc(G) and Desc(H)
classify twisted PoissonR-deformations and twisted associativeR-deformations of
OX, respectively. These twisted deformations are stacky versions of usual defor-
mations (similar to the stacks of algebroids in [Ko, KS]). The fact that twisted
COMBINATORIAL DESCENT DATA 11
R-deformations ofOX totally trivialize on any aﬃne open covering relies on our
paper [Ye4].
There is a diagram of weak equivalences of cosimplicial crossed groupoids
G
Φ ˜G

H
Φ ˜H

˜G
˜Ψ // ˜H
The weak equivalences Φ ˜G : G→˜G and Φ ˜H : H →˜H come from suitable res-
olutions of the sheaves of DG Lie algebrasTpoly,XandDpoly,Xrespectively. The
weak equivalence ˜Ψ : ˜G→˜H comes from the Kontsevich Formality Theorem and
its adaptation to the algebro-geometric setting; see [Ye1, Theorems 10.3 and 10.6].
Due to Theorem 0.1 we obtain a bijection
tw.quant : Desc(G)→Desc(H),
tw.quant := Desc(Φ ˜H)−1◦Desc( ˜Ψ)◦Desc(Φ ˜G).
A reﬁnement argument shows thattw.quant is independent of the resolutions. We
call it thetwisted quantization map.
The twisted quantization maptw.quant does not arise from a reﬁnement or any
similar geometric operation. Indeed, it is conjectured that in some cases (e.g. when
X is a Calabi-Yau surface) the twisted quantization would send a sheaf to a stack,
thus destroying the geometry.
An earlier approach to twisted deformation quantization (in previous versions
of [Ye1]) relied onnonabelian multiplicative integration on surfaces[Ye6]. The new
approach uses Theorem 0.1, and is much shorter. Let us mention however that the
ideas of [Ye6] were recently picked up by [BGNT2], for comparing various nerves
of a 2-groupoid.
Remark 3.3. A crossed groupoid (i.e. crossed module over a groupoid) is the
same as astrict 2-groupoid; see [Ye2, Proposition 5.5]. The homotopy setπ0(G)
and groupsπi(G,x ) are the same in both incarnations. A crossed groupoid is also
the same as a category with inner gauge groups(P, IG, ig) where P is a groupoid –
see [Ye1, Section 5 and Proposition 10.4].
Traditionally papers used the2-groupoid language to discuss descent for gerbes
(cf. [BGNT1]). In [Ye1] we realized that the crossed groupoid language is more
eﬀective: geometric descent data comes naturally in terms of a cosimplicial crossed
groupoid(see[Ye1, Section10]), andalsotheDeligneconstruction(see[Ye2, Section
6]) appears as a crossed groupoid, so it is more natural to talk about the Deligne
crossed groupoid.
Another reason for preferring the crossed groupoid language is that deﬁning
combinatorial descent data, and proving Theorem 2.4, is easier this way.
Remark 3.4.To the best of our knowledge there is no prior proof of Theorem 0.1,
and moreover such a general result was not even conjectured before.
ResultsofsimilarﬂavordoappearintheworkofBreen[Br1,Br2]onclassiﬁcation
of gerbes. Indeed Breen shows that the morphism of crossed groups arising from
a reﬁnement (cf. Remark 3.1) induces a bijection onDesc(−). It is possible that
Theorem 0.1 can be given a shorter proof using Breen’s diagram calculus.
Another earlier result, a special case of our Theorem 0.1, is [BGNT1, Proposition
3.3.1]. However it is too restricted for the purposes of [Ye1].
Assertions in [CH] that are similar to Theorem 0.1 are, to the best of our under-
standing, not actually proved there.
The paper [Pr] by Prezma, which is a follow-up to our own present note, extends
Theorem 0.1 signiﬁcantly (see next remark). The proof given in [Pr] uses methods
12 AMNON YEKUTIELI
from homotopy theory, and is much more sophisticated than our direct calculations.
Nonetheless our proof is somewhat shorter, and is completely self-contained.
Remark 3.5. LetG∈∆ (CrGrpd). The setDesc(G) has a crossed groupoid struc-
ture, in which the gauge transformations are the1-morphisms; soπ0(Desc(G)) =
Desc(G). See [Pr], and also [Br2, Section 5], [Hi] and [BGNT1] for special cases. A
morphism Φ : G→H in ∆ (CrGrpd) induces a morphism
Desc(Φ) : Desc(G)→Desc(H)
in CrGrpd.
Prezma [Pr] proves that ifΦ is a cosimplicial weak equivalence, then the mor-
phism of crossed groupoidsDesc(Φ) is a weak equivalence. This of course implies
Theorem 0.1. The result of Prezma extends Jardine’s corresponding result for (or-
dinary) groupoids [Ja]. Moreover Prezma shows how to extend his equivalence
theorem to higher (n> 2) groupoids.
Remark 3.6. We should emphasize that Theorem 0.1 holds in much greater gen-
erality than stated. First observe that we made no use of the full cosimplicial
structure of the cosimplicial crossed groupoidsG and H – all we needed is that
these are 3-truncated semi-cosimplicial crossed groupoids. Namely that G and H
are functors ∆≤3
inj →CrGrpd, where ∆≤3
inj is the subcategory of ∆ on the object
set{0, 1, 2, 3}, and with only injective functionsα: p→q. Likewise for the weak
equivalence Φ : G→H.
The reason we chose to use the cosimplicial language is convenience. It also ﬁts
nicely with the conventions of [Ye1].
Other papers dealing with descent for gerbes and stacks (cf. [Br1, Br2, DP])
indicate that Theorem 0.1 might be extended further. It is almost clear to us
that the theorem holds for4-truncated pseudo-semi-cosimplicial crossed groupoids,
namely for pseudo-functorsG,H : ∆≤4
inj →CrGrpd. This would correspond to a
Čech construction performed on astack of crossed groupoidson a spaceX.
A more complicated extension would be to replace the 2-category CrGrpd of
crossed groupoids with the 2-category w2Grpd of weak 2-groupoids, i.e. to work
with pseudo-functors ∆≤4
inj→w2Grpd.
It is reasonable to assume that proving such extended results would require
either a bare-hands approach like ours, or else a very sophisticated homotopical
machinery.
