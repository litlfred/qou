---
doc_id: arxiv-math-0603217v3
doc_title: "K; exp(2π √−1) would determine the simplicial volume of the knot complement S3 \ K. In [15]"
section_id: sec-003-4-comments
section_title: "Comments"
section_number: 4
pages: 4-5
source_pdf: 0603217v3.pdf
source_sha256: d7375d4fee00dd98
doc_brief: "A VERSION OF THE VOLUME CONJECTURE HITOSHI MURAKAMI — W e propose a version of the volume conjecture that would rela te a certain limit of the colored Jones polynomials of a knot to th e volume"
---
In [4, (5.29)], Gukov proposed the following conjecture.
Conjecture 4.1. [4] Let K be a knot in the three-sphere. For a ∈ C \ Q, deﬁne
the function l(a) as follows:
(4.1) l(a) := − d
d a
{
a lim
N →∞
log JN
(
K; exp(2πa √−1/N )
)
N
}
.
Then the pair
(
exp
(
l(a)
)
, − exp(πa √−1)
)
is a zero of the A-polynomial of K in-
troduced in [1].
Using our parameterization u := 2πa √−1 − 2π √−1, we have l(a) = −vK(u)/ 2 −
π √−1. Then Conjecture 4.1 states that the pair
(
− exp
(
−vK(u)/ 2
)
, exp(u/ 2)
)
is
a zero of the A-polynomial.
In the case of the ﬁgure-eight knot, we can prove this. For the to rus knot T (a, b ),
either
(
− exp
(
−vK(u)/ 2
)
, exp(u/ 2)
)
or
(
− exp
(
vK(u)/ 2
)
, exp(u/ 2)
)
is a zero of the
A-polynomial. (See, for example, [18, Example 4.1] for the A-polynomials of torus
knots.) This would depend on how we choose a meridian/longitude pair.
Remark 4.2. If |a| is small enough the right hand side of (4.1) vanishes [3]. This
corresponds to the ( l − 1)-factor of the A-polynomial [1, 2.5]. See Remark 2.5.
The function H(K; u) deﬁned by (2.2) is a kind of potential function introduced
in [16, Theorem 3]. (To be more precise, Φ( u) = 4 H(K; u) − 4πu √
−1, where
Φ( u) is Neumann–Zagier’s potential function.) The following observation indicates
a relation between H(K; u) and the Alexander polynomial.
Observation 4.3. Let ∆( K; t) be the Alexander polynomial of a knot K. For the
ﬁgure-eight knot and torus knots, the equations H(K; u) = 0 and ∆
(
K; exp(u)
)
= 0
share a root. Note that here we regard H(K; u) as a function deﬁned on the whole
complex plane.
Proof. First note that ∆( E; t) = −t2 + 3t − 1 and ∆
(
T (a, b ); t
)
=
(
tab − 1
)
(t −
1)/ (ta − 1)
(
tb − 1
)
.
For the ﬁgure-eight knot E, we have from [15]
H(E; u) = Li 2(y− 1 exp(−u)) − Li2(y exp(−u)) +
(
log(−y) + π
√
−1
)
u,
where y is a solution to the equation y + y− 1 = 2 cosh( u) − 1. Put u :=
± arccosh(3/ 2). Then y = 1 and so H(E; u) vanishes. Note that we take the
branch of log so that log( −1) = −π √−1. It is easy to see that exp( ± arccosh(3/ 2))
are the roots of ∆( E; exp(u)) = 0.
For the torus knot T (a, b ) the zero of H
(
T (a, b ); u
)
is 2 π √−1/ (ab) − 2π √−1. It
is also a zero of ∆( T (a, b ); exp(u)). □
A VERSION OF THE VOLUME CONJECTURE 5
