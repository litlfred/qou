---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-109-163-graded-torsion-weak-stability-and-idempotenc
section_title: "Graded Torsion: Weak Stability and Idempotence"
section_number: 16.3
pages: 358-367
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
we begin the study of derived torsion over a connected graded ring. We adhere
to Conventions 15.1.17 and 15.2.1. Thus K is a ﬁeld, and all graded K-rings are
algebraically graded central K-rings. The symbol ⊗means ⊗K. The enveloping
ring of a graded K-ring A is the graded K-ring Aen = A⊗Aop. The category of left
algebraically graded A-modules is M(A, gr), and it is a K-linear abelian category.
Its derived category is D(A, gr).
Recall the notion of left noetherian connected graded K-ring from Deﬁnitions
15.1.29 and 15.2.18. In this subsection we will assume the following setup:
358
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Setup 16.3.1. We are given a left noetherian connected graded K-ring A, with
augmentation ideal m = L
i≥1 Ai ⊆A. We are also given graded K-rings B and C.
The graded rings B and C are auxiliary – they are just placeholders, allowing us
to write more general formulas. For instance, M(A ⊗Bop, gr) is M(Aen, gr) when
we take B := A, but it is M(A, gr) when B := K.
Since A is left noetherian, the augmentation ideal m is a ﬁnite graded left A-
module.
We shall often make implicit use of the canonical isomorphisms
(16.3.2)
A ⊗A M
≃
−→M
and
HomA(A, M)
≃
−→M
in M(A ⊗Bop, gr). There are similar canonical isomorphisms
(16.3.3)
A ⊗L
A M
≃
−→M
and
RHomA(A, M)
≃
−→M
in D(A ⊗Bop, gr). Also we view K ∼= A/m as a graded Aen-module via the aug-
mentation ring homomorphism A →K.
We are interested in graded m-torsion. This makes sense for bimodules, and
hence the slightly complicated deﬁnition below.
Deﬁnition 16.3.4. Under Setup 16.3.1:
(1) Let M ∈M(A⊗Bop, gr). An element m ∈M is called an m-torsion element
if mj ·m = 0 for j ≫0.
(2) The set of m-torsion elements of M is denoted by Γm(M), and it is called
the m-torsion submodule of M.
(3) We call M an m-torsion module if Γm(M) = M.
(4) We denote by Mtor(A ⊗Bop, gr) the full subcategory of M(A ⊗Bop, gr) on
the m-torsion modules.
The fact that Γm(M) is a graded (A ⊗Bop)-submodule of M is easy to see.
Indeed, we can express the torsion submodule as follows:
(16.3.5)
Γm(M) = lim
j→HomA(A/mj, M) ⊆HomA(A, M),
using the identiﬁcation (16.3.2), where j ≥1, mj is the j-fold product m · · · m ⊆A,
A →A/mj+1 →A/mj are the canonical graded ring surjections, and the operation
limj→is in the category M(A ⊗Bop, gr).
It is clear that
Γm : M(A ⊗Bop, gr) →Mtor(A ⊗Bop, gr)
is a linear functor, and the inclusions Γm(M) ⊆M assemble into a monomorphism
σ : Γm ↣Id of functors from M(A ⊗Bop, gr) to itself.
The ring B plays an auxiliary role in Deﬁnition 16.3.4. Because there is no men-
tion of torsion for Bop-modules, the notation Mtor(A ⊗Bop, gr) is not ambiguous.
However, in Subsection 16.5, where torsion for Bop modules does become an option,
we will switch to the richer notation M(tor,..)(A ⊗Bop, gr). See Deﬁnition 16.5.5.
Lemma 16.3.6. Under Setup 16.3.1 the following hold.
(1) The functor Γm commutes with graded ring homomorphisms C →B, in the
sense that the diagram
M(A ⊗Bop, gr)
Γm
/
Rest

Mtor(A ⊗Bop, gr)
Rest

M(A ⊗Cop, gr)
Γm
/ Mtor(A ⊗Cop, gr)
is commutative.
359
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) The functor Γm is idempotent,
in the sense that for every M
∈
M(A ⊗Bop, gr) the homomorphisms
σΓm(M) , Γm(σM) : Γm(Γm(M)) →Γm(M)
are bijective and are equal to each other.
(3) Let φ : M →N be a homomorphism in M(A ⊗Bop, gr), such that M is m-
torsion. Then there is a unique homomorphism φ′ : M →Γm(N) satisfying
φ = σN ◦φ′.
(4) The functor Γm is left exact.
(5) The functor Γm commutes with direct limits.
(6) The
category
Mtor(A ⊗Bop, gr)
is
a
thick
abelian
subcategory
of
M(A ⊗Bop, gr), closed under taking subobjects and quotients.
Exercise 16.3.7. Prove Lemma 16.3.6. (Hint: for item (6) you will need the fact
that A is left noetherian.)
Recall that for a module M ∈M(A, gr), its socle is Soc(M) = HomA(K, M).
The socle is a functor, and there is a monomorphism Soc ↣Γm of functors from
M(A, gr) to itself.
Lemma 16.3.8. Let M ∈M(A, gr), and let W := Soc(M). If M is an m-torsion
module, then W is a graded-essential submodule of M.
Proof. Take any nonzero graded A-submodule M ′ ⊆M. Let m ∈M ′ be some
nonzero homogeneous element. Because M is a torsion module, yet m̸ = 0, there
is a unique j ∈N such that mj+1·m = 0 but mj ·m̸ = 0. So there is a homoge-
neous element a ∈mj such that a·m̸ = 0. The element a·m is then a nonzero
homogeneous element in M ′ ∩W.
□
The K-linear dual (see Deﬁnition 15.2.25) of the ring A is the graded bimodule
A∗= HomK(A, K) ∈M(Aen, gr). The augmentation ring homomorphism A →K
induces, by dualizing, a canonical monomorphism
(16.3.9)
K ↣A∗
in M(Aen, gr). For every W ∈M(K, gr) there is an induced monomorphism
(16.3.10)
W ∼= W ⊗K ↣W ⊗A∗
in M(Aen, gr).
Lemma 16.3.11. Under Setup 16.3.1, let W ∈M(K, gr), and deﬁne I := A∗⊗
W ∈M(A, gr). Consider the canonical monomorphism W ↣I in M(A, gr) from
(16.3.10). Then:
(1) I is a graded-injective A-module.
(2) I is an m-torsion A-module.
(3) W = Soc(I).
(4) W is a graded-essential submodule of I.
Proof.
(1) Say W = L
x∈X K(−ix). Then I ∼= L
x∈X A∗(−ix) in M(A, gr). According to
Proposition 15.2.5(2) and Theorem 15.2.17(1), the graded A-module I is graded-
injective.
(2) The A-module A∗is m-torsion, and a direct sum of torsion modules is torsion
(see Lemma 16.3.6(5)).
(3) This is because K = Soc(A∗), via the canonical monomorphism (16.3.9).
(4) Combine items (2) and (3) with Lemma 16.3.8.
□
360
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proposition 16.3.12. Under Setup 16.3.1, let M ∈M(A, gr), and let W :=
Soc(M). The three conditions below are equivalent.
(i) M is an m-torsion graded A-module.
(ii) W is a graded-essential A-submodule of M.
(iii) There is a graded-essential monomorphism ϵ : M ↣A∗⊗W in M(A, gr),
that restricts to the identity on W.
Proof.
(i) ⇒(ii): This is Lemma 16.3.8.
(ii) ⇒(iii): By Lemma 16.3.11 the graded A-module A∗⊗W is graded-injective.
Hence there is a homomorphism ϵ : M →A∗⊗W in M(A, gr) that makes the
diagram
W /
/


M
ϵ
z
A∗⊗W
in M(A, gr) commutative. Let M ′ := Ker(ϵ). If M ′ were nonzero, then, because
W ⊆M is a graded-essential submodule, we would have W ∩M ′̸ = 0. But W →
A∗⊗W is a monomorphism. We conclude that ϵ is a monomorphism too.
Finally, by Lemma 16.3.11(4) we know that W is a graded-essential submodule
of A∗⊗W. It follows that the monomorphism ϵ is graded-essential.
(iii) ⇒(i): The graded A-module A∗is torsion. We know that the subcategory
Mtor(A, gr) of M(A, gr) is closed under taking arbitrary direct sums and subobjects.
Hence M is m-torsion.
□
Coﬁnite graded modules were deﬁned in Deﬁnition 15.2.33.
Corollary 16.3.13. Assume A is a noetherian connected graded ring. Let M ∈
Mtor(A, gr). The two conditions below are equivalent.
(i) M is a coﬁnite graded A-module.
(ii) W := Soc(M) is a ﬁnite graded K-module.
Proof. Graded Matlis Duality (Theorem 15.2.34) tells us that the coﬁnite graded
A-modules are the artinian objects in the abelian category M(A, gr).
(i) ⇒(ii): We are given that M is a coﬁnite graded A-module. Hence so is its
submodule W.
Since W is an A-module via K, it must be an artinian graded
K-module. So W is ﬁnite over K.
(ii) ⇒(i): Since A∗is a coﬁnite graded A-module, and A∗⊗W is a ﬁnite direct
sum of degree twists of A∗, we see that A∗⊗W is a coﬁnite graded A-module.
By Proposition 16.3.12 we know that M is isomorphic to a graded submodule of
A∗⊗W; so M is also a coﬁnite graded A-module.
□
Remark 16.3.14. We do not know if the corollary remains true if A is just left
noetherian.
Now we pass to derived categories and functors.
Deﬁnition 16.3.15. Under Setup 16.3.1, we denote by Dtor(A ⊗Bop, gr) the full
subcategory of D(A ⊗Bop, gr) on the complexes M whose cohomology modules
Hp(M) belong to Mtor(A ⊗Bop, gr) for all p.
Proposition 16.3.16. Under Setup 16.3.1 the following hold.
361
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(1) The functor Γm has a triangulated right derived functor
RΓm : D(A ⊗Bop, gr) →D(A ⊗Bop, gr).
If I ∈D(A ⊗Bop, gr) is K-graded-injective over A, then the morphism
ηR
I : Γm(I) →RΓm(I) is an isomorphism.
(2) There is a unique morphism σR : RΓm →Id of triangulated functors from
D(A ⊗Bop, gr) to itself, such that for every M ∈D(A ⊗Bop, gr) there is
equality σR
M ◦ηR
M = Q(σM) of morphisms Γm(M) →M in D(A ⊗Bop, gr).
(3) The category Dtor(A ⊗Bop, gr) is a full triangulated subcategory of
D(A ⊗Bop, gr), and it contains the image of the functor RΓm.
(4) The functor RΓm commutes with graded K-ring homomorphisms C →B,
in the sense that the diagram
D(A ⊗Bop, gr)
RΓm /
Rest

Dtor(A ⊗Bop, gr)
Rest

D(A ⊗Cop, gr)
RΓm / Dtor(A ⊗Cop, gr)
is commutative up to isomorphism. Likewise for the morphism of triangu-
lated functors σR.
(5) For every M ∈D(A ⊗Bop, gr) and p ∈Z there is an isomorphism
Hp(RΓm(M)) ∼= lim
j→Extp
A(A/mj, M)
in M(A ⊗Bop, gr). This isomorphism is functorial in M.
Proof. (1) By Corollary 15.3.8(3) every M ∈C(A ⊗Bop, gr) has a resolution ρ :
M →I in Cstr(A ⊗Bop, gr) by a complex I that is K-graded-injective over A. If
ψ : I →I′ is a quasi-isomorphism in Cstr(A⊗Bop, gr) between such complexes, then
it is a homotopy equivalence in Cstr(A, gr), and hence Γm(ψ) is a quasi-isomorphism.
We see that the full subcategory J ⊆K(A ⊗Bop, gr) on these complexes I satisﬁes
the conditions of Theorem 8.4.9. Therefore the right derived functor RΓm exists,
and ηR
I is an isomorphism for all I ∈J.
(2) This is a special case of Lemma 16.2.5.
(3) Clear from Lemma 16.3.6(6).
(4) This is immediate from items (1) and (2).
(5) Use formula (16.3.5), and the fact that cohomology commutes with direct limits.
□
Deﬁnition 16.3.17. Under Setup 16.3.1, the i-th local cohomology functor is the
functor
Hi
m := RiΓm : M(A ⊗Bop, gr) →M(A ⊗Bop, gr),
the i-th right derived functor of Γm.
Corollary 16.3.18. For every i ∈N there is an isomorphism Hi
m ∼= Hi ◦RΓm of
functors from M(A ⊗Bop, gr) to itself.
Proof. This is immediate from Proposition 16.3.16(1).
□
Proposition 16.3.19. For every i ∈N the functor
Hi
m : M(A ⊗Bop, gr) →M(A ⊗Bop, gr)
commutes with direct limits.
362
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. In view of Proposition 16.3.16(4), with C := K, we can assume that B = K,
so A ⊗Bop = A. Since direct limits commute with each other, by Proposition
16.3.16(5) it suﬃces to prove that for every i, j the functor Exti
A(A/mj, −) com-
mutes with direct limits. Now A is left noetherian, so we can ﬁnd a resolution
P →A/mj by a nonpositive complex, where each P i is a ﬁnite graded-free A-
module. And the functor
Exti
A(A/mj, −) ∼= Hi ◦HomA(P, −) : M(A, gr) →M(A, gr)
commutes with inﬁnite direct limits.
□
Deﬁnition 16.1.2, when used in our context, says that the right cohomological
dimension of the functor Γm is
(16.3.20)
d := sup {p ∈N | Hp
m̸ = 0} ∈N ∪{±∞}.
The cohomological dimension of a triangulated functor was introduced in Def-
inition 12.4.1. A triangulated functor is called quasi-compact if it commutes with
inﬁnite direct sums (Deﬁnition 16.1.7).
Theorem
16.3.21. Under Setup 16.3.1, assume the torsion functor Γm
:
M(A, gr) →M(A, gr) has ﬁnite right cohomological dimension. Then the derived
torsion functor
RΓm : D(A ⊗Bop, gr) →D(A ⊗Bop, gr)
is quasi-compact and has ﬁnite cohomological dimension.
Proof. According to Proposition 16.3.16(4), the functor
Γm : M(A ⊗Bop, gr) →M(A ⊗Bop, gr)
also has ﬁnite right cohomological dimension. The right derived functors
RqΓm = Hq
m : M(A ⊗Bop, gr) →M(A ⊗Bop, gr)
are quasi-compact by Proposition 16.3.19. So Theorem 16.1.10 applies.
□
Lemma 16.3.22. Let I ∈M(A, gr), and let W := Soc(I). The following three
conditions are equivalent.
(i) I is graded-injective and m-torsion.
(ii) I is graded-injective and W is an essential submodule of I.
(iii) There is an isomorphism I ∼= A∗⊗W in C(A, gr) which is the identity on
W.
In condition (iii) we view W as a submodule of A∗⊗W using the canonical
embedding (16.3.10).
Proof.
(i) ⇒(ii): This is Lemma 16.3.8.
(ii) ⇒(iii): By Proposition 16.3.12 there is an essential monomorphism ϵ : I →
A∗⊗W in M(A, gr) that extends the identity of W. Because I is graded-injective,
the monomorphism ϵ is split, by some epimorphism σ : A∗⊗W →I. But W is a
graded-essential submodule of A∗⊗W, and therefore σ is also a monomorphism.
We conclude that both σ and ϵ are isomorphisms.
(iii) ⇒(i): According to Lemma 16.3.11, the graded A-module A∗⊗W is graded-
injective and m-torsion.
□
Lemma 16.3.23. Let M ∈M(A, gr) be an m-torsion module, and let I be an
injective hull of M in M(A, gr). Then I ∼= A∗⊗W, where W is the socle of M. In
particular, I is an m-torsion module.
363
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. By Proposition 16.3.12 there is a graded-essential monomorphism ϵ : M ↣
A∗⊗W in M(A, gr). From Lemma 16.3.11(1) we know that A∗⊗W is a graded-
injective module over A. So by the uniqueness (up to isomorphism) of graded-
injective hulls, we get an isomorphism I ∼= A∗⊗W. Finally, by Lemma 16.3.11(2),
A∗⊗W is m-torsion.
□
Lemma 16.3.24. Let I be a graded-injective A-module. Then there is an isomor-
phism Γm(I) ∼= A∗⊗W in M(A, gr), where W is the socle of I.
Proof. Consider the essential monomorphism ϵ : W ↣A∗⊗W from Lemma
16.3.11(4), and the monomorphism τ : W ↣I.
Because I is graded-injective,
there is a homomorphism ψ : A∗⊗W →I in M(A, gr) such that ψ ◦ϵ = τ. Since
ϵ is a graded-essential monomorphism, the usual calculation (see the proof of the
implication (ii) ⇒(iii) in Proposition 16.3.12) shows that ψ is a monomorphism.
Let J ⊆I be the image of ψ, so ψ : A∗⊗W
≃
−→J. We know (from Lemma 16.3.11)
that J is graded-injective and m-torsion. Hence there is a direct sum decomposition
I = J ⊕J′ in M(A, gr), and Γm(J) = J.
By Proposition 16.3.12 we know that W ∩J′ = Soc(J′) is a graded-essential
submodule of Γm(J′); but W ⊆J, so W ∩J′ = 0, and therefore Γm(J′) = 0. The
conclusion is that Γm(I) = J.
□
Theorem 16.3.25. Under Setup 16.3.1, the torsion functor
Γm : M(A, gr) →M(A, gr)
is stable, namely for every graded-injective A-module I the m-torsion submodule
Γm(I) is graded-injective.
Proof. This is immediate from Lemma 16.3.24 and Lemma 16.3.11(1).
□
Here is the graded NC version of Deﬁnition 13.2.5.
Deﬁnition 16.3.26.
(1) A minimal complex of graded-injective A-modules is a bounded below com-
plex I of graded-injective A-modules, such that for every p the submodule
Zp(I) ⊆Ip is graded-essential.
(2) Let M ∈D+(A, gr). A minimal graded-injective resolution of M is a quasi-
isomorphism ρ : M →I in Cstr(A, gr), where I is a minimal complex of
graded-injective A-modules.
Lemma 16.3.27. Let M ∈D+(A, gr). Then M has a minimal graded-injective
resolution.
Proof. The proof of Proposition 13.2.6 works here too.
□
There is uniqueness for minimal graded-injective resolutions, but we won’t need
it.
For the next proposition, and for later results, it will be convenient to use this
notation:
Notation 16.3.28. If the torsion functor Γm has ﬁnite right cohomological dimen-
sion, then we let ⋆:= ⟨empty⟩, the empty boundedness indicator; otherwise we let
⋆:= +. Thus D⋆is either D or D+.
Proposition 16.3.29. With Notation 16.3.28, let M ∈D⋆(A ⊗Bop, gr).
The
following conditions are equivalent:
(i) M ∈D⋆
tor(A ⊗Bop, gr).
(ii) The morphism σR
M : RΓm(M) →M in D(A ⊗Bop, gr) is an isomorphism.
364
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. The implication (ii) ⇒(i) is due to Proposition 16.3.16(3).
For the other implication, we can forget the ring B; it is not relevant. First let
us assume that M ∈D+
tor(A, gr). By Lemma 16.3.23 the injective hull in M(A, gr)
of a torsion module is torsion. Then, according to Theorem 11.5.8, there is a quasi-
isomorphism M →I in C+
str(A, gr), where I is a complex of torsion graded-injective
A-modules. It follows that homomorphism σI : Γm(I) →I in C+
str(A, gr), that
represents σR
M, is an isomorphism.
When H(M) is not bounded below, but Γm has ﬁnite right cohomological dimen-
sion, we can use smart truncation, as in the proof of Theorem 12.5.2(2).
□
Proposition 16.3.30. With Notation 16.3.28, Let M ∈D⋆
tor(A ⊗Bop, gr) and
N ∈D+(A ⊗Cop, gr). Then there is an isomorphism
RHomA(M, N)
≃
−→RHomA
 M, RΓm(N)

in D(B ⊗Cop, gr), and it is functorial in M and N.
Proof. Choose a resolution M →IM in C⋆
str(A ⊗Bop, gr) where IM is K-graded-
injective over A, each Ip
M is graded-injective over A, and inf(IM) = inf(H((M));
this is possible by Corollary 15.3.7(3). Choose the same sort of resolution N →IN
in C+
str(A ⊗Cop, gr). Then
(16.3.31)
RHomA(M, N) ∼= HomA(IM, IN)
in D(B ⊗Cop, gr), and RΓm(N) ∼= Γm(IN) in D(A ⊗Cop, gr). By Theorem 16.3.25
each Γm(Ip
N) is graded-injective as an A-module, so Γm(IN) is a bounded below
complex of graded-injective A-modules, and therefore it is a K-graded-injective
complex over A. We see that
(16.3.32)
RHomA
 M, RΓm(N)
 ∼= HomA
 IM, Γm(IN)

in D(B ⊗Cop, gr).
By Proposition 16.3.29 (in both cases of Notation 16.3.28) the homomorphism
σIM : Γm(IM) →IM is a quasi-isomorphism. Hence in the commutative diagram
HomA(IM, IN)
Hom(σIM ,id)
/ HomA
 Γm(IM), IN

HomA
 IM, Γm(IN)
 Hom(σIM ,id) /
Hom(id,σIN )
O
HomA
 Γm(IM), Γm(IN)

Hom(id,σIN )
O
in Cstr(B ⊗Cop, gr) the two horizontal arrows are quasi-isomorphisms. The right
vertical arrow is an isomorphism in Cstr(B ⊗Cop, gr) by Lemma 16.3.6(3).
It
follows that the left vertical arrow is a quasi-isomorphism. Combining this with the
isomorphisms (16.3.31) and (16.3.32) we obtain the desired isomorphism above.
□
The next deﬁnition is a specialization of Deﬁnitions 16.1.3, 16.1.4 and 16.2.1.
Deﬁnition 16.3.33. Under Setup 16.3.1:
(1) A module N ∈M(A ⊗Bop, gr) is called graded-m-ﬂasque if it is a right
Γm-acyclic object, i.e. if Hq
m(N) = 0 for all q > 0.
(2) The functor
Γm : M(A ⊗Bop, gr) →M(A ⊗Bop, gr)
is
called
weakly
stable
if
for
every
graded-injective
module
I
∈
M(A ⊗Bop, gr), the module Γm(I) ∈M(A ⊗Bop, gr) is graded-m-ﬂasque.
(3) A complex N ∈D(A ⊗Bop, gr) is called a K-graded-m-ﬂasque complex if it
is a right Γm-acyclic complex, i.e. if the morphism ηR
N : Γm(N) →RΓm(N)
in D(A ⊗Bop, gr) is an isomorphism.
365
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
The term “ﬂasque” in this meaning seems to have been ﬁrst used in [190].
Example 16.3.34. Suppose M ∈M(A, gr) is an m-torsion module. Consider its
minimal graded-injective resolution 0 →M →I0 →I1 →· · · . By Lemma 16.3.23
and induction on q, we see that all the graded modules Iq are m-torsion; in fact
Iq ∼= A∗⊗W q for some W q ∈M(K, gr). Thus RΓm(M) ∼= Γm(I) = I ∼= M, so
RqΓm(M) = 0 for all q > 0, and M is a graded-m-ﬂasque A-module.
Theorem 16.3.35. Under Setup 16.3.1, the torsion functor
Γm : M(A ⊗Bop, gr) →M(A ⊗Bop, gr)
is weakly stable.
Proof. Take an injective object I ∈M(A ⊗Bop, gr).
According to Proposition
15.2.13(3), the module I is graded-injective over A. By Lemma 16.3.24 we know
that there is an isomorphism Γm(I) ∼= A∗⊗W in M(A, gr) for some graded K-
module W. This is a graded-injective A-module, and therefore Γm(I) is graded-m-
ﬂasque as an object of M(A, gr). Finally, by Proposition 16.3.16(4), the property
of being graded-m-ﬂasque is insensitive to the restriction functor M(A⊗Bop, gr) →
M(A, gr), so Γm(I) is graded-m-ﬂasque as an object of M(A ⊗Bop, gr).
□
In Proposition 16.3.16(2) we presented a morphism σR : RΓm →Id of triangu-
lated functors from D⋆(A ⊗Bop, gr) to itself. Here we are using Notation 16.3.28.
According to Deﬁnition 16.2.3 the pair (RΓm, σR) is a copointed triangulated func-
tor. Recall that (RΓm, σR) is an idempotent copointed triangulated functor if for
every complex M ∈D⋆(A ⊗Bop, gr) the morphisms
σR
RΓm(M) , RΓm(σR
M) : RΓm(RΓm(M)) →RΓm(M)
in D(A ⊗Bop, gr) are isomorphisms.
Corollary 16.3.36 ([157]). With Notation 16.3.28, the copointed triangulated func-
tor (RΓm, σR) on D⋆(A ⊗Bop, gr) is idempotent.
Proof. By Theorem 16.3.35 the functor Γm is weakly stable, and by Lemma 16.3.6(2)
the copointed functor (Γm, σ) is idempotent. Thus Theorem 16.2.8 applies.
□
We end the subsection with an example showing a torsion functor as in Theorem
16.3.35 which is weakly stable but not stable. The example is a slight modiﬁcation
of an example in [157].
Example 16.3.37. Let A := K[t], the polynomial ring in a variable t of degree
1. It is connected noetherian, and its augmentation ideal m is generated by t. Let
B := K[s0, s1, . . .], the commutative polynomial ring in countably many variables
s0, s1, . . . of degree 1. So B is a graded ring, and it is not noetherian. Theorem
16.3.35 tells us that the functor
Γm : M(A ⊗B, gr) →M(A ⊗B, gr)
is weakly stable. (Since B is commutative, it doesn’t matter whether we write B
or Bop). We will prove that Γm is not stable.
Consider a countable collection {Ip}p∈N of graded-injective B-modules. Then
I := Q
p∈N Ip(−p) is a graded-injective B-module, and therefore J := HomB(A ⊗
B, I) is a graded-injective (A⊗B)-module. If the functor Γm on M(A⊗B, gr) were
stable, this would imply that Γm(J) is also a graded-injective (A⊗B)-module. Since
B →A ⊗B is ﬂat, Γm(J) is then a graded-injective B-module (see Proposition
15.2.13).
As graded B-modules there are isomorphisms
A ⊗B ∼=
M
p∈N B·tp ∼=
M
p∈N B(−p).
366
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Therefore
J = HomB(A ⊗B, I) ∼=
Y
p∈N I(p)
as graded B-modules, and
Γm(J) ∼= lim
p→
Yp
q=0 I(q)

∼=
M
p∈N I(p).
Now for each p the graded-module Ip is a direct summand of I(p), and hence
L
p∈N Ip is a direct summand of Γm(J), as graded B-modules. Therefore L
p∈N Ip
is a graded-injective B-module.
The conclusion is that a countable direct sum of graded-injective B-modules is
graded-injective. According to the Bass-Papp Theorem [93, Theorem 3.46], that
holds also in the graded sense (cf. Proposition 15.1.26), the graded ring B is noe-
therian. This is a contradiction.
