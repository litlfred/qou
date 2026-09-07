---
doc_id: arxiv-0705.2975v1
doc_title: "On the Definitions of Difference Galois Groups"
section_id: sec-006-more-on-picard-vessiot-rings
section_title: "More on Picard-Vessiot rings"
section_number: null
pages: 20-25
source_pdf: 0705.2975v1.pdf
source_sha256: 683d6bd44cea6704
doc_brief: "On the Definitions of Difference Galois Groups — We compare several deﬁnitions of the Galois group of a linear diﬀerence equation that have arisen in algebra, analysis and model theory and sh ow"
---
Throughout the rest of this section, we ﬁx a diﬀerence ring K, some A ∈ GLn(K), R =
K[Y, det(Y )−1] as above, with σ(Y ) = AY , and R′ =R/q a Picard-Vessiot ring for σ(X) =
AX overK. We denote the image of Y in R′ by y. We keep the notation introduced in
the previous subsections.
Ifq is not a prime ideal, then there exists ℓ and a prime σℓ-idealp ofR which is a maximal
σℓ-ideal of R, such that q = ⋂ ℓ−1
i=0σi(p), and R′ ≃ ⊕ ℓ−1
i=0Ri, where Ri = R/σi(p) (see
Corollary 1.16 of [23]. One veriﬁes that the second proof does not us e the fact that CK
is algebraically closed). Thus the σℓ-diﬀerence ring R0 is a Picard-Vessiot ring for the
diﬀerence equation σℓ(X) = σℓ−1(A) · · ·σ(A)AX overK. We denote σℓ−1(A) · · ·σ(A)A by
Aℓ.
We will identify R′ with ⊕ℓ−1
i=0Ri, and denote by ei the primitive idempotent of R′ such
that eiR′ = Ri. Then ei = σi(e0). We will denote by R∗ the ring of quotients of R′, i.e.,
R∗ = ⊕ℓ−1
i=0R∗
i , where R∗
i is the ﬁeld of fractions of Ri. The diﬀerence ring R∗ is also called
the total Picard-Vessiot ring of σ(X) = AX over K. There are two numerical invariants
associated to R′: the number ℓ = ℓ(R′), and the number m(R′) which is the product of
ℓ(R′) with [ DR∗
0 : DKCR∗
0]. We call m(R′) the m-invariant of R′. We will be considering
other Picard-Vessiot rings for σ(X) = AX, and will use this notation for them as well.
Recall that the Krull dimension of a ring S is the maximal integer n (if it exists) such
that there is a (strict) chain of prime ideals of S of length n. We denote it by Kr .dim(S).
If S is a domain, and is ﬁnitely generated over some subﬁeld k, then Kr .dim(S) equals
the transcendence degree over k of its ﬁeld of fractions. Observe that if S is a domain of
ﬁnite Krull dimension, and 0 ⁄=I is an ideal of S, then Kr.dim(S)> Kr.dim(S/I). Also, if
S = ⊕iSi, then Kr.dim(S) = sup {Kr.dim(Si)}.
Lemma 4.5 1. CR′ is a ﬁnite algebraic extension of CK, and is linearly disjoint from
K over CK (inside R′).
2. If CR′ ⊗CK DK is a domain, then R′ is a Picard-Vessiot ring for σ(X) = AX over
KC R′.
20
Proof. 1. We know by Lemma 1.7 of [23] that CR′ is a ﬁeld. Assume by way of contradic-
tion thatCR′ andK are not linearly disjoint over CK, and choose n minimal such that there
are a1,...,a n ∈ CR′ which are CK-linearly independent, but not K-linearly independent.
Let 0 ⁄= c1,...,c n ∈ K be such that ∑ n
i=1aici = 0. Multiplying by c−1
1 , we may assume
c1 = 1. Then σ(∑ n
i=1aici) = ∑ n
i=1aiσ(ci) = 0, and therefore ∑ n
i=2ai(σ(ci) −ci) = 0. By
minimality of n, all (σ(ci) −ci) are 0, i.e., all ci ∈CK, which gives us a contradiction.
Observe that e0CR′ ⊂Fix (σℓ)(R0), and we may therefore replace R′ by the domain R0.
Since R0 is a ﬁnitely generated K-algebra, we know that its Krull dimension equals the
transcendence degree over K of its ﬁeld of fractions. Thus R0 cannot contain a subﬁeld
which is transcendental over K, i.e., the elements of Fix (σℓ)(R0) are algebraic over K. his
furthermore implies that Fix (σℓ)(R0) is an algebraic extension of Fix (σℓ)(K). Since the
latter ﬁeld is an algebraic extension of CK, we have the conclusion.
2. Our hypothesis implies that K[CR′] is a ﬁeld. Hence R′ is a simple diﬀerence ring
containingKC R′, and is therefore a Picard-Vessiot ring for σ(X) = AX overKC R′.
Lemma 4.6 1. CR′ =CR∗.
2. Fix (σℓ)(e0R∗) = e0CR′.
3. DR∗ = ⊕ℓ−1
i=0DeiR∗.
Proof. 1. If c ∈ CR∗, then c can be represented by some ℓ-tuple ( a0
b0
,..., aℓ−1
bℓ−1
), where
ai,b i ∈Ri, and bi ⁄= 0. Thus the ideal I = {d ∈R′ |dc ∈R′} is a σ-ideal of R′ and contains
the element b = (b0,...,b ℓ−1) ⁄= 0. Since R′ is simple, 1 ∈I, i.e., c ∈R′.
2. Assume that a ∈e0R∗ satisﬁes σℓ(a) = a. Then a =e0a, ∑ ℓ−1
i=0σi(e0a) is ﬁxed by σ, and
therefore belongs to CR′. Hence a ∈e0CR′.
3. If a ∈R∗ satisﬁes σm(a) = a for some m, then σmℓ(eia) = eia.
Remark 4.7 Observe that ℓ and the isomorphism type of the K-σℓ-diﬀerence algebra R0
completely determine the isomorphism type of the diﬀerence algebra R′. Indeed, for each
i = 1,...,ℓ − 1, one chooses a copy Ri of the domain R0, together with an isomorphism
fi :R0 →Ri which extends σi onK. This fi then induces an automorphism σℓ ofRi. One
then deﬁnes σ on ⊕ℓ−1
i=0Ri by setting σ(a0,...,a ℓ−1) = (f1(a0),f 2f −1
1 (a1),...,σ ℓf −1
ℓ−1(aℓ−1)).
Proposition 4.8 LetK ⊂K1 be diﬀerence ﬁelds of characteristic 0 whereK1 =K(CK1),
and assume that CK =DK. Then R′ ⊗KK1 = ⊕d
i=1R′
i, where each R′
i is a Picard-Vessiot
ring for σ(X) = AX over K1, and d ≤ [CR′ : CK]. Moreover, each R′
i has the same
Krull-dimension and m-invariant as R′.
Proof. Our assumption implies that K ⊗CK CK1 is a domain. Let C be the relative
algebraic closure of CK in CK1. Then K(C) = K[C], and R′ ⊗KK(C) ≃R′ ⊗CK C.
21
Leta ∈CR′ be such that CR′ =CK(a) and let f (X) ∈CK[X] be its minimal polynomial
overCK. Let g1(X),...,g d(X) be the irreducible factors of f (X) over C. Then f (X) =∏ d
i=1gi(X), and C ′
R ⊗CKC ≃ ⊕ d
i=1Ci, where Ci is generated over C by a root of gi(X) = 0.
Indeed, identifying C with 1 ⊗C, every prime ideal of CR′ ⊗CK C must contain some
gi(a ⊗ 1); on the other hand, each gi(a ⊗ 1) generates a maximal ideal of CR′ ⊗CKC. Thus
R′ ⊗CK C ≃R′ ⊗CR′ (CR′ ⊗CK C) ≃ ⊕ d
i=1R′ ⊗CR′ Ci.
By Lemmas 2.3 and 4.5, each R′ ⊗CR′ Ci = R′
i is a simple diﬀerence ring, with ﬁeld of
constants Ci. Hence R′
i is a Picard-Vessiot ring for σ(X) = AX over KC (and also over
KC i). Note that d ≤ deg(f ) = [ CR′ : CK], and that Kr .dim(R′
i) = Kr .dim(R′) (because
KC is algebraic over K, and R′
i is ﬁnitely generated over K).
By Proposition 2.4, R′
i ⊗KC i K1Ci is a Picard-Vessiot ring. Because Ci and K1 are
linearly disjoint over C, and Ci is algebraic over C, KC i ⊗KC K1 ≃K1Ci, and therefore
R′
i ⊗KC K1 ≃R′
i ⊗KC iK1Ci.
This shows that R′ ⊗KK1 is the direct sum of Picard-Vessiot rings over K1.
IdentifyingCR′ with ejCR′ =CRj , we obtain
R′
i = (⊕ℓ−1
j=0Rj) ⊗CR′ Ci ≃ ⊕ ℓ−1
j=0Rj ⊗CR′ Ci.
Each Rj being a Picard-Vessiot ring for σℓ(X) = AℓX, we know by Proposition 2.4 that
Rj ⊗CR′ Ci is also a Picard-Vessiot ring for σℓ(X) = AℓX. Thus R0 ⊗CR′ Ci = ∑ s−1
j=0Sj,
where each Sj is a simple σℓs-diﬀerence ring, and a domain. Because all rings Rj are
isomorphic over CR′, and all Sj are isomorphic over CR′, m(R′
i) is the product of ℓs with
m(S0) = [DS∗
0 :CS∗
0 ], where S∗
0 is the ﬁeld of fractions of S0. To show that m(R′
i) = m(R′),
it therefore suﬃces to show that sm(S0) = m(R0). By Lemma 4.5.2, Fix (σℓs)(S∗
0 ) =
Fix (σℓ)(R∗
0 ⊗CR′ Ci) = Fix (σ)(R′ ⊗CR′ Ci) = Ci.
We know that DR∗
0 is a (cyclic) Galois extension of CR′ =Fix (σℓ)(R∗
0), and is therefore
linearly disjoint from Ci overDR∗
0 ∩Ci =C ′
i. Write C ′
i =CR′(α), and let a,b ∈R0, b ⁄= 0,
be such that (inside R∗
0), CR′(a/b) = C ′
i. The minimal prime ideals of R0 ⊗CR′ Ci are the
ideals Q0,...,Q r−1, where r = [C ′
i : CR′] and Qk is generated by σkℓ(a) ⊗ 1 −σkℓ(b) ⊗α.
This shows that r =s, since s is also the number of minimal prime ideals of R0 ⊗CR′ Ci.
Let e be a primitive idempotent of R0 ⊗CR′ Ci such that S0 = e(R0 ⊗CR′ Ci). Then
eCiDR∗
0 is a subﬁeld of S∗
0, contained in DS∗
0 , and its degree over eCi =Fix (σℓs)(S∗
0) is the
quotient of [DR∗
0 :CR′] by [C ′
i :CR′], i.e., equals m(R0)/s. To ﬁnish the proof, it therefore
suﬃces to show that DS∗
0 =eCiD∗
R0.
Assume that c ∈R∗
0 ⊗CR′ Ci satisﬁes σm(c) = c for some m ⁄= 0. Write c = ∑
kak ⊗ck,
where the ak are in R∗
0, and the ck are in Ci and are linearly independent over CR′. Then
σm(c) = c = ∑
kσm(ak)ck, which implies σm(ak) = ak for all k, and all ak’s are in DR∗
0 .
22
As every element of DS∗
0 is of the form ec for such a c (Lemma 4.6.3), this shows that
DS∗
0 =eCiD∗
R0. This ﬁnishes the proof that m(R′
i) = m(R′).
Consider now R′ ⊗KC K1. It is the direct sum of ℓs σℓs-diﬀerence rings, each one being
isomorphic to S0 ⊗KCK1. Because K1 is a regular extension of KC ,S0 ⊗KCK1 is a domain,
of Krull dimension equal to Kr .dim(S0) = Kr.dim(R′). Inside its ﬁeld of fractions (a σℓs-
diﬀerence ﬁeld) K1 and S∗
0 are linearly disjoint over KC , which implies that CK1Ci is the
ﬁeld of constants of S0 ⊗KC K1, CK1DS∗
0 is the ﬁeld of elements ﬁxed by some power of σ,
and [CK1DS∗
0 :CK1Ci] = [D∗
S0 :Ci] = m(S0). This shows that m(R′
i ⊗KC K1) = m(R′) and
ﬁnishes the proof.
Proposition 4.9 Assume that CK =DK. Then all Picard-Vessiot rings for σ(X) = AX
over K have the same Krull dimension and the same m-invariant.
Proof. Let C be the algebraic closure of CK, and let R′′ be a Picard-Vessiot ring for
σ(X) = AX over K. By Proposition 4.8, R′ ⊗K KC is the direct sum of ﬁnitely many
Picard-Vessiot rings for σ(X) = AX overKC , and each of these rings has the same Krull
dimension and m-invariant as R′. The same statement holds for R′′. On the other hand,
by Proposition 1.9 of [23], all Picard-Vessiot rings over KC are isomorphic.
Corollary 4.10 Assume DK = CK. Let R′′ = K[V, det(V )−1], where σ(V ) = AV , and
assume that Kr.dim(R′′) = Kr.dim(R′) and that R′′ has no nilpotent elements. Then R′′ is
a ﬁnite direct sum of Picard-Vessiot rings for σ(X) = AX.
Proof. Because R′′ has no nilpotent elements and is Noetherian, (0) is the intersection
of the ﬁnitely many prime minimal ideals of R′′. Let P be the set of minimal prime ideals
of R′′. Then the intersection of any proper subset of P is not (0), i.e., no element of P
contains the intersection of the other elements of P. Also, if P ∈ P , then σ(P ) ∈ P ,
and there exists m > 0 such that σm(P ) = P . Then IP = ⋂ m−1
i=0 σi(P ) is a σ-ideal,
which is proper if the orbit of P under σ is not all of P. Observe that for each P ∈ P ,
Kr.dim(R′′/P ) ≤ Kr.dim(R′′/IP ) ≤ Kr.dim(R′′) = Kr .dim(R′), and that for some P we
have equality.
If I is a maximal σ-ideal of R′′, then Kr .dim(R′′/I) = Kr .dim(R′) = Kr .dim(R′′) by
Proposition 4.8, and this implies that I is contained in some P ∈ P . Hence I = IP and
R′′/IP is a Picard-Vessiot ring. If I = (0), then we are ﬁnished. Otherwise, P contains some
elementP1 not in the orbit of P under σ. Observe that IP1 is contained in some maximal
σ-ideal of R′′, and is therefore maximal, by the same reasoning. Since the interse ction of
any proper subset of P is non-trivial, IP +IP1 is a σ-ideal of R′′ which contains properly
IP , and therefore equals 1. If P1,...,P r are representatives from the σ-orbits in P, the
Chinese Remainder Theorem then yields R′′ ≃ ⊕ r
i=1R′′/IPi.
23
Proposition 4.11 Assume CK =DK. Then KC L[R] is a Picard-Vessiot ring for σ(X) =
AX over KC L,
Kr.dim(R′) = tr.deg(L/KC L), and [DL :CL] = m(R′).
Proof. Let us ﬁrst assume that R′ is a domain. There is some generic diﬀerence ﬁeld U
containing R′ and its ﬁeld of fractions R∗, and which is suﬃciently saturated. Because L
is a regular extension of K, there is some K-embedding ϕ of L into U, and we will denote
byT the image of Y in U, and by y the image of Y in R′. Then ϕ(CL) ⊂CU , and there is
some B ∈ GLn(CU ) such that T =yB. Hence
KC U [T, det(T )−1] = KC U [y, det(y)−1].
By Proposition 4.8, R′ ⊗K KC U is a direct sum of Picard-Vessiot rings of σ(X) = AX
over KC U , and clearly one of those is the domain KC U [y, det(y)−1]. Thus Kr .dim(R′) =
tr.deg(R∗/K) = tr.deg(L/KC L), DR∗CU =ϕ(DL)CU , and m(R′) = [DL :CL].
This implies also that Kϕ(CL)[T, det(T )−1] is a simple diﬀerence ring, and therefore
a Picard-Vessiot ring for σ(X) = AX over Kϕ(CL). Hence KC L[R] is a Picard-Vessiot
extension for σ(X) = AX overKC L.
In the general case, we replace R′ byR0,σ byσℓ, ﬁnd some generic suﬃciently saturated
σℓ-diﬀerence ﬁeld U containingR0, and a K-embeddingϕ of theσℓ-diﬀerence domain L into
U, and conclude as above that KFix (σℓ)[R0] = KFix (σℓ)[ϕ(R)], that the Krull dimension
of R′ equals tr.deg(L/KC L), and that m(R0) = [Fix (σℓ)(ϕ(DL)) : Fix (σℓ)].
Because K and DL are linearly disjoint over CK, [KD L : KC L] = [ DL : CL], whence
DKC L =KC L, and by Corollary 4.10, the diﬀerence domain KC L[R] is a simple diﬀerence
ring, i.e., a Picard-Vessiot ring for σ(X) = AX over KC L. By Proposition 4.8 m(R′) =
[DL :CL].
We have m(R′) = ℓm(R0), and m(R0) is the quotient of [ DL : CL] by the greatest
common divisor of [ DL :CL] and ℓ.
Corollary 4.12 Assume that CK =DK. Let R′′ =K[V, det(V )−1] be a diﬀerence domain,
where σ(V ) = AV , with ﬁeld of fractions L1, and assume that CL1 is a ﬁnite algebraic
extension of CK. Then R′′ is a Picard-Vessiot ring for σ(X) = AX over K.
Proof. Let U be a suﬃciently saturated generic diﬀerence ﬁeld containing R′′, and let
ϕ be a K-embedding of L into U. Then KC U [ϕ(R)] = KC U [R′′]. Hence Kr .dim(R′′) =
Kr.dim(R′) and R′′ is a Picard-Vessiot ring by Corollary 4.10.
Corollary 4.13 Assume that CK is algebraically closed. Then ℓ(R′) = [DL :CL].
Proof. Immediate from Proposition 4.11 and the fact that DR∗ =CR′ =CK.
24
Corollary 4.14 The diﬀerence ring KC L[R] is a Picard-Vessiot ring for σ(X) = AX over
KC L. All Picard-Vessiot rings for σ(X) = AX over K have the same Krull dimension,
which equals tr.deg(L/KC L).
Proof. Let m = [DK : CK]. Note that replacing σ by some power of σ does not change
the ﬁelds DK or DL, and that Fix (σm)(K) = DK. Therefore we can apply the previous
results to the equation σm(X) = AmX overK. By Corollary 4.12 and because KC L[R] is
a domain, KC L[R] is a Picard-Vessiot ring for σm(X) = AmX overKC L, and therefore a
simple σm-diﬀerence ring, whence a simple σ-diﬀerence ring, and ﬁnally a Picard-Vessiot
ring for σ(X) = AX overK.
Let R′ = R/q be a Picard-Vessiot ring for σ(X) = AX over K. Assume ﬁrst that R′
is a domain, and let U be a generic diﬀerence ﬁeld containing it. Because L is a regular
extension of K, there is a K-embedding ϕ of L into U, and from KC U [ϕ(R)] = KC U [R′]
and Lemma 4.5.1, we obtain the result. If R′ is not a domain, then we reason in the same
fashion, replacing R′ byR0 and σ byσℓ, to obtain the result.
Proposition 4.15 Assume that CR′ = CK = DK and K ⊂ U . Then GR′ and H are
isomorphic.
Proof. By Proposition 2.4, we may replace R′ by R′ ⊗K KD ′
U , and consider the ring
Kϕ(CL)[T, det(T )−1] ⊗Kϕ(CL)KD ′
U , which is a Picard-Vessiot ring by Proposition 4.11 and
Corollary 4.10. We identify 1 ⊗KD ′
U with KD ′
U . These two rings are isomorphic over
KD ′
U by Proposition 1.9 of [23], and it therefore suﬃces to show that
Aut(ϕ(L) ⊗Kϕ(CL)KD ′
U/KD ′
U ) = H(D′
U ).
Insideϕ(L)⊗Kϕ(CL)KD ′
U ,ϕ(L)⊗1 and KD ′
U are linearly disjoint over Kϕ(CL). Hence, the
algebraic loci of ( T, det(T )−1) over Kϕ(CL) and over KD ′
U coincide. As H was described
as the subgroup of GL n which leaves this algebraic set invariant, we get the result.
