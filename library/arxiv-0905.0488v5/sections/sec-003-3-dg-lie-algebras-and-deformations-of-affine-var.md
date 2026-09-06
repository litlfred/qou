---
doc_id: arxiv-0905.0488v5
doc_title: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI"
section_id: sec-003-3-dg-lie-algebras-and-deformations-of-affine-var
section_title: "DG Lie Algebras and Deformations of Affine Varieties"
section_number: 3
pages: 19-21
source_pdf: 0905.0488v5.pdf
source_sha256: fcf8dee7cd3849b9
doc_brief: "TWISTED DEFORMATION QUANTIZATION OF ALGEBRAIC VARIETIES AMNON YEKUTIELI — Let X be a smooth algebraic variety over a ﬁeldK containing the real numbers."
---
We now recall some facts on DG Lie algebras from [Ye7, Ye9].
Deﬁnition 3.1. (1) A DG Lie algebrag =⨁
i∈Z gi is said to be ofquantum
type if gi = 0 for i< −1.
(2) A quasi quantum type DG Lie algebrais a DG Lie algebra˜g that admits a
DG Lie quasi-isomorphism˜g→g to some quantum type DG Lie algebrag.
Fix a quasi quantum type DG Lie K-algebra g, and a parameter K-algebra
(R, m). There is an induced LieR-algebra mˆ⊗g = ⨁
i mˆ⊗gi. The Lie bracket
is [−,−] and the diﬀerential isd. A solution ω∈mˆ⊗g1 of the Maurer-Cartan
equation d(ω) + 1
2[ω,ω] = 0 is called anMC element, and the set of such elements
isdenotedby MC(mˆ⊗g). Thegroup Exp(mˆ⊗g0)iscalledthe gauge group. Forγ∈
mˆ⊗g0 there is an aﬃne actionaf(γ) on theR-module mˆ⊗g1, namely af(γ)(ω) :=
[γ,ω]−d(γ). So for g := exp(γ)∈Exp(mˆ⊗g0) there is an aﬃne automorphism
Af(g) := exp(af(γ)) of mˆ⊗g1. It is known thatAf(g) preserves the setMC(mˆ⊗g).
See [GM], [CKTB], [Ye1, Section 3] or [Ye7, Section 1] for details.
Givenω∈MC(mˆ⊗g) there is a square zero derivationdω:= d+ad(ω) of degree
1 on mˆ⊗g, and a bracket[α1,α2]ω:= [dω(α1),α2] forα1,α2∈mˆ⊗g−1 (that’s not
a Lie bracket in general). Deﬁne theR-module
(3.2) aω:= Coker(dω: mˆ⊗g−2→mˆ⊗g−1).
By [Ye7, Proposition 6.6],aωis anR-linear Lie algebra, with bracket induced by
[−,−]ω. And by [Ye7, Proposition 6.7], aωis an m-adically complete R-module
(this is where we needg to be quasi quantum type!). Soaωis a pronilpotent Lie
algebra, and there is an associated pronilpotent groupNω:= Exp(aω).
The R-linear function dω: aω→mˆ⊗g0 is a Lie algebra homomorphism, so it
induces a group homomorphism
(3.3) Dω:Nω→Exp(mˆ⊗g0) , Dω:= exp(dω).
A short calculation shows thataf(dω(α))(ω) = 0 for anyα∈mˆ⊗g−1. The ex-
ponential of this formula is Af(Dω(a))(ω) = ωfor any a ∈Nω. We see that
Dω(a) ∈Exp(mˆ⊗g0)(ω), where the latter is the stabilizer of ωin the group
Exp(mˆ⊗g0).
20 AMNON YEKUTIELI
Now takeg∈Exp(mˆ⊗g0), and letω′:= Af(g)(ω)∈MC(mˆ⊗g). According to
[Ye7, Corollary 6.9] there is a group isomorphism
(3.4) Ad(g) :Nω
≃
− →Nω′,
which is functorial ing, and the diagram
Nω
Ad(g)

Dω // Exp(mˆ⊗g0)
Ad(g)

Nω′
Dω′
// Exp(mˆ⊗g0)
is commutative. By deﬁnition of the bracket[−,−]ω, the adjoint action in the Lie
algebra aωis adaω(α1)(α2) = ad(dω(α1))(α2); hence, by exponentiating this equa-
tion, we see that conjugation in the groupNωis AdNω(a1)(a2) = Ad(Dω(a1))(a2)
for ai∈Nω.
Crossed groupoids were introduced in Deﬁnition 1.2. The considerations above
justify the next deﬁnition.
Deﬁnition 3.5.Let g be a quasi quantum type DG Lie algebra, and let(R, m)
be a parameter algebra, both over the ﬁeldK. The Deligne crossed groupoidis the
crossed groupoid Del(g,R ) with these components:
•The groupoid Del1(g,R ) is the transformation groupoid associated to the
action Af of the group Exp(mˆ⊗g0) on the set MC(mˆ⊗g). (This is the
usual Deligne groupoid ofmˆ⊗g.)
•The groupoidDel2(g,R ) is the totally disconnected groupoid with set of ob-
jects MC(mˆ⊗g). Forω∈MC(mˆ⊗g)its automorphism group inDel2(g,R )
isNω= Exp(aω), whereaωis the pronilpotent Lie algebra in formula (3.2).
•The twisting AdDel1↷Del2(g), for g ∈Exp(mˆ⊗g0), is the group isomor-
phism Ad(g) in formula (3.4).
•The feedback D is the group homomorphism in formula (3.3).
It is obvious from the construction that the crossed groupoidDel(g,R ) is func-
torial in both g and R. When g is a quantum type DG Lie algebra thenaω=
(mˆ⊗g−1)ωof course. If g is of quantum type andR is artinian, thenDel(g,R ) is
precisely the 2-groupoid introduced by Deligne in [De]; see also [Ge1].
LetX be a smooth algebraic variety overK. There are two important sheaves of
DG Lie algebras onX: the sheafTpoly,X of polyderivations, and the sheafDpoly,X
of polydiﬀerential operators. Within Dpoly,X there is the subalgebraDnor
poly,X of
normalized polydiﬀerential operators. The sheavesTpoly,X,Dpoly,X andDnor
poly,X are
quasi-coherent gradedOX-modules, and the inclusionDnor
poly,X→Dpoly,X is a quasi-
isomorphism. Full details on these DG Lie algebras can be found in [Ye1, Ye2]. For
any open set U ⊂X we get quantum type DG Lie algebras Γ(U,Dnor
poly,X) and
Γ(U,Tpoly,X), so Deligne crossed groupoids exist.
Here is how the DG Lie algebrasTpoly,X andDnor
poly,X control deformations of
OX.
Theorem 3.6 (Geometrization, [Ye9, Theorem 0.1]). Let K be a ﬁeld of charac-
teristic 0, X a smooth algebraic variety overK, R a parameter algebra overK, and
U an aﬃne open set inX. There are equivalences of crossed groupoids
geo : Del
(
Γ(U,Dnor
poly,X),R
{
→AssDef(R,OU)
and
geo : Del
(
Γ(U,Tpoly,X),R
{
→PoisDef(R,OU)
which we callgeometrization. The equivalencesgeo commute with homomorphisms
R→R′of parameter algebras, and with inclusions of aﬃne open setsU′→U.
TWISTED DEFORMATION QUANTIZATION 21
The dependence ofAssDef(R,OU) and PoisDef(R,OU) on R and U is shown in
Proposition 2.15.
Remark 3.7. Suppose R = K[[ℏ]]. In our earlier paper [Ye1] we referred to
an associative R-deformation ofOX as a “deformation quantization ofOX”. In
retrospect this name seems inappropriate, and hence the new name used here.
Another, more substantial, change is that in [Ye1, Deﬁnition 1.6] we required
that the associative deformationA shall be endowed with a diﬀerential structure.
This turns out to be redundant – indeed, Theorem 3.6 implies that any associative
R-deformationA ofOX admits a diﬀerential structure. Moreover, any two such
diﬀerential structures are equivalent.
Remark 3.8. In [KS2] Kashiwara and Schapira consider associativeC[[ℏ]]-defor-
mationsA ofOX, for a complex manifoldX. Their deﬁnition is very similar to our
Deﬁnition 2.7 (forR = C[[ℏ]]), except that they do not require an augmentation
A→OX. [KS2, Proposition 2.2.3] is very similar to the fullness of the functor
geo on 1-morphisms (in the associative case of Theorem 3.6 above). However it is
not known whethergeo is essentially surjective on objects in the complex analytic
setting – this is [KS2, Remark 2.2.7].
