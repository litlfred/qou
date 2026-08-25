---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-004-14-applications-to-knot-theory
section_title: "Applications to knot theory"
section_number: 1.4
pages: 5-7
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
speciﬁc applications of Theorem 1.4. We determine bounds on the cusp
shape of a knot based solely on a diagram of that knot.
Before we state the results, we review some deﬁnitions.
Deﬁnition 1.5. Let K ⊂ S3 be a knot with diagram D(K). Deﬁne a
twist region to be a region of D(K) where two strands of the diagram twist
around each other maximally. Precisely, if D(K) is viewed as a 4–valent
planar graph with over–under crossing information at each v ertex, then a
twist region is a maximal string of bigons in the complement o f the graph
arranged end to end, or a single vertex of the graph adjacent t o no bigons.
We also require the diagram to be reduced, in the sense of the f ollowing
two deﬁnitions. These deﬁnitions are illustrated elsewher e (see e.g. [15],
[12]).
Deﬁnition 1.6. A diagram D(K) is prime if when any simple closed curve
γ intersects D(K) transversely in two points in the interiors of edges, then
γ bounds a subdiagram containing no crossings of the original diagram.
Deﬁnition 1.7. The diagram D(K) is twist reduced if when any simple
closed curve γ intersects D(K) transversely in four points in the interiors
of edges, with two of these points adjacent to one crossing an d two others
adjacent to another crossing, then γ bounds a subdiagram consisting of a
(possibly empty) collection of bigons arranged end to end be tween these two
crossings.
Any diagram of a prime knot or link can be simpliﬁed into a prim e, twist
reduced diagram. If the diagram is not prime, then crossings on one side of
a simple closed curve are extraneous and can be removed. If th e diagram is
not twist reduced, then performing ﬂypes will amalgamate tw o twist regions
adjacent to a simple closed curve into one, reducing the numb er of twist
regions.
6 JESSICA S. PURCELL
For a hyperbolic knot complement, we can choose a horoball ne ighborhood
about the cusp such that a meridian on the boundary of that hor oball has
length 1 (see e.g. [2]). Consider the geodesic arc orthogona l to the meridian
which runs from meridian to meridian on this horospherical t orus. Deﬁne
the length of this arc to be the height of the cusp. Note that when the
meridian is the shortest curve on the cusp (as will be the case in the knots
of this paper), this deﬁnition of height agrees with that in T heorem 1.4.
Let K be a knot in S3 which admits a prime, twist reduced diagram with
at least 2 twist regions, with each twist region containing a t least 6 crossings.
Then it was shown in [12] that S3 − K is hyperbolic. The following theorem
gives bounds on the cusp shape.
Theorem 1.8. Let K be a knot in S3 which admits a prime, twist reduced
diagram with a total of n ≥ 2 twist regions, with each twist region containing
at least c ≥ 116 crossings. In a hyperbolic structure on S3 − K, take a
horoball neighborhood U about K. Normalize so that the meridian on ∂U
has length 1. Then the height H of the cusp of S3 − K satisﬁes:
H ≥ n (1 − f (c))2.
Here f (c) is a positive function of c which approaches 0 as c increases to
inﬁnity.
Additionally, H ≤ n(√
n − 1 + f (c))2.
The function f is given explicitly in Section 6. We can plug in values of
c to obtain more speciﬁc estimates. For example, in Corollary 6.7 we let
c = 145. Then 1 − f (c) is approximately 0 .8154.
Note that the shortest non-meridional slope on the cusp of S3 − K will
have length at least that of the height. So Theorem 1.8 implie s that in this
case, the shortest non-meridional slope has length at least n (1 − f (c))2.
By results of Hodgson and Kerckhoﬀ [14], Dehn ﬁlling along a s lope with
normalized length at least 7 .515 results in a hyperbolic manifold. Corollary
6.7 implies that for a complicated knot, the shortest non-me ridional slope
will have normalized length at least √n(0.8154). Thus the normalized length
of a slope will be larger than 7 .515 whenever n ≥ 85. Thus we have the
following corollary to Theorem 1.8:
Corollary 1.9. Let K be a knot in S3 which admits a prime, twist reduced
diagram with at least 85 twist regions and at least 145 crossings per twist
region. Then any non-trivial Dehn ﬁlling of S3 − K is hyperbolic.
Corollary 1.9 is proven without any reference to the geometr ization con-
jecture. If we assume that conjecture, then we recently prov ed (with Futer
[12]) that the numbers 85 and 145 could be reduced to 4 and 6 res pectively.
However, note the proof of that result gives no geometric inf ormation on
cusp geometry.
The numbers of crossings, 116 and 145, can be reduced signiﬁc antly for
certain classes of knots. We illustrate this in section 6.4 f or 2–bridge knots.
CUSP SHAPES UNDER CONE DEFORMATION 7
