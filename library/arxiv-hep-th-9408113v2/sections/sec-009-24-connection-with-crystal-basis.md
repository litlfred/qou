---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-009-24-connection-with-crystal-basis
section_title: "Connection with crystal basis."
section_number: 2.4
pages: 60-79
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
toc_source: inferred
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
2.4.1. Level 1 vacuum representation Λ0 of the aﬃne Lie algebra c
sln.
Theorem 11. Let µ = (µ1, . . ., µn) be a composition. Then
X
λ, l(λ)≤n
Kλ,µ · Kλ, (1|λ|)(q) = qn(µ′)

|µ|
µ1, . . ., µn

q
,
(2.28)
where

N
m1, . . ., mn

q
:=
(q)N
(q)m1 . . . (q)mn
is the q-analog of multinomial coeﬃcient (N = m1 + · · · + mn).
Let us explain notation. Here
i) Kλ,µ is the so-called Kostka number, which is equal to the number of (semi)standard
Young tableaux of shape λ and weight µ, or, equivalently, to the dimension of weight µ
subspace Vλ(µ) of the irreducible highest weight λ representation Vλ of the Lie algebra
gln:
Kλ,µ = dim Vλ(µ).
Dilogarithm identities
61
ii) Kλ,µ(q) is the so-called Kostka-Foulkes polynomial (see e.g. [Ma]), which can be
deﬁned from a decomposition of the Schur functions in terms of the Hall-Littlewood ones:
sλ(x) =
X
µ
Kλ,µ(q)Pµ(x; q).
It is well-known (see e.g. [Lu2] or [Ma]), that polynomial Kλ,µ(q) := qn(µ)−n(λ)Kλ,µ(q−1)
coincides with Lusztig’s q-analog of weight multiplicity dim Vλ(µ).
iii) n(λ) :=
n
X
i=1
(i −1)λi =
n
X
i=1

λ′
j
2

=
X
1≤i<j≤n
min(λi, λj), if λ = (λ1, . . . , λn) ∈Zn
+.
The proof of Theorem 11 is based on the well-known results from the theory of sym-
metric functions. We will use the notation and terminology involving symmetric functions
from Macdonald [Ma].
Lemma 6.
X
λ
sλ(x)Kλ,µ(q) = Qµ

x
1 −q

.
Here we used the standard λ-ring theory notation, namely, for any symmetric function
f(x) := f(x1, x2, . . .) and a new set of variables y = (y1, y2, . . .) one can deﬁne f(xy) =
f(. . ., xiyj . . .).
Proof. Let us remind that the Hall-Littlewood functions Pλ and Qλ satisfy the following
orthogonality condition (see [Ma], Chapter II, (4.4))
X
λ
Qλ(x; q)Pλ(y; q) =
Y
i,j
1 −qxiyj
1 −xiyj
.
Consequently,
X
λ
Qλ

x
1 −q

Pλ(y, q) =
Y
i, j
k ≥0
1 −qk+1xiyj
1 −qkxiyj
=
Y
i,j
(1 −xiyj)−1 =
X
λ
sλ(x)sλ(y).
Here we used the orthogonality of Schur’s functions ([Ma], Chapter I, (4.3)). It remains to
remind the deﬁnition of Kostka-Foulkes polynomials:
sλ(y) =
X
µ
Kλ,µ(q)Pµ(y; q).
To continue, let us remark that if m ≥n, then
Q(kn)(x1, . . ., xm; q) = (q; q)n(en(x))k,
see [Ma], Chapter III,
(2.8).
62
Anatol N. Kirillov
Therefore, in order to prove Theorem 9 we have to decompose the symmetric function
λ
sλ(x)Kλ,(1n)(q) = Q(1n)

x
1 −q

= (q; q)nen

x
1 −q

in terms of the monomial symmetric ones mλ(x). For this purpose, let us remind that by
deﬁnition (CT:= constant term)
en

x
1 −q

= CT

t−n Y
j
(−txj; q)∞

.
Thus, using the Euler result
(−z; q)∞=
∞
n=0
znq
n(n−1)
2
(q; q)n
,
one can obtain
en

x
1 −q

=
X
µ⊢n
qn(µ′)
(q; q)µ
mµ(x),
where for a partition µ = (µ1, µ2, . . ., µn), we set (q; q)µ :=
n
Y
j=1
(q; q)µj. Consequently,
X
λ
sλ(x)Kλ,(1n)(q) =
X
µ⊢n
qn(µ′)

n
µ1 . . . µn

q
mµ(x).
Remark. The identity (2.28) is implicitly contained in the Terada preprint [Te]. The
proof given in [Te] is based on a study of the cohomology groups of the variety of N-stable
ﬂags. Our proof is pure algebraic and based on the theory of symmetric functions. Later
B. Leclerc and J.-Y. Thibon gave almost the same proof (unpublished). It is possible to
give a pure combinatorial proof of (2.28) using the properties of the Robinson-Schensted
correspondence. Finally, the identity (2.28) can be extracted from [DJKMO1].
Corollary 6 (of Theorem 11).
X
λ, l(λ)≤n
sλ(x)Kλ,(1|λ|)(q) =
X
m∈Zn
+
q
Σ

mi
2

xm

|m|
m1, . . ., mn

q
.
(2.29)
Dilogarithm identities
63
Now we are going to consider an appropriate limit |m| →∞in (2.29). More exactly,
let us assume that |m| = nN, and consider the following variant of (2.29):
q−(N2−N)n
2
X
λ,l(λ)≤n
sλ(x1, . . ., xn)
(x1 . . . xn)N Kλ,(1|λ|)(q)
=
X
k ∈Zn,
|k| = 0, ki ≥−N, ∀i
xk1
1 . . . xkn
n q
1
2
P
k2
i

nN
k1 + N, . . . , kn + N

q
.
(2.30)N
First of all,
lim
N→∞RHS(2.30)N =
1
(q)n−1
∞
X
m ∈Zn
|m| = 0
xmq
1
2
P
m2
i =
1
(q)n−1
∞
X
k∈Zn−1
zk1
1 . . . zkn−1
n−1 q
1
2 kAn−1kt,
where zi =
xi
xi−1
, 1 ≤i ≤n −1, x0 := xn. On the other hand,
lim
N→∞LHS(2.30)N =
X
λ = (λ1 ≥λ2 ≥· · · ≥λn) ∈Zn
|λ| = 0
sλ(x1, . . ., xn)bλ(q),
where for given weight λ we set (λN := λ + (N n))
bλ(q) := lim
N→∞q−n(N2−N)
2
KλN,(1|λN |)(q) = qn(λ′)
(q)n−1
∞
Y
1≤i≤j≤n
(1 −qλi−λj−i+j).
(2.31)
Finally, it is follow from (2.30)N that
X
λ, l(λ)≤n
sλ(x1, . . ., xn)bλ(q) = Θ(x)
(q)n−1
∞
,
where
Θ(x) =
X
m = (m1, . . ., mn) ∈Zn,
|m| = 0
xmq
1
2 (m2
1+...+m2
n),
is the theta-function corresponding to the basic representation V (Λ0) of c
sln.
Hence, bλ(q) is the branching function for representation Λ0 of the aﬃne algebra c
sln.
Remark. It is interesting to compare the formula (2.31) with the following result of
V. Kac ([Kac], (14.12.10)): for the inﬁnite rank aﬃne algebra of type A∞
dimqL(Λs1 + Λs2 + · · · + Λsn) =
1
(q)n∞
Y
1≤i<j≤n
(1 −qsi−sj+j−i),
where s1 ≥s2 ≥· · · ≥sn are arbitrary integers.
64
Anatol N. Kirillov
2.4.2. Kostka-Foulkes polynomials.
We start with reminding some basic properties of the Kostka polynomials (see e.g.
[Ma], [Kir3]).
Proposition F (Hook-formula). Let λ ⊢n be a partition of natural number n. Then
we have
Kλ,(1n)(q) = qn(λ′)
(q)n
Y
x∈λ

1 −qh(x),
(2.32)
where h(x) := λi + λ′
j −i −j + 1 is the hook-length corresponding to the box x = (i, j) ∈λ.
Before stating the next result about Kostka polynomials, let us explain some notation.
Namely, let STY(λ, µ) be a set of all (semi)standard Young tableaux of shape λ and
weight (or content, or evolution) µ. It is well-known (see e.g. [Ma]) that #|STY(λ, µ)| =
dim Vλ(µ), i.e.
the number of (semi)standard Young tableaux of shape λ and weight
µ is equal to the dimension of weight µ subspace of the highest weight λ irreducible
representation Vλ of the Lie algebra gln. Following A. Lascoux and M.-P. Sch¨utzenberger,
for given partitions λ and µ we denote by c(T) (correspondently c(T)) the charge (cocharge)
of a tableau T ∈STY(λ, µ).
Proposition G (Lascoux-Sch¨utzenberger [LS]). If λ and µ are partitions, then
Kλ,µ(q) =
X
T ∈STY(λ,µ)
qc(T ).
In the remaining part of this section we are going to explain a new combinatorial
formula for Kostka polynomial Kλ,µ(q) coming from the Bethe ansatz technique (see e.g.
[Kir2], [Kir3]).
From the representation theoretic point of view, Bethe’s ansatz method for the gener-
alized Heisenberg magnet gives a very powerful and convenient algorithm for decomposing
the tensor product of some special representations of semi-simple Lie algebra g into irre-
ducible parts (see e.g. [KR2], [Ku]). In the case of the Lie algebra gln, the Bethe ansatz
method gives for a tensor product multiplicity MultVλ(Vµ1 ⊗· · · ⊗VµN )an equivalent de-
scription as the number of solutions to some special system of algebraic equations (the
so-called Bethe equations, see Exercise 2). Using the so-called ”string conjecture” one
can ﬁnd the number of ”string solutions” to the system of Bethe’s equations. In spite of
the well-known fact (see e.g. [EKK]) that solution to the Bethe equations does not have a
”string nature” in general, the total number of solutions (with multiplicities) to the system
of Bethe’s equations given by using the ”string conjecture”, appears to be correct. The
last statement (the so-called combinatorial completeness of Bethe’s states) was proven in
[Kir2] (see also [KL]) for the case when all weights µi have a rectangular shape (i.e. each
weight µi is a proportional to some fundamental weight wa).
A possibility to apply the Bethe ansatz technique to combinatorics of Young tableaux
is based on the well-known fact (see e.g. [Lit] or [Stn]) that for the Lie algebra gLn (more
Dilogarithm identities
65
generally, for the Lie superalgebra gl(N/M)) a weight multiplicity can be expressed in
terms of tensor product multiplicity. Namely, if l(λ) ≤n and µ = (µ1, . . ., µN), then
#|STY(λ, µ)| = Kλ,µ = dim V (gl(N))
λ
(µ) = Mult
V
(gl(n))
λ

V (gl(n))
µ1w1
⊗· · · ⊗V (gl(n))
µN w1

.
More generally (see e.g. [Se], [KR2]), if λ, µ as above and η = (η1, . . ., ηM), then
dim V (gl(N/M))
λ
(µ|η) = Mult
V
(gl(n))
λ

V (gl(n))
µ1w1
⊗· · · ⊗V (gl(n))
µN w1
⊗V (gl(n))
wη1
⊗· · · ⊗V (gl(n))
wηM

.
Now we are going to state the main result about the tensor product multiplicities which
follows from Bethe’s ansatz technique.
Thus, let µ1, . . ., µN be the rectangular shape
partitions (i.e, µj = mi,jwi for some i, 1 ≤i ≤n, 1 ≤j ≤N) and λ be a partition such
that |λ| = P
j |µj| and l(λ) ≤n. Let us denote by µ(i), 1 ≤i ≤n, a composition composed
by those m̸ = 0 for which there exists µj (1 ≤j ≤N) such that µj = mwi.
Proposition 1 ([KR2]).
Mult
V
(gl(n))
λ

V (gl(n))
µ1
⊗· · · ⊗V (gl(n))
µN

=
X
{ν}
K{ν},
(2.33)
where summation is taken over all conﬁgurations {ν} of type (λ; {µ}).
Let us explain the notation in (2.33). By deﬁnition, a conﬁguration {ν} of type (λ; {µ})
is a collection of partitions (or Young diagrams) {ν} = {ν(1), ν(2), . . .} such that
i) |ν(k)| := ν(k)
1
+ ν(k)
2
+ . . . =
X
j≥k+1
(λj −(j −k)|µ(j)|),
ii) P (k)
r
(ν; {µ}) := Qr(µ(k)) +Qr(ν(k−1)) −2Qr(ν(k)) +Qr(ν(k+1)) ≥0, for all k, r ≥1,
where ν(0) := 0 and Qr(ν) :=
X
j≤r
ν′
j. Let us remind that for a partition λ we denote by
λ′ = (λ′
1, λ′
2, . . .) the conjugate partition, i.e. λ′
i = {j | λj ≥i}.
We deﬁne the Kostka number K{ν} corresponding to a conﬁguration {ν} as follows
K{ν} :=
Y
k,r


P (k)
r
(ν; {µ}) + mr(ν(k))
mr(ν(k))

,
(2.34)
where mr(ν(k)) is a number of length r parts in partition ν(k) and

N
n

is the binomial
coeﬃcient:

N
n

=



N!
n!(N −n)!,
if 0 ≤n ≤N;
0
otherwise.
An analytical proof of Proposition 1 is given in [Kir1] and [Kir2]. Another proof of
Proposition 1 (see [Kir3] and [KK]) is based on a combinatorial interpretation of the both
66
Anatol N. Kirillov
sides of equality (2.34). The left hand side of (2.34) admits an interpretation as the number
of special kind of tableaux (see [KK]), whereas the right hand side admits that in terms of
rigged conﬁgurations (see [Kir3]). The main step of a combinatorial proof of Proposition
1 is to construct a bijection between the set of rigged conﬁgurations and that of special
kind of tableaux. The bijection constructed in [Kir3] has many intriguing and mysterious
properties such as agreements with cocharge construction, the Sch¨utzenberger involution
and so on. For example, let us deﬁne a q-analog of the RHS(2.34) by the following way
Kλ,{µ}(q) :=
X
{ν}
K{ν}(q),
K{ν}(q) := qc(ν) Y
k,r


P (k)
r
(ν; {µ}) + mr(ν(k))
mr(ν(k))


q
,
(2.35)
where summation is taken over all conﬁgurations {ν} of type (λ; {µ}) and the cocharge
c(ν) of a conﬁguration {ν} is deﬁned by
c(ν) :=
X
k,r≥1

(ν(k−1))′
r −(ν(k))′
r
2

−n(λ),
ν(0) := 0.
Theorem 12 ([Kir3]). i) Let us assume that µ := µ(1) is a partition, l(µ) ≤N and
µ(i) = 0, if 2 ≤i ≤n. Then
Kλ,{µ}(q) = Kλ,µ(q),
where Kλ,µ(q) is the Lusztig q-analog of weight multiplicity for the Lie algebra glN.
ii) Let us assume that µ := µ(1) is a partition, l(µ) ≤N and µ(i)
k
= 0 for all k ≥2
and 2 ≤i ≤n. Let us deﬁne the partition η = (µ(2)
1 , µ(3)
1 , . . ., µ(n)
1 )+ corresponding to a
composition (µ(2)
1 , µ(3)
1 , . . . , µ(n)
1 ). If l(η′) ≤M then
Kλ,{µ}(q) = Kλ,µ|η(q),
where Kλ,µ|η(q) is the q-analog of weight multiplicity dim V (gl(N|M))
λ
(µ|η) for the Lie
superalgebra gl(N|M) (see e.g. [Ser]).
The formula (2.35) is very convenient in many combinatorial applications (see e.g.
[Kir3], [Kir5], [Kir8], [F]). However, there exist other forms for (2.35), using the diﬀerent
parameterizations of the same type conﬁgurations set. For example, it is possible (and use-
ful !) to rewrite the formula (2.35) for Kλ,{µ}(q) using the vacancy numbers {P (k)
r
(ν; {µ})}
instead of parameters {ν(k)
r
}. But having in mind the applications of our formula (2.35)
for (dual) Kostka polynomials to a problem of computing the branching functions for in-
tegrable highest weight representations of the aﬃne Lie algebras, it is more convenient
to rewrite the RHS(2.35) in terms of parameters mr(ν(k)). Namely, let us ﬁx a natural
number l such that mp(ν(k)) = 0, if p ≥l and 1 ≤k ≤n. We deﬁne a vector m := m(ν) =
(m1(ν(1)), . . ., ml(ν(1)), m1(ν(2)), . . ., ml(ν(2)), . . ., m1(ν(n)), . . ., ml(ν(n))) ∈Zln
+ .
Dilogarithm identities
67
Then it is almost trivial exercise to show that
1) P (k)
r
(ν; {µ}) + mr(ν(k)) = (m(I −B) + m0)(k)
r , where
i) B = Cn ⊗T −1
l
∈Matln×ln(Z), and
Cn =





2
−1
· · ·
0
−1
· · ·
· · ·
· · ·
· · ·
· · ·
−1
0
· · ·
−1
2





n×n
,
T −1
l
=





2
−1
· · ·
0
−1
2
· · ·
· · ·
· · ·
· · ·
· · ·
−1
2
−1
0
· · ·
−1
1





−1
l×l
= (min(a, b))1≤a,b≤l ;
ii) vector m0 := (m(k)
0,r), where m(k)
0,r =
X
j≤r
(µ(k))′
j, and I := Iln = (δa,b)1≤a,b≤ln.
2) c(ν) = 1
2mBmt −n(λ);
3) vector m ∈Zln
+ satisﬁes the following constraint m · Q = γ, where
i) γ := (γ(k)
r ), γ(k)
r
=
X
j≥k+1
n
λj −(j −k) | µ(j)|
o
;
ii) Q := In ⊗


1
. . .
1
. . .
l
. . .
l


l×l
.
Consequently, we have
qn(λ)Kλ,{µ}(q) =
X
m ∈Zln
+
m · Q = γ
q
1
2 mBmt Y
a

(m(I −B) + m0)a
ma

q
.
(2.36)
Example (Melzer’s conjecture [Me1]). Let us consider a particular case of our formula
(2.36) for (dual) Kostka polynomials when λ = ( 1
2L+S, 1
2L−S), µ(1) = (1L) and µ(k) = 0,
if k ≥2. Here a ”spin” S is a half-integer such that M := 1
2L −S ∈Z+.
First of all, in our case we have B = 2T −1
M , a vector m0 = (L, . . ., L) ∈ZM
+ and the
vacancy numbers for given conﬁguration m ∈ZM
+
are the following ones Pa(m; {µ}) =
L −2(mT −1
M )a. Consequently (compare [Me1], (3.10)),
F(L)
S
(q) := q−n(λ)
X
ma ∈Z+
PM
a=1 ama = M
q
1
2 mBmt
M
Y
a=1

L + (m(I −B))a
ma

q
= Kλ,(1L)(q).
(2.37)
68
Anatol N. Kirillov
On the other hand, using the hook-formula (see Proposition F) for Kostka polynomials,
one can easily ﬁnd
Kλ,(1L)(q) =
1 −q2S+1
1 −q
1
2 L+S+1

L
1
2L −S

q
(2.38)
=

L
1
2L −S

q
−q2S+1

L
1
2L −S −1

q
≡B(L)
S (q).
Thus, F(L)
S
(q) = B(L)
S (q), as we set out to prove.
Now if L →∞, S →∞and M = 1
2L −S is ﬁxed (Thermodynamic limit), then it
follows from (2.37) and (2.38) that
X
m = (ma) ∈ZM
+
PM
a=1 ama = M
q
1
2 mBmt
M
Y
a=1
(q)ma
= qM
(q)M
.
Another interesting limit is L →∞, M →∞and S being ﬁxed (Thermodynamic
Bethe ansatz (TBA) limit). In the last case one can ﬁnd
1 −q2S+1
1 −q
X
{ma∈Z+}
q
1
2 mBmt+|m|
Y
a≥1
(q)ma
= 1 −q2S+1
(q)∞
,
(2.39)
where summation in (2.39) is taken over all sequences {ma ∈Z+}∞
a=1 such that ma = 0
for almost all indices a, and B := B∞= 2(min(a, b)), 1 ≤a, b < ∞.
A proof of the ”limiting” identity (2.39). First of all let us remark that if a
partition λ consists of only two parts, then for any weight µ and any conﬁguration ν of
type (λ; µ) one can compute the cocharge of ν by the following rules
c(ν) = mBmt −n(λ) = 2n(ν) := 2
X
k≥1

ν′
k
2

.
(2.40)
Now let us consider a sequence of conﬁgurations {ν := ν(M)} of types (λ := (M + 2S, M);
(1|λ|)), M ≥1. It is clear from the formulae for cocharge (see (2.40)), that under the
limit M →∞and S is ﬁxed, the sequence of conﬁgurations {ν(M)} gives a non-zero
contribution to the limit
lim
M →∞
S is ﬁxed
Kλ=(M+2S,M),(1|λ|)(q)
if and only if
lim
M→∞c(ν(M)) < ∞.
Dilogarithm identities
69
The last condition is equivalent to the following one: ν(M) = (ν1, eν), where ν1 :=
ν1(M) →∞if M →∞and the partition eν does not depend on M. It is clear that under
these assumptions the cocharge c(ν) = P
k≥1(eν′
k)2 + |eν| does not depend on M at all. It
remains to consider the limit (ν := ν(M))
lim
M→∞K{ν(M)}(q) = lim
L→∞qc(ν) Y
n

L −2Qn(ν) + mn(ν)
mn(ν)

q
.
It is clear that if n ≤eν1, then L −2Qn(ν(M)) →∞, if M →∞, and
lim
M→∞

L −2Qn(ν(M)) + mn(ν(M))
mn(ν(M))

=
1
(q)mn(eν)
.
Now, if eν1 < n < ν1, then νn(ν) = 0. Finally, if n = ν1, then L −2Qn(ν(M)) = 2S and
mn(ν(M)) = 1. It remains to put ma := mn(eν).
It is well-known (see e.g. [BS]), that the RHS of (2.39) is the character χVir
S
= Tr qL0−S2
of the irreducible highest weight representation of the Virasoro algebra at central charge
c = 1 and highest weight h = S2, S ∈1
2Z≥0.
More generally, let us consider the case when λ is a partition l(λ) ≤n and µ(1) = (1|λ|),
µ(k) = 0, if k ≥2. Then we have (L := |λ|, eL := |λ| −λ1)
Kλ,(1L)(q) =
X
m
q
1
2 mBmt Y
a

(m(I −B) + m0)a
ma

q
,
(2.41)
where B = Cn−1 ⊗T −1
e
L , m0 = (m(k)
0,r) and m(k)
0,r = L · δk,1, 1 ≤k ≤n −1, 1 ≤r ≤eL. The
summation in (2.41) is taken over all sequences m ∈Z(n−1)e
L
+
under the following constraint
e
L
X
r=1
rm(k)
r
=
X
j≥k+1
λj,
1 ≤k ≤n −1.
It follows from the hook-formula (see Proposition F) that
Kλ,(1L)(q) =
(q)L
x∈λ
(1 −qh(x))
.
Now let us consider the limit L →∞, λ1 →∞, but the partition eλ = (λ2, λ3, . . ., λn)
is ﬁxed (Thermodynamic limit). Then one can obtain the following identity
X
m=(m(k)
r
)
q
1
2 mBmt
e
L
Y
r=1
(q; q)m(1)
r
Y
k≥2, r≥1

(m(I −B))(k)
r
m(k)
r

q
=
qn(eλ)+|eλ|
Y
x∈eλ
(1 −qh(x))
,
(2.42)
70
Anatol N. Kirillov
where summation on m in (2.42) is the same as in (2.41). Another interesting limit is
L →∞all λi →∞(1 ≤i ≤n), but the diﬀerences (λn+1 := 0) λi −λi+1 (1 ≤i ≤n) are
ﬁxed (TBA limit). In this case one can obtain the following result
lim
L→∞KλL,(1|λL|)(q) =
Y
1≤i<j≤n
(1 −qλi−λj−i+j)
(q)n−1
∞
,
(2.43)
where λL = λ + (Ln).
It is well-known (see e.g. [KP] or Section 2.4.1, (2.31)), that the RHS of (2.43) is the
branching function for level 1 vacuum representation Λ0 of c
sln.
2.4.3. Level k vacuum representation kΛ0 of the aﬃne Lie algebra c
sl2
Theorem 13. Let µ = (µ1, µ2) be the length two composition, |µ| = 2N. Then
X
λ, l(λ)≤2
Kλ,µKλ,(2N)(q) =
X
m


N
µ1 −m
2
, µ2 −m
2
, m


q
· q
1
2 m2q
1
2 (n(µ′)−N).
(2.44)µ
Let us deduce from Theorem 13 some combinatorial applications. First of all, it is clear
that Kλ,µ = 1 if λ ⪰µ with respect to the dominant order (see e.g. [Ma]) and Kλ,µ = 0
otherwise. Hence (λ = (λ1 ≥λ2)),
Kλ,(2N)(q) = RHS(2.44)(λ1,λ2) −RHS(2.44)(λ1+1,λ2−1).
(2.45)
Using (2.45), one can ﬁnd
N
X
l=0
q−l 1 −q2l+1
1 −q
K(N+l,N−l),(2N )(q2)
(2.46)
= qN2−2N X
k
qk2



X
l≥0
′ (ql + q−l)ql2
"
N −k
N −k −l
2
#
q2




N
k

q2 .
The next Lemma makes it possible to simplify the RHS(2.46).
Lemma 7.
RHS(2.46) = qN2−2N
N
X
k=0
qk2+k(1 + q) . . .(1 + qN−k)

N
k

q2
.
(2.47)
Analytical proof of Lemma 7 will be given elsewhere.
Dilogarithm identities
71
Corollary 7 (Milne’s conjecture [Ml2]).
m
X
l=0
q−l 1 −q2l+1
1 −q
K(m+l,m−l),(2m)(q2)
(2.48)
=
m
X
k=0
qm2−2mqk2+k(1 + q) . . .(1 + qm−k)

m
k

q2 .
Corollary 8 (of Theorem 13). Let λ = (λ1, λ2) be a partition, |λ| ≡0 (mod 2), and
b2Λ0
λ
(q) be the branching function for the level 2 vacuum representation 2Λ0 of the aﬃne
Lie algebra c
sl2. Then
b2Λ0
λ
(q) = lim
N→∞q−NKλN,µN (q),
where λN = (λ1 + 2N, λ2 + 2N) and µN = (2M), M = 1
2|λ| + 2N.
Finally, let us generalize the identity (2.44)µ to the higher levels.
Theorem 14.
X
l(λ)≤2
Kλ,µKλ,(kN)(q)
(2.49)
=
X
m=(m1,m2,...,mk−1)∈Zk−1
+
q
1
k n(µ′)−k−1
2
Nq
mAk−1mt
k2


N
µ1 −m1
k
, µ2 −mk−1
k
, 1
k (mAk−1)a


q
.
Corollary 9 (of Theorem 14). Let λ = (λ1, λ2) be a partition, |λ| ≡0 (mod 2k), and
bkΛ0
λ
(q) be the branching function for the level k vacuum representation kΛ0 of the aﬃne
Lie algebra c
sl2. Then
lim
N→∞q−k(N2−N)KλN,µN (q) = bkΛ0
λ
(q),
where λN := (λ1 + kN, λ2 + kN) and µN = (kM), M := M(N) = 1
k|λ| + 2N.
Let us remind that, by deﬁnition, the partition (kM) is the one consisting of M parts
all equal to k.
Proof. Consider the following sum
ΣN :=
X
λ , l(λ) ≤2
|λ| = 2kN
sλ(x1, x2)
(x1x2)kN q−k(N2−N)Kλ,(k2N)(q).
(2.50)
It follows from Theorem 14 that
ΣN =
2kN
X
µ1=0
(x1/x2)µ1−kN
X
m=(m1,...,mk−1)∈Zk−1
+
q
1
k n(µ′)−(k−1)N−k(N2−N)q
mAk−1mt
k2
·


2N
µ1 −m1
k
, µ2 −mk−1
k
, 1
k (mAk−1)a


q
.
72
Anatol N. Kirillov
Let us put µ1 = m1 + (l + N)k (thus, µ2 = (N −l)k −m1) and z = x1/x2. It is clear that
1
k n(µ′) −(k −1)N −k(N 2 −N) = m2
1
k + kl2 + 2m1l.
Hence, we have
ΣN =
X
m = (m1, . . ., mk−1) ∈Zk−1
+
X
l ∈Z
l ≥−N −m1
k
zkl+m1qkl2+2m1lq
km2
1+mAk−1mt
k2
·


2N
l + N, N −l −m1 + mk−1
k
, 1
k (mA)a


q
.
Consequently,
lim
N→∞ΣN =
1
(q)2∞
X
m=(m1,...,mk−1)∈Zk−1
+
X
l∈Z
zkl+m1qkl2+2m1lq
km2
1+mAk−1mt
k2
k−1
Y
a=1
(q)−1
sa ,
(2.51)
where sa := 1
k (mAk−1)k−a.
Now let us rewrite the summation in the RHS(2.51) in terms of parameters
sa,
a = 1, . . ., k −1. One can easily check that
k−1
X
a=1
asa = m1,
km2
1 + mAk−1mt
k2
= sT −1
k−1st.
Consequently,
lim
N→∞ΣN =
1
(q)2∞
∞
X
m1=0
X
s = (s1, . . ., sk−1) ∈Zk−1
+
P
a asa = m1
X
l∈Z
zkl+m1qkl2+2m1l qsT −1
k−1st
Y
a
(q)sa
=
1
(q)2∞
∞
X
m1=0
Θk
m1(z)ck
m1(q) = ch(V (kΛ0)).
On the other hand,
lim
N→∞
X
λ, l(λ) ≤2
|λ| = 2kN
sλ(x1, x2)
(x1x2)kN q−k(N2−N)KλN,µN (q) =
X
λ = (λ1 ≥λ2)
|λ| = 0
sλ(x)bλ(q),
where bλ(q) = lim
N→∞q−k(N2−N)KλN,(k2N)(q).
Dilogarithm identities 73

Consequently, b,(q) is the branching function of level k vacuum-sl5 representation kA.
|
We assume that any branching function bh (q) of integrable highest weight representa-
tion V(A) of the affine Lie algebra Sly can be constructed as an appropriate limit of the
Kostka-Foulkes polynomials. More exactly:

Conjecture 4. Let A = kAo be the level k vacuum representation of the affine Lie
algebra sl,. Then

bX (q) = Nim, Ey canny(q),
where An := A+ ((KN)"), A= (Ar > Ap > +++ > An) and |A| = 0.

Remark. There exists an interesting connection between the Milne polynomials ([MI11],
[M12], [Gal])

My(as0) = Yo sale) Kala) = Qu (<<).
where x = (x1,...,%,), and the characters chV (A) of integrable highest weight represen-
tations V(A) of the affine Lie algebra Sl,. Roughly speaking, the character chV(A) is
an appropriate limit of Milne’s polynomials (see the proofs of Theorems 11,13 and 14).
It would be interesting to know the solutions to what kind of hierarchy (= a system of
nonlinear partial differential equations) the characters of integrable highest weight repre-
sentations of $1, are.

2.4.4. Crystal basis and Robinson-Schensted correspondence.

In this section we are going to discuss briefly a connection between a combinatorial
description of the so-called crystal basis [Ka] of an integrable sl,,-module V* of level k,
found by Jimbo, Misra, Miwa and Okado in [JMMO] (see also [MM], [KKNMMNN] and
[DJKMO]1], [DJKMO2]) and the Kostka-Foulkes polynomials via the Robinson-Schemsted-
Knuth (RSK) correspondence (see e.g. [Sa], where a construction and basic properties of
RSK are given).

The starting point for us is the following variant of the Jimbo-Misra-Miwa-Okado for-
mula for the character ch(V,*) in the paths realization of the crystal basis, due to E. Frenkel
and A. Szenes [FrSz2]. Thus (see [Fr$z2], Section 6), let us introduce the set

Sh = {a=(a1,...,4n) | ai > 0, ay +--+ + Gn =k}.

Denote by 7 : (a1,42,---,;@n) — (Gn, 41,---,@n—1) the cyclic permutation acting on S*
and define the element a* € S* by a* = (k,0,...,0). Now the ground state path pu is
the sequence (a*, ra*,r?a*,...), and the set of restricted paths R* is the set of sequences
n = (no,m,---) of elements nj € S*_ which coincide with jz except for a finite set of indices.

Define the weight function w on R* by the formula

fe)

w(n) = > m[H(tm—1;,%m) _ A(tm—1;lm)] 5

m=1
74
Anatol N. Kirillov
where Hn(a, b) := max
1≤i≤n(hi(a, b)) and
hi(a, b) =
i
X
j=1
aj −
i−1
X
j=1
bj.
Theorem G ([JMMO]). As formal power series in q
ch V k
n =
X
η∈Rk
n
qw(η).
Now let us introduce the sets
WN = {η ∈Rk
n | ηj = µj for j ≥nN},
W a
N = {η ∈Rk
n | ηnN−1 = a, ηj = µj for j ≥nN},
a ∈Sk
n,
and the polynomials (the characters of WN and W a
N)
wN(q) =
X
η∈WN
qw(η),
wa
N(q) =
X
η∈W a
N
qw(η).
Further, let us consider the column vector wN of characters wa
N in a certain order,
which is ﬁxed once and for all. In the paper [FrSz2] the recurrence relation for vectors wN
was obtained. Namely,
wN+1 = q−knNMk(qnN+n−1) . . .Mk(qnN+1)Mk(qnN)wN,
where Mk(x)a,b = xHn(a,b), for a, b ∈Sk
n. This important recurrence relation gives a way
to compute the polynomials wN(q).
Two particular cases when either k = 1 and n ≥2 is arbitrary or n = 2 and k ≥1 is
arbitrary seem to be the most accessible from combinatorial point of view. Namely, let us
consider at ﬁrst the level k = 1 case. Then we can imagine each ﬁnite path η ∈WN as a
word w = a1 . . . anN of length m = nN, composed from the numbers 1, 2, . . .n. Let µ be
the weight of w, i.e. µi = {j | aj ∈w, aj = i}. For given weight µ, l(µ) ≤n, let us denote
by M(µ) the set of all words of weight µ. It is well-known (see e.g. [An1]) that
Card M(µ) =
|µ|!
µ1! . . .µn! =

|µ|
µ1, . . ., µn

.
Deﬁnition 7 ([Fo]). A function ϕ on the set M(µ) is called to be mahonian statistics,
if
X
w∈M(µ)
qϕ(w) = qd(ϕ)

|µ|
µ1, . . ., µn

q
,
where a positive integer d(ϕ) depends only on weight µ.
The classical examples of mahonian statistics (with d(µ) = 0) are the number of inver-
sions (inv(w)) and major (or greater) index (Maj(w)) of a word w ∈M(µ), see e.g. [An1],
Section 3.4, or Exercise 1 to Section 2.4. The next result was proven in [DJKMO1] using
the recurrence relations technique.
Dilogarithm identities
75
Theorem H (Date-Jimbo-Kuniba-Miwa-Okado). The weight function w(η) on the set
restricted paths R1
n deﬁnes on the weight µ subsets M(µ) ⊂WN the mahonian statistics
with d(ϕ) = 0.In other words
X
η∈M(µ)
qw(η) =

|µ|
µ1, . . ., µn

q
.
Proof. First of all, we are going to replace a restricted path η ∈R1
n by some word.
More exactly, let η ∈R1
n ∩WN. The path η has the form η = (η1, η2, . . ., ηnN), where
each ηj ∈S1
n. But S1
n = {e1, e2, . . ., en}, where ei = (0, . . ., 0, 1, 0, . . ., 0). Thus one can
replace the path η by the word w just changing ej on j. Let us assume that the word w
has a weight µ. Our next task is to rewrite the weight function w(η) given on the set of
restricted paths, as a function on the set of words. The crucial observation is following: if
ei and ej belong to S1
n, then H(ei, ej) = χ(i ≥j), where for any statement P the symbol
χ(P) is equal to 1, if P is true and χ(P) = 0 otherwise. Using this observation, one can
ﬁnd
w(η) =
nN−1
X
m=1
mχ(am ≥am+1) −nN(N −1)
2
,
where w = a1a2 . . . anN is the word corresponding to the restricted path η ∈R1
n ∩WN.
To go further, let us introduce on the set of words w = a1 . . . anN the statistics g
Maj(w):
g
Maj(w) =
nN−1
X
m=1
mχ(am ≥am+1).
Note that the classical major index of the word is deﬁned as
Maj(w) =
nN−1
X
m=1
mχ(am > am+1).
It is the MacMahon Theorem (see e.g. [An1], Theorem 3.7) that
X
w∈M(µ)
qMaj(w) =

|µ|
µ1, . . ., µn

q
.
The proof given in [An1], Theorem 3.7, can be modiﬁed to show the statistics g
Maj is
also machonian with d(ϕ) = n(µ′).
It is an interesting task to ﬁnd a purely combinatorial proof of equidistribution for the
statistics Maj and g
Maj −n(µ′). We are going to consider this question in more details in
a separate publication.
76
Anatol N. Kirillov
Another interesting question is a connection between the weight function w(η) (or
g
Maj(w)) and the Robinson-Schensted correspondence. Namely, applying the Robinson-
Schensted correspondence to a given word w ∈M(µ), we obtain the pair (P, Q) of
(semi)standard Young tableaux of the same shape, say λ, such that
P ∈STY(λ, µ),
Q ∈STY(λ, (1nN)).
It is well-known (see e.g. [Sa]) that if w
RS
←→(P, Q), then Maj(w) = indQ, where the
index of a standard tableau T ∈STY(λ, 1|λ|) is deﬁned as ind(T) = P
j∈Des(T ) j and
Des(T) is the so-called descent set of tableau T (j ∈Des(T) iﬀ(j + 1) lies in tableau T
strictly below than j). This result allows to give a pure combinatorial proof of Theorem 9.
Indeed, it is also well-known result (see e.g. [Ma]) that
Kλ,(1|λ|)(q) =
T ∈STY(λ,1|λ|)
qind(T ).
A relation between g
Maj-statistics and RS-correspondence is more complicated and will be
considered elsewhere.
Exercises to Section 2.4.
1. Let µ be a composition, l(µ) = n. Consider the set
M(µ) =

w = a1a2 · · · a|µ| | ak ∈[1, n], #{i | ai = j} = µj
	
.
Let us deﬁne the number of inversions for a word w as
inv(w) =
X
1≤i<j≤|µ|
χ(ai > aj).
i) Prove
X
w∈M(µ)
qinv(w) =

|µ|
µ1, . . .µn

q
.
(P. MacMahon, 1914)
ii) Given w ∈M(µ), let wij be the subword of w formed by deleting all letters am such
that am̸ = i or j. For example, if w = 2411213144321 ∈M(5, 3, 2, 3) then w12 = 21121121,
w13 = 1113131, w14 = 41111441, w23 = 22332, w24 = 242442, w34 = 43443.
The Z-index (Zeilberger’s index) of w is deﬁned to be the sum of the major indices of
all 2-letter subwords, wij, of w. That is
Z(w) =
X
1≤i<j≤n
Maj(wij).
Dilogarithm identities
77
Analogously, let us introduce the eZ-index of w as follows
eZ(w) =
X
1≤i<j≤n
g
Maj(wij) −n(µ).
For our example, inv(w) = 29, Maj(w) = 47, g
Maj(w) −n(µ) = 59 −15 = 44,
Z(w) = 12 + 10 + 8 + 4 + 7 + 5 = 46, eZ(w) = 19 + 13 + 23 + 11 + 8 + 8 −15 = 67.
Prove
X
w∈M(µ)
qZ(w) =

|µ|
µ1, . . ., µn

q
.
(D. Zeilberger, D. Bressoud, 1985)
iii) Give a combinatorial proof of equidistribution for the statistics
inv,
Maj
and
Z.
Further details and proofs one can ﬁnd in [Bre3], [ZB], [Gre] and [Han].
2. (Tensor product multiplicities and Bethe’s ansatz equations).
Let µ(j) = (µ(j)
1
≥· · · ≥µ(j)
n
≥0), 1 ≤j ≤N, and λ be the highest weights and Vµ(j),
Vλ be the corresponding irreducible ﬁnite dimensional representations of the Lie algebra
gln.
Conjecture 5. The tensor product multiplicity
MultVλ(Vµ(1) ⊗· · · ⊗Vλ(N))
is equal to the number of solutions to the following system of algebraic equations on vari-
ables v1 = {v1,1, . . ., v1,m1}, v2 = {v2,1, . . ., v2,m2}, ... ,vn = {vn,1, . . . , vn,mn} (we assume
that v0 = vn+1 = φ)
N
Y
j=1
vk −λ(j)
k i
vk −λ(j)
k+1i
=
Y
vk−1
vk −vk−1 + i/2
vk −vk−1 −i/2
Y
v′
k̸=vk
vk −v′
k −i
vk −v′
k + i
Y
vk+1
vv −vk+1 + i/2
vk −vk+1 −i/2.
Here i = √−1. The number of equations and that of variables are the same and are equal
to m1+· · ·+mn. The relation between the weights λ and µ(1), . . ., µ(N) and the composition
m = (m1, m2, . . ., mn) is the following
2mk −mk−1 −mk+1 =
X
l≥k+1



N
X
j=1
µ(j)
l
−λl


.
3. Given two partitions λ and µ, |λ| = |µ|, and a natural number k. Let us consider
the new partitions
λN := (λ, (kN))+ and µN := (µ, (kN))+,
where for any composition ν we denote by ν+ the corresponding partition (for example, if
ν = (4419583162), then ν+ = (9865443211)).
Prove that there exists the limit
lim
N→∞KλN,µN (q) := Gλ,µ;k(q),
and this limit is a rational function.
78
Anatol N. Kirillov
• Problem. Find an algebraic/representation theoretic interpretation of the rational
functions Gλ,µ;k(q).
See [Stn2], [Kir3] and [Kir9] for proofs and further results about the rational functions
Gλ,µ;k(q).
4. Prove the following relations
i)
X
λ
dimV (n)
λ
· Kλ,µ(1) =
Y
j

n + µj −1
µj

,
ii)
X
λ

n
λ′

q
· Kλ,µ(1) =
Y
j

n + µj −1
µj

q
.
Here

n
λ

:=
Y
x=(i,j)∈λ
1 −qn+i−j
1 −qh(x)
is the generalized q-binomial coeﬃcient; V (n)
λ
is the
highest weight λ irreducible representation of gl(n) and Kλ,µ(1) is the Kostka number.
Hint: use the Littelwood formula
X
λ
sλ(x1, . . ., xn)sλ(y1, . . ., ym) =
n
Y
i=1
m
Y
j=1
1
1 −xiyj
.
5. (Construction of elements in C(F)). We use the notation from the Section 2.3.1.
Deﬁnition 8. Every equation of the following form
XA Y
r∈I
(1 −ζkr
m Xr)Ar = 1,
(1)
where A, kr, Ar are integers, ζm = exp
2πi
m

∈F, and I is a ﬁnite set of natural numbers,
is called a (generalized) cyclotomic equation.
Now, suppose that a ∈F ∗, a̸ = 1 satisﬁes the cyclotomic equation (1), and let a natural
number N satisfy
i) 2 | NA,
ii) r | NA, m | (NAr/r)kr, for r ∈I.Show that
b :=
X
r∈I
(NAr/r)[ζkr
m ar] ∈C(F).
Remark. Let b be the image of b in the Bloch group B(F). It is an interesting problem
to ﬁnd an eﬀective criteria when b ∈B(F)tor.
Dilogarithm identities
