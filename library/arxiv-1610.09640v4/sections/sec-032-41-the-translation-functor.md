---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-032-41-the-translation-functor
section_title: "The Translation Functor"
section_number: 4.1
pages: 79-82
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
morphism, all in the context of the DG categoryC(A, M).
We then study properties of DG functorsF : C(A, M)→C(B, N) between such
DGcategories. InviewofTheorem3.9.16itsuﬃcestolookatcovariantDGfunctors
(and not to worry about contravariant DG functors).
4.1. The Translation Functor.The translation functor goes back to the begin-
nings of derived categories – see Remark 4.1.13. The treatment in this subsection,
with the “littlet operator”, is taken from [173, Section 1]. Here and later, the word
“operator” is used as a synonym for “morphism in a linear category”.
Deﬁnition 4.1.1.Let M ={Mi}i∈Z be a graded object in M, i.e. an object of
G(M). The translation of M is the object
T(M) =
{
T(M)i}
i∈Z∈G(M)
deﬁned as follows: the graded component of degreei of T(M) is T(M)i :=Mi+1.
Deﬁnition 4.1.2(The little t operator). LetM ={Mi}i∈Z be an object ofG(M).
We deﬁne
tM :M→T(M)
to be the degree−1 morphism of graded objects ofM, that for every degreei is
the identity morphismtM|Mi := idMi :Mi ≃
− →T(M)i−1 of the objectMi in M.
Note that the morphismtM : M→T(M) is a degree−1 isomorphism in the
graded category G(M).
Deﬁnition 4.1.3.ForM∈G(M) we deﬁne the morphismt−1
M : T(M)→M in
G(M) to be the inverse oftM.
Of course the morphismt−1
M has degree+1. The reason for stating this deﬁnition
is to avoid the potential confusion between the morphismt−1
M in G(M) and the
degree−1 component of the morphism tM, which we denote by tM|M−1, as in
Deﬁnition 4.1.2 above.
Deﬁnition 4.1.4.Let M ={Mi}i∈Z be a DGA-module in M, i.e. an object of
C(A, M). The translation of M is the object
T(M)∈C(A, M)
deﬁned as follows.
(1) As a graded object ofM, it is as speciﬁed in Deﬁnition 4.1.1.
(2) The diﬀerentialdT(M) is deﬁned by the formula
dT(M) :=−tM◦dM◦t−1
M .
(3) Let fM : A→EndM(M) be the DG ring homomorphism that determines
the action ofA on M. Then
fT(M) :A→EndM(T(M))
is deﬁned by
fT(M)(a) := (−1)j·tM◦fM(a)◦t−1
M
for a∈Aj.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
79
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Thus, thediﬀerentialdT(M) ={di
T(M)}i∈Z makesthisdiagramin Mcommutative
for everyi :
T(M)i di
T(M)
// T(M)i+1
Mi+1
tM
OO
−di+1
M //Mi+2
tM
OO
And the leftA-module structure makes this diagram inM commutative for everyi
and everya∈Aj :
T(M)i fT(M)(a) // T(M)i+j
Mi+1
tM
OO
(−1)j·fM(a) //Mi+j+1
tM
OO
Proposition 4.1.5.The morphismstM and t−1
M are cocycles, in the DGK-modules
HomA,M
(
M, T(M)
{
and HomA,M
(
T(M),M
{
respectively.
Proof. We use the notation dHom for the diﬀerential in the DG module
HomA,M
(
M, T(M)
{
. Let us calculate. BecausetM has degree−1, we have
dHom(tM) = dT(M)◦tM + tM◦dM
= (−tM◦dM◦t−1
M )◦tM + tM◦dM = 0.
As for t−1
M : this is done using the graded Leibniz rule, just like in the proof
Proposition 3.4.9. □
Deﬁnition 4.1.6.Given a morphismφ∈HomA,M(M,N )i we deﬁne the morphism
T(φ)∈HomA,M
(
T(M), T(N)
{i
to be
T(φ) := (−1)i·tN◦φ◦t−1
M .
To clarify this deﬁnition, let us writeφ={φj}j∈Z, so thatφj :Mj→Nj+i is a
morphism inM. Then T(φ)j : T(M)j→T(N)j+i is T(φ)j = (−1)i·tN◦φj+1◦t−1
M .
The corresponding commutative diagram inM, for eachi,j, is:
(4.1.7) T(M)j T(φ)j
// T(N)j+i
Mj+1
tM
OO
(−1)i·φj+1
//Nj+i+1
tN
OO
Theorem 4.1.8. Let M be an abelian category and letA be a DG ring.
(1) The assignmentsM↦→T(M) and φ↦→T(φ) are a DG functor
T : C(A, M)→C(A, M).
(2) The collection t :={tM}M∈C(A,M) is a degree−1 isomorphism
t : Id→T
of DG functors fromC(A, M) to itself.
Proof.
80
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) Take morphismsφ1 : M0 →M1 and φ2 : M1 →M2, of degrees i1 and i2
respectively. Then
T(φ2◦φ1) = (−1)i1+i2·tM2◦(φ2◦φ1)◦t−1
M0
= (−1)i1+i2·tM2◦φ2◦(t−1
M1◦tM1)◦φ1◦t−1
M0
=
(
(−1)i2·tM2◦φ2◦t−1
M1
{
◦
(
(−1)i1·tM1◦φ1◦t−1
M0
{
= T(φ2)◦T(φ1).
Clearly T(idM) = id T(M), and T(λ·φ+ψ) = λ·T(φ) + T(ψ) for all λ∈K and
φ,ψ∈HomA,M(M0,M 1)i. So T is aK-linear graded functor.
By Proposition 4.1.5 we know thatd◦t =−t◦d and d◦t−1 =−t−1◦d. This
implies that for every morphismφin C(A, M), we haveT(d(φ)) = d(T(φ)). So T
is a DG functor.
(2) Take some φ∈HomA,M(M0,M 1)i. We have to prove that tM1◦φ=
(−1)i·T(φ)◦tM0 as elements ofHomA,M
(
M0, T(M1)
{i+1
. But by Deﬁnition 4.1.6
we have
T(φ)◦tM0 =
(
(−1)i·tM1◦φ◦t−1
M0
{
◦tM0 = (−1)i·tM1◦φ. □
Deﬁnition 4.1.9.We callT the translation functorof the DG categoryC(A, M).
Corollary 4.1.10.
(1) The functor T is an automorphism of the DG categoryC(A, M).
(2) For everyk,l∈Z there is an equality of functorsTl◦Tk = Tl+k.
Proof. (1) By the theorem,T is a DG functor. By deﬁnition,T is bijective on the
set of objects ofC(A, M) and on the sets of morphisms.
(2) By part (1) of this corollary, the inverseT−1 is a uniquely deﬁned functor (not
just up to an isomorphism of functors). Thus we can deﬁneTk, thek-th power of
T, and the equality stated holds. □
Proposition 4.1.11. Consider anyM∈C(A, M).
(1) There is equality tT(M) = −T(tM) of degree−1 morphisms T(M) →
T2(M) in C(A, M).
(2) There is equalitytT−1(M) =−T−1(tM) between these degree−1 morphisms
T−1(M)→T(T−1(M)) =M = T−1(T(M)) in C(A, M).
Proof. (1) This is an easy calculation, using Deﬁnition 4.1.6: T(tM) =
−tT(M)◦tM◦t−1
M =−tT(M).
(2) A similar calculation. □
Proposition 4.1.12. Let M ∈C(A, M) and i∈Z. There is equality dTi(M) =
Ti(dM) in HomA,M
(
Ti(M), Ti(M)
{1
.
Proof. We start withi = 1. The diﬀerentialdM is an element ofHomM(M,M )1.
By Deﬁnitions 4.1.4 and 4.1.6 we getdT(M) =−tM◦dM◦t−1
M = T(dM). Using
induction oni the assertion holds for alli≥0.
Fori≤0 we use descending induction oni. We assume that the assertion holds
fori. Let us deﬁneN := Ti−1(M), soT(N) = Ti(M). By the previous paragraph,
with the DG moduleN, we know thatdTi(M) = dT(N) = T(dN) = T(d Ti−1(M)).
Applying the functor T−1 to this equality we get Ti−1(dM) = T−1(
Ti(dM)
{
=
T−1(dTi(M)) = dTi−1(M). □
81
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 4.1.13. There are several names in the literature for the translation
functor T : twist, shift and suspension. There are also several notations:T(M) =
M[1] = ΣM. In the later part of this book we shall use the notationM[k] := Tk(M)
for thek-th translation.
