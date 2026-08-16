---
doc_id: arxiv-1011.1343v1
doc_title: "Institut für Kernphysik, Institute for Advanced Simulatio n and JCHP"
section_id: sec-007-5-flash-forward-combining-nuclear-eft-with-latti
section_title: "Flash forward: Combining nuclear EFT with lattice simulations"
section_number: 5
pages: 13-19
source_pdf: 1011.1343v1.pdf
source_sha256: 7d50e5e28e695191
doc_brief: "Chiral symmetry, nuclear forces and all that Ulf-G. Meißner — 8 sections: The early days at Stony Brook; Flashback: The Texas revolution; The chiral theory of nuclear force"
---
simulations
Having now constructed nuclear forces between two, three an d four nucleons, one has a
new tool to address the nuclear many-body problem. One venue is to combine standard
many-body techniques with these forces, as exempliﬁed by th e NCSM calculation shown
13
-120
-110
-100
-90
-80
-70
-60
 0  0.02  0.04  0.06  0.08  0.1
< E12C > (MeV)
t (MeV-1)
LO
+ ∆NLO
+ ∆IB + ∆EM
+ ∆NNLO
+ 4N Contact
-10
-5
 0
 5
 10
 15
 20
 0  0.02  0.04  0.06  0.08  0.1
t (MeV-1)
∆NLO
∆IB + ∆EM
∆NNLO
4N Contact
Figure 11: Ground-state energy of 12C as a function of Euclidean time. For details,
see [45].
in Sec. 4.2 or the discussion of nuclear matter in Sec. 4.3 (se e also the contribution by
Josef Speth, Siegfried Krewald and Frank Grümmer to this Fes tschrift). Here, I brieﬂy
want to outline a very diﬀerent and novel approach that combi nes the chiral EFT for the
forces with the method of Monte Carlo simulations, that are s o successfully utilized in the
lattice approach to QCD. The basic idea is to formulate the ch iral EFT on a Euclidean
space-time lattice as depicted in the left panel of Fig. 10 - h ere, the lattice spacing serves
as an UV regulator and has to be chosen such that the nucleons - which are treated as
non-relativistic point-like particles on the lattice site s - do not overlap. A lattice spacing
of a = 2 fm entails an UV cut-oﬀ Λ = π/a ≃ 300 MeV. The pion and nucleon propagators
as well as the one- and two-pion exchanges and the multi-nucl eon contact interactions
are written in terms of lattice variables, making use of Hubb ard-Stratonovich ﬁelds to
bring the 4- and 6-nucleon interactions into a quadratic for m (for more details, see [43]
and references therein as well as the nice review by Dean Lee [ 44]). Given this Euclidean
formulation of the action, the generating functional of the theory can then be evaluated
with stochastic methods, such as the hybrid Monte Carlo appr oach. It is important to
stress that the approximate Wigner SU(4) symmetry of the nuc lear interactions strongly
suppresses the sign oscillations and thus makes such nuclea r lattice simulations easier to
handle than lattice QCD calculations. Within this scheme, a systematic study of nuclei
up to A ≃ 40 will be possible using petascale computing as long as the t otal spin and
isospin of the nucleus under consideration is zero. Also, th e nuclear phase diagram can
be studied for a wide range of temperatures and densities, as indicated in the right panel
of Fig. 10. The state-of-the-art of these simulations is the calculation of the ground-state
energy of 6Li and 12C [45]. In these works, for the ﬁrst time the contributions fr om the
Coulomb interaction between protons and strong isospin-br eaking eﬀects were included.
A parameter-free prediction for the energy diﬀerence betwe en the triton and 3He could
14
be given,
E(3H) − E(3He) = 0 .78(5) MeV , (5)
in good agreement with the empirical value of 0 .76 MeV. The ground-state energies
of 6Li and 12C are calculated as −32.9(9) MeV and −99(2) MeV, respectively, not far
from the empirical values of −32.0 and −92.2 MeV, cf. also Fig. 11. This accuracy is
comparable to other so-called ab initio calculations (like the NCSM or Greens function
Monte Carlo), that often are based on a less consistent formu lation of the underlying
nuclear forces.
Taking 12C as the benchmark, it is interesting to estimate the require d computing time
and storage needed for the calculation of larger nuclei #2. With an improved algorithm,
the required CPU time for the 12C simulation on a BlueGene/P architecture and the
necessary storage to make the conﬁgurations (about 3500) av ailable is
X CPU
12C = 5 × 10− 5 PFlop − yr , X storage
12C = 0.14 TB . (6)
For a nucleus with A nucleons and with total spin S and isospin I the required CPU
time and data storage place can be estimated as
X CPU ≈ X CPU
12C ×
( A
12
) 3.2
exp[0.10(A − 12) + 3(S mod 2) + 4 I] ,
X storage ≈ X storage
12C ×
( A
12
) 2
exp[0.10(A − 12) + 3(S mod 2) + 4 I] , (7)
so that e.g. the calculation of the ground-states energies o f the magnesium isotopes
24,25,26Mg would require 0 .002, 0.064, 0.131 PFlop-yr and one would need 1 .9, 73.8, 145.5
TB to store the conﬁgurations for the calculation of matrix e lements for these nuclei. In
many cases, neutron scattering oﬀ nuclei can also be calcula ted making use of Lüscher’s
formula that relates the continuum phase shift to the ﬁnite e nergy shift measured on
the lattice. The CPU and storage requirements for neutron sc attering of the isotopes
24,26Mg would be 0 .064, 5.43 PFlop-yr and 73 .8, 5473 TB, respectively. All this work
remains to be done but bears a lot of promise. The possibiliti es that would be oﬀered
in a future exascale era are simply breath-taking.
6 Some ﬁnal words
The chiral eﬀective Lagrangian of QCD oﬀers a tool to systema tically investigate the
structure of the nucleon and the nuclear interactions with h igh accuracy - it appears
that we are now on the right track to achieve what could only be dreamed about a few
decades ago - see the discussion in Sec. 1. Nuclear physics wi ll no longer be based on
model-building and phenomenological approaches, althoug h still quite a bit of work is
ahead of us. But this work - even if hard and time-consuming - w ill be very rewarding
at the end. Furthermore, strangeness nuclear physics can al so be addressed within this
#2I am grateful to Dean Lee for providing me with these estimate s.
15
framework [46], but here a sound data basis has yet to be estab lished. Eventually, lattice
QCD might also contribute signiﬁcantly - but there are still quite a few obstacles to be
overcome, see e.g [47]. It is fair to say that nuclear physics as a ﬁeld, and I personally,
owe a lot to Gerry - thank you.
Acknowledgements
I am very much indebted to Gerry - as a physicist and a human. I a m grateful to Evgeny
Epelbaum, Dean Lee, Mannque Rho, Rocco Schiavilla, and Stev en Weinberg for useful
communications during the preparation of this contributio n. I also thank Silas Beane
and Véronique Bernard for a careful reading of the manuscrip t.
References
[1] M. Rho and G. E. Brown, Comments Nucl. Part. Phys. 10 (1981) 201.
[2] D. O. Riska and G. E. Brown, Phys. Lett. 38B (1972) 193.
[3] U.-G. Meißner and M. Gari, Phys. Lett. B 125 (1983) 364.
[4] G. E. Brown and A. D. Jackson, A. D, The nucleon-nucleon in teraction, North-
Holland Pub. Co., (Amsterdam and New York, 1976)
[5] N. Fettes, U.-G. Meißner and S. Steininger, Nucl. Phys. A 640 (1998) 199
[arXiv:hep-ph/9803266]; N. Fettes and U.-G. Meißner, Nucl . Phys. A 676 (2000)
311 [arXiv:hep-ph/0002162]; N. Fettes and U.-G. Meißner, N ucl. Phys. A 693 (2001)
693 [arXiv:hep-ph/0101030].
[6] P. Buettiker and U.-G. Meißner, Nucl. Phys. A 668 (2000) 97
[arXiv:hep-ph/9908247].
[7] N. Fettes, U.-G. Meißner, M. Mojzis and S. Steininger, An nals Phys. 283 (2000)
273 [Erratum-ibid. 288 (2001) 249] [arXiv:hep-ph/0001308].
[8] G. Ecker, J. Gasser, A. Pich and E. de Rafael, Nucl. Phys. B 321 (1989) 311;
G. Ecker, J. Gasser, H. Leutwyler, A. Pich and E. de Rafael, Ph ys. Lett. B 223
(1989) 425; J. F. Donoghue, C. Ramirez and G. Valencia, Phys. Rev. D 39 (1989)
1947.
[9] V. Bernard, N. Kaiser and U.-G. Meißner, Nucl. Phys. A 615 (1997) 483
[arXiv:hep-ph/9611253].
[10] J. Gasser, V. E. Lyubovitskij and A. Rusetsky, Phys. Rep t. 456 (2008) 167
[arXiv:0711.3522 [hep-ph]].
[11] S. Weinberg, Physica A 96 (1979) 327.
16
[12] S. Weinberg, Phys. Lett. B 251 (1990) 288, S. Weinberg, Nucl. Phys. B 363 (1991)
3.
[13] S. O. Bäckman, G. E. Brown and J. A. Niskanen, Phys. Rept. 124 (1985) 1.
[14] U. van Kolck, Phys. Rev. C 49 (1994) 2932.
[15] C. Ordonez, L. Ray and U. van Kolck, Phys. Rev. Lett. 72 (1994) 1982, C. Ordonez,
L. Ray and U. van Kolck, Phys. Rev. C 53 (1996) 2086 [arXiv:hep-ph/9511380].
[16] S. Weinberg, Phys. Lett. B 295 (1992) 114 [arXiv:hep-ph/9209257].
[17] E. Epelbaum, W. Glöckle and U.-G. Meißner, Nucl. Phys. A 637 (1998) 107
[arXiv:nucl-th/9801064].
[18] E. Epelbaum, W. Glöckle and U.-G. Meißner, Phys. Lett. B 439 (1998) 1;
[arXiv:nucl-th/9804005]. E. Epelbaum, W. Glöckle, A. Krüg er and U.-G. Meißner,
Nucl. Phys. A 645 (1999) 413 [arXiv:nucl-th/9809084].
[19] S. K. Bogner, T. T. S. Kuo and A. Schwenk, Phys. Rept. 386 (2003) 1
[arXiv:nucl-th/0305035].
[20] E. Epelbaum, W. Glöckle and U.-G. Meißner, Nucl. Phys. A 671 (2000) 295
[arXiv:nucl-th/9910064].
[21] N. Kaiser, R. Brockmann and W. Weise, Nucl. Phys. A 625 (1997) 758
[arXiv:nucl-th/9706045].
[22] E. Epelbaum, W. Glöckle and U.-G. Meißner, Eur. Phys. J. A 19 (2004) 125
[arXiv:nucl-th/0304037].
[23] E. Epelbaum, W. Glöckle and U.-G. Meißner, Nucl. Phys. A 747 (2005) 362
[arXiv:nucl-th/0405048].
[24] D. R. Entem and R. Machleidt, Phys. Lett. B 524 (2002) 93
[arXiv:nucl-th/0108057]; D. R. Entem and R. Machleidt, Phy s. Rev. C 68
(2003) 041001 [arXiv:nucl-th/0304018].
[25] E. Epelbaum, U.-G. Meißner, W. Glöckle and C. Elster, Ph ys. Rev. C 65 (2002)
044001 [arXiv:nucl-th/0106007].
[26] S. Barshay and G. E. Brown, Phys. Rev. Lett. 34 (1975) 1106.
[27] J. L. Friar, D. Huber and U. van Kolck, Phys. Rev. C 59 (1999) 53
[arXiv:nucl-th/9809065].
[28] V. Bernard, E. Epelbaum, H. Krebs and U.-G. Meißner, Phy s. Rev. C 77 (2008)
064004 [arXiv:0712.1967 [nucl-th]].
17
[29] S. Ishikawa and M. R. Robilotta, Phys. Rev. C 76 (2007) 014006 [arXiv:0704.0711
[nucl-th]].
[30] E. Epelbaum, Prog. Part. Nucl. Phys. 57 (2006) 654 [arXiv:nucl-th/0509032].
[31] E. Epelbaum, H. W. Hammer and U.-G. Meißner, Rev. Mod. Ph ys. 81 (2009) 1773
[arXiv:0811.1338 [nucl-th]].
[32] P. Navratil, V. G. Gueorguiev, J. P. Vary, W. E. Ormand an d A. Nogga, Phys. Rev.
Lett. 99 (2007) 042501 [arXiv:nucl-th/0701038].
[33] U.-G. Meißner, AIP Conf. Proc. 1011 (2008) 49.
[34] N. Kaiser, S. Fritsch and W. Weise, Nucl. Phys. A 697 (2002) 255
[arXiv:nucl-th/0105057].
[35] S. Fritsch, N. Kaiser and W. Weise, Nucl. Phys. A 750 (2005) 259
[arXiv:nucl-th/0406038].
[36] J. A. Oller, A. Lacour and U.-G. Meißner, J. Phys. G 37 (2010) 015106
[arXiv:0902.1986 [nucl-th]]; A. Lacour, J. A. Oller and U.- G. Meißner, Ann. Phys.
(NY) (2010) in print, doi:10.1016/j.aop.2010.06.012 [arX iv:0906.2349 [nucl-th]].
[37] G. A. Baker, Rev. Mod. Phys. 43 (1971) 479.
[38] P. Saviankou, S. Krewald, E. Epelbaum and U.-G. Meißner , arXiv:0802.3782 [nucl-
th].
[39] S. Kölling, E. Epelbaum, H. Krebs and U.-G. Meißner, Phy s. Rev. C 80 (2009)
045502 [arXiv:0907.3437 [nucl-th]].
[40] D. Rozpedzik, J. Golak, S. Kölling and E. Epelbaum, arXi v:1010.6269 [nucl-th].
[41] S. Pastore, R. Schiavilla and J. L. Goity, Phys. Rev. C 78 (2008) 064002
[arXiv:0810.1941 [nucl-th]]; S. Pastore, L. Girlanda, R. S chiavilla, M. Viviani and
R. B. Wiringa, Phys. Rev. C 80 (2009) 034004 [arXiv:0906.1800 [nucl-th]].
[42] L. Girlanda, A. Kievsky, L. E. Marcucci, S. Pastore, R. S chiavilla and M. Viviani,
arXiv:1008.0356 [nucl-th].
[43] B. Borasoy, E. Epelbaum, H. Krebs, D. Lee and U.-G. Meißn er, Eur. Phys. J. A 31
(2007) 105 [arXiv:nucl-th/0611087].
[44] D. Lee, Prog. Part. Nucl. Phys. 63 (2009) 117 [arXiv:0804.3501 [nucl-th]].
[45] E. Epelbaum, H. Krebs, D. Lee and U.-G. Meißner, Phys. Re v. Lett. 104 (2010)
142501 [arXiv:0912.4195 [nucl-th]]; E. Epelbaum, H. Krebs , D. Lee and U.-
G. Meißner, Eur. Phys. J. A 45 (2010) 335 [arXiv:1003.5697 [nucl-th]].
18
[46] C. L. Korpa, A. E. L. Dieperink and R. G. E. Timmermans, Ph ys. Rev. C 65
(2002) 015208 [arXiv:nucl-th/0109072]; H. W. Hammer, Nucl . Phys. A 705 (2002)
173 [arXiv:nucl-th/0110031]; H. Polinder, J. Haidenbauer and U.-G. Meißner, Nucl.
Phys. A 779 (2006) 244 [arXiv:nucl-th/0605050]; H. Polinder, J. Haide nbauer and
U.-G. Meißner, Phys. Lett. B 653 (2007) 29 [arXiv:0705.3753 [nucl-th]]. J. Haiden-
bauer and U.-G. Meißner, Phys. Lett. B 684 (2010) 275 [arXiv:0907.1395 [nucl-th]].
[47] S. Beane, PoS C D09 (2009) 076 [arXiv:0912.5404 [hep-lat]].
19
