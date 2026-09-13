---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-037-411-preparations
section_title: "Preparations"
section_number: 4.1.1
pages: 90-103
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The exact PIMC expectation value of operator ˆO is calculated by Eq.(2.3) and
therefore Eq.(2.11), and we need to choose a proper total imaginary time τ and time
step ∆τ to project out the ground state |Φ0⟩. In this section, we discuss the choice of
τ and ∆τ and use 4He as an example.
From Eq.(2.6) we can see that, the residual amount of excited states depends on
the ratio ai/a0 and the factor e−(Ei−E0)τ1. We have to make sure that the coeﬃcient of
the ﬁrst excited state|Φ1⟩ is negligible compared with the ground state |Φ0⟩.
The experimental ground state energy E0 of 4He is about -28.3 MeV and the
ﬁrst excited state energy E1 is the energy of a separated nucleon and triton, -8 MeV
(Tilley et al. (1992)). The energy diﬀerence E1−E0 is about -20 MeV. If we choose
τ1 = 0.1 MeV−1 then e−(E1−E0)τ1 will be e−2≈ 0.135. If there is only |Φ0⟩ and|Ψ1⟩
in|ΨT⟩, and if|a1/a0| is small enough, then the percentage of the ﬁrst excited state
|Φ1⟩ in|ΨT⟩ will be greatly suppressed by |a1/a0e−(E1−E0)τ1|, therefore e−Hτ1|ΨT⟩ is
dominated by the ground state |Φ0⟩. In fact, if there are other excited states in |ΨT⟩,
the ground state|Φ0⟩ will be projected out even sooner, because|a1/a0| will be smaller
for a good trial wave function and other excited states |Φi⟩ will die out faster than
|Φ1⟩ due to the factor |ai/a0e−(Ei−E0)τ1|. So, even a less than 0.1 MeV−1 imaginary
time τ1 may still be adequate.
The analysis above suggests that τ1 = 0.1 MeV−1 should be enough for our PIMC
80
to project out the ground state. Since we usually put operator ˆO in the middle of
two propagators as⟨ΨT|e−Hτ1 ˆOe−Hτ2|ΨT⟩ as shown in Eq.(2.3), and we usually set
τ1 =τ2, so we can conclude that the total imaginary time τ for our PIMC calculations
can be set as τ = 2τ1 = 2× 0.1 = 0.2 MeV−1. In our PIMC calculations, besides using
τ = 0.2 MeV−1, and we also show results with τ = 0.15 MeV−1 and τ = 0.3 MeV−1
for comparisons. The total imaginary time for chiral N 2LO interaction has a similar
range and τ = 0.2 MeV−1 should be enough as well.
Given a total imaginary time τ, for the time step ∆τ, we need to consider the
computational cost and the accuracy. In GFMC (Carlson (1987)), ∆τ is usually chosen
to be 10−5∼ 10−4 MeV−1. In our PIMC calculation, we ﬁnd that a10−4∼ 10−3 MeV−1
time step ∆τ works reasonably well. Depending on τ and ∆τ, the number of beads for
PIMC ranges from 41 to 1501. In the most time consuming case, forτ = 0.3 MeV−1 and
∆τ = 2× 10−4 MeV−1, we need 1500 short-time propagators and therefore 1501 beads.
Such a calculation (all the calculations are performed at the Agave Cluster at Research
Computing at Arizona State University), in order to reach a less than 0.02 MeV error
in the ground state energy calculation, takes about 20 thousand core hours for the
chiral N2LO interaction and 13 thousand core hours for the AV6’ interaction. For 41
beads it takes about 240 core hours to reach less than 0.02 MeV error, which means it
can be done on a modern laptop in few days or less.
4.1.2 Calculations
The calculation of the ground state energy E0 can be recast into the form of
Eq.(2.87) as discussed in section 2.7.1, with the operator ˆO being the Hamiltonian
H =T +V . And we calculate the ground state energy E0 by
E0(∆τ) =
1
2Re
{
⟨ΨT|H[U(∆τ)]N|ΨT⟩ +⟨ΨT|[U(∆τ)]NH|ΨT⟩
}
Re⟨ΨT|[U(∆τ)]N|ΨT⟩ , (4.1)
81
which in the limit of ∆τ = 0 becomes the true expectation E0 as shown in Eq.(2.12),
E0 =
1
2Re
(
⟨ΨT|He−Hτ|ΨT⟩ +⟨ΨT|e−HτH|ΨT⟩
)
Re⟨ΨT|e−Hτ|ΨT⟩ . (4.2)
The the corresponding g(R)lr takes the form of Eq.(2.108) which can be written as,
g(R)lr = 1
2
[∑
S
⟨ψl
T|H|R0S⟩⟨S|ψr
0(R)⟩ +
∑
S
⟨ψl
N(R)|S⟩⟨RNS|H|ψr
T⟩
]
gF (R), (4.3)
and the corresponding gV
lr,M(R) is,
gV
lr,M(R) =



∑
S
⟨ψl
T|H|R0S⟩⟨S|ψr
0(R)⟩, M = 0.
∑
S
⟨ψl
N(R)|S⟩⟨RNS|H|ψr
T⟩, M =N.
(4.4)
All the other functions are the same as discussed in section 2.7.1.
The calculations of ⟨RS|H|ψr
T⟩ and⟨ψl
T|H|RS⟩ are straightforward. First, they
can be calculated as,
⟨RS|H|ψr
T⟩ =⟨RS|T|ψr
T⟩ +⟨RS|V|ψr
T⟩, (4.5)
⟨ψl
T|H|RS⟩ =⟨ψl
T|T|RS⟩ +⟨ψl
T|V|RS⟩. (4.6)
Then, with the help of Eqs.(2.62) and (2.53), taking 4He as an example, the potential
energy part becomes,
⟨RS|V|ψr
T⟩=
⟨
S
⏐⏐⏐⏐⏐
{
∑
i<j
[
VNN
ij (rij)+VEM
ij (rij)
]
}∏r
i<j
[ 6∑
p=1
fp
ij(rij)Op
ij
] 96∑
N=1
φN
⏐⏐⏐⏐⏐N
⟩
,(4.7)
⟨ψl
T|V|RS⟩=
96∑
N=1
⟨
N
⏐⏐⏐⏐⏐φ∗
N
{
∑
i<j
[
VNN
ij (rij)+VEM
ij (rij)
]
}∏l
i<j
[ 6∑
p=1
fp
ij
∗(rij)Op
ij
]⏐⏐⏐⏐⏐S
⟩
.(4.8)
For the kinetic energy operator T we have,
⟨RS|T|ψr
T⟩=
4∑
i=1
−ℏ2∇2
i
2m ⟨RS|ψr
T⟩=− ℏ2
2m
4∑
i=1
(
d2
dx2
i
+ d2
dy2
i
+ d2
dz2
i
)
⟨RS|ψr
T⟩, (4.9)
⟨ψl
T|T|RS⟩=
4∑
i=1
−ℏ2∇2
i
2m ⟨ψl
T|RS⟩=− ℏ2
2m
4∑
i=1
(
d2
dx2
i
+ d2
dy2
i
+ d2
dz2
i
)
⟨ψl
T|RS⟩. (4.10)
82
The 2nd order derivatives in Eqs.(4.9) and (4.10) are calculated numerically by using
the 2nd order central ﬁnite diﬀerence formula (Fornberg (1988)) 1 .
In our PIMC calculations for 4He, we include 2000 steps in one block. A step
means any one of the trial moves described in section 3.2, it can be either accepted or
rejected. We adjusted the number of beads for multi-level sampling as well as the step
parameters for regular sampling, and ﬁnd out the samples are uncorrelated after 125
steps so that each block is uncorrelated with the others (we make sure the samples of
the root mean square radius rm at the middle bead are uncorrelated). We typically
calculate the ground-state energy E0, r2
m, potential VNN +VEM along the beads, and
one-particle number density ρ(r). We begin to take samples after running several
blocks from the initial condition in order to reach the equilibrium.
In Fig. 4.1, we show the calculation of the 4He ground state energy E0 for diﬀerent
total imaginary time τ = 0.15 MeV−1, τ = 0.2 MeV−1 and τ = 0.3 MeV−1, with
various time steps ∆τ. As discussed in section 4.1.1, at τ = 0.2 MeV−1, we can expect
the true ground state energy E0 for 4He to be located within our calculated ground
state energy within its error bar. We added τ = 0.15 MeV−1 and τ = 0.3 MeV−1 for
comparison. Particularly, we can see that for∆τ <5×10−4 MeV−1, forτ = 0.2 MeV−1
and τ = 0.3 MeV−1, all of the calculated E0 are almost the same within their error
bars. Forτ = 0.15 MeV−1, the smallest ∆τ we use is 1.5× 10−4 MeV−1 which means
1000 short-time propagators and 1001 beads, and its E0 is−26.155± 0.008 MeV.
1For example, for xi the x coordinate of particle i, it is calculated as,
d2⟨RS|ψr
T⟩
dx2
i
=
⟨Rx+
i
S|ψr
T⟩+⟨Rx−
i
S|ψr
T⟩−2⟨RS|ψr
T⟩
∆2 , (4.11)
d2⟨ψl
T|RS⟩
dx2
i
=
⟨ψl
T|Rx+
i
S⟩+⟨ψl
T|Rx−
i
S⟩−2⟨ψl
T|RS⟩
∆2 . (4.12)
where ∆ is the spatial ﬁnite diﬀerence which is set as about 10−2 fm in our calculations. Rx+
i
means
keeping all the other coordinates in the conﬁguration of the system R the same and just change xi to
xi + ∆, and Rx−
i
means change xi to xi− ∆.
83
/s48/s46/s48 /s48/s46/s49 /s48/s46/s50 /s48/s46/s51 /s48/s46/s52 /s48/s46/s53 /s48/s46/s54 /s48/s46/s55 /s48/s46/s56 /s48/s46/s57 /s49/s46/s48 /s49/s46/s49 /s49/s46/s50 /s49/s46/s51
/s45/s50/s54/s46/s51/s53
/s45/s50/s54/s46/s51/s48
/s45/s50/s54/s46/s50/s53
/s45/s50/s54/s46/s50/s48
/s45/s50/s54/s46/s49/s53
/s71/s114/s111/s117/s110/s100/s32/s115/s116/s97/s116/s101/s32/s101/s110/s101/s114/s103/s121/s32/s40/s77/s101/s86/s41
/s84/s105/s109/s101/s32/s115/s116/s101/s112/s32 /s40 /s49/s48
/s45/s51/s32
/s77 /s101/s86
/s45/s49
/s41
/s71/s70/s77 /s67
/s65/s70/s68/s77 /s67
/s32/s61/s32/s48/s46/s49/s53/s32/s77 /s101/s86
/s45/s49
/s32/s61/s32/s48/s46/s50/s48/s32/s77 /s101/s86
/s45/s49
/s32/s61/s32/s48/s46/s51/s48/s32/s77 /s101/s86
/s45/s49
/s52
/s72/s101
Figure 4.1: Energy vs. time step ∆τ for diﬀerent total imaginary time τ for 4He based
on the AV6’ potential (quadratic range).
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48 /s51/s46/s53 /s52/s46/s48 /s52/s46/s53 /s53/s46/s48
/s45/s50/s54/s46/s52
/s45/s50/s54/s46/s51
/s45/s50/s54/s46/s50
/s45/s50/s54/s46/s49
/s45/s50/s54/s46/s48
/s45/s50/s53/s46/s57
/s45/s50/s53/s46/s56
/s45/s50/s53/s46/s55
/s45/s50/s53/s46/s54
/s45/s50/s53/s46/s53
/s71/s114/s111/s117/s110/s100/s32/s115/s116/s97/s116/s101/s32/s101/s110/s101/s114/s103/s121/s32/s40/s77/s101/s86/s41
/s84/s105/s109/s101/s32/s115/s116/s101/s112/s32 /s40 /s49/s48
/s45/s51/s32
/s77 /s101/s86
/s45/s49
/s41
/s71/s70/s77 /s67
/s65/s70/s68/s77 /s67
/s32/s61/s32/s48/s46/s49/s53/s32/s77 /s101/s86
/s45/s49
/s32/s61/s32/s48/s46/s50/s48/s32/s77 /s101/s86
/s45/s49
/s32/s61/s32/s48/s46/s51/s48/s32/s77 /s101/s86
/s45/s49
/s52
/s72/s101
Figure 4.2: Energy vs. time step ∆τ for diﬀerent total imaginary time τ for 4He based
on the AV6’ potential (wide range).
84
/s48/s46/s48 /s48/s46/s49 /s48/s46/s50 /s48/s46/s51 /s48/s46/s52 /s48/s46/s53 /s48/s46/s54 /s48/s46/s55 /s48/s46/s56 /s48/s46/s57 /s49/s46/s48 /s49/s46/s49 /s49/s46/s50 /s49/s46/s51
/s45/s50/s53/s46/s50/s53
/s45/s50/s53/s46/s50/s48
/s45/s50/s53/s46/s49/s53
/s45/s50/s53/s46/s49/s48
/s45/s50/s53/s46/s48/s53
/s45/s50/s53/s46/s48/s48
/s45/s50/s52/s46/s57/s53
/s45/s50/s52/s46/s57/s48
/s45/s50/s52/s46/s56/s53
/s45/s50/s52/s46/s56/s48
/s67/s104/s105/s114/s97/s108/s32/s78
/s50
/s76/s79/s32/s103/s114/s111/s117/s110/s100/s32/s115/s116/s97/s116/s101/s32/s101/s110/s101/s114/s103/s121/s32/s40/s77/s101/s86/s41
/s84/s105/s109/s101/s32/s115/s116/s101/s112/s32 /s40 /s49/s48
/s45/s51/s32
/s77 /s101/s86
/s45/s49
/s41
/s71/s70/s77 /s67
/s65/s70/s68/s77 /s67
/s32/s61/s32/s48/s46/s50/s48/s32/s77 /s101/s86
/s45/s49
/s32/s61/s32/s48/s46/s51/s48/s32/s77 /s101/s86
/s45/s49
/s52
/s72/s101
Figure 4.3: Energy vs. time step ∆τ for diﬀerent total imaginary time τ for 4He based
on the local chiral N 2LO interaction (linear range).
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48 /s51/s46/s53 /s52/s46/s48 /s52/s46/s53 /s53/s46/s48
/s45/s50/s53/s46/s51/s48
/s45/s50/s53/s46/s50/s53
/s45/s50/s53/s46/s50/s48
/s45/s50/s53/s46/s49/s53
/s45/s50/s53/s46/s49/s48
/s45/s50/s53/s46/s48/s53
/s45/s50/s53/s46/s48/s48
/s45/s50/s52/s46/s57/s53
/s45/s50/s52/s46/s57/s48
/s45/s50/s52/s46/s56/s53
/s45/s50/s52/s46/s56/s48
/s67/s104/s105/s114/s97/s108/s32/s78
/s50
/s76/s79/s32/s103/s114/s111/s117/s110/s100/s32/s115/s116/s97/s116/s101/s32/s101/s110/s101/s114/s103/s121/s32/s40/s77/s101/s86/s41
/s84/s105/s109/s101/s32/s115/s116/s101/s112/s32 /s40 /s49/s48
/s45/s51/s32
/s77 /s101/s86
/s45/s49
/s41
/s71/s70/s77 /s67
/s65/s70/s68/s77 /s67
/s32/s61/s32/s48/s46/s50/s48/s32/s77 /s101/s86
/s45/s49
/s32/s61/s32/s48/s46/s51/s48/s32/s77 /s101/s86
/s45/s49
/s52
/s72/s101
Figure 4.4: Energy vs. time step ∆τ for diﬀerent total imaginary time τ for 4He based
on the local chiral N 2LO interaction (wide range).
85
Forτ = 0.2 MeV−1, the smallest ∆τ we use is 1.5× 10−4 MeV−1 which means 1333
short-time propagators and 1334 beads, and its E0 is−26.162± 0.004 MeV. For
τ = 0.3 MeV−1, the smallest ∆τ we use is 2× 10−4 MeV−1 which means 1500 short-
time propagators and 1501 beads, and its E0 is−26.173± 0.006 MeV.
Also, as pointed out in section 2.5 and by Eq.(2.79), for the AV6’ interaction, our
PIMC results should contain even orders of ∆ τ error comparing with the true ground
state results for small time step ∆τ. Usually we do an extrapolation at ∆ τ 2 order,
⟨ ˆO(∆τ)⟩ =⟨ ˆO⟩ +C2∆τ 2. (4.13)
In order to do extrapolation by using Eq.(4.13), we need to ﬁnd the range of ∆τ
where the error of ∆τ 2 dominates, so that we can observe a clear ∆ τ 2 dependence of
⟨ ˆO(∆τ)⟩. As a rough estimation, by looking at Eq.(2.79) we would require|C2∆τ2
C4∆τ4|≫ 1.
There are combinations of commutator terms of kinetic energy T and potential V in
coeﬃcients C2 and C4. For example there can be TTV in C2 and TTTTV in C4 and
we can roughly estimate|C2∆τ2
C4∆τ4| as| Re⟨ΨT|TTV |ψT⟩
Re⟨ΨT|TTTTV |ψT⟩∆τ2|. For the AV6’ interaction, the
magnitude of T and V are 102 MeV order, so|C2∆τ2
C4∆τ4|≈| Re⟨ΨT|TTV |ψT⟩
Re⟨ΨT|TTTTV |ψT⟩∆τ2| may be
roughly estimated as|C2∆τ2
C4∆τ4|≈| 106
1010∆τ2| =| 1
104∆τ2|. In order to make sure|C2∆τ2
C4∆τ4|≫ 1,
we may expect ∆τ to be around 10−4∼ 10−3 MeV−1.
We ﬁnd that in Fig. 4.1 we can observe a clear ∆ τ 2 dependence when ∆τ <1.3×
10−3 MeV−1, and by using Eq.(4.13), the true ground state energy E0 is extrapolated
to−26.16(1) MeV. This is consistent with GFMC result (Wiringa and Pieper (2002))
which is E0 = −26.15(2) MeV. This is reasonable because in this work, we are
summing over all the spin and isospin states like GFMC does. So our results should
be comparable with GFMC’s. The diﬀerence is that GFMC is a DMC method based
on Eq.(2.13), and we are doing a PIMC calculation based on Eq.(2.3).
In Fig. 4.3 we show the results of 4He based on the local chiral N 2LO two-body
86
interaction. We choose the coordinate space cutoﬀ (Gezerlis et al. (2014)) as R0 = 1.2
fm. As discussed in section 2.5 and Eq.(2.83), due to the existence of the spin-orbit
operator, a ∆τ error will exist in evaluating ⟨ ˆO(∆τ)⟩. We do observe the ∆τ error
dominates when ∆τ <1.3×10−3 MeV−1. So we do a linear extrapolation in this range
for the chiral interaction,
⟨ ˆO(∆τ)⟩ =⟨ ˆO⟩ +C1∆τ, (4.14)
and the extrapolated ground-state energy is found to be E0 =−24.99(1) MeV.
Fig. 4.2 shows a wider range of ∆ τ than Fig. 4.1, and we use Eq.(2.78) up to ∆ τ 4
in both the numerator and the denominator to do the ﬁtting for all the data points.
In Fig. 4.4 we ﬁt the wide range of the data by using Eq.(2.83) up to ∆ τ 3.
Table 4.1: The AV6’ interaction based light nuclei ground state energies.
AZ EPIMC
0 (MeV) τ (MeV−1) EGFMC
0 (MeV) EEXPT
0 (MeV)
2H −2.24(4) 0.5 -2.22
3H −7.953(5) 0.4 −7.95(1) -8.48
3He −7.336(6) 0.5 -7.72
4He −26.162(4) 0.2 −26.15(2) -28.30
Table 4.2: The local chiral N 2LO interaction based light nuclei ground state energies.
AZ EPIMC
0 (MeV) τ (MeV−1) EGFMC
0 (MeV) EAFDMC
0 (MeV) EEXPT
0 (MeV)
2H −2.203(2) 0.5 -2.22
3H −7.74(1) 0.4 −7.74(1) −7.76(3) -8.48
3He −7.11(1) 0.5 −7.01(1) −7.12(3) -7.72
4He −25.00(1) 0.2 −24.86(1) −25.17(5) -28.30
87
The ground state energy for all the A≤ 4 nuclei are listed in Table 4.1 for the
AV6’ interaction and in Table 4.2 for the chiral N 2LO interaction. The GFMC and
AFDMC results (Lonardoni et al. (2018b)) are listed for comparison. Overall, all the
PIMC, GFMC and AFDMC results are consistent with each other within 1% error.
We also listed the experimental value of the binding energies (Wiringa and Pieper
(2002); Lee (2020); Wikipedia contributors (2020c)) for comparison. The diﬀerence
between the experimental values EEXPT
0 and our results is mainly due to the absence
of the three body interactions in our calculations.
4.1.3 Veriﬁcations
In order to further support our conclusion that τ = 0.2 MeV−1 indeed projected
out the ground state and therefore our PIMC results are reliable, we calculate the
potential V =VNN +VEM along all the beads on the path. This is a typical quantity
to calculate in PIMC calculations (Sarsa et al. (2000)). The calculation is done in the
same way as introduced in section 2.7.1. We just need to use the potential operator V
as the operator ˆO, and we place the V at each imaginary time position from bead 0 to
the last bead N on the path. In other words, the gV
lr,M(R) in Eq.(2.107) needs to be
calculated from M = 0 to M =N =τ/∆τ. In this way, we are actually calculating
⟨V (τ1)⟩ which is,
⟨V (τ1)⟩ = Re⟨ΨT|e−Hτ1
(
VNN +VEM)
e−H(τ−τ1)|ΨT⟩
Re⟨ΨT|e−Hτ|ΨT⟩ , (4.15)
where τ1 ranges from 0 MeV−1 to τ as we put the V operator from bead 0 to bead
N.⟨V (τ1)⟩ is symmetric around τ1 =τ/2. When τ/2 is big enough to project out the
ground state,⟨V (τ/2)⟩ is the ground state potential energy.
In Fig. 4.5 2 , we show the results of⟨V (τ1)⟩ as a functions of τ1 forτ = 0.2 MeV−1
2Note that the potential operators and the Hamiltonian do not commute, so the eigenstates of
88
/s48/s46/s48/s48 /s48/s46/s48/s53 /s48/s46/s49/s48 /s48/s46/s49/s53 /s48/s46/s50/s48
/s45/s49/s53/s53
/s45/s49/s53/s48
/s45/s49/s52/s53
/s45/s49/s52/s48
/s45/s49/s51/s53
/s45/s49/s51/s48
/s45/s49/s50/s53
/s52
/s72/s101
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s101/s86
/s45/s49
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s101/s86
/s45/s49
/s86
/s78/s78
/s43/s86
/s69/s77/s32
/s40/s77/s101/s86/s41
/s52
/s72/s101
/s48/s46/s48/s48 /s48/s46/s48/s53 /s48/s46/s49/s48 /s48/s46/s49/s53 /s48/s46/s50/s48 /s48/s46/s50/s53 /s48/s46/s51/s48
/s45/s49/s50/s55
/s45/s49/s50/s54
/s45/s49/s50/s53
/s45/s49/s50/s52
/s45/s49/s50/s51
/s32/s32/s40/s77/s101/s86
/s45/s49
/s41
Figure 4.5: The potential energy along the beads for τ = 0.2 and 0.3 MeV−1 for 4He
based on the AV6’ interaction.
/s48/s46/s48/s48 /s48/s46/s48/s53 /s48/s46/s49/s48 /s48/s46/s49/s53 /s48/s46/s50/s48
/s45/s49/s48/s53
/s45/s49/s48/s52
/s45/s49/s48/s51
/s45/s49/s48/s50
/s45/s49/s48/s49
/s45/s49/s48/s48
/s45/s57/s57
/s52
/s72/s101
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s101/s86
/s45/s49
/s32/s32
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s32
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s32
/s45/s52
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s45/s51
/s32/s77 /s101/s86
/s45/s49
/s101/s86
/s45/s49
/s86
/s78/s78
/s43/s86
/s69/s77/s32
/s40/s77/s101/s86/s41
/s52
/s72/s101
/s48/s46/s48/s48 /s48/s46/s48/s53 /s48/s46/s49/s48 /s48/s46/s49/s53 /s48/s46/s50/s48 /s48/s46/s50/s53 /s48/s46/s51/s48
/s45/s49/s48/s52
/s45/s49/s48/s51
/s45/s49/s48/s50
/s45/s49/s48/s49
/s45/s49/s48/s48
/s45/s57/s57
/s32/s32/s40/s77/s101/s86
/s45/s49
/s41
Figure 4.6: The potential energy along the beads for τ = 0.2 and 0.3 MeV−1 for 4He
based on the local chiral N 2LO interaction.
89
andτ = 0.3 MeV−1. On the upper panel of Fig. 4.5, we show for diﬀerent time step ∆τ
how⟨V (τ1)⟩ change as τ1 from 0 MeV−1 to the total imaginary time τ = 0.2 MeV−1.
As expected, since PIMC is projecting out the Hamiltonian’s ground state, and the
Hamiltonian’s ground state is not the same as the potential operator’s eigenstate, the
time step error introduced by ∆τ will have noticeable impact on⟨V (τ1)⟩. That is why
the curve of⟨V (τ1)⟩ vs.τ1 are diﬀerent for diﬀerent∆τ. However, as ∆τ decreases, time
step error will become smaller and smaller. And indeed, as we can see, the result for
∆τ = 1.5×10−4 MeV−1 almost coincides with that of ∆τ = 2.5×10−4 MeV−1.⟨V (τ1)⟩
is about−127∼− 123 MeV. It looks like⟨V (τ1)⟩ has converged when ∆τ≤ 2.5×10−4
MeV−1. This is a clear signal that a stable eigenstate of the Hamiltonian for τ = 0.2
MeV−1 has been reached, and smaller ∆τ and therefore more beads will not improve
the convergence. Furthermore, in order to verify if this eigenstate is truly the ground
state, we calculate for a larger total imaginary time of τ = 0.3 MeV−1 with a similar
time step ∆τ = 2× 10−4 MeV−1, i.e. 1501 beads. The result is in the lower panel of
Fig. 4.5. Indeed, the curve of ⟨V (τ1)⟩ vs. τ1 is almost the same as the τ = 0.2 MeV−1
and ∆τ≤ 2.5× 10−4 MeV−1 cases. This means further increasing the total time τ
will not change the state, so the stable state reached for τ = 0.2 MeV−1 must be the
ground state.
Therefore, the ground state of the Hamiltonian is indeed reached when τ = 0.2
MeV−1, and ∆τ around 1.5∼ 2.5× 10−4 MeV−1 is small enough. Besides, from Fig.
4.5 we can see that in the area when 0.075 MeV−1≤τ1≤ 0.125 MeV−1 for τ = 0.2
MeV−1, and the area when 0.075 MeV−1≤τ1≤ 0.225 MeV−1 forτ = 0.3 MeV−1, the
curves of⟨V (τ1)⟩ vs.τ1 are almost ﬂat. So that even τ = 2× 0.075 = 0.15 MeV−1 may
the potential operators and the Hamiltonian are not the same. So even when the system reaches the
ground state of its Hamiltonian, this ground state |Φ0⟩ is not an eigenstate of the potential operators.
So⟨V (τ1)⟩ has larger ﬂuctuations than ⟨H(τ1)⟩. So in order to make Fig. 4.5 look ‘smooth’, we need
to take a longer computation time than computing the ground state energy.
90
be suﬃcient to project out the ground state. Fig. 4.6 is a similar graph for the local
chiral interaction which also indicates τ = 0.2 MeV−1 is suﬃcient 3 .
/s50/s46/s48
/s49/s46/s57
/s49/s46/s56
/s49/s46/s55
/s49/s46/s54
/s49/s46/s53
/s49/s46/s52
/s49/s46/s51
/s49/s46/s50
/s49/s46/s49
/s49/s46/s48
/s48/s46/s57
/s48/s46/s56
/s48/s46/s55
/s45/s48/s46/s54 /s45/s48/s46/s53 /s45/s48/s46/s52 /s45/s48/s46/s51 /s45/s48/s46/s50 /s45/s48/s46/s49 /s48/s46/s48 /s48/s46/s49 /s48/s46/s50 /s48/s46/s51 /s48/s46/s52 /s48/s46/s53 /s48/s46/s54
/s48/s46/s48
/s48/s46/s49
/s48/s46/s50
/s48/s46/s51
/s48/s46/s52
/s48/s46/s53
/s48/s46/s54
/s48/s46/s55
/s48/s46/s56
/s48/s46/s57
/s49/s46/s48
/s66
/s49
/s40 /s41
/s69
/s49
/s47/s69
/s48
/s48/s46/s48
/s48/s46/s49
/s48/s46/s50
/s48/s46/s51
/s48/s46/s52
/s48/s46/s53
/s48/s46/s54
/s48/s46/s55
/s48/s46/s56
/s48/s46/s57
/s49/s46/s48
/s49/s46/s49
/s49/s46/s50
/s49/s46/s51
/s49/s46/s52
/s49/s46/s53
/s49/s46/s54
/s49/s46/s55
/s49/s46/s56
/s49/s46/s57
/s50/s46/s48
/s50/s46/s49
/s50/s46/s50
/s50/s46/s51
/s50/s46/s52
/s50/s46/s53
/s50/s46/s54
/s50/s46/s55
/s50/s46/s56
/s50/s46/s57
/s51/s46/s48
/s82
/s40/s49/s41
/s83
/s40 /s41
Figure 4.7: PIMC leading order structure function R(1)
S (τ, ∆τ).
Besides checking the potential along the beads, the robustness of the ground state
energy PIMC calculation can be understood as follows.
The trial state |ΨT⟩, after operating with [U(∆τ)]N, can be expanded by the
eigenstates of the Hamiltonian,
[U(∆τ)]N|ΨT⟩ =
∞∑
n=0
An(τ, ∆τ)|Φn⟩ =A0(τ, ∆τ)
[
|Φ0⟩ +
+∞∑
i=1
Ai(τ, ∆τ)
A0(τ, ∆τ)|Φi⟩
]
. (4.16)
where An(τ, ∆τ) are the coeﬃcients which depend on τ and ∆τ for|Φn⟩. We know
3In order to save computation time, we did not include spin-orbit interaction, but it does not alter
the conclusion. Fig. 4.6 is not as smooth as Fig. 4.5 simply because we used fewer core hours for it
than we did for Fig. 4.5.
91
that lim
∆τ→0
[U(∆τ)]N =e−Hτ and we also notice from Eq.(2.6) that,
e−Hτ|ΨT⟩ =a0e−E0τ
[
|Φ0⟩ +
∞∑
i=1
ai
a0
e−(Ei−E0)τ|Φi⟩
]
, (4.17)
So, comparing Eq.(4.16) and Eq.(4.17) we ﬁnd that for ∆ τ→ 0,
lim
∆τ→0
A0(τ, ∆τ) =a0e−E0τ, (4.18)
lim
∆τ→0
An(τ, ∆τ)
A0(τ, ∆τ) = an
a0
e−(En−E0)τ⇒ lim
τ→∞
[
lim
∆τ→0
An(τ, ∆τ)
A0(τ, ∆τ)
]
= 0. (4.19)
We calculate the ground state energy by using Eq.(4.1), the two parts in it are
essentially the same and we pick one of them to take a closer look. We ﬁnd
⟨ΨT|H[U(∆τ)]N|ΨT⟩
⟨ΨT|[U(∆τ)]N|ΨT⟩ =E0
1 +∑+∞
i=1
a∗
iAi(τ,∆τ)Ei
a∗
0A0(τ,∆τ)E0
1 +∑+∞
i=1
a∗
iAi(τ,∆τ)
a∗
0A0(τ,∆τ)
≡E0RS(τ, ∆τ), (4.20)
since Eq.(4.20) is real, we deﬁne a real function RS(τ, ∆τ) as our PIMC error structure
function,
RS(τ, ∆τ)≡Re
1 +∑+∞
i=1
a∗
iAi(τ,∆τ)Ei
a∗
0A0(τ,∆τ)E0
1 +∑+∞
i=1
a∗
iAi(τ,∆τ)
a∗
0A0(τ,∆τ)
, (4.21)
and we can deﬁne its cutoﬀ functions R(n)
S (τ, ∆τ) such that
R(n)
S (τ, ∆τ)≡Re
1 +∑n
i=1
a∗
iAi(τ,∆τ)Ei
a∗
0A0(τ,∆τ)E0
1 +∑n
i=1
a∗
iAi(τ,∆τ)
a∗
0A0(τ,∆τ)
. (4.22)
Considering Eq.(4.19), RS(τ, ∆τ) and R(n)
S (τ, ∆τ) will converge to 1 when τ is big
enough and ∆τ is small enough, and the energy will converge to E0. We ﬁnd that the
structure Eq.(4.20) may be much less sensitive to ∆τ than one may expect. We can
assume the errors in Eq.(4.20) are mostly coming from the leading order errors in its
denominator and the numerator. If the leading order error is from the ﬁrst excited
state, Eq.(4.20) can be approximated as
⟨ΨT|H[U(∆τ)]N|ΨT⟩
⟨ΨT|[U(∆τ)]N|ΨT⟩ ≈E0×Re
1 + a∗
1A1(τ,∆τ)E1
a∗
0A0(τ,∆τ)E0
1 + a∗
1A1(τ,∆τ)
a∗
0A0(τ,∆τ)
=E0R(1)
S (τ, ∆τ), (4.23)
92
and since Eq.(4.20) is real, we can assume a∗
1A1(τ,∆τ)
a∗
0A0(τ,∆τ) in Eq.(4.23) is mostly real and
we can deﬁne a real function B1(τ, ∆τ) as
B1(τ, ∆τ) =Rea∗
1A1(τ, ∆τ)
a∗
0A0(τ, ∆τ) (4.24)
such that
RS(τ, ∆τ)≈R(1)
S (τ, ∆τ)≈
1 +B1(τ, ∆τ)E1
E0
1 +B1(τ, ∆τ) . (4.25)
Therefore, our result E(∆τ) in Eq.(4.1) will be very close to the true expectation
E0, as long as Eq.(4.25) is close to 1. In Fig. 4.7 we plot the contour graph and show
how the value of the leading order structure function R(1)
S (τ, ∆τ) changes as B1(τ, ∆τ)
and E1/E0 change. We ﬁnd as long as B1(τ, ∆τ)∈ [−0.1, 0.1] (which is a reasonable
range for a proper ∆τ), R(1)
S (τ, ∆τ) will be close to 1 (the green area), it ﬂuctuates
from 0.9 to 1.1 so E(∆τ) will be around E0 with at most 10% error or so. In fact, our
results in section 4.1.2 shows that E(∆τ) in PIMC works even better. From Figs. 4.2
and 4.4 we see that even with a wide range of ∆ τ, the diﬀerence between E(∆τ) and
E0 is less than 3% which is well below 10%. The robust E(∆τ) value also indicates
the ground state path is robust, so the expectation values of other operators should
be reliable too.
