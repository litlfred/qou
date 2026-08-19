---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-030-theoretical-framework
section_title: "Theoretical framework"
section_number: null
pages: 57-63
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
In the two-body sector we solve the LO non-pertubatively and we include the NLO and N2LO corrections
perturbatively. For the free part of the Hamiltonian, we use anO(a4)-improved version
Hfree = 1
2mN
∑
⃗n,i, j
2ω0a†
i, j
(⃗n) ai, j
(⃗n)
+
3∑
l=1
∑
ˆs
(−1)kωl
[
a†
i, j
(⃗n) ai, j
(⃗n + lˆs) + a†
i, j
(⃗n) ai, j
(⃗n− lˆs)] .
(5.1)
The coeﬃcientsωl represent the improved action including a stretching factor which connects theO(a4)
action with theO(a3) action to correct the dispersion relation of the nucleon-nucleon system. Explicitly
we use
ω0 = 10
(49
36− 5
4
)
+ 49
36, ω 1 = 10
(3
2− 4
3
)
+ 3
2,
ω2 = 10
( 3
20− 1
12
)
+ 3
20, ω 3 = 10
( 1
90− 0
)
+ 1
90.
(5.2)
For a more detailed discussion on this, see Sec. 4.2. In the LO potential, we include smeared contact
interaction operators which are projected on the S waves and the one-pion-exchange (OPE) potential.
The short-range contact interaction reads
HLO,contact =
∑
⃗n1,⃗n2
f (⃗n1−⃗n2
) :
c0ρa†,a(⃗n1)ρa†,a(⃗n2) + css
3∑
S =1
ρa†,a
S (⃗n1)ρa†,a
S (⃗n2)
+cii
3∑
I=1
ρa†,a
I (⃗n1)ρa†,a
I (⃗n2) + csi
3∑
S,I=1
ρa†,a
S,I (⃗n1)ρa†,a
S,I (⃗n2)
 :
(5.3)
with
c0 = (3C1S 0
+ 3C3S 1
)/16, css = (−3C1S 0
+ C3S 1
)/16,
cii = (C1S 0
− 3C3S 1
)/16, cis = (−C1S 0
− C3S 1
)/16.
(5.4)
f (⃗n) is the so-called smearing function, deﬁned by
f (⃗n) =F
 f−1
0 exp
−b⃗q 4
4


(⃗n) , (5.5)
withF denoting the Fourier transformation in the discrete space, and b is the smearing parameter.
Furthermore, the normalization constant is given by f0 = ∑
⃗q exp(−b⃗q 4/4). For the momentum-squared
51
Chapter 5 The Tjon band in Nuclear Lattice E ﬀective Field Theory
discretization we use also anO(a4) improved one,
⃗q 2 = 6ω0 + 2
3∑
l=1
3∑
s=1
(−1)nωs cos
(2sπkl
L
)
. (5.6)
As already argued in Ref. [32], this smearing improves theS wave description above a relative momentum
of 50 MeV , and hence reduces the clustering instability for the few-body systems like4He. The long-range
OPE is given by
HOPE =− g2
A
8F2
π
∑
S 1,S 2,I
∑
n1,n2
GS 1,S 2
(⃗n1−⃗n2
) : ρa†,a
S 1,I
(⃗n1
)ρa†,a
S 2,I
(⃗n2
) : (5.7)
where the pion propagator is
GS 1,S 2
(⃗q) =
qS 1qS 2
M2
π +⃗q 2 (5.8)
with
qS = sin
(2πkS
L
)
, (5.9)
in momentum space. The pion mass is Mπ = 134.98 MeV . For the pion-nucleon coupling constant
and the pion decay constant, we use the values gA = 1.29 (to account for the Goldberger-Treiman
discrepancy) and Fπ = 92.2 MeV . While there are various ways to regularize the long-range part with a
Gaussian smearing function in momentum space or an analog function directly in position space [22], a
similar analysis was done in Chapter 4 for the NLEFT approach where it was argued that the hard cut-oﬀ
regularization due to lattice spacing is suﬃcient for the values of a we use in this chapter.
The NLO contact interaction contribution consists of ten terms totally. First, we have to include two
operators which are not NLO operators by power counting but are necessary for accounting for the
back-reaction of the NLO ﬁts on the LO contribution. More precisely, for a coarse lattice spacing, these
represent the full non-local structure of the TPEP [82] while for ﬁner lattices they could be dropped. In
addition, these additional terms assure that the NLO contributions can be treated perturbatively. Therefore,
we keep them for consistency. These terms read,
V1
NLO = −∆C
2 :
∑
⃗n
ρ(⃗n)ρ(⃗n) :, (5.10)
V2
NLO = −
∆CI2
2 :
∑
⃗n
3∑
I=1
ρI
(⃗n)ρI
(⃗n) :. (5.11)
Then we have the seven standard NLO contact interactions,
V3
NLO = −
Cq2
2 :
∑
⃗n
3∑
l=1
ρ(⃗n)∇2
lρ(⃗n) :, (5.12)
V4
NLO = −
CI2,q2
2 :
∑
⃗n
3∑
I=1
3∑
l=1
ρI
(⃗n)∇2
lρI
(⃗n) :, (5.13)
V5
NLO = −
CS 2,q2
2 :
∑
⃗n
3∑
S =1
3∑
l=1
ρS
(⃗n)∇2
lρS
(⃗n) :, (5.14)
52
5.2 Two-body-sector
V6
NLO = −
CS 2,I2,q2
2 :
∑
⃗n
3∑
S,I=1
3∑
l=1
ρS,I
(⃗n)∇2
lρS,I
(⃗n) :, (5.15)
V7
NLO =
C(q·S )2
2 :
∑
⃗n
3∑
S =1
∇SρS
(⃗n) 3∑
S′=1
∇S′ρS′
(⃗n) :, (5.16)
V8
NLO =
CI2,(q·S )2
2 :
∑
⃗n
3∑
S =1
∇SρS,I
(⃗n) 3∑
S′=1
∇S′ρS′
(⃗n) :, (5.17)
V9
NLO = −
iCI=1
(q×S )·k
2 :
∑
⃗n
3∑
S =1
3∑
l,l′=1
εl,S,l′
[
Πl
(⃗n)∇l′ρS
(⃗n) + Π l,S
(⃗n)∇l′ρ(⃗n)]
:, (5.18)
withεa,b,c the totally antisymmetric Levi-Civita tensor in three dimensions. Finally, we also include the
following SO(3) breaking term
V10
NLO =
CS O(3)
2 :
∑
S
ρS
(⃗n)∇2
SρS
(⃗n) :, (5.19)
which allows us to remove lattice artefacts (unphysical partial wave mixing) due to rotational symmetry
breaking. Rotational symmetry breaking is caused by the breakdown of the continuum SO(3) group to
the SO(3, Z), which consists of a ﬁnite number of irreducible representations and consequently allows a
mixing of partial waves, which should not mix in the continuum. More details can be found in [33, 80,
82, 83, 132]. Speciﬁcally, this term is tuned to remove the mixing between the 3S 1-3D1 and the 3D3-3G3
channels, but the physical mixing like e.g. 3S 1-3D1 is of course not aﬀected. Unphysical partial wave
mixing in higher waves is so small that it can be ignored. More details of the notation can be found
App. B.
At N2LO, there are no further contact terms. Further, we need to include the TPEP at NLO and N2LO.
While they are largely absorbed in the NLO contact terms for a very coarse lattice, they play an important
role for ﬁner lattices [115]. At NLO, the TPEP reads
VTPEP
NLO =
∑
⃗n1,⃗n2

3∑
I=1
− : ρI
(⃗n1
)ρI
(⃗n2
) :
384π2F4
π
[
4M2
π
(
5g4
A− 4g2
A− 1
)
VTPEP,1
NLO (⃗n1−⃗n2)
+
(
23g4
A− 10g2
A− 1
)
VTPEP,2
NLO (⃗n1−⃗n2) + 48g4
AM4
πVTPEP,3
NLO (⃗n1−⃗n2)
]
− 3g4
A
64π2F4
π
:
3∑
S 1,S 2=1
VTPEP,4
NLO (⃗n1−⃗n2, S 1, S 2)ρS 1
(⃗n1
)ρS 2
(⃗n2
)
−
3∑
S =1
VTPEP,2
NLO (⃗n1−⃗n2)ρS
(⃗n1
)ρS
(⃗n2
) :


(5.20)
with the Fourier-transformed parts
VTPEP,1
NLO
(⃗n) =F [L(|⃗q|)](⃗n), (5.21)
VTPEP,2
NLO
(⃗n) =F
[
L(|⃗q|)⃗q 2 ](⃗n), (5.22)
53
Chapter 5 The Tjon band in Nuclear Lattice E ﬀective Field Theory
VTPEP,3
NLO
(⃗n) =F
L(|⃗q|)⃗q 2 1
4M2
π +⃗q 2

(⃗n), (5.23)
VTPEP,4
NLO (⃗n, S 1, S 2) =F
[
L(|⃗q|) qS 1qS 2
](⃗n), (5.24)
where
L (q) = 1
2q
√
4M2
π + q2 log
√
4M2
π + q2 + q
√
4M2
π + q2− q
, (5.25)
and|⃗q| =
√∑3
i=1 q2
i . Note that this notation is diﬀerent from Eq. (5.6), as the TPEP contributions should
be absorbed in the NLO contact interaction up toO(Q2).
At N2LO, the TPE potential has a subleading contribution given by
VTPEP
N2LO =
∑
⃗n1,⃗n2
− 3g2
A
16πF4
π
: ρ(⃗n1
)ρ(⃗n2
) :
×
[
2M2
π
(2c1− c3
) VTPEP,1
N2LO
(⃗n1−⃗n2
)− c3VTPEP,2
N2LO
(⃗n1−⃗n2
)]
− g4
Ac4
32πF4
π
:
3∑
S 1,S 2=1
ρS 1
(⃗n1
)ρS 2
(⃗n2
) VTPEP,3
N2LO
(⃗n1−⃗n2, S 1, S 2
)
−
3∑
S =1
ρS
(⃗n1
)ρS
(⃗n2
) VTPEP,4
N2LO (⃗n1−⃗n2):


(5.26)
with c1 =−1.10 GeV−1, c3 =−5.54 GeV−1 and c4 = 4.17 GeV−1 [46] and
A (q) = 1
2q arctan q
2Mπ
(5.27)
with
VTPEP,1
N2LO
(⃗n) =F
[
A(|⃗q|)(
2M2
π +⃗q 2)](⃗n), (5.28)
VTPEP,2
N2LO
(⃗n) =F
[
A(|⃗q|)
(
2M2
π +⃗q 2)
⃗q 2](⃗n), (5.29)
VTPEP,3
N2LO
(⃗n, S 1, S 2
) =F
[
A(|⃗q|)(
4M2
π +⃗q 2)
qS 1qS 2
](⃗n, S 1, S 2
), (5.30)
VTPEP,4
N2LO
(⃗n) =F
[
A(|⃗q|)(
4M2
π +⃗q 2)
⃗q 2](⃗n). (5.31)
Additionally, we also include corrections due to an improved version of the OPE and isospin-breaking
eﬀects due to the diﬀerent pion masses. The correction caused by an improved discretization is given by
VDx =− g2
A
8F2
π
∑
S 1,S 2,I
∑
⃗n1,⃗n2
[ ˜GS 1,S 2(⃗n1−⃗n2)− GS 1,S 2(⃗n1−⃗n2)
]
: ρa†,a
S 1,I(⃗n1)ρa†,a
S 2,I(⃗n2): , (5.32)
where the improved propagator is deﬁned as
˜GS 1,S 2
(⃗q) =
˜qS 1 ˜qS 2
M2
π +⃗q 2, (5.33)
54
5.2 Two-body-sector
with ˜qS = (4/3) sin(2πk/L) + (1/6) sin(4πk/L) and⃗q 2 according to Eq. (5.6).
The isospin corrections caused by the pion mass diﬀerences are deﬁned as
VIB =− g2
A
8F2
π
∑
S 1,S 2,I
∑
⃗n1,⃗n2
[ ¯GS 1,S 2(⃗n1−⃗n2)− GS 1,S 2(⃗n1−⃗n2)
]
: ρa†,a
S 1,I(⃗n1)ρa†,a
S 2,I(⃗n2): . (5.34)
The pion propagator with charged pions reads
¯GS 1,S 2
(⃗q) =
qS 1qS 2
M2
π± +⃗q 2. (5.35)
The charged pion mass is M± = 139.57 MeV . Note that since isospin breaking is an NLO correction, we
do not need to include the propagator discretization corrections analogous to Eqs. (5.32) and (5.33) for
the charged pion propagator in Eq. (5.35). Hence, the complete 2N N2LO Hamiltonian reads
H2N
N2LO =
10∑
i=1
V i
NLO + VTPEP
NLO + VTPEP
N2LO + VDx + VIB (5.36)
As we want to describe light nuclei in a later stage, we also have to include Coulomb forces as well as
proton-proton and neutron-neutron contact terms (for details, see Ref. [82]),
VCoul = αEM
2
∑
⃗n1,⃗n2
1
max(0.5,|⃗n1−⃗n2|) : ρp(⃗n1)ρp(⃗n2): , (5.37)
V pp =
C pp
2
∑
n
: ρp
(⃗n)ρp
(⃗n) : , (5.38)
V nn = Cnn
2
∑
n
: ρn
(⃗n)ρn
(⃗n) : . (5.39)
withαEM the electromagnetic ﬁne-structure constant and the projection densities are given in App. B.
Thus, the complete electromagnetic contribution reads
V2N
EM = VCoul + V pp + V nn. (5.40)
The alert reader might notice that V pp and V nn are really strong isospin-breaking terms. We book them
here, because V pp is used to renormalize the Coulomb potential.
Now, the Hamiltonian is deﬁned and, in the standard approach, we introduce a spherical wall boundary
on the relative separation between nucleons in order to compute scattering phase shifts. This spherical
wall is placed at radius Rwall outside the interaction region. We then solve for standing waves solutions of
the transfer matrix [33]
: exp [−αt
(Hfree + HLO
)] : |Ψ⟩ =λ|Ψ⟩, (5.41)
withαt = at/a and the energy given by
E =−log (λ)
αt
. (5.42)
The solutions must be identiﬁed with the correct partial wave, then one could use the energy shift between
the free and interacting system to calculate the phase shifts [61]. The NLO and N2LO energy corrections
are implemented perturbatively just by calculating the corresponding matrix element. In what follows,
55
Chapter 5 The Tjon band in Nuclear Lattice E ﬀective Field Theory
we utilize a more sophisticated procedure: Using the radial projection method we impose a spherical
wall, but we ﬁrst project the system onto its partial waves where the only degree of freedom is the radial
one. This projection accelerates the ﬁt procedures and is necessary particularly in the case of small lattice
spacings. Then the basis turns from a three-dimensional vector|⃗R⟩ to a radial basis|R⟩l,lz:
|R⟩l,lz =
∑
⃗R′
Yl,lz( ˆR′)δR,R′
⏐⏐⏐⏐⃗R′⟩
. (5.43)
Here, the Yl,lz are the spherical harmonics speciﬁed by their angular momentum l, lz. Consequently, all
operators are projected to a radial basis, too,
O(⃗R)→O (R), (5.44)
and the problem can be solved completely in the reduced basis analogous to Eqs. (5.41,5.42). Details of
the method can be found in Refs. [83, 133] where the projection, the binning, the new radial metric and
the extraction method for coupled channels are explained. In an uncoupled channel, the projected radial
wave function solutionψp
l (r) can be directly identiﬁed with the spherical Bessel functions in a region
between the interaction region and the spherical wall, which we conﬁne to be between Rin and Rout. Thus,
the phase shiftδl can be read oﬀ immediately,
ψp
l (r) =N p [cot(δl
) jl(pr) + nl(pr)], (5.45)
where p is the relative momentum,N p a normalization constant and jl(pr) and nl(pr) the spherical Bessel
functions of ﬁrst and second kind. For the perturbative energy corrections, we have to use the projected
potentials and the new phase shifts are calculated using the energy shifts according to Ref. [61]. For the
lattice spacing of a = 1.97 fm we use L = 32 [l.u.], Rwall = 14.02 [l.u.], Rin = 9.02 and Rout = 12.02 [l.u.].
For the smaller lattice spacings, we use the same values for these parameters in physical units (fm). For
the neutron-proton ﬁt procedure we follow Ref. [116]. In general, we do a χ2 ﬁt to partial wave analysis
data PW A, NijmI, NijmII and Reid93 of [134] according to [22],
χ2 =
∑
i
(
δi−δPW A
i
)2
∆2
i
(5.46)
where the error is deﬁned as ∆i = max[∆PW A
i ,|δNijmI
i −δPW A
i |,|δNijmII
i −δPW A
i |,|δReid93
i −δPW A
i |]. Further
details on errors and error propagation can be found in App. C. At LO we ﬁt the LECs C1S 0
and C3S 1
to the 1S 0 and 3S 1 channel up to 100 MeV , and we keep the smearing parameterb ﬁxed at b = 0.07.
While we could use it as a ﬁt parameter as well for the coarse lattice, it will cause some problem for
small lattice spacing. As one can see in Ref. [116], most of the partial waves are better described with
smaller lattice spacing except for the 1S 0 channel which becomes too strong. The reason is that the
LO smearing parameter is mainly determined by the 3S 1 channel due to the diﬀerent errors in the PW A
analysis. This e ﬀect is negligible for large lattice spacings but becomes sizable for smaller ones and
worsens the prediction of the 1S 0 wave. Hence, we keep the smearing parameter close to the ﬁt value for
a = 1.97 fm and all corrections are done by NLO and N2LO insertions.
Once the LO is ﬁxed, we include isospin-breaking e ﬀects, the improved description of the OPEP,
the TPEP at NLO and N2LO as well as the NLO contact terms. We ﬁt all remaining coeﬃcients to S
and P waves up to 150 MeV momentum as well as the deuteron binding energy. Afterwards we ﬁt the
proton-proton interaction term to the pp 1S 0 phase shift and the neutron-neutron interaction term to the
56
5.2 Two-body-sector
