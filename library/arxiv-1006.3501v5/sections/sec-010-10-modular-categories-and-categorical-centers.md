---
doc_id: arxiv-1006.3501v5
doc_title: "On two approaches to 3-dimensional TQFTs"
section_id: sec-010-10-modular-categories-and-categorical-centers
section_title: "Modular categories and categorical centers"
section_number: 10
pages: 31-34
source_pdf: 1006.3501v5.pdf
source_sha256: e939aec50387ce2d
toc_source: outline
doc_brief: "On two approaches to 3-dimensional TQFTs — W e prove that|M |C = τZ(C)(M ) for any closed oriented 3-manifold M and for any spherical fusion category C of non-zero dimension."
---
We recall the basics on modular categories and the Drinfeld center.
10.1. Modular categories ( [Tu]). A braiding in a monoidal category B is a nat-
ural isomorphism τ ={τX,Y : X⊗Y→Y⊗X}X,Y ∈Ob(B) such that
τX,Y ⊗Z = (id Y⊗τX,Z )(τX,Y⊗ idZ ) and τX⊗Y,Z = (τX,Z⊗ idY )(idX⊗τY,Z ).
These conditions imply that τX,1 =τ1,X = id X for all X∈ Ob(B) and so that (2)
is satisﬁed.
32 V. TURAEV AND A. VIRELIZIER
A monoidal category endowed with a braiding is said to be braided. The braiding
and its inverse are depicted as follows
τX,Y =
PSfrag replacements X
X
Y
Y
and τ −1
Y,X =
PSfrag replacements X
X
Y
Y
.
For any object X of a braided pivotal category B, one deﬁnes a morphism
θX =PSfrag replacements
X
X
= (id X⊗ ~evX )(τX,X⊗ idX ∗ )(idX⊗ coevX ) :X→X.
This morphism, called the twist, is invertible and
θ−1
X =PSfrag replacements
X
X
= (ev X⊗ idX )(idX ∗⊗τ −1
X,X )(~coevX⊗ idX ) :X→X.
Note that θ1 = id 1, θX⊗Y = (θX⊗θY )τY,XτX,Y for any X,Y ∈ Ob(B). The twist
is natural: θYf =fθ X for any morphism f : X→Y inB.
A ribbon category is a braided pivotal category B whose twist is self-dual, i.e.,
(θX )∗ = θX ∗ for all X∈ Ob(B). This is equivalent to the equality of morphisms
PSfrag replacements
X
X
=PSfrag replacements
X
X
for any X ∈ Ob(B). In a ribbon category θ−1
X =PSfrag replacements
X
X
=PSfrag replacements
X
X
. A ribbon
categoryB is spherical and gives rise to topological invariants of links in S3. Namely,
everyB-colored framed oriented link L⊂ S3 determines an endomorphism of the
unit object FB(L)∈ End(1) which turns out to be a topological invariant of L.
HereL isB-colored if every component of L is endowed with an object of B (called
the color of this component). The deﬁnition of FB(L) goes by an application of
the Penrose calculus to a diagram of L; a new feature is that with the positive
and negative crossings of the diagram one associates the braiding a nd its inverse,
respectively. For more on this, see [Tu].
A modular category (over k) is a ribbon fusion category B (over k = End(1)) such
that the matrix S = [tr(τj,iτi,j )]i,j∈J is invertible, whereJ is a representative set of
simple objects of B andτ is the braiding of B. The matrix S is called the S-matrix
ofB. Note that for any simple object J ofB, the twist θJ :J→J is multiplication
by an invertible scalar vJ∈ k called the twist scalar ofJ. This scalar depends only
on the isomorphism class of J and vJ ∗ = vJ . Set ∆ ± =∑
i∈J v±1
i (dim(i))2∈ k.
It is known that ∆ +∆ − = dim(B) = ∑
i∈J (dim(i))2, see [Tu]. We say that B is
anomaly free if ∆ + = ∆ −.
10.2. The center of a monoidal category. LetC be a monoidal category. A
half braiding ofC is a pair ( A,σ ), where A∈ Ob(C) and
σ ={σX :A⊗X→X⊗A}X∈Ob(C)
is a natural isomorphism such that
(15) σX⊗Y = (id X⊗σY )(σX⊗ idY )
for all X,Y ∈ Ob(C). This implies that σ1 = id A. We call A the underlying object
of the half braiding ( A,σ ).
The center of C is the braided category Z(C) deﬁned as follows. The objects
ofZ(C) are half braidings ofC. A morphism (A,σ )→ (A′,σ ′) inZ(C) is a morphism
f :A→A′ inC such that (id X⊗f )σX =σ′
X (f⊗ idX ) for all X∈ Ob(C). The unit
object of Z(C) is 1Z(C) = (1,{idX}X∈Ob(C)) and the monoidal product is
(A,σ )⊗ (B,ρ ) =
(
A⊗B, (σ⊗ idB)(idA⊗ρ)
)
.
ON TWO APPROACHES TO 3-DIMENSIONAL TQFTS 33
The braiding τ inZ(C) is deﬁned by
τ(A,σ),(B,ρ) =σB : (A,σ )⊗ (B,ρ )→ (B,ρ )⊗ (A,σ ).
There is a forgetful functorZ(C)→C assigning to every half braiding ( A,σ ) the
underlying object A and acting in the obvious way on the morphisms. This is a
strict monoidal functor.
IfC is a monoidal k-category, then soZ(C) and the forgetful functor is k-linear.
Observe that End Z(C)(1Z(C)) = End C(1) = k.
IfC is pivotal, then so is Z(C) with (A,σ )∗ = (A∗,σ ∨), where
σ∨
X =
PSfrag replacements A
A
X
X
σX ∗ : A∗⊗X→X⊗A∗,
and ev (A,σ) = ev A, coev (A,σ) = coev A, ~ev(A,σ) = ~evA, ~coev(A,σ) = ~coevA. The (left
and right) traces of morphisms and dimensions of objects in Z(C) are the same as
inC. If C is spherical, then so is Z(C).
10.3. The center of a fusion category. LetC be a spherical fusion category
over k. Fix a representative set I of simple objects of C.
Lemma 10.1. The centerZ(C) ofC is ribbon.
Proof. We need only to verify thatPSfrag replacements
X
X
=PSfrag replacements
X
X
for any half braiding X = (A,σ ) ofC.
Let (pα : A→ iα,q α : iα→ A)α∈Λ be an I-partition of A. For any α,β ∈ Λ such
that iα =iβ =i∈I we obtain using the naturality of σ thatPSfrag replacements
A
A
A
i
i
σA
σi
pα
qβ
= (dim(i))−1
PSfrag replacements
A
A
A iiσA
σi
pα
qβ
= (dim(i))−1
PSfrag replacements
A
A i
i
i
σA σi
pα
qβ
= (dim(i))−1
PSfrag replacements
A
A A
i
iσAσi
α
pα
qβ
=
PSfrag replacements
A
A A
i
i
σAσi
α
pα
qβ
.
We conclude using that any f∈ EndC(A) expands as f =∑
α,β∈Λ qα(pαfq β)pβ and
that pαfq β = 0 if iα⁄=iβ. □
Lemma 10.2 ([M¨ u2, Lemma 3.10]). If dim(C) is invertible in k, then for any half
braidings (A,σ ) and (B,ρ ) ofC, the k-linear endomorphism π(B,ρ)
(A,σ) of HomC(A,B )
deﬁned by
π(B,ρ)
(A,σ)(f ) = (dim(C))−1∑
i∈I
dim(i)
PSfrag replacements
A
B
f
i
i
σi∗
ρi
34 V. TURAEV AND A. VIRELIZIER
is a projector onto HomZ(C)((A,σ ), (B,ρ )).
Theorem 10.3 ([M¨ u2, Theorem 1.2, Proposition 5.18]). LetC be a spherical fusion
category over an algebraically closed ﬁeld such that dimC⁄= 0 . Then Z(C) is an
anomaly free modular category with ∆ + = ∆ − = dimC.
Note that dimZ(C) = ∆ +∆ − = (dimC)2.
