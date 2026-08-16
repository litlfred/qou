---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-006-33-cross-ratio-parameters
section_title: "Cross-ratio parameters"
section_number: 3.3
pages: 16-20
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry STEPHANE BASEILHAC RICCARDO BENEDETTI — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
parameters for R(g,r ) which are related to the shear-bend coordinates for pleated hyp erbolic surfaces.
These parameters are obtained via an idealization procedure that includes the choice of a base point
on the Riemann sphere. We ﬁx this base point as 0. Note that the B+(2, C)-orbit of 0 is the whole of
C, while B−(2, C) ﬁxes 0. Hence the symmetry between Z(T,b )+ and Z(T,b )− given by the map Ψ
in (15) shall be broken.
Deﬁnition 3.6. (Compare with Deﬁnition 2.7.) Let ( K,b ) be any oriented surface branched triangu-
lation. Let z be any PSL (2, C)-valued cocycle on (K,b ). We say that z is idealizable if for any triangle
t of (T,b ) with b-ordered edges e0, e1 and e2, the points u0 = 0, u1 =z(e0)(0) and u2 =z(e2)(0) are
distinct in C. We say that the complex triangle with vertices u0,u1 and u2 is the idealization of t.
Deﬁnition 3.7. Let (T,b ) be an e-triangulation of F obtained from a branched ideal triangulation
(T ′,b ′) of S \V . A cocycle z ∈ Z (T,b )+ is (strongly) idealizable if:
(a) z is idealizable;
(b) Ψ( z) ∈ Z (T,b )−, which cannot be idealizable at the triangles having an edge on ∂F , is nevertheless
idealizable at every other triangle.
QUANTUM HYPERBOLIC GEOMETRY 17
We denote by ZI (T,b )+ the set of (strongly) idealizable cocycles, and we put ZI (T,b )− = Ψ( ZI (T,b )+)
and RI (T,b ) = p+(ZI (T,b )+) = p−(ZI (T,b )−).
Clearly, ZI (T,b )+ is a non-empty dense open subset of Z(T,b )+. If every edge of T has distinct
endpoints (in case we say that T quasi-regular), then RI (T,b ) = R(g,r ). In general, characters of
representations with a free action on a non-empty domain of CP1 (such as quasi-Fuchsian representa-
tions) always belong to RI (T,b ), for any (T,b ). By using the arguments of [22], Theorem 1, it can be
shown that for any character ρ ∈ R(g,r ) of irreducible representations, there exists an e-triangulation
(T,b ) with idealizable cocycles representing ρ. In fact, the union of a ﬁnite number of spaces ZI (T,b )+
cover the whole of R(g,r )irr .
Exponential I-parameters. For any cocycle z ∈ ZI (T,b )+, we associate a non zero complex weight
W +(z)(e) to each edge e ofT that is not contained in ∂F , as follows. Let pe be the initial endpoint of
e, and tl andtr the left and right adjacent triangles (as viewed from e). Locally modify the branching
on tl ∪tr by cyclically reordering the vertices on each triangle, so that pe is eventually the source of
the new branching on both tl and tr. The (+)-exponential I-parameterW +(z)(e) is the cross-ratio
modulus at e of the (possibly degenerate) branched oriented hyperbolic ideal t etrahedron spanned by
the idealization of tr ∪tl, where the branching completes the one of tl ∪tr so that ∗b = 1.
Let us assume now that Ψ( z) ∈ ZI (T,b )−. For each v ∈ V , denote by e1
v and e2
v the edges of the
triangle tv of T ′ having cv as corner. At an edge e of T ′ distinct from any of the ei
v, we deﬁne the
(−)-exponential I-parameterW −(Ψ(z))(e) in the same way as W +(z)(e), but taking the idealization
for Ψ( z) instead of z. If e is one of the ei
v, the formula works as well, except that each left/right
triangle with an edge on ∂F is replaced with the innermost triangle in the corresponding triangle tv
of T ′. Note that tr ∪tl is again a quadrilateral, because 0 is a ﬁxed point of the cocycle values at the
boundary edges of F .
By varying the edge in T or T ′ for every C±, we have two (±)-exponential I parameter maps (recall
that the number of edges of T ′ is −3χ(F ), and p denotes the number of triangles of T ′):
W + : ZI (T,b, C+) → (C \ {0})−3χ(F )+2p
W − : ZI (T,b, C−) → (C \ {0})−3χ(F ).
Deﬁnition 3.8. We call W ±(T,b, C) = W ±(ZI (T,b, C±)) the (±)-exponential I-parameter space of
RI (T,b, C).
We stress again that the result of the idealization strongly depends on the choice of the base point, here
0. In particular, the exponential I-parameters are not invariant under arbitrary gauge transformations
of cocycles. A remarkable exception is for gauge transformations associated to 0-cochains λ with values
in PB −(2, C). Indeed, these act on the idealization of quadrilaterals as confor mal transformations
of the four vertices (this is because 0 is ﬁxed by every λ(v), v ∈ V ), and cross-ratios are conformal
invariants. This makes a big diﬀerence between W + andW −. In fact the whole of the residual gauge
group G(T,b, C+) acts on W +(T,b, C) via the map W +. On the other hand, consider the subgroup of
G(T,b, C−) deﬁned as
BG(T,b, C−) :=
∏
i=1,...,r
Stab(C−
i ) ∩PB −(2, C).
Any ﬁber ( W −)−1(W −(z)) is given by the BG(T,b, C−)-orbit of z in ZI (T,b, C−). Hence the ac-
tual residual gauge transformations of W −(T,b, C) are in one-one correspondence with the quotient
set G(T,b, C−)/BG(T,b, C−), where the equivalence class of λ is BG(T,b, C−)λ. For the matter of
notational convenience, formally put BG(T,b, C+) := ∏
i=1,...,r Id. The map
Θ ± :W ±(T,b, C) → R(g,r, C±)
given by Θ ±(W ±(z)) = p±
C (z), with p±
C deﬁned in (16), is a principal G(T,b, C±)/BG(T,b, C±)-bundle.
The situation is particularly clean when C has no trivial entries :
Proposition 3.9. If C has no trivial entries the ( −)-exponential I-parameter mapW − : ZI (T,b, C−) →
W −(T,b, C) is invariant under gauge transformations.
18 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Geometry and computation of Θ ±. The maps Θ ± can be deﬁned directly in terms of I-parameters.
A way to see this is to consider I triangulations of cylinders C = F × [0, 1], as discussed in Section
6.3, and the corresponding pseudo-developing maps. We give here a nother description. Let us just
consider Θ −. Recall that PSL (2, C) is isomorphic to Isom +(H3), with the natural conformal action
on CP1 = ∂ ¯H3 via linear fractional transformations. For any ρ ∈ R (g,r, C−), take a representative
˜ρ : π1(F,q ) → PSL (2, C) in the conjugacy class. Consider the associated ﬂat principal PSL (2, C)-
bundle F˜ρ. A trivializing atlas deﬁnes a cocycle z ∈ Z (T,b, C−). If ρ ∈ RI (T,b, C−), we can take
z ∈ ZI (T,b, C−), so that the trivializing atlas of F˜ρ associated to the cellulation T ′∗ dual to T ′, with
edges oriented by using the orientation of F and the branching orientation of the edges of T ′, has
non trivial transition functions. These can be viewed as transition f unctions for the ﬁber bundle
associated to F˜ρ and with ﬁbre H3. For each 2-simplex t of T ′, there is a unique gt ∈ Isom(H3)
(possibly reversing the orientation) mapping the vertices u0, u1 and u2 of the idealization of t to 0,
∞ and −1 respectively. Then, the transition function along the edge of T ′∗ positively transverse to
a given edge e of T ′ is of the form ( gtl)−1 ◦ϕ(z)(e) ◦gtl ∈ Isom+(H3), where tl is the triangle on
the left of e, and ϕ(z)(e) is the isometry of H3 of hyperbolic type ﬁxing 0 and ∞ and mapping 1 to
W −(z)(e). Analytic continuation deﬁnes the parallel transport of F˜ρ along paths transverse to T ′,
whence a representation into PSL (2, C) of the groupoid of such paths, well-deﬁned up to homotopy
rel(∂)). In particular, it gives a practical recipe to compute ˜ ρ, that we describe now.
e e e
Figure 8. The recipe for reading oﬀ holonomies from exponential I-parameters.
Let the base point q be not in the 1-skeleton of T ′. Given an element of π1(F,q ), represent it by a
closed curve γ in F transverse to T ′, and which do not departs from an edge it just entered. Assume
thatγ intersects an edge e of T ′ positively with respect to the orientation of F . Figure 8 shows three
possible branching conﬁgurations for the two triangles glued along e. Fix arbitrarily a square root
W −(z)(e)1/2 of W −(z)(e). Consider the elements of PSL (2, C) given by
γ(e) =
(
W −(z)(e)1/2 0
0 W −(z)(e)−1/2
)
, p =
(
0 1
1 0
)
, l =
(
−1 1
−1 0
)
and r = l−1. The matrix γ(e) represents the isometry with ﬁxed points 0 , ∞ ∈ CP1 and mapping 1
to W −(z)(e). The elliptic elements p and l send (0, 1, ∞) to ( ∞, 1, 0) and ( ∞, 0, 1) respectively. For
the portion of γ on the left of Figure 8, if γ turns to the left after crossing e the parallel transport
operator is γ(e) ·p ·l, while it is γ(e) ·p ·r ifγ turns to the right. (The matrix multiplication is on the
right, as is the action of PSL (2, C) on the total space of F˜ρ). In the middle and right pictures the
parallel transport operators along the portion of γ are given by γ(e) ·l or γ(e) ·p ·l, and γ(e) ·p ·r or
γ(e) ·r respectively. We see that the action of p,l andr depends on the reordering of the vertices after
the mapping γ(e). If γ intersects e negatively, we replace γ(e) with γ(e)−1 in the above expressions.
A similar recipe applies for any other branching of the two triangles glu ed along e.
Continuing this way each time γ crosses an edge of T ′ until it comes back to q, we get an element
[W (z)]q(γ) ∈PSL (2, C) that depends only on the homotopy class of γ based at q and coincides with
˜ρ(γ), because of the identity Dz(γ ·x) = [W (z)]q(γ) ·Dz(x) for any x ∈ ˜F , where Dz : ˜F → CP1 is a
˜ρ-equivariant pseudo-developing map from the universal cover ˜F of F . Varying γ, we eventually get
the representation [W (z)]q = ˜ρ :π1(F,q ) →PSL (2, C).
QUANTUM HYPERBOLIC GEOMETRY 19
(−)-exponential I-parameters and pleated surfaces. When C− has no trivial entries, there
is a nice interpretation of the parameter space W −(T,b, C) in terms of pleated hyperbolic surface
structures on S \V . (see eg. [10]; compare also with [9], Section 8.)
As before, let T ′ be a triangulation of S with verticesV , viewed as an ideal triangulation of S◦ =S \V .
A pleated surface (with pleating locus T ′) is a pair ( ˜f,r ), where r : π1(S◦) → PSL (2, C) is a group
homomorphism (not up to conjugacy), and ˜f : ~S◦ → H3 is a map from the universal cover ~S◦ of S◦
such that:
• ˜f sends homeomorphically each component of the preimage ˜T ′ of T ′ in ~S◦ to a complete
geodesic in H3;
• ˜f sends homeomorphically the closure of each component of ˜S◦ \ ˜T ′ to an ideal triangle in H3;
• ˜f is r-equivariant, that is, for all x ∈ ˜S◦,γ ∈π1(S◦) we have ˜f(γx) = r(γ)˜f(x).
Two pleated surfaces ( ˜f,r ) and (˜f′,r ′) are said isometric if there exists an isometry A ∈PSL (2, C) and
a lift ˜φ : ˜S◦ → ˜S◦ of an isotopy of S◦ such that ˜f′ =A ◦˜f ◦ ˜φ andr′(γ) = Ar(γ)A−1 for all γ ∈π1(S◦).
From [8] it is known that isometry classes of pleated surfaces ( ˜f,r ) are in one-one correspondence
with arrays {xe}e of non zero complex numbers xe associated to the edges e of T ′, the exponential
shear-bend parameters.
To a pleated surface ( ˜f,r ) we can associate the type C− = ( C1,..., Cr) of the conjugacy class of r,
deﬁned as in Section 3.2. For instance, it is shown in [29] that the set o f isometry classes of pleated
surfaces given by real positive shear-bend parameters is real-an alytic diﬀeomorphic to the Teichm¨ uller
space of hyperbolic metrics on S◦, with totally geodesic boundary completion or non compact ﬁnite
area completion at vi, according to the type of Ci, loxodromic or parabolic.
In general, we can also associate a sign to each loxodromic puncture. Namely, if A is a small annulus
neignborhood of vi, each connected component ˜A of the preimage of A in ˜S◦ is the ﬁxed point set of
a subgroup π of π1(S◦). This subgroup is the image of the fundamental group of A for some choice
of base points and paths between these base points. All the edges of ˜T ′ that meet ˜A are sent by ˜f to
geodesics lines that meet at one of the two ﬁxed points of r(π). We specify this ﬁxed point by a sign,
as it determines an orientation (whence a generator) for the axis o f the group r(π). Since any two
subgroups π as above are conjugated, for each puncture the ﬁxed point assig nment is r-equivariant,
so that the sign is canonically associated to the puncture.
Recall that in Deﬁnition 3.3 the types Ci where assigned to the components of ∂F endowed with the
boundary orientation. Let us remove this constraint, and associa te to each boundary component with
loxodromic type an orientation that we specify by a sign, positive for the boundary orientation, and
negative otherwise. Then, for each type C− with l loxodromic entries and each l-uple of signs s, we
get a space ZI (T,b, C−,s ). We deﬁne W −(T,b, C,s ) = W (ZI (T,b, C−,s )).
Proposition 3.10. For each type C with non trivial entries Ci,l being loxodromic, and for each l-uple
of signs s, the space W −(T,b, C,s ) coincides with the exponential shear-bend parameter space PSs
C
of isometry classes of pleated surfaces of type C and signs s:
(17) PSs
C = {{xe} ∈ (C \ {0})−3χ(S◦) | ∀i = 1,...,r,
∏
xe =µi}.
Here the product is over all edges e withvi ∈∂e (counted with multiplicities), µi is 1 if Ci is parabolic,
and, if Ci is loxodromic, µi is the dilation factor of the generator of < Ci> speciﬁed by the sign of vi.
(Hence, in either case this is an eigenvalue of Ci.)
Proof. By the results of [8] recalled above, each point of W −(T,b, C,s ) is identiﬁed with the family
of exponential shear-bend parameters of an isometry class of ple ated hyperbolic surface on S◦ with
pleated locus T ′. The deﬁnition of the map Θ : W −(T,b, C,s ) → RI (T,b, C) shows that this isometry
class has type C. Furthermore, by using the recipe given above for computing Θ, we check that the
holonomy of any positively oriented (with respect to the boundary o rientation) small loop about the
puncture vi is exactly Ci. The upper left diagonal entry is just the product of a square roo t of the
exponential I-parameters at the edges with endpoint vi. From (17), which is an easy consequence of
results in [8] (see sections 12.2-12.3 in that paper), we deduce that W −(T,b, C,s ) ⊂ PSs
C.
20 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
Conversely, for any ( ˜f,r ) ∈ PS s
C we have conj(r) ∈ RI (T,b, C), because r is injective. Also, by [9],
Proposition 33, it is known that the isometry class of ( ˜f,r ) is determined by r and the signs s. As the
map Θ is onto, let us take z ∈ ZI (T,b, C−,s ) with conj ◦f (z) = conj( r) and consider the isometry
class of pleated hyperbolic surfaces associated to W −(z). There is a representative ( ˜f′,r ) with the
same holonomy r. As the signs of ( ˜f′,r ) are s, the same as for ( ˜f,r ), the two pleated surfaces coincide.
So PSs
C ⊂W −(T,b, C,s ). ✷
Remark 3.11. Exponential shear-bend parameters do not depend on branching s but the orientation
of F (taking the opposite branching edge orientation simultaneously exc hanges the left and right tri-
angles). However, branchings govern all choices in QHFT tensors. Also, they allow us to interpret
exponential shear-bend parameters as exponential I-parameters, thus coming from 1-cocycles repre-
senting arbitraryPSL (2, C)-characters on the triangulated boundary of arbitrary compact orientable
3-manifolds. When C has no trivial entries, the maps W ± deﬁne decorated shear-bend parameter
spaces similar to those occurring in [22, 26].
Remark 3.12. For types C with no trivial entries, we can use simpler e-triangulations of F (see
Figure 9): for each of the triangles tv of the base surface S we remove the interior of a monogon
inside tv, and triangulate the resulting quadrilateral by adding an edge ev with endpoints v and the
b-output vertex of the opposite edge. We extend b by orienting ev from that vertex to v. Proposition
3.4 applies to the cocycle parameters based on such e-triangulations, for points of R(g,r ), and also
the treatment of exponential I-parameters works as well.
Figure 9. More economic e-triangulation.
