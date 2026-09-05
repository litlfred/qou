---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-009-33-local-p2
section_title: "Local P2"
section_number: 3.3
pages: 27-30
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
---
satisﬁes the following q-diﬀerence equation9
z(c−abqz)D2
qΦ +
(1−c
1−q + (1−a)(1−b)− (1−abq)
1−q z
)
DqΦ− (1−a)(1−b)
(1−q)2 Φ = 0, (3.94)
where
Df(z) = f(z)−f(zq)
(1−q)z . (3.95)
It is easy to see that, when a =b =−1, c =q, the equation (3.94) becomes (3.91), after setting
q→ ˜q.
3.3 Local P2
The next example we consider is the canonical bundle over the surface P2, which is also called
the local P2 geometry,
X =O(−3)→ P2. (3.96)
This geometry is also toric and it is described by the toric diagram in Fig. 6. There is one
true K¨ ahler modulus corresponding to the internal vertex of the toric diagram, and no mass
parameter. For the topological string theory on local P2, the full moduli space is identiﬁed with
the family of mirror curves described by the equation
ex + ey + e−x−y + ˜u = 0, x,y ∈ C, (3.97)
and it is parametrised by u = 1/˜u3. The maximal conifold point on the moduli space is at the
discriminant locus of (3.97)
u =− 1
27. (3.98)
The free energies of the topological string at the maximal conifold point were computed in [42, 86]
by using the holomorphic anomaly equations [84, 85]. The series for F0(λ) was written down in
(2.6). For g = 1, 2, one ﬁnds
F1(λ) =− 1
12 log(λ) + 5π2λ
18
√
3− π4λ2
486 − 40π6λ3
2187
√
3 + 283π8λ4
32805 +..., (3.99a)
F2(λ) =− 1
240λ2 + 4π6λ
405
√
3− 3187π8λ2
492075 +.... (3.99b)
9See for instance http://dlmf.nist.gov/17.6.E27.
– 26 –
ϕ0;1(gs)
Figure 7. The singularities in the Borel plane for the series ϕ0;1(gs).
We can then construct the formal power series Φ 0;N(gs) by (2.11).
In this section we will study the resurgent structure of the power series for both N = 1 and
N = 2 of the local P2 geometry.
3.3.1 The ﬁrst resurgent structure
From the free energiesFg(λ) we assemble the series for N = 1
Φ0;1(gs) = exp
(VP2
gs
)
ϕ0;1(gs), (3.100)
with
VP2 = 3V
4π2 (3.101)
and
ϕ0;1(gs) = 1−π2gs
6
√
3 +π4g2
s
216 + 59π6g3
s
19440
√
3− 251π8g4
s
1399680− 23687π10g5
s
58786560
√
3 + 785699π12g6
s
31744742400 +.... (3.102)
The resurgent structure of Φ0;1(gs) is very simple. The Borel transform ˆΦ0;1(ζ) has inﬁnitely
many singularities along the imaginary axis located at
in, n ∈ Z⁄=0, (3.103)
as illustrated in Fig. 7. They correspond to the asymptotic series in the same family as Φ 0;1(gs)
Φ0,n;1(gs) = Φ0;1(gs)e−n i
gs, n ∈ Z. (3.104)
We conclude that the minimal resurgent structure associated to Φ0;1(gs) is the set{Φ0,n;1(gs)}n∈Z.
Following the structure of Borel singularities, there is a single generating series of Stokes
constants
S00;1(q) =
∑
n∈Z⁄=0
S00,n;1qn/3. (3.105)
– 27 –
Note that we have scaled the power of q by a factor of 1/3, as compared to (2.34), similarly to
what we did in the example of F0. The meaning of this will be clear in the next subsection. The
generating function can be decomposed as
S00;1(q) = S+
1 (q) + S−
1 (q), (3.106)
where S±
1 (q) are q and q−1-series respectively, encoding the Stokes constants in the upper and
lower half planes. The identity
Φ0;1(gs)∗ = Φ0;1(g∗
s), (3.107)
implies that
S−
1 (q) = (1 + S+
1 (q−1))−1− 1, (3.108)
and therefore we only have to compute S+
1 (q).
To compute the q-series S+
1 (q), we invoke the TS/ST correspondence [18, 19]. The integral
kernel for the local P2 geometry is [59]
ρP2(x1,x 2) = e2πa(x1+x2)
2b coshπx1−x2+ih
b
Φb(x2 + 2ia)
Φb(x1− 2ia), (3.109)
where
a =h = b
6, (3.110)
and the Planck constant ℏ is related to b by
ℏ = 2πb2
3 . (3.111)
As in the case of local F0, we can use the explicit expression (3.109) to extend the integral kernel
to complex values of ℏ in C′, corresponding to Re b> 0. The ﬁrst “bosonic” trace has the integral
form [59]
TrρP2 = 1
2b cos(πh/b)
∫
R
e4πxa Φb(x + 2ia)
Φb(x− 2ia)dx, (3.112)
which is also identiﬁed with the fermionic trace Z1(ℏ). This integral can be quickly evaluated
by either using the integral Ramanujan formula or by completing the integration contour from
above, and it yields [59]
TrρP2 = 1√
3be
πi
12 (b2+b−2)+πi
4−πi
9 b2 Φb(cb− ib
3 )2
Φb(cb− 2ib
3 ). (3.113)
Note that in the limit ℏ→∞ , or gs =−1/ℏ→ 0, (3.113) is asymptotically
TrρP2∼− i 3−3/4(2πgs/3)1/2Φ0;1(gs), (3.114)
and therefore the relation (3.5) is upheld.
More is actually true. By high precision numerical calculation, we verify that, when gs is in
the second quadrant, the Borel resummation of Φ 0;1(gs) is identical to the ﬁrst spectral trace,
up to a simple prefactor
TrρP2 =−i 3−3/4(2πgs/3)1/2sII (Φ0;1)(gs). (3.115)
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
TrρP2 =−i 3−3/4(2πgs/3)1/2sI(Φ0;1)(gs)K1(q), (3.116)
where
K1(q) = (q2/3;q)3
∞
(q1/3;q)3∞
, (3.117)
with
q = e2πib2
= e−3i/gs. (3.118)
Note that, here,q is deﬁned in such a way thatq1/3 accounts for the distance between neighboring
singularities in the tower (3.103). Therefore,
S+
1 (q) =K1(q)− 1 = 3q1/3 + 3q2/3 +q + 3q4/3 + 6q5/3− 3q7/3 + 9q8/3 + 9q3 +.... (3.119)
Using (3.108) we ﬁnd the Stokes constants in the lower half plane
S−
1 (q) =−3q−1/3 + 6q−2/3− 10q−1 + 12q−4/3− 9q−5/3 +q−2 +.... (3.120)
These Stokes constants are illustrated in Fig. 8.
