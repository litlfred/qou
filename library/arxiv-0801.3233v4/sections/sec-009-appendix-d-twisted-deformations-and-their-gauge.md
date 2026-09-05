---
doc_id: arxiv-0801.3233v4
doc_title: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli"
section_id: sec-009-appendix-d-twisted-deformations-and-their-gauge
section_title: "Appendix D. Twisted Deformations and their Gauge Gerbes"
section_number: null
pages: 15-18
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
doc_brief: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0."
---
This section summarizes the main concepts of the paper [Ye5].
Recall that agroupoid G is a category in which all morphisms are invertible.
We denote byG(i,j ) the set of arrows from the objecti to the objectj. Note that
G(i,i ) is a group. Any elementg∈G(i,j ) deﬁnes a group isomorphism
Ad(g) : G(i,i )
≃
−→G(j,j ),
namely Ad(g)(h) :=g◦h◦g−1.
A stack of groupoidsG on X is the geometrization of the notion of groupoid,
in the same way that a sheaf of groups is the geometrization of the notion of a
16 AMNON YEKUTIELI
group. Thus for any open setU ⊂X there is a groupoid G(U). And there are
restriction functors G(U)→G(V ) for any inclusionV ⊂U. These satisfy a rather
complicated list of conditions. In particular, given any open setU⊂X and any
object i∈Ob G(U), there is a sheaf of groupsG(i,i ) on U. For details see [Ye6,
Sections 1-2], or [Gi, BM, KS1].
A stack of groupoids G is called agerbe if it is locally nonempty and locally
connected.
Deﬁnition D.1.LetX be a smooth algebraic variety overK. Atwisted associative
(resp. Poisson) deformation A ofOX is the following data:
(1) A gerbe G on X, called thegauge gerbeof A.
(2) For any open setU⊂X and i∈Ob G(U), an associative (resp. Poisson)
deformationAi ofOUi.
The conditions are:
(a) For anyi∈Ob G(U), the sheaf of groupsG(i,i ) coincides with IG(Ai),
the sheaf of inner gauge transformations of the deformationAi.
(b) For anyi∈Ob G(U), anyj∈Ob G(V ), anyW ⊂U∩V and anyg∈
G(W )(i,j ), the isomorphism of sheaves of groups
Ad(g) :G(i,i )|W
≃
−→G(j,j )|W
is induced from a (necessarily unique) gauge equivalence
Ai|W
≃
−→Aj|W.
Theorem D.2([Ye6]). Deﬁnitions5.1 and D.1 are equivalent.
The proof relies on the fact that the gauge gerbeG is pronilpotent, and its
abelian slices are coherent OX-modules. Hence for any aﬃne open set U the
groupoid G(U) is nonempty and connected.
Finally let us say a few words on the proof of Theorem 6.1 in [Ye5] 1.
Fix an aﬃne open coveringU ={U0,...,Um}ofX, such that for eachi there
is an étale morphismUi→An
K. Given a sheafG of DG Lie algebras onX, the
Čech construction gives a cosimplicial DG Lie algebraC(U,G) ={Cp(U,G)}p∈N.
Thus from Theorem 4.3 we deduce that there is a diagram
(D.3) C(U,Tpoly,X)

C(U,Dpoly,X)

C(U, MixU(Tpoly,X))
C(U,Ψ σ) // C(U, MixU(Dpoly,X))
in which the objects are cosimplicial DG Lie algebras, the vertical arrows are cosim-
plicial DG Lie algebra homomorphisms, and the horizontal arrow is a cosimplicial
L∞morphism. Moreover, in each cosimplicial dimensionp the diagram
Cp(U,Tpoly,X)

Cp(U,Dpoly,X)

Cp(U, MixU(Tpoly,X))
Cp(U,Ψ σ) // Cp(U, MixU(Dpoly,X))
has objects that are quantum type DG Lie algebras, the vertical arrows are DG Lie
algebra quasi-isomorphisms, and the horizontal arrow is anL∞quasi-isomorphism.
1This is the proof in the new version of [Y e5], still in preparation as of July 2011.
TWISTED DEFORMATION QUANTIZATION 17
NowtakeanyquantumtypeDGLiealgebra g. Toitweassociate, inafunctorial
way, theDeligne 2-groupoid Del(g[[ℏ]]+), as in [Ge]. If we are given a cosimplicial
quantum type DG Lie algebrag ={gp}p∈N, then there is a cosimplicial2-groupoid
Del(g[[ℏ]]+) :=
{
Del(gp[[ℏ]]+)
}
p∈N.
Next letG ={Gp}p∈N be any cosimplicial2-groupoid. To it we associate the set
CDD(G) of combinatorial descent data, and the quotient set by gauge equivalences
CDD(G). The setsCDD(G) and CDD(G) depend functorially onG.
SoforacosimplicialquantumtypeDGLiealgebra g ={gp}p∈N wecanassociate
the set
LDD(g[[ℏ]]+) := CDD
(
Del(g[[ℏ]]+)
{
of Lie descent data2, and its quotient set
LDD(g[[ℏ]]+) := CDD
(
Del(g[[ℏ]]+)
{
.
See [BGNT, Section 3.2], whereLDD(g[[ℏ]]+) is called “descent data for Deligne
2-groupoids”.
We have the following theorem, extending [BGNT, Proposition 3.3.1].
Theorem D.4([Ye5]). Let g and h be cosimplicial quantum type DG Lie algebras,
and letΦ : g→h be a cosimplicialL∞quasi-isomorphism. Then there is a bijection
LDD(Φ) : LDD(g[[ℏ]]+)
≃
−→LDD(h[[ℏ]]+),
depending functorially onΦ, with an explicit formula.
Applying this theorem to the diagram (D.3) we obtain a canonical diagram of
bijections of sets
LDD
(
C(U,Tpoly,X)[[ℏ]]+{

tw.quant //_ _ _ _ _ _ _ _LDD
(
C(U,Dpoly,X)[[ℏ]]+{

LDD
(
C(U, MixU(Tpoly,X))[[ℏ]]+{ // LDD
(
C(U, MixU(Dpoly,X))[[ℏ]]+{
.
Theorem D.2 implies that twisted Poisson deformations ofOX, modulo twisted
gauge equivalence, correspond bijectively to elements of
LDD
(
C(U,Tpoly,X)[[ℏ]]+{
.
Likewise, twisted associative deformations, modulo twisted gauge equivalence, cor-
respond bijectively to elements of
LDD
(
C(U,Dpoly,X)[[ℏ]]+{
.
The resulting bijection
tw.quant :{twisted Poisson deformations ofOX}
twisted gauge equivalence
≃
−→{twisted associative deformations ofOX}
twisted gauge equivalence
is canonical (independent ofU andσ).
2In the version of [Y e5] dated August 2009, this is called “additive descent data”, and denoted
by ADD(g[[ℏ]]+).
18 AMNON YEKUTIELI
