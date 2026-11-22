---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-009-62-critical-volume-and-trivial-holonomy
section_title: "Critical volume and trivial holonomy"
section_number: 6.2
pages: 13-17
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Critical volume and trivial holonomy
Lemma 6.2 (Rivin, Chan–Hodgson) On the open afﬁne polyhedron P of sequences
(wi) satisfying (3), deﬁne the volume functional V as the sum of the hyperbolic volumes
of tetrahedra ∆i with dihedral angles xi, yi, zi, as given by Figure 5. Then (wi) is a
critical point for V in P if and only if the gluing of the tetrahedra ∆i deﬁnes a complete
ﬁnite-volume hyperbolic structure on the punctured torus bundle Vϕ.
Proof This now standard fact holds for general ideal triangulations as well (see for
example Chan [9] or Rivin [22]). The following proof, however, is deliberately speciﬁc
to the example at hand. This will enable us to introduce a few objects and relationships
that will be useful in the sequel. Conversely, the main idea of the present proof (associate
to each edge of Vϕ an explicit deformation in the space of angle structures) can be used
to prove the general case of Rivin’s theorem.
First we assume (wi) is critical. Let B be the torus at inﬁnity of Vϕ with the vertices
of the tessellation A removed. Let σ be the hyperelliptic involution of the ﬁber T,
Geometry & Topology 10 (2006)
1252
Franc¸ois Gu´eritaud and David Futer
so σ acts as a translation on B. Deﬁne B′ = B/σ and A′ = A/σ. Let t0 be a
triangle of A′, ϵ0 an oriented edge of t0 and x0 an interior point of t0. The group of
orientation-preserving similarities of the Euclidean plane C is C∗⋉C.
Deﬁnition 6.3 For a given (wi) in P, the holonomy function is the representation
ρ: π1(B′, x0) →C∗⋉C
deﬁned as follows. Given an element α of π1(B′, x0), view α as a cyclic sequence
of triangles t0, t1, . . . , ts = t0 of A′, such that any two consecutive ti’s share an edge.
Then, draw an oriented copy τ0 of t0 in the plane C, with angles speciﬁed by (wi), by
making the image of the oriented edge ϵ0 coincide with (0, 1). Sharing an edge with
τ0, draw a copy τ1 of t1, also with angles speciﬁed by (wi). Then draw a copy τ2 of t2
adjacent to τ1, etc. By deﬁnition, ρ(α) is the orientation-preserving similarity mapping
the copy of the oriented edge ϵ0 in τ0 to the copy of ϵ0 in τs. The reduced holonomy
function ψ : π1(B′, x0) →C∗is deﬁned as the projection of ρ on the ﬁrst factor.
It is a simple exercise to check that ρ is well-deﬁned, and is a representation (the
concatenation rule being that αβ denotes the path α followed by the path β). Note that
ψ, having a commutative target, factors through a representation ψ : H1(B′, Z) →C∗.
Sublemma 6.4 Let α be an element of H1(B′, Z) represented by a curve around
a 4–valent vertex of A′, and let β be represented by a curve that follows a “grey”
(hinge) level in A′ (Figure 7). If (wi) is critical for the volume functional V , then
ψ(α) = ψ(β) = 1.
y2
y1
ˇ
R
R
R
L
y2
x2
x1
z1
y1
z0
x1
z1 y0
˛
y1
z2
x0
x1
y0
z0
x0
z1
x1
z1
y1
z2
x2
Figure 7
Proof We already know that ψ(α), ψ(β) belong to R∗
+, since the angle conditions (1)
deﬁning P impose oriented parallelism. It remains to prove that |ψ(α)| = |ψ(β)| = 1.
Geometry & Topology 10 (2006)
Canonical triangulations
1253
At a critical point, the partial derivatives of V with respect to any of the wi must vanish.
Between and near two identical letters, say R and R, according to Figure 5, the angles
are given by the table
Ω
R
R
i
0
1
2
wi
a
b
c
xi
ξ −b
−a + 2b −c
−b + ξ′
yi
η + b
a + c
b + η′
zi
π −2a
π −2b
π −2c
(the exact expression of ξ, ξ′, η, η′ depends on the letters before and after RR, but only
the b–contribution matters here). Using Proposition 6.1, criticality of V implies
1 = exp −∂V
∂b
= sin y0 sin2 x1 sin y2
sin x0 sin2 z1 sin x2
.
Using the fact that edge lengths in a triangle are proportional to angle sines, it follows
that the edge lengths in Figure 7 (left) around the central vertex ﬁt nicely together. So
|ψ(α)| = 1. The case of a subword LL is treated similarly, which takes care of all
4–valent vertices of the tessellation A′.
Near a hinge between two different letters, say L followed by R, the angles are
Ω
L
R
i
0
1
2
wi
a
b
c
xi
ξ + b
a + b −c
−b + ξ′
yi
η −b
−a + b + c
b + η′
zi
π −2a
π −2b
π −2c
This time, criticality implies
1 = exp −∂V
∂b
= sin x0 sin y1 sin x1 sin y2
sin y0 sin2 z1 sin x2
.
As shown in Figure 7 (right) and by the same trigonometric argument, this means that
the ﬁrst and last edges crossed by β have the same length. So ψ(β) = 1. (If Ωis
reduced to LR, the computation is formally the same, identifying indices 0 and 2.) The
case of a subword RL is similar. Sublemma 6.4 is proved.
Now let α be an element of π1(B′, x0) that is conjugated to a simple loop around a
4–valent vertex of A′. By Sublemma 6.4 (and an easy conjugation argument), ρ(α) is
a translation. Moreover, ρ(α) ﬁxes the vertex around which α revolves, so ρ(α) = 1,
the identity of the Euclidean plane.
Geometry & Topology 10 (2006)
1254
Franc¸ois Gu´eritaud and David Futer
Sublemma 6.5 Let U be the quotient of the torus at inﬁnity of Vϕ by the action of
the hyperelliptic involution σ of the ﬁber, so that B′ ⊂U. Suppose (wi) is critical
for V . Then the representation ρ: π1(B′, x0) →C∗⋉C descends to a representation
ρU : π1(U, x0) →C∗⋉C whose ﬁrst projection ψU : π1(U, x0) →C∗is trivial.
 
Figure 8
Proof To see that ρU is well-deﬁned, we only need to check that, if γ is (conjugated
to) a loop around a vertex v of A′, then ρ(γ) = 1. If v has valence 4, it has already
been done. If not, by the argument preceding Sublemma 6.5, it is sufﬁcient to check
that ψ([γ]) = 1, where [γ] denotes the homology class of γ. But in H1(B′, Z), the
element [γ] is a sum of loops around 4–valent vertices and curves following “grey”
levels (see Figure 8: the vertical edges of B′ on the two sides of the picture are identiﬁed,
and the curves crossing these edges undergo a “split-and-paste” process to yield γ).
So by Sublemma 6.4, ψ([γ]) = 1; therefore ρU is well-deﬁned. Moreover, if β is a
curve following a “grey” level, Sublemma 6.4 tells that ρU(β) = ρ(β) is a nonidentical
Euclidean translation. The value of ρU on another generator of π1(U) (which is abelian)
must commute with ρU(β), and therefore be a translation too. So ρU has its image
contained in {1} ⋉C and ψU = 1, completing the proof.
By assigning length 1, for example, to the reference edge ϵ0 of A′, a critical point (wi)
of the volume functional thus deﬁnes the lengths of all other edges of A′ in a coherent
way. This yields a complete Euclidean metric g on U. The universal cover eU of U thus
embeds into C (the embedding, also called the developing map of the local Euclidean
Geometry & Topology 10 (2006)
Canonical triangulations
1255
structure, can only be injective, because the eg–geodesic joining two distinct points of eU
is sent to a geodesic of C); so there is an isometry eU ≃C. The metric g lifts from U
to the torus at inﬁnity of Vϕ and its tessellation A, producing a geometric realization of
A and of Figure 4 in C (Euclidean plane tiling). Above each triangle of the universal
cover of A now sits one ideal tetrahedron with vertex at inﬁnity: the tetrahedron is the
hyperbolic convex hull of ∞and the vertices of the triangle. Note that these tetrahedra
ﬁll H3 completely above a certain height.
To make sure that the pasted metric on the union V = Vϕ of all ideal tetrahedra is
now complete, assume a geodesic γ(t) in V hits inﬁnity at time T < ∞. If K ⊂V is
compact, ie has a compact intersection with each tetrahedron ∆i, then γ must eventually
exit K (if not, the γ(T −1/n) accumulate at some point p of some tetrahedron, but
centered at p there is a small embedded hyperbolic ball: absurd). So for t sufﬁciently
close to T , there is a lift of γ(t) arbitrarily high above the tessellation A (embedded in
C in the upper half space model). But at sufﬁciently great height, the tetrahedra above
A ﬁll H3 completely, so geodesics are deﬁned for long times (eg times larger than 1):
a contradiction. The ﬁrst implication of Lemma 6.2 is proved.
To prove the converse, it is enough to show that if the gluing of the tetrahedra yields
a complete hyperbolic metric, then the gluing of their vertex links yields a geometric
realization of A, ie of Figure 4 (checking ∂V/∂wi = 0 then amounts to a rerun of
the two computations in Sublemma 6.4, distinguishing whether i is a hinge index or
not). But the latter is clear: given a complete hyperbolic metric, consider a triangulated
universal cover H3 →Vϕ and send (a lift of) the cusp to inﬁnity in the upper half
space model. It is a classic argument that deck transformations of H3 which ﬁx inﬁnity
must be parabolic, so the link of inﬁnity has two translational periods and provides a
Euclidean realization of A (and of Figure 4).
