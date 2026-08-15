---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-024-122-two-tetrahedron-ideal-triangulations
section_title: "Two tetrahedron ideal triangulations"
section_number: 12.2
pages: 42-45
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
tions of orientable cusped 3-manifolds that decompose into two tetrahedra, and these 10
triangulations correspond to seven manifolds up to homeomorphism. The relevant data are
presented in Table 3.
THE 3D-INDEX AND NORMAL SURF ACES 43
n Hyp. Geom. Semi-Geom. Strict Ang. Struct. Semi-Ang. Taut 1-eﬃcient
2 2 2 2 2 2 2 2
3 12 12 12 12 12 12 12
4 138 110 121 119 134 134 134
5 1346 670 798 801 1165 1118 1190
6 14961 3857 4923 5221 10908 9927 11512
Table 2. This table provides data on the ideal triangulations of hyperbolic
manifolds in the census. Hyp. gives the total number of hyperbolic manifolds.
Geom. gives the number of triangulations which SnapPy found an approximate
hyperbolic structure and Semi-Geom. records the number of triangulations
which SnapPy found an approximate hyperbolic structure possibly with ﬂat
(and non-degenerate) tetrahedra. Strict. Ang. Struct. records the number
of triangulations admitting a strict angle structure, while Semi-Ang. records
the number of triangulations admitting a semi-angle structure. Finally, Taut
records the number of triangulations admitting a Taut structure and 1-eﬃcient
records the number of 1-eﬃcient triangulations of hyperbolic manifolds.
signature name 1-eﬃcient
cMcabbgds S1×D2 Yes
cMcabbgij S1×D2 Yes
cMcabbgik S1×D2 Yes
cPcbbbalm SFS [D2(3, 1)(3, 1)] Yes
cPcbbbali SFS [D2(3, 1)(3, 2)] Yes
cPcbbbadh SFS [D2(2, 1)(3, 1)] Yes
cPcbbbadu SFS [D2(2, 1)(3, 1)] Yes
cPcbbbdxm Figure 8 sister (m003) Yes
cPcbbbiht Figure 8 (m004) Yes
cPcbbbdei SFS [D2(2, 1)(3, 1)]∪SFS [A2(2, 1)] No
Table 3. The complete census of ideal triangulations with two tetrahedra.
The homeomorphism descriptions come from an appeal to the surgery de-
scription given by Martelli and Petronio [MP06], (which the diligent reader
can verify using a tangle computation).
Some Pachner Paths.
To provide a certiﬁcate of a path in the Pachner graph we list the vertices and also provide
the face consumed by a 2-3 move or the edge consumed by a 3-2 move. In the ﬁrst case,
we take the index of the face in the labelled triangulation determined by the isomorphism
signature. In the second, we take−index− 1 of the edge (the minus sign indicates that an
edge is being consumed and shifting by−1 removes the ambiguity of−0 and +0 that would
arise if we were required to perform a 3-2 along edge 0).
44 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Example 12.3. Solid Torus.The (open) solid torus has 3 minimal ideal triangulations
with 2 tetrahedra. The paths shown in Table 4 are 1-eﬃcient paths in the Pachner graph
connecting these minimal triangulations.
Path 1 Path 2 Path 3
isoSig 2-3 move isoSig 2-3 move isoSig 2-3 move
‘cMcabbgds’ 0 ‘cMcabbgds’ 0 ‘cMcabbgij’ 0
‘dLQbcccaego’ 0 ‘dLQbcccaego’ 4 ‘dLQbcccahgc’ 5
‘eLPkbcdddhgcgj’ -3 ‘eLPkbcdddhcgcf’ -2 ‘eLAkbccddaegtr’ -3
‘dLQbcccahgc’ -3 ‘dLQacccjrgr’ 2 ‘dLQbcbcaekv’ 2
‘cMcabbgij’ ‘end’ ‘eLPkbcdddhcgbf’ -1 ‘eLAkbccddaegtn’ -4
- - ‘dLQbcccahgo’ -3 ‘dLQbcccahgo’ -3
- - ‘cMcabbgik’ ‘end’ ‘cMcabbgik’ ‘end’
Table 4. Some 1-eﬃcient paths for triangulations of the solid torus
Remark 12.4. This analysis shows that the 1-eﬃcient Pachner graph (of ideal triangulations)
of the solid torus is not connected. Speciﬁcally, we can say the following: Both ‘gLLAQbece-
fefaaopaaj’ and ‘gLLAQbecefefaaopaan’ are six tetrahedral triangulations of the solid torus
that 1) have no degree 3 edges and 2) each 2-3 move along a face in either triangulation
results in a not 1-eﬃcient triangulation. However, we can still relate the 3D-index to the
3D-index of the triangulations of the solid torus in Table 3. In fact, both of these six tetra-
hedral triangulations have (three) degree two edges. After performing a 2-0 move on any
degree two edge of one of these triangulations, the resulting triangulation is 1-eﬃcient and
connected to the triangulation ‘cMcabbgij’ via a path of 1-eﬃcient triangulations. There-
fore, the 3D-index is consistent with the two tetrahedral triangulation of an ideal solid torus
‘cMcabbgij’ by [GHRS15, Theorem 5.1].
Example 12.5. Trefoil Complement.The trefoil complement (SFS [D2(2, 1)(3, 1)]) has
two minimal triangulations that are connected along a path of length 6 (see Figure 13 and
Table 5) and a 1-eﬃcient path of length 12 (see Figure 13 and Table 6).
12.3. Angle Structures, 1-eﬃciency and Pachner moves.A natural question is how
are various properties of triangulations related by Pachner moves. Throughout this section,
Tn will be a triangulation with n tetrahedra, f will be a face in this triangulation that
identiﬁes two distinct tetrahedratf,1 and tf,2, and Tn+1,f will be the result of performing
a 2-3 move along the facef. If we call the pairs of edges incident tof in the bi-pyramid
deﬁned bytf,1 andtf,2, thebelt off, then we can make the following observation that is well-
known to the experts. We include it because it promotes a useful mentality and compares
favourably to our discussion of 1-eﬃciency and Pachner moves.
Proposition 12.6.Let Tn be a triangulation withn tetrahedra. With all notation as above,
Tn+1,f admits a strict angle structure if and only if the set of angle structures contains a
strict angle structure (resp. semi-angle structure) such that each of the three pairs of edges
along the belt off have a sum in(0,π ) (resp. [0,π ]).
THE 3D-INDEX AND NORMAL SURF ACES 45
g O4 O8 6
f O3 O5 T3 O7 O9 5
e O2 T2 O6 T4 O10 4
d O1 T1 T5 O11 3
c Ts Tf 2
Figure 13. A shortest Pachner path between minimal triangulations of the
trefoil (green) and a longer 1-eﬃcient path (red). Note, the 1-eﬃcient path is
a shortest path through 1-eﬃcient triangulations using 2-3/3-2 moves. If 0-
2/2-0, moves are allowed then the red and green paths shorten to{Ts,O 6,Tf}
(blue dashed). Also, a computation in Regina shows all triangulations on the
green path exceptTs and Tf are not 1-eﬃcient.
Figure name isoSig move
Ts ‘cPcbbbadh’ 2
T1 ‘dLQacccbgjs’ 1
T2 ‘eLPkbcdddacrnn’ 4
T3 ‘fvPQccdedeeccvbfb’-1
T4 ‘eLPkbcdddackjj’ -2
T5 ‘dLQacccbgbk’ -3
Tf ‘cPcbbbadu’ ‘end’
Table 5. A shortest Pachner path between the two minimal triangulations
of the trefoil complement.
Proof. We only need to consider the tetrahedra in the bi-pyramid as the other angles will be
unaﬀected by a 2-3 move.
Considering Figure 12, this problem reduces to a problem in the Euclidean plane: namely
showing that the triangles incident to the vertices at the top and bottom of the bi-pyramid
each split into 3 triangles with angles in the desired range. However, the angles around the
vertex are all in(0,π ) (resp. [0,π ]), so the vertex is embedded in the interior (resp. interior
or a side).
The other direction is obvious as an angle structure onTn+1,f implies that all angles along
the edges of the bi-pyramid are positive (resp. non-negative). □
