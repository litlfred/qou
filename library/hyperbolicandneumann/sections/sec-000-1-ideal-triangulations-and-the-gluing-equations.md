---
doc_id: hyperbolicandneumann
doc_title: "HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP"
section_id: sec-000-1-ideal-triangulations-and-the-gluing-equations
section_title: "Ideal triangulations and the gluing equations"
section_number: 1
pages: 1-3
source_pdf: HyperbolicAndNeumann.pdf
source_sha256: 3d66fe4c64bdc62b
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
2. Volumes and Dehn surgeries 3
3. The Bloch group and the extended Bloch group 7
4. Symplectic properties 9
5. Quantization 10
6. Connections to number theory 12
References 17
Walter Neumann—henceforth simply Walter—has made huge contributions to topology,
singularity theory, and number theory. His work on the combinatorics of triangulations of
3-manifolds and its interactions with algebraic K-theory certainly can be counted as among
the most far-reaching and beautiful of these. In this short note we will try to recount some
of the high points of this work, taking as our starting point the papers [31] (by Walter and
the second author) and [28] (by him alone). In the ﬁrst sections we describe the contents of
these two papers and of related later work of Walter, both alone and with other coauthors,
in some detail, while the ﬁnal sections will present further development of some of these
themes in later work of other people, including ourselves.
1. Ideal triangulations and the gluing equations
The starting point of the paper [31] was Thurston’s amazing insight in the 1980’s that
all 3-dimensional manifolds should be canonically divisible into pieces having a well-deﬁned
geometric structure of one of 8 types, the most important of which is the hyperbolic one.
In conjunction with the famous Mostow ridigity theorem, this means that 3-dimensional
topology becomes a part, ﬁrst of diﬀerential geometry, and then of algebraic number theory,
something that is not at all the case in other dimensions. The main class is that of oriented
hyperbolic 3-manifolds, which have a riemannian metric with constant negative curvature
that can be normalized to −1 and hence are locally isometric to hyperbolic 3-space H 3. Of
particular interest is the volume spectrum, the set of volumes of all complete hyperbolic 3-
manifolds of ﬁnite volume (in which case they are either compact or the union of a compact
part and a ﬁnite number of “cusps” diﬀeomorphic to the product of a half-line and a torus).
These volumes have both striking number-theoretical properties (they belong to the image
under the regulator map of the Bloch group, as discussed in Section 3) and striking metric
1
2 STA VROS GAROUF ALIDIS AND DON ZAGIER
properties (they form a countable well-ordered subset of R>0, as discussed in Section 2), and
the primary goal of the paper [31] was to understand them as thoroughly as possible.
In this section we discuss ideal triangulations and their NZ-equations in some detail.
Ideal triangulations of 3-manifolds with torus boundary components were introduced by
Thurston [32] as a convenient way to describe and eﬀectively compute [5] complete hyperbolic
structures on 3-manifolds. Recall that in hyperbolic geometry an ideal tetrahedron is the
convex hull of four points in the boundary ∂(H 3) ∼= P 1(C ) of 3-dimensional hyperbolic
space H 3. The (orientation preserving) isometry group of H 3 is the group PSL 2(C ), acting
on the boundary by fractional linear transformations of P 1(C ), and since under this group
any four distinct points can be put in standard position (0 , 1,∞,z ) for some z∈ C r{0, 1}
(the cross-ratio of the four points), any (oriented) ideal tetrahedron is the convex hull ∆( z)
for some complex number z ∈ C r{0, 1}, called the shape parameter of the tetrahedron.
This number is not quite unique because of the choice of which three vertices we send to 0,
1 and∞, meaning that the oriented tetrahedra ∆(z), ∆(z′) and ∆(z′′), wherez′ = 1/(1−z)
and z′′ = 1− 1/z, are isometric. In this way one attaches a shape parameter z, z′ or z′′ to
each pair of opposite edges of a given oriented ideal tetrahedron. Note that the shape of a
tetrahedron is an arbitrary complex number not equal to 0 or 1, and whether it has positive,
zero or negative imaginary part is irrelevant to our discussion.
WhenT is an ideal triangulation of a hyperbolic 3-manifold M with N tetrahedra with
shape parameters z1,...,z N, then we get one polynomial equation (“gluing equation”) for
each edge. Speciﬁcally, the shape parameters at that edge of all tetrahedra that are incident
with it must clearly have arguments that add up to 2π (because otherwise the metric would
not be smooth along that edge), but in fact the shape parameters themselves have product +1
by an easy argument. Since each of the possible shape parameters z, z′, z′′ of ∆(z) belongs
to the multiplicative group
⟨
z, 1−z,−1
⟩
, this equation for each edge ei has the form
±
N∏
j=1
z
R′
ij
j (1−zj)R′′
ij = 1. (1)
Since it is easily seen that the number of edges in the triangulation is the same as the
numberN of simplices, this gives usN polynomial equations among theN complex numbers
z1,...,z N. The obvious thought is that this leads to a 0-dimensional moduli space and
explains the rigidity, but this is wrong since rigidity only applies to complete hyperbolic
structures, and in fact the N edge relations are never multiplicatively independent. An
obvious example is that their product is always 1, and this is the only dependence if the
boundary of the 3-manifold is a torus (often called a cusp), but in general there are h
multiplicatively independent relations among the N equations (1), where h is the number
of cusps of the 3-manifold (assuming that all boundary components are tori). Thus the
true expected dimension of the moduli space of hyperbolic structures is in fact h. That
the dimension really is h is an important theorem of Thurston ( §5 of [32]) and was given
a new and simpler proof in [31] using the algebraic structure of the gluing equations. The
0-dimensional moduli space (rigidity) arises when we require the hyperbolic structure given
by the shape parameters zi to be complete, because this entails two further independent
relations at each cusp. Speciﬁcally, each “peripheral curve” (meaning an isotopy class of
HYPERBOLIC 3-MANIFOLDS, THE BLOCH GROUP, AND THE WORK OF W ALTER NEUMANN 3
curves on the torus cross-section of one of the cusps) gives a relation, so if one chooses a
meridian and a longitude (µi,λi) at each cusp i = 1,...,h , one obtains 2h further equations
±
N∏
j=1
z
M′
ij
j (1−zj)M′′
ij = 1, ±
N∏
j=1
z
L′
ij
j (1−zj)L′′
ij = 1, (i = 1,...,h ). (2)
Thus the full set of gluing equations is described by an (N + 2h)× 2N matrixU =
(R′ R′′
M′ M′′
L′ L′′
)
.
It was shown in [31] that the matrix U has some key symplectic properties, of which the
most important (Theorem 2.2) says that
UJ 2NUt =
(
0N,N 02h,N
0N,2h 2J2h
)
, (3)
where J2n :=
( 0 −1n
1n 0
)
, while the others say that the N× 2N matrix R =
(
R′R′′)
has rank
N−h, the full matrix U has rank N +h, and that the space [ U]⊂ R2N spanned by the
rows of U is the orthogonal complement of [R] with respect to the symplectic structure J2N
(Prop. 2.3). The rank statement was then used to prove that the dimension of the above-
mentioned deformation space of (non-complete) hyperbolic structures is at least h, and then
a further argument using Mostow rigidity showed that it is exactlyh. This gives rise in the 1-
cusp case to a polynomialP (m,𝓁 ) = 0, wherem2 and𝓁2 denote the left-hand sides of the two
equations (2) andP is a certain polynomial (a factor of what is now called theA-polynomial)
that was calculated explicitly in [31] for the simplest hyperbolic knot 4 1 (ﬁgure 8). In the
general case the deformation space is a component of the “character variety” as introduced
and studied in [4] and studied later by Walter and his students Abhijit Champanerkar [3]
and Stefan Tillmann [33].
To get a complete manifold with h cusps, we impose h further gluing conditions, namely
the equations (1) and the ﬁrst of each of the equations (2). (But in fact these h meridian
equations together with the edge equations imply the longitude equations, so in the end all
relations (1) and (2) hold.) Now rigidity applies and there are no deformations. But there
is another process, with a lot more freedom, to obtain rigid complete hyperbolic structures
from the original cusped manifold, namely to do a Dehn surgery at some or all of the cusps.
Speciﬁcally, when we do a (p,q )-surgery at a cusp (meaning that we truncate the 3-manifold
at the torus boundary and glue on a solid torus in such a way as to kill the homotopy class
of p times a chosen meridian times q times a chosen longitude), then we impose the gluing
equation m2p𝓁2q = 1, where m2 and𝓁2 as above are the left-hand sides of one of the pairs of
equations (2). In the next section, still following [31], we discuss how the volumes behave
under this process.
