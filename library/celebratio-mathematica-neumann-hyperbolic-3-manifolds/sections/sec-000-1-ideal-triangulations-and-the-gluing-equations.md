---
doc_id: celebratio-mathematica-neumann-hyperbolic-3-manifolds
doc_title: "Jump to Bibliography by Stavros Garoufalidis and Don Zagier Published: 2023"
section_id: sec-000-1-ideal-triangulations-and-the-gluing-equations
section_title: "Ideal triangulations and the gluing equations"
section_number: 1
pages: 1-4
source_pdf: Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds.pdf
source_sha256: 9e541693c60cbd3f
toc_source: inferred
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
The starting point of the paper [1] was Thurston’s amazing insight in the 1980’s
that all 3-dimensional manifolds should be canonically divisible into pieces having
a well-defined geometric structure of one of eight types, the most important of
which is the hyperbolic one. In conjunction with the famous Mostow rigidity the‐
orem, this means that 3-dimensional topology becomes a part, first of differential
geometry, and then of algebraic number theory, something that is not at all the
case in other dimensions. The main class is that of oriented hyperbolic 3-mani‐
folds, which have a riemannian metric with constant negative curvature that can
be normalized to 
 and hence are locally isometric to hyperbolic 3-space 
. Of
Walter D. Neumann
Walter D. Neumann
⇧
COLLECTION
COLLECTION
CV
Works
Early Life
Perspective
Students
Gallery
Celebration
Splice Diagrams
Lipschitz Geometry
Hyperbolic 3-Manifolds
Geometry of 3-manifolds
Credits
Cover
particular interest is the volume spectrum, the set of volumes of all complete hy‐
perbolic 3-manifolds of finite volume (in which case they are either compact or
the union of a compact part and a finite number of “cusps” diffeomorphic to the
product of a half-line and a torus). These volumes have both striking number-the‐
oretical properties (they belong to the image under the regulator map of the Bloch
group, as discussed in Section  3) and striking metric properties (they form a
countable well-ordered subset of 
, as discussed in Section 2), and the primary
goal of the paper [1] was to understand them as thoroughly as possible.
In this section we discuss ideal triangulations and their NZ-equations in some de‐
tail. Ideal triangulations of 3-manifolds with torus boundary components were in‐
troduced by Thurston [e7] as a convenient way to describe and effectively com‐
pute [e24] complete hyperbolic structures on 3-manifolds. Recall that in hyperbol‐
ic geometry an ideal tetrahedron is the convex hull of four points in the boundary
 of 3-dimensional hyperbolic space 
. The (orientation-pre‐
serving) isometry group of 
 is the group 
, acting on the boundary by
fractional linear transformations of 
, and since under this group any four
distinct points can be put in standard position 
 for some
 (the cross-ratio of the four points), any (oriented) ideal tetrahed‐
ron is the convex hull 
 for some complex number 
, called the
shape parameter of the tetrahedron. This number is not quite unique because of
the choice of which three vertices we send to 0, 1 and 
, meaning that the ori‐
ented tetrahedra 
, 
 and 
, where 
 and 
,
are isometric. In this way one attaches a shape parameter ,  or 
 to each pair of
opposite edges of a given oriented ideal tetrahedron. Note that the shape of a tet‐
rahedron is an arbitrary complex number not equal to 0 or 1, and whether it has
positive, zero or negative imaginary part is irrelevant to our discussion.
When 
 is an ideal triangulation of a hyperbolic 3-manifold 
 with 
 tetrahedra
with shape parameters 
, then we get one polynomial equation (“gluing
equation”) for each edge. Specifically, the shape parameters at that edge of all tet‐
rahedra that are incident with it must clearly have arguments that add up to 
(because otherwise the metric would not be smooth along that edge), but in fact
the shape parameters themselves have product 
 by an easy argument. Since
each of the possible shape parameters , , 
 of 
 belongs to the multiplicat‐
ive group 
, this equation for each edge  has the form
Since it is easily seen that the number of edges in the triangulation is the same as
the number 
 of simplices, this gives us 
 polynomial equations among the 
⇧
complex numbers 
. The obvious thought is that this leads to a 0-dimen‐
sional moduli space and explains the rigidity, but this is wrong since rigidity only
applies to complete hyperbolic structures, and in fact the 
 edge relations are nev‐
er multiplicatively independent. An obvious example is that their product is al‐
ways 1, and this is the only dependence if the boundary of the 3-manifold is a tor‐
us (often called a cusp), but in general there are  multiplicatively independent re‐
lations among the 
 equations (1), where  is the number of cusps of the 3-mani‐
fold (assuming that all boundary components are tori). Thus the true expected di‐
mension of the moduli space of hyperbolic structures is in fact  . That the dimen‐
sion really is  is an important theorem of Thurston (§5 of [e7]) and was given a
new and simpler proof in [1] using the algebraic structure of the gluing equations.
The 0-dimensional moduli space (rigidity) arises when we require the hyperbolic
structure given by the shape parameters 
 to be complete, because this leads to
two further independent relations at each cusp. Specifically, each “peripheral
curve” (meaning an isotopy class of curves on the torus cross-section of one of the
cusps) gives a relation, so if one chooses a meridian and a longitude 
 at
each cusp 
, one obtains 
 further equations
Thus the full set of gluing equations is described by an 
 matrix
It was shown in [1] that the matrix 
 has some key symplectic properties, of
which the most important (Theorem 2.2) says that
where
while the others say that the 
 matrix 
 has rank 
, the
full matrix  has rank 
, and the space 
 spanned by the rows of 
is the orthogonal complement of 
 with respect to the symplectic structure 
(Proposition 2.3). The rank statement was then used to prove that the dimension
of the above-mentioned deformation space of (noncomplete) hyperbolic struc‐
tures is at least  , and then a further argument using Mostow rigidity showed that
⇧
it is exactly  . This gives rise in the 1-cusp case to a polynomial 
,
where 
 and 
 denote the left-hand sides of the two equations (2) and 
 is a
certain polynomial (a factor of what is now called the -polynomial) that was cal‐
culated explicitly in [1] for the simplest hyperbolic knot 
 (figure-8). In the gen‐
eral case the deformation space is a component of the “character variety” as intro‐
duced and studied in [e4] and studied later by Walter and his students Abhijit
Champanerkar [e11] and Stefan Tillmann [e12].
To get a complete manifold with  cusps, we impose  further gluing conditions,
namely the equations (1) and the first of each of the equations (2). (But in fact
these  meridian equations together with the edge equations imply the longitude
equations, so in the end all relations (1) and (2) hold.) Now rigidity applies and
there are no deformations. But there is another process, with a lot more freedom,
to obtain rigid complete hyperbolic structures from the original cusped manifold,
namely to do a Dehn surgery at some or all of the cusps. Specifically, when we do
a 
-surgery at a cusp (meaning that we truncate the 3-manifold at the torus
boundary and glue on a solid torus in such a way as to kill the homotopy class of 
times a chosen meridian times  times a chosen longitude), then we impose the
gluing equation 
, where 
 and 
 as above are the left-hand sides of
one of the pairs of equations (2). In the next section, still following [1], we discuss
how the volumes behave under this process.
