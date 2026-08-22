---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-002-2-necessary-conditions-on-dihedral-angles
section_title: "NECESSARY CONDITIONS ON DIHEDRAL ANGLES"
section_number: 2
pages: 5-7
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
In order for the linear program L to have any chance of having a solution, the
dihedral angles ∆ must satisfy some constraints. Indeed, suppos eL has a solution.
Condition 2.1. All of the dihedral angles must be positive.
· 6
Furthermore, the sum of all of the dihedral angles of all of the edg es of T must be
equal to the sum of all of the angles of all of the faces of T, orF (T )π. On the other
hand, it is almost equally obvious that if t1,...,t n ∈F (T ) is is some proper subset
of the faces of T , then the sum of the dihedral angles at the edges incident to one
of the ti must be strictly greater than the nπ. In other words:
Condition 2.2. Let F ⊆ F (T ), and let E(F ) be the set of all edges incident to
an element of F . Then
∑
e∈E(F )
∆( e) ≥π|F |, (3)
with equality if and only if F =F (T ) or E(F ) = ∅.
Definition 2.3. For a subcomplex F of T , we deﬁne the excess of F to be
excess F =
∑
e∈E(F )
∆( e) −π|F |,
Definition 2.4. An edge e of a subcomplex F of T is a relative boundary edge
of F if it is incident to a top-dimensional face of F on exactly one side, and is not
a boundary edge of T .
The following lemma will prove useful in the sequel.
Lemma 2.5. Let ∆ : E(T ) → (0,π ] be an assignment of dihedral angles to edges
of T satisfying condition 2.2. Let t1,t 2,...,t n be a collection of closed triangles of
T , and let F = t1 ∪t2 ∪... ∪tn – assume F ⁄= T . Let ∑
∂ F be the sum of the
dihedral angles of the boundary edges of F . Then
0< excess F <
∑
∂
F. (4)
Proof. The ﬁrst inequality of 4 is a restatement of Condition 2.2, applied to
the subcomplex F . To show the second inequality, let
F =
⋃
t∈F (T )\{t1,...,t n}
t.
Evidently,
F ∪ F =T,
while
F ∩ F =∂F.
Applying the conditions 2.2 to F , we see that
0<
∑
e∈E(F )
∆( e) −π|F (F )|, (5)
while applying them to F , we see that
0<
∑
e∈E(F )
∆( e) −π|F (F )|. (6)
· 7
Note now that
|F (F )| + |F (F )| = |F (T )|, (7)
while
∑
e∈E(F )
∆( e) +
∑
e∈E(F )
∆( e) −
∑
∂
F =
∑
e∈E(T )
∆( e). (8)
Adding inequalities 5 and 6, and applying equations 7 and 8, we obtain
∑
e∈E(F )
∆( e) −π|F (F )|
<

 ∑
e∈E(F )
∆( e) −π|F (F )|

 +

 ∑
e∈E(
F)
∆( e) −π|F (F )|


=

 ∑
e∈E(F )
∆( e) +
∑
e∈E(
F )
∆( e)

 −
(
π|F (F )| +π|F (
F )|
)
=
∑
e∈E(T )
∆( e) +
∑
∂
F +π|F (T )| =
∑
∂
F,
where the last equality is obtained by applying the equality case of Con dition 2.2.
