---
doc_id: bsmf-2002-130-3-457-0
doc_title: "Bull. Soc. math. France 130 (3), 2002, p. 457–491 HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE by Xiliang Bao & Francis Bonahon"
section_id: sec-007-5-convergence-of-hyperideal-polyhedra
section_title: "Convergence of hyperideal polyhedra"
section_number: 5
pages: 25-32
source_pdf: BSMF_2002__130_3_457_0.pdf
source_sha256: 63f79235d0c13ba8
toc_source: inferred
---
We showed in Theorem 11 that the map Θ : PΓ →KΓ ⊂RE, which to a
hyperideal polyhedron associates its dihedral angles, is a local homeomorphism.
This section is devoted to proving that it is a covering map.
Recall that KΓ was deﬁned as the set of those θ ∈RE such that:
0) For every e ∈E, the coordinate θe of θ corresponding to e is in the
interval ]0, π[;
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
482
BAO (X.) & BONAHON (F.)
1) For every closed curve γ embedded in Γ and passing through the edges
e1, e2, . . . , en of Γ, !n
i=1 θei ≤2π with equality allowed only when γ is the
boundary of a face of S2 −Γ.
2) For every arc γ embedded in Γ, passing through the edges e1, e2, . . . ,
en of Γ, and joining two distinct vertices which are in the closure of the same
component of S2 −Γ but such that γ is not contained in the boundary of that
component, !n
i=1 θei < π.
Proposition 21. — The map Θ : PΓ →KΓ is proper.
Proof. — Since KΓ is locally compact and PΓ is metrizable, it suﬃces to prove
the following: If Pn ∈PΓ, n ∈N, is a sequence such that Θ(Pn) converges to
some θ∞∈KΓ, then there is a subsequence Pnk, k ∈N, which converges to a
polyhedron P∞∈PΓ.
Consider such a sequence Pn ∈PΓ, n ∈N.
As usual, we use the same
symbol Pn ∈%PΓ to denote a hyperideal polyhedron representing the class
Pn ∈PΓ, and we let P Proj
n
be the projective polyhedron associated to the
polyhedron Pn. Let xn = Φ(Pn) ∈(RP3)V be the vertex set of P Proj
n
. Pick
three consecutive vertices v1, v2, v3 ∈V on the boundary of a face f of the
model polyhedron P Proj
0
.
After modifying Pn by an element of PO(3, 1) if
necessary, we can arrange that the corresponding vertices xn
v1 and xn
v2 of P Proj
n
sit on the closure of the axis R × {0} ⊂R3 in RP3 while the vertex xn
v3 is in
the closure of the plane {0} × R2 in RP3. By compactness of RP3, we can also
assume after passing to a subsequence that xn converges to x∞∈(RP3)V .
For each face f ∈F, the corresponding face f n of P Proj
n
is contained in a
projective plane Πn
f of RP3. After passing to a subsequence, we can assume
that the plane Πn
f converges to a plane Π∞
f
for each f ∈F. By construction,
the limit plane Π∞
f
meets the closure of H3 in RP3. In particular, either it
meets H3 or it is tangent to the sphere at inﬁnity ∂∞H3.
Similarly, for an edge e ∈E joining two vertices v, v′ ∈V , let en be the
corresponding edge of P Proj
n
. Among the two line segments joining the vertices
xn
v and xn
v′ of P Proj
n
in RP3, en is also the one that meets H3. As n tends to ∞,
en converges to a line segment e∞which joins x∞
v to x∞
v′ and which meets the
closure of H3 (after passing to a subsequence if by any chance x∞
v = x∞
v′ ).
Note that the limit edge e∞could conceivably be reduced to a single point.
We ﬁrst prove that this does not happen.
Lemma 22. — There is no edge e ∈E such that the corresponding limit edge
e∞is reduced to a single point.
Proof of Lemma 22. — Suppose otherwise, and that there is a point p ∈RP3
such that Ep = {e ∈E; e∞= p} is non-empty. Note that p must be on the
sphere at inﬁnity ∂∞H3. Indeed, it must be in the closure of H3 since each en
meets H3, but cannot be in H3 since the end points of en are outside H3.
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
483
Consider the vertices v1, v2 and v3 which we selected at the beginning of
the proof of Proposition 21. The edge e12 joining v1 to v2 cannot be in Ep,
since the corresponding line segment e∞
12 contains the diameter R × {0} ∩H3.
The edge e23 joining v2 to v3 cannot be in Ep either, because its end points
x∞
v2 and x∞
v3 are distinct since they are respectively contained in the closures
of R × {0} and {0} × R2, which are disjoint. In the boundary of the model
polyhedron P Proj
0
, let Kp be the union of all the edges e ∈Ep. By the above
remark and because e12 and e23 are contained in the same face of P Proj
0
, the
interiors of e12 and e23 are contained in the same component of ∂P Proj
0
−Kp.
Let U be a regular neighborhood of Kp in ∂P Proj
0
, and let γ be a component
of ∂U which is contained in the same component of ∂P Proj
0
−Kp as the interiors
of e12 and e23.
Let e1, e2, . . . , em, em+1 = e1 ∈E be the edges of P Proj
0
traversed by γ, in
this order. Note that γ deﬁnes a closed curve γΓ in the dual graph Γ, crossing
the edges corresponding to e1, e2, . . . , em. This closed curve is not necessarily
embedded, but it is immersed in Γ in the sense that each ei is diﬀerent from ei+1.
Also, by construction, each limit edge e∞
i
has one end point equal to p, but is
not reduced to this point.
Let f1, f2, . . . , fm, fm+1 = f1 be the faces met by γ, so that γ crosses
the edge ei between the faces fi and fi+1. By construction, each of the limit
planes Π∞
fi passes through p.
In R3, the euclidean plane Π∞
fi ∩R3 bounds
a preferred euclidean half-space H∞
fi , namely the limit of the half space Hn
fi
bounded by Πn
fi ∩R3 and containing the polyhedron Pn ⊂H3. The intersec-
tion C of these half-spaces H∞
fi is a convex cone with vertex p, containing the
limit edges e∞
i
in its boundary. In addition, every extremal half-line of C must
coincide with one of the e∞
i
near p.
The intersection of C with a small horosphere S ⊂H3 centered at p is a
polygon QS, possibly non-compact and/or reduced to a subset of a geodesic
of S. Note that the polygon QS is convex for the euclidean metric of S induced
by the hyperbolic metric of H3.
We split the analysis into several cases.
Case 1. None of the limit edges e∞
i
is tangent to ∂∞H3.
In particular, the planes Π∞
fi all meet H3 and deﬁne hyperbolic planes
H3 ∩Π∞
fi . As n tends to ∞, the hyperbolic plane H3∩Πn
fi converges to H3∩Π∞
fi .
The dihedral angle between two such consecutive planes H3∩Πn
fi and H3∩Πn
fi+1
is equal to the coordinate θn
ei of θn = Θ(Pn) ∈RE corresponding to ei ∈E. Be-
cause θn converges to a point θ∞∈KΓ ⊂]0, π[E, the limit θ∞
ei of θn
ei is diﬀerent
from 0 and π. It follows that the two hyperbolic planes H3 ∩Πn
fi and H3 ∩Πn
fi+1
have non-trivial intersection, and that their dihedral angles along this intersec-
tion geodesic is equal to θ∞
ei . Note that the hyperbolic dihedral angle between
the hyperbolic planes H3 ∩Πn
fi and H3 ∩Πn
fi+1 is also equal to the euclidean
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
484
BAO (X.) & BONAHON (F.)
angle between the two lines S∩Πn
fi and S∩Πn
fi+1 in the horosphere S. It follows
that the polygon QS = C ∩S is compact and, as in the proof of Proposition 5,
that !m
i=1 θ∞
ei = 2π.
Because of the hypothesis that θ∞satisﬁes Condition 1 in the deﬁnition
of KΓ, this implies that the closed curve γΓ in Γ deﬁned by γ is embedded, and
bounds a component of S2−Γ corresponding to a vertex v4 ∈V . It follows that
a component W of ∂P Proj
0
−γ contains only one vertex of P Proj
0
, namely v4.
This W cannot be a component of the interior of the regular neighborhood U
of Kp since, by deﬁnition of Kp, each of these components contains at least one
edge of P Proj
0
. Therefore, W must be a component of ∂P Proj
0
−U and meets
the interiors of the edges e12 and e23. As a consequence, the vertex v4 in W
must be equal to v2, and v1 and v3 must be in Kp. However, this would imply
that x∞
v1 = x∞
v3 = p, contradicting the fact that x∞
v1 and x∞
v3 belong to disjoint
subsets of RP3, namely the respective closures of R × {0} and {0} × R2. We
consequently reach a contradiction in the case where none of the limit edges e∞
i
is tangent to ∂∞H3.
Case 2.
Some but not all limit edges e∞
i
are tangent to ∂∞H3, and all
those e∞
i
which are tangent to ∂∞H3 are equal.
Assume that e∞
i
= e∞
i+1 = · · · = e∞
j
are tangent to ∂∞H3 but that e∞
i−1 and
e∞
j+1 are both diﬀerent from e∞
i
= e∞
j . Then, for i < k ≤j, the plane Π∞
fk may
be tangent to ∂∞H3 and in particular have trivial intersection with H3. As a
consequence, we loose any geometric control on the angles θn
ek with i ≤k ≤j.
However, by hypothesis, the two edges e∞
i−1 and e∞
j+1 cannot be tangent
to ∂∞H3. It follows that the two planes Π∞
fi and Π∞
fj+1 intersect the horo-
sphere S in two geodesic lines Π∞
fi ∩S and Π∞
fj+1 ∩S. These two geodesic lines
are parallel since Π∞
fi and Π∞
fj+1 meet along the line containing e∞
i , which is
disjoint from H3. In addition, Π∞
fi ∩S and Π∞
fj+1 ∩S delimit an end of the
polygon QS = S ∩C which is adjacent to the tangent limit edge e∞
i .
The convex polygon QS can have no other end. Indeed, the only possibility
for this would be that the convex cone C locally contains near p a line tangent
to ∂∞H3, contradicting our hypothesis that all those e∞
i
which are tangent to
∂∞H3 are tangent to each other. We conclude that e∞
k
is tangent to ∂∞H3
exactly when i ≤k ≤j. Considering the dihedral angles at the corners of ∂QS
as in Case 1, it now follows that !i−1
k=j+1 θ∞
ej = π, counting indices modulo m.
In the graph Γ, let γ′
Γ be the part of the immersed curve γΓ which crosses the
edges ej+1, ej+2, . . . , ei−1. Because !i−1
k=j+1 θ∞
ej = π and because θ∞satisﬁes
Condition 1 in the deﬁnition of KΓ, the arc γ′
Γ is actually embedded in Γ.
For i ≤k < j, the limit edges e∞
k and e∞
k+1 are equal and tangent to ∂∞H3
at p. If we orient the edges ek and ek+1 by the outer normal orientation of
∂U along γ, we conclude that they must end on the same vertex v of P Proj
0
.
(Otherwise, an edge of the face f n
k+1 of P Proj
n
would be unable to meet H3).
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
485
As a consequence, the faces fi and fj+1 share this vertex v ∈V . In particular,
the end points of γ′
Γ (namely the vertices of Γ respectively corresponding to
fi and fj+1) are contained in the closure of the same component A of S2 −Γ,
namely the component corresponding to v ∈V . Since θ∞satisﬁes Condition 2
in the deﬁnition of KΓ and since !i−1
k=j+1 θ∞
ej = π, we conclude that γ′
Γ is
contained in the boundary of A. But this implies that the closed curve γΓ is
equal to the boundary of the component A of S2 −Γ. We already saw in Case 1
that this is impossible, as this leads to a contradiction.
Case 3. Some but not all limit edges e∞
i
are tangent to ∂∞H3, and at least
two of the e∞
i
which are tangent to ∂∞H3 are diﬀerent.
The convex polygon QS = S ∩C in the horosphere S is non-compact since
some e∞
i
is tangent to ∂∞H3. On the other hand, the hypothesis that there
exists an e∞
j
which is not tangent to ∂∞H3 provides a corner of ∂QS where
the external dihedral angle is at least θ∞
ej > 0. It follows that the boundary
∂QS is non-empty and connected. There consequently exists indices i1, i2 such
that the limit edge e∞
i
is tangent to ∂∞H3 if and only if i1 ≤i ≤i2, counting
indices modulo m.
If e∞
i
and e∞
i+1 are tangent to ∂∞H3, either e∞
i
= e∞
i+1, or e∞
i
and e∞
i+1 are
collinear and point in opposite directions at p. Indeed, this immediately follows
by consideration of the possible limits for the face f n
i+1, using the fact that it
is a convex polygon and that each of its edges must meet H3. (There are two
cases, according to whether Π∞
fi+1 is tangent to ∂∞H3 or not). If e∞
i
and e∞
i+1
pointed in opposite directions at p, this would provide a geodesic line which is
completely contained in the convex polyhedron QS, which is incompatible with
the fact that ∂QS has a corner with strictly positive external dihedral angle.
Therefore e∞
i
= e∞
i+1 for all i1 ≤i < i2. But this contradicts the hypothesis
that there are at least two diﬀerent e∞
i
which are tangent to ∂∞H3.
Case 4. All the limit edges e∞
i
are tangent to ∂∞H3.
In particular, the boundary ∂QS has no corners, and consists of 0, 1 or 2
parallel geodesic lines. As a consequence, there can be at most two indices i
such that Π∞
fi is not tangent to ∂∞H3.
For each i, either e∞
i
= e∞
i+1, or e∞
i
and e∞
i+1 are collinear and point in
opposite directions at p; in addition, if we orient the edges ei and ei+1 by
the outer normal orientation of ∂U along γ, their terminal end points must
necessarily be equal in the ﬁrst case, and distinct in the second case. Again,
this follows by consideration of the limit of the face f n
i+1, using the fact that it
is a convex polygon and that each of its edges must meet H3. Note that only
the second alternative can hold if Π∞
fi+1 is not tangent to ∂∞H3.
If all the limit edges e∞
i
are equal, then the edges ei all have a vertex v in
common, and γ just turns around this vertex v. However, as in Case 1, this
contradicts the fact that the interiors of the two edges e12 and e23 are contained
in the same component of ∂P Proj
0
−Kp as γ.
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
486
BAO (X.) & BONAHON (F.)
Otherwise, counting indices modulo m, there are i, j such that e∞
i
= e∞
i+1 =
· · · = e∞
j
but such that e∞
i−1 and e∞
j+1 are both diﬀerent from e∞
i
= e∞
j . Then,
the oriented edges ek, with i ≤k ≤j have the same terminal end point v,
which is distinct from the terminal end point v′ of ei−1 and from the terminal
end point v′′ of ej+1. The two vertices v′ and v′′ are actually equal; otherwise,
one would get a contradiction from the limit of the convex triangle Tn in P Proj
n
whose vertices are the vertices of P Proj
n
corresponding to v, v′ and v′′, using
the fact that by Lemma 3 each edge of Tn must meet H3.
We conclude from this analysis that the terminal end point of each ei with
1 ≤i ≤m must be equal to v or v′ = v′′.
If v and v′ are joined by an edge e ∈E, then γ must be the boundary of a
regular neighborhood of e, by 3-connectedness of Γ. In particular, the edge e12
must be equal to e or to one of the ei with 1 ≤i ≤m, by deﬁnition of γ.
However, the limit edge e∞joins the limit points x∞
v and x∞
v′ , and is contained
in a line tangent to ∂∞H3 at p. Since e∞
12 contains the diameter R × {0} ∩H3,
it follows that e12 cannot be equal to e. Similarly, e12 cannot be equal to one
of the ei as e∞
i
is tangent to ∂∞H3 at p by deﬁnition of γ.
Finally, if v and v′ are not joined by an edge, then the ei are the only edges
whose interior is contained in the same component of ∂P Proj
0
−Kp as γ. This
again contradicts the deﬁnition of γ since e12 cannot be equal to any of these ei,
as above.
As a consequence, we reach a contradiction in all cases. This completes the
proof of Lemma 22.
Lemma 23. — No plane Π∞
f
is tangent to ∂∞H3.
Proof of Lemma 23. — Suppose that Π∞
f
is tangent to ∂∞H3. Then, because
no limit edge e∞is reduced to a single point, by Lemma 22, the consideration
of the possible degenerations of the face f n of P Proj
n
shows the following: There
are two edges e1 and e2 of the face f, meeting at a vertex v, such that the limit
point x∞
v is on the sphere ∂∞H3 and such that the limit edges e∞
1 and e∞
2 point
in opposite directions at x∞
v .
By consideration of the convex cone C delimited by the limit planes Π∞
f ′
associated to the faces f ′ ∈F that contain v, one concludes as in the proof of
Lemma 22 that there exists a third edge e3 containing v such that e∞
3 is equal
to e∞
1
and e∞
2 . However, this provides a face f0, containing v, such that the
convex polygon f n
0 converges to a line segment that is tangent to ∂∞H3 at one
of its end points. This is not possible if no limit edge e∞is reduced to a point.
This proves Lemma 23.
For an edge e ∈E, we already know by Lemma 22 that the limit edge e∞
is not reduced to a single point. If f and f ′ ∈F are the two faces separated
by e, Lemma 23 shows that the hyperbolic planes Π∞
f ∩H3 and Π∞
f ′ ∩H3 are
tome 130 – 2002 – no 3
HYPERIDEAL POLYHEDRA IN HYPERBOLIC 3-SPACE
487
non-trivial. Since the dihedral angle θn
e between the hyperbolic planes Πn
f ∩H3
and Πn
f ′ ∩H3 converges to the coordinate θ∞
e̸ =0, π of the limit point θ∞∈KΓ,
it follows that Π∞
f ∩H3 and Π∞
f ′ ∩H3have a non-trivial intersection, and make
dihedral angle of θ∞
e
along this intersection. In particular, the limit edge e∞
meets H3.
For a face f ∈F, the plane Πn
f containing the corresponding face f n of
P Proj
n
converges to a plane Π∞
f
which meets H3 and, for each edge e of f, the
edge en of f n converges to an edge e∞which meets H3 but whose end points
are outside of H3. It follows that f n converges to a convex polygon f ∞⊂Π∞
f
which is really 2-dimensional and has the same combinatorics as f.
As a consequence, as f ranges over all the elements of F, the union of the
polygons f∞forms a polyhedral sphere S∞which has the same combinatorial
type as ∂P Proj
0
. In addition, S∞is locally convex since the dihedral angle θ∞
e
of S∞along the edge e∞corresponding to e ∈E is in ]0, π[.
Let P Proj
∞
⊂RP3 be bounded by the sphere S∞, oriented by its identiﬁcation
to ∂P Proj
0
. To show that P Proj
∞
is a projective convex polyhedron, we only have
to show that it does not contain any projective line. (Remember that we had
included this condition in the deﬁnition of convex polyhedra in RP3). However,
by local convexity, the only way this could fail is if P Proj
∞
was projectively
equivalent to an inﬁnite prism in R3 ⊂RP3, in which case the dual graph of
the cell decomposition of ∂P Proj
∞
= S∞would be homeomorphic to a circle. But
this dual graph is Γ by construction, and cannot be a circle by 3-connectedness.
Therefore, P Proj
∞
is a convex projective polyhedron. We already noted that
its vertices are all outside H3, and that its edges all meet H3.
Therefore
P∞= P Proj
∞
∩H3 is a hyperideal polyhedron.
By construction, the vertices
of P Proj
∞
are the limit of the vertices of P Proj
n
, and it follows that P∞is the
limit of the sequence Pn in PΓ.
This concludes the proof of Proposition 21.
If we retrace back the proof of Proposition 21, and in particular the proof
of Lemma 22, we can summarize it as follows: If the sequence Pn ∈PΓ, n ∈N,
admits no converging subsequence then, possibly after passing to a subsequence,
it necessarily degenerates according to one of the following patterns:
1) one of the dihedral angles of Pn converges to 0 or π;
2) Pn develops a very long and thin ‘neck’ around a very short simple closed
curve in ∂Pn which corresponds to a ﬁxed curve in the model polyhedron ∂P0;
3) the truncated polyhedron P Trun
n
develops a very long and thin ‘neck’
around a very short simple closed curve in ∂P Trun
n
which corresponds to a ﬁxed
curve in ∂P Trun
0
and crosses exactly one of the new faces of ∂P Trun
n
associated
to vertices of P Proj
0
.
An immediate corollary of Proposition 21 is the following.
BULLETIN DE LA SOCI´ET´E MATH´EMATIQUE DE FRANCE
488
BAO (X.) & BONAHON (F.)
Corollary 24. — The map Θ : PΓ →KΓ is a covering map.
Proof. — The map Θ is a local homeomorphism by Theorem 11, and it is
proper by Proposition 21. Since KΓ is locally compact, this implies that Θ is
a covering map.
