---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-037-46-examples-of-dg-functors
section_title: "Examples of DG Functors"
section_number: 4.6
pages: 87-91
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
A and B are DG rings. Here are four examples of DG functors, of various types.
We work out in detail the translation isomorphism, the cone isomorphism and the
gauge in each example. These examples should serve as templates for constructing
other DG functors.
87
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Example 4.6.1. Here A =B =K, so C(A, M) = C(M) and C(B, N) = C(N). Let
F : M→N be aK-linear functor. It extends to a functorC(F ) : C(M)→C(N) as
follows: on objects, a complex
M =
(
{Mi}i∈Z,{di
M}i∈Z
{
∈C(M)
goes to the complex
C(F )(M) :=
(
{F (Mi)},{F (di
M)}
{
∈C(N).
A morphism φ = {φj}j∈Z in C(M) goes to the morphism C(F )(φ) :=
{F (φj)}j∈Z in C(N). A slightly tedious calculation shows thatC(F ) is a graded
functor.
Given a complexM∈C(M), letN := C(F )(M)∈C(N). Then the translation
of N is TN(N) = C(F )
(
TM(M)
{
; and the little t operator ofN is tN = C(F )(tM).
So the translation isomorphism
τC(F) : C(F )◦TM
≃
− →TN◦C(F )
of functors Cstr(M)→Cstr(N) is the identity automorphism of this functor.
Let φ: M0→M1 be a morphism in Cstr(M), whose image under C(F ) is the
morphism ψ:N0→N1 in Cstr(N). Then
Cone(ψ) =N1⊕TN(N0) = C(F )
(
Cone(φ)
{
as graded objects inN, with diﬀerential
dCone(ψ) =
dN1 ψ◦t−1
N0
0 d T(N0)

= C(F )
(dM1 φ◦t−1
M0
0 d T(M0)
{
= C(F )
(
dCone(φ)
{
.
We see that the cone isomorphismcone(F,φ) is the identity automorphism of the
DG module Cone(ψ). The gaugeγC(F) of the graded functorC(F ) is zero. There-
fore, by Theorem 4.3.2,C(F ) is a DG functor.
The next example is much more complicated, and we work out the full details
(only once – later on, such details will be left to the reader).
Example 4.6.2. Let A and B be DG rings, and ﬁx someN∈DGModB⊗Aop =
C(B⊗Aop). In other words,N is a DGB-A-bimodule. For everyM∈C(A) we
have a DGK-module F (M) := N⊗AM, as in Deﬁnition 3.3.23. The diﬀerential
of F (M) is
(4.6.3) dF(M) = dN⊗idM + idN⊗dM.
See formula (3.1.19) regarding the Koszul sign rule that’s involved. ButF (M) has
the structure of a DGB-module: for everyb∈B, n∈N and m∈M, the action
is b·(n⊗m) := (b·n)⊗m. Clearly
F : C(A) = DGModA→C(B) = DGModB
is a linear functor. We will show that it is actually a DG functor.
Let M0,M 1∈C(A), and consider theK-linear homomorphism
(4.6.4) F : HomA(M0,M 1)→HomB(N⊗AM0,N⊗AM1).
Take anyφ∈HomA(M0,M 1)i. Then
F (φ)∈HomB(N⊗AM0,N⊗AM1)
is the homomorphism that on a homogeneous tensorn⊗m∈(N⊗AM0)k+j, with
n∈Nk and m∈Mj
0, has the value
F (φ)(n⊗m) = (−1)i·k·n⊗φ(m)∈(N⊗AM1)k+j+i.
In other words,
(4.6.5) F (φ) = idN⊗φ.
88
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We see that the homomorphismF (φ) has degreei. SoF is a graded functor.
Let us calculateγF, the gauge ofF. From (4.6.5) and (4.6.3) we getγF,M =
dN⊗idM, which is often a nonzero endomorphism ofF (M). Still, take any degree
i morphism φ:M0→M1 in C(A). Then
γM1◦F (φ) = (dN⊗idM1)◦(idN⊗φ)
= dN⊗φ= (−1)i·(idN⊗φ)◦(dN⊗idM0) = (−1)i·F (φ)◦γM0.
We see thatγF satisﬁes the condition of Deﬁnition 3.5.4(1), which is really Deﬁni-
tion 3.1.39. By Theorem 4.3.2,F is a DG functor. (It is also possible to calculate
directly thatF is a DG functor.)
Finally let us ﬁgure out what is the translation isomorphismτF of the functor
F. TakeM∈C(A). Then τF,M : F (TA(M))→TB(F (M)) is an isomorphism in
Cstr(B). By Deﬁnition 4.4.1 we haveτF,M = tF(M)◦F (tM)−1. Take anyn∈Nk
andm∈Mj+1, so thatn⊗tM(m)∈(N⊗A TA(M))k+j =F (TA(M))k+j, a degree
k +j element ofF (TA(M)). But
n⊗tM(m) = (−1)k·(idN⊗tM)(n⊗m) = (−1)k·F (tM)(n⊗m).
Therefore
τF,M (n⊗tM(m)) = (−1)k·tF(M)(n⊗m)∈TB(F (M))k+j.
Observe that whenN is concentrated in degree0, we are back in the situation of
Example 4.6.1, in which there are no sign twists, andτF,M is the identity automor-
phism.
Example 4.6.6. Let A and B be DG rings, and ﬁx someN∈DGModA⊗Bop =
C(B⊗Aop). For any M ∈DGModA we deﬁneF (M) := HomA(N,M ). This is
a DG B-module: for every b∈Bi and φ∈HomA(N,M )j, the homomorphism
b·φ∈HomA(N,M )i+j has value (b·φ)(n) := (−1)i·(j+k)·φ(n·b) ∈Mi+j+k on
n∈Nk. As in the previous example,
F : C(A) = DGModA→C(B) = DGModB
is aK-linear graded functor.
The value of the gaugeγF at M∈C(A) is γF,M = Hom(dN, idM). See formula
(3.1.20) regarding this notation. Namely forψ∈F (M)j = HomA(N,M )j we have
γF,M (ψ) = (−1)j·ψ◦dN. It is not too hard to check thatγF is a degree1 morphism
of graded functors. Hence, by Theorem 4.3.2,F is a DG functor.
The formula for the translation isomorphismτF is as follows. TakeM∈C(A).
Then
τF,M :F (TA(M)) = HomA(N, TA(M))→TB(F (M)) = TB(HomA(N,M ))
is, by deﬁnition,τF,M = tF(M)◦F (tM)−1. Now F (tM)−1 = Hom(idN, t−1
M ). So
given anyψ∈F (TA(M))k, we haveτF,M (ψ) = tF(M)(t−1
M◦ψ)∈TB(F (M))k.
We end with a contravariant example.
Example 4.6.7. LetA be a commutative ring. Fix some complexN∈C(A). For
any M∈C(A) let F (M) := HomA(M,N )∈C(A). For every degreei morphism
φ: M0 →M1 in C(A) let F (φ) : F (M1)→F (M0) be the degree i morphism
F (φ) := HomA(φ,idN).
A direct calculation, that we leave to the reader, shows that
F : HomC(A)(M0,M 1)→HomC(A)
(
F (M1),F (M0)
{
is a strict homomorphism of DGK-modules. It also satisﬁes conditions (a) and (b)
of Deﬁnition 3.9.1. Thus we have a contravariant DG functorF : C(A)→C(A).
89
Derived Categories | Amnon Yekutieli | 14 Apr 2019
For contravariant DG functors we do not talk about translation isomorphisms or
gauges.
We will return to theDG bifunctors Hom(−,−) and (−⊗−) later in the book,
in Subsection 9.1.
90
Derived Categories | Amnon Yekutieli | 14 Apr 2019
