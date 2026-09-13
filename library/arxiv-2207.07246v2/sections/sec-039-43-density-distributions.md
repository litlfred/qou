---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-039-43-density-distributions
section_title: "Density Distributions"
section_number: 4.3
pages: 105-110
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The ground state of 4He is an angular momentum J = 0 state and is spherically
symmetric. We can use the one-particle number densityρ(r) to describe the probability
density for one particle to be at distance r from the nuclei’s center of mass. With this
convention we normalize it as
∫
4πr2ρ(r)dr = 1. (4.30)
95
The distribution ρ(r) can be extracted from high energy electron-nucleus scattering
experiments, and is related with the electric form factor by Fourier transform (Xu
(2009); Lynn et al. (2019)). The label of a particle does not matter, so we can just
take particle 1 as the reference particle, and the operator ˆρ(r) can be written as 6 ,
ˆρ(r) =δ
(
r−
⏐⏐⏐⏐⏐ˆr1− 1
A
A∑
j=1
ˆrj
⏐⏐⏐⏐⏐
)
. (4.32)
Note that due to the kinetic energy operator T in the Hamiltonian H, ˆρ(r) does
not commute with H. Therefore it cannot be calculated very accurately by diﬀusion
based QMC method. But it can be calculated directly by PIMC. The ground state
expectation value for the one-particle number density ρ(r) is,
ρ(r) = Re⟨Φ0|ˆρ(r)|Φ0⟩
Re⟨Φ0|Φ0⟩
=
Re⟨ΨT|e−H∆τ...e−H∆τδ
(
r−
⏐⏐ˆr1− 1
A
∑A
j=1 ˆrj
⏐⏐
)
e−H∆τ...e−H∆τ|ΨT⟩
Re⟨ΨT|e−H∆τ...e−H∆τe−H∆τ...e−H∆τ|ΨT⟩ . (4.33)
Eq.(4.33) can be recast into the form of Eq.(2.87) in section 2.7.1. We put the operator
ˆρ(r) at the middle bead M, the corresponding gV
lr,M(R) can be written as,
gV
lr,M(R) =⟨ψl
M−1(R)|Ge
−VM ∆τ
2 δ
(
r−
⏐⏐ˆr1− 1
A
A∑
j=1
ˆrj
⏐⏐
)
e
−V†
M ∆τ
2 G|ψr
M+ 1(R)⟩, (4.34)
while the other functions remain the same as in section 2.7.1.
The δ function in ρ(r) cannot be directly sampled. However it can be integrated.
We can expand in a histogram basis and the width of each bin is h, and r can be
represented byrk whenr∈ [kh,kh +h) andk is an integer. The basis of the histogram
6In the code, we actually calculate the averaged ˆρ(r) operator (Lynn et al. (2019)),
ˆρ(r) = 1
A
A∑
i=1
δ

r−
⏐⏐⏐⏐⏐⏐
ˆri− 1
A
A∑
j=1
ˆrj
⏐⏐⏐⏐⏐⏐

. (4.31)
We use Eq.(4.32) for illustration purpose.
96
can be represented by bk which is 1 when r∈ [kh,kh +h) and 0 otherwise. ρ(rk) can
be represented by a number ak such that,
ak =
∫
ρ(r)bkdr
4
3πh3[(k + 1)3−k3]. (4.35)
Considering Eq.(4.33) and Eq.(2.87) in section 2.7.1, ak can be written as,
ak =
∑
l
∑
r
∫
dR
{
3
∫
Alr(R)bkdr
4πh3[(k+1)3−k3]
}
Plr(R)
∑
l
∑
r
∫
dRBlr(R)Plr(R) , (4.36)
so we just need to sample 3
∫
Alr(R)bkdr
4πh3[(k+1)3−k3] to get ak. Note that Alr(R) =
Re[gV
lr,M(R)]
|Re[fV
lr (R)]| , and
Eq.(4.34) of gV
lr,M(R) contain the δ function, so the integral
∫
Alr(R)bkdr becomes,
∫
Alr(R)bkdr
=
Re
[∫
⟨ψl
M−1(R)|Ge
−VM ∆τ
2 δ
(
r−
⏐⏐ˆr1−
∑A
j=1 ˆrj
A
⏐⏐
)
e
−V†
M ∆τ
2 G|ψr
M+ 1(R)⟩bkdr
]
|Re[f(R)lr]|
=



Re[f(R)lr]
|Re[f(R)lr]|,
⏐⏐⏐⏐r1−
∑A
j=1 rj
A
⏐⏐⏐⏐∈ [kh,kh +h).
0, otherwise.
(4.37)
Note that Re[f(R)lr]
|Re[f(R)lr]| is either 1 or -1, so 3
∫
Alr(R)bkdr
4πh3[(k+1)3−k3] just becomes either 3
4πh3[(k+1)3−k3],
−3
4πh3[(k+1)3−k3] or 0.
The sampling of ak histogram value is then straightforward. We deﬁne a one-
dimensional array A(n) and initialize it to zero. We sample according to Plr(R)
as described in chapter 3, and each time when we take a sample, we look at the
conﬁguration of the middle bead M. At bead M, there always exists an integer k such
thatrk =|r1− 1
A
∑A
j=1rj|. At the same time, the kth element in A(k) takes a sample
of 3Re[f(R)lr]/|Re[f(R)lr]|
4πh3[(k+1)3−k3] , so A(k) =A(k) + 3Re[f(R)lr]/|Re[f(R)lr]|
4πh3[(k+1)3−k3] . For any other element j
in arrayA(n), they each take a sample of 0 and so A(j) remain the same. We continue
sampling according to Plr(R) and continue. Once we have enough N samples, then
97
/s48/s46/s48 /s48/s46/s50 /s48/s46/s52 /s48/s46/s54 /s48/s46/s56 /s49/s46/s48 /s49/s46/s50 /s49/s46/s52 /s49/s46/s54 /s49/s46/s56 /s50/s46/s48 /s50/s46/s50 /s50/s46/s52 /s50/s46/s54 /s50/s46/s56 /s51/s46/s48
/s48/s46/s48/s48
/s48/s46/s48/s49
/s48/s46/s48/s50
/s48/s46/s48/s51
/s48/s46/s48/s52
/s48/s46/s48/s53
/s48/s46/s48/s54
/s48/s46/s48/s55
/s48/s46/s48/s56
/s48/s46/s48/s57
/s48/s46/s49/s48
/s79/s110/s101/s45/s112/s97/s114/s116/s105/s99/s108/s101/s32/s110/s117/s109/s98/s101/s114/s32/s100/s101/s110/s115/s105/s116/s121 /s40 /s102/s109
/s45/s51
/s41
/s114/s32/s40/s102/s109/s41
/s52
/s72/s101
/s32 /s32/s64/s32 /s48/s46/s49/s53/s32/s77 /s101/s86
/s45/s49
/s32 /s64/s32 /s48/s46/s50/s32/s32/s32/s77 /s101/s86
/s45/s49
/s32 /s32/s64/s32 /s48/s46/s51/s32/s32/s32/s77 /s101/s86
/s45/s49
/s32
/s110
/s32
/s112
Figure 4.8: The ground state one-particle number density distributions of 4He based
on the AV6’ interaction.
/s48/s46/s48 /s48/s46/s50 /s48/s46/s52 /s48/s46/s54 /s48/s46/s56 /s49/s46/s48 /s49/s46/s50 /s49/s46/s52 /s49/s46/s54 /s49/s46/s56 /s50/s46/s48 /s50/s46/s50 /s50/s46/s52 /s50/s46/s54 /s50/s46/s56 /s51/s46/s48
/s48/s46/s48/s48
/s48/s46/s48/s49
/s48/s46/s48/s50
/s48/s46/s48/s51
/s48/s46/s48/s52
/s48/s46/s48/s53
/s48/s46/s48/s54
/s48/s46/s48/s55
/s48/s46/s48/s56
/s48/s46/s48/s57
/s48/s46/s49/s48
/s48/s46/s49/s49
/s48/s46/s49/s50
/s79/s110/s101/s45/s112/s97/s114/s116/s105/s99/s108/s101/s32/s110/s117/s109/s98/s101/s114/s32/s100/s101/s110/s115/s105/s116/s121 /s40 /s102/s109
/s45/s51
/s41
/s114/s32/s40/s102/s109/s41
/s32 /s64/s32 /s48/s46/s50/s32/s77 /s101/s86
/s45/s49
/s32 /s32/s64/s32 /s48/s46/s51/s32/s77 /s101/s86
/s45/s49
/s32/s32/s32/s32/s32
/s32
/s110
/s32
/s112
/s52
/s72/s101
Figure 4.9: The ground state one-particle number density distributions of 4He based
on the local chiral N 2LO interaction.
98
each of the ak can be evaluated by ak = A(k)/N with corresponding error bar. As
shown in Fig. 4.8, ρ(rk) are given by these values. We can see from Fig. 4.8 for AV6’
interaction and Fig. 4.9 for the local chiral N 2LO interaction that for diﬀerent total
imaginary time, the particle number density distribution of 4He are almost identical.
These are further evidence that we have reached the ground state.
From Eq.(4.31) and Eq.(4.32), we can further deﬁne the single-proton number
density ˆρp and the single-neutron number density ˆρn as
ˆρp(n)(r)=δ
(
r−
⏐⏐⏐⏐⏐ˆr1− 1
A
A∑
j=1
ˆrj
⏐⏐⏐⏐⏐
)
P 1
p(n) = 1
A
A∑
i=1
δ
(
r−
⏐⏐⏐⏐⏐ˆri− 1
A
A∑
j=1
ˆrj
⏐⏐⏐⏐⏐
)
Pi
p(n). (4.38)
where Pi
p = 1+τ1z
2 and Pi
n = 1−τ1z
2 are the proton and neutron projection operator for
nucleon with label i. Since Pi
p +Pi
n = 1, we have
ˆρ(r) = ˆρp(r) + ˆρn(r). (4.39)
The sampling method of ˆρp(r) and ˆρn(r) is similar with that of ˆρ(r). In Fig. 4.8 and
Fig. 4.9, ρp(r) and ρn(r) are also presented. As expected from the rms radii results, in
4He the two protons and the two neutrons are distributed evenly, and ρp(r) and ρn(r)
are almost identical.
In Fig. 4.10 all the density distributions for A≤ 4 light nuclei are presented. For
2H the ρp(r) and ρn(r) are identical, and as r decreases, the density distributions
based on the AV6’ interaction decrease rapidly which are diﬀerent from those based
on the local chiral N 2LO interaction. This is because, as shown in Fig. 2.2, for the
two-nucleon system the central part becomes the dominant part as r decreases, and
the AV6’ interaction has a much more repulsive central radial function than the chiral
one, this makes the proton and the neutron highly unlikely to be very close to each
other and the center of mass, which means density distributions will rapidly decrease
as r decreases. For 3H there is one proton and two neutrons, and at a given r, it is
99
/s48/s46/s48 /s48/s46/s53 /s49/s46/s48 /s49/s46/s53 /s50/s46/s48 /s50/s46/s53 /s51/s46/s48
/s48/s46/s48/s48
/s48/s46/s48/s49
/s48/s46/s48/s50
/s48/s46/s48/s51
/s48/s46/s48/s52
/s48/s46/s48/s53
/s48/s46/s48/s54
/s48/s46/s48/s55
/s48/s46/s48/s56
/s48/s46/s48/s57
/s48/s46/s49/s48
/s48/s46/s49/s49
/s48/s46/s49/s50
/s48/s46/s49/s51
/s79/s110/s101/s45/s112/s97/s114/s116/s105/s99/s108/s101/s32/s110/s117/s109/s98/s101/s114/s32/s100/s101/s110/s115/s105/s116/s121 /s40 /s102/s109
/s45/s51
/s41
/s114/s32/s40/s102/s109/s41
/s76/s111/s99/s97/s108/s32/s67/s104/s105/s114/s97/s108/s32/s78
/s50
/s76/s79 /s32/s32/s32/s32 /s32/s32/s32/s32/s32
/s112
/s32/s32/s32/s32/s32
/s110
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s52
/s72/s101/s32 /s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s51
/s72/s101/s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s51
/s72/s32/s32/s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s50
/s72/s32/s32/s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32 /s65/s114/s103/s111/s110/s110/s101/s32/s118/s54/s39 /s32/s32 /s32/s32/s32/s32/s32/s32
/s112
/s32/s32/s32/s32/s32
/s110
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s52
/s72/s101/s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s51
/s72/s101/s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s51
/s72/s32/s32/s32
/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32/s32
/s50
/s72/s32/s32/s32
Figure 4.10: The ground state one-particle number density distributions ofA≤ 4 light
nuclei based on the AV6’ interaction and the local chiral N 2LO interaction. The lines
are a guide to the eye.
reasonable that the probability of ﬁnding a neutron ρn(r) is always higher than that
of ﬁnding a proton ρp(r). 3H and its mirror nuclei 3He shows nearly the same ρ(r)
distribution, however their ρp(r) and ρn(r) distributions are as if they are exchanged,
i.e., 3H’s ρp(r) is like the 3He’s ρn(r) and 3H’s ρn(r) is like 3He’s ρp(r).
