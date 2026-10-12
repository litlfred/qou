---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-145-4b-the-stratification-in-our-setting
section_title: "4B. The stratification in our setting"
section_number: null
pages: 261-263
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
that we use in this paper.
Theorem 4.1. Let κ = Fq, q prime. The result of Theorem A holds if we replace the hypothesis that
for each 1 ≤i ≤2r, the form Fi is di-th power-free and TFi is ﬁnite, by the weaker hypothesis that for
each 1 ≤i ≤2r, the reduction modulo q of the form Fi is (di, q)-admissible, and for each 1 ≤i ≤2r,
deg Fi < q.
Corollary 4.2. Let κ = Fq, q prime. The result of Corollary B holds if we replace the hypothesis that for
each 1 ≤i ≤2r, the form Fi is di-th power-free and TFi is ﬁnite, by the weaker hypothesis that for each
1 ≤i ≤2r, the reduction modulo q of the form Fi is (di, q)-admissible.
In the above corollary, we are able to omit the condition deg Fi < q seen in Theorem 4.1 by possibly
enlarging C′; see (4-9). Through similar considerations, we can remove consideration of the set S, as we
record here:
Corollary 4.3. In addition, given n,r, 1, D in either Corollary B or Corollary 4.2, we may take the set
S = S(n,r, 1, D) to be the empty set, at the expense of replacing C′ = C′(n,r, 1, D) by a possibly
larger constant C′′ = C′′(n,r, 1, D).
Within the Burgess argument, we will consider the sum
X
m (mod q)
χ(F{x}(m)) =
X
m (mod q)
2r
Y
i=1
χi(F(m + x(i)))
in which we have ﬁxed a multiplicative Dirichlet character χ of order 1 modulo a prime q and then set
χi = χ if i is odd and χi = χ if i is even. This is then clearly of the form S(x(1), . . . , x(2r)) as deﬁned
in (4-4), with the choice that all the Fi are equal to our ﬁxed F ∈Fq[x1, . . . , xn] of degree D. For later
reference, we record the following immediate consequence of Theorem 4.1 and Corollary 4.3 (choosing
the subset Mi of κ to be (0, ki] for each 1 ≤i ≤2r).
Theorem 4.4. Let integers n,r, 1, D ≥1 be ﬁxed. Then there exist constants C = C(n,r, D) and
C′′ = C′′(n,r, 1, D) such that the following holds.
1928
Lillian B. Pierce and Junyan Xu
Fix a prime q and let χ be a multiplicative Dirichlet character of order 1 modulo q. Suppose
F ∈Z[x1, . . . , xn] has the property that its reduction modulo q is (1, q)-admissible and deﬁne F{x}(X)
accordingly as in (2-6).
Then for every 1 ≤j ≤n, for every tuple k = (k1, . . . , kn) ∈Zn with
1 ≤k1 ≤k2 ≤· · · ≤kn ≤q,
#

(x(1), . . . , x(2r)) ∈(0, k]2r :

X
m (mod q)
χ(F{x}(m))

 > Cq(n+ j−1)/2

≤C′′∥k∥2r Bn,r( j; k)−1, (4-7)
in which Bn,r( j; k) is deﬁned as in (4-5).
Remark. Note that the trivial upper bound in (4-7) is ∥k∥2r. The fundamental consequence of Theorem 4.4
is that it shows that generically among {x} ∈(0, k]2r, square-root cancellation holds, as soon as r is
sufﬁciently large relative to n. Precisely, as soon as r ≥n, so that the exponent ⌊(r −1)/(n−1)⌋appearing
in Bn,r(1; k) is strictly positive, the number of {x} ∈(0, k]2r such that square-root cancellation is violated
is O(∥k∥2rk−1
1 ), which sufﬁces for our claim, as long as k1 is at least a positive power of ∥k∥.
Also, to aid in understanding the role of the function Bn,r( j; k) in this result, we note that the
bound (4-7) is in the format of (2-11) with the choice R = 2nr and with the R-dimensional box being
(0, k1] × · · · × (0, k1] × · · · × (0, kn] × · · · × (0, kn],
in which each factor (0, ki] appears 2r times. Thus when θ j ≤2r (this holds for j ≤n −1), we only
save factors of k1. In the ﬁnal case j = n when θn = nr, we save some factors of ki for 1 ≤i ≤⌈n/2⌉as
well. This leads to the deﬁnition of Bn,r( j; k). Finally, we remark for later reference that by construction,
under the hypotheses of the theorem, we always have
∥k∥2r Bn,r( j; k)−1 ≥1.
(4-8)
Remark. Conjecturally, one might hope to improve the result of Theorem 4.4 by proving that one can take
larger values for the codimension θ j used to deﬁne the savings factor Bn,r( j; k)−1. (Precise implications
may be found in Section A.2, where we show that even the conjecturally best possible values for the
codimension do not signiﬁcantly change our main result.) For comparison, in the most extreme case, it is
not hard to see that we must have θn ≤nr, and hence certainly must also have θ j ≤nr for all j ≤n. For
recall from Theorem A that Xn is a subscheme of A2nr
κ
such that for all (x(1), . . . , x(2r)) ∈A2nr
κ
\ Xn(κ),
|S(x(1), . . . , x(2r))|≤C(#κ)n−1/2. In fact, Xu’s paper shows the stronger result that for all ﬁnite extensions
k/κ and (x(1), . . . , x(2r)) ∈A2nr
k
\ Xn(k), it holds that |Sk(x(1), . . . , x(2r))| ≤C(#k)n−1/2; here Sk is
deﬁned analogously to S but summing over m ∈kn and with χi replaced by χi(Nk/κ( · )). That is, all
(x(1), . . . , x(2r)) such that |Sk(x(1), . . . , x(2r))| > C(#k)n−1/2 must lie in Xn(k). Then we claim that
dim Xn ≥nr (and consequently θn ≤nr). To see this, we consider any tuple (x(1), . . . , x(2r)) for which
x( j) = x( j+r) for j = 1, . . . ,r. There are (#k)nr such tuples, and each of them has the property that
|Sk(x(1), . . . , x(2r))|=(#k)n. This is >C(#k)n−1/2 if #k is sufﬁciently large (which we can choose it to be).
Burgess bounds for short character sums evaluated at forms
1929
