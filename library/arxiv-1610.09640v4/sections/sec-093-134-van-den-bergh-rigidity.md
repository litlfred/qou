---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-093-134-van-den-bergh-rigidity
section_title: "Van den Bergh Rigidity"
section_number: 13.4
pages: 273-280
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
plex R over a noetherian commutative ring A is not unique. This lack of uniqueness
(not to mention any sort of functoriality!) was the source of major diﬃculties in
[62], ﬁrst for gluing dualizing complexes on schemes, and then for producing the
trace morphisms associated to maps of schemes.
In 1997, M. Van den Bergh [153] discovered the idea of rigidity for dualizing
complexes. This was done in the context of noncommutative ring theory: A is
a noncommutative noetherian ring, central over a base ﬁeld K.
The theory of
noncommutative rigid dualizing complexes was developed further in several papers
of J.J. Zhang and A. Yekutieli, among them [183] and [187]. We shall talk about
this noncommutative theory in Section 18 of the book.
Here we will deal with the commutative side only, which turns out to be extremely
powerful. Before explaining it, let us ﬁrst observe that this is one of the rare cases
in which an idea originating from noncommutative algebra had signiﬁcant impact
in commutative algebra and algebraic geometry.
In this subsection we study Van den Bergh rigidity in the following context:
Setup 13.4.1. A is a commutative ring, and B is a ﬂat commutative A-ring.
We introduce the notion of rigid complex over B relative to A, and describe
some of its properties. In Subsection 13.5 we will discuss rigid dualizing and residue
complexes. This material is adapted from the papers [188], [189] and [175].
The theory of rigid complexes does not really require the assumption that B is
ﬂat over A, but ﬂatness makes the theory much easier. See Remark 13.4.24.
Consider the enveloping ring B ⊗A B. It comes equipped with a few ring homo-
morphisms:
(13.4.2)
B
ηi
−→B ⊗A B
ϵ−→B,
where η0(b) := b⊗1, η1(b) := 1⊗b, and ϵ(b0 ⊗b1) := b0·b1. We view B as a module
over B ⊗A B via ϵ. Of course ϵ ◦ηi = idB.
Suppose we are given B-modules M0 and M1. Then the tensor product M0⊗AM1
is a (B ⊗A B)-module. In this way we get an additive bifunctor
(−⊗A −) : M(B) × M(B) →M(B ⊗A B).
Passing to complexes, and then to homotopy categories, we obtain a triangulated
bifunctor
(13.4.3)
(−⊗A −) : K(B) × K(B) →K(B ⊗A B).
273
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Lemma 13.4.4. The bifunctor (13.4.3) has a left derived bifunctor
(−⊗L
A −) : D(B) × D(B) →D(B ⊗A B).
If either M0 or M1 is a complex of B-modules that is K-ﬂat over A, then the
morphism ηL
M0,M1 : M0 ⊗L
A M1 →M0 ⊗A M1 in D(B ⊗A B) is an isomorphism.
Proof. This is a variant of Theorem 12.3.1. We know by Corollary 11.4.26 and
Proposition 10.3.4 that every complex M ∈C(B) admits a K-ﬂat resolution P →
M. Because B is ﬂat over A, the complex P is also K-ﬂat over A. By Theorem
9.3.16 the left derived bifunctor (−⊗L
A −) exists, and the condition on ηL
M0,M1
holds.
□
Remark 13.4.5. The innocuous looking Lemma 13.4.4 is actually of tremendous
importance. Without the ﬂatness of A →B we could do very little homological
algebra of bimodules. Getting around the lack of ﬂatness requires the use of ﬂat
DG ring resolutions, as explained in Remark 13.4.24.
Every module L ∈M(B) has an action by B ⊗A B coming from the homomor-
phism ϵ in (13.4.2). Consider now a module N ∈M(B⊗AB). The K-module N has
two possible B-module structures, coming from the homomorphisms ηi. Thus the
K-module HomB⊗AB(L, N) has three possible B-module structures: there is one
action from the B-module structure on L, and there are two from the B-module
structures on N.
Lemma 13.4.6. The three B-module structures on HomB⊗AB(L, N) coincide.
Exercise 13.4.7. Prove the lemma.
We are mostly interested in the B-module L = B. As the module N changes,
we get an additive functor
HomB⊗AB(B, −) : M(B ⊗A B) →M(B).
Passing to complexes, and then to homotopy categories, we get a triangulated
functor
HomB⊗AB(B, −) : K(B ⊗A B) →K(B).
This has a right derived functor
(13.4.8)
RHomB⊗AB(B, −) : D(B ⊗A B) →D(B),
that is calculated by K-injective resolutions. Namely if I ∈C(B ⊗A B) is a K-
injective complex, then the morphism
ηR
B,I : HomB⊗AB(B, I) →RHomB⊗AB(B, I)
in D(B) is an isomorphism.
By composing the bifunctor (−⊗L
A −) from Lemma 13.4.4 and the functor
RHomB⊗AB(B, −) from (13.4.8) we obtain a triangulated bifunctor
(13.4.9)
RHomB⊗AB(B, −⊗L
A −) : D(B) × D(B) →D(B).
Deﬁnition 13.4.10. Under Setup 13.4.1, the squaring operation is the functor
SqB/A : D(B) →D(B)
deﬁned as follows:
(1) For a complex M ∈D(B), its square is the complex
SqB/A(M) := RHomB⊗AB(B, M ⊗L
A M) ∈D(B).
(2) For a morphism φ : M →N in D(B), its square is the morphism
SqB/A(φ) := RHomB⊗AB(B, φ ⊗L
A φ) : SqB/A(M) →SqB/A(N)
in D(B).
274
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
It will be good to have an explicit formulation of the squaring operation. Let us
ﬁrst choose a K-projective resolution σ : P →M in C(B). Note that P is unique up
to homotopy equivalence, and σ is unique up to homotopy. Since B is ﬂat over A, the
complex P is K-ﬂat over A. We get an isomorphism presP : P ⊗A P
≃
−→M ⊗L
A M
in D(B ⊗A B), that we call a presentation. It is uniquely characterized by the
commutativity of the diagram
M ⊗L
A M
ηL
M,M
/ M ⊗A M
P ⊗L
A P
ηL
P,P
∼
=
/
Q(σ)⊗L
AQ(σ)
∼
=
O
P ⊗A P
presP
∼
=
g
Q(σ⊗Aσ)
O
in D(B ⊗A B).
Next we choose a K-injective resolution ρ : P ⊗A P →I in C(B ⊗A B). The
complex I is unique up to homotopy equivalence, and the homomorphism ρ is
unique up to homotopy. The resolution ρ gives rise to an isomorphism
presI : HomB⊗AB(B, I)
≃
−→RHomB⊗AB(B, P ⊗A P)
in D(B) such that the diagram
HomB⊗AB(B, P ⊗A P)
ηR
B,P ⊗AP /
Q(Hom(id,ρ))

RHomB⊗AB(B, P ⊗A P)
RHom(id,Q(ρ))
∼
=

HomB⊗AB(B, I)
ηR
B,I
∼
=
/
presI
∼
=
4
RHomB⊗AB(B, I)
is commutative.
The combination of the presentations presP and presI gives an isomorphism
presP,I : HomB⊗AB(B, I)
≃
−→SqB/A(M)
in D(B), that we also call a presentation.
Let φ : M →N be a morphism in D(B). The morphism SqB/A(φ) can also
be made explicit using presentations. For that we need to choose a K-projective
resolution σN : Q →N in C(B), and a K-injective resolution ρN : Q ⊗A Q →J in
C(B ⊗A B). These provide us with a presentation
presQ,J : HomB⊗AB(M, J)
≃
−→SqB/A(N).
There are homomorphisms ˜φ : P →Q in Cstr(B), and χ : I →J in Cstr(B ⊗A B),
both unique up to homotopy, such that the diagrams
P
Q(σ)
∼
=
/
Q( ˜φ)

M
φ

Q
Q(σN)
∼
=
/ N
M ⊗L
A M
φ⊗L
Aφ

P ⊗A P
presP
∼
=
o
Q(ρ)
∼
=
/
Q( ˜φ⊗A ˜φ)

I
Q(χ)

N ⊗L
A N
Q ⊗A Q
presQ
∼
=
o
Q(ρN)
∼
=
/ J
275
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in D(B) and D(B ⊗A B) respectively are commutative. See Subsections 10.1 and
10.2. Then the diagram
(13.4.11)
HomB⊗AB(B, I)
presP,I
∼
=
/
Q(Hom(id,χ))

SqB/A(M)
SqB/A(φ)

HomB⊗AB(B, J)
presQ,J
∼
=
/ SqB/A(N)
in D(B) is commutative.
The squaring operation is not an additive functor.
In fact, it is a quadratic
functor:
Theorem 13.4.12. Let φ : M →N be a morphism in D(B) and let b ∈B. Then
SqB/A(b·φ) = b2· SqB/A(φ),
as morphisms SqB/A(M) →SqB/A(N) in D(B).
Proof. We shall use presentations. Let ˜φ : P →Q be a homomorphism in Cstr(B)
that represents φ, as above. Then the homomorphism b· ˜φ : P →Q Cstr(B) repre-
sents b·φ. Tensoring we get a homomorphism
(b· ˜φ) ⊗A (b· ˜φ) : P ⊗A P →Q ⊗A Q
Cstr(B ⊗A B). But
(b· ˜φ) ⊗A (b· ˜φ) = (b ⊗b)·(˜φ ⊗A ˜φ).
Hence on the K-injectives we get the homomorphism (b⊗b)·χ : I →J Cstr(B⊗AB).
We conclude that
HomB⊗AB
 idB, (b ⊗b)·χ

: HomB⊗AB(B, I) →HomB⊗AB(B, J)
represents SqB/A(b·φ). Finally, by Lemma 13.4.6 we know that
HomB⊗AB
 idB, (b ⊗b)·χ

= HomB⊗AB(b2· idB, χ)
= b2· HomB⊗AB(idB, χ).
□
Deﬁnition 13.4.13. Let M ∈D(B). A rigidifying isomorphism for M over B
relative to A is an isomorphism ρ : M
≃
−→SqB/A(M) in D(B).
Deﬁnition 13.4.14. A rigid complex over B relative to A is a pair (M, ρ), consist-
ing of a complex M ∈D(B) and a rigidifying isomorphism ρ : M
≃
−→SqB/A(M) in
D(B).
Deﬁnition 13.4.15. Suppose (M, ρ) and (N, σ) are rigid complexes over B relative
to A. A morphism of rigid complexes φ : (M, ρ) →(N, σ) is a morphism φ : M →N
in D(B), such that the diagram
M
ρ
∼
=
/
φ

SqB/A(M)
SqB/A(φ)

N
σ
∼
=
/ SqB/A(N)
in D(B) is commutative.
The category of rigid complexes over B relative to A is denoted by D(B)rig/A.
276
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Recall (Deﬁnition 13.1.5) that a complex M ∈D(B) has the derived Morita
property if the derived homothety morphism hmR
M : B →RHomB(M, M) in D(B)
is an isomorphism.
Theorem 13.4.16. Let (M, ρ) be a rigid complex over B relative to A. If M has
the derived Morita property, then the only automorphism of (M, ρ) in D(B)rig/A is
the identity.
Proof. Let φ : (M, ρ)
≃
−→(M, ρ) be an automorphism in D(B)rig/A. By Proposi-
tion 13.1.6, there is a unique invertible element b ∈B such that φ = b· idM, as
morphisms M →M in D(B).
Next, according to Theorem 13.4.12, we have
SqB/A(φ) = SqB/A(b· idM) = b2· SqB/A(idM).
Plugging this into the diagram in Deﬁnition 13.4.15 we get a commutative diagram
M
ρ
∼
=
/
b· idM

SqB/A(M)
b2 · idM

M
ρ
∼
=
/ SqB/A(M)
in D(B). Once more using Proposition 13.1.6 we see that b2 = b. Because b is an
invertible element, it follows that b = 1. Thus φ = idM.
□
Example 13.4.17. Assume B = A, and take M := B.
Then B ⊗A B ∼= B,
M ⊗L
A M ∼= M, and there are canonical isomorphisms
SqB/A(M) = RHomB⊗AB(B, M ⊗L
A M) ∼= HomB(B, M) ∼= M.
Thus the pair (M, idM) belongs to D(B)rig/A. Furthermore, the complex M has
the derived Morita property, so Theorem 13.4.16 applies.
Remark 13.4.18. To the reader who might object to Example 13.4.17 for being
silly, we have two things to say. First, the existence theorem for rigid dualizing
complexes 13.5.7, whose proof is beyond the scope of this book, starts with the
tautological rigid structure of K ∈D(K), where K is the regular base ring. The
rigid structure is then propagated to all ﬂat essentially ﬁnite type (FEFT) K-rings
using induction and coinduction of rigid structures. See the exercise and examples
below for an indication of these procedures.
The second fact we want to point out is that when A is an FEFT K-ring, then A
has exactly one rigid complex (M, ρ) ∈D(A)rig/K (up to a unique isomorphism) that
is nonzero on each connected component of Spec(A); and it is the rigid dualizing
complex of A (that will be deﬁned in the next subsection). This is proved in [188],
[13] and [139].
Exercise 13.4.19. Assume A̸ = 0, and take B := A[t1, . . . , tn], the polynomial
ring in n variables.
(1) Let C := B ⊗A B, and let I be the kernel of the multiplication homomor-
phism ϵ : C →B. Show that I is generated by the sequence c = (c1, . . . , cn),
where cj := tj ⊗1 −1 ⊗tj.
(2) Show that the Koszul complex K(C; c) is a free resolution of B over C.
(Hint: for 1 ≤m ≤n deﬁne Bm := A[t1, . . . , tm] and Cm := Bm ⊗A Bm.
By direct calculation show that K(C1; c1) →B1 is a quasi-isomorphism.
Next, there is a ring isomorphism Bm ⊗A B1
≃
−→Bm+1, 1 ⊗t1 7→tm+1.
277
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
This induces a ring isomorphism Cm ⊗A C1 ∼= Cm+1 and an isomorphism
of complexes
K(Cm; cm) ⊗A K(C1; c1) ∼= K(Cm+1; cm+1).
Use this last formula and induction on m to prove that K(Cm; cm) →Bm
is a quasi-isomorphism.)
(3) Prove that
Exti
C(B, C) ∼=
(
B
if
i = n
0
if
i̸ = n.
(Hint: use the Koszul resolution from above.)
(4) Conclude from item (3) that the complex B[n] ∈D(B) is rigid relative to
A; namely that there is a rigidifying isomorphism ρ : B[n]
≃
−→SqB/A
 B[n]

in D(B).
Example
13.4.20. Let A be a nonzero noetherian ring,
and let B
:=
A[t1, . . . , tn] as in the exercise above. Let ∆B/A := Ωn
B/A, the module of degree n
diﬀerential forms of B relative to A. It is the n-th exterior power of Ω1
B/A, so it is
a free B module of rank 1, with basis d(t1) ∧· · · ∧d(tn). By the previous example,
there exists some rigidifying isomorphism ρ for the complex ∆B/A[n].
However, it can be shown (see [188] or [175]) that the complex ∆B/A[n] has a
canonical rigidifying isomorphism relative to A. I.e. there is a rigidifying isomor-
phism ρ : ∆B/A[n]
≃
−→SqB/A
 ∆B/A[n]

in D(B) which is invariant under A-ring
automorphisms of B.
This rigidifying isomorphism ρ is an incarnation of Grothendieck’s Fundamen-
tal Local Isomorphism [62, Proposition II.7.2] and the Residue Isomorphism [62,
Theorem II.8.2].
It is well-known that a ﬁnitely generated module M over a noetherian ring A is
ﬂat iﬀit is projective. See [105, Corollary to Theorem 7.12].
Example 13.4.21. Let A be a noetherian ring, and let A →B be a ﬁnite ﬂat
ring homomorphism.
So B is a ﬁnitely generated projective A-module.
Deﬁne
∆B/A := HomA(B, A) ∈M(B).
It can be shown (see [175]) that the complex
∆B/A has a canonical rigidifying isomorphism relative to A. I.e. there is a rigidifying
isomorphism ρ : ∆B/A
≃
−→SqB/A(∆B/A) in D(B) which is invariant under A-ring
automorphisms of B.
Remark 13.4.22. The squaring operation SqB/A is functorial also in the ring B,
in two directions. For this remark we assume that the ring A is noetherian, and
the rings B and C are ﬂat essentially ﬁnite type A-rings. (See Remark 13.4.24
regarding the ﬂatness.)
Suppose u : B →C is a ﬁnite A-ring homomorphism, and θ : N →M is a
backward (or trace) morphism in D(B) over u, in the sense of Deﬁnition 12.6.11.
Then there is a backward morphism
Squ/A(θ) : SqC/A(N) →SqB/A(M)
in D(B) over u. The morphism Squ/A(θ) is functorial in u and θ in an obvious sense.
Furthermore, under suitable ﬁniteness conditions, if θ is a nondegenerate backward
morphism (see Deﬁnition 12.6.13), then so is Squ/A(θ). We call this property the
trace functoriality of the squaring operation.
The trace functoriality of the squaring operation allows us to talk about rigid
trace morphisms. With u : B →C as above, suppose that (M, ρ) ∈D(B)rig/A and
278
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(N, σ) ∈D(C)rig/A. A rigid trace morphism θ : (N, σ) →(M, ρ) over u relative to
A is a trace morphism θ : N →M over u such that the diagram
N
σ
∼
=
/
θ

SqC/A(N)
Squ/A(θ)

M
ρ
∼
=
/ SqB/A(M)
in D(B) is commutative.
Next, suppose v : B →C is an essentially étale homomorphism (i.e. formally
étale, plus the EFT condition that was already assumed) of A-rings, and λ : M →N
is a forward morphism over v, in the sense of Deﬁnition 12.6.3. Then there is a
forward morphism
qv/A(λ) : SqB/A(M) →SqC/A(N)
in D(B) over u. The morphism Sqv/A(λ) is functorial in v and λ in an obvious
sense. Furthermore, under suitable ﬁniteness conditions, if λ is a nondegenerate
forward morphism (see Deﬁnition 12.6.7), then so is Sqv/A(λ). We call this property
the étale functoriality of the squaring operation.
The étale functoriality of the squaring operation allows us to talk about rigid lo-
calization morphisms. With v : B →C as above, suppose that (M, ρ) ∈D(B)rig/A,
and (N, σ) ∈D(C)rig/A. A rigid localization morphism λ : (M, ρ) →(N, σ) over v
relative to A is a forward morphism λ : N →M over v such that the diagram
M
ρ
∼
=
/
λ

SqB/A(M)
Sqv/A(λ)

N
σ
∼
=
/ SqC/A(N)
in D(B) is commutative.
These functorialities of the squaring operation are hard to prove. An imprecise
study of them was made in the papers [188] and [189]. A correct treatment of the
trace functoriality can be found in the paper [173]; and a correct treatment of the
étale functoriality will appear in [175].
Remark 13.4.23. The squaring operation is related to Hochschild cohomology.
Assume for simplicity that A is a ﬁeld and M is a B-module. Then for each i the
cohomology
Hi(SqB/A(M)) = Exti
B⊗AB(B, M ⊗A M)
is the i-th Hochschild cohomology with values in the B-bimodule M ⊗A M. For
more on this material see [14], [137] and [138].
Remark 13.4.24. It is possible to avoid the assumption that B is ﬂat over A. This
is done by choosing a commutative DG ring ˜B that is K-ﬂat as a DG A-module,
with a DG ring quasi-isomorphism ˜B →B over A. Such resolutions always exist
(see [188] or [173]). Then we take
(13.4.25)
SqB/A(M) := RHom ˜
B⊗A ˜
B(B, M ⊗L
A M).
This was the construction used by Zhang and Yekutieli in the paper [188].
Unfortunately there was a serious error in [188]: we did not prove that for-
mula (13.4.25) is independent of the resolution ˜B. This error was discovered, and
corrected, by L. Avramov, S. Iyengar, J. Lipman and S. Nayak in their paper [14].
There were ensuing errors in [188] regarding the functoriality of the squaring
operation in the ring B (as described in Remark 13.4.22).
The paper [14] did
279
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
not treat such functoriality at all, and the constructions and proofs of the trace
functoriality were corrected only in our recent paper [173].
It is worthwhile to
mention that the correct proofs (both in [14] and [173]) rely on noncommutative
DG rings and DG bimodules over them; and the squaring operation is replaced by
the rectangle operation.
Because the non-ﬂat case is so much more complicated, we have decided not to
reproduce it in the book. The interested reader can look up the research papers
[173], [175], [176] and [177], the survey article [168], or the lecture notes [174].
A general treatment of derived categories of bimodules, based on K-ﬂat DG ring
resolutions, will be in the paper [178].
