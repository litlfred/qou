---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-001-11-overview-of-volume-conjectures
section_title: "Overview of volume conjectures"
section_number: 1.1
pages: 1-3
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
---
The volume conjecture of the colored Jones polynomials, discovered by R. Kashaev, H. Murakami and J.
Murakami, suggests that the N-th colored Jones polynomials of a hyperbolic knot evaluated at the N-th
root of unity t = e
2πi
N grow exponentially with exponential growth rate equal to the hyperbolic volume
of the knot complement.
Conjecture 1. [10, 15] Let K be a hyperbolic knot and J′
N(K;t) be the normalized N-th colored Jones
polynomials of K evaluated at t such that J′
N(unknot,t ) = 1 for all N∈ N. We have
lim
N→∞
2π
N log|J′
N(K;e
2πi
N )| = Vol(S3\K),
where Vol(S3\K) is the hyperbolic volume of the knot complement in S3.
Later, H. Murakami and J. Murakami extended the above volume conjecture to non-hyperbolic links
and suggested that the exponential growth rate captures the simplicial volume of the link complement.
Conjecture 2. [15] Let L be a link and J′
⃗N(L;t) be the ⃗N-th normalized colored Jones polynomials of L
evaluated at t, where ⃗N = (N,...,N ). We have
lim
N→∞
2π
N log|J′
⃗N(L;e
2πi
N )| =v3||S3\L||,
where||S3\L|| is the simplicial volume of the link complement.
In 2015, Q. Chen and T. Yang discovered a version of volume conjecture for the Turaev-Viro invariants
at a primitive 2r-th root of unity, where r is odd. The conjecture can be stated as follows.
Conjecture 3. [2] For every hyperbolic 3-manifold M with ﬁnite volume, we have
limr→∞
r odd
2π
r log
(
TVr(M,e
2πi
r )
)
= Vol(M)
It turns out when the 3-manifold is a link complement, the Turaev-Viro invariant is related to the
unnormalized colored Jones polynomials of the link evaluated at certain ( N + 1/2)-th root of unity as
follows.
1
arXiv:1912.10638v2  [math.GT]  24 May 2020
Theorem 1. [5]. Let L be a link in S3 with n components. Then given an odd integer r = 2N + 1≥ 3,
we have
TVr
(
S3\L,e
2πi
r
)
= 2n−1
(2 sin(2π
r )√r
)2 ∑
1≤⃗M≤r−1
2
⏐⏐⏐⏐J⃗M
(
L,e
2πi
N + 1
2
)⏐⏐⏐⏐
2
.
Here,J⃗M(L,t ) is the unnormalized colored Jones polynomials of the link L with
JN(U,t ) = t
N
2 −t−N
2
t
1
2−t− 1
2
for the unknot U and any N∈ N.
Therefore, by studying the asymptotics of the colored Jones polynomials of links at this ( N + 1/2)-th
root of unity, one can relate the volume conjecture of the colored Jones polynomials of a link to the
volume conjecture of the Turaev-Viro invariants of its complement. In particular, in [5], the volume
conjecture for the Turaev-Viro invariants is extended to the complement of non-hyperbolic links and this
generalization is proved for all knots with zero simplicial volume.
Conjecture 4. [5] For every link L in S3, we have
limr→∞
r odd
2π
r log(TVr(S3\L,e
2πi
r )) =v3||S3\L||,
wherev3 is the volume of an ideal regular tetrahedron.
Besides, in [5], R. Detcherry, E. Kalfagianni and T. Yang ask the following question:
Conjecture 5. (Question 1.7 in [5]) Is it true that for any hyperbolic link L in S3, we have
lim
N→∞
2π
N + 1
2
log|J⃗N(L,e
2πi
N + 1
2 )| = Vol(S3\L) ?
The answer is aﬃrmative when L is the ﬁgure eight knot. In fact, for the ﬁgure eight knot we can
say more. In [23], Thomas Au and the author consider the M-th colored Jones polynomials of the ﬁgure
eight knot evaluated at the (N + 1/2)-th root of unity t =e
2πi
N +1/2 . Here we regard M as a sequence in N
and deﬁne the limiting ratio
s = lim
N→∞
M
N + 1/2.
As a direct consequence of Theorem 7 (ii) in [23], we have the following result.
Theorem 2. [23] For the ﬁgure eight knot 41, there exists δ >0 such that for any 1−δ < s≤ 1, we
have
lim
N→∞
2π
N + 1
2
log|JM(41,e
2πi
N + 1
2 )| = Vol
(
S3\41,u = 2πi(1−s)
)
,
where Vol
(
S3\41,u = 2πi(1−s)
)
is the volume of S3\41 equipped with the (possibly incomplete) hyperbolic
structure such that the logarithm of the holonomy of the meridian is given by u = 2πi(1−s).
An important remark is that Theorerm 2 is true for the root of unity t = e
2πi
N +1/2 but false for the
original root t =e
2πi
N 1. As a generalization, we propose the generalized volume conjecture for hyperbolic
links at t =e
2πi
N +1/2 as follows (c.f. Question 4.6 and Theorem 4.8 in [3]).
1 This type of generalized volume conjecture has been studied in several literatures (e.g. [9], [12], [14]). Unfortunately,
in the original setting, i.e. t = e
2πi
N , this generalization fails even for knots (see Section 4 in [3]). Besides, the original
volume conjecture is not true for split links due to the choice of normalization. Even if the normalization problem is ﬁxed,
in [22] R. van der Veen shows that the conjecture is false for the Whitehead chains with more than one belt.
On the other hand, if we consider the root q = e
2πi
N +1/2 rather than the original root, the above problems disappear and
it gives a hope to have a generalized volume conjecture to hyperbolic links. Note that the diﬀerence between these two
roots of unities has also been discussed in [23].
2
Conjecture 6. (Generalized volume conjecture for hyperbolic links) Let L be a hyperbolic link with n
components. Let M1,M 2,...,M n be sequences of positive integers in N. Let si = lim
N→∞
Mi
N + 1/2. Then
there exists δL > 0 such that whenever the limiting ratio si∈ (1−δL, 1], we have
lim
N→∞
2π
N + 1
2
log|JM1,...,Mn(L,e
2πi
N + 1
2 )| = Vol(S3\L,ui = 2πi(1−si)),
where Vol(S3\L,ui = 2πi(1−si)) is the volume of S3\L equipped with the hyperbolic structure such that
the logarithm of the holonomy of the meridian around the i-th component is given by ui = 2πi(1−si).
