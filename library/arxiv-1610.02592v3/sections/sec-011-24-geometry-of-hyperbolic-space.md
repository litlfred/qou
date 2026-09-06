---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-011-24-geometry-of-hyperbolic-space
section_title: "Geometry of hyperbolic space"
section_number: 2.4
pages: 76-81
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
We study the geometry ofHn. We prove thatHn has constant sectional
curvature−1,thatthedistancefunctionalonglinesisconvex,wedeﬁneconvex
combinations and barycenters, and study parallel transport along lines. Finally,
we prove thatIsom(Hn) is a unimodular Lie group.
2.4.1. Areaandcurvature. Wecanverifythat Hn hasconstantsectional
curvature−1. It should be no surprise thatHn has constant curvature, since
it has many symmetries (i.e. isometries). To calculate its sectional curvature
we compute the area of a disc.
Proposition 2.4.1. The disc of radiusr in H2 has area
A(r ) =π
(
e
r
2−e−r
2
)2
= 4π sinh2 r
2 = 2π(coshr− 1).
Proof. Recall that the volume form is
ω =
√
detg·dx 1··· dxn.
LetD(r ) be a disc inH2 of radiusr. If we centre it in0 in the disc model, its
Euclidean radius istanh r
2 by Corollary 2.1.26 and we get
A(r ) =
∫
D(r)
√
detg·dxdy =
∫
D(r)
( 2
1−x 2−y 2
)2
dxdy
=
∫ 2π
0
∫ tanh r
2
0
( 2
1−ρ2
)2
ρ·dρdθ = 2π
[ 2
1−ρ2
]tanh r
2
0
= 4π
(
1
1− tanh2 r
2
− 1
)
= 4π sinh2 r
2.
The proof is complete. □
Corollary 2.4.2.The hyperbolic spaceHn has sectional curvature−1.
2.4. GEOMETRY OF HYPERBOLIC SPACE 69
Figure 2.14. Distance between points in disjoint lines is a strictly convex
function in hyperbolic space.
Proof. Pickp∈ Hn and W ⊂ Tp a 2-dimensional subspace. The image
expp(W ) is the hyperbolic plane tangent toW inp. On a hyperbolic plane
A(r ) = 2π(coshr− 1) = 2π
(r 2
2! +r 4
4! +o(r 4)
)
=πr 2 +πr 4
12 +o(r 4)
and henceK =−1 following the area formula in Section 1.2.8. □
2.4.2. Convexity of the distance function.We recall that a function
f : Rn→ R is strictly convexif
f (tv + (1−t)w )<tf (v ) + (1−t)f (w )
for any pairv,w ∈ Rn of distinct points and anyt∈ (0, 1).
Exercise 2.4.3. A positive strictly convex function is continuous and admits
a minimum if and only if it is proper.
We now prove that the distance function is strictly convex on disjoint lines
of Hn. Given two linesl,l′⊂ Hn, we ﬁx an isometry of each line withR and
we get an identiﬁcation ofl×l′ with the Euclidean planeR× R.
Proposition 2.4.4. Letl,l′⊂ Hn be two disjoint lines. The map
l×l′−→ R>0
(x,y )↦−→d(x,y )
is strictly convex; it is proper if and only if the lines are ultraparallel.
Proof. With our identiﬁcations we have(x,y )∈ R× R. The functiond
is clearly continuous, hence to prove its convexity it suﬃces to show that
d
(x1 +x2
2 ,y1 +y2
2
)
< d(x1,y 1) +d(x2,y 2)
2
for any pair of distinct points(x1,y 1), (x2,y 2)∈l×l′. Suppose x1⁄=x2 and
denote bym andn the midpointsx1+x2
2 and y1+y2
2 as in Figure 2.14.
70 2. HYPERBOLIC SPACE
Let σp be the reﬂection at the pointp∈ Hn. The isometryτ =σn◦σm
translates the liner containing the segmentmn by the quantity 2d(m,n ):
hence it is a hyperbolic transformation with axisr. We draw the pointso =
τ(m)andzi =τ(xi )intheﬁgureandnotethat z1 =σn(x2), henced(x2,y 2) =
d(z1,y 1). The triangular inequality implies that
d(x1,z 1)⩽d(x1,y 1) +d(y1,z 1) =d(x1,y 1) +d(x2,y 2).
A hyperbolic transformation has minimum displacement on its axisr andx1⁄=
m is not inr, hence
2d(m,n ) =d(m,o ) =d(m,τ (m))<d (x1,τ (x1)) =d(x1,z 1).
Finally we get2d(m,n )<d (x1,y 1) +d(x2,y 2) and henced is convex.
The functiond is proper, that is it has minimum, if and only if the two
lines are ultraparallel by Proposition 2.2.3. □
Exercise 2.4.5. The distance function on parallel lines inRn is not strictly
convex (it is only convex).
2.4.3. Convex combinations. Let p1,...,p k be k points in Hn, Rn, or
Sn andt1,...,t k be non-negative numbers witht1 +... +tk = 1. Theconvex
combination
p =t1p1 +... +tkpk
is another point in the space deﬁned as follows:
in Rn : p =t1p1 +... +tkpk
inIn,Sn : p = t1p1 +... +tkpk
‖t1p1 +... +tkpk‖
where‖v‖ =
√
−⟨v,v⟩ on In. Using convex combination we may deﬁne the
barycenter of the points as1
kp1 +... + 1
kpk. The barycenter may in turn be
used to prove the following.
Proposition 2.4.6. Letϕ: Hn→ Hn be a non-trivial isometry andk> 2:
• ifϕ is elliptic thenϕk is elliptic or trivial;
• ifϕ is parabolic thenϕk is parabolic;
• ifϕ is hyperbolic thenϕk is hyperbolic.
Proof. Ifϕ: Hn→ Hn is an isometry with no ﬁxed points, thenϕk also
is: ifϕk(x) = x thenϕ ﬁxes the ﬁnite set{x,ϕ (x),...,ϕ k−1(x)} and hence
also its barycenter.
If ϕ is parabolic then it ﬁxes the horospheres centred at some pointp∈
∂Hn and alsoϕk does, hence it is still parabolic (it cannot be hyperbolic). If
ϕ is hyperbolic it has two ﬁxed points at inﬁnity, andϕk too. □
Proposition 2.4.7. Every ﬁnite groupΓ< Isom(Hn) ﬁxes a point inHn.
Proof. The barycenter of any orbit is ﬁxed byΓ. □
2.4. GEOMETRY OF HYPERBOLIC SPACE 71
2.4.4. Parallel transport. On Riemannian manifolds, the parallel trans-
port is a way to slide frames along geodesics. OnHn we can do this simply as
follows: for every geodesicγ, we putγ into vertical position in the half-space
modelHn, and slide the frames vertically in the obvious way.
This construction furnishes in particular, for every pairx,y ∈ Hn of points,
acanonicalisometrybetween Tx Hn andTy Hn, obtainedbyslidingframesalong
the unique geodesicγ containingx andy.
This canonical identiﬁcation is of course not transitive on a triple of non-
collinear pointsx,y,z : the curvature ofHn is responsible for that.
2.4.5. Unimodularity. ThefollowingisaconsequenceofCorollary1.4.16.
Corollary 2.4.8.The isometry groupIsom(Hn) is unimodular.
Remark 2.4.9. A Haar measure forIsom(Hn) may be constructed con-
cretely as follows: ﬁx a pointx∈ Hn and deﬁne the measure of a Borel set
S⊂ Isom(Hn) as the measure ofS(x) = ∪ϕ∈Sϕ(x)⊂ Hn. This measure
is obviously left-invariant, and is hence also right-invariant sinceIsom(Hn) is
unimodular. As a consequence, it does not depend on the choice ofx.
2.4.6. References. The hyperbolic space is introduced in various books:
two standard references are Benedetti – Petronio [4] and Ratcliﬀe [49], and
most of the arguments presented here were borrowed from these two sources.
TheproofofProposition2.4.4wastakenfromFarb–Margalit[ 18]. Thurston’s
notes contain some useful trigonometric formulae that we have omitted, see
[56, Chapter 2].
CHAPTER 3
Hyperbolic manifolds
A hyperbolic manifold is a Riemannian manifold locally isometric to the
hyperbolic space Hn. Maybe the most striking aspect of geometric topology
is that, despite this quite restrictive deﬁnition, there are plenty of hyperbolic
manifolds around, especially in the dimensionsn = 2 and 3. For that reason
hyperbolic manifolds (and hence hyperbolic geometry) play a central role in
the topology of surfaces and three-manifolds.
The study of complete hyperbolic manifolds is tightly connected to that
of discrete subgroups in the Lie groupIsom(Hn) and of polyhedra inHn, so
it has both an algebraic and geometric ﬂavour. We start this chapter by
describing these connections; then we show some examples and discuss some
important variations: non-complete hyperbolic manifolds, hyperbolic manifolds
with geodesic boundary, cone manifolds, and orbifolds.
