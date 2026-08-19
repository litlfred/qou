---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-007-32-collapsing-the-octahedral-decomposition-to-an
section_title: "Collapsing the octahedral decomposition to an ideal triangulation"
section_number: 3.2
pages: 11-13
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
section we discuss how to collapse the ideal cell decomposition OD of S3\ (K∪{p,q}) into
an ideal triangulationTD ofS3\K. The collapsing depends on fixing an alternating segment
s ofD. By alternating we mean that we overpass the diagram at one end of s and underpass
at the other end. We denote by r1 and r2 two regions adjacent to s, and by o and u the
over-arc and under-arc containing s, respectively (see Figure 9).
Recall that the octahedral decomposition OD has four edges corresponding to the regions
r1, r2, the over-arc o, and the under-arc u, respectively. We remove all tetrahedra of OD
that contain one of those four edges. When viewed from the top, they are represented by
triangles lying inr1 orr2, and ones lying besideo oru. After removing those triangles as well
as dashed lines in between, we add new dashed lines or arcs in an obvious way so that every
dashed line is connected, shown as in Figure 9. Then all faces of the remaining tetrahedra are
paired along dashed lines or arcs. This results in an collapsed ideal triangulation of S3\K.
As the pair (D,s ) is determined by the open diagram ˚D obtained by cutting D acrosss, we
denote the collapsed triangulation simply by T˚D. Note that s being alternating implies the
technical assumption (†) on ˚D in Section 2.3.
±
±
±
u
o
s
 ···
r1
r2
±
±
±
±
±
±
±
···
±
±
Figure 9. Modified face-pairings.
Suppose that the over-arc o, the under-arc u, and the regions r1 and r2 haveno, nu, nr1
and nr2 segments of D, respectively. When OD collapses into T˚D, tetrahedra lying in r1
or r2, and ones lying beside o or u disappear: total ( nr1 +nr2 + 4nu + 4no− 8) disappear.
Therefore, if D has n crossings,
#(tetrahedra ofT˚D) = 4n−nr1−nr2− 4nu− 4no + 8.
On the other hand, when OD collapses intoT˚D, edges of different types can be identified.
In this case, we keep the bigger type according to the following order.
C <R<O,U.
For instance, if a C-edge and an O-edge are identified, we call the identified one an O-edge.
Exceptionally, if an O-edge and a U-edge are identified, we retain both types: the identified
edge is both an O-edge and a U-edge.
12 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
To describe how edges change explicitly, we denote the crossings ofu ando byc1,...,c nu+1
and cnu,...,c nu+no respectively, in order so that the common ones, cnu and cnu+1, are the
crossings ofs. We also denote a segment of u oro by [ci,ci+1] for 1≤i≤no +nu− 1. When
OD collapses intoT˚D,
• (nu +no) C-edges disappear. These correspond to c1,...,c nu+no: more precisely,
(Ca) the one corresponding to c1 is identified with the U-edge corresponding to
the under-arc of c1;
(Cb) the one corresponding tocnu+no is identified with the O-edge corresponding
to the over-arc of cnu+no;
(Cc) the others disappear.
• (nu +no + 2) R-edges disappear. Precisely, two R-edges corresponding to regions
adjacent to [ci,ci+1] for 1≤i≤nu +no− 1:
(Ra) disappear if i =nu (i.e., if [ci,ci+1] =s);
(Rb) are identified with the O-edge corresponding to the over-arc of c1 ifi = 1;
(Rc) are identified with the U-edge corresponding to the under-arc of cnu+no if
i =nu +no− 1;
(Rd) are identified to one R-edge, otherwise.
• (nu +no− 3) O-edges disappear. Precisely,
(Oa) the O-edge corresponding to the over-arc containing [ ci,ci+1] vanishes for
1<i ≤nu;
(Ob) two O-edges corresponding to adjacent over-arcs at ci other than o are
identified for nu + 1<i<n u +no.
• (nu +no− 3) U-edges disappear. Precisely,
(Ua) the U-edge corresponding to the under-arc containing [ci,ci+1] vanishes for
nu <i ≤no +nu;
(Ub) two U-edges corresponding to adjacent under-arcs at ci other than u are
identified for 1 <i<n u.
In addition, for each segments′̸=s lying inr1 orr2, an O-edge corresponding to the over-arc
containings′ is identified with a U-edge corresponding to the under-arc containing s′. This
leads to (nr1 +nr2−2) identifications between O-edges and U-edges. We refer to Appendix A
for details. Therefore, if D has n crossings,
#(edges ofT˚D) = (4n + 2)− (nu +no)− (nu +no + 2)
− (nu +no− 3)− (nu +no− 3)− (nr1 +nr2− 2)
= 4n−nr1−nr2− 4no− 4nu + 8.
This double-checks that the number of edges is equal to the number of tetrahedra.
Example 2.4 continued. For the open diagram ˚D of Figure 2, its closureD is shown on the
left of Figure 10. The diagram D has six crossings, and thus the octahedral decomposition
OD has six C-edges and eight R-edges, as well as six O-edges o1,...,o 6 and six U-edges
u1,...,u 6. It is convenient to label a segment of D byoi/uj where oi and uj correspond to
the over and under-arcs containing the segment, respectively.
We choose an alternating segments as the one with o6/u1 (the leftmost one). Then, when
OD collapses into the collapsed triangulation T˚D,
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 13
• four C-edges adjacent to the segment with o1/u1, o6/u1, or o6/u6 disappear,
• two R-edges adjacent to the segment with o6/u1 disappear,
• two R-edges adjacent to the segment with o1/u1 are identified with o1,
• two R-edges adjacent to the segment with o6/u6 are identified with u6,
• o6 and u1 disappear.
In addition, we obtain identifications
o4 =u4, o 1 =u2, o 2 =u2, o 5 =u6, o 3 =u3, o 4 =u5
from segments lying in the unbounded region ofD. It follows that the collapsed triangulation
T˚D has two C-edges, two R-edges, and four O or U-edges:
{(o1 =o2 =u2), (o3 =u3), (o4 =u4 =u5), (o5 =u6)}.
To connect the 8 shape parameters of the collapsed triangulation T˚D with the 3 variables
of the Yokota potential of Figure 2, we will eliminate five of them by solving to the gluing
equations of two C-edges and two R-edges, and completeness equation of the meridian; see
Section 4.2 for details.
o1
u1
o1
u2
R-edges
C-edges
o2
u2
o2
u3
o3
u3
o3
u4
o4
u4
o4
u5
o5
u5
o5
u6
o6
u6
o6
u1
o1
o1
u2
o2
u2
o2
u3
o3
u3
o3
u4
o4
u4
o4
u5
o5
u5
o5
u6
u6
Figure 10. Edges ofOD andT˚D.
