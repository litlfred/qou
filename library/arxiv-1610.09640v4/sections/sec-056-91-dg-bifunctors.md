---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-056-91-dg-bifunctors
section_title: "DG Bifunctors"
section_number: 9.1
pages: 165-167
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
was for categories without further structure. Here we will consider DG categories,
and matters become a bit more complicated.
As a warmup, let us begin with linear bifunctors.
Deﬁnition 9.1.1.Let C1 and C2 be linear categories. We deﬁne the linear category
C1⊗C2 as follows. The set of objects is
Ob(C1⊗C2) := Ob(C1)×Ob(C2).
For each pair of objects(M1,M 2), (N1,N 2) in C1⊗C2, i.e.Mi,Ni∈Ob(Ci), we let
HomC1⊗C2
(
(M1,M 2), (N1,N 2)
{
:= HomC1(M1,N 1)⊗HomC2(M2,N 2).
Given morphisms φi∈HomCi(Li,Mi) and ψi∈HomCi(Mi,Ni), for i = 1, 2,
their tensors are morphisms
φ1⊗φ2∈HomC1⊗C2
(
(L1,L 2), (M1,M 2)
{
and
ψ1⊗ψ2∈HomC1⊗C2
(
(M1,M 2), (N1,N 2)
{
.
Everymorphismin C1⊗C2 isasumofsuchpuretensors. Wedeﬁnethecomposition
to be
(ψ1⊗ψ2)◦(φ1⊗φ2) := (ψ1◦φ1)⊗(ψ2◦φ2)
∈HomC1⊗C2
(
(L1,L 2), (N1,N 2)
{
.
Deﬁnition 9.1.2.Let C1, C2 and D be linear categories. Alinear bifunctor
F : C1×C2→D
is, by deﬁnition, a linear functorF : C1⊗C2→D.
Now to the DG situation.
Deﬁnition 9.1.3.Let C1 and C2 be DG categories. We deﬁne the DG category
C1⊗C2 as follows: the set of objects is
Ob(C1⊗C2) := Ob(C1)×Ob(C2).
For each pair of objects(M1,M 2), (N1,N 2) in C1⊗C2 we let
HomC1⊗C2
(
(M1,M 2), (N1,N 2)
{
:= HomC1(M1,N 1)⊗HomC2(M2,N 2).
The formula for the composition involves the Koszul sign rule. Given morphisms
φi∈HomCi(Li,Mi)di and ψi∈HomCi(Mi,Ni)ei, for i = 1, 2, their tensors are
morphisms
φ1⊗φ2∈HomC1⊗C2
(
(L1,L 2), (M1,M 2)
{d1+d2
and
ψ1⊗ψ2∈HomC1⊗C2
(
(M1,M 2), (N1,N 2)
{e1+e2
.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
165
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We deﬁne the composition to be
(ψ1⊗ψ2)◦(φ1⊗φ2) := (−1)d1·e2·(ψ1◦φ1)⊗(ψ2◦φ2)
∈HomC1⊗C2
(
(L1,L 2), (N1,N 2)
{d1+d2+e1+e2
.
Example 9.1.4.Suppose C1 and C2 are single-object DG categories, sayOb(Ci) =
{xi}. Then C1⊗C2 also has a single-object, sayy := (x1,x 2). The endomorphism
DG rings satisfy
EndC1⊗C2(y) = EndC1(x1)⊗EndC2(x2).
See formula 3.1.20 and Example 3.3.10.
DG functors between DG categories were introduced in Deﬁnition 3.5.1.
Deﬁnition 9.1.5.Let C1, C2 and D be DG categories. ADG bifunctor
F : C1×C2→D
is, by deﬁnition, a DG functorF : C1⊗C2→D, where C1⊗C2 is the DG category
from Deﬁnition 9.1.3.
Warning: due to the signs that the composition of odd morphisms acquires, a DG
bifunctor F does not become, after we forget the DG structure, a linear bifunctor
in the sense of Deﬁnition 9.1.2.
Proposition 9.1.6. Given a DG bifunctorF : C1×C2→D, there are induced
linear bifunctors on the strict subcategories
Str(F ) : Str(C1)×Str(C2)→Str(D)
and on the homotopy categories
Ho(F ) : Ho(C1)×Ho(C2)→Ho(D).
Exercise 9.1.7. Prove this proposition.
Let F be a DG bifunctor as in Deﬁnition 9.1.5. If we ﬁx an objectM1∈C1,
then F (M1,−) : C2→D is a DG functor. Similarly if we ﬁx the second argument
of F.
For DG bifunctors there are several options for contravariance. In Subsection
3.9 we talked about contravariant DG functors, and the opposite DG categoryCop
of a given DG categoryC.
Deﬁnition 9.1.8.Let C1, C2 and D be DG categories. A DG bifunctor that is
contravariant in the ﬁrst or the second argumentis, by deﬁnition, a DG bifunctor
F : C♦1
1 ×C♦2
2 →D
as in Deﬁnition 9.1.5, where the symbols}1 and}2 are either⟨empty⟩or op, as
the case may be.
Here are the two main examples of DG bifunctors. We give each of them in the
commutative version and the noncommutative version.
Example 9.1.9.Consider a commutative ringA. The category of complexes ofA-
modules is the DG categoryC(A), and we takeC1 = C2 = D := C(A). For each pair
of objectsM1,M 2∈C(A) there is an objectF (M1,M 2) :=M1⊗AM2∈C(A). This
is the usual tensor product of complexes. We deﬁne the action ofF on morphisms
as follows: givenφi∈HomC(A)(Mi,Ni)ki, we let
F (φ1,φ2) :=φ1⊗φ2∈HomC(A)
(
F (M1,M 2),F (N1,N 2)
{k1+k2
.
The result is a DG bifunctor
F = (−⊗A−) : C(A)×C(A)→C(A).
166
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Example9.1.10. ConsiderDGrings A0,A 1,A 2 (possiblynoncommutative, butK-
central). Deﬁne the DG categoriesCi := C(Ai−1⊗Aop
i ) and D := C(A0⊗Aop
2 ). For
each pair of objectsM1∈C1 and M2∈C2 there is a DGK-module F (M1,M 2) :=
M1⊗A1 M2; see Deﬁnition 3.3.23. This has a canonical DG(A0⊗Aop
2 )-module
structure:
(a0⊗a2)·(m1⊗m2) := (−1)j2·(k1+k2)·(a0·m1)⊗(m2·a2)
for elementsai∈Aji
i and mi∈Mki
i . In this wayF (M1,M 2) becomes an object of
D. We deﬁne the action ofF on morphisms as follows: givenφi∈HomCi(Mi,Ni)ki,
we let
F (φ1,φ2) :=φ1⊗φ2∈HomD
(
F (M1,M 2),F (N1,N 2)
{k1+k2
.
The result is a DG bifunctor
F = (−⊗A1−) : C(A0⊗Aop
1 )×C(A1⊗Aop
2 )→C(A0⊗Aop
2 ).
Compare this example to the one-sided construction in Example 4.6.2.
Example 9.1.11. Again we take a commutative ringA, but now our bifunctorF
arises from Hom, and so there is contravariance in the ﬁrst argument. We deﬁne the
DG categories C1 = C2 = D := C(A), the same as in Example 9.1.9. For every pair
of objectsM1,M 2∈C(A) there is an objectF (M1,M 2) := HomA(M1,M 2)∈C(A).
This is the usual Hom complex. We deﬁne the action ofF on morphisms as follows:
given
φ1∈HomCop
1
(M1,N 1)k1 = HomC(A)op(M1,N 1)k1 = HomA(N1,M 1)k1
and
φ2∈HomC2(M2,N 2)k2 = HomC(A)(M2,N 2)k2 = HomA(M2,N 2)k2
we let
F (φ1,φ2) := Hom(φ1,φ2)∈HomA
(
HomA(M1,M 2), HomA(N1,N 2)
{k1+k2
= HomD
(
F (M1,M 2),F (N1,N 2)
{k1+k2
.
The result is a DG bifunctor
F = HomA(−,−) : C(A)op×C(A)→C(A).
Example 9.1.12. Consider DG ringsA0,A 1,A 2 (possibly noncommutative, but
K-central). There is a DG bifunctor
F := HomA1(−,−) : C(A1⊗Aop
0 )op×C(A1⊗Aop
2 )→C(A0⊗Aop
2 ).
The details here are so confusing that we just leave them out. (We shall come back
to this bifunctor in Sections 14-18, and then we shall have to deal with the details.)
