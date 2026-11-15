---
doc_id: stateintegralsqseries
doc_title: "FROM STATE INTEGRALS TO q-SERIES"
section_id: sec-007-23-the-connection-with-the-differential-operator
section_title: "The connection with the differential operators l and '0365l"
section_number: 2.3
pages: 8-10
source_pdf: state.integrals.qseries.pdf
source_sha256: a5e86443f35e21c0
toc_source: outline
doc_brief: "FROM STATE INTEGRALS TO q-SERIES — It is well-known to the experts that multi-dimensional state integra ls of prod- ucts of Faddeev’s quantum dilogarithm which arise in Quantum Topolog y can be"
duplicate_of: "arxiv-1304.2705v1"
---
connect the series E(m)
l
(q) and eE(m)
l
(˜q) with the action of the diﬀerential operators δl and eδl
on a series F(x) and eF(ex) respectively. Consider formal power series
F(x) =
∞
X
m=0
t(m)xm
eF(ex) =
∞
X
m=0
et(m)exm .
FROM STATE INTEGRALS TO q-SERIES
9
Lemma 2.3. We have:
∞
X
m=0
 rY
j=1
E(m)
lj
(q)
!
t(m) = ⟨
rY
j=1
δljF⟩
(32)
∞
X
m=0
mrt(m) = ⟨δrF⟩
(33)
and
∞
X
n=0
 rY
j=1
eE(n)
lj (˜q)
!
et(n) = ⟨
rY
j=1
eδlj eF⟩
(34)
∞
X
n=0
nret(n) = ⟨edr eF⟩.
(35)
Proof. For a positive natural number l we have:
∞
X
m=0
E(m)
l
(q)t(m) =
∞
X
m=0
⟨δl(xm)⟩t(m) =
D
δl(
∞
X
m=0
t(m)xm)
E
= ⟨δlF⟩.
Moreover, for positive natural numbers l, l′ we have:
∞
X
m=0
E(m)
l
(q)E(m)
l′
(q)t(m) =
∞
X
m=0
⟨δl(xm)⟩⟨δl′(xm)⟩t(m)
=
D
δl
 ∞
X
m=0
⟨δl′(xm)⟩t(m)xm
! E
.
Now,
⟨δl′(xm)⟩t(m)xm =
∞
X
s=1
sl′−1qs
1 −qs qsmt(m)xm = δl′(xm)t(m)
and summing up over m, we obtain that
∞
X
m=0
⟨δl′(xm)⟩t(m)xm = δl′F(q, x) .
It follows that
∞
X
m=0
E(m)
l
(q)E(m)
l′
(q)t(m) = ⟨δlδl′F⟩.
The general case of Equation (32) follows by induction on r. Equation (33) is obvious.
□
10
STAVROS GAROUFALIDIS AND RINAT KASHAEV
