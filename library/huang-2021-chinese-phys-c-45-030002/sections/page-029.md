---
doc_id: huang-2021-chinese-phys-c-45-030002
doc_title: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures"
section_id: page-029
section_title: "Page 29"
section_number: null
pages: 29-29
source_pdf: Huang_2021_Chinese_Phys._C_45_030002.pdf
source_sha256: 1dd3329ed87476c8
toc_source: undetermined
doc_brief: "The AME 2020 atomic mass evaluation (I). Evaluation of input data, and adjustment procedures — 343 sections: Page 1; Page 2; Page 3"
---
Chinese Physics C
Vol. 45, No. 3 (2021) 030002
If the levels are regularly spaced, i.e. E2 = 2E1,
σ =
√
6
12 E2 = 0.204E2 ,
while for a value of E1 very near 0 or E2,
σ =
√
2
6 E2 = 0.236E2 .
B.3
Case of more than 3 spectral lines
For more than 3 lines, one may easily infer Mexp =
∑n
i=0 Mi/(n+1), but the determination of σ requires the
knowledge of P(m). As the exact calculation of P(m)
becomes rather diﬃcult, it is more simple to do simula-
tions.
However, care must be taken that the values of the
xi’s are explored with an exact equality of chance to
occur. For each set of xi’s, m is calculated, and the his-
togram Nj(mj) of its distribution is built. Calling nbin
the number of bins of the histogram, one gets :
P(mj)
=
Nj
∑nbin
j=1 Nj
,
(38)
and
Mexp
=
nbin
∑
j=1
P(mj)mj ,
σ2
=
nbin
∑
j=1
P(mj)(mj −Mexp)2 .
For three excited isomers, the ground state mass
M0 ± σ0 can be determined from the measured mass
Mexp ± σexp and the knowledge of the excitation ener-
gies E1 ±σ1, E2 ±σ2 and E3 ±σ3 as:
M0
=
Mexp −1
4(E1 +E2 +E3),
σ2
0
=
σ2
exp +(1
4σ1)2 +(1
4σ2)2 +(1
4σ3)2 +σ2 .
An example of a Fortran program based on the Cern
library was given for the cases of two, three and four lines
in Ame2016 [2].
Appendix C
Deﬁnition of decay energies
Conventionally, the total energy released in α de-
cay, Qα, is deﬁned as the diﬀerence between the atomic
masses of the mother and daughter nuclides:
Qα = Mmother −Mdaughter −M4He .
(39)
This value equals the sum of the observed energy of the
α particle and that of the recoiling nuclide (with only a
minor correction for the fact that the cort`ege of atomic
electrons in the latter may be in an excited state). Un-
fortunately, some authors in the literature quote Qα as
a value ‘corrected for screening’, which essentially means
that they take the masses of bare nuclides for the M
values in the above equation.
A similar bad habit has been observed for some pub-
lished proton-decay energies. We very strongly object to
this custom; at the very least, the symbol Q should not
be used for the diﬀerence in nuclear masses.
High precision α-decay energies
The most precise α-decay energies are those measured
absolutely using magnetic spectrographs, as summarized
in Ref. [1991Ry01] and references therein. All α-energy
standards are determined using this method.
The re-
lation between the α-particle energy Eα and the decay
energy, Qα is:
Qα = (M −mα)−
√
(M −mα)2 −2×M ×Eα +78.6 eV.
(40)
where M is the mass of the parent nuclide, mα is the
mass of the doubly ionized α particle and 78.6 eV is the
binding energy of two electrons in helium. This formula
had been discussed in Ame1977 and has been used since
then.
The electron binding energy of helium has just
been taken into account since Ame2016.
References
1 G. Audi, Int. J. Mass Spectr. 251, 85 (2006).
2 W.J. Huang, G. Audi, M. Wang, F.G. Kondev, S. Naimi
and X. Xu, Chin. Phys. C 41, 030002 (2017).
3 M. Wang, G. Audi, W.J. Huang, F.G. Kondev, S. Naimi
and X. Xu, Chin. Phys. C 41, 030003 (2017).
4 M. Wang, W.J. Huang, F.G. Kondev, G. Audi and
S. Naimi, Chin. Phys. C 45, 030002 (2021).
5 F.G. Kondev, M. Wang, W.J. Huang, S. Naimi and
G. Audi, Chin. Phys. C 45, 030001 (2021).
6 B. Pritychenko, E. Bˇet´ak, M.A. Kellett, B. Singh and
J. Totans, Nucl. Instrum. Methods Phys. A 640, 213
(2011).
http://www.nndc.bnl.gov/nsr/
7 T.P. Kohman, J.H.E. Mattauch and A.H. Wapstra, J. de
Chimie Physique 55, 393 (1958).
8 D. B. Newell, F. Cabiati, J. Fischer, K. Fujii, S. G.
Karshenboim, H. S. Margolis, E. d. Mirandés, P. J. Mohr,
F. Nez, K. Pachucki, T. J. Quinn, B. N. Taylor, M. Wang,
B. M. Wood, and Z. Zhang, Metrologia 55 L13-L16 (2018).
https://physics.nist.gov/cuu/Constants/index.html
9 Bureau International des Poids et Mesures (BIPM) SI
Brochure (2019, 9th edition).
10 L. Morel, Z. Yao, P. Cladeand and S. Guellati-Khelifa,
Nature(London) 588, 61 (2020).
030002-28
