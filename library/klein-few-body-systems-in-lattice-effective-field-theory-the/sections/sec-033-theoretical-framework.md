---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-033-theoretical-framework
section_title: "Theoretical framework"
section_number: null
pages: 65-68
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
Although we work in the three-body sector, we are still able to do an exact calculation using the Lanczos
method. Therefore we extend the former analysis of the 2N sector to the triton, which means that we
cannot work in radial coordinates anymore but we calculate the spectrum in a cubic box. In addition
to two-body forces we include three-body potentials, which were reviewed in [115]. They consist of a
59
Chapter 5 The Tjon band in Nuclear Lattice E ﬀective Field Theory
0
20
40
60
80
100
0 50 100 150 200
0
20
40
60
80
100
120
140
160
180
0 50 100 150 200
-10
-5
0
5
10
0 50 100 150 200
-20
-15
-10
-5
0
5
10
15
20
0 50 100 150 200
-20
-15
-10
-5
0
5
10
15
20
0 50 100 150 200
-20
-15
-10
-5
0
5
10
15
20
0 50 100 150 200
-20
-15
-10
-5
0
5
10
15
20
0 50 100 150 200
-10
-5
0
5
10
0 50 100 150 200
-10
-5
0
5
10
0 50 100 150 200
-10
-5
0
5
10
0 50 100 150 200
-10
-5
0
5
10
0 50 100 150 200
δ(1S0) [degrees]
pCM[MeV]
δ(3S1) [degrees]
pCM[MeV]
ϵ1 [degrees]
pCM[MeV]
δ(1P1) [degrees]
pCM[MeV]
δ(3P0) [degrees]
pCM[MeV]
Nijmegen PW ALattice LOLattice N2LO
δ(3P1) [degrees]
pCM[MeV]
δ(3P2) [degrees]
pCM[MeV]
δ(1D2) [degrees]
pCM[MeV]
δ(3D1) [degrees]
pCM[MeV]
δ(3D2) [degrees]
pCM[MeV]
δ(3D3) [degrees]
pCM[MeV]
Figure 5.3: LO (squares) and NNLO (circles) neutron-proton phase shifts and mixing angles for a = 1.32 fm. The
NPW A is given by the solid line.
three-body contact interaction, a one- and a two-pion exchange interaction. These terms are
V3N
contact = D3N
contact
∑
⃗n
: ρ(⃗n)ρ(⃗n)ρ(⃗n) : , (5.50)
V3N
OPE =−D3N
OPE
∑
⃗n1,S 1,⃗n2,S 2,I
[
GS 1,S 2
(⃗n1−⃗n2
)×: ρS 1,I
(⃗n1
)ρS 2,I
(⃗n2
)ρ(⃗n2
) :
]
, (5.51)
V3N
TPE = V3N
TPE,m2 + V3N
TPE,p2 + V3N
TPE,xx. (5.52)
The latter equation describing the TPEP among three particles can be split up into three parts which
read
V3N
TPE,q2 = D3N
q2
∑
⃗n1,S 1,⃗n2,S 2,
⃗n3,S 3,I
[
GS 1,S 3
(⃗n1−⃗n3
) GS 2,S 3
(⃗n2−⃗n3
) : ρS 1,I
(⃗n1
)ρS 2,I
(⃗n2
)ρ(⃗n3
) :
]
, (5.53)
V3N
TPE,m2 = D3N
m2
∑
⃗n1,S 1,⃗n2,S 2,⃗n3,I
[
GS 1
(⃗n1−⃗n3
) GS 2
(⃗n2−⃗n3
) : ρS 1,I
(⃗n1
)ρS 2,I
(⃗n2
)ρ(⃗n3
) :
]
, (5.54)
60
5.3 Three-body sector
0
20
40
60
80
100
0 50 100 150 200
0
20
40
60
80
100
0 50 100 150 200
0
20
40
60
80
100
0 50 100 150 200
δ(1S0) [degrees]
pCM [MeV]
Lattice spacing a = 1.97 fm
δ(1S0) [degrees]
pCM [MeV]
Lattice spacing a = 1.64 fm
Nijmegen PW A
Lattice LO+Coul
Lattice N2LO+Coul
δ(1S0) [degrees]
pCM [MeV]
Lattice spacing a = 1.32 fm
Figure 5.4: LO (squares) and NNLO (circles) (both including Coulomb) proton-proton 1S 0 phase shift for a =
1.97 fm, a = 1.64 fm and a = 1.32 fm. The NPW A is given by the solid line.
V3N
TPE,xx = D3N
xx
∑
⃗n3, ˜S 1, ˜S 2, ˜S 3,I1,I2,
I3,⃗n2,S 2,⃗n3,S 3
[
GS 1, ˜S 1
(⃗n1−⃗n3
) GS 2, ˜S 2
(⃗n2−⃗n3
)ϵ ˜S 1, ˜S 2, ˜S 3
ϵI1,I2,I3
×: ρS 1,I1
(⃗n1
)ρS 2,I2
(⃗n2
)ρ ˜S 3,I3
(⃗n3
) :
]
,
(5.55)
where the coeﬃcients are
D3N
contact =−3cE
F4
πΛ
, D3N
OPE = cD
4F3
πΛ
gA
2Fπ
,
D3N
q2 = c3
F2
π
g2
A
4F2
π
, D3N
m2 =−2c1
F2
π
M2
πg2
A
4F2
π
,
D3N
xx = c4
2F2
π
g2
A
4F2
π
, (5.56)
with Λ = 700 MeV as the reference scale. There are two new dimensionless parameters cD and cE which
must be determined using at least two three-body observables. While we use the well-measured triton
binding energy as one parameter, it was summarized in Ref. [115] that cD and cE could be disentangled
by additionally including of nucleon-deuteron scattering, triton beta decays or some other observable in
the analysis. As this is beyond the scope of this work, we keep the correlation between cD and cE and we
ﬁx cD =−0.79 as it was shown to be ofO(1). Hence, we use cE as the only ﬁt parameter and ﬁx it with
the triton binding energy of E
3H
B =−8.4820(1) MeV . In the subsequent part of this chapter we also have a
look on systematic errors due to this particular choice of cD. Of course, there are better ways of ﬁxing cD
by now, but for the sake of consistency we have to use the same method that was employed in earlier
NLEFT calculations
As we are interested in the binding energy of the system, we have to calculate the ground state at large
enough volume or do an inﬁnite volume extrapolation for a three-particle system. Using a box volume of
V≈ (10· 1.97 fm)3≈ (12· 1.64 fm)3≈ (20 fm)3 for the two coarsest lattices is enough for neglecting the
ﬁnite volume eﬀects and it is still calculable with in a reasonable amount of computational resources.
Unfortunately, this volume is not computable with the given resources anymore for a lattice spacing of
a = 1.32 fm as the problem scales∝ L6. Finite volume binding energy corrections for three particles
61
Chapter 5 The Tjon band in Nuclear Lattice E ﬀective Field Theory
were calculated in the unitary limit as well as the shallow binding of one particle to a deeply bound dimer
in Refs. [87, 88, 90]. While the triton is a system between these two limits, the numerical di ﬀerence
between the two calculations is negligible once the volume is chosen large enough. Hence, we do an
inﬁnite volume extrapolation using the LO formula in the unitary limit given by
E3N (L) = E3N
∞ +A
exp
(
2κL√
3
)
(κL)
3
2
, (5.57)
whereκ =
√
−mE3N
∞ . We use all data points for L = 10 [l.u.] and larger as for smaller lattices the NLO
contributions of the ﬁnite volume corrections become signiﬁcant. Afterwards, we ﬁt each perturbative
higher-order operator⟨Oi⟩ according to
⟨Oi
⟩ (L) = ⟨Oi
⟩
∞ +Ai
exp
(
2κL√
3
)
(κL)
3
2
. (5.58)
