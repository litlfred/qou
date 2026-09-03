---
doc_id: arxiv-2303.08330v2
doc_title: "A Cable Knot and BPS-Series II John Chae"
section_id: sec-010-the-colored-jones-polynomial-of-a-cable-knot
section_title: "The colored Jones polynomial of a cable knot"
section_number: null
pages: 14-17
source_pdf: 2303.08330v2.pdf
source_sha256: 94981fa0a792b3fa
doc_brief: "A Cable Knot and BPS-Series II John Chae — This is a companion paper to earlier work of the author, which genera lizes to an inﬁnite family of (2 , 2w + 1)-cabling of the ﬁgure eight knot ( |w| > 3)"
---
For (r,2)-cabling of a knot K in S3, its unnormalized sl2(C) colored Jones polynomial of is [22]
˜JC(r, 2)(K),n(t) = t− rs(n2− 1)
n− 1
2∑
w=− n− 1
2
t4rw(sw+1) ˜JK,(2sw+1)(t), t 4 = q
The 0-framed unknot U normalization is
˜JU,n(t) = t2n− t− 2n
t2− t− 2 .
14
B The recursion relation for the ﬁgure eight knot
We record the recursion relation and its initial data for the ﬁgure eight knot found in [6]. We
note that a closed form formula was found in [16].
h1(q) = 1
h3(q) = 2
h5(q) = 1
q + 3 + q
h7(q) = 2
q2 + 2
q + 5 + 2q + 2q2
h9(q) = 1
q4 + 3
q3 + 4
q2 + 5
q + 8 + 5q + 4q2 + 3q3 + q4
h11(q) = 2
q6 + 2
q5 + 6
q4 + 7
q3 + 10
q2 + 10
q + 15 + 10q + 10q2 + 7q3 + 6q4 + 2q5 + 2q6
h13(q) = 1
q9 + 3
q8 + 4
q7 + 7
q6 + 11
q5 + 15
q4 + 18
q3 + 21
q2 + 23
q + 27 + 23q + 21q2 + 18q3 + 15q4
+ 11q5 + 7q6 + 4q7 + 3q8 + q9
hm+14(q) =− q− m
2 − 11
2
q
m
2 + 13
2 − 1
[
hm
(
q
m
2 + 17
2 − qm+9
)
+ hm+2
(
q
m
2 + 15
2 − q
m
2 + 17
2 + qm+9− qm+10
)
+ hm+4
(
−q
m
2 + 11
2 − q
m
2 + 17
2 − q
m
2 + 19
2 + q
3m
2 + 21
2 + qm+8 + qm+9 + qm+12− q7
)
+ hm+6
(
−q
m
2 + 9
2 + q
m
2 + 11
2 − q
m
2 + 15
2 − q
m
2 + 17
2 + q
3m
2 + 25
2 + qm+9 + qm+10− qm+12 + qm+13− q5
)
+ hm+8
(
q
m
2 + 11
2 + q
m
2 + 13
2 − q
m
2 + 17
2 + q
m
2 + 19
2 − q
3m
2 + 31
2 − qm+8 + qm+9− qm+11− qm+12 + q2
)
+ hm+10
(
q
m
2 + 9
2 + q
m
2 + 11
2 + q
m
2 + 17
2 − q
3m
2 + 35
2 − qm+9− qm+12− qm+13 + 1
)
+ hm+12
(
q
m
2 + 11
2 − q
m
2 + 13
2 + qm+11− qm+12
)
]
C The deﬁnitions of the operators
We list the deﬁnitions of the operators in the ˆA-polynomial (4) in Section 2.
Q(t, M, L ) = Q2(t, M )L2 + Q1(t, M )L + Q0(t, M ), B (t, M ) :=
2∑
j=0
cjb(t, t 2j+2M 2)
b(t, M ) = M (1 + t4M 2)(−1 + t4M 4)(−t2 + t14M 4)
t2− t− 2
c0 = ˆP0(t, t 4M 2) ˆP1(t, t 6M 2), c 1 =− ˆP1(t, t 2M 2) ˆP1(t, t 6M 2), c 2 = ˆP1(t, t 2M 2) ˆP2(t, t 4M 2).
15
Q2(t, M ) = ˆP2(t, t 4M 2) ˆP1(t, t 2M 2) ˆP0(t, t 6M 2)
Q1(t, M ) = ˆP0(t, t 4M 2) ˆP1(t, t 6M 2) ˆP2(t, t 2M 2)− ˆP1(t, t 6M 2) ˆP1(t, t 2M 2) ˆP1(t, t 4M 2)
+ ˆP2(t, t 4M 2) ˆP1(t, t 2M 2) ˆP0(t, t 6M 2)
Q0(t, M ) = ˆP0(t, t 4M 2) ˆP1(t, t 6M 2) ˆP0(t, t 2M 2),
ˆP0(t, M ) : = t6M 4(−1 + t12M 4)
ˆP1(t, M ) : = −(−1 + t4M 2)(1 + t4M 2)
(
1− t4M 2− t4M 4− t12M 4− t12M 4− t12M 6 + t16M 8)
ˆP2(t, M ) : = t10M 4(−1 + t4M 4).
The deﬁnitions of the operators in the ˆA-polynomial (12) in Section 4 are
Q(t, M, L ) := 1 + DetA9
DetA L + DetA8
DetA L2, B (t, M ) :=
6∑
j=0
cjb(t, t 2(2+j)M 3)
where A is a matrix and A9 and A8 are obtained from A (see Section 4 in [22]).
References
[1] Bar-Natan D., Garoufalidis S., On the Melvin–Morton–Ro zansky conjecture, Invent. Math.
125 (1996), 103–133.
[2] A. Beliakova, S. Wehrli, Categoriﬁcation of the colored Jones polynomial and Rasmussen
invariant of links, Canad. J. Math. 60 (2008), 1240–1266.
[3] J. Chae, A Cable Knot and BPS Series, SIGMA arXiv:2204.02794.
[4] B. Cooper, V. Krushkal, Categoriﬁcation of the Jones-We nzl Projectors Quantum Topol. 3
(2012), no. 2, 139–180. arXiv:1005.5117.
[5] Garoufalidis S., Le T Q T., The colored Jones function is q –holonomic,
Geometry and Topology 9 (2005), 1253–1293, arXiv:math/0309214.
[6] Gukov S., Manolescu C., A two-variable series for knot co mplements, Quantum Topol. 12,
2021, 1–109. arXiv:1904.06057.
[7] Gukov S., Pei D., Putrov P., Vafa C., BPS spectra and 3-man ifold invariants,
J. Knot Theory Ramiﬁcations 29 (2020), 2040003, 85 pages, arXiv:1701.06567.
[8] Hedden M., On knot Floer homology and cabling, Algebraic and Geometric Topology 5 (2005),
1197–1222, arXiv:math/0406402.
[9] Khovanov M., A categoriﬁcation of the Jones polynomial, Duke Math. J. 101 (2000), 359–
426, arXiv:math.QA/9908171.
[10] Khovanov M., A categoriﬁcation of the colored Jones pol ynomial,
J. Knot Theory Ramiﬁcations 14 (2005), 111–130, arXiv:math/0302060.
16
[11] Khovanov M., Hopfological algebra and categoriﬁcatio n at a root of unity: the ﬁrst steps,
arXiv:math/0509083.
[12] M. Khovanov and L. Rozansky, Matrix factorizations and link homology 1,
arXiv:math/0401268.
[13] M. Khovanov and L. Rozansky, Matrix factorizations and link homology 2, Geom. Topol. 12
(2008), 1387–1425, arXiv:math/0505056.
[14] Melvin P.M., Morton H.R., The coloured Jones function, Comm. Math. Phys. 169 (1995),
501–520.
[15] A. Oblomkov, J. Rasmussen, V. Shende. The Hilbert schem e of a plane curve singularity
and the HOMFLY homology of its link. With an appendix by Eugen e Gorsky. Geom. Topol.
2018, 22. arXiv:1201.2115.
[16] Park S., Inverted state sums, inverted Habiro series, a nd indeﬁnite theta functions,
arXiv:2106.03942.
[17] Park S., Large color R-matrix for knot complements and strange identities,
Journal of Knot Theory and Its Ramiﬁcations 29, No. 14, 2050097 (2020). arXiv:2004.02087.
[18] Y. Qi, Hopfological Algebra, Compositio Mathematica 150, 1 (2014). arXiv:1205.1814.
[19] Reshetikhin N., Turaev V., Invariants of 3-manifolds v ia link polynomials and quantum
groups, Invent. Math. 103 (1991), 547–597.
[20] Rozansky L., Higher order terms in the Melvin–Morton ex pansion of the colored Jones poly-
nomial, Comm. Math. Phys. 183 (1997), 291–306, arXiv:q-alg/9601009.
[21] Rozansky L., The Universal R-Matrix, Burau Representa ion and the Melvin-Morton Expan-
sion of the Colored Jones Polynomial, Adv. Math 134 (1998), 1–31, arXiv:q-alg/9604005.
[22] Ruppe D., The AJ-conjecture and cabled knots over the ﬁg ure eight knot,
Topology and its Applications 188 (2015), 27–50, arXiv:1405.3887.
[23] Tran A., On the AJ conjecture for cables of the ﬁgure eigh t knot,
New York Journal of Mathematics 20 (2014), 727–741, arXiv:1405.4055.
[24] Trinh M., From the Hecke Category to the Unipotent Locus , arXiv:2106.07444.
[25] Witten E., Quantum ﬁeld theory and the Jones polynomial , Comm. Math. Phys. 121 (1989),
351–399.
17
