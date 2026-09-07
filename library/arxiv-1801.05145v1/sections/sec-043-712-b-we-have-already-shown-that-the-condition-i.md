---
doc_id: arxiv-1801.05145v1
doc_title: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS"
section_id: sec-043-712-b-we-have-already-shown-that-the-condition-i
section_title: "(b), we have already shown that the condition (i) in Deﬁni-"
section_number: 7.1.2
pages: 48-52
source_pdf: 1801.05145v1.pdf
source_sha256: 808da260edd433f7
doc_brief: "MONOIDAL CATEGORIFICATION OF CLUSTER ALGEBRAS — We prove that the quantum cluster algebra structure of a unipote nt quantum coordinate ring Aq(n(w)), associated with a symmetric Kac-Moody algebra and"
---
tion 7.1.1 holds for ({µx(M)i}i∈J,µx( ~B)). The condition (ii) is clear from the deﬁnition.
Let us show (iii). Set Ni :=µx(M)i and b′
ij :=µx( ~B)ij for i ∈ J and j ∈ Jex. It is
enough to show that, for any y ∈ Jex, there exists a self-dual simple module M ′′
y ∈ C
such that there is a short exact sequence
0 /d47/d47
q ⨀
b′
iy>0
N
⊙b′
iy
i /d47/d47
q
~Λ(Ny,M ′′
y )Ny ◦M ′′
y /d47/d47⨀
b′
iy<0
N
⊙(−b′
iy)
i /d47/d47
0(7.5)
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
Then using (
7.6) repeatedly, we have
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
Then (
7.5) is read as
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
Thus the exact sequence (
7.10) becomes the exact sequence in C:
0 /d47/d47qm(B ⊙P ) ⊙A /d47/d47qnMy ◦ (L ∇M ′
y) /d47/d47(L ⊙Q) ⊙A /d47/d470(7.11)
for some m,n ∈ Z. Since ( L ⊙Q) ⊙A is self-dual, n = ~Λ(My,L ∇M ′
y). On the other
hand, by Proposition
