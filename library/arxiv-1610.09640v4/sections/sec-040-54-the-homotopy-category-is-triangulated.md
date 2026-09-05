---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-040-54-the-homotopy-category-is-triangulated
section_title: "The Homotopy Category is Triangulated"
section_number: 5.4
pages: 102-109
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
aK-linear abelian categoryM and a DG centralK-ring A, whereK is the commu-
tative base ring. These ingredients give rise to theK-linear DG categoryC(A, M)
of DGA-modules in M, as in Subsection 3.8.
The strict category Cstr(A, M) and the homotopy category K(A, M) were in-
troduced in Deﬁnition 3.8.5. Recall that theseK-linear categories have the same
objects as C(A, M). The morphismK-modules are
HomCstr(A,M)(M0,M 1) = Z0(
HomC(A,M)(M0,M 1)
{
and
HomK(A,M)(M0,M 1) = H0(
HomC(A,M)(M0,M 1)
{
.
There is a full additive functorP : Cstr(A, M)→K(A, M) which is the identity
on objects, and on morphisms it sends a homomorphism to its homotopy class.
Morphisms in K(A, M) will often by decorated with a bar, like¯φ.
Consider the translation functorT from Deﬁnition 4.1.9. SinceT is a DG functor
from C(A, M) to itself (see Corollary 4.1.10), it restricts to a linear functor from
Cstr(A, M) to itself, and it induces a linear functor¯T from K(A, M) to itself, such
that P◦T = ¯T◦P.
Proposition 5.4.1.
(1) The category Cstr(A, M), equipped with the translation functorT, is a T-
additive category.
102
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(2) The category K(A, M), equipped with the translation functor ¯T, is a T-
additive category.
(3) Letτ: P◦T
≃
− →¯T◦P be the identity automorphism. Then the pair
(P,τ) : Cstr(A, M)→K(A, M)
is a T-additive functor.
Proof. (1) We need to prove thatCstr(A, M) is additive. Of course the zero complex
is a zero object. Next we consider ﬁnite direct sums. LetM1,...,Mr be a ﬁnite
collection of objects inC(A, M). Each Mi is a DGA-module in M, and we write
it as Mi ={Mj
i}j∈Z. In each degree j the direct sum Mj := ⨁r
i=1Mj
i exists
in M. Let M :={Mj}j∈Z be the resulting graded object inM. The diﬀerential
dM : Mj→Mj+1 exists by the universal property of direct sums; so we obtain a
complex M∈C(M). The DG A-module structure onM is deﬁned similarly: for
a∈Ak, there is an induced degreek morphism f(a) : M →M in C(M). Thus
M becomes an object of C(A, M). But the embeddings ei : Mi→M are strict
morphisms, so (M,{ei}) is a coproduct of the collection{Mi}in Cstr(A, M).
(2) Now consider the category K(A, M). Because the functor P : Cstr(A, M)→
K(A, M) is additive, and is bijective on objects, part (1) above and Proposition
2.5.2 say thatK(A, M) is an additive category.
(3) Clear. □
From now on we denote byT, instead of by¯T, the translation functor ofK(A, M).
Deﬁnition 5.4.2.A triangle
L
¯α
− →M
¯β
− →N
¯γ
− →T(L)
in K(A, M) is said to be adistinguished triangleif there is a standard triangle
L′α′
−→M′β′
−→N′γ′
−→T(L′)
in Cstr(A, M), as in Deﬁnition 4.2.5, and an isomorphism of triangles
L′P(α′) //
¯φ

M′P(β′) //
¯ψ

N′ P(γ′) //
¯χ

T(L′)
T(¯φ)

L ¯α //M
¯β //N
¯γ // T(L) .
in K(A, M).
Theorem 5.4.3. The T-additive category K(A, M), with the set of distinguished
triangles deﬁned above, is a triangulated category.
The proof is after three lemmas.
Lemma 5.4.4.LetM∈C(A, M), and consider the standard coneN := Cone(idM).
Then the DG module N is null-homotopic, i.e. 0 →N is an isomorphism in
K(A, M).
Proof. We shall exhibit a homotopyθfrom 0N to idN. Recall from Subsection
4.2 that N = Cone(idM) = M⊕T(M) =

M
T(M)

as graded modules, with a
diﬀerential whose matrix presentation isdN =

dM t−1
M
0 d T(M)

. And by the deﬁnition
in Subsection 4.1 we have dT(M) =−tM◦dM◦t−1
M . Deﬁneθ: N →N to be
103
Derived Categories | Amnon Yekutieli | 14 Apr 2019
the degree−1 morphism with matrix presentationθ:=

0 0
tM 0

. Then, using the
formulas above fordN and dT(M), we get
dN◦θ+θ◦dN =
idM 0
0 id T(M)

= idN. □
Exercise 5.4.5. Here is a generalization of Lemma 5.4.4. Consider a morphism
φ:M0→M1 in Cstr(A, M). Show that the three conditions below are equivalent:
(i) φis a homotopy equivalence.
(ii) ¯φis an isomorphism inK(A, M).
(iii) The DG moduleCone(φ) is null-homotopic.
Try to do this directly, not using Proposition 5.2.7(2) and Theorem 5.4.3.
The next lemma is based on [75, Lemma 1.4.2].
Lemma 5.4.6. Consider a morphism α: L→M in Cstr(A, M), the standard
triangle L
α
− →M
β
− →N
γ
− →T(L) built onα, and the standard triangleM
β
− →N
φ
− →
P
ψ
− →T(M) built on β, all in Cstr(A, M). So N = Cone(α) and P = Cone(β).
There is a morphism ρ: T(L)→P in Cstr(A, M) s.t. ¯ρis an isomorphism in
K(A, M), and the diagram
M
¯β //
idM

N
¯γ //
idN

T(L)
−T(¯α) //
¯ρ

T(M)
idT(M)

M
¯β //N
¯φ //P
¯ψ // T(M)
commutes in K(A, M).
Proof. Note that N = M⊕T(L) and P = N⊕T(M) = M⊕T(L)⊕T(M) as
graded modules. ThusP and dP have the following matrix presentations:
P =
)
]
M
T(L)
T(M)

[ , dP =
)
]
dM α◦t−1
L t−1
M
0 d T(L) 0
0 0 d T(M)

[ .
Deﬁne morphismsρ: T(L)→P and χ: P →T(L) in Cstr(A, M) by the matrix
presentations
ρ:=
)

0
idT(L)
−T(α)

[ , χ:=
0 id T(L) 0
.
Direct calculations show that χ◦ρ= id T(L), ρ◦γ= ρ◦χ◦φand ψ◦ρ=
−T(α).
It remains to prove thatρ◦χis homotopic toidP. Deﬁne a degree−1 morphism
θ:P→P by the matrix
θ:=
)

0 0 0
0 0 0
tM 0 0

[.
Then a direct calculation, using the equalities tM◦dM + dT(M)◦tM = 0 and
T(α) = tM◦α◦t−1
L givesθ◦dP + dP◦θ= idP−ρ◦χ. □
Lemma 5.4.7.Consider a standard triangleL
α
− →M
β
− →N
γ
− →T(L) in Cstr(A, M).
For every integerk, the triangle
Tk(L)
Tk(α)
−−−−→Tk(M)
Tk(β)
−−−−→Tk(N)
(−1)k·Tk(γ)
−−−−−−−−−→Tk+1(L)
is isomorphic, inCstr(A, M), to a standard triangle.
104
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Combine Corollary 4.1.10, Corollary 4.5.6 withF = T, and Proposition
4.4.4. □
Proof of Theorem5.4.3. We essentially follow the proof of [75, Proposition 1.4.4],
adding some details.
(TR1): By deﬁnition the set of distinguished triangles inK(A, M) is closed under
isomorphisms. This establishes item (a).
As for item (b): consider any morphism¯α:L→M in K(A, M). It is represented
by a morphismα: L→M in Cstr(A, M). Take the standard triangle on αin
Cstr(A, M). Its image inK(A, M) has the desired property.
Finally, Lemma 5.4.4 shows that the triangle M
idM
−−→M →0 →T(M) is
isomorphic in K(A, M) to the triangleM
idM
−−→M
¯e
− →Cone(idM)
¯p
− →T(M). The
latter is the image of a standard triangle, and so it is distinguished.
(TR2): Consider the triangles
(5.4.8) L
¯α
− →M
¯β
− →N
¯γ
− →T(L)
and
(5.4.9) M
¯β
− →N
¯γ
− →T(L)
−T(¯α)
−−−−→T(M)
in K(A, M). If (5.4.8) is distinguished, then by Lemma 5.4.6 so is (5.4.9).
Conversely, if (5.4.9) is distinguished, then by turning it5 times, and using the
previous step (namely by Lemma 5.4.6), we see that the triangle
T2(L)
T2(¯α)
−−−−→T2(M)
T2(¯β)
− −−− →T2(N)
T2(¯γ)
− −−− →T3(L)
is distinguished. According to Lemma 5.4.7 (withk =−2), the triangle gotten by
applying T−2 to this is distinguished. But this is just the triangle (5.4.8).
(TR3): Consider a commutative diagram inK(A, M) :
(5.4.10) ¯L ¯α //
¯φ

¯M
¯β //
¯ψ

¯N
¯γ // T(¯L)
¯L′ ¯α′
// ¯M′ ¯β′
// ¯N′ ¯γ′
// T(¯L′)
where the horizontal triangles are distinguished. By deﬁnition the rows in (5.4.10)
are isomorphic inK(A, M)to the images under the functorPof standard triangles in
Cstr(A, M). These are the rows in diagram (5.4.11) below. The vertical morphisms
in (5.4.10) are also induced from morphisms inCstr(A, M), i.e. ¯φ= P(φ) and ¯ψ=
P(ψ). Thus (5.4.10) is isomorphic to the image underP of the following diagram:
(5.4.11) L α //
φ

M
β //
ψ

N
γ // T(L)
L′ α′
//M′ β′
//N′ γ′
// T(L′)
Warning: the diagram (5.4.11) is only commutative up to homotopy inCstr(A, M).
Since the rows in (5.4.11) are standard triangles (see Deﬁnition 4.2.5), the objects
N and N′are cones:N = Cone(α) and N′= Cone(α′). The commutativity up to
homotopy of this diagram means that there is a degree−1 morphism θ:L→M′
in C(A, M) such thatα′◦φ=ψ◦α+ d(θ).
105
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁne the morphismχ:N =

M
T(L)

→N′=

M′
T(L′)

by the matrix presenta-
tion
χ:=
)
ψ θ◦t−1
L
0 T( φ)
[
.
An easy calculation shows thatχis a morphism inCstr(A, M), and that there are
equalities T(φ)◦γ=γ′◦χandχ◦β=β′◦ψ. Therefore, when we apply the functor
P, and conjugate by the original isomorphism between (5.4.10) and the image of
(5.4.11), we obtain a commutative diagram
¯L ¯α //
¯φ

¯M
¯β //
¯ψ

¯N
¯γ //
¯χ

T(¯L)
T(¯φ)

¯L′ ¯α′
// ¯M′ ¯β′
// ¯N′ ¯γ′
// T(¯L′)
in K(A, M), where ¯χis conjugate toP(χ).
(TR4): We may assume that the three given distinguished triangles are standard
triangles in Cstr(A, M). Namely, we can assume thatα:L→M and β:M→N
are morphisms in Cstr(A, M); the DG modules P,Q,R are P = Cone(α), Q =
Cone(β◦α) and R = Cone(β); and the morphismsγ,δ,ϵin Cstr(A, M) are γ=eα,
δ=eβ◦αand ϵ=eβ. All this in the notation of Subsection 4.2.
In matrix notation we have
P =
M
T(L)

, Q =
N
T(L)

, R =
N
T(M)

.
We deﬁne the morphismsφ: P→Q and ψ: Q→R in Cstr(A, M) by the matrix
presentations
φ:=
β 0
0 id T(L)

, ψ :=
idN 0
0 T( α)

.
(We leave to the reader to verify thatφand ψcommute with the diﬀerentials
dP, dQ and dR; this is just linear algebra, using the matrix presentations of the
diﬀerentials of the cones from Deﬁnition 4.2.1.) Deﬁne the morphismρ:R→T(Q)
in Cstr(A, M)tobethecompositionofthemorphisms R→T(M)
T(γ)
−−−→T(Q). Then
the diagram (5.1.11) inCstr(A, M) is commutative.
It remains to prove that the triangle
(5.4.12) P
¯φ
− →Q
¯ψ
− →R
¯ρ
− →T(P )
in K(A, M) is distinguished. LetC := Cone(φ); so we have a standard triangle
(5.4.13) P
φ
− →Q
eφ
−→C
pφ
−→T(P )
in Cstr(A, M). We are going to prove that the triangles (5.4.12) and (5.4.13) are
isomorphic in K(A, M), by producing an isomorphism¯χ:C
≃
− →R in K(A, M) that
makes the diagram
P
¯φ //
id

Q
¯eφ //
id

C
¯pφ //
¯χ

T(P )
id

P
¯φ //Q
¯ψ //R
¯ρ // T(P )
commutative.
106
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Here are the matrices for the objectC, the morphismχ:C→R, and another
morphism ω:R→C, both inCstr(A, M).
C =
)
]]]
N
T(L)
T(M)
T2(L)

[, χ:=
idN 0 0 0
0 T( α) id T(M) 0

, ω :=
)
]]
idN 0
0 0
0 id T(M)
0 0

[.
Again, we leave it to the reader to check thatχand ωcommute with the diﬀeren-
tials. It is easy to see thatω◦ψ=eφ, ρ◦χ=pφand χ◦ω= idR.
Finally we must ﬁnd a homotopy betweenω◦χand idC. Consider the degree
−1 endomorphism θof C :
θ:=
)
]]
0 0 0 0
0 0 0 0
0 0 0 0
0 t T(L) 0 0

[.
Then dC◦θ+θ◦dC = idC−ω◦χ. □
A full subcategory of a DG category is of course a DG category itself. Full ad-
ditive (resp. triangulated) subcategories of additive (resp. triangulated) categories
were deﬁned in Deﬁnition 2.2.6 (resp. 5.2.2).
Corollary 5.4.14. Let C⊆C(A, M) be a full subcategory satisfying these three
conditions:
(a) Cstr is a full additive subcategory ofCstr(A, M).
(b) C is translation invariant, i.e.M∈C if and onlyT(M)∈C.
(c) C is closed under standard cones, i.e. for every morphismφin Cstr the
object Cone(φ) belongs to C.
Then K := Ho(C) is a full triangulated subcategory ofK(A, M).
Proof. EachconditionhereimpliesthesamenumberedconditioninDeﬁnition5.2.2.
□
Here is a partial converse to the corollary.
Proposition 5.4.15. Suppose K⊆K(A, M) is a full triangulated subcategory. Let
C⊆C(A, M) be the full subcategory on the set of objectsOb(K). Then the DG
category C satisﬁes conditions(a)-(c) of Corollary 5.4.14, and K = Ho(C).
Exercise 5.4.16. Prove Proposition 5.4.15.
Here are two remarks about other sorts of triangulated categories.
Remark 5.4.17. Let E be an exact category in the sense of D. Quillen [122].
Assume that E is a Frobenius category, i.e. E has enough injectives and enough
projectives, and an object is injective if and only if it is projective. Thestable
category of E is the quotient categoryE := E/ E0, where E0⊆E is the two-sided
ideal of morphisms factoring through a projective object. The set of objects ofE is
the same as that ofE. D. Happel [58] has shown thatE is a triangulated category.
By deﬁnition, analgebraic triangulated categoryis a triangulated category K
which is equivalent to the stable categoryE of some Frobenius categoryE. It turns
out that all the derived categories studied in this book (see Section 7) are in fact
algebraic triangulated categories; see the paper [78] of B. Keller.
Here are a couple of other examples of algebraic triangulated categories. LetM
be an additive category, and letE := Cstr(M), the strict category of complexes inM.
Put on E the exact structure in which the short exact sequences are the degreewise
split sequences. Then E becomes a Frobenius category; the projective-injective
107
Derived Categories | Amnon Yekutieli | 14 Apr 2019
objects in it are the contractible complexes. In this case the idealE0 coincides with
the null-homotopic morphisms inE = Cstr(M), and henceE = K(M), the homotopy
category of M.
For the second example, suppose thatK is a ﬁeld andA a noetherianK-ring
which is Gorenstein, i.e.Ahas ﬁnite injective dimension as a left and as a right mod-
ule over itself. The category of ﬁnitely generatedA-modules is Mf(A) = ModfA.
Let E⊆Mf(A)bethefullsubcategoryonthemodules M suchthat Exti
A(M,A ) = 0
for alli> 0. These modules are sometimes calledmaximal Cohen-Macaulay mod-
ules. Put on E the exact structure in which the exact sequences are the exact
sequences in Mf(A) with all terms belonging to E. Then E is a Frobenius cate-
gory. The projective-injective objects ofE are the modules in it that are projective
A-modules. Moreover, according to R.-O. Buchweitz [34], the triangulated cate-
gory E in this case is equivalent to thestable derived categoryof A, which is the
Verdier quotientDb
f (A)/D(A)perf. Here Db
f (A) is the derived category of bounded
complexes with ﬁnitely generated cohomologies (see subsection 7.4),D(A)perf is the
fullsubcategoryontheperfectcomplexes(seeSection14), andVerdierquotientsare
explained in Remark 7.1.14. Note that the triangulated categoryDb
f (A)/D(A)perf
is called thetriangulated category of singularitiesby D.O. Orlov [117], and this was
later shortened to thesingularity categoryof A.
Remark 5.4.18. In 1961, A. Dold and D. Puppe [44] tried to formalize the prop-
erties of the stable homotopy category of topological spaces. What they got is a
theory almost identical to the theory of triangulated categories studied here (Deﬁ-
nition 5.1.10), with the exception of the octahedral axiom (TR4).
In more modern terms we can consider the notion of astable model category, that
we now deﬁne. LetC be a pointed Quillen model category, meaning that it has a
zero object. One deﬁnes asuspension functor Σ and aloop functor Ω on C using
pushout and pullback diagrams involving the zero object. LetD be thehomotopy
category of C. (In the terminology of our book,D is actually thederived category
of C, because it is gotten by inverting the weak equivalences inC; see Sections 6-8.)
If the functorsΣ and Ω induce auto-equivalences onD, quasi-inverse to each other,
then C is called a stable model category. In this case it can be shown thatD is a
triangulated category, with translation functorT := Σ . A more general notion is
that of astable inﬁnity category(see [100] or [67]).
A topological triangulated categoryis, by deﬁnition, a triangulated categoryK
which is equivalent to a full triangulated subcategory of the homotopy categoryD
of a stable model categoryC, as above. For more information on these topics see
[68], [135], [136], [100] and [38].
108
Derived Categories | Amnon Yekutieli | 14 Apr 2019
