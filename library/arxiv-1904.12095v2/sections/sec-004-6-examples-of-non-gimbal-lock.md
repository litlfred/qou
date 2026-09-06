---
doc_id: arxiv-1904.12095v2
doc_title: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner"
section_id: sec-004-6-examples-of-non-gimbal-lock
section_title: "Examples of (non-)gimbal lock"
section_number: 6
pages: 14-15
source_pdf: 1904.12095v2.pdf
source_sha256: 7006b250f0d3c991
doc_brief: "Verified computations for closed hyperbolic 3-manifolds Matthias Goerner — Extending methods ﬁrst used by Casson, we show how to verify a hyper- bolic structure on a ﬁnite triangulation of a closed"
---
This section is giving examples where the conditionΘe = 2π from Theorem 2.3 is known
to be fulﬁlled for most but not all edges. LetT be a ﬁnite, orientable triangulation witho
vertices and m edges. We partition the edges as E ∼ = {e∼
1 , .. .,e∼
l } and E = = {e=
1 ,. .. ,e=
m−l }
depending on whether we know that Θe is close to or, respectively, exactly equal to 2π.
Geometrically, this yields a singular hyperbolic structure with cone singularities along
the edges with Θe∼
i
⁄= 2π. Looking at a vertex v connected to such an edge, its neighbor-
hood is the hyperbolic cone of its link which isS2 topologically but has a spherical cone
structure different from the standard S2. In this section, we extend Deﬁnition 5.1 to the
case where l = |E ∼| might not be 3 o and say that gimbal lock is avoided if Dg has no
kernel.
Example 6.1. Consider the case l = 1 with e∼
1 connecting two distinct vertices v1 and
v2. Assume Θe∼
1 ⁄= 2π. The links of v1 and v2 would have a spherical cone structure
with exactly one singularity. These do not exist, so Θe′ = 2π. This also follows from
Lemma 4.10.
15
Example 6.2 (Gimbal lock). Let us start with a (non-singular) hyperbolic structure onT
such that the edgese∼
1 ,. .. ,e∼
l form a simple closed geodesic. Such a hyperbolic structure
can often be deformed so that the geodesic becomes a cone singularity 3, i.e., such that
Θe∼
1 = · · · =Θe∼
l
are close but not equal to 2π. Note that the spherical structure of the link
of a vertex vi connected to e∼
i and e∼
i +1 gets deformed to have two conical singularities
at antipodal points with equal cone angle. In the language of cocycles, pick a gimbal
loop Γi for vi as in Deﬁnition 4.4 such that the associated gimbal matrix is of the form
mΓi = RΘe∼
i
·
∏
1 ·RΘe∼
i +1
·
∏−1
1 = RΘe∼
i
R−Θe∼
i +1
(6.1)
where ∏
1 ∈ SO3 is a rotation byπ about an axis orthogonal toz. Then mΓi = Id whenever
Θe∼
i
= Θe∼
i +1
, so Dg has a non-trivial kernel. If we add edges to E ∼ such that |E ∼| = 3o,
Dg still has a non-trivial kernel, so we have gimbal lock and thus not a contradiction to
Theorem 5.3.
Example 6.3 (Perturbing previous example to avoid gimbal lock). Consider the situation
in the previous example but move one vertex, say v1, slightly. Assume Θe∼
1 ⁄= 2π. The
link of v1 would be a spherical cone structure with exactly two cone singularities having
distance < π (when scaling such that the curvature is 1). Such a cone structure does
not exist [MP16, Corollary 3.5]. In the language of cocycles, ∏
1 in Equation 6.1 is now
a rotation by an angle strictly between 0 and π, so mΓ1 is the product of two rotations
about two different axes and thus only the identity when Θe∼
l
= Θe∼
1 = 2π. In fact, this
forces Θe∼
1 = · · · =Θe∼
l
= 2π.
Example 6.4 (A non-hyperbolic manifold fulﬁlling all but six edge equations). Consider
the two tetrahedron triangulation ofS3 obtained by identifying the boundary of the ﬁrst
tetrahedron with the boundary of the second tetrahedron via the identity map. Assign
the same length to all edges such that each tetrahedron has a hyperbolic structure in-
dividually but all of the six edges equations are violated. Perform several 1-4 moves on
one or both of the tetrahedra preserving the hyperbolic structure on each tetrahedron.
This gives an example of a non-hyperbolic manifold where more thanm −3o but not all
edge equations are fulﬁlled. Compare this to the ideal case where Neumann-Zagier (see
Appendix) state that all edge equations must be fulﬁlled whenever m − o are fulﬁlled.
We give a characterization of gimbal lock in 1-vertex triangulations later in Theorem 9.5.
