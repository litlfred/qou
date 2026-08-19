---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO"
section_id: sec-015-33-using-braid-foliations-to-detect-destabilizat
section_title: "Using braid foliations to detect destabilizations and exchange moves"
section_number: 3.3
pages: 34-37
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS JOAN S BIRMAN WILLIAM W MENASCO — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
In this section we will show how to recognize, from the foliation of F, when a closed
braid admits a destabilization or an exchange move.
Destabilizations are easy. It is shown in [ 4] that X+ admits a destabilization if the
foliation has a vertex of valence 1, as in Figure 22(a). The embedding of a tile which
contains the vertex of valence 1, for one of the two possible choices of the sign of the
singularity, is illustrated in sketch (b).
+ + +
X
X
(a)
(b)
new X
new X
v v w
w
v
v
Figure 22: Destabilization along a valence 1 vertex, viewed (a) on the foliated surface and (b) in
3–space
Lemma 3.3.1 Destabilizations which are predicated on the existence of a valence 1
vertex reduce the number of singularities (resp. vertices) in the foliation of F by 1 (resp.
1).
Proof Clear. See Figure 22(a).
Before we can describe our exchange moves, a new concept is needed. We observe that,
intuitively, b–arcs in the foliation of F arise when there are ‘pockets’ in the surface,
and we are now interested in the case when a ‘pocket is empty’ and so can be removed.
We now make this precise. A b–arc β in the foliation is an inessential b–arc if it joins
a pair of vertices v, w which are consecutive vertices in the natural cyclic ordering of
vertices along A. We use the term ‘inessential’ because, if we think of a ﬁberHθ of H
as a disc with the braid axis A as its boundary, then an inessential b–arc will cut off a
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 447
disc ∆⊂ Hθ which has the property ∆∩ F =β . The disc ∆ cannot be pieced by X,
for if it were there would be an a–arc α which either intersected our inessential b–arc,
which is impossible because F is embedded, or α has a vertex endpoint between v and
w, which is impossible because v and w are consecutive vertices on A. The disc ∆
can be used to push β (and nearby leaves in nearby disc ﬁbers) across A, reducing the
number of vertices in the foliation of F. Peek ahead to the right sketch in Figure 24 for
examples of b–arcs which are inessential and also essential. An essential b –arc is one
which is not inessential.
Exchange moves were deﬁned in Figure 2 as a move on a block-strand diagram. Our
task now is to detect them in the foliation. The complexity function mentioned in
Theorem 2 will include the number of singularities in the foliation of a clasp annulus
which is bounded by the given braids. As will be seen shortly, exchange moves always
reduce this complexity function. However, the exchange moves that are used in this
paper come in two ﬂavors, and it’s necessary to check both.
The ab–exchange move: In Figure 23(a) we have illustrated v, a type ab valence 2
+
-
-
+
(a)
(b)
Xw
vq
s
p
t
α
new Xα′
A
α X
X
v
w
A
α′
X
new X
Figure 23: The type ab–exchange move
vertex. The left and right sketches in (a) (resp. (b)) show the conﬁgurations on the
foliated surface F (resp. in 3–space), the left sketches being before and the right sketches
being after the exchange move. In both (a) and (b) the vertex v is adjacent to two type
ab singularities, and these singularities have opposite signs. The ab–exchange move
occurs in the passage from the left to the right sketch. One pushes the subarc α⊂ X
across the shaded disc to α′. If we choose α′ so that it is everywhere transverse to
Geometry &Topology 10 (2006)
448 Joan S Birman and William W Menasco
leaves of the foliation (as is clearly possible) the move takes closed braids to closed
braids. Figure 23(b) illustrates the embedding for one particular choice of signs and
orderings.
Note that if the b–arcs which end at the vertex v are all essential, then X must encircle
the subarc vw of the braid axis which is inside the pocket. The braid changes we make
can then be understood by looking at the projection onto a plane orthogonal to the braid
axis. After the exchange move the shaded disc will have vanished. Peering down the
braid axis (as we did in Figure 2) we see that the projection has changed in the predicted
manner. For full details, consult [4].
The bb–exchange move: In Figures 24 and 25 we have illustrated v, a type bb valence 2
vertex. The non-singular leaves which have an endpoint at v are all type b. The left and
right sketches show the changes in 3–space. The changes in the braid projection can be
understood by looking down the axis onto a plane orthogonal to the braid axis. The
A
X
X
X
k
v
w
m
u
A
X
X
u
k+m
∆(θ)
X
X
Hθ
inessential b–
arcβ(θ)
essential
b–arcβ′(θ)
Figure 24: The type bb–exchange move, followed by an isotopy of F
foliation does not change at all after a bb–exchange move, however there is a change in
the order of the vertices along the braid axis. The ‘pocket has been emptied’ and after
the exchange move, the empty pocket can be collapsed by pushing every b–arcβ(θ)
across its disc ∆(θ), as in Figure 25. Remark: The pocket could of course have much
more complicated braiding inside it. The proof that it can always be emptied in this
way is non-trivial; details may be found in our earlier paper [7] or the article by Birman
and Finkelstein [4]. The passage from the left to right sketches in Figure 25 shows the
change in the foliation, after the removal of all inessential b–arcs.
Lemma 3.3.2 Suppose that the foliation of F has a vertex v of valence 2 and type ab
or bb. Assume that the adjacent singularities have opposite signs. Then the closed
braid X =∂F admits an exchange move. After the move, there is a surface F
′
, isotopic
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 449
++
+− +
-
p′
pq
s
v w1w2
p′
pw2
Figure 25: Changes in foliation after the removal of inessential b–arcs
to F, with a decomposition containing two fewer vertices and two fewer singularities
than the decomposition of F.
Proof See Figures 22(a), 24 and 25.
