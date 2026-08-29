---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-008-31-family-of-random-walks-and-h-transform
section_title: "Family of random walks and h-transform"
section_number: 3.1
pages: 15-18
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
v0, one can construct a family of commuting Markov kernels as follows. For sake of simplicity we
assume here that A is irreducible, although the same reasoning apply beyond irreducibility. Let hr
(resp. hl) be the right (resp. left) Perron-Frobenius vector of A, normalized so that hl(v0) = 1 and
⟨hl,hr⟩L2(V ) = 1. By irreducibility of A, hl(v)> 0 and hr(v)> 0 for all v∈V . In the case where
we are considering an adjacency matrix M which is not necessarily irreducible, we say that v is a
positive eigenvector ofM ifv is an eigenvector ofM which has positive coeﬃcients in its expansion
in the canonical basis.
Lemma 3.2. For all v ∈ V , hl and hr are respectively left and right eigenvectors of sv with
eigenvalue hl(v).
Proof. The fact that hl andhr are eigenvectors ofsv is deduced from the fact that both vectors are
eigenvectors of A and sv commutes with A. Hence, they are left and right positive eigenvectors of
sv, and thus correspond to the same eigenvalue we denote temporarily by λ. On the one hand, we
have by deﬁnition of sv
⟨hl,svev0⟩ =⟨hl,ev⟩ =hl(v),
and on the other hand,
⟨hl,svev0⟩ =⟨s∗
vhl,ev0⟩ =λ⟨hl,ev0⟩ =λ.
We conclude that
λ =hl
v.
□
It will be convenient to introduce the Hadamard product on vectorsx,y∈L2(V )↦→x·y∈L2(V )
deﬁned by
(x·y)(v) =x(v)y(v).
If x has nonzero entries, we write 1
x for the vector having entry 1
x(v) at v.
16 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Deﬁnition 3.3. The h-spaceL2
h(V ) is the vector space L2(V ) endowed with the Hilbert product
⟨x,y⟩h =⟨hl·x,hr·y⟩ =
∑
v∈V
µh(v)x(v)y(v),
with µh =hl·hr called the invariant probability measure of A.
The h-transform of an operator B∈End(L2(V )) is the operator Bh given by
Bh(x) = 1
hr·B(hr·x).
The space L2
h(V ) can be also seen as the Hilbert space of L2-functions on V with respect to the
probability measure µh.
Since hr has positive entries, the map B ↦→ Bh is well-deﬁned. Its is actually an algebra
isomorphism of End(L2(V )) which amounts to a conjugation by a diagonal matrix; we denote by
Ah the algebra{Bh,B∈A} , which is isomorphic to A. It is readily seen that
(Bh)∗(x) =hr·B∗
( 1
hr·x
)
,
while taking the adjoint (·)h,∗ of B with respect to⟨·,·⟩h yields
Bh,∗(x) = 1
µh·B∗
(
µh·x
)
.
Forv∈V , let us write
Pv = sh
v
hl(v)∈A h.
Proposition 3.4. The set {Pv,v∈V} is a family of commuting Markov kernels on L2(V ) with
common invariant measure µh.
Proof. Let v∈V and denote by 1∈V the vector with 1(v) = 1 for all v∈V . Remark ﬁrst that
by Lemma 3.2,
Pv(1V ) = 1
hl(v)
1
hr·sv(hr) = 1
hr·hr = 1.
Then, writing svsv′ =∑
v′′∈V cv′′
vv′sv′′ with cv′′
vv′≥ 0 for all v,v′,v′′∈V , we have
Pv(ev′) =hr(v′) 1
hr·sv(sv′ev0) =
∑
v′′∈V
hr(v′)cv′′
vv′
( 1
hr·sv′′(ev0)
)
=
∑
v′′∈V
hr(v′)
hr(v′′)cv′′
vv′ev′′.
Since
hr
v′
hr
v′′
cv′′
vv′ ≥ 0 for all v,v′,v′′∈ V , Pv is an adjacency matrix and thus a Markov kernel on
L2
h(V ). Since by Lemma 3.2
(sh
v)∗[µh] =hr·s∗
v
( 1
hr·µh
)
=hr·s∗
v(hl) =hl(v)hr·hl =hl(v)µh,
the vector µh is a positive eigenvector of Pv with eigenvalue 1. Hence, µh is an invariant measure
of Pv. □
Remark that we can similarly view the set{Pv,v∈V} as a family of commuting Markov kernels
on L2
h(V ) with common invariant measure having density 1 with respect to µh. We have indeed
similarly
(Pv)h,∗[1] = 1
µhhr· s∗
v
hl(v)
( 1
hr·µh· 1
)
= 1
hl· s∗
v
hl(v)(hl) = 1
hl·hl = 1.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 17
3.2. Convolution product on L2
h(V ). Similarly to (6) there is an isomorphism from L2
h(V ) to
Ah given by
(7) Mh :
{
L2(V )→ A h
ev↦→ µh(v)Pv .
We can then transpose the multiplicative structure on Ah to a multiplication on L2
h(V ). This
motivates the following deﬁnition.
Deﬁnition 3.5. The convolution of x,y∈L2
h(V ) is the vector x∗y deﬁned by
x∗y =
∑
v∈V
µh(v)x(v)Pv(y) =
∑
v∈V
hr(v)x(v)sh
v(y).
A vector u∈L2
h(V ) with nonnegative real entries is called a h-probability measure if
⟨1,u⟩h = 1.
We denote by M1(V ) the set of h-probability measures. We have then the following results
analogous to the usual convolution on classical groups.
Proposition 3.6. The convolution product turns L2
h(V ) into an algebra isomorphic to A through
the map Mh. Moreover, the set M1(V ) is stable by convolution.
Proof. To prove the ﬁrst statement, it is enough to prove that Mh intertwines∗ and the operator
product on Ah. By linearity, it is enough to prove it on ev
hr(v), ev′
hr(v′) for v,v′∈ V . Let v,v′∈ V .
Then, using that µh =hl·hr and Pv = sh
v
hl(v),
ev
hr(v)∗ ev′
hr(v′) =
∑
v′′∈V
(
hr· ev
hr(v)
)
(v′′)sh
v′′
( ev′
hr(v′)
)
=sh
v
( ev′
hr(v′)
)
= 1
hr
·sv(ev′).
Since ev′ =sv′ev0, writing svsv′ =∑
v′′∈V cv′′
vv′sv′′ we get
sv(ev) =
∑
v′′∈V
cv′′
vv′ev′′.
Hence,
ev
hr(v)∗ ev′
hr(v′) =
∑
v′′∈V
cv′′
vv′
ev′′
hr(v′′).
Since we have Mh
(
ev
hr(v)
)
=sh
v, we deduce that
Mh
( ev
hr(v)∗ ev′
hr(v′)
)
=Mh
( ev
hr(v)
)
Mh
( ev′
hr(v′)
)
.
Hence, (L2
h(V ), +,∗) is an algebra which is isomorphic to Ah (and thus toA).
Suppose that x,y∈M 1(V ). Then,
⟨1,x∗y⟩h =
∑
v∈V
µh(v)x(v)⟨1,P v(y)⟩h
=
∑
v∈V
µh(v)x(v)
⟨
hl,hr· 1
hr· sv(hr·y)
hl(v)
⟩
=
∑
v∈V
hr(v)x(v)
⟨
hl,sv(hr·y)
⟩
.
18 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
By Lemma 3.2, hl is an eigenvector of s∗
v with eigenvalue hl(v) for all v∈V , thus, using the fact
that x,y∈M 1(V ),
⟨1,x∗y⟩h =
∑
v∈V
hr(v)x(v)
⟨
s∗
vhl,hr·y
⟩
=
∑
v∈V
µh(v)x(v)
⟨
hl,hr·y
⟩
=
∑
v∈V
µh(v)x(v)⟨1,y⟩h =⟨1,x⟩h = 1.
□
