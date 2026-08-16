---
doc_id: arxiv-math-0603217v3
doc_title: "K; exp(2π √−1) would determine the simplicial volume of the knot complement S3 \ K. In [15]"
section_id: sec-002-3-proof
section_title: "Proof"
section_number: 3
pages: 3-4
source_pdf: 0603217v3.pdf
source_sha256: d7375d4fee00dd98
doc_brief: "A VERSION OF THE VOLUME CONJECTURE HITOSHI MURAKAMI — W e propose a version of the volume conjecture that would rela te a certain limit of the colored Jones polynomials of a knot to th e volume"
---
In this section we prove Conjecture 2.1 for torus knots. (To be ho nest, (2.3) is
proved only up to a constant, that is, we prove (2.4) instead.)
Let T (a, b ) be the torus knot of type ( a, b ), where a and b are coprime integers
with a > 1 and b > 1. Then the author proved in [12, Theorem 1.1] the following
theorem.
Theorem 3.1 ([12]). Suppose that |r| > 1/ (ab), Re r > 0 and Im r > 0, then
lim
N →∞
log JN
(
T (a, b ); exp(2πr √
−1/N )
)
N =
(
1 − 1
2abr − abr
2
)
π
√
−1.
Therefore the functions H
(
T (p, q ); u
)
and vT (a,b )(u) in Conjecture 2.1 are deﬁned
as follows:
H
(
T (p, q ); u
)
= (u + 2π
√
−1)

1 − 1
2ab
(
1 + u
2π √ − 1
) −
ab
(
1 + u
2π √ − 1
)
2

 π
√
−1
= −(ab(u + 2π √−1) − 2π √−1)2
4ab
and
vT (a,b )(u) = 2 d H
(
T (a, b ); u
)
d u − 2π
√
−1 = −ab(u + 2π
√
−1)
for u with |u + 2π √−1| > 2π/ (ab), Re( u) < 0 and Im( u) > −2π .
So the volume function V
(
T (a, b ); u
)
is
V
(
T (a, b ); u
)
= Im
(
H(T (a, b ); u
)
− π Re(u) − 1
2 Re(u) Im(vT (a,b )(u))
= − 1
4 ab Im(u2) − abπ Re(u) + π Re(u)
− π Re(u) − 1
2 Re(u)(−ab Im(u) − 2abπ )
= 0.
On the other hand the right hand side of (2.4) equals
− 1
2
(
Re
(
u(t)
)
(−ab) d Im
(
u(t)
)
d t + ab Re
(
u(t)
)d Im
(
u(t)
)
d t
)
= 0,
4 HITOSHI MURAKAMI
which proves (2.4).
This conﬁrms Conjecture 2.1 for the torus knot T (a, b ).
Remark 3.2. The volume function for a torus knot would be zero. See [3, Appen-
dix B].
Remark 3.3. Note that the pair
(
u, v T (a,b )(u)
)
satisﬁes the equality:
(−1) × u +
(−1
ab
)
× vT (a,b )(u) = 2 π
√
−1.
So the corresponding geometric object would be the generalized De hn surgery along
the torus knot T (a, b ) with invariant
(
1, 1/ (ab)
)
, or the ab-Dehn surgery with cone-
angle 2 abπ [17, Chapter 4, § 4.5] (see also Remark 2.3). It would be interesting
that the ab-Dehn surgery along the torus knot T (a, b ) is reducible [10].
