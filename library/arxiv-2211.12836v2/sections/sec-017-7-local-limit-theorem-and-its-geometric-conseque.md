---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-017-7-local-limit-theorem-and-its-geometric-conseque
section_title: "Local limit theorem and its geometric consequences"
section_number: 7
pages: 56-60
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
In this section, we prove a local limit theorem for the h-probability measure (∗m)∗δI and
deduce Corollary 2.7, which gives asymptotics of structure coeﬃcients in the ring QH(Gk,n). For
simplicity, we assume that Var (m) = 0 to avoid any lattice issue.
Theorem 7.1. LetM >0 and suppose that m = (µr)1≤r≤m is a sequence ofh-probability measures
on Bk,n such that Var 2(m) = 0 and⟨ˆm⟩3≤MK (m) and let I∈Bk,n. Then,
((∗m)∗δI) [I′] =δ|I′|=⟨I⟩+m⟨m⟩)[n]n
[
KSU (k)
t0γ (ξn(I),ξn(I′)) +o
( 1√n
)]
,
where
t0 = 2πm
n2 , γ = k
2(k2− 1)K(m),
and o(·) only depends on γ ,M, t0 and k.
Proof. Recall that Φn[δI](J) = SI(ξn(J))
SI(ξn(I0) by (19). Then, by Proposition 3.10, Lemma 4.5 and Lemma
4.4, for I′∈Bk,n
((∗m)∗δI) [I′] =
∑
J∈Bk,n
Φ[δI](J)
m∏
j=1
Φ[µj](J)˜uJ
I′
=
∑
J∈Bk,n
m∏
j=1
Φ[µj](J)SI(ξn(J))
SI(ξn(I0))
|V (ξn(J))|2SI′(ξn(J))
|V (ξn(I0))|2SI′(ξn(I0))
=
∑
J∈Bk,n
m∏
j=1
Φ[µj](J)SJ(ξn(I))SJ(ξn(I′)).
Set t0 = (2π)2m
n2 and γ = kK(m)
2(k2−1). Then, applying Proposition 5.3 with Var 2(m) = 0 gives
((∗m)∗δI) [I′] =
∑
J∈Bk,n
SJ(ξn(I′))SJ(ξn(I))e
2im⟨m⟩⟨J⟩
kn B(J)
with
B(J)≤ exp
(
−t0
γK( ˜J)
k + t0M
n O
([
kK( ˜J)K(m)
]3/2))
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 57
and, when‖ ˜J‖∞≤c n
m1/3M 1/3K(m)1/2 :=θ1n1/3 (with θ2 depending on t0,γ,k and M)
B(J) = exp
(
−t0
γK( ˜J)
k + t0M
n O
([
kK( ˜J)K(m)
]3/2))
.
Noting that K( ˜J)≤‖ ˜J‖2
∞ =‖ ˆJ‖2
∞, there is θ2> 0 depending on k,γ and M so that
−t0
γK( ˜J)
k + t0M
n O
([
kK( ˜J)K(m)
]3/2)
≤− t0
2
γK( ˜J)
k + t0M
n O
([
kK( ˜J)K(m)
]3/2)
when sup( ˆJi− ˆJi+1[n])≤ θ2n. By Lemma 5.5, for sup( ˆJi− ˆJi+1[n])≥ θ2n, there exists δ,η > 0
depending on t0,k,γ and M such that
(61) B(J)≤ exp
(
−n2
(
δ + η
n3
))
.
Let us split ((∗m)∗δI) [I′] as
((∗m)∗δI) [I′] =
∑
J∈Bk,n
sup( ˆJi− ˆJi+1[n])>θ1n1/3
SJ(ξn(I))SJ(ξn(I′))e2iπm⟨m⟩·⟨λJ⟩
kn B(J)
+
∑
J∈Bk,n
sup( ˆJi− ˆJi+1[n])<θ1n1/3
SJ(ξn(I))SJ(ξn(I′))e2iπm⟨m⟩·⟨λJ⟩
kn B(J) :=S1 +S2,
and, using (25), split KSU (k)
γt0
(
ξn(I′),R−m⟨m⟩
kn
(ξn (I))
)
as
KSU (k)
γt0
(
ξn(I′),R−m⟨m⟩
kn
(ξn (I))
)
=
∑
J∈Bk
Jk=0
exp(−κ0,γ(J)t0)SJ(ξn(I′))SJ
(
R−m⟨m⟩
kn
(ξn (I))
)
=
∑
J∈Bk
Jk=0
sup(Ji−Ji+1[n])<θ1n1/3
e
2iπm⟨m⟩)⟨J⟩
kn −κ0,γ(J)t0SJ(ξn(I′))SJ(ξn(I))
+
∑
J∈Bk
Jk=0
sup(Ji−Ji+1[n])≥θ1n1/3
e−κ0,γ(J)t0SJ(ξn(I′))SJ
(
R−m⟨m⟩
kn
(ξn (I))
)
:=S′
1 +S′
2.
Then, we have
⏐⏐⏐((∗m)∗δI) [I′]−nδ⟨I′⟩=⟨I⟩+m⟨m⟩)⟩[n]KSU (k),γ
t0,δI
(ξn(I′))
⏐⏐⏐≤
⏐⏐S1−δ⟨I′⟩=⟨I⟩+m⟨m⟩)[n]S′
1
⏐⏐ +
⏐⏐S2| +|S′
2
⏐⏐.
58 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
First, by Lemma 5.4, (61) and the rough bound SJ(ξn(J′))≤dJ≤nk(k−1)/2 for J,J′∈Bk,n,
|S2|≤
∑
J∈Bk,n
θ1n1/3<sup( ˆJi− ˆJi+1[n])<θ2n
d2
J exp
(
−t0γ
2kK( ˜J)
)
+
∑
J∈Bk,n
sup( ˆJi− ˆJi+1[n])≥θ2n
d2
J exp
(
−n2
(
δ + η
n3
))
≤#Bk,nnk(k−1)
[
exp
(
−t0γθ2
1
k2 n2/3
)
+ exp
(
−n2
(
δ + η
n3
))]
≤nk2
exp
(
−Cn1/3
)
=o (1)
with o (1) only depending on γ,k,t 0 and M. Likewise, by the absolute convergence of the Fourier
expansion of the heat kernel on SU (k) for t≥t0, see [21],
⏐⏐S′
2
⏐⏐ =o(1).
Next, using that SJ(ξn(I)) = S ˆJ(ξn(I))e
2iπJk⟨I⟩
n and summing on Jk when sup( ˆJi− ˆJi+1[n]) <
θ1n1/3 and for n large enough (so that ˆJ +l1k⁄= ˆJ +l′1k when 0≤l⁄=l′≤n− 1) yields
S1 =
∑
J∈Bk,n
Jk=0
sup(Ji−Ji+1[n])<θ1n1/3
B(J)S ˆJ(ξn(I))S ˆJ(ξn(I′))
(n−1∑
l=0
e
2iπ(m⟨m⟩)/k(⟨J⟩+kl)+(⟨I⟩−⟨I′⟩)l
n
)
=nδm⟨m⟩)+⟨I⟩=⟨I′⟩[n]
∑
J∈Bk,n
Jk=0
sup(Ji−Ji+1[n])<θ1n1/3
B(J)e
2iπm⟨m⟩)⟨J⟩
kn SJ(ξn(I))SJ(ξn(I′)).
with
B(J) = exp
(
−t0
γK( ˜J)
k + t0M
n O
([
kK( ˜J)K(m)
]3/2))
.
Hence, using that t0M
n O
([
kK( ˜J)K(m)
]3/2)
=O(1) when sup(Ji−Ji+1[n])<θ 1n1/3,
⏐⏐S1−δ⟨I′⟩=⟨I⟩+m⟨m⟩[n]S′
1
⏐⏐
≤n
∑
J∈Bk,n
Jk=0
sup(Ji−Ji+1[n])<θ1n1/3
⏐⏐⏐SJ
(
R−m⟨m⟩
kn
(ξn (I))
)
SJ(ξn(I′))
⏐⏐⏐ exp
(
−t0
γK( ˜J)
2k
)
exp
(
−t0
γK( ˜J)
k
)⏐⏐⏐⏐exp
(t0M
n O
([
k2γK( ˜J)
]3/2))
− 1
⏐⏐⏐⏐
≤
∑
J∈Bk,n
Jk=−(k−1)/2
sup(Ji−Ji+1[n])<n1/6
d2
J exp
(
−t0
γK( ˜J)
2k
)
O(1)≤KSU (k)
γt0/2 (0, 0)O(1) =O (1),
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 59
with O(1) depending on M,t 0,γ and k. Finally,
⏐⏐⏐((∗m)∗δI) [I′]−nδ⟨I′⟩=⟨I⟩+m⟨m⟩[n]KSU (k)
γt0
(
ξn(I′),R−m⟨m⟩
kn
(ξn (I))
)⏐⏐⏐ =O(1),
with O(·) depending on k,γ,M and t0. □
We can now turn to the proof of Corollary 2.7.
Proof of Corollary 2.7. Recall that in the case where ∑m+1
i=0 di≤ dimHold(Gk,n) = k(n−k) +dn
and for generic manifolds M0,...,M m+1, we have by (63)
#Md,a0,...,am+1
M0,...,Mm+1 =
⟨( m∏
i=0
[Mi]
)
[qd], [Mm+1]
⟩
H∗(Gk,n)
,
where⟨·,·⟩ denotes the Poincar´ e duality inH∗(Gk,n) and for x∈QH(Gk,n) = C[q]⊗H∗(Gk,n), we
write x =∑
d≥0x[qd]⊗qd. By the multiplication rule (62), for d′≥ 0 we have (∏m
i=0[Mi]) [qd′
]∈
Hd′n+k(n−k)−∑m
i=0di and thus, for d′ ⁄= d′′, (∏m
i=0[Mi]) [qd′
] and (∏m
i=0[Mi]) [qd′′
] are in diﬀerent
dimension components of H∗(Gk,n). Hence, we deduce that
#Md,a0,...,am+1
M0,...,Mm+1 =
∑
I∈Bk,n,⟨I⟩=dm+1
am+1
I
⟨( m∏
i=0
[Mi]
)
[qd],σλI
⟩
H∗(Gk,n)
=
∑
I∈Bk,n,⟨I⟩=dm+1
am+1
I
⟨( m∏
i=0
[Mi]
)
,σλI
⟩
H∗(Gk,n)
,
where x is the image of x in QH(Gk,n)/⟨q = 1⟩ and we recall that the am+1
I ’s are the coeﬃcients
appearing in the decomposition [ Mm+1] = ∑
I∈Bk,n,⟨I⟩=dm+1am+1
I σλI. Then, recalling that the
Poincar´ e duality satisﬁes⟨σλ,σµ⟩H∗(Gk,n) =δλ,µc (see for example the introduction of [5]), we have
#Md,a0,...,am+1
M0,...,Mm+1 =
∑
I∈Bk,n,⟨I⟩=dm+1
am+1
I cIc∏m
i=0[Mi],
wherecI∏m
i=0[Mi],I ∈Bk,n are the coeﬃcients of∏m
i=0[Mi] on the basis{σλI,I ∈Bk,n} and we recall
that Ic = (n− 1−Ik−j+1)1≤j≤k. By Proposition 4.2, the linear map from QH(Gk,n)/⟨q = 1⟩ to
B(L2(Bk,n)) mappingσλ toT (sλ) is an algebra isomorphism fromQH(Gk,n)/⟨q = 1⟩ to the algebra
A⊂B (L2(Bk,n)) for which Bk,n is positively multiplicative, and T (sλ) is the unique element of A
sending I0 to Iλ. Hence, by Proposition 3.6 and (7) we have
cI∏m
i=0[Mi] =hr
I
(
(Mh)−1([M0])∗···∗ (Mh)−1([Mm])
)
(I),
60 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
where (Mh)−1([Mi]) = ∑
I∈Bk,n
1
hr
I
ai
IeI and hr
I = V (ξn(I0)2
nk SI(ξn(I0)) by Lemma 4.5. Now, since
hl
I =SI(ξn(I0)) by the same lemma,
Φn
[
(Mh)−1([Mi])
]
(I0) =
⟨
1, (Mh)−1([Mi])
⟩
h
=
⟨
1, 1
hr

 ∑
I∈Bk,n
ai
IeI


⟩
h
=
⟨
hl,

 ∑
I∈Bk,n
ai
IeI


⟩
=
∑
I∈Bk,n
ai
ISI(ξn(I0)) =qDim(Mi),
and we deduce that 1
qDim(Mi)(Mh)−1(Mi) is a h-probability measure on Bk,n. Then, recalling that
δI = 1
µh(I)eI = 1
hl(I)hr(I)eI, we have
(Mh)−1(M0) =
∑
I∈Bk,n,⟨I⟩=d0
aISI(ξn(I0))δI,
so that ﬁnally
cI′∏m
i=1[Mi] = V (ξn(I0))2SI′(ξn(I0))∏m
i=0qDim(Mi)
nk
∑
I∈Bk,n,⟨I⟩=d0
aISI(ξn(I0)) (δI∗ (∗m)) (I′),
with m = (µi)1≤i≤m where µi = 1
qDim(Mi)(Mh)−1(Mi). Hence, applying Theorem 2.6 with the
notation of Corollary 2.7, we deduce that
cI′∏m
i=0[Mi] =V (ξn(I0))2QI′(ξn(I0))∏m
i=1qDim(Mi)
nk−1
∑
I∈Bk,n,⟨I⟩=d0
aIsI(ξn(I0))
(
KSU (k)
(2π)2m
n2 γ
(
R−m⟨m⟩
kn
(ξn(I)),ξn(I′)
)
+O
( 1
n
))
,
with O(·) only depending on m
n2,k and‖ ˜m‖i, i = 2, 3. Then, writing pi
I = aISI(ξn(I0))
qDim(Mi) for 0≤i≤
m + 1, so that ∑
I∈Bk,npi
I = 1, we get
#Md,a0,...,am+1
M0,...,Mm+1 = V (ξn(I0))2∏m+1
i=0 qDim(Mi)
nk−1

 ∑
I,I′∈Bk,n
pM0
I pMm+1
I′ KSU (k)
γt0 (xn
I,xn
I′) +O
( 1
n
)
,
with xn
I =R−m⟨m⟩
kn
(ξn(I)) and yn
I′ =ξn((I′)c). □
