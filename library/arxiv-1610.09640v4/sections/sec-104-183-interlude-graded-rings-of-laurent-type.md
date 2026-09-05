---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-104-183-interlude-graded-rings-of-laurent-type
section_title: "Interlude: Graded Rings of Laurent Type"
section_number: 18.3
pages: 425-429
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
were introduced in Section 15, and we now return to them, and refer to them
simply as graded rings. In this section we specialize to a particular kind of graded
ring, that is needed for the next two subsections. The two main results here are
Theorems 18.3.10 and 18.3.20.
We continue with Convention 18.1.1; in particular,K is a base ﬁeld, and all rings
are central overK.
Deﬁnition 18.3.1.A graded ring˜B is called agraded ring of Laurent typeif there
is an invertible central element˜c in ˜B of degree 1. Such an element ˜c is called a
uniformizer of ˜B.
Of course if ˜B is a graded ring of Laurent type, then ˜Bi·˜Bj = ˜Bi+j for all
i,j ∈Z. A graded ring with this property is called astrongly graded ring.
The next lemma describes the structure of graded rings of Laurent type. Let
K[t,t−1] be the ring of Laurent polynomials in the degree1 variablet. Given a ring
B (notgraded), wedeﬁnethegradedringofLaurenttype B[t,t−1] :=B⊗KK[t,t−1].
The uniformizer ist, and the degree0 component isB.
Lemma 18.3.2. Let ˜B be a graded ring of Laurent type, with uniformizer˜c, and
deﬁneB := ˜B0, the degree0 subring. Then there is a unique isomorphism of graded
rings B[t,t−1]
≃
− →˜B that is the identity onB, and sendst↦→˜c.
Exercise 18.3.3. Prove Lemma 18.3.2.
Note that for ˜B as in the lemma, there is also a surjective ring homomorphism
˜B→B that sends ˜c↦→1. This is not a graded ring homomorphism.
Recall that given a graded ring˜B, the category of graded˜B-modules isM( ˜B, gr).
For a graded module˜M∈M( ˜B, gr), let us writeDeg0( ˜M) := ˜M0, the homogeneous
component of degree0 of ˜M.
Lemma 18.3.4. Assume ˜B is a graded ring of Laurent type, withB := ˜B0.
(1) The functor Deg0 : M( ˜B, gr)→M(B) is an equivalence of abelian cate-
gories, with quasi-inverseN↦→˜B⊗BN∼=K[t,t−1]⊗N.
(2) There is a bifunctorial isomorphism
Deg0
(
Hom ˜B( ˜M, ˜N)
{≃
− →HomB
(
Deg0( ˜M), Deg0( ˜N)
{
for ˜M, ˜N∈M( ˜B, gr). It sends ˜φ↦→˜φ|Deg0( ˜M).
(3) If the graded ring ˜B is left noetherian, then the ringB is left noetherian,
and the functor Deg0 : Mf( ˜B, gr)→Mf(B) is an equivalence of abelian
categories.
425
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Since Deg0 is exact, it extends to derived categories.
Lemma 18.3.5. Assume ˜B is a graded ring of Laurent type, withB := ˜B0.
(1) For every boundedness condition⋆, the functorDeg0 : D⋆( ˜B, gr)→D⋆(B)
is an equivalence of triangulated categories.
(2) If the graded ring ˜B is left noetherian, thenDeg0 : D⋆
f ( ˜B, gr)→D⋆
f (B) is
an equivalence.
Exercise 18.3.6. Prove Lemmas 18.3.4 and 18.3.5.
Lemma 18.3.7. Let ˜B and ˜C be graded rings, withB := ˜B0 and C := ˜C0. As-
sume ˜B is a graded ring of Laurent type. For˜M, ˜N∈D( ˜B⊗˜Cop, gr) there is an
isomorphism
Deg0
(
RHom ˜B( ˜M, ˜N)
{≃
− →RHomB
(
Deg0( ˜M), Deg0( ˜N)
{
in D(Cen), which is functorial in these complexes.
Proof. Choose a semi-graded-free resolution ˜P →˜M over ˜B⊗˜Cop. Because ˜C
is a graded-freeK-module, it follows that the complex˜P is semi-graded-free over
˜B. Since B = Deg 0( ˜B), the complex Deg0( ˜P ) is semi-free over the ringB; so
Deg0( ˜P )→Deg0( ˜M) is a semi-free resolution overB. We get these isomorphisms:
Deg0
(
RHom ˜B( ˜M, ˜N)
{∼= Deg0
(
Hom ˜B( ˜P, ˜N)
{
∼=†HomB
(
Deg0( ˜P ), Deg0( ˜N)
{∼= RHomB
(
Deg0( ˜M), Deg0( ˜N)
{
in D(Cen). The isomorphism∼=†comes from Lemma 18.3.4(2). □
Lemma 18.3.8.Let ˜B be a graded ring, and let˜c be a central homogeneous element
of ˜B of positive degree. Then the central element˜c−1 is regular in ˜B.
Proof. Take a nonzero element˜b∈˜B, with homogeneous component decomposition
˜b = ˜b1 +···+ ˜br, see (15.1.1). So eitherr = 1 and ˜b = ˜b1 is homogeneous, orr≥2,
and then deg(˜b1) < deg(˜bi) for all 2≤i≤r. Then the homogeneous component
decomposition of ˜b·(˜c−1) is
˜b·(˜c−1) =−˜b1 + (higher degree terms).
The element−˜b1 is nonzero, and therefore˜b·(˜c−1)⁄= 0. □
Derived pseudo-ﬁnite complexes were introduced in Deﬁnition 12.9.1.
Lemma 18.3.9. LetA,B,C be rings; letM1,M 2∈D(A); letN1∈D(B); and let
N2∈D(B⊗C). There is a morphism
θ: RHomA(M1,M 2)⊗RHomB(N1,N 2)→RHomA⊗B(M1⊗N1,M 2⊗N2)
in D(C), which is functorial in these complexes.
IfM1 is derived pseudo-ﬁnite overA,N1 is derived pseudo-ﬁnite overB, and the
complexesM2 andN2 have bounded below cohomologies, thenθis an isomorphism.
Proof. Choose semi-free resolutions P1→M1 and Q1→N1, over A and B re-
spectively. Then P1⊗Q1→M1⊗N1 is a semi-free resolution overA⊗B; see
Proposition 11.4.12. The morphismθis represented by the obvious homomorphism
˜θ: HomA(P1,M 2)⊗HomB(Q1,N 2)→HomA⊗B(P1⊗Q1,M 2⊗N2)
in Cstr(C).
Nowassumethat H(M2)and H(N2)areboundedbelow. Byreplacing M2 andN2
with suitable smart truncations, we can assume these are bounded below complexes.
We ﬁx them.
If P1 and Q1 are pseudo-ﬁnite semi-free, then˜θis an isomorphism inCstr(C),
by the usual calculation; see Lemma 12.9.11.
426
Derived Categories | Amnon Yekutieli | 14 Apr 2019
If we ﬁxN1, then the complexes M1 for which θis an isomorphism form a
saturated full triangulated subcategory ofD(A). Likewise, if we ﬁxM1, then the
complexes N1 for which θis an isomorphism form a saturated full triangulated
subcategory ofD(B). See Proposition 5.3.22. Therefore, as in the proof of Theorem
12.9.10, θis an isomorphism wheneverM1 is derived pseudo-ﬁnite overA and N1
is derived pseudo-ﬁnite overB. □
The inside and outside actions from Subsection 18.2 make sense also in the
graded setting. Here is the ﬁrst main result of this subsection.
Theorem 18.3.10.Let ˜B be a graded ring of Laurent type, withB := ˜B0. Assume
that B is a derived pseudo-ﬁnite complex overBen. Given complexes ˜M, ˜N ∈
D+( ˜Ben, gr), there is an isomorphism
Deg0
(
RHom ˜Ben,out( ˜B, ˜M⊗˜N)
{
≃
− →RHomBen,out
(
B, Deg0( ˜M)⊗Deg0( ˜N)
{
[−1]
in D(Ben,in) = D(Ben), which is functorial in these complexes.
Proof. Say ˜c is a uniformizer of˜B. The ring ˜Ben = ˜B⊗˜Bop is actuallyZ2-graded.
Taking the degree0 component is for the total degree, so the ringDeg0( ˜Ben) retains
aZ-grading, that we shall call thehidden grading. For the hidden grading there is
a graded ring isomorphism
(18.3.11) Ben[s,s−1] =Ben⊗K[s,s−1]
≃
− →Deg0( ˜Ben),
where s is a variable of hidden degree 1, and it goes to the element ˜c⊗˜c−1 ∈
Deg0( ˜Ben).
Similarly for complexes: given ˜M, ˜N∈D( ˜Ben, gr), there is a canonical isomor-
phism
(18.3.12) Deg0( ˜M)⊗Deg0( ˜N)⊗K[s,s−1]
≃
− →Deg0( ˜M⊗˜N)
in D
(
Bfour[s,s−1]
{
. We are neglecting the hidden grading from this stage onward
in the proof.
AccordingtoLemma18.3.7–thatappliesbecause ˜Ben isagradedringofLaurent
type – there is an isomorphism
(18.3.13) Deg0
(
RHom ˜Ben,out( ˜B, ˜M⊗˜N)
{∼= RHomDeg0( ˜Ben,out)
(
B, Deg0( ˜M⊗˜N)
{
in D
(
Deg0( ˜Ben,in)
{
. After applying the restriction functor D
(
Deg0( ˜Ben,in)
{
→
D(Ben,in) = D(Ben), (18.3.13) becomes an isomorphism inD(Ben). We then have
the following isomorphisms inD(Ben) :
(18.3.14)
RHomDeg0( ˜Ben,out)
(
B, Deg0( ˜M⊗˜N)
{
∼=†RHomBen,out⊗K[s,s−1]
(
B⊗K,
(
Deg0( ˜M)⊗Deg0( ˜N)
{
⊗K[s,s−1]
{
∼=‡RHomBen,out
(
B, Deg0( ˜M)⊗Deg0( ˜N)
{
⊗RHomK[s,s−1]
(
K,K[s,s−1]
{
.
The isomorphism∼=†comes from formulas (18.3.11) and (18.3.12). The isomor-
phism∼=‡is by Lemma 18.3.9; it justiﬁed becauseB is a derived pseudo-ﬁnite
complex over Ben, and of course K is a derived pseudo-ﬁnite complex over the
noetherian ringK[s,s−1].
The elements−1∈K[s,s−1] is regular, so we have the Koszul resolution
0→K[s,s−1]
(s−1)·(−)
−−−−−−→K[s,s−1]→K→0.
We use it to calculate
RHomK[s,s−1]
(
K,K[s,s−1]
{∼=K[−1]
427
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(K). Plugging this into (18.3.14) ﬁnishes the proof. □
From here until the end of this subsection we consider a connected graded ring
˜A, with a degree1 central element ˜c∈˜A. Deﬁne the ringA := ˜A/(˜c−1), and the
canonical ring surjectionf : ˜A→A. Of course the ringA is not graded.
Let ˜A˜c be the localization of˜A with respect to˜c, i.e. inverting the homogeneous
multiplicatively closed set{˜ci}i∈N. Because the image of ˜c in ˜A˜c is an invertible
central element of degree1, the graded ring ˜A˜c is a graded ring of Laurent type,
with uniformizer ˜c. We let inc : Deg 0( ˜A˜c) = ( ˜A˜c)0→˜A˜c be the inclusion of the
degree 0 component of ˜A˜c. There is also the ring homomorphismf˜c : ˜A˜c→A,
f˜c(˜c) = 1.
Lemma 18.3.15.
(1) The ring homomorphism
g :=f˜c◦inc : Deg0( ˜A˜c) = ( ˜A˜c)0→A
is an isomorphism.
(2) The ring isomorphismg extends to a graded ring isomorphism˜g : ˜A˜c
≃
− →
A[t,t−1] that sends ˜c↦→t.
The situation is shown in this commutative diagram of rings:
˜A
f
$$ $$// ˜A˜c
f˜c // //A
( ˜A˜c)0
OO
inc
OO
;; g
;; ;;
Proof. In this proof we work with the graded ring of Laurent type˜B := ˜A˜c and its
uniformizer ˜c.
(1) The homomorphismf : ˜A→A is surjective, so every nonzeroa∈A can be
written asa =f(˜b) for some nonzero˜b∈˜A. Consider the homogeneous component
decomposition
(18.3.16) ˜b = ˜b1 +···+ ˜br
of ˜b, as in (15.1.1), withr≥1. Deﬁnea′:= ∑r
i=1
˜bi·˜c−deg(˜bi)∈( ˜A˜c)0. Then
a =g(a′). We see thatg is surjective.
Next we look at
(18.3.17) Ker(g) = Ker(f˜c)∩( ˜A˜c)0⊆( ˜A˜c)0.
The ideal Ker(f˜c) is generated by the central element˜c−1. Consider a nonzero
element ˜b·(˜c−1)∈˜A˜c. Let(18.3.16)bethehomogeneouscomponentdecomposition
of the nonzero element ˜b. Then the homogeneous component decomposition of
˜b·(˜c−1) is ˜b·(˜c−1) = −˜b1 +···+ ˜br·˜c. This is not a homogeneous element,
and hence it cannot lie inside ( ˜A˜c)0. From formula (18.3.17) we conclude that
Ker(g) = 0. Thusg is a ring isomorphism.
(2) Let
(18.3.18) h :A
≃
− →( ˜A˜c)0
be the inverse ofg. It extends to a graded ring homomorphism˜h :A[t,t−1]→˜A˜c,
t↦→˜c. This is an isomorphism, because˜A˜c is a graded ring of Laurent type. The
isomorphism ˜g is the inverse of˜h. □
428
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Exercise 18.3.19. Show that the functorIndf : M( ˜A, gr)→M(A), Indf =A⊗˜A
(−), is exact.
Here is the second main result of the subsection. Connected gradedK-rings were
deﬁned in Deﬁnition 15.2.18.
Theorem 18.3.20. Let ˜A be a noetherian connected graded ring, let˜c∈˜A be a
homogeneous central element of degree1, and letA := ˜A/(˜c−1). Then:
(1) The ringA is noetherian.
(2) There is an isomorphismAen⊗L
˜Aen
˜A∼=A⊕A[1] in D(Aen).
(3) The bimoduleA is a derived pseudo-ﬁnite complex over the ringAen.
Proof.
(1) By Theorem 15.1.28 the ringUngr( ˜A) is noetherian. Since there is a surjection
of rings Ungr( ˜A)→A, it follows thatA is noetherian.
(2) We have these isomorphisms
Aen⊗L
˜Aen
˜A∼=1 A⊗L
˜A
˜A⊗L
˜AA
∼=2 A⊗L
˜AA∼=3 A⊗L
˜A
˜A˜c⊗L
˜A˜c
A∼=4 A⊗L
˜A˜c
A
in D(Aen). The isomorphism∼=1 is a rearrangement of the derived tensor factors.
The isomorphism∼=2 is from the left unitor isomorphism˜A⊗L
˜AA∼=A in D( ˜A⊗Aop).
The isomorphism∼=3 is because the ring homomorphism ˜A→A factors through
˜A˜c, andA∼= ˜A˜c⊗L
˜A˜c
A in D( ˜A⊗Aop). And, ﬁnally, the isomorphism∼=4 is because
A⊗L
˜A
˜A˜c∼=A in D( ˜A⊗˜Aop
˜c )
Now by Lemma 18.3.8 we know that˜c−1 is a regular central element in˜A˜c. So
there is a short exact sequence
(18.3.21) 0→˜A˜c
(˜c−1)·(−)
−−−−−−−→˜A˜c
f˜c
−−→A→0
in M( ˜A˜c⊗Aop). Here ˜A˜c is anAop-module via the ring homomorphismh :A→˜A˜c
from formula (18.3.18). We view the short exact sequence (18.3.21) as a quasi-
isomorphism ˜P→A in Cstr( ˜A˜c⊗Aop), where
˜P :=
(
···→0→˜A˜c
(˜c−1)·(−)
−−−−−−−→˜A˜c→0→···
{
is a complex concentrated in cohomological degrees−1, 0. Because ˜P is semi-free
over ˜A˜c, this allows us to calculate:
A⊗L
˜A˜c
A∼=A⊗˜A˜c
˜P∼=
(
···→0→A
0
−→A→0→···
{∼=A[1]⊕A
in D(Aen).
(3) By Proposition 15.3.24 there is a quasi-isomorphism ˜Q→˜A in Cstr( ˜Aen, gr)
from a nonpositive complex˜Q of ﬁnite graded-free˜Aen-modules. We can forget the
grading now, and just view˜Q→˜A as a free resolution of the module˜A over the
ring ˜Aen. We get P := Aen⊗˜Aen ˜Q∼= Aen⊗L
˜Aen
˜A in D(Aen). The complex P is
pseudo-ﬁnite semi-free overAen. By item (2) the complexA is a direct summand
of P in D(Aen), and hence it is a derived pseudo-ﬁnite complex overAen. □
