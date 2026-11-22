---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-104-153-resolutions-and-derived-functors
section_title: "Resolutions and Derived Functors"
section_number: 15.3
pages: 338-345
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
Conventions 15.1.17 and 15.2.1. Thus K is a base ﬁeld and ⊗= ⊗K. In the next
deﬁnitions we collect the algebraically graded versions of some deﬁnitions from
Sections 10 and 11.
Deﬁnition 15.3.1. Let A be a graded ring, and let P ∈C(A, gr).
(1) The complex P is called a graded-free complex if all the graded A-modules
P i are graded-free, and the diﬀerential is zero.
(2) The complex P is called a semi-graded-free complex if it admits a ﬁltration
{Fj(P)}j≥−1 in Cstr(A, gr), such that F−1(P) = 0, P = S
j Fj(P), and
GrF
j (P) is a graded-free complex for every j.
(3) The complex P is called a K-graded-projective complex if for every acyclic
complex N ∈C(A, gr), the complex HomA(P, N) is acyclic.
Deﬁnition 15.3.2. Let A be a graded ring, and let I ∈C(A, gr).
(1) The complex I is called a graded-cofree complex if all the A-modules Ip are
graded-cofree, and the diﬀerential is zero.
(2) The complex I is called a semi-graded-cofree complex if it admits a coﬁl-
tration {Fq(I)}q≥−1 in Cstr(A, gr), such that F−1(I) = 0, each GrF
q (I) is
graded-cofree complex, and I = lim←q Fq(I).
(3) The complex I is called a K-graded-injective complex if for every acyclic
complex N ∈C(A, gr), the complex HomA(N, I) is acyclic.
Deﬁnition 15.3.3. A complex P ∈C(A, gr) is called a K-graded-ﬂat complex if
for every acyclic complex N ∈C(Aop, gr) the complex N ⊗A P is acyclic.
Theorem 15.3.4. Let A be a graded ring, and let M ∈C(A, gr).
(1) There exists a quasi-isomorphism ρ : P →M in Cstr(A, gr), where P is a
semi-graded-free complex, and sup(P) = sup(H(M)).
(2) There exists a quasi-isomorphism ρ : M →I in Cstr(A, gr), where I is a
semi-graded-cofree complex, and inf(I) = inf(H(M)).
Proof.
(1) This is a modiﬁcation of Theorem 11.4.17 and Corollary 11.4.27. The proof is
the same, after a few obvious modiﬁcations.
(2) This is a modiﬁcation of Theorem 11.6.24 and Corollary 11.6.31. The proof is
the same, after a few obvious modiﬁcations. The injective object K∗we use here is
K∗:= K of course.
□
The various kinds of complexes mentioned in the deﬁnitions above are related
as follows.
Theorem 15.3.5. Let A be a graded ring.
(1) A complex P ∈C(A, gr) is K-graded-projective if and only if it is isomorphic
in K(A, gr) to a semi-graded-free complex Q.
(2) If P ∈C(A, gr) is K-graded-projective, then it is K-graded-ﬂat.
(3) If P ∈C(A, gr) is K-graded-projective, then P ∗∈C(Aop, gr) is K-graded-
injective.
(4) A complex I ∈C(A, gr) is K-graded-injective iﬀit is isomorphic in K(A, gr)
to a semi-graded-cofree complex J.
Proof.
(1) By Theorem 11.4.14, that applies to this context too, a semi-graded-free complex
Q is K-graded-projective. And by Proposition 10.2.3, a complex P ∈C(A, gr) is K-
graded-projective iﬀHomK(A,gr)(P, N) = 0 for every acyclic complex N ∈C(A, gr).
338
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
First let’s assume that there is an isomorphism P ∼= Q in K(A, gr) to a semi-
graded-free complex Q. Then for every acyclic complex N ∈C(A, gr) we get
HomK(A,gr)(P, N) ∼= HomK(A,gr)(Q, N) = 0.
Therefore P is K-graded-projective.
Conversely, let’s assume that P is K-graded-projective. By Theorem 15.3.4(1)
there is a quasi-isomorphism ρ : Q →P in Cstr(A, gr) from a semi-graded-free
complex Q. By Corollary 10.2.14, P(ρ) : Q →P is an isomorphism in K(A, gr).
(2) Take N ∈C(Aop, gr). We have the adjunction isomorphism
(N ⊗A P)∗= HomK(N ⊗A P, K)
∼= HomA(P, HomK(N, K)) = HomA(P, N ∗)
in Cstr(K, gr). If N is acyclic then so are N ∗, HomA(P, N ∗) and (N ⊗A P)∗. Since
the functor (−)∗is faithfully exact, we see that N ⊗A P is acyclic too. Therefore
P is K-graded-ﬂat.
(3) Take N ∈C(Aop, gr). We have the adjunction isomorphism
HomAop(N, P ∗) = HomAop(N, HomK(P, K))
∼= HomK(N ⊗A P, K) = (N ⊗A P)∗
in Cstr(K, gr). By item (2) P is K-graded-ﬂat. If N is acyclic then so are N ⊗A P,
(N ⊗A P)∗and HomAop(N, P ∗). Therefore P ∗is K-graded-injective.
(4) By Theorem 11.6.21, that applies to this context too, a semi-graded-cofree com-
plex J is K-graded-injective. And by Proposition 10.1.3, a complex I ∈C(A, gr) is
K-graded-injective iﬀHomK(A,gr)(N, I) = 0 for every acyclic complex N ∈C(A, gr).
First let’s assume that there is an isomorphism I ∼= J in K(A, gr) to a semi-
graded-cofree complex J. Then for every acyclic complex N ∈C(A, gr) we get
HomK(A,gr)(N, I) ∼= HomK(A,gr)(N, J) = 0.
Therefore I is K-graded-injective.
Conversely, let’s assume that I is K-graded-injective. By Theorem 15.3.4(2) there
is a quasi-isomorphism ρ : I →J in Cstr(A, gr) to a semi-graded-cofree complex J.
By Corollary 10.1.19, P(ρ) : I →J is an isomorphism in K(A, gr).
□
The next proposition tells us that some resolving properties of complexes are
preserved by the restriction functor C(A ⊗B, gr) →C(A, gr).
Proposition 15.3.6. Let A and B be graded rings.
(1) If P ∈C(A ⊗B, gr) is K-graded-projective, then it is K-graded-projective
in C(A, gr).
(2) If P ∈C(A ⊗B, gr) is K-graded-ﬂat, then it is K-graded-ﬂat in C(A, gr).
(3) If I ∈C(A ⊗B, gr) is K-graded-injective, then it is K-graded-injective in
C(A, gr).
Proof.
(1) Take N ∈C(A, gr). We have isomorphisms
HomA(P, N) ∼= HomA⊗B(P, HomA(A ⊗B, N))
∼= HomA⊗B(P, HomK(B, N))
in Cstr(K, gr). As an object of C(K, gr), B is K-graded-projective. Hence, if N is
acyclic, then so is HomA(P, N).
(2, 3) Like item (1), but using the fact that B is K-graded-ﬂat over K, and using
other adjunction isomorphisms.
□
Corollary 15.3.7. Let A and B be graded rings, and let M ∈C(A ⊗B, gr).
339
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(1) There exists a quasi-isomorphism P →M in Cstr(A ⊗B, gr), where P is a
K-graded-projective complex over A, every P i is a graded-projective module
over A, and sup(P) = sup(H(M)).
(2) There exists a quasi-isomorphism P →M in Cstr(A ⊗B, gr), where P is
a K-graded-ﬂat complex over A, every P i is a graded-ﬂat module over A,
and sup(P) = sup(H(M)).
(3) There exists a quasi-isomorphism M →I in Cstr(A ⊗B, gr), where I is
a K-graded-injective complex over A, every Ip is a graded-injective module
over A, and inf(I) = inf(H(M)).
Proof.
(1) Take the resolution P →M from Theorem 15.3.4(1).
In view of Theorem
15.3.5(1), Proposition 15.3.6(1) and Proposition 15.2.6(2), the complex P has the
required properties.
(2) Use item (1), plus Theorem 15.3.5(2).
(3) Take the resolution M →I from Theorem 15.3.4(2). This will do, by Theorem
15.3.5(4), Proposition 15.3.6(3), Proposition 15.2.11(3) and Proposition 15.2.13(3).
□
Corollary 15.3.8. Let A, B and C be graded rings.
(1) The triangulated right derived bifunctor
RHomA(−, −) : D(A ⊗Bop, gr)op × D(A ⊗Cop, gr) →D(B ⊗Cop, gr)
exists.
(2) Let M ∈D(A ⊗Bop, gr) and N ∈D(A ⊗Cop, gr). Assume that either M
is K-graded-projective over A, or N is K-graded-injective over A. Then the
morphism
ηR
M,N : HomA(M, N) →RHomA(M, N)
in D(B ⊗Cop, gr) is an isomorphism.
(3) Let B′ →B and C′ →C be graded K-ring homomorphisms. Then the
diagram
D(A ⊗Bop, gr)op × D(A ⊗Cop, gr)
RHomA(−,−)
/
Rest ×
Rest

D(B ⊗Cop, gr)
Rest

D(A ⊗B′ op, gr)op × D(A ⊗C′ op, gr)
RHomA(−,−) / D(B′ ⊗C′ op, gr)
is commutative up to isomorphism.
Proof. The same arguments used in the proof of Proposition 14.3.15 work here,
because there exist enough acyclic resolutions – see Corollary 15.3.7.
□
Corollary 15.3.9. The category D(A, gr) has inﬁnite direct sums. On objects, the
direct sum is degreewise, for the Z2 grading.
Proof. The proof of Theorem 10.1.26 works here.
□
Corollary 15.3.10. Let A, B and C be graded rings.
(1) The triangulated left derived bifunctor
(−⊗L
A −) : D(B ⊗Aop, gr) × D(A ⊗Cop, gr) →D(B ⊗Cop, gr)
exists.
340
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(2) Let M ∈D(B ⊗Aop, gr) and N ∈D(A⊗Cop, gr). Assume that either M is
K-graded-ﬂat over Aop, or N is K-graded-ﬂat over A. Then the morphism
ηL
M,N : M ⊗L
A N →M ⊗A N
in D(B ⊗Cop, gr) is an isomorphism.
(3) Let B′ →B and C′ →C be graded K-ring homomorphisms. Then the
diagram
D(B ⊗Aop, gr) × D(A ⊗Cop, gr)
(−⊗L
A−)
/
Rest ×
Rest

D(B ⊗Cop, gr)
Rest

D(B′ ⊗Aop, gr) × D(A ⊗C′ op, gr)
(−⊗L
A−) / D(B′ ⊗C′ op, gr)
is commutative up to isomorphism.
Proof. The same arguments used in the proof of Proposition 14.3.13 work here,
because there exist enough acyclic resolutions – see Corollary 15.3.7.
□
Corollary 15.3.11. Let A, B and C be graded rings.
(1) Given M ∈M(A ⊗Bop, gr) and N ∈M(A ⊗Cop, gr), for every p ∈N there
is a canonical isomorphism
Extp
A(M, N) ∼= Hp RHomA(M, N)

in M(B ⊗Cop, gr).
Here Extp
A(−, −) is the classical p-th right derived
bifunctor of HomA(−, −).
(2) Given M ∈M(B ⊗Aop, gr) and N ∈M(A ⊗Cop, gr), for every p ∈N there
is a canonical isomorphism
TorA
p (M, N) ∼= H−p M ⊗L
A N

in M(B ⊗Cop, gr). Here TorA
p (−, −) is the classical p-th left derived bi-
functor of (−⊗A −).
Proof. This is clear from Corollary 15.3.8(2) and Corollary 15.3.10(2) respectively.
□
Corollary 15.3.12. Let A, B, C and D be graded rings.
(1) Let L ∈D(A ⊗Bop, gr), M ∈D(B ⊗Cop, gr) and N ∈D(C ⊗Dop, gr).
There is an isomorphism
L ⊗L
B (M ⊗L
C N) ∼= (L ⊗L
B M) ⊗L
C N
in D(A ⊗Dop, gr). This isomorphism is functorial in L, M, N.
(2) Let L ∈D(B ⊗Aop, gr), M ∈D(C ⊗Bop, gr) and N ∈D(C ⊗Dop, gr).
There is an isomorphism
RHomB
 L, RHomC(M, N)
 ∼= RHomC(M ⊗L
B L, N)
in D(A ⊗Dop, gr). This isomorphism is functorial in L, M, N.
Proof. Both assertions are immediate consequences of the associativity of the tensor
product for modules, and the Hom-tensor adjunction for modules.
□
The triangulated category D(Aen, gr) has a biclosed monoidal structure on it,
with monoidal operation (−⊗L
A −) and monoidal unit A. See Remark 14.3.23 for
the nongraded variant. In the next deﬁnition we present the pertinent operations
related to this structure; these will be needed for several constructions. We do
not need to know anything about the concept of monoidal structure beyond this
terminology. The interested reader can look it up in [102]; the previous corollaries
(almost) guarantee that the monoidal axioms hold in this context.
341
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Deﬁnition 15.3.13 (Monoidal Operations). Let A and B be graded rings, and let
M ∈D(A ⊗Bop, gr) and N ∈D(B ⊗Aop, gr) be complexes.
(1) The left unitor isomorphism for M is the obvious isomorphism lu : A ⊗L
A
M
≃
−→M in D(A ⊗Bop, gr).
(2) The right unitor isomorphism for N is the obvious isomorphism ru : N ⊗L
A
A
≃
−→N in D(B ⊗Aop, gr).
(3) The left co-unitor isomorphism for M is the obvious isomorphism lcu :
RHomA(A, M)
≃
−→M in D(A ⊗Bop, gr).
Here is a notion that is dual to a minimal complex of injectives (see Deﬁnition
13.2.5). Recall that for a complex P, the module of degree i coboundaries is Bi(P) =
Im
 di−1
P
: P i−1 −→P i
⊆P i.
Deﬁnition 15.3.14. Let A be a connected graded ring, with augmentation ideal
m. A minimal complex of graded-free A-modules is a bounded above complex P,
such that for every i the graded module P i is graded-free, and there is an inclusion
Bi(P) ⊆m·P i.
Proposition 15.3.15. Let A be a connected graded ring, and let P be a bounded
above complex of graded-free A-modules. The following conditions are equivalent:
(i) P is a minimal complex of graded-free A-modules.
(ii) The complex K ⊗A P has zero diﬀerential.
Exercise 15.3.16. Prove this proposition.
Deﬁnition 15.3.17. Let A be a connected graded ring, and let M ∈M(A, gr).
A minimal graded-free resolution of M is a quasi-isomorphism ρ : P →M in
Cstr(A, gr) from a minimal complex of graded-free A-modules P.
Proposition 15.3.18. Let A be a connected graded ring, and let M ∈M(A, gr) be
a bounded below graded module. Then:
(1) M has a minimal graded-free resolution η : P →M.
(2) For every i there is an isomorphism P i ∼= A ⊗TorA
−i(K, M) in M(A, gr).
(3) The minimal graded-free resolution η : P →M in item (1) above is unique,
up to a non-unique isomorphism in Cstr(A, gr).
Proof.
(1) Let V0 := K ⊗A M and P 0 := A ⊗V0.
By Proposition 15.2.30 there is a
surjection η : P 0 →M.
Let M −1 := Ker(η) ⊆P 0.
By construction we have
M −1 ⊆m ⊗V0 = m·P 0. And of course M −1 is a bounded below graded A-module.
Next let V1 := K ⊗A M −1 and P −1 := A ⊗V1. By Proposition 15.2.30 there
is a surjection d−1 : P −1 →M −1. The graded module M −2 := Ker(d−1) ⊆P −1
satisﬁes M −2 ⊆m ⊗V1 = m·P −1. And so on.
(2) Due to minimality, the diﬀerential of the complex K⊗AP is zero; see Proposition
15.3.15. Therefore
TorA
−i(K, M) ∼= Hi(K ⊗L
A M) ∼= Hi(K ⊗A P) ∼= K ⊗A P i ∼= V−i.
(3) Suppose η′ : P ′ →M is some other minimal graded-free resolution. Because P
and P ′ are K-projective in C(A, gr), there is a homotopy equivalence φ : P →P ′
in Cstr(A, gr). Therefore
(15.3.19)
id ⊗φ : K ⊗A P →K ⊗A P ′
is a quasi-isomorphism.
But by Proposition 15.3.15, these complexes have zero
diﬀerentials, so (15.3.19) is an isomorphism in Cstr(K, gr). The graded Nakayama
Lemma (Proposition 15.2.30(3)) implies that φ : P →P ′ is an isomorphism in
Cstr(A, gr).
□
342
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Exercise 15.3.20. Try to generalize Proposition 15.3.18 to a complex M ∈
C(A, gr). The trick is to ﬁnd the correct boundedness conditions on M.
Corollary 15.3.21. Assume A is a left noetherian connected graded ring, and M
is a ﬁnite graded A-module. Then in the minimal graded-free resolution η : P →M,
the graded-free A-modules P i are all ﬁnite.
Proof. In the proof of Proposition 15.3.18(1), the graded K-modules Vi are all
ﬁnite.
□
Here is a graded version of Deﬁnitions 11.4.29 and 12.9.1.
Deﬁnition 15.3.22. Let A be a graded ring.
(1) A complex P ∈C(A, gr) is called pseudo-ﬁnite semi-graded-free if it is a
bounded above complex of ﬁnite graded-free A-modules.
(2) A complex L ∈D(A, gr) is called derived graded-pseudo-ﬁnite if it belongs
to the saturated full triangulated subcategory of D(A, gr) generated by the
pseudo-ﬁnite semi-graded-free complexes.
Example 15.3.23. If the graded ring A is connected and left noetherian, then
the derived graded-pseudo-ﬁnite complexes over A are precisely the objects of
D−
f (A, gr). See Theorems 11.3.18 or 11.4.40.
Proposition 15.3.24. Assume A is a left noetherian connected graded ring. Con-
sider A as a graded Aen-module. Then in the minimal graded-free resolution ρ :
P →A of A over Aen, the graded-free Aen-modules P i are all ﬁnite.
The subtle point is that the graded ring Aen might not be left noetherian – see
Remark 15.1.30.
Proof. Let us write P i ∼= Aen ⊗V−i, where V−i ∈M(K, gr). We shall prove that all
the V−i are ﬁnite graded K-modules.
When we restrict the quasi-isomorphism ρ : P →A to the category Cstr(Aop, gr),
it becomes a homotopy equivalence. Hence τ := ρ ⊗id : P ⊗A K →A ⊗A K is
a quasi-isomorphism in Cstr(A, gr). Writing Q := P ⊗A K ∈C(A, gr), we get a
graded-free resolution τ : Q →K over A. Note that Qi ∼= A ⊗V−i in Cstr(A, gr).
Now
(15.3.25)
K ⊗A Q ∼= K ⊗A P ⊗A K ∼= K ⊗Aen P
in Cstr(K, gr). Because P is a minimal complex of graded-free Aen-modules, the
complex K ⊗Aen P has zero diﬀerential; see Proposition 15.3.15.
But then the
complex K ⊗A Q has zero diﬀerential. We conclude that Q is a minimal complex of
graded-free A-modules, and hence τ : Q →K is a minimal graded-free resolution
over A. Corollary 15.3.21 says that the graded A-modules Qi are ﬁnite; and hence
the graded K-modules V−i are ﬁnite.
□
Corollary 15.3.26. If A is a left noetherian connected graded ring, then A is a
derived graded-pseudo-ﬁnite complex over Aen.
Proof. This is an immediate consequence of Proposition 15.3.24, which says that
the complex P is pseudo-ﬁnite graded-semi-free over Aen.
□
Theorem 15.3.27. Let A, B, C and D be graded rings.
For complexes L ∈
D(A ⊗Cop, gr), M ∈D(A ⊗Bop, gr) and N ∈D(B ⊗Dop, gr) there is a morphism
evR,L
L,M,N : RHomA(L, M) ⊗L
B N →RHomA(L, M ⊗L
B N)
in D(C ⊗Dop, gr), called derived graded tensor-evaluation. The morphism evR,L
L,M,N
is functorial in the objects L, M, N. Moreover, if all three conditions below hold,
then evR,L
L,M,N is an isomorphism.
343
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(i) The complex L is derived graded-pseudo-ﬁnite over A.
(ii) The complex M has bounded below cohomology.
(iii) The complex N has ﬁnite graded-ﬂat dimension over B.
Just to clarify, condition (ii) says that Hi(M) = 0 for i ≪0. We do not care
about the boundedness (in algebraic degree) of the graded modules Hi(M).
Proof. The proof of just like that of Theorem 12.9.10, but working in the graded
derived categories. For condition (iii), notice that if N has ﬁnite graded-ﬂat di-
mension over B, then there is an isomorphism P ∼= N in D(B, gr), where P is a
bounded complex of graded-ﬂat B-modules.
□
Deﬁnition 15.3.28. Let A be a graded ring.
(1) The full subcategory of D(A, gr) on the complexes M whose cohomology
modules Hp(M) belong to Mdwf(A, gr) is denoted by Ddwf(A, gr).
(2) The full subcategory of D(A, gr) on the complexes whose cohomology mod-
ules belong to Mf(A, gr) is denoted by Df(A, gr).
(3) The full subcategory of D(A, gr) on the complexes whose cohomology mod-
ules belong to Mcof(A, gr) is denoted by Dcof(A, gr).
Because Mdwf(A, gr) is a a thick abelian subcategory of M(A, gr), it follows that
Ddwf(A, gr) is a full triangulated subcategory of D(A, gr). Likewise for Df(A, gr)
when A is left noetherian, and for Dcof(A, gr) when A is right noetherian connected.
Because (−)∗is exact, it induces a triangulated functor
(15.3.29)
(−)∗: D(A, gr)op →D(Aop, gr).
Proposition 15.3.30. Let A be a graded ring.
(1) If M ∈Ddwf(A, gr) then M ∗∈Ddwf(Aop, gr).
(2) The functor
(−)∗: Ddwf(A, gr)op →Ddwf(Aop, gr)
is an equivalence of K-linear triangulated categories.
(3) If A is left noetherian connected, then the functor
(−)∗: Df(A, gr)op →Dcof(Aop, gr)
is an equivalence of K-linear triangulated categories.
Exercise 15.3.31. Prove this proposition.
(Hint: use Proposition 15.2.28 and
Theorem 15.2.34.)
The next result is from [153].
Theorem 15.3.32. Let A, B and C be graded K-rings.
(1) For M ∈D(A ⊗Bop, gr) and N ∈D(A ⊗Cop, gr) there is a morphism
θM,N : RHomA(M, N) →RHomAop(N ∗, M ∗)
in D(B ⊗Cop, gr), that is functorial in M and N.
(2) If M ∈Ddwf(A ⊗Bop, gr) and N ∈Ddwf(A ⊗Cop, gr) then θM,N is an
isomorphism.
Proof.
(1) Choose a K-graded-projective resolution ρ : P →M in Cstr(A ⊗Bop, gr).
By Proposition 15.3.6 the complex P is K-graded-projective over A; so there is a
canonical isomorphism
φρ : RHomA(M, N)
≃
−→HomA(P, N)
in D(B ⊗Cop, gr). K-linear duality gives a homomorphism
˜θP,N : HomA(P, N) →HomAop(N ∗, P ∗)
344
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in Cstr(B ⊗Cop, gr).
Now ρ∗: M ∗→P ∗is a quasi-isomorphism in Cstr(B ⊗Aop, gr), and according
to Proposition 15.3.6(1) and Theorem 15.3.5(3) the the complex P ∗is K-graded-
injective over Aop. Therefore there is a canonical isomorphism
ψρ∗: HomAop(N ∗, P ∗)
≃
−→RHomAop(N ∗, M ∗)
in D(B ⊗Cop, gr). The resulting morphism
θM,N := ψρ∗◦Q(˜θP,N) ◦φρ : RHomA(M, N) →RHomAop(M ∗, N ∗)
in D(B ⊗Cop, gr) is functorial in M and N.
(2) Because the restriction functors between the derived categories are conservative
(see Proposition 14.3.10), we can forget the rings B and C, and just consider θM,N
as a morphism D(K, gr).
For every integer i there is a canonical isomorphism
(15.3.33)
Hi RHomA(M, N)
 ∼= HomDdwf(A,gr)
 M, N[i]

.
Using the isomorphism N ∗[−i] ∼= N[i]∗in D(Aop, gr) we also have
(15.3.34)
Hi RHomAop(N ∗, M ∗)
 ∼= HomDdwf(Aop,gr)
 N ∗, M ∗[i]

∼= HomDdwf(Aop,gr)
 N[i]∗, M ∗
.
The construction of θM,N in the proof of item (1) above shows that the K-linear
homomorphism
Hi(θM,N) : Hi RHomA(M, N)

→Hi RHomAop(N ∗, M ∗)

becomes, after using the isomorphisms (15.3.33) and (15.3.34), the duality mor-
phism
HomDdwf(A,gr)
 M, N[i]

→HomDdwf(Aop,gr)
 N[i]∗, M ∗
.
According to Proposition 15.3.30(2) this is an isomorphism.
□
Remark 15.3.35. In this section, and the two sections following it, we work over
a base ﬁeld K. This simpliﬁes a lot of the constructions. It is however possible to
relax this condition, and to work over a noetherian commutative base ring K that is
not a ﬁeld. But then there are (at least) two complications. The ﬁrst complication
is that we will have to ﬁx an injective cogenerator K∗of M(K); cf. Subsection 11.6.
Matlis Duality will take the form M ∗:= HomK(M, K∗), and HomK(−, −) might
also involve continuity in a delicate way.
The second complication is that for the homological algebra to be eﬀective,
the graded K-rings would have to be ﬂat. The absence of ﬂatness poses serious
diﬃculties. This can be tackled using K-ﬂat DG ring resolutions; and these DG
rings would have to be bigraded (with upper and lower indices, as explained in the
Subsection 15.1). This sort of resolution has not been studied yet, as far as we
know; but cf. [180] for some preliminary ideas.
