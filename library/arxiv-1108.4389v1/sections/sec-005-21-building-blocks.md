---
doc_id: arxiv-1108.4389v1
doc_title: "b partition functions of two mirror 3d N = 2 gauge theories are equal. Three-dimensional N = 2 ﬁeld theories associated to 3-manifolds can be thought of as theories that describe b"
section_id: sec-005-21-building-blocks
section_title: "Building blocks"
section_number: 2.1
pages: 8-11
source_pdf: 1108.4389v1.pdf
source_sha256: d3ac77510654d828
doc_brief: "Gauge Theories Labelled by Three-Manifolds — We propose a dictionary between geometry of triangulated 3-manifolds and physics of three-dimensional N = 2 gauge theories."
---
ated by Thurston [ 6]. More precisely, we wish to build 3-manifolds that support irreducible
ﬂat SL(2, C) connectionsA. For this purpose, it is often convenient to replace ﬂat SL(2, C)
connections with hyperbolic metrics 1 on M — that is, metrics of constant curvature −1.
Then the SL(2, C) structures become geometric, and can be manipulated in a much more
intuitive manner.
The 3-manifolds we consider have two
geodesic boundary
annular cusps
torus cusp
Figure 3: Types of boundaries for M
diﬀerent types of boundary, geodesic bound-
aries and generalized cusps. Geometrically,
the geodesic boundaries are (possibly punc-
tured) geodesic surfaces of any genus, and
come with an induced 2-dimensional hyper-
bolic metric. Any triangulation of M will
determine a triangulation of the geodesic bound-
ary, which will be part of the data in even-
tually deﬁning a 3d gauge theory.
In contrast, “cusp” boundaries do not
have a triangulation that is relevant in deﬁn-
ing 3d gauge theories. Geometrically, cusps
are knotted loci where the hyperbolic metric
onM develops a cone angle, or theSL(2, C)
connection has a speciﬁed monodromy de-
fect. Such loci can be resolved to boundaries
with the topology of either tori T 2 or annuli
S1×I. In either case, the induced metric
on cusp boundaries is Euclidean. Well-studied examples of 3-manifolds with torus cusps are
knot complements in S3. More generally, a cusp might begin and end at punctures on the
geodesic boundary of M (Figure 3). Then, the resolved cusp has the topology of an annulus.
The total boundary of M, with potential components of both types, determines a bound-
ary moduli space of ﬂat connections,
P∂M ={ﬂat SL(2, C) connections on ∂M}
/
(gauge equivalence). (2.1)
1The equivalence between ﬂat connections and hyperbolic geometry results from the fact that the isometry
group of hyperbolic three-space is ( P )SL(2, C), cf. [6, 7, 8, 9]. Almost all ﬂat connections can be realized as
(possibly degenerate) hyperbolic metrics; for further remarks on this in the context of ideal triangulations, see
[10, 11], and Section 4 of [ 12].
– 7 –
This is a symplectic phase space, with a natural holomorphic symplectic form
ω∂M = 1
ℏ
∫
∂M
Tr
(
δA∧ δA
)
. (2.2)
The semiclassical parameter ℏ here governs the normalization of the symplectic form. Ge-
ometrically, ω∂M is an analytic continuation of the Weil-Petersson form in 2-dimensional
hyperbolic geometry. In addition to the phase space P∂M , we can also deﬁne a Lagrangian
submanifold [8]
LM ={ﬂat SL(2, C) connections on M}
/
(gauge) ⊂ P ∂M , (2.3)
which is the set of ﬂat connections on ∂M that can be extended as ﬂat connections inside the
3-dimensional bulk of M. Mathematically, LM is described as the image of the “character
variety” ofM inside the character variety of ∂M .
Our goal now is to construct a manifold M together with the pair (P∂M,LM) from ideal
hyperbolic tetrahedra. This will give us an extremely explicit realization of boundary phase
spaces, Lagrangians, and the symplectic structure (2.2), which in turn will enable us in Section
4 to explicitly build the 3d gauge theory associated to M. As previewed in the introduction,
this 3d theory will depend on M, a triangulation of its geodesic boundary, and a polarization
Π of its phase spaceP∂M — with additional ingredients such asLM playing roles like moduli
spaces of vacua.2
2.1 Building blocks
0
1
∞
z
z
z
￿
z
￿￿
z
￿
z
￿￿
∂H
3
z
￿￿
Figure 4: An ideal hyperbolic
tetrahedron in H3, with vertices
on ∂H3
The fundamental building block used in building our 3-
manifolds M is an ideal hyperbolic tetrahedron (Figure 4).
Geometrically, an ideal tetrahedron ∆ has faces that are
geodesic surfaces and vertices that lie right on the boundary
of hyperbolic 3-space H3. As shown in Figure 4, hyperbolic
3-space can be viewed as the interior of a 3-ball, with the
Riemann sphere as its boundary.
The full hyperbolic structure of ∆ is determined by a
single complex cross-ratio of the positions of its vertices on
∂H3. There are three diﬀerent ways to write this one cross-
ratio, encoded in three diﬀerent edge parameters (z,z′,z′′).
Geometrically, the edge parameters are dihedral angles on
pairs of opposite edges of the tetrahedron [ 6]. Explicitly,
z≡ exp(Z) with Z = (torsion) +i (angle), (2.4)
and similarly for z′ = exp(Z′) and z′′ = exp(Z′′), where “torsion” measures the twisting of
the hyperbolic metric as one moves around an edge. As discussed in [12], the edge parameters
2We note that topologically, one might engineer (resolved) cusp boundaries that look identical to geodesic
boundaries. In particular, networks of annular cusps can assume the topology of nontrivial punctured Riemann
surfaces [13]. Formally, the phase spacesP∂M associated to the two types of boundary would then be equivalent.
However, the natural coordinate systems — and in particular the polarizations — for phase spaces on cusp
and geodesic boundaries are very diﬀerent. In turn, the 3d gauge theories associated to 3-manifolds with the
two diﬀerent types of boundary will be quite diﬀerent.
– 8 –
satisfy zz′z′′ =−1, which leads to the deﬁnition of the boundary phase space
P∂∆ =
{
(z,z′,z′′)∈ (C∗\{1})3⏐⏐zz′z′′ =−1
}
≃ (C∗\{1})2, (2.5)
or in a lifted, logarithmic form,
P∂∆ =
{
(Z,Z′,Z′′)∈ (C\2πiZ)
⏐⏐Z +Z′ +Z′′ =iπ
}
. (2.6)
This is an aﬃne linear space, with symplectic form ω∂∆ = 1
ℏdZ∧dZ′ or, equivalently, a
Poisson structure such that
{Z,Z′} ={Z′,Z′′} ={Z′′,Z} = ℏ. (2.7)
The edge parameters also obey a second relationz+z′−1−1 = 0, which deﬁnes the Lagrangian
submanifold
L∆ ={z +z′−1− 1 = 0} ={eZ +e−Z′
− 1 = 0} ⊂ P∂∆. (2.8)
Any cyclic permutation of the Lagrangian equation (with z→ z′→ z′′→ z) could also be
used.
Topologically, it is convenient to truncate or regularize the
z
￿￿
zz
￿
z
￿￿
z z
￿
Figure 5: A truncated ideal
tetrahedron
four vertices of an ideal tetrahedron, as in Figure 5. The tetra-
hedron then has four large, geodesic boundaries, whose induced
metric is hyperbolic; and four small boundaries at the truncated
vertices, whose induced metric is Euclidean. In fact, the condi-
tionZ+Z′+Z′′ =iπ that deﬁnes the phase space in (2.6) simply
says that the sum of angles in the small Euclidean triangles at
the vertices is always π.
While the Lagrangian equation z +z′−1− 1 = 0 follows
directly from the geometric deﬁnition of ( z,z′,z′′) as equivalent cross-ratios, it also has an
intrinsic description in terms ofSL(2, C) connections. If we view the boundary ∂∆ of a tetra-
hedron as a four-punctured sphere, the phase spaceP∂∆ is the set of ﬂatSL(2, C) connections
with unipotent monodromy around the four punctures. The Lagrangian L∆ is then the sub-
space of ﬂat connections with trivial monodromy — in other words, the ﬂat connections that
can be extended from the boundary into the bulk of the tetrahedron. Understanding this
description explicitly in coordinates (z,z′,z′′) requires a bit of further background, which we
defer to Section 2.3.
In order to deﬁne the gauge theory associated to a tetrahedron, we will need to choose
a polarization Π for its boundary phase space. This means choosing aﬃne linear coordinates
onP∂∆ that are canonically conjugate to each other with respect to the Poisson structure
above, with one coordinate thought of as “position” and the other as “momentum.” There
– 9 –
are three natural possibilities, which we call Π Z, ΠZ′, and ΠZ′′ ,
position X conjugate momentum P
ΠZ : Z Z ′′
ΠZ′ : Z′ Z
ΠZ′′ : Z′′ Z′
(2.9)
Each of these polarizations can be encoded in a choice of opposite edges on the tetrahedron,
such that the edge parameters of the distinguished edges act as “positions” (Figure 6).
z￿￿
zz￿
z￿￿
z z￿
z￿￿
zz￿
z￿￿
z z￿
z￿￿
zz￿
z￿￿
z z￿
ΠZ ΠZ￿ ΠZ￿￿
Figure 6: Natural polarizations for a tetrahedron, with the thickened pairs of opposite edges corre-
sponding to the “position” coordinate.
We can deﬁne a larger class of polarizations by starting with any of those in ( 2.9), and
acting with an aﬃne symplectic transformation Sp(2, Z) ⋉ (iπZ)2. By this we mean taking
the vector
(
position, momentum
)
, multiplying by Sp(2, Z)≃SL(2, Z) matrices, and shifting
both position and momentum by integer multiples ofiπ. For example, instead of ΠZ, we could
have considered polarization Π−
Z in which X− =Z is position and P− =−Z′ is momentum;
then the transformation from ΠZ to Π−
Z is
ΠZ → Π−
Z :
(
X−
P−
)
=
(
1 0
1 1
)(
X
P
)
+
(
0
−iπ
)
. (2.10)
Similarly, to go from ΠZ to ΠZ′, we transform
(
Z′
Z
)
=
(
−1−1
1 0
)(
Z
Z′′
)
+
(
iπ
0
)
, (2.11)
where the matrix involved is ST =
( 0−1
1 0
)
( 1 0
1 1 )∈ Sp(2, Z). The identity ( ST )3 = I corre-
sponds to the fact that three cyclic permutations of shape parameters brings us back where
we started.
