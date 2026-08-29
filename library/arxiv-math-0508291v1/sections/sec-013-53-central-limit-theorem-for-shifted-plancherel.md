---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-013-53-central-limit-theorem-for-shifted-plancherel
section_title: "Central limit theorem for shifted Plancherel measure"
section_number: 5.3
pages: 34-42
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
subsection studies the statistic W =
√
n!
zµ 2n−l(µ )
X λ
µ
gλ
, where µ ∈ OP (n) is
ﬁxed and λ ∈DP (n) is chosen from shifted Plancherel measure. The main
goal is a proof of Theorem 5.2.
UsingL, one constructs an exchangeable pair ( W,W ′) as follows. Choose
λ from the shifted Plancherel measure on partitions of size n. Then choose
ρ with probability L(λ,ρ ) and let ( W,W ′) = (W (λ),W (ρ)). Using Jτ , one
constructs an “exchangeable pair” ( W,W ∗) as follows. Choose λ from the
shifted Plancherel measure on partitions of size n. Then choose ρ with
“probability” Jτ (λ,ρ ) and let ( W,W ∗) = (W (λ),W (ρ)). The pair ( W,W ′)
is a valid candidate for Stein’s method, but the pair ( W,W ∗) is much easier
to work with, and by Proposition 5.9, when τ = (n − 1, 1), this gives insight
into the genuine exchangeable pair ( W,W ′). Even though the transition
probabilities of Jτ can be negative, for convenience the usual language of
probability theory (expected value, variance, etc.) will b e used when working
with them.
Lemma 5.10. (1) E(W ∗|W ) =
( X τ
µ
gτ
)
W .
(2) E(W ′|W ) = m1(µ )
n W .
35
Proof. For the ﬁrst assertion, the deﬁnition of J(n−1, 1) and Lemma 5.4 imply
that
E(W ∗|λ) =
√
n!
zµ 2n−l(µ )
∑
ρ∈DP (n)
gρ
2l(ρ)gλgτ
∑
ν∈OP (n)
2l(ν)X λ
νX ρ
νX τ
ν
zν
X ρ
µ
gρ
=
√
n!
zµ 2n−l(µ )
1
gλgτ
∑
ν∈OP (n)
2l(ν)X λ
νX τ
ν
zν
∑
ρ∈DP (n)
X ρ
νX ρ
µ
2l(ρ)
=
√
n!
zµ 2n−l(µ )
X λ
µ
gλ
X τ
µ
gτ
=
( X τ
µ
gτ
)
W (λ).
The ﬁrst assertion follows since this depends on λ only through W .
For the second assertion, observe that by Proposition 5.9,
E(W ′ −W |λ) =
∑
ρ
L(λ,ρ ) (W (ρ) −W (λ))
= n − 2
n
∑
ρ
J(n−1, 1)(λ,ρ ) (W (ρ) −W (λ))
= −
( n − 2
n
)
W (λ) + n − 2
n
∑
ρ
J(n−1, 1)(λ,ρ )W (ρ).
By the ﬁrst assertion and Lemma 5.6, this is
−
( n − 2
n
)
W (λ) + n − 2
n
m1(µ) − 2
n − 2 W (λ) =
( m1(µ)
n − 1
)
W (λ),
which implies the result. □
Corollary 5.11 will not be needed but is worth recording.
Corollary 5.11. The eigenvalues of Jτ are
X τ
µ
gτ as µ ranges over OP (n).
The functions ψµ (λ) =
√
n!
zµ 2n−l(µ )
X λ
µ
gλ
are a basis of eigenvectors of Jτ , or-
thonormal with respect to the inner product
⟨f1,f 2⟩ =
∑
λ ∈DP (n)
f1(λ)f2(λ) 2n−l(λ )g2
λ
n! .
Proof. The proof of part 1 of Lemma 5.10 shows that ψµ is an eigenvector of
Jτ with eigenvalue
X τ
µ
gτ . The orthonormality assertion follows from Lemma
5.4 and the fact from [Mac] that all X λ
µ are real valued. The basis assertion
follows since |DP (n)| = |OP (n)|. □
Lemma 5.12. E(W ∗ −W )2 = 2
(
1 −
X τ
µ
gτ
)
.
36
Proof. This follows from the proof of Lemma 2.3 (which does not requi re
non-negative transition probabilities) and part 1 of Lemma 5.10. □
For the remainder of this subsection, pm( ˜Kν ) will denote the coeﬃcient
of ˜Kν in ( ˜Kµ )m. When m = 0 this is to be interpreted through Lemma 5.5,
so that p0( ˜K(1n)) = 1 and p0( ˜Kν ) = 0 for ν ⁄= (1 n). Due to the signs in the
deﬁnition of ˜Kν , these numbers are not probabilities so care must be taken in
working with them. For instance it is not true that ∑
ν∈OP (n)pm( ˜Kν ) = 1.
However the following three relations will be useful.
Lemma 5.13. ∑
ν∈OP (n)p2( ˜Kν )2l(ν)−n = 2 2[l(µ )−n].
Proof. Using Lemma 5.5, one has that,
∑
ν∈OP (n)
p2( ˜Kν )2l(ν) = 2 2l(µ )−n ∑
ρ∈DP (n)
2−l(ρ) (X ρ
µ )2
gρ
∑
ν∈OP (n)
2l(ν)
zν
X ρ
ν.
By page 248 of [Mac], X n
ν = 1, so that Lemma 5.3 implies that
∑
ν∈OP (n)
2l(ν)
zν
X ρ
νX n
ν = 2δρ,n.
The result follows. □
Lemma 5.14. E
( X λ
µ
gλ
) 4
= (2n−l(µ ))4∑
ν∈OP (n)p2( ˜Kν )2 2l(ν )zν
2nn! .
Proof. Consider the coeﬃcient of ˜K(1n) in ( ˜Kµ )4. On one hand, by Lemma
5.5 it is equal to (2 l(µ )−n)4E
( X λ
µ
gλ
) 4
. On the other hand,
( ˜Kµ )4 = ( ˜Kµ )2( ˜Kµ )2 =

 ∑
ν∈OP (n)
p2( ˜Kν ) ˜Kν


2
.
From Lemmas 5.5 and Lemma 5.4, it follows that the coeﬃcient o f ˜K(1n) in
˜Kν1
˜Kν2 is 0 if ν1 ⁄=ν2, and that the coeﬃcient of ˜K(1n) in ( ˜Kν )2 is 2l(ν )−nzν
n! .
Thus the coeﬃcient of ˜K(1n) in ( ˜Kµ )4 is equal to
∑
ν∈OP (n)
p2( ˜Kν )2 2l(ν)−nzν
n! .
Comparing the two expressions for the coeﬃcient of ˜K(1n) in ( ˜Kµ )4 proves
the result. □
Lemma 5.15. p3( ˜Kµ ) = 2n−l(µ )
zµ
∑
ν∈OP (n)p2( ˜Kν )22l(ν)−nzν .
Proof. By Lemma 5.5,
p3( ˜Kµ ) = n!(2l(µ )−n)3
zµ
E
(
X λ
µ
gλ
) 4
.
37
Now use Lemma 5.14. □
The next lemmas are crucial.
Lemma 5.16. E((W ∗)2|λ) = n!
zµ 2l(µ )
∑
ν∈OP (n)
X λ
ν
gλ
X τ
ν
gτ 2l(ν)p2( ˜Kν ).
Proof. It follows from the deﬁnitions that E((W ∗)2|λ) is equal to
n!
zµ 2n−l(µ )
∑
ρ∈DP (n)
gρ
2l(ρ)gλgτ
∑
ν∈OP (n)
2l(ν)X λ
νX ρ
νX τ
ν
zν
( X ρ
µ
gρ
) 2
= n!
zµ 2n−l(µ )
∑
ν∈OP (n)
X λ
ν
gλ
X λ
τ
gτ
2l(ν)

 1
zν
∑
ρ∈DP (n)
g2
ρ
2l(ρ)
X ρ
ν
gρ
( X ρ
µ
gρ
) 2

.
The result now follows from Lemma 5.5. □
Lemma 5.17.
Var (E[(W ∗ −W )2|λ]) = n!2n
z2µ 22l(µ )
∑
ν ∈OP (n)
ν ⁄=(1n)
2l(ν)p2( ˜Kν )2zν
( X τ
ν
gτ
+ 1 − 2X τ
µ
gτ
) 2
Proof. By Lemmas 5.16, 5.12, and 5.10, Var (E[(W ∗ −W )2|λ]) is equal to
E(E((W ∗ −W )2|λ)2) − 4
(
1 − X τ
µ
gτ
) 2
= E

 n!
zµ 2l(µ )
∑
ν∈OP (n)
X λ
ν
gλ
X τ
ν
gτ
2l(ν)p2( ˜Kν ) +
(
1 − 2X τ
µ
gτ
)
W 2


2
−4
(
1 − X τ
µ
gτ
) 2
= T1 +T2 +T3 − 4
(
1 − X τ
µ
gτ
) 2
where
T1 =
( n!
zµ 2l(µ )
) 2
E

 ∑
ν∈OP (n)
p2( ˜Kν )X λ
ν
gλ
X τ
ν
gτ
2l(ν)


2
T2 = 2
(
1 − 2X τ
µ
gτ
) (n!)2
z2µ
∑
ν∈OP (n)
X τ
νp2( ˜Kν )
gτ 2n−l(ν) E
(
X λ
ν (X λ
µ )2
(gλ )3
)
T3 =
(
1 − 2X τ
µ
gτ
) 2( n!
2n−l(µ )zµ
) 2
E
(
X λ
µ
gλ
) 4
.
38
These expressions for T1,T 2,T 3 can be simpliﬁed. Lemma 5.4 implies that
T1 = n!2n
(zµ )222l(µ )
∑
ν∈OP (n)
p2( ˜Kν )22l(ν)zν
( X τ
ν
gτ
) 2
.
From Lemma 5.5 it follows that
T2 = 2
(
1 − 2X τ
µ
gτ
) n!2n
(zµ )222l(µ )
∑
ν∈OP (n)
p2( ˜Kν )22l(ν)zν
X τ
ν
gτ
.
By Corollary 5.14,
T3 = n!2n
22l(µ )(zµ )2
(
1 − 2X τ
µ
gτ
) 2 ∑
ν∈OP (n)
p2( ˜Kν )22l(ν)zν.
Hence, one can write
T1 +T2 +T3 = n!2n
(zµ )222l(µ )
∑
ν∈OP (n)
2l(ν)zνp2( ˜Kν )2
( X τ
ν
gτ
+ 1 − 2X τ
µ
gτ
) 2
and the result follows since by Lemmas 5.5 and 5.4, the ν = (1 n) term in
the above sum is 4
(
1 −
X τ
µ
gτ
) 2
. □
Lemma 5.18 will also be helpful.
Lemma 5.18. Letk be a positive integer.
(1) E(W ∗ −W )k is equal to
(
n!2n−l(µ )
zµ
) k/ 2 k∑
m=0
(−1)k−m
( k
m
) ∑
ν∈OP (n)
X τ
νzν
gτn!2n−l(ν)pm( ˜Kν )pk−m( ˜Kν ).
(2) E(W ∗ −W )4 is equal to
(
n!2n−l(µ )
zµ
) 2
 ∑
ν∈OP (n)
(
8
(
1 − X τ
µ
gτ
)
− 6
(
1 − X τ
ν
gτ
)) zνp2( ˜Kν )2
n!2n−l(ν)

.
39
Proof. To prove the ﬁrst assertion, observe that
E((W ∗ −W )k|λ)
=
( n!
zµ 2n−l(µ )
) k/ 2 ∑
ρ∈DP (n)
gρ
2l(ρ)gλgτ
∑
ν∈OP (n)
2l(ν)X λ
νX ρ
νX τ
ν
zν
·
k∑
m=0
(−1)k−m
( k
m
)( X ρ
µ
gρ
) m(
X λ
µ
gλ
) k−m
=
( n!
zµ 2n−l(µ )
) k/ 2 1
gλgτ
k∑
m=0
(−1)k−m
( k
m
) (
X λ
µ
gλ
) k−m
·
∑
ν∈OP (n)
2l(ν)X λ
νX τ
ν
zν
∑
ρ∈DP (n)
g2
ρ
2l(ρ)
X ρ
ν
gρ
( X ρ
µ
gρ
) m
=
( n!
zµ 2n−l(µ )
) k/ 2 1
2ngλgτ
k∑
m=0
(−1)k−m
( k
m
)
(2n−l(µ ))m
(
X λ
µ
gλ
) k−m
·
∑
ν∈OP (n)
2l(ν)X λ
νX τ
νpm( ˜Kν ),
where the last equation is Lemma 5.5. Hence E(W ∗ −W )k is equal to
E(E((W ∗ −W )k|λ))
=
( n!
zµ 2n−l(µ )
) k/ 2 (2n−l(µ ))k
2n
k∑
m=0
(−1)k−m
( k
m
)
·
∑
ν∈OP (n)
2l(ν)X τ
ν
gτ
pm( ˜Kν )
(2n−l(µ ))k−m E

X λ
ν
gλ
(
X λ
µ
gλ
) k−m
.
The ﬁrst assertion now follows from Lemma 5.5.
For the second assertion, the ﬁrst assertion gives that E(W ∗ −W )4 is
equal to
(
n!2n−l(µ )
zµ
) 2 4∑
m=0
(−1)m
( 4
m
) ∑
ν∈OP (n)
zν
2n−l(ν)n!
X τ
ν
gτ
pm( ˜Kν )p4−m( ˜Kν ).
The special case τ = (n) gives that
0 =
(
n!2n−l(µ )
zµ
) 2 4∑
m=0
(−1)m
( 4
m
) ∑
ν∈OP (n)
zν
2n−l(ν)n!pm( ˜Kν )p4−m( ˜Kν ).
Thus in general, E(W ∗ −W )4 is equal to
−
(
n!2n−l(µ )
zµ
) 2 4∑
m=0
(−1)m
( 4
m
) ∑
ν∈OP (n)
(
1 − X τ
ν
gτ
) zνpm( ˜Kν )p4−m( ˜Kν )
2n−l(ν)n! .
40
The m = 0, 4 terms vanish since only ν = (1 n) could contribute, but it
contributes 0. The m = 2 term contributes
−6
(
n!2n−l(µ )
zµ
) 2 ∑
ν∈OP (n)
(
1 − X τ
ν
gτ
) zνp2( ˜Kν )2
n!2n−l(ν) .
Them = 1, 3 terms are equal and together contribute
8
(
n!2n−l(µ )
zµ
) (
1 −X τ
µ
gτ
)
p3( ˜Kµ ).
By Lemma 5.15, this is
8
(
n!2n−l(µ )
zµ
) 2(
1 − X τ
µ
gτ
) ∑
ν∈OP (n)
zνp2( ˜Kν )2
n!2n−l(ν) .
Adding the terms together proves the second assertion. □
The ﬁnal combinatorial ingredient for the proof of Theorem 5 .2 is an upper
bound for p2( ˜Kν ). Lemma 5.19 reduces this to a result obtained earlier in
the section on Gelfand pairs.
Lemma 5.19. Let p2( ˜Kν ) be as in this subsection and let p2(Kν ) be as in
Subsection 4.4. Then p2( ˜Kν ) ≤p2(Kν ) for all ν ∈OP (n).
Proof. Clearly p2(Kν ) is equal to |BnωνBn| multiplied by the coeﬃcient of
ων in 
 1
|Bn|2
∑
x1,x 2∈Bn
x1ωµx2


2
.
Next consider p2( ˜Kν ). By deﬁnition it is the coeﬃcient of ˜Kν in ( ˜Kµ )2.
Corollary 3.2 of [Stm] gives that the coeﬃcient of ων in ˜Kν is 1
|Bnω ν Bn| .
Hence p2( ˜Kν ) is |BnωνBn| multiplied by the coeﬃcient of ων in

 1
|Bn|2
∑
x1,x 2∈Bn
φ(x1x2)x1ωµx2


2
,
where φ is the linear character of Bn described in Subsection 4.1. Since
φ(x1x2) is always ±1, the result follows. □
Finally, we prove Theorem 5.2.
Proof. (Of Theorem 5.2) One can assume that n ≥ 2(2i + 1). In the O
notation throughout the proof, i is ﬁxed and n is growing.
One applies Theorem 2.1 to the pair ( W,W ′), where µ = (2i+ 1, 1n−2i−1).
Then a = 1 − m1(µ )
n by part 2 of Lemma 5.10. Proposition 5.9 implies that
E((W ′ −W )2|λ) = n − 2
n E((W ∗ −W )2|λ)
41
for all λ. Thus
Var (E[(W ′ −W )2|λ]) =
( n − 2
n
) 2
Var (E[(W ∗ −W )2|λ]).
Lemmas 5.17 and 5.6 give that the ﬁrst error term in applying T heorem 2.1
to the pair ( W,W ′) is at most
n − 2
n
n!2n−l(µ )
(
1 − m1(µ )
n
)
zµ
/radicaltp
/radicalvertex
/radicalvertex
/radicalvertex
√
∑
ν ∈OP (n)
ν ⁄=(1n)
zνp2( ˜Kν )2
n!2n−l(ν)
( n +m1(ν) − 2m1(µ)
n − 2
) 2
.
Observe that n−2
n
n!2n−l(µ )
(
1− m1(µ )
n
)
zµ
is O(n2i+2). In the sum over ν ⁄= (1 n), the
term coming from ν = (2i+1, 2i+1, 1n−4i−2) contributes 0. Since n ≥ 2(2i+
1), Lemmas 5.19 and 4.19 imply that zν p2( ˜Kν )2
n!2n−l(ν ) =O(n−4i−3) for all other ν in
the sum, and the number of such ν is bounded by a constant depending on
i but not n. Moreover if p2(~Kν ) ⁄= 0, then p2(Kν ) ⁄= 0, implying by Lemma
4.18 that m1(ν) ≥ n − 4i − 2 and thus that n+m1(ν)−2m1(µ )
n−2 = O(n−1).
Combining these observations gives that the ﬁrst term in the upper bound
of Theorem 2.1 is O(n−1/ 2).
By the Cauchy-Schwarz inequality,
E|W ′ −W |3 ≤
√
E(W ′ −W )2E(W ′ −W )4.
Proposition 5.9 implies that E(W ′ −W )k = n−2
n E(W ∗ −W )k for allk. Hence
Lemmas 5.12 and 5.6 imply that the second error term in Theore m 2.1 is at
most [
(n − 2)
πn
E(W ∗ −W )4
(1 − m1(µ )
n )
] 1/ 4
.
By part 2 of Lemma 5.18 and Lemma 5.6, this can be written as

 1
π
(n!2n−l(µ ))2
(1 − m1(µ )
n )(zµ )2
∑
ν∈OP (n)
(
2 − 8m1(µ)
n + 6m1(ν)
n
) zνp2( ˜Kν )2
n!2n−l(ν)


1/ 4
.
The quantity (n!2n−l(µ ))2
(1− m1(µ )
n )(zµ )2 is O(n4i+3). The contribution from ν = (1 n) to
the sum is 8(2i+1)
n p2( ˜K(1n))2, which by Lemmas 5.5 and 5.4 is 8(2i+1)3
24i n−4i−3+
O(n−4i−4). By Lemmas 5.19 and 4.19, the contribution to the sum from ν
not equal to either (1 n) or (2i + 1, 2i + 1, 1n−4i−2) is O(n−4i−4). The contri-
bution from ν = (2i + 1, 2i + 1, 1n−4i−2) is − 4(2i+1)
n
zν p2( ˜Kν )2
n!2n−l(ν ) . Lemma 5.13
implies that p2( ˜K(2i+1, 2i+1, 1n−4i−2)) = 1 + O(n−1), since p2( ˜Kν ) = O(n−1)
forν ⁄= (2i + 1, 2i + 1, 1n−4i−2) by Lemma 5.19. Thus the contribution from
ν = (2i + 1, 2i + 1, 1n−4i−2) is − 8(2i+1)3
24i n−4i−3 +O(n−4i−4). Hence there is
42
useful cancellation and
∑
ν∈OP (n)
(
2 − 8m1(µ)
n + 6m1(ν)
n
) zνp2( ˜Kν )2
n!2n−l(ν) =O(n−4i−4).
It follows that the second term in the upper bound of Theorem 2 .1 is
O(n−1/ 4), completing the proof. □
