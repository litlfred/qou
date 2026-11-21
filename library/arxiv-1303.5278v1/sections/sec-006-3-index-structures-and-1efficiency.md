---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-006-3-index-structures-and-1efficiency
section_title: "Index structures and 1–efficiency"
section_number: 3
pages: 9-16
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
We ﬁrst give a sketch proof of Theorem 1.5, showing that a semi–angle structure implies
1–eﬃciency. We follow [KR05] and indicate the required small modiﬁcation. Suppose that M
is oriented with cusps and has an ideal triangulation T with a semi-angle structure. Assume
that there is an embedded normal torus or Klein bottle or sphere or projective plane, where
the normal torus is not a peripheral torus. Firstly, exactly as in [Lac00b] the latter two cases
are excluded by a simple Euler characteristic argument. Similarly, if there is a cube with
knotted hole bounded by an embedded normal torus, then a barrier argument as in [JR03]
establishes that there is a normal 2-sphere bounding a ball containing this normal torus,
which is a contradiction. Embedded Klein bottles are excluded, so we are reduced to the
cases of an embedded essential non peripheral normal torus or a normal torus bounding a
solid torus.
In both cases, there is a sweepout between the normal torus and a peripheral normal
torus (for essential tori) or to a core circle of the solid torus. By a minimax argument (see
[Rub97], [Sto00]), there is an almost normal torus associated with this sweepout. This is
either obtained by attaching a tube parallel to an edge to a normal 2-sphere or has a single
10 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
properly embedded octagonal disc in a tetrahedron and a collection of normal triangular and
quadrilateral discs. The ﬁrst case is excluded, since we have ruled out such normal 2-spheres.
The semi-angle structure now implies that a standard combinatorial Gauss-Bonnet argu-
ment can be applied. Each polygonal disc in our torus has curvature given by Σiαi−(n−2)π,
where n is the number of edges of the disc and αi are the interior angles at the vertices of
the disc. Gauss-Bonnet then says that the sum of the curvatures of all the discs is zero,
since the Euler characteristic of the torus is zero. Every normal triangular disc contributes
zero and each normal quadrilateral is non-positive in the curvature sum. On the other hand,
any embedding of an octagon into an ideal tetrahedron with a semi-angle structure gives a
strictly negative contribution. See Figure 3. Hence the Euler characteristic of such a surface
cannot be zero and there could not have been an embedded normal torus to begin with. This
completes the sketch proof.
□
α
α
α
α
γ
γ
β
β
Figure 3. A normal octagon in a tetrahedron with a semi-angle structure
with angles α, β, γ ∈[0, π]. The curvature of this octagon is 4α + 2β + 2γ −
(8 −2)π = 2α + 2π −6π = 2α −4π < 0.
A useful observation (see [KR05]) following from Theorem 1.5 is the following;
Corollary 3.1. Suppose that T is an ideal triangulation of an oriented 3-manifold M with
cusps. If M is an-annular and T admits a semi-angle structure then M is strongly 1-eﬃcient.
Proof. The key observation is that the semi-angle structure on T lifts to a semi-angle structure
on the lifted triangulation eT, for any covering space f
M of M. Assume that there is an
immersed normal torus T in M which is not a covering of the peripheral torus. If f
M is chosen
as the covering space whose fundamental group corresponds to the image of π1(T), then T
lifts to a normal torus eT so that the inclusion map induces an onto map π1( eT) →π1(f
M).
We can now use eT as a barrier (see [JR03]) to produce an embedded normal non-peripheral
torus T ∗, which is either essential and isotopic into a boundary cusp, or bounds a solid torus
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
11
or cube with knotted hole. (Here the an-annular assumption is used to show that the covering
space f
M is atoroidal). The rest of the argument is exactly the same as in Theorem 1.5.
□
Proof of Theorem 1.2. We closely follow Luo–Tillmann [LT08]. We use the following version
of Farkas’ lemma, which is given as Lemma 10 (3) in [LT08]:
Lemma 3.2. Let A be a real K × L matrix, b ∈RK, and · denote the usual Euclidean inner
product on RK. Then {x ∈RL | Ax = b, x > 0}̸ = ∅if and only if for all y ∈RK such that
ATy̸ = 0 and ATy ≤0, one has y · b < 0.
For our purposes, Ax = b is the matrix form (4) of the generalised angle structure equa-
tions, so b = (2π, . . . , 2π, π, . . . , π)T. Consider a particular quad-choice Q, as in Deﬁnition
2.12. If there is to be an index structure, then we must be able to ﬁnd the appropriate
generalised angle structure x. That is, xl > 0 if l corresponds to one of the Qn, and xl can
have any real value if not. We refer to the former as restricted variables, and the latter as
unrestricted variables.
The problem with applying Farkas’ lemma directly is that it applies to the set of solutions
{Ax = b | x > 0}. That is, all variables are strictly positive. However, we use a standard
trick: for each unrestricted variable xl, introduce a new variable x′
l. The new variable acts
precisely like −xl, so the old xl can be written in the new coordinates as xl −x′
l. This allows
both new variables xl, x′
l > 0, making them restricted variables, so that Farkas’ lemma can
be applied.
The eﬀect that this has on the matrix A is as follows: We get a new column after each
unrestricted xl for x′
l, and the values in the new column are the negatives of the values in
the column for xl.
Now we apply Farkas’ lemma.
We get a solution to our system if and only if for all
y ∈RK such that ATy̸ = 0 and ATy ≤0, we have y · b < 0. The transposed matrix AT has
dual variables (z1, ..., zn, w1, ..., wt), where the wi correspond to the tetrahedra and the zj
correspond to the edges. The dual system AT(z, w)T ≤0 is given by inequalities:
wi + zj + zk ≤0
whenever the ith tetrahedron contains a quad that faces the edges j and k (which may not
be distinct). This holds for all the rows corresponding to the xl, and we get the following
for the x′
l:
−(wi + zj + zk) ≤0
The two of these together imply that wi + zj + zk = 0 for the quads corresponding to
unrestricted angles, while wi + zj + zk ≤0 for restricted angles. The rest of the argument is
the same as in [LT08], as follows.
Kang and Rubinstein [KR04] give a basis of the normal surface solution space C(M; T)
which consists of one element for each edge and one element for each tetrahedron of T.
For the edge e, the corresponding basis element has each of the quad types in the normal
quadrilateral type sequence for e with coeﬃcient −1 (or −2 if that quad appears twice), and
each of the triangle disc types that intersect e with coeﬃcient +1. For each tetrahedron σ,
the corresponding basis element has each of the quad types in σ with coeﬃcient −1, and
each of the triangle disc types in σ with coeﬃcient +1.
12 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
If we have a solution to the dual system, then we can form a normal surface solution class
Ww,z as a sum of tetrahedral and edge basis elements with coeﬃcients given by the wi and zj
corresponding to their tetrahedra and edges respectively. There is a linear functional χ∗on
R7n called the generalised Euler characteristic, which agrees with the Euler characteristic in
the case of an embedded normal surface represented by an element of C(M; T). It is shown
in [LT08] that the generalised Euler characteristic χ∗(Ww,z) is equal to y · b, and that the
normal quad coordinates of Ww,z are given by −(wi+zj+zk). From the above inequalities, we
ﬁnd that the obstruction classes are solutions to the normal surface matching equations with
zero quad coordinates for unrestricted angles, non-negative quad coordinates for restricted
angles (i.e. the quads speciﬁed by the quad-choice Q), at least one quad coordinate strictly
positive, and generalised Euler characteristic χ∗(Ww,z) ≥0.
If there are any negative triangle coordinates, we can add vertex linking copies of the
boundary tori to the solution until all normal disc coordinates are non-negative. Now, since
at most one quad coordinate in each tetrahedron is non-zero, we can in fact realise the
normal surface solution class as an embedded normal surface, and so the generalised Euler
characteristic is equal to the Euler characteristic. Therefore, an obstruction class to this
quad-choice having an associated generalised angle structure is an embedded normal sphere,
projective plane, Klein bottle or torus, with the only quads appearing being of the quad
types given by the quad-choice. Thus, if the triangulation is 1-eﬃcient, then there can be
no such obstruction.
The above argument shows that a 1-eﬃcient triangulation admits an index structure. For
the converse, note that if a triangulation is not 1-eﬃcient, then there is an embedded normal
sphere, projective plane, Klein bottle or non-vertex linking torus. This must then have at
least one non-zero quad coordinate, and since it is embedded, there can be only one non-zero
quad coordinate in each tetrahedron. Choosing these quad types in the tetrahedra containing
the surface, and arbitrarily choosing quad types in any other tetrahedra, we construct a quad-
choice that by the above argument cannot have a suitable generalised angle structure, and
so there is no index structure. This completes the proof of Theorem 1.2.
□
Corollary 3.3. Suppose that M is a compact oriented irreducible 3-manifold with incom-
pressible tori boundary components and no immersed incompressible tori or Klein bottles,
except those which are homotopic into the boundary tori. Then M admits an ideal trian-
gulation T having an index structure.
Moreover if M has no essential annuli (i.e M is
an-annular) then for any ﬁnite sheeted covering space f
M, the lifted triangulation also admits
an index structure.
Proof. To construct 1-eﬃcient triangulations, we can use a construction of Lackenby [Lac00a].
He proves that if M is a compact oriented irreducible 3-manifold with incompressible tori
boundary components and M has no immersed essential annuli, except those homotopic into
the boundary tori, then M admits a taut ideal triangulation T. Then by Corollary 3.1 such
triangulations are strongly 1-eﬃcient. Note that the lift of such a triangulation to any ﬁnite
sheeted covering space is also 1-eﬃcient.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
13
There is a remaining case of small Seifert ﬁbred spaces. For these are precisely the oriented
3-manifolds with tori boundary components which admit essential annuli, but no embedded
incompressible tori which are not homotopic into the boundary components.
Such examples have base orbifold either a disc with two cone points or an annulus with
one cone point or Möbius band with no cone points. The cone points are the images of the
exceptional ﬁbres in the Seifert structure. These manifolds have immersed incompressible
tori, but do not have embedded incompressible tori or Klein bottles, except in the case
where the base orbifold has orbifold Euler characteristic zero: a disc with two cone points
corresponding to exceptional ﬁbres of multiplicity two or orbit surface a Möbius band with
no cone points. This represents two diﬀerent Seifert ﬁbrations of the same manifold. We
exclude this latter case.
Now to construct a suitable ideal triangulation, note that these Seifert ﬁbred spaces M are
bundles over a circle with a punctured surface of negative Euler characteristic as the ﬁbre.
To see this, note that M is Seifert ﬁbred over an orientable base orbifold B with χorb(B) < 0.
Then M admits a connected horizontal surface F which is orientable with χ(F) < 0 since
F is an orbifold covering of B. (A surface is horizontal if it is everywhere transverse to the
Seifert ﬁbration.) Since M is orientable it follows that F non-separating, so M ﬁbres over
the circle with F as ﬁbre (see, for example, [Hat07, sections 1.2 and 2.1].)
After Lemma 6 in [Lac00a], it is shown that, starting with any ideal triangulation of the
punctured surface F, a bundle can be formed as a layered triangulation. This is done by
realising a sequence of diagonal ﬂips on the surface triangulation needed to achieve any
given monodromy map. Such a triangulation then gives an ideal triangulation with a taut
structure. So by Theorem 1.5 these are 1-eﬃcient triangulations and hence admit index
structures.
□
Remark 3.4. The small Seifert ﬁbred spaces from the proof of Corollary 3.3 have ﬁnite
sheeted coverings with embedded incompressible tori so that the lifted triangulations do not
all admit index structures, in contrast with the hyperbolic case.
Example 3.5. The trefoil knot complement has an ideal layered triangulation with two
tetrahedra and two edges, one of degree 2 and one of degree 10. See Figure 4. The comple-
ment of the trefoil knot can be seen as a punctured torus bundle with monodromy given by
RL−1, where
L =

1
0
1
1

R =

1
1
0
1

.
Following the caption of Figure 4, we obtain a triangulation of the complement of the trefoil
consisting of two tetrahedra. The matrix form of the generalised angle structure equations
for this triangulation is




1
1
0
0
0
0
1
1
2
2
2
2
1
0
1
0
1
0
0
1
0
1
0
1











Z1
Z2
Z′
1
Z′
2
Z′′
1
Z′′
2







=




2π
2π
π
π



.
14 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
L−1
R
(0, 0)
(1, 0)
(1, 1)
(0, 1)
(0, 1)
(0, 0)
(1, 0)
(1, 1)
(0, −1)
(1, 1)
(0, 0)
(1, 0)
Figure 4. A layered triangulation of the complement of the trefoil knot, seen
as a punctured torus bundle.
On the left, the monodromy is decomposed
into generators which act on the punctured torus. The diagrams are shown
sheared to highlight the fact that the monodromy has the eﬀect of rotation
by −π/3. The arrows show where edges of a triangulation of the punctured
torus map to under the generators. In the middle, we realise each change in
the triangulation by layering on a ﬂat tetrahedron. The arrows are shown on
the bottom and top of the stack of two tetrahedra to show the gluing. On the
right, we see the edges after the identiﬁcations induced by gluing the top to
the bottom. There are two tetrahedra and two edges in the triangulation, one
of degree two (shown with a dashed line) and the other of degree ten.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
15
There is a taut structure given by choosing angles (π, π, 0, 0, 0, 0)T. This assigns the angle
π to the quad types facing the degree 2 edge and 0 to all other angles. This taut structure is
compatible with the layering construction. By Theorem 1.5, this triangulation is 1–eﬃcient.
It is easy to see that there are no other semi-angle structures for this particular triangu-
lation, because of the degree 2 edge. However, consistent with Theorem 1.2, it admits an
index structure. To see this, we have to produce a generalised angle structure for each of
the 32 = 9 possible quad-choices. However, by symmetry of the matrix we can reduce this
number to three, represented by the following three pairs of conditions that must be satisﬁed
by three generalised angle structures.
(Z1 > 0, Z2 > 0),
(Z1 > 0, Z′
2 > 0),
(Z′
1 > 0, Z′
2 > 0)
These three representatives are all satisﬁed by, for example, (π, π, x, x, −x, −x)T for any
x > 0.
Note that there is a well-known 6-fold cyclic covering by the bundle which is a product
of a once punctured torus and a circle. This covering is toroidal so we see that there is an
index structure on the trefoil knot space but not on this covering space.
e1
e2
a
b
q
Figure 5. Part of a triangulation that does not admit an index structure,
and part of the corresponding surface. The edge e1 is degree 1, so the two
faces incident to it are identiﬁed (indicated by the arrows).
Example 3.6. We give an example of a subset of a triangulation consisting of two tetrahedra
identiﬁed in a particular way. Namely, we have a tetrahedron σ1 with opposite edges e1 of
degree 1 and e2 of degree 2, and another tetrahedron σ2 which is the second tetrahedron
incident to e2. See Figure 5. If these tetrahedra are part of any ideal triangulation with
torus boundary components then that triangulation will not have an index structure, and
will have a normal torus that is not vertex-linking, so it is not 1–eﬃcient.
First we show that there is no index structure. Since e1 is degree 1, for any generalised
angle structure the angle of σ1 at the quad type facing e1 must be 2π. This quad type also
16 STAVROS GAROUFALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
faces e2. The angle of the quad type in σ2 facing e2 must add to 2π to give 2π, and so it
must be zero. Therefore this angle can never be strictly positive, and so there is no index
structure.
Next, we ﬁnd the corresponding embedded normal torus. It has a single quadrilateral in
σ2, labelled q in Figure 5. Two of its triangles are in σ1, also shown. When the two identiﬁed
faces of σ1 are glued to each other, the boundary of the shown surface consists of the two arcs
labelled a and b, on two of the boundary faces of σ2. Now consider the vertex–linking normal
torus T, given by the link of the vertex at which the endpoints of e2 meet. We complete our
surface into an embedded normal torus by deleting from T the normal triangles in σ1 and
σ2 at the endpoints of e2, and gluing the resulting boundary arcs to a and b. The resulting
surface is boundary parallel and so is a torus, but is obviously not vertex–linking since it
contains a quadrilateral.
