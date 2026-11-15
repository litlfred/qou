---
doc_id: zhao-standard-2010
doc_title: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity"
section_id: sec-016-9-computational-results-in-weight-three-four-and
section_title: "Computational results in weight three, four and five"
section_number: 9
pages: 29-34
source_pdf: Zhao_standard_2010.pdf
source_sha256: 94a70847c2937ba7
toc_source: inferred
doc_brief: "Standard Relations of Multiple Polylogarithm Values at Roots of Unity — Let N be a positive integer."
---
Computational results in weight three, four and five
In this last section we brieﬂy discuss our results in weight three, four and ﬁve.
Since the computational complexity increases exponentially with the weight we
cannot do as many cases as we have done in weight two.
Combining the FDS (28), (29), RDS (30)-(35), and the weight one relations (13)
and using MAPLE we have veriﬁed that d(3, 1) = 1, d(3, 2) ≤3, d(3, 3) ≤8....
N
1
2
3
4
5
6
7
SR(3)
1
3
8
9
22
23
50
D(3)
1
3
8
8
27
21
64
SR(4)
1
5
16
21
61
69
D(4)
1
5
16
16
81
55
256
SR(5)
2
8
32
D(5)
2
8
32
32
243
144
1024
N
8
9
10
11
12
13
SR(3)
38
67
70
157
94
246
D(3)
27
64
56
216
56
343
Table 2: Upper bounds of d(w, N) by the standard relations and [17, 5.25].
Documenta Mathematica 15 (2010) 1–34
30
Jianqiang Zhao
We have done similar computation in other small weight and low level cases
and listed the results in Table 2. The values of Deligne and Goncharov’s bound
D(w) = D(w, N) in Table 2 should be compared with the bound SR(w) =
SR(w, N) obtained by the standard relations.
Note that SR(3, 4) = D(3, 4) + 1. By numerical computation using EZface [9]
and GiNac [27] we ﬁnd the following non-standard relation in weight 3:
5L4(1, 2|2, 3) =46L4(1, 1, 1|1, 0, 0) −7L4(1, 1, 1|2, 2, 1) −13L4(1, 1, 1|1, 1, 1)
+ 13L4(1, 2|3, 1) −L4(1, 1, 1|3, 2, 0) + 25L4(1, 1, 1|3, 0, 0)
−8L4(1, 1, 1|1, 1, 2) + 18L4(2, 1|3, 0),
(53)
and ﬁve non-standard relations in weight 4:
0 = −255608l1 −265360l2 −219216l3 −19306179l4 −214008l5 + 45560l6
−148296l7 −1117280l8 −677152l9 + 86512l10 −239320l11 −50032l12
−121008l13 −96944l14 + 202328l15 −1178499l16 + 98944l17
+ 1565754l18 + 23071580l19 + 363568l20 −3310177l21,
(54)
0 =29752l1 + 23312l2 + 10960l3 + 6123413l4 + 16440l5 −12408l6
+ 7144l7 + 58272l8 + 86976l9 −15952l10 + 41144l11 + 13552l12
+ 29552l13 + 9840l14 −36696l15 + 375805l16 −41760l17
−477366l18 −7196900l19 −62128l20 + 1048983l21,
(55)
0 =477444l1 + 431352l2 + 268168l3 + 98404710l4 + 308964l5 −233140l6
+ 130028l7 + 1563872l8 + 1516032l9 −296664l10 + 702308l11 + 190136l12
+ 506440l13 + 141592l14 −636468l15 + 6027441l16 −701600l17
−7683609l18 −115803282l19 −1063768l20 + 16877562l21,
(56)
0 = −5976l1 + 1776l2 + 8496l3 −2132671l4 + 3176l5 + 1752l6
+ 3832l7 + 50976l8 −2688l9 + 2320l10 −10264l11 −5808l12
−6128l13 + 2320l14 + 8120l15 −132307l16 + 13856l17
+ 162614l18 + 2487604l19 + 12720l20 −368485l21,
(57)
0 = −474064l1 −405248l2 −243520l3 −54556373l4 −283952l5 + 84368l6
−170640l7 −1033056l8 −994784l9 + 174880l10 −540432l11 −156544l12
−240512l13 −49344l14 + 411152l15 −3357683l16 + 292256l17
+ 4291792l18 + 64572648l19 + 743136l20 −9470695l21.
(58)
where by setting L = L4, 14 = {1}4, ...
l1 = L(14|2, 1, 0, 1),
l2 = L(14|2, 12, 0),
l3 = L(14|2, 0, 3, 1),
l4 = L(14|2, 03),
l5 = L(14|1, 2, 0, 3),
l6 = L(14|32, 0, 3),
l7 = L(14|3, 1, 3, 2),
l8 = L(14|3, 03),
l9 = L(14|3, 0, 1, 0),
l10 = L(14|3, 0, 12),
l11 = L(2, 12|0, 3, 0), l12 = L(3, 1|0, 3),
l13 = L(14|2, 2, 3, 0), l14 = L(2, 12|3, 12),
l15 = L(2, 12|3, 0, 3),
l16 = L(12, 2|23),
l17 = L(14|2, 0, 1, 0), l18 = L(2, 12|22, 0),
l19 = L(14|{2, 0}2),
l20 = L(22|3, 0),
l21 = L(14|24).
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
31
We now can prove this by using the octahedral symmetry of P1 −({0, ∞}∪µ4)
(see Remark 5.3). This idea was suggested to the author by Deligne in a letter
dated Feb. 14, 2008.
Theorem 9.1. ([30]) If the conjecture in [17, 5.27(c)] is true then all the linear
relations among MPVs of level four and weight three (resp. weight four) are the
consequences of the standard relations and the octahedral relation (53) (resp.
the ﬁve octahedral relations (54)-(58)).
Proof. For the proof please see[30, §3].
From the available data in Table 2 we can formulate the following conjecture.
Conjecture 9.2. Suppose the level N = p is a prime ≥5. Then
d(3, p) ≤p3 + 4p2 + 5p + 14
12
.
Moreover, equality holds if standard relations produce all the linear relations.
We formulated this conjecture under the belief that the upper bound of d(3, p)
produced by the standard relations should be a polynomial of p of degree 3.
Then we ﬁnd the coeﬃcients by the bounds of d(3, p) for p = 5, 7, 11, 13 in
Table 2.
When w > 2 it’s not too hard to improve the bound of d(w, p) given in [17,
5.25] by the same idea as used in the proof of [17, 5.24] (for example, decrease
the bound by (p2 −1)/24). But they are often not the best. We conclude our
paper with the following conjecture.
Conjecture 9.3. If N is a standard level then the standard relations always
provide the sharp bounds of d(w, N), namely, all linear relations can be derived
from the standard ones, if further N > 3 then the bound D(w, N) in (36) by
Deligne and Goncharov can be lowered. If N is a non-standard level then the
bound D(w, N) is sharp and there exists a positive integer w0(N) so that at
least one non-standard relation exists in MPV(w, N) for each w ≥w0(N).
It is likely that one can take w0(4) = w0(6) = w0(9) = 3 and w0(N) = 2 for all
the other non-standard levels N.
References
[1] H. Bass, Generators and relations for cyclotomic units, Nagoya Math. J.
27 (2)(1966), 401–407.
[2] A.A. Beilinson and P. Deligne, Interpr´etation motivique de la conjecture
de Zagier reliant polylogarithmes et r´egulateurs, in: Motives, Proceedings
of the Research Conference on Motives held July 20–August 2, 1991, in
Seattle, Washington, U. Jannsen, S.L. Kleiman and J.P. Serre eds., Proc.
of Symp. in Pure Math. 55, Part II, pp. 97–121, AMS 1994.
Documenta Mathematica 15 (2010) 1–34
32
Jianqiang Zhao
[3] M. Bigotte, , G. Jacob, N.E. Oussous and M. Petitot, Lyndon words and
shuﬄe algebras for generating the coloured multiple zeta values relations
tables, Theoretical Computer Sci. 273 (1-2)(2002), 271–282.
[4] M. Bigotte, , G. Jacob, N.E. Oussous and M. Petitot, Generating power
series of coloured polylogarithm functions and Drifel’d associator, Computer
Math (Chiang Mai, 2000), 39–48, Lecture Notes Ser. Comput., 8, World
Sci. Publ., River Edge, NJ, 2000.
[5] J. Bl¨umlein, D.J. Broadhurst, and J.A.M. Vermaseren, The multiple zeta
value data mine, arXiv: 0907.2557.
[6] J.M. Borwein, D.M. Bradley, D.J. Broadhurst, and P. Lisonˇek, Special val-
ues of multiple polylogarithms, Trans. AMS 353 (2001), 907–941.
[7] J.M. Borwein, D.M. Bradley, D.J. Broadhurst, and P. Lisonˇek, Combina-
torial aspects of multiple zeta values, Electron. J. Combin. 5 (1), (1998),
Research Paper 38.
[8] J. M. Borwein, D. J. Broadhurst, and D. M. Bradley, Evaluations of k-
fold Euler/Zagier sums: a compendium of results for arbitrary k, Elec. J.
Combin. 4 (2)(1997), #R5. Wilf Festschrift.
[9] J.
Borwein,
P.
Lisonek,
and
P.
Irvine,
An
interface
for
evalua-
tion of Euler sums, available online at http://oldweb.cecm.sfu.ca/cgi-
bin/EZFace/zetaform.cgi
[10] D. J. Broadhurst, Massive 3-loop Feynman diagrams reducible to SC*
primitives of algebras of the sixth root of unity, European Phys. J. C 8
(1999), 311–333
[11] D. J. Broadhurst, Conjectured enumeration of irreducible multiple zeta
values, from knots and Feynman diagrams, preprint: hep-th9612012.
[12] K.-T.-Chen, Algebras of iterated path integrals and fundamental groups,
Trans. Amer. Math. Soc. 156 (1971), 359–379.
[13] M. Conrad, Construction of Bases for the Group of Cyclotomic Units, J.
Number Theory 81(2000), 1–15.
[14] M. Conrad and J. Zhao, An integral structure of multi-polylog values at
roots of unity, in preparation.
[15] P. Deligne, Le groupe fondamental de la droite projective moins trois
points, Galois groups over Q, (Berkeley, CA, 1987), pp. 79–297, Springer,
New York, 1989.
[16] P. Deligne, Le groupe fondamental de la Gm−µN, unpublished manuscript.
Documenta Mathematica 15 (2010) 1–34
Relations of Multiple Polylogarithm Values
33
[17] P. Deligne and A. Goncharov, Groupes fondamentaux motiviques de Tate
mixte, Annales Scientiﬁques de l´Ecole Normale Sup´erieure, 38 (1)(2005),
1–56. Also available math.NT/0302267.
[18] V. Ennola, On relations between cyclotomic units, J. Number Theory 4
(1972), 236–247.
[19] A. B. Goncharov, Polylogarithms in arithmetic and geometry, in: Proc.
ICM, Z¨urich, 374–387, Vol. I, Birkh¨auser, 1994.
[20] A. Goncharov, The dihedral Lie algebras and Galois symmetries of
π(l)
1 (P1 −({0, ∞} ∪µN)), Duke Math. J. 110 (3)(2001), 397–487.
[21] M. E. Hoﬀman, Multiple harmonic series, Paciﬁc J. Math., 152 (2)(1992),
275–290.
[22] M. E. Hoﬀman, Quasi-shuﬄe products, J. Alg. Combin. 11 (2000), 49–68.
[23] M. E. Hoﬀman, Algebra of Multiple Zeta Values and Euler Sums, Mini-
Conference on Zeta Functions, Index, and Twisted K-Theory: Interac-
tions with Physics, Oberwolfach, Germany, May 2, 2006. Available online
www.usna.edu/Users/math/meh.
[24] K. Ihara, M. Kaneko, and D. Zagier, Derivation and double shuﬄe rela-
tions for multiple zeta values, Comp. Math. 142 (2006), 307–338.
[25] M. Kontsevich, Vassiliev’s knot invariants, I. M. Gel’fand Seminar, Adv.
Soviet Math., 16 (2)(1993), 137–150.
[26] G. Racinet, Doubles m´elanges des polylogarithmes multiples aux racines
de l’unit´e, Publ. Math. IHES 95 (2002), 185–231.
[27] J. Vollinga, S. Weinzierl, Numerical evaluation of multiple polylogarithms,
arXiv:hep-ph/0410259
[28] D. Zagier, Values of Zeta Function and Their Applications, Proceedings
of the First European Congress of Mathematics, 2, (1994), 497–512.
[29] J. Zhao, Analytic continuation of multiple polylogarithms, Analysis Math-
ematica, 33 (2007). arXiv: math.AG/0302054
[30] J. Zhao, Multiple polylogarithm values at roots of unity, C. R. Acad. Sci.
Paris, Ser. I. 346 (2008), 1029–1032. DOI: 10.1016/j.crma.2008.09.011
[31] J. Zhao, On a conjecture of Borwein, Bradley and Broadhurst, in press: J.
reine angew. Math., published online on Jan. 20, 2010. arXiv: 0705.2267.
Documenta Mathematica 15 (2010) 1–34
34
Jianqiang Zhao
Jianqiang Zhao
Department of Math.
Eckerd College
St. Petersburg, FL 33711
USA
zhaoj@eckerd.edu
Max-Planck Inst. f¨ur Math.
Vivatsgasse 7
53111 Bonn,
Germany
Documenta Mathematica 15 (2010) 1–34
