---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-042-51-classi
section_title: "Classi"
section_number: 5.1
pages: 83-86
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
cation of quandles
It was a classical problem in group theory to classify the isomorphism classes
of groups of order n for each n. The following problem is a corresponding
problem for connected quandles.
Chapter 5 was written by T. Ohtsuki, following suggestions and comments given by S.
Kamada and M. Saito. Section 5.6 was added by C. Rourke and B.Sanderson.
19We call this propertyconnectedhere following [190]. This is also calledweakly homogeneous
in some of the literature.
Geometry &TopologyMonographs, Volume 4 (2002)
456 T. Ohtsuki (Editor)
Problem 5.1 Classify the isomorphism classes of connected quandles of order
n for each positive integer n.
See Table 4 for a list of connected quandles of order n for some n.
n # Connected quandles of order n
Self-dual Not self-dual
1 1 A trivial quandle
2 0
3 1 R3
4 1 2=(t2 +t +1 )
5 3 R5 5=(t−2), its dual
6 2 2 subquandles of Conj( S4)
7 5 R7 7=(t−2), 7=(t−3), their duals
8  3 An abelian extension 2=(t3 +t + 1), its dualof 2=(t2 +t +1 )
9 8 R9, 3=(t2−t +1 ) , 9=(t−2), 3=(t2 +t−1),
R3R3, 3=(t2 +1 ) their duals
10  1 A subquandle of Conj( S5)
11 9 R11 11=(t−a)( a =2; 3; ; 9)
12  2 R3
(
2=(t2 +t +1 )

,
An icosahedral quandle
13 11 R13 13=(t−a)( a =2; 3; ; 11)
14  0
15  4 R3R5, R3
(
5=(t−2)

, its dualA subquandle of Conj( S5)
...
Prime p p−2 Rp p=(t−a)( a =2; 3; ;p−2)
Table 4: A table of some connected quandles. The second column shows the numbers
of isomorphism classes of connected quandles of order n.W e d e n o t eZ[t1]=(n)b y
n . Conj(Sm) denotes the conjugation quandle of the mth symmetric group Sm .A n
icosahedral quandle is a quandle whose elements are the vertices of an icosahedron such
that Sx of each element x is given by a rotation of the icosahedron centered at x.
Remark (M. Gra~na) It is shown, in [116] in terms of set theoretical solutions
of the quantum Yang-Baxter equation, that a connected quandle of prime order
p is isomorphic to the Alexander quandle Z[t]=(p;t−a)f o rs o m ea.I t i s
shown in [11, 308] that two connected Alexander quandles are isomorphic if
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 457
and only if they are isomorphic asZ[t1]-modules. These give the classi
cation
of connected quandles of prime order shown in Table 4.
Remark (M. Gra~na) It is shown in [11] that a simple quandle of prime power
order is an Alexander quandle; it is a 
nite 
eld F such that t acts by mul-
tiplication by some primitive element w (i.e. w generates F as an algebra).
Further, it is shown in [156] that a connected quandle of prime square order
is an Alexander quandle. This gives the classi
cation of connected quandles of
order 9 shown in Table 4.
Remark S. Yamada made the list of isomorphism classes of quandles (and
racks) of order  7 by computer search. The list of connected quandles of
order 7 in Table 4 follows from it. S. Nelson [308] classi
es the Alexander
quandles of order  15; connected ones among them are listed in Table 4.
Remark The following modi
cation of Problem 5.1 gives an algorithm to list
connected quandles: classify the isomorphism classes of connected quandles

xing the conjugacy class of the union of Sx and an identity map. For a
quandle X we denote by SX the set of Sx (x2 X ) ,w h i c hi sr e g a r d e da sa
subset of Sn when X is of order n.T h e m a pX! Sn ,t a k i n gx7! Sx ,i s
often injective, though in general the map X!SX is a quotient map, and the
order of SX divides n when X is connected. Let us investigate this problem
in some simple cases.
Let X be a connected quandle of order n whose SX includes (12)2 Sn . Then,
for anyi there is a sequence 1 =a0;a 1; ;ak =i such that (a0a1); (a1a2);2
SX since X is connected. Further, since SX is closed with respect to conjuga-
tion, SX includes (1i)2 Sn , and hence any (ij)2 Sn . Therefore, n =3 ,a n d
X is isomorphic to the dihedral quandle R3 .
Let X be a connected quandle of order n whose SX includes (123) 2 Sn .
Suppose that SX further included (145) 2 Sn . Then, since SX is closed
with respect to conjugation, SX would include (ijk)2 Sn for any fi;j;kg
f1; 2; 3; 4; 5g. This would contradict, since the order of SX is at mostn. Hence,
n =4 ,a n dX is isomorphic to the conjugation subquandle of A4 consisting of
(123), (134), (142), and (243), which is isomorphic to Z[t1]=(2;t 2 +t +1 ) .
Let X be a connected quandle of order n whose SX includes (1234) 2 Sn .
If SX further included (1567) 2 Sn , a contradiction would follow from a sim-
ilar argument as above. Hence, it is sucient to consider the cases that SX
include (1234) and either of (1256), (2156), (1526), (1536), or ( ijk5) for any
fi;j;kg =f1; 2; 3g. It follows from some concrete computations that such a
Geometry &TopologyMonographs, Volume 4 (2002)
458 T. Ohtsuki (Editor)
X is isomorphic to either of the Alexander quandle Z[t1]=(5;t−2), its dual
quandle, or the conjugation subquandle of S4 including (1234).
