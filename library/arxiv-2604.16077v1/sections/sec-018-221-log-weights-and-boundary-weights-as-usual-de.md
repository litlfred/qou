---
doc_id: arxiv-2604.16077v1
doc_title: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT"
section_id: sec-018-221-log-weights-and-boundary-weights-as-usual-de
section_title: "Log weights and boundary weights. As usual denote by ¯M the compact manifold with"
section_number: 2.2.1
pages: 13-14
source_pdf: 2604.16077v1.pdf
source_sha256: 2f1140b9d5fee38a
doc_brief: "VOLUME CONJECTURE AND QUANTUM HYPERBOLIC INV ARIANTS: THE FIGURE EIGHT KNOT COMPLEMENT — We compute the real part of the semi-classical limit of the se quence of quantum hyperbolic invariants (QHI)"
---
interiorM ; so ∂ ¯M is a disjoint union of c tori. Recall the holonomy map (10).
It is well-known that, besides the holonomy ρw, a point w ∈ G(T,b ) determines a group
homomorphism
(15) δw : H1(∂ ¯M ; Z) − → C∗
γ ↦− →δw(γ).
Thus we have a map δ : G(T,b ) →H 1(∂ ¯M ; C∗), w ↦→δw. We call δ the dilation factor . The
scalar δw(γ) is the square of one among the two (reciprocally inverse) ei genvalues of ρw(γ),
and can be computed as a signed monomial in the classical shap e parameters wi
k (see [49],
or the formulas in [14, Lemma E.6.8]; these formulas immedia tely follow from (22) below).
If T is a geometric triangulation, as deﬁned in Section 2.1.2, an d w is close enough to the
pointwhyp ∈G(T,b ), then δw is the holonomy of a similarity structure on ∂ ¯M (see, e.g., [14,
Proposition E.6.5], [52, Proposition 2.3]).
Similarly, by adjoining to w ∈ G(T,b ) a compatible system of edge colors d, one can deﬁne
two classes h2 ∈ H 1(M ; Z/2Z) and lκ ∈ H 1(∂ ¯M ; C), such that for all γ ∈ H1(∂ ¯M ; Z) we
have (where j∗ : H 1( ¯M, Z/2) →H 1(∂ ¯M, Z/2) is induced by the inclusion j : ∂ ¯M → ¯M ):
lκ(γ) = Log(δw(γ)) mod( iπZ) (16)
j∗(h2)(γ) = (lκ(γ) − Log(δw(γ)))/iπ mod(2Z).(17)
Let us explain this. To deﬁne the classes lκ and h2, ﬁrst we stipulate that lκ(0) := 0 and
h2(0) := 0, for the 0 classes in H1(∂ ¯M ; Z) or H1(M ; Z/2) respectively. Given a non-zero class
γ ∈H1(∂ ¯M ; Z), we represent it by a union of oriented simple closed curves in∂ ¯M which are
essential (i.e., do not bound a disk) and transverse to the 1-skeleton of ∂T , the triangulation
of ∂ ¯M induced by T . We can assume that these curves have no “back-tracking”, i.e., they
intersect each triangle of ∂T in a disjoint union of segments. Call such curves normal curves
in ∂T . If a triangle F of ∂T is a section of the tetrahedron ∆ of T near one of its vertices,
for every vertex v of F denote by Ev the abstract edge of ∆ containing v, by w(Ev) the
classical shape parameter of Ev, by d(Ev) its color, and by ∗v the branching sign of ∆. Given
a union of normal curves C, we write F : C →Ev to mean that C intersects the triangle F in
subsegments joining the two edges of F havingv has endpoint. We count these subsegments
algebraically, by using the orientation of C: if there are s+ (resp. s−) such segments whose
orientation is compatible with (resp. opposite to) the orie ntation of ∂ ¯M as viewed from v,
then we set ind(C,v ) := s+ −s−. Then, for any non zero class γ ∈H1(∂ ¯M ; Z) represented
by a union of normal curves C in ∂T , we set (the sum is over all the triangles of ∂T )
(18) lκ(γ) :=
∑
F : C→Ev
∗v ind(C,v )
(
Log(w(Ev)) +π
√
−1d(Ev)
)
.
Similarly, we deﬁne the non oriented normal curves in T as transverse to the 2-skeleton and
intersecting each tetrahedron in a disjoint union of segmen ts. For any normal curve in T , we
write ∆ : C → E to mean that C intersects the tetrahedron ∆ in subsegments joining the
faces of ∆ adjacent to an abstract edge E of ∆. For any such a tetrahedron, we denote by
ind(C,E ) the number of these segments, and by d(E) the color of E. Then, for any non-zero
class γ ∈ H1(M ; Z/2) represented by a union of normal curves C in T we have (the sum is
over all the tetrahedra of T )
(19) h2(γ) =
∑
∆ :C→E
ind(C,E )d(E) mod(2 Z).
