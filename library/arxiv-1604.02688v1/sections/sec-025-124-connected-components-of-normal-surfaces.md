---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-025-124-connected-components-of-normal-surfaces
section_title: "Connected components of normal surfaces"
section_number: 12.4
pages: 45-50
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
mids related by a 2-3 move, one with two tetrahedra which we callB2 and one with three
tetrahedra which we callB3. We will also think of these as subsets of two triangulations
related by a 2-3 move,Tn and Tn+1,f where f is face identiﬁed inB2. In this discussion, we
assume that the exterior faces ofB2 are not identiﬁed. However, if the exterior faces ofB2
46 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Figure name isoSig move
Ts ‘cPcbbbadh’ 1
O1 ‘dLQacccjgjb’ 5
O2 ‘eLAkbbcdddugaj’ 2
O3 ‘fLLQcccddeeabvnln’ 5
O4 ‘gLvQQadfeeﬀjatxcfj’-5
O5 ‘fLAPcacceeejgjﬀc’ -3
O6 ‘eLMkbbdddadiih’ 0
O7 ‘fLAPcacceeejgjcrc’ 6
O8 ‘gLvQQadfeeﬀjaaxcfj’-4
O9 ‘fLLQcccddeeabvrln’ -4
O10 ‘eLAkbbcdddurar’ -2
O11 ‘dLQacccjgjs’ -3
Tf ‘cPcbbbadu’ ‘end’
Table 6. A shortest one-eﬃcient Pachner path between the two minimal
triangulations of the trefoil complement.
are identiﬁed (and thereforeB3), then some of these pieces might not appear as subsets of
embedded normal surfaces.
If Sn is a normal surface ofTn then each piece will have at most one normal arc in face
f. Using the notation from Section 3.1 and Figure 1, we thus obtain a census of connected
components Sn∩ B2 as follows:
(1) tA0,tB1;
(2) (tA1 +tB1), (tA2 +tB3), (tA3 +tB2);
(3) (qA01:23 + tB1), (qA02:13 + tB3), (qA03:12 + tB2), (qB01:23 + tA1), (qB02:13 + tA3), and
(qB03:12 +tA2);
(4) (qA01:23 +qB01:23), (qA02:13 +qB03:12), (qA03:12 +qB02:13).
If Sn+1 is a normal surface of Tn+1,f, we can obtain an analogous result. Namely, the
observation that each connected component ofSn+1∩ B3 intersects an interior face ofB3 in
at most one normal arc, yields the following list:
(1) (tC0 +tD0 +tE0), (tC1 +tD1 +tE1);
(2) (tC2 +tE3), (tD2 +tC3), (tD3 +tE2);
(3) (tD0 +qC02:13 +qE03:12), (tE0 +qD02:13 +qC03:12), (tC0 +qE02:13 +qD03:12), (qD01:23 +
tC3 +tE2), (tE1 +qD03:12 +qC02:13), (tC1 +qE03:12 +qD02:13);
(4) (qD01:23 +tC3 +tE2), (qE01:23 +tD3 +tC2), (qC01:23 +tE3 +tD2);
(5) (qC01:23+qD01:23+tE2+tE3), (qD01:23+qE01:23+tC2+tC3), (qE01:23+qC01:23+tD2+tD3);
(6) (qC01:23 +qD01:23 +qE01:23).
Examples of the normal surface pieces of type 3) and 4) are given in Figures 14 and 15.
Examples of the normal surface pieces of type 5) and 6) are given in Figures 16 and 17.
The following proposition allows us relate the pieces in both list above via the 2-3 move
that transforms B2 to B3.
THE 3D-INDEX AND NORMAL SURF ACES 47
Figure 14. The eﬀect of a 2-3 move on a normal disk comprised of a triangle
and quad.
Figure 15. The eﬀect of a 2-3 move on a normal disk comprised of two quads.
48 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Figure 16. An example of a normal surface piece ofB3.
Figure 17. A second example of a normal surface piece ofB3.
Proposition 12.7. Let Tn and Tn+1,f be the triangulations deﬁned above. For each normal
surface Sn of Tn there exists a normal surfaceSn+1 of Tn+1,f obtained by dividing up the
normal discs of Sn which intersect B2. In particular, if Tn+1,f is 1-eﬃcient, then Tn is
1-eﬃcient.
Proof. Following Figure 11, we can consider the images ofSn∩ B2 under the 2-3 move:
(1) tA0 =tC0 +tD0 +tE0, tB0 =tC1 +tD1 +tE1
(2) tA1 +tB1 =tC2 +tE3, tA2 +tB3 =tD2 +tC3, tA3 +tB2 =tE2 +tD3
(3) qA01:23 +tB1 =tD0 +qC02:13 +qE03:12, qA02:13 +tB3 =tE0 +qD02:13 +qC03:12, qA03:12 +
tB2 = tC0 +qE02:13 +qD03:12, qB01:23 +tA1 = tD1 +qC03:12 +qE02:13, qB02:13 +tA3 =
tE1 +qD03:12 +qC02:13, qB03:12 +tA2 =tC1 +qE03:12 +qD02:13,
(4) qA01:23 +qB01:23 =qD01:23 +tC3 +tE2, qA02:13 +qB03:12 =qE01:23 +tD3 +tC2, qA03:12 +
qB02:13 =qC01:23 +tE3 +tD2.
THE 3D-INDEX AND NORMAL SURF ACES 49
Relations (1) and (2) follow from Figure 12.
Note thatqA01:23 +tB1 =tD0 +qC02:13 +qE03:12 follows from Figure 14, and the remaining
two relations can be obtained by an appropriate rotation (and relabelling) of that ﬁgure.
Finally,qA01:23+qB01:23 =qD01:23+tC3+tE2 follows from Figure 15, and again the remaining
two relations can be obtained by an appropriate rotation (and relabelling) of that ﬁgure.
Thus, for any normal surface ofSn, we can map the normal surface pieces locally to build
a normal surface with the same Euler characteristic inTn+1,f. Restricting this observation
to the case of embedded normal surfaces with non-negative Euler characteristics shows if
Tn+1,f is 1-eﬃcient, thenTn must be as well. □
We point out that the Luo-Tillmann’s deﬁnition of Euler characteristic on quadrilateral
discs in the presence of a generalised angle structure (compare [LT08, Lemma 15] in the case
that the curvature is 0) provides a useful mnemonic for keeping track of relations of type (3)
and (4). Namely, these relations are just the angle sums which occur after a 2-3 move, e.g.
edge A01 decomposes into edgesC02 and E03 and edgesA23 and B23 form D23.
Proposition 12.8. Let Tn and Tn+1,f be the triangulations deﬁned above, such that the
exterior faces ofB2 are not identiﬁed. IfTn is 1-eﬃcient andTn+1,f is not 1-eﬃcient, then
Tn+1,f exhibits an embedded normal surface with exactly two of the three quad types parallel
to the degree three edge created by the 2-3 move.
Proof. If Tn is 1-eﬃcient andTn+1,f is not 1-eﬃcient, then there must be an embedded normal
surface Sn+1 in Tn+1,f which intersects B3. If this intersection is only triangular discs then
Sn+1 would descend to an embedded normal surface inTn, and soSn+1∩ B3 must contain
at least one connected component with at least one quad. However, the case analysis in
Proposition 12.7 of the normal discs inB3 shows that each connected componentSn+1∩ B3
is in the image of an embedded normal disk ofB2 save four: qC01:23 +qD01:23 +tE2 +tE3,
qD01:23 +qE01:23 +tC2 +tC3, qE01:23 +qC01:23 +tD2 +tD3, and (qC01:23 +qD01:23 +qE01:23).
However, if the last piece is part ofSn+1∩ B3, then there exists a collection of embedded
normal spheres ˆSn+1 of Tn+1,f formed by cutting out all copies of this annulus and capping
oﬀ with triangles. If none of these spheres have pieces of the form:qC01:23+qD01:23+tE2+tE3,
qD01:23 +qE01:23 +tC2 +tC3, andqE01:23 +qC01:23 +tD2 +tD3, then there exists an embedded
normal sphere inTn, a contradiction. If no annuli of the form(qC01:23 +qD01:23 +qE01:23) exist
inSn+1∩B3, thenagaintheremustbeatleastonepieceoftheform: qC01:23+qD01:23+tE2+tE3,
qD01:23 +qE01:23 +tC2 +tC3, andqE01:23 +qC01:23 +tD2 +tD3, which completes the proof. □
AlthoughqC01:23+qD01:23+tE2+tE3,qD01:23+qE01:23+tC2+tC3, andqE01:23+qC01:23+tD2+tD3
are not in the image of embedded normal discs ofTn, they are in the image of a pair of
immersed normal discs. For example,qA03:12 +qB02:13 +qA01:23 +qB01:23 =qC01:23 +qD01:23 +
tE2 +tE3 +tC3 +tD2. This is the key observation in the proof of the following lemma.
Proposition 12.9. Let Tn and Tn+1,f be the triangulations deﬁned above, such that the
exterior faces of B2 are not identiﬁed. IfTn admits a strict angle structure, thenTn+1,f is
1-eﬃcient.
Proof. Suppose Tn+1,f is not 1-eﬃcient. Then there is a closed embedded normal surface
Sn+1 of Tn+1,f with non-negative Euler characteristic.
50 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Just as above,Sn+1∩ B3 must contain pieces of the form below, otherwise there is a closed
embedded surfaceSn of Tn with non-negative Euler characteristic:
qC01:23 +qD01:23 +tE2 +tE3, qD01:23 +qE01:23 +tC2 +tC3, qE01:23 +qC01:23 +tD2 +tD3, and
(qC01:23 +qD01:23 +qE01:23).
By an identical argument to the one used in Proposition 12.8, we can rule out the annuli of
the form(qC01:23+qD01:23+qE01:23). Thus,Sn+1∩B3 contains exactly one of the following pairs
of quads:qC01:23 +qD01:23 +tE2 +tE3,qD01:23 +qE01:23 +tC2 +tC3, orqE01:23 +qC01:23 +tD2 +tD3.
Without loss of generality, assume it isqC01:23 +qD01:23 +tE2 +tE3. Create a new surface
S′
n+1, by adding a boundary torus toSn+1 untilSn+1∩B3 contains the same number of copies
of (tC3 +tD2) asqC01:23 +qD01:23 +tE2 +tE3. Note thatχ(Sn+1) =χ(S′
n+1). The image ofS′
n+1
under the 3-2 move, is an immersed normal surfaceSn with the same boundary arcs onB2
as∂B3∩S′
n+1, with the property that for each copy ofqC01:23 +qD01:23 +tE2 +tE3 +(tC3 +tD2)
in B3∩S′
n+1 there is a copy ofqA03:12 +qB02:13 +qA01:23 +qB01:23. In the presence of any
generalised angle structure onTn, each quad is assigned an Euler characteristic, while the
Euler characteristic of the triangles vanishes. Moreover, this Euler characteristic agrees
with the Euler characteristic ofS′
n+1. However, if Tn admits a strict angle structure, then
each quad has a negative contribution to Euler characteristic while each triangle does not
contribute to Euler characteristic. This contradictsχ(Sn+1)≥ 0. □
Remark 12.10. The analogous statement to Proposition 12.9 for 0-2 moves does not hold.
In fact, ‘eLAkbbcdddhjac’ has a degree 2 edge and is not 1-eﬃcient. However, performing
a 2-0 move along this edge results in the 1-eﬃcient (in fact, geometric) triangulation of the
ﬁgure 8 sister manifold, ‘cPcbbbdxm’.
Example 12.11.We next provide an example of how a geometric triangulation can ‘degen-
erate’ to a triangulation which is not 1-eﬃcient in two 2-3 moves: The triangulation ‘eLAk-
bccddhhnqw’ is geometric, the 2-3 move along face 5 gives ‘fLAMcbccdeemejman’ which
does not admit a strict angle structure, and the 2-3 move along face 8 gives ‘gLALQacceﬀf-
bgfgmqt’ which is not 1-eﬃcient.
However, perhaps the simplest example of a non 1-eﬃcient triangulation arising from
a 2-3 move on a 1-eﬃcient triangulation has already been discussed in Table 5. In fact
the ﬁrst Pachner move in that path a 2-3 move along face 2 of ‘cPcbbbadh’ resulting in
‘dLQacccbgjs’ breaks 1-eﬃciency. We again point out that there is an immersed normal
surface in ‘cPcbbbadh’ determined by the quadsq0:02:13, q0:03:12, q1:02:13, andq1:02:13 (face 2
is 0(023) = 1(023) ), which maps to an embedded normal torus in ‘dLQacccbgjs’. (Note:
Regina’s labelling routine is diﬀerent from that of the lists in this section.)
