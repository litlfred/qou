---
doc_id: arxiv-1002.0126v1
doc_title: "An introduction to the volume conjecture"
section_id: sec-009-42-geometric-interpretation-of-the-limit
section_title: "Geometric interpretation of the limit"
section_number: 4.2
pages: 26-29
source_pdf: 1002.0126v1.pdf
source_sha256: ea218a0586a13490
doc_brief: "An introduction to the volume conjecture — This is an introduction to the Volume Conjecture and its gene r- alizations for nonexperts."
---
geometric interpretation of the limit (4.8).
Since V (z1, z2, . . . , zc) is the sum of the terms as in (4.4), we ﬁrst describe a
geometric meaning of Li 2(ζ±i
N ).
Recall that an ideal hyperbolic tetrahedron can be put in H3. Regarding the
xy-plane as the complex plain, we can assume that the three of the fou r (ideal)
vertices are at 0, 1 and z∈ C (Im z > 0), respectively (Figure 31). Thus the set
⇒
Figure 31. Parametrization of ideal hyperbolic tetrahedra
{z∈ C| Im z > 0} gives a parametrization of ideal hyperbolic tetrahedra. We
denote by ∆( z) the hyperbolic tetrahedron parametrized by z.
The volume of ∆( z) is given as follows (see for example [31, p. 324]):
(4.10) Vol(∆( z)) = Im Li 2(z) + log|z| arg(1− z).
So we expect V (x1, x2, . . . , xc) gives the sum of the volumes of certain tetrahedra
related to the knot.
In fact we can express the volume of the knot complement in terms o f V (z1, z2, . . . , zc)
[33, 40].
We follow [33] to describe this.
We decompose the knot complement into topological, truncated tet rahedra. To
do this we put an octahedron at each positive crossing as in Figure 32 , where i,
j, k and l are labeling of the four arcs around the vertex. Then decompose t he
AN INTRODUCTION TO THE VOLUME CONJECTURE 27
⇒
Figure 32. An octahedron put at a crossing
octahedron into ﬁve tetrahedra as in Figure 33, where the four of them are decorated
with ξi
N , ξ−j
N , ξk
N and ξ−l
N , respectively and the one in the center is decorated with
ξm
N , where m := l− i = j− k. Here each truncated tetrahedron is just a topological
one with some decoration.
Figure 33. decomposition of the octahedron into ﬁve tetrahedra
Now only two of the vertices are attached to the knot. We pull the t wo of the
remaining four vertices to the top (+ ∞) and the other two to the bottom ( −∞)
as shown in Figure 34. We attach ﬁve tetrahedra to every crossing (if the crossing
is negative, we change them appropriately) in this way. At each arc t wo faces
meet, and we paste them together. Thus we have a decomposition o f S3\ (K∪
{+∞,−∞}). By deforming this decomposition a little we get a decomposition of
S3\K by (topological) truncated tetrahedra, decorated with complex n umbers ξ±ik
N
(k=1,2,. . . ,c).
Next we want to regard each tetrahedron as an ideal hyperbolic on e.
Recall that when we approximate the summation in (4.5) by the integr al in (4.6)
we replace ξik
N with a complex variable zk. Following this we replace the decoration
ξik
N for a tetrahedron with a complex number zk. Then regard the tetrahedron
decorated with zk as an ideal hyperbolic tetrahedron parametrized by zk.
28 HITOSHI MURAKAMI
Figure 34. Pull the vertices to + ∞ and−∞.
So far this is just formal parametrizations. We need to choose app ropriate values
for parameters so that the tetrahedra ﬁt together to provide a complete hyperbolic
structure to S3\ K. To do this we choose z1, z2, . . . , zc so that:
• Around each edge several tetrahedra meet. To make the knot co mplement
hyperbolic, the sum of these dihedral angles should be 2 π,
• Even if the knot complement is hyperbolic, the structure may not be com-
plete. To make it complete, the parameters should be chosen as follo ws.
Since we truncate the vertices of the tetrahedra, four small tria ngles
appear at the places where the vertices were (see Figure 31 for th e triangle
associated with the vertex at inﬁnity). After pasting these triang les make a
torus which can be regarded as the boundary of the regular neighb orhood
of the knot K. Each triangle has a similarity structure provided by the
parameter zk. We need to make this boundary torus Euclidean.
See [34, Chapter 4],[31, § 2] for more details.
Surprisingly these conditions are the same as the system of equatio ns (4.9) that
we used in the steepest descent method! Therefore we can expec t that a solution
(x1, x2, . . . , xc) to (4.9) gives the complete hyperbolic structure.
Then, what does V (x1, x2, . . . , xc) = 2 π√−1 limN →∞ log
(
JN (K, ξN )
)
/N mean?
Recall the formula (4.10) and that V (x1, x2, . . . , xc) is a sum of dilogarithm
functions and logarithm functions. Using these facts we can prove
Im V (x1, x2, . . . , xc) = Vol(S3\ K),
that is,
Im
(
2π
√
−1 lim
N →∞
log
(
JN (K, ξN )
)
N
)
= Vol(S3\ K).
So we have proved
2π lim
N →∞
log|JN (K, ξN )|
N = Vol(S3\ K),
AN INTRODUCTION TO THE VOLUME CONJECTURE 29
which is the Volume Conjecture (Conjecture 3.1).
