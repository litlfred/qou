---
doc_id: arxiv-math-0408210v3
doc_title: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM"
section_id: sec-009-3-the-local-version-of-the-algebraic-index-theor
section_title: "The local version of the algebraic index theorem"
section_number: 3
pages: 12-16
source_pdf: 0408210v3.pdf
source_sha256: 16d5ccb83a86954f
doc_brief: "A SIMPLE ALGEBRAIC PROOF OF THE ALGEBRAIC INDEX THEOREM — In math.QA/0311303 B. Feigin, G. Felder, and B."
---
Let M be either a smooth real symplectic manifold of dimension 2 n or a smooth aﬃne
algebraic variety (over C) of the complex dimension 2 n endowed with an algebraic symplectic
form. Let ∗ be a star-product in the vector space C(M)((ℏ)) of smooth (resp. regular)
functions on M. Throughout this section we denote the algebra ( C(M)((ℏ)), ∗) by A and
the subalgebra (C(M)[[ℏ]], ∗) of A by A+
Due to remark 2 after theorem 2, we may safely assume that ∗ is obtained by Fedosov’s
procedure. Since in this case the vector bundle is trivial the Fedoso v star-product depends
only on the pair (∂s, Ω ℏ), where ∂s is the symplectic connection on M and Ω ℏ ∈ ℏΩ 2(M)[[ℏ]]
is a series of closed two-forms. Let D = ∇ + ℏ−1[A, · ] be the corresponding Fedosov connec-
tion.
For any idempotent P in the matrix algebra glN (A+) we assign the top degree De Rham
cohomology class
cl(P ) = [Ψ D(P )] ∈H 2n(M)((ℏ)), (31)
where D is naturally extended to the Fedosov connection on the Weyl algebr a bundle
W (End(LN )) associated with the trivial bundle LN of rank N .
Due to statements i) and ii) (31) gives a well-deﬁned map
cl : K0(A+) ↦→H 2n(M)((ℏ))
from the K0-group of the algebra A+ to H 2n(M)((ℏ)).
Deﬁnition 6 The zeroth term q =P |ℏ=0 of an idempotent P ∈ glN (A+) is called the prin-
cipal part of P .
It is obvious that q is an idempotent in the matrix algebra glN (C(M)) and the operation of
taking the principal part gives a well-deﬁned principal symbol map
Ξ : K0(A+) ↦→K0(C(M)). (32)
12
Due to the observation of L. Boutet de Monvel and V. Guillemin [4] for any idempotent
q in the matrix algebra glN (C(M)) there exists an idempotent P ∈ glN (A+) whose principal
part is q. (See the explicit formula for P in [9], eq. (6 . 1. 4))
Using standard arguments of the index theory we can prove that t he cohomology class
(31) of an idempotent P ∈ glN (A+) depends only on its principal part. For our purposes we
need a slightly more general statement:
Proposition 3 Let V be a vector bundle over M and ∗ be the Fedosov star-product in
EndV [[ℏ]]. Then if two idempotents P1,P 2 ∈ (EndV [[ℏ]], ∗) have the same principal part
P1
⏐⏐⏐
ℏ=0
=P2
⏐⏐⏐
ℏ=0
,
the cohomology classes [Ψ D(P1)] and [Ψ D(P2)] coincide.
Proof is a straightforward generalization of the arguments in the proof o f theorem 6. 1. 3 in
[9] . ✷
The precise dependence of the cohomology class cl(P ) on the principal part q of P is
given by the local algebraic index theorem
Theorem 4 For any element Π ∈K0(A+) the cohomology class cl(Π) coincides with the top
component of the cup product
cl(Π) =
[
ˆA(M) exp
(
−F
ℏ
)
ch(Ξ(Π))
]
2n
,
of the ˆA-genus of M, the exponent e− F
ℏ of the Deligne-Fedosov class
F =
[
−ω + Ω ℏ
]
of the star-product in A+ and the Chern character ch(Ξ(Π)) of the principal symbol Ξ(Π) of
Π .
Proof. Let P be an idempotent in the matrix algebra glN (A+) and q ∈ glN (C(M)) be the
principal part of P . As an idempotent endomorphism of the trivial bundle LN or rank N, q
deﬁnes a subbundle E =Imq ⊂LN .
It suﬃces to prove that the 2 n-form Ψ D(P ) has the same cohomology class as the 2 n-th
component of the form
det
( R/ 2
sinh (R/ 2)
) 1/ 2
exp
( ω − Ω ℏ
ℏ
)
tr exp(RE),
where R is the curvature form of the symplectic connection ∂s, RE is the curvature form of
the vector bundle E , and tr stands for the ordinary matrix trace.
We start with an observation that q is a ﬂat section of End(LN ) with respect to the
connection
∂LN =d + [q(dq) − (dq)q, · ]. (33)
Let DLN be the Fedosov connection (17) corresponding to the initial symple ctic connec-
tion∂s on M, the initial series Ω h of closed two-forms and the connection (33) on the trivial
13
bundle LN . By claim 3 of theorem 2 there exists an element U ∈ IN ⊕W 1(EndLN ) which
establishes the equivalence between the connections D andDLN in the sense of deﬁnition 4.
Therefore, by statement iii) of theorem 3
Ψ D(P ) − Ψ DLN ( ~P ) ∈dΩ 2n−1(M)((ℏ)),
where ~P =σ(U −1 ◦P ◦U) is an idempotent in the algebra ( EndLN, ˜∗), with the star-product
˜∗ corresponding to the Fedosov connection DLN .
Notice that, ~P and P have the same principal part ~P
⏐⏐⏐
ℏ=0
=P
⏐⏐⏐
ℏ=0
=q. Let us consider
q as an element in the algebra ( EndLN, ˜∗) . By claim 1 of theorem 2 we may assume that
DLN satisﬁes normalization condition (27). Therefore, by lemma 1 the ele mentq is ﬂat with
respect to DLN , and hence q is an idempotent of the algebra ( EndLN, ˜∗) . By proposition 3
we may safely assume that ~P =q .
We recall that E =Imq ⊂LN is the subbundle of LN , corresponding to the idempotent
q and denote by ~E the subbundle ~E ⊂LN corresponding to the complementary idempotent
IN −q ∈EndLN . Thus, our trivial vector bundle LN is isomorphic to the direct sum E ⊕ ~E .
Let us ﬁx an isomorphism u
u : L ~→ E ⊕ ~E.
Since qu =uqu−1 ∈EndE⊕ ~E is the projector onto E along ~E
qu
⏐⏐⏐
Γ( E)((ℏ))
=Im, q u
⏐⏐⏐
Γ( ~E)((ℏ))
= 0, (34)
where m is the rank of E and Im is the identity endomorphism of E .
Due to remark 1 after theorem 2
DE⊕ ~E =DLN + [uDLN (u−1), · ] (35)
is the Fedosov connection on the Weyl algebra bundle W (EndE⊕ ~E).
Furthermore,qu =uqu−1 is ﬂat with respect to DE⊕ ~E, and hence the connection DE⊕ ~E
preserves the following subspaces of EndE⊕ ~E((ℏ))
{a ∈EndE⊕ ~E((ℏ)) | a
⏐⏐⏐
Γ( E)((ℏ))
⊂ Γ(E)((ℏ)), a
⏐⏐⏐
Γ( ~E)((ℏ))
= 0},
{a ∈EndE⊕ ~E((ℏ)) | a
⏐⏐⏐
Γ( ~E)((ℏ))
⊂ Γ( ~E)((ℏ)), a
⏐⏐⏐
Γ( E)((ℏ))
= 0}.
The latter implies that DE⊕ ~E is a direct sum DE ⊕D ~E of the Fedosov connections
DE = ∇E + 1
ℏ [AE, · ], D
~E = ∇
~E + 1
ℏ [A
~E, · ] (36)
on the bundles W (EndE) and W (End ~E), respectively. Thus, due to (34) and statement i)
of theorem 3 we have
Ψ DLN ( ~P ) = Ψ DE (Im),
where Im is as above the identity endomorphism of the vector bundle E .
14
Using statement iv) of theorem 3 we get that
Ψ DE (Im) − 1
ℏnQn(C(AE,A E),...,C (AE,A E)) ∈dΩ 2n−1(M)((ℏ)), (37)
where Qn ∈ ((Snh)∗)h is the n-th component of the adjoint invariant form (11), h = glN ⊕
sp2n , AE ∈ Ω 1(W (EndE)) is the one-form of the Fedosov connection DE (36), and C is the
ﬁberwise “curvature” (7) of the projection (9).
To compute C(AE,A E) we mention that since the Fedosov connection DE⊕ ~E is obtained
from the DLN via conjugation (35) the connection DE⊕ ~E has the same Fedosov-Weyl curva-
ture (18)
ℏ(R +RE⊕ ~E) + 2∇E⊕ ~EAE⊕ ~E + 1
ℏ [AE⊕ ~E,A E⊕ ~E] = −ω + Ω ℏ.
Here AE⊕ ~E is the one-form of the Fedosov connection DE⊕ ~E, ∇E⊕ ~E is the operator (16)
corresponding to the symplectic connection ∂s and the connection ∂E⊕ ~E onE ⊕ ~E obtained
from ∂LN via the isomorphism u . Finally, RE⊕ ~E is the curvature form of the connection
∂E⊕ ~E .
On the other hand the Fedosov connection DE⊕ ~E is a direct sum of the Fedosov connec-
tions DE and D ~E . Hence,
ℏ(R +RE) + 2∇EAE + 1
ℏ [AE,A E] = −ω + Ω ℏ, (38)
where RE is the curvature form of the connection ∂E on E and ∇E is the operator (16)
corresponding to the symplectic connection ∂s on M and the connection ∂E .
Notice that, the projection pr(AE) may be non-zero. However, using the trick of propo-
sition 1 we can absorb the terms that contribute to pr(AE) into the operator ∇E. In this
way we change both 3 the symplectic connection ∂s on M and the connection ∂E on E ,
and therefore we change curvature forms R and RE. It is not hard to show that after this
rearrangement equation (38) still holds.
Since pr(AE) is now vanishing pr∇(AE) = ∇pr(AE) = 0 . Thus, applying pr to both
sides of (38) we get
C(AE,A E) = ℏ2R + ℏ2RE − ℏ(−ω + Ω ℏ). (39)
Substituting (39) into equation (37) we complete the proof of the t heorem. ✷
4 Concluding remarks.
We would like to mention that our result (theorem 4) is derived from th e purely algebraic fact
(10) about the cohomology of Lie algebra of matrices over the Weyl algebra. In this respect
our approach is very reminiscent of ﬁnding “local” proofs of the Riem ann-Roch-Hirzebruch
theorem [1], [3], [5], [6], and [12]. Thus, in [1] and [3] the Riemann-Roch the orem for families
of Riemann curves is deduced from purely algebraic facts about the cohomology of the Lie
algebra of vector ﬁelds. In paper [12] this idea is generalized to highe r dimensions.
3Notice that, both the new Christoﬀel form Γ and the new connectio n form Γ E become formal power
series in ℏ .
15
The Bressler-Nest-Tsygan theorem [6] or the Riemann-Roch theo rem for deformation
quantizations, which we already mentioned in the introduction, is also a local statement based
on purely algebraic relations between Hochschild, cyclic, and Lie algeb ra (co)homology. It
seems that this result is the most general Riemann-Roch type theo rem which can be proven
in the symplectic setting using the methods of [6].
A very similar statement to our result is proposed in recent paper [11 ] by B. Feigin, A.
Losev, and B. Shoikhet. In this paper the authors consider the alg ebra Diﬀ( E) of holomorphic
diﬀerential operators acting on sections of a holomorphic vector b undle E over a compact
complex manifold X of the complex dimension n. They give a tractable notion of Hochschild
homology HH • of Diﬀ( E) for which HH •(Diﬀ( E)) = H 2n−•(X, C) and construct a map
Λ : Diﬀ( E) ↦→H 2n(X, C) (40)
which induces an isomorphismHH 0(Diﬀ( E)) ∼=H 2n(X, C) . Then, using the original Riemann-
Roch-Hirzebruch theorem and assuming that the Euler character istic of E is nonzero the
authors of [11] deduce that for any D ∈ Diﬀ( E), the pairing of Λ( D) with the fundamental
class [X] coincides with the super-trace str(D) of D .
We would like mention that the technique used in [11] to deﬁne the map ( 40) is very
similar to the procedure of constructing the Hochschild cocycle (5) . This technique was
originally proposed in paper [14] and we suspect that it has an indepen dent interest.
Notice that, since our proof of theorem 4 is purely algebraic, it can b e generalized in
a straightforward manner to the setting of the symplectic Lie algeb roids [17] . In this case
the local algebraic index theorem relates the cohomology classes of the De Rham complex
associated with the corresponding Lie algebroid.
