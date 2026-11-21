---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-006-21-a-residue-computation
section_title: "A residue computation"
section_number: 2.1
pages: 6-8
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
toc_source: outline
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
residue theorem on a semicircle γR with center 0 and radius R, oriented counterclockwise in
the upper half-plane:
Then, we will take the limit R →∞. To compute the residue of the integrand, we need to
expand Φb(x) near the pole
xm,n = cb + ibm + ib−1n
for natural numbers m and n. Let
φm(x) = (qm+1ex; q)∞
(qm+1; q)∞
(23)
eφn(x) =
(˜q; ˜q)∞
(˜qex; ˜q)∞
(˜q−1; ˜q−1)n
(˜q−1ex; ˜q−1)n
(24)
Lemma 2.1. We have:
(25)
Φb(x + xm,n) = (q; q)∞
(˜q; ˜q)∞
1
(q; q)m
1
(˜q−1; ˜q−1)n
φm(2πbx) eφn(2πb−1x)
1 −e2πb−1x
.
FROM STATE INTEGRALS TO q-SERIES
7
Proof. Equation (1) implies the functional equations
Φb(x + cb + ib)
Φb(x + cb)
=
1
1 −qe2πbx
Φb(x + cb + ib−1)
Φb(x + cb)
=
1
1 −˜q−1e2πb−1x
which give
Φb(x + xm,n) = Φb(x + cb)
1
(qe2πbx; q)m
1
(˜q−1e2πb−1x; ˜q−1)n
Φb(x + cb) =
1
1 −e2πb−1x
(qe2πbx; q)∞
(˜qe2πb−1x; ˜q)∞
.
Thus,
Φb(x + xm,n) = (q; q)∞
(˜q; ˜q)∞
1
(q; q)m
1
(˜q−1; ˜q−1)n
·
1
1 −e2πb−1x
(qe2πbx; q)∞
(q; q)∞
(˜q; ˜q)∞
(˜qe2πb−1x; ˜q)∞
(q; q)m
(qe2πbx; q)m
(˜q−1; ˜q−1)n
(˜q−1e2πb−1x; ˜q−1)n
= (q; q)∞
(˜q; ˜q)∞
1
(q; q)m
1
(˜q−1; ˜q−1)n
·
1
1 −e2πb−1x
(qm+1e2πbx; q)∞
(qm+1; q)∞
(˜q; ˜q)∞
(˜qe2πb−1x; ˜q)∞
(˜q−1; ˜q−1)n
(˜q−1e2πb−1x; ˜q−1)n
The result follows.
□
The decoupling of (m, n) in the quadratic form comes as follows: since A, m, n are integers,
eAπimn = 1 and a computation gives
e−Aπi(x+xn,m)2 = iA
q
˜q
 A
8
tA
m(q)etA
n(˜q)e−Aπix2+2Aπx(b(m+ 1
2 )+b−1(n+ 1
2 ))
where
tA
m(q) = (−1)AmqA m(m+1)
2
,
etA
n(˜q) = (−1)An˜q−A n(n+1)
2
.
The Dedekind function η(τ) = q1/24(q; q)∞(with q = e2πiτ) satisﬁes the modular equation
η(−τ −1) = √−iτη(τ) [And76]. It follows that
(26)
(q; q)∞
(˜q; ˜q)∞
= e
πi
4
 ˜q
q
 1
24
b−1 .
After we set w = x/(2π), the above discussion implies that
(27)
IA,B(b) =
 ˜q
q
 B−3A
24
eπi B+2(A+1)
4
∞
X
m,n=0
(Resw=0FA,B,m,n(w)) tA
m(q)
(q; q)B
m
etA
n(˜q)
(˜q−1; ˜q−1)B
n
,
8
STAVROS GAROUFALIDIS AND RINAT KASHAEV
where
(28)
FA,B,m,n(w) = e
A
4πiw2+Aw(b(m+ 1
2 )+b−1(n+ 1
2 ))
 
φm(bw) eφn(b−1w)
b(1 −eb−1w)
!B
.
2.2. The Taylor series of φm(x) and eφn(x). In this section we express the Taylor series
of φm(x) and eφn(x) in terms of the q-series E(m)
l
(q) and eE(m)
l
(˜q) deﬁned by:
E(m)
l
(q) =
∞
X
s=1
sl−1qs(m+1)
1 −qs
= ⟨δl(xm)⟩
(29a)
eE(n)
l
(˜q) =





−n + E(n)
1 (˜q)
if l = 1
E(n)
l
(˜q)
if l > 1 is odd
2E(0)
l (˜q) −E(n)
l
(˜q)
if l > 1 is even
(29b)
Proposition 2.2. We have:
φm(x) = exp
 
−
∞
X
l=1
1
l!E(m)
l
(q)xl
!
(30a)
eφn(x) = exp
 ∞
X
l=1
1
l!
eE(m)
l
(˜q)xl
!
.
(30b)
The proof of this proposition is given in Section 2.6. The ﬁrst few terms in Equations
(30a)-(30a) are given by:
φm(x) = exp
„
−E(m)
1
x −1
2 E(m)
2
x2 −1
6 E(m)
3
x3 −1
24 E(m)
4
x4 −. . .
«
(31a)
= 1 −E(m)
1
x + 1
2 (E(m)2
1
−E(m)
2
)x2 + 1
6 (−E(m)3
1
+ 3E(m)
1
E(m)
2
−E(m)
3
)x3+
1
24 (E(m)4
1
−6E(m)2
1
E(m)
2
+ 3E(m)2
2
+ 4E(m)
1
E(m)
3
−E(m)
4
)x4 + . . .
(31b)
eφn(x) = exp
„
e
E(n)
1
x + 1
2
e
E(n)
2
x2 + 1
6
e
E(n)
3
x3 + 1
24
e
E(n)
4
x4 −. . .
«
(31c)
= 1 + e
E(n)
1
x + 1
2 ( e
E(n)2
1
+ e
E(n)
2
)x2 + 1
6 ( e
E(n)3
1
+ 3 e
E(n)
1
e
E(n)
2
+ e
E(n)
3
)x3+
1
24 ( e
E(n)4
1
+ 6 e
E(n)2
1
e
E(n)
2
+ 3 e
E(n)2
2
+ 4 e
E(n)
1
e
E(n)
3
+ e
E(n)
4
)x4 + . . .
(31d)
where E(m)
l
= E(m)
l
(q) and eE(m)
l
= eE(m)
l
(˜q).
