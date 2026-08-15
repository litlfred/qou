---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-024-11-examples
section_title: "Examples"
section_number: 11
pages: 21-25
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
Let M be the manifold m009 from the SnapPy census [3]. The census triangulationT of M
is shown in Figure 15. We refer to the three edges asedge 1, edge 2, and edge 3, according to
the number of arrow heads. By inspecting the ﬁgure, one checks that there are four transitive
edge sets: The non-degenerate edge set where all edges are nonzero, the edge-degenerate edge
set where only edge 1 is zero, the edge-degenerate edge set where only edge 2 is zero, and the
totally degenerate edge set (which we ignore, see Section 6.2). The edge relation around edge 1
is given by
(11.1) c23,0
c21,0c13,0
+ c01,1
c03,1c31,1
+ c10,0
c12,0c20,0
+ c01,2
c03,2c31,2
+ c23,1
c21,1c13,1
+ c32,2
c30,2c02,2
= 0
22 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
0 2
31
0 2
31
0 2
31
c13,0
c23,0
c01,1 c12,1c03,1 c23,1c01,0
c02,0 c02,1 c02,2
c23,2c12,2
c13,2c13,1
c12,0 c01,2 c03,2
t2
b
c
t1
a d
Figure 15. Census triangulation of m009. The signs on the faces indicate the
obstruction cocycleσ3.
and the edge relation around edge 2 is given by
(11.2) c02,0
c01,0c12,0
+ c30,1
c31,1c10,1
+ c20,2
c23,2c30,2
+ c12,1
c13,1c32,1
= 0.
Since there is no transitive edge set where edge 3 is zero (except the totally degenerate edge
set), Theorem 9.3 implies that the reduced Ptolemy variety (all variants) is given by setting the
Ptolemy coordinate of edge 3 equal to1.
11.1. ThePtolemyvariety P (T ). Theidentiﬁcationrelationscorrespondingtothethreeedges
are
(11.3)
c23,0 =−c23,2 =−c01,1 =c01,2 =−c01,0 =−c23,1
c13,0 =c12,1 =−c13,2 =−c03,1 =c13,0
c13,1 =c03,2 =c02,0 =c12,2 =−c02,1 =c03,0 =c02,2 =c12,0.
Letting x = c23,0, y = c13,0 and z = c13,1, the Ptolemy relationsc03,ic12,i +c01,ic23,i = c02,ic13,i
become
(11.4) z2−x2 =zy, −y2 +x2 =−z2, z 2−x2 =−zy.
One easily checks that the only solution to this isx =y =z = 0, so the Ptolemy varietyP (T ) is
empty. There are thus no irreducible, boundary-unipotentSL(2, C)-representations of m009 (as
mentioned in Section 3.1, the geometricPSL(2, C)-representation has no boundary-unipotent lift
to SL(2, C)).
11.2. The Ptolemy varieties P
σ
(T ). An elementary cohomology computation shows that
H 2(ˆM; Z/2Z) = Z/2Z⊕ Z/2Z and that the three non-trivial classes are represented by cocycles
σi∈C2(ˆM; Z/2Z) whose restrictionsσi
k to thekth simplex ofT are given by
(11.5)
σ1
0 =f∗
0 +f∗
2, σ 1
1 =f∗
0 +f∗
1, σ 1
2 = 0,
σ2
0 =f∗
0 +f∗
1, σ 2
1 =f∗
0 +f∗
3, σ 2
2 =f∗
0 +f∗
1,
σ3
0 =f∗
1 +f∗
2, σ 3
1 =f∗
1 +f∗
3, σ 3
2 =f∗
0 +f∗
1,
where f∗
i ∈C2(∆; Z/2Z) denotes the cochain taking the facefi opposite vertexi to−1 and all
other faces to1. The cocycleσ3 is indicated in Figure 15.
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 23
One easily checks thatσi
k =δ(ηi
k), whereηi
k is given by
(11.6)
η1
0 =ε∗
13, η 1
1 =ε∗
23, η 1
2 = 0,
η2
0 =ε∗
23, η 2
1 =ε∗
12, η 2
2 =ε∗
23,
η3
0 =ε∗
03, η 3
1 =ε∗
02, η 3
2 =ε∗
23,
where ε∗
ij∈C1(∆; Z/2Z) is the cochain takingεij to−1 and all other edges to1. The Ptolemy
variety for the trivial obstruction class is equal toP (T ), which is trivial, as we saw earlier. Recall
that the reduced Ptolemy variety is obtained by setting the Ptolemy coordinatez of edge 3 equal
to 1.
11.2.1. Ptolemy variety forσ1. The identiﬁcation relations (3.1) are
(11.7)
c23,0 =−c23,2 =−c01,1 =c01,2 =−c01,0 =c23,1
c13,0 =−c12,1 =c13,2 =c03,1 =c13,0
c13,1 =c03,2 =c02,0 =c12,2 =−c02,1 =c03,0 =c02,2 =c12,0.
Again, lettingx =c23,0, y =c13,0 and z =c13,1, the Ptolemy relations become
(11.8) z2−x2 =zy, −y2−x2 =−z2, z 2−x2 =zy.
Setting z = 1, the equations then have the three solutions
(11.9) (x,y,z ) = (0, 1, 1), (x,y,z ) = (−1, 0, 1), (x,y,z ) = (1, 0, 1).
However, not all of these solutions are valid, since the edge equations may not be satisﬁed. The
edge relation (11.1) around edge 1 (deﬁned wheny and z are nonzero) is
(11.10) x
−zy + −x
y(−z) + x
z(−z) + x
z(−y) + x
yz + x
−zz =−2x
z2 = 0
which is satisﬁed whenx is zero. Similarly, the edge relation (11.2) around edge 2 (deﬁned when
z and x are nonzero) is
(11.11) z
−xz + −y
−zx + −z
−x(−z) + −y
z(−x) = 2y
zx− 2
x = 0,
which is not satisﬁed. Hence, the reduced Ptolemy variety forσ1 consists of a single point given
by (x,y,z ) = (0, 1, 1).
11.2.2. Ptolemy variety forσ2. The Ptolemy relations are
(11.12) z2 +x2 =yz, y 2 +x2 =−z2, z 2 +x2 =−yz,
which have no non-trivial solution. Hence, the Ptolemy varietyP
σ2
(T ) is empty.
11.2.3. Ptolemy variety forσ3. The Ptolemy relations are
(11.13) z2 +x2 =yz, y 2 +x2 =−z2, z 2 +x2 =−yz,
and settingz = 1 they are equivalent to
(11.14) x2 +y + 1 = 0, y 2 +y + 2 = 0, z = 1
Hence, there are no solutions withx ory being 0, andP
σ3
(T )red is deﬁned over the number ﬁeld
Q(w), wherew4 +w2 + 2 = 0, and is given byx =w, y =−w2− 1, z = 1.
24 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
11.3. The Ptolemy varietyEP (T ) and theA-polynomial. A fundamental rectangle for the
boundary ofM is shown in Figure 16. Using the rules illustrated in Figure 3 we obtain that the
identiﬁcation relations are given by
00
3
0
12
21 30
22
20
32 02
11
10
31
22
3
0
3
1
0
0
1
32
1
3 3
2
0 3
1
01
2
0
120
1
3
1
2 20
30 1
1 0
bc t1
a
d b
t2
t1a
c
t2
c
d t2
t1
b
d
b
Figure 16. Fundamental rectangle form009.
(11.15)
c23,0
t2
=−m2c23,2
c=−m2c01,1
d=m2c01,2
b=−mc01,0
a=−c23,1,
c13,0
t1
=c12,1
c=−c13,2
d=−c03,1,
c13,1
d=c03,2
t2
=m−1lc02,0
b=m−1lc12,2
c=−m−1lc02,1
a=lc03,0
t2
=mc02,2
b=c12,0,
where the symbolα= indicates that the identiﬁcation is via the face pairingα. Hence, the Ptolemy
relations become
(11.16) mz2−lx2−m2yz, m 2ly2−lx2−m3z2, m 5z2−lx2 +m3lyz.
One easily checks that there are no non-trivial solutions withx = 0. The edge relation (5.4)
around edge 2 is
(11.17) ml−1z
−m−1xz + y
(−z)m−2x + −m−1z
−m−2x(−z) + y
zx = 0 ⇐⇒ m2z +m2ly +mlz−ly = 0
Adding this equation to the Ptolemy relations (11.16) and substitutingz = 1, one can check
(using magma [1]) that the system is equivalent to
(11.18)
x2 +yl−m8 + 3m6 +m5l +m4−m3l− 3m2−ml = 0,
y2l +yl2 +m4l−m3−m2l−ml2−m−l = 0,
ym +yl +m4−m2−ml− 1 = 0,
yl3−yl−m5l +m4l2 +m3l +m2−ml3 + 2ml−l2 = 0,
m6l− 2m4l−m3l2−m3− 2m2l +l = 0.
This shows that theA-polynomial of m009 is given by
(11.19) A(m,l ) =m6l− 2m4l−m3l2−m3− 2m2l +l.
It also follows thatEP (T ) is a branched cover over theA-polynomial curve of degree 2. Another
magma computation shows that it is given explicitly by
(11.20) x2 =−−m4− 2m3l +ml
l2(m2− 1) , y =−m2 +ml
m2l−l , z = 1, A (m,l ) = 0.
Note thaty and x2 are regular functions on theA-polymial curve.
TRIANGULATION INDEPENDENT PTOLEMY V ARIETIES 25
