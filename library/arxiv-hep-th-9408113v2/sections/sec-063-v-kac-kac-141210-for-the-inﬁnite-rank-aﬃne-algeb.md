---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-063-v-kac-kac-141210-for-the-inﬁnite-rank-aﬃne-algeb
section_title: "Kac ([Kac], (14.12.10)): for the inﬁnite rank aﬃne algebr a of type A∞"
section_number: V
pages: 63-68
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
dimqL(Λ s1 + Λ s2 +··· + Λ sn) = 1
(q)n
∞
∏
1≤i<j≤n
(1−qsi−sj +j−i),
where s1≥s2≥···≥ sn are arbitrary integers.
64 Anatol N. Kirillov
2.4.2. Kostka-Foulkes polynomials.
We start with reminding some basic properties of the Kostka p olynomials (see e.g.
[Ma], [Kir3]).
Proposition F (Hook-formula). Let λ⊢n be a partition of natural number n. Then
we have
Kλ,(1n)(q) = qn(λ′) (q)n
∏
x∈λ
(
1−qh(x)
), (2.32)
whereh(x) := λi +λ′
j−i−j + 1 is the hook-length corresponding to the box x = (i,j )∈λ.
Before stating the next result about Kostka polynomials, le t us explain some notation.
Namely, let STY( λ,µ ) be a set of all (semi)standard Young tableaux of shape λ and
weight (or content, or evolution) µ. It is well-known (see e.g. [Ma]) that # |STY(λ,µ )| =
dim Vλ(µ), i.e. the number of (semi)standard Young tableaux of shape λ and weight
µ is equal to the dimension of weight µ subspace of the highest weight λ irreducible
representationVλ of the Lie algebra gln. Following A. Lascoux and M.-P. Sch¨ utzenberger,
for given partitionsλ andµ we denote byc(T ) (correspondently
c(T )) the charge (cocharge)
of a tableau T∈ STY(λ,µ ).
Proposition G (Lascoux-Sch¨ utzenberger [LS]).If λ and µ are partitions, then
Kλ,µ(q) =
∑
T ∈STY(λ,µ)
qc(T ).
In the remaining part of this section we are going to explain a new combinatorial
formula for Kostka polynomial Kλ,µ(q) coming from the Bethe ansatz technique (see e.g.
[Kir2], [Kir3]).
From the representation theoretic point of view, Bethe’s an satz method for the gener-
alized Heisenberg magnet gives a very powerful and convenie nt algorithm for decomposing
the tensor product of some special representations of semi- simple Lie algebra g into irre-
ducible parts (see e.g. [KR2], [Ku]). In the case of the Lie al gebra gln, the Bethe ansatz
method gives for a tensor product multiplicity Mult Vλ (Vµ1⊗···⊗ VµN )an equivalent de-
scription as the number of solutions to some special system o f algebraic equations (the
so-called Bethe equations, see Exercise 2). Using the so-ca lled ”string conjecture” one
can ﬁnd the number of ”string solutions” to the system of Beth e’s equations. In spite of
the well-known fact (see e.g. [EKK]) that solution to the Bet he equations does not have a
”string nature” in general, the total number of solutions (w ith multiplicities) to the system
of Bethe’s equations given by using the ”string conjecture” , appears to be correct. The
last statement (the so-called combinatorial completeness of Bethe’s states) was proven in
[Kir2] (see also [KL]) for the case when all weights µi have a rectangular shape (i.e. each
weightµi is a proportional to some fundamental weight wa).
A possibility to apply the Bethe ansatz technique to combina torics of Young tableaux
is based on the well-known fact (see e.g. [Lit] or [Stn]) that for the Lie algebra gLn (more
Dilogarithm identities 65
generally, for the Lie superalgebra gl(N/M)) a weight multiplicity can be expressed in
terms of tensor product multiplicity. Namely, if l(λ)≤n and µ = (µ1,...,µ N ), then
#|STY(λ,µ )| =Kλ,µ = dim V (gl(N))
λ (µ) = Mult
V
(gl(n))
λ
(
V (gl(n))
µ1w1 ⊗···⊗ V (gl(n))
µN w1
)
.
More generally (see e.g. [Se], [KR2]), if λ,µ as above and η = (η1,...,η M ), then
dim V (gl(N/M))
λ (µ|η) = Mult
V
(gl(n))
λ
(
V (gl(n))
µ1w1 ⊗···⊗ V (gl(n))
µN w1 ⊗V (gl(n))
wη 1
⊗···⊗ V (gl(n))
wη M
)
.
Now we are going to state the main result about the tensor prod uct multiplicities which
follows from Bethe’s ansatz technique. Thus, let µ1,...,µ N be the rectangular shape
partitions (i.e, µj = mi,jwi for some i, 1≤ i≤ n, 1≤ j≤ N ) and λ be a partition such
that|λ| =∑
j|µj| andl(λ)≤n. Let us denote by µ(i), 1≤i≤n, a composition composed
by those m⁄= 0 for which there exists µj (1≤j≤N ) such that µj =mwi.
Proposition 1 ([KR2]).
Mult
V
(gl(n))
λ
(
V (gl(n))
µ1 ⊗···⊗ V (gl(n))
µN
)
=
∑
{ν}
K{ν}, (2.33)
where summation is taken over all conﬁgurations {ν} of type (λ;{µ}).
Let us explain the notation in (2.33). By deﬁnition, a conﬁgu ration{ν} of type (λ;{µ})
is a collection of partitions (or Young diagrams) {ν} ={ν(1),ν (2),...} such that
i)|ν(k)| :=ν(k)
1 +ν(k)
2 +... =
∑
j≥k+1
(λj− (j−k)|µ(j)|),
ii)P (k)
r (ν;{µ}) := Qr(µ(k)) +Qr(ν(k−1))− 2Qr(ν(k)) +Qr(ν(k+1))≥ 0, for all k,r≥ 1,
where ν(0) := 0 and Qr(ν) :=
∑
j≤r
ν′
j. Let us remind that for a partition λ we denote by
λ′ = (λ′
1,λ ′
2,... ) the conjugate partition, i.e. λ′
i ={j| λj≥i}.
We deﬁne the Kostka number K{ν} corresponding to a conﬁguration {ν} as follows
K{ν} :=
∏
k,r


P (k)
r (ν;{µ}) +mr(ν(k))
mr(ν(k))

, (2.34)
where mr(ν(k)) is a number of length r parts in partition ν(k) and
(
N
n
)
is the binomial
coeﬃcient:
(
N
n
)
=



N !
n!(N−n)!, if 0≤n≤N ;
0 otherwise.
An analytical proof of Proposition 1 is given in [Kir1] and [K ir2]. Another proof of
Proposition 1 (see [Kir3] and [KK]) is based on a combinatori al interpretation of the both
66 Anatol N. Kirillov
sides of equality (2.34). The left hand side of (2.34) admits an interpretation as the number
of special kind of tableaux (see [KK]), whereas the right han d side admits that in terms of
rigged conﬁgurations (see [Kir3]). The main step of a combin atorial proof of Proposition
1 is to construct a bijection between the set of rigged conﬁgu rations and that of special
kind of tableaux. The bijection constructed in [Kir3] has ma ny intriguing and mysterious
properties such as agreements with cocharge construction, the Sch¨ utzenberger involution
and so on. For example, let us deﬁne a q-analog of the RHS(2.34) by the following way
K λ,{µ}(q) :=
∑
{ν}
K{ν}(q), K {ν}(q) := qc(ν)∏
k,r


P (k)
r (ν;{µ}) +mr(ν(k))
mr(ν(k))


q
, (2.35)
where summation is taken over all conﬁgurations {ν} of type ( λ;{µ}) and the cocharge
c(ν) of a conﬁguration {ν} is deﬁned by
c(ν) :=
∑
k,r≥1
(
(ν(k−1))′
r− (ν(k))′
r
2
)
−n(λ), ν (0) := 0.
Theorem 12 ([Kir3]). i) Let us assume that µ := µ(1) is a partition, l(µ)≤ N and
µ(i) = 0, if 2≤i≤n. Then
K λ,{µ}(q) = K λ,µ(q),
whereK λ,µ(q) is the Lusztig q-analog of weight multiplicity for the Lie algebra glN .
ii) Let us assume that µ := µ(1) is a partition, l(µ)≤ N and µ(i)
k = 0 for all k≥ 2
and 2≤ i≤ n. Let us deﬁne the partition η = (µ(2)
1 ,µ (3)
1 ,...,µ (n)
1 )+ corresponding to a
composition (µ(2)
1 ,µ (3)
1 ,...,µ (n)
1 ). If l(η′)≤M then
Kλ,{µ}(q) = K λ,µ|η(q),
where K λ,µ|η(q) is the q-analog of weight multiplicity dim V (gl(N|M ))
λ (µ|η) for the Lie
superalgebra gl(N|M ) (see e.g. [Ser]).
The formula (2.35) is very convenient in many combinatorial applications (see e.g.
[Kir3], [Kir5], [Kir8], [F]). However, there exist other fo rms for (2.35), using the diﬀerent
parameterizations of the same type conﬁgurations set. For e xample, it is possible (and use-
ful !) to rewrite the formula (2.35) for Kλ,{µ}(q) using the vacancy numbers{P (k)
r (ν;{µ})}
instead of parameters {ν(k)
r }. But having in mind the applications of our formula (2.35)
for (dual) Kostka polynomials to a problem of computing the b ranching functions for in-
tegrable highest weight representations of the aﬃne Lie alg ebras, it is more convenient
to rewrite the RHS(2.35) in terms of parameters mr(ν(k)). Namely, let us ﬁx a natural
numberl such that mp(ν(k)) = 0, if p≥l and 1≤k≤n. We deﬁne a vector m :=m(ν) =
(m1(ν(1)),...,m l(ν(1)),m 1(ν(2)),...,m l(ν(2)),...,m 1(ν(n)),...,m l(ν(n)))∈ Zln
+.
Dilogarithm identities 67
Then it is almost trivial exercise to show that
1) P (k)
r (ν;{µ}) +mr(ν(k)) = (m(I−B) +m0)(k)
r , where
i) B =Cn⊗T −1
l ∈ Matln×ln(Z), and
Cn =





2 −1 ··· 0
−1 ···
··· ··· ···
··· − 1
0 ··· − 1 2





n×n
,
T −1
l =





2 −1 ··· 0
−1 2 ···
··· ··· ···
··· − 1 2 −1
0 ··· − 1 1





−1
l×l
= (min(a,b ))1≤a,b≤l ;
ii) vector m0 := (m(k)
0,r ), where m(k)
0,r =
∑
j≤r
(µ(k))′
j, and I :=Iln = (δa,b)1≤a,b≤ln.
2)
c(ν) = 1
2mBmt−n(λ);
3) vector m∈ Zln
+ satisﬁes the following constraint m·Q =γ, where
i) γ := (γ(k)
r ), γ(k)
r =
∑
j≥k+1
{
λj− (j−k)| µ(j)|
}
;
ii) Q :=In⊗


1 ... 1
...
l ... l


l×l
.
Consequently, we have
qn(λ)
Kλ,{µ}(q) =
∑
m∈ Zln
+
m·Q =γ
q
1
2 mBmt∏
a
[
(m(I−B) +m0)a
ma
]
q
. (2.36)
Example (Melzer’s conjecture [Me1]). Let us consider a particular c ase of our formula
(2.36) for (dual) Kostka polynomials when λ = ( 1
2L+S, 1
2L−S),µ(1) = (1 L) andµ(k) = 0,
if k≥ 2. Here a ”spin” S is a half-integer such that M := 1
2L−S∈ Z+.
First of all, in our case we have B = 2T −1
M , a vector m0 = (L,...,L )∈ ZM
+ and the
vacancy numbers for given conﬁguration m∈ ZM
+ are the following ones Pa(m;{µ}) =
L− 2(mT −1
M )a. Consequently (compare [Me1], (3.10)),
F (L)
S (q) := q−n(λ) ∑
ma∈ Z+∑ M
a=1ama =M
q
1
2 mBmt
M∏
a=1
[
L + (m(I−B))a
ma
]
q
=K λ,(1L)(q).
(2.37)
68 Anatol N. Kirillov
On the other hand, using the hook-formula (see Proposition F ) for Kostka polynomials,
one can easily ﬁnd
K λ,(1L)(q) = 1−q2S+1
1−q
1
