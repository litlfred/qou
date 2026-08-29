---
doc_id: arxiv-hep-th-9303139v2
doc_title: "ITFA 93-10 March 1993 A.Morozov"
section_id: sec-046-16-here-it-is-for-the-ﬁrst-time-that-we-encounte
section_title: "Here it is for the ﬁrst time that we encounter an important idea: matrix models -"
section_number: 16
pages: 43-46
source_pdf: 9303139v2.pdf
source_sha256: 79b9a45fd4c5b4aa
doc_brief: "ITFA 93-10 March 1993 A.Morozov — The theory of matrix models is reviewed from the point of view of its relation to integrable hierarchies."
---
the ordinary 1-matrix model (2.1) in this case - can be considered as deﬁning integral
transformations. This view on matrix models can to large extent deﬁne their role in the
future developement of string theory.
40
satisﬁed. If both n = N = 1, it is also trivially true, though for diﬀerent
reasons for diﬀerent choice of signs: for the upper signs, the ratio at the l.h.s.
is just unity and all derivatives vansih; for the lower signs we have:
 ∂
∂λ
!m
−
 
−∂
∂h
!m
=




X
a+b=m−1
a,b≥0
 ∂
∂λ
!a 
−∂
∂h
!b




 ∂
∂λ + ∂
∂h
!
,
and this obviously vanishes since ( ∂
∂λ + ∂
∂h)f(λ −h) ≡0 for any f(x).
If m > 0 and Λ, H are indeed matrices, direct evaluation becomes much
more sophisticated. We present the ﬁrst two nontrivial examples: m = 1 and
m = 2. The following relartions will be usefull. Let Q ≡
1
Λ⊗I−I⊗H. Then
Det±1Q ∂
∂Λtr
Det∓1Q = ± [(I ⊗Tr)Q] ;
Det±1Q
∂
∂Htr
Det∓1Q = ∓[(tr ⊗I)Q] ;
 ∂
∂Λtr
⊗I
!
Q = −[(tr ⊗I)Q] Q;
 
I ⊗
∂
∂Htr
!
Q = [(I ⊗Tr)Q] Q.
(2.79)
This is already enough for the proof in the case of m = 1. Indeed:
Det±1Q
 ∂
∂Λtr
⊗I ∓I ⊗
∂
∂Htr
!
QDet∓1Q =
= {−[(tr ⊗I)Q] Q ± [(I ⊗Tr)Q] Q} ∓
∓{[(I ⊗Tr)Q] Q ∓[(tr ⊗I)Q] Q} = 0.
The ﬁrst two terms at the r.h.s. come arise from Λ-, while the last two - from
H-derivatives.
In the case of m = 2 one should take derivatives once again. This is
a little more tricky, and the same compact notation are not suﬃcient. In
addition to (2.79) we now need:
 ∂
∂Λtr
⊗I
!
[(tr ⊗I)Q] Q = −[(tr ⊗I)Q]2 Q −B.
(2.80)
41
Here
[(tr ⊗I)Q]2 = [(tr ⊗I) [(tr ⊗I)Q] Q] ,
(2.81)
while in order to write B explicitly we need to restore matrix indices (Greek
for the Λ-sector and Latin - for the H one). The (αi, γk)-component of (2.80)
looks like:
 
∂
∂Λβα
δim
!
Qmj
δδ Qjk
βγ = −Qij
δδQjl
ββQlk
αγ −Qil
δβQlj
αδQjk
βγ
(2.82)
and appearence of the second term at the r.h.s. implies, that Bik
αγ = Qil
δβQlj
αδQjk
βγ.
Further,

∂
∂Λtr ⊗I

[(I ⊗Tr)Q] Q =
−[(I ⊗Tr) [(tr ⊗I)Q] Q] Q −[(I ⊗Tr) [(I ⊗Tr)Q] Q] Q;

I ⊗
∂
∂Htr

[(tr ⊗I)Q] Q =
+ [(tr ⊗I) [(I ⊗Tr)Q] Q] Q + [(I ⊗Tr) [(tr ⊗I)Q] Q] Q;

I ⊗
∂
∂Htr

[(I ⊗Tr)Q] Q = + [(I ⊗Tr) [(I ⊗Tr)Q] Q] Q + B.
(2.83)
It is important that B that appears in the last relation in the form of Bik
αγ =
Qlj
αδQil
δβQjk
βγ is exactly the same B as in eq.(2.80).
Now we can prove (2.78) for m = 2:
Det±1Q

∂
∂Λtr
2 ⊗I −I ⊗

∂
∂Htr
2
QDet∓1Q =
= {± [(I ⊗Tr)Q] (−[(tr ⊗I)Q] Q ± [(I ⊗Tr)Q] Q) −
−(−[(tr ⊗I) [(tr ⊗I)Q] Q] Q −B) ±
± (−[(I ⊗Tr) [(tr ⊗I)Q] Q] Q −[(tr ⊗I) [(I ⊗Tr)Q] Q] Q)} −
−{∓[(tr ⊗I)Q] ([(I ⊗Tr)Q] Q ∓[(tr ⊗I)Q] Q) +
+ ([(I ⊗Tr) [(I ⊗Tr)Q] Q] Q + B) ∓
∓([(tr ⊗I) [(I ⊗Tr)Q] Q] Q + [(I ⊗Tr) [(tr ⊗I)Q] Q] Q)}
(2.84)
where the terms 1,2,3,4,5,6 in the ﬁrst braces cancel the terms 1,3,2,4,6,5 in
the second braces and identity (2.81) and its counterpart with (tr ⊗I) →
(I ⊗Tr) is used.
Explicit proof of eq.(2.78) for generic m is unknown.
42
3
Eigenvalue models
3.1
What are eigenvalue models
Given the present state of knowledge we need to consider in most cases only
the narrow class of the ”eigenvalue” models. These models have the property
of being associated with conventional integrable hierarchies (of (multicom-
ponent) KP and Toda type), where integrable ﬂows just commute (instead
of forming less trivial closed algebras), and thus with the level-1 Kac-Moody
algebras (by artiﬁcial tricks, familiar from the bosonization formalism in
conformal ﬁeld theory [58] these can be sometimes generalized to particular
other levels like k = 2). This means that the models are essentially associated
with abelian Cartan subalgebras rather than with full matrix algebras. 17 In
CFT-formulation (see below) this means that the eigenvalue models can be
represented in terms of the free ﬁelds, which bosonize the Cartan subalgebra
of the whole group in the WZNW model (the remaining (β, γ)-ﬁelds [16] be-
ing (almost) neglected - their remnants are observed in the form of ”cocycle”
factors in the Frenkel-Kac formulas [47], see [58]). In the matrix-integral
representations the integrals for the eigenvalue models are in fact reduced to
those over diagonal matrices (consisting of eigenvalues of original matrices,
thus the name ”eigenvalue models”).
Most important, from the physical point of view eigenvalue models de-
scribe only topological (discrete) degrees of freedom, but not any propagat-
ing particles.
