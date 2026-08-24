---
doc_id: 0310279v5
doc_title: "Stabilization in the braid groups I: MTWS"
section_id: sec-013-31-braid-foliations-of-seifert-surfaces
section_title: "Braid foliations of Seifert surfaces"
section_number: 3.1
pages: 26-30
source_pdf: 0310279v5.pdf
source_sha256: a1d472d37291a333
doc_brief: "Stabilization in the braid groups I: MTWS — 30 sections: Introduction; The problem; Block-strand diagrams and template"
---
We are given X∈B (X ) with b(X) = n and with braid structure (A, H) in R3. To make
this review as simple as possible, we assume that X is a knot. Choose a Seifert surface
F of minimal genus for X. After modifying F we will show that it supports a special
type of singular foliation which was studied and used by the authors in [8]–[10]. We
call it a braid foliation.
There are choices of orientation which determine the sign conventions in braid foliations.
First, we assign the standard orientation to R3 and choose the braid axis A to be the
positively oriented z–axis. Using cylindrical coordinates, this determines a sense of
increase of the polar angle coordinateθ. Next, the closed braid X is oriented so that it
points in the direction of increasingθ at each point of X∩ Hθ . The orientation on X
induces an orientation on F, and so determines a positive normal at each interior point
on F.
Since X = ∂F is a closed braid, A∩ F is non-empty. The intersections of H with
F may be assumed to be (a) radial in a neighborhood of each point of A∩ F and (b)
transverse to the boundary in a neighborhood of∂F. See Figure 15.
Vertices in the foliation are points where A pierces F. We call a vertex positive or
negative, according asA intersects F from the negative or positive side ofF respectively.
The sketches in Figure 15 illustrate the positive side of F, so that the ﬂow induced by
the ﬁbration is anticlockwise (resp. clockwise) about a positive (resp. negative) vertex.
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 439
A
+ vertex − vertex
viewed on the surface
+ side
of surface
− side
of surface
viewed in 3–space near the boundary
(a) (b)
Figure 15: (a) Foliation of surface near a vertex (b) Foliation of surface near the boundary
Singularities in the foliation occur at points where F is tangent to one of the ﬁbers of
H. The singularities may be assumed to be ﬁnite in number and to occur on distinct
ﬁbers of H. By Morse’s classiﬁcation theorem every singularity may be assumed to
result from a local maximum or minimum or a saddle point tangency between F and
a ﬁber of H. Let s be a singular point of the foliation of F, and let Hθ be the disc
ﬁber which contains s. We say that the singularity s is positive if the outward-drawn
oriented normal to the oriented surface F coincides in direction with the normal to Hθ
in the direction of increasingθ. Otherwise s is negative.
Leaves in the foliation are components of intersection of Hθ with the surface F. A
singular leaf is a leaf which contains a singularity of the foliation. Every other leaf is a
non-singular leaf.
A very basic property of our braid foliations of Seifert surfaces is that non-singular
leaves may all be assumed to be arcs. We review the reasons (which goes back to
Bennequin [2]). Suppose that there is a simple closed curve α(θ) in F∩ Hθ for some
non-singular polar angleθ. The fact that F is pierced non-trivially by the braid axis, and
that the foliation is transverse to the boundary, shows that F cannot be foliated entirely
by simple closed curves, so if we follow the sequence of arcs α(θ) as θ increases or
decreases we must arrive at a singularity. Let Hθ0 be the singular ﬁber. The singularity
may be assumed to be either be a center or a saddle point, but if it is a center, then by
followingα(θ) in the opposite direction we will arrive at another singularity, and that
one cannot also be a center because F is not a 2–sphere, so it must be a saddle point,
and the singularity must be a homoclinic point (a singularity which is formed when
a generic leaf has a saddle point singularity with itself), as illustrated in Figure 16(a).
Note that the singular leaf α(θ0) lies in both F and Hθ0 , and necessarily bounds a disc
∆ in the latter. Assuming that ∆ is innermost, we surger F along ∆ as in Figure 16.
Geometry &Topology 10 (2006)
440 Joan S Birman and William W Menasco
(a)
(b)
surgery + isotopy
surgery + isotopy
∆(θ0)
α(θ0)
Figure 16: In this sketch the ﬁbers of H are to be thought of as horizontal planes. (a) Surgering
F along the disc ∆ removes the singularity. (b) The change in foliation on F.
The surgered surface has two components. By assumption F has maximal Euler
characteristic, which implies that one of the two components is a 2–sphere. Discarding
it, and smoothing the new F, we can eliminate the singularity.
It remains to consider the case when the interior of the disc ∆ intersects F. Since s0 is
the only singularity in Hθ , there are no singularities in the interior of ∆. But then each
component of F∩ int(∆)⊂ Hθ must be a simple closed curve. Let c be an innermost
such simple closed curve. Then we can surger F along c, and then smooth the surgered
surface by an isotopy. This will introduce center singularities but no additional saddles.
Any S2′s that are formed we discard. (We leave it to the reader to draw appropriate
pictures). After a ﬁnite number of such surgeries we obtain a new surface F′ which
has the same homoclinic point in its foliation, but does not meet the disc ∆. We then
do the surgery which is illustrated in Figure 16, reducing the number of saddle point
singularities. In this way all leaves which are simple closed curves can be eliminated.
Since each non-singular leaf is an arc, one of its endpoints could either be at a vertex
of the foliation or a point on the boundary, however we now claim that non-singular
leaves which have both endpoints on the boundary do not occur. For, suppose there
is a leaf l which has both endpoints on the boundary. Let N(l) be a neighborhood of
the leaf on F. Thinking of N(l) as a rectangle, it will have a pair of opposite edges on
the boundary, and the orientation on these edges will be consistent with the orientation
on N(l). However, l also lies in a ﬁber Hθ of H, and the boundary of F is a closed
Geometry &Topology 10 (2006)
Stabilization in the braid groups I: MTWS 441
braid. But then, the orientation on one of the edges of N(l) will agree with that of the
normal to Hθ and (since l is by hypothesis non-singular) the orientation of the other
must disagree with the that of the normal, but that is impossible because the boundary
curve is a closed braid.
It follows from this that the non-singular leaves have two types: those which have one
endpoint on the boundary and the other at a vertex (we call them a–arcs) and those
which have both endpoints being vertices of the foliation (we call them b–arcs). See
Figure 17.
A
A A
X
a b
+
+ −
Figure 17: Non-singular leaves in the foliation of F
Singularities fall into three types, which we call types aa, ab and bb, the notation
indicating that just before an aa–singularity (resp. ab, bb–singularity) the non-singular
leaves were both type a (resp. types a and b, resp. both type b). We shall refer to the
2–cells which are foliated neighborhoods of the singular leaves as ‘tiles’. See Figure 18.
1
2
3
4
−
−
+ + s
type bb
1 3
4
s+ +
−
type ab
X
1 3
s+ +
X
X
type aa
Figure 18: Tiles of type bb, ab, aa
The foliation may be used to decompose the surface F into a union of foliated 2–cells,
each of which contains exactly one singularity of the foliation. Each 2–cell is a regular
neighborhood on F of a singular leaf. These foliated 2–cells are our tiles and the
resulting decomposition of F is a tiling. See the three sketches in Figure 18. The tile
Geometry &Topology 10 (2006)
442 Joan S Birman and William W Menasco
vertices are the points where the braid axis A intersects the surface F. (There are also
other vertices on∂F, but we prefer to exclude them when we refer to tile vertices.) The
tile edges are arbitrary choices of a–arcs or b–arcs. (There are also other tile edges
which are subarcs of X, but it will be convenient to ignore those, just as we ignored the
vertices which are on X.)
Assume that the vertices and singularities in the braid foliation of F have been labeled.
The combinatorial data which is associated to the foliation is a listing of the signed
vertices, in the natural cyclic order in which they occur on A, and a listing of the
signed singularities, in the natural cyclic order in which they occur in the ﬁbration. The
following proposition is very natural, because leaves in the foliation of F are level sets
for the embedding of F:
Proposition 3.1.1 (Birman–Menasco [10], Birman–Finkelstein [ 4, Theorem 4.1])
Let T be any tile in the braid foliation of F. Label the vertices and singularities of
T by their signs and their cyclic orders as above. Then this decorated braid foliation
determines the embedding of T . More globally, the embedding of all of the aa and ab
tiles in the foliation of F determines the embedding of X in R3\ A.
We illustrate in Figure 19 the embeddings of the three tiles in Figure 18, for one of the
ﬁnitely many choices of the combinatorial data on these tiles.
A A A
X
X
X
s
s s
1
1 1
2 2
3
3 34
type bb type ab type aa
Figure 19: Embeddings of tiles of type bb, ab, aa in 3–space
