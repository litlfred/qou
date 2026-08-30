---
doc_id: 18
doc_title: "Combinatorial scalar curvature and rigidity of ball packings"
section_id: sec-007-4-the-space-ofconf-ormal-simplices
section_title: "The space ofconf ormal simplices"
section_number: 4
pages: 5-7
source_pdf: 18.pdf
source_sha256: 0b7bf055085cb04b
doc_brief: "Combinatorial scalar curvature and rigidity of ball packings — 19 sections: Introduction; These; Conformal simplices"
---
In this section we will describe the space of Euclidean conformal sim-
plices C
T introduced in section 1. The ﬁrst observation is the following:
56 DARYL COOPER AND IGOR RIVIN
Lemma 4.1. A simplexT is conformal if and onlyif there exists a unique
spheresT which is tangent to all of the edges ofT. Furthermore, the point
of tangencyof sT with the edgeeij is at distanceri fromvi.
Proof. We will show this result in all dimensions greater than 1. The “if”
direction is trivial. We will show the “only if” direction by induction on
dimension. In dimension 2, where all triangles are conformal, the result is
obvious.
Now letT be a conformal simplex with radiir
i. First note that there is
a unique sphere s tangent to e1j,j ⁄=1 . such that the points of tangency
arer1 away fromv1. Consider the intersection ofs with one of the faces of
T containing v1 – by induction we know that that the lower dimensional
sphere is tangent to all of the edges of that face. Since all edges ofT belong
to a face containingv1, the lemma follows. □
Now, ﬁrst normalize so that the radius ofst is equal to 1, and consider
the pattern of circles formed on sT by the spheres of radii ri centered at
the vertices ofT. These circles are mutually tangent. Conversely, any such
pattern of circlesC determines a conformal simplex. Since for any two cir-
cle packingsC1 and C2 of the sphere S2 whose nerve is the simplex graph,
there is a conformal transformation sendingC1 toC2 (this is elementary ge-
ometry, not requiring the Andreev-Thurston theorem; in particular, it also
works in any dimension), the set of such packings can be naturally identi-
ﬁed with the group of conformal transformations of the sphere –PSL (2, C).
Since we are only interested in the congruence class of the conformal sim-
plex T, and are no interested in which way it is pointing, we must further
normalize by factoring out the rotation groupSO(3). What we have just
determined is:
Theorem 4.2. The space ofisometry classes of Euclidean conformal sim-
plices C
T can be naturallyidentiﬁed with the hy perbolic spaceH3. In par-
ticular, CT is homeomorphic to the ballB4 = H3 × R.
Note. The discussion above applies just as well to hyperbolic conformal
simplices, except that since we can no longer normalize by ﬁxing the radius
of the mid-spheres
t, and so CH ≃ H3 × R+, where CH is the deformation
space of hyperbolic conformal simplices.
It will be useful to know exactly how CT is parametrized by our coor-
dinates, in particular, what the boundary of CT (as a subset of R4) looks
like. Note that while for any three positive real numbers r1,r 2, and r3,
the sums r1 +r2,r 1 +r3, and r2 +r3 satisfy the triangle inequality, not
every positive quadruple r =( r1,r 2,r 3,r 4) deﬁnes a geometric conformal
simplex. Degeneracy occurs when r4 is large enough so that the sphere
COMBINATORIAL SCALAR CURVATURE 57
of radius r4 is large enough to be tangent to the other three spheres, yet
small enough that its centerv4 lies in the plane deﬁned byv1, v2, and v3.
This condition is deﬁned by Soddy’s theorem – below we state a version
for arbitrary dimension, recently obtained
1 by M. Kovalev [3].
Theorem 4.3. LetSi,i =1,...,n +2, ben +2 pairwise tangent distinct
spheres in then-dimensional Euclidean spaceEn, such thatSi has radius
Ri. Then
(4.1) n
n+2∑
i=1
K2
i =
(n+2∑
i=1
Ki
)2
,
whereKi =1/Ri, if Si does not contain the other spheres, otherwiseKi =
−1/Ri.
While the above theorem is generally quite useful, it is not necessary to
obtain the following observation:
Theorem 4.4. The space CT ⊂ R4 is not convex.
Proof. Consider the section C1,1
T of CT deﬁned by r1 = r2 =1 . We can
think of C1,1
T as a subset of a plane. As described above, one component
∂1 of the boundary of C1,1
T is deﬁned by the condition that there are four
mutually-tangent circles in the plane, of radii 1,1,r 3,r 4 – C1,1
T itself lies
above ∂1. Notice that as r4 approaches inﬁnity, r3 also grows, but to a
ﬁnite limit, and so∂1 is not convex. □
Note. Using Theorem 4.3, it can actually be shown that∂1, as deﬁned in
the proof above is strictlyconcave.
