---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-075-128-existence-of-dg-ring-resolutions
section_title: "Existence of DG Ring Resolutions"
section_number: 12.8
pages: 240-245
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
DG ring quasi-isomorphismA→B does not change the derived categories: the
restriction functor D(B)→D(A) is an equivalence of triangulated categories.
Sometimes it is advantageous to replace a given DG ring by a quasi-isomorphic
one (see Remarks 12.8.21, 12.8.22, 13.4.24, 14.3.24 and 18.1.30). In this subsection
we studysemi-free DG rings, andsemi-free DG ring resolutions.
As before, we ﬁx a nonzero commutative base ringK. All DG rings are K-
central, namely we work in the categoryDGRng/cK. We use the shorthand “NC”
for “noncommutative”.
Graded sets and ﬁltered graded sets were introduced in Deﬁnitions 11.4.4 and
11.4.6 respectively. The next deﬁnition was mentioned brieﬂy in Example 3.1.23.
Deﬁnition 12.8.1.Let X be a graded set. TheNC polynomial ring onX is the
gradedK-ringK⟨X⟩.
Perhaps we should say a few words on the structure of the ringK⟨X⟩. Given
n≥0 and elements x1,...,xn∈X, their product x1···xn∈K⟨X⟩is called a
monomial (or a word), and its degree is
(12.8.2) deg(x1···xn) := deg(x1) +···+ deg(xn)∈Z.
Forn = 0 the unique monomial is denoted by1. As a gradedK-module, K⟨X⟩is
free, with basis the set of monomials. Multiplication inK⟨X⟩is by concatenation
of monomials, extendedK-bilinearly.
Deﬁnition 12.8.3.Let (X,F ) be a ﬁltered graded set. There is an induced ﬁltra-
tion F =
{
Fj
(
K⟨X⟩
{}
j≥−1 onK⟨X⟩byK-submodules, as follows:
Fj
(
K⟨X⟩
{
:=
{
0 if j =−1
K⟨Fj(X)⟩if j≥0.
For everyj≥0 the ﬁltered pieceFj
(
K⟨X⟩
{
is a graded subring ofK⟨X⟩. And
of courseK⟨X⟩=
jFj
(
K⟨X⟩
{
.
Recall that given a DG ringA, we denote by A♮the graded ring gotten by
forgetting the diﬀerentialdA. Here is the main deﬁnition of this subsection.
Deﬁnition 12.8.4.A NC semi-free DGK-ring is a DGK-ring A that admits an
isomorphism of gradedK-rings A♮∼= K⟨X⟩, for some ﬁltered graded set(X,F ),
such that under this isomorphism there is an inclusiondA
(
Fj(X)
{
⊆Fj−1
(
K⟨X⟩
{
for everyj≥0. Such a ﬁltered graded set(X,F )is called amultiplicative semi-basis
of A.
In this book we are mostly interested in semi-free DG rings because of the propo-
sition below.
Proposition 12.8.5. If A is a NC semi-free DGK-ring, then as a DGK-module
A is semi-free, and hence K-ﬂat.
240
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Suppose we are given an isomorphismA♮∼=K⟨X⟩for some ﬁltered graded
set (X,F ), as in Deﬁnition 12.8.4. LetY be the set of monomials in the elements
of X. The setY is graded, see (12.8.2), and it forms a basis ofA♮as a gradedK-
module. However, sinceX could have elements of positive degree, this is not enough
to makeA into a semi-free DGK-module; we need to put a suitable ﬁltration on
Y. Cf. Proposition 11.4.8.
For an element x ∈X let ordF (x) := min {j |x ∈Fj(X)} ∈N. Thus
Fj(X) = {x∈X |ordF (x)≤j}. We extend this order function to monomials
by ordF (x1···xn) := ∑
i ordF (xi). The element 1 (the monomial of length 0)
gets order 0. Then we deﬁneGj(Y ) :={y∈Y |ordF (y)≤j}. This is a ﬁltration
G ={Gj(Y )}j≥−1 of the graded setY, and it induces a ﬁltrationG ={Gj(A)}j≥−1
on A by K-submodules, where Gj(A)⊆A is deﬁned to be theK-linear span of
Gj(Y ).
The graded Leibniz rule, together with the inclusion dA(Fj(X)) ⊆
Fj−1(K⟨X⟩) from Deﬁnition 12.8.4, imply thatdA(Gj(A))⊆Gj−1(A) for every
j ≥0. And GrG
j (A) is a free DGK-module, with basis GrG
j (Y ) := {y ∈Y |
ordF (y) =j}. ThusG is a semi-free ﬁltration on the DGK-module A, andA is a
semi-free DGK-module; see Deﬁnition 11.4.3.
Finally, according to Theorem 11.4.14 and Proposition 10.3.4,A is a K-ﬂat DG
K-module. □
Deﬁnition 12.8.6.LetA be a DGK-ring. A NC semi-free DG ring resolutionof
A relative toK is a quasi-isomorphismu : ˜A→A of DGK-rings, where ˜A is a NC
semi-free DGK-ring. We also callu : ˜A→A a NC semi-free resolution ofA in
DGRng/cK.
The important result of this subsection is the next existence theorem.
Theorem 12.8.7. Let A be a DGK-ring. There exists a NC semi-free DG ring
resolutionu : ˜A→A of A relative toK.
The proof of the theorem comes after two lemmas. IfX and Y are graded sets,
a degree i function f : X →Y is a function such thatf(Xj)⊆Yj+i for all j.
Likewise, a degreei functionf :X→B to a graded ringB is a function such that
f(Xj)⊆Bj+i for allj.
Lemma 12.8.8.LetX be a graded set, and consider the gradedK-ringB :=K⟨X⟩.
Suppose dX :X→B is a degree1 function.
(1) The function dX extends uniquely to aK-linear degree 1 derivation dB :
B→B.
(2) The derivation dB is a diﬀerential onB, i.e. dB◦dB = 0, if and only if
dB(dX((x)) = 0 for everyx∈X.
Proof.
(1) For elementsx1,...,xn∈X, withkj := deg(xj), deﬁne
(12.8.9) dB(x1···xn) :=
n
j=1
(−1)k1+···+kj−1·x1···xj−1·dX(xj)·xj+1···xn.
This extends uniquely to aK-linear homomorphism dB : B→B of degree 1. A
calculation shows that the graded Leibniz rule holds, so this is degree1 derivation.
(2) It is enough to verify thatdB◦dB = 0 on monomials. This is an elementary
calculation, using formula (12.8.9). □
Lemma 12.8.10. LetB,C ∈DGRng/cK. Assume thatB is NC semi-free, with a
multiplicative semi-basis(X,F ). Letw :X→C be a degree0 function.
241
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) The function w extends uniquely to a gradedK-ring homomorphism w :
B♮→C♮.
(2) The graded ring homomorphismw becomes a DG ring homomorphismw :
B→C if and only ifdC(w(x)) =w(dB(x)) for everyx∈X.
Proof. Item (1) is clear. As for item (2), it is enough to verify thatdC◦w =w◦dB
on monomials x1···xn ∈B. This is done by induction on n, using the graded
Leibniz rule. □
Proof of Theorem12.8.7. The strategy is this: we are going to construct an in-
creasing sequence of semi-free DG rings
(12.8.11) F0( ˜A)⊆F1( ˜A)⊆F2( ˜A)⊆···,
together with a compatible system of DG ring homomorphisms Fj(u) :
Fj( ˜A)→A. At the same time we will construct an increasing sequence of graded
sets
(12.8.12) ∅ =F−1(X)⊆F0(X)⊆F1(X)⊆F2(X)⊆···,
such that there is equality of graded ringsFj( ˜A)♮=K⟨Fj(X)⟩for everyj≥0.
Then we will deﬁne the DG ring
(12.8.13) ˜A := lim
j→
Fj( ˜A),
the DG ring homomorphism
(12.8.14) u := lim
j→
Fj(u) : ˜A→A,
and the graded set
(12.8.15) X := lim
j→
Fj(X).
The graded setX is ﬁltered byF :=
{
Fj(X)
}
j≥−1. By the construction (X,F )
will be a multiplicative semi-basis of˜A, so that the latter is a semi-free DG ring.
The construction will also ensure thatu is a quasi-isomorphism. All this will be
done in several steps.
Step 1. In this step we deal withj = 0. Let’s choose a collection{¯ax}x∈F0(X) of
nonzero homogeneous elements of H(A) that generates it as aK-ring. We make
F0(X) into a graded set by declaringdeg(x) := deg(¯ax) for x∈F0(X). Next, for
eachx we choose a homogeneous cocycleax∈Z(A) that represents the cohomology
class ¯ax. In this way we obtain a degree0 functionF0(u) :F0(X)→A,F0(u)(x) :=
ax.
Deﬁne the DG ringF0( ˜A) := K⟨F0(X)⟩, with zero diﬀerential. According to
Lemma 12.8.10 the functionF0(u) : F0(X)→A extends uniquely to a DG ring
homomorphism F0(u) : F0( ˜A) →A. The choice of the collection {¯ax}x∈F0(X)
guarantees that the gradedK-ring homomorphismH(F0(u)) : H(F0( ˜A))→H(A) is
surjective.
Step 2. In this step and the next one we deal with the induction. Let j ≥0.
The assumption is that we have a semi-free DG ringFj( ˜A), with a multiplicative
semi-basis
(12.8.16) ∅ =F−1(X)⊆F0(X)⊆···⊆Fj−1(X)⊆Fj(X)⊆Fj(X)⊆···
(constant from levelj onward), and a DG ring homomorphismFj(u) :Fj( ˜A)→A
such that the graded ring homomorphismH(Fj(u)) : H(Fj( ˜A))→H(A) is surjec-
tive.
242
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁne the graded two-sided idealKj := Ker
(
H(Fj(u))
{
⊆H(Fj( ˜A)). So there
is an exact sequence of gradedH(Fj( ˜A))-bimodules
(12.8.17) 0→Kj→H(Fj( ˜A))
H(Fj(u))
−−−−−−→H(A)→0.
Choose a collection{¯ay}y∈Yj+1 of nonzero homogeneous elements ofKj that gen-
erates it as anH(Fj( ˜A))-bimodule (i.e. as a two-sided ideal). We makeYj+1 into a
graded set by declaringdeg(y) := deg(¯ay)−1 fory∈Yj+1. Next, for each element
y∈Yj+1 we choose a homogeneous cocycleay∈Z
(
Fj( ˜A)
{
that represents the co-
homology class ¯ay. In this way we obtain a collection{ay}y∈Yj+1 of homogeneous
cocycles inFj( ˜A).
Deﬁne the graded set Fj+1(X) := Fj(X)⊔Yj+1 and the graded ring
Fj+1( ˜A)♮:= K⟨Fj+1(X)⟩. By deﬁnitionFj( ˜A)♮is a graded subring ofFj+1( ˜A)♮.
Next, deﬁne the degree1 function dFj+1(X) :Fj+1(X)→Fj+1( ˜A) by the formula
dFj+1(X)(x) :=
{
dFj( ˜A)(x) if x∈Fj(X)
ax if x∈Yj+1.
In this formula we are using the collection of homogeneous cocycles{ay}y∈Yj+1 that
has been chosen above. According to Lemma 12.8.8 the functiondFj+1(X) extends
uniquely to a diﬀerential onFj+1( ˜A), making it into a DG ring. And of course
Fj( ˜A)⊆Fj+1( ˜A) is a DG subring.
Let us denote byvj : Fj( ˜A)→Fj+1( ˜A) the inclusion. Because the cocycles
ay∈Fj( ˜A), fory∈Yj+1, become coboundaries inFj+1( ˜A), we see that
(12.8.18) Kj⊆Ker(H(vj))⊆H(Fj( ˜A)).
Observe that the DG ringFj+1( ˜A) is semi-free, with multiplicative semi-basis
∅ =F−1(X)⊆F0(X)⊆···⊆Fj(X)⊆Fj+1(X)⊆Fj+1(X)⊆···,
constant from levelj + 1 onward.
Step 3. In this step we continue step 2, to construct the DG ring homomor-
phism Fj+1(u) : Fj+1( ˜A)→A. For each elementy∈Yj+1 the cohomology class
¯ay ∈H(Fj( ˜A)) belongs to the kernel of H(Fj(u)). This means that the cocycle
Fj(u)(ay)∈A is a coboundary. So we can ﬁnd a homogeneous elementby∈A such
that dA(by) = Fj(u)(ay). Deﬁne the degree0 function Fj+1(u) : Fj+1(X)→A by
the formula
Fj+1(u)(x) :=
{
Fj(u)(x) if x∈Fj(X)
bx if x∈Yj+1.
By Lemma 12.8.10 this function extends uniquely to a DG ring homomorphism
Fj+1(u) : Fj+1( ˜A)→A. Note that the restriction ofFj+1(u) to Fj( ˜A) coincides
with Fj(u).
Step 4. Applying steps 2-3 recursively, we obtain direct systems{Fj( ˜A)}j≥0 and
{Fj(u)}j≥0 of DG rings and homomorphisms, and we can deﬁne the DG ring˜A by
formula (12.8.13), and the DG ring homomorphism˜u by formula (12.8.14). The
graded setX from formula (12.8.15) is ﬁltered, and by the construction in steps 1
and 2 the ﬁltered graded set(X,F ) is a multiplicative semi-basis of˜A.
It remains to prove that the graded ring homomorphismH(u) : H( ˜A)→H(A)
is bijective. Recall that for eachj≥0 we denoted byvj the inclusion Fj( ˜A)⊆
243
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Fj+1( ˜A). Deﬁne the graded ringLj := Im(H(vj))⊆H(Fj+1( ˜A)). We get a com-
mutative diagram
0 // Kj // inc // H(Fj( ˜A))
H(Fj(u)) // //
αj

H(vj)

H(A) // 0
Lj

inc

βj
88 88
H(Fj+1( ˜A))
H(Fj+1(u))
KKKK
in Gstr(K). The top row is an exact sequence (it is (12.8.17)). Because αj is
surjective, thereisequality Ker(βj) =αj
(
Ker(H(Fj(u))
{
=αj(Kj). Butbyformula
(12.8.18) we know thatαj(Kj) = 0 . The conclusion is that βj : Lj →H(A) is
bijective. Hence{Lj}j≥0 is a constant direct system, andlimj→βj : limj→Lj→
H(A) is bijective.
Now the direct systems{Lj}j≥0 and
{
H(Fj( ˜A))
}
j≥0 are sandwiched. Therefore
the second direct system has a limit too, and it is the same limit; i.e.
lim
j→
H(Fj(u)) : lim
j→
H(Fj( ˜A))→H(A)
is bijective. Because cohomology commutes with direct limits, and by formula
(12.8.13), this implies thatH(u) is bijective. □
Exercise 12.8.19. Modify the proof of Theorem 12.8.7 to make the quasi-iso-
morphism u : ˜A→A surjective.
Corollary 12.8.20. If H(A) is nonpositive, thenA has a semi-free DG ring reso-
lution ˜A→A such that ˜A is nonpositive.
Proof. Under this assumption, the graded setX in the proof of Theorem 12.8.7 is
nonpositive. □
Remark 12.8.21.NC semi-free DG rings have important lifting properties within
DGRng/cK. V. Hinich, in [66], calls themstandard coﬁbrant objectsof the Quillen
model structure onDGRng/cK.
One can also consider the full subcategoryDGRng≤0/cK of nonpositive NC DG
rings. NC nonpositive semi-free DG rings are studied in detail in [173]. This is done
in a slightly more general context: the base ringK is allowed to be a commutative
DG ring (see next remark), andK→A is a central homomorphism of DG rings
(i.e. the image ofK is in Cent(A)). The lifting properties are the same.
See Remark 6.2.38 for the relatedA∞theory.
Remark 12.8.22. There are alsocommutative semi-free DG rings. Recall that a
commutative DG ring in this book means nonpositive and strongly commutative;
see Deﬁnitions 3.1.22 and 3.3.4. The commutative DG rings form the category
DGRng≤0
sc /K, which is a full subcategory ofDGRng/cK.
A nonpositive graded setS gives rise to the commutative polynomial ringK[S],
see Example 3.1.23. A commutative DG ring˜A is called commutative semi-free if
it admits a graded ring isomorphism˜A♮∼=K[S] for some nonpositive graded setS.
The graded setS is automatically ﬁltered by degree, namelyFj(S) := 
i≥−jSi.
This implies (cf. Proposition 12.8.5) that˜A is semi-free as a DGK-module .
In [173] it is proved that every A ∈DGRng≤0
sc /K admits a surjective quasi-
isomorphism ˜A→Afromacommutativesemi-freeDGring ˜A. Itisalsoprovedthat
244
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the commutative semi-free DG rings have good lifting properties inDGRng≤0
sc /K.
The situation studied in [173] is a bit more general: the base ringK is allowed to
be itself a commutative DG ring; so the theory becomes relative.
IfinExample6.2.35wetakethe topologicalspace X tobeasinglepoint, thenthe
category DGRng≤0
sc /KX discussed there coincides withDGRng≤0
sc /K, and the semi-
pseudo-free DGKX-rings are just the semi-free commutative DG rings mentioned
here.
Unlike the geometric setting, the categoryDGRng≤0
sc /K admits a Quillen model
structure (at least whenK containsQ), and the calculus of fractions for the derived
category D(DGRng≤0
sc /K) can be deduced from it.
The fully faithful embedding
DGRng≤0
sc /K→DGRng≤0/cK
induces a functor
D(DGRng≤0
sc /K)→D(DGRng≤0/cK)
between the derived categories, which presumably is neither full nor faithful (but
we did not explore this question seriously).
