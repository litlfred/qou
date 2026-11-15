---
doc_id: angled-survey
doc_title: "From angled triangulations to hyperbolic structures"
section_id: sec-003-4-leadingtrailing-deformations
section_title: "Leading–trailing deformations"
section_number: 4
pages: 10-16
source_pdf: angled-survey.pdf
source_sha256: 8b49e682a39848bc
toc_source: inferred
doc_brief: "From angled triangulations to hyperbolic structures — This survey paper contains an elementary exposition of Casson and Rivin’s technique for ﬁnding the hyperbolic metric on a 3–manifold M with"
---
Given a point p of the angle polytope A(τ), let TpA(τ) be the tangent space
to A(τ) at the point p. There is a particularly convenient choice of spanning vec-
tors for TpA(τ). These leading–trailing deformations, which were probably folklore
knowledge to experts for several years, are the main innovation in our direct proof
of Theorem 1.2. In a certain sense, they serve as a more concrete reformulation of
Neumann and Zagier’s symplectic pairing [22]. To the best of the authors’ knowl-
edge, this is the ﬁrst place where they are described in print.
Definition 4.1. Let C be a cusp torus of M, with a tessellation by boundary
triangles coming from τ.
Let σ ⊂C be an oriented normal closed curve (see
Deﬁnition 2.2), consisting of segments σ1, . . . σk. Every oriented segment σi lies
in a boundary triangle Δi. We deﬁne the leading corner of Δi to be the corner
opposite the side where σi enters Δi, and mark it with a +. We deﬁne the trailing
corner of Δi to be the corner opposite the side where σi leaves Δi, and mark it
with a ⊖. See Figure 3.
For every oriented segment σi, we deﬁne a vector w(σi) ∈R3n, where as above
each coordinate of R3n corresponds to one pair of opposite edges in one of the n
tetrahedra. Every corner of Δi corresponds to one such edge pair in a tetrahedron.
The vector w(σi) will have a 1 in the coordinate corresponding to the leading corner
168
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
11
+
+
+
+
+
+
+
+
⊖
⊖
⊖
⊖
⊖
⊖
⊖
⊖
Figure 3. The leading–trailing deformation along σ increases the
angles marked + and decreases the angles marked ⊖.
of Δi, a −1 in the coordinate corresponding to the trailing corner of Δi, and 0’s
otherwise.
Finally, the leading-trailing deformation corresponding to σ is the vector w(σ) =

i w(σi).
Example 4.2. Let e be an edge of M, and suppose for simplicity that all
tetrahedra adjacent to e are distinct. Let σ be a simple closed curve on ∂M, running
counterclockwise about one endpoint of e. The boundary triangles intersected by σ
have angles αi, βi, γi, labeled clockwise with αi inside σ. Then the leading–trailing
deformation w(σ) adds 1 to every βi and subtracts 1 from every γi, keeping the
angle sum in each tetrahedron equal to π. In addition, the dihedral angle marked
βi is adjacent to the same edge of M as the dihedral angle marked γi+1. Thus the
angle sum at each edge is unchanged. (See Figure 4.) Observe that w(σ) has no
eﬀect at all on the dihedral angles αi adjacent to e.
α1
α2
α3
α3
α4
α4
α5
e
+
+
+
+
+
+
+
+
+
+
+
⊖
⊖
⊖
⊖
⊖
⊖
⊖
⊖
⊖
⊖
⊖
Figure 4. The leading–trailing deformation about a single edge e
of M. Every increase to an angle in a tetrahedron is canceled out
by a decrease to an adjacent angle.
In the more general setting, we will prove in Lemma 4.5 that leading–trailing
deformations are always tangent to A(τ). To do that, we need a better understand-
ing of the interaction between diﬀerent deformations.
Definition 4.3. Let τ be an ideal triangulation of M, and let ρ, σ be oriented
normal closed curves on ∂M that intersect transversely (if at all). Deﬁne the signed
intersection number ι(ρ, σ) to be the number of times that σ crosses ρ from right to
169
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
12
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
σ
σ
σ′
σ′
σ′′
σ′′
⇒
⇒
⇒
Figure 5. Decomposing σ into smaller curves. Left: when two
segments of σ pass through the same boundary triangle, we may
cut and rejoin to form two normal curves σ′, σ′′. Right: a local
isotopy in the complement of the vertices may be required to ensure
that σ′, σ′′ are again normal curves.
left, minus the number of times that σ crosses ρ from left to right. This deﬁnition
has a few immediate properties:
• It is anti-symmetric: ι(ρ, σ) = −ι(σ, ρ).
• It depends only on the homology classes of σ and ρ in H1(∂M).
• By considering a transverse pushoﬀof σ, one obtains ι(σ, σ) = 0.
Lemma 4.4. Let ρ, σ be oriented normal closed curves on ∂M that intersect
transversely, if at all. Then
∂
∂w(σ)Im(H(ρ)) = 2 ι(ρ, σ).
Recall that Im(H(ρ)) is the linear, angled part of the holonomy in Deﬁnition
2.3.
Proof. The proof involves three steps.
Step 1 introduces several simplifying assumptions with no loss of generality.
First, it will help to assume that every tetrahedron T is embedded in M (that
is, T does not meet itself along an edge or face). This assumption can always be
met by passing to a ﬁnite–sheeted cover of M, since π1(M) is residually ﬁnite by
Selberg’s lemma. Note that the tetrahedra, angles, boundary curves, holonomies,
and leading–trailing deformations all lift naturally to covers. This assumption also
implies that boundary triangles Δi, Δj meet in either at most one edge or at most
one vertex.
Next, no generality is lost by assuming that σ passes through each boundary
triangle at most once. For, if two segments σi, σj run through the same boundary
triangle Δ, we may cut and rejoin the curve σ into a pair of shorter normal closed
curves σ′, σ′′. See Figure 5. (To ensure that σ′ and σ′′ are normal curves, it may
be necessary to move them by isotopy in the complement of the vertices, as in the
right panel of the ﬁgure.) Note that this operation is natural and topologically
additive: we have w(σ) = w(σ′) + w(σ′′), and ι(ρ, σ) = ι(ρ, σ′) + ι(ρ, σ′′). Thus, if
170
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
13
we prove the lemma for each of σ′ and σ′′, the result will follow for σ. In particular,
we may now assume that σ is embedded.
Similarly, we may assume that ρ also passes through each boundary triangle
at most once. For, if ρi, ρj run through the same boundary triangle Δ, we may
decompose ρ into a pair of curves ρ′, ρ′′ just as above. This natural operation
ensures H(ρ) = H(ρ′) + H(ρ′′), and ι(ρ, σ) = ι(ρ′, σ) + ι(ρ′′, σ). Thus it suﬃces to
consider each of ρ′ and ρ′′ in place of ρ.
Given these simplifying assumptions, suppose that the segments σ1, . . . , σk of
σ are contained in distinct boundary triangles Δ1, . . . , Δk. A priori, there are two
ways in which w(σ) could aﬀect the angular component of H(ρ):
(1) A segment of ρ lies in the same boundary triangle Δi that contains σi.
Then, w(σi) changes the angles of Δi, thereby changing Im(H(ρ)).
(2) A segment of ρ lies in a boundary triangle Δ′
i, where Δi̸ = Δ′
i are two
truncated vertices of the same ideal tetrahedron. By changing dihedral
angles in the ambient tetrahedron, w(σi) also changes the angles of Δ′
i.
We consider the eﬀect of (2) in Step 2 and the eﬀect of (1) in Step 3.
Step 2 is to show that the eﬀect of w(σ) in the boundary triangles “on the
other side” of the ambient tetrahedra, as in (2) above, will never change Im(H(ρ)).
To see why this is true, it helps to group together boundary triangles that share a
common vertex v.
Let v be a vertex of ∂M, and let σv = σ1 ∪. . . ∪σj be a maximal union of
consecutive segments in σ, such that the ambient boundary triangles Δ1 . . . , Δj are
all adjacent to v. By our embeddedness assumption, each Δi is adjacent to v in
only one corner. Recall that v is one endpoint of an edge e ⊂M; we will investigate
the eﬀect of w(σv) on boundary triangles Δ′
1, . . . , Δ′
j at the other end of edge e.
The arc σv can take one of three forms:
(i) σv = σ, and forms a closed loop about v.
(ii) σv takes a right turn in Δ1, followed by a sequence of left turns about v,
followed by a right turn in Δj.
(iii) σv takes a left turn in Δ1, followed by a sequence of right turns about v,
followed by a left turn in Δj.
Scenario (i) is depicted in the right panel of Figure 4. Here, v is in the interior
of a polygon Pv = Δ1 ∪. . . ∪Δj. Notice that none of the external angles along ∂Pv
actually change, even though the shapes of constituent triangles are changing. The
same will be true in the boundary polygon P ′
v = Δ′
1 ∪. . . ∪Δ′
j at the other end of
e. Thus, if ρ passes through P ′
v, its holonomy will be unaﬀected by this change.
In Scenario (ii), we once again construct a polygon Pv by gluing Δ1 to Δ2 along
their (unique) shared edge, and so on up to Δj. Let P ′
v = Δ′
1 ∪. . . ∪Δ′
j be the
polygon formed by the boundary triangles in the same tetrahedra, on the other end
of e. These two polygons are depicted in Figure 6. Notice that although Δi and
Δ′
i are in the same oriented similarity class (both have the same angles αi, βi, γi,
in clockwise order), the triangles in these similarity classes are rearranged to form
P ′
v. In particular, w(σv) does not change any of the external angles along ∂P ′
v,
even though the shapes of constituent triangles Δ′
i are changing. Thus, if ρ passes
through P ′
v, its holonomy will be unaﬀected.
Scenario (iii) is the mirror image of (ii). Once again, w(σv) does not change
any of the external angles along ∂P ′
v.
171
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
14
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
α1
α1
α2
α2
α3
α3
α4
α4
+
+
+
+
+
+
+
+
⊖
⊖
⊖
⊖
⊖
⊖
⊖
⊖
v
Pv
P ′
v
Figure 6. Left: the boundary polygon Pv comprised of boundary
triangles Δ1, . . . , Δj adjacent to v. In each Δi, the smallest angle
is αi. Right: in the boundary polygon P ′
v = Δ′
1 ∪. . . ∪Δ′
j, at
the other end of the edge that starts at v, none of the total angles
along ∂P ′
v change.
We conclude that for every vertex v in a boundary triangle visited by σ, the
polygon P ′
v on the other end of the same edge will have all its external angles
unaﬀected by w(σv). Since each segment σi of σ belongs to three diﬀerent maximal
arcs σv (corresponding to the three distinct vertices of Δi), we have 
v w(σv) =
3w(σ). Thus, since each w(σv) does not aﬀect the holonomy of ρ “on the other
side” of the ambient tetrahedra, neither does w(σ). This completes Step 2.
Step 3 considers the holonomy of ρ in the same boundary triangles that are
also visited by σ. Consider a maximal consecutive string of segments σ1, . . . , σj,
contained in Δ1, . . . , Δj, such that consecutive segments ρ1, . . . , ρj run through the
same boundary triangles. Depending on orientations, we can have either ρ1 ⊂Δ1
or ρ1 ⊂Δj.
In the special case where Δ1 ∪. . . ∪Δj contains all of σ and all of ρ, the two
curves cut oﬀexactly the same corners of boundary triangles (possibly in opposite
cyclic order). Then, since ∂M is orientable, we must have ι(ρ, σ) = 0. In this case,
the angles that go into computing the angular holonomy Im(H(ρ)) are exactly the
angles that are unaﬀected by w(σ). Thus, in this special case, ∂Im(H(ρ))/∂w(σ) =
0 = 2 ι(ρ, σ).
In the general case, we may assume that σ and ρ do not run in parallel through
Δ1 or through Δj (otherwise, the sequence 1, . . . , j is not maximal). As above, it
helps to construct a polygon P by gluing Δ1 to Δ2 along their (unique) shared
edge, and so on up to Δj. By Deﬁnition 4.1, each Δi has one mark of + in the
leading corner relative to σi, and one mark of ⊖in the trailing corner. Altogether,
the polygon P contains 2j markers, with j pluses and j minuses. We consider how
many of these markers are to the left and right of ρ.
If σ enters polygon P to the right of ρ and leaves to the left of ρ, the interior of
P contributes +1 to ι(ρ, σ). Also, the part of P to the left of ρ will have a surplus
of two +’s. Thus w(σ1 ∪. . . ∪σj) increases the angular component of H(ρ) by 2.
See Figure 7.
If σ enters polygon P to the left of ρ and leaves to the right of ρ, the interior of
P contributes −1 to ι(ρ, σ). Also, the part of P to the left of ρ will have a surplus
of two ⊖’s. Thus w(σ1 ∪. . . ∪σj) increases the angular component of H(ρ) by −2.
172
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
FROM ANGLED TRIANGULATIONS TO HYPERBOLIC STRUCTURES
15
σ
ρ
+
+
+
+
⊖
⊖
⊖
⊖
Figure 7. When σ crosses ρ from right to left, the part of the
polygon P to the left of ρ contains an excess of two +’s.
Finally, if σ enters and leaves P on the same side of ρ, the interior of P con-
tributes 0 to ι(ρ, σ). Also, the part of P to the left of ρ will have the same number
of +’s and ⊖’s, hence w(σ1 ∪. . . ∪σj) does not aﬀect the angular component of
H(ρ).
Summing these contributions over the (disjoint) polygons of intersection, we
conclude that ∂Im(H(ρ))/∂w(σ) = 2 ι(ρ, σ), as desired.
□
We can now show that every leading–trailing deformation w(σ) is tangent to
A(τ).
Lemma 4.5. Let p ∈A(τ) be an angle structure, and let σ be an oriented
normal curve on a cusp of M. Then the vector w(σ) is tangent to A(τ). In other
words, for all suﬃciently small ε > 0,
p + εw(σ) ∈A(τ).
Proof. Let us check the conditions of Deﬁnition 3.1. By condition (1) of the
deﬁnition, p lies in the open set (0, π)3n. Thus, for suﬃciently small ε, we have
p + εw(σ) ∈(0, π)3n also.
Next, observe that in Deﬁnition 4.1, every vector w(σi) only aﬀects a single
tetrahedron. In this tetrahedron, εw(σi) adds ε to the dihedral angle on one (lead-
ing) pair of opposite edges, and adds −ε to the dihedral angle on another (trail-
ing) pair of opposite edges. Thus the deformation of angles coming from w(σi)
keeps the angle sum equal to π in every tetrahedron. Clearly, the same is true for
w(σ) = 
i w(σi).
Finally, we check condition (3) of Deﬁnition 3.1. Let e be an edge of M, and
let ρ be a normal closed curve on ∂M that encircles one endpoint of e. Because
ρ is homotopically trivial, we have ι(ρ, σ) = 0. Thus, by Lemma 4.4, deforming
the dihedral angles along w(σ) does not change the imaginary part of H(ρ). But
Im(H(ρ)) is nothing other than the sum of dihedral angles about edge e; this sum
stays constant, equal to 2π.
□
There is a convenient choice of leading–trailing deformations that will span
TpA(τ).
Proposition 4.6. For every edge ei of M, where 1 ≤i ≤n, choose a normal
closed curve ρi about one endpoint of ei. In addition, if M has k cusps, choose
simple closed normal curves σ1, . . . , σ2k that will span H1(∂M). Then the vectors
w(ρi) and w(σj) span the tangent space TpA(τ).
173
Licensed to Temple Univ.  Prepared on Tue Jul 30 15:53:49 EDT 2019for download from IP 155.247.31.215.
License or copyright restrictions may apply to redistribution; see https://www.ams.org/publications/ebooks/terms
16
DAVID FUTER AND FRANC¸ OIS GU´ERITAUD
Notice that the curves ρ1, . . . , ρn, σ1, . . . , σ2k are exactly the ones whose holo-
nomy is being considered in Deﬁnition 2.4.
Proof. By Proposition 3.2, dim TpA(τ) = n+k. Thus it suﬃces to show that
w(ρi), w(σj) span a vector space of this dimension.
First, we claim that the vectors w(σ1), . . . , w(σ2k) are linearly independent
from one another, and from each of the w(ρi). Suppose, after renumbering, that σ1
and σ2 are homology basis curves on the same torus of ∂M. Then ι(σ1, σ2) = ±1,
while ι(σj, σ2) = 0 for every j̸ = 1 (including j = 2). Similarly, since each ρi is
homotopically trivial, ι(ρi, σ2) = 0 for every i. Thus, by Lemma 4.4, w(σ1) is the
only deformation among the ρi and σj that aﬀects Im(H(σ2)). Therefore, w(σ1)
is independent from all the other vectors in the collection. Similarly, each w(σj) is
independent from all the other vectors in the collection.
To complete the proof, it will suﬃce to show that w(ρ1), . . . , w(ρn) span a
vector space of dimension n −k. Let B be the (n × 3n) matrix whose ith row is
w(ρi). Then, we claim that rank(B) = n −k. The proof of this claim is virtually
identical to the proof of Lemma 3.3.
For every cusp c, we deﬁne a row vector
rc ∈Rn, whose ith entry is the number of endpoints that the ith edge ei has at cusp
c. (This is the second half of the vector rc from Lemma 3.3.) Then, by the same
argument as in that lemma, one checks that the vectors rc form a basis for the row
null space of B. Therefore, rank(B) = n −k, and the w(ρi), w(σj) span a vector
space of dimension (n −k) + 2k, as required.
□
