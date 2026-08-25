---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-046-results
section_title: "Results"
section_number: null
pages: 79-81
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
with coeﬃcients
ω0 = 49
36, ω 1 = 3
2, ω 2 = 3
20, ω 3 = 1
90. (6.14)
The lattice artifacts due to the free Hamiltonian start atO(a6). At LO, we have a contact interaction in
the two-boson sector,
VLO = C0
2
∑
n
: ρ2(n): , (6.15)
whereρ(n) = a†(n)a(n) and the :: symbols indicate normal ordering where the annihilation operators
stand to the right and the creation operators stand to the left. The lattice contact interaction is tuned to the
same value as the continuum-limit interaction, C0. At NLO we have a ﬁnite renormalization of the LO
interaction,
VNLO = ∆C0
2
∑
n
: ρ2(n): , (6.16)
which is suﬃcient to cancel the function A2(a) in Eq. (6.10).
At N2LO, two additional operators are required in the two-boson sector. The ﬁrst is proportional to
the square of the transferred momentum between particles,
VN2LO,q2 =−
Cq2
2 :
∑
n
ρ(n)[ρ(n + 1) +ρ(n− 1)− 2ρ(n)] :, (6.17)
and it removes the residual energy dependence C2(a) in Eq. (6.10) for on-shell two-boson scattering. The
second N2LO operator is a Galilean-invariance-restoring (GIR) term that is proportional to the square of
the total momentum,
VN2LO,GIR =−CGIR
8
∑
n
[
a†(n + 1)a†(n + 1)a(n)a(n) + a†(n− 1)a†(n− 1)a(n)a(n)
−2a†(n)a†(n)a(n)a(n)
]
.
(6.18)
We use this operator to correct the two-boson dispersion relation on the lattice, thereby removing the
B2(a) term in Eq. (6.10). One three-boson interaction is also needed at order N2LO,
VN2LO,3b = C3b
6
∑
n
: ρ3 (n) : , (6.19)
which cancels the contribution the function A3(a) in Eq. (6.11). In all of our lattice calculations, we must
also careful that ﬁnite volume errors are not being confused with lattice discretization errors. To this end,
we always take the volume to be suﬃciently large so that the ﬁnite volume errors are negligible.
6.4 Results
We now present lattice results at LO, NLO and N2LO and the discrepancies that remain when compared
with the zero-range continuum limit. All continuum observables are calculated with C0 =−0.1 and
m = 938.92 MeV , which give binding energies roughly comparable to that of the deuteron, triton and
helium-4. Of course, in the real world there is no ﬁve-body nucleonic state analogous to the ﬁve-boson
bound state we consider here. Nevertheless, our analysis of residual lattice errors for this bosonic system
will demonstrate the steps needed for systematic lattice improvement in nuclear lattice simulations.
73
Chapter 6 Lattice Improvement in Lattice E ﬀective Field Theory
row observable continuum result LO NLO N2LO
1 E2b
B −2.347 MeV 0.974(6) — —
2 r2b
rms 1.486 fm 0.997(3) 3.05(2) 4.1(3)
3 E3b
B −9.389 MeV 0.97(2) 2.97(2) —
4 r3b
rms 1.108 fm 0.97(2) 3.01(1) 4.0(3)
5 E4b
B −23.473 MeV 0.967(5) 3.05(1) 3.9(1)
6 r4b
rms 0.867 fm 0.97(1) 3.09(5) 4.1(2)
7 E5b
B −46.946 MeV 0.94(2) 3.21(4) 3.9(2)
8 r5b
rms 0.709 fm 0.86(5) 3.4(1) 4.0(2)
9 m2b
eﬀ 1877.8 MeV 2.91(9) 2.96(5) —
10 1/a2 46.946 MeV 0.978(6) 2.99(6) —
11 1/a3 0 MeV 2.80(3) 2.93(6) 4.08(3)
Table 6.1: Continuum observables and lattice error exponents bO as deﬁned in Eq. (6.21).
We vary the lattice spacing from a maximum of a = 1.97 fm to values as small as computationally
possible, while keeping the physical box length large enough so that ﬁnite volume eﬀects are negligible.
The determination of the lattice parameters are as follows. At LO, we consider the contact interaction
with the continuum value C0 =−0.1, and no ﬁtting is needed. At NLO we ﬁt ∆C0 to reproduce the
two-boson continuum bound-state energy E2b
B . At N2LO, we ﬁt the coe ﬃcients ∆C0, Cq2, CGIR and
C3b in order to simultaneously reproduce the continuum two-boson bound-state energy E2b
B , two-boson
eﬀective range r2, two-boson eﬀective mass meﬀ,2, and the three-boson bound-state energy E3b
B . We
determine the eﬀective range using Eq. (6.6) and compute the elastic scattering phase shifts at ﬁnite
volume using the relation [93],
exp[2iδ(p)] exp (ipL) = 1. (6.20)
Each lattice observable is ﬁtted using the asymptotic ﬁt function,
O(a) = Oc + AO· abO, (6.21)
where Oc is the zero-range continuum-limit value of the observable and AO and bO are ﬁt parameters in
the limit a→ 0. We show the LO bound state energies and root-mean-square radii for up to ﬁve bosons
in Fig. 6.4 as well as the best ﬁts using the asymptotic form in Eq. (6.21). The vertical lines give the
upper limits of the ﬁt range. The low-energy coupling constants are summarized in Tab. 6.2. As we see
from rows one through eight of Table 6.1, the LO exponent bO is consistent with 1. This is the same
as theO(a1) estimate we derived from our perturbative analysis and the A2(a) correction in Eq. (6.10).
While the lattice errors in the two-boson system are nearly linear in a over a fairly wide range, the higher
powers of a become stronger as we increase the number of bosons. This goes hand-in-hand with the
decreasing radius of the bound state, and is a signature that we are probing higher-momentum scales as
we increase the number of particles.
The NLO and N2LO bound state energies and root-mean-square radii for up to ﬁve boson are shown
in Fig. 6.5 as well as the best ﬁts using the asymptotic form in Eq. (6.21). The crosses indicate the NLO
results while the open circles are the N2LO results. The vertical lines gives the upper limits of the ﬁt
range. As shown in rows one through eight of Table 6.1, the NLO exponent bO is about 3 while the
N2LO exponent bO is about 4. This is consistent with ourO(a3) estimate of errors at NLO andO(a4)
estimate of errors at N2LO. We again see that the higher powers of a become stronger as we increase the
74
