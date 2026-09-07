---
doc_id: arxiv-0801.3233v4
doc_title: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli"
section_id: sec-007-appendix-a-dg-lie-algebras-and-deformations
section_title: "Appendix A. DG Lie Algebras and Deformations"
section_number: null
pages: 9-12
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
doc_brief: "Contemporary Mathematics Twisted Deformation Quantization of Algebraic Varieties (Survey) Amnon Yekutieli — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0."
---
TheﬁrsttimeDG(diﬀerentialgraded)Liealgebraswereusedtostudyproblems
in deformation theory was in the paper [SS] of Schlessinger and Stasheﬀ (1977).
In 1986 Deligne (in a letter to Millson, see [GM]) formulated the idea that “in
characteristic zero, a deformation problem is controlled by a diﬀerential graded
Lie algebra, with quasi-isomorphic diﬀerential graded Lie algebras giving the same
deformation theory”. This idea will be explained in this appendix, for associative
and Poisson deformations of smooth aﬃne algebraic varieties. More details can be
found in the papers [Ye1, Ye5].
10 AMNON YEKUTIELI
Recall that a DG Lie algebra is a gradedK-module g =⨁
i∈Z gi, with a bracket
[−,−]of degree0satisfying the graded version of the Lie algebra identities, together
with a graded derivationd of degree 1 and square 0.
Deﬁnition A.1.A DG Lie algebrag =⨁
i∈Z gi is said to be ofquantum typeif
gi = 0 for alli< −1.
Given a DG Lie algebrag, let us deﬁne a new DG Lie algebra
g[[ℏ]]+ :=
⨁
p∈Z
ℏgp[[ℏ]]⊂
⨁
p∈Z
gp[[ℏ]],
in which ℏ is central.
The Maurer-Cartan equationin g[[ℏ]]+ is
d(ω) + 1
2[ω,ω] = 0
for an element
ω=
∞∑
j=1
ωjℏj∈g1[[ℏ]]+.
The set of solutions of this equation is denoted byMC(g[[ℏ]]+).
Let exp(g0[[ℏ]]+) be the pronilpotent group associated to the pronilpotent Lie
algebra g0[[ℏ]]+. There is an action of the groupexp(g0[[ℏ]]+) on g1[[ℏ]]+, and this
action preserves the subsetMC(g[[ℏ]]+). One deﬁnes
(A.2) MC(g[[ℏ]]+) := MC(g[[ℏ]]+)
exp(g0[[ℏ]]+) ,
the quotient set for this action.
Let us return to our deformation problem, where X is a smooth algebraic
variety overK. Take an aﬃne open setU⊂X, and letC := Γ(U,OX).
One can show that any Poisson (resp. associative) deformation ofC is iso-
morphic toC[[ℏ]] as K[[ℏ]]-algebra (resp. K[[ℏ]]-module) augmented toC. Thus it
suﬃces to understand formal Poisson brackets (resp. star products) onC[[ℏ]].
LetTC denote the module of derivations ofC. Forp≥−1 deﬁne
Tp
poly(C) :=
⋀p+1
C
TC.
SoT−1
poly(C) =C,T 0
poly(C) =TC andT 1
poly(C) =⋀2
CTC. The direct sum
Tpoly(C) :=
⨁
p≥−1
Tp
poly(C)
is a DG Lie algebra, called the algebra ofpoly derivationsofC. The Lie bracket is
the Schouten-Nijenhuis bracket, and the diﬀerential is0.
An element
ω=
∞∑
j=1
ωjℏj∈T1
poly(C)[[ℏ]]+
determines a skew-symmetricK[[ℏ]]-bilinear biderivation ofC[[ℏ]], namely
(A.3) {f,g}:=
∞∑
j=1
ωj(f,g )ℏj
forf,g ∈C. A calculation shows thatωsatisﬁes the Maurer-Cartan equation if and
only if the corresponding biderivation{−,−}satisﬁes the Jacobi identity, i.e. it is a
TWISTED DEFORMATION QUANTIZATION 11
formal Poisson bracket onC[[ℏ]]. Moreover, the action of groupexp
(
T 0
poly(C)[[ℏ]]+{
corresponds to gauge equivalences between formal Poisson brackets. In this sense
Tpoly(C) controls Poisson deformations ofC.
The second DG Lie algebra in this picture is that of thepoly diﬀerential oper-
ators. A functionφ: Cp+1→C is called a poly diﬀerential operator of order≤i
if it is a diﬀerential operator of order≤i in each of its arguments. The set of all
such operators is denoted byDp
poly(C). ThusD−1
poly(C) =C andD0
poly(C) =D(C),
the ring of diﬀerential operators. The direct sum
Dpoly(C) :=
⨁
p≥−1
Dp
poly(C)
is a sub DG Lie algebra of the shifted Hochschild cochain complex (with its Ger-
stenhaber Lie bracket).
A solution ω= ∑∞
j=1ωjℏj of the Maurer-Cartan equation inDpoly(C)[[ℏ]]+
determines a star product onC[[ℏ]], by the formula
(A.4) f ⋆g:=fg +
∞∑
j=1
ωj(f,g )ℏj
forf,g ∈C. Suchastarproductiscalled diﬀerential(asopposedtoanordinarystar
product, for which the coeﬃcientsωj are just K-bilinear; cf. equation (1.1)). The
group exp
(
D0
poly(C)[[ℏ]]+{
is the group of diﬀerential gauge equivalences between
diﬀerential star products. Thusthe DG Lie algebraDpoly(C) controls diﬀerential
star products.
Fortunately we have this result:
Theorem A.5([Ye5]). LetC be a smoothK-algebra.
(1) Any star product⋆onC[[ℏ]] is gauge equivalent to a diﬀerential star prod-
uct ⋆′.
(2) Let⋆and ⋆′be diﬀerential star products onC[[ℏ]], and letg :⋆→⋆′be a
gauge equivalence. Theng is a diﬀerential gauge equivalence.
The proof of Theorem A.5 goes like this: it is well known that star products on
C[[ℏ]] are controlled by the shifted Hochschild cochain complex; this was essentially
shown already in [Ge]. We know that the inclusion of the DG Lie algebraDpoly(C)
into the shifted Hochschild cochain complex is quasi-isomorphism (cf. [Ye3]). This,
together with the Equivalence Theorem (see below), implies part (1) of Theorem
A.5. Part (2) is a direct calculation.
Theupshotisthatthe DG Lie algebraDpoly(C) in fact controls all star products
on C[[ℏ]].
BothTpoly(C) andDpoly(C) are quantum type DG Lie algebras (this is the
reason for the name!).
Geometrically, there are sheaves of DG Lie algebrasTpoly,X andDpoly,X onX,
that are quasi-coherent asOX-modules. For any aﬃne open setU as above we have
Γ(U,Tpoly,X) =Tpoly(C),
and likewise forDpoly.
In order to control global deformations one has to resort to some kind of reso-
lution of these sheaves of DG Lie algebras, such as the mixed resolutions mentioned
in Theorem 4.3.
12 AMNON YEKUTIELI
Remark A.6.The Hochschild cochain complex is not functorial inC at all. On the
other hand the complexDpoly(C)is functorial with respect to étale homomorphisms
C→C′.
Remark A.7. The product⋆in equation (A.4) could fail to be unital. To ensure
that ⋆has 1∈C as unit, we have to takeω∈MC(Dnor
poly(C)[[ℏ]]+). HereDnor
poly(C)
is the algebra ofnormalized poly diﬀerential operators. However, since the inclusion
Dnor
poly(C)→Dpoly(C) is a quasi-isomorphism, the setsMC(−) are the same. For
this reason we can allow ourselves to neglect the distinction betweenDnor
poly(C) and
Dpoly(C) in this survey.
