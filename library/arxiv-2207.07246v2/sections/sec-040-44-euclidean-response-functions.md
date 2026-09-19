---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-040-44-euclidean-response-functions
section_title: "Euclidean Response Functions"
section_number: 4.4
pages: 110-116
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
Response functions are important quantities (Carlson and Schiavilla (1992); Benhar
et al. (1994); Carlson and Schiavilla (1994); Carlson et al. (2002); Sick (2003); Lovato
et al. (2013, 2015)) and the related operators do not commute with H. Using PIMC to
calculate the response functions thus has a natural advantage over diﬀusion methods.
100
In an electron-nucleus scattering experiment, the response of a weakly coupled
external probe can be written as the function S(k,ω ) which can be expanded in the
energy eigenstates (Carlson and Schiavilla (1994)), as
S(k,ω ) =
∑
n⟨Φ0|ρ†(k)|Φn⟩⟨Φn|ρ(k)|Φ0⟩δ(ω +E0−En)
⟨Φ0|Φ0⟩ , (4.40)
wherek is the momentum transfer between the ﬁnal and initial momentum of the
nucleus, and ω is the energy transfer which is the diﬀerence between the ﬁnal and
initial energy of the nucleus. (k,ω ) is the four-momentum carried by the virtual photon
(Bacca and Pastore (2014)) which is exchanged between the electron and the nucleus.
En is eigenenergy of the excited states |Φn⟩, and the ρ(k) is the coupling operator.
The S(k,ω ) in Eq.(4.40) is called the response function. It is useful because it
is related with the scattering cross section therefore directly connects theory and
experiment. For diﬀerent scattering processes the couplings of the probe to the nucleus
gives diﬀerentρ(k) operators. However, it is not easy to directly calculate the response
function itself. Instead, we calculate the Euclidean response function E(k,τ ) ofS(k,ω )
by using QMC, and then ﬁnd ways (Shen et al. (2012); Lovato et al. (2015)) to invert
E(k,τ ) to S(k,ω ).
The Euclidean response function E(k,τ ) is related to S(k,ω ) by the following
Laplace transform,
E(k,τ ) =
∫ ∞
0
e−τ(ω−ωqe)S(k,ω )dω
= eωqeτ∑
n⟨Φ0|ρ†(k)e−Hτ|Φn⟩⟨Φn|ρ(k)|Φ0⟩
e−E0τ|⟨Φ0|Φ0⟩
= eωqeτ⟨Φ0|ρ†(k)e−Hτρ(k)|Φ0⟩
⟨Φ0|e−Hτ|Φ0⟩
= eωqeτ⟨ΨT|e−Hτ1
[
ρ†(k)e−Hτρ(k)
]
e−Hτ1|ΨT⟩
⟨ΨT|e−Hτ1e−Hτe−Hτ1|ΨT⟩ , (4.41)
where ωqe =k2/2m is the quasielastic energy transfer (Lovato et al. (2020)) and τ1 is
chosen to be large enough to project out the ground state Φ 0.
101
In this work, we calculate the 4He Euclidean response functions that correspond to
several diﬀerent single-nucleon couplings ρ(k), which are similar to those in Carlson
and Schiavilla’s 1994 paper (Carlson and Schiavilla (1994)). Those include the nucleon
coupling ρN(k) , proton coupling ρp(k), isovector coupling ρτ(k), spin-longitudinal
coupling ρστL (k) and spin-transverse coupling ρστT (k). They are deﬁned as,
ρN(k) =
A∑
i=1
eik·ri, (4.42)
ρp(k) =
A∑
i=1
eik·ri 1 +τiz
2 , (4.43)
ρτ(k) =
A∑
i=1
eik·riτiz, (4.44)
ρστL (k) =
A∑
i=1
eik·ri(σi· ˆk)τiz, (4.45)
ρστT (k) =
A∑
i=1
eik·ri(σi× ˆk)τiz. (4.46)
Note thatτiz is the diﬀerence between the proton and neutron projection operators,
so it is related with the diﬀerence between protons and neutrons. σi· ˆk andσi× ˆk
can be related with diﬀerent mesons including pion, EM scattering, magnetic ﬁelds,
etc (Carlson and Schiavilla (1998)).
In diﬀusion QMC such as GFMC and AFDMC, it is often ⟨ΨT|ρ†(k)e−Hτρ(k)|Φ0⟩
that is calculated. Since the operator ρ†(k)e−Hτρ(k) does not commute with the
Hamiltonian,⟨ΨT|ρ†(k)e−Hτρ(k)|Φ0⟩ is mostly a mixed estimator (although forward
walking extrapolation can improve this) instead of the true ground state estimator
⟨Φ0|ρ†(k)e−Hτρ(k)|Φ0⟩. This disadvantage of diﬀusion QMC is exactly the advantage
of PIMC method, because PIMC can project out the ground state Φ0 from both⟨ΨT|
and|ΨT⟩ by using the projection operator e−Hτ1 with the short-time approximation.
PIMC really calculates the ground state estimator ⟨Φ0|ρ†(k)e−Hτρ(k)|Φ0⟩, whether
ρ†(k)e−Hτρ(k) commutes with the Hamiltonian or not.
102
0 ML=N-M1 N-1 N
…
…
…
…
…
…
Figure 4.11: Illustration of gV
lr,M(R) in Eq.(4.47) for Euclidean response functions.
The calculations of E(k,τ ) in PIMC is straightforward. Eq.(4.41) can be recast
into the form of Eq.(2.87) in section 2.7.1. As illustrated in Fig. 4.11, we can denote the
total imaginary time as τtot =N∆τ, and τ1 =L∆τ, L =N−M, τ = (M−L)∆τ =
(2M−N)∆τ. We just need to place the operator ρ†(k) at bead L, and place ρ(k) at
bead M, and gV
lr,M(R) can be written as,
gV
lr,M(R) =eωqeτ⟨ψl
L−1(R)|e
−VL∆τ
2 ρ†(k)e−Vτρ(k)e
−V†
M ∆τ
2 |ψr
M+ 1(R)⟩, (4.47)
where e−Vτ is deﬁned as,
e−Vτ≡e
−V†
L∆τ
2 G
(
e
−VL+1∆τ
2 e
−V†
L+1∆τ
2
)
G ... G
(
e
−VM−1∆τ
2 e
−V†
M−1∆τ
2
)
Ge
−VM ∆τ
2 . (4.48)
All the other functions and calculations are the same as those in section 2.7.1.
The ground state of 4He has total isospin and its z component both 0, and it is a
spherically symmetric object. Therefore the response functions do not depend on the
direction ofk. So when calculating the E(k,τ ), the momentumk can be averaged over
all the directions. The angle averaged response functions are not calculated on the ﬂy
103
because they are relatively more time-consuming comparing with other quantities, so
they are calculated after we have enough paths stored on the storage systems. For a
given amount of computation time, the angle averaged E(k,τ ) have less variance than
the non angle averaged E(k,τ ). The angle averaged E(k,τ ) is calculated as,
E(k,τ ) = eωqeτ⟨ΨT|e−Hτ1
[ 1
4π
∫
ρ†(k)e−Hτρ(k)dΩ
]
e−Hτ1|ΨT⟩
⟨ΨT|e−Hτ1e−Hτe−Hτ1|ΨT⟩ , (4.49)
so that the correspondingly gV
lr,M(R) is calculated as 7 ,
gV
lr,M(R) =eωqeτ⟨ψl
L−1(R)|Ge
−VL∆τ
2
[∫
ρ†(k)e−Vτρ(k)dΩ
4π
]
e
−V†
M ∆τ
2 G|ψr
M+ 1(R)⟩, (4.50)
wheree−Vτ is deﬁned in Eq.(4.48). For any operator ˆO which is independent of k, e.g.,
ˆO can be e−Hτ or e−Vτ as deﬁned in Eq.(4.48).
/s48/s46/s48/s48 /s48/s46/s48/s49 /s48/s46/s48/s50 /s48/s46/s48/s51 /s48/s46/s48/s52
/s48/s46/s48
/s48/s46/s53
/s49/s46/s48
/s49/s46/s53
/s50/s46/s48
/s50/s46/s53
/s51/s46/s48
/s51/s46/s53
/s52/s46/s48
/s69/s40/s107/s44 /s41
/s32/s40/s77 /s101/s86
/s45/s49
/s41
/s52
/s72/s101 /s32/s32/s32 /s32/s32/s32/s80/s73/s77/s67/s32/s32/s32/s71/s70/s77/s67
/s32/s32/s32
/s78
/s32/s32/s32/s32/s32/s32 /s32/s32/s32 /s32
/s32/s32/s32
/s112
/s32/s32/s32/s32/s32/s32 /s32/s32/s32
/s32/s32/s32 /s32/s32/s32/s32/s32/s32/s32 /s32/s32
/s32/s32/s32
/s76
/s32/s32/s32/s32 /s32/s32/s32
/s32/s32/s32
/s84 
/s32/s32/s32/s32 /s32/s32/s32
/s107/s61/s51/s53/s48/s32/s77 /s101/s86/s47/s99
/s116/s111/s116
/s61/s48/s46/s50/s32/s77/s101/s86
/s45/s49
/s44/s32 /s61/s48/s46/s48/s48/s48/s49/s53/s32/s77/s101/s86
/s45/s49
/s44/s32/s78/s61/s49/s51/s51/s52
Figure 4.12: Angle averaged Euclidean response functions of 4He at k = 350 MeV/c
for the AV6’ interaction.
7The detailed angle averaged calculations of
∫
ρ†(k) ˆOρ(k)dΩ/4π for each response function can
be found in Appendix E.1.
104
/s48/s46/s48/s48 /s48/s46/s48/s49 /s48/s46/s48/s50 /s48/s46/s48/s51 /s48/s46/s48/s52
/s48/s46/s48
/s48/s46/s53
/s49/s46/s48
/s49/s46/s53
/s50/s46/s48
/s50/s46/s53
/s51/s46/s48
/s51/s46/s53
/s52/s46/s48
/s69/s40/s107/s44 /s41
/s32/s40/s77 /s101/s86
/s45/s49
/s41
/s52
/s72/s101 /s32/s32/s32/s32/s32 /s80/s73/s77 /s67/s32/s32/s71/s70/s77 /s67
/s32/s32/s32
/s78
/s32/s32/s32/s32/s32/s32/s32 /s32/s32/s32
/s32/s32/s32
/s112
/s32/s32/s32/s32/s32/s32/s32 /s32/s32/s32 /s32
/s32/s32/s32 /s32/s32/s32/s32/s32/s32/s32 /s32
/s32/s32/s32
/s76
/s32/s32/s32/s32/s32 /s32/s32/s32 /s32
/s32/s32/s32
/s84 
/s32/s32/s32/s32/s32 /s32/s32/s32
/s107/s61/s51/s53/s48/s32/s77 /s101/s86/s47/s99
/s116/s111/s116
/s61/s48/s46/s50/s32/s77/s101/s86
/s45/s49
/s44/s32 /s61/s48/s46/s48/s48/s48/s49/s53/s32/s77/s101/s86
/s45/s49
/s44/s32/s78/s61/s49/s51/s51/s52
Figure 4.13: Angle averaged Euclidean response functions of 4He at k = 350 MeV/c
for the local chiral N 2LO interaction.
Fig. 4.12 and Fig 4.13 shows all the angle averaged Euclidean response functions
Eα for each ρα deﬁned in this work. Fig. 4.12 is for the AV6’ interaction and Fig 4.13
is for the local chiral N 2LO interaction. Each of the Eα has been normalized such
that limk→∞Eα(k,τ = 0) = 1. Our calculations are done in the center of mass frame,
but we have converted our results to the lab frame 8 . We calculate our response
functions in the center of mass frame ﬁrst because it can give lower variance compare
with lab frame. We then multiply our results by e−16.3τ (the 16.3 MeV is the center of
mass energy for this k = 350 MeV/c) in order to compare with the results in Carlson
and Schiavilla’s paper (Carlson and Schiavilla (1994)) which are digitized as the red
dots in Figs. 4.12 and 4.13. The small diﬀerence between ours and theirs comes from
several sources. First, we use PIMC, they use GFMC. Second, the interactions are
8See Appendix E.2 for the conversion process.
105
somewhat diﬀerent, they used the Argonne v8 interaction combined with the Urbana
model-VIII. Third, we use τiz in stead of τ+(i) for the isovector, spin-longitudinal
and spin-transverse couplings, this is suggested in their paper when dealing with an
isoscalar target like the ground state 4He, and with interactions that conserve the
number of protons and neutrons. The small diﬀerence can also indicate our results are
more accurate because in PIMC we do not need forward walking as DMC does.
