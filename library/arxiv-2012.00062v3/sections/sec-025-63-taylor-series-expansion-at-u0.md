---
doc_id: arxiv-2012.00062v3
doc_title: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY"
section_id: sec-025-63-taylor-series-expansion-at-u0
section_title: "Taylor series expansion at u=0"
section_number: 6.3
pages: 54-56
source_pdf: 2012.00062v3.pdf
source_sha256: 2aacb7fa43f5e0da
toc_source: outline
doc_brief: "PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY — The partition function of complex Chern-Simons theory on a 3-manifold with torus boundary reduces to a ﬁnite dimensional"
---
the descendant holomorphic blocks and descendant state-integral of the 52 knots at u = 0.
Using the deﬁnition of H(x, y, z; q) and (161a)–(161b), we ﬁnd
Am(eu; q) = (q; q)2
∞
∞
X
n=0
qn(n+1)+nm
(q; q)3
n
φn(u)φn(−u)
= (q; q)2
∞

α(m)
0
(q) + u2α(m)
2
(q) + O(u3)

(284)
where
α(m)
0
(q) = H+
0,m(q),
(285)
α(m)
2
(q) =
∞
X
n=0
qn(n+1)+nm
(q; q)3
n
(−E(n)
2 (q)),
(286)
and
Cm(e−u; q) = Bm(eu; q)
= (1 −e−u)−2(q; q)−2
∞φ0(u)−2φ0(−u)−2
∞
X
n=0
qn(n+1)+nm
(q; q)3
n
φn(u)φn(2u)e(m+2n)u
= u−2(q; q)−2
∞

β(m)
0
(q) + uβ(m)
1
(q) + u2β(m)
2
(q) + O(u3)

(287)
where the coeﬃcients satisfy
β(m)
0
(q) = H+
0,m(q),
(288)
β(m)
1
(q) = H+
1,m(q),
(289)
β(m)
2
(q) = 1
2H+
2,m(q) + α(m)
2
(q).
(290)
Similarly, using the deﬁnition of H(x, y, z; q−1), we ﬁnd
Am(eu; q−1) =
1
(1 −eu)(1 −e−u)(q; q)2
∞
∞
X
n=0
(−1)nq
1
2 n(n+1)−nm
(q; q)3
n
eφn(u)eφn(−u)
= −u−2(q; q)−2
∞

eα(m)
0
(q) + u2eα(m)
2
(q) + O(u3)

(291)
where
eα(m)
0
(q) = H−
0,−m(q),
(292)
eα(m)
2
(q) =
∞
X
n=0
(−1)nq
1
2 n(n+1)−nm
(q; q)3
n

−1
12 + 2E(0)
2 (q) −E(n)
2 (q)

,
(293)
PEACOCK PATTERNS AND RESURGENCE IN COMPLEX CHERN-SIMONS THEORY
55
and
Cm(e−u; q−1) = Bm(eu; q−1)
= (1 −eu)(1 −e2u)−1(q; q)2
∞φ0(u)2φ0(−u)2
∞
X
n=0
(−1)nq
1
2 n(n+1)−nm
(q; q)3
n
eφn(u)eφn(2u)e(2n+m)u
= 1
2(q; q)2
∞

eβ(m)
0
(q) + ueβ(m)
1
(q) + u2eβ(m)
2
(q) + O(u3)

(294)
where the coeﬃcients satisfy
eβ(m)
0
(q) = H−
0,−m(q),
(295)
eβ(m)
1
(q) = −H−
1,−m(q),
(296)
eβ(m)
2
(q) = 1
2H−
2,−m(q) + eα(m)
2
(q)
(297)
Applying these results to the right hand side of (243), as well as using the trick
1
2πi = −1
12(τE2(q) −τ −1E2(˜q)),
(298)
we ﬁnd the O(1/u2) and O(1/u) contributions from (291) and (294) cancel, and the O(u0)
contributions reproduce (103).
As an application of the above computations, we demonstrate that Theorem 11, especially
(91), (93), as well as the recursion relation (86), can be proved by taking the u = 0 limit of
the analogue identities in Theorem 24.
Using the expansion formulas of holomorphic blocks (284), (287), (291), (294), the Wron-
skians can be expanded as
Wm(eu; q) =
 X
j=0
W +
m,j(q)uj
! 

(q; q)2
∞
0
0
0
u−2(q; q)−2
∞
0
0
0
u−2(q; q)−2
∞

,
(299)
Wm(eu; q−1) =
 X
j=0
W −
m,j(q)uj
! 

−u−2(q; q)−2
∞
0
0
0
1
2(q; q)2
∞
0
0
0
1
2(q; q)2
∞


(300)
where
W +
m,j(q) =



α(m)
j
β(m)
j
(−1)jβ(m)
j
α(m+1)
j
β(m+1)
j
(−1)jβ(m+1)
j
α(m+2)
j
β(m+2)
j
(−1)jβ(m+2)
j


(q),
W −
m,j(q) =



eα(m)
j
eβ(m)
j
(−1)j eβ(m)
j
eα(m+1)
j
eβ(m+1)
j
(−1)j eβ(m+1)
j
eα(m+2)
j
eβ(m+2)
j
(−1)j eβ(m+2)
j


(q).
(301)
Note that α(m)
j
(q) = eα(m)
j
(q) = 0 if j is odd. Taking the determinant of (299), we ﬁnd
det Wm(eu; q) = u−1(q; q)−2
∞det Wm(q) + O(u0)
(302)
which together with the u-expansion of the right hand side of (255) leads to the determinant
identity (91). Furthermore, by substituting (299), (300) into the Wronskian relation (256),
56
STAVROS GAROUFALIDIS, JIE GU, AND MARCOS MARIÑO
we ﬁnd the left hand side reduces to
1
2W−1(q)


0
0
1
0
2
0
1
0
0

W−1(q−1)


0
0
1
0
1
0
1
0
0

+ O(u1),
(303)
which together with the u-expansion of the right hand side, leads in the leading order to
(92) for m = 1. The more general case follows from the identity of m = 1 by applying the
recursion relations (86) on the Wronskians.
Finally, from the expression (285),(288) of the leading order coeﬃcients α(m)
0
(q), β(m)
0
(q),
of Am(eu; q), Bm(eu; q), Cm(eu; q) in the expansion of u, one concludes that the recursion
relation (86) should be the u = 0 limit of the recursion relation (254) in m, and one can
easily check it is indeed the case.
ϕσ1(τ)
ϕσ2(τ)
ϕσ3(τ)
Figure 10. The singularities in the Borel plane for the series ϕσj(u; τ) with
j = 1, 2, 3 of knot 52 where u is close to zero.
