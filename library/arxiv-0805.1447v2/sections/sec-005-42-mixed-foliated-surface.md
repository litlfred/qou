---
doc_id: arxiv-0805.1447v2
doc_title: "Braid ordering and the geometry of closed braid"
section_id: sec-005-42-mixed-foliated-surface
section_title: "Mixed foliated surface"
section_number: 4.2
pages: 12-16
source_pdf: 0805.1447v2.pdf
source_sha256: b7ee20b0a7f5f3da
doc_brief: "Braid ordering and the geometry of closed braid — The relationships between braid ordering and the ge- ometry of its closure is studied."
---
case. The strategy is almost the same as tiled case, but we need to
do some additional arguments to evaluate valance of vertices beca use
the decomposition by regions do not determine cellular decomposition .
First we see the same conclusion of lemma 2 holds.
Lemma 3. Let F be a mixed foliated essential genus g(⁄= 0) closed
surface in the complement of closed braid ˆβ . If β contains a valance v
vertex, then [β ]D < v
2 + 1.
Proof. Let p be a valance v vertex. We can use the same arguments
appeared in proof of lemma 2. The main diﬀerence is a presence of
c-circles and bc-singularity around p. First we modify closed braid as
in the proof of lemma 2 so that we can consider sub-braiding in each
interval [θi − ε, θ i + ε], [ θi + ε, θ i+1 − ε]. Assume that singular point in
the ﬁber Hθ2 is bc-singularity. Then by taking appropriate conjugation
of sub-braiding [ θ1 + ε, θ 3 − ε], bc-singularity is now modeled as in the
ﬁgure 7. Then braiding in the interval [ θ1 + ε, θ 3 − ε] can be written
as shown in ﬁgure 8, which contains only one σ ±1
1 . Thus, the same
argument of the proof of lemma 2 gives desired estimation.
BRAID ORDERING AND THE GEOMETRY OF CLOSED BRAID 13
/C8/CB/CU/D6/CP/CV /D6/CT/D4/D0/CP
/CT/D1/CT/D2 /D8/D7
/A1 /A1 /A1/A1 /A1 /A1/A1 /A1 /A1
Figure 7. Model of bc-singularity
/C8/CB/CU/D6/CP/CV /D6/CT/D4/D0/CP
/CT/D1/CT/D2 /D8/D7
/AI
/BD
/B7 Ꜽ
/AI
/BE
/AI
/BF
/A0 Ꜽ
Figure 8. Braiding in [ θ1 + ε, θ 3 − ε]: bc-singularity case
□
Then, we want to estimate the minimal valance of vertices. Since
there might be all types of singularity in the foliation of F , in gen-
eral decomposition into regions dose not deﬁne usual sense of cellu lar
decomposition: bc-region is annulus, and cc-region is pair of pants.
However, in special case of normal mixed foliation, deﬁned below, on e
can constructs canonical cellular decomposition via decomposition in to
regions as shown in [BM2]. First we describe this.
We say mixed foliation is normal if there exists no cc-singularity. In
normal mixed foliation case, we can construct canonical cellular de-
composition as follows. First we see that in normal mixed foliation,
bc-annuli always occur in pairs. This is because the c-circle boundar y
of bc-annuli must be attached to c-circle boundary of another bc -annuli,
since there is no cc-regions and boundary of bb-tile are all b-arcs. Now,
take annulus W obtained by attaching two bc-annuli along their c-circle
boundaries. Each component of ∂W has two vertices. By cutting W
14 TETSUYA ITO
along the arc which connects two vertices which lies diﬀerent compo-
nents of ∂W , as shown in ﬁgure 9, we obtain two 2-cells, called be-tile.
These cutting arcs are called e-edge. Now decomposition into be-tile
and bb-tile determines cellular decomposition of F .
Figure 9. Construction of be-tile
Note that there might exist be-tile which has no singular point or
two singular points, but from construction of be-tile, be-tile with ze ro
singularity and be-tile with two singularity must occur in pairs in each
neighbor of vertex, so the notion of vertex and valance deﬁned in s ection
3 coincide with the usual meaning of vertex and valance in this cellular
decomposition. Then we see the same Euler characteristic formula
holds:
Lemma 4. Let F be a normal mixed foliated surface with genus g ⁄= 0
and V (v) be a number of vertex whose valance is v in cellular decom-
position described above. Then,
3∑
v=1
(4 − v)V (v) + 8g − 8 =
∞∑
v=4
(v − 4)V (v)
holds.
Proof. A be-tile has exactly four 1-cells in its boundary and each 1-cell
is boundary of two 2-cells, so the same argument in proof of lemma 1
gives desired result. □
So we can estimate minimal valance of vertices in case of normal
mixed foliation by using lemma 4 as in the tiled case. To estimate
general mixed foliated case, we perform ”preimage surgery” to de lete
cc-singularities. Let F be a mixed foliated surface and we denote F by
BRAID ORDERING AND THE GEOMETRY OF CLOSED BRAID 15
the preimage of F ; that is, F is a foliated surface forgetting information
of embedding.
Let c be an one of the c-circle boundary of cc-pants P . c is also a
boundary of some other cc-pants or bc-annulus Q. We modify folia-
tions of P and Q as shown in ﬁgure 10 by ﬁlling c by discs and changes
foliation in P and Q, according to type of regions. Since modiﬁed
regions are trivially foliated, these regions are amalgamated to some
other regions and they disappears. Moreover, this operation can be
done so that obtained surface is connected by choosing c-circle bo und-
ary c appropriately and reduces genus of F because all c-circle in the
foliation is non-null homotopic in F . Thus, this modiﬁcation deletes
two regions P and Q, hence two singular points. We call this operation
preimage surgery because we can regard this modiﬁcation as surgery of
F along c-circle c. We remark that preimage surgery is not realizable
as a surgery of embedded surface F , because we cannot choose take a
disc bounded by c without intersecting original surface F in S3.
Since each preimage surgery reduces a genus of F , after k ≤ g preim-
age surgery we obtain normal mixed foliated surface F ′. As we re-
marked before, F ′ cannot be realized as an embedded surface, but we
can use the arguments of proof of lemma 4, because the proof use s only
information from cellular decomposition of F ′. Therefore we can use
lemma 4 for F ′ to estimate valance of vertices of preimage-surgered
surface F ′.
bc-annulus
cc-pants
surgery
surgery
preimage
preimage
Figure 10. Preimage surgery
16 TETSUYA ITO
Proof of Theorem 1(2)(3). Assume F is mixed foliated and after per-
forming preimage surgery k-times described above, we create abstract
foliated surface F ′ with no cc-singularity, that is, normal mixed foli-
ated. Let m be a minimal valance of vertices of F ′. Then, we trace
preimage surgery procedure backwards. Each surgery deletes a t most
one bc-singularity, so original surface F has at most more than k bc-
singular points than that of F ′. Since singular leaf containing bc-
singularity has two vertices as its endpoints and there exist at least
two vertices in F , we conclude minimal valance of vertices in F is
smaller than m + k. Thus, we only need to estimate m to estimate
minimal valance of vertices in original surface F .
Let V (v) be the number of valance v vertices of F ′. If V (i) is non-
zero for some 1 ≤ i ≤ 3, then form the argument above, we conclude
the minimal valance of vertices of F is smaller than 3 + g, so [ β ]D <
3+g
2 ≤ 2g + 1, so we can assume V (i) is zero for all 1 ≤ i ≤ 3. In this
case, the Euler characteristic formula for F ′ become
8(g − k) − 8 >
∞∑
i=4
(v − 4)V (v).
Mixed foliated means there exist at least one b-arc in the foliation, so
there exist at least two vertices in F ′. Therefore the minimal value
of valance of vertices in F ′ is less than 4( g − k). Therefore, from
our earlier argument, minimal valance of vertices in F is smaller than
4(g − k) + k = 4 g − 3k + 1. Now, lemma 3 establishes an inequality
[β ]D < 2g − 3k
2 < 2g + 1.
From statement (1) and (2), we conclude if [ β ]D ≥ 2g + 1, then F is
neither tiled nor mixed-foliated, hence circular-foliated. This comple tes
proof of theorem 1 □
