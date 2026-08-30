---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-009-6-delaunay-triangulations-of-infinite-sets-of-po
section_title: "DELAUNAY TRIANGULATIONS OF INFINITE SETS OF POINTS"
section_number: 6
pages: 16-17
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
In this section we will show that theorem 3.1 for singular Euclidean str uctures can
be extended without change to inﬁnite locally ﬁnite complexes:
Theorem 6.1. LetT be an inﬁnite but locally ﬁnite complex, and let ∆ : E(T ) →
(0,π ]. Then there exists a singular euclidean structure on T , with cone points at
vertices of T , whose Delaunay triangulation is combinatorially equival ent to T , and
whose dihedral angles are given by ∆ if and only if each ﬁnite subcomplex F ⊂ T
with E(F ) ⁄= ∅ has positive excess.
There are two ingredients in the argument. The ﬁrst (Lemma 6.2) is a n extension
of section 3, the second (6.3) is a geometric estimate which will enable us to extract
the necessary subsequences.
Lemma 6.2. Let T be a complex, and let ∆ : E(T ) → (0,π ]. Then there exists
a Euclidean structure with cone angles at vertices of T , and dihedral angles given
by ∆ , except at the boundary edges of T , where they are smaller than prescribed by
∆ if the excess of any subcomplex F of T , such that E(F ) ⁄= ∅ is positive.
Remark. Lemma 6.2 can be viewed as a relative version of theorem 3.1.
Proof. The argument parallels very closely that of section 3. The existence of
the desired structure is, as before, equivalent to a negative obje ctive of a linear
program, and as before, we set up a slightly simpler linear program ﬁr st. To wit,
the program L′ is:
Positivity. All angles are strictly positive.
Euclidean Faces. For every face t, αt +βt +γt =π.
Boundary edge dihedral angles. For every boundary edge e = AB, in-
cident to the triangle ABC , γ +xe = ∆( e), where the slack variables
(see the comments following the statement of Theorem 3.2) xe are also
non-negative.
Interior edge conditions. For every interior edge e = AB, incident to
triangles ABC and ABD, α +δ = ∆( e).
We relax the program L′ to a program L′
1 by dropping the requirement that the
angles be strictly positive, make the objective 0, as before, and we see that the dual
to the new weakened linear program L′
1 is the following:
The dual program. Maximize F (u, v) : π ∑
t∈F (T )ut + ∑
e∈E(T ) ∆( e)ve, subject
to the conditions
the inequalities of L∗
1. ut +ve ≤ 0 whenever e is an edge of t.
new inequalities. Whenevere is a boundary edge of T ,ve ≤ 0
· 17
Since the constraints of the above program L′∗
1 are a superset of the constraints
of L∗
1, Theorem 3.3 still tells us that the objective function is maximized if th ere
exists a u, such that ut = −ve = u, for all t ∈ F (T ), e ∈ E(T ). Now, this is not
enough to guarantee that the objective is zero, since the equality case of condition
