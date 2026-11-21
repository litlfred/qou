---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS"
section_id: sec-027-44-an-illustrative-example
section_title: "An illustrative example"
section_number: 4.4
pages: 37-41
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
toc_source: outline
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry between a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
the origin. We equip this with a symplectic form giving the exceptional divisor area c > 0. Let
Clk denote the Cliﬀord algebra associated to a non-degenerate quadratic form on Ck, of total
dimension 2k.
Lemma 4.19. X contains a Lagrangian torus T which, equipped with the Spin structure which
is non-trivial on both factors, has HF(T, T ) ∼= Cl2̸ = 0.
Proof. There is a natural Hamiltonian torus action on C2, which is inherited by the blow-up
since we have blown up a toric ﬁxed point. The relevant moment polytope is depicted in Figure
3; in this ﬁgure the ﬁbre lying over the black dot, placed symmetrically at the “internal corner”
of the polytope, deﬁnes the Lagrangian torus T .
38
IVAN SMITH
Figure 3. A Lagrangian torus in O(−1)
All the holomorphic disks with boundaries on the ﬁbres of the moment map can be computed
explicitly, cf. [19, 7]; in this case the torus bounds 3 families of Maslov index 2 disks, all having
the same area, so T is in fact monotone. The three dotted lines emanating from the black dot
in Figure 3 are schematic images of the three Maslov index 2 disks through a point; the disks
actually ﬁbre over arcs in the aﬃne structure on the moment polytope determined by complex
rather than symplectic geometry, but the disks do intersect the boundary facets as indicated. We
equip T with the Spin structure which is bounding on both factors. The contributions of these
disks to the Floer diﬀerential and product can be determined explicitly exactly as in op. cit.;
the Lagrangian moment map ﬁbres with non-zero Floer cohomology for some Spin structure are
precisely those lying over critical values of the superpotential, which in this example is
W(z1, z2) = z1 + z2 + ecz1z2.
The constituent monomials are indexed by the toric boundary strata of the moment polytope,
cf. [7, Proposition 4.3], with the logarithm of the corresponding coeﬃcient giving the distance
of the deﬁning hyperplane from the origin in R2. There is a unique critical point (−e−c, −e−c)
lying over the ﬁbre of the moment map given by the black dot (c, c) = (−log|z1|, −log|z2|). Since
the critical point is non-degenerate, this torus has HF(T 2, T 2) ∼= Cl2.
□
Remark 4.20. The torus T is actually special Lagrangian with respect to the pullback of the
holomorphic volume form dz1/z1 ∧dz2/z2 from C2. The pullback has ﬁrst order poles along the
proper transforms of the axes and the exceptional divisor, hence any Maslov index 2 disk must
meet this locus transversely once, as in Figure 3.
For another viewpoint on the Lagrangian torus T ⊂O(−1), recall the construction of the
symplectic blow-up. We let
O(−1) =

((z1, z2), [w1 : w2]) ∈C2 × P1 

 z1w2 = w1z2
	
be the standard embedding of the tautological line bundle and write O(−1)δ = Φ−1(B(δ)) for
the preimage of the ball B(δ) ⊂C2 under the ﬁrst projection Φ. The standard symplectic form
giving the exceptional sphere area πχ2 > 0 is just Ωχ = Φ∗ωstd + χ2π∗
P1ωF S, where ωF S is the
appropriately normalised Fubini-Study form on the projective line. The basic observation, see
e.g. [66, Lemma 7.11], is that
(O(−1)δ\O(−1)0, Ωχ) ∼= (B(
p
χ2 + δ2\B(χ), ωstd) ⊂C2.
(4.6)
Thus there is a symplectic form on the blow-up with area c on the exceptional sphere whenever
a ball of radius strictly larger than c/√π embeds in the original space. Now take the equator
S1 ⊂P1 = E inside the exceptional divisor.
Consider the union of the circles inside ﬁbres
lying over the equator which bound disks of area c; from the above discussion, such a tubular
neighbourhood embeds in the blow-up (in general this will be true if c is suﬃciently small, but a
ball of any size ﬁts in C2). The torus T swept out by these ﬁbres of constant radius is Lagrangian,
since via Equation 4.6 it comes from a Cliﬀord-type torus inside a sphere in C2; it is invariant
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
39
under the usual S1 × S1 action, and in fact co-incides with the toric ﬁbre discussed in Lemma
4.19.
To put the reformulation in a more general context, note that we have correspondences
Γ1 = S1
eq ⊂{pt} × P1 ∼= E;
Γ2 ⊂E × X
(4.7)
with Γ2 = ∂νE the 3-sphere which is the boundary of a tubular neighbourhood νE of the ex-
ceptional curve, viewed not as a submanifold in X but in the product E × X. This 3-sphere
is the graph of a Hopf map from C2\{0} →P1. We claim that for suitable symplectic forms,
these correspondences are monotone Lagrangian (compare to Remark 3.5 to see why this is deli-
cate). Let (•, ω)−denote the symplectic manifold (•, −ω). Recall that a co-isotropic submanifold
W ⊂(M, ωM) with integrable characteristic distribution and reduced space (N, ωN) deﬁnes a
Lagrangian graph in (N, ωN)−× (M, ωM).
Lemma 4.21. Equip E = P1 with the symplectic form 2ωF S of area 2π, and equip X = O(−1)
with the symplectic form Ω1 giving the zero-section area π.
Deﬁne ∂νE as the boundary of
the sphere of radius
√
2 in C2, viewed via (4.6) as the boundary of the unit disk subbundle
O(−1)1 ⊂O(−1).
Then the correspondence Γ2 ⊂E−× X associated to νE is a monotone
Lagrangian submanifold.
Proof. The key point is that the symplectic form on P1 obtained by taking the reduction of the
coisotropic submanifold νE ⊂(O(−1), Ω1) has area 2π, even though the zero-section in that line
bundle has area π. This is clear from the description of (4.6), or from a toric picture, Figure 3
(the line parallel to the boundary facet deﬁning the exceptional curve and passing through the
distinguished point • deﬁnes a co-isotropic 3-sphere, and the reduced space is obviously a P1 of
area determined by the radius of the corresponding ball in C2 before blowing up). Therefore,
the co-isotropic Γ2 deﬁnes a Lagrangian graph inside (P1, −2ωF S) × (O(−1), Ω1). On the other
hand, the ﬁrst Chern class of this product is the class (−2, 1) ∈H2(P1) ⊕H2(O(−1)) ∼= Z2, so
Γ2 is indeed monotone.
□
The composite of the two correspondences
Γ1 ◦Γ2 ⊂{pt} × X
is exactly the Lagrangian torus T . This also partially explains the particular choice of Spin-
structure on T ; it should be equipped with a Spin-structure which in the Γ2-direction is inherited
from the ambient correspondence S3, hence on that circle factor we must pick the bounding
structure.
Lemma 4.22. The Lagrangian torus T of Lemma 4.19 has a non-trivial idempotent.
Proof. Cl2 is a matrix algebra, hence splits into two idempotents each of which has endomorphism
algebra of rank 1. More precisely, if Cl2 is generated by x and y of degree 1 subject to xy+yx = 1
with x2 = 0 = y2, then xy = e+ and yx = e−are idempotents; the morphisms between the
corresponding summands of T are HF(e+, e−) ∼= K.
□
Remark 4.23. The proof shows there are two “indistinguishable” idempotents in HF(T, T ), and
one could use either in the construction of the functor below. In fact,
e+ ∼= e−[1]
and
e−∼= e+[1]
(which is compatible with the fact that the double shift is isomorphic to the identity in the
Z2-graded Fukaya category).
The same binary choice appears on the mirror side, when one
considers Kn¨orrer periodicity for Orlov’s derived categories of singularities. In principle, this
choice ﬁbrewise in a family of Cliﬀord-like 2-tori could lead to an obstruction to the existence of
a global idempotent, but this obstruction will vanish when we later blow up the base-locus of a
pencil of hyperplanes.
40
IVAN SMITH
Remark 4.24. Non-triviality of HF(T, T ) implies that the Lagrangian correspondences Γi are
non-trivial elements of their Fukaya categories. Note that the individual correspondences Γ1 ∼= S1
and Γ2 ∼= S3 cannot split for reasons of degree: in both cases only the identity lives in HF ev.
The composite correspondence Γ1 ◦Γ2 has an idempotent summand which deﬁnes a functor
Φ(e+) : F({pt}) →T wπF(X)
(4.8)
which takes the unique Lagrangian submanifold of the base locus {pt} to an object on the RHS
with the same Floer cohomology; i.e. the summand of the functor is fully faithful. To obtain a
slightly less trivial example, one can consider blowing up a collection of points in C2 by equal
amounts.
Taking a common size for the blow-ups implies that the resulting space contains
Lagrangian 2-spheres, which arise from the symplectic cut of trivial Lagrangian cylinders in C2.
Example 4.25. Let p = (0, 0) ∈C2 and consider the arc γ ⊂R+ ⊂C = {w = 0} ⊂C2, with
co-ordinates (z, w) on C2. The blow-up at p is eﬀected symplectically by choosing a ball with
boundary
S3
ε = {|z|2 + |w|2 = ε2}
and quotienting out Hopf circles. Suppose now we consider the circles {|w| = ε} lying over the
arc γ ⊂{w = 0}. The union of these circles is a Lagrangian tube in C2 which meets S3
ε only over
the end-point of γ at the origin, where the intersection is precisely the circle {z = 0, |w| = ε}
which is collapsed in forming the blow-up, cf. Figure 4.
Figure 4. The symplectic cut of a Lagrangian tube in Blp∐q(C2) (the dotted
balls are collapsed in performing the blow-up)
The Lagrangian tube therefore deﬁnes a smooth Lagrangian disk in Blp(C2). If we now blow
up C2 at p = (0, 0) and q = (2, 0), with equal weights c = πε2 at the two-points, there is a
Lagrangian sphere L ⊂Blp∐qC2 in the homology class ±(E1 −E2). This arises from a pair of
such disks, and is naturally a matching sphere associated to a path γ ⊂C = {w = 0} between
the points p = (0, 0) and q = (2, 0).
Lemma 4.26. The torus T ⊂Bl0(C2) meets the Lagrangian disk ∆which is the symplectic cut
of R≥0 × {|w| = ε} cleanly in a circle. The Floer cohomology HF(T 2, ∆) ∼= H∗(S1).
Proof. The disk ∆ﬁbres over the horizontal arc emanating from the vertex on the y-axis in the
moment image of Figure 3. The disk and the torus meet cleanly along the circle where z = ε ∈R+.
We claim the Morse-Bott-Floer diﬀerential vanishes: it is enough to see that HF(T 2, ∆)̸ =
0.
To prove this, we introduce a Lefschetz ﬁbration viewpoint on these constructions.
The
trivial ﬁbration C2 →C which is projection to the z-co-ordinate induces a Lefschetz ﬁbration on
FLOER COHOMOLOGY AND PENCILS OF QUADRICS
41
Bl0(C2) with a unique critical ﬁbre, which contains the exceptional sphere. The vanishing cycle
is homotopically trivial, and the monodromy is Hamiltonian isotopic to the identity. There is a
unique radius of circle centred at the origin in the base, determined by the size c of the blow-up
parameter, for which the Lagrangian torus which is swept out by the vanishing cycle in each
ﬁbre (deﬁned relative to parallel transport along a radial arc) is actually monotone, and this is
our torus T . The disk ∆of Lemma 4.26 is the unique Lefschetz thimble, and the non-vanishing
of HF(T, ∆) is an instance of the general fact that a basis of vanishing thimbles generates a
category containing all weakly unobstructed compact Lagrangians. This is a theorem of [92] in
the case of exact Lefschetz ﬁbrations; Proposition 5.8 explains why the argument applies in the
current setting.
□
From Lemma 4.26 one sees that HF(e±, ∆) ∼= K. In the Fukaya category V of the Lefschetz
ﬁbration, the individual summands e± are isomorphic up to shifts to the disk ∆. We record one
elementary point from this reformulation. Suppose one has an A2-chain of Lagrangian S0’s, i.e.
two zero-spheres V0 and V1 sharing a point, say V0 = {(−1, 0), (0, 0)} and V1 = {(0, 0), (1, 0)} ⊂
C2. We ﬁx real arcs ∆i ⊂C × {0} bounding the Vi and meeting at the origin, with respect
to which we obtain spun Lagrangian 2-spheres ˆVi ⊂Bl3 points(C2), and we consider the Floer
product
HF( ˆV0, ˆV1) ⊗HF(T, ˆV0) −→HF(T, ˆV1).
(4.9)
The relevant Lagrangians ﬁbre, in the Lefschetz ﬁbration described above – locally restricting to
a subspace Bl0(C2) of the 3-point blow-up – over a circle centred at the origin and the positive
and negative real half-lines; the ˆVi are here viewed as compactiﬁcations of Lagrangian disks
ﬁbring over these half-lines. In this local picture, the triangle product must be non-vanishing,
just because the Lagrangian disks are actually isomorphic in the Fukaya category of the Lefschetz
ﬁbration, both being the unique Lefschetz thimble. On the other hand, by the maximum principle
all the holomorphic triangles are local, hence this non-vanishing actually applies to Equation 4.9.
