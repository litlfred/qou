---
doc_id: arxiv-hep-th-9408113v2
doc_title: "Dilogarithm identities"
section_id: sec-067-2-nq
section_title: "Nq"
section_number: 2
pages: 71-76
source_pdf: 9408113v2.pdf
source_sha256: dadd96e1155e820f
doc_brief: "Dilogarithm identities — We study the dilogarithm identities from algebraic, analytic, asymptotic, K-theoretic, combinatorial and representation-theoretic points of view."
---
mAk−1mt
k2


N
µ1−m1
k ,µ2−mk−1
k , 1
k (mAk−1)a


q
.
Corollary 9 (of Theorem 14). Let λ = (λ1,λ 2) be a partition, |λ|≡ 0 (mod 2 k), and
bkΛ 0
λ (q) be the branching function for the level k vacuum representation kΛ 0 of the aﬃne
Lie algebra ˆsl2. Then
lim
N→∞
q−k(N 2−N)KλN ,µN (q) = bkΛ 0
λ (q),
whereλN := (λ1 +kN,λ 2 +kN ) and µN = (kM ), M :=M (N ) = 1
k|λ| + 2N .
Let us remind that, by deﬁnition, the partition ( kM ) is the one consisting of M parts
all equal to k.
Proof. Consider the following sum
Σ N :=
∑
λ ,l(λ)≤ 2
|λ| = 2kN
sλ(x1,x 2)
(x1x2)kN q−k(N 2−N)Kλ,(k2N )(q). (2.50)
It follows from Theorem 14 that
Σ N =
2kN∑
µ1=0
(x1/x2)µ1−kN ∑
m=(m1,...,mk−1)∈Zk−1
+
q
1
k n(µ′)−(k−1)N−k(N 2 −N)q
mAk−1 mt
k2
·


2N
µ1−m1
k ,µ2−mk−1
k , 1
k (mAk−1)a


q
.
72 Anatol N. Kirillov
Let us put µ1 =m1 + (l +N )k (thus,µ2 = (N−l)k−m1) and z =x1/x2. It is clear that
1
kn(µ′)− (k− 1)N−k(N 2−N ) = m2
1
k +kl2 + 2m1l.
Hence, we have
Σ N =
∑
m = (m1,...,m k−1)∈ Zk−1
+
∑
l∈ Z
l≥−N− m1
k
zkl+m1qkl2+2m1lq
km2
1 +mAk−1mt
k2
·


2N
l +N,N −l− m1 +mk−1
k , 1
k (mA)a


q
.
Consequently, lim
N→∞
Σ N =
1
(q)2
∞
∑
m=(m1,...,mk−1)∈Zk−1
+
∑
l∈Z
zkl+m1qkl2+2m1lq
km2
1 +mAk−1mt
k2
k−1∏
a=1
(q)−1
sa, (2.51)
where sa := 1
k (mAk−1)k−a.
Now let us rewrite the summation in the RHS(2.51) in terms of p arameters sa,
a = 1,...,k − 1. One can easily check that
k−1∑
a=1
asa =m1, km2
1 +mAk−1mt
k2 =sT −1
k−1st.
Consequently, lim
N→∞
Σ N =
1
(q)2
∞
∞∑
m1=0
∑
s = (s1,...,s k−1)∈ Zk−1
+∑
aasa =m1
∑
l∈Z
zkl+m1qkl2+2m1lqsT −1
k−1st
∏
a
(q)sa
= 1
(q)2
∞
∞∑
m1=0
Θ k
m1 (z)ck
m1(q) = ch(V (kΛ 0)).
On the other hand,
lim
N→∞
∑
λ,l (λ)≤ 2
|λ| = 2kN
sλ(x1,x 2)
(x1x2)kN q−k(N 2−N)KλN ,µN (q) =
∑
λ = (λ1≥λ2)
|λ| = 0
sλ(x)bλ(q),
where bλ(q) = lim
N→∞
q−k(N 2−N)KλN ,(k2N )(q).
Dilogarithm identities 73
Consequently,bλ(q) is the branching function of level k vacuum-ˆsl2 representationkΛ 0.
We assume that any branching function bΛ
λ (q) of integrable highest weight representa-
tion V (Λ) of the aﬃne Lie algebra ˆsln can be constructed as an appropriate limit of the
Kostka-Foulkes polynomials. More exactly:
Conjecture 4. Let Λ = kΛ 0 be the level k vacuum representation of the aﬃne Lie
algebra ˆsln. Then
bΛ
λ (q) = lim
N→∞
K λN ,(kN n)(q),
whereλN :=λ + ((kN )n), λ = (λ1≥λ2≥···≥ λn) and|λ| = 0.
Remark. There exists an interesting connection between the Milne po lynomials ([Ml1],
[Ml2], [Ga])
Mµ(x;q) :=
∑
λ
sλ(x)Kλ,µ(q) = Qµ
( x
1−q
)
,
where x = (x1,...,x n), and the characters ch V (Λ) of integrable highest weight represen-
tations V (Λ) of the aﬃne Lie algebra ˆsln. Roughly speaking, the character ch V (Λ) is
an appropriate limit of Milne’s polynomials (see the proofs of Theorems 11,13 and 14).
It would be interesting to know the solutions to what kind of h ierarchy (= a system of
nonlinear partial diﬀerential equations) the characters o f integrable highest weight repre-
sentations of ˆsln are.
2.4.4. Crystal basis and Robinson-Schensted correspondence.
In this section we are going to discuss brieﬂy a connection be tween a combinatorial
description of the so-called crystal basis [Ka] of an integr able ˆsln-module V k
n of level k,
found by Jimbo, Misra, Miwa and Okado in [JMMO] (see also [MM] , [KKNMMNN] and
[DJKMO1], [DJKMO2]) and the Kostka-Foulkes polynomials vi a the Robinson-Schemsted-
Knuth (RSK) correspondence (see e.g. [Sa], where a construc tion and basic properties of
RSK are given).
The starting point for us is the following variant of the Jimb o-Misra-Miwa-Okado for-
mula for the character ch(V k
n ) in the paths realization of the crystal basis, due to E. Fren kel
and A. Szenes [FrSz2]. Thus (see [FrSz2], Section 6), let us i ntroduce the set
Sk
n ={a = (a1,...,a n)|ai≥ 0, a1 +··· +an =k}.
Denote by τ : (a1,a 2,...,a n)→ (an,a 1,...,a n−1) the cyclic permutation acting on Sk
n
and deﬁne the element ak∈ Sk
n by ak = (k, 0,..., 0). Now the ground state path µ is
the sequence ( ak,τ ak,τ 2ak,... ), and the set of restricted paths Rk
n is the set of sequences
η = (η0,η 1,... ) of elements ηj∈Sk
n, which coincide with µ except for a ﬁnite set of indices.
Deﬁne the weight function w onRk
n by the formula
w(η) =
∞∑
m=1
m [H(ηm−1,η m)−H(µm−1,µ m)],
74 Anatol N. Kirillov
where Hn(a, b) := max
1≤i≤n
(hi(a, b)) and
hi(a, b) =
i∑
j=1
aj−
i−1∑
j=1
bj.
Theorem G ([JMMO]). As formal power series in q
chV k
n =
∑
η∈Rk
n
qw(η).
Now let us introduce the sets
WN ={η∈R k
n| ηj =µj for j≥nN},
W a
N ={η∈R k
n| ηnN−1 = a, ηj =µj for j≥nN}, a∈Sk
n,
and the polynomials (the characters of WN and W a
N )
wN (q) =
∑
η∈WN
qw(η), w a
N (q) =
∑
η∈W a
N
qw(η).
Further, let us consider the column vector wN of characters wa
N in a certain order,
which is ﬁxed once and for all. In the paper [FrSz2] the recurr ence relation for vectors wN
was obtained. Namely,
wN+1 =q−knNMk(qnN+n−1)...M k(qnN+1)Mk(qnN )wN,
whereMk(x)a,b =xHn(a,b), for a, b∈Sk
n. This important recurrence relation gives a way
to compute the polynomials wN (q).
Two particular cases when either k = 1 and n≥ 2 is arbitrary or n = 2 and k≥ 1 is
arbitrary seem to be the most accessible from combinatorial point of view. Namely, let us
consider at ﬁrst the level k = 1 case. Then we can imagine each ﬁnite path η∈WN as a
word w =a1...a nN of length m =nN , composed from the numbers 1 , 2,...n . Let µ be
the weight of w, i.e. µi ={j|aj∈w, aj =i}. For given weight µ,l (µ)≤n, let us denote
byM (µ) the set of all words of weight µ. It is well-known (see e.g. [An1]) that
Card M (µ) = |µ|!
µ1!...µ n! =
(
|µ|
µ1,...,µ n
)
.
Deﬁnition 7 ([Fo]). A function ϕ on the set M (µ) is called to be mahonian statistics,
if
∑
w∈M (µ)
qϕ(w) =qd(ϕ)
[
|µ|
µ1,...,µ n
]
q
,
where a positive integer d(ϕ) depends only on weight µ.
The classical examples of mahonian statistics (with d(µ) = 0) are the number of inver-
sions (inv(w)) and major (or greater) index (Maj( w)) of a word w∈M (µ), see e.g. [An1],
Section 3.4, or Exercise 1 to Section 2.4. The next result was proven in [DJKMO1] using
the recurrence relations technique.
Dilogarithm identities 75
Theorem H (Date-Jimbo-Kuniba-Miwa-Okado). The weight function w(η) on the set
restricted pathsR1
n deﬁnes on the weight µ subsets M (µ)⊂ WN the mahonian statistics
with d(ϕ) = 0 .In other words
∑
η∈M (µ)
qw(η) =
[
|µ|
µ1,...,µ n
]
q
.
Proof. First of all, we are going to replace a restricted path η∈R 1
n by some word.
More exactly, let η∈R 1
n∩WN . The path η has the form η = (η1,η 2,...,η nN ), where
each ηj∈ S1
n. But S1
n ={e1,e 2,...,e n}, where ei = (0,..., 0, 1, 0,..., 0). Thus one can
replace the path η by the word w just changing ej on j. Let us assume that the word w
has a weight µ. Our next task is to rewrite the weight function w(η) given on the set of
restricted paths, as a function on the set of words. The cruci al observation is following: if
ei and ej belong to S1
n, then H(ei,e j) = χ(i≥j), where for any statement P the symbol
χ(P ) is equal to 1, if P is true and χ(P ) = 0 otherwise. Using this observation, one can
ﬁnd
w(η) =
nN−1∑
m=1
mχ(am≥am+1)− nN (N− 1)
2 ,
where w = a1a2...a nN is the word corresponding to the restricted path η∈R 1
n∩WN .
To go further, let us introduce on the set of words w =a1...a nN the statistics ~Maj(w):
~Maj(w) =
nN−1∑
m=1
mχ(am≥am+1).
Note that the classical major index of the word is deﬁned as
Maj(w) =
nN−1∑
m=1
mχ(am >a m+1).
It is the MacMahon Theorem (see e.g. [An1], Theorem 3.7) that
∑
w∈M (µ)
qMaj(w) =
[
|µ|
µ1,...,µ n
]
q
.
The proof given in [An1], Theorem 3.7, can be modiﬁed to show t he statistics ~Maj is
also machonian with d(ϕ) = n(µ′).
It is an interesting task to ﬁnd a purely combinatorial proof of equidistribution for the
statistics Maj and ~Maj−n(µ′). We are going to consider this question in more details in
a separate publication.
76 Anatol N. Kirillov
Another interesting question is a connection between the we ight function w(η) (or
~Maj(w)) and the Robinson-Schensted correspondence. Namely, app lying the Robinson-
Schensted correspondence to a given word w ∈ M (µ), we obtain the pair ( P,Q ) of
(semi)standard Young tableaux of the same shape, say λ, such that
P∈ STY(λ,µ ), Q∈ STY(λ, (1nN )).
It is well-known (see e.g. [Sa]) that if w
RS
←→(P,Q ), then Maj( w) = ind Q, where the
index of a standard tableau T ∈ STY(λ, 1|λ|) is deﬁned as ind( T ) = ∑
j∈Des(T )j and
Des(T ) is the so-called descent set of tableau T (j∈ Des(T ) iﬀ ( j + 1) lies in tableau T
strictly below than j). This result allows to give a pure combinatorial proof of Th eorem 9.
Indeed, it is also well-known result (see e.g. [Ma]) that
Kλ,(1|λ |)(q) =
∑
T ∈STY(λ,1|λ |)
qind(T ).
A relation between ~Maj-statistics and RS-correspondence is more complicated and will be
considered elsewhere.
Exercises to Section 2.4.
