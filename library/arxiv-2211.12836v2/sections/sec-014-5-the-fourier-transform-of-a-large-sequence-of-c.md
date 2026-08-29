---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION"
section_id: sec-014-5-the-fourier-transform-of-a-large-sequence-of-c
section_title: "The Fourier transform of a large sequence of convolution"
section_number: 5
pages: 32-46
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION — We study a class of commuting Markov kernels whose simplest element describes the movement ofk particles on a discrete"
---
The goal of this section is to estimate the discrete Fourier transform of the convolution of a
sequence (µi)1≤i≤m of h-probability measures in Bk,n when m is large compared to n. Mimicking
the previous deﬁnition for elements of Bk,n, for x∈ Rk we set⟨x⟩ =∑k
j=1xj and then deﬁne
~x =x−⟨x⟩
k 1k =
(
x1−⟨x⟩
k ,...,x k−⟨x⟩
k
)
.
We then introduce for x∈ Rk the shifted norm
K(x) =‖x‖2−‖ ˜I0‖2,
where‖·‖ denotes the usual Euclidean norm on Rk. We will regularly use for x∈ Rk the identity
(26) K (˜x) =K(x)−⟨x⟩2
k ,
whose proof is left to the reader. Remark that we have in particular K( ˜I0) = 0 and that I∈Bk,n
satisﬁes K(˜I) = 0 if and only if I = I0 +𝓁1k for some 0 ≤ 𝓁≤ n−k. Finally, we introduce for
I∈Bk,n the shifted conﬁguration
ˆI =I−Ik1k = (I1−Ik,...,I k−1−Ik, 0),
so that ˆI∈ Bk,n. We introduced in Section 2 for µ∈M 1(Bk,n), the random variable Iµ∈ Bk,n
whose distribution is
P(Iµ =I) =µ(I)µh(I) =|V (ξn(I))|2
nk µ(I).
We then set
(27)
‖µ‖r = E
[
‖˜Iµ‖r
]
, ⟨µ⟩ = E [⟨Iµ⟩],⟨ˆµ−I0⟩r = E
[
⟨ˆIµ−I0⟩r
]
and Varr(µ) = E
[⏐⏐⏐⟨Iµ⟩−⟨ µ⟩
⏐⏐⏐
r]
for r≥ 2. We simply write Var (µ) for Var 2(µ) in the sequel, and we ﬁnally set
K(µ) :=‖µ‖2−‖ ˜I0‖2 = E
[
K(˜Iµ)
]
.
The ﬁrst main estimate of the Fourier transform is the following lemma, which shows pointwise
asymptotics of the Fourier transform as n goes to inﬁnity. For sake of completeness, we give
asymptotic results which hold uniformly in k. In the following statement, recall that for I∈ Bk
withI1<I k+n, we setλI =I−I0 andI(n) is the unique element ofBk,n such that{I(n)
i [n]}1≤i≤k =
{Ii[n]}1≤i≤k.
Lemma 5.1. Letn,k≥ 2. For any h-probability measureµ∈Bk,n and I∈Bk with n≥‖I‖∞,
e−2iπ (⟨µ⟩−⟨I0⟩)·⟨λI⟩
kn Φn[µ](I(n)) = 1− (2π)2
2n2
[
K(µ)K(˜I)
k2− 1 + Var (µ)⟨λI⟩2)
k2
]
+ 1
n3O
(Var 3(µ)·|⟨λI⟩|3
k3 +⟨ˆµ−I0⟩3·‖ ˜I‖3
∞
)
,
and
⏐⏐⏐Φn[µ](I(n))
⏐⏐⏐≤ 1− (2π)2
2n2
K(µ)K(˜I)
k2− 1 + 1
n3O
(
⟨ˆµ−I0⟩3·‖ ˜I‖3
∞
)
,
whereO(·) only depends on numeric constants.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 33
The main ingredient in the proof of the latter lemma is an asymptotic formula for ratios of Schur
functions. Recall that Λ k denotes the set of partitions with at most k parts and for ⃗ u∈ Rk we
abbreviate exp(i⃗ u) for the vector (exp(iu1),..., exp(iuk)).
Lemma 5.2. Let k≥ 2. For any λ∈ Λk with λk = 0 and ⃗ u∈ Rk such that ∑k
i=1ui = 0 and
⟨λ⟩ max(‖⃗ u‖∞,k/ 3)≤n,
sλ
(
exp
(
2πi⃗ u/n
))
sλ
(
exp
(
2πi~I0/n
)) = 1− (2π)2
2(k2− 1)n2
[
K(~Iλ)K(⃗ u)
]
+O
((⟨λ⟩· (‖⃗ u‖∞ +k)
n
)3)
,
with O(·) only depending on numeric constants.
The proof of this lemma uses shifted Schur functions, as introduced in [45]. Shifted Schur
functions form a particular basis{s∗
λ}λ∈R of the ring of polynomials functions in {xi}i≥1 which are
symmetric in the variables{xi−i}i≥1. Their main useful property for us is the following generalized
binomial formula for all k≥ 1 and µ∈ Λk, see [45, Sec. 5],
(28) sµ(1 +x1,..., 1 +xk)
sµ(1,..., 1) =
∑
ν⊂µ
1
(k ↿ν)s∗
ν(µ1,...,µ k)sν(x1,...,x k),
wheresν,ν ∈ Λk are the usual Schur functions and (k ↿ν) =∏k
i=1
(νi+k−i)!
(k−i)! =∏l(ν)
i=1
∏νi
j=1(k−i+j).
We will be mostly interested in the ﬁrst shifted Schur functions, namely for |ν|≤ 2. We then have
s∗
(1)(x1,x 2,... ) =
∑
i≥1
xi, s∗
(2)(x1,x 2,... ) =
∑
i≤j
xj(xi− 1), s∗
(11)(x1,x 2,... ) =
∑
i<j
xj(xi + 1).
Proof of Lemma 5.2. We only prove this lemma for λ∈ Λk such that ⟨λ⟩≥ 3, the case ⟨λ⟩≤ 2
being done similarly. Let k≥ 1 and λ∈ Λk with⟨λ⟩≥ 3. By (28), for ( x1,...,x k)∈ Ck we have
sλ(1 +x1,..., 1 +xk)
sλ(1,..., 1) =
∑
ν⊂λ
1
(k ↿ν)s∗
ν(λ)sν(⃗ x)
=1 + 1
(k ↿ (1))s∗
(1)(λ)s(1)(⃗ x) + 1
(k ↿ (2))s∗
(2)(λ)s(2)(⃗ x)
+ 1
(k ↿ (11))s∗
(11)(λ)s(11)(⃗ x) +Cλ(⃗ x),(29)
with Cλ(⃗x) =∑
ν⊂λ
⟨ν⟩≥3
1
(k↿ν)s∗
ν(λ)sν(⃗ x). Remark ﬁrst that for ⃗ x∈ Ck,|sν(⃗ x)|≤‖ ⃗ x‖⟨ν⟩
∞sν(1..., 1), so
that, using that (k ↿ν) =sν(1k)H(ν) with 1k the constant vector of length k equal to 1 and H(µ)
the Hook length of µ, see [45, Eq. 5.5],
|Cλ(⃗x)|≤
∑
ν⊂λ
⟨ν⟩≥3
1
(k ↿ν)s∗
ν(λ)sν(⃗ x)≤
∑
ν⊂λ
⟨ν⟩≥3
sν(1..., 1)
(k ↿ν) s∗
ν(λ)‖⃗ x‖⟨ν⟩
∞
≤
∑
ν⊂λ
⟨ν⟩≥3
s∗
ν(λ)
H(ν)‖⃗ x‖⟨ν⟩
∞.
Using that (|λ|−⟨ν⟩)!
⟨λ⟩! s∗
ν(λ) = dimV (λ\ν)
dimV (λ) , where V (λ) denotes the Specht irreducible representation
of the symmetric group S⟨λ⟩ associated to λ (see [45, Eq. 0.14]), and the classical Hook length
34 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
formula dimV (λ) = ⟨λ⟩!
H(λ), we get
|Cλ(⃗x)|≤
∑
ν⊂λ
⟨ν⟩≥3
H(ν)−1 ⟨λ⟩! dimV (λ\ν)
(⟨λ⟩−⟨ ν⟩)! dimV (λ)‖⃗ x‖⟨ν⟩
∞
≤
∑
ν⊂λ
⟨ν⟩≥3
(⟨λ⟩
⟨ν⟩
)dimV (ν) dimV (λ\ν)
dimV (λ) ‖⃗ x‖⟨ν⟩
∞
≤
⟨λ⟩∑
l=3
(⟨λ⟩
l
)
‖⃗ x‖l
∞


∑
ν⊂λ
⟨ν⟩=l
dimV (ν) dimV (λ\ν)
dimV (λ)

.
Remark that dim V (λ) = ∑
ν⊂λ
⟨ν⟩=l
dimV (ν) dimV (λ\ν) for all 1 ≤ l ≤ ⟨λ⟩ by restricting the
representationV (λ) of S⟨λ⟩ to Sl×S⟨λ⟩−l, so that ∑
ν⊂λ
⟨ν⟩=l
dimV (ν) dimV (λ\ν)
dimV (λ) = 1 and ﬁnally
|Cλ(⃗x)|≤
⟨λ⟩∑
l=3
(⟨λ⟩
l
)
‖⃗ x‖l
∞
≤‖⃗ x‖3
∞
⟨λ⟩!
3!(⟨λ⟩− 3)!(1 +‖⃗ x‖∞)⟨λ⟩−3≤⟨λ⟩3
6 ‖⃗ x‖3
∞(1 +‖⃗ x‖∞)⟨λ⟩−3
as long as ‖x‖∞ < 1, with C only depending on λ. Remark that for ‖x‖∞≤ 1/⟨λ⟩, the latter
bound simpliﬁes as
(30) |Cλ(⃗x)|≤ e·⟨λ⟩3
6 ‖⃗ x‖3
∞.
Let us then focus on the ﬁrst terms of the right-hand side of (29). First, we have 1
(k↿(1)) = 1
k and
s∗
(1) =s1, so that
1
(k ↿ (1))s∗
(1)(λ)s(1)(⃗ x) = 1
ks(1)(λ)s(1)(⃗ x).
Set xi = exp(iui/n)− 1, for 1≤i≤k. We then have |xi|≤ (1∧|ui|/n) and there is a numerical
constantC′> 0 such that
⏐⏐⏐xi−iui/n + u2
i
2n2
⏐⏐⏐≤ C′|ui|3
n3 . Using that ∑k
i=1ui = 0, this yields
⏐⏐⏐⏐⏐s(1)(⃗ x) + 1
2n2
k∑
i=1
u2
i
⏐⏐⏐⏐⏐≤ kC′‖⃗ u‖3
∞
n3 .
Hence, introducing the second power sum p2(⃗ u) =∑k
i=1u2
i ,
(31) 1
(k ↿ (1))s∗
(1)(λ)s(1)(⃗ x) =−s(1)(λ)p2(⃗ u)
2kn2 +K,
with|K|≤ C⟨λ⟩‖⃗ u‖3
∞
n3 with C numeric.
Next, 1
(k↿(11)) = 1
k(k−1) and 1
(k↿(2)) = 1
k(k+1). Introducing the shifted power sum p∗
2 =∑k
i=1(xi−
i)2− (−i)2 =∑k
i=1xi(xi− 2i), we then have the shifted Newton identities
s∗
2 = 1
2(s2
1 +p∗
2), s∗
11 = 1
2(s2
(1)−p∗
2)−s(1).
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 35
Hence, using additionally the usual Newton identities yields
1
(k ↿ (2))s∗
(2)(λ)s(2)(⃗ x) + 1
(k ↿ (11))s∗
(11)(λ)s(11)(⃗ x)
= 1
4k(k + 1)
[
s2
(1)(λ) +p∗
2(λ)
]
·
[
s2
(1)(⃗ x) +p2(⃗ x)
]
+ 1
4k(k− 1)
[
s2
(1)(λ)−p∗
2(λ)− 2s(1)(λ))
]
·
[
s2
(1)(⃗ x)−p2(⃗ x)
]
= 1
2k(k2− 1)
[
s2
(1)(λ)
(
ks2
(1)(⃗ x)−p2(⃗ x)
)
+p∗
2(λ)
(
kp2(⃗ x)−s2
(1)(⃗ x)
)
− (k + 1)s(1)(λ)
(
s2
(1)(⃗ x)−p2(⃗ x)
)]
.
There exists a numeric constant C >0 such that
|xi−iui/n|≤ C|ui|2
n2 .
Hence, since s(1)(⃗ u) = 0, we have
⏐⏐s(1)(⃗ x)
⏐⏐≤ Ck‖⃗ u‖2
∞
n2 , which yields
⏐⏐s(1)(⃗ x)2⏐⏐≤2Ck2‖⃗ u‖3
∞
n3
for some numeric constant C >0 when‖⃗ u‖∞≤n. Likewise,
⏐⏐x2
i +u2
i/n2⏐⏐≤ 2C|ui|3
n3 for 1≤i≤k,
so that
⏐⏐p2(⃗ x) +p2(⃗ u)/n2)
⏐⏐≤ 2Ck‖⃗ u‖3
∞
n3 .
Therefore,
1
(k ↿ (2))s∗
(2)(λ)s(2)(⃗ x)+ 1
(k ↿ (11))s∗
(11)(λ)s(11)(⃗ x)
= 1
2k(k2− 1)n2
[
s2
(1)(λ)p2(⃗ u)−kp∗
2(λ)p2(⃗ u)− (k + 1)s(1)(λ)p2(⃗ u)
]
+K′,(32)
with
K′≤C ‖⃗ u‖3
∞
n3k(k2− 1)
[
s2
(1)(λ)(k3 +k) +k2|p∗
2(λ)| +s(1)(λ)(k3 +k2)
]
≤C′‖⃗ u‖3
∞s2
(1)(λ)
n3 ,
for some numeric C,C′ > 0, where we used on the last inequality that |p∗
2(λ)|/k≤ s(1)(λ)2 for
λ∈ Λk. Remark that
p∗
2(λ) + (k + 1)s(1)(λ) =
k∑
i=1
λi(λi +k− 2i + 1) =
k∑
i=1
(
λi + k− 2i + 1
2
)2
−
(k− 2i + 1
2
)2
=‖λ + ˜I0‖2−‖ ˜I0‖2 =K(λ + ˜I0),
36 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
where K is deﬁned at the beginning of this section and we recall that ˜I0 = I0− ⟨I0⟩
k 1k =(k+1−2i
2
)
1≤i≤k. Hence, putting (30), (31) and (32) together yields then, for ‖⃗ u‖∞/n≤ 1
⟨λ⟩,
sλ(exp(iu1/n),..., exp(iuk/n))
sλ(1,..., 1) = 1− 1
2k(k2− 1)n2
[
−s2
(1)(λ)p2(⃗ u) +kp2(⃗ u)K(λ + ˜I0)
]
+O
((⟨λ⟩·‖ ⃗ u‖∞
n
)3)
,
= 1− 1
2(k2− 1)n2
[
p2(⃗ u)
(
K(λ + ˜I0)−
s2
(1)(λ)
k
)]
+O
((⟨λ⟩·‖ ⃗ u‖∞
n
)3)
,(33)
where the last term of the right-hand side of the ﬁrst equality takes into account the correction
coming from (31). Since s(1)(λ) =⟨λ⟩ =|Iλ|−⟨ I0⟩ and λ + ˜I0 =Iλ +⟨I0⟩
k 1k, we have by (26)
K(λ + ˜I0)−
s2
(1)(λ)
k =K( ~λ +I0) +|λ + ˜I0|
k −⟨λ⟩2
k =K(~λI).
Hence,
(34) sλ(exp(iu1/n),..., exp(iuk/n))
sλ(1,..., 1) = 1− K(~Iλ)‖⃗ u‖2
2(k2− 1)n2 +O
((⟨λ⟩·‖ ⃗ u‖∞
n
)3)
,
where we used that p2(⃗ u) =‖⃗ u‖2. In the special case where ⃗ u= 2π~I0 = 2π((k− 1)/2,..., −(k−
1)/2), which satisﬁes ∑k
i=1ui = 0, we have⟨I0⟩∞≤ 2πk, so that
(35) sλ(exp(2iπ~I0/n))
sλ(1,..., 1) = 1− (2π)2K(~Iλ)‖~I0‖2
2(k2− 1)n2 +O
((⟨λ⟩· k
n
)3)
.
Then, taking the ratio of (34) with (35) yields, as long as⟨λ⟩ max(‖⃗ u‖∞,k/ 3)≤n (remark that the
constant 1/3 is arbitrary and chosen for later simpliﬁcation), which impliesK(~Iλ) max(‖⃗ u‖2
∞,k 2)≤
kn2,
sλ(exp(2iπ⃗ u/n))
sλ(exp(2iπ~I0/n))
= 1− (2π)2
2(k2− 1)n2
[
K(~Iλ)K(⃗ u)
]
+O
((⟨λ⟩· (‖⃗ u‖∞ +k)
n
)3)
.
□
Proof of Lemma 5.1. Let us ﬁx I∈Bk and ﬁrst assume that µ =δJ, n≥⟨J⟩∞. Then, for such n,
by (19) and the fact that ξn(I) =ξn(I(n)), we have
Φn[µ](I(n)) = SJ(ξn(I(n)))
SJ(ξn(I0)) = SJ(ξn(I))
SJ(ξn(I0)).
By deﬁnition of the map ξn in (1) and the deﬁnition of SJ following (10),
SJ(ξn(I)) =sλJ
(
exp
(
2iπ
(
I− k− 1
2 1k
)))
=sλJ
(
exp
(
2iπ
(
I−⟨I0⟩
k 1k
)))
,
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 37
where we used that ⟨I0⟩ = ∑k
j=1(k−j) = k(k−1)
2 . Moreover, recall that ˜I = I−⟨I⟩/k1k and
ˆJ =J−Jk1k and remark that from the deﬁnition of SJ we have for ⃗ u∈ Rk such that ⃗ u= 0,
SJ(⃗ u) =S ˆJ+Jk1k
(⃗ u) =eiJk
∑k
l=1ulS ˆJ(⃗ u) =S ˆJ(⃗ u).
Hence, using that SJ(⃗ u+l1k) = exp(il⟨λJ⟩)SJ(⃗ u) for l∈ R, we get
SJ(ξn(I))
SJ(ξn(I0)) = exp(2iπ(⟨I⟩−⟨ I0⟩)·⟨λJ⟩/(kn))
SJ
(
ξn(I)− 2π
n
⟨I⟩−⟨I0⟩
k 1k
)
SJ
(
2iπ ˜I0/n
)
= exp(2iπ⟨λI⟩·⟨ λJ⟩/(kn))· S ˆJ(2π ˜I/n)
S ˆJ(2π ˜I0/n))
(36)
where we also used the fact that ∑k
i=1ξn(I)i = 2π(⟨I⟩−⟨I0⟩
n . Then, since ˆJk = 0, λ ˆJ = ˆJ−I0∈ Λk
satisﬁes
(
λ ˆJ
)
k = 0. Moreover, remark that ‖˜I‖∞≥ (k− 1)/2, so that ⟨λ ˆJ⟩ max(‖˜I‖∞,k/ 3)≤ n
when⟨λ ˆJ⟩·‖ ˜I‖∞ =⟨ ˆJ−I0⟩·‖ ˜I‖∞≤n. In particular, as long as ⟨ ˆJ−I0⟩·‖ ˜I‖∞≤n, we have by
Lemma 5.2
(37)
S ˆJ(2π ˜I/n)
S ˆJ(2π ˜I0/n)
=
sλ ˆJ
(
exp
(
2iπ ˜I/n
))
sλ ˆJ
(
exp
(
2iπ ˜I0/n
)) = 1− (2π)2
2(k2− 1)n2
[
K(˜I)K( ˜J)
]
+O


(
⟨ ˆJ−I0⟩·‖ ˜I‖∞
n
)3

where we used that‖˜I‖∞≥ (k− 1)/2 to simplify the bound O(·) and that ~ˆJ = ~J.
Consider nowµ∈M 1(Bk,n). Using the previous relation forJ =Iµ on the event⟨ˆIµ−I0⟩< n
‖˜I‖∞
,
we get
E
[SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
]
= 1− (2π)2
2(k2− 1)n2 E
(
1⟨ˆIµ−I0⟩< n
‖ ˜I‖∞
K
(
~Iµ
))
K
(
~I
)
+ 1
n3O
(
⟨ˆµ−I0⟩3‖˜I‖3
∞
)
+ P
(
⟨ˆIµ−I0⟩> n
‖˜I‖∞
)
,
where we used that SJ(ξn(I))
SJ(ξn(I0))≤ 1 for all J∈Bk,n by (16) to get a rough bound on the expectation
E
[
S ˆIµ(2π ˜I/n)
S ˆIµ(2π ˜I0/n)1⟨ˆIµ−I0⟩> n
‖ ˜I‖∞
]
. By Markov inequality, P
(
⟨ˆIµ−I0⟩> n
‖˜I‖∞
)
≤ ‖˜I‖3
∞
n3 ⟨ˆµ−I0⟩3, where
we recall from (27) that ⟨ˆµ−I0⟩3 = E
[
⟨ˆIµ−I0⟩3
]
. Similarly, using (26) to get K(˜I)≤⟨ ˆI−I0⟩2
for I∈Bk,n, we have
1
k2− 1 E
(
1⟨ˆIµ−I0⟩≥ n
‖ ˜I‖∞
K
(
~Iµ
))
≤ 1
k2− 1 E
(
1⟨ˆIµ−I0⟩> n
‖ ˜I‖∞
⟨ˆIµ−I0⟩2
)
≤ 3‖˜I‖∞
k2n ⟨ˆµ−I0⟩3,
so that, using also that K(˜I)≤k‖˜I‖2
∞, we get
(38) E
[SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
]
= 1− (2π)2
2(k2− 1)n2
[
K(µ)K(˜I)
]
+ 1
kn3O
(
⟨ˆµ−I0⟩3‖˜I‖3
∞
)
,
38 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
where we recall that K(µ) = Eµ(K(~Iµ)). A similar reasoning also yields
(39) E
[⏐⏐⏐⏐⏐
SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
⏐⏐⏐⏐⏐
]
≤ 1− (2π)2
2(k2− 1)n2
[
K(µ)K(˜I)
]
+ 1
kn3O
(
⟨ˆµ−I0⟩3‖˜I‖3
∞
)
.
For the ﬁrst statement, remark that we have by (36) , for α0∈ R,
e−2iπα0⟨λI⟩
kn E
[SIµ(ξn(I))
SIµ(ξn(I0))
]
=E
[
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn
SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
]
=E
[
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn
]
+ E
[SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
]
− 1
+ E
[(
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn − 1
)(SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
− 1
)]
.(40)
Using the Taylor expansion of eit for t∈ R yields
(41)
e2iπ⟨λI⟩·(⟨λJ⟩−α0)
kn = 1+ 2iπ⟨λI⟩· (⟨λJ⟩− α0)
kn − (2π)2⟨λI⟩2· (⟨λJ⟩− α0)2
2k2n2 +O
(
⟨λI⟩3· (⟨λJ⟩− α0)3
k3n3
)
,
for I,J ∈ Bk,n, with O(·) independent of I,J and α0 because the term on the left-hand side is
bounded. Hence, averaging on Iµ yields
E
[
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn
]
=1 + 2iπ⟨λI⟩·
(
E(⟨λIµ⟩)−α0
)
kn −
(2π)2⟨λI⟩2· E
[(
⟨λIµ⟩− α0
)2]
2k2n2
+O


⟨λI⟩3· E
[(
⟨λIµ⟩− α0
)3]
k3n3

,(42)
and putting (38) and (42) together yields
E
[
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn
]
+ E
[SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
]
− 1
=1 + 2iπ⟨λI⟩·
(
E(⟨λIµ⟩)−α0
)
kn − (2π)2
2(k2− 1)n2K(µ)K(~I)−
(2π)2⟨λI⟩2· E
[(
⟨λIµ⟩− α0
)2]
2k2n2
(43)
+ 1
n3O


|⟨λI⟩|3· E
[(
⟨λIµ⟩− α0
)3]
k3 + 1
k⟨ˆµ−I0⟩3·‖ ˜I‖3
∞


QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 39
Finally, we have by (37), the fact that
(
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn − 1
)
and
(
S ˆIµ(2π ˜I/n)
S ˆIµ(2π ˜I0/n)− 1
)
are bounded
by 2 and the inequality |eit− 1|≤ t for t∈ R,
⏐⏐⏐⏐⏐E
[(
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn − 1
)(SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
− 1
)]⏐⏐⏐⏐⏐
=E
[⏐⏐⏐⏐e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn − 1
⏐⏐⏐⏐
⏐⏐⏐⏐⏐
SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
− 1
⏐⏐⏐⏐⏐ 1⟨ˆIµ−I0⟩≤n/‖I‖∞
]
+O
(
P(⟨ˆIµ−I0⟩>n/‖I‖∞)
)
≤E
[
2π⟨λI⟩·
⏐⏐⟨λIµ⟩− α0
⏐⏐
kn · (2π)2
2n2
K(˜I)K(~Iµ)
k2− 1 · 1⟨ˆIµ−I0⟩≤n/‖I‖∞
]
+ 1
kn3O
(
⟨ˆµ−I0⟩3‖˜I‖3
∞
)
+O
(
P(⟨ˆIµ−I0⟩>n/‖I‖∞)
)
≤ 1
n3O

E


⟨λI⟩·
⏐⏐⏐⟨λIµ⟩− α0
⏐⏐⏐
k ·⟨ ˆIµ−I0⟩2·‖ ˜I‖2
∞

 +O
(
⟨ˆµ−I0⟩3‖˜I‖3
∞
)

,
where we used Markov inequality to bound P(⟨ˆIµ−I0⟩ > k1/3n/‖I‖∞) by 1
kn3⟨ˆµ−I0⟩3‖˜I‖3
∞ and
used the inequality K( ˜Iµ)≤⟨ ˆIµ−I0⟩2 and K(˜I)≤ k‖˜I‖2
∞ on the last inequality. By the Young
inequalityab≤ a3
3 + 3b3/2
2 for a,b≥ 0, we ﬁnally get
E
[(
e2iπ
⟨λI⟩·(⟨λIµ⟩−α0)
kn − 1
)(SˆIµ
(2π ˜I/n)
SˆIµ
(2π ˜I0/n)
− 1
)]
= 1
n3O


|⟨λI⟩|3· E
[(
⟨λIµ⟩− α0
)3]
k3 +⟨ˆµ−I0⟩3‖˜I‖3
∞

.
Putting the latter estimates with (43) into (40) and setting α0 = E(⟨λIµ⟩) =⟨µ⟩−⟨ I0⟩ yields then
e−2iπ (⟨µ⟩−⟨I0⟩)·⟨λI⟩
kn Φn[µ](I(n))
= 1 + 2iπ
kn⟨λI⟩Eµ
[
⟨λIµ⟩− (⟨µ⟩−⟨ I0⟩)
]
− (2π)2
2n2
[
K(µ)K(~I)
k2− 1 +⟨λI⟩2Var (µ)
k2
]
+ 1
n3O
(|⟨λI⟩|3·Var 3(µ)
k3 +⟨ˆµ−I0⟩3‖˜I‖3
∞
)
= 1− (2π)2
2n2
[
K(µ)K(~I)
k2− 1 +⟨λI⟩2Var (µ))
k2
]
+ 1
n3O
(|⟨λI⟩|3·Var 3(µ)
k3 +⟨ˆµ−I0⟩3‖˜I‖3
∞
)
.
To get the second statement of the lemma, note that by (36),
⏐⏐⏐Φn[µ](I(n))
⏐⏐⏐ =
⏐⏐⏐⏐E
[SIµ(ξn(I))
SIµ(ξn(I0))
]⏐⏐⏐⏐≤ E
[⏐⏐⏐⏐
SIµ(ξn(I))
SIµ(ξn(I0))
⏐⏐⏐⏐
]
= E


⏐⏐⏐⏐⏐⏐
SˆIµ
(
2π ˜I/n
)
SˆIµ
(
2π ˜I0/n
)
⏐⏐⏐⏐⏐⏐

.
Using (39) yields then the result. □
From Lemma 5.1, we can deduce asymptotics of the discrete Fourier transform of a convolution
of Markov kernels on Bk,n. For a sequence m = (µr)1≤r≤m of h-probability measures, recall the
40 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
notation from Section 2.4
X(m) =
(
1
m
m∑
r=1
X(µr)
)
−X(I0),
for X(µ) =K(µ) or any quantity deﬁned in (27). We also set
∗m =µ1∗µ2∗...µ m.
Proposition 5.3. Let M > 0 and suppose that m = (µr)1≤r≤m is a sequence of h-probability
measures on Bk,n such that Var 3(m)≤ MVar (m)3/2 and⟨ˆm⟩3 ≤ MK (m)3/2. Then, for all
J∈Bk with J1<J k +n, we have
⏐⏐⏐Φn[∗m](J(n))
⏐⏐⏐≤A(J) exp
(
−m(2π)2
2n2
K( ˜J)K(m)
k2− 1 + mM
n3 O
([
kK( ˜J)K(m)
]3/2))
with A(J)≤ 1 and
A(J) = exp
[
− m(2π)2
2n2
[Var (m)⟨λJ⟩2
k2
]
+ mM
n3 O
(
Var (m)3/2·|⟨λJ⟩|3
k3
)]
.
When‖ ˜J‖∞≤ c n
m1/3M 1/3K(m)1/2 and⟨λJ⟩≤ c kn
m1/3M 1/3Var (m)1/2 for some numeric c > 0 small
enough, we get
e−2iπm⟨m⟩)·⟨λJ⟩
kn Φn[∗m](J(n)) = exp
[
− m(2π)2
2n2
[
K(m)K( ˜J)
k2− 1 + Var (m)⟨λJ⟩2
k2
]
+ mM
n3 O
(
Var (m)3/2·|⟨λJ⟩|3
k3 +
[
k·K(m)·K( ˜J)
]3/2
)]
.
To prove this proposition, we will need the following estimate.
Lemma 5.4. For all I∈Bk with I⁄=I0,
‖˜I‖2
∞≤kK(˜I).
As a consequence, for µ∈M 1(Bk,n),
⟨ˆµ−I0⟩3≤ 2
√
2k3‖˜µ‖3.
Proof. First remark that either‖˜I‖∞ = ˜I1 or‖˜I‖∞ = ˜Ik. Up to replacingI by (−Ik,..., −I1),which
does not change K(˜I), we can assume that‖˜I‖∞ = ˜I1. Then, recall that K(˜I) =‖˜I‖2−‖I0‖2 and
write ˜I =I0 +x for some nondecreasing sequence x∈ Rk satisfying∑k
i=1xi = 0. Then, we have
k∑
i=2
((I0)i +xi)2 =
k∑
i=2
(I0)2
i + 2
k∑
i=2
(I0)ixi +
k∑
i=2
x2
i.
Since I0 and x are nondecreasing sequences, by Chebyschev’s sum inequality, ∑k
i=2(I0)ixi ≥
1
k−1(∑k
i=2(I0)i)(∑k
i=2xi), and by convexity, ∑k
i=2x2
i ≥ 1
k−1
(∑k
i=2xi
)2
. Hence, replacing xi by
1
k−1
(∑k
i=2xi
)
yields a vector ˜I′ = ˜I0 + (x1, 1
k−1
∑k
i=2xi,... ) such that ˜I′
1 = ˜I1,∑k
i=1 ˜I′
i = 0 and
K(˜I)≥K(˜I′). We thus only need to show that K(˜I′)≥‖ ˜I′
1‖2 = ˜I1.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 41
Now, the condition ∑k
i=1xi = 0 yields that 1
k−1
∑k
i=2xi =− x1
k−1. Hence,
kK(˜I′)−‖ ˜I‖2
∞ = (k− 1)
(
x1 + (˜I0)1
)2
+k
k∑
i=2
(
(˜I0)i− x1
k− 1
)2
−k‖˜I0‖2 :=g(x1).
Since (I0)i = k+1−2i
2 for 1≤i≤k, we haveg′(x1) = 2(k−1)
(
x1 + k−1
2
)
+2k∑k
i=2
(
x1
k−1− k+1−2i
2
)
≥
0 for x1≥ 0. It is thus suﬃcient to check that g(x1)≥ 0 for the smallest possible value of x1
satisfying x1 > 0 and x1−
(
− x1
k−1
)
≥ 1 (since ˜I and thus also ˜I′ satisfy the latter condition).
This value is x1 = k−1
k , which actually corresponds to I = (k,k − 2,..., 0). Using the formula
‖x + ˜I0‖2−‖ ˜I0‖2 =∑k
i=1xi(xi +k + 1− 2i), we then have
g
(k− 1
k
)
=k
(
k− 1
k
(k− 1
k +k− 1
)
−
k∑
i=2
1
k
(
−1
k +k + 1− 2i
))
−
(k− 1
2 + k− 1
k
)2
=
((k− 1)2(k + 1)
k − (k− 1)
(
k− 1− 1
k
)
+k(k− 1)
)
−
(k + 1
2 − 1
k
)2
=k2− 1−
(k + 1
2
)2
≥ 0.
The second statement is a consequence of the ﬁrst one. First,‖ˆI‖∞≤ 2‖˜I‖∞ and⟨ˆI−I0⟩≤ k‖ˆI‖∞
implies⟨ˆI−I0⟩2≤ 2kK(˜I) when I⁄=I0. Since the inequality is also satisﬁed when I =I0,
⟨ˆµ−I0⟩3 = E
[
⟨Iµ⟩3]
≤ E
[
⟨Iµ⟩3]
≤ 2
√
2k3E
[
K(˜Iµ)3/2
]
≤ 2
√
2k3E
[
‖˜Iµ‖3
]
=‖˜µ‖3.
□
Proof of Proposition 5.3. ForJ =I0 the result is clear, since Φn[∗m](I0) = 1 (because∗m is again
a h-probability measure) and K(˜I0) =⟨λI0⟩ = 0.
LetJ⁄=I0∈Bk withJ1<J k+n and let m = (µr)1≤r≤m be a sequence ofh-probability measures
satisfying the hypothesis of the proposition. First, Lemma 5.1 yields that for all 1 ≤r≤n,
⏐⏐⏐Φn[µr](J(n))
⏐⏐⏐≤ 1− (2π)2
2n2
[
K(µr)K( ˜J)
k2− 1
]
+ 1
n3O
(
⟨ˆµr−I0⟩3·‖ ˜J‖3
∞
)
,
with O(·) only depending on numeric constants. Using (18) with the inequality 1 + u≤ eu for
u∈ R yields then
⏐⏐⏐Φn[∗m](J(n))
⏐⏐⏐ =
m∏
r=1
⏐⏐⏐Φn[µr](J(n))
⏐⏐⏐
≤
m∏
r=1
[
1− (2π)2
2n2
[
K(µr)K( ˜J)
k2− 1
]
+ 1
n3O
(
⟨ˆµr−I0⟩3·‖ ˜J‖3
∞
)]
≤ exp
(
−(2π)2
2n2
K( ˜J)∑m
r=1K(µr)
k2− 1 + 1
n3O
(
‖ ˜J‖3
∞·
m∑
r=1
⟨ˆµr−I0⟩3
))
.
42 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Since‖ ˜J‖2
∞≤kK( ˜J) for J⁄=I0 by Lemma 5.4, we thus have, using the hypothesis of the proposi-
tion,
1
n3O
(
‖ ˜J‖3
∞·
m∑
r=1
⟨ˆµr−I0⟩3
)
= m
n3O
(
k3/2K( ˜J)3/2·⟨ ˆmr⟩3
)
= m
n3O
(
k3/2K( ˜J)3/2·K(m)3/2
)
,
and thus
(44)
⏐⏐⏐Φn[∗m](J(n))
⏐⏐⏐≤ exp
(
−(2π)2
2n2
K( ˜J)∑m
r=1K(µr)
k2− 1 + m
n3O
(
k3/2K( ˜J)3/2·K(m)3/2
))
.
Then, Lemma 5.1 yields for all 1 ≤r≤n,
e−2iπ (⟨µr⟩−⟨I0⟩)·⟨λJ⟩
kn Φn[µr](J(n)) = 1− (2π)2
2n2
[
K(µr)K( ˜J)
k2− 1 + Var (µr)⟨λJ⟩2
k2
]
+ 1
n3O
(Var 3(µr)·|⟨λJ⟩|3
k3 +⟨ˆµr−I0⟩3·‖ ˜J‖3
∞
)
,
with O(·) only depending on numeric constants. Using the inequality 1 + u≤ eu for u∈ R, (18)
and the hypothesis of the proposition then gives as before
⏐⏐⏐Φn[∗m](J(n))
⏐⏐⏐ =
m∏
r=1
⏐⏐⏐Φn[µr](J(n))
⏐⏐⏐≤ exp
[
− m(2π)2
2n2
[
K(m)K( ˜J)
k2− 1 + Var (m)⟨λJ⟩2
k2
]
+ mM
n3 O
(Var 3(m)·|⟨λJ⟩|3
k3 +
[
k·K(m)·K( ˜J)
]3/2)]
.
The latter inequality together with (44) imply the ﬁrst statement of the proposition.
Since K(µr)≤ (⟨ˆµr⟩−⟨ I0⟩)2 and K( ˜J)≤ k‖ ˜J‖2
∞, K(µr)K( ˜J)
k2−1 = O(‖ ˜J‖2
∞⟨ˆµr−I0⟩2). More-
over, Var 2(µr) ≤ Var 3(µr)2/3. Hence, assuming that ‖ ˜J‖∞ ≤ c n
sup1≤r≤m⟨ˆµr−I0⟩ and ⟨λJ⟩ ≤
c kn
sup1≤r≤mVar 3(µr)1/3 for c small enough, we have
(2π)2
2n2
[
K(µr)K( ˜J)
k2− 1 + Var (µr)⟨λJ⟩2
k2
]
+ 1
n3O
(Var 3(µr)·|⟨λJ⟩|3
k3 +⟨ˆµr−I0⟩3·‖ ˜J‖3
∞
)
≤ 1/2.
The hypotheses⟨ ˆm⟩3≤MK (m)3/2 implies thatm1/3M 1/2K(m)1/2≥ sup1≤r≤m⟨ˆµr−I0r⟩. Hence,
when‖ ˜J‖∞ ≤ c n
m1/3M 1/3K(m)1/2 and⟨λJ⟩ ≤c kn
m1/3M 1/3Var (m)1/2 we have in particular ‖ ˜J‖∞ ≤
c n
sup1≤r≤m⟨ˆµr−I0⟩. Similarly, ⟨λJ⟩≤ c kn
m1/3M 1/3Var (m)1/2 implies that ⟨λJ⟩≤ c kn
sup1≤r≤mVar 3(µr)1/3 .
Hence, for such J, using the estimate 1 + u = exp(u +O(u3/2)) for|u|≤ 1/2 yields then
e−2iπ (⟨µr⟩−⟨I0⟩)·⟨λJ⟩
kn Φn[µr](J(n))
= exp
[
− (2π)2
2n2
[
K(µr)K( ˜J)
k2− 1 + Var (µr)⟨λJ⟩2
k2
]
+ 1
n3O
(Var 3(µr)·|⟨λJ⟩|3
k3 +⟨ˆµr−I0⟩3·‖ ˜J‖3
∞
)
+ 1
n3O
(
K(µr)3/2K( ˜J)3/2
k3 + Var (µr)3/2|⟨λJ⟩|3
k3
)]
.
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 43
Since Var (µr)3/2≤Var 3(µr), K(µr)3/2≤⟨ ˆµr−I0⟩3 and K( ˜J)
k ≤‖ ˜J‖2
∞,
O
(
K(µr)3/2K( ˜J)3/2
k3 + Var (µr)3/2|⟨λJ⟩|3
k3
)
=O
(
⟨ˆµr−I0⟩3‖ ˜J‖3
∞ + Var 3(µr)|⟨λJ⟩|3
k3
)
.
Hence, since K( ˜J)≤k‖ ˜J‖2
∞ by Lemma 5.4,
e−2iπ (⟨µr⟩−⟨I0⟩)·⟨λJ⟩
kn Φn[µr](J(n))
= exp
[
− (2π)2
2n2
[
K(µr)K( ˜J)
k2− 1 + Var (µr)⟨λJ⟩2
k2
]
+ 1
n3O
(
k3/2⟨ˆµr−I0⟩3·K( ˜J)3/2 + Var 3(µr)·|⟨λJ⟩|3
k3
)]
.
Using (18) for 1≤r≤m yields then
e−2iπm⟨m⟩)·⟨λJ⟩
kn Φn[∗m](J(n)) =
m∏
r=1
e−2iπ (⟨µr⟩−⟨I0⟩)·⟨λJ⟩
kn Φn[µr](J)
= exp
[
− m(2π)2
2n2
[
K(m)K( ˜J)
k2− 1 + Var (m)⟨λJ⟩2
k2
]
+ m
n3O
(
k3/2⟨ ˆm⟩3·K( ˜J)3/2 + Var 3(m)·|⟨λJ⟩|3
k3
)]
.
The hypothesisVar 3(m)≤MVar (m)3/2 and⟨ ˆm⟩3≤MK (m)3/2 yields then the second statement
of the proposition. □
Remark that the ﬁrst statement of Proposition 5.3 is only relevant when K( ˜J)≤ c n2k3
M 2K(m) for
some numeric c> 0. We conclude this section by a crude estimate of Φ n[∗m] when K( ˜J)≥cn2.
Lemma 5.5. For any 0<c< 1/2, there exists 0<t< 1 depending on c such that for I,J ∈Bk,n
with sup((Ii−Ii+1) mod n)≥cn,
|SJ(ξn(I))|
SJ(ξn(I0))≤ max
(k−2
k ,t
)
1 +O
(k2⟨λ ˆJ⟩2
n2
).
In particular, there exists η,δ > 0 only depending on k and c such that for any sequence m =
(µi)1≤i≤m of h-probability measures with⟨ ˆm⟩3≤MK (m)3/2 and I∈Bk such that sup((ˆIi− ˆIi+1)
mod n)≥cn,
Φn[∗m](I(n))≤ exp
(
−mδ + mM
η3n3K(m)3/2
)
.
44 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Proof. We prove the ﬁrst part of the lemma in the case where n/2≥λ1−λ2≥cn, the other cases
being deduced similarly. Set λ =λ ˆJ and ζj =e2iπij/n for 1≤j≤n. Then, by (36),
|SJ(ξn(I))| =|sλ(ζ1,ζ 2,ζ 3,... )|
≤
∑
µ⊂λ
l(µ)≤2
⏐⏐sµ(ζ1,ζ 2)sλ/µ(ζ3,...,ζ k)
⏐⏐
≤|sλ(ζ3,...,ζ k)| +
∑
0≤b<a+1≤λ+1
b≤λ2
⏐⏐s(a,b)(ζ1,ζ 2)sλ/(a,b)(ζ3,...,ζ k)
⏐⏐
+
∑
0<a≤λ2
⏐⏐s(a,a)(ζ1,ζ 2)sλ/(a,a)(ζ3,...,ζ k) +s(a,a−1)(ζ1,ζ 2)sλ/(a,a−1)(ζ3,...,ζ k)
⏐⏐
:=S1 +S2 +S3.
First, by the Weyl dimension formula sλ(1k) =∏
1≤i<j≤k
(λi−λj+j−i)
j−i for λ⁄=∅,
S1≤sλ(1k−2) =δl(λ)≤k−2
1∏
1≤i≤k−2
λi+k−1−i
k−1−i
λi+k−i
k−i
·sλ(1k)
≤k− 2
k sλ(1k).(45)
Then, if 0≤b<a , then
|s(a,b)(ζ1,ζ 2)| =|e2(ζ1,ζ 2)|b|hb−a(ζ1,ζ 2)| =|hb−a(ζ1,ζ 2)|,
whereel andhl are respectively the elementary and complete homogeneous symmetric polynomials.
Forl> 0, hl(ζ1,ζ 2) = ζl+1
1 −ζl+1
2
ζ1−ζ2
and thus, using that i1≥i2,
|hl(ζ1,ζ 2)| =| sin((l + 1)π(i1−i2)/n)|
sin(π(i1−i2)/n) .
Remark that for π
2(l+1)≤x≤π/2, the inequality sin(u)>u − u3
6 for u∈]0,π/ 2] yields
| sin((l + 1)x)|
sin(x) ≤ 1
sin(x)≤ 1
sin
(
π
2(l+1)
)≤ 2(l + 1)
π
(
1−
(
π
2(l+1)
)2
/6
) <u 1(l + 1)
for u1 = 2
π
(
1−(π
4 )
2
/6
) < 1 independent of l. Hence, if l is such that 1
2(l+1)≤ i1−i2
n ≤ 1− 1
2(l+1),
|hl((ζ1,ζ 2)|≤ t(l + 1) =ts(a,b)(1, 1).
Since c ≤ i1−i2
n ≤ 1− c, there is a ﬁnite number only depending on c and l ∈ N satisfying
min
(i1−i2
n , 1− i1−i2
n
)
≤ 1
2(l+1). For each of them, the function x↦→ sin((l+1)x)
sinx is strictly decreasing
on [0,π/ (2(l+1))] with maximum (l+1) at 0. Hence, there exists a constant u2< 1 only depending
on c such that for any l such that min
(i1−i2
n , 1− i1−i2
n
)
≤ 1
2(l+1),
| sin((l + 1)π(i1−ik)/n)|
sin(π(i1−i2)/n) ≤u2(l + 1).
We have thus found a constant u = (u1∨u2)< 1 only depending on c such that for all l≥ 1,
(46) |hl((ζ1,ζ 2)|≤ u(l + 1).
QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY DYSON BROWNIAN MOTION 45
In particular, for 0≤b<a ,
|s(a,b)(ζ1,ζ 2)| =|hb−a(ζ1,ζ 2)|≤ u(b−a + 1) =us(a,b)(1, 1),
and summing on all contributions yields
(47) S2≤
∑
0≤b<a+1≤λ+1
b≤λ2
s(a,b)(1, 1)sλ/(a,b)(1k−2).
Then, for a≤ λ2, remark that sλ/(a,a)(1k−2)≤ sλ/(a,a−1)(1k−2). Indeed, any semistandard ﬁlling
of λ/(a,a ) yields a semistandard ﬁlling of λ/(a,a− 1) by putting 1 in the cell (2 ,a ). Hence, using
that|s(a,a)(ζ1,ζ 2)| = 1 and
|s(a,a−1)(ζ1,ζ 2)| =|h1(ζ1,ζ 2)|≤ 2 cos(cπ) = cos(cπ)s(a,a−1)(1, 1),
we get⏐⏐s(a,a)(ζ1,ζ 2)sλ/(a,a)(ζ3,...,ζ k) +s(a,a−1)(ζ1,ζ 2)sλ/(a,a−1)(ζ3,...,ζ k)
⏐⏐
≤s(a,a)(1, 1)sλ/(a,a)(1k−2) + cos(cπ)s(a,a−1)(1, 1)sλ/(a,a−1)(1k−2)
≤ 1 + cos(cπ)
2
(
s(a,a)(1, 1)sλ/(a,a)(1k−2) +s(a,a−1)(1, 1)sλ/(a,a−1)(1k−2)
)
.
Summing on all a≤λ2 yields then
(48) S3≤ 1 + cos(cπ)
2
∑
a≤λ2
(
s(a,a)(1, 1)sλ/(a,a)(1k−2) +s(a,a−1)(1, 1)sλ/(a,a−1)(1k−2)
)
.
Putting (45),(47) and (48) together yields the existence of t< 1 depending only on c such that
S1 +S2 +S3≤ max
(k− 2
k ,t
) ∑
µ⊂λ
l(µ)≤2
sµ(1, 1)sλ/µ(1k−2)≤ max
(k− 2
k ,t
)
sλ(1k).
On the other hand, by (35) we have
SJ(ξn(I0))
SJ(0,..., 0) = 1 +O
(k2⟨λ⟩2
n2
)
,
so that ﬁnally
|SJ(ξn(I))|
SJ(ξn(I0))≤ max
(k−2
k ,t
)
1−c′k2⟨λ ˆJ⟩2
n2
,
with t< 1 depending on c and c′> 0 numeric.
For the second statement, recalling that Φn[µ](I(n)) = E
[
SIµ(ξn(I (n)))
SIµ(ξn(I (n)))
]
= E
[SIµ(ξn(I))
SIµ(ξn(I))
]
and that
⏐⏐⏐ SJ(ξn(I))
SJ(ξn(I0))
⏐⏐⏐≤ 1 for all J∈Bk,n, for η >0 to choose later we have
⏐⏐⏐Φn[µ](I(n))
⏐⏐⏐≤ P(⟨ˆIµ⟩>ηn )) + E
[⏐⏐⏐⏐
SIµ(ξn(I))
SIµ(ξn(I))
⏐⏐⏐⏐ 1⟨ˆIµ⟩≤ηn
)
,
so that by Markov inequality and the ﬁrst part of the statement, there exists t> 0 only depending
on c such that
⏐⏐⏐Φn[µ](I(n))
⏐⏐⏐≤
E
[
⟨ˆIµ⟩3
]
η3n3 + max(k−2
k ,t )
1−c′k2η2 ≤ 1−δ +
E
[
⟨ˆIµ⟩3
]
η3n3 ,
where we choose η (only depending on c and k) such that
max(k−2
k ,t)
1−c′k2η2 = 1−δ with δ >0.
46 J. GUILHOT, C. LECOUVEY, AND P. TARRAGO
Let m = (µr)1≤r≤m be a sequence of h-probability measures satisfying the hypotheses of the
lemma. Applying the bound 1 −δ +
E[⟨ˆIµ⟩3]
η3n3 ≤ exp
(
−δ +
E[⟨ˆIµ⟩3]
η3n3
)
and taking the product on all
Φn[Iµr](I(n)) yield then with (18)
Φn[∗m](I(n))≤ exp
(
−mδ + 1
n3η3
m∑
r=1
E
[
⟨ˆIµr⟩3
])
≤ exp
(
−m
(
δ + M
n3η3K(m)3/2
))
.
□
