---
doc_id: s40687-023-00400-3
doc_title: "bonn.mpg.de/stavros 2MaxPlanckInstitutefor Mathematics,Bonn,Germany Fulllistofauthorinformationis availableattheendofthearticle DedicatedtoWalterNeumann andDonZagier,withadmiration"
section_id: sec-009-31-the-knot-41
section_title: "The knot 41"
section_number: 3.1
pages: 12-16
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
and /Delta12. Using the default triangulation of SnapPy for 41 with isometry signature
cPcbbbiht_BaCB, thegluingequationsare
e1 : z2
1 z′
1z2
2 z′
2 = 1,
e2 : z′
1(z′′
1)2z′
2(z′′
2)2 = 1 ,
thecorrespondinggluingequationmatricesare
G =
(
22
00
)
, G′=
(
11
11
)
, G′′=
(
00
22
)
,
andtheNZmatricesare
A =
(
11
−1 −1
)
, B =
(
−1 −1
11
)
with
ABT =
(
−22
2 −2
)
symmetric.Wecanreadtheaboveinformationbylookingatthetriangulatedcuspshown
inFig. 3.
To describe the ideal triangulation~T of the inﬁnite cyclic cover~M of M,w ec o n s i d e r
thetriangulationoftheperipheraltorusinducedfrom T ={ /Delta11,/Delta12}(seeFig. 3)together
with its lift to the universal cover, the Euclidean planeE2. Note that each triangle ofE2
withcorner zj hasalabel j ∈{ 1,2}ofthecorrespondingtetrahedron.
We now describe a second labeling of each triangle ofE2 by an integer, obtained by
choosing a cocycle representative of the abelianization mapα : π1(M) ↠ Z. This con-
struction is standard and is appears in unpublished work of Goerner and also in Zickert
[29,Sec.3.5].Let G denotethedualdual1-skeletonofthetriangulationof
E2 (seeFig. 4).
Eachvertexandedgeof Gcorrespondtoatetrahedronandface-pairingof T ,respectively,
and that the edges ofG are oriented from/Delta10 to /Delta11. Since the face-pairings generate the
fundamental groupπ1(M), one can assign an integerα(pi) to each face-pairingpi cor-
responding to the abelianization mapα : π1(M) ↠ Z. Since in our case there are two
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 13 of 23 37
Fig. 4 Face-pairings
Fig. 5 Thedual1-complexof E2,wherethelabeling α(v)j ofavertex v indicatesthat v islabeledbythe j-th
tetrahedron
tetrahedra,wehavefourface-pairings,thusfourintegers α(p1),... ,α(p4)thatarerequired
tosatisfy
α(p2) − α(p4) = 1 α(p1) − α(p4) = 1,
α(p1) − α(p3) = 1 α(p2) − α(p3) = 1.
(39)
NotethattheseequationsaredirectlyobtainedfromFig. 4withthe μ-actiondescribedin
Fig.3.
Since E2 is a contractible space, we can assign an integerα(v) to each vertexv of G
suchthat α(v2) − α(v1) = α([v1,v2]),where[ v1,v2]isanorientededgeof G from v1 to v2.
Explicitly,thegeneralsolutionofthelinearequations( 39)isgivenby
(α(p1),α(p2),α(p3),α(p4)) = (a, a, a−1,a −1) ( a ∈ Z). (40)
It follows from the construction that if a vertexv corresponds to/Delta1j in T , then it corre-
sponds toμα(v) · ~/Delta1j in ~T . Choosing (α(p1),α(p2),α(p3),α(p4)) = (0,0,−1,−1) andα(v)
and~ei asinFig. 4,weobtainthetable
0 1 2
~e1 z′
2 z2
1 z2
2 z′
1
~e2 z′
1(z′′
2)2 (z′′
1)2z′
2
where the (i, k)-entry is the product of shape parameters contributed fromμk · ~/Delta11 and
μk · ~/Delta12 to~ei (theemptyentriesare1).Thegluingequationaround ~ei istheproductofthe
entries of the corresponding row in the above table, i.e., the product over the vertices of
polygonsaroundeachedge ~e
i inFig. 4.Hence,wehave
G(t) =
(
2t 2t
00
)
, G′(t) =
(
t2 1
tt 2
)
, G′′(t) =
(
00
2t2 2t
)
, (41)
A(t) =
(
−t2 +2t 2t −1
−t −t2
)
, B(t) =
(
−t2 −1
2t2 − t −t2 +2t
)
, (42)
37 Page 14 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
Fig. 6 Thetriangulationoftheperipheraltorusof6 3
givingthat
A(t)B(1/t)T =
(
−2t +2 −2t−1 t + t−2
t2 + t−1 −2t +2 −2t−1
)
,
whichspecializestothematrix ABT when t = 1.
3.2 The knot 6 3
The default SnapPy triangulation of the knot 6 3 with isometry signature
gLLPQccdefffhggaacv_aBBbhassixtetrahedra /Delta11,... ,/Delta16 withtheperipheraltorus
showninFig. 6.
Thegluingequationsofthesixedgesare
e1 : z1z2z3z4z6 = 1,
e2 : z′
1z′
2(z′′
2)2z′
4(z′′
4)2z′
6 = 1,
e3 : z′′
1 z′
2z′
3z′
5z′′
6 = 1,
e4 : z′′
1 z′
3z′
4z′
5z′′
6 = 1,
e5 : z′
1z3(z′′
3)2z5(z′′
5)2z′
6 = 1,
e6 : z1z2z4z5z6 = 1
andthecorrespondinggluingequationmatricesare
G =
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
111101
000000
000000
000000
001010
110111
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
, G
′=
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
000000
110101
011010
001110
100001
000000
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
, G
′′=
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
000000
020200
100001
100001
002020
000000
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
. (43)
S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37 Page 15 of 23 37
Fig. 7 Thedual1-skeletonof E2
TheNZmatricesare
A =
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
111101
−1 −10 −10 −1
0 −1 −10 −10
00 −1 −1 −10
−10 1 0 1 −1
110111
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
, B =
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
000000
−11 0 1 0 −1
1 −1 −10 −11
10 −1 −1 −11
−10 2 0 2 −1
000000
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
,
with
AB
T =
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
0 0000 0
00 −1 −120
0 −13 2 −40
0 −12 3 −40
02 −4 −460
0 0000 0
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
symmetric. As in Sect.3.1, we assign an integer to (each oriented edge and) each vertex
ofthedualcomplexaccordingtotheabelianizationmap α : π
1(M) ↠ Z.SeeFig. 7.
Choosingalift ~ei of ei asinFig. 7,wehavethetable
0 1 2 3
~e1 z4 z1z3z6 z2
~e2 z′
1z′′
4 z′′
2 z′
4 z′
2z′′
4 z′′
2 z′
6
~e3 z′′
1 z′
5 z′
2z′
3z′′
6
~e4 z′′
1 z′
3z′
4 z′
5z′′
6
~e5 z′′
3 z′′
5 z′
6 z3z5 z′
1z′′
3 z′′
5
~e6 z1z2z4z5z6
37 Page 16 of 23 S. Garoufalidis, S. Yoon Res Math Sci (2023) 10:37
wherethe( i, k)-entryistheproductofshapeparameterscontributedfrom μk ·~/Delta11,... ,μk ·
~/Delta16 to~ei.Hence,wehave
G(t) =
⎛
⎜⎜⎜
⎜⎜⎜
⎜⎜⎝
tt
2 t 10 t
000000
000000
000000
00 t 0 t 0
t
2 t2 0 t2 t2 t2
⎞
⎟⎟⎟
⎟⎟⎟
⎟⎟⎠
, G
′(t) =
⎛
⎜⎜⎜
⎜⎜⎜
⎜⎜⎝
000000
1 t
2 0 t 0 t3
0 tt 010
00 t2 t2 t3 0
t2 00001
000000
⎞
⎟⎟⎟
⎟⎟⎟
⎟⎟⎠
,
G
′′(t) =
⎛
⎜⎜⎜⎜
⎜⎜⎜
⎜⎝
00 0 0 00
0 t + t
3 01 + t2 00
10 0 0 0 t
t2 0000 t3
001 + t2 01 + t2 0
00 0 0 00
⎞
⎟⎟⎟⎟
⎟⎟⎟
⎟⎠
(44)
and
A(t) =
⎛
⎜⎜
⎜⎜⎜
⎜⎜⎜⎝
tt
2 t 10 t
−1 −t2 0 −t 0 −t3
0 −t −t 0 −10
00 −t2 −t2 −t3 0
−t2 0 t 0 t −1
t2 t2 0 t2 t2 t2
⎞
⎟⎟
⎟⎟⎟
⎟⎟⎟⎠
,
B(t) =
⎛
⎜⎜⎜
⎜⎜⎜
⎜⎜⎝
00 0 0 0 0
−1 t − t
2 + t3 01 − t + t2 0 −t3
1 −t −t 0 −1 t
t2 0 −t2 −t2 −t3 t3
−t2 01 + t2 01 + t2 −1
00 0 0 0 0
⎞
⎟⎟⎟
⎟⎟⎟
⎟⎟⎠
, (45)
givingthat
A(t)B(1/t)T =⎛
⎜⎜
⎜
⎜
⎜
⎜⎝
00 0 0 0 0
0 −2t +4 −2t
−1 −t2 + t −1 −1 + t−1 − t−2 t3 + t−2 0
0 −1 + t−1 − t−2 3 t−1 + t−3 −t −1 − t−1 − t−2 0
0 −t2 + t −1 t3 + t 3 −t3 − t2 − t−1 −10
0 t2 + t−3 −t2 − t1 −1 − t−1 −1 − t−1 − t−2 − t−3 2t +2 +2t−1 0
00 0 0 0 0
⎞
⎟⎟
⎟
⎟
⎟
⎟⎠
whichspecializestomatrix ABT when t = 1.
