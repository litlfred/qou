---
doc_id: arxiv-1610.02592v3
doc_title: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022"
section_id: sec-057-131-volume-of-tetrahedra
section_title: "Volume of tetrahedra"
section_number: 13.1
pages: 413-418
source_pdf: 1610.02592v3.pdf
source_sha256: 81020523d7d2bc1a
doc_brief: "An Introduction to Geometric Topology Bruno Martelli arXiv:1610.02592v3 [math.GT] 5 Apr 2022 — 68 sections: Introduction; Differential topology; Riemannian geometry"
---
The volume of an ideal hyperbolic tetrahedron is a simple (but integral)
formula that involves theLobachevsky function: we now prove this formula
here. As a consequence we show that the regular ideal tetrahedron is the
hyperbolic tetrahedron with maximal volume.
13.1.1. The Lobachevsky function.The Lobachevsky functionis
Λ(θ) =−
∫ θ
0
log|2 sint|dt.
The functionlog|2 sint|is−∞onπZbut is integrable, henceΛis well-deﬁned
and continuous onR. Its ﬁrst derivatives are
Λ′(θ) =− log|2 sinθ|, Λ′′(θ) =− cotθ.
The function Λ has derivative +∞ onπZ and is an odd function, because its
derivative is even.
405
406 13. MOSTOW RIGIDITY THEOREM
Proposition13.1.1. Thefunction Λisπ-periodic. Wehave Λ(0) = Λ
(π
2
)
=
Λ(π) = 0 . The function Λ is strictly positive on
(
0, π
2
)
, strictly negative on(π
2,π
)
, and has absolute maximum and minimum atπ
6 and 5
6π. For allm∈ N
the following holds:
Λ(mθ) =m
m−1∑
k=0
Λ
(
θ +kπ
m
)
.
Proof. We prove the equality form = 2:
Λ(2θ)
2 =−1
2
∫ 2θ
0
log|2 sint|dt =−
∫ θ
0
log|2 sin 2t|dt
=−
∫ θ
0
log|2 sint|dt−
∫ θ
0
log
⏐⏐⏐2 sin
(
t +π
2
)⏐⏐⏐dt
= Λ(θ)−
∫ π
2 +θ
π
2
log|2 sint|dt
= Λ(θ) + Λ
(
θ +π
2
)
− Λ
(π
2
)
.
By setting θ = π
2 we get Λ(π) = 0 . Since the derivative Λ′ is π-periodic
and Λ(π) = 0 , also Λ is π-periodic. Since Λ is π-periodic and odd, we have
Λ
(π
2
)
= 0. We have also proved the formula form = 2.
To prove the formula for genericm we use a generalisation of the duplica-
tion formula for the sinus. From the equality
zm− 1 =
m−1∏
k=0
(
z−e− 2πik
m
)
we deduce
2 sin(mt) =
m−1∏
k=0
2 sin
(
t +kπ
m
)
and hence
Λ(mθ)
m =− 1
m
∫ mθ
0
log|2 sint|dt =−
∫ θ
0
log|2 sin(mt)|dt
=−
m−1∑
k=0
∫ θ
0
log
⏐⏐⏐⏐2 sin
(
t +kπ
m
)⏐⏐⏐⏐dt
=−
m−1∑
k=0
(∫ θ+kπ
m
0
log|2 sint|dt−
∫ kπ
m
0
log|2 sint|dt
)
=−
m−1∑
k=0
Λ
(
θ +kπ
m
)
+C(m)
13.1. VOLUME OF TETRAHEDRA 407
Figure 13.1. Every pair of opposite edges in an ideal tetrahedron has
an axis orthogonal to both which is a symmetry axis for the tetrahedron.
whereC(m) is a constant independent ofθ. By integrating both sides we get
1
m
∫ π
0
Λ(mθ) =−
m−1∑
k=0
∫ π
0
Λ
(
θ +kπ
m
)
+C(m)π.
Since Λ is odd andπ-periodic, we have∫ π
0
Λ(mθ) = 0
for any integerm. Hence C(m) = 0 and the formula is proved. Finally we
note that Λ′′(θ) =− cotθ is strictly negative in(0, π
2 ) and strictly positive in
(π
2,π ), henceΛ is strictly positive in(0, π
2 ) and strictly negative in(π
2,π ). □
13.1.2. Volumes of ideal tetrahedra.An ideal tetrahedron inH3 is the
convex hull of four non-planar ideal points. Quite surprisingly, every ideal
tetrahedron has some non-trivial symmetries.
Proposition 13.1.2.For any pair of opposite edges in an ideal tetrahedron
∆ there is a unique line r orthogonal to both as in Figure 13.1 and ∆ is
symmetric with respect to aπ-rotation aroundr.
Proof. The opposite edgese ed e′ are ultraparallel lines inH3 and hence
have a common perpendicularr. Aπ-rotation aroundr inverts bothe ande′
but preserve the 4 ideal vertices of∆, hence ∆ itself. □
As a consequence, two opposite edges in∆ have coinciding dihedral angles
as in Figure 13.2-(left). Moreover, we haveα +β +γ =π because a small
horosphere based at a vertex intersects∆ into a Euclidean triangle with inner
angles α,β, andγ. The regular ideal tetrahedron has of course equal angles
α =β =γ = π
3.
Theorem 13.1.3.Let ∆ be an ideal tetrahedron with dihedral anglesα,β
andγ. We have
Vol(∆) = Λ(α) + Λ(β) + Λ(γ).
408 13. MOSTOW RIGIDITY THEOREM
Figure 13.2. The dihedral anglesα,β,γ of an ideal tetrahedron. Op-
posite edges have the same angle andα +β +γ =π (left). To calculate
the volume we use the half-space model, send a vertex to∞, and divide
the tetrahedron in six sub-tetrahedra (right).
Proof. We represent∆ in the half-space modelH3 with one vertexv0 at
inﬁnity and three verticesv1,v 2,v 3 in C. Let C be the circle containingv1,
v2, andv3: up to composing with elements inPSL2(C) we can suppose that
C =S1. The Euclidean triangleT⊂ C with verticesv1,v2, andv3 has interior
anglesα,β, andγ.
We ﬁrst consider the case0∈T, that isα,β,γ ⩽ π
2. We decomposeT
into six triangles as in Figure 13.2: the tetrahedron∆ decomposes accordingly
into six tetrahedra lying above them, and we prove that the one∆α lying above
the yellow triangle has volumeΛ(α)
2 . This proves the theorem.
The tetrahedron ∆α is the intersection of four half-spaces: three vertical
ones bounded by the hyperplanesy = 0,x = cosα, andy =x tanα, and one
bounded by the half-spherez 2 =x 2 +y 2. Therefore
Vol(∆α) =
∫ cosα
0
dx
∫ x tanα
0
dy
∫ ∞
√
1−x 2−y 2
1
z 3dz
=
∫ cosα
0
dx
∫ x tanα
0
dy
[
− 1
2z 2
]∞
√
1−x 2−y 2
= 1
2
∫ cosα
0
dx
∫ x tanα
0
1
1−x 2−y 2dy.
To solve this integral we use the relation
1
1−x 2−y 2 = 1
2
√
1−x 2
( 1√
1−x 2−y + 1√
1−x 2 +y
)
13.1. VOLUME OF TETRAHEDRA 409
and hence Vol(∆α) equals
1
4
∫ cosα
0
dx√
1−x 2
([
− log(
√
1−x 2−y )
]x tanα
0
+
[
log(
√
1−x 2 +y )
]x tanα
0
)
=1
4
∫ cosα
0
dx√
1−x 2
(
− log(
√
1−x 2−x tanα) + log(
√
1−x 2 +x tanα)
)
.
By writingx = cost and hencedx =− sintdt we obtain
Vol(∆α) = 1
4
∫ α
π
2
− sint
sint
(
− log sint cosα− cost sinα
sint cosα + cost sinα
)
dt
=−1
4
∫ α
π
2
log sin(t +α)
sin(t−α)dt =−1
4
∫ α
π
2
log|2 sin(t +α)|
|2 sin(t−α)|dt
= 1
4
∫ π
2 +α
2α
log|2 sint|dt− 1
4
∫ π
2−α
0
log|2 sint|dt
= 1
4
(
−Λ
(π
2 +α
)
+ Λ(2α) + Λ
(π
2−α
))
= 1
4
(
−Λ
(π
2 +α
)
+ 2Λ(α) + 2Λ
(π
2 +α
)
− Λ
(π
2 +α
))
= 1
2Λ(α)
using Proposition 13.1.1.
If 0⁄∈ T the triangleT may be decomposed analogously into triangles,
some of which contribute negatively to the volume, and we obtain the same
formula. □
Corollary 13.1.4. The regular ideal tetrahedron is the hyperbolic tetrahe-
dron of maximum volume.
Proof. It is easy to prove that every hyperbolic tetrahedron is contained in
an ideal tetrahedron: hence we may consider only ideal tetrahedra. Consider
the triangleT ={0⩽α,β,α +β⩽π} and
f : T−→ R
(α,β )↦−→Λ(α) + Λ(β) + Λ(π−α−β).
The continuous functionf is null on∂T and strictly positive on the interior of
T because it measures the volume of the ideal tetrahedron of dihedral angles
α,β,γ =π−α−β. Hencef has at least a maximum on some interior point
(α,β ). The gradient
∇f =
(Λ′(α)− Λ′(π−α−β)
Λ′(β)− Λ′(π−α−β)
)
=
(− log|2 sinα| + log|2 sin(π−α−β)|
− log|2 sinβ| + log|2 sin(π−α−β)|
)
must vanish there, and this holds if and only ifsinα = sin(π−α−β) = sinβ,
i.e. if and only if the tetrahedron has all dihedral angles equal toπ
3. □
410 13. MOSTOW RIGIDITY THEOREM
