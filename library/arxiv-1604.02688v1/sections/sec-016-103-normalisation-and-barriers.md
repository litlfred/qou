---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-016-103-normalisation-and-barriers
section_title: "Normalisation and barriers"
section_number: 10.3
pages: 30-34
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
[Kne29] for ‘normalisation’ of an embedded closed surfaceS in a triangulationT of a manifold
M. We can assume initially that the surfaceS is transverse to the triangulation.There are
ﬁve basic moves:
(1) Compress S along an embedded diskD in the interior of a tetrahedron∆, which
meets S in C = ∂D, where eitherC is essential inS or a disk bounded byC in S
meets ∂∆.
(2) Isotope a diskD′ of intersection ofS with a tetrahedron across a face of the tetrahe-
dron, where∂D′ lies in a face and is an innermost curve in that face.
THE 3D-INDEX AND NORMAL SURF ACES 31
(3) Isotope an innermost arc of intersection ofS with a face of the triangulation across
an edge. Here the arc has both ends on the edge and there are no intersections ofS
with the bigon cut oﬀ by the arc in the face.
(4) Boundary compress the intersection ofS with a tetrahedron. This occurs along a
bigon which intersectsS in one arc of its boundary with the other arc contained in
an edge of the tetrahedron.
(5) Finally, any component which is a sphere contained in the interior of a tetrahedron
is removed.
Kneser [Kne29] and Haken [Hak61b] show that any surface can either be normalised,
i.e. either converted to a non-empty normal surface by a sequence of such moves, or else
converted to the empty surface.
Remark 10.11. If an embedded sphereS or an embedded torusT is converted to the empty
surface when normalised in one of its complementary regions, then that region is a 3-ball or
solid torus inM bounded byS or T respectively.
In fact, ifS orT did not bound a 3-ball or solid torus respectively then there is no isotopy
or a disk compression followed by an isotopy, shrinkingS or T respectively to a point.
Deﬁnition 10.12.An embedded surface S′ is a barrier for the normalisation of S if it
satisﬁes the following conditions. Firstly,S′∩S =∅. Secondly, S can be normalised by
moves in the complement ofS′.
Theorem 10.13. Let T be an ideal triangulation of compact manifold with boundary con-
sisting of tori. Suppose that S′ is a “simple” embedded generalised normal surface inT,
i.e. has at most one generalised normal disk in each tetrahedron. ThenS′ is a barrier for
normalisation of any surface in its complement.
Proof. Consider the two regionsR,R′ obtained by splitting a tetrahedron∆ open along a
generalised normal diskD in S′. The faces of these regions consist of a copy ofD and the
result of splitting the faces of∆ open along∂D. The latter produce faces which are either
triangles, quadrilaterals or pentagons. (Hexagons cannot arise since a generalised normal
disk has at most two diﬀerent arc types in any triangular face of∆.)
Choose a maximal family of disjoint non parallel properly embedded bigon compressing
disks for each of the regionsR,R′, as in the fourth normalisation move. Thus, a quadrilateral
face ofR or R′ has two associated bigon disks, one along each edge of∆ in its boundary,
whereas a pentagon has one such bigon. (Figure 10 exhibits the case whereD is a 12-gon,
with ∂∆ stereographically projected to the plane.)
If either region is compressed along all these disks, each of the resulting components is
either a tetrahedron, where the compression ofD gives a face of the tetrahedron, or a 3-ball
with boundary a pair of disks, where one disk is the result of compressingD and the other
disk is in a face of∆.
Suppose thatS is a surface disjoint fromS′. If S meets either regionR,R′, then notice
that the intersection ofS with the above families of bigon disks can be used to perform
normalisation moves onS in the complement ofS′. For if there is a loopC inS∩Di where
32 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
Figure 10. (left) A schematic diagram of the 12-gon determined by coordi-
nates (2, 1, 0). (right) An embedding of this 12-gon. The regionR faces the
dark (red) shaded side, whileR′ faces the lighter side.
Di is one of the bigon disks and eitherC is essential onS or a disk bounded byC in S
meets ∂∆, then this gives a ﬁrst normalisation move. On the other hand, if there are arcs
in S∩Di, these give third or fourth normalisation moves.
After performing all such normalisation moves, the resulting surface again denoted byS
is still disjoint fromS′ but also from all the bigon disks inR,R′. It is easy to see that we
can perform additional ﬁrst or second normalisation moves so thatS∩ ∆ consists entirely of
triangular normal disks and spheres in interior∆and after discarding any sphere components
we have normalisedS in ∆.
This argument can clearly be performed in all tetrahedra containing a generalised normal
disk, and in tetrahedra containing only normal disks, the argument in [JR03] applies. This
completes the proof. □
Corollary 10.14. If S∗ is a two-sided embedded “simple” generalised normal surface (i.e.
has at most one generalised normal disk in each tetrahedron), then it can be pushed oﬀ itself
to either side and normalised in its complement.
Remark 10.15. If we consider an arbitrary generalised normal surfaceS∗ which is not nec-
essarily simple, the same idea shows that any surfaceS in the complement ofS∗ can be
transformed into ageneralised normal surface, by moves similar to the ones above for nor-
malisation. The diﬀerence in this case is that ifS∗ has parallel generalised normal disks
bounding a product regionR in a tetrahedron andS meetsR, thenS might be transformed
to intersectR in parallel copies of these generalised normal disks.
Theorem 10.16.Let T be a 1-eﬃcient ideal triangulation of a cusped, orientable 3-manifold
M, and assume thatM is not a solid torus orT 2×I. Then T contains no closed embedded
simple generalised normal surface˜S with χ( ˜S)≥ 0.
Proof. Recall that T 1-eﬃcient implies thatM is irreducible and atoroidal. Suppose ﬁrst
that ˜S is two-sided inM. Now by the barrier argument in Corollary 10.14, we can push the
simple generalised surface˜S oﬀ itself on either side, and normalise it. The result is either (i)
a normal sphere, or (ii) a normal torus, or else (iii) the surface becomes empty.
THE 3D-INDEX AND NORMAL SURF ACES 33
The ﬁrst case clearly contradicts the assumption of 1-eﬃciency.
In the second case, note that the surface may normalise to a peripheral torus at a cusp
when it is pushed oﬀ itself to a side containing a cusp. Since we are assuming thatM is
not T 2×I, it follows that normalisation to a peripheral torus cannot occur on both sides
of a generalised normal torus. But then, pushing oﬀ to at least one side, we would get a
normal torus which is topologically but not normally parallel into a cusp, again contradicting
1-eﬃciency.
So we are left with the case that the surface becomes empty. If˜S is a sphere, it cannot
bound a ball on both sides and hence yields a normal sphere on one side or the other by
Remark 10.15, contrary to assumption.
If ˜S is a torus, it could be compressible. In this case, the torus bounds a solid torus or
cube-with-knotted-hole. In the latter case, the sphere resulting from compressing˜S does not
bound a ball in the complement of˜S so can be normalised giving a normal sphere, contrary
to assumption. So we are left with the ﬁnal case, where˜S is a torus bounding a solid torus.
The other side of ˜S must contain a cusp ofM. But then if ˜S is compressible on this side,
the result is a sphere which can be normalised, contradicting the assumption of 1-eﬃciency.
On the other hand, if˜S is incompressible on the side containing a cusp, either˜S normalises
to give a non-peripheral normal torus, contrary to 1-eﬃciency, orM is a solid torus, which
is excluded by our hypothesis. So the case where˜S is two-sided is complete.
If the generalised normal surface ˜S is one-sided it is a projective plane or Klein bottle.
The ﬁrst case contradicts irreducibility. If ˜S is a Klein bottle, the boundary of a small
regular neighbourhood of ˜S is either an incompressible torus, contradicting the atoroidal
assumption, or compressible andM is a closed prism manifold, contradicting the hypothesis
that M has a cusp. This completes the proof. □
Lemma 10.17.Let T be a 1-eﬃcient ideal triangulation ofM, which is either a solid torus
or T 2×I. Then T contains no closed embedded simple generalised normal surface˜S with
χ( ˜S)> 0, and no closed embedded normal surface˜S with χ( ˜S) = 0 which is non-peripheral.
However, T always contains a closed embedded generalised normal˜S with χ( ˜S) = 0. In fact,
there is an almost normal torus˜S containing one octagonal disk.
Proof. If there was a simple generalised normal surface˜S withχ( ˜S)> 0, then ˜S would be a
sphere or projective plane. A projective plane can be normalised and in the case of a sphere,
˜S could be normalised to the side which was not a ball. Both cases contradict 1-eﬃciency.
Similarly there cannot be a non-peripheral normal surface˜S with χ( ˜S) = 0 for the same
reason.
By a standard sweepout argument, starting with a peripheral normal torus at a cusp and
sweeping to a core circle or the other cusp, there must be an intermediate almost normal
torus ˜S - see Rubinstein [Rub97] or Stocking [Sto00]. If˜S was obtained by attaching a tube
to a normal sphere, this would contradict 1-eﬃciency. Hence˜S must have one octagonal
disk as claimed. □
Remark 10.18. The proof of Theorem 10.16 shows that a 1-eﬃcient triangulationT of a
closed orientable 3-manifoldM other thanS3 or a lens spacecontains no closed embedded
simple generalised normal surface ˜S with χ( ˜S)≥ 0. (Here 1-eﬃcient means there are no
34 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
embedded normal spheres, projective planes, Klein bottles or tori, except for vertex linking
spheres and edge linking tori. The former are boundaries of a small regular neighbourhood
of a vertex, and the latter are obtained similarly from an edge which is a loop.)
Corollary 10.19.Let T be a 1-eﬃcient ideal triangulation of a manifoldM other than the
