---
doc_id: 18
doc_title: "Combinatorial scalar curvature and rigidity of ball packings"
section_id: sec-004-4-the-space-of-conformal-simplices
section_title: "The space of conformal simplices"
section_number: 4
pages: 5-7
source_pdf: 18.pdf
source_sha256: 0b7bf055085cb04b
toc_source: inferred
doc_brief: "Combinatorial scalar curvature and rigidity of ball packings — 11 sections: Front matter; Introduction; Conformal simplices"
---
In this section we will describe the space of Euclidean conformal sim-
plices CT introduced in section 1. The ﬁrst observation is the following:
56
DARYL COOPER AND IGOR RIVIN
Lemma 4.1. A simplex T is conformal if and only if there exists a unique
sphere sT which is tangent to all of the edges of T. Furthermore, the point
of tangency of sT with the edge eij is at distance ri from vi.
Proof. We will show this result in all dimensions greater than 1. The “if”
direction is trivial. We will show the “only if” direction by induction on
dimension. In dimension 2, where all triangles are conformal, the result is
obvious.
Now let T be a conformal simplex with radii ri. First note that there is
a unique sphere s tangent to e1j, j̸ = 1. such that the points of tangency
are r1 away from v1. Consider the intersection of s with one of the faces of
T containing v1 – by induction we know that that the lower dimensional
sphere is tangent to all of the edges of that face. Since all edges of T belong
to a face containing v1, the lemma follows.
□
Now, ﬁrst normalize so that the radius of st is equal to 1, and consider
the pattern of circles formed on sT by the spheres of radii ri centered at
the vertices of T. These circles are mutually tangent. Conversely, any such
pattern of circles C determines a conformal simplex. Since for any two cir-
cle packings C1 and C2 of the sphere S2 whose nerve is the simplex graph,
there is a conformal transformation sending C1 to C2 (this is elementary ge-
ometry, not requiring the Andreev-Thurston theorem; in particular, it also
works in any dimension), the set of such packings can be naturally identi-
ﬁed with the group of conformal transformations of the sphere – PSL(2, C).
Since we are only interested in the congruence class of the conformal sim-
plex T, and are no interested in which way it is pointing, we must further
normalize by factoring out the rotation group SO(3). What we have just
determined is:
Theorem 4.2. The space of isometry classes of Euclidean conformal sim-
plices CT can be naturally identiﬁed with the hyperbolic space H3. In par-
ticular, CT is homeomorphic to the ball B4 = H3 × R.
Note. The discussion above applies just as well to hyperbolic conformal
simplices, except that since we can no longer normalize by ﬁxing the radius
of the mid-sphere st, and so CH ≃H3 × R+, where CH is the deformation
space of hyperbolic conformal simplices.
It will be useful to know exactly how CT is parametrized by our coor-
dinates, in particular, what the boundary of CT (as a subset of R4) looks
like. Note that while for any three positive real numbers r1, r2, and r3,
the sums r1 + r2, r1 + r3, and r2 + r3 satisfy the triangle inequality, not
every positive quadruple r = (r1, r2, r3, r4) deﬁnes a geometric conformal
simplex. Degeneracy occurs when r4 is large enough so that the sphere
COMBINATORIAL SCALAR CURVATURE
57
of radius r4 is large enough to be tangent to the other three spheres, yet
small enough that its center v4 lies in the plane deﬁned by v1, v2, and v3.
This condition is deﬁned by Soddy’s theorem – below we state a version
for arbitrary dimension, recently obtained1 by M. Kovalev [3].
Theorem 4.3. Let Si, i = 1, . . . , n + 2, be n + 2 pairwise tangent distinct
spheres in the n-dimensional Euclidean space En, such that Si has radius
Ri. Then
(4.1)
n
n+2

i=1
K2
i =
n+2

i=1
Ki
2
,
where Ki = 1/Ri, if Si does not contain the other spheres, otherwise Ki =
−1/Ri.
While the above theorem is generally quite useful, it is not necessary to
obtain the following observation:
Theorem 4.4. The space CT ⊂R4 is not convex.
Proof. Consider the section C1,1
T
of CT deﬁned by r1 = r2 = 1. We can
think of C1,1
T
as a subset of a plane. As described above, one component
∂1 of the boundary of C1,1
T
is deﬁned by the condition that there are four
mutually-tangent circles in the plane, of radii 1, 1, r3, r4 – C1,1
T
itself lies
above ∂1. Notice that as r4 approaches inﬁnity, r3 also grows, but to a
ﬁnite limit, and so ∂1 is not convex.
□
Note. Using Theorem 4.3, it can actually be shown that ∂1, as deﬁned in
the proof above is strictly concave.
