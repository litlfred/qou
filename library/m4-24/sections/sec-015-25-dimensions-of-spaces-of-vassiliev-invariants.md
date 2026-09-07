---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-015-25-dimensions-of-spaces-of-vassiliev-invariants
section_title: "Dimensions of spaces of Vassiliev invariants"
section_number: 2.5
pages: 33-36
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
We denote byA(S1;R)conn the submodule of A(S1;R) spanned by Jacobi dia-
grams with connected uni-trivalent graphs. As a graded vector space A(S1;Q)
is isomorphic to the symmetric tensor algebra of A(S1;Q)conn . A Vassiliev in-
variant v is called primitive if v(K1#K2)= v(K1)+ v(K2) for any oriented
knots K1 and K2 . The degree d subspace of A(S1;Q)conn is dual to the dth
graded vector space for Q-valued primitive Vassiliev invariants.
Problem 2.12 Determine the dimension of the space of primitive Vassiliev
invariants of each degreed. Equivalently, determine the dimension of the space
A(S1;Q)(d)
conn for each d.
d 0 1 2 3 4 5 6 7 8 9 10
dimA(S1)(d)
conn 0 1 1 1 2 3 5 8 12 18 27
dimA(S1)(d) 1 1 2 3 6 10 19 33 60 104 184
dimA(S1)(d)=FI 1 0 1 1 3 4 9 14 27 44 80
d 11 12 13 14
dimA(S1)(d)
conn 39 55  78  108
dimA(S1)(d) 316 548  932  1591
dimA(S1)(d)=FI 132 232  384  659
Table 1: Some dimensions given in [67, 224]
Remark The dimension ofA(S1;Q)(d)
conn can partially be computed as follows.
LetB denote the vector space over Q spanned by vertex-oriented uni-trivalent
graphs subject to the AS and IHX relations, and let B(d)
conn denote the subspace
ofB spanned by connected uni-trivalent graphs with 2d vertices.
Geometry &TopologyMonographs, Volume 4 (2002)
406 T. Ohtsuki (Editor)
It is known that A(S1;Q)(d)
conn is isomorphic to B(d)
conn by (21). Let B(d;u)
conn be
the subspace ofB(d)
conn spanned by uni-trivalent graphs withu univalent vertices
(hence, with 2 d−u trivalent vertices), and 
d;u its dimension. Then, the
dimension ofA(S1;Q)(d)
conn is presented by P
u2
d;u .
Bar-Natan [28] gave a table of 
d;u for d 9 and for some other ( d;u )b y
computer.
The series of 
k;k is given as follows. The direct sum kB(k;k)
conn is isomorphic to
the polynomial ring Q[x2] as a graded vector space by (23); in other words, it
is spanned by \wheels". Hence, the series of 
k;k is presented by the following
generating function, X
k0

k;ktk = 1
1−t2:
That is, 
k;k =1i f k is even, and 0 otherwise.
The series of 
k+1;k is given as follows. The direct sum kB(k+1;k)
conn is isomor-
phic to Q[2; 2
3] as a graded vector space by (25), where i denotes the i-th
elementary symmetric polynomial in some variables. Hence, the series of 
k+1;k
is presented by the following generating function,
X
k0

k+1;ktk = 1
(1−t2)(1−t6):
The series of 
k+2;k is presented by
X
k0

k+2;ktk = 1
(1−t2)(1−t4)(1−t6);
sincekB(k+2;k)
conn is isomorphic, as a graded vector space, to Q[2; 2
3; 4]w i t h
elementary symmetric polynomials in some variables by (27).
It is conjectured [101] that the series of 
k+3;k would be presented by
X
k0

k+3;ktk ?= 1+ t2 +t8−t10
(1−t2)(1−t4)(1−t6)(1−t10):
It has been shown that 
d;u =0f o r d 9a n df o rd u + 2. However, it is
conjectured yet for other (d;u ).
A conjecture of a two-variable generating function for the series of 
d;u with
two parameters d and u is given in [67].
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 407

d;u u =2 u =4 u =6 u =8 u =1 0 u =1 2 u =1 4 total
d =1 1 1
d =2 1 1
d =3 1 1
d =4 1 1 2
d =5 2 1 3
d =6 2 2 1 5
d =7 3 3 2 8
d =8 4 4 3 1 12
d =9 5 6 5 2 18
d =1 0 6 8 8 4 1 27
d =1 1 8 10 11 8 2 39
d =1 2 9 13 15 12 5 1 55
d =1 3  11  16  20  18  10 3  78
d =1 4  13  19  25  26  17 7 1  108
Table 2: A table of 
d;u [67, 224]
Remark An asymptotic evaluation of a lower bound of dim A(S1)(d)
conn was
given in [87]; dimA(S1)(d)
conn grows at least as dlogd when d!1 . Further, it
w a si m p r o v e di n[ 1 0 1 ] ;d i mA(S1)(d)
conn grows at least as ec
p
d for any c<
p
2=3
when d!1 .
Remark Upper bounds of dimA(S1)(d)
conn were given dimA(S1)(d)
conn  (d−1)!
in [86] and dimA(S1)(d)
conn  (d−2)!=2( f o rd> 5) in [313]. Stoimenow [373]
introduced the number d of \regular linearized chord diagrams", and showed
that dimA(S1)(d)=FI d . Further, he showed that d is asymptotically at
most d!=1:1d ,w h i c hw a si m p r o v e db yd!=(2 ln 2 +o(1)) in [63]. Furthermore,
Zagier [410] showed that
1X
n=0
(1−q)(1−q2) (1−qn)=
1X
d=0
d(1−q)d2Z[[1−q]]; (12)
and that
d d!
p
d
(2=6)d
(
C0 +C1
d + C2
d2 +

with C0 =1 2
p
3−5=2e2=12  2:704, C1 −1:527, C2 −0:269. It follows
that the asymptotic growth of dimA(S1)(d)=FI is at most O(d!
p
d(2=6)−d).
Geometry &TopologyMonographs, Volume 4 (2002)
408 T. Ohtsuki (Editor)
d 0 1 2 3 4 5 6 7 8 9 10
dimA(S1)(d)=FI 1 0 1 1 3 4 9 14 27 44 80
d 1 1 2 5 15 53 217 1014 5335 31240 201608
Table 3: Upper bounds d of dimA(S1)(d)=FI (see [373])
