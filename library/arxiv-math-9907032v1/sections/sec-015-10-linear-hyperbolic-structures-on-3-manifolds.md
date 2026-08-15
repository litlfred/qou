---
doc_id: arxiv-math-9907032v1
doc_title: "Mathematics Department, California Institute of Technolog y"
section_id: sec-015-10-linear-hyperbolic-structures-on-3-manifolds
section_title: "LINEAR HYPERBOLIC STRUCTURES ON 3-MANIFOLDS"
section_number: 10
pages: 23-26
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
As explained in [19], the study of Euclidean triangulations on surfaces is essentially
equivalent to the study of hyperbolic ideally triangulated complexes, which are
combinatorially just cones over the triangulated surface. Hence, the contents of
this section are closely related to the subject-matter of much of t he rest of the
paper, in more than just the linear programming approach.
Consider a 3-manifold M 3 with boundary a collection of tori, and consider a
topological ideal triangulation T of M 3. We would like to know when there is a
complete hyperbolic structure on M 3, such that T is a geometric ideal triangula-
tion. In general, this is a very diﬃcult question, at least as hard as Th urston’s
hyperbolization conjecture (since even if M 3 admits a hyperbolic structure of ﬁnite
volume, there might not be an ideal triangulation combinatorially equiv alent to T ).
However, below we will consider a “linear” version of the question abo ve.
Recall that an ideal simplex S in H3 has the properties that
Euclidean links. The link of each vertex is a Euclidean triangle.
Equal opposite dihedral angle. If S = ABCD , then the dihedral angles at the
edgesAB andCD are equal (this is actually a consequence of the condition on the
links).
An ideal simplex is thus determined by the angles of the link of any one o f its
vertices (all links are easily seen to be the same).
Now, if T comes from a genuine hyperbolic structure, it must be true that th e
sum of the dihedral angles incident to the edges of T must equal 2π, and so for T
to correspond to such a structure, the following linear program mu st have a strictly
positive solution:
The variables. These are the dihedral angles of the simplices. For each simplex
S we use three angles α,β,γ corresponding to the angles of the link of one vertices
of S.
Simplex conditions. For each simplex S, the sum of the dihedral angles is equal
to π:
fS :α +β +γ =π. (34)
· 24
Edge conditions. For each edge e of T the sum of the dihedral angles of all sim-
plices incident to e equals 2π :
fe :
∑
λi = 2π. (35)
Definition 10.1. We say that if the above linear program has a non-negative
solution, then the pair (M 3,T ) admits a weak linear hyperbolic structure . If the
linear program has a strictly positive solution, then we say that the pair (M 3,T )
admits a linear hyperbolic structure.
It is clear that the existence of a linear hyperbolic structure is, in ge neral, no guar-
antee of the existence of a genuine hyperbolic structure, since th e linear conditions
do not preclude “Dehn surgery” singularities, as well as translation al singularities
along edges of T (see [25; 14] for discussion). Conversely, as remarked above, th e
existence of a complete hyperbolic structure on M 3 is no guarantee that there is a
positively oriented ideal triangulation combinatorially equivalent to T (or, indeed,
any positively oriented triangulation). However, linear hyperbolic st ructures have
the advantage of being considerably more tractble.
Theorem 10.2. In order for there to exist a weak linear hyperbolic structur e
for (M 3,T ), every normal surface with respect to T must have non-negative Euler
characteristic. In order for there to exist a linear hyperbo lic structure for (M 3,T ),
every non-boundary-parallel normal surface with respect t o T must have strictly
negative Euler characteristic.
Proof. We will use the method of Section 3. First, let us write the dual progr am
of the linear program (referred to as Lh in the sequel) for weak hyperbolic structure:
Our variables are {vS}, where S ranges over all the simplices of T , and {ve} where
S ranges over all the edges of T .
The dual program L∗
h is:
. Maximize ∑
S∈S(T )vS + 2 ∑
e∈E(T )ve.
. Subject to vS +ve1 +ve2 ≤ 0 for all faces S and pairs of opposite edges e1,e 2.
In order for the primal program to have a non-empty feasible regio n, the objective
of the dual must be non-positive.
Consider now a normal surface S (see, eg, [8; 12; 9] for rudiments of normal
surface theory). The surface S intersects each simplex S in a collection of disks,
which are combinatorially either triangles (cutting oﬀ one vertex of S from the
other three), or quadrilaterals (separating one pair of vertices f rom another). For
each simplex S, deﬁne tS(S) to be the number of triangular components of S ∩S,
and qS(S) to be the number of quadrilateral components. For each edge e of T ,
deﬁne ie(S) to be the number of intersections of S with e. The intersections of S
with the simplices of T induces a triangulation T of S, where each triangular disk
contributes one triangle, and each quadrangle contributes two. D eﬁne uS(S) to be
the number of triangles of T sitting inside a simplex S. Evidently, uS =tS + 2qS.
Note that, by Euler’s formula, χ(S) = ∑
e∈E(T )ie − 1
2
∑
S∈S(T )uS. This is seen
to be very similar in form to the objective function of L∗
h, so let us set vS = −uS,
and ve =ie.
· 25
Lemma 10.3. The assignment of the variables as above satisﬁes the inequa lity
constraints of L∗
h.
Proof of lemma. We need to check that for S a simplex and e1,e 2 a pair of
disjoint edges of S. We need to check that
ie1 +ie2 ≤uS. (36)
By linearity, we need just check the inequality 36 for connected com ponents of S ∩S.
If that component is a triangle t, then t contributes 1 to ie1 +ie2 (since a “normal
triangle” intersects exactly one of each pair of opposite edge). Als o, t contributes
1 to uS, so for a triangular face, the right and left hand sides of (36) are e qual.
Suppose now we have a quadrilateral component q. It contributes 2 to the right
hand side of (36). As for the left hand sides, q hits two pairs of opposite sides of
S, so if e1 and e2 is one of those pairs, then we have a contribution of 2 to the left
hand side, and otherwise we have a contribution of 0.
Remark 10.4. Notice that if S is such that all of the components of S ∩ S,
for all S ∈S(T ) are triangles, then all of the constraints of L∗
h are equalities with
the assignment of variables as above. Any such S is easily seen to be a union of
boundary tori.
Lemma 10.3 concludes the proof of the “weak” part of Theorem 10.2 , since if any
S had positive Euler characteristic, the program L∗
h would have a positive objective,
and thus the program Lh would have no solution.
For the proof of the “strong part” we use the same trick as in Sect ion 3. Deﬁne
new variables α′ =α +ǫ, etc. Our primal linear hyperbolicity program Ls is now:
. Minimize: −ǫ
. subject to face constraints α′ +β′ +γ′ + 3ǫ =π.
. and to edge constraints ∑
α prime +v(e)ǫ = 2π, where v(e) is the valence of e.
The dual program L∗
s is then
. Maximize ∑
S∈S(T )vS + 2 ∑
e∈E(T )ve.
. Subject to the old constraints vS +ve1 +ve2 ≤ 0 for all faces S and pairs of
opposite edges e1,e 2.
. and the new constraint 3 ∑
S∈S(T )vS + ∑
e∈E(T )v(e)vE ≤ −1.
In order for ( M 3,T ) to be linearly hyperbolic, the objective must be strictly
negative.
Observe that the sum of the left hand sides of the old constraints is equal to the
left hand side of the new constraint. Indeed, each vS occurs three times (once for
each pair of opposite edges), and each ve occurs the number of times equal to the
valence of e. Hence, the new constraints simply says that in at least one of the
old constraints the inequality must be strict. Keeping in mind Remark 10.4, this
implies that every non-boundary-parallel normal surface must ha ve strictly negative
Euler characteristic, thus proving the second part of Theorem 10 .2
Some remarks may be in order: It is easy to see (and not surprising) that an
identical theorem can be proved if the cone angles around the edge s ofT are required
· 26
to not be smaller than 2 π, while if the angles are smaller than 2 π, one can show
an analogous “orbifold” version of the theorem. A more interesting question is
whether theconverse of Theorem 10.2 holds. This is equivalent to as king whether
every assignment of variables satisfying the constraints of progr ams L∗
h and L∗
s
comes from a normal surface.
