---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-108-162-weakly-stable-and-idempotent-copointed-funct
section_title: "Weakly Stable and Idempotent Copointed Functors"
section_number: 16.2
pages: 355-358
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
this subsection is adapted from [157, Section 2]. Recall that we follow Conventions
15.1.17 and 15.2.1. Like Subsection 16.1, the results of this subsection apply in
much greater generality. We state the results in the special context of algebraically
graded rings and modules, since we need them for the graded m-torsion functor
F := Γm.
Deﬁnition 16.2.1. Let A be a graded ring and F : M(A, gr) →M(A, gr) a left
exact linear functor.
(1) The functor F is called stable if for every injective object I ∈M(A, gr), the
object F(I) is injective.
(2) The functor F is called weakly stable if for every injective object I ∈
M(A, gr), the object F(I) is right F-acyclic, in the sense of Deﬁnition 16.1.3.
Clearly stable implies weakly stable.
Remark 16.2.2. The name “stable” comes from the theory of torsion classes; see
[148, Section VI.7]. Indeed, a torsion class is called stable if the corresponding
torsion functor F is a stable functor, as deﬁned above.
The name “weakly stable” was coined in [157], where it was shown that for a
ﬁnitely generated ideal a in a commutative ring A, the torsion functor Γa is weakly
stable iﬀthe ideal a is weakly proregular. We should mention the well-known fact
that if the commutative ring A is noetherian, then for every ideal a ⊆A the torsion
functor Γa is stable (cf. [63, Lemma III.3.2]; or use the Matlis classiﬁcation of
injective A-modules in Subsection 13.2).
Deﬁnition 16.2.3. Let M be a linear category (e.g. M(A, gr) or D(A, gr) for a
graded ring A), with identity functor IdM.
355
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(1) A copointed linear functor on M is a pair (F, σ), consisting of a linear functor
F : M →M and a morphism of functors σ : F →IdM.
(2) The copointed linear functor (F, σ) is called idempotent if the morphisms
σF (M), F(σM) : F(F(M)) →F(M)
are isomorphisms for all objects M ∈M.
(3) If M is a triangulated category, F is a triangulated functor, and σ is a mor-
phism of triangulated functors, then we call (F, σ) a copointed triangulated
functor.
The name “copointed” is explained in Remark 16.2.11.
Weak stability and idempotence together have the following eﬀect.
Lemma 16.2.4. Let (F, σ) be an idempotent copointed linear functor on M(A, gr),
and assume that F is left exact and weakly stable. If I is a right F-acyclic object
of M(A, gr), then F(I) is also a right F-acyclic object of M(A, gr).
Proof. Choose an injective resolution ρ : I →J; i.e. J is a complex of injectives
concentrated in nonnegative degrees, and ρ is a quasi-isomorphism in Cstr(A, gr).
Since Hq(F(J)) ∼= RqF(I), and since I is a right F-acyclic object, we see that
the homomorphism of complexes F(ρ) : F(I) →F(J) is a quasi-isomorphism.
Therefore both F(ρ) and RF(F(ρ)) are isomorphisms in D(A, gr).
The weak stability of F implies that F(J) is a bounded below complex of right
F-acyclic objects. According to Lemma 16.1.5 the complex F(J) is right F-acyclic.
This means that the morphism ηR
F (J) : F(J) →RF(J) is an isomorphism.
The idempotence of the copointed functor F says that the morphisms σF (I) and
σF (J) are isomorphisms in Cstr(A, gr). We get a commutative diagram in D(A, gr) :
F(I)
F (ρ)
∼
=

F(F(I))
σF (I)
∼
=
o
ηR
F (I)
/
F (F (ρ))

RF(F(I))
RF (F (ρ))
∼
=

F(J)
F(F(J))
σF (J)
∼
=
o
ηR
F (J)
∼
=
/ RF(F(J))
We conclude that ηR
F (I) is an isomorphism; and this means that the object F(I) is
right F-acyclic.
□
The next lemma is a generalization of [118, Proposition 3.10].
Lemma 16.2.5. Suppose we are given a copointed linear functor (F, σ) on
M(A, gr).
Then there is a unique morphism σR : RF →IdD(A,gr) of triangu-
lated functors from D(A, gr) to itself, satisfying this condition: for every complex
M ∈D(A, gr) there is equality σR
M ◦ηR
M = σM of morphisms F(M) →M in
D(A, gr).
In a commutative diagram:
(16.2.6)
F(M)
ηR
M /
σM
%
RF(M)
σR
M

M
Proof. The existence of the morphism σR comes for free from the universal property
of the right derived functor. Still, for later reference, we give the construction.
For a K-injective complex I the morphism ηR
I : F(I) →RF(I) in D(A, gr) is an
isomorphism, and we deﬁne σR
I : RF(I) →I to be σR
I := σI ◦(ηR
I )−1.
356
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
For an arbitrary complex M we choose a quasi-isomorphism ρ : M →I into a
K-injective complex, and then we let σR
M := ρ−1 ◦σR
I ◦RF(ρ) in D(A, gr). The
corresponding commutative diagram in D(A, gr) is (16.2.7).
(16.2.7)
F(M)
ηR
M
/
F (ρ)

σM
&
RF(M)
RF (ρ)
∼
=

σR
M
/ M
ρ
∼
=

F(I)
ηR
I
∼
=
/
σI
9
RF(I)
σR
I
/ I
It is easy to see that the collection of morphisms {σR
M}M∈D(A,gr) has the desired
properties.
□
In this way we obtain a copointed triangulated functor (RF, σR) on D(A, gr).
Theorem 16.2.8. Let (F, σ) be an idempotent copointed linear functor on
M(A, gr), and assume that F is left exact and weakly stable.
(1) The copointed triangulated functor (RF, σR) on D+(A, gr) is idempotent.
(2) If F has ﬁnite right cohomological dimension, then the copointed triangu-
lated functor (RF, σR) on D(A, gr) is idempotent.
Proof. Let M ∈D(A, gr). Choose a K-injective resolution M →I in Cstr(A, gr),
such that I is a complex consisting of injective objects of M(A, gr), and inf(I) =
inf(H(M)). It suﬃces to prove that the morphisms
σR
RF (I), RF(σR
I ) : RF(RF(I)) →RF(I)
in D(A, gr) are isomorphisms.
Note that by our choice, if M ∈D+(A, gr) then I is a bounded below complex.
Since each Iq is an injective object, it is right F-acyclic. Because F is a weakly
stable functor, each of the objects F(Iq) is right F-acyclic too. If the functor F
has ﬁnite right cohomological dimension, or if I is bounded below, Lemma 16.1.5
says that the complexes I and F(I) are both right F-acyclic complexes.
Consider the diagram
(16.2.9)
F(F(I))
F (σI)

ηR
F (I)
/ RF(F(I))
RF (σI)

RF (ηR
I ) / RF(RF(I))
RF (σR
I )

F(I)
ηR
I
/ RF(I)
id
/ RF(I)
in D(A, gr). The left square is commutative: it is gotten from the vertical morphism
σI : F(I) →I, to which we apply in the horizontal direction the morphism of
functors ηR : F →RF.
The right square is also commutative: it comes from
applying the functor RF to the commutative diagram
F(I)
ηR
I
/
σI

RF(I)
σR
I

I
id
/ I
that characterizes σR
I .
Because I and F(I) are right F-acyclic complexes, the
morphisms ηR
I and ηR
F (I) are isomorphisms. Hence RF(ηR
I ) is an isomorphism. So
the horizontal morphisms in the diagram 16.2.9 are all isomorphisms. We are given
357
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
that F is idempotent, and thus F(σI) is an isomorphism. The conclusion of this
discussion is that RF(σR
I ) is an isomorphism.
Next, let φ : RF(I) →J be an isomorphism in D(A, gr) to a K-injective complex
J such that inf(J) = inf(H(RF(I))). We know that ηR
I : F(I) →RF(I) is an
isomorphism, and therefore the composed morphism φ ◦ηR
I
: F(I) →J is an
isomorphism in D(A, gr). Let ˜ψ : F(I) →J be a quasi-isomorphism in Cstr(A, gr)
representing φ◦ηR
I . Since F(I) and J are both right F-acyclic complexes, it follows
that F( ˜ψ) : F(F(I)) →F(J) is a quasi-isomorphism.
Consider the following
commutative diagram
F(F(I))
F ( ˜
ψ)
/
σF (I)

F(J)
ηR
J
/
σJ

RF(J)
σR
J

RF(RF(I))
σR
RF (I)

RF (φ)
o
F(I)
˜
ψ
/ J
id
/ J
RF(I)
φ
o
in D(A, gr). All horizontal arrows here are isomorphisms. We are given that F is
idempotent, and thus σF (I) is an isomorphism. The conclusion is that σR
RF (I) is an
isomorphism.
□
We end this subsection with a notion dual to “copointed functor”.
Deﬁnition 16.2.10. Let M be a linear category (e.g. M(A, gr) or D(A, gr)), with
identity functor IdM.
(1) A pointed linear functor on M is a pair (G, τ), consisting of a linear functor
G : M →M and a morphism of functors τ : IdM →G.
(2) The pointed linear functor (G, τ) is called idempotent if the morphisms
τG(M), G(τM) : G(M) →G(G(M))
are isomorphisms for all objects M ∈M.
(3) If M is a triangulated category, G is a triangulated functor, and τ is a
morphism of triangulated functors, then we call (G, τ) a pointed triangulated
functor.
Remark 16.2.11. Idempotent copointed functors already appeared in the litera-
ture under another name: idempotent comonads. Another name for (nearly) the
same notion is a (Bousﬁeld) colocalization functor, see e.g. [90]. Dually, idempo-
tent pointed functors are the same thing as idempotent monads. See [115] for a
discussion of these concepts.
In [76, Section 4.1], what we call an idempotent pointed functor is called a
projector. It is proved there that for an idempotent pointed functor (G, τ), and
an object M ∈M, the isomorphisms τG(M) and G(τM) are equal. The same proof
(with arrows reversed) shows that for an idempotent copointed functor (F, σ), and
an object M, the morphisms σF (M) and F(σM) are equal. We shall not require
these facts.
