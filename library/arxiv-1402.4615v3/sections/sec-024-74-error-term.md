---
doc_id: arxiv-1402.4615v3
doc_title: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS"
section_id: sec-024-74-error-term
section_title: "Error term"
section_number: 7.4
pages: 45-50
source_pdf: 1402.4615v3.pdf
source_sha256: b6e7c795cd1a7cd2
doc_brief: "GAUSSIAN FLUCTUATIONS OF YOUNG DIAGRAMS AND STRUCTURE CONSTANTS OF JACK CHARACTERS — In this paper, we consider a deformation of Plancherel meas ure linked to Jack polynomials."
---
d )
of the random vectors satisﬁes the assumptions of Theorem 7. 1. In order to prove
that the random vector ˜Wd is asymptotically Gaussian, we need to show that quan-
tities A and B from Theorem 7.1 vanish as n → ∞ . This section is devoted to
making these calculations.
Lemma 7.7. The following inequality holds:
(25) Var(α)
n
(
(E(α)
n )
˜Wd(Wi − W ∗
i )(Wj − W ∗
j )
)
≤ 1
ijni+j+2
×






∑
µ1,µ2,l
|µ1|+ℓ(µ1)≤i+j
|µ2|+ℓ(µ2)≤i+j
H (i,j)
µ1,µ2;(1l)(n)l − (i + j)2

∑
l≥0
g(i),(j);l(n)l


2






,
where
H (i,j)
µ1,µ2;µ := (i+j−|µ1|+m1(µ1))(i+j−|µ2|+m1(µ2))g(i),(j);µ1 g(i),(j);µ2 gµ1,µ2;µ.
Note that the sums in the Lemma are clearly ﬁnite.
Proof. Following Fulman [Ful04, Proof of Proposition 6.4], from Jensen’s inequal-
ity for conditional expectations, the fact that ˜Wd is determined by λ implies that
E(α)
n
(
(E(α)
n )
˜Wd(Wi − W ∗
i )(Wj − W ∗
j )
) 2
≤ E(α)
n
(
(E(α)
n )λ(Wi − W ∗
i )(Wj − W ∗
j )
) 2
.
46 M. DOŁ ˛ EGA AND V . FÉRAY
Fix a partition λ of n. We have, by Proposition 7.2, that
(26)
(E(α)
n )λ(W ∗
i − Wi)(W ∗
j − Wj) = α(n − 1)
α(n − 1) + 1 (E(α)
n )λ(W ′
i − Wi)(W ′
j − Wj)
= α(n − 1)
α(n − 1) + 1
(
(E(α)
n )λ(W ′
i W ′
j) − (E(α)
n )λ(W ′
i )Wj − (E(α)
n )λ(W ′
j)Wi + WiWj
)
= α(n − 1)
α(n − 1) + 1
(
(E(α)
n )λ(W ′
i W ′
j) +
((i + j)(α(n − 1) + 1)
αn(n − 1) − 1
)
WiWj
)
,
where the last equality follows from Proposition 7.4. But th e product WiWj ex-
pands as
(27) WiWj = 1
√ijn(i+j)/2
∑
|µ|≤i+j+2
g(i),(j);µ Chµ .
Thus, strictly from the deﬁnition of L(α), one has
(28) (E(α)
n )λ(W ′
i W ′
j) =
∑
ρ⊢n
L(λ, ρ)Wi(ρ)Wj(ρ)
=
∑
τ ⊢n
θτ (λ)θτ (n−1, 1) (zτ )2α2ℓ(τ )
αnn!√ijn(i+j)/2
∑
|µ|≤i+j+2
g(i),(j);µ
∑
ρ⊢n
Chµ(ρ)θτ (ρ)
j(α)
ρ
.
We may assume n ≥ i + j. Recall that Chµ(ρ) is a multiple of θµ1n−|µ| (ρ) and,
hence, using Lemma 7.3 (1), only terms corresponding to τ = µ1n−|µ| survives
and we get:
(29) (E(α)
n )λ(W ′
i W ′
j) = 1
√ijn(i+j)/2
∑
|µ|≤i+j+2
g(i),(j);µ Chµ(λ)
θµ∪1n−|µ| (n − 1, 1)
zµ∪1n−|µ| αℓ(µ∪1n−|µ| )
αnn! .
We now apply Lemma 7.3 (2):
(30) (E(α)
n )λ(W ′
i W ′
j) = 1
√ijn(i+j)/2
∑
|µ|≤i+j+2
g(i),(j);µ Chµ(λ)
× (α(n − 1) + 1)(n − |µ| + m1(µ)) − n
αn(n − 1) .
One can substitute above equation and equation (27) to the eq uation (26) and
simplify it to obtain
(31) (E(α)
n )λ(W ∗
i − Wi)(W ∗
j − Wj)
= 1
√ijn(i+j)/2
∑
|µ|≤i+j+2
i + j − |µ| + m1(µ)
n g(i),(j);µ Chµ(λ).
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 47
Notice that g(i),(j);µ = 0 for |µ| + ℓ(µ) > i + j, unless µ = (i, j) (Lemma 5.6 (4)).
In the latter case (µ = ( i, j)), the numerical factor i + j − |µ| + m1(µ) vanishes.
It gives that the summation in equation (31) can be restricte d to partitions µ with
|µ| + ℓ(µ) ≤ i + j.
Taking the square, it gives us
(32) E(α)
n
(
(E(α)
n )λ(W ∗
i − Wi)(W ∗
j − Wj)
) 2
= 1
ijni+j+2 E(α)
n

 ∑
|µ|+ℓ(µ)≤i+j
(i + j − |µ| + m1(µ))g(i),(j);µ Chµ(λ)


2
= 1
ijni+j+2
∑
µ1,µ2,µ
|µ1|+ℓ(µ1)≤i+j
|µ2|+ℓ(µ2)≤i+j
H (i,j)
µ1,µ2;µE(α)
n (Chµ(λ))
= 1
ijni+j+2
∑
µ1,µ2,l
|µ1|+ℓ(µ1)≤i+j
|µ2|+ℓ(µ2)≤i+j
H (i,j)
µ1,µ2;(1l)(n)l,
where H (i,j)
µ1,µ2;µ is deﬁned as in the statement of the lemma. The last equality comes
from the easy formula for the expectation of Chµ, see equation (8).
Let us now analyse
(
E(α)
n
(
(E(α)
n ) ˜Wd(W ∗
i − Wi)(W ∗
j − Wj)
))
. After expand-
ing the product, each term can be dealt with as follows:
E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i W ∗
j )
)
= E(α)
n (W ∗
i W ∗
j ) = E(α)
n (WiWj)
E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i Wj)
)
= E(α)
n
(
Wj(E(α)
n )
˜Wd(W ∗
i )
)
=
(
1 − i
n
)
E(α)
n (WiWj)
E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i Wj)
)
=
(
1 − j
n
)
E(α)
n (WiWj).
E(α)
n
(
(E(α)
n )
˜Wd(WiWj)
)
= E(α)
n (WiWj)
The ﬁrst equation comes from the fact that ˜W ∗
d and ˜Wd have the same distribution,
while the second one is a consequence of Proposition 7.4. The third one is similar
to the second one. Therefore
(33)
(
E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i − Wi)(W ∗
j − Wj)
)) 2
=
(i + j
n E(α)
n (WiWj)
) 2
= (i + j)2
ijni+j+2
(∑
µ
g(i),(j);µE(α)
n (Chµ)
) 2
= (i + j)2
ijni+j+2
(∑
l
g(i),(j);l(n)l
) 2
,
48 M. DOŁ ˛ EGA AND V . FÉRAY
where we used equations (27) and (8) in the second and third equalities. We ﬁnish
the proof by the following inequality:
(34) Var(α)
n
(
(E(α)
n )
˜Wd(Wi − W ∗
i )(Wj − W ∗
j )
)
= E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i − Wi)(W ∗
j − Wj)
) 2
−
(
E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i − Wi)(W ∗
j − Wj)
)) 2
≤ E(α)
n
(
(E(α)
n )λ(W ∗
i − Wi)(W ∗
j − Wj)
) 2
−
(
E(α)
n
(
(E(α)
n )
˜Wd(W ∗
i − Wi)(W ∗
j − Wj)
)) 2
.
□
Proposition 7.8. Let d ∈ N and let
A =
∑
2≤i,j≤d+1
n
i
√
Var(α)
n
(
(E(α)
n ) ˜Wd(Wi − W ∗
i )(Wj − W ∗
j )
)
.
Then A = O(n−1/2).
Proof. By Lemma 7.7 we need to estimate the following sum:
(35)





∑
µ1,µ2,l≥1
|µ1|+ℓ(µ1)≤i+j
|µ2|+ℓ(µ2)≤i+j
H (i,j)
µ1,µ2;(1l)(n)l − (i + j)2∑
l,k
g(i),(j);(1l)g(i),(j);(1k )(n)l(n)k






1/2
.
Let us ﬁrst consider the second sum, which is simpler. Suppos e that i ⁄= j. Then,
by Lemma 5.6 (2), summands corresponding to l ≥ (i + j)/2 or k ≥ (i + j)/2
vanish and the sum is O(ni+j−1).
Consider now the case i = j (recall that i, j ≥ 2). We use this time Lemma 5.6
(1): summands corresponding to l ≥ i + 1 or k ≥ i + 1 vanish. Therefore there is
no summands of order ni+j+1. The unique summand of order ni+j (corresponding
to l = k = i) is i2 (n)2
i by Lemma 5.6 (3).
Finally, we have that
(36) (i + j)2∑
l,k
g(i),(j);(1l)g(i),(j);(1k )(n)l(n)k = δi,j4 i4ni+j + O(ni+j−1).
Let us describe the terms corresponding to l ≥ i + j in the ﬁrst sum of (35). By
Lemma 5.6 (1), gµ1,µ2,(1l), and hence H (i,j)
µ1,µ2,(1l), vanishes unless
|µ1| + ℓ(µ1) + |µ2| + ℓ(µ2) ≥ 2l ≥ 2(i + j).
Comparing it with the conditions under the ﬁrst summation sy mbol of (35), we
have, in fact, equalities instead of inequalities above, i. e.
l = i + j = |µ1| + ℓ(µ1) = |µ2| + ℓ(µ2).
Moreover, in this case, by Lemma 5.6 (1), we have that gµ1,µ2;(1i+j ) = 0 unless
µ1 ∪ µ2 = 1 i+j, which means that µ1 = µ2 = (1(i+j)/2) (in particular, i + j must
LARGE DIAGRAMS AND STRUCTURE CONSTANTS 49
be even). Then, by Lemma 5.6 (2), one has that g(i),(j);(1(i+j)/2) = 0 unless i = j.
Therefore, H (i,j)
µ1,µ2;(1l) = 0 if i ⁄= j and l ≥ i + j.
Additionally, using the deﬁnition ofH (i,j)
µ1,µ2,µ, the observations above and Lemma
5.6 (3), one has that H (i,i)
(1i),(1i);(12i) = 4 i4. Concluding,
(37)
∑
µ1,µ2,l
H (i,j)
µ1,µ2;(1l)(n)l = δi,j4 i4ni+j + O(ni+j−1).
Comparing equations (36) and (37), it gives
(38)

 ∑
µ1,µ2,l
H (i,j)
µ1,µ2;(1l)(n)l − (i + j)2∑
l,k
g(i),(j);(1l)g(i),(j);(1k)(n)l(n)k


1/2
= O(n(i+j−1)/2),
which implies that
A =
∑
2≤i,j≤d+1
1
i√ijn(i+j)/2 O(n(i+j−1)/2) = O(n−1/2),
which ﬁnishes the proof. □
Lemma 7.9. For any k ≥ 2, and λ ⊢ n there exists Bα,k ∈ R, which depends only
on k and α such that
|Mk(λ)| ≤ Bα,k max(λ1, λ′
1)k.
Proof. As explained in Section 2, M (α)
k (λ) = M (1)
k (Aα(λ)) is the k-th moment
of the transition measure of the anisotropic digram Aα(λ). But this measure is
supported by the contents of inner corners of Aα(λ). All these contents are clearly
bounded in absolute value by max(√
α λ1, √α−1λ′
1). Hence the k-th moment
of the measure is bounded by the k-th power of this number, which proves the
lemma. □
Proposition 7.10. Let d ∈ N and let
β :=
∑
2≤i,j,k≤d+1
n
i |(W ∗
i − Wi)(W ∗
j − Wj)(W ∗
k − Wk)|.
Then B := E(α)
n (β) = O(n−1/2).
Proof. Fix some integer k ≥ 2. From the deﬁnition of M (α), we know that λ∗
is obtained from λ by removing a box from the diagram of λ and reattaching it
somewhere. It means that λ = τ (i1) and λ∗ = τ (i2) for some τ ⊢ n − 1. It implies
that
|W ∗
k − Wk| ≤
√
k
−1
n−k/2
⏐
⏐
⏐Ch(k)(τ (i1)) − Ch(k)(τ (i2))
⏐
⏐
⏐.
50 M. DOŁ ˛ EGA AND V . FÉRAY
By equation (11), the right hand side of the above inequality is equal to
√
k
−1
n−k/2
⏐
⏐
⏐
⏐
⏐
⏐
⏐
∑
ρ
a(k)
ρ



∑
g,h≥0,
π⊢h
bρ
g,π (γ) Mπ(τ )
(
zg
i1 − zg
i2
)



⏐
⏐
⏐
⏐
⏐
⏐
⏐
,
where |π| ≤ | ρ| −g − 2. By Proposition 3.7 we know, thata(k)
ρ = 0 for |ρ| > k + 1,
hence a(k)
ρ bρ
g,π(γ) = 0 for |π| > k − g − 1. But zg
i1 and zg
i2 are bounded by
Oα,g(max(λ1, λ′
1)g), as α-contents of some box or corner of λ. Thanks to Lemma
7.9, it implies that there exists some Cα,k ∈ R which depends only on k and α
such that
|W ∗
k − Wk| ≤ n−k/2Cα,k max(λ1, λ′
1)k−1.
If λ1 ≤ 2e√
n
α and λ′
1 ≤ 2e√
nα, then, for any integers i, j, k ≥ 2, one has
(39)⏐
⏐(W ∗
i − Wi)(W ∗
j − Wj)(W ∗
k − Wk)
⏐
⏐ ≤ |(W ∗
i −Wi)||(W ∗
j −Wj)||(W ∗
k −Wk)|
= O(n−3/2).
Summing over i, j and k, we get β = O(n−1/2). Otherwise, we use the obvious
bounds λ1, λ′
1 ≤ n, and we get
(40)⏐
⏐(W ∗
i − Wi)(W ∗
j − Wj)(W ∗
k − Wk)
⏐
⏐ ≤ |(W ∗
i −Wi)||(W ∗
j −Wj)||(W ∗
k −Wk)|
= O(n(i+j+k)/2−3)
that is β = O(n3(d+1)/2−2). By Lemma 6.3, the probability that the second case
occurs is exponentially small. Hence the bound of the ﬁrst ca se holds in expecta-
tion. It ﬁnishes the proof. □
