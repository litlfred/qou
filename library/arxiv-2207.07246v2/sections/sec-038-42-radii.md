---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-038-42-radii
section_title: "Radii"
section_number: 4.2
pages: 103-105
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The root mean square (rms) radius rm can be interpreted as the average distance
between any one of the particles and the system’s center of mass. The label of the
nucleon does not matter, so we can just take nucleon number 1 as reference. The
operator can be written as 4 ,
ˆrm =
⏐⏐⏐⏐⏐ˆr1− 1
A
A∑
j=1
ˆrj
⏐⏐⏐⏐⏐, (4.26)
4In the code, we calculate the averaged operator ˆrm = 1
A
∑A
i=1
⏐⏐⏐ˆri− 1
A
∑A
j=1 ˆrj
⏐⏐⏐.
93
and we calculate⟨r2
m⟩ for its ground state expectation value as
⟨r2
m⟩ = Re⟨Φ0|ˆr2
m|Φ0⟩
Re⟨Φ0|Φ0⟩
=
Re⟨ΨT|e−H∆τ...e−H∆τ
⏐⏐⏐r1− 1
A
∑A
j=1rj
⏐⏐⏐
2
e−H∆τ...e−H∆τ|ΨT⟩
Re⟨ΨT|e−H∆τ...e−H∆τe−H∆τ...e−H∆τ|ΨT⟩ . (4.27)
Note that ˆrm does not commute with H, so PIMC is well suited to calculate it.
Eq.(4.27) can be recast into the form of Eq.(2.87) in section 2.7.1. We put the operator
ˆr2
m at the middle bead M, the corresponding gV
lr,M(R) can be written as,
gV
lr,M(R) =⟨ψl
M−1(R)|Ge
−VM ∆τ
2
⏐⏐⏐⏐⏐r1− 1
A
A∑
j=1
rj
⏐⏐⏐⏐⏐
2
e
−V†
M ∆τ
2 G|ψr
M+ 1(R)⟩, (4.28)
while other functions remain the same as in section 2.7.1. Once we calculated ⟨r2
m⟩,
the rms value is simply rm =
√
⟨r2
m⟩. Note that these are point nucleon radii.
Similarly, we can deﬁne the proton(neutron) radii operator ˆrp(n) as 5 ,
ˆrp(n) =
⏐⏐⏐⏐⏐ˆr1− 1
A
A∑
j=1
ˆrj
⏐⏐⏐⏐⏐P 1
p(n), (4.29)
where P 1
p = 1+τ1z
2 and P 1
n = 1−τ1z
2 are the proton and neutron projection operator
respectively for nucleon whose label is 1.
In Tables 4.3 and 4.4, we list our PIMC ground state point nucleon rms radii of
light nuclei based on the AV6’ interaction and the N 2LO local chiral interaction. For
2H, since there is no Coulomb interaction, rm = rp = rn. For other nuclei however,
due to the isospin dependent NN interaction (mainly due to the τi·τj part in the NN
interaction) and the Coulomb interaction, rm,rp andrn are not the same. E.g., for 3H,
the only proton is more likely in the center and the two neutrons are likely on the two
sides, so the proton is more closer to the center of the mass of the system, so rp <r n.
5In the code, we calculate the averaged operator ˆrp(n) = 1
Np(n)
∑A
i=1
⏐⏐⏐ˆri− 1
A
∑A
j=1 ˆrj
⏐⏐⏐Pi
p(n), where
Np(n) is the number of protons (neutrons).
94
Table 4.3: PIMC rms radii of light nuclei based on the AV6’ interaction.
AZ rm (fm) rp (fm) rn (fm)
2H 1 .98(2)
3H 1 .7261(5) 1.6240(4) 1 .7751(5)
3He 1 .7426(6) 1.7962(6) 1.6289(5)
4He 1 .4716(2) 1.4736(2) 1.4693(2)
Table 4.4: PIMC rms radii of light nuclei based on the local chiral N 2LO interaction.
AZ rm (fm) rp (fm) rn (fm)
2H 1 .991(1)
3H 1 .7497(7) 1.6430(6) 1 .8007(7)
3He 1 .7725(8) 1.8292(9) 1.6520(7)
4He 1 .4860(4) 1.4882(4) 1.4834(4)
3He is the opposite. The small diﬀerence between rp and rn for 4He is caused by the
Coulomb interaction.
