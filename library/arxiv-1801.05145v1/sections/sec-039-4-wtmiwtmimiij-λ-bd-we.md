---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-039-4-wtmiwtmimiij-λ-bd-we
section_title: "(wt(Mi),wt(Mi))[Mi]}i∈J, −Λ, ~B,D ). We"
section_number: 4
pages: 48-54
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
assume further that
The Q(q1/2)-algebra Q(q1/2) ⊗
Z[q±1]
K(C) is isomorphic to Q(q1/2) ⊗
Z[q±1]
Aq1/2([S ]).(7.4)
Then, for each x ∈Jex, the pair
(
{µx(M)i}i∈J,µx( ~B)
)
is admissible in C.
Proof. In Proposition 7.1.2 (b), we have already shown that the condition (i) in Deﬁni-
tion 7.1.1 holds for ({µx(M)i}i∈J,µx( ~B)). The condition (ii) is clear from the deﬁnition.
Let us show (iii). Set Ni :=µx(M)i and b′
ij :=µx( ~B)ij for i ∈ J and j ∈ Jex. It is
enough to show that, for any y ∈ Jex, there exists a self-dual simple module M ′′
y ∈ C
such that there is a short exact sequence
0 /d47/d47q ⨀
b′
iy>0
N
⊙b′
iy
i /d47/d47q
~Λ(Ny,M ′′
y )Ny ◦M ′′
y /d47/d47⨀
b′
iy<0
N
⊙(−b′
iy)
i /d47/d470(7.5)
and
d(Ni,M ′′
y ) = 0 for i ⁄=y.
If x =y, then b′
iy = −bix and hence M ′′
y =Mx satisﬁes the desired condition.
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 49
Assume that x ⁄=y andbxy = 0. Then b′
iy =biy for any i andNi =Mi for any i ⁄=x.
Hence M ′′
y =µy(M)y satisﬁes the desired condition.
We will show the assertion in the case bxy > 0. We omit the proof of the case bxy < 0
because it can be shown in a similar way.
Recall that we have
b′
iy =
{
biy +bixbxy if bix > 0,
biy if bix ≤ 0(7.6)
for i ∈J diﬀerent from x and y.
Set
M ′
x :=µx(M)x, M ′
y :=µy(M)y,
C := ⨀
bix>0
M ⊙bix
i , S := ⨀
bix<0, i⁄=y
M ⊙−bix
i ,
P := ⨀
biy>0,i⁄=x
M ⊙biy
i , Q := ⨀
b′
iy<0, i⁄=x
M
⊙−b′
iy
i ,
A := ⨀
b′
iy≤0, bix>0
M ⊙bixbxy
i ⊙ ⨀
biy<0,b ′
iy>0,b ix>0
M ⊙−biy
i
≃ ⨀
biy<0,b ix>0
M ⊙ min(bixbxy,−biy)
i ,
B := ⨀
biy≥0, bix>0
M ⊙bixbxy
i ⊙ ⨀
b′
iy>0,b iy<0,b ix>0
M
⊙b′
iy
i .
Then using ( 7.6) repeatedly, we have
Q ⊙A ≃ ⨀
biy<0
M ⊙−biy
i , A ⊙B ≃C⊙bxy, and B ⊙P ≃ ⊙ ⨀
b′
iy>0
M
⊙b′
iy
i .
Set
L := (M ′
x)⊙bxy, V :=M ⊙bxy
x
and set
X := ⨀
biy>0
M ⊙biy
i ≃M ⊙bxy
x ⊙P =V ⊙P, Y := ⨀
biy<0
M ⊙−biy
i ≃Q ⊙A.
Then ( 7.5) is read as
0 /d47/d47q(B ⊙P ) /d47/d47q ~Λ(My,M ′′
y )My ◦M ′′
y /d47/d47L ⊙Q /d47/d470.(7.7)
Note that we have
0 →qC →q
~Λ(Mx,M ′
x)Mx ◦M ′
x →M ⊙bxy
y ⊙S → 0,(7.8)
0 →qX →q
~Λ(My,M ′
y)My ◦M ′
y →Y → 0.(7.9)
50 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Taking the convolution products of L = (M ′
x)⊙bxy and ( 7.9), we obtain
0 /d47/d47qL ◦X /d47/d47q
~Λ(My,M ′
y)L ◦ (My ◦M ′
y) /d47/d47L ◦Y /d47/d470,
0 /d47/d47qX ◦L /d47/d47q
~Λ(My,M ′
y)(My ◦M ′
y) ◦L /d47/d47Y ◦L /d47/d470.
Since L commutes with My, we have
Λ(L,Y ) = Λ( L,My ∇M ′
y)
= Λ(L,My) + Λ(L,M ′
y) = Λ( L,My ◦M ′
y).
On the other hand, we have
Λ(M ′
x,X ) − Λ(M ′
x,Y )
= Λ(M ′
x, ⨀
biy>0
M ⊙biy
i ) − Λ(M ′
x, ⨀
biy<0
M ⊙−biy
i )
=
∑
biy>0
Λ(M ′
x,Mi)biy −
∑
biy<0
Λ(M ′
x,Mi)(−biy)
=
∑
i∈J
Λ(M ′
x,Mi)biy =
∑
i⁄=x
Λ(M ′
x,Mi)biy + Λ(M ′
x,Mx)bxy
=
∑
i⁄=x
Λ(M ′
x,Mi)(b′
iy −δ(bix > 0)bixbxy) + Λ(M ′
x,Mx)bxy
=
∑
i⁄=x
Λ(M ′
x,Mi)b′
iy −
∑
bix>0
Λ(M ′
x,Mi)bixbxy + Λ(M ′
x,Mx)bxy
=
(a)
0 − Λ(M ′
x, ⨀
bix>0
M ⊙bix
i )bxy + Λ(M ′
x,Mx)bxy
=
(
−Λ(M ′
x, ⨀
bix>0
M ⊙bix
i ) + Λ(M ′
x,Mx)
)
bxy
= (−Λ(M ′
x,M ′
x ∇Mx) + Λ(M ′
x,Mx))bxy
= (−Λ(M ′
x,M ′
x) − Λ(M ′
x,Mx) + Λ(M ′
x,Mx))bxy = 0.
Note that we used the compatibility of the pair
((
−Λ(µx(Mi),µx(Mj))
)
i,j∈J, µx( ~B)
)
when we derive the equality (a).
Since L = (M ′
x)⊙bxy, the equality Λ( M ′
x,X ) = Λ( M ′
x,Y ) implies
Λ(L,X ) = Λ( L,Y ) = Λ( L,My ◦M ′
y).
MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS 51
Hence the following diagram is commutative by Proposition 3.2.8 (i):
0 /d47/d47qL ◦X /d47/d47
rL,X
/d15/d15
q
~Λ(My,M ′
y)L ◦ (My ◦M ′
y)
rL,My◦M ′
y
/d15/d15
/d47/d47L ◦Y /d47/d47
rL,Y ≀
/d15/d15
0
0 /d47/d47qd+1X ◦L /d47/d47qd+~Λ(My,M ′
y)(My ◦M ′
y) ◦L /d47/d47qdY ◦L /d47/d470,
where d = −Λ(L,X ) = −Λ(L,My ◦M ′
y) = −Λ(L,Y ). Note that since L = (M ′
x)⊙bxy
commutes with Q and A, rL,Y is an isomorphism. Hence we have
Im(rL,Y ) ≃L ◦Y.
Therefore we obtain an exact sequence
0 /d47/d47Im(rL,X) /d47/d47Im(rL,My◦M ′
y
) /d47/d47L ◦Y /d47/d470.(7.10)
On the other hand, rL,My◦M ′
y
decomposes (up to a grading shift) by Lemma 3.1.5 as
follows:
L ◦My ◦M ′
y
∼
rL,My
◦M ′
y
/d47/d47
rL,My◦M ′
y
/d43/d43
My ◦L ◦M ′
y My◦rL,M ′
y
/d47/d47My ◦M ′
y ◦L.
Since L = (M ′
x)⊙bxy commutes with My, the homomorphisms rL,My
◦M ′
y is an isomor-
phism and hence we have
Im(rL,My◦M ′
y
) ≃My ◦ (L ∇M ′
y) up to a grading shift.
Similarly, rL,X decomposes (up to a grading shift) as follows:
L ◦V ◦P rL,V ◦P
/d47/d47
rL,X
/d44/d44
V ◦L ◦P V ◦rL,P
∼ /d47/d47V ◦P ◦L.
Since L commutes with P , the homomorphism V ◦ rL,P is an isomorphism and hence
we have
Im(rL,X) ≃ (L ∇V ) ◦P ≃
(
(M ′
x)◦bxy ∇M◦bxy
x
)
◦P up to a grading shift.
On the other hand, Lemma 3.2.22 implies that
(M ′
x)◦bxy ∇M◦bxy
x ≃ (M ′
x ∇Mx)◦bxy ≃C◦bxy ≃B ⊙A
and hence we obtain
Im(rL,X) ≃ (B ⊙P ) ⊙A up to a grading shift.
52 S.-J. KANG, M. KASHIW ARA, M. KIM, S.-J. OH
Thus the exact sequence ( 7.10) becomes the exact sequence in C:
0 /d47/d47qm(B ⊙P ) ⊙A /d47/d47qnMy ◦ (L ∇M ′
y) /d47/d47(L ⊙Q) ⊙A /d47/d470(7.11)
for some m,n ∈ Z. Since ( L ⊙Q) ⊙A is self-dual, n = ~Λ(My,L ∇M ′
y). On the other
hand, by Proposition 3.2.13 (i) and Proposition 7.1.2 (d), we have
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
On the other hand, ( 7.14) implies
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
