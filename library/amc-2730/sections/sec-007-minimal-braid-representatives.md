---
doc_id: amc-2730
doc_title: "Braid representatives minimizing the number of simple walks *"
section_id: sec-007-minimal-braid-representatives
section_title: "Minimal braid representatives"
section_number: null
pages: 21-27
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
toc_source: outline
doc_brief: "Braid representatives minimizing the number of simple walks * — Given a knot, we develop methods for finding a braid representative that minimizes the number of simple walks."
---
Minimal braid representatives
In Table 5, we list knots up to 9 crossings with the braid representatives giving minimal
numbers of simple walks. More extensive tables of knots up to 13 crossings and braid
representatives for them can be found online at [7]. (In [7] and Table 1 below, we use the
notation for braid words from sagemath, meaning that a braid word σε1
a1 ¨ ¨ ¨ σεℓ
aℓis denoted
by rε1a1, . . . , εℓaℓs. Tables 4 and 5 use even more compactified notation similar to that at
the end of [16].)
These results are empirical. The braid words listed in Table 5 and [7] are the output of
a sagemath program developed by the second author. It takes as input braid representatives
Knot
Braid Word
|SWβ|
11a322
r´1, ´1, 2, ´3, 4, ´3, 2, ´3, 4, 1, 2, ´3, ´2, ´2s
51
12a23
r´1, ´3, 2, ´3, ´5, 2, 4, 1, 2, ´3, ´4, 5, 4, ´3, ´5, 4, 2s
153
12a155
r´1, 2, 2, ´3, 4, ´3, 4, ´5, ´4, 3, 2, 1, ´4, 5, 2, ´3, 2s
127
12a288
r´1, 2, 2, ´3, 2, ´3, 2, 1, 2, ´3, 4, 2, ´3, 4s
71
12a449
r´1, 2, 4, ´3, 4, 5, 4, 2, ´3, ´4, ´4, ´5, 1, 2, 4, ´3, 2s
125
12a494
r´1, 2, ´3, 4, 5, 2, ´3, ´4, ´4, 1, 2, ´3, 4, ´5, 4, ´3, 2s
137
12a750
r´1, 2, ´3, 2, ´3, 5, 4, ´3, ´4, ´4, ´5, ´4, ´4, ´3, 1, 4, ´2, 3, ´2s
183
12n546
r´1, 2, 3, 1, ´2, 1, 1, 1, 1, ´2, ´3, ´3, 2s
41
12n601
r´1, ´1, 2, 3, 3, 3, 2, ´4, ´4, ´3, 1, 2, 3, 3, ´4, 2s
67
12n622
r´1, ´1, 2, 2, 3, 3, 2, ´4, 1, ´2, 3, ´4, ´2, 3s
47
Table 1: Knots up to 12 crossings whose minimizing braid word begins with σ´1
1 .
for knots (given by the braids from [19] and [29]) and applies cyclic permutation, reflection,
and rotation. It then selects the braid word that minimizes the number of simple walks.
The output braid word may represent the knot K or its mirror image K˚, whichever has
fewest simple walks.
The braids listed have the fewest simple walks among all known braid representatives
for the given knots. In general, the question of finding a complete list of braid representa-
tives for a given knot is a delicate and open problem. As we shall see, it is not enough to
consider only braid representatives of minimal width. Even if it were, it is an open problem
to develop an algorithm for computing the braid width of a knot (see Open Problem 1 in
[6]). Nevertheless, these problems have been studied extensively, and much is known about
minimal braid representatives of low-crossing knots; see [13, 16] and [29].
Given a knot, one can look for braid representatives that minimize its braid width or the
braid length. For many knots, there is a braid representative that simultaneously minimizes
both the width and length, but in general, the braid representatives that minimize width
need not be the same as the ones that minimize length. The earliest known examples are
the knots 16472381 and 161223549, which were discovered by Stoimenow and have braid
width 4 but no minimal length braid representative of width 4, [28, Figure 7].
This interesting aspect has been further studied by Gittings [13] and Van Cott [30], and
the “smallest” example is the knot 10136. For all other knots with up to 10 crossings, there
is a braid representative that simultaneously minimizes the braid width and length. Further
examples of knots whose minimal width braid representatives are not minimal length are
listed in Table 4. (These examples come from [19].)
Interestingly, the braid representative that minimizes the number of simple walks is not
always a minimal length braid, nor is it always a minimal width braid either. For example,
consider the knots 10136 and 11n8 and their braid representatives in Table 4. For 10136, the
number of simple walks is minimized on a braid representative of minimal length but not
one of minimal width, whereas for 11n8, the number of simple walks is minimized on a
braid representative of minimal width but not one of minimal length. Similar examples can
be found among the other knots listed in Table 4.
Our computations suggest that, for any knot, one can always minimize the number
of simple walks on a braid representative of minimal width or minimal length. This is
an interesting problem for future investigation. In order to make progress, we need more
information about the minimal width and minimal length braid representatives for knots.
At present, we do not have complete information on the 13-crossing knots. In particular,
we do not know which 13-crossing knots have minimal length braid representatives that
are not minimal width. The braid representatives for the 13-crossing knots from [29] are
known to be of minimal width, but they are not known to be of minimal length.
Notice that for every knot in Table 5, the braid representative that minimizes the number
of simple walks begins with σ1. This is actually true for all knots up to 10 crossings, but
not immediately true for knots with 11 or more crossings (see [7]).
In general, by Lemma 5.4, the minimizing braid representative can always be chosen to
begin with either σ1 or σ´1
1 . For knots with 11 and 12 crossings, there are only a handful
of examples whose minimizing braid representative begins with σ´1
1
and not σ1. They are
listed in Table 1. (There are in addition 82 examples among the knots with 13 crossings,
see [7].) In each case, we can find a minimizing braid representative that begins with σ1 by
reversing the braid word and applying cyclic permutation. We explain these steps in more
detail.
Take, for example, the first knot in Table 1, namely 11a322. Its minimizing braid rep-
resentative is the braid word σ´2
1 σ2σ´1
3 σ4σ´1
3 σ2σ´1
3 σ4σ1σ2σ´1
3 σ´2
2 . The reversed braid
word will have the same number of simple walks, so it follows that σ´2
2 σ3σ2σ1
σ4σ´1
3 σ2σ´1
3 σ4σ´1
3 σ2σ´2
1
is also a minimizing braid word for 11a322. Now repeated ap-
plication of Lemma 5.4 shows that the braid word σ1σ4σ´1
3 σ2σ´1
3 σ4σ´1
3 σ2σ´2
1 σ´2
2 σ3σ2
is also minimizing for 11a322.
3
4
5
6
7
8
9
10
11
12
13
0
20
40
60
Average Number of Simple Walks
Table 2: Average number of simple walks by crossing number.
The same method applies to the other knots in Table 1. Each one admits a minimizing
braid word that starts with σ1. A similar argument applies to the braid representatives for
the 13 crossing knots that begin with σ´1
1 . This follows by a routine but somewhat tedious
exercise.
Table 2 shows the growth rate of the number of simple walks as a function of the
crossing number of the knot. Table 3 shows the growth rate of the number of simple walks
as a function of the braid length. Note that Table 3 contains information for knots with up
to 12 crossings but not the 13-crossing knots. The reason is that we do not have definitive
information about the braid representatives of minimal length for the 13-crossing knots.
We end this paper with a few questions and open problems for future investigation. One
is whether braid words that minimize the number of simple walks have a preferred shape
or form. By Proposition 4.4, we can assume the braid word is reduced and irreducible, and
by Lemma 5.4, we can assume it begins with σ1 or σ´1
1 . We conjecture the braid word
can always be chosen to begin with σ1. Further results as to the shape of minimizing braid
words would be helpful for developing efficient search algorithms.
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
0
50
100
Average Number of Simple Walks
Table 3: Average number of simple walks by braid length.
More generally, it would be extremely useful to automate the generation of minimal
width and/or minimal length braid representatives for a given knot. Such tools would allow
fast computation of the colored Jones polynomial and other quantum knot invariants, en-
abling calculations for higher crossing knots, including those in the knot tables of Burton
[8], who has recently extended the classification of knots to 19 crossings.
Auxilliary files
Sagemath programs and datasets are available online [7]. This includes a program that
generates all the simple walks as operators for a given braid and another that selects braid
words that minimize the number of simple walks. It also includes input datasets used to
create Tables 4 and 5, as well as output datasets of braid words that minimize the number
of simple walks for knots up to 13 crossings.
Knot
Minimal width braid
|SW|
Minimal length braid
|SW|
10136
123´121´1223´12´21
21
12´13´12243´1412´1
17
11n8
123´12´112´11´1232221
20
121´1213´12243´141
23
11n121
12322´112´11´1223´121
20
12123´121´1243´141
21
11n131
12322´2122´13´1212´1
17
123´121322´13´143´14
21
12n17
2´112´134´232´23´143´141
63
p12´1q23´1224325´145´1
52
12n20
3´112´1p32´1q21´123´1221
26
p12´1q2p3´12q243´141
32
12n24
12´132´232´13´11´123´121
35
2´112´13´12243´341
32
12n65
2´1123´14243´123´14´123´11
26
121´13´123´14´13254´151
25
12n119
2´1122´1313p12´1q23´11
31
2´113´1243´14122´112
23
12n284
p12´2q23132´112´13´1
36
2´112´13´123´143´123´141
32
12n311
4121´123´142´13´1432´13´11
37
2´11324´13´123´154´1351
30
12n314
2´13´1p12´1q33132´11
34
p12´1q23´12143´12´143
24
12n358
2´13´1121´1212´13132´11
24
3´12´11432´134´13421
20
12n362
123´221´1223´12´132´11
42
3´12´112´243´141221
24
12n403
12´1342´13´11´123´121
37
1213´12´112´143´1241
20
12n482
2´13´113´1221´2232´112
29
2´112´13´1243´123´241
32
Table 4: Simple walks for representatives of minimal braid width and length.
Knot
Braid Word
|SW|
31
13
1
41
p12´1q2
2
51
15
3
52
12312´1
2
61
121´13´123´11
3
62
132´112´1
4
63
122´112´2
5
71
17
8
72
12331´1213´1
3
73
1421´121
6
74
12232´13212´1
5
75
1321´1221
5
76
122´1132´13
8
77
p12´1q232´13
8
81
1234´12´13212´14´1
4
82
152´112´1
9
83
121´13´123´14´134´11
9
84
123´123´312´1
7
85
p132´1q2
8
86
1321´13´123´11
7
87
142´112´2
10
88
1221´13´123´21
10
89
132´112´3
9
810
132´1122´2
9
811
121´1223´123´11
7
812
p12´134´1q2
14
813
1223´123´212´1
8
814
1221´1p23´1q21
8
815
123132´132
9
816
122´112´1122´1
9
817
1p12´1q32´1
9
818
p12´1q4
10
819
p123q2
5
820
12312´3
5
821
1221´2221
6
91
19
21
92
12343´142´132212´1
5
93
1621´121
14
94
1232243´112
9
95
121´12342´13´14321
10
96
1521´1221
12
97
1234223´112´1
9
Knot
Braid Word
|SW|
98
1412´13´1423´112´1
13
99
1231´1214
12
910
1232´13231´121
11
911
12´113312´13
15
912
123´141´123´1414
13
913
1232´1321´1231
10
914
121´13´123´143´141
11
915
1223´141´123´141
16
916
1231´12213
10
917
p12´1q22´1p32´1q2
17
918
122322312´13´1
10
919
12´23´1243´1412´1
14
920
132´13132´13
15
921
121´123´1243´141
12
922
12´1312´332´1
17
923
1221´123´122132
15
924
1312´1312´3
17
925
12334´112´134´1
14
926
12´112312´132´1
13
927
122´112´232´13
15
928
12´11312´232
17
929
p12´132´1q22´1
16
930
122´212´132´13
16
931
12´11312´1322´1
15
932
1p12´1q2312´13
14
933
p12´1q22´1312´13
16
934
12´13p12´1q232´1
13
935
1234´1341´142´132123´1
17
936
132´11312´13
14
937
p12´13q243´123´12´14´1
29
938
123221´123´1221
13
939
123´12143´12´14´1342
18
940
12´1312´1132´13
14
941
13´1423´123´212´134
20
942
123´1212´33´1
7
943
1233´1123´12
8
944
123´12212´13´12´1
7
945
123312´132´1
8
946
123´1212´132´13
8
947
p123´12q23´1
8
948
12322´112´13´11´121
9
949
1221312´13212´1
9
Table 5: Knots up to 9 crossings and braid words minimizing the number of simple walks.
ORCID iDs
Hans U. Boden
https://orcid.org/0000-0001-5516-8327
References
[1] J. W. Alexander, A lemma on systems of knotted curves, Proc. Natl. Acad. Sci. USA 9 (1923),
93–95.
[2] C. W. Armond, Walks along braids and the colored Jones polynomial, J. Knot Theory Ramif. 23
(2014), 1450007, 15, doi:10.1142/s0218216514500072, https://doi.org/10.1142/
s0218216514500072.
[3] Y. Berest, J. Gallagher and P. Samuelson, Cyclotomic expansion of generalized Jones poly-
nomials, Lett. Math. Phys. 111 (2021), Paper No. 37, 32, doi:10.1007/s11005-021-01373-6,
https://doi.org/10.1007/s11005-021-01373-6.
[4] C. Bijaoui, H. U. Boden, B. Myers, R. Osburn, W. Rushworth, A. Tronsgard and S. Zhou,
Generalized Fishburn numbers and torus knots, J. Comb. Theory Ser. A 178 (2021), Pa-
per No. 105355, 15, doi:10.1016/j.jcta.2020.105355, https://doi.org/10.1016/j.
jcta.2020.105355.
[5] J. S. Birman, Braids, Links, and Mapping Class Groups, Princeton University Press, Princeton,
N.J.; University of Tokyo Press, Tokyo, 1974, annals of Mathematics Studies, No. 82, https:
//www.jstor.org/stable/j.ctt1b9rzv3.
[6] J. S. Birman and T. E. Brendle, Braids: a survey, in: Handbook of Knot Theory, Elsevier B. V.,
Amsterdam, pp. 19–103, 2005, doi:10.1016/b978-044451452-3/50003-4, https://doi.
org/10.1016/b978-044451452-3/50003-4.
[7] H. U. Boden and M. Shimoda, Braid representatives minimizing the number of simple walks,
2022, arXiv:2109.11483 [math.CO].
[8] B. A. Burton, The Next 350 Million Knots, in: 36th International Symposium on Computa-
tional Geometry (SoCG 2020), Schloss Dagstuhl–Leibniz-Zentrum für Informatik, Dagstuhl,
Germany, volume 164 of Leibniz International Proceedings in Informatics (LIPIcs), 2020 pp.
25:1–25:17, doi:10.4230/lipics.socg.2020.25, https://doi.org/10.4230/lipics.
socg.2020.25.
[9] D. Cooper, M. Culler, H. Gillet, D. D. Long and P. B. Shalen, Plane curves associated to
character varieties of 3-manifolds, Invent. Math 118 (1994), 47–84, doi:10.1007/bf01231526,
https://doi.org/10.1007/bf01231526.
[10] D. Futer, E. Kalfagianni and J. Purcell, Guts of surfaces and the colored Jones polynomial,
volume 2069 of Lecture Notes in Mathematics, Springer, Heidelberg, 2013, doi:10.1007/
978-3-642-33302-6, https://doi.org/10.1007/978-3-642-33302-6.
[11] S. Garoufalidis, On the characteristic and deformation varieties of a knot, in: Proceedings of the
Casson Fest, Geom. Topol. Publ., Coventry, volume 7 of Geom. Topol. Monogr., 2004 pp. 291–
309, doi:10.2140/gtm.2004.7.291, https://doi.org/10.2140/gtm.2004.7.291.
[12] S. Garoufalidis, The Jones slopes of a knot, Quantum Topol. 2 (2011), 43–69, doi:10.4171/qt/
13, https://doi.org/10.4171/qt/13.
[13] T. A. Gittings,
Minimum braids:
a complete invariant of knots and link,
2004,
arXiv:math/0401051 [math.CO].
[14] M. Hajij and J. Levitt, An efficient algorithm to compute the colored Jones polynomial, 2018,
arXiv:1804.07910 [math.CO].
[15] V. Huynh and T. T. K. Le, The colored Jones polynomial and the Kashaev invariant, Fundam.
Prikl. Mat. 11 (2005), 57–78, doi:10.1007/s10958-007-0361-5, https://doi.org/10.
1007/s10958-007-0361-5.
[16] V. F. R. Jones, Hecke algebra representations of braid groups and link polynomials, Ann.
Math. (2) 126 (1987), 335–388, doi:10.2307/1971403, https://doi.org/10.2307/
1971403.
[17] E. Kalfagianni and A. T. Tran, Knot cabling and the degree of the colored Jones polynomial,
N. Y. J. Math. 21 (2015), 905–941, http://nyjm.albany.edu:8000/j/2015/21_
905.html.
[18] R. M. Kashaev, The hyperbolic volume of knots from the quantum dilogarithm, Lett.
Math. Phys. 39 (1997), 269–275, doi:10.1023/a:1007364912784, https://doi.org/10.
1023/a:1007364912784.
[19] C. Livingston and A. H. Moore, Knotinfo: Table of knot invariants, 2021, https://
knotinfo.math.indiana.edu.
[20] J. Lovejoy and R. Osburn, The colored Jones polynomial and Kontsevich-Zagier series for
double twist knots, II, N. Y. J. Math. 25 (2019), 1312–1349.
[21] J. Lovejoy and R. Osburn, The colored Jones polynomial and Kontsevich-Zagier series for
double twist knots, J. Knot Theory Ramif. 30 (2021), Paper No. 2150031, 28, doi:10.1142/
s0218216521500310, https://doi.org/10.1142/s0218216521500310.
[22] G. Masbaum, Skein-theoretical derivation of some formulas of Habiro, Algebraic Geom.
Topol. 3 (2003), 537–556, doi:10.2140/agt.2003.3.537, https://doi.org/10.2140/
agt.2003.3.537.
[23] H. Murakami and J. Murakami, The colored Jones polynomials and the simplicial volume of
a knot, Acta Math. 186 (2001), 85–104, doi:10.1007/bf02392716, https://doi.org/10.
1007/bf02392716.
[24] H. Murakami and Y. Yokota, Volume Conjecture for Knots, volume 30 of SpringerBriefs in
Mathematical Physics, Springer, Singapore, 2018, doi:10.1007/978-981-13-1150-5, https:
//doi.org/10.1007/978-981-13-1150-5.
[25] T. Ohtsuki, On the asymptotic expansion of the Kashaev invariant of the 52 knot, Quantum
Topol. 7 (2016), 669–735, doi:10.4171/qt/83, https://doi.org/10.4171/qt/83.
[26] T. Ohtsuki, On the asymptotic expansions of the Kashaev invariant of hyperbolic knots with
seven crossings, Int. J. Math. 28 (2017), 1750096, 143, doi:10.1142/s0129167x17500963,
https://doi.org/10.1142/s0129167x17500963.
[27] T. Ohtsuki and Y. Yokota, On the asymptotic expansions of the Kashaev invariant of the
knots with 6 crossings, Math. Proc. Cambridge Philos. Soc. 165 (2018), 287–339, doi:
10.1017/s0305004117000494, https://doi.org/10.1017/s0305004117000494.
[28] A. Stoimenow, On the crossing number of positive knots and braids and braid index
criteria of Jones and Morton-Williams-Franks,
Trans. Am. Math. Soc. 354 (2002),
3927–3954,
doi:10.1090/s0002-9947-02-03022-2,
https://doi.org/10.1090/
s0002-9947-02-03022-2.
[29] A.
Stoimenow,
Knot
data
tables,
2022,
http://stoimenov.net/stoimeno/
homepage/ptab/index.html.
[30] C. A. Van Cott, Relationships between braid length and the number of braid strands, Al-
gebr. Geom. Topol. 7 (2007), 181–196, doi:10.2140/agt.2007.7.181, https://doi.org/
10.2140/agt.2007.7.181.
