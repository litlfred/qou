---
doc_id: arxiv-math-0503227v2
doc_title: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios By Jason Fulman"
section_id: sec-002-3-central-limit-theorem-for-jack-measure
section_title: "Central limit theorem for Jack measure"
section_number: 3
pages: 9-13
source_pdf: 0503227v2.pdf
source_sha256: 4e83adfdef827103
doc_brief: "An Inductive Proof of the Berry-Esseen Theorem for Character Ratios Running head: Berry-Esseen Theorem for Character Ratios By Jason Fulman — Bolthausen used a variation of Stein’s method to give an"
---
For α > 0 the Jack α measure on partitions of size n chooses a partition λ
with probability
α nn!
∏
x∈λ (αa (x) + l(x) + 1)(αa (x) + l(x) + α ) ,
where the product is over all boxes in the partition. Here a(x) denotes the
number of boxes in the same row of x and to the right of x (the “arm” of x)
10
and l(x) denotes the number of boxes in the same column of x and below x
(the “leg” of x). For example the partition of 5 below
would have Jack α measure
30α 2
(3α + 1)(α + 2)(2α + 1)(α + 1)2 .
Note that when α = 1, Jack measure reduces to Plancherel measure of
the symmetric group. The papers [O2], [BO] emphasize that fo r α ﬁxed
the study of Jack α measure is an important open problem, about which
relatively little is known for general values of α . It is a discrete analog of
eigenvalue ensembles from random matrix theory and like Jac k polynomials
[GHJ], should also be relevant to the moduli space of curves.
Given α > 0, the quantity to be studied is
Tn,α (λ) =
∑
i(α
( λ i
2
)
−
( λ ′
i
2
)
)
√
α
( n
2
) ,
where as usual λ i is the length of the ith row of λ and λ ′
i is the length of
the ith column of λ. It is of interest to study the quantity Tn,α (λ) under
Jack measure for several reasons. When α = 1 it reduces to the study of the
character ratio of transpositions under Plancherel measur e. When α = 2
it is a spherical function of the Gelfand pair ( S2n, H 2n) where H2n is the
hyperoctahedral group of size 2 nn!. Also by Corollary 1 of [DHol], there
is a natural random walk on perfect matchings of the complete graph on n
vertices, whose eigenvalues are precisely Tn, 2(λ )
√
n(n−1) , occurring with multiplicity
proportional to the Jack 2 measure of λ.
The paper [F2] used the “exchangeable pairs” version of Stei n’s method
to prove a central limit theorem for Tn,α with error term Cα n−1/ 4 where Cα
is a constant depending on α . This was sharpened in [F3] using martingales
to Cα,s n−s for any s < 1
2 .
The main result of this section is Theorem 3.1.
Theorem 3.1. Suppose that α ≥ 1 and let λ be chosen from the Jack α
measure on partitions of size n. Then there is a constant Cα depending on
α so that for all n ≥ 2 and real x0,
⏐
⏐
⏐
⏐P (Tn,α (λ) ≤ x0) − 1
√
2π
∫ x0
−∞
e− t2
2 dt
⏐
⏐
⏐
⏐ ≤ Cα n−1/ 2.
Note that in Theorem 3.1 we suppose that α ≥ 1 since the Jack α proba-
bility of λ is equal to the Jack 1
α
probability of the transpose of λ, implying
that for any x, the Jack α probability that Tn,α = x is equal to the Jack 1
α
probability that Tn, 1
α
= −x. Also note that Cα must depend on α , since by
11
Corollary 5.3 of [F2], the random variable Tn,α has mean 0, variance 1, and
third moment α −1√
α (n
2) .
There is no need to write out a proof of Theorem 3.1, which uses exactly
the same logic as that of Theorem 2.5. But it is necessary to gi ve analogs of
Lemmas 2.1, 2.2, 2.3, and 2.4, and we do that. The concentrati on inequality
needed for Xn,α is Lemma 6.6 of [F2] and can be used to give another proof
of some results in this section.
There is an α -analog of Kerov’s growth process (due to Kerov [K4]) giving
a sequence of partitions ( λ(1), · · · , λ (n)) with λ(j) distributed according to
the Jackα measure on partitions of size j; see [F3] for details. Moreover from
the deﬁnition of Tn,α , it follows that
Tn,α = 1√
α
( n
2
) (X1,α + · · · + Xn,α ).
Here X1,α = 0 and if j ≥ 2 then Xj,α = cα (x) where x is the box added to
λ(j − 1) to obtain λ(j) and the “ α -content” cα (x) of a box x is deﬁned to
be α (column number of x-1) - (row number of x-1).
Lemma 3.2 is an analog of Lemma 2.1 and is generalized in [F3] t o arbi-
trary spherical functions of the Gelfand pair ( S2n, H 2n).
Lemma 3.2. ([F3])
(1) E(Xj,α |λ(j − 1)) = 0 for 2 ≤ j ≤ n and all partitions λ(j − 1).
(2) E(Xj,α |Tn,α ) = (j−1)√α√
(n
2) Tn,α for all 1 ≤ j ≤ n.
(3) E(X 2
j,α ) = α (j − 1).
(4) E(T 2
n,α ) = 1 .
Lemma 3.3 is the α version of Lemma 2.2.
Lemma 3.3. Let λ(j − 1) be a partition of size j − 1 ≥ 1.
(1) ([K4]) E(X 2
j,α |λ(j − 1)) = α (j − 1).
(2) ([La])
E(X 4
j,α |λ(j − 1)) = α 2
( j
2
)
+ α (α − 1)2(j − 1) + 3α
∑
x∈λ (j−1)
cα (x)2
+3α (α − 1)
∑
x∈λ (j−1)
cα (x).
Lemma 3.4 is the α version of Lemma 2.3. The proof is combinatorial, as
opposed to the algebraic argument given for Lemma 2.3.
Lemma 3.4. Consider the Jack α measure on partitions of size n.
(1) If m ≥ 1 is an integer then
E
( ∏
x∈λ
(m + cα (x))
)
= mn.
12
(2) Let er,α (λ) denote the rth elementary symmetric function of the α -
contents of the boxes of λ. Then E(er,α (λ)) = 0 for 1 ≤ r ≤ n.
Proof. It suﬃces to prove the ﬁrst assertion since the second assert ion follows
from the ﬁrst by taking the coeﬃcient of mn−r on both sides. Page 324 of
[Mac] proves the identity
∑
λ
bλ (q, t )Pλ (y; q, t )Pλ (z; q, t ) = e
∑
n≥1( 1
n
1−tn
1−qn pn(y)pn(z))
where the sum is over all λ of all sizes, Pλ (y; q, t ) denotes a Macdonald
symmetric function, pn(y) = ∑
i yn
i denotes the nth power sum symmetric
function, and bλ (q, t ) is a number to be discussed more below. We apply the
homomorphism of the ring of symmetric functions determined by pr(y) ↦→
mur, pr(z) ↦→l1−r for all r ≥ 1 where m, l are positive integers; this is
possible since the pr’s are algebraically independent. Then we take the limit
q = tα , t ↦→1 in which Macdonald polynomials become Jack polynomials.
With these substitutions, consider the left hand side of the identity. By
pages 380 and 381 of [Mac],
bλ (q, t ) ↦→
∏
x∈λ
αa (x) + l(x) + 1
αa (x) + l(x) + α
Pλ (y; q, t ) ↦→u|λ |∏
x∈λ
m + cα (x)
αa (x) + l(x) + 1
Pλ (z; q, t ) ↦→ 1
l|λ |
∏
x∈λ
l + cα (x)
αa (x) + l(x) + 1 .
Letting l → ∞ , one sees that the coeﬃcient of un in the left-hand side of
the identity is 1
α nn! E
( ∏
x∈λ (m + cα (x))
)
.
Consider the right hand side of the identity with these subst itutions. One
obtains e
∑
n≥1( mun
nαl n−1 ). Letting l → ∞ , one obtains e
mu
α , and taking the
coeﬃcient of un gives mn
α nn! . Comparing with the previous paragraph proves
the ﬁrst assertion of the lemma. □
Finally, we give the analog of Lemma 2.4.
Lemma 3.5. Suppose that n ≥ 3. There is a constant Dα such that
(1) E(|Xn,α |3) ≤ Dα n3/ 2.
(2) E(|Tn−1,α ||Xn,α |3) ≤ Dα n3/ 2.
Proof. The proof method is the same as that of Lemma 2.4, using the
Cauchy-Schwarz inequality in the ﬁrst part and the conditio nal Cauchy-
Schwarz inequality in the second part. One uses that E(X 2
n,α |λ(n − 1)) =
13
α (n − 1) for all λ(n − 1) (part 1 of Lemma 3.3). Also one needs that
E(X 4
n,α ) = α 2
( n
2
)
+ α (α − 1)2(n − 1) + 3α E

 ∑
x∈λ (n−1)
cα (x)2


= α 2
( n
2
)
+ 3α 2
( n − 1
2
)
+ α (α − 1)2(n − 1).
The ﬁrst equality used part 2 of Lemma 3.3 and the fact that E(Tn−1,α ) =
0. The second equality used part 4 of Lemma 3.2 and Lemma 3.4 wi th
r = 2. □
