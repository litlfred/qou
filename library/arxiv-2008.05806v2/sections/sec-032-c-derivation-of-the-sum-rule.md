---
doc_id: arxiv-2008.05806v2
doc_title: "Sum rule for the Compton amplitude and implications for the proton-neutron mass diﬀerence"
section_id: sec-032-c-derivation-of-the-sum-rule
section_title: "C Derivation of the sum rule"
section_number: null
pages: 25-26
source_pdf: 2008.05806v2.pdf
source_sha256: 4e1f9af118ba81b1
toc_source: outline
doc_brief: "Sum rule for the Compton amplitude and implications for the proton-neutron mass difference — The Cottingham formula expresses the lead- ing contribution of the electromagnetic interaction to the"
---
C Derivation of the sum rule
To calculate the limiting value of the dispersion integral
(21), we ﬁrst use partial fractions and split the integral
into two parts:
¯T disp = −¯Sa + ¯T disp′ ,
(C.1)
¯Sa = −m2
Q2
Z xth
0
dx
¯F(x, Q2)
Q2 + m2x2 ,
¯T disp′ = 4m2ν2
Q2
Z xth
0
dx
¯F(x, Q2)
Q4 −4m2x2ν2 −iǫ .
The reason for denoting the ﬁrst term by −¯Sa is that it
is independent of ν and hence amounts to a contribution
to the subtraction function.
To perform the limit in the remainder, we decom-
pose the structure function into two parts with ¯F =
( ¯F −F R)+F R. In the diﬀerence ¯F −¯F R, the terms pro-
portional to x1−α cancel. We assume that the remainder
is suﬃciently smooth for x →0, so that ( ¯F −F R)/x2
is integrable and the integration can be interchanged
with the limit.7 This leads to
¯T disp′ →−¯Sb + ¯T disp′′ ,
(C.2)
¯Sb = 1
Q2
Z xth
0
dx
¯F −¯F R
x2
,
¯T disp′′ =
X
α>0
bα(Q2)
Q2
Jα ,
Jα =
Z xth
0
dx
x1−α
ξ2 −x2 −iǫ ,
with ξ = Q2/(2mν). The integral Jα represents a hy-
pergeometric function. What remains to be done is to
work out the behaviour of this function at small values
of ξ.
This can be done by making use of the known prop-
erties of the hypergeometric functions. Alternatively,
one may observe that the contributions from the crit-
ical region x ∼ξ remain the same if the integral is
extended to inﬁnity – it can then be done explicitly.
On the interval xth < x < ∞, on the other hand, the
limit can be interchanged with the integral, which can
then be done explicitly as well. The result reads
Jα = −
π
2 sin 1
2παe−1
2 iπαξ−α +
1
αxα
th
+ O(ξ2) .
(C.3)
The ﬁrst term is proportional to να. The Reggeon
amplitudes speciﬁed in equation (18) have the same
behaviour when ν becomes large. Indeed, one readily
checks that the two expressions agree, so that
lim
ν→∞( ¯T disp′′ −¯T R) = −¯Sc
(C.4)
¯Sc = −
X
α>0
bα(Q2)
αxα
th
.
7If the singularity is more complicated, the sum rule does not
get lost, but the explicit form must be adapted.
Collecting terms, the formula (22) yields ¯S = ¯Sa + ¯Sb +
¯Sc. This agrees with the expression (23) for ¯S quoted
in section 5.
References
1. W. Heisenberg, Z. Phys. 77 (1932) 1.
2. W. N. Cottingham, Annals Phys. 25 (1963) 424.
3. M. Elitzur and H. Harari, Annals Phys. 56 (1970) 81.
4. J. Gasser and H. Leutwyler, Nucl. Phys. B 94 (1975) 269.
5. J. D. Bjorken, Phys. Rev. 179 (1969) 1547.
6. A. Walker-Loud, C. E. Carlson and G. A. Miller, Phys.
Rev. Lett. 108 (2012) 232301 [arXiv:1203.0254].
7. F. B. Erben, P. E. Shanahan, A. W. Thomas
and R. D. Young, Phys. Rev. C 90 (2014) 065205
[arXiv:1408.6628].
8. A. W. Thomas, X. G. Wang and R. D. Young, Phys. Rev.
C 91 (2015) 015209 [arXiv:1406.4579].
9. A. Walker-Loud, PoS CD 2018 (2019) 045
[arXiv:1907.05459].
10. O. Tomalak, Eur. Phys. J. Plus 135 (2020) 411 [arXiv:
1810.02502].
11. J. Gasser, M. Hoferichter, H. Leutwyler and A. Rusetsky,
Eur. Phys. J. C 75 (2015) 375; Erratum: Eur. Phys. J. C
80 (2020) 353 [arXiv:1506.06747].
12. H. Leutwyler, PoS CD 2015 (2015) 022
[arXiv:1510.07511].
13. M. Hoferichter, PoS CD 2018 (2019) 028.
14. D. J. Gross and F. Wilczek, Phys. Rev. Lett. 30 (1973)
1343.
15. H. D. Politzer, Phys. Rev. Lett. 30 (1973) 1346.
16. S. Weinberg, Phys. Rev. Lett. 31 (1973) 494.
17. J. C. Collins, Nucl. Phys. B 149 (1979) 90; Errata: Nucl.
Phys. B 153 (1979) 546, Nucl. Phys. B 915 (2017) 392.
18. J. Gasser, H. Leutwyler and A. Rusetsky,
arXiv:2003.13612.
19. W. A. Bardeen and W. K. Tung, Phys. Rev. 173 (1968)
1423; Erratum: Phys. Rev. D 4 (1971) 3229.
20. R. Tarrach, Nuovo Cim. A 28 (1975) 409.
21. R. Jost and H. Lehmann, Nuovo Cimento 5 (1957) 1598.
22. F. J. Dyson, Phys. Rev. 110 (1958) 1460.
23. N. N. Bogoliubov and V. S. Vladimirov, Nauchn. Dokl.
Vysshei Shkoly, Fiz.-Mat. Nauki 3 (1958) 26, reprinted in:
Collection of scientiﬁc works of N.N. Bogoliubov, volume
1, p. 683, NAUKA (Ed.), Moscow, 2005.
24. H. Leutwyler and P. Otterson, in: Scale and Conformal
Symmetry in Hadron Physics, ed. R. Gatto, John Wiley
& Sons, New York (1973), p.1.
25. M. Gell-Mann, M. Goldberger, F. Low, E. Marx and
F. Zachariasen, Phys. Rev. 133 (1964) B145.
26. S. Mandelstam, Phys. Rev. 137 (1965) B949.
27. M. T. Grisaru, H. Schnitzer and H. S. Tsao, Phys. Rev.
Lett. 30 (1973) 811.
28. M. T. Grisaru, H. Schnitzer and H. S. Tsao, Phys. Rev.
D 8 (1973) 4498.
29. L. N. Lipatov, Sov. J. Nucl. Phys. 23 (1976) 338 [Yad.
Fiz. 23 (1976) 642].
30. E. Kuraev, L. Lipatov and V. S. Fadin, Sov. Phys. JETP
45 (1977) 199 [Zh. Eksp. Teor. Fiz. 72 (1977) 377].
31. I. Balitsky and L. Lipatov, Sov. J. Nucl. Phys. 28 (1978)
822 [Yad. Fiz. 28 (1978) 1597].
32. Gribov,
V.
The
Theory
of
Complex
Angular
Mo-
menta: Gribov Lectures on Theoretical Physics (Cam-
bridge Monographs on Mathematical Physics). Cam-
bridge: Cambridge University Press 2003.
26
33. I. Caprini, Phys. Rev. D 93 (2016) 076002
[arXiv:1601.02787].
34. K. G. Wilson, Phys. Rev. 179 (1969) 1499.
35. R. J. Hill and G. Paz, Phys. Rev. D 95 (2017) 094017
[arXiv:1611.09917].
36. A. J. Buras, Rev. Mod. Phys. 52 (1980) 199.
37. Y. L. Dokshitzer, Sov. Phys. JETP 46 (1977) 641 [Zh.
Eksp. Teor. Fiz. 73 (1977) 1216].
38. V. Gribov and L. Lipatov, Sov. J. Nucl. Phys. 15 (1972)
438 [Yad. Fiz. 15 (1972) 781].
39. G. Altarelli and G. Parisi, Nucl. Phys. B 126 (1977) 298.
40. J. Gasser and H. Leutwyler, Phys. Rept. 87 (1982) 77.
41. S. Aoki et al. [Flavour Lattice Averaging Group], Eur.
Phys. J. C 80 (2020) 113 [arXiv:1902.08191].
42. J. Gasser and H. Leutwyler, Nucl. Phys. B 250 (1985)
539.
43. J. Kambor, C. Wiesendanger and D. Wyler, Nucl. Phys.
B 465 (1996) 215 [hep-ph/9509374].
44. A. Anisovich and H. Leutwyler, Phys. Lett. B 375 (1996)
335 [hep-ph/9601237].
45. G. Colangelo, S. Lanz, H. Leutwyler and E. Passemar,
Eur. Phys. J. C 78 (2018) 947 [arXiv:1807.11937].
46. K. G. Chetyrkin and M. F. Zoller, JHEP 1206 (2012)
033 [arXiv:1205.2892].
47. A. Grozin, hep-ph/0508242.
48. M. A. Shifman, A. I. Vainshtein and V. I. Zakharov, Nucl.
Phys. B 147 (1979) 385.
49. D. Drechsel, S. S. Kamalov and L. Tiator, Eur. Phys. J.
A 34 (2007) 69 [arXiv:0710.0306].
50. S. S. Kamalov, S. N. Yang, D. Drechsel, O. Hanstein
and L. Tiator, Phys. Rev. C 64 (2001) 032201 [nucl-
th/0006068].
51. M. Hilt, B. C. Lehnhart, S. Scherer and L. Tiator, Phys.
Rev. C 88 (2013) 055207 [arXiv:1309.3385].
52. http://portal.kph.uni-mainz.de/MAID/
53. P. E. Bosted and M. E. Christy, Phys. Rev. C 77 (2008)
065206 [arXiv:0711.0159].
54. M. E. Christy and P. E. Bosted, Phys. Rev. C 81 (2010)
055213 [arXiv:0712.3731].
55. J. Alwall and G. Ingelman, Phys. Lett. B 596 (2004) 77
[hep-ph/0402248].
56. S. Alekhin, J. Bl¨umlein and S. Moch, Phys. Rev. D 89
(2014) 054028 [arXiv:1310.3059].
57. S. Alekhin, J. Bl¨umlein, S. Moch and R. Placakyte, Phys.
Rev. D 96 (2017) 014011 [arXiv:1701.05838].
58. S. Alekhin, J. Bl¨umlein and S. Moch, PoS DIS 2019
(2019) 002 [arXiv:1909.03533].
59. A. M. Baldin, Nucl. Phys. 18 (1960) 310.
60. M. Tanabashi et al. (Particle Data Group), Phys. Rev. D
98 (2018) 030001 and 2019 update.
61. H. W. Grießhammer, J. A. McGovern and D. R. Phillips,
PoS CD 2018 (2019) 009.
62. V. Lensky, F. Hagelstein, V. Pascalutsa and
M. Vanderhaeghen, Phys. Rev. D 97 (2018) 074012
[arXiv:1712.03886].
63. F. Hagelstein, Symmetry 12 (2020) 1407
[arXiv:2006.16124].
64. J. M. Alarc´on, F. Hagelstein, V. Lensky and
V.
Pascalutsa,
Phys.
Rev.
D
102
(2020)
014006
[arXiv:2005.09518].
65. J. A. Melendez, R. J. Furnstahl, H. W. Grießhammer,
J. A. McGovern, D. R. Phillips and M. T. Pratola, arXiv:
2004.11307.
66. W. Detmold, B. C. Tiburzi and A. Walker-Loud, Phys.
Rev. D 73 (2006) 114505 [hep-lat/0603026].
67. W. Detmold, B. C. Tiburzi and A. Walker-Loud, Phys.
Rev. D 79 (2009) 094505 [arXiv:0904.1586].
68. W. Detmold, B. C. Tiburzi and A. Walker-Loud, Phys.
Rev. D 81 (2010) 054502 [arXiv:1001.1131].
69. R. Bignell, W. Kamleh and D. Leinweber, Phys. Rev. D
101 (2020) 094502 [arXiv:2002.07915].
70. J. J. Sakurai and D. Schildknecht, Phys. Lett. 40B
(1972) 121.
71. C. G. Callan, Jr. and D. J. Gross, Phys. Rev. Lett. 22
(1969) 156.
72. V. Punjabi, C. F. Perdrisat, M. K. Jones, E. J. Brash
and C. E. Carlson, Eur. Phys. J. A 51 (2015) 79
[arXiv:1503.01452].
73. J. J. Kelly, Phys. Rev. C 70 (2004), 068202.
74. Z. Ye, J. Arrington, R. J. Hill and G. Lee, Phys. Lett. B
777 (2018) 8 [arXiv:1707.09063].
75. K.
Borah,
R.
J.
Hill,
G.
Lee
and
O.
Tomalak,
arXiv:2003.13640.
76. S. R. Beane, K. Orginos and M. J. Savage, Nucl. Phys.
B 768 (2007) 38 [hep-lat/0605014].
77. T. Blum, R. Zhou, T. Doi, M. Hayakawa, T. Izubuchi,
S. Uno and N. Yamada, Phys. Rev. D 82 (2010) 094508
[arXiv:1006.1311].
78. G. M. de Divitiis et al. [RM123 Collaboration], Phys.
Rev. D 87 (2013) 114505 [arXiv:1303.4896].
79. S. Borsanyi et al. [Budapest-Marseille-Wuppertal Col-
laboration],
Phys.
Rev.
Lett.
111
(2013)
252001
[arXiv:1306.2287].
80. S. Borsanyi et al., Science 347 (2015) 1452
[arXiv:1406.4088].
81. M. G. Endres, A. Shindler, B. C. Tiburzi and A. Walker-
Loud, Phys. Rev. Lett. 117 (2016) 072002
[arXiv:1507.08916].
82. R. Horsley et al., JHEP 1604 (2016) 093
[arXiv:1509.00799].
83. D. A. Brantley, B. Joo, E. V. Mastropas, E. Mereghetti,
H. Monge-Camacho, B. C. Tiburzi and A. Walker-Loud,
arXiv:1612.07733.
84. R. Horsley et al. [CSSM and QCDSF and UKQCD
Collaborations],
J.
Phys.
G
46
(2019)
115004
[arXiv:1904.02304].
85. O. Tomalak and M. Vanderhaeghen, Eur. Phys. J. A 51
(2015) 24 [arXiv:1408.5330].
86. M. Damashek and F. J. Gilman, Phys. Rev. D 1 (1970)
1319.
87. C. A. Dominguez, C. Ferro Fontan and R. Suaya, Phys.
Lett. 31B (1970) 365.
88. S. J. Brodsky, F. J. Llanes-Estrada and A. P. Szczepa-
niak, Phys. Rev. D 79 (2009) 033012 [arXiv:0812.0395].
89. S. J. Brodsky, F. E. Close and J. F. Gunion, Phys. Rev.
D 5 (1972) 1384.
90. S. J. Brodsky, F. E. Close and J. F. Gunion, Phys. Rev.
D 6 (1972) 177.
91. M. Creutz, Phys. Rev. D 7 (1973) 1539.
92. D. M¨uller and K. M. Semenov-Tian-Shansky, Phys. Rev.
D 92 (2015) 074025 [arXiv:1507.02164].
93. D. M¨uller and K. M. Semenov-Tian-Shansky, EPJ Web
Conf. 112 (2016) 01016 [arXiv:1601.01830].
