---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-041-55-from-dg-functors-to-triangulated-functors
section_title: "From DG Functors to Triangulated Functors"
section_number: 5.5
pages: 109-110
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
DG ring B, and a second abelian category N. DG functors were introduced in
Subsection 3.5.
Consider a DG functorF : C(A, M)→C(B, N). From Theorem 4.4.3 we know
that the translation isomorphismτF is an isomorphism of DG functorsτF : F◦
TA,M
≃
− →TB,N◦F. Therefore, when we pass to the homotopy categories, and
writing ¯F := Ho(F ) and ¯τF := Ho(τF ), we get a T-additive functor ( ¯F, ¯τF ) :
K(A, M)→K(B, N).
If G : C(A, M)→C(B, N) is another DG functor, then we have another T-
additive functor ( ¯G, ¯τG) : K(A, M) →K(B, N). And if η: F →G is a strict
morphism of DG functors, then there is a morphism of additive functors ¯η:=
Ho(η) : ¯F→¯G. This notation will be used in the next theorem.
Theorem 5.5.1.LetA andB be DG rings, letM and N be abelian categories, and
let F : C(A, M)→C(B, N) be a DG functor.
(1) The T-additive functor
( ¯F, ¯τF ) : K(A, M)→K(B, N)
is a triangulated functor.
(2) SupposeG : C(A, M)→C(B, N) is another DG functor, andη:F→G is
a strict morphism of DG functors. Then
¯η: ( ¯F, ¯τF )→( ¯G, ¯τG)
is a morphism of triangulated functors.
Proof.
(1) Take a distinguished triangleL
¯α
− →M
¯β
− →N
¯γ
− →T(L) in K(A, M). Since we
are only interested in triangles up to isomorphism, we can assume that this is
the image under the functorP of a standard triangleL
α
− →M
β
− →N
γ
− →T(L) in
Cstr(A, M). According to Theorem 4.5.5 and Corollary 4.5.6, there is a standard
triangle L′α′
−→M′β′
−→N′γ′
−→T(L′) in Cstr(B, N), and a commutative diagram
F (L)
F(α) //
φ

F (M)
F(β) //
ψ

F (N)
τF,L◦F(γ) //
χ

T(F (L))
T(φ)

L′ α′
//M′ β′
//N′ γ′
// T(L′)
in Cstr(B, N), in which the vertical arrows are isomorphisms. (Actually, we can
takeL′=F (L),φ= idF(L), etc.) After applying the functorP to this diagram, we
see that the condition in Deﬁnition 5.2.1(1) is satisﬁed.
(2) By Deﬁnition 5.2.1(2), all we need to prove that¯ηis a morphism of T-additive
functors. Let’s use these abbreviations:K := K(A, M) and L := K(B, N). Deﬁnition
5.1.5 requires that for every objectM∈K the diagram
(5.5.2) ¯F (TK(M))
¯τF,M //
¯ηTK(M)

TL( ¯F (M))
TL(¯ηM)

¯G(TK(M))
¯τG,M // TL( ¯G(M)) .
in Liscommutative. GoingbacktoDeﬁnitions4.1.6and4.4.1weseethat TL(ηM) =
tG(M)◦ηM◦t−1
F(M), τF,M = tF(M)◦F (t−1
M ) and τG,M = tG(M)◦G(t−1
M ), as mor-
phisms inC(B, N). Thus the path in (5.5.2) that starts by going right is represented
109
Derived Categories | Amnon Yekutieli | 14 Apr 2019
by the morphism
TL(ηM)◦τF,M = tG(M)◦ηM◦t−1
F(M)◦tF(M)◦F (t−1
M )
= tG(M)◦ηM◦F (t−1
M )
in Cstr(B, N), and other path is represented bytG(M)◦G(t−1
M )◦ηTK(M). Because
tG(M) is an isomorphism (of degree−1) in C(B, N), it suﬃces to prove thatηM◦
F (t−1
M ) =G(t−1
M )◦ηTK(M) in C(B, N); namely that the diagram
F (TK(M))
F(t−1
M )
//
ηTK(M)

F (M)
ηM

G(TK(M))
G(t−1
M )
//G(M)
iscommutative. Thisistruebecause η:F→GisastrictmorphismofDGfunctors,
and here it acts on the degree1 morphism t−1
M : TK(M)→M in C(B, N). □
Corollary5.5.3. For every integerk, the pair
(
Tk, (−1)k·idTk+1
{
is a triangulated
functor from K(A, M) to itself.
Proof. Combine Theorem 5.5.1 and Proposition 4.4.4. □
Remark 5.5.4. In [25], A.I. Bondal and M.M. Kapranov introduced the concept
of pretriangulated DG category. This is a DG categoryC for which the homotopy
category Ho(C) is canonically triangulated (the details of the deﬁnition are too
complicated to mention here). Our DG categories C(A, M) are pretriangulated
in the sense of [25]; but they have a lot more structure (e.g. the objects have
cohomologies too).
Suppose C and C′are pretriangulated DG categories. In [25] there is a (rather
complicated) deﬁnition ofpre-exact DG functorF : C→C′. It is stated there that
if F is a pre-exact DG functor, thenHo(F ) : Ho( C)→Ho(C′) is a triangulated
functor. This is analogous to our Theorem 5.5.1. Presumably, Theorems 4.4.3 and
4.5.5 imply that every DG functorF : C(A, M)→C(A′, M′) is pre-exact in the
sense of [25]; but we did not verify this.
