---
doc_id: physrevd108106023
doc_title: "I. INTRODUCTION Knot-quiver correspondence (KQC) conjectured by Kucharski-Reineke-Stosic-Sulkowski [1] provides a new encoding of HOMFL Y -PT invariants of knots in terms of the re"
section_id: sec-008-acknowledgments
section_title: "Acknowledgments"
section_number: null
pages: 8-11
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
doc_brief: "Knot-quiver correspondence for double twist knots Vivek Kumar Singh * — 9 sections: INTRODUCTION; DOUBLE TWIST KNOTS; Fk ˜Fk /C1/C1/C1 /C1/C1/C1 Fk ˜Fk"
---
The work of V . K. S. is supported by “Tamkeen under
the NYU Abu Dhabi Research Institute Grant No. CG008
and ASPIRE Abu Dhabi under Project AARE20-336 ”.
V . K. S. would like to thank P . Sulkowski, Q. Chen,
Hisham Sati, and Urs Schreiber for the helpful discussion.
P . R. is thankful for the SERB (MA TRICS) MTR/2019/
000956 funding, which enabled her to visit University of
Warsaw and present these results. P . R. would also like to
acknowledge the ICTP ’s Associate programme, which
helped her to complete this project during the visit as a
senior associate. S. C. and P . R. would like to thank all the
speakers and the organizers of the Learning workshop
on BPS states and three-manifolds for discussions and
interactions on “knot-quiver” correspondence. B. P . M.
acknowledges the research grant for faculty under IoE
Scheme (Grant No. 6031) of Banaras Hindu University.
A. D. would like to thank UGC for the research fellowship.
P . R. would like to acknowledge the SPARC/2019-2020/
P2116/ project funding.
APPENDIX: QUIVER MATRIX
For clarity, we present the steps in obtaining the quiver
representation for a knot 8
3 in this appendix. The Alexander
polynomial in variable X is Δ83 ðXÞ¼ð 1 − 4XÞ. Such a
form implied that we could perform the reverse MMR
method discussed [13] for ΔK ðXÞ¼ 1 − pX with p being
integer. The r-colored Jones polynomials take the following
interesting form:
Jrð83; qÞ¼
X
r≥k8≥… ≥k1≥0
ðq2; q2Þk8
/C20r
k8
/C21/C20k8
k7
/C21/C20k7
k6
/C21/C20k6
k5
/C21/C20k5
k4
/C21/C20k4
k3
/C21/C20k3
k2
/C21/C20k2
k1
/C21
q
Pp
i;j¼1 aijkikj q
Pp
i¼1 biki ð−1Þ
Pp
i¼1 ciki :
By comparing these polynomials with known r-colored Jones polynomials, we have successfully determined the unknown
parameters aij, bi, ci. The exact expression is
Jrð83; qÞ¼
X
r≥k8≥… ≥k1≥0
ð−1Þk2þk4þk6 ðq2; q2Þk8
/C20r
k8
/C21Y6
i¼0
/C20k8−i
k7−i
/C21
q2k1þ3k2þ2rk2−2k1k2−2k3k8þ2k5k8
× q−k4−2rk4þ2k1k4−2k3k4þk2
4þ2k5−2k1k5þ2k3k5þ3k6 qþ2rk6−2k1k6þ2k3k6−2k5k6þk2
6−2k7þ2k1k7−2k3k7
× qþ2k5k7−2k8−2rk8þ2k1k8þk2
2−2k3þ2k1k3−2k7k8 :
Using the q-binomial and q-Pochhammer identities discussed in Ref. [1], we could rewrite the r-colored Jones
polynomial as
Jrð83; qÞ¼
X
r;k;α
ð−1Þk2þk4þk6þα8
Q6
i¼0ðq2; q2Þk8−i−α8−i−k8−i−1þα8−i−1
ðq2; q2Þr
ðq2; q2Þr−k8
Q6
i¼0ðq2; q2Þα8−i−α8−i−1 ðq2; q2Þk1−α1
× 1
ðq; qÞα1
qð3k2þ2rk2þk2
2−k4−2rk4Þþ2ðk1−k3þk5−k7Þq2ð−k1k2þk1k3þk1k4−k3k4−k1k5þk3k5−k1k6þk3k6−k5k6Þ
× q
P6
i¼0 2ðα8−i−α7−iÞðk7−i−α7−iÞþα8ðα8þ1Þþk2
4þ3k6 qðþ2rk6þk2
6−2k8−k2
8−2rk8þ2ðþk1k7−k3k7ÞÞq2ðk5k7þk1k8−k3k8þk5k8−k7k8Þ; ðA1Þ
where the summation variables in the first line must obey r ≥ k8 ≥ α8 ≥ k7 ≥ α7… ≥ k1 ≥ α1 ≥ 0.B ym a k i n gt h e
following substitutions αj ¼ Pj−1
i¼0 d19−2jþ2i and kj ¼ P2j−1
i¼0 d18−2jþi in Eq. (A1), we obtain the motivic series quiver
representation form,
Jrð83; qÞ¼
X
d1þd2… þd17 ¼r
ð−1Þd3þd5þd6þd8þd11 þd13 þd14 þd16
ðq; qÞrq
P
C
83
ði;jÞdidj
Q17
i¼1ðq2; q2Þdi
qð−2d2−d3−4d4−3d5−d6Þ
× qðd8þ2d9þd11 −2d12 −d13 þd14 þ2d15 þ3d16 þ4d17 Þ:
VIVEK KUMAR SINGH et al. PHYS. REV . D 108, 106023 (2023)
106023-8
We can read off the quiver matrix elements C83 from the above expression. See Sec. II A, where we have presented the
matrix. The explicit matrix elements for CKð3;−2Þ and CKð3;−3Þ are presented below,
Cð3;−2Þ ¼
0
BBBB
BBB
B
BBB
BBB
B
BBB
B
BBB
BBB
B
BBB
B
BBB
BBB
B
BBB
B
BBB
BBB
B
BBB
BBB
B
BBB
@
0
−1 −1 −1 −1 0000 −1 −1 −1 −1 0000 −1 −1 −1 −1 0000
−1 −2 −2 −3 −3 −2 −2 −1 −1 −2 −2 −3 −3 −2 −2 −1 −1 −2 −2 −3 −3 −2 −2 −1 −1
−1 −2 −1 −2 −2 −1 −10 0 −1 −1 −2 −2 −1 −10 0 −1 −1 −2 −2 −1 −10 0
−1 −3 −2 −4 −4 −3 −3 −1 −1 −2 −2 −4 −4 −3 −3 −1 −1 −2 −2 −4 −4 −3 −3 −1 −1
−1 −3 −2 −4 −3 −2 −20 0 −1 −1 −3 −3 −2 −20 0 −1 −1 −3 −3 −2 −20 0
0 −2 −1 −3 −2 −1 −10 0 −1 −1 −2 −2 −1 −10 0 −1 −1 −2 −2 −1 −10 0
0 −2 −1 −3 −2 −1 011 00 −1 −1 0011 00 −1 −1 0011
0 −10 −10 0111 0000 1111 0000 1111
0 −10 −10 0112 1111 2222 1111 2222
−1 −2 −1 −2 −1 −1 001 00 −1 −1 0011 00 −1 −1 0011
−1 −2 −1 −2 −1 −1 001 0100 1122 1100 1122
−1 −3 −2 −4 −3 −2 −10 1 −10 −2 −2 −1 −11 1 00 −2 −2 −1 −11 1
−1 −3 −2 −4 −3 −2 −10 1 −10 −2 −1 0022 11 −1 −1 0022
0 −2 −1 −3 −2 −1 012 01 −10 1122 1100 1122
0 −2 −1 −3 −2 −1 012 01 −10 1233 2211 2233
0 −10 −10 0112 1212 2333 2222 3333
0 −10 −10 0112 1212 2334 3333 4444
−1 −2 −1 −2 −1 −1 001 0101 1223 2211 2233
−1 −2 −1 −2 −1 −1 001 0101 1223 2322 3344
−1 −3 −2 −4 −3 −2 −10 1 −10 −2 −1 0123 1200 1133
−1 −3 −2 −4 −3 −2 −10 1 −10 −2 −1 0123 1201 2244
0 −2 −1 −3 −2 −1 012 01 −10 1234 2312 3344
0 −2 −1 −3 −2 −1 012 01 −10 1234 2312 3455
0 −10 −10 0112 1212 2334 3434 4555
0 −10 −10 0112 1212 2334 3434 4556
1
CCCC
CCC
C
CCC
CCC
C
CCC
C
CCC
CCC
C
CCC
C
CCC
CCC
C
CCC
C
CCC
CCC
C
CCC
CCC
C
CCC
A
;
KNOT-QUIVER CORRESPONDENCE FOR DOUBLE TWIST KNOTS PHYS. REV . D 108, 106023 (2023)
106023-9
Cð3;−3Þ ¼
0
BBB
B
B
B
B
B
B
B
B
B
BBB
B
B
B
B
B
B
B
B
B
BBB
B
B
B
B
B
B
B
B
BBB
B
B
B
B
B
B
B
B
B
BBB
B
B
B
B
B
B
B
B
B
BBB
B
B
B
B
B
B
B
B
B
BBB
B
B
B
B
B
B
B
B
BBB
B
B
B
B
@
0
−1 −1 −1 −1 −1 −1 000000 −1 −1 −1 −1 −1 −1 000000 −1 −1 −1 −1 −1 −1 000000
−1 −2 −2 −3 −3 −3 −3 −2 −2 −2 −2 −1 −1 −2 −2 −3 −3 −3 −3 −2 −2 −2 −2 −1 −1 −2 −2 −3 −3 −3 −3 −2 −2 −2 −2 −1 −1
−1 −2 −1 −2 −2 −2 −2 −1 −1 −1 −10 0 −1 −1 −2 −2 −2 −2 −1 −1 −1 −10 0 −1 −1 −2 −2 −2 −2 −1 −1 −1 −10 0
−1 −3 −2 −4 −4 −5 −5 −4 −4 −3 −3 −1 −1 −2 −2 −4 −4 −5 −5 −4 −4 −3 −3 −1 −1 −2 −2 −4 −4 −5 −5 −4 −4 −3 −3 −1 −1
−1 −3 −2 −4 −3 −4 −4 −3 −3 −2 −20 0 −1 −1 −3 −3 −4 −4 −3 −3 −2 −20 0 −1 −1 −3 −3 −4 −4 −3 −3 −2 −20 0
−1 −3 −2 −5 −4 −6 −6 −5 −5 −3 −3 −1 −1 −2 −2 −4 −4 −6 −6 −5 −5 −3 −3 −1 −1 −2 −2 −4 −4 −6 −6 −5 −5 −3 −3 −1 −1
−1 −3 −2 −5 −4 −6 −5 −4 −4 −2 −20 0 −1 −1 −3 −3 −5 −5 −4 −4 −2 −20 0 −1 −1 −3 −3 −5 −5 −4 −4 −2 −20 0
0 −2 −1 −4 −3 −5 −4 −3 −3 −2 −20 0 −1 −1 −3 −3 −4 −4 −3 −3 −2 −20 0 −1 −1 −3 −3 −4 −4 −3 −3 −2 −20 0
0 −2 −1 −4 −3 −5 −4 −3 −2 −1 −11 1 00 −2 −2 −3 −3 −2 −2 −1 −11 1 00 −2 −2 −3 −3 −2 −2 −1 −11 1
0 −2 −1 −3 −2 −3 −2 −2 −1 −1 −10 0 −1 −1 −2 −2 −2 −2 −1 −1 −1 −10 0 −1 −1 −2 −2 −2 −2 −1 −1 −1 −10 0
0 −2 −1 −3 −2 −3 −2 −2 −1 −10 1 1 00 −1 −1 −1 −1 000011 00 −1 −1 −1 −1 000011
0 −10 −10 −10 010111 000000 111111 000000 111111
0 −10 −10 −10 010112 111111 222222 111111 222222
−1 −2 −1 −2 −1 −2 −1 −10 −10 0 1 00 −1 −1 −1 −1 000011 00 −1 −1 −1 −1 000011
−1 −2 −1 −2 −1 −2 −1 −10 −10 0 1 010000 111122 110000 111122
−1 −3 −2 −4 −3 −4 −3 −3 −2 −2 −10 1 −10 −2 −2 −3 −3 −2 −2 −1 −11 1 00 −2 −2 −3 −3 −2 −2 −1 −11 1
−1 −3 −2 −4 −3 −4 −3 −3 −2 −2 −10 1 −10 −2 −1 −2 −2 −1 −1 0022 11 −1 −1 −2 −2 −1 −1 0022
−1 −3 −2 −5 −4 −6 −5 −4 −3 −2 −10 1 −10 −3 −2 −4 −4 −3 −3 −1 −11 1 00 −2 −2 −4 −4 −3 −3 −1 −11 1
−1 −3 −2 −5 −4 −6 −5 −4 −3 −2 −10 1 −10 −3 −2 −4 −3 −2 −2 0022 11 −1 −1 −3 −3 −2 −2 0022
0 −2 −1 −4 −3 −5 −4 −3 −2 −10 1 2 01 −2 −1 −3 −2 −1 −1 0022 11 −1 −1 −2 −2 −1 −1 0022
0 −2 −1 −4 −3 −5 −4 −3 −2 −10 1 2 01 −2 −1 −3 −2 −1 01133 2200 −1 −1 001133
0 −2 −1 −3 −2 −3 −2 −2 −1 −10 1 2 01 −10 −10 011122 110000 111122
0 −2 −1 −3 −2 −3 −2 −2 −1 −10 1 2 01 −10 −10 011233 221111 222233
0 −10 −10 −10 010112 121212 232333 222222 333333
0 −10 −10 −10 010112 121212 232334 333333 444444
−1 −2 −1 −2 −1 −2 −1 −10 −10 0 1 010101 121223 221111 222233
−1 −2 −1 −2 −1 −2 −1 −10 −10 0 1 010101 121223 232222 333344
−1 −3 −2 −4 −3 −4 −3 −3 −2 −2 −10 1 −10 −2 −1 −2 −1 −1 00123 1200 −1 −1 001133
−1 −3 −2 −4 −3 −4 −3 −3 −2 −2 −10 1 −10 −2 −1 −2 −1 −1 00123 120100 112244
−1 −3 −2 −5 −4 −6 −5 −4 −3 −2 −10 1 −10 −3 −2 −4 −3 −2 −1 0123 12 −10 −2 −2 −1 −1 1133
−1 −3 −2 −5 −4 −6 −5 −4 −3 −2 −10 1 −10 −3 −2 −4 −3 −2 −1 0123 12 −10 −2 −1 002244
0 −2 −1 −4 −3 −5 −4 −3 −2 −10 1 2 01 −2 −1 −3 −2 −1 01234 2301 −10 112244
0 −2 −1 −4 −3 −5 −4 −3 −2 −10 1 2 01 −2 −1 −3 −2 −1 01234 2301 −10 123355
0 −2 −1 −3 −2 −3 −2 −2 −1 −10 1 2 01 −10 −10 011234 231212 233344
0 −2 −1 −3 −2 −3 −2 −2 −1 −10 1 2 01 −10 −10 011234 231212 233455
0 −10 −10 −10 010112 121212 232334 343434 454555
0 −10 −10 −10 010112 121212 232334 343434 454556
1
CCC
C
C
C
C
C
C
C
C
C
CCC
C
C
C
C
C
C
C
C
C
CCC
C
C
C
C
C
C
C
C
CCC
C
C
C
C
C
C
C
C
C
CCC
C
C
C
C
C
C
C
C
C
CCC
C
C
C
C
C
C
C
C
C
CCC
C
C
C
C
C
C
C
C
CCC
C
C
C
C
A
[1] P . Kucharski, M. Reineke, M. Sto šić, and P . Su łkowski,
Adv. Theor. Math. Phys. 23, 1849 (2019) .
[2] P . Kucharski, M. Reineke, M. Sto šić, and P . Su łkowski,
Phys. Rev. D 96, 121902 (2017) .
[3] T. Ekholm, P . Kucharski, and P . Longhi, arXiv:2108.12645.
[4] T. Ekholm, A. Gruen, S. Gukov, P . Kucharski, S. Park,
M. Sto šić, and P . Su łkowski, J. Geom. Phys. 177, 104520
(2022).
[5] M. Stosic and P . Wedrich, Int. Math. Res. Not. 2021, 4169
(2021).
VIVEK KUMAR SINGH et al. PHYS. REV . D 108, 106023 (2023)
106023-10
[6] J. Jankowski, P . Kucharski, H. Larraguível, D. Noshchenko,
and P . Sułkowski, Phys. Rev. D 104, 086017 (2021) .
[7] T. Ekholm, P . Kucharski, and P . Longhi, J. High Energy
Phys. 02 (2020) 018.
[8] T. Ekholm, P . Kucharski, and P . Longhi, Commun. Math.
Phys. 379, 361 (2020) .
[9] A. Mironov, A. Morozov, A. Morozov, P . Ramadevi, and
V . K. Singh, J. High Energy Phys. 07 (2015) 109.
[10] A. Mironov, A. Morozov, A. Morozov, P . Ramadevi,
V . K. Singh, and A. Sleptsov,J. Phys. A 50, 085201 (2017).
[11] Knot data, http://knotebook.org (2018).
[12] M. Stosic and P . Wedrich, J. Lond. Math. Soc. 104, 341
(2021).
[13] S. Banerjee, J. Jankowski, and P . Sułkowski, J. High Energy
Phys. 12 (2020) 095.
[14] Q. Chen, K. Liu, and S. Zhu, arXiv:2110.03616.
[15] H. E. Wang, Y . J. Yang, H. D. Zhang, and S. Nawata, Ann.
Henri Poincare 22, 2691 (2021) .
[16] H. Ooguri and C. V afa, Nucl. Phys. B577, 419 (2000) .
[17] M. Reineke, Doc. Math. 17, 1 (2012) .
[18] M. Kontsevich and Y . Soibelman, Commun. Numb. Theor.
Phys. 5, 231 (2011) .
[19] A. I. Efimov, Compos. Math. 148, 1133 (2012) .
[20] P . R. Devi, T. R. Govindarajan, and R. K. Kaul, Nucl. Phys.
B402, 548 (1993) .
[21] S. Nawata, P . Ramadevi, Zodinmawia, and X. Sun, J. High
Energy Phys. 11 (2012) 157.
[22] J. Lovejoy and R. Osburn, J. Knot Theor. Ramif. 30,2 8
(2021).
[23] S. Chauhan, D. Noshchenko, P . Ramadevi, and V . K. Singh
(to be published).
[24] S. Gukov and C. Manolescu, Quantum Topol. 12 (2021).
[25] T. Ekholm, A. Gruen, S. Gukov, P . Kucharski, S. Park, and
P. S ułkowski, Commun. Math. Phys. 396, 143 (2022) .
[26] P . Kucharski, J. High Energy Phys. 09 (2020) 075.
[27] S. Park, J. Knot Theor. Ramif. 29, 2050097 (2020) .
[28] H. E. Wang, Y . J. Yang, H. D. Zhang, and S. Nawata, Ann.
Henri Poincar´e 22, 2691 (2021) .
KNOT-QUIVER CORRESPONDENCE FOR DOUBLE TWIST KNOTS PHYS. REV . D 108, 106023 (2023)
106023-11
