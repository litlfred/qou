---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-001-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 4-6
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Preliminaries
In this section, we review deﬁnitions and basic properties of the notation used in this
paper.
2.1
Integral presentation of (q)n
In this section, we review the integral expression of q-factorials (q)n and their basic prop-
erties.
Let N be an integer ≥2. We put q = exp(2π√−1/N), and put
(x)n = (1 −x)(1 −x2) · · · (1 −xn)
for n ≥0. It is known [18] (see also [20]) that for any n, m with n ≤m,
(q)n(q)N−n−1 = N,
(4)
∑
n≤k≤m
1
(q)m−k(q)k−n
= 1.
(5)
Following Faddeev [5], we deﬁne a holomorphic function φ(t) on {t ∈C | 0 < Re t < 1}
by
φ(t) =
∫∞
−∞
e(2t−1)xdx
4x sinh x sinh(x/N) ,
noting that this integrand has poles at nπ√−1 (n ∈Z), where, to avoid the pole at 0, we
choose the following contour of the integral,
γ = (−∞, −1 ] ∪
{
z ∈C

 |z| = 1, Im z ≥0
}
∪[ 1, ∞).
It is known [7, 31] that
(q)n = exp
(
φ
( 1
2N
)
−φ
(2n + 1
2N
))
,
(q)n = exp
(
φ
(
1 −2n + 1
2N
)
−φ
(
1 −1
2N
))
.
(6)
4
We put ℏ= 2π√−1/N, and put
Φd(z) = Li2
(
z
)
+
∑
1≤k≤d
ℏ2kc2k ·
(
z d
dz
)2k−2
z
1 −z ,
where we deﬁne c2k by
t/2
sinh(t/2) =
∑
k≥0
c2k t2k.
Then, it is known [7, 31] (see also [20]) that, for any d ≥0,
φ(t) =
N
2π√−1 Φd(e2π√−1 t) + O(ℏ2d+1),
(7)
φ(k)(t) =
N
2π√−1
( d
dt
)kΦd(e2π√−1 t) + O(ℏ2d+1),
(8)
for each k > 0. More precisely, as for the convergence of
1
N φ(t) as N →∞, we recall the
following proposition.
Proposition 2.1 (See [20]). We ﬁx any suﬃciently small δ > 0 and any M > 0. Let d
be any non-negative integer. Then, in the domain
{
t ∈C

 δ ≤Re t ≤1 −δ,
|Im t| ≤M
}
,
(9)
φ(t) is presented by
φ(t) =
N
2π√−1 Li2(e2π√−1 t) + O
( 1
N
)
,
where O(1/N) means the error term whose absolute value is bounded by C/N for some
C > 0, which is independent of t (but possibly dependent on δ). In particular,
1
N φ(t)
uniformly converges to
1
2π√−1Li2(e2π√−1 t) in the domain (9).
As for properties of φ(t), it is a consequence of (4) and (6) (see [20]) that, for any t ∈C
with 0 < Re t < 1,
φ(t) + φ(1 −t) = 2π
√
−1
(
−N
2
(
t2 −t + 1
6
)
+
1
24N
)
.
(10)
Further, the following formulas are known (due to Kashaev, see [20]),
φ
( 1
2N
)
=
N
2π√−1
π2
6 + 1
2 log N + π√−1
4
−π√−1
12N ,
φ
(
1 −1
2N
)
=
N
2π√−1
π2
6 −1
2 log N + π√−1
4
−π√−1
12N .
(11)
5
