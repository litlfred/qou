---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-044-3213-i-and-proposition-712-d-we-have
section_title: "(i) and Proposition 7.1.2 (d), we have"
section_number: 3.2.13
pages: 52-54
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
d(My,L ∇M ′
y) ≤ d(My,L ) + d(My,M ′
y) = 1.
By the exact sequence ( 7.11), My ◦ (L ∇M ′
y) is not simple and we conclude
d(My,L ∇M ′
y) = 1.
Then Lemma 3.2.18 implies that m = 1. Thus we obtain an exact sequence in C:
0 /d47/d47q(B ⊙P ) ⊙A /d47/d47q
~Λ(My,L∇M ′
y)My ◦ (L ∇M ′
y) /d47/d47(L ⊙Q) ⊙A /d47/d470.(7.12)
Now we shall rewrite ( 7.12) by using • ◦A instead of • ⊙A. We have
~Λ(B,A ) + ~Λ(A,A ) = bxy ~Λ(C,A ) = bxy ~Λ(M ′
x ∇Mx,A )
=bxy ~Λ(M ′
x,A ) +bxy ~Λ(Mx,A ) = ~Λ(L,A ) +bxy ~Λ(Mx,A ).
On the other hand, the exact sequence ( 7.9) gives
bxy ~Λ(Mx,A ) + ~Λ(P,A ) = ~Λ(X,A ) = ~Λ(M ′
y ∇My,A )
= ~Λ(M ′
y,A ) + ~Λ(My,A ) = ~Λ(My ∇M ′
y,A ) = ~Λ(Y,A ) = ~Λ(Q,A ) + ~Λ(A,A ).
It follows that
~Λ(B ◦P,A ) = ~Λ(B,A ) + ~Λ(P,A )
=
(~Λ(L,A ) +bxy ~Λ(Mx,A ) − ~Λ(A,A )
)
+
(~Λ(Q,A ) + ~Λ(A,A ) −bxy ~Λ(Mx,A )
)
= ~Λ(L,A ) + ~Λ(Q,A ) = ~Λ(L ◦Q,A ).
Hence we have
0 /d47/d47q(B ⊙P ) ◦A /d47/d47qcMy ◦ (L ∇M ′
y) /d47/d47(L ⊙Q) ◦A /d47/d470,
where c = ~Λ(My,L ∇M ′
y) − ~Λ(B ⊙P,A ) by Lemma 3.1.4.
Thus we obtain the identity in K(R-gmod):
qc[My][L ∇M ′
y] =
(
q[B ⊙P ] + [L ⊙Q]
)
[A].
On the other hand, the hypothesis ( 7.4) implies that there exists φ ∈ Q(q1/2) ⊗Z[q±1]
K(C) corresponding to µyµx([M]) so that it satisﬁes
[My]φ =q[B ⊙P ] + [L ⊙Q](7.13)
and
φ[µx(M)i] = qλ′
yi [µx(M)i]φ for i ⁄=y,(7.14)
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 53
where µyµx(−Λ) = ( λ′
ij)i,j∈J.
Hence, in Q(q1/2) ⊗Z[q±1]K(C), we have
[My]φ[A] =
(
q[B ⊙P ] + [L ⊙Q]
)
[A] = qc[My][L ∇M ′
y].
Since Q(q1/2) ⊗Z[q±1]K(C) is a domain, we conclude that
φ[A] = qc[L ∇M ′
y].
On the other hand, (
7.14) implies
φ[A] = ql[A]φ for some l ∈ Z.
Hence, Theorem 4.1.3 implies that, when we write
φ =
∑
b∈B(∞)
ab[Lb] for some ab ∈ Q(q1/2),
we have
Lb ◦A ≃qlA ◦Lb whenever ab ⁄= 0.
In particular, each module Lb ◦A with ab ⁄= 0 is simple because A is a real simple
module. Thus we obtain
qc[L ∇M ′
y] = φ[A] =
∑
b∈B(∞)
ab[Lb ◦A].
Since L ∇M ′
y is simple, there exists b0 such that Lb0 ◦A is isomorphic to L ∇M ′
y up
to a grading shift, and ab = 0 for b ⁄= b0. Set M ′′
y := Lb0. Then we conclude that
φ[A] = qm[M ′′
y ◦A] = qm[M ′′
y ][A] so that
φ =qm[M ′′
y ] for some m ∈ Z.
We emphasize that M ′′
y is a self-dual simple module in R-gmod which satisﬁes that
M ′′
y ◦A ≃L ∇My up to a grading shift.
Now ( 7.13) implies
qm[My ◦M ′′
y ] = q[B ⊙P ] + [L ⊙Q].
Hence there exists an exact sequence
0 − − →W − − →qmMy ◦M ′′
y − − →Z − − →0,
whereW =qB ⊙P andZ =L ⊙Q orW =L ⊙Q andZ =qB ⊙P . By Lemma 3.2.18,
the second case does not occur and we have an exact sequence
0 − − →qB ⊙P − − →qm My ◦M ′′
y − − →L ⊙Q − − →0.
SinceMy,M ′′
y andL ⊙Q are self-dual, we have m = ~Λ(My,M ′′
y ), and we obtain the
desired short exact sequence ( 7.7).
54 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Since φ commutes with [ µx(M)i] up to a power of q in K(C), and µx(M)i is real
simple, M ′′
y commutes with µx(M)i for i ⁄=y, by Corollary 4.1.4. □
Corollary 7.1.4. Let ({Mi}i∈J, ~B) be an admissible pair in C. Under the assump-
tion (7.4), C is a monoidal categoriﬁcation of the quantum cluster algebr a Aq1/2([S ]).
Furthermore, the following statements hold :
(i) The quantum monoidal seed S = ( {Mi}i∈J, −Λ, ~B,D ) admits successive muta-
tions in all directions.
(ii) Any cluster monomial in Z[q±1/2] ⊗Z[q±1]K(C) is the isomorphism class of a real
simple object in C up to a power of q1/2.
(iii) Any cluster monomial in Z[q±1/2] ⊗Z[q±1] K(C) is a Laurent polynomial of the
initial cluster variables with coeﬃcient in Z≥0[q±1/2].
Proof. (i) and (ii) are straightforward.
Let us show (iii). Let x be a cluster monomial. By the Laurent phenomenon ([ 3]),
we can write
xX c =
∑
a∈ZJ
≥0
caX a,
where X = (Xi)i∈J is the initial cluster, c ∈ ZJ
≥0 and ca ∈ Q(q±1/2). Since x and X c
are the isomorphism classes of simple modules up to a power of q1/2, their product xX c
can be written as a linear combination of the isomorphism classes of sim ple modules
with coeﬃcients in Z≥0[q±1/2]. Since every X a is the isomorphism class of a simple
module up to a power of q1/2, we have ca ∈ Z≥0[q±1/2]. □
