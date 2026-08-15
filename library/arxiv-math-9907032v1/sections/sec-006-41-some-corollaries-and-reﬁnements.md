---
doc_id: arxiv-math-9907032v1
doc_title: "Mathematics Department, California Institute of Technolog y"
section_id: sec-006-41-some-corollaries-and-reﬁnements
section_title: "Some corollaries and reﬁnements"
section_number: 4.1
pages: 11-13
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
Here are some easy consequences of Theorem 4.3:
Special case 1. F = T . Then, since E′(F ) = ∅, we just get the Gauss-Bonnet
theorem (with curvature deﬁned in terms of the dihedral angles).
Special case 2. The complement of F is an annulus containing no vertices of T
– this corresponds to a simple cycle in the Poincar´ e dual T ∗. For every edge in
E′(F ), ne = 2. Theorem 4.3 just says that ∑
e∈E′δ′(e)> 0.
Special case 3. For every edge in E′(F ),ne = 1. This will hold in the case where
F is a subset of T with a collar, and removing the edges in E′ separates the 1-
skeleton of T into (at least) two connected components. In this case, Theorem 4.3
tells us that
∑
e∈E′(F )
δ′(e) ≥ 2πχ(F ) −K(F ).
A drawback of both conditions 2.2 and Theorem 4.3 is that they requir e their
respective inequalities to be checked for every subcomplex of T in order to verify
whether a given assignment of dihedral angles is admissible. It is not h ard to see
that this requirement can be weakened somewhat.
Let F be the subcomplex in question.
Observation 4.4. It can assumed that every edge in E(F ) is an edge of at least
one face.
Observation 4.5. The 1-skeleton of the Poincar´ e dualF ∗ of F can be assumed
connected – this is somewhat stronger than saying that F is connected.
Observation 4.6. It can be assumed that the 1-skeleton of
F
∗
– the Poincar´ e
dual of the complement of F – has no isolated vertices.
It is straightforward to check all of the above observations.
In the special situation where δ(e) ≤π for all e ∈E(T ) – that is, δ is Delaunay,
one can further assume that every face f of
F is adjacent to at most one face of
F . Otherwise, adjoin f to F , to create a new complex F ′. This complex has one
more face than F , but its sum of dihedral angles is at most π greater than that of
F . Hence, it is enough to check that F ′ satisﬁes the hypotheses of Theorem 4.3, or
the conditions 2.2.
Definition 4.7. A simple subcomplex of T is a subcomplex F such that both F
and T \F are connected.
Theorem 4.8. To verify that Conditions 2.1 and 2.2 (or equivalently, cond itions
of Theorem 4.3[(b)]) hold for all subcomplexes of T , it is necessary and suﬃcient
to check them for simple subcomplexes.
· 12
Proof. By Observation 4.5, it is enough to check the connected subcomplex es of
T . If such a subcomplex F is simple, then we are done. Otherwise, its complement
is not connected. Let C be a connected component of the complement of F .
Lemma 4.9. The complex C is simple.
Proof. By construction, C is connected. Also, every point of T \C can be con-
nected by a path to a point of F . Since F is assumed connected, the lemma follows.
Consider F ′ = F ∪ C . By assumption, F ′ ⁄=T. Now

 ∑
e∈E(F )
∆( e) −π|F (F )|

 +

 ∑
e∈E(C)
∆( e) −π|F (C)|

 −
∑
∂
C (12)
=

 ∑
e∈E(F ′)
∆( e) −π|F (F )′|

. (13)
By lemma 2.5 (more precisely, a version for simple complexes),

 ∑
e∈E(C)
∆( e) −π|F (C)|

 −
∑
∂
C < 0, (14)
thus,

 ∑
e∈E(F )
∆( e) −π|F (F )|

>

 ∑
e∈E(F ′)
∆( e) −π|F (F )prime|

. (15)
Thus, in order to check that condition 2.2 holds for F , it is enough to check
that it holds for F ′. The proof of Theorem 4.8 is ﬁnished by the obvious induction
argument on the number of connected components of the complem ent of F .
In the case where T is a genuine simplicial complex (that is, two cells intersect
in a lower-dimensional cell), simple subcomplexes corresponds to non-coterminous
minimal cutsets of edges of T :
Definition 4.10. A collection C of edges of T is a cutset if removing the edges
in C disconnects the 1-skeleton of T . A cutset C is minimal if no proper subset of
C is a cutset. A cutset C is coterminous if all of the edges in C are incident to the
same vertex.
In other words, a minimal cutset corresponds to a separating simp le curve in
the Poincar´ e dualT ∗ of T (the curve need not be closed if T has boundary). A
coterminous cutset corresponds to a boundary of a face in the du al. The non-
coterminous simple cutset corresponding to the subcomplex F is nothing other
than the set of edges E′(F ) deﬁne just before the statement of theorem 4.3.
In the case where the surface S is a ﬂat disk, theorems 3.3, 1.6, 4.3, and 4.8
immediately imply:
· 13
Theorem 4.11. Let T be a triangulation of the disk, let ∆ : E(T ) → (0,π ] be
an assignment of dihedral angles to the edges of T , let V∂ (T ) be the set of boundary
vertices ofT and let Λ : V∂ (T ) → (0,π ] be the assignment of boundary angles. Then,
there exists a collection of points p1,...,p V (T ) in the plane E2 whose Delaunay
triangulation is combinatorially equivalent to T , has dihedral angles given by ∆ ,
and whose convex hull is a polygon with angles given by Λ , if and only if:
—If v is an interior vertex of T , then
∑
e ∈E(T ) incident to v
(π − ∆( e)) = 2π. (16)
—If v is a boundary vertex of T , then
∑
e ∈E(T ) incident to v
(π − ∆( e)) + (π − Λ(v)) = 2π. (17)
—If E is a non-coterminous minimal cutset corresponding to a simp le closed curve
in the Poincar´ e dualT ∗ of T , then
∑
e∈E
(π − ∆( e))> 2π. (18)
—If E is a non-coterminous minimal cutset not corresponding to a s imple closed
curve in T ∗, and E separates the boundary vertices of T into two groups v1,...,v k
and vk+1,...,v |V∂ (T )|, then
∑
e∈E
(π − ∆( e)) +
k∑
i=1
(Π − Λ(vi))> 2π. (19)
Remark. Theorem 4.11 is nothing but one of the main results (Theorem 0.1) of
[20], stated in a diﬀerent language (without mentioning convex ideal p olyhedra), so
we have succeeded in deducing that theorem in a purely combinatoria l way from
the results of [19]. In addition, Theorem 4.8 is seen to be a direct gene ralization of
[20][Theorem 0.1] to a characterization of dihedral angles of Delauna y triangulations
of arbitrary, possibly singular, Euclidean surfaces.
