---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-5
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Introduction
In [16, 17] Kashaev deﬁned the Kashaev invariant ⟨L ⟩N ∈C of a link L for N = 2, 3, · · ·
by using the quantum dilogarithm. In [18] he conjectured that, for any hyperbolic link L,
2π · lim
N→∞
log ⟨L ⟩N
N
= vol(S3 −L),
where “vol” denotes the hyperbolic volume, and gave evidence for the conjecture for
the ﬁgure-eight knot, the 52 knot and the 61 knot, by formal calculations. In 1999, H.
Murakami and J. Murakami [24] proved that the Kashaev invariant ⟨L ⟩N of any link L
is equal to the N-colored Jones polynomial JN(L; e2π√−1/N) of L evaluated at e2π√−1/N,
where JN(L; q) denotes the invariant obtained as the quantum invariant of links associated
with the N-dimensional irreducible representation of the quantum group Uq(sl2). Further,
as an extension of Kashaev’s conjecture, they conjectured that, for any knot K,
2π · lim
N→∞
log |JN(K; e2π√−1/N)|
N
= vol(S3 −K),
where “vol” in this formula denotes the simplicial volume (normalized by multiplying
by the hyperbolic volume of the regular ideal tetrahedron). This is called the volume
conjecture. As a complexiﬁcation of the volume conjecture, it is conjectured in [25] that,
for a hyperbolic link L,
2π
√
−1 · lim
N→∞
log JN(L; e2π√−1/N)
N
= cs(S3 −L) +
√
−1 vol(S3 −L)
(1)
for an appropriate choice of a branch of the logarithm, where “cs” denotes the Chern-
Simons invariant. Furthermore, it is conjectured [11] (see also [3, 12, 46]) from the view-
point of the SL(2, C) Chern-Simons theory that the asymptotic expansion of JN(K; e2π√−1/k)
1
of a hyperbolic knot K as N, k →∞ﬁxing u = N/k is given by the following form,
JN(K; e2π√−1/k)
∼
N,k→∞
u=N/k: ﬁxed
eNςN 3/2 ω ·
(
1 +
∞
∑
i=1
κi ·
(2π√−1
N
)i)
(2)
for some scalars ς, ω, κi depending on K and u, though they do not discuss the Jones
polynomial in the Chern-Simons theory in the case of vanishing quantum dimension,
which is discussed in [38]. These conjectures look interesting in the sense that they make
a bridge between quantum topology and hyperbolic geometry, and it suggests the existence
of a future theory between them.
An approach toward a proof of the volume conjecture has been known, which is due to
Kashaev [18], Thurston [35] and Yokota [42]. We brieﬂy review this approach, as follows.
By deﬁnition, the Kashaev invariant ⟨K ⟩N (which we review in Section 2.1) of a knot K
is given by a sum of fractions whose denominators are product of copies of (q)n, where
q = exp(2π√−1/N) and (x)n = (1 −x)(1 −x2) · · · (1 −xn); for example, the Kashaev
invariant ⟨52 ⟩N of the 52 knot is given by
⟨52 ⟩N =
∑
0 ≤i,j
i+j < N
N 3q
(q)i+j(q)N−i−j−1(q)j(q)j(q)i
,
as shown in (7). By the approximation (q)n ∼exp
(
N
2π√−1
(
Li2(1) −Li2(e2πn√−1/N)
))
, we
expect the following approximation,
⟨52 ⟩N ∼
?
N 3q
∑
0 ≤i,j
i+j < N
exp
(
N
2π√−1
ˇV (e2π√−1 i/N, e2π√−1 j/N)
)
,
where we put
ˇV (x, y) = Li2(xy) + Li2
( 1
xy
)
+ Li2(y) −Li2
(1
y
)
−Li2
(1
x
)
−Li2(1).
Further, by formally replacing the sum with an integral putting t = i/N and s = j/N,
we expect that
⟨52 ⟩N ∼
?? N 5q
∫
0 ≤t,s
t+s ≤1
exp
(
N
2π√−1
ˇV (e2π√−1 t, e2π√−1 s)
)
dt ds.
Furthermore, by applying the saddle point method, we expect that the asymptotic behav-
ior might be described by a critical value of ˇV . Yokota [42] showed that a critical value
of such a function ˇV is given by the hyperbolic volume of the knot complement. There
are problems justifying this series of arguments.
The volume conjecture has been rigorously proved for some particular knots and links
such as torus knots [19] (see also [5]1), the ﬁgure-eight knot (by Ekholm, see also [1]2),
1A detailed asymptotic expansion of the colored Jones polynomial for torus knots is given in [5].
2A detailed proof of the volume conjecture for the ﬁgure-eight knot was given in [1] and the term N3/2 in (2) was also
veriﬁed there.
2
Whitehead doubles of (2, p)-torus knots [47], positive iterated torus knots [37], the 52
knot [20], and some links [9, 15, 36, 37, 41, 47]; for details see e.g. [22]. They (except
for the 52 knot) have particular properties; for example, the simplicial volumes of the
complements of torus knots are 0, and a critical point of ˇV for the ﬁgure-eight knot is on
the original contour of the integral. The volume conjecture for them has been proved by
using such particular properties. In particular, the 52 knot is of a general case; the volume
conjecture for the 52 knot has been proved by Kashaev and Yokota [20] by presenting the
above mentioned sum by the residue of a certain integral.
The aim of this paper is to give a presentation of the asymptotic expansion of the
Kashaev invariant ⟨52 ⟩N of the 52 knot rigorously (Theorem 1.1 below). Let y0 be the
unique solution with positive imaginary part of (y −1)3 = y,
y0 = 0.3376410213... + √−1 · 0.5622795120... .
We put
x0 = 1 −1
y0
,
ς =
1
2π√−1
(
Li2(x0y0) + Li2
( 1
x0y0
)
+ Li2(y0) −Li2
( 1
y0
)
−Li2
( 1
x0
)
−π2
6
)
= 0.4501096100... + √−1 · 0.4813049796... ,
ω = eπ√−1/4( y0 −1
2y0 + 1
)1/2 = 0.0901905774... −√−1 · 0.6499757866... .
Then, we have
Theorem 1.1. The asymptotic expansion of the Kashaev invariant ⟨52 ⟩N of the 52 knot
is given by the following form,
⟨52 ⟩N = eNςN 3/2 ω ·
(
1 +
d
∑
i=1
κi ·
(2π√−1
N
)i + O
(
1
N d+1
))
,
for any d, where κi is some constant given by a polynomial in y0 with rational coeﬃcients;
in particular, κ1 is given by
κ1 =
1
(2y0 + 1)3
(37
4 y2
0 −31
6 y0 + 35
8
)
+ 1 =
1
12696(1650y2
0 −3498y0 + 2197) + 1
= 1.0537470859... −√−1 · 0.1055728779... .
We can numerically observe that the limit of q−1⟨52 ⟩N e−N ςN −3/2 tends to the above
mentioned value of ω.
N
q−1⟨52 ⟩N e−N ς N −3/2
200
0.0915851738... −√−1 · 0.6519891312...
500
0.0907489101... −√−1 · 0.6507787459...
1000
0.0904698237... −√−1 · 0.6503768725...
3
Further, we can numerically observe that the limit of (⟨52 ⟩N(eN ςN 3/2ω)−1−1)N/(2π√−1)
tends to the above mentioned value of κ1.
N
(⟨52 ⟩N(eN ςN 3/2ω)−1 −1)N/(2π√−1)
200
1.0567234007... −√−1 · 0.0885918466...
500
1.0549811019... −√−1 · 0.0987904427...
1000
1.0543713307... −√−1 · 0.1021833710...
As the conjecture (2) suggests, ω and κi’s of (2) are expected to be invariants of K
for any hyperbolic knot K. We have computed ω and κ1 for the 52 knot in this paper.
It is conjectured that 2√−1 ω2 of a hyperbolic knot is equal to the twisted Reidemeister
torsion associated with the action on sl2 of the holonomy representation of the hyperbolic
structure; see Remark 1.4 below. We discuss about it for some knots in [28].
We give a proof of the theorem in Section 5 by justifying the above mentioned approach.
An outline of the proof is as follows. We rewrite the sum (7) by an integral by the Poisson
summation formula. When we apply the Poisson summation formula, the right-hand side
of the Poisson summation formula consists of inﬁnitely many summands, and we show
that we can ignore them all except for the one at 0 in the sense that they are of suﬃciently
small order at N →∞(Proposition 4.6 and Lemma 5.8). Further, by the saddle point
method (Proposition 3.5), we calculate the asymptotic expansion of the integral, and
obtain the presentation of the theorem.
By the method of this paper, the asymptotic behavior of the Kashaev invariant is
discussed for the hyperbolic knots with up to 7 crossings in [27, 26] and for some hyperbolic
knots with 8 crossings in [34].
Remark 1.2. The author has written the ﬁrst version of this paper in August 2011. In
February 2012, [2] was uploaded in the arXiv, in which Dimofte and Garoufalidis deﬁne a
formal power series from an ideal tetrahedral decomposition of a knot complement, which
is expected to be equal to the asymptotic expansion of the Kashaev invariant of the knot.
Remark 1.3. The right-hand side of (1) is equal to 2π√−1 ς, and it is called the complex
volume. It is known, see e.g. [45], that the complex volume can be expressed by a critical
value of the potential function. It is also known, see e.g. [10], that the complex volume
can be regarded as the SL(2, C) Chern-Simons invariant.
Remark 1.4. The normalization of the above mentioned Reidemeister torsion is the
cohomological Reidemeister torsion associated with the meridian used in [23]. We note
that the twisted Reidemeister torsion in [4] is the twisted Reidemeister torsion associated
with the longitude, and it can be changed to the twisted Reidemeister torsion associated
with the meridian by [29, Th´eor`eme 4.1] as mentioned in [23].
The paper is organized as follows. In Section 2, we review deﬁnitions and basic proper-
ties of the notation used in this paper. In Section 3, we calculate the asymptotic expansion
of Gaussian integrals by the saddle point method, and show Proposition 3.5. In Section
4, we calculate the sum corresponding to the integrals of Section 3 by the Poisson sum-
mation formula, and show Proposition 4.6. In Section 5, we give a proof of Theorem 1.1
4
by using the Poisson summation formula (Proposition 4.6) and the saddle point method
(Proposition 3.5).

The author would like to thank Yoshiyuki Yokota for many helpful comments on the
volume conjecture and the calculation of the Kashaev invariant, and Takashi Kumagai
for many helpful comments on the calculation of the saddle point method and the Pois-
son summation formula. The author would also like to thank Tudor Dimofte, Stavros
Garoufalidis, Rinat Kashaev, Hitoshi Murakami, Toshie Takata and Dylan Thurston for
many helpful comments. He would also like to thank the referees for careful reading of
the manuscript.
