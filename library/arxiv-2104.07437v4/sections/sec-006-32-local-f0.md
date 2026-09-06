---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-006-32-local-f0
section_title: "Local F0"
section_number: 3.2
pages: 15-20
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
by results in the 4d limit of the theory [78], it has been suggested thatq-Painlev´ e equations could
play such a rˆ ole [79], but a complete description is still lacking. Recently, and following the same
philosophy, [80] obtained a “wave equation” in the case of the resolved conifold. Connections
between partition functions in the 4d case and integrable equations have been also studied in
[81–83].
3.2 Local F0
The ﬁrst example we consider is the canonical bundle over the Hirzebruch surface F0 = P1× P1,
which is also called the local F0 geometry,
X =O(−2,−2)→ P1× P1. (3.11)
This geometry is a toric variety and it is described by the toric diagram in Fig. 2. The K¨ ahler
moduli of this geometry are one true modulus u corresponding to the internal vertex of the toric
diagram, and one mass parameter mF0 corresponding to one of the four boundary vertices. For
the topological string theory on local F0, the full moduli space is identiﬁed with the family of
mirror curves described by the equation
ex +mF0e−x + ey + e−y + ˜u = 0, x,y ∈ C. (3.12)
The moduli are a “true” modulus u = 1/˜u2 and the mass parameter mF0. The maximal conifold
point on the moduli space is in the discriminant of (3.12). For simplicity we only consider
mF0 = 1, in which case the maximal conifold point is located at
u = 1
16. (3.13)
The free energies of the topological string at the maximal conifold point can be computed by
the holomorphic anomaly equations [84, 85], and in terms of the local ﬂat coordinate λ they are
[43, 86]
F0(λ,m F0 = 1) =λ2
2
(
logλ + log
(π2
4
)
− 3
2
)
− 2C
π2 − π2λ3
12 + 5π4λ4
288 − 7π6λ5
960 +..., (3.14a)
F1(λ,m F0 = 1) =− 1
12 log(λ) +π2λ
24 + 13π4λ2
288 − 29π6λ3
576 +..., (3.14b)
F2(λ,m F0 = 1) =− 1
240λ2 + 53π6λ
1920 +..., (3.14c)
– 14 –
4C/π 2
ϕ0(gs)
−4C/π 2
ϕ1(gs)
Figure 3. The singularities in the Borel plane for the series ϕ0(gs), ϕ1(gs).
where C = Im(Li2(i)) = 0.915966... is the Catalan’s constant, and we have restricted the mass
parameter mF0 = 1. We can then construct the formal power series Φ 0;N(gs) by (2.11).
In this section we are only concerned with the case of N = 1. We will see that this example
already has a very rich resurgent structure, and it is very similar to the quantum invariants of
the ﬁgure eight knot studied in [11, 12]. Furthermore, we will show the power of the TS/ST
correspondence, which enables us to write down the complete set of Stokes constants.
3.2.1 The ﬁrst resurgent structure
By using the free energies (3.14a)–(3.14c) we can construct the ﬁrst asymptotic series for N = 1
by (2.11)
Φ0;1(gs) = eVF0/gsϕ0;1(gs), (3.15)
where
VF0 = 2C
π2, (3.16)
and
ϕ0;1(gs) = 1 +π2
24gs + 73π4
1152g2
s + 13541π6g3
s
414720 + 855509π8g4
s
39813120 + 150067879π10g5
s
6688604160 +.... (3.17)
Since we are only concerned with N = 1, we will suppress the subscript ;1 in the remainder of
the section.
The series Φ 0(gs) has a very rich resurgent structure. The Borel transform ˆΦ0(ζ) has two
inﬁnite towers of singularities located at
in, n ∈ Z⁄=0, (3.18)
ζ0 + in′, n ′∈ Z, (3.19)
with ζ0 = 2VF0, which is illustrated in the left panel of Fig. 3. The ﬁrst tower of singularities
along the imaginary axis corresponds to the following asymptotic series in the same family
Φ0,n(gs) = Φ0(gs)e−n i
gs, n ∈ Z. (3.20)
– 15 –
The second tower of singularities indicates the existence of a new family of asymptotic series.
Since the singularity ζ0 on the positive real axis is the nearest singularity, it controls the large
order behavior of the coeﬃcients an of ϕ0(gs) by
an∼ S01,0
2πi
∞∑
k=0
bkζk−n
0 Γ(n−k)
= S01,0
2πi ζ−n
0 Γ(n)
(
b0 + b1ζ0
n− 1 + b2ζ2
0
(n− 1)(n− 2) +...
)
, (3.21)
wherebk are the coeﬃcients of the series that resurges at ζ0, and S01,0 is the Stokes constant. By
systematically extracting the coeﬃcients bk, we ﬁnd that the second family of series is given by
Φ1,n(gs) = Φ1(gs)e−n i
gs, n ∈ Z, (3.22)
with
Φ1(gs) = iΦ0(−gs). (3.23)
Along the way, we also ﬁnd the value of the ﬁrst Stokes constant
S01,0 = 4. (3.24)
Next we study the resurgent structure of the new series Φ 1(gs). Since it is related to Φ 0(gs)
by (3.23), its Borel singularities are mirror reﬂection of those of Φ 0(gs) with respect to the
imaginary axis, as illustrated in the right panel of Fig. 3. They are located at
in, n ∈ Z⁄=0, (3.25)
ζ1 + in′, n ′∈ Z, (3.26)
with ζ1 =−4C/π2, associated with Φ 1,n(gs) and Φ 0,n′(gs) respectively. In addition, using the
same large order analysis we ﬁnd that the Stokes constant at the singularity ζ1 on the negative
real axis is
S10,0 =−4. (3.27)
Therefore we conclude that {Φ0,n(gs), Φ1,n(gs)} form a minimal resurgent structure. We denote
by Φ(gs) the 2-vector of asymptotic series
Φ(gs) =
(Φ0(gs)
Φ1(gs)
)
. (3.28)
As shown in Fig. 4, the Stokes rays passing through the Borel singularities of both series arrange
into a peacock pattern, very similar to the one found for the asymptotic series of the ﬁgure eight
knot in [11, 12]. The Stokes rays divide the complex plane into inﬁnitely many sectors, and only
inside a sector can the Borel resummation of Φ(gs) be deﬁned. We denote by sR(Φ)(gs) the Borel
resummation along a ray in the sector R of the asymptotic series. As in [11, 12] we denote the
four sectors bordering the real axis by I,II,III,IV in the anti-clockwise order.
Following the structure of Borel singularities, we can collect all the Stokes constants into the
matrix
S(q) = (Sσσ′(q))σ,σ′=0,1. (3.29)
– 16 –
III
III IV
Figure 4. Stokes rays and sectors in the gs-plane for Φ(gs).
In this section we will scale powers of q by 1/2 in the generating series of Stokes constants for
the reason that will become clear in the next subsection, in other words
Sσ,σ′(q) =
∑
n∈Z
Sσσ′,nqn/2. (3.30)
We also decompose the matrix S(q) as
S(q) = S(0) + S+(q) + S−(q), (3.31)
where S(0) is an oﬀ-diagonal constant matrix containing Stokes constants on the real axis, the
entries of S+(q) are q-series encoding Stokes constants in the upper half plane, while the entries
of S−(q) are q−1-series encoding Stokes constants in the lower half plane.
The constant matrix S(0) has only two non-vanishing oﬀ-diagonal entries
S(0) =
( 0 S01,0
S10,0 0
)
, (3.32)
and they were already obtained in (3.24), (3.27). One ﬁnds that the matrix S(0) is skew-
symmetric. To compute the Stokes matrices S+(q) and S−(q) it is beneﬁcial to use the TS/ST
correspondence as well as more advanced machinery of radial asymptotic analysis, which we will
explain in detail in the following two subsections. We quote the results here for completeness.
The Stokes automorphism SI↦→II (q) from sector I to II is deﬁned by
sII (Φ)(gs) = SI↦→II (q)sI(Φ)(gs), (3.33)
and its explicit expression is
SI↦→II (q) = 1
2
( 2g(q)G(q) G′(q)g(q)−g′(q)G(q)
G(q)g′(q)−g(q)G′(q) 2 g′(q)G′(q),
)
, (3.34)
– 17 –
ϕ0(gs)
6
3
6
17
−6
33
4
−8
36
−192
1048
−8
36
ϕ1(gs)
−6
33
−186
1036
6
3
−4
8
−36
192
−1048
8
−36
Figure 5. Stokes constants for the minimal resurgent structure {Φ0,n(gs), Φ1,n(gs)} of local F0.
where the q-series g(q),G (q),g′(q),G′(q) are deﬁned in (3.75), (3.77a), (3.77b). We note that
SI↦→II (q) is also skew-symmetric. The Stokes constants in the upper half plane can be read oﬀ
from SI↦→II (q). In particular,
S+
00(q) =SI↦→II (q)1,1− 1
=6q1/2 + 3q + 6q3/2 + 17q2− 26q5/2 + 52q3 +..., (3.35a)
S+
01(q) =SI↦→II (q)1,2/SI↦→II (q)1,1
=− 8q1/2 + 36q− 192q3/2 + 1048q2− 5752q5/2 + 31656q3 +..., (3.35b)
S+
10(q) =SI↦→II (q)2,1/SI↦→II (q)1,1
=8q1/2− 36q + 192q3/2− 1048q2 + 5752q5/2− 31656q3 +..., (3.35c)
S+
11(q) =SI↦→II (q)2,2− SI↦→II (q)1,2SI↦→II (q)1,1SI↦→II (q)2,1− 1
=− 6q1/2 + 33q + 582q3/2 + 1420q2 + 2528q5/2 + 7383q3 +.... (3.35d)
Note that the deﬁnition of the Stokes automorphism (3.33), together with the diﬀerence between
neighboring series in the same family (3.20), (3.22) implies that q is identiﬁed naturally with
q = e− 2i
gs. (3.36)
To compute the Stokes constants in the lower half plane, we notice that
Φ(gs)∗ =
(1 0
0−1
)
Φ(g∗
s), q (gs)∗ =q(g∗
s)−1. (3.37)
Therefore by complex conjugating both sides of (3.33) we ﬁnd
sIV (Φ)(gs) = SIII↦→IV (q)sIII (Φ)(gs), (3.38)
with
SIII↦→IV (q) =
(1 0
0−1
)
SI↦→II (q−1)−1
(1 0
0−1
)
. (3.39)
– 18 –
The Stokes constants in the lower half plane can also be read oﬀ and we ﬁnd
S−
00(q) =− 6q−1/2 + 33q−1 + 582q−3/2 + 1420q−2 +..., (3.40a)
S−
01(q) =− 8q−1/2 + 36q−1− 192q−3/2 + 1048q−2 +..., (3.40b)
S−
10(q) =8q−1/2− 36q−1 + 192q−3/2− 1048q−2 +..., (3.40c)
S−
11(q) =6q−1/2 + 3q−1 + 6q−3/2 + 17q−2 +.... (3.40d)
We illustrate the Stokes constants in Fig. 5.
