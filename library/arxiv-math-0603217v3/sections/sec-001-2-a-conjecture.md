---
doc_id: arxiv-math-0603217v3
doc_title: "K; exp(2π √−1) would determine the simplicial volume of the knot complement S3 \ K. In [15]"
section_id: sec-001-2-a-conjecture
section_title: "A conjecture"
section_number: 2
pages: 1-3
source_pdf: 0603217v3.pdf
source_sha256: d7375d4fee00dd98
doc_brief: "A VERSION OF THE VOLUME CONJECTURE HITOSHI MURAKAMI — W e propose a version of the volume conjecture that would rela te a certain limit of the colored Jones polynomials of a knot to th e volume"
---
Let K be a knot in S3. Denote by JN (K; q) the colored Jones polynomial associ-
ated to the N -dimensional irreducible representation of the Lie algebra sl(2, C) [9].
We normalize it so that J2(K; q) is the Jones polynomial [5] and that JN (U ; q) = 1,
where U is the unknot.
We propose the following conjecture as a version of the volume conj ecture.
Date: July 16, 2018.
2000 Mathematics Subject Classiﬁcation. Primary 57M27 57M25 57M50.
Key words and phrases. colored Jones polynomial, volume conjecture, A-polynomia l, Alexan-
der polynomial, torus knot, ﬁgure-eight knot.
This research is partially supported by Grant-in-Aid for Sc ientiﬁc Research (B) (15340019).
1
2 HITOSHI MURAKAMI
Conjecture 2.1 (Parameterized Volume Conjecture). There exists an open subset
OK of C such that for any u ∈ O K the following limit exists:
(2.1) lim
N →∞
log JN
(
K; exp
((
u + 2π √−1
)
/N
))
N .
Moreover the function of u
(2.2) H(K; u) :=
(
u + 2π
√
−1
)
lim
N →∞
log JN
(
E; exp
((
u + 2π √−1
)
/N
))
N
is analytic on OK. If we put
vK(u) := 2 d H(K; u)
d u − 2π
√
−1,
then the following formula holds:
(2.3) V (K; u) = Im
(
H(K; u)
)
− π Re(u) − 1
2 Re(u) Im
(
vK(u)
)
,
where V (K; u) is the volume function corresponding to the representation from
π1(S3 \ K) to SL(2; C) sending the meridian and the longitude to the elements the
ratios of whose eigenvalues are exp(u) and exp
(
vK(u)
)
respectively [1, § 4.5].
Remark 2.2. If u is parameterized by a real number t, then V
(
K; u(t)
)
satisﬁes the
following diﬀerential equation from Schl¨ aﬂi’s formula:
(2.4) d V
(
K; u(t)
)
d t
= − 1
2
(
Re
(
u(t)
)d Im
(
vK
(
u(t)
))
d t − Re
(
vK
(
u(t)
))d Im
(
u(t)
)
d t
)
.
See [16, § 5] and [1, § 4.5]. Note that we use the same convention for the merid-
ian/longitude pair as in [16], which is diﬀerent from that in [1] and [4]. Note also
that the right hand side of the equation in the last line of Page 62 of [1 ] should be
multiplied by four (see [4, (5.6)]).
Remark 2.3. If there exist coprime integers p and q satisfying pu+qvK(u) = 2 π √
−1,
then u would deﬁne the ( p, q )-Dehn surgery along K [17]. If this is a hyperbolic
manifold, V (K; u) is its hyperbolic volume.
Remark 2.4. The open set OK may not contain 0. Therefore Conjecture 2.1 is
not a generalization of the volume conjecture. (Recall that the volume conjecture
[6, 14] states that when u = 0, then the limit (2.1) gives the simplicial volume of
the knot complement.) In fact the case where K is a torus knot, the limit (2.1) is
not continuous at 0 [7, 12]. See also [3, Proposition B.2].
Remark 2.5. S. Garoufalidis and T. Le proved that if u is close enough to −2π √
−1,
then JN
(
K; exp
(
(u + 2π √−1)/N
))
converges to 1 / ∆( K; exp(u + 2π √−1)
)
, where
∆( K; t) is the Alexander polynomial of K [2]. (See also [11] for the ﬁgure-eight
knot.) In this case the right hand side of (2.1) vanishes and so we hav e H(K; u) = 0
and vK(u) = −2π √−1. Therefore from (2.3) the volume function V (K; u) van-
ishes. This corresponds to the case where u deﬁnes an abelian representation,
whose volume function is zero. See [3, Appendix B]. So we exclude such a case in
Conjecture 2.1.
Note that the conjecture above is proved for the ﬁgure-eight kn ot by Yokota and
the author [15]. In fact we proved [15, Corollary 2.4] that for the ﬁ gure-eight knot
E
V (E; u) = Im
(
H(E; u)
)
− π Re(u) − 1
4 Im
(
u vE(u)
)
− π
2 length(γ),
A VERSION OF THE VOLUME CONJECTURE 3
where length( γ) is the length of the geodisic γ added to complete the incom-
plete hyperbolic structure of S3 \ E corresponding to u. But since length( γ) =
− Im
(
u vE(u)
)
/ (2π ) from [16, (34)], we have
V (E; u) = Im
(
H(E; u)
)
− π Re(u) − 1
4 Im
(
u vE(u)
)
+ 1
4 Im
(
u vE(u)
)
= Im
(
H(E; u)
)
− π Re(u) − 1
2 Re(u) Im
(
vE(u)
)
as required.
See also [13, (4.1)]. (The sign of π Re u in [13, (4.1)] should be negative because
the author used a wrong deﬁnition of the function H in the old version of [15].)
Note also that Gukov uses a diﬀerent polarization in his generalization of the
volume conjecture [4, (5.12)]. It agrees with Conjecture 2.1 when R e(u) = 0. The
diﬀerence for Re( u) ⁄= 0 can be explained by a choice of polarization. Details will
be described in a forthcoming paper.
