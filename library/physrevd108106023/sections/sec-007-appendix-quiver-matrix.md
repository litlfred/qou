---
doc_id: physrevd108106023
doc_title: "Knot-quiver correspondence for double twist knots"
section_id: sec-007-appendix-quiver-matrix
section_title: "APPENDIX: QUIVER MATRIX"
section_number: null
pages: 8-11
source_pdf: PhysRevD.108.106023.pdf
source_sha256: 50c7980e88cd21a0
toc_source: inferred
doc_brief: "Knot-quiver correspondence for double twist knots — 9 sections: Front matter; INTRODUCTION; Reverse engineering of Melvin-Mort"
---
For clarity, we present the steps in obtaining the quiver
representation for a knot 83 in this appendix. The Alexander
polynomial in variable X is Δ83ðXÞ ¼ ð1 −4XÞ. Such a
form implied that we could perform the reverse MMR
method discussed [13] for ΔKðXÞ ¼ 1 −pX with p being
integer. The r-colored Jones polynomials take the following
interesting form:
Jrð83; qÞ ¼
X
r≥k8≥…≥k1≥0
ðq2; q2Þk8
 r
k8
 k8
k7
 k7
k6
 k6
k5
 k5
k4
 k4
k3
 k3
k2
 k2
k1

q
Pp
i;j¼1 aijkikjq
Pp
i¼1 bikið−1Þ
Pp
i¼1 ciki:
By comparing these polynomials with known r-colored Jones polynomials, we have successfully determined the unknown
parameters aij, bi, ci. The exact expression is
Jrð83; qÞ ¼
X
r≥k8≥…≥k1≥0
ð−1Þk2þk4þk6ðq2; q2Þk8
 r
k8
 Y
6
i¼0
 k8−i
k7−i

q2k1þ3k2þ2rk2−2k1k2−2k3k8þ2k5k8
× q−k4−2rk4þ2k1k4−2k3k4þk2
4þ2k5−2k1k5þ2k3k5þ3k6qþ2rk6−2k1k6þ2k3k6−2k5k6þk2
6−2k7þ2k1k7−2k3k7
× qþ2k5k7−2k8−2rk8þ2k1k8þk2
2−2k3þ2k1k3−2k7k8:
Using the q-binomial and q-Pochhammer identities discussed in Ref. [1], we could rewrite the r-colored Jones
polynomial as
Jrð83; qÞ ¼
X
r;k;α
ð−1Þk2þk4þk6þα8
Q6
i¼0ðq2; q2Þk8−i−α8−i−k8−i−1þα8−i−1
ðq2; q2Þr
ðq2; q2Þr−k8
Q6
i¼0ðq2; q2Þα8−i−α8−i−1ðq2; q2Þk1−α1
×
1
ðq; qÞα1
qð3k2þ2rk2þk2
2−k4−2rk4Þþ2ðk1−k3þk5−k7Þq2ð−k1k2þk1k3þk1k4−k3k4−k1k5þk3k5−k1k6þk3k6−k5k6Þ
× q
P6
i¼0 2ðα8−i−α7−iÞðk7−i−α7−iÞþα8ðα8þ1Þþk2
4þ3k6qðþ2rk6þk2
6−2k8−k2
8−2rk8þ2ðþk1k7−k3k7ÞÞq2ðk5k7þk1k8−k3k8þk5k8−k7k8Þ;
ðA1Þ
where the summation variables in the first line must obey r ≥k8 ≥α8 ≥k7 ≥α7… ≥k1 ≥α1 ≥0. By making the
following substitutions αj ¼ Pj−1
i¼0 d19−2jþ2i and kj ¼ P2j−1
i¼0 d18−2jþi in Eq. (A1), we obtain the motivic series quiver
representation form,
Jrð83; qÞ ¼
X
d1þd2…þd17¼r
ð−1Þd3þd5þd6þd8þd11þd13þd14þd16 ðq; qÞrq
P
C
83
ði;jÞdidj
Q17
i¼1ðq2; q2Þdi
qð−2d2−d3−4d4−3d5−d6Þ
× qðd8þ2d9þd11−2d12−d13þd14þ2d15þ3d16þ4d17Þ:
We can read off the quiver matrix elements C83 from the above expression. See Sec. II A, where we have presented the
matrix. The explicit matrix elements for CKð3;−2Þ and CKð3;−3Þ are presented below,
Cð3;−2Þ ¼
0
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
@
0
−1 −1 −1 −1
0
0
0
0
−1 −1 −1 −1
0
0
0
0
−1 −1 −1 −1
0
0
0
0
−1
−2 −2 −3 −3
−2 −2 −1 −1
−2 −2 −3 −3
−2 −2 −1 −1
−2 −2 −3 −3
−2 −2 −1 −1
−1
−2 −1 −2 −2
−1 −1 0
0
−1 −1 −2 −2
−1 −1 0
0
−1 −1 −2 −2
−1 −1 0
0
−1
−3 −2 −4 −4
−3 −3 −1 −1
−2 −2 −4 −4
−3 −3 −1 −1
−2 −2 −4 −4
−3 −3 −1 −1
−1
−3 −2 −4 −3
−2 −2 0
0
−1 −1 −3 −3
−2 −2 0
0
−1 −1 −3 −3
−2 −2 0
0
0
−2 −1 −3 −2
−1 −1 0
0
−1 −1 −2 −2
−1 −1 0
0
−1 −1 −2 −2
−1 −1 0
0
0
−2 −1 −3 −2
−1 0
1
1
0
0 −1 −1
0
0
1
1
0
0 −1 −1
0
0
1
1
0
−1 0 −1 0
0
1
1
1
0
0
0
0
1
1
1
1
0
0
0
0
1
1
1
1
0
−1 0 −1 0
0
1
1
2
1
1
1
1
2
2
2
2
1
1
1
1
2
2
2
2
−1
−2 −1 −2 −1
−1 0
0
1
0
0 −1 −1
0
0
1
1
0
0 −1 −1
0
0
1
1
−1
−2 −1 −2 −1
−1 0
0
1
0
1
0
0
1
1
2
2
1
1
0
0
1
1
2
2
−1
−3 −2 −4 −3
−2 −1 0
1
−1 0 −2 −2
−1 −1 1
1
0
0 −2 −2
−1 −1 1
1
−1
−3 −2 −4 −3
−2 −1 0
1
−1 0 −2 −1
0
0
2
2
1
1 −1 −1
0
0
2
2
0
−2 −1 −3 −2
−1 0
1
2
0
1 −1 0
1
1
2
2
1
1
0
0
1
1
2
2
0
−2 −1 −3 −2
−1 0
1
2
0
1 −1 0
1
2
3
3
2
2
1
1
2
2
3
3
0
−1 0 −1 0
0
1
1
2
1
2
1
2
2
3
3
3
2
2
2
2
3
3
3
3
0
−1 0 −1 0
0
1
1
2
1
2
1
2
2
3
3
4
3
3
3
3
4
4
4
4
−1
−2 −1 −2 −1
−1 0
0
1
0
1
0
1
1
2
2
3
2
2
1
1
2
2
3
3
−1
−2 −1 −2 −1
−1 0
0
1
0
1
0
1
1
2
2
3
2
3
2
2
3
3
4
4
−1
−3 −2 −4 −3
−2 −1 0
1
−1 0 −2 −1
0
1
2
3
1
2
0
0
1
1
3
3
−1
−3 −2 −4 −3
−2 −1 0
1
−1 0 −2 −1
0
1
2
3
1
2
0
1
2
2
4
4
0
−2 −1 −3 −2
−1 0
1
2
0
1 −1 0
1
2
3
4
2
3
1
2
3
3
4
4
0
−2 −1 −3 −2
−1 0
1
2
0
1 −1 0
1
2
3
4
2
3
1
2
3
4
5
5
0
−1 0 −1 0
0
1
1
2
1
2
1
2
2
3
3
4
3
4
3
4
4
5
5
5
0
−1 0 −1 0
0
1
1
2
1
2
1
2
2
3
3
4
3
4
3
4
4
5
5
6
1
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
C
A
;

VIVEK KUMAR SINGH et ai.

o|ToTe Tele nr one Nala n ene Alanna nan t[n tantra t[t+ Nn tn vo
o|ToToT celeron er Nene NBR ANNAN HH tHINn TO tTN +t Ht H HH wT
ot TTT PN TPT en ale a Te Tele naam ti[a mana alana + ww
ot TPT TPN TT ea ale az Te Tele nan wm t[a mana alana t+ +
olN aT MH +HIM NBO L eo a ou Ttolea
i ee Re es ee a;o roteedgpeotp eS Nm tln nn oO 1c anaannn mn
olN tr tT MOH tIN NAO LL on VT ONS BW OL on TT Oln se
ee ee ee ee ed aN|o rotoseosslp ce Am tin nm oOo 1c a a t+ +
apa wet Owl tm NS SC LI VG ONT INS GO OL = =oN alos
Wy tororot fo orhtoreoreop se ro rerdryrpre a fo
ayn nn towMit mn na QC Lia gm ntmnN ag L o =o ratr awl L
rytororot forltororeps ro rerdryrppes a ST Pro rr om
ayn nt mtn NAN as QC LIa GN BAN AIS QO KG LX o cou o ole a
rytoro yoreororhrororep se po rrprypes ao asc oe aut +
= 9 Nt tT A NN _ | a ol “ “ = a
Hyroroborotorproreorrpse porrpti1ese ao noo 1 Vee oon
TW TIT Tp eT ee cle n ene slen ne nar mam nnn ala naam + +
TPT TTTIT TNT se Tee -|e-e-e-f- eas s|aa- aan naa
co|\ToToeo TT elon one Nene NB AIAN HAN MH HIN NM HON Ott +t +
o|ToToT elon omer alent nde AAanAn nanan rnnaaalnnnm naam
oy TTT PNG TPT en alee Te T elena nm manne ee al N NAAM
ot TTT PN TT ea ale za Te Tele nae an alae coco cofe aaa
olN a tT MH +t1N NB OL a Sn cot tlooxwas
fyi or roperdytorprasse aye roreoreoryr © oan roo} toe om
olN a tF MH tIM NY LL es ee TTtANAFA BA OK
Serr tt ritr ris nied Prrryrresrs Prrryrrescrs
apa mwa tO wt mM Ms SC LI VG MNT INN OCG ae wt HN MINN OS
Hhrororeot To orytororopes ported tyrreenrn rorororprpreean
alo NH TOMI TM AG QC LIA OG MNT TIN Mee LLG GN NT TIN MM AS LL
ry tororot Torlt ororops ro ror? tyrore Scorer dt tyrorort
Seals Re i ae i Coe ae a ee tmTtaANA BA OS
rytoro yoreororPrororep se rporrrprfrpepeosrarn rorororyropoeoonn
melana anton tna ANN =|7 ANH A AN es oe ANH A AN es oe
Hyrorororotorproreorrpse ro rrroryr ort Seo rrorrytoro dt
TIN RNR N BIR BE MB SB Hlo HO CO oO ole oe OH swe coooolnn ewe
Tes ie ee ee De Pe DD i=) oo coc co an oo coc co an
Selannsnaen ale gon gg lao oe ee leo OOo et elo oor tle crc ree
Hptob or tr ttf free ecrrirs1ijesss ecrrirs1ijesss
o|\ToToT celeron eR Nee eR RBI NNN ANA AJR ee RR BRINN ANNAN
Sy, eoy7reyreyer err ae er eee eyr Fr FFF Te er er ee eyr FATA
aIN wren NN AIAN A — Staton iito! — Seen titentite! a
Syrororororryt pore Seorrrresses Seorrrresses
aanaanalanwaa =eananaalaeanaa =eananaalaeanaa
Slrororotororyt to oror Se Syr or ror ro oty rb br br Sf Shr ror br br ory rr ree
olN aT MH TIN Ne BL LIQ GCN NM MINN ee LLCO GC NNN MINN SS LL
Shroroto tor tyrorr sd Sort lt ryt ror Sort lt ryt ror
oIN at MH tTIMN MANN EL CJ e aN Mt tIN NNN LD Blom eNO Mt HIM MANN OY
ioe OD OD OO DD rel dD Oe
Sal SO os 2 as Cs Ss Oe or SD sO or or OO
Wyboro oro d Toryb toror Sf Ser or oror roryt torre fpr or ror br ryt top ree
aN NH TO MVSH HH NH se BIN AN TTC VIH HN NH Sse BIN AN TTF VO YVIH HN HS SS
Wytoro rod Po PPro rob or or orp ro br bot tT Tp ror br br br rp or td Tp rr tt
an nt nT TIO NNN =— se mon tT TIM NN =— se mon tT TIM NN
Wytor yor to tyrororpr eS Serorore rt tyr or pore fyr roror to tyroror re es
mela nt tT KH HIT TNH Hew BINA tT tH HIT TO HGH Bein aA tr TH HIT tN HN =
Wybor yo vor red bor or or rp rb bb rp Pr Pr rrp rt
BIN BANNAN Ae eee QD Asa ae NNN Ae Be Be Be QC Aa ANNAN NAIR ee Be QO KL
Wytboro ror obo tebe bo bop SO Shr br ror pr ory hb bb SSP tr br br bry td ee
FIANNA N NM MIAN A AN TPT AINANMNMNM NAN MINANANANAN TAINAN HMH AMINA AAA TT
[Oe Oe De DD nD DD DDO OD
Slroreptperfesr err Ff Fyre tr pe eorye rer er ef Fyre te th hl herr ere se

i

7

1S)

[4] T. Ekholm, A. Gruen, S. Gukov, P. Kucharski, S. Park,

[1] P. Kucharski, M. Reineke, M. StoSi¢, and P. Sutkowski,

M. Sto8i¢, and P. Sutkowski, J. Geom. Phys. 177, 104520
(2022).
[5] M. Stosic and P. Wedrich, Int. Math. Res. Not. 2021, 4169

Adv. Theor. Math. Phys. 23, 1849 (2019).
[2] P. Kucharski, M. Reineke, M. StoSi¢, and P. Sutkowski,

Phys. Rev. D 96, 121902 (2017).
[3] T. Ekholm, P. Kucharski, and P. Longhi, arXiv:2108.12645.

(2021).

[6] J. Jankowski, P. Kucharski, H. Larraguível, D. Noshchenko,
and P. Sułkowski, Phys. Rev. D 104, 086017 (2021).
[7] T. Ekholm, P. Kucharski, and P. Longhi, J. High Energy
Phys. 02 (2020) 018.
[8] T. Ekholm, P. Kucharski, and P. Longhi, Commun. Math.
Phys. 379, 361 (2020).
[9] A. Mironov, A. Morozov, A. Morozov, P. Ramadevi, and
V. K. Singh, J. High Energy Phys. 07 (2015) 109.
[10] A. Mironov, A. Morozov, A. Morozov, P. Ramadevi,
V. K. Singh, and A. Sleptsov, J. Phys. A 50, 085201 (2017).
[11] Knot data, http://knotebook.org (2018).
[12] M. Stosic and P. Wedrich, J. Lond. Math. Soc. 104, 341
(2021).
[13] S. Banerjee, J. Jankowski, and P. Sułkowski, J. High Energy
Phys. 12 (2020) 095.
[14] Q. Chen, K. Liu, and S. Zhu, arXiv:2110.03616.
[15] H. E. Wang, Y. J. Yang, H. D. Zhang, and S. Nawata, Ann.
Henri Poincare 22, 2691 (2021).
[16] H. Ooguri and C. Vafa, Nucl. Phys. B577, 419 (2000).
[17] M. Reineke, Doc. Math. 17, 1 (2012).
[18] M. Kontsevich and Y. Soibelman, Commun. Numb. Theor.
Phys. 5, 231 (2011).
[19] A. I. Efimov, Compos. Math. 148, 1133 (2012).
[20] P. R. Devi, T. R. Govindarajan, and R. K. Kaul, Nucl. Phys.
B402, 548 (1993).
[21] S. Nawata, P. Ramadevi, Zodinmawia, and X. Sun, J. High
Energy Phys. 11 (2012) 157.
[22] J. Lovejoy and R. Osburn, J. Knot Theor. Ramif. 30, 28
(2021).
[23] S. Chauhan, D. Noshchenko, P. Ramadevi, and V. K. Singh
(to be published).
[24] S. Gukov and C. Manolescu, Quantum Topol. 12 (2021).
[25] T. Ekholm, A. Gruen, S. Gukov, P. Kucharski, S. Park, and
P. Sułkowski, Commun. Math. Phys. 396, 143 (2022).
[26] P. Kucharski, J. High Energy Phys. 09 (2020) 075.
[27] S. Park, J. Knot Theor. Ramif. 29, 2050097 (2020).
[28] H. E. Wang, Y. J. Yang, H. D. Zhang, and S. Nawata, Ann.
Henri Poincar´e 22, 2691 (2021).
