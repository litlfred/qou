---
doc_id: arxiv-math-9907032v1
doc_title: "Mathematics Department, California Institute of Technolog y"
section_id: sec-005-4-dihedral-angles-of-delaunay-triangulations
section_title: "DIHEDRAL ANGLES OF DELAUNAY TRIANGULATIONS"
section_number: 4
pages: 9-11
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
In the preceding section it was shown that in order for the linear pro gram L to
have a solution, it is necessary and suﬃcient that the putative dihed ral angles δ(e)
satisfy the inequalities 2.1 and 2.2. Below, we use these to derive anot her set of
necessary conditions 4.3, and show that under the additional assu mption that the
original dihedral angles do not exceed π, these are equivalent to the inequalities 2.2.
The virtue of the inequalities 4.3 is that it is easier to interpret them ge ometrically.
A special case of them is one of the main results of [20] – the connect ion will be
explained in section 6.
First, some deﬁnitions (these are the analogs of the deﬁnitions of s ection 1 without
reference to face angles) – as before T is a triangulation of S, V (T ) is the set of
vertices of T , E(T ) is the set of edges, and F (T ) is the set of faces. We assume
that each edge e ∈E(T ) is given a weight δ(e) ∈ R. The weight δ(e) will be called
the dihedral angle at e. The quantity δ′(e) = π −δ(e) will be called the exterior
dihedral angle at e.
· 10
If v is a vertex of T , then the cone angle Cv is deﬁned to be
Cv =
∑
e incident to v
δ′(e),
while the curvature κv is deﬁned to be κv = 2π −Cv.
Note. The cone angle of a boundary point is, thus, not the same as the bou ndary
angle (in the language of section 1, but smaller by π.
Below, it will often be useful to talk of the Poincar´ e dualofT . Recall that this is
the complex T ∗, such that the set of vertices of T ∗ is in one-to-one correspondence
with the set of faces of T , the set of edges of T ∗ are in one to one correspondence
with the edges of T – two vertices of T ∗ are joined by an edges if and only if the
corresponding faces of T share an edge, and ﬁnally the faces of T ∗ correspond to the
vertices of T – the vertices of a face v∗ of T ∗ correspond to the faces of T incident
to the corresponding vertex v.
Definition 4.1. A subcomplex F of T is closed, if whenever a cell t is in F ,
then so are all of the lower-dimensional cells incident to t.
Definition 4.2. The total curvature of a subcomplex F of T is deﬁned as
K(F ) =
∑
v∈V (F )
κv.
Notation. Let F be a subcomplex of T , and let E′(F ) be the set of those edges
e of T which are not edges of faces of T , but such that at least one endpoint of e
belongs to T . For each edge e of T , deﬁne nF (e) to be the number of endpoints of
e which belong to F .
For example, if e ∈E(F ), then nF (e) = 2; if e /∈E(F ) ∪E′(F ), then nF (e) = 0.
Theorem 4.3. For every non-empty subcomplex F ofT the following are equiv-
alent:
(a). ∑
e∈E′(F )
nF (e)δ′(e) ≥ 2πχ(F ) −K(F ),
with equality if and only if F =T.
(b). Conditions 2.1 and 2.2 hold.
Proof. We will show that (b) ⇒ (a); the converse is immediate.
K(F ) =
∑
v∈V (F )
(2π −
∑
v ∈e
δ′(e)) = 2π|V (F )| −
∑
v∈V (F )
∑
v ∈e
δ′(e). (9)
The last sum of equation 9 can be rewritten thus:
∑
v∈V (F )
∑
e incident to v
δ′(e) = 2
∑
e∈E(F )
δ′(e) +
∑
e∈E′(F )
nF (e)δ′(e). (10)
Finally, using the deﬁnition of δ′(e), and combining equations 9 and 10 it follows
that
K(F ) = 2πχ(F ) + 2(
∑
e∈E(F )
δ(e) −π|F (F )|) −
∑
e∈E′(F )
δ′(e). (11)
· 11
Now, assume that the dihedral angles satisfy the inequalities 2.2. Th is means that
the middle term on the right hand side of equation 11 is non-negative ( and strictly
positive unless F =T ).
