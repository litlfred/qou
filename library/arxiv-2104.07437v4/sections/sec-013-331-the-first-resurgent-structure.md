---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-013-331-the-first-resurgent-structure
section_title: "The first resurgent structure"
section_number: 3.3.1
pages: 28-30
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
---
The ﬁrst resurgent structure
From the free energies Fg(λ) we assemble the series for N = 1
Φ0;1(gs) = exp
VP2
gs

ϕ0;1(gs),
(3.100)
with
VP2 = 3V
4π2
(3.101)
and
ϕ0;1(gs) = 1 −π2gs
6
√
3 + π4g2
s
216 + 59π6g3
s
19440
√
3 −251π8g4
s
1399680 −23687π10g5
s
58786560
√
3 + 785699π12g6
s
31744742400 + . . . . (3.102)
The resurgent structure of Φ0;1(gs) is very simple. The Borel transform bΦ0;1(ζ) has inﬁnitely
many singularities along the imaginary axis located at
in,
n ∈Z̸=0,
(3.103)
as illustrated in Fig. 7. They correspond to the asymptotic series in the same family as Φ0;1(gs)
Φ0,n;1(gs) = Φ0;1(gs)e−n i
gs ,
n ∈Z.
(3.104)
We conclude that the minimal resurgent structure associated to Φ0;1(gs) is the set {Φ0,n;1(gs)}n∈Z.
Following the structure of Borel singularities, there is a single generating series of Stokes
constants
S00;1(q) =
X
n∈Z̸=0
S00,n;1qn/3.
(3.105)
– 27 –
Note that we have scaled the power of q by a factor of 1/3, as compared to (2.34), similarly to
what we did in the example of F0. The meaning of this will be clear in the next subsection. The
generating function can be decomposed as
S00;1(q) = S+
1 (q) + S−
1 (q),
(3.106)
where S±
1 (q) are q and q−1-series respectively, encoding the Stokes constants in the upper and
lower half planes. The identity
Φ0;1(gs)∗= Φ0;1(g∗
s),
(3.107)
implies that
S−
1 (q) = (1 + S+
1 (q−1))−1 −1,
(3.108)
and therefore we only have to compute S+
1 (q).
To compute the q-series S+
1 (q), we invoke the TS/ST correspondence [18, 19]. The integral
kernel for the local P2 geometry is [59]
ρP2(x1, x2) =
e2πa(x1+x2)
2b cosh π x1−x2+ih
b
Φb(x2 + 2ia)
Φb(x1 −2ia),
(3.109)
where
a = h = b
6,
(3.110)
and the Planck constant ℏis related to b by
ℏ= 2πb2
3
.
(3.111)
As in the case of local F0, we can use the explicit expression (3.109) to extend the integral kernel
to complex values of ℏin C′, corresponding to Re b > 0. The ﬁrst “bosonic” trace has the integral
form [59]
TrρP2 =
1
2b cos(πh/b)
Z
R
e4πxa Φb(x + 2ia)
Φb(x −2ia)dx,
(3.112)
which is also identiﬁed with the fermionic trace Z1(ℏ). This integral can be quickly evaluated
by either using the integral Ramanujan formula or by completing the integration contour from
above, and it yields [59]
TrρP2 =
1
√
3be
πi
12 (b2+b−2)+ πi
4 −πi
9 b2 Φb(cb −ib
3 )2
Φb(cb −2ib
3 ).
(3.113)
Note that in the limit ℏ→∞, or gs = −1/ℏ→0, (3.113) is asymptotically
TrρP2 ∼−i 3−3/4(2πgs/3)1/2Φ0;1(gs),
(3.114)
and therefore the relation (3.5) is upheld.
More is actually true. By high precision numerical calculation, we verify that, when gs is in
the second quadrant, the Borel resummation of Φ0;1(gs) is identical to the ﬁrst spectral trace,
up to a simple prefactor
TrρP2 = −i 3−3/4(2πgs/3)1/2sII(Φ0;1)(gs).
(3.115)
– 28 –
ϕ0;1(gs)
3
3
1
3
−3
6
Figure 8. Stokes constants for the asymptotic series from the ﬁrst trace of local P2.
On the other hand, when gs is in the ﬁrst quadrant
TrρP2 = −i 3−3/4(2πgs/3)1/2sI(Φ0;1)(gs)K1(q),
(3.116)
where
K1(q) = (q2/3; q)3
∞
(q1/3; q)3∞
,
(3.117)
with
q = e2πib2 = e−3i/gs.
(3.118)
Note that, here, q is deﬁned in such a way that q1/3 accounts for the distance between neighboring
singularities in the tower (3.103). Therefore,
S+
1 (q) = K1(q) −1 = 3q1/3 + 3q2/3 + q + 3q4/3 + 6q5/3 −3q7/3 + 9q8/3 + 9q3 + . . . .
(3.119)
Using (3.108) we ﬁnd the Stokes constants in the lower half plane
S−
1 (q) = −3q−1/3 + 6q−2/3 −10q−1 + 12q−4/3 −9q−5/3 + q−2 + . . . .
(3.120)
These Stokes constants are illustrated in Fig. 8.
