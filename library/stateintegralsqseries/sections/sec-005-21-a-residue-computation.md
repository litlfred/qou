---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-005-21-a-residue-computation
section_title: "A residue computation"
section_number: 2.1
pages: 6-10
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
residue theorem on a semicircle γR with center 0 and radius R, oriented counterclockwise in
the upper half-plane:
Then, we will take the limit R→∞ . To compute the residue of the integrand, we need to
expand Φb(x) near the pole
xm,n =cb +ibm +ib−1n
for natural numbers m and n. Let
φm(x) = (qm+1ex;q)∞
(qm+1;q)∞
(23)
~φn(x) = (˜q; ˜q)∞
(˜qex; ˜q)∞
(˜q−1; ˜q−1)n
(˜q−1ex; ˜q−1)n
(24)
Lemma 2.1. We have:
(25) Φ b(x +xm,n) = (q;q)∞
(˜q; ˜q)∞
1
(q;q)m
1
(˜q−1; ˜q−1)n
φm(2πbx)~φn(2πb−1x)
1−e2πb−1x .
FROM STATE INTEGRALS TO q-SERIES 7
Proof. Equation (1) implies the functional equations
Φb(x +cb +ib)
Φb(x +cb) = 1
1−qe2πbx
Φb(x +cb +ib−1)
Φb(x +cb) = 1
1− ˜q−1e2πb−1x
which give
Φb(x +xm,n) = Φb(x +cb) 1
(qe2πbx;q)m
1
(˜q−1e2πb−1x; ˜q−1)n
Φb(x +cb) = 1
1−e2πb−1x
(qe2πbx;q)∞
(˜qe2πb−1x; ˜q)∞
.
Thus,
Φb(x +xm,n) = (q;q)∞
(˜q; ˜q)∞
1
(q;q)m
1
(˜q−1; ˜q−1)n
·
1
1−e2πb−1x
(qe2πbx;q)∞
(q;q)∞
(˜q; ˜q)∞
(˜qe2πb−1x; ˜q)∞
(q;q)m
(qe2πbx;q)m
(˜q−1; ˜q−1)n
(˜q−1e2πb−1x; ˜q−1)n
= (q;q)∞
(˜q; ˜q)∞
1
(q;q)m
1
(˜q−1; ˜q−1)n
·
1
1−e2πb−1x
(qm+1e2πbx;q)∞
(qm+1;q)∞
(˜q; ˜q)∞
(˜qe2πb−1x; ˜q)∞
(˜q−1; ˜q−1)n
(˜q−1e2πb−1x; ˜q−1)n
The result follows. □
The decoupling of (m,n ) in the quadratic form comes as follows: sinceA,m,n are integers,
eAπimn = 1 and a computation gives
e−Aπi(x+xn,m)2
=iA
(q
˜q
)A
8
tA
m(q)~tA
n (˜q)e−Aπix2+2Aπx(b(m+ 1
2 )+b−1(n+ 1
2 ))
where
tA
m(q) = (−1)AmqAm(m+1)
2 , ~tA
n (˜q) = (−1)An˜q−An(n+1)
2 .
The Dedekind function η(τ) = q1/24(q;q)∞ (with q = e2πiτ ) satisﬁes the modular equation
η(−τ−1) =√−iτη (τ) [And76]. It follows that
(26) (q;q)∞
(˜q; ˜q)∞
=e
πi
4
( ˜q
q
) 1
24
b−1.
After we set w =x/(2π), the above discussion implies that
(27) IA,B(b) =
( ˜q
q
)B−3A
24
eπiB+2(A+1)
4
∞∑
m,n=0
(Resw=0FA,B,m,n(w)) tA
m(q)
(q;q)B
m
~tA
n (˜q)
(˜q−1; ˜q−1)B
n
,
8 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
where
(28) FA,B,m,n(w) =e
A
4πiw2+Aw(b(m+ 1
2 )+b−1(n+ 1
2 ))
(
φm(bw)~φn(b−1w)
b(1−eb−1w)
)B
.
2.2. The Taylor series of φm(x) and ~φn(x). In this section we express the Taylor series
of φm(x) and ~φn(x) in terms of the q-series E(m)
l (q) and ~E(m)
l (˜q) deﬁned by:
E(m)
l (q) =
∞∑
s=1
sl−1qs(m+1)
1−qs =⟨δl(xm)⟩(29a)
~E(n)
l (˜q) =



−n +E(n)
1 (˜q) if l = 1
E(n)
l (˜q) if l> 1 is odd
2E(0)
l (˜q)−E(n)
l (˜q) if l> 1 is even
(29b)
Proposition 2.2. We have:
φm(x) = exp
(
−
∞∑
l=1
1
l!E(m)
l (q)xl
)
(30a)
~φn(x) = exp
( ∞∑
l=1
1
l!
~E(m)
l (˜q)xl
)
.(30b)
The proof of this proposition is given in Section 2.6. The ﬁrst few terms in Equations
(30a)-(30a) are given by:
φm(x) = exp
„
−E(m)
1 x− 1
2E(m)
2 x2− 1
6E(m)
3 x3− 1
24E(m)
4 x4−...
«
(31a)
= 1−E(m)
1 x + 1
2 (E(m)2
1 −E(m)
2 )x2 + 1
6 (−E(m)3
1 + 3E(m)
1 E(m)
2 −E(m)
3 )x3+
1
24 (E(m)4
1 − 6E(m)2
1 E(m)
2 + 3E(m)2
2 + 4E(m)
1 E(m)
3 −E(m)
4 )x4 +...(31b)
eφn(x) = exp
„
eE(n)
1 x + 1
2
eE(n)
2 x2 + 1
6
eE(n)
3 x3 + 1
24
eE(n)
4 x4−...
«
(31c)
= 1 + eE(n)
1 x + 1
2 (eE(n)2
1 + eE(n)
2 )x2 + 1
6 (eE(n)3
1 + 3eE(n)
1 eE(n)
2 + eE(n)
3 )x3+
1
24 (eE(n)4
1 + 6eE(n)2
1 eE(n)
2 + 3eE(n)2
2 + 4eE(n)
1 eE(n)
3 + eE(n)
4 )x4 +...(31d)
where E(m)
l =E(m)
l (q) and ~E(m)
l = ~E(m)
l (˜q).
2.3. The connection with the diﬀerential operators δl and ~δl. In this section we
connect the series E(m)
l (q) and ~E(m)
l (˜q) with the action of the diﬀerential operators δl and~δl
on a series F (x) and ~F (~x) respectively. Consider formal power series
F (x) =
∞∑
m=0
t(m)xm ~F (~x) =
∞∑
m=0
~t(m)~xm.
FROM STATE INTEGRALS TO q-SERIES 9
Lemma 2.3. We have:
∞∑
m=0
( r∏
j=1
E(m)
lj (q)
)
t(m) =⟨
r∏
j=1
δljF⟩(32)
∞∑
m=0
mrt(m) =⟨δrF⟩(33)
and
∞∑
n=0
( r∏
j=1
~E(n)
lj (˜q)
)
~t(n) =⟨
r∏
j=1
~δlj
~F⟩(34)
∞∑
n=0
nr~t(n) =⟨~dr~F⟩.(35)
Proof. For a positive natural number l we have:
∞∑
m=0
E(m)
l (q)t(m) =
∞∑
m=0
⟨δl(xm)⟩t(m) =
⟨
δl(
∞∑
m=0
t(m)xm)
⟩
=⟨δlF⟩.
Moreover, for positive natural numbers l,l′ we have:
∞∑
m=0
E(m)
l (q)E(m)
l′ (q)t(m) =
∞∑
m=0
⟨δl(xm)⟩⟨δl′(xm)⟩t(m)
=
⟨
δl
( ∞∑
m=0
⟨δl′(xm)⟩t(m)xm
)⟩
.
Now,
⟨δl′(xm)⟩t(m)xm =
∞∑
s=1
sl′−1qs
1−qsqsmt(m)xm =δl′(xm)t(m)
and summing up over m, we obtain that
∞∑
m=0
⟨δl′(xm)⟩t(m)xm =δl′F (q,x ).
It follows that
∞∑
m=0
E(m)
l (q)E(m)
l′ (q)t(m) =⟨δlδl′F⟩.
The general case of Equation (32) follows by induction on r. Equation (33) is obvious. □
10 STA VROS GAROUF ALIDIS AND RINAT KASHAEV
