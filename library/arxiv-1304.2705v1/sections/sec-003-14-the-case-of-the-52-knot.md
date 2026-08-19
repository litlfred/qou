---
doc_id: arxiv-1304.2705v1
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-003-14-the-case-of-the-52-knot
section_title: "The case of the 52 knot"
section_number: 1.4
pages: 5-6
source_pdf: 1304.2705v1.pdf
source_sha256: cb07e66e418e11f2
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
---
F (q, x) = F2,3(q, x) =
∞∑
m=0
tm(q)xm, ~F (q,~x) = F1,3(q,~x) =
∞∑
m=0
Tm(q)~xm
where
tm(q) = qm(m+1)
(q)3
m
, T n(q) = ( −1)n q
1
2 n(n+1)
(q)3
n
= tn(q−1) .
Let
Rm,n(q, ˜q) = − b2
2
(
1 + 4m + 4m2 − 6E(m)
1 (q) − 12mE(m)
1 (q) + 9E(m)2
1 (q) − 3E(m)
2 (q)
)
− 1
2πi + 1
2
(
1 + 2m − 3E(m)
1 (q)
)(
1 + 2n − 6E(n)
1 (˜q)
)
+ b−2
2
(
−n − n2 − 6E(0)
2 (˜q) + 3E(n)
1 (˜q) + 6nE(n)
1 (˜q) − 9E(n)2
1 (˜q) + 3E(n)
2 (˜q)
)
,
where E(m)
l (q) are deﬁned in Equation ( 29a). For k = 1, . . . ,4 let
(18) gk(q) =
∞∑
m=0
pk(m)tm(q), G k(˜q) =
∞∑
n=0
Pk(n)Tn(˜q) ,
where
p1,m(q) = 1 + 4 m + 4m2 − 6E(m)
1 (q) − 12mE(m)
1 (q) + 9E(m)2
1 (q) − 3E(m)
2 (q)(19a)
p2,m(q) = 1 + 2 m − 3E(m)
1 (q)(19b)
p3,m(q) = 1(19c)
6 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
and
P1,m(q) = 1(20a)
P2,m(q) = 1 + 2 n − 6E(n)
1 (˜q)(20b)
P3,m(q) = −n − n2 − 6E(0)
2 (˜q) + 3E(n)
1 (˜q) + 6nE(n)
1 (˜q) − 9E(n)2
1 (˜q) + 3E(n)
2 (˜q) .(20c)
Corollary 1.8. (a) We have:
I2,3(q) = −e
3πi
4
( q
˜q
) 1
8 ∞∑
m,n=0
Rm,n(q, ˜q)tm(q)Tn(˜q)
(21)
= −e
3πi
4
( q
˜q
) 1
8
(
−b2
2 g1(q)G1(˜q) − 1
2πi g3(q)G1(˜q) + 1
2g2(q)G2(˜q) + b−2
2 g3(q)G3(˜q)
)
(b) F and ~F satisfy the linear q-diﬀerence equations
F (q, q3x) − (3 − q2x)F (q, q2x) + 3F (q, qx) − F (q, x) = 0
~F (q, q3x) − 3~F (q, q2x) + (3 − q2x)~F (q, qx) − ~F (q, x) = 0 .
Remark 1.9. A computation gives that P (A, B) = P (B − A, B) for ( A, B) = (1 , 2) and
(A, B) = (2 , 3) corresponding to the invariants of the 4 1 and 5 2 knots. In all other cases that
we tried, we found that P (A, B) is not equal to P (B − A, B).
