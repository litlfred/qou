---
doc_id: arxiv-1507.03238v3
doc_title: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES"
section_id: sec-014-5-the-edge-relations
section_title: "The edge relations"
section_number: 5
pages: 13-14
source_pdf: 1507.03238v3.pdf
source_sha256: 1da6a5498c08a521
doc_brief: "TRIANGULATION INDEPENDENT PTOLEMY VARIETIES — The Ptolemy variety forSL(2, C) is an invariant of a topological ideal triangulation of a compact 3-manifold M."
---
We now deﬁne a relation among the Ptolemy coordinates of a decorated (boundary-unipotent)
representation. This relation is a consequence of the Ptolemy relations in the case when all
Ptolemy coordinates are nonzero, but if some Ptolemy coordinates are zero, this relation is
independent of the Ptolemy relations. Hence, when deﬁning the invariant Ptolemy variety this
relation must be imposed in addition to the Ptolemy relations.
Let K be the space obtained by cyclically gluing together ordered simplices∆0,..., ∆N−1
along a common edge. We order the vertices of each simplex such that the common edge is
the 01 edge of each simplex, and such that the orientations induced by the orderings agree (see
Figure 7). We refer to the edges (other than the common edge) astop, bottom, andcenter edges
respectively.
Lemma 5.1.Letc be a Ptolemy assignment onK where all the Ptolemy coordinates of the top
and bottom edges ofK are nonzero. We then have
(5.1)
N−1∑
k=0
c23,k
c12,kc13,k
= 0 ⇐⇒
N−1∑
k=0
c23,k
c02,kc03,k
= 0.
Moreover, if the Ptolemy coordinatec01 of the interior edge is also nonzero, both equations are
satisﬁed.
Proof. We ﬁrst assume thatc01⁄= 0. We have
(5.2)
c01
N−1∑
k=0
c23,k
c12,kc13,k
=
N−1∑
k=0
c02,kc13,k−c03,kc12,k
c12,kc13,k
=
N−1∑
k=0
c03,k−1c13,k−c03,kc13,k−1
c13,k−1c13,k
=
N−1∑
k=0
(c03,k−1
c13,k−1
− c03,k
c13,k
)
= 0.
Here, the ﬁrst equality follows from the Ptolemy relations (2.1), and the second from the identiﬁ-
cation relationsc12,k =c13,k−1 andc02,k =c03,k−1 (indices moduloN). By a similar computation,
one also has
(5.3) c01
N−1∑
k=0
c23,k
c02,kc03,k
= 0.
14 MATTHIAS GOERNER AND CHRISTIAN K. ZICKERT
Since we are assuming thatc01⁄= 0, (5.2) and (5.3) together prove the second statement.
If c01 = 0 , the Ptolemy relations become c03,kc12,k = c02,kc13,k, which together with the
identiﬁcation relationsc12,k =c13,k−1 and c02,k =c03,k−1 imply that the ratio betweenc12,kc13,k
and c02,kc03,k is independent ofk. This concludes the proof. □
0
1
2 33
23
2 3
2
3 2c01
c23,1
c23,N−1
c23,2
c23,0
c02,k=c03,k−1
c12,k=c13,k−1
x(d1)
⇐⇒
N−1∑
k=0
dk= 0
dk = c23,k
c12,kc23,k
x(dN−1)
N−1∏
k=0
x(dk) =I
x(d0)
Figure 7. A Ptolemy assignment onK. Figure 8. Bruhat cocycle
on K (near top vertex).
Deﬁnition 5.2.We call the (equivalent) relations (5.1)edge relations around the center edge
of K.
Remark 5.3.When all Ptolemy coordinates are nonzero, the fundamental correspondence pro-
vides a natural cocycle on the spaceK obtained fromK by truncating the simplices. In this case,
the edge relations are equivalent to the relation coming from the fact that the product of short
edges around the top and bottom isI (see Figure 8). When some of the Ptolemy coordinates
are zero this relation is no longer automatically satisﬁed and must be imposed.
5.1. Edgerelationsfor PSL(2, C)Ptolemyassignments. TheobviousanalogueofLemma5.1
for PSL(2, C) Ptolemy assignments still holds and we deﬁne the edge relations forPSL(2, C)
Ptolemy assignments by the exact same formula 5.1.
