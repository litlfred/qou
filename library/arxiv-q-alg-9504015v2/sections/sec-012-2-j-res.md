---
doc_id: arxiv-q-alg-9504015v2
doc_title: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution"
section_id: sec-012-2-j-res
section_title: "J (res)"
section_number: 2
pages: 12-14
source_pdf: 9504015v2.pdf
source_sha256: ea5588225a393477
doc_brief: "Witten's invariants of rational homology spheres at prime values of K and trivial connection contribution — We establish a relation between the coeﬃcients of asymptotic expan sion of the trivial"
---
α1,...,αN (L; k)
obviously satisﬁes eq. (2.22). Moreover, for some w ∈ Z Z[ˇq],








1
xN K−1
2
∑ ′
−K≤α j ≤K
α j ∈2Z Z+1
(1≤j≤N)
ˇq4∗∑ N
j=1 pjα2
j J (res)
α1,...,αN (L; k) x(N +1) K−1
2 +1








⋄
=
[
x
K+1
2 w
] ⋄
= 0, (2.23)
so that we can neglect the contribution of this term in all further ca lculations.
To estimate the contribution of a polynomial
( ∏ N
j=1 αj
) ∑
m≤ 3
4 n ˜Dm,n(α1, . . . , αN ) xn we
need the following simple lemma:
Lemma 2.1 For p, m ∈ Z Z, m ≥ 0
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpα2
α2m = xmax{0, K−1
2 −m}w, w ∈ Z Z[ˇq]. (2.24)
The lemma needs a proof only for m < K−1
2 . To prove that an element u ∈ Z Z[ˇq] is divisible
by xn, n ≤ K − 1 one may present it as an integer coeﬃcient polynomial of x and check
that the coeﬃcients in front of all xn′
, n′ < n are divisible by K. We substitute ˇq = x + 1 in
eq. (2.24) and express the powers of ˇ q in terms of “binomial” polynomials
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpα2
α2m =
∑
n≥0
∑ ′
−K≤α ≤K
α ∈2Z Z+1
Pn(pα2)α2mxn =
∑
n≥0
∑
0≤m′≤n
∑ ′
−K≤α ≤K
α ∈2Z Z+1
Cn,m′
n! p2m′
α2(m+m′)xn,(2.25)
11
here
α(α − 1) · · ·(α − n + 1) =
∑
m′≤n
Cn,m′αm′
, C n,m′ ∈ Z Z. (2.26)
It is well known in number theory that
∑ ′
−K≤α ≤K
α ∈2Z Z+1
α2m = 0 (mod K) for 0 ≤ m < K − 2. (2.27)
Therefore the numerator of the contribution of a term
Cn,m ′
n! p2m′
α2(m+m′)xn will be divisible
by K for all m + m′ < K−1
2 ≤ K − 2, that is, for all n < K−1
2 − m. The denominator n! is
harmless, because since n < K , it is not divisible by K and can not cancel the factors of K
coming from the sum over α. This proves the lemma.
This lemma can be easily generalized to the “binomial” polynomials (2.13):
Lemma 2.2 For p, p′, m ∈ Z Z, p′ ∈ 2Z Z, m ≥ 0
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇqpα2
Pm
(
α + p′ − 1
2
)
= xmax{0, K−1
2 −[ m
2 ]} w, w ∈ Z Z[ˇq]. (2.28)
The proof is similar to that of the previous lemma. The choice of summa tion range for α
obviates the fact that odd powers of α in Pm
(
α+p′−1
2
)
can be ignored. The numerators of
the contributions of even powers of α are divisible by K. The coeﬃcients of Pm have a
denominator m!, but we may assume that m < K − 1 (otherwise eq. (2.28) is obvious) so
that the denominator does not cancel the factors of K.
Let ¯m(n) be the maximum value of m appearing in the l.h.s. of eq. (2.12). Then for every
coeﬃcient C (n)
m1,...,mN from the r.h.s. of that equation
m1 + · · · + mN ≤ ¯m(n). (2.29)
Therefore we can combine eqs. (2.12) and (2.28) into the following es timate of the contribu-
tion of polynomials ˜Dm,n to the sum (2.22):
∑ ′
−K≤α ≤K
α ∈2Z Z+1
ˇq4∗∑ N
j=1 pj α2
j


N∏
j=1
(
αj + p∗
j
)

 ∑
m≤ 3
4 n
˜Dm,n(α1 + p∗
1, . . . , αN + p∗
N ) xn
= xN K−1
2 +n− ¯m(n) w, w ∈ Z Z[ˇq]. (2.30)
12
Since ¯m(n) ≤ 3
4 n ≤ n, this estimate is enough to prove eq. (2.22) and also the Theorem 1.1 .
Note that the proof required only a weaker bound m ≤ n for ˜Dm,n rather than a stronger
bound m ≤ 3
4 n of [18]. However the bound m ≤ 3
4n is necessary to prove that only a ﬁnite
number of polynomials ˜Dm,n contribute to the coeﬃcients of xn′
, n′ ≤ K−1
2 in the expansion
of [ Z ′(M; k)]⋄. Indeed, since ¯ m(n) ≤ 3
4 n, then n − ¯m(n) ≥ 1
4n and eq. (2.30) suggests that
we may limit our attention to only those polynomials (2.15) for which
n ≤ 2(K − 1). (2.31)
