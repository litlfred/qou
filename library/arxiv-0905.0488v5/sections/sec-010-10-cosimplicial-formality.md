---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-010-10-cosimplicial-formality
section_title: "Cosimplicial Formality"
section_number: 10
pages: 42-45
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
In this section we prove Theorem 10.6. We work in Setup 9.3.
Recall the sheaves of DG Lie algebrasTpoly,X andDpoly,X from Section 3. The
Lie brackets are notOX-linear (they are diﬀerential operators), but forgetting
them, bothTpoly,X andDpoly,X are bounded below complexes of quasi-coherent
OX-modules.
The antisymmetrization homomorphism (also called the HKR map)
(10.1) Υ 1 :Tp
poly,X→Dp
poly,X
is deﬁned as follows. Forp≥0 and for local sectionsξi∈T0
poly,X and ci∈OX, we
let
Υ 1(ξ1∧···∧ξp+1)(c1,...,cp+1) := 1
(p+1)!
∑
σ
sign(σ)ξσ(1)(c1)···ξσ(p+1)(cp+1).
Thesummationisoverpermutations σoftheset {1,...,p +1}. Forp =−1welet Υ 1
be the identity map ofOX. According to [Ye2, Corollary 4.12] the homomorphism
Υ 1 :Tpoly,X →Dpoly,X is a quasi-isomorphism of sheaves ofOX-modules. Note
that Υ 1 does not respect the Lie brackets; butH(Υ 1) :Tpoly,X→H(Dpoly,X) is an
isomorphism of sheaves of graded Lie algebras.
LetG andH be sheaves of DG Lie algebras onX. We denote by∏iG thei-fold
cartesian product of the sheafG. An L∞morphism Ψ : G → His a sequence
Ψ = {Ψi}i≥1 of K-multilinear sheaf morphismsΨi :∏iG→H, such that for any
open setU the sequence{Γ(U, Ψi)}i≥1 is anL∞morphism Γ(U,G)→Γ(U,H). We
say that Ψ is an L∞quasi-isomorphism if Ψ 1 :G→His a quasi-isomorphism of
sheaves of K-modules. See Section 8 for a reminder onL∞morphisms.
LetU ﬁnite aﬃne open covering ofX. Recall the mixed resolutionmix :M→
MixU(M) of any quasi-coherentOX-moduleM from [Ye1, Section 6]. This is a
functorial quasi-isomorphism, which is a “mix” of the commutative Čech resolution
relativetothecovering U, andthejetresolution(withitsGrothendieckconnection).
The complex MixU(M) is acyclic for the functorΓ(V,−) for any aﬃne open set
V ⊂X. Hence the homomorphism of cosimplicialK-modules
C(U, mix) : C(U,M)→C(U, MixU(M))
(cf. (9.1)) is a cosimplicial quasi-isomorphism (i.e. it is a quasi-isomorphism in
each simplicial dimension). Taking the sheaves Tpoly,X andDpoly,X, we obtain
quasi-isomorphisms of sheaves of DG Lie algebrasTpoly,X →MixU(Tpoly,X) and
Dpoly,X→MixU(Dpoly,X). See [Ye1, Proposition 6.3].
Let g : X′→X be a morphism of varieties,M (resp.M′) a quasi-coherent
OX-module (resp.OX′-module), φ:M→g∗(M′) anOX-linear map, U (resp.
U′) a ﬁnite aﬃne open covering ofX (resp. X′), andρ:U′→U a morphism of
coverings extendingg. The construction of mixed resolutions (see [Ye1, Section 6]
or [Ye3, Section 4]) shows that there is an induced sheaf homomorphism
Mixρ(φ) : MixU(M)→g∗(MixU′(M′))
on X. And of course globally there is a homomorphism of cosimplicialK-modules
C(ρ,φ) : C(U,M)→C(U′,M′).
TWISTED DEFORMATION QUANTIZATION 43
Now assumeg : X′→X is an étale morphism. LetG denote eitherTpoly or
Dpoly, so thatGX is eitherTpoly,X orDpoly,X. As we already saw in Section 9, there
is a homomorphism of sheaves of DG Lie algebrasg∗:GX→g∗(GX′) on X. Then
there is an induced homomorphism of sheaves of DG Lie algebras
Mixρ(g∗) : MixU(GX)→g∗(MixU′(GX′))
on X. Globally there is a commutative diagram of homomorphism of cosimplicial
DG Lie algebras
(10.2) C(U,GX)
C(ρ,g∗) //
C(U,mix)

C(U′,GX′)
C(U′,mix)

C
(
U, MixU(GX)
{ C(ρ,Mixρ(g∗)) // C
(
U′, MixU′(GX′)
{
where the vertical arrows are cosimplicial quasi-isomorphisms. Ifg : X′→X is
an isomorphism (e.g.X′= X and U′→U is a reﬁnement), then the horizontal
arrows are also cosimplicial quasi-isomorphisms.
Letn be the dimension ofX. Anétale coordinate systemon an open setU⊂X
is an étale morphisms :U→An
K. SinceX is smooth, it is possible to ﬁnd a ﬁnite
aﬃne open coveringU ={Uk}k∈K, with an étale coordinate systemsk :Uk→An
K
for eachk. Let us writes :={sk}k∈K. We refer to(U,s) succinctly as acovering
with étale coordinates.
Suppose g : X →X′is an étale morphism of varieties, and we are given a
covering with étale coordinates (U′,s′) of X′, where the indexing set isK′. A
morphism of coverings with coordinates extendingg is a function ρ: K′→K,
such thatg(U′
k′)⊂Uρ(k′) and sρ(k′)◦g = s′
k′for everyk′∈K′. We refer to this
morphism byρ: (U′,s′)→(U,s).
The next result is a slight improvement of [Ye1, Theorem 0.2]. A similar result
is [VdB, Theorem 1.1].
Theorem 10.3 (Sheaf Formality). Let X be a smooth algebraic variety overK,
and assumeR⊂K. Let (U,s) be a ﬁnite aﬃne open covering with étale coordinates
of X. Then:
(1) There is anL∞quasi-isomorphism
Ψ s ={Ψ s;i}i≥1 : MixU(Tpoly,X)→MixU(Dpoly,X)
between sheaves of DG Lie algebras onX.
(2) The diagram of isomorphisms of sheaves of graded Lie algebras
Tpoly,X
H(Υ 1) //
H(mix)

H(Dpoly,X)
H(mix)

H(MixU(Tpoly,X))
H(Ψ s;1) // H(MixU(Dpoly,X))
on X is commutative.
(3) Suppose g : X→X′is an étale morphism of varieties,(U′,s′) is a ﬁnite
aﬃne open covering with étale coordinates ofX′, andρ: (U′,s′)→(U,s)
is a morphism of coverings with coordinates extendingg. Then the diagram
of L∞morphisms onX
MixU(Tpoly,X)
Ψ s //
Mixρ(g∗)

MixU(Dpoly,X)
Mixρ(g∗)

g∗(MixU′(Tpoly,X′))
g∗(Ψ s′) //g∗(MixU′(Dpoly,X′))
44 AMNON YEKUTIELI
is commutative.
Proof. Part (1) is the content of [Ye1, Theorem 0.2], which is repeated in greater
detail (and with a correct proof) as [Ye1, Erratum, Theorem 1.2]. Part (3) is
a direct consequence of the construction of theL∞quasi-isomorphism Ψ s in the
proof of [Ye1, Erratum, Theorem 1.2].
The idea for the proof of part (2) was communicated to us by M. Van den Bergh.
LetM be a bounded below complex of quasi-coherentOX-modules. Forp≥0 let
Gp(MixU(M)) :=
⨁
i≥p
Mixi
U(M).
This gives a decreasing ﬁltrationG = {Gp}p≥0 of MixU(M) by subcomplexes.
Note that grp
G(MixU(M)) = Mixp
U(M)[−p] as complexes. The ﬁltrationG gives
rise to a convergent spectral sequenceEp,q
r (M)⇒Hp+q(MixU(M)), and its ﬁrst
page is
Ep,q
1 (M) = Hp+q(
grp
G(MixU(M))
{∼= Mixp
U(Hq(M)).
The diﬀerentialEp,q
1 (M)→Ep+1,q
1 (M) is the diﬀerential of the mixed resolution.
Note that all these objects are quasi-coherent sheaves onX. Because of the quasi-
isomorphism mix : Hq(M)→MixU(Hq(M)) we have
(10.4) Ep,q
2 (M)∼=
{
Hq(M) if p = 0
0 if p⁄= 0.
We see that the spectral sequence collapses, andEp,q
∞(M) =Ep,q
2 (M). In particular
the induced ﬁltration on the limitHp+q(MixU(M)) of the spectral sequence has
only one nonzero jump (at levelG0).
According to [Ye1, Erratum, Theorem 1.2] the homomorphism of complexes
Ψ s;1 : MixU(Tpoly,X)→MixU(Dpoly,X)
respects the ﬁltrationsG, and for everyp there is equality of homomorphisms of
complexes
(10.5) grp
G(Ψ s;1)[p] = Mixp
U(Υ 1) : Mixp
U(Tpoly,X)→Mixp
U(Dpoly,X).
Moreover, by [Ye3, Theorem 4.17],Mixp
U(Υ 1) is a quasi-isomorphism.
Since Ψ s;1 respects the ﬁltrations, there is an induced map of spectral sequences
Ep,q
r (Ψ) : Ep,q
r (T )→Ep,q
r (D), where we abbreviateT :=Tpoly,X etc. From (10.5)
we see that there is an isomorphism in the ﬁrst pages of the spectral sequences
Ep,q
1 (Ψ) : Mixp
U(Tq
poly,X)∼=Ep,q
1 (T )→Ep,q
1 (D)∼= Mixp
U(Hq(Dpoly,X)).
Since the diﬀerentials are the same, it follows thatEp,q
2 (Ψ) : Ep,q
2 (T )→Ep,q
2 (D) is
an isomorphism.
Finally let’s examine the diagram of isomorphisms
Tq
poly,X
Hq(Υ 1) //
α

Hq(Dpoly,X)
α

E0,q
2 (T )
E0,q
2 (Ψ) //
β

E0,q
2 (D)
β

Hq(MixU(Tpoly,X))
Hq(Ψ s;1) // Hq(MixU(Dpoly,X)) .
The arrowsαcome from (10.4); and the top square commutes because of (10.5) with
p = 0. The arrowsβcome from the collapse of the spectral sequence, and for this
reason the bottom square is commutative. So the whole diagram is commutative.
□
TWISTED DEFORMATION QUANTIZATION 45
Theorem 10.6 (Cosimplicial Formality). In the situation of Theorem10.3 there
is a diagram
C(U,Tpoly,X)
C(U,mix)

C(U,Dnor
poly,X)
C(U,mix)

C
(
U, MixU(Tpoly,X)
{ C(U,Ψ s) // C
(
U, MixU(Dpoly,X)
{
,
where the objects are cosimplicial quantum type DG Lie algebras, the vertical arrows
are cosimplicial DG Lie quasi-isomorphisms, and the arrowΨ s is a cosimplicialL∞
quasi-isomorphism.
This diagram is functorial with respect to étale morphismsg : X′→X and
morphisms of coveringsρ: (U′,s′)→(U,s) extending g, as in diagram(10.2).
Proof. The diagram is obtained by applying the Čech cosimplicial construction
C(U,−) to theL∞quasi-isomorphism Ψ s in Theorem 10.3(1), to the mixed resolu-
tionsTpoly,X→MixU(Tpoly,X) andDpoly,X→MixU(Dpoly,X), and to the inclusion
Dnor
poly,X→Dpoly,X.
Functoriality is guaranteed by Theorem 10.3(3), and by the étale functoriality
ofTpoly,X,Dpoly,X andDnor
poly,X from [Ye2, Proposition 4.6]. □
