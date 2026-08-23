---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-001-1-background
section_title: "BACKGROUND"
section_number: 1
pages: 3-5
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
1.1 Singular similarity structures.
Consider an oriented surface S, possibly with boundary, and with a number of dis-
tinguished points {p1,...,p n}. A similarity structure on S is given by an atlas for
S\{p1,...,p n}, such that the transition maps are Euclidean similarities. A similar-
ity structure induces a holonomy representation Hs of Γ = π1(S\{p1,...,p n}) into
the similarity Sim ( E2) ≃ ~C∗, where the tilde indicates the universal cover. We
deﬁne the dilatational holonomy as the induced representation Hd : Γ → R, where
Hd(γ) = log dilatationHs(γ) = log |Hs(γ)|. The rotational holonomy can almost be
deﬁned as Hr(γ) = arg Hs(γ), but for the slight complication that we need to take
the argument in ~C∗, since we want to distinguish, eg, the angle of 4 π from one of
2π. This notion of argument is what is used in the sequel. In particular, if γ is a
loop surrounding one of the distinguished points pi, then Hr(γ) is the cone angle at
pi. In the case where Hd(Γ) = {0}, the similarity structure is a singular Euclidean
structure, with cone angles deﬁned by Hr as above. In the sequel, references to
the holonomy of a similarity structure will actually mean the dilatational holon-
omyHd. A more concrete way to think of both similarity and Euclidean struct ure
is by assembling our surface out of Euclidean triangles, in the patter n given by
some complex T . In the case where the lengths of the edges of the triangles being
glued together agree, then we have a singular Euclidean structure . If not, then we
have a similarity structure. In either case, the vertices of T are potentially cone
points, with cone angles given by the sums of the appropriate angles of the incident
triangles.
· 4
Consider an oriented surface S, possibly with boundary, and assume that S has
a Euclidean metric (or, more generally, a similarity structure – with th e exception
of the results of Section 6 , some of which depend on the metric Theo rem 6.3,
the metric structure or lack thereof plays no role in the arguments ). with cone
singularities. We will be dealing with semi-simplicial triangulations of S, that is,
triangulations where two and where distinct closed cells might interse ct in a collec-
tion of lower-dimensional cells. All triangulations will be assumed semi- simplicial,
unless speciﬁed otherwise. A subcomplex F of T will be called closed if whenever
an open face F is in F , so are all of the faces of ∂F .
Assume now that the surface S is equipped with a ﬁnite geodesic semi-simplicial
triangulation T , such that the 0-skeleton of T , which is denoted by V (t), contains
all of the cone points of S. Each face of T is then a Euclidean triangle. There are
two kinds of edges of T – the interior edges, incident to two faces of T , and the
boundary edges, incident to only one face of T .
Definition 1.1. Lete be an edge of T . First, suppose that e is a boundary edge,
and let t =ABC be a face of T incident to e, so that e =AB. Then the dihedral
angle δ(e) at e is the angle of t at the vertex C. Now, assume that e is an internal
edge of T, so that e is incident to t1 =ABC and t2 =ABD, so that e =AB. Then
the dihedral angle at e is the sum of the angle of t1 at C, and the angle of t2 at D.
The exterior dihedral angle δ′(e) at e is deﬁned to be δ′(e) = π −δ(e).
The cone angle at an interior vertex v of T is the sum of all the angles of the
faces of T incident to v at v; the boundary angle at a boundary angle is deﬁned in
the same way.
The following is a slight extension of [19, Lemma 4.2].
Lemma 1.2. The cone angle at an interior vertex v ∈V (T ) is equal to the sum
of the exterior dihedral angles at the edges of T incident to v. At a boundary vertex,
the boundary angle is equal to the sum of the exterior dihedra l angles as above, less
π.
Proof. First, let v be an interior vertex. Suppose that there are n triangles
t1,...,t n incident to v. The sum of all of their angles is nπ. The cone angle at v
is the sum of the angles of the triangles ti at v. On the other hand, the sum of the
dihedral angles of the edges e1,...,e n incident to v is the sum of all of the angles
of ti not incident to v. Thus,
nπ = Cone angle at v +
n∑
i=1
δ(ei). (1)
The result follows by rearranging the terms.
Ifv is a boundary vertex, and there are n faces incident to v, then there are n + 1
edges, and equation 1 becomes:
nπ = boundary angle at v +
n+1∑
i=1
δ(ei), (2)
and the result follows by rearranging terms, as above.
· 5
Observation 1.3. The sum of all of the dihedral angles of all of the edges of
T is equal to the π|V (T )| – in combination with the Lemma above this gives the
Gauss-Bonnet theorem in this polyhedral context, since the curvature at an interior
vertexv ofT is deﬁned to be 2π−Cone angle at v, while the curvature at a boundary
vertex is deﬁned to be π − boundary angle at v.
Proof. Every angle of every face of T is opposite to exactly one edge of T .
The next theorem is [19, Theorem 6.16].
Theorem 1.4. Let ∆ : E(T ) → (0, 2π) be an assignment of dihedral angles
to the edges of T , and Hd a holonomy representation. There exists at most one
singular similarity structure on S with holonomy Hd (and in particular, at most
one singular Euclidean structure, up to scaling), such that so that δ(e) = ∆( e), for
every edge e ∈E(T ).
Definition 1.5. A triangulation T with δ(e) ≤ π for every interior e ∈ E(T )
is called a Delaunay triangulation .
Let ∆ be a map – ∆ : E(T ) → (0, 2π). When does there exist a singular Euclidean
metric on S with the dihedral angles prescribed by ∆? It is clear that there are
certain linear constraints which must be satisﬁed – to wit, for every face t =ABC
of T , we must be able to ﬁnd angles α, β, and γ, such that:
Positivity. All angles are strictly positive.
Euclidean Faces. For every face t, αt +βt +γt =π.
Boundary edge dihedral angles. For every boundary edge e = AB, incident to
the triangle ABC , γ = ∆( e).
Interior edge conditions. For every interior edge e = AB, incident to triangles
ABC and ABD, α +δ = ∆( e).
The system of equations and inequalities above specify a linear program L. The
feasible region (set of solutions) of L must be non-empty in order for us to have any
hope of having a singular Euclidean metric on S with prescribed dihedral angles.
One of the principal results (Theorem 6.1) of [19] is that if all of the d ihedral angles
are no greater than π (that is, the triangulation is Delaunay), then Conditions 1-4
are also suﬃcient, thus:
Theorem 1.6. If the feasible region of L is non-empty and every dihedral angle
is at most π, then there exists a similarity structure with any prescrib ed holonomy
Hd and, in particular, a singular Euclidean metric on S with the prescribed dihedral
angles – this structure is unique by Theorem 1.4 (and the metr ic is unique up to
scaling).
