---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Steklov Mathematical Institute"
section_id: sec-060-3-f-the-indecomposable-part-of
section_title: "(F ) (the indecomposable part of"
section_number: 3
pages: 60-63
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "DILOGARITHM IDENTITIES ANATOL N. KIRILLOV — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
K3(F ), i.e. the cokernel of the product map K1(F )⊗3→K3(F )) using the relative group
K2 of projective line over F modulo two points and the solutions of the Bether-ansatz-li ke
system of algebraic equations is given.
2.4. Connection with crystal basis.
2.4.1. Level 1 vacuum representation Λ 0 of the aﬃne Lie algebra ˆsln.
Theorem 11. Letµ = (µ1,...,µ n) be a composition. Then
∑
λ, l (λ)≤n
Kλ,µ·Kλ, (1|λ |)(q) = qn(µ′)
[
|µ|
µ1,...,µ n
]
q
, (2.28)
where
[
N
m1,...,m n
]
q
:= (q)N
(q)m1... (q)mn
is the q-analog of multinomial coeﬃcient (N =m1 +··· +mn).
Let us explain notation. Here
i) Kλ,µ is the so-called Kostka number, which is equal to the number o f (semi)standard
Young tableaux of shape λ and weight µ, or, equivalently, to the dimension of weight µ
subspace Vλ(µ) of the irreducible highest weight λ representation Vλ of the Lie algebra
gln:
Kλ,µ = dim Vλ(µ).
Dilogarithm identities 61
ii) Kλ,µ(q) is the so-called Kostka-Foulkes polynomial (see e.g. [Ma] ), which can be
deﬁned from a decomposition of the Schur functions in terms o f the Hall-Littlewood ones:
sλ(x) =
∑
µ
Kλ,µ(q)Pµ(x;q).
It is well-known (see e.g. [Lu2] or [Ma]), that polynomial K λ,µ(q) := qn(µ)−n(λ)Kλ,µ(q−1)
coincides with Lusztig’s q-analog of weight multiplicity dim Vλ(µ).
iii) n(λ) :=
n∑
i=1
(i− 1)λi =
n∑
i=1
(
λ′
j
2
)
=
∑
1≤i<j≤n
min(λi,λ j), if λ = (λ1,...,λ n)∈ Zn
+.
The proof of Theorem 11 is based on the well-known results from the theory of sym-
metric functions. We will use the notation and terminology i nvolving symmetric functions
from Macdonald [Ma].
Lemma 6. ∑
λ
sλ(x)Kλ,µ(q) = Qµ
( x
1−q
)
.
Here we used the standard λ-ring theory notation, namely, for any symmetric function
f (x) := f (x1,x 2,... ) and a new set of variables y = (y1,y 2,... ) one can deﬁne f (xy) =
f (...,x iyj... ).
Proof. Let us remind that the Hall-Littlewood functions Pλ andQλ satisfy the following
orthogonality condition (see [Ma], Chapter II, (4.4))
∑
λ
Qλ(x;q)Pλ(y;q) =
∏
i,j
1−qxiyj
1−xiyj
.
Consequently,
∑
λ
Qλ
( x
1−q
)
Pλ(y,q ) =
∏
i,j
k≥ 0
1−qk+1xiyj
1−qkxiyj
=
∏
i,j
(1−xiyj)−1 =
∑
λ
sλ(x)sλ(y).
Here we used the orthogonality of Schur’s functions ([Ma], C hapter I, (4.3)). It remains to
remind the deﬁnition of Kostka-Foulkes polynomials:
sλ(y) =
∑
µ
Kλ,µ(q)Pµ(y;q).
To continue, let us remark that if m≥n, then
Q(kn)(x1,...,x m;q) = (q;q)n(en(x))k, see [Ma] , Chapter III, (2.8).
62 Anatol N. Kirillov
Therefore, in order to prove Theorem 9 we have to decompose th e symmetric function
∑
λ
sλ(x)Kλ,(1n)(q) = Q(1n)
( x
1−q
)
= (q;q)nen
( x
1−q
)
in terms of the monomial symmetric ones mλ(x). For this purpose, let us remind that by
deﬁnition ( CT := constant term)
en
( x
1−q
)
=CT

t−n∏
j
(−txj;q)∞

.
Thus, using the Euler result
(−z;q)∞ =
∞∑
n=0
znq
n(n−1)
2
(q;q)n
,
one can obtain
en
( x
1−q
)
=
∑
µ⊢n
qn(µ′)
(q;q)µ
mµ(x),
where for a partition µ = (µ1,µ 2,...,µ n), we set ( q;q)µ :=
n∏
j=1
(q;q)µj . Consequently,
∑
λ
sλ(x)Kλ,(1n)(q) =
∑
µ⊢n
qn(µ′)
[
n
µ1...µ n
]
q
mµ(x).
Remark. The identity (2.28) is implicitly contained in the Terada pr eprint [Te]. The
proof given in [Te] is based on a study of the cohomology group s of the variety of N -stable
ﬂags. Our proof is pure algebraic and based on the theory of sy mmetric functions. Later
B. Leclerc and J.-Y. Thibon gave almost the same proof (unpub lished). It is possible to
give a pure combinatorial proof of (2.28) using the properti es of the Robinson-Schensted
correspondence. Finally, the identity (2.28) can be extrac ted from [DJKMO1].
Corollary 6 (of Theorem 11).
∑
λ, l (λ)≤n
sλ(x)Kλ,(1|λ |)(q) =
∑
m∈Zn
+
q
Σ
(
mi
2
)
xm
[
|m|
m1,...,m n
]
q
. (2.29)
Dilogarithm identities 63
Now we are going to consider an appropriate limit |m|→∞ in (2.29). More exactly,
let us assume that |m| =nN , and consider the following variant of (2.29):
q− (N 2 −N )n
2
∑
λ,l(λ)≤n
sλ(x1,...,x n)
(x1...x n)N Kλ,(1|λ |)(q)
=
∑
k∈ Zn,
|k| = 0,k i≥−N, ∀i
xk1
1 ...x kn
n q
1
2
∑
k2
i
[
nN
k1 +N,...,k n +N
]
q
. (2.30)N
First of all, lim
N→∞
RHS(2.30)N =
1
(q)n−1∞
∑
m∈ Zn
|m| = 0
xmq
1
2
∑
m2
i = 1
(q)n−1∞
∑
k∈Zn−1
zk1
1 ...z kn−1
n−1 q
1
2 kAn−1kt
,
where zi = xi
xi−1
, 1≤i≤n− 1, x0 :=xn. On the other hand,
lim
N→∞
LHS(2.30)N =
∑
λ = (λ1≥λ2≥···≥ λn)∈ Zn
|λ| = 0
sλ(x1,...,x n)bλ(q),
where for given weight λ we set (λN :=λ + (N n))
bλ(q) := lim
N→∞
q− n(N 2 −N )
