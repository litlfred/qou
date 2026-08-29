---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-003-2-sheafification-functors
section_title: "Sheafification functors."
section_number: 2
pages: 9-16
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — W e introduce “sheaﬁﬁcation” functors from categories of (l ax monoidal) linear functors to categories of quasi-coherent sheaves"
---
In this section we deﬁne and describe particular functors th at generalize sheaﬁﬁcation functors
for aﬃne schemes or projective schemes. The idea is to interp ret the category of modules or
graded modules respectively as a category of R-linear functors. More precisely:
Deﬁnition 2.1. Given a ﬁbered category X over a ring R, an R-algebraA and a subcategory D
of QCoh X we deﬁne L R(D,A ) as the category of contravariantR-linear functors Γ : D − →ModA
and natural transformations as arrows. We deﬁne a functor Ω ∗ : QCohA X − → LR(D,A ) by
Ω F
− = HomX (−, F ) : D − →ModA
The functor Ω ∗ is called the Yoneda functor associated with D. A left adjoint of Ω ∗ is called a
sheaﬁﬁcation functor associated with D. If F ∈ QCohA X we will call Ω F the Yoneda functor
associated with F .
Example 2.2. The analogy with the sheaﬁﬁcation functor associated with X = Pn
R or any
quasi-projective and quasi-compact scheme over R is the following. If C = {OX (n)}n∈Z then with
Γ ∈ LR(C,R ) we can associate the Z-gradedR-moduleM = ⨁
n∈Z Γ OX (−n). The functorial prop-
erties of Γ allow us to deﬁne a structure of graded S-module onM , whereS = ⨁
n∈Z H0(OX (n)) is
the homogeneous coordinate ring of X . This associations extends to an equivalence of categories
between LR(C,R ) and the category of graded S-modules. The functor Ω ∗ corresponds to the
functor Γ ∗ which carries a quasi-coherent sheaf F on X to the graded S-module ⨁
n∈Z H0(F (n)).
Finally the sheaﬁﬁcation functor from the graded S-modules to QCoh X is left adjoint to Γ ∗.
Let us ﬁx an R-algebra A and a ﬁbered category π : X − → Aﬀ /R.
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 10
2.1. Sheaﬁfying R-linear functors. In this section we want to explicitly describe sheaﬁﬁcation
functors for small subcategories of QCoh X . In particular we ﬁx a small (and non empty)
subcategory C of QCoh X .
In the construction of the sheaﬁﬁcation functors we will mak e use of the coend construction
in the settings of categories enriched over categories of mo dules over a ring. The general theory
simpliﬁes considerably in this context and we will also appl y such construction only in particular
cases. In the following remark we collect all the properties we will need.
Remark 2.3. Let Y be a ﬁbered category over R, F : C − →QCoh Y be an R-linear functor and
Γ ∈ LR(C,A ). The coend of the R-linear functor Γ − ⊗RF− : Cop ⊗ C − →QCohA Y, denoted by
ˆE∈C
Γ E ⊗RFE ∈ QCohA Y
is the cokernel of the map
⨁
E
u
− − →E
(Γu ⊗ idFE − idΓ E ⊗Fu) :
⨁
E
u
− − →E
Γ E ⊗RFE − →
⨁
E∈C
Γ E ⊗RFE
Moreover it comes equipped with an A-linear natural isomorphism
HomQCohA Y (
ˆE∈C
Γ E ⊗RFE, H)
α
− − →HomLR(C,A )(Γ, HomY (F−, H)) for H ∈ QCohA Y
given by
α(
ˆE∈C
Γ E ⊗RFE
u
− − → H)(x) = u ◦pE (x ⊗ −) :FE − → Hfor E ∈ C,x ∈ Γ E
where pE : Γ E ⊗RFE − →
´E∈C Γ E ⊗RFE for E ∈ C are the structure morphisms. Its inverse is
uniquely determined by the expression
α−1(Γ
v
− − →HomY (F−, H)) ◦pE : Γ E ⊗R E − → H, x⊗y ↦− →vE (x)(y) for E ∈ C
Natural transformationsF − →F ′ and Γ − →Γ ′ yields morphisms
´E∈C
Γ E ⊗RFE − →
´E∈C
Γ E ⊗R
F ′
E and ´E∈C Γ E ⊗R FE − → ´E∈C Γ ′
E ⊗R FE respectively. Those can be deﬁned either using
Yoneda’s lemma and the above characterization of Hom (
´E∈C Γ E ⊗RFE, −) or directly using the
description of
´E∈C Γ E ⊗RFE as a cokernel.
All the above claims are standard in the theory of coend in the enriched settings (in our case
enriched by Mod R), but, in this simpliﬁed context, it is elementary to prove t hem directly.
We start by showing that C (and therefore any essentially small subcategory of QCoh X )
admits a sheaﬁﬁcation functor.
Proposition 2.4. The Yoneda functor Ω ∗ : QCohA X − → LR(C,A ) has a left adjoint F−, C : LR(C,A ) − →
QCohA X given by
FΓ, C : X op − →(Sets), X ∋ ξ ↦− →
ˆE∈C
Γ E ⊗R E(ξ) ∈ Mod(H0(Oπ (ξ)) ⊗RA)
where E(ξ) denotes the evaluation C − →Mod H0(Oπ (ξ)) of sheaves in ξ ∈ X . Alternatively
FΓ, C =
ˆE∈C
Γ E ⊗R E ∈ QCohA X
where E denotes the inclusion C − →QCoh X .
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 11
Proof. It is enough to apply 2.3 with Y = X and F : C − → QCoh X the inclusion. Using the
description of coend as cokernel one can check that the two fu nctors deﬁned in the statement
are canonically isomorphic. □
Deﬁnition 2.5. We denote byγΓ : Γ − − →Ω FΓ , C
− = HomX (−, FΓ, C) andδG : FΩ G, C − → Gfor Γ ∈
LR(C,A ) and G ∈ QCohA X the unit and the counit of the adjunction between Ω ∗ : QCohA X − →
LR(C,A ) and F∗, C : LR(C,A ) − →QCohA X respectively.
Given ξ ∈ X , E ∈ C , ψ ∈ E (ξ) and x ∈ Γ E we denote by xE,ψ ∈ F Γ, C(ξ) the image of x ⊗ψ
under the map Γ E ⊗R E(ξ) − → FΓ, C(ξ)
Proposition 2.6. Let Γ ∈ LR(C,A ). The unit γΓ : Γ − − →Ω FΓ , C
− = HomX (−, FΓ, C) is given by
Γ E
x
HomX (E, FΓ, C)
(φ ↦− →xE,φ )
If G ∈ QCohA X the counit δG : FΩ G, C − → G is given by
FΩ G, C(ξ) ∋xE,ψ ↦− →x(ψ) ∈ G (ξ) for E ∈ C,x ∈ Ω G
E = HomX (E, G),ξ ∈ X,ψ ∈ E (ξ)
Proof. IfpE : Γ E ⊗R E − → FΓ, C for E ∈ C are the maps associated with the coend deﬁning FΓ, C,
then pE (x ⊗ψ) = xE,ψ for x ∈ Γ E,ψ ∈ E (ξ) and ξ ∈ X . All the claims follows by a direct check
using the explicit description of the isomorphism
HomQCohA X (
ˆE∈C
Γ E ⊗R E, H)
α
− − →HomLR(C,A )(Γ, Ω H) for H ∈ QCohA X
and its inverse given in 2.3. □
Given a map g : Y − → X of ﬁbered categories we want to express g∗FΓ, C ∈ QCohA Y for
Γ ∈ LR(C,A ) as Fg∗Γ,g ∗C for a suitable choice of g∗C ⊆ QCoh Y and g∗Γ ∈ LR(g∗C,A ).
Deﬁnition 2.7. Let Y be a ﬁbered category, g : Y − → X be a morphism and D be a subcategory
of QCoh X . We set g∗D for the subcategory of QCoh Y of sheavesg∗E for E ∈ D . If D′ ⊆ QCoh Y
is a subcategory containing g∗D we can deﬁne a restriction functor
LR(D′,A ) LR(D,A )
Γ Γ ◦g∗
g∗
Proposition 2.8. Let Y be a ﬁbered category, g : Y − → X be a morphism and D be a sub-
category of QCoh Y such that g∗C ⊆ D . Then g∗ : LR(D,A ) − →LR(C,A ) has a left adjoint
g∗ : LR(C,A ) − →LR(D,A ) and it is given by
(g∗Γ) G =
ˆE∈C
Γ E ⊗R HomY (G,g ∗E) ∈ ModA for Γ ∈ LR(C,A ), G ∈ D
where HomY (G,g ∗−) is thought of as a functor C − → ModR. If Y = X and g = idX , so that
C ⊆ D and (idX )∗ : LR(D,A ) − →LR(C,A ) is the restriction, then the unit Γ − →(id∗
X Γ) |C is an
isomorphism for Γ ∈ LR(C,A ).
Proof. Let Ω ∈ LR(D,A ). Applying 2.3 with F = HomY (G,g ∗−) we get a bijection between
HomA((g∗Γ) G, Ω G) and the set ofA-linear natural transformations Γ E − →HomR(Hom(G,g ∗E), Ω G)
for E ∈ C . A natural transformation g∗Γ − →Ω corresponds to a collection γ of A-linear maps
γG, E : Γ E − →HomR(Hom(G,g ∗E), Ω G) natural in E ∈ C and such that
γG, E (x)(φ ◦u) = Ω u(γG, E (x)(φ)) for x ∈ Γ E, G
φ
− − →g∗E, G
u
− − →G ∈ D
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 12
Set µγ (x) = γg∗E, E (x)(idg∗E ) ∈ Ωg∗E for E ∈ C ,x ∈ Γ E. If γ is a collection as above it follows
that γG, E(x)(ψ) = Ω ψ (µγ (x)) for E ∈ C , G ∈ D , x ∈ Γ E and G
ψ
− − →g∗E and that µγ : Γ E − →
Ωg∗E = (g∗Ω) E is A-linear and natural in E. Conversely, given a morphism µ : Γ − →(g∗Ω) in
LR(C,A ) we can always deﬁne a collection γ as above by setting γG, E (x)(ψ) = Ω ψ (µ(x)). It is
easy to check that γ induces a morphism g∗Γ − →Ω and that the above constructions yields a
bijection Hom (g∗Γ, Ω) ≃ Hom(Γ,g ∗Ω) .
Assume now Y = X and g = idX and let Γ ∈ LR(C,A ) and E ∈ C . Denote by α : Γ − →
(id∗
X Γ) |C the unit morphism. If p ~E : Γ ~E ⊗ HomX (E, ~E) − →(id∗
X Γ) E are the structure morphisms
as in 2.3, then αE = pE(− ⊗ idE). In particular, given H ∈ ModA and using 2.3, the map
HomA(αE, H) : HomA((id∗
X Γ) E, H) − →HomA(Γ E, H) sends an A-linear natural transformation
δ : Γ − − →HomR(HomX (E, −), H) to Γ E ∋ x ↦− →δ(x)(idE ) ∈ H . Since δ corresponds to an
R-linear natural transformation Hom X (E, −) − →HomA(Γ −, H), by Yoneda lemma we see that
HomA(αE, H) is an isomorphism. □
The above proposition yields a natural extension of any Γ ∈ LR(C,A ) to a functor Γex ∈
LR(QCoh X,A ). By abuse of notation we will denote them by the same symbol Γ . This means
that if Γ ∈LR(C,A ) and G ∈ QCoh X then we can evaluate Γ on G, writing Γ G.
Given a map g : Y − → X we will denote by g∗ : LR(C,A ) − →LR(g∗C,A ) the left adjoint of the
restriction LR(g∗C,A ) − →LR(C,A ). So, given Γ ∈ LR(C,A ), g∗Γ is a functor g∗C − → ModA
but it also deﬁnes a functor QCoh Y − →ModA denoted, by our convention, by the same symbol.
By 2.8 the functor g∗Γ : QCoh Y − → ModA coincides with the value of the left adjoint of the
restriction LR(QCoh Y,A ) − →LR(C,A ).
Remark 2.9. Given Γ ∈ LR(C,A ) and E ∈ C we have R-linear morphisms of rings
H0(OX ) ≃ EndX (OX ) − →EndX (E) − →EndA(Γ E )
This deﬁnes a lifting of Γ to an R-linear functor Γ : C − →Mod(H0(OX )⊗RA) and an equivalence
LR(C,A ) − →LR(C, H0(OX ) ⊗RA)
In particular, if g : SpecB − → X is a map and Γ ∈ LR(C,A ) then (g∗Γ)B has a B ⊗RA-module
structure. By 2.4 and 2.8 there is a canonical A-linear isomorphism
FΓ, C(B) ≃ (g∗Γ)B
and it is easy to see that it is also B-linear.
Proposition 2.10. Let g : Y − → X be a morphism of ﬁbered categories. Then there exists an
isomorphism g∗FΓ, C ≃ Fg∗Γ,g ∗C natural in Γ ∈ LR(C,A ), that is a 2-commutative diagram
LR(C,A ) QCohA X
LR(g∗C,A ) QCohA Y
F−, C
g∗ g∗
F−,g ∗ C
Proof. Let Γ ∈ LR(C,A ). Let also Spec B
ξ
− − → Ybe a map and N ∈ ModB ⊗RA. Denote by
F : C − → ModB and G : g∗C − → ModB the functors obtained by taking sections over B. In
particular F =G ◦g∗. We have isomorphisms
HomB⊗RA(Fg∗Γ,g ∗C(B),N ) ≃ HomLR(g∗C,A )(g∗Γ, HomB(G,N )) ≃ HomLR(C,A )(Γ,g ∗ HomB(G,N ))
= HomLR(C,A )(Γ, HomB(F,N )) ≃ HomB⊗RA((g∗FΓ, C)(B),N )
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 13
In particular we get an isomorphism (g∗FΓ, C)(B) ≃ Fg∗Γ,g ∗C(B). By a direct check it follows
that this isomorphism is natural in Γ and it also extends as an isomorphism of functors g∗FΓ, C ≃
Fg∗Γ,g ∗C. □
Notice that, as soon as g∗ : QCoh X − → QCoh Y has a right adjoint g∗ : QCoh Y − →QCoh X
(see 1.7), then g∗Ω G ≃ Ωg∗G for G ∈ QCohA Y and the above proposition follows taking the left
adjoints.
Remark 2.11. IfA − →A′ is a morphism ofR-algebras then we have pull-back functors LR(C,A ) − →
LR(C,A ′) and QCohA X − → QCohA′ X . The ﬁrst one is obtained considering the tensor product
− ⊗AA′, while the second one corresponds to the pullback QCoh XA − →QCoh XA′ along the
projection XA′ − → XA. Alternatively, those functors are left adjoints to the res triction of scalars
LR(C,A ′) − →LR(C,A ) and QCohA′ X − → QCohA X respectively. It is easy to see that in this
way we obtain two fpqc stacks (not in groupoids) L R(C, −) and QCoh − X over the category of
aﬃne R-schemes. Notice that the functor Ω ∗ : QCoh− X − → LR(C, −) is not a morphism of
stacks because Hom X (E, G) ⊗AA′ ⁄≃HomX (E, G ⊗AA′) in general for E ∈ C and G ∈ QCohA X .
Proposition 2.12. The functor F∗, C : LR(C, −) − →QCoh− X is a morphism of stacks.
Proof. Given a morphism A − →A′ of R-algebras we have a 2-commutative diagram
QCohA′ X LR(C,A ′)
QCohA X LR(C,A )
Ω ∗
Ω ∗
where the vertical arrows are obtained by restricting the sc alars from A′ to A. Using 2.11 and
taking the left adjoint functors of the functors in the diagr am we exactly get the 2-commutative
diagram expressing the fact that F∗, C preserves Cartesian arrows. □
We conclude this section by showing that, when considering s heaﬁﬁcation functors F−, C, we
can always reduce problems to the case when C is an additive category. Moreover in this case
the sections of F−, C have a nice expression in terms of a direct limit.
Deﬁnition 2.13. Given a subcategory D of QCoh X we denote by D⊕ the subcategory of
QCoh X whose objects are all ﬁnite direct sums of sheaves in D.
Notice that if D is small then D⊕ is small.
Proposition 2.14. The restriction LR(C⊕,A ) − →LR(C,A ) and its left adjoint are inverses of
each other. In particular if Γ ∈ LR(C⊕,A ) then we have a canonical isomorphism FΓ, C⊕ ≃ F Γ |C, C.
Proof. Denote the restriction by α and its left adjoint by β. From 2.8 we know thatαβ(Γ) ≃ Γ for
Γ ∈ LR(C,A ). Conversely, if Γ ∈ LR(C⊕,A ), we have a canonical morphism γ : βα(Γ) − →Γ . If
E ∈ C the mapγE is easily seen to be an isomorphism and by additivity this als o follows forγ. For
the last claim it is enough to note that the composition QCoh A X
Ω ∗
− − →LR(C⊕,A ) − →LR(C,A )
is exactly Ω ∗ : QCohA X − → LR(C,A ). □
Remark 2.15. If C is an R-linear and additive category and F,G : C − →ModA are R-linear
(covariant or contravariant) functors then any natural tra nsformationλ : F − →G of functors of
sets is R-linear. Indeed by considering C op we can consider only covariant functors. In this case
it is easy to show that the maps λX : F (X) − →G(X) forX ∈ C areR-linear using functoriality
on the map ridX : X − →X for r ∈R and pr 1, pr2, pr1 + pr2 : X ⊕X − →X, where pr ∗ are the
projections.
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 14
Deﬁnition 2.16. Let Spec B − → X be a map. We denote by JB, C the category of pairs (E,ψ )
where E ∈ C ⊕ and ψ ∈ E (B). Given Γ ∈ LR(C,A ) we have a functor Γ : JB, C − →ModA given
by Γ E,ψ = Γ E.
Proposition 2.17. Let SpecB − → X be a map and Γ ∈ LR(C,A ). The category JB, C is non-
empty and for all ξ,ξ ′ ∈JB, C there exists ξ′′ ∈JB, C and maps ξ′′ − →ξ, ξ′′ − →ξ′. The A-linear
maps Γ E,ψ = Γ E − → FΓ, C⊕(B) ≃ F Γ, C(B), x ↦− →xE,ψ for (E,ψ ) ∈ JB, C (see 2.5) induce an
A-linear isomorphism
lim− →
(E,ψ )∈J op
B, C
Γ E,ψ − → FΓ, C(B)
In particular all elements of FΓ, C(B) are of the form xE,ψ for some E ∈ C ⊕,x ∈ Γ E andψ ∈ E (B).
The multiplication by b ∈B on the ﬁrst limit is induced by mapping Γ E,ψ to Γ E,bψ using idΓ E for
(E,ψ ) ∈JB, C.
Proof. By 2.14 we can assume C = C⊕. Denote by H and α : H − → FΓ, C(B) the limit and the
map in the statement respectively. The category JB, C is not empty because (E, 0) ∈JB, C for all
E ∈ C and the map α is well deﬁned because, for all x ∈ Γ E and for all (E,ψ )
u
− − →(E,u (ψ)) we
havexE,u (ψ ) = (Γu(x))E,ψ , by deﬁnition of FΓ, C(B) as coend. Moreover if (E1,ψ 1), (E2,ψ 2) ∈JB, C
then we have maps pr i : ( E1 ⊕ E2,ψ 1 ⊕ψ2) − →(Ei,ψi) for i = 1, 2, where pr i is the projection.
In particular any element of H comes from a map Γ E,ψ − → H, where (E,ψ ) ∈ JB, C. Thus all
elements of FΓ, C(B) are of the form xE,ψ for some E ∈ C ⊕, x ∈ Γ E and ψ ∈ E (B) provided that
we prove that α is an isomorphism.
Given an A-module N then HomA(H,N ) isA-linearly isomorphic to the set of natural trans-
formations of sets βE : E(B) − →HomA(Γ E,N ). Since C is additive, by 2.15, those transfor-
mations are automatically R-linear. Given b ∈ B there is an A-linear map φb ∈ EndA(H) as
described in the last sentence in the statement. A direct che ck shows that, given an A-module
N , the map Hom A(φb,N ) : HomA(H,N ) − →HomA(H,N ) sends an R-linear natural transfor-
mation βE : E(B) − →HomA(Γ E,N ) to βE ◦bidE. This easily implies that φ : B − →EndA(H)
makes H into a B ⊗RA-module and that α : H − → FΓ, C(B) is also B-linear. Since B ⊗RA-
linear maps H − →N , for N ∈ ModB ⊗RA, corresponds to B-linear natural transformations
E(B) − →HomA(Γ E,N ) and thus to A-linear natural transformations Γ E − →HomB(E(B),N )
as described above, one can check directly (using 2.3) that HomB⊗RA(α,N ) induces the identity
on Hom LR(C,A )(Γ −, HomB(−(B),N )). This implies that α : H − → FΓ, C(B) is an isomorphism.
□
2.2. Sheaﬁfying R-linear monoidal functors. In this section we show how “ring structures”
on a quasi-coherent sheaf over X correspond to “monoidal” structures on the corresponding
Yoneda functor.
We start setting up some deﬁnitions:
Deﬁnition 2.18. Let C and D be R-linear symmetric monoidal categories. A (contravariant)
pseudo-monoidal functor Ω : C − →D is an R-linear (and contravariant) functor together with
a natural transformation
ιΩ
V,W : Ω V ⊗ ΩW − →ΩV ⊗W for V,W ∈ C
A (contravariant) pseudo-monoidal functor Ω : C − →D is
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 15
1) symmetric or commutative if for all V,W ∈ C the following diagram is commutative
ΩV ⊗ ΩW ΩV ⊗W
ΩW ⊗ ΩV ΩW ⊗V
ιΩ
V,W
ιΩ
W,V
where the vertical arrows are the obvious isomorphisms;
2) associative if for all V,W,Z ∈ C the following diagram is commutative
ΩV ⊗ ΩW ⊗ ΩZ ΩV ⊗W ⊗ ΩZ
ΩV ⊗ ΩW ⊗Z ΩV ⊗W ⊗Z
ιΩ
V,W ⊗id
ιΩ
V,W ⊗Z
id⊗ιΩ
W,Z ιΩ
V ⊗W,Z
IfI andJ are the unit objects of C and D respectively, a unity for Ω is a morphism 1 :J − →ΩI
such that, for all V ∈ C , the compositions
ΩV ⊗J
id⊗1
− − − →ΩV ⊗ ΩI
ιΩ
V,I
− − − →ΩV ⊗I − →ΩV and J ⊗ ΩV
1⊗id
− − − →ΩI ⊗ ΩV
ιΩ
I,V
− − − →ΩI⊗V − →ΩV
coincide with the natural isomorphisms ΩV ⊗J − →ΩV and J ⊗ ΩV − →ΩV respectively. A
(contravariant) monoidal functor Ω : C − →D is a symmetric and associative pseudo-monoidal
(contravariant) functor with a unity 1.
A morphism of pseudo-monoidal functors (Ω,ι Ω ) − →(Γ,ι Γ ), called a monoidal morphism or
tranformation, is a natural transformation Ω − →Γ which commutes with the monoidal structures
ι∗. A morphism of monoidal functors is a monoidal transformati on preserving the unities.
Deﬁnition 2.19. We deﬁne the categories:
• RingsA X , whose objects are B ∈ QCohA X with an A-linear map m : B ⊗OXA
B − →B,
called the multiplication;
• QAlgA X , as the (not full) subcategory of Rings A X whose objects are B with a commu-
tative, associative multiplication with a unity and the arr ows are morphisms preserving
unities;
We also set Rings X = RingsR X and QAlg X = QAlgR X .
Let D be a monoidal subcategory of QCoh X , that is a subcategory such that OX ∈ D and
for all E, E ′ ∈ D we have E ⊗ E ′ ∈ D . We deﬁne the category PML R(D,A ) (resp. ML R(D,A )),
whose objects are Γ ∈ LR(D,A ) with a pseudo-monoidal (resp. monoidal) structure.
Remark 2.20. Ifq : XA − → X is the projection, the equivalence QCoh XA − →QCohA X extends
to an equivalence
q∗ : QRings XA − →QRingsA X
Indeed, if G ∈ QCoh XA thenq∗(G ⊗OXA
G) = q∗G ⊗OXA
q∗G (see 1.11). We will use the following
notation, which is somehow implicit in the deﬁnition of QAlg A X : a sheaf B ∈ QRingsA X with
B ≃q∗B′ is associative (resp. commutative, has a unity, ...) if B′ has the same property.
If B ∈ QRingsA X with multiplication m, then the composition B ⊗OX B − → B ⊗OXA
B
m
− − →B induces a ring structure on B as an OX -module, i.e. B ∈ QRings X . Moreover
B ∈ QRingsA X is associative (resp. commutative, has a unity) if and only i f B has the same
property. If B ∈ QAlgA X we can form the relative spectrum Spec B over XA and also over X .
The ﬁnal result is the same.
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 16
Remark 2.21. For B ∈ RingsA X or Γ ∈ PMonR(D,A ) having a unity is a property, not an
additional datum. Indeed in both cases unities are unique.
Let D be a monoidal subcategory of QCoh X . If B ∈ RingsA X with multiplication m, we
endow Ω B ∈ LR(D,A ) with the pseudo monoidal structure
ιB : Hom(E, B)⊗AHom(E, B) − →Hom(E⊗E, B⊗OXA
B)
Hom(E⊗E,m )
− − − − − − − − − →Hom(E⊗E, B), E, E ∈ D
that is ιB
E, E (φ ⊗ψ) = m ◦ (φ ⊗ψ). If 1 ∈ B is a unity then we set 1B = 1 ∈ Ω B
OX = H0(B)
Proposition 2.22. The structures deﬁned above yield an extension of the functor Ω ∗ : QCohA X − →
LR(D,A ) to a functor Ω ∗ : QRingsA X − → PMLR(D,A ). Moreover if B ∈ RingsA X is associa-
tive (resp. commutative, has a unity 1 ∈ B) then Ω B is associative (resp. symmetric, has unity
1B ∈ Ω B
OX ). In particular we also get a functor Ω ∗ : QAlgA X − → MLR(D,A ).
Proof. The proof is elementary and it consists of applying the deﬁni tions. □
Let C be a small monoidal subcategory of QCoh X . Given Γ ∈ PMonR(C,A ) with monoidal
structure ι, we deﬁne the multiplication mΓ : AΓ, C ⊗OXA
AΓ, C − →AΓ, C on AΓ, C = FΓ, C by
AΓ, C(B) ⊗B⊗RA AΓ, C(B) ∋xE,ψ ⊗xE,ψ − →ιE, E (x ⊗x)E⊗E,ψ ⊗ψ ∈ AΓ, C(B)
where Spec B − → X is a map, E, E ∈ C , ψ ∈ E (B), ψ ∈ E(B), x ∈ Γ E, x ∈ Γ E (see 2.5). We
continue to denote by AΓ, C the sheaf FΓ, C together with the multiplication map just deﬁned.
If 1 ∈ Γ OX is a unity we set 1Γ ∈ AΓ, C the image of 1 under the morphism Γ OX − →Ω AΓ , C
OX =
H0(AΓ, C).
Proposition 2.23. The structures deﬁned above yield an extension of the functor F∗, C : LR(C,A ) − →
QCohA X to a functor A∗, C : PMLR(C,A ) − →RingsA X which is left adjoint to Ω ∗ : RingsA X − →
PMLR(C,A ). More precisely, if B ∈ RingsA X then the morphism δB : AΩ B, C − → B pre-
serves multiplications and unities, while if Γ ∈ PMonR(C,A ) then the natural transformation
γΓ : Γ − →Ω AΓ , C is monoidal and preserves unities (see 2.5).
If Γ ∈ PMonR(C,A ) is associative (resp. symmetric, has a unity 1 ∈ Γ OX ) then AΓ, C is asso-
ciative (resp. commutative, has unity 1Γ ∈ AΓ, C). In particular we get a functor A∗, C : MLR(C,A ) − →
QAlgA X which is left adjoint to Ω ∗ : QAlgA X − → MLR(C,A ).
Proof. A lot of properties have to be checked. All of them are very eas y, because they consist
only in the application of the deﬁnitions. We therefore leav e them to the reader. □
