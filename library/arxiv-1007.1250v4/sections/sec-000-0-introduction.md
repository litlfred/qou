---
doc_id: arxiv-1007.1250v4
doc_title: "Nonabelian Multiplicative Integration on Surfaces"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 3-137
source_pdf: 1007.1250v4.pdf
source_sha256: 541ba4fb3068de8b
doc_brief: "Nonabelian Multiplicative Integration on Surfaces — We construct a 2 -dimensional twisted nonabelian multiplicative integral ."
---
necessary to devise a theory of 2 -dimensional nonabelian multiplicative integration .
Our work was guided by the problem at hand, plus ideas borrowed from the
papers [BM, BS, Ko].
Instead of a single Lie group, the 2-dimensional operation involves a pair
(G, H) of Lie groups, with a certain interaction between them. This structure
is called a Lie crossed module. A Lie crossed module
(0.2.1) C = ( G, H, Ψ, Φ)
consists, in addition to the Lie groups H and G, of an analytic action Ψ of G on H
by automorphisms of Lie groups, which we call the twisting; and of a map of Lie
groups Φ : H→ G, called the feedback. The conditions are that Φ is G-equivariant
(with respect to Ψ and to the conjugation action Ad G of G on itself); and
(0.2.2) Ψ◦ Φ = AdH .
See [BM, BS]. The integrand is now a pair (α, β), with
(0.2.3) α∈ Ω1(X)⊗ g and β∈ Ω2(X)⊗ h.
Here h is the Lie algebra of H.
Let x0 be a point in X, so the pair (X, x0) is a pointed manifold. The geometric
data (the cycle) for the multiplicative integration is a kite (σ, τ) in (X, x0). Let us
denote by v0, . . . ,vp the vertices of the p-dimensional simplex ∆p. By deﬁnition
a smooth triangular kite (σ, τ) in (X, x0) consists of smooth maps σ : ∆1 → X
and τ : ∆2→ X, such that σ(v0) = x0 and σ(v1) = τ(v0). See Figure 1 for an
illustration.
The next theorem summarizes our construction. It encapsulates many results
scattered throughout the paper.
2 AMNON YEKUTIELI
Figure 1. A smooth triangular kite (σ, τ) in the pointed manifold (X, x0).
Theorem 0.2.4 (Existence of MI on Triangles). Let C = ( G, H, Ψ, Φ) be a Lie crossed
module, (X, x0) a pointed manifold, and (α, β) a pair of differential forms as in (0.2.3).
Given any smooth triangular kite (σ, τ) in (X, x0), there is an element
MI(α, β| σ, τ)∈ H
called the twisted multiplicative integral of (α, β) on (σ, τ).
The operation MI(−,−) enjoys these properties:
(a) The element MI(α, β| σ, τ) has an explicit formula as the limit of Riemann prod-
ucts.
(b) The operation MI(−,−) is functorial in C and (X, x0).
(c) If H is abelian and G is trivial, then
MI(α, β| σ, τ) = expH
(∫
τ
β
)
.
More on the construction in Subsections 0.6-0.8 and 0.10 of the Introduction.
As far as we know, this is the ﬁrst construction of a nonabelian multiplica-
tive integration on surfaces of such generality. The very special case G = H =
GLm(R) was done by Schlesinger in the 1920’s; cf. [DF, KMR].
0.3. Actually, in the body of the paper we work in a much more complicated
situation. Instead of a Lie crossed module (0.2.1), we work with a Lie quasi crossed
module with additive feedback (See Section 5). The reason for the more complicated
setup is that this is what was required, at the time, for our work on twisted defor-
mation quantization in the paper [Ye3]. More on this in Subsection 0.11 below. In
the Introduction we stick to the simpler setup of a Lie crossed module, which is
interesting enough. Note however that all the results mentioned in the Introduc-
tion are valid also in the more complicated setup.
0.4. In this subsection we explain the nonabelian 2-dimensional Stokes Theo-
rem. For this to hold it is necessary to impose a condition on the integrand (α, β).
Recall the feedback Φ : H→ G. Consider the induced Lie algebra homomor-
phism
Lie(Φ) : h→ g.
By tensoring this induces a homomorphism of differential graded Lie algebras
φ : Ω(X)⊗ h→ Ω(X)⊗ g.
We say that (α, β) is a connection-curvature pair for C/X if
(0.4.1) φ(β) = d(α) + 1
2 [α, α]
in Ω2(X)⊗ g. (In [BM] this condition is called the vanishing of the fake curvature.)
NONABELIAN MULTIPLICATIVE INTEGRATION 3
Figure 2. The boundary ∂(σ, τ) of the kite (σ, τ) from Figure 1.
Figure 3. A smooth triangular balloon (σ, τ) in the pointed man-
ifold (X, x0).
The boundary of a triangular kite (σ, τ) is the closed path ∂(σ, τ) depicted in
Figure 2.
Theorem 0.4.2 (Stokes Theorem for Triangles). Let C = ( G, H, Ψ, Φ) be a Lie crossed
module, (X, x0) a pointed manifold, and (α, β) a connection-curvature pair for C/X.
Given any smooth triangular kite (σ, τ) in (X, x0), one has
Φ
(
MI(α, β| σ, τ)
)
= MI(α| ∂(σ, τ))
in G.
The special case G = H = GLm(R) is Schlesinger’s Theorem (see [DF, KMR]).
0.5. We now approach the main result of the paper, namely the nonabelian 3-
dimensional Stokes Theorem.
A smooth triangular balloon in (X, x0) is a pair (σ, τ), consisting of smooth maps
σ : ∆1→ X and τ : ∆3→ X, such that σ(v0) = x0 and σ(v1) = τ(v0). See Figure
3 for an illustration.
The boundary of a balloon (σ, τ) is a sequence
∂(σ, τ) =
(
∂1(σ, τ), ∂2(σ, τ), ∂3(σ, τ), ∂4(σ, τ)
)
of triangular kites. See Figure 4. We write
(0.5.1) MI (α, β| ∂(σ, τ)) :=
4
∏
1=1
MI(α, β| ∂i(σ, τ)),
4 AMNON YEKUTIELI
Figure 4. The four triangular kites that make up the sequence
∂(σ, τ). Here (σ, τ) is the triangular balloon from Figure 3.
where the order of the product is left to right.
Let H0 := Ker(Φ), which is a closed Lie subgroup of H. We call it the iner-
tia subgroup, and h0 := Lie(H0) is called the inertia subalgebra. Note that H0 is
contained in the center of H, so H0 is an abelian Lie group. A form
γ∈ Ωp(X)⊗ h0
is called an inert p-form.
We say that a form α ∈ Ω1(X)⊗ g is tame connection if it belongs to some
connection-curvature pair (α, β). We show (in Subsection 8.3) that given a tame
connection α and an inert 3-form γ, there is a well deﬁned twisted abelian multi-
plicative integral
MI(α, γ| σ, τ)∈ H0.
For g∈ G there is a Lie group automorphism Ψ(g) : H→ H. Its derivative is
Ψh(g) := Lie(Ψ(g)) : h→ h.
As g varies we get a map of Lie groups
(0.5.2) Ψh : G→ GL(h).
The derivative of Ψh is a map of Lie algebras
Lie(Ψh) : g→ gl(h) = End(h).
This extends by tensor product to a homomorphism of differential graded Lie
algebras
ψh : Ω(X)⊗ g→ Ω(X)⊗ End(h).
Given a connection-curvature (α, β), its 3-curvature is the form
(0.5.3) γ := d(β) + ψh(α)(β)∈ Ω3⊗ h.
(This is the name given in [BM].)
We can now state the main result of the paper. (See Theorem 9.3.5 for the full
version.)
NONABELIAN MULTIPLICATIVE INTEGRATION 5
Theorem 0.5.4 (Stokes Theorem for Tetrahedra) . Let C = ( G, H, Ψ, Φ) be a Lie
crossed module, (X, x0) a pointed manifold, and (α, β) a connection-curvature pair for
C/X. Let γ be the 3-curvature of (α, β). Then:
(1) The form γ is inert.
(2) Given any smooth triangular balloon (σ, τ) in (X, x0), one has
MI(α, β| ∂(σ, τ)) = MI(α, γ| σ, τ)
in H.
In this generality, Theorem 0.5.4 appears to have no precursor in the literature.
The special (but most important) case, namely γ = 0, was taken to be true in
some papers (e.g. [Ko, BS]), but no proofs were provided there.
Assertion (1) in the theorem can be viewed as a generalized Bianchi identity.
0.6. In this and the next few subsections we will explain some of the work lead-
ing to the theorems mentioned above.
The methods used in the constructions and proofs are of two kinds: geometric
and inﬁnitesimal. The geometric methods consist of dividing kites into smaller
ones, and studying the effect on the corresponding approximations (Riemann
products). The inﬁnitesimal methods involve Taylor expansions and estimates
for the nonabelian exponential map.
Throughout most of the paper we work with linear quadrangular kites in polyhe-
dra, and with piecewise smooth differential forms, rather than with smooth triangular
kites in manifolds and smooth differential forms. The reason for choosing quad-
rangular kites is mainly that it is much easier to carry out calculations of Taylor
expansions on squares, as compared to triangles. Also the combinatorics of quad-
rangular kites and their binary subdivisions is simpler than that of triangles. See
Subsections 4.1-4.2. A review of the piecewise linear geometry of poyhedra, and
of piecewise smooth differential forms, can be found in Section 1.
The key technical result that allows us to calculate nonabelian products is The-
orem 2.1.2 on estimates for the nonabelian exponential map. These estimates are
gotten from the CBH formula. Section 2 is devoted to the proof of these estimates.
For heuristic purposes we introduce the concept of “tiny scale”. By tiny scale
(depending on context of course) we mean geometric or algebraic elements that
are so small that the relevant estimates (arising from the CBH formula or Taylor
expansion) apply to them. See Remark 3.3.5.
0.7. For n≥ 0 let In be the n-dimensional cube. We give names to some vertices:
v0 := (0, . . . , 0), and
vi := (0, . . . , 1, . . . , 0)
with 1 in the i-th position, for i = 1, . . . ,n. The base point for In is v0.
Let (X, x0) be a pointed polyhedron. By linear string in X we mean a sequence
σ = ( σ1, . . . ,σm) of piecewise linear maps σi : I1→ X, such that σi(v1) = σi+1(v0).
The maps σi are called the pieces of σ. In Section 3 we construct the non-
abelian multiplicative integral MI (α| σ) of a piecewise smooth differential form
α∈ Ω1
pws(X)⊗ g on a string σ. This construction is quite simple and essentially
the same as the classical one. We also prove a few basic properties of this MI.
0.8. In Section 4 we construct the 2-dimensional nonabelian multiplicative inte-
gral MI(α, β| σ, τ). Here (σ, τ) is a linear quadrangular kite in the pointed poly-
hedron (X, x0). By deﬁnition this means that σ is a string in X, and τ : I2→ X is
a linear map. The conditions are that the initial point of σ is x0, and the terminal
6 AMNON YEKUTIELI
point of σ is τ(v0). The integrand (α, β) consists of piecewise smooth differential
forms:
α∈ Ω1
pws(X)⊗ g and β∈ Ω2
pws(X)⊗ h.
The coarse approximation of the 2-dimensional nonabelian multiplicative inte-
gral is as follows. Given a kite (σ, τ) in (X, x0), let
g := MI(α| σ)∈ G;
so applying the operator Ψh(g) from (0.5.2) we have a new (twisted) 2-form
Ψh(g)(β)∈ Ω2
pws(X)⊗ h.
We deﬁne the basic Riemann product of (α, β) on (σ, τ) to be
(0.8.1) RP 0(α, β| σ, τ) := expH
(∫
τ
Ψh(g)(β)
)
∈ H.
(Actually in the body of the paper we use another formula for
RP0(α, β| σ, τ), that converges faster; see Deﬁnition 4.3.3 and Remark 4.3.4.)
For the limiting process we introduce the binary subdivisions of I2. The k-th
binary subdivision is the cellular decomposition of I2 into 4k equal squares, and
we denote it by sd k I2. The 1-skeleton of sd k I2 is denoted by sk 1 sdk I2. Its fun-
damental group (based at v0) is denoted by π1(sk1 sdk I2). It is very important
that the group π1(sk1 sdk I2) is a free group on 4 k generators. We say that a kite
(σ, τ) is patterned on sdk I2 if for every piece σi of the string σ, the image σi(I1) is
a 1-cell of sd k I2, and τ(I2) is a 2-cell of sd k I2.
A tessellation of I2 is by deﬁnition a sequence
(
(σi, τi)
)
i=1,...,4k of square kites in
(I2, v0), each patterned on sd k I2, satisfying the following topological condition.
Let us denote by [∂(σi, τi)] the element of π1(sk1 sdk I2) represented by the closed
string ∂(σi, τi). Then
(0.8.2)
4k
∏
1=1
[∂(σi, τi)] = [ ∂I2]
in π1(sk1 sdk I2).
For the construction we choose a particular tessellation for every k. It is called
the k-th binary tessellation , and the notation is tes k I2. The actual deﬁnition of
tesk I2 is not important (since it is quite arbitrary, and chosen for convenience).
All that is important are its two properties:
• It is a tessellation; i.e. equation (0.8.2) holds.
• It has a recursive (self similar) nature.
For ﬁxed k and a kite (σ, τ) we obtain, by a simple geometric operation, the
k-binary tessellation
tesk(σ, τ) =
(
tesk
i (σ, τ)
)
i=1,...,4k
of (σ, τ), which is a sequence of kites in (X, x0). (See Deﬁnition 4.2.7.)
For every i∈{ 1, . . . , 4k} we have the basic Riemann product
RP0(α, β| tesk
i (σ, τ))
on the kite tes k
i (σ, τ). We deﬁne the k-th Riemann product to be
(0.8.3) RP k(α, β| σ, τ) :=
4k
∏
1=1
RP0(α, β| tesk
i (σ, τ)).
NONABELIAN MULTIPLICATIVE INTEGRATION 7
In Theorem 4.4.15 we prove that the limit
lim
k→∞
RPk(α, β| σ, τ)
exists in H. The proof goes like this: for sufﬁciently large k the kites tesk
i (σ, τ) are
all tiny. We use estimates to show that the limits
lim
k′→∞
RPk′ (α, β| tesk
i (σ, τ))
exist for every i. Due to the recursive nature of the binary tessellations, this is
enough. We can ﬁnally deﬁne
(0.8.4) MI (α, β| σ, τ) := lim
k→∞
RPk(α, β| σ, τ).
0.9. In Section 6 we prove the 2-dimensional Stokes Theorem. It is the same
as Theorem 0.4.2, except that it talks about piecewise smooth forms on a pointed
polyhedron and linear quadrangular kites. Again the proof is by reduction (using
the recursive nature of the binary tessellations) to the case of a tiny kite. And then
we use approximations (both of Taylor expansions and the exponential map) to
do the calculation.
A very important technical consequence of the 2-dimensional Stokes Theorem
is:
Theorem 0.9.1 (Fundamental Relation). Let C = ( G, H, Ψ, Φ) be a Lie crossed mod-
ule, (X, x0) a pointed polyhedron, (α, β) a piecewise smooth
connection-curvature pair for C/X, and (σ, τ) a linear quadrangular kite in (X, x0).
Consider the elements
g := MI
(
α| ∂(σ, τ)
)
∈ G
and
h := MI(α, β| σ, τ)∈ H.
Then
Ψ(g) = AdH(h)
as automorphisms of the Lie group H.
In Section 8 we prove the ﬁrst version of the main result of the paper, namely
the 3-dimensional Stokes Theorem (Theorem 8.6.6). This is like Theorem 0.5.4,
only for piecewise smooth connection-curvature pairs, and for linear quadrangu-
lar balloons.
The strategy of the proof is this. Using Theorem 0.9.1, and a lot of combina-
torics of free groups (done in Section 7), we reduce the problem to the case of a
tiny balloon. And for a tiny balloon we use Taylor expansions and the estimates
from Theorem 2.1.2.
0.10. Finally, in Section 9, we show how to pass from quadrangular kites to
triangular ones. This is very easy, using the following trick. The triangle ∆2 is
naturally embedded in the square I2; and there is a piecewise linear retraction
h : I2→ ∆2. Consider the “universal triangular kite” (σ′, τ′) , and the “universal
quadrangular kite” (σ′, τ′′), both in (I2, v0); see Figures 34, 35 and 36. There is a
piecewise linear retraction
g : I2→ σ′(I1)∪ τ′(I2).
These maps are related by
τ′◦ h = g◦ τ′′,
as maps I2→ I2.
8 AMNON YEKUTIELI
Given a smooth kite (σ, τ) in a pointed manifold (X, x0), there a piecewise
smooth map f : I2→ X such that f◦ σ′ = σ and f◦ τ′ = τ. Given a smooth
connection-curvature pair (α, β) for C/X, the pair
(α′, β′) := ( f∗(α), f∗(β))
is a piecewise smooth connection-curvature pair (α, β) for C/I2. We deﬁne
(0.10.1) MI (α, β| σ, τ) := MI(α′, β′| σ′, τ′′).
The results proved for quadrangular kites can be easily transferred to triangu-
lar kites by similar geometric tricks.
0.11. The reason we became interested in nonabelian multiplicative integration
is its application to twisted deformation quantization of algebraic varieties, as
developed in our paper [Ye3] (see also the survey article [Ye4]). Twisted deforma-
tions of an algebraic variety X are very close to gerbes and to stacks of algebroids
(in the sense of [Ko]). Our original strategy was to classify these twisted defor-
mations in terms of Maurer-Cartan solutions in a DG Lie algebra gotten as the
commutative ˇCech resolution of a sheaf of DG Lie algebras on X. The multiplica-
tive integration was supposed to be a key component of this construction. Some
of the details are explained in Subsections 5.6, 5.7 and 9.5.
In the meanwhile we discovered a more direct approach to the classiﬁcation
of twisted deformations, using descent data in cosimplicial crossed groupoids,
and a related invariance result (see Sections 5-6 in the latest version of [Ye3], and
Theorem 0.1 in [Ye6]).
In the version of [Ye3] dated 26 August 2009 there was a “result” labeled The-
orem 11.2, about cosimplicial quantum type DG Lie algebras, Deligne crossed
groupoids and descent data. The proof of this “result” was only sketched, and
we never completed the proof (it was supposed to have appeared in a separate
paper). It is now presented as Conjecture 9.5.2 at the end of this paper.
Speaking of conjectures, we should mention Conjecture 9.4.1 regarding the
rationality of the 2-dimensional multiplicative integral when the Lie groups G
and H are unipotent algebraic groups.
Despite the fact that the original motivation for this paper no longer exists, we
believe that the constructions and results presented here have independent value.
This can be seen for instance by the role our work has in the recent paper [BGNT].
See the next subsection for a discussion of [BGNT] and other related papers.
0.12. We end the introduction with a discussion of recent related work. Our 2-
dimensional nonabelian multiplicative integral is closely related to the differential
geometry of gerbes , as developed by Breen and Messing [BM]. Indeed, the notion
of fake curvature, that goes into our deﬁnition of connection-curvature pair, and
the notion of 3-curvature, are both taken from [BM].
There is a series of papers by Baez, Schreiber and Waldorf ([BS], [SW1], [SW2]
and others) on nonabelian gauge theory. They develop a theory of nonabelian curva-
ture that seems to be very similar to our 2-dimensional nonabelian multiplicative
integral, even though the ﬂavor of their work is very different (it is much more
abstract). It seems that [SW2] contains a proof the 3-dimensional Stokes Theorem
in the special case where the 3-curvature is zero.
Very recently the paper [BGNT] by Bressler, Gorokhovsky, Nest and Tsygan
came out. The goal of this paper is to prove that several existing notions of the
NONABELIAN MULTIPLICATIVE INTEGRATION 9
nerve of a 2-groupoid are equivalent (as simplicial sets). The comparison be-
tween the Hinich simplicial set and the Deligne-Getzler simplicial set is done
using 2-dimensional nonabelian multiplicative integration. The method seems to
be quite similar, at least morally, to our original program (see previous subsec-
tion and Conjecture 9.5.2). The 2-dimensional nonabelian multiplicative integral
that is developed in Sections 4-5 of [BGNT] is inspired by our work, and they ob-
tain a version of our 3-dimensional Stokes Theorem in their setting (see [BGNT,
Theorems 5.1 and 5.2]).
The difference between the construction in [BGNT] and ours is that they work
in the special case of a Lie crossed module (G, H, Ψ, Φ) consisting of unipotent
algebraic groups G and H, and an algebraic connection-curvature pair (α, β) with
vanishing 3-curvature. The construction goes like this: they write a particular
partial differential equation, and the multiplicative integral is its unique solution.
This construction is signiﬁcantly shorter than ours; and presumably it coincides
with our construction in this setup. Cf. Subsection 5.5 of our paper. See the end of
Subsection 9.4 regarding the relation between the work of [BGNT] and Conjecture
9.4.1.
0.13. Acknowledgments. Work on this paper began together with Fredrick Leit-
ner, and I wish to thank him for his contributions, without which the paper could
not have been written. Thanks also to Michael Artin, Maxim Kontsevich, Damien
Calaque, Lawrence Breen, Amos Nevo, Yair Glasner, Barak Weiss and Victor Vin-
nikov for assistance on various aspects of the paper.
NONABELIAN MULTIPLICATIVE INTEGRATION 11
Figure 5. The polyhedra ∆1∼= I1, ∆2 and I2, with their vertices
and orientations.
1. P olyhedra and Piecewise Smooth Geometry
1.1. Conventions. In this paper we work over the ﬁeld R of real numbers. We
denote by An = An(R) the real n-dimensional afﬁne space, with the usual smooth
(i.e. C∞ differentiable) manifold structure, and the standard euclidean metric. The
symbol⊗ stands for⊗R. The coordinate functions on An are t1, . . . ,tn.
1.2. Embedded Polyhedra. By linear map f : Am→ An we mean the composi-
tion of a linear homomorphism and a translation. Thus the group of invertible
linear maps of An is GL n(R) ⋉ Rn. By linear subset X of An we mean the zero
locus of some set of linear functions (not necessarily homogeneous). In other
words X is the image of some injective linear map f : Am→ An; and then we let
m be the dimension of X.
Given a set S⊂ An, its linear (resp. convex) hull is the smallest linear (resp.
convex) subset of An containing S. In case S is ﬁnite, say S ={x1, . . . ,xm}, then
a point x is in the linear (resp. convex) hull of S if and only if x = ∑m
i=1 aixi for
some real numbers a1, . . . ,am satisfying ∑ ai = 1 (resp. and ai≥ 0).
By embedded polyhedron we always mean a convex bounded ﬁnite polyhedron
in An, for some n. Namely a polyhedron X in An is the convex hull of a ﬁnite
subset of An. A point x∈ X is called a vertex if it is not in the convex hull of any
ﬁnite subset of X−{ x}. If we denote by S the set of vertices of X, then S is ﬁnite,
and X is the convex hull of S. The dimension dim X is the dimension of the linear
hull of X, and we call An the ambient linear space of X. The standard euclidean
metric on An restricts to a global metric (a distance function) dist X on X. We
denote by diam (X) the diameter of X, namely the maximal distance between
any two points. The linear functions on An (spanned by t1, . . . ,tn) restrict to
functions X→ R, that we also call linear functions. The R-moduleOlin(X) of
linear functions has rank equal to m := dim X. An R-basis{si}i=1,...,m ofOlin(X)
is called a linear coordinate system on X.
We shall mostly encounter two kinds of embedded polyhedra. The ﬁrst is
the n-dimensional cube In. This is the subset of An deﬁned by the inequalities
0≤ t1, . . . ,tn≤ 1. As a convex set it is spanned by its 2 n vertices. See Figure 5
for an illustration.
The second kind of embedded polyhedron is the n-dimensional simplex ∆n, em-
bedded in An+1. We use barycentric coordinates t0, t1 . . . ,tn on An+1 when deal-
ing with the simplex. In these coordinates ∆n is the subset of An+1 deﬁned by
the conditions 0≤ t0, . . . ,tn and ∑n
i=0 ti = 1. As a convex set it is spanned by its
n + 1 vertices.
12 AMNON YEKUTIELI
Suppose X and Y are both embedded polyhedra. A linear map f : X→ Y
is a function that extends to a linear map between the ambient linear spaces.
Such a map f is determined by its value on a sequence (v0, . . . ,vn) of linearly
independent vertices of X, where n := dim X. Thus we shall often describe the
linear map f as
f (v0, . . . ,vn) = ( w0, . . . ,wn),
or just f = (w0, . . . ,wn), where wi := f (vi).
In case X is the cube In, embedded in An, we shall look at the following linearly
independent vertices: v0 is the origin (0, . . . , 0), and for i = 1, . . . ,n we take
(1.2.1) vi := (0, . . . , 1, . . . , 0),
with 1 in the i-th position. In case of the simplex ∆n, embedded in An+1 with
barycentric coordinates, we look at all its vertices, and use the notation
(v0, . . . ,vn), where vi is as in equation (1.2.1).
1.3. Smooth Maps and Forms. The algebra of smooth real functions on An is
denoted by O(An). The de Rham DG (differential graded) algebra of smooth
differential forms on An is
Ω(An) =
n⨁
p=0
Ωp(An),
with differential d and wedge product∧.
Let X be an m-dimensional polyhedron embedded in An. The set X is a com-
pact topological space, its interior Int (X) is an m-dimensional manifold, and the
boundary ∂X is a ﬁnite union of (m− 1)-dimensional polyhedra. But X also has
a differentiable structure.
Deﬁnition 1.3.1. Let X⊂ An be an embedded polyhedron, and let U⊂ X be an
open set.
(1) A function f : U → R is said to be smooth if it extends to a smooth
function ˜f : ˜U→ R on some open neighborhood ˜U of U in An.
(2) A map f : U→ Ap is called smooth if the functions ti◦ f : U→ R are
smooth for all i∈{ 1, . . . ,p}.
(3) Suppose Y⊂ Ap is an embedded polyhedron, and V⊂ Y is an open set.
A map f : U→ V is called smooth if the composed map f : U→ Ap is
smooth.
(4) Let V be an open subset of an embedded polyhedron. A map f : U→ V
is called a diffeomorphism of it is bijective, and both f and f−1 are smooth.
We denote byO(U) the R-algebra of all smooth functions U→ R. A smooth
map f : U→ V between open subsets of embedded polyhedra induces an R-
algebra homomorphism f∗ :O(V)→O (U), namely pullback.
Suppose X is an embedded polyhedron and U⊂ X is an open set. We let
Int(U) := U∩ Int(X) and ∂(U) := U∩ ∂(X). Note that Int (U) is a manifold, and
it is dense in U.
Deﬁnition 1.3.2. Let X⊂ An be an embedded polyhedron, and let U⊂ X be an
open set. A smooth differential p-form on U is a differential form α∈ Ωp(Int(U)),
that extends to a form ˜α∈ Ωp( ˜U) on some open neighborhood ˜U of U in An.
We denote by Ωp(U) the set of differential p-forms on U, and we let
Ω(U) :=
⨁
p≥0
Ωp(U).
NONABELIAN MULTIPLICATIVE INTEGRATION 13
This is a DG subalgebra of Ω(Int(U)).
Suppose U and V are open subsets of embedded polyhedra. A smooth map
f : U→ V induces a DG algebra homomorphism f∗ : Ω(V)→ Ω(U). If f is an
inclusion then we usually write α|U := f∗(α) for α∈ Ω(V).
Let X be an m-dimensional embedded polyhedron, and U⊂ X a nonempty
open set. Then Ωp(U) is a freeO(U)-module of rank (m
p ). Indeed, if we choose a
linear coordinate system{si}i=1,...,m on X, then the family
(1.3.3) {dsi1∧···∧ dsip}1≤i1<···<ip≤m
is a basis for Ωp(U) asO(U)-module.
Deﬁnition 1.3.4. Let s = {si}i=1,...,m be a linear coordinate system on the m-
dimensional polyhedron X. Given a form α∈ Ωp(X), it has a unique expansion
as a sum
α = ∑
i
˜αi· dsi1∧···∧ dsip,
where i = ( i1, . . . ,ip) runs over the set of strictly increasing multi-indices in the
range{1, . . . ,m}, and ˜αi∈O (X). The functions ˜αi are called the coefﬁcients of α
with respect to the linear coordinate system s.
Let us denote by Ωconst(An) the R-subalgebra of Ω(An) generated by the ele-
ments dt1, . . . , dtn. Now suppose X is an m-dimensional polyhedron in An. The
image of Ωconst(An) under the canonical surjection Ω(An)→ Ω(X) is denoted
by Ωconst(X), and its elements are called constant differential forms . There is an
isomorphism of graded algebras
Ω(X)∼=O(X)⊗ Ωconst(X).
If we choose a linear coordinate system s ={si}i=1,...,m on X, then (1.3.3) is an
R-basis for Ωp
const(X).
Deﬁnition 1.3.5. Given a smooth form α∈ Ωp(X) and a point x∈ X, we deﬁne
the constant form associated to α at x to be
α(x) := ∑
i
˜αi(x)· dsi1∧···∧ dsip∈ Ωp
const(X),
where the functions ˜αi are the coefﬁcients of α relative to some linear coordinate
system s ={si}, as in Deﬁnition 1.3.4.
Note that α(x) is independent of the linear coordinate system.
Let f : X→ Y be a linear map between embedded polyhedra. If g is a linear
function on Y, then f∗(g) = g◦ f is a linear function on X; and if α∈ Ωconst(Y),
then f∗(α)∈ Ωconst(X).
1.4. Manifolds with Sharp Corners. Manifolds with corners are modeled on
Rn
≥0; cf. [Le] or [Jo]. However not all polyhedra are manifolds with corners;
so we introduce a variant in which the local model is an embedded polyhedron.
See Remark 1.4.4 below.
Deﬁnition 1.4.1. Let X be a topological space.
(1) A smooth chart with sharp corners on X is a pair (U, φ), where U is an open
subset of an embedded polyhedron, and φ : U→ X is a map such that
φ(U) is open in X and φ : U→ φ(U) is a homeomorphism.
14 AMNON YEKUTIELI
(2) Two smooth charts with sharp corners (U1, φ1) and (U2, φ2) are compati-
ble if
φ−1
2 ◦ φ1 : φ−1
1
(
φ1(U1)∩ φ2(U2)
)
→ φ−1
2
(
φ1(U1)∩ φ2(U2)
)
is a diffeomorphism.
(3) A smooth atlas with sharp corners on X is a collection{(Ui, φi)} of compati-
ble charts with sharp corners, such that X =⋃
i φi(Ui).
Deﬁnition 1.4.2. A smooth manifold with sharp corners is a Hausdorff second count-
able topological space X endowed with a smooth atlas with sharp corners{(Ui, φi)}.
Deﬁnition 1.4.3. Let X and Y be smooth manifolds with sharp corners, with
atlases{(Ui, φi)} and{(Vj, ψj)} respectively. A map f : X→ Y is called smooth if
for every i, j the map
ψ−1
j ◦ f◦ φi : ( f◦ φi)−1(ψj(Vj))→ Vj
is smooth.
Remark 1.4.4. If we were to restrict the class of polyhedra in Deﬁnition 1.4.2 to
cubes (or simplices), then we would recover the usual deﬁnition of manifold with
corners. “Sharp corners” occur when too many faces of a polyhedron meet at a
vertex (to be precise, more than the dimension of the manifold; e.g. at the top
vertex of a pyramid with square base).
There are several notions of smooth maps between manifolds with corners in
the literature. Suppose X and Y are smooth manifolds with corners, and f : X→
Y is a smooth map in the sense of Deﬁnition 1.4.3. Then f is called “weakly
smooth” in [Jo]. In order for f to be smooth according to [Jo] it must satisfy a
condition involving the boundary strata of X and Y; such a condition can’t even
be stated when sharp corners are present.
Proposition 1.4.5. The category of smooth manifolds with sharp corners contains the
following categories as full subcategories:
(1) The category of smooth manifolds (without boundary) and smooth maps between
them.
(2) The category of embedded polyhedra and smooth maps between them (Deﬁnition
1.3.1(3)).
We leave out the easy proof.
A function f : X→ R is called smooth if when viewed as a map f : X→ A1 it
is smooth. We denote byO(X) the R-algebra of smooth functions.
If U is an open subset of a smooth manifold with sharp corners X, then U
inherits a structure of smooth manifold with sharp corners.
A smooth manifold with sharp corners X has an intrinsic decomposition X =
∂X ∐ Int(X), where the interior Int (X) is a manifold without boundary, and the
boundary ∂X is a manifold with sharp corners. The condition for a point x∈ X
to belong to Int (X) is that it has an open neighborhood that’s isomorphic, as
manifold with sharp corners, to a manifold without boundary.
We say that a manifold with sharp corners X has dimension n if the mani-
fold Int(X) has dimension n. (Of course every connected component of X has a
dimension.) In this case ∂X has dimension n− 1.
Let X be a smooth manifold with sharp corners with atlas {(Ui, φi)}. For
every i we have a diffeomorphism φi : Int(Ui)→ Int(φi(Ui)) between manifolds
NONABELIAN MULTIPLICATIVE INTEGRATION 15
without boundaries, and Int (φi(Ui)) = φi(Ui)∩ Int(X). The module of smooth
differentials Ωp(Ui) was introduced in Deﬁnition 1.3.2.
Deﬁnition 1.4.6. Let X be a smooth manifold with sharp corners with atlas
{(Ui, φi)}. A smooth differential p-form on X is a differential form α∈ Ωp(Int(X)),
such that for every i the form
φ∗
i (α|Int(φi(Ui)))∈ Ωp(Int(Ui))
extends to a form ˜αi∈ Ωp(Ui).
We denote by Ωp(X) the set of differential p-forms on X, and we let
Ω(X) :=
⨁
p≥0
Ωp(X).
This is a DG subalgebra of Ω(Int(X)). Of course Ω0(X) =O(X).
A smooth map f : X→ Y between manifolds with sharp corners induces a
DG algebra homomorphism f∗ : Ω(Y)→ Ω(X).
Convention 1.4.7. For the rest of the paper, by “manifold” we always mean a
smooth manifold with sharp corners, as deﬁned in Deﬁnition 1.4.2. Smooth maps
between manifolds are in the sense of Deﬁnition 1.4.3.
1.5. Abstract Polyhedra. It turns out that the geometric structure of a polyhe-
dron is easy to encode, and it is nicer to work with polyhedra that are not em-
bedded.
By a global metric on a topological space Z we mean a distance function dist Z :
Z2 → R≥0 that induces the topology of Z. Recall that if Z is an embedded
polyhedron in Am, then Z inherits a global metric from the ambient afﬁne space,
and also an R-module of linear functionsOlin(Z)⊂O (Z).
Deﬁnition 1.5.1. A polyhedron is a smooth manifold with sharp corners X, to-
gether with a global metric dist X and an R-submoduleOlin(X)⊂O (X). The
condition is that there exists an isomorphism of smooth manifolds with sharp
corners f : X ≃− →Z for some embedded polyhedron Z⊂ Am, with these two
properties:
(i) f is an isometry; i.e. f : (X, distX)→ (Z, distZ) is an isomorphism of
metric spaces.
(ii) The R-algebra isomorphism f∗ : O(Z) → O (X) satisﬁes
f∗(Olin(Z)) =Olin(X).
The composed map f : X → Am is called a linear metric embedding . If only
property (ii) holds, then f : X→ Am is called a a linear embedding.
In terms of this deﬁnition, an embedded polyhedron is a polyhedron X
equipped with a particular linear metric embedding f : X→ Am.
Deﬁnition 1.5.2. Let X and Y be polyhedra, and let f : X→ Y be a map.
(1) We say f is smooth if it is a smooth map of smooth manifolds with sharp
corners (see Deﬁnition 1.4.3).
(2) We say f is linear if f∗(Olin(Y))⊂O lin(X).
By linear coordinate system on X we mean an R-basis ofOlin(X).
Proposition 1.5.3. Let X be a polyhedron, and let s ={si}i=1,...,n be linear coordinate
system on X. Consider the induced smooth map f : X→ An. Then the image Z := f (X)
is an n-dimensional embedded polyhedron in An, f : X→ Z is an isomorphism of smooth
16 AMNON YEKUTIELI
manifolds with sharp corners, and f ∗(Olin(Z)) =Olin(X). I.e. the map f : X→ An is
a linear embedding.
The proof is left as an exercise.
Suppose we are given linear embeddings X→ Am and Y→ An. It is easy to
see that a map f : X→ Y is linear in the sense of Deﬁnition 1.5.2 if and only if f
extends to a linear map Am→ An.
Note that we said nothing about the metrics in Proposition 1.5.3.
Deﬁnition 1.5.4. An orthonormal linear coordinate system on X is a linear coordinate
system s such that the induced map f : X→ An is a linear metric embedding.
Let s be an orthonormal linear coordinate system on X. Then for any x, y∈ X
the distance between them is
distX(x, y) =
(
∑
n
i=1
(
si(x)− si(y)
)2)1/2
.
We can view our polyhedra as “Riemannian manifolds”, in the following sense.
First note that we can talk about the DG algebra Ωconst(X) of constant forms: it
is the DG algebra generated over R by the family of forms {dsi}i=1,...,n, where
s ={si}i=1,...,n is a linear coordinate system. If moreover s is an orthonormal
linear coordinate system, then consider the constant symmetric 2-form
ωX :=
n
∑
i=1
dsi⊗ dsi∈ Ω1
const(X)⊗R Ω1
const(X)⊂ Ω1(X)⊗O(X) Ω1(X).
The form ωX is independent of the orthonormal linear coordinate system. It
encodes the global metric (the distance function dist X) in the obvious way.
Suppose f : X→ Y is a linear map between polyhedra. Then
f∗(ωY)∈ Ω1
const(X)⊗R Ω1
const(X).
The map f is conformal if and only if f∗(ωY) = aωX for some positive real
number a, which we call the scaling factor. And f is a linear metric embedding if
and only if a = 1.
Let X be a polyhedron. The linear functions on X, i.e. the elements ofOlin(X),
allow us to construct the convex hull of any subset S⊂ X (cf. Proposition 1.5.3).
A sub-polyhedron Z of X is by deﬁnition the convex hull of a ﬁnite subset of X.
Z inherits from X (by restriction) a structure of a polyhedron. The inclusion map
Z→ X is also called a linear metric embedding.
1.6. Piecewise Smooth Forms and Maps. Let X be an n-dimensional polyhedron
(Deﬁnition 1.5.1). A p-dimensional linear simplex in X is by deﬁnition the image
of an injective linear map τ : ∆p → X. A linear triangulation of X is a ﬁnite
collection{Xj}j∈J of linear simplices in X, such that Xj⁄= Xk if j⁄= k; each face
of a simplex Xj is the simplex Xk for some k∈ J; for any j, k∈ J the intersection
Xj∩ Xk is the simplex Xl for some l∈ J; and X = ⋃
j∈J Xj. We let Jp :={j∈ J|
dim Xj = p}, so J = ∐0≤p≤n Jp. The topological space
skp T :=
⋃
q≤p
⋃
j∈Jq
Xj
is called the p-skeleton of the triangulation T.
We shall have to use piecewise smooth differential forms on polyhedra. Sup-
pose T ={Xj}j∈J is a linear triangulation of a polyhedron X. A piecewise smooth
NONABELIAN MULTIPLICATIVE INTEGRATION 17
differential p-form on X, relative to the triangulation T, is a collection{αj}j∈J of differ-
ential forms, with αj∈ Ωp(Xj), such that for any inclusion Xj⊂ Xk of simplices
one has αj|Xk = αk. Let us denote by Ωp
pws(X; T) the set of piecewise smooth
differential p-form on X relative to T, and
Ωpws(X; T) :=
n⨁
p=0
Ωp
pws(X; T),
where n := dim X. This is a DG algebra.
Next suppose S ={Yk}k∈K is a linear triangulation of X which is a subdi-
vision of T. This means that each simplex Yk is contained in some simplex Xj.
Take a piecewise smooth differential form α ={αj}∈ Ωp
pws(X; T). Then there is
a unique piecewise smooth differential form β ={βk}∈ Ωp
pws(X; S) satisfying
βk = αj|Yk for any inclusion Yk⊂ Xj. In this way we get a DG algebra homo-
morphism Ωpws(X; T)→ Ωpws(X; S), which is actually injective. Since any two
triangulations have a common subdivision, the DG algebras Ωpws(X; T) form a
directed system.
Deﬁnition 1.6.1. Let X be a polyhedron. The algebra of piecewise smooth differential
forms on X is the DG algebra
Ωpws(X) := lim
T→
Ωpws(X; T),
where T runs over all linear triangulations of X.
This deﬁnition is very similar to Sullivan’s PL forms; see [FHT].
Note that any element of Ωp
pws(X) is represented by some α ∈
Ωp
pws(X; T), where T is a linear triangulation of X. Such a triangulation T is
called a smoothing triangulation for α. There are injective DG algebra homomor-
phisms
(1.6.2) Ω(X)→ Ωpws(X; T)→ Ωpws(X).
It is an exercise to show that the cohomology of Ω(X) vanishes in positive
degrees, and H 0 Ω(X) = R (recall that X is convex). Also the homomorphisms
(1.6.2) are quasi-isomorphisms. (We shall not use these facts.)
Deﬁnition 1.6.3. Let X be a polyhedron, and let Y be a manifold (see Convention
1.4.7).
(1) Let T ={Xj}j∈J be a linear triangulation of X. A map f : X→ Y is called
a piecewise smooth map relative to T if f|Xj : Xj→ Y is smooth for every
j∈ J.
(2) A map f : X→ Y is a piecewise smooth map if it is piecewise smooth relative
to some linear triangulation T; and then we say that T is a smoothing
triangulation for f .
Note that a piecewise smooth map f : X→ A1 is the same as an element of
the R-algebraOpws(X) := Ω0
pws(X). Given a piecewise smooth map f : X→ Y,
there is an induced DG algebra homomorphism
f∗ : Ω(Y)→ Ωpws(X).
Next suppose X and Y are both polyhedra. Then we can talk about piecewise
linear maps f : X→ Y, using linear triangulations of X as explained in the previ-
ous paragraph. Given a piecewise linear map f : X→ Y, there is an induced DG
18 AMNON YEKUTIELI
algebra homomorphism
f∗ : Ωpws(Y)→ Ωpws(X).
As usual, if f is an embedding, then we write α|X := f∗(α) for α∈ Ωpws(Y).
Let α∈ Ωp
pws(X). The form α can be presented as follows. Choose a smoothing
triangulation T = {Xj}j∈J for α; so that α|Xj ∈ Ωp(Xj) for every j. Let s =
(s1, . . . ,sn) be a linear coordinate system on X. For any j let ˜αj,i∈O (Xj) be the
coefﬁcients of α|Xj with respect to s, as in Deﬁnition 1.3.4. Then
(1.6.4) α|Xj = ∑
i
˜αj,i· dsi1∧···∧ dsip∈ Ωp(Xj),
where the multi-index i = (i1, . . . ,ip) runs through all strictly increasing elements
in{1, . . . ,n}p.
Let X be an n-dimensional polyhedron. Given a form α∈ Ωpws(X) and a
point x∈ X, we say that x is a smooth point of α if there exists some n-dimensional
simplex Y in X, such that x∈ Int Y and α|Y∈ Ω(Y). The smooth locus of α, i.e.
the set of all smooth points of α, is open and dense in X. Its complement, called
the singular locus of α, is contained in a ﬁnite union of simplices of dimensions
< n. Indeed, given any triangulation T that smooths α, the singular locus of α is
contained in the (n− 1)-skeleton of T.
Let f : X→ Y be a piecewise smooth map from a polyhedron to a manifold.
As above we can talk about the smooth locus of f , and whether f|Z : Z→ Y is
smooth for some simplex Z⊂ X.
1.7. Sobolev Norm. It shall be very convenient to have a bound for piecewise
smooth forms on polyhedra and some of their derivatives.
Let X be a polyhedron, with orthonormal linear coordinate system s =
(s1, . . . ,sn). Given a smooth function f∈O (X) and a multi-index
i = (i1, . . . ,iq)∈{ 1, . . . ,n}q,
we write
∂i f := ∂q
∂si1···∂siq
f∈O (X).
In the case q = 0, so the only sequence is the empty sequence ∅, we write ∂∅ f :=
f . We refer to the operators ∂i as the partial derivatives with respect to s.
Deﬁnition 1.7.1. Let X be a polyhedron of dimension n, and let s be an orthonor-
mal linear coordinate system on X.
(1) Take a smooth differential form α∈ Ωp(X). Consider the coefﬁcients ˜αi of
α with respect to s, as in Deﬁnition 1.3.4. Let ∂j be the partial derivatives
with respect to s. For a point x∈ X and a natural number q we deﬁne
‖α‖Sob;x,q :=
(
∑i,j (∂j ˜αi)(x)2
)1/2
,
where the sum is on all j∈{ 1, . . . ,n}q and on all strictly increasing i∈
{1, . . . ,n}p.
(2) For α∈ Ωp(X) we deﬁne
‖α‖Sob := sup
q=0,1,2
sup
x∈X
‖α‖Sob;x,q .
NONABELIAN MULTIPLICATIVE INTEGRATION 19
(3) Take a piecewise smooth differential form α∈ Ωp
pws(X). Let {Xj}j∈J be
some smoothing triangulation for α, and let αj := α|Xj∈ Ωp(Xj). Deﬁne
‖α‖Sob := sup
j∈J
‖αj‖Sob .
The number‖−‖Sob is called the Sobolev norm to order 2.
Remark 1.7.2. Even for a smooth function f , our Sobolev norm‖ f‖Sob is not the
same as the usual order 2 Sobolev norm from functional analysis, namely ‖ f‖s
with s = 2. But it is in the “same spirit”, and hence we use this name.
Proposition 1.7.3. Let X be an n-dimensional polyhedron.
(1) For α∈ Ωp(X), x∈ X and q∈ N, the number‖α‖Sob;x,q is independent of the
orthonormal linear coordinate system s on X. Hence the number ‖α‖Sob is also
coordinate independent.
(2) Given α∈ Ωp
pws(X), its Sobolev norm‖α‖Sob is independent of the smoothing
triangulation{Xj}j∈J.
(3) Let Z be a sub-polyhedron of X and let α∈ Ωp
pws(X). Then‖α|Z‖Sob≤‖ α‖Sob.
Proof. (1) Let us denote by V the vector space of constant vector ﬁelds on X.
This is a rank n vector space, endowed with a canonical inner product. The set
{ ∂
∂si
}i=1,...,n is an orthonormal basis for V.
For p, q∈ N let us denote by T q(V) and⋀p(V) the tensor power and exterior
power of V, respectively. The vector space T q(V)⊗⋀p(V) has an induced inner
product.
For a strictly increasing sequence
i = (i1, . . . ,ip)∈{ 1, . . . ,n}p
let us write
πi := ∂
∂si1
∧···∧ ∂
∂sip
∈⋀p(V).
Then the set {∂j⊗ πi}, where the indices run over all j∈ {1, . . . ,n}q and all
strictly increasing i∈{ 1, . . . ,n}p, is an orthonormal basis of T q(V)⊗⋀p(V).
Now V is the linear dual of Ω1
const(X), so πi can be viewed as a linear map
Ωp(X) → O(X). Given α ∈ Ωp(X), its coefﬁcients with respect to s satisfy
˜αi = πi(α). Thus
∂j ˜αi = ( ∂j◦ πi)(α)
inO(X).
Suppose s′ = (s′
1, . . . ,s′
n) is another orthonormal linear coordinate system. Let
us denote by ∂′
j, ˜α′
i and π′
i the new operators and coefﬁcient, namely those with
respect to s′. The set{∂′
j⊗ π′
i} is also an orthonormal basis of T q(V)⊗⋀p(V). So
this set and the set{∂j⊗ πi} are related by a constant orthogonal matrix (of size
nq· (n
p)). It follows that
∑
i,j
(∂′
j ˜α′
i)(x)2 = ∑
i,j
(∂j ˜αi)(x)2
for any x∈ X.
We see that‖α‖Sob;x,q is independent of coordinates. The assertion for ‖α‖Sob
is now clear.
(2) The supremum on x can be restricted to a dense open set in each cell Xj
of the triangulation {Xj}j∈J. Therefore we get the same value by replacing the
triangulation{Xj}j∈J with a reﬁnement.
20 AMNON YEKUTIELI
(3) Given Z, choose an orthonormal linear coordinate system on it, and extend it
to an orthonormal linear coordinate system on X. Now it is clear. □
1.8. Orientation and Integration. An orientation on a manifold means a choice
of a volume form, up to multiplication by a positive smooth function. However
in the case of a polyhedron we can normalize the volume form:
Deﬁnition 1.8.1. Let X be a polyhedron of dimension n. An orientation on X is a
constant form or (X)∈ Ωn
const(X), such that
or(X) = ds1∧···∧ dsn
for some orthonormal linear coordinate system (s1, . . . ,sn) on X.
Note that if (s′
1, . . . ,s′
n) is some other orthonormal linear coordinate system,
then
or(X) =±ds′
1∧···∧ ds′
n.
If the sign is + then (s′
1, . . . ,s′
n) is said to be positively oriented.
For the polyhedron In there is a standard orientation, coming from its embed-
ding in An. It is
or(In) := dt1∧···∧ dtn,
where (t1, . . . ,tn) is the standard coordinate system on An. Likewise for the
polyhedron ∆n: we let
or(∆n) := dt1∧···∧ dtn,
where (t0, . . . ,tn) is the barycentric coordinate system on An+1. For n = 1, 2 the
orientations can be also described by arrows – see Figure 5.
Deﬁnition 1.8.2. Let X be an n-dimensional oriented polyhedron and let α ∈
Ωn(X). The coefﬁcient of α is the function ˜α∈O (X) such that α = ˜α· or(X).
In other words, ˜α is the coefﬁcient of α with respect to any positively oriented
orthonormal linear coordinate system, in the sense of Deﬁnition 1.3.4.
An orientation on X induces an orientation on the (n− 1)-dimensional polyhe-
dra that make up the boundary ∂X (by contracting the orientation volume form
of X with a constant outer gradient to the face; cf. [Wa, Section 4.8]).
Let X be an n-dimensional oriented polyhedron. Suppose α = {αj}j∈J
∈ Ωn
pws(X; T), where T = {Xj}j∈J is some linear triangulation of X. Any n-
dimensional simplex Xj inherits an orientation, and hence the integral
∫
Xj
αj is
well-deﬁned. We let ∫
X
α := ∑
j∈Jn
∫
Xj
αj∈ R .
This integration is compatible with subdivisions, and thus we have a well-deﬁned
function ∫
X
: Ωn
pws(X)→ R.
Theorem 1.8.3 (Stokes Theorem). Let X be an oriented n-dimensional polyhedron, and
let α∈ Ωn−1
pws (X). Then
∫
X
dα =
∫
∂X
α .
NONABELIAN MULTIPLICATIVE INTEGRATION 21
Proof. Choose a linear triangulation T ={Xj}j∈J of X that smooths α; so that
α ={αi}j∈J with αj∈ Ωn−1(Xj). Then by deﬁnition of
∫
∂X α, and by cancellation
due to opposite orientations of inner (n− 1)-dimensional simplices, we get
∫
∂X
α = ∑
j∈Jn
∫
∂Xj
αj.
And the usual Stokes Theorem tells us that∫
∂Xj
αj =
∫
Xj
dαj .
□
1.9. Piecewise Continuous Forms. For a polyhedron X, let us denote byOcont(X)
the set of continuous R-valued functions on X. This is a commutative R-algebra
containingOpws(X).
Deﬁnition 1.9.1. Let p be a natural number. By piecewise continuous p-form on X
we mean an element γ∈ Ωp
pwc(X), where we deﬁne
Ωp
pwc(X) :=Ocont(X)⊗Opws(X) Ωp
pws(X).
A piecewise continuous p-form γ can be represented as follows: there are con-
tinuous functions f1, . . . ,fm∈O cont(X), and piecewise smooth forms α1, . . . ,αm∈
Ωp
pws(X), such that
(1.9.2) γ =
m
∑
i=1
fi· αi.
For p = 0 we have Ωp
pwc(X) =Ocont(X) of course. But for p > 0 these forms
are much more complicated, as we shall see below.
Warning: the exterior derivative d (γ) is not deﬁned for γ∈ Ωp
pwc(X); at least
not as a piecewise continuous form (it is a distribution). The problem of course
is that the functions fi above cannot be derived.
However, given γ∈ Ωp
pwc(X) and a piecewise linear map g : Y→ X between
polyhedra, the pullback
g∗(γ)∈ Ωp
pwc(Y)
is well deﬁned. In terms of the expansion (1.9.2), the formula is
g∗(γ) =
m
∑
i=1
g∗( fi)· g∗(αi).
Here g∗( fi)∈O cont(Y) and g∗(αi)∈ Ωp
pws(Y). If g is a closed embedding then
we write γ|Y := g∗(γ) as usual.
The presentation (1.9.2) of γ∈ Ωp
pwc(X) can be expanded further. Choose a
linear triangulation {Xj}j∈J of X that smooths all the piecewise smooth forms
α1, . . . ,αm. Also choose a linear coordinate system s = ( s1, . . . ,sn) on X. For any
i∈{ 1, . . . ,m} and j∈ J let ei,j,k∈O (Xj) be the coefﬁcients of the smooth form
αi|Xj with respect to s, as in Deﬁnition 1.3.4. Then
(1.9.3) γ|Xj =
m
∑
i=1
∑
k
fi· ei,j,k· dsk1∧···∧ dskp∈ Ωp
pwc(Xj),
where as usual the multi-index k = ( k1, . . . ,kp) runs through all strictly increas-
ing elements in{1, . . . ,n}p.
22 AMNON YEKUTIELI
For top degree forms one can say more. Let γ∈ Ωn
pwc(X). In this case the
expansion (1.9.3) can be simpliﬁed to
(1.9.4) γ|Xj =
m
∑
i=1
fi· ei,j· ds1∧···∧ dsn∈ Ωn
pwc(Xj),
with ei,j∈O (Xj).
Now assume that the polyhedron X is oriented. We can choose the coordinate
system s = (s1, . . . ,sn) so that it is orthonormal and positively oriented; and then
or(X) = ds1∧···∧ dsn.
For any j∈ Jn we can integrate the continuous function ∑m
i=1 fi· ei,j on the ori-
ented n-dimensional simplex Xj, obtaining
∫
Xj
γ :=
∫
Xj
m
∑
i=1
fi· ei,j· ds1∧···∧ dsn∈ R.
Using this formula we deﬁne
(1.9.5)
∫
X
γ := ∑
j∈Jn
∫
Xj
γ∈ R.
Proposition 1.9.6. For an n-dimensional oriented polyhedron X and a piecewise contin-
uous form γ∈ Ωn
pwc(X), the number
∫
X γ is independent of the presentation (1.9.4) of
γ.
We leave out the easy proof.
More generally, suppose X is an n-dimensional polyhedron (not necessarily
oriented), Z is an oriented p-dimensional polyhedron, τ : Z→ X is a piecewise
linear map, and γ∈ Ωp
pwc(X). Then τ∗(γ)∈ Ωp
pwc(Z), and we can use (1.9.5) to
integrate γ along τ as follows:
(1.9.7)
∫
τ
γ :=
∫
Z
τ∗(γ)∈ R.
NONABELIAN MULTIPLICATIVE INTEGRATION 23
2. E stimates for the Nonabelian Exponential Map
2.1. The Exponential Map. Nonabelian exponential map We need some prelim-
inary results on the exponential maps of Lie groups. Let G be a (ﬁnite dimen-
sional) Lie group over R, with Lie algebra g = Lie(G). The exponential map
expG : g→ G
is an analytic map, satisfying exp G(0) = 1 and exp (−α) = exp(α)−1. The ex-
ponential map is a diffeomorphism near 0 ∈ g. Namely there is an open neigh-
borhood U0(g) of 0 in g, such that V0(G) := expG(U0(g)) is open in G, and
expG : U0(g)→ V0(G) is a diffeomorphism. Let log G : V0(G)→ U0(g) be the
inverse of exp G. We call such V0(G) an open neighborhood of 1 in G on which logG
is deﬁned. See [Va, Sections 2.10] for details.
The exponential map is functorial. Namely given a map φ : G→ H of Lie
groups, the diagram
Lie(G)
expG //
Lie(φ)

G
φ

Lie(H)
expH // H
is commutative.
When there is no danger of confusion we write exp and log instead of exp G
and logG, respectively.
The product in G is denoted by·, and the Lie bracket in g is denoted by [−,−].
Given a ﬁnite sequence (g1, . . . ,gm) of elements in the group G, we write
(2.1.1)
m
∏
i=1
gi := g1· g2··· gm∈ G .
It is a basic fact that if α1, . . . ,αm∈ g are commuting elements, then
m
∏
i=1
exp(αi) = exp
(
∑
m
i=1 αi
)
.
The next theorem lists several estimates for the discrepancy when the elements
do not necessarily commute.
Theorem 2.1.2. Let G be a Lie group, with Lie algebra g. Let V 0(G) be an open neigh-
borhood of 1 in G on which log is well-deﬁned, and let ‖−‖ be a euclidean norm on g.
Then there are real constants ϵ0(G) and c0(G) with the following properties:
(i) 0 < ϵ0(G)≤ 1 and 0≤ c0(G).
(ii) Let α1, . . . ,αm∈ g be such that ∑m
i=1‖αi‖ < ϵ0(G). Then
m
∏
i=1
exp(αi)∈ V0(G),
‖‖ log
(
∏
m
i=1 exp(αi)
)‖‖≤ c0(G)· ∑
m
i=1‖αi‖
and
‖‖ log
(
∏
m
i=1 exp(αi)
)
− ∑
m
i=1 αi
‖‖≤ c0(G)·
(
∑
m
i=1‖αi‖
)2.
(iii) Let α1, α2∈ g be such that‖α1‖ +‖α2‖ < ϵ0(G). Then
‖[α1, α2]‖≤ c0(G)·‖ α1‖·‖ α2‖,
24 AMNON YEKUTIELI
‖‖ log
(
exp(α1)· exp(α2)
)
− (α1 + α2 + 1
2 [α1, α2])
‖‖
≤ c0(G)·‖ α1‖·‖ α2‖·
(
‖α1‖ +‖α2‖
)
.
and
‖‖ log
(
exp(α1)· exp(α2)· exp(α1)−1· exp(α2)−1)
− [α1, α2]
‖‖
≤ c0(G)·‖ α1‖·‖ α2‖·
(
‖α1‖ +‖α2‖
)
.
(iv) Let α1, . . . ,αm, β1, . . . ,βm∈ g be such that
m
∑
i=1
(‖αi‖ +‖βi‖) < ϵ0(G) .
Then
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
(
∏
m
i=1 exp(αi)
)
− ∑
m
i=1 βi
‖‖
≤ c0(G)·
(
∑
m
i=1(‖αi‖ +‖βi‖)
)
·
(
∑
m
i=1‖βi‖
)
.
and ‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
(
∏
m
i=1 exp(αi)
)‖‖
≤ c0(G)·
(
∑
m
i=1‖βi‖
)
.
(v) Let α1, . . . ,βm be as in property (iv), and assume moreover that [αi, αj]
= 0 for all i, j. Then
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− ∑
m
i=1(αi + βi)
‖‖
≤ c0(G)·
(
∑
m
i=1(‖αi‖ +‖βi‖)
)
·
(
∑
m
i=1‖βi‖
)
.
The theorem is proved at the end of Subsection 2.5, after some preparations.
The constants c0(G) and ϵ0(G) are called a commutativity constant and a conver-
gence radius for G respectively. (If G is abelian one can take c0(G) = 0.)
2.2. The CBH Theorem. There is an element F(x, y) in the completed free Lie
algebra over Q in the variables x, y, called the Hausdorff series. See [Bo, Sections
II.6 and II.7], where the letter H is used instead of F. For any i, j≥ 0 let us denote
by Fi,j(x, y) the homogeneous component of F(x, y) of degree i in x and degree j
in y. So
F(x, y) = ∑
i,j≥0
Fi,j(x, y)
Now consider a Lie group G as before, with Lie algebra g. Choose a euclidean
norm‖−‖ on the vector space g. Given elements α, β∈ g we can evaluate Fi,j(x, y)
on them, obtaining an element Fi,j(α, β)∈ g.
The Campbell-Baker-Hausdorff Theorem says that there is an open neighborhood
U1 of 0 in g (its size depending on the norm) such that the series F(α, β) converges
absolutely and uniformly for α, β∈ U1, and moreover
(2.2.1) exp
(
F(α, β)
)
= exp(α)· exp(β).
This assertion is not explicit in the book [Bo]; it requires combining various
scattered results in Sections II.7 and III.4 of [Bo]. An explicit statement of the
CBH Theorem is [Va, Theorem 2.15.4]. However the treatment of the structure of
the Hausdorff series is not sufﬁciently detailed in [Va].
For a positive number r we denote by U(r) the open ball of radius r and center
0 in g, and by U(r) its closure (the closed ball).
NONABELIAN MULTIPLICATIVE INTEGRATION 25
Lemma 2.2.2. There are constants ϵ1 and c 1, such that 0 < ϵ1, U (ϵ1)⊂ U1, 0≤ c1,
and for every α, β∈ U(ϵ1) the inequality
‖‖ F(α, β)− (α + β + 1
2 [x, y])
‖‖≤ c1·‖ α‖·‖ β‖· (‖α‖ +‖β‖)
holds.
Proof. Let us denote by fi,j the norm of the bi-homogeneous function
Fi,j : g× g→ g.
Namely
fi,j := sup{‖Fi,j(α, β)‖|‖ α‖,‖β‖≤ 1}.
So for any α, β∈ g one has
‖Fi,j(α, β)‖≤ fi,j·‖ α‖i·‖ β‖j.
In [Bo, Section II.7.2] it is shown that there is a positive number ϵ1, such that the
series ∑i,j≥0 fi,jϵi+j
1 converges (to a ﬁnite sum). By shrinking ϵ1 if necessary, we
may assume that U(ϵ1)⊂ U1.
Now in [Bo, Section II.6.4] it is proved that
F1,0(x, y) = x, F0,1(x, y) = y, F1,1(x, y) = 1
2 [x, y]
and
Fi,0(x, y) = F0,j(x, y) = 0 for i, j⁄= 1.
Thus for α, β∈ U(ϵ1) we have
F(α, β)− (α + β + 1
2 [x, y]) = ∑
(i,j)∈I
Fi,j(α, β),
where
I :={(i, j)| i, j≥ 1 and i + j≥ 3}.
Now if (i, j)∈ I and 0≤ a, b≤ ϵ1, then
aibj≤ ab(a + b)· ϵi+j−3
1 .
Therefore for α, β∈ U(ϵ1), with a :=‖α‖ and b :=‖β‖, we have the estimate
‖‖ ∑
(i,j)∈I
Fi,j(α, β)
‖‖≤ ∑
(i,j)∈I
‖‖ Fi,j(α, β)
‖‖
≤ ∑
(i,j)∈I
fi,j· ai· bj≤ ab(a + b)· ϵ−3
1 · ∑
(i,j)∈I
fi,j· ϵi+j
1 .
Taking the number
c1 := ϵ−3
1 · ∑
(i,j)∈I
fi,j· ϵi+j
1
does the trick. □
26 AMNON YEKUTIELI
2.3. Calculations with a Few Elements. We continue with the chosen open set
V0(G)⊂ G and norm‖−‖ on the Lie algebra g. In this subsection we translate
the estimate for the CBH series to estimates on exp and log. Recall our notation:
U(r) is the open ball of positive radius r in g, and U(r) is the closed ball.
Lemma 2.3.1. There exist constants ϵ2, c2∈ R such that
0 < ϵ2≤ 1 and 1≤ c2,
and such the following formulas hold for every α, β∈ U(ϵ2).
exp(α)· exp(β)∈ V0(G), (2.3.2)
‖ [α, β]‖≤ c2·‖ α‖·‖ β‖ , (2.3.3)
and
(2.3.4)
‖‖ log
(
exp(α)· exp(β)
)
− (α + β + 1
2 [α, β])
‖‖
≤ c2·‖ α‖·‖ β‖·
(
‖α‖ +‖β‖
)
.
Proof. The existence of a positive ϵ2 making formula (2.3.2) true is easy (due to
continuity). We can assume ϵ2≤ min(1, ϵ1).
The existence of a number c2 making inequality (2.3.3) valid is also easy, be-
cause the function‖ [α, β]‖ is bilinear and g is ﬁnite dimensional. We can assume
that c2≥ max(1, c1).
Finally, the validity of formula (2.3.4) comes from Lemma 2.2.2 and the CBH
formula (2.2.1). □
Lemma 2.3.5. There is a real number c3 such that c3≥ c2, and for any α1, α2, β1, β2∈ g
satisfying‖αi‖ +‖βi‖ < ϵ2 the inequality
(2.3.6)
‖‖ log
(
exp(α1 + β1)· exp(α2 + β2)
)
− log
(
exp(α1)· exp(α2)
)‖‖
≤ c3· (‖β1‖ +‖β2‖).
holds.
Proof. Given α∈ U(ϵ2) we have a smooth (in fact analytic) function fα : U(ϵ2)→
g deﬁned by
fα(β) := log
(
exp(α)· exp(β)
)
.
Let g∗ be the dual space of g, and let d β fα∈ g∗ be the derivative of fα at β. Then
Taylor expansion of fα around β gives us
(2.3.7) fα(β + γ) = fα(β) + (dβ fα)(γ) + (R≥2
β fα)(γ)
for any γ∈ U(ϵ2). Here R≥2
β fα is just the remainder, in other words the higher
order part of the Taylor expansion. The linear term (dβ fα)(γ) can be estimated
by
‖(dβ fα)(γ)‖≤ a1·‖ γ‖
for a suitable positive number a1. The remainder (R≥2
β fα)(γ) can be estimated by
‖(R≥2
β fα)(γ)‖≤ a2·‖ γ‖2
for some positive number a2.
These inequalities tell us that if α, β, γ∈ U(ϵ2) then
(2.3.8)
‖‖ log
(
exp(α)· exp(β + γ)
)
− log
(
exp(α)· exp(β)
)‖‖
=
‖‖ log
(
fα(β + γ)
)
− log
(
fα(β)
)‖‖
≤ a1·‖ γ‖ + a2·‖ γ‖2≤ (a1 + a2)·‖ γ‖.
NONABELIAN MULTIPLICATIVE INTEGRATION 27
In a similar way we look at the function gβ(α) := fα(β), and we obtain con-
stants b1, b2 such that
(2.3.9)
‖‖ log
(
exp(α + γ)· exp(β)
)
− log
(
exp(α)· exp(β)
)‖‖≤ (b1 + b2)·‖ γ‖.
Therefore by taking
c3 := max{c2, a1 + a1, b1 + b2}
all conditions are satisﬁed. □
Lemma 2.3.10. There exists a constant c4≥ c3 such that the following inequalities hold
for any α, β∈ g satisfying‖α‖,‖β‖ < ϵ2.
‖‖ log
(
exp(α)· exp(β)
)
− (α + β)
‖‖≤ c4·‖ α‖·‖ β‖
and ‖‖ log
(
exp(α)· exp(β)
)‖‖≤‖ α‖ +‖β‖ + c4·‖ α‖·‖ β‖ .
Proof. From Lemma 2.3.1 and the triangle inequality we get
‖‖ log
(
exp(α)· exp(β)
)
− (α + β)
‖‖
≤ c2·‖ α‖·‖ β‖·
(
‖α‖ +‖β‖
)
+ 1
2 c2·‖ α‖·‖ β‖
≤ 3c2·‖ α‖·‖ β‖ .
This proves the ﬁrst inequality, with c4 := max(c3, 3c2). The second inequality is
an immediate consequence. □
2.4. Calculations with Many Elements. Let us deﬁne
(2.4.1) ϵ4 := 1
12 c−1
4 · ϵ2 .
Lemma 2.4.2. Let α1, . . . ,αm∈ g be such that ∑m
i=1‖αi‖ < ϵ4. Then the relation and
inequalities below hold:
(2.4.3)
m
∏
i=1
exp(αi)∈ V0(G),
(2.4.4)
‖‖ log
(
∏
m
i=1 exp(αi)
)‖‖≤ 3
2
m
∑
i=1
‖αi‖
and
(2.4.5)
‖‖ log
(
∏
m
i=1 exp(αi)
)
− ∑
m
i=1 αi
‖‖≤ c4·
(
∑
m
i=1‖αi‖
)2 .
Proof. Recall that ϵ2≤ 1 and c4≥ 1.
For m = 1 all is clear. Take m = 2. Then since‖αi‖ < ϵ2 we have
exp(α1)· exp(α2)∈ V0(G)
by Lemma 2.3.1. Next, since‖α1‖≤ 1
6 c−1
4 , it follows that
c4·‖ α1‖·‖ α2‖≤ 1
6‖α2‖ .
From this and Lemma 2.3.10 we see that
‖‖ exp(α1)· exp(α2)
‖‖≤‖ α1‖ +‖α2‖ + c4·‖ α1‖·‖ α2‖≤ 3
2· (‖α1‖ +‖α2‖) .
Hence (2.4.4) holds for m = 2. Again using Lemma 2.3.10 we have
‖‖ log
(
exp(α1)· exp(α2)
)
− (α1 + α2)
‖‖
≤ c4·‖ α1‖·‖ α2‖≤ c4· (‖α1‖ +‖α2‖)2.
This ﬁnishes the case m = 2.
28 AMNON YEKUTIELI
Now assume the assertions are true for m ≥ 2, and consider α1, . . . ,
αm+1∈ g such that ∑m+1
i=1 ‖αi‖ < ϵ4. Deﬁne
β := log
(
∏
m
i=1 exp(αi)
)
,
so that
m+1
∏
i=1
exp(αi) = exp(β)· exp(αm+1).
By the induction hypothesis, i.e. inequality (2.4.4) for m, we have
(2.4.6) ‖β‖≤ 3
2
m
∑
i=1
‖αi‖≤ 3
2
m+1
∑
i=1
‖αi‖≤ 3
2· 1
6 c−1
4 · ϵ2 = 1
4 c−1
4 · ϵ2 .
This implies‖β‖ < ϵ2. Since we also have‖αm+1‖ < ϵ2, Lemma 2.3.1 says that
exp(β)· exp(αm+1)∈ V0(G).
This veriﬁes (2.4.3) for m + 1.
Using Lemma 2.3.1 again we see that
‖‖ log
(
exp(β)· exp(αm+1)
)‖‖≤‖ β‖ +‖αm+1‖ + c4·‖ β‖·‖ αm+1‖ .
Because we also have the inequality c4·‖ β‖≤ 1
2, we conclude that
‖β‖ +‖αm+1‖ + c4·‖ β‖·‖ αm+1‖≤ 3
2·‖ β‖ + 3
2·‖ αm+1‖≤ 3
2·
m+1
∑
i=1
‖αi‖ .
Thus inequality (2.4.4) holds for m + 1.
According to Lemma 2.3.10 we have
‖‖ log
(
exp(β)· exp(αm+1)
)
− (β + αm+1)
‖‖≤ c4·‖ β‖·‖ αm+1‖.
The induction assumption for inequality (2.4.5) says that
‖‖ β− ∑
m
i=1 αi
‖‖≤ c4·
(
∑
m
i=1‖αi‖
)2 .
Combining these with the inequality (2.4.6) we obtain
‖‖ log
(
exp(β)· exp(αm+1)
)
− ∑
m+1
i=1 αi
‖‖
≤
‖‖ log
(
exp(β)· exp(αm+1)
)
− (β + αm+1)
‖‖
+
‖‖ (β + αm+1)− ∑
m+1
i=1 αi
‖‖
≤ c4·‖ β‖·‖ αm+1‖ + c4·
(
∑
m
i=1‖αi‖
)2
≤ c4·
(( 3
2 ∑
m
i=1‖αi‖
)
·‖ αm+1‖ +
(
∑
m
i=1‖αi‖
)2)
≤ c4·
(
∑
m+1
i=1 ‖αi‖
)2 .
This proves (2.4.5). □
Lemma 2.4.7. Let α1, . . . ,αm, β1, . . . ,βm∈ g be such that
m
∑
i=1
(
‖αi‖ +‖βi‖
)
< ϵ4 .
Then ‖‖ log
(
∏
m
i=1
(
exp(αi)· exp(βi)
))
− log
((
∏
m
i=1 exp(αi)
)
·
(
∏
m
i=1 exp(βi)
))‖‖
≤ 4c2
4·
(
∑
m
i=1‖αi‖
)
·
(
∑
m
i=1‖βi‖
)
NONABELIAN MULTIPLICATIVE INTEGRATION 29
and ‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
(
∏
m
i=1
(
exp(αi)· exp(βi)
))‖‖
≤ 2c2
4· ∑
m
i=1‖αi‖·‖ βi‖.
Proof. For the ﬁrst inequality we note that for any i, j one has
‖‖ log
(
exp(βj)· exp(αi)
)
− log
(
exp(αi)· exp(βj)
)‖‖
≤ 2c2·‖ αi‖·‖ βj‖·
(
‖αi‖ +‖βj‖
)
+ c2·‖ αi‖·‖ βj‖
≤ 2c2·‖ αi‖·‖ βj‖.
This is due to Lemma 2.3.1. Now for our inequality we have to move all the
exp(βj) in the product across all the exp (αi). According Lemma 2.3.5 the “cost”
of each such move is at most 2 c3· 2c2·‖ αi‖·‖ βj‖. So the total “cost” is at most
∑
m
i,j=1 2c3· 2c2·‖ αi‖·‖ βj‖ = 4c2c3·
(
∑
m
i=1‖αi‖
)
·
(
∑
m
j=1‖βj‖
)
.
Since c4≥ c2, c3 this proves the ﬁrst inequality.
For the second inequality we note that, due to Lemma 2.3.10, we have
‖‖ log
(
exp(αi + βi)
)
− log
(
exp(αi)· exp(βi)
)‖‖≤ c4·‖ αi‖·‖ βi‖.
Since we have to make such a change for every i, according to Lemma 2.3.5 the
total “cost” is at most 2 c3c4· ∑m
i=1‖αi‖·‖ βi‖. □
Lemma 2.4.8. There exists a constant c 5 such that c 5 ≥ max(c4, 3
2 ), and for every
α1, . . . ,αm, β1, . . . ,βm∈ g satisfying
m
∑
i=1
(
‖αi‖ +‖βi‖
)
< ϵ4
one has:
(2.4.9)
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
(
∏
m
i=1 exp(αi)
)
− ∑
m
i=1 βi
‖‖
≤ c5·
(
∑
m
i=1(‖αi‖ +‖βi‖)
)
·
(
∑
m
i=1‖βi‖
)
and
(2.4.10)
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
(
∏
m
i=1 exp(αi)
)‖‖
≤ c5·
(
∑
m
i=1‖βi‖
)
.
If moreover [αi, αj] = 0 for all i, j, then
(2.4.11)
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− ∑
m
i=1(αi + βi)
‖‖
≤ c5·
(
∑
m
i=1(‖αi‖ +‖βi‖)
)
·
(
∑
m
i=1‖βi‖
)
.
Proof. According to Lemma 2.4.7 we have
(2.4.12)
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
((
∏
m
i=1 exp(αi)
)
·
(
∏
m
i=1 exp(βi)
))‖‖
≤ 2c2
4·
m
∑
i=1
‖αi‖·‖ βi‖ .
By Lemma 2.4.2 we know that
(2.4.13)
‖‖ log
(
∏
m
i=1 exp(βi)
)
− ∑
m
i=1 βi
‖‖≤ c4·
(
∑
m
i=1‖βi‖
)2 .
30 AMNON YEKUTIELI
Combining Lemmas 2.3.10 and 2.4.2 we get
(2.4.14)
‖‖ log
((
∏
m
i=1 exp(αi)
)
·
(
∏
m
i=1 exp(βi)
))
−
(
log
(
∏
m
i=1 exp(αi)
)
+ log
(
∏
m
i=1 exp(βi)
))‖‖
≤ c4·
‖‖ log
(
∏
m
i=1 exp(αi)
)‖‖·
‖‖ log
(
∏
m
i=1 exp(βi)
)‖‖
≤ c4·
( 3
2 ∑
m
i=1‖αi‖
)
·
( 3
2 ∑
m
i=1‖βi‖
)
= 9
4 c4·
(
∑
m
i=1‖αi‖
)
·
(
∑
m
i=1‖βi‖
)
.
Putting all these together we obtain the inequality
(2.4.15)
‖‖ log
(
∏
m
i=1 exp(αi + βi)
)
− log
(
∏
m
i=1 exp(αi)
)
− ∑
m
i=1 βi
‖‖
≤ 2c2
4·
(
∑
m
i=1‖αi‖
)
·
(
∑
m
i=1‖βi‖
)
+ 9
4 c2
4·
(
∑
m
i=1‖αi‖
)
·
(
∑
m
i=1‖βi‖
)
+ c4·
(
∑
m
i=1‖βi‖
)2
≤ 6c2
4·
(
∑
m
i=1(‖αi‖ +‖βi‖)
)
·
(
∑
m
i=1‖βi‖
)
.
This proves inequality (2.4.9) with c5 := 7c2
4.
Inequality (2.4.10) follows easily from (2.4.15), once we notice that
6c2
4·
(
∑
m
i=1(‖αi‖ +‖βi‖)
)
≤ 6c2
4· 2ϵ3≤ c4 .
When [αi, αj] = 0 for all i, j we have
log
(
∏
m
i=1 exp(αi)
)
= ∑
m
i=1 αi.
So inequality (2.4.10) holds. □
2.5. Final Touches.
Lemma 2.5.1. There is a real number c 6 such that c 6≥ c5, and for any α, β∈ g with
‖α‖,‖β‖ < ϵ4 the inequality
(2.5.2)
‖‖ log
(
exp(α)· exp(β)· exp(α)−1· exp(β)−1)
− [α, β]
‖‖
≤ c6·‖ α‖·‖ β‖·
(
‖α‖ +‖β‖
)
.
holds.
Proof. Let’s write
a := exp(α), b := exp(β),
γ+ := α + β + 1
2 [α, β], γ− :=−α− β + 1
2 [α, β],
δ+ := log(a· b)− γ+, δ− := log(a−1· b−1)− γ−.
According to Lemma 2.3.1 we have
‖δ+‖,‖δ−‖≤ c2·‖ α‖·‖ β‖·
(
‖α‖ +‖β‖
)
and
‖γ+‖,‖γ−‖≤‖ α‖ +‖β‖ + 1
2 c2·‖ α‖·‖ β‖≤ (1 + c2)(‖α‖ +‖β‖) .
Now
a· b = exp(γ+ + δ+)
and
a−1· b−1 = exp(γ− + δ−).
NONABELIAN MULTIPLICATIVE INTEGRATION 31
So by Lemma 2.3.5 we have
‖‖ log
(
(a· b)· (a−1· b−1)
)
− log
(
exp(γ+)· exp(γ−)
)‖‖
≤ c3· (‖δ+‖ +‖δ−‖)
≤ 2c2c3·‖ α‖·‖ β‖·
(
‖α‖ +‖β‖
)
.
On the other hand, since α + β and−α− β commute, by formula (2.4.11) in
Lemma 2.4.8 we have‖‖ log
(
exp(γ+)· exp(γ−)
)
− [α, β]
‖‖
=
‖‖ log
(
exp((α + β) + 1
2 [α, β])· exp((−α− β) + 1
2 [α, β])
)
−
(
(α + β) + 1
2 [α, β] + (−α− β) + 1
2 [α, β]
)‖‖
≤ c5·
(
2·‖ α‖ + 2·‖ β‖ +‖[α, β]‖
)
·
(
‖[α, β]‖
)
≤ c5· (2 + c2· ϵ4)· c2·‖ α‖·‖ β‖·
(
‖α‖ +‖β‖
)
.
In the last inequality we used
‖[α, β]‖≤ c2·‖ α‖·‖ β‖≤ c2· ϵ4·‖ β‖ .
Therefore (2.5.2) holds with
c6 := 2c2c3 + c5· (2 + c2ϵ4)· c2 .
□
Proof of Theorem 2.1.2. Take c0(G) := c6 and ϵ0(G) := ϵ4. Since ϵ4≤ ϵ2 and
c6≥ c5≥ max(c4, 3
2 )≥ c4≥ c3≥ c2 ,
the assertions of the theorem are contained on Lemmas 2.3.1, 2.4.2, 2.4.8 and
2.5.1. □
NONABELIAN MULTIPLICATIVE INTEGRATION 33
3. M ultiplicative Integration in Dimension One
Nonabelian multiplicative integration in dimension 1 is classical, dating back
to work of Volterra (cf. [DF]). In modern differential geometry it is usually viewed
as the holonomy of a connection along a path. We prefer to do everything from
scratch, for several reasons: this allows us to introduce notation; it serves as
a warm-up for the much more difﬁcult 2-dimensional integration; and also to
cover the case of piecewise smooth differential forms.
3.1. Binary Tessellations. Recall that I1 is the unit line segment in A1 = A1(R),
which we view as an oriented polyhedron (cf. Section 1). The vertices (endpoints)
of I1 are v0 = 0 and v1 = 1, and the coordinate function is t1.
Let X be a polyhedron. Consider a linear map σ : I1→ X. The length of the
line segment Z := σ(I1)⊂ X (possibly zero) is denoted by len (σ). If σ is not
constant then it is a conformal map, and the scaling factor is precisely len (σ). In
this case σ determines an orientation on the 1-dimensional polyhedron Z. We
may choose an orthonormal linear coordinate function f1 on Z, such that d f1 is
the orientation of Z. Then σ∗(d f1) = len(σ)· dt1.
Next consider a piecewise linear map σ : I1→ X. By deﬁnition (cf. Subsection
1.6) there is a linear triangulation {Yj}j∈J of I1 such that σ|Yj : Yj→ X is a linear
map for every j∈ J. We deﬁne
len(σ) := ∑
j∈J1
len(σj).
It is convenient to have a composition operation for piecewise linear maps.
Suppose σ : I1 → X and ρ : I1 → I1 are piecewise linear maps. Then the
set-theoretical composition σ◦ ρ is also a piecewise linear map I1→ X. Given
ﬁnite sequences σ = ( σi)i=1,...,m and ρ = ( ρj)j=1,...,n of piecewise linear maps
σi : I1→ X and ρj : I1→ I1, we deﬁne the sequence of piecewise linear maps
σ◦ ρ := ( σi◦ ρj)(i,j)∈{1,...,m}×{1,...,n}
in lexicographical order, i.e.
(3.1.1) σ◦ ρ = ( σ1◦ ρ1, σ1◦ ρ2,··· , σ2◦ ρ1, σ2◦ ρ2,··· , σm◦ ρn) .
Deﬁnition 3.1.2. For any k≥ 0, the k-th binary tessellation of I1 is the sequence
tesk I1 = ( σk
1, . . . ,σk
2k )
of linear maps in σk
i : I1→ I1 deﬁned recursively as follows.
• For k = 0 we deﬁne σ0
1 to be the identity map of I1.
• For k = 1 we take the linear maps σ1
1 , σ1
2 deﬁned on vertices by
σ1
1 (v0, v1) := (v0, 1
2 ),
σ1
2 (v0, v1) := ( 1
2, v1).
• For k≥ 1 we deﬁne
tesk+1 I1 := (tes1 I1)◦ (tesk I1),
using the convention (3.1.1).
We call σ0
1 the basic map.
See Figure 6 for an illustration of tes 2 I1.
34 AMNON YEKUTIELI
Figure 6. The 2-nd binary tessellation of I1. The arrowheads
indicate the orientations of the linear maps σ2
i : I1→ I1.
3.2. Riemann Products. Let g be a ﬁnite dimensional Lie algebra over R. For
any n-dimensional polyhedron X we then have the DG Lie algebra of piecewise
smooth g-valued differential forms
Ωpws(X)⊗ g =
n⨁
p=0
Ωp
pws(X)⊗ g
(Subsection 1.6). The operations are as follows: for αi∈ Ωpi
pws(X) and γi∈ g one
has
d(α1⊗ γ1) = d(α1)⊗ γ1∈ Ωp1+1
pws (X)⊗ g
and
[α1⊗ γ1, α2⊗ γ2] = ( α1∧ α2)⊗ [γ1, γ2]∈ Ωp1+p2
pws (X)⊗ g.
By deﬁnition, any particular piecewise smooth differential form α belongs to
Ωpws(X; T)⊗ g, for some linear triangulation T of X. This construction is func-
torial in the following sense. Suppose f : X→ Y is a piecewise linear map of
polyhedra, and φ : g→ h is map of Lie algebras. Then there is a homomorphism
of DG Lie algebras
f∗⊗ φ : Ωpws(Y)⊗ g→ Ωpws(X)⊗ h.
In case h = g and φ is the identity map, we shall often write f∗ instead of f∗⊗ φ.
From now on in this section we consider a Lie group G, with Lie algebra g,
and a polyhedron X. We ﬁx some euclidean norm ‖−‖ on the vector space g. As
in Section 1 we also ﬁx an open neighborhood V0(G) of 1 in G on which log G is
deﬁned, a convergence radius ϵ0(G), and a commutativity constant c0(G). The
choices of V0(G), ϵ0(G) and c0(G) are auxiliary only; they are needed for the
proofs, but do not effect the results.
Deﬁnition 3.2.1. Let α∈ Ω1
pws(I1)⊗ g. The basic Riemann product of α on I1 is the
element
RP0(α| I1)∈ G
deﬁned as follows. Let w := 1
2, namely the midpoint of I1.
• Suppose w is a smooth point of α. Then there is some 1-
dimensional simplex Y in I1, such that w∈ Int Y and α|Y is smooth. Let
˜α∈O (Y)⊗ g be the coefﬁcient of α|Y, as in Deﬁnition 1.8.2; namely
α|Y = ˜α· dt1.
We deﬁne
RP0(α| I1) := expG
(˜α(w)
)
.
• If w is a singular point of α, then we let RP 0(α| I1) := 1.
Observe that the element ˜α(w)∈ g in the deﬁnition above is independent of
the simplex Y.
NONABELIAN MULTIPLICATIVE INTEGRATION 35
Deﬁnition 3.2.2. Let α∈ Ω1
pws(X)⊗ g, and let σ : I1→ X be a piecewise linear
map. Then σ∗(α)∈ Ω1
pws(I1)⊗ g, and we deﬁne the basic Riemann product of α
along σ to be
RP0(α| σ) := RP0
(
σ∗(α)| I1)
∈ G.
Note that if σ is a constant map then σ∗(α) = 0, so RP0(α| σ) = 1.
Deﬁnition 3.2.3. Let α∈ Ω1
pws(X)⊗ g, and let σ : I1→ X be a piecewise linear
map. For k≥ 0 we deﬁne the k-th reﬁned Riemann product of α along σ to be
RPk(α| σ) :=
2k
∏
i=1
RP0(α| σ◦ σk
i )∈ G,
using the k-th binary tessellation tesk I1 = ( σk
1, . . . ,σk
2k ) and the convention (2.1.1).
3.3. Convergence of Riemann Products. As before we are given a form α ∈
Ω1
pws(X)⊗ g. Recall ‖α‖Sob, the Sobolev norm to order 2 of α, from Subsection
1.7.
Lemma 3.3.1. There are constants c1(α) and ϵ1(α) with the following properties.
(i) These inequalities hold:
0 < ϵ1(α)≤ 1 ,
c1(α)≥ 1 ,
ϵ1(α)· c1(α)≤ 1
2· ϵ0(G) .
(ii) For any piecewise linear map σ : I1→ X such that len(σ) < ϵ1(α), and for any
sufﬁciently large k, one has
RPk(α| σ)∈ V0(G)
and
‖ logG
(
RPk(α| σ)
)
‖≤ c1(α)· len(σ).
(iii) Moreover, if the map σ in (ii) is linear, then the assertions there hold for any
k≥ 0.
Proof. We are given a piecewise linear map σ : I1→ X. Let us write ϵ := len(σ).
Excluding the trivial case, we may assume that ϵ > 0.
Take k≥ 0. For any index i∈{ 1, . . . , 2k} let Wi := σk
i (I1) and wi := σk
i ( 1
2 );
so wi is the midpoint of the segment (1-dimensional polyhedron) Wi. Deﬁne
ϵi := len(σ◦ σk
i ), Zi := σ(Wi) and zi := σ(wi). Note that ∑i ϵi = ϵ.
We will say that an index i is good if the map σ|Wi is linear and injective. In
this case Zi is a segment of length ϵi and midpoint zi. Otherwise we will call
i a bad index. The sets of good and bad indices are denoted by good (k) and
bad(k) respectively. Let m be the number of singular points of the map σ. Then
|bad(k)|≤ m. In particular, if σ is linear then bad (k) = ∅.
Let
α′ := σ∗(α)∈ Ω1
pws(I1)⊗ g.
For an index i we deﬁne an element λi∈ g as follows. If wi is a smooth point of
α′, then let ˜α′
i be the coefﬁcient of α′ near wi, and let
λi := ( 1
2 )k· ˜α′
i(wi).
Otherwise we let λi := 0. In any case we have
expG(λi) = RP0(α′| σk
i ) = RP0(α| σ◦ σk
i ).
36 AMNON YEKUTIELI
Therefore
(3.3.2)
2k
∏
i=1
expG(λi) = RPk(α| σ).
Furthermore, if i is a good index and wi is a smooth point of α′, then zi is a
smooth point α|Zi, and then
(3.3.3) λi = ϵi· ˜αi(zi),
where ˜αi is the coefﬁcient of α|Zi near zi.
Now here are the estimates. For any index i we have
‖λi‖≤ ( 1
2 )k·‖ α′‖Sob .
If i is a good index then by (3.3.3) we have
‖λi‖≤ ϵi·‖ α‖Sob .
Hence
(3.3.4)
2k
∑
i=1
‖λi‖ = ∑
i∈good(k)
‖λi‖ + ∑
i∈bad(k)
‖λi‖
≤ ϵ·‖ α‖Sob + m· ( 1
2 )k·‖ α′‖Sob .
Let
ϵ1(α) := 1
2· (1 +‖α‖Sob)−1· ϵ0(G)
and
c1(α) := 2·
(
1 + c0(G)·‖ α‖Sob
)
.
Choose k0 large enough so that
m· ( 1
2 )k0·‖ α′‖Sob < min
( 1
2· ϵ0(G), 1
2· c1(α)· ϵ· (1 + c0(G))−1)
.
If σ is linear then m = 0, and we may take k0 := 0.
Now suppose that ϵ < ϵ1(α) and k≥ k0. According to inequality (3.3.4) we
have
2k
∑
i=1
‖λi‖ < ϵ0(G) .
Therefore by property (ii) of Theorem 2.1.2 and by formula (3.3.2) we get
RPk(α| σ)∈ V0(G)
and
‖ logG
(
RPk(α| σ)
)
‖≤ c0(G)·
(
∑
2k
i=1‖λi‖
)
≤ c1(α)· ϵ .
□
Remark 3.3.5. Heuristically we think of ϵ in the proof of the lemma above as a
“tiny” size. In the “tiny scale” we can measure things (i.e. ‖logG(g)‖ is deﬁned),
and we can use Taylor series and CBH series.
Lemma 3.3.6. There are constants c2(α) and ϵ2(α) with the following properties.
(i) These inequalities hold:
0 < ϵ2(α)≤ ϵ1(α) ,
c2(α)≥ c1(α) .
NONABELIAN MULTIPLICATIVE INTEGRATION 37
(ii) Suppose σ : I1→ X is a linear map such that len(σ) < ϵ2(α), and α|σ(I1) is
smooth. Then for any k≥ 0 one has
‖‖ logG
(
RPk(α| σ)
)
− logG
(
RP0(α| σ)
)‖‖≤ c2(α)· len(σ)3.
Proof.
Take
ϵ2(α) := min
(
ϵ1(α), 1
4 ϵ0(G)· (1 +‖α‖Sob)−1)
.
Let σ be a linear map with ϵ := len(α) satisfying 0 < ϵ < ϵ2(α). Let Z := σ(I1),
which is a 1-dimensional oriented polyhedron, and z := σ( 1
2 ), the midpoint of
Z. Choose a positively oriented orthonormal linear coordinate function s1 on Z,
such that s1(z) = 0.
Let ˜α∈O (Z)⊗ g be the coefﬁcient of α|Z, i.e. α|Z = ˜α· dt1. Consider the Taylor
expansion to second order of the smooth function ˜α : Z→ g, around the point z:
(3.3.7) ˜α(x) = a0 + s1(x)· a1 + s1(x)2· g(x)
for x ∈ Z, where a0 := ˜α(z) ∈ g, a1 := ( ∂
∂s1
˜α)(z) ∈ g, and g : Z → g is a
continuous function. We know that
‖a0‖,‖a1‖,‖g(x)‖≤‖ α‖Sob .
And, as we have seen before,
(3.3.8) RP 0(α| σ) = expG
(
ϵa0
)
.
Take k≥ 0. For i∈{ 1, . . . , 2k} let σi := σ◦ σk
i and zi := σi( 1
2 ). Since ϵ < ϵ2(α)
it follows that
(3.3.9)
2k
∑
i=1
‖( 1
2 )kϵ· a0‖≤ ϵ·‖ α‖Sob≤ 1
4 ϵ0(G) .
Because|s1(zi)|≤ 1
2 ϵ we also have
(3.3.10)
2k
∑
i=1
‖( 1
2 )kϵ· s1(zi)· a1‖≤ 1
2 ϵ2·‖ α‖Sob≤ 1
4 ϵ0(G)
and
(3.3.11)
2k
∑
i=1
‖( 1
2 )kϵ· s1(zi)2· g(zi)‖≤ 1
4 ϵ3·‖ α‖Sob≤ 1
4 ϵ0(G) .
Deﬁne
λi := ( 1
2 )kϵ· ˜α(zi)∈ g.
By the Taylor expansion (3.3.7) we have
(3.3.12) λi = ( 1
2 )kϵ· a0 + ( 1
2 )kϵ· s1(zi)· a1 + ( 1
2 )kϵ· s1(zi)2· g(zi).
Since σ∗(ds1) = ϵ· dt1, we see that
RP0(α| σi) = expG(λi),
and hence
(3.3.13) RP k(α| σ) =
2k
∏
i=1
expG(λi).
38 AMNON YEKUTIELI
Because the constant terms in the Taylor expansions (3.3.12) of the λi are all
equal to ( 1
2 )kϵ· a0, we can use property (v) of Theorem 2.1.2, together with the
estimates (3.3.9), (3.3.10), (3.3.11), to deduce
(3.3.14)
‖‖ logG
(
∏
2k
i=1 expG(λi)
)
− ∑
2k
i=1 λi
‖‖
≤ c0(G)·
(
ϵ·‖ α‖Sob· (1 + 1
2 ϵ + 1
4 ϵ2)
)
·
(
ϵ·‖ α‖Sob· ( 1
2 ϵ + 1
4 ϵ2)
)
≤ ϵ3· c0(G)·‖ α‖2
Sob· 2 .
Trivially the sum of the constant terms of the Taylor expansions of the λi is
2k
∑
i=1
( 1
2 )kϵ· a0 = ϵ· a0.
The linear terms satisfy
s1(zi) =−s1(z2k−i)
because of symmetry; and therefore they cancel out:
2k
∑
i=1
( 1
2 )kϵ· s1(zi)· a1 = 0.
Therefore, using the estimate (3.3.11) to eliminate the quadratic terms of the Tay-
lor expansions, we conclude that
(3.3.15)
‖‖ ∑
2k
i=1 λi− ϵa0
‖‖≤ 1
4 ϵ3·‖ α‖Sob.
Finally we deﬁne
c2(α) := max
(
c1(α), 2c0(G)·‖ α‖2
Sob + 1
4·‖ α‖Sob
)
.
Combining equations (3.3.8) and (3.3.13), plus the estimates (3.3.15) and (3.3.14),
we obtain ‖‖ logG
(
RP0(α| σ)
)
− logG
(
RPk(α| σ)
)‖‖≤ c2(α)· ϵ3 .
□
Deﬁnition 3.3.16. Let us ﬁx a constant ϵ2(α) as in Lemma 3.3.6. A piecewise
linear map σ : I1→ X with len(σ) < ϵ2(α) will be called an α-tiny piecewise linear
map (in this section).
Remark 3.3.17. We shall use the term “tiny” several times in the paper, each
time with a new meaning, depending on context. The notion “tiny” should be
considered as “local to each section”.
Lemma 3.3.18. Let σ : I1 → X be an α-tiny linear map. Then there is a constant
c3(α, σ)≥ 0, such that for any integers k′≥ k≥ 0 one has
‖‖ logG
(
RPk′ (α| σ)
)
− logG
(
RPk(α| σ)
)‖‖≤ c3(α, σ)· len(σ)· ( 1
2 )k .
Proof. We may assume that len (σ) > 0. Let Z := σ(I1)⊂ X, and let m be the
number of singular points of the differential form α|Z.
Take k≥ 0. For an index i∈{ 1, . . . , 2k} deﬁne σi := σ◦ σk
i and Zi := σi(I1).
We say that i is good if α|Zi is smooth, and otherwise i is bad. The set of good
and bad indices are denoted by good (k) and bad (k) respectively. Since for any
singular point x of α|Z there is at most one index i such that x∈ Int Zi, it follows
that the cardinality of bad (k) is at most m.
NONABELIAN MULTIPLICATIVE INTEGRATION 39
Next take k′≥ k≥ 0, and let l := k′− k. By the recursive deﬁnition of the
binary tessellations we have
RPk(α| σ) =
2k
∏
i=1
RP0(α| σi)
and
RPk′ (α| σ) =
2k
∏
i=1
RPl(α| σi).
If i∈ good(k) then by Lemma 3.3.6 we know that
‖‖ logG
(
RPl(α| σi)
)
− logG
(
RP0(α| σ)i
)‖‖≤ c2(α)· len(σ)3· ( 1
2 )3k.
On the other hand, i∈ bad(k), then by Lemma 3.3.1 we know that
‖‖ logG
(
RPl(α| σi)
)
− logG
(
RP0(α| σ)i
)‖‖≤ 2· c1(α)· len(σ)· ( 1
2 )k.
Therefore by property (iv) of Theorem 2.1.2 we have
‖‖ logG
(
RPk′ (α| σ)
)
− logG
(
RPk(α| σ)
)‖‖
=
‖‖ logG
(
∏
2k
i=1 RPl(α| σi)
)
− logG
(
RP0(α| σi)
)‖‖
≤ c0(G)·
(
|bad(k)|· 2· c1(α)· len(σ)· ( 1
2 )k
+|good(k)|· c2(α)· len(σ)3· ( 1
2 )3k)
.
Thus we may take
c3(α, σ) := c0(G)·
(
2m· c1(α) + c2(α)
)
.
□
Theorem 3.3.19. Let X be a polyhedron, let α∈ Ω1
pws(X)⊗ g, and let σ : I1→ X be a
piecewise linear map. Then the limit limk→∞ RPk(α| σ) exists.
Proof. For any k we have
RPk(α| σ) =
2k
∏
i=1
RP0(α| σ◦ σk
i ) =
2k
∏
i=1
RP0
(
(σ◦ σk
i )∗(α)| I1)
=
2k
∏
i=1
RP0
(
σ∗(α)| σk
i
)
= RPk
(
σ∗(α)| σ0
1
)
by deﬁnition. So after replacing α with σ∗(α), we can assume that X = I1, and
we have to prove that the limit lim k→∞ RPk(α| σ0
1 ) exists.
Take k large enough such that for each i∈ {1, . . . , 2k} the linear map σk
i is
α-tiny. For any k′≥ 0 we have
RPk+k′ (α| σ0
1 ) =
2k
∏
i=1
RPk′ (α| σk
i ).
Thus it sufﬁces to prove that for any i the limit limk′→∞ RPk′ (α| σk
i ) exists.
We have now reduced our problem to showing that for any α-tiny linear map
σ : I1→ X the limit lim k→∞ RPk(α| σ) exists. But this follows immediately from
Lemma 3.3.18. □
40 AMNON YEKUTIELI
Deﬁnition 3.3.20. In the situation of Theorem 3.3.19, the multiplicative integral of
α on σ is
MI(α| σ) := lim
k→∞
RPk(α| σ)∈ G.
If X = I1 and σ = σ0
1 , the basic map, then we write MI (α| I1) := MI(α| σ0
1 ).
Remark 3.3.21. If the group G is abelian, then RP k(α| σ) is the exponential of a
Riemann sum, and therefore in the limit we get
MI(α| σ) = expG
(∫
σ
α
)
.
Proposition 3.3.22. Let σ : I1→ X be a piecewise linear map.
(1) If σ is α-tiny (see Deﬁnition 3.3.16), then MI(α| σ)∈ V0(G), and
‖‖ logG
(
MI(α| σ)
)‖‖≤ c1(α)· len(σ) .
(2) If σ is linear and α-tiny, and if α|σ(I1) is smooth, then for any k≥ 0 one has
‖‖ logG
(
MI(α| σ)
)
− logG
(
RP0(α| σ)
)‖‖≤ c2(α)· len(σ)3 .
(3) For any k≥ 0 one has
MI(α| σ) =
2k
∏
i=1
MI(α| σ◦ σk
i ).
Proof. (1) By Lemma 3.3.1, for sufﬁciently large k we have RPk(α| σ)∈ V0(G) and
‖‖ logG
(
RPk(α| σ)
)‖‖≤ c1(α)· len(σ)≤ 1
2· ϵ0(G) .
Let B be the closed ball of radius 1
2 ϵ0(G) in g, and let Z := expG(B), which is
a compact subset of G. Since for every k one has RP k(α| σ)∈ Z, it follows that
in the limit MI (α| σ)∈ Z⊂ V0(G). The bound on
‖‖ logG
(
MI(α| σ)
)‖‖ is then
obvious.
(2) This is immediate from Lemma 3.3.6.
(3) For every k′≥ 0 we have by deﬁnition
RPk+k′ (α| σ) =
2k
∏
i=1
RPk′ (α| σ◦ σk
i ).
Now pass to the limit k′→ ∞. □
3.4. Functoriality of the MI. The next results are on the functoriality of the mul-
tiplicative integral with respect to G and X.
Proposition 3.4.1. Let Φ : G→ H be a map of Lie groups, with induced Lie algebra
map φ := Lie(Φ) : g→ h. Let f : Y→ X be a piecewise linear map between polyhedra,
and let α∈ Ω1
pws(X)⊗ g. Then for any piecewise linear map σ : I1→ Y one has
Φ
(
MI(α| f◦ σ)
)
= MI
(
( f∗⊗ φ)(α)| σ
)
in H.
Proof. It sufﬁces to consider f and Φ separately; so we look at two cases.
Case 1. H = G and Φ is the identity map. Here for every k≥ 0 and i∈{ 1, . . . , 2k}
we have
RP0(α| f◦ σ◦ σk
i )
)
= RP0
(
( f◦ σ)∗(α)| σk
i
)
= RP0
(
f∗(α)| σ◦ σk
i
)
.
NONABELIAN MULTIPLICATIVE INTEGRATION 41
Hence
RPk(α| f◦ σ) = RPk
(
( f◦ σ)∗(α)| I1)
= RPk
(
f∗(α)| σ
)
.
Going to the limit in k we see that
MI(α| f◦ σ) = MI
(
( f◦ σ)∗(α)| I1)
= MI
(
f∗(α)| σ
)
.
Case 2. Here we assume that Y = X and f is the identity map. Since
MI(α| σ) = MI(σ∗(α)| σ0
1 )
and
MI(φ(α)| σ) = MI((σ∗⊗ φ)(α)| σ0
1 ) = MI(φ(σ∗(α))| σ0
1 ),
we can replace σ with σ0
1 and α with σ∗(α). Therefore we can assume that σ is a
linear map.
Put a euclidean norm on h such that φ : g→ h has operator norm ‖φ‖≤ 1.
This implies that ‖φ(α)‖Sob≤‖ α‖Sob. So we can assume that ϵ1(φ(α))≥ ϵ1(α)
and c1(φ(α))≤ c1(α) (cf. proof of Lemma 3.3.1).
Take k large enough such that σ◦ σk
i is α-tiny for every i∈{ 1, . . . , 2k}. Then
σ◦ σk
i is also φ(α)-tiny.
By part (3) of Proposition 3.3.22 we have
MI(α| σ) =
2k
∏
i=1
MI(α| σ◦ σk
i )
and
MI
(
φ(α)| σ
)
=
2k
∏
i=1
MI
(
φ(α)| σ◦ σk
i
)
.
So it sufﬁces to prove that
Φ
(
MI(α| σ◦ σk
i )
)
= MI
(
φ(α)| σ◦ σk
i
)
for every i.
By this reduction we can assume that σ is α-tiny and also φ(α)-tiny. Take any
k≥ 0, and for every i∈{ 1, . . . , 2k} let wi := σk
i ( 1
2 )∈ I1. If wi is a smooth point of
σ∗(α)∈ Ω1
pws(I1)⊗ g,
then it is also a smooth point of
(σ∗⊗ φ)(α)∈ Ω1
pws(I1)⊗ h.
In this case we have
(3.4.2) Φ
(
RP0(α| σ◦ σk
i )
)
= RP0
(
φ(α)| σ◦ σk
i
)
.
In case wi is a singular point of (σ∗⊗ φ)(α), then it is also a singular point of
σ∗(α). Hence (3.4.2) also holds (both sides are 1).
The only problem is when wi is a smooth point of (σ∗⊗ φ)(α) but a singular
point of σ∗(α).
Now we use the estimate provided by Lemma 3.3.1 (noting that φ◦ logG =
logH◦ Φ):
‖‖ logH
(
Φ
(
RP0(α| σ◦ σk
i )
))
− logH
(
RP0
(
φ(α)| σ◦ σk
i
))‖‖
≤ 2· c1(α)· len(σ)· ( 1
2 )k .
42 AMNON YEKUTIELI
Let m be the number of singular points of σ∗(α). Then using property (iv) of
Theorem 2.1.2 we get
‖‖ logH
(
Φ
(
RPk(α| σ)
))
− logH
(
RPk
(
φ(α)| σ
))‖‖
≤ 2m· c1(α)· len(σ)· ( 1
2 )k .
Since m is independent of k, in the limit k→ ∞ we get
Φ
(
MI(α| σ)
)
= MI
(
φ(α)| σ
)
.
□
A particular case of the above is when we are given a representation of G,
namely a map of Lie groups Φ : G→ GLm(R) for some m. The Lie algebra of
GLm(R) is glm(R) = Mm(R), the algebra of m× m matrices. For a matrix a∈
Mm(R) let us denote by‖a‖ its operator norm, as linear operator a : Rm→ Rm,
where Rm has the standard euclidean inner product.
Proposition 3.4.3. Let Φ : G→ GLm(R) be a representation, and let α∈ Ω1
pws(X)⊗
g. Then there is a constant c 4(α, Φ)≥ 0 such that the following holds:
(∗) Given a piecewise linear map σ : I1→ X, let g := MI(α| σ)∈ G. Then
‖Φ(g)‖≤ exp
(
c4(α, Φ)· len(σ)
)
,
where exp the usual real exponential function.
Proof. Let’s write H := GLm(R), h := glm(R) and α′ := Lie(Φ)(α) ∈
Ω1
pws(X)⊗ h. We use the operator norm on h to determine the constants ϵ1(α′)
and c1(α′) in Deﬁnition 3.3.16.
Take k large enough so that σ◦ σk
i is α′-tiny for every i ∈ {1, . . . , 2k}. Let
d := len(σ) and di := len(σ◦ σi), so d = ∑2k
i=1 di. Deﬁne hi := MI(α′| σ◦ σk
i )∈ H.
Then hi∈ V0(H), and we can deﬁne γi := logH(hi)∈ h.
Since the matrix γi satisﬁes
‖γi‖≤ c1(α′)· di,
it follows that its exponential hi satisﬁes
‖hi‖≤ exp
(
c1(α′)· di
)
.
Now
Φ(g) = MI(α′| σ) =
2k
∏
i=1
hi,
so we obtain
‖Φ(g)‖≤ exp
(
c1(α′)· d
)
.
Therefore we can take c4(α, Φ) := c1(α′). □
3.5. Strings.
Deﬁnition 3.5.1. Let X be a polyhedron. A string in X is a sequence σ =
(σ1, . . . ,σm) of piecewise linear maps σi : I1→ X, such that σi(v1) = σi+1(v0)
for all i. The maps σi : I1→ X are called the pieces of σ. We write σ(v0) := σ1(v0)
and σ(v1) := σm(v1), and call these points the initial and terminal points of σ,
respectively. The length of σ is len(σ) := ∑m
i=1 len(σi).
NONABELIAN MULTIPLICATIVE INTEGRATION 43
Figure 7. The strings σ = ( σ1, σ2, σ3), τ = ( τ1, τ2) and σ∗ τ in
the polyhedron X.
Suppose α∈ Ω1
pws(X)⊗ g. We say that σ is an α-tiny string if len(σ) < ϵ1(α);
cf. Deﬁnition 3.3.16.
Here are a few operations on strings. Suppose σ = ( σ1, . . . ,σm) and τ =
(τ1, . . . ,τl) are two strings in X, with τ(v0) = σ(v1). Then we deﬁne the concate-
nated string
(3.5.2) σ∗ τ := ( σ1, . . . ,σm, τ1, . . . ,τl).
See Figure 7 for an illustration.
The ﬂip of I1 is the linear bijection ﬂip : I1→ I1 deﬁned on vertices by
ﬂip (v0, v1) := (v1, v0).
Given a piecewise linear map σ : I1→ X we let
(3.5.3) σ−1 := σ◦ ﬂip : I1→ X.
For a string σ = ( σ1, . . . ,σm) in X we deﬁne the inverse string
(3.5.4) σ−1 := ( σ−1
m , . . . ,σ−1
1 ).
The empty string is the unique string of length 0, and we denote it by ∅. For
any string σ we let σ∗ ∅ := σ and ∅∗ σ := σ.
Let f : X→ Y be a piecewise linear map between polyhedra, and let σ =
(σ1, . . . ,σm) be a string in X. We deﬁne the string f◦ σ in Y to be
(3.5.5) f◦ σ := ( f◦ σ1, . . . ,f◦ σm).
Remark 3.5.6. The reason for working with strings (rather than with paths, as is
the custom in algebraic topology) is that composition of strings, as deﬁned above,
is associative, whereas composition of paths is only associative up to homotopy.
It will be convenient to integrate along a string. As before G is a Lie group
with Lie algebra g.
Deﬁnition 3.5.7. Suppose α∈ Ω1
pws(X)⊗ g and σ = ( σ1, . . . ,σm) is a string in X.
The multiplicative integral MI(α| σ) of α on σ is
MI(α| σ) :=
m
∏
i=1
MI(α| σi)∈ G.
44 AMNON YEKUTIELI
Proposition 3.5.8. Let α∈ Ω1
pws(X)⊗ g.
(1) Given strings σ and τ in X such that τ(v0) = σ(v1), one has
MI(α| σ∗ τ) = MI(α| σ)· MI(α| τ).
(2) Given a string σ in X , one has
MI(α| σ−1) = MI(α| σ)−1.
(3) If σ is an α-tiny string in X (i.e len(σ) < ϵ1(α)), then MI(α| σ)∈ V0(G), and
‖‖ logG
(
MI(α| σ)
)‖‖≤ c1(α)· len(σ) .
Proof. (1) This is trivial.
(2) By part (1) it sufﬁces to consider a piecewise linear map σ : I1→ X. Since the
ﬂip reverses orientation on I1, it follows that
RP0(α| σ−1) = RP0(α| σ)−1.
From this, and the symmetry of the binary tessellations, it follows that for every
k≥ 0 one has
RPk(α| σ−1) = RPk(α| σ)−1.
In the limit we get MI (α| σ−1) = MI(α| σ)−1.
(3) Say σ = ( σ1, . . . ,σm). Take k large enough so that 2 k≥ m. Let σ′ : I1→ X be
the unique piecewise linear map satisfying σ′◦ σk
i = σi for i≤ m, and σ′◦ σk
i is
the constant map σ(v1) for i > m. Note that len (σ′) = len(σ). By Deﬁnition 3.5.7
and Proposition 3.3.22(3) we have MI (α| σ′) = MI(α| σ). Now use Proposition
3.3.22(1). □
Proposition 3.5.9. Let Φ : G→ H be a map of Lie groups, let f : Y→ X be a piecewise
linear map between polyhedra, and let α∈ Ω1
pws(X)⊗ g. Then for any string σ in Y one
has
Φ
(
MI(α| f◦ σ)
)
= MI
(
( f∗⊗ Lie(Φ))(α)| σ
)
∈ H.
Proof. This is an immediate consequence of Proposition 3.5.8(1) and
Proposition 3.4.1. □
Proposition 3.5.10. Let Φ : G→ GLm(R) be a representation, and let α∈ Ω1
pws(X)⊗
g. Given a string σ in X let g := MI(α| σ). Then the norm of the operator Φ(g) on Rm
satisﬁes
‖Φ(g)‖≤ exp
(
c4(α, Φ)· len(σ)
)
,
where c4(α, Φ) is the constant from Proposition 3.4.3.
Proof. By part (1) of Proposition 3.5.8 the left side of this inequality is multiplica-
tive with respect to the operation∗. And clearly the right side is also multiplica-
tive with respect to∗. So it sufﬁces to consider a piecewise linear map σ : I1→ X.
Now we can use Proposition 3.4.3. □
For a string σ = ( σ1, . . . ,σm) and a form α∈ Ω1
pws(X)⊗ g we write
∫
σ
α :=
m
∑
i=1
∫
σi
α∈ g,
where ∫
σi
α =
∫
I1
σ∗
i (α)
is the usual integral of this g-valued piecewise smooth differential form.
NONABELIAN MULTIPLICATIVE INTEGRATION 45
Proposition 3.5.11. Let α∈ Ω1
pws(X)⊗ g, and let σ be an α-tiny string in X. Then
‖‖ logG
(
MI(α| σ)
)
−
∫
σ
α
‖‖≤ c0(G)· c1(α)2· len(σ)2 .
What this result says, is that in the tiny scale the nonabelian integral is very
close to the abelian integral.
Proof. Step 1. We begin the proof with a reduction to the case m = 1, and σ = σ1
is a single linear map I1→ X. First we append a few empty strings at the end
of σ, so that the number of linear pieces becomes m = 2k for some k. This does
not change len (σ) nor MI (α| σ). Let Z be an oriented 1-dimensional polyhe-
dron (a line segment) of length len(σ), partitioned into segments Z1, . . . ,Zm, with
len(Zi) = len(σi). Let σ′ : I1→ Z be the unique oriented linear bijection. There is
a unique piecewise linear map f : Z→ X, such that σi = f◦ σ′◦ σk
i as piecewise
linear maps I1→ X for every i. Let α′ := f∗(α)∈ Ω1
pws(Z)⊗ g. According to
Propositions 3.3.22(3), 3.5.7 and 3.5.9 we have
MI(α| σ) = MI(α′| σ′).
And clearly ∫
σ
α =
∫
σ′
α′.
Because the piecewise linear map f : Z→ X is a linear metric embedding on
each of its linear pieces, it follows that ‖α′‖Sob ≤ ‖α‖Sob; and hence we can
choose ϵ1(α′)≥ ϵ1(α) and c1(α′)≤ c1(α).
Note that
len(σ′) = len(Z) = len(σ) < ϵ1(α) .
So we can replace X with Z, σ with σ′ and α with α′. Doing so, we can now
assume that m = 1 and σ is a single linear map.
Step 2. Here we assume that σ is an α-tiny linear map, and we let ϵ := len(σ).
Take any k≥ 0. We know that
RPk(α| σ) =
2k
∏
i=1
RP0(α| σ◦ σk
i ).
Also (by Lemma 3.3.1) we have
RPk(α| σ), RP0(α| σ◦ σk
i )∈ V0(G).
For any i let
λi := logG
(
RP0(α| σ◦ σk
i )
)
∈ g,
so
RPk(α| σ) =
2k
∏
i=1
expG(λi).
Let us write
RSk(α| σ) :=
2k
∑
i=1
λi.
This is a Riemann sum for the usual integral.
By Lemma 3.3.1 we have
‖λi‖≤ c1(α)· ( 1
2 )k· ϵ
46 AMNON YEKUTIELI
for every i. Using property (ii) of Theorem 2.1.2 we see that
‖‖ logG
(
RPk(α| σ)
)
− RSk(α| σ)
‖‖
≤ c0(G)·
(
∑
2k
i=1‖λi‖
)2≤ c0(G)· c1(α)2· ϵ2 .
In the limit k→ ∞ we have
lim
k→∞
RSk(α| σ) =
∫
σ
α
and
lim
k→∞
RPk(α| σ) = MI(α| σ),
so the proof is done. □
Corollary 3.5.12. Let α∈ Ω1
pws(X)⊗ g, and let σ be an α-tiny closed string in X which
bounds a polygon Z. Then
‖‖ logG
(
MI(α| σ)
)‖‖≤ c0(G)· c1(α)2· len(σ)2 + area(Z)·‖ α‖Sob .
Proof. Choose an orientation on Z. By the abelian Stokes Theorem (Theorem
1.8.3) we have ‖‖
∫
σ
α
‖‖ =
‖‖
∫
Z
d(α)
‖‖≤ area(Z)·‖ α‖Sob .
Now combine this estimate with the Proposition above. □
Proposition 3.5.13. Let Φ : G→ GLm(R) be a representation, and let α∈ Ω1
pws(X)⊗
g. Then there are constants ϵ5(α, Φ) and c5(α, Φ) such that
0 < ϵ5(α, Φ)≤ 1 and c 5(α, Φ)≥ 1 ,
and such that conditions (i)-(iii) below hold for every string σ in X satisfying len(σ) <
ϵ5(α, Φ). Let us write
α′ := Lie(Φ)(α)∈ Ω1
pws(X)⊗ gln(R),
and
g′ := MI(α′| σ) = Φ
(
MI(α| σ)
)
∈ GLm(R).
Let 1 be the identity operator on Rm, and let‖−‖ denote the operator norm on Rm. The
conditions are:
(i)
‖g′− 1‖≤ c5(α, Φ)· len(σ) .
(ii) ‖‖ g′−
(
1 +
∫
σ
α′)‖‖≤ c5(α, Φ)· len(σ)2 .
(iii) Assume α′ is smooth. Let x 0 be the initial point of σ, and let α′(x0) be the
constant form deﬁned in Deﬁnition 1.3.5. Then
‖‖ g′−
(
1 +
∫
σ
α′(x0)
)‖‖≤ c5(α, Φ)· len(σ)2 .
Proof. Let us write H := GLm(R) and h := gln(R). Deﬁne ϵ5(α, Φ) := ϵ1(α′), in
the sense of Deﬁnition 3.3.16, and let d := c1(α′)· ϵ1(α′).
By reasons of convergence of analytic functions on compact domains, there is
a constant c such that for every matrix λ∈ h with‖λ‖≤ d the inequalities
(3.5.14)
‖‖ expH(λ)− 1
‖‖≤ c·‖ λ‖
and
(3.5.15)
‖‖ expH(λ)− (1 + λ)
‖‖≤ c·‖ λ‖2
NONABELIAN MULTIPLICATIVE INTEGRATION 47
hold.
Take a string σ with ϵ := len(σ) < ϵ5(α, Φ). By Proposition 3.5.8(3) we have
g′∈ V0(H) and
‖λ‖≤ c1(α′)· ϵ≤ d ,
for the elements g′ := MI(α′| σ) and λ := logH(g′)∈ h. Inequality (3.5.14) gives
(3.5.16) ‖g′− 1‖≤ c· c1(α′)· ϵ .
Next, using Proposition 3.5.11 and inequality (3.5.15) we have
(3.5.17)
‖‖ g′−
(
1 +
∫
σ
α′)‖‖≤
‖‖ g′− (1 + λ)
‖‖ +‖λ−
∫
σ
α′‖
≤ c· c1(α′)2· ϵ2 + c1(α′)2· ϵ2 .
Finally, assume that α′ is smooth. By Taylor expansion of the coefﬁcients of α′
(cf. (3.3.7)) we have the estimate
‖‖ α′(x)− α′(x0)
‖‖≤‖ α′‖Sob· ϵ
for every point x in the image of the string σ. Therefore
(3.5.18)
‖‖
∫
σ
α′−
∫
σ
α′(x0)
‖‖≤‖ α′‖Sob· ϵ2 .
From the inequalities (3.5.16), (3.5.17) and (3.5.18) we can now easily extract a
constant c5(α, Φ) for which all three conditions hold. □
NONABELIAN MULTIPLICATIVE INTEGRATION 49
4. M ultiplicative Integration in Dimension Two
We pass up to dimension 2. Here it turns out that things are really much more
complicated, for geometrical reasons.
A rudimentary multiplicative integration on surfaces was already introduced
by Schlesinger in 1928, in his nonabelian 2-dimensional Stokes Theorem (see [DF,
Appendix A.II,9]). However we need stronger results, for which a more compli-
cated multiplicative integration procedure is required.
It turns out (this was already in Schlesinger’s work) that the correct multi-
plicative integral is twisted: there is a 2-form, say β, that is integrated, but this
integration is twisted by a 1-form α. The geometric cycles on which integration is
performed are the kites, to be deﬁned now.
4.1. Kites. By a pointed polyhedron (X, x0) we mean a polyhedron X (see Section
1), together with a base point x0∈ X. As base point for I2 we always take the
vertex v0; cf. (1.2.1).
Deﬁnition 4.1.1. Let (X, x0) be a pointed polyhedron.
(1) A quadrangular kite in (X, x0) is a pair (σ, τ), where σ is a string in X (see
Deﬁnition 3.5.1), and τ : I2→ X is a linear map. The conditions are that
σ(v0) = x0 and σ(v1) = τ(v0).
(2) If τ(I2) is 2-dimensional then we call (σ, τ) a nondegenerate kite.
(3) If τ(I2) is a square in X (of positive size), then we call (σ, τ) a square kite.
See Figure 8 for illustration.
Until Section 9, where triangular kites are introduced, we shall only encounter
quadrangular kites. Hence is Sections 4-8 a kite shall always mean a quadrangu-
lar kite.
Consider a kite (σ, τ). The image τ(I2) is a parallelogram in X. We denote
the area of τ(I2) by area(τ). If τ(I2) is a square, then we denote the side of this
square by side(τ).
We view (I2, v0) as an oriented pointed polyhedron. Suppose (σ, τ) is a non-
degenerate kite in (I2, v0). If the orientation of τ is positive, then we say that the
kite (σ, τ) is positively oriented.
We shall need the following composition operation on kites. Suppose (σ1, τ1)
is a kite in (X, x0), and (σ2, τ2) is a kite in (I2, v0). Then τ1◦ τ2 : I2→ X is a linear
map, and σ1∗ (τ1◦ σ2) is a string in X. (See (3.5.2) for the concatenation operation
∗.) We deﬁne
(4.1.2) (σ1, τ1)◦ (σ2, τ2) :=
(
σ1∗ (τ1◦ σ2), τ1◦ τ2
)
,
which is also a kite in (X, x0). Note that this composition operation is associative.
For an illustration see Figures 8 and 9.
Let (σ, τ) be a kite in (X, x0), and let f : (X, x0)→ (Y, y0) be a piecewise
linear map between pointed polyhedra. Assume that the restriction of f to the
subpolyhedron τ(I2)⊂ X is linear. As in formula (3.5.5) we have a string f◦ σ in
Y. We deﬁne
(4.1.3) f◦ (σ, τ) := ( f◦ σ, f◦ τ),
which is a kite in (Y, y0).
Given a kite (σ, τ) in (X, x0), its boundary is the closed string ∂(σ, τ) deﬁned as
follows. First we deﬁne
(4.1.4) ∂I2 := (v0, v1)∗ (v1, (1, 1))∗ ((1, 1), v2)∗ (v2, v0) .
50 AMNON YEKUTIELI
Figure 8. A linear quadrangular kite (σ, τ) in the pointed poly-
hedron (X, x0), and a linear quadrangular kite (σ′, τ′) in the
pointed polyhedron (I2, v0).
Figure 9. Continued from Figure 8: the linear quadrangular kite
(σ, τ)◦ (σ′, τ′) in the pointed polyhedron (X, x0).
Figure 10. The boundary ∂(σ, τ) = σ∗ ∂τ∗ σ−1 of the kite (σ, τ)
from Figure 8.
This is a closed string in I2, based at v0. Next we let ∂τ := τ◦ (∂I2), where
composition is in the sense of (3.5.5). So ∂τ is a closed string in X. Finally we
deﬁne
(4.1.5) ∂(σ, τ) := σ∗ (∂τ)∗ σ−1,
where σ−1 is the inverse string from (3.5.4). See Figure 10.
NONABELIAN MULTIPLICATIVE INTEGRATION 51
Figure 11. The map f|Y∪Z : Y∪ Z→ X, where Z = Z1∪ Z2∪ Z3.
Here is a useful fact about the geometry of kites.
Proposition 4.1.6. Let (σ, τ) be a kite in (X, x0). Then there is a square kite (σ′, τ′)
in (I2, v0), and a piecewise linear map of pointed polyhedra f : (I2, v0)→ (X, x0), such
that len(σ′)≤ 1, f is linear on τ′(I2), and
(σ, τ) = f◦ (σ′, τ′)
as kites in (X, x0).
Proof. Say σ = ( σ1, . . . ,σm) is the decomposition of σ into pieces. If m = 0 (i.e. σ is
the empty string), then we let σ′ also be the empty string, and we take τ′ := idI2
and f := τ.
Otherwise, if m > 0, then we deﬁne the square kite (σ′, τ′) in (I2, v0) as follows.
The square map τ′ : I2→ I2 is deﬁned on vertices by the formula
τ′(v0, v1, v2) :=
(
( 1
2, 1
2 ), (1, 1
2 ), ( 1
2, 1)
)
.
And we let Y := τ′(I2).
Next consider the oriented line segment Z going from v0 to ( 1
2, 1
2 ). We divide
Z into m equal pieces, labeled Z1, . . . ,Zm. We let σ′
i : I1→ Z be the positively
oriented linear map with image Zi. And we let σ′ be the string σ′ := ( σ′
1, . . . ,σ′
m).
The map f|Y is deﬁned to be the unique linear map Y→ X such that f◦ τ′ = τ.
And for every i the map f|Zi deﬁned to be the unique piecewise linear map
Zi→ X such that f◦ σ′
i = σi. We thus have a map f|Y∪Z : Y∪ Z→ X; see Figure
11 for an illustration.
Finally let g : I2→ Y∪ Z be any piecewise linear retraction; for instance as
suggested by Figure 12. We deﬁne f := f|Y∪Z◦ g : I2→ X. See Figure 13. □
52 AMNON YEKUTIELI
Figure 12. A piecewise linear retraction g : I2→ Y∪ Z.
Figure 13. The piecewise linear map f := f|Y∪Z◦ g, and the kite
(σ′, τ′) such that f◦ (σ′, τ′) = ( σ, τ).
Figure 14. The 1-st binary subdivision sd 1 I2 of I2. Here w := ( 1
2, 1
2 ).
4.2. Binary Tessellations of I 2. For k≥ 0 the k-th binary subdivision of I2 is the
cellular subdivision sd k I2 of I2 into 4k squares, each of side ( 1
2 )k. The 1-skeleton
of sd k I2 is the set sk 1 sdk I2 consisting of the union of all edges (i.e. 1-cells) in
sdk I2. Thus sk 1 sdk I2 is a grid. See Figure 14.
Deﬁnition 4.2.1. Let k be a natural number.
(1) Let p = 0, 1, 2. A linear map σ : Ip→ I2 is said to be patterned on sdk I2 if
the image σ(Ip) is a p-cell of sdk I2.
(2) A string σ = ( σ1, . . . ,σm) in I2 is said to be patterned on sd k I2 if each
piece σi : I1→ I2 is a linear map patterned on sd k I2.
(3) A square kite (σ, τ) in (I2, v0) is said to be patterned on sd k I2 if both the
linear map τ and the string σ are patterned on sd k I2.
NONABELIAN MULTIPLICATIVE INTEGRATION 53
Figure 15. The probe σpr in I2. Here w := ( 1
2, 1
2 ).
The fundamental group of the topological space sk 1 sdk I2, based at v0, is de-
noted by π1(sk1 sdk I2). It is a free group on 4 k generators. Given a closed string
σ patterned on sd k I2 and based at v0, we denote by [σ] the corresponding ele-
ment of π1(sk1 sdk I2). In particular, if (σ, τ) is a kite patterned on sd k I2, then
the boundary ∂(σ, τ) represents an element
[∂(σ, τ)]∈ π1(sk1 sdk I2).
Recall the boundary ∂I2 from equation (4.1.4).
Deﬁnition 4.2.2. Let k be a natural number. A tessellation of I2 patterned on sdk I2
is a sequence
ρ =
(
(σ1, τ1), . . . ,(σ4k, τ4k )
)
of kites in (I2, v0), satisfying these two conditions:
(i) Each kite (σi, τi) is patterned on sd k I2.
(ii) One has
4k
∏
i=1
[∂(σi, τi)] = [ ∂I2]
in the group π1(sk1 sdk I2). The product is according to the convention
(2.1.1).
Remark 4.2.3. Suppose ρ is a tessellation of I2 patterned on sd k I2. Then, in the
notation of the deﬁnition, each kite (σi, τi) is positively oriented, and each 2-cell
of sdk I2 occurs as τi(I2) for exactly one index i.
This assertion (that we will not use in the paper) can be proved directly, by
a topological argument. But it also follows from Corollary 7.5.2, by taking the
abelian Lie groups G := 1 and H := GL1(R), and the differential forms α := 0
and β := f· dt1∧ dt1, where f : I2→ R is a smooth nonnegative bump function
supported in the interior of a given 2-cell of sd k I2.
The probe is the string
(4.2.4) σpr :=
(
v0, (0, 1
2 )
)
∗
(
(0, 1
2 ), ( 1
2, 1
2 )
)
(with two pieces) in I2. See Figure 15 for an illustration and Remark 4.3.4 for an
explanation.
Deﬁnition 4.2.5. Let k be a natural number. The k-th binary tessellation of I2 is the
sequence
tesk I2 =
(
tesk
1 I2, . . . , tesk
4k I2)
=
(
(σk
1, τk
1 ), . . . ,(σk
4k, τk
4k )
)
of kites in (I2, v0), patterned on sd k I2, that is deﬁned recursively as follows.
54 AMNON YEKUTIELI
Figure 16. The 1-st binary tessellation tes 1 I2. The arrowheads
indicate the orientation of the linear maps.
Figure 17. The kite (σ2
7 , τ2
7 ) in tes2 I2.
(1) For k = 0 let σ0
1 be the empty string, and let τ0
1 be the identity map of I2.
(2) For k = 1 all four strings σ1
i are the same; they are σ1
i := σpr. The four
linear maps τ1
i : I2→ I2 are patterned on sd 1 I2, positively oriented, and
have τ1
i (v0) = ( 1
2, 1
2 ). It remains to specify the points τ1
i (v1):
τ1
1 (v1) = ( 1
2, 0), τ1
2 (v1) = ( 1, 1
2 ), τ1
3 (v1) = ( 1
2, 1), τ1
4 (v1) = ( 0, 1
2 ).
(3) For k≥ 2 we deﬁne
tesk I2 := (tes1 I2)◦ (tesk−1 I2).
Here composition of sequences of kites is using the operations (4.1.2) and
(3.1.1).
See Figures 16 and 17 for an illustration.
It is clear that sequence tes k I2 is a tessellation of I2 patterned on sd k I2, in the
sense of Deﬁnition 4.2.2. We call (σ0
1 , τ0
1 ) the basic kite.
NONABELIAN MULTIPLICATIVE INTEGRATION 55
Hopefully there will be no confusion between the linear map σk
i belonging
tesk I1, and the string σk
i belonging tesk I2; these are distinct objects that share the
same notation.
An easy calculation shows that
(4.2.6) len (σk
i )≤ 2
for all k and i.
Deﬁnition 4.2.7. Let (σ, τ) be a kite in (X, x0). For k∈ N and i∈{ 1, . . . , 4k} let
tesk
i (σ, τ) := ( σ, τ)◦ tesk
i I2 = ( σ, τ)◦ (σk
i , τk
i ),
which is also a kite in (X, x0). The sequence of kites
tesk(σ, τ) :=
(
tesk
1(σ, τ), . . . , tesk
4k (σ, τ)
)
is called the k-th binary tessellation of (σ, τ).
Remark 4.2.8. The choice of strings for the kites in the binary tessellations (and
the ordering of the kites) is clearly artiﬁcial, and also very asymmetrical. As
we shall see later, in favorable situations this will not matter at all – any other
tessellation works! See Corollary 7.5.2.
4.3. Additive Twisting and Riemann Products. Let h be a ﬁnite dimensional
vector space (over R). We denote by GL(h) the group of linear automorphisms of
h, which is a Lie group (noncanonically isomorphic to GL d(R) for d := dim h).
Deﬁnition 4.3.1. A twisting setup is the data C = ( G, H, Ψh), consisting of:
(1) Lie groups G and H, with Lie algebras g and h respectively.
(2) A map of Lie groups Ψh : G→ GL(h), called an additive twisting.
Warning: we do not assume that the map Ψh(g) : h→ h, for g∈ G, is an
automorphism of Lie algebras!
Example 4.3.2. Let G be any Lie group. Take H := G and Ψh := Adh, the adjoint
action of H = G on its Lie algebra. Then (G, H, Ψh) is a twisting setup. Here
Ψh(g) is in fact an automorphism of Lie groups.
Let us ﬁx, for the rest of this section, a twisting setup C = ( G, H, Ψh). The Lie
algebras of G and H are g and h respectively.
We choose some euclidean norm ‖−‖g on the vector space g. As in Section
2 we also choose an open neighborhood V0(G) of 1 in G on which log G is well-
deﬁned, a convergence radius ϵ0(G), and a commutativity constant c0(G). Like-
wise we choose‖−‖h, V0(H), ϵ0(H) and c0(H). Given g∈ G, the linear operator
Ψh(g)∈ End(h) is given the operator norm ‖Ψh(g)‖. It should be noted that
these choices are auxiliary only, and do not effect the deﬁnition of the multiplica-
tive integration.
Piecewise smooth differential forms were discussed in Subsection 1.6. The
string σpr (the probe) was introduced in (4.2.4).
Deﬁnition 4.3.3 (Basic Riemann Product) . Let (X, x0) be a pointed polyhedron,
let
α∈ Ω1
pws(X)⊗ g,
let
β∈ Ω2
pws(X)⊗ h,
56 AMNON YEKUTIELI
Figure 18. Calculating RP 0(α, β| σ, τ) in the smooth case. Here
Z = τ(I2), z = τ( 1
2, 1
2 ), and Y is a triangle in Z such that β|Y is
smooth.
and let (σ, τ) be a kite in (X, x0). We deﬁne an element
RP0(α, β| σ, τ)∈ H,
called the basic Riemann product of (α, β) on (σ, τ), as follows. Write Z := τ(I2)
and z := τ( 1
2, 1
2 )∈ Z. There are two cases to consider:
(1) Assume dim Z = 2 and z is a smooth point of the form β|Z. Put on Z
the orientation compatible with τ. Choose a triangle Y in Z such that
z∈ Int Y and β|Y is smooth, and let ˜β∈O (Y)⊗ h be the coefﬁcient of β|Y
with respect to the orientation form of Y (see Deﬁnition 1.8.2). Also let
g := MI(α| σ∗ (τ◦ σpr))∈ G.
We deﬁne
RP0(α, β| σ, τ) := expH
(
area(Z)· Ψh(g)( ˜β(z))
)
.
(2) If dim Z < 2, or dim Z = 2 and z is a singular point of β|Z, we deﬁne
RP0(α, β| σ, τ) := 1.
It is obvious that case (1) of the deﬁnition is independent of the triangle Y. See
Figure 18 for an illustration.
Remark 4.3.4. We call the stringσpr “the probe” because it reaches into the middle
of the square I2. The “reading” it gives, namely the formula for RP 0(α, β| σ, τ) in
part (1) of the deﬁnition above, is better than (0.8.1), because it converges to the
limit faster: order of side (τ)4 versus side(τ)3. Cf. Lemma 4.4.4 below.
Suppose we are given a ﬁnite sequence of kites
ρ =
(
(σ1, τ1), . . . ,(σm, τm)
)
in (X, x0). We write
(4.3.5) RP 0(α, β| ρ) :=
m
∏
i=1
RP0
(
α, β| σi, τi
)
.
Recall the binary tessellation tes k(σ, τ) from Deﬁnition 4.2.7.
NONABELIAN MULTIPLICATIVE INTEGRATION 57
Deﬁnition 4.3.6 (Reﬁned Riemann Product). Let (X, x0) be a pointed polyhedron,
let α∈ Ω1
pws(X)⊗ g, let β∈ Ω2
pws(X)⊗ h, and let (σ, τ) be a kite in (X, x0). For
k≥ 0 we deﬁne
RPk(α, β| σ, τ) := RP0
(
α, β| tesk(σ, τ)
)
=
4k
∏
i=1
RP0
(
α, β| (σ, τ)◦ (σk
i , τk
i )
)
.
Lemma 4.3.7. Let f : (X′, x′
0)→ (X, x0) be a piecewise linear map of pointed polyhedra,
and let (σ′, τ′) be a kite in (X′, x′
0). Assume that f is linear on τ′(I2), and let
(σ, τ) := f◦ (σ′, τ′),
which is a kite in (X, x0). Let α′ := f∗(α) and β′ := f∗(β). Then
RPk(α, β| σ, τ) = RPk(α′, β′| σ′, τ′)
for any k≥ 0.
Proof. Take k≥ 0 and i∈{ 1, . . . , 4k}. We will prove that
(4.3.8) RP 0(α, β| (σ, τ)◦ (σk
i , τk
i )) = RP0(α′, β′| (σ′, τ′)◦ (σk
i , τk
i )).
Let Z := τ(I2)⊂ X and Z′ := τ′(I2)⊂ X′. If dim Z < 2 then β|Z = 0 and
β′|Z′ = 0, and hence both sides of (4.3.8) equal 1.
If dim Z = 2 then the linear map f|Z′ : Z′→ Z is bijective. Let w := ( 1
2, 1
2 )∈ I2,
zi := ( τ◦ τk
i )(w)∈ Z and z′
i := ( τ′◦ τk
i )(w)∈ Z′. Then zi is a smooth point of
β|Z if and only if z′
i is a smooth point of β′|Z′. In the singular case again both
sides of (4.3.8) equal 1.
In the smooth case we know (by Proposition 3.5.9) that
MI(α| σ∗ (τ◦ σk
i )∗ (τ◦ τk
i◦ σpr)) = MI(α′| σ′∗ (τ′◦ σk
i )∗ (τ′◦ τk
i◦ σpr)).
This says the twistings are the same. Let ˜βi be the coefﬁcient of β near zi, as in
case (1) of Deﬁnition 4.3.3; and let ˜β′
i be the coefﬁcient of β′ near z′
i. Then
area(Zi)· ˜βi(zi) = area(Z′
i )· ˜β′
i(z′
i).
So in this case we also get equality in (4.3.8). □
4.4. Convergence of Riemann Products. We continue with the setup of Subsec-
tion 4.3. Fix differential forms α∈ Ω1
pws(X)⊗ g and β∈ Ω2
pws(X)⊗ h.
Lemma 4.4.1. There are constants c1(α, β) and ϵ1(α, β) with the following properties.
(i) The inequalities below hold:
1≤ c1(α, β)
0 < ϵ1(α, β)≤ 1
ϵ1(α, β)· c1(α, β)≤ 1
4 ϵ0(H) .
(ii) Suppose (σ, τ) is a square kite in (X, x0) such that side(τ) < ϵ1(α, β) and
len(σ)≤ 4· diam(X). Then for any k≥ 0 one has
RPk(α, β| σ, τ)∈ V0(H)
and ‖‖ logH
(
RPk(α, β| σ, τ)
)‖‖≤ c1(α, β)· side(τ)2 .
58 AMNON YEKUTIELI
Figure 19. The kite (σ, τ) in (X, x0) and the points z1, . . . ,z4k in
τ(I2). Here k = 1.
Figure 20. The kite (σ2, τ2) in (X, x0).
Proof. Let w := ( 1
2, 1
2 )∈ I2. Given a square kite (σ, τ), let Z := τ(I2), z := τ(w)
and ϵ := side(τ).
For i∈{ 1, . . . , 4k} deﬁne
(4.4.2) (σi, τi) := ( σ, τ)◦ (σk
i , τk
i ).
This is a square kite in (X, x0) satisfying side(τi) = ( 1
2 )kϵ and area(τi) = ( 1
4 )kϵ2.
Let Zi := τi(I2) and zi := τi(w). see Figures 19 and 20 for illustration. Since
len(σk
i )≤ 2 and ϵ≤ diam(X), we have
(4.4.3) len (σi∗ (τi◦ σpr)) = len(σ) + ϵ· len(σk
i ) + ( 1
2 )kϵ≤ 7· diam(X).
Consider the group elements
gi := MI(α| σi∗ (τi◦ σpr))∈ G
and
hi := RP0(α, β| σi, τi)∈ H.
By deﬁnition of the Riemann product we have
RPk(α, β| σ, τ) =
4k
∏
i=1
hi.
Take i∈{ 1, . . . , 4k}. If zi is a smooth point of β|Z (this is the good case), then
let ˜βi be the coefﬁcient of β|Z near zi, and let
λi := ( 1
4 )k· ϵ2· Ψh(gi)( ˜βi(zi))∈ h.
NONABELIAN MULTIPLICATIVE INTEGRATION 59
Otherwise, if zi is a singular point of β|Z (this is the bad case), then we let λi := 0.
In any case, by deﬁnition we have hi = expH(λi).
According to Proposition 3.4.3 and the inequality (4.4.3) we have
‖Ψh(gi)‖≤ exp
(
c4(α, Ψh)· 7· diam(X)
)
for some constant c4(α, Ψh). Note that this bound is independent of k and (σ, τ).
Let
c := exp
(
c4(α, Ψh)· 7· diam(X)
)
·‖ β‖Sob + 1,
ϵ1(α, β) := ϵ0(H)
1
2· c− 1
2
and
c1(α, β) := c·
(
c0(H) + 1
)
.
Now assume our kite satisﬁes ϵ < ϵ1(α, β). Because ‖ ˜βi(zi)‖≤‖ β‖Sob in the
good case, and λi = 0 in the bad case, we see that
‖λi‖≤ ( 1
4 )k· ϵ2· c < ( 1
4 )k· ϵ0(H).
Hence ∑4k
i=1‖λi‖ < ϵ0(H), and by property (ii) of Theorem 2.1.2 we can deduce
that
∏
4k
i=1 hi∈ V0(H)
and
‖‖ logH
(
∏
4k
i=1 hi
)‖‖≤ c0(H)·
(
∑
4k
i=1‖λi‖
)
≤ c0(H)· ϵ2· c≤ c1(α, β)· ϵ2 .
□
Lemma 4.4.4. There are constant ϵ2(α, β) and c2(α, β) with the following properties:
(i) c2(α, β)≥ c1(α, β) and 0 < ϵ2(α, β)≤ ϵ1(α, β).
(ii) Suppose (σ, τ) is a square kite in (X, x0) such that β|τ(I2) is smooth, side(τ) <
ϵ2(α, β) and len(σ)≤ 4· diam(X). Then
‖‖ logH
(
RPk(α, β| σ, τ)
)
− logH
(
RP0(α, β| σ, τ)
)‖‖≤ c2(α, β)· side(τ)4
for every k≥ 0.
The exponent 4 in “side (τ)4” in the inequality above will be of utmost impor-
tance later on. On the other hand, the factor 4 appearing in “4· diam(X)” is quite
arbitrary (any number bigger than 2 would probably do just as well).
Proof. Let w := ( 1
2, 1
2 )∈ I2. Suppose (σ, τ) is some square kite in (X, x0). Write
Z := τ(I2), z0 := τ(w)∈ Z and ϵ := side(Z). Assume that ϵ > 0 and β|Z is
smooth (otherwise there is nothing to prove). Put on Z the orientation compatible
with τ.
Let ˜β∈O (Z)⊗ h be the coefﬁcient of β|Z, as in Deﬁnition 1.8.2. Let
g0 := MI(α| σ∗ (τ◦ σpr))∈ G,
and
λ0 := ϵ2· Ψh(g0)( ˜β(z0))∈ h.
So by deﬁnition
expH(λ0) = RP0(α, β| σ, τ).
Suppose π is some string in Z, with initial point z0. Let z be the terminal point
of π. See Figure 21.
60 AMNON YEKUTIELI
Figure 21. A string π in Z = τ(I2), with initial point z0 and
terminal point z.
We shall need the following variant of the Taylor expansion of ˜β(z) to second
order around z0:
˜β(z) = ˜β(z0) +
∫
π
(d ˜β)(z0) + R2( ˜β, π).
Here d ˜β∈ Ω1(Z)⊗ h, and (d ˜β)(z0)∈ Ω1
const(Z)⊗ h is the associated constant
form (see Deﬁnition 1.3.5). Thus
∫
π(d ˜β)(z0) is the linear term in the expansion
– it depends linearly on π. And the quadratic remainder term R 2( ˜β, π)∈ h has
this bound:
‖R2( ˜β, π)‖≤‖ β‖Sob· len(π)2 .
Therefore we get the estimate
(4.4.5)
‖‖ ˜β(z)−
( ˜β(z0) +
∫
π
(d ˜β)(z0)
)‖‖≤‖ β‖Sob· len(π)2 .
Next let
g := MI(α| π)∈ G
and
α′ := Lie(Ψh)(α)∈ Ω1
pws(X)⊗ End(h).
Assume that len (π) < ϵ5(α, Ψh). According to Proposition 3.5.13 we have this
estimate for the operator Ψh(g)∈ End(h):
(4.4.6)
‖‖ Ψh(g)−
(
1 +
∫
π
α′(z0)
)‖‖≤ c5(α, Ψh)· len(π)2 .
And by Proposition 3.5.10 we have the bound
(4.4.7)
‖‖ Ψh(g)
‖‖≤ exp(c4(α, Ψh)· ϵ5(α, Ψh)) .
By combining inequalities (4.4.5), (4.4.6) and (4.4.7), we see that there exists a
constant c(α, β) such that
(4.4.8)
‖‖ Ψh(g)( ˜β(z))−
(
˜β(z0) +
(∫
π
α′(z0)
)
( ˜β(z0)) +
∫
π
(d ˜β)(z0)
)‖‖
≤ c(α, β)· len(π)2 .
This holds for every string π in Z with len (π) < ϵ5(α, Ψh), π(v0) = z0 and
π(v1) = z.
Now take k≥ 0. For any index i∈{ 1, . . . , 4k} let πi be the unique string in Z
such that
(τ◦ σpr)∗ πi = ( τ◦ σk
i )∗ (τ◦ τk
i◦ σpr)
as strings. This is a string with initial point z0, and with terminal point
zi := ( τ◦ τk
i )(w).
Notice that for i≤ 2k the strings πi and π2k+i are reﬂections of each other relative
to the point z0. See Figure 22.
NONABELIAN MULTIPLICATIVE INTEGRATION 61
Figure 22. The strings π1 and π3 in Z. Here k = 1.
Deﬁne
gi := MI(α| πi)∈ G
and
λi := ( 1
4 )k· ϵ2· Ψh(g0· gi)( ˜β(zi))∈ h.
So we have
expH(λi) = RP0(α, β| (σ, τ)◦ (σk
i , τk
i )).
And the bound for λi is
(4.4.9) ‖λi‖≤ ( 1
4 )k· ϵ2· c′(α, β) ,
where we write
c′(α, β) := exp(c4(α, Ψh)· 7· diam(X))·‖ β‖Sob + 1 .
Using the abbreviation
γ := ϵ2· Ψh(g0)(d ˜β)∈ Ω1
pws(Z)⊗ h,
formula (4.4.8), and the inequality len (πi)≤ ϵ, we obtain
(4.4.10)
‖‖ λi− ( 1
4 )k·
(
λ0 +
(∫
πi
α′(z0)
)
(λ0) +
∫
πi
γ(z0)
)‖‖
≤ c(α, β)· ( 1
4 )k· ϵ4 .
For this to be true we should assume that ϵ < ϵ5(α, Ψh).
Let us set
ϵ2(α, β) := min
(
ϵ1(α, β), c′(α, β)−1/2· ϵ0(H)1/2, ϵ5(α, Ψh)
)
,
We now assume furthermore that ϵ < ϵ2(α, β). In particular, from (4.4.9) we
obtain
4k
∑
i=1
‖λi‖≤ ϵ0(H) .
We know that
4k
∏
i=1
expH(λ0) = RPk(α, β| σ, τ).
Therefore we can use property (ii) of Theorem 2.1.2 to deduce that
‖‖ logH
(
RPk(α, β| σ, τ)
)
−
4k
∑
i=1
λi
‖‖≤ c0(H)· ϵ4· c′(α, β)2 .
The geometric symmetry of the sequence of strings π1. . . . ,π4k implies that
(∫
πi
α′(z0)
)
(λ0) =−
(∫
π2k +i
α′(z0)
)
(λ0)
62 AMNON YEKUTIELI
for i≤ 2k; and therefore
4k
∑
i=1
(∫
πi
α′(z0)
)
(λ0) = 0.
Similarly
4k
∑
i=1
∫
πi
γ(z0) = 0.
Plugging in the estimate (4.4.10) we obtain
‖‖
4k
∑
i=1
λi− λ0
‖‖≤ c(α, β)· ϵ4 .
We see that the constant
c2(α, β) := c(α, β) + c0(H)· c′(α, β)2 + c1(α, β) .
works. □
Deﬁnition 4.4.11. Let us ﬁx constants ϵ2(α, β) and c2(α, β) as in Lemma 4.4.4. A
square kite (σ, τ) in (X, x0) will be called (α, β)-tiny in this section if
side(τ) < ϵ2(α, β)
and
len(σ)≤ 4· diam(X) .
Deﬁnition 4.4.12. Let (σ, τ) be a nondegenerate kite in (X, x0). For k∈ N and
i∈{ 1, . . . , 4k} let Zi := ( τ◦ τk
i )(I2)⊂ X. An index i is called good if the forms
α|Zi and β|Zi are smooth. Otherwise i is called bad. The sets of good and bad
indices are denoted by good (τ, k) and bad(τ, k) respectively.
Lemma 4.4.13. Let Z be a 2-dimensional subpolyhedron of X. There exist constants
a0(α, β, Z) and a 1(α, β, Z) such that for any nondegenerate kite (σ, τ) in (X, x0) with
τ(I2)⊂ Z, one has
|bad(τ, k)|≤ a0(α, β, Z) + a1(α, β, Z)· 2k .
Proof. Let Z1, . . . ,Zm be line segments in Z such that the singular locus of α and
the singular locus of β are contained in ⋃m
j=1 Zj. Take a0(α, β, Z) := 2m and
a1(α, β, Z) := 2· ∑m
j=1 len(Zj). □
Lemma 4.4.14. Let Z be a 2-dimensional subpolyhedron of X. Then there is a constant
c3(α, β, Z)≥ 0, such that for any (α, β)-tiny kite (σ, τ) satisfying τ(I2)⊂ Z, and any
k′≥ k≥ 0, one has‖‖ logH
(
RPk′ (α, β| σ, τ)
)
− logH
(
RPk(α, β| σ, τ)
)‖‖
≤ ( 1
4 )k· c3(α, β, Z)· side(τ)2 .
Proof. Let (σ, τ) an (α, β)-tiny kite such that τ(I2)⊂ Z. Write ϵ := side(τ). For
i∈{ 1, . . . , 4k} let (σi, τi) be as in equation (4.4.2), and let Zi := τi(I2)⊂ Z. Note
that side(Zi) = ( 1
2 )k· ϵ.
Let l := k′− k. If i∈ good(τ, k), then by Lemma 4.4.4 we know that
‖‖ logH
(
RPl(α, β| σi, τi)
)
− logH
(
RP0(α, β| σi, τi)
)‖‖≤ c2(α, β)· (( 1
2 )k· ϵ)4 .
If i∈ bad(τ, k), then by Lemma 4.4.1 we know that
‖‖ logH
(
RPl(α, β| σi, τi)
)
− logH
(
RP0(α, β| σi, τi)
)‖‖≤ 2c1(α, β)· (( 1
2 )k· ϵ)2 .
NONABELIAN MULTIPLICATIVE INTEGRATION 63
Therefore by property (iv) of Theorem 2.1.2 and Lemma 4.4.13 we have
‖‖ logH
(
RPk′ (α, β| σ, τ)
)
− logH
(
RPk(α, β| σ, τ)
)‖‖
=
‖‖ logH
(
∏
4k
i=1 RPl(α, β| σi, τi
)
− logH
(
∏
4k
i=1 RP0(α, β| σi, τi
)‖‖
≤ c0(H)·
(
|good(τ, k)|· c2(α, β)· ( 1
2 )4k· ϵ4
+|bad(τ, k)|· 2c1(α, β)· ( 1
2 )2k· ϵ2)
≤ c3(α, β, Z)· ( 1
2 )k· ϵ2
where we take (very generously)
c3(α, β, Z) := c0(H)·
(
c2(α, β) + 2(a0(α, β, Z) + a1(α, β, Z))· c1(α, β)
)
.
□
Theorem 4.4.15. Let (X, x0) be a pointed polyhedron, let α∈ Ω1
pws(X)⊗ g, let β∈
Ω2
pws(X)⊗ h, and let (σ, τ) be a kite in (X, x0). Then the limit
lim
k→∞
RPk(α, β| σ, τ)
exists in H.
Proof. According to Proposition 4.1.6 and Lemma 4.3.7 we can assume that(X, x0) =
(I2, v0) and len(σ)≤ 1.
Take k large enough such that for each i∈{ 1, . . . , 4k} the kite (σi, τi), in the
notation of (4.4.2), is (α, β)-tiny. For any k′≥ 0 we have
RPk+k′ (α, β| σ, τ) =
4k
∏
i=1
RPk′ (α, β| σi, τi).
Thus it sufﬁces to prove that for any i the limit
lim
k′→∞
RPk′ (α, β| σi, τi)
exists. Now Lemma 4.4.14 says that the sequence
(
RPk′ (α, β| σi, τi)
)
k′≥0
is a Cauchy sequence in H; and therefore it converges. □
Deﬁnition 4.4.16 (Multiplicative Integral). Let (G, H, Ψh) be a twisting setup, let
(X, x0) be a pointed polyhedron, let α∈ Ω1
pws(X)⊗ g, let β∈ Ω2
pws(X)⊗ h, and
let (σ, τ) be a kite in (X, x0). We deﬁne the multiplicative integral of β twisted by α
on (σ, τ) to be
MI(α, β| σ, τ) := lim
k→∞
RPk(α, β| σ, τ)∈ H.
If (X, x0) = ( I2, v0) then we write
MI(α, β| I2) := MI(α, β| σ0
1 , τ0
1 ),
where (σ0
1 , τ0
1 ) is the basic kite.
64 AMNON YEKUTIELI
4.5. Some Properties of MI. We continue with the setup of the previous subsec-
tions.
Proposition 4.5.1. In the situation of Deﬁnition 4.4.16, for any k≥ 0 one has
MI(α, β| σ, τ) =
4k
∏
i=1
MI
(
α, β| (σ, τ)◦ (σk
i , τk
i )
)
.
Proof. For any k′≥ 0 we have
RPk+k′ (α, β| σ, τ) =
4k
∏
i=1
RPk′
(
α, β| (σ, τ)◦ (σk
i , τk
i )
)
.
Now take the limit lim k′→∞. □
Proposition 4.5.2. Consider the situation of Deﬁnition 4.4.16, and assume that (σ, τ)
is an (α, β)-tiny kite.
(1) One has
MI(α, β| σ, τ)∈ V0(H),
and ‖‖ logH
(
MI(α, β| σ, τ)
)‖‖≤ c1(α, β)· side(τ)2 .
(2) If β|τ(I2) is smooth then
‖‖ logH
(
MI(α, β| σ, τ)
)
− logH
(
RP0(α, β| σ, τ)
)‖‖≤ c2(α, β)· side(τ)4 .
(3) Let Z be a 2-dimensional subpolyhedron of X containing τ(I2). For any k ≥ 0
one has ‖‖ logH
(
MI(α, β| σ, τ)
)
− logH
(
RPk(α, β| σ, τ)
)‖‖
≤ ( 1
2 )k· c3(α, β, Z)· side(τ)2 .
Proof. Immediate from Lemmas 4.4.1, 4.4.4 and 4.4.14. □
Proposition 4.5.3 (Functoriality in X). Let f : (Y, y0)→ (X, x0) be a piecewise linear
map between pointed polyhedra, let α∈ Ω1
pws(X)⊗ g, let β∈ Ω2
pws(X)⊗ h, and let
(σ, τ) be a kite in (Y, y0). Assume that f is linear on τ(I2). Then
MI(α, β| f◦ σ, f◦ τ) = MI
(
f∗(α), f∗(β)| σ, τ
)
.
Proof. Immediate from Lemma 4.3.7. □
The next proposition says that “in the tiny scale the 2-dimensional MI is
abelian”.
Proposition 4.5.4. There are constant ϵ2′ (α, β) and c2′ (α, β) with the following proper-
ties:
(i) c2′ (α, β)≥ c2(α, β) and 0 < ϵ2′ (α, β)≤ ϵ2(α, β).
(ii) Suppose (σ, τ) is a square kite in (X, x0) such that side(τ) < ϵ2′ (α, β) and
len(σ)≤ 4· diam(X). Let g := MI(α| σ)∈ G. Then
‖‖ logH
(
MI(α, β| σ, τ)
)
− Ψh(g)
(∫
τ
β
)‖‖≤ c2′ (α, β)· side(τ)3 .
Actually with more effort we can get a better estimate (order side(τ)4) in prop-
erty (ii) above.
NONABELIAN MULTIPLICATIVE INTEGRATION 65
Proof. This is very similar to Proposition 3.5.11. Take
ϵ2′ (α, β) := min
(
ϵ2(α, β), ϵ5(α, Ψh)
)
,
where ϵ5(α, Ψh) is the constant from Proposition 3.5.13. Let’s write ϵ := side(τ)
and Z := τ(I2). Assume that ϵ < ϵ2′ (α, β).
Take k≥ 0. For i∈{ 1, . . . , 4k} let
(σi, τi) := ( σ, τ)◦ (σk
i , τk
i ) = tesk
i (σ, τ).
Write Zi := τi(I2) and zi := τi(w), where w := ( 1
2, 1
2 )∈ I2 as usual. The sets
good(τ, k) and bad(τ, k) were deﬁned in Deﬁnition 4.4.12.
Deﬁne
g′
0 := MI(α| τ◦ σpr)∈ G,
g′
i := MI(α| (τ◦ σk
i )∗ (τ◦ τk
i◦ σpr))
and
λi := logH
(
RP0(α, β| σi, τi)
)
∈ h
for i∈{ 1, . . . , 4k}. From Deﬁnition 4.3.3 and Proposition 3.5.10 we know that
(4.5.5) ‖λi‖≤ ( 1
4 )k· ϵ2·‖ Ψh(g· g′
i)‖·‖ β‖Sob≤ ( 1
4 )k· ϵ2· c ,
where we let
c := exp
(
c4(α, φ)· 6 diam(X)
)
·‖β‖Sob .
According to property (ii) of Theorem 2.1.2 we have
(4.5.6)
‖‖ logH
(
RPk(α, β| σ, τ)
)
− ∑
4k
i=1 λi
‖‖
≤ c0(H)·
(
∑
4k
i=1‖λi‖
)2≤ c0(H)· ( 1
4 )2k· ϵ4· c2 .
For i∈ good(τ, k) let ˜βi be the coefﬁcient of β|Zi. Deﬁne
µi :=
{
( 1
4 )k· ϵ2· Ψh(g)
( ˜βi(zi)
)
if i is good ,
0 otherwise
and
RSk(α, β| σ, τ) :=
4k
∑
i=1
µi.
Now let us compare µi to λi. If i is a bad index, then
‖µi− λi‖ =‖λi‖≤ ( 1
4 )k· ϵ2· c
by (4.5.5). On the other hand, if i is a good index then
µi = Ψh(g· g′
0· g′−1
i · g−1)(λi).
By Proposition 3.5.10 the operators Ψh(g) and Ψh(g−1) have known
bounds (since the length of the string σ is bounded by 4· diam(X)). Hence there is
a bound for the conjugation operator Ad (Ψh(g)) on End(h). And by Proposition
3.5.13 there is an estimate for the norm of the operator Ψh(g′
0· g′−1
i )− 1, where 1
denotes the identity operator of h. Since Ad (Ψh(g)) ﬁxes 1, we can conclude that
there is a constant c′ (independent of of (σ, τ) or k) such that
‖‖ Ψh(g· g′
0· g′−1
i · g−1)− 1
‖‖
=
‖‖ Ad(Ψh(g))
(
Ψh(g′
0· g′−1
i )− 1
)‖‖≤ c′· ϵ .
Hence using (4.5.5) we get
‖µi− λi‖≤ c′· c· ( 1
4 )k· ϵ3 .
66 AMNON YEKUTIELI
Summing over all i we see that
‖‖ ∑
4k
i=1 λi− ∑
4k
i=1 µi
‖‖≤
4k
∑
i=1
‖µi− λi‖
≤| good(τ, k)|· c′· c· ( 1
4 )k· ϵ3 +|bad(τ, k)|· ( 1
4 )k· ϵ2· c
≤ 4k· c′· c· ( 1
4 )k· ϵ3 + (a0 + a1· 2k)· ( 1
4 )k· ϵ2· c .
Here a0 := a0(α, β, Z) and a1 := a1(α, β, Z) are the constants from Lemma 4.4.13.
Combining this estimate with (4.5.6) we obtain
(4.5.7)
‖‖ logH
(
RPk(α, β| σ, τ)
)
− RSk(α, β| σ, τ)
‖‖
≤ c0(H)· ( 1
4 )2k· ϵ4· c2 + 4k· c′· c· ( 1
4 )k· ϵ3
+ (a0 + a1· 2k)· ( 1
4 )k· ϵ2· c .
Finally, by properties of the usual Riemann integration we have
lim
k→∞
RSk(α, β| σ, τ) = Ψh(g)
(∫
τ
β
)
.
Hence in the limit k→ ∞ we get
‖‖ logH
(
MI(α, β| σ, τ)
)
− Ψh(g)
(∫
τ
β
)‖‖≤ c′· c· ϵ3 ,
and we can take c2′ (α, β) := c′· c. □
4.6. Transfer of Twisting Setups. Suppose H′ is another Lie group, with Lie
algebra h′. The vector space of R-linear maps h→ h′ is denoted by Hom (h, h′).
Consider theOpws(X)-moduleOpws(X)⊗ Hom(h, h′). An element
φ∈O pws(X)⊗ HomR(h, h′)
is called a piecewise smooth family of linear maps from h to h′. Indeed, we may view
φ as a piecewise smooth map
φ : X→ Hom(h, h′).
For any point x∈ X there is a linear map φ(x) : h→ h′.
Deﬁnition 4.6.1. Suppose C = ( G, H, Ψh) and C′ = ( G′, H′, Ψ′
h′ ) are two twisting
setups. A transfer of twisting setups from C to C′, parametrized by (X, x0), is the
data
ΘX = ( ΘG, ΘH, Θh,X),
consisting of:
(1) Maps of Lie groups ΘG : G→ G′ and ΘH : H→ H′.
(2) An element Θh,X∈O pws(X)⊗ Hom(h, h′).
The following condition is required:
(∗) The equality
Lie(ΘH) = Θh,X(x0)
holds in Hom(h, h′).
We denote this transfer by ΘX : C→ C′.
Note that for x⁄= x0 the linear map φ(x) : h→ h′ might fail to be a Lie algebra
homomorphism.
NONABELIAN MULTIPLICATIVE INTEGRATION 67
Deﬁnition 4.6.2. Let ΘX : C→ C′ be a transfer of twisting setups as in Deﬁnition
4.6.1, and let α∈ Ω1
pws(X)⊗ g. We say that α is a connection compatible with ΘX if
the following condition, called the holonomy condition, holds.
(♦) Let σ be a string in X, with x0 = σ(v0) and x1 := σ(v1). Deﬁne
g := MI(α| σ)∈ G
and g′ := ΘG(g)∈ G′. Then the diagram
h
Θh,X (x0)

h
Θh,X (x1)

Ψh(g)oo
h′ h′
Ψ′
h′ (g′)
oo
is commutative.
Remark 4.6.3. The holonomy condition for α can be stated as a differential equa-
tion. We shall not need this equation in our treatment.
Consider a transfer of twisting setups ΘX as above. The family of linear maps
Θh,X induces, by tensoring, a homomorphism of graded Ωpws(X)-modules
(4.6.4) Θh,X : Ωpws(X)⊗ h→ Ωpws(X)⊗ h′.
Warning: usually Θh,X does not commute with the de Rham operator d.
Proposition 4.6.5 (Functoriality in C). Let ΘX : C→ C′ be a transfer of twisting
setups, let α∈ Ω1
pws(X)⊗ g, and let β∈ Ω2
pws(X)⊗ h. Assume that α is a connection
compatible with ΘX. We write
α′ := Lie(ΘG)(α)∈ Ω1
pws(X)⊗ g′
and
β′ := Θh,X(β)∈ Ω2
pws(X)⊗ h′.
Then for every kite (σ, τ) in (X, x0) one has
ΘH
(
MI(α, β| σ, τ)
)
= MI
(
α′, β′| σ, τ
)
in H′.
Proof. Consider a kite (σ′, τ′) in (I2, v0) and a piecewise linear map f like in
Proposition 4.1.6. By Proposition 4.5.3 we have
MI(α, β| σ, τ) = MI
(
f∗(α), f∗(β)| σ′, τ′)
.
On the other hand
(
ΘG, ΘH, f∗(Θh,X)
)
is a transfer of twisting setups
parametrized by (I2, v0), and by Proposition 4.5.3 we have
MI
(
α′, β′| σ, τ
)
= MI
(
f∗(α′), f∗(β′)| σ′, τ′)
= MI
(
Lie(Θ1)( f∗(α)), f∗(Θh,X)( f∗(β))| σ′, τ′)
.
Therefore we can assume that (X, x0) = ( I2, v0) and len(σ)≤ 1. Using Proposi-
tion 4.5.1 we can further assume that (σ, τ) is (α, β)-tiny and (α′, β′)-tiny.
Fix k≥ 0. For i∈{ 1, . . . , 4k} let
(σi, τi) := ( σ, τ)◦ (σk
i , τk
i ).
Deﬁne
gi := MI(α| σi∗ (τi◦ σpr))∈ G
68 AMNON YEKUTIELI
and
g′
i := MI(α′| σi∗ (τi◦ σpr))∈ G′.
By Proposition 3.5.9 we have g′
i = ΘG(gi). Also deﬁne Zi := τi(I2) and zi :=
τi( 1
2, 1
2 ).
Suppose that i∈ good(τ, k), with notation as in Deﬁnition 4.4.12. Then there
is a function ˜βi∈O (Zi)⊗ h, called the coefﬁcient of β|Zi, satisfying
β|Zi = ˜βi· dt1∧ dt2.
The function
˜β′
i := Θh,X( ˜βi)∈O (Zi)⊗ h′,
is then the coefﬁcient of β′|Zi. Note that
˜β′
i(zi) = Θh,X(zi)
( ˜β(zi)
)
in h′. By condition (∗) of Deﬁnition 4.6.1 and condition ( ♦) of Deﬁnition 4.6.2 we
have
Ψ′
h′ (g′
i)
( ˜β′
i(zi)
)
= Ψ′
h′ (g′
i)
(
Θh,X(zi)
( ˜βi(zi)
))
= Θh,X(x0)
(
Ψh(gi)
( ˜βi(zi)
))
= Lie(ΘH)
(
Ψh(gi)
( ˜βi(zi)
))
.
By deﬁnition we have
RP0(α, β| σi, τi) = expH
(
( 1
4 )k· area(τ)· Ψh(gi)( ˜βi(zi))
)
and
RP0(α′, β′| σi, τi) = expH′
(
( 1
4 )k· area(τ)· Ψh(g′
i)( ˜β′
i(zi))
)
.
Since
expH′◦ Lie(ΘH) = ΘH◦ expH
we conclude that
(4.6.6) RP 0(α′, β′| σi, τi) = ΘH
(
RP0(α, β| σi, τi)
)
.
Like in Lemma 4.4.13 we can ﬁnd a bound for|bad(τ, k)|, and like in the proof
of Lemma 4.4.14 we can estimate
‖‖ logH′
(
ΘH
(
RP0(α, β| σi, τi)
))
− logH′
(
RP0
(
α′, β′| σi, τi)
)‖‖
when i∈ bad(τ, k). From these estimates and from (4.6.6) we conclude that there
is a constant c, independent of k, such that
‖‖ logH′
(
ΘH
(
RPk(α, β| σ, τ)
))
− logH′
(
RPk
(
α′, β′| σ, τ)
)‖‖≤ c· ( 1
2 )k .
In the limit k→ ∞ we see that
ΘH
(
MI(α, β| σ, τ)
)
= MI(α′, β′| σ, τ).
□
NONABELIAN MULTIPLICATIVE INTEGRATION 69
5. Q uasi Crossed Modules and Additive Feedback
The full strength of multiplicative integration requires a more elaborate setup
than the twisting setup of Deﬁnition 4.3.1.
5.1. Quasi Crossed Modules. Let (Y, y0) be a pointed analytic manifold. By
automorphism of pointed analytic manifolds we mean an analytic diffeomorphism
f : Y→ Y such that f (y0) = y0. We denote by Aut (Y, y0) the group of all such
automorphisms.
Let G be a Lie group. An analytic action of G on (Y, y0) by automorphisms
of pointed manifolds is an analytic map Ψ : G× Y→ Y having the following
properties. First, for any g∈ G the map Ψ(g) : Y→ Y, Ψ(g)(y) := Ψ(g, y), is
an automorphism of pointed analytic manifolds. Second, the function Ψ : G→
Aut(Y, y0), g↦→ Ψ(g), is a group homomorphism.
Given an analytic action of G on (Y, y0), and an element g∈ G, the differential
dy0
(
Ψ(g)
)
: Ty0Y→ Ty0Y
is an R-linear automorphism of the tangent space T y0Y. In this way we get a map
of Lie groups G→ GL(Ty0Y), which we call the linear action induced by Ψ.
Let H be a Lie group, with unit element 1. We view it as a pointed analytic
manifold (H, 1).
Deﬁnition 5.1.1. A Lie quasi crossed module is the data
C = ( G, H, Ψ, Φ0)
consisting of:
(1) Lie groups G and H.
(2) An analytic action Ψ of G on H by automorphisms of pointed manifolds,
called the multiplicative twisting.
(3) A map of Lie groups Φ0 : H→ G, called the multiplicative feedback.
The condition is:
(∗) Consider Ψ as a group homomorphism Ψ : G→ Aut(H, 1). Then there is
equality
Ψ◦ Φ0 = AdH
as group homomorphisms H→ Aut(H, 1).
Remark 5.1.2. Let (G, H, Ψ, Φ0) be a Lie quasi crossed module. Suppose G0 is a
closed Lie subgroup of G such that the following hold: Φ0(H)⊂ G0; Ψ(g) is a
group automorphism of H for any g∈ G0; and Φ0 : H→ G0 is G0-equivariant
(relative to Ψ and Ad G0). Then (G0, H, Ψ, Φ0) is called a Lie crossed module . See
[BM, BS]. In this situation condition (∗) is called the Pfeiffer condition in the litera-
ture.
Note that we can always ﬁnd such a subgroup G0: just take G0 to be the closure
of Φ0(H) in G. An easy calculation shows that this subgroup has the required
properties.
Here are three of examples of Lie quasi crossed modules.
Example 5.1.3. Suppose
1→ N→ H
Φ0
−→G→ 1
is a central extension of Lie groups. Since Ad H(h) is trivial for h∈ N, the action
AdH induces an action of G on H, which we denote by Ψ. We get a Lie crossed
module (G, H, Ψ, Φ0).
70 AMNON YEKUTIELI
Example 5.1.4. A very special case of Example 5.1.3 is whenH = G and Φ0 = idG.
Namely
(G, H, Ψ, Φ0) = ( G, G, AdG, idG).
This is the situation dealt with in the classical work of Schlesinger.
Example 5.1.5. Let H be a unipotent Lie group, namely H is nilpotent and simply
connected, and let h := Lie(H). The map exp H : h→ H is then an analytic
diffeomorphism. Take G := GL(h). The canonical action of G on h becomes, via
expH, and action of G on H by automorphisms of pointed manifolds, which we
denote by Ψ. The adjoint action Adh of H on h is a map of Lie groups Φ0 : H→ G.
Then (G, H, Ψ, Φ0) is a Lie quasi crossed module.
Next let G0 ⊂ G be the group of Lie algebra automorphisms of h. Then
(G0, H, Ψ, Φ0) is a Lie crossed module.
5.2. Additive Feedback and Compatible Connections. Let (G, H, Ψ, Φ0) be a Lie
quasi crossed module. We write g := Lie(G) and h := Lie(H). Recall that the
Lie algebra h is the tangent space to H at the element 1. Hence the multiplicative
twisting Ψ induces a linear action
Ψh : G→ GL(h).
We see that from the Lie quasi crossed module (G, H, Ψ, Φ0) we obtain a twisting
setup (G, H, Ψh). As in Section 4, we call Ψh the additive twisting.
Recall that Hom(h, g) is the space of R-linear maps h→ g, and an element
φ∈O pws(X)⊗ HomR(h, g)
is called a piecewise smooth family of linear maps from h to g.
Deﬁnition 5.2.1. Let (G, H, Ψ, Φ0) be a Lie quasi crossed module, and let (X, x0)
be a pointed polyhedron. An additive feedback for (G, H, Ψ, Φ0) over (X, x0) is an
element
ΦX∈O pws(X)⊗ Hom(h, g)
satisfying this condition:
(∗∗) There is equality
Lie(Φ0) = ΦX(x0)
in Hom(h, g).
Deﬁnition 5.2.2. Let (X, x0) be a pointed polyhedron. A Lie quasi crossed module
with additive feedback over (X, x0) is the data
C/X = ( G, H, Ψ, Φ0, ΦX)
consisting of:
• A Lie quasi crossed module C = ( G, H, Ψ, Φ0).
• An additive feedback ΦX for C over (X, x0).
When we talk about a Lie quasi crossed module with additive feedback C/X,
by default we use the notation of Deﬁnitions 5.2.1 and 5.2.2, and we write g :=
Lie(G) and h := Lie(H).
Let C/X be a Lie quasi crossed module with additive feedback over (X, x0).
Given a piecewise linear map f : (Y, y0)→ (X, x0) between pointed polyhedra,
consider
f∗(ΦX)∈O pws(Y)⊗ HomR(h, g).
NONABELIAN MULTIPLICATIVE INTEGRATION 71
Then
(5.2.3) f∗(C/X) := ( G, H, Ψ, Φ0, f∗(ΦX))
is a Lie quasi crossed module with additive feedback over (Y, y0).
Deﬁnition 5.2.4. Let C/X be a Lie quasi crossed module with additive feedback
over (X, x0). A connection compatible with C/X is a differential form
α∈ Ω1
pws(X)⊗ g
satisfying the holonomy condition:
(♦) Let σ be a string in X, with x0 = σ(v0) and x1 := σ(v1). Deﬁne
g := MI(α| σ)∈ G.
Then the diagram
h
ΦX (x0)

h
Ψh(g)oo
ΦX (x1)
g g
Adg(g)oo
is commutative.
It could happen that C/X does not admit any compatible connection.
Example 5.2.5. Suppose (G, H, Ψ, Φ0) is a Lie crossed module (see Remark 5.1.2)
and (X, x0) is a pointed polyhedron. Deﬁne ΦX := Lie(Φ0); this is a G-equi-
variant Lie algebra map h→ g, which we view as a constant element ofOpws(X)⊗
Hom(h, g). In this way we obtain a Lie quasi crossed module with additive feed-
back C/X := ( G, H, Ψ, Φ0, ΦX) over (X, x0). Since ΦX is G-equivariant, it follows
that any α∈ Ω1
pws(X)⊗ g is a connection compatible with C/X.
An example of an additive feedback, and of a compatible connection, is given
in Subsection 5.6.
To a Lie quasi crossed module with additive feedback C/X there are two natu-
rally associated twisting setups, namely (G, H, Ψh) and
(G, G, Adg).
Proposition 5.2.6. Let
C/X = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module with additive feedback over (X, x0). Then:
(1) The data ΘX := (idG, Φ0, ΦX) is a transfer of twisting setups
(G, H, Ψh)→ (G, G, Adg)
parametrized by (X, x0), in the sense of Deﬁnition 4.6.1.
(2) A form α∈ Ω1
pws(X)⊗ g is a connection compatible with C/X if and only if it
is a connection compatible with ΘX, in the sense of Deﬁnition 4.6.2.
Proof. Immediate from the deﬁnitions. □
Proposition 5.2.7. Let C/X be a Lie quasi crossed module with additive feedback over
(X, x0), and let α be a compatible connection for C/X. Suppose f : (Y, y0)→ (X, x0) is
a piecewise linear map between pointed polyhedra. Then f∗(α) is a compatible connection
for f∗(C/X).
72 AMNON YEKUTIELI
Proof. Take a string σ in Y with σ(v0) = y0, and let y1 := σ(v1). Then f◦ σ is a
string in X. According to Proposition 3.5.9 we have
MI(α| f◦ σ) = MI( f∗(α)| σ).
Let’s call this element g. Let x1 := f (y1). Then
ΦX(xi) = f∗(ΦX)(yi)
as homomorphisms h→ g, for i = 0, 1. We see that the holonomy condition is
satisﬁed for f∗(α), relative to f∗(C/X). □
Deﬁnition 5.2.8. Suppose
C/X = ( G, H, Ψ, Φ0, ΦX)
and
C′/X = ( G′, H′, Ψ′, Φ′
0, Φ′
X)
are two Lie quasi crossed modules with additive feedbacks over(X, x0). A transfer
between them is a transfer of twisting setups
ΘX = ( ΘG, ΘH, Θh,X) : (G, H, Ψh)→ (G′, H′, Ψ′
h′ )
parametrized by (X, x0), in the sense of Deﬁnition 4.6.1, satisfying this condition:
Φ′
X◦ Θh,X = Lie(ΘG)◦ ΦX
inOpws(X)⊗ Hom(h, g′).
5.3. Connection-Curvature Pairs.
Deﬁnition 5.3.1. Let C/X = ( G, H, Ψ, Φ0, ΦX) be a Lie quasi crossed module
with additive feedback over a pointed polyhedron (X, x0); see Deﬁnition 5.2.2. A
connection-curvature pair for C/X is a pair (α, β), consisting of Lie algebra valued
differential forms
α∈ Ω1
pws(X)⊗ g
and
β∈ Ω2
pws(X)⊗ h,
satisfying the conditions below.
(i) α is a connection compatible with C/X (Deﬁnition 5.2.4).
(ii) The equation
ΦX(β) = d(α) + 1
2 [α, α]
holds in Ω2
pws(X)⊗ g.
Remark 5.3.2. Condition (ii) above is often referred to as vanishing of the fake
curvature. See [BM, BS].
Proposition 5.3.3. Let C/X be a Lie quasi crossed module with additive feedback over
(X, x0), and let (α, β) be a connection-curvature pair for C/X.
(1) Let f : (Y, y0)→ (X, x0) be a piecewise linear map between pointed polyhedra.
Then
(
f∗(α), f∗(β)
)
is a connection-curvature pair in
f∗(C/X).
NONABELIAN MULTIPLICATIVE INTEGRATION 73
(2) Let C′/X be another Lie quasi crossed module with additive feedback over(X, x0),
and let
ΘX = ( ΘG, ΘH, Θh,X) : C/X→ C′/X
be a morphism of Lie quasi crossed module with additive feedback. Assume that
α is compatible with Θh,X. See Deﬁnitions 5.2.8 and 4.6.2. Then
(
Lie(ΘG)(α), Θh,X(β)
)
is a connection-curvature pair for C′/X.
Proof. (1) By Proposition 5.2.7 the form α′ := f∗(α) is a connection compatible
with f∗(C/X). Next let us write β′ := f∗(β) and Φ′
X := f∗(ΦX). . Since
f∗ : Ω1
pws(X)⊗ g→ Ω1
pws(Y)⊗ g
is a DG Lie algebra homomorphism, we have
Φ′
X(β′) = f∗(ΦX(β)) = f∗(
d(α) + 1
2 [α, α]
)
= d(α′) + 1
2 [α′, α′].
(2) The fact that α is compatible with Θh,X, and that ΘX satisﬁes the condition ( ♦)
in Deﬁnition 4.6.2, imply directly that α′ := Lie(ΘG)(α) is a connection compati-
ble with C′/X.
Let β′ := Θh,X(β). Then
Φ′
X(β′) = Lie(ΘG)(ΦX(β)) = Lie(ΘG)
(
d(α) + 1
2 [α, α]
)
= d(α′) + 1
2 [α′, α′].
We see that condition (ii) of Deﬁnition 5.3.1 holds. □
Deﬁnition 5.3.4 (Tame Connection). Let C/X be a Lie quasi crossed module with
additive feedback over (X, x0). A form α∈ Ω1
pws(X)⊗ g is called a tame connection
for C/X if there exists a form β∈ Ω2
pws(X)⊗ h such that (α, β) is a connection-
curvature pair (as in Deﬁnition 5.3.1).
In other words, α is a tame connection if it is a compatible connection (Deﬁni-
tion 5.2.4), and its curvature d (α) + 1
2 [α, α] comes from Ω2
pws(X)⊗ h.
Corollary 5.3.5. In the situation of Proposition 5.3.3, the forms f∗(α) and Lie(ΘG)(α)
are tame connections.
The proof is trivial.
5.4. Moving the Base Point. In this subsection we consider the following setup:
C/X = ( G, H, Ψ, Φ0, ΦX)
is a Lie quasi crossed module with additive feedback over a pointed polyhedron
(X, x0). We are given a form α∈ Ω1
pws(X)⊗ g, which is a connection compatible
with C/X. And we are given a string ρ in X, with initial point ρ(v0) = x0 and
terminal point x1 := ρ(v1). Let
g := MI(α| ρ)∈ G.
Recall that Ψ(g) is an automorphism of the pointed analytic manifold (H, 1).
We deﬁne a new multiplication on the manifold H, by the formula
h1·g h2 := Ψ(g)−1(
Ψ(g)(h1)· Ψ(g)(h2)
)
for h1, h2∈ H. In this way we obtain a new Lie group, that is denoted by Hg, and
a Lie group isomorphism
Ψ(g) : Hg→ H.
See Figure 23.
74 AMNON YEKUTIELI
Figure 23. The string ρ from x0 to x1, the group element g :=
MI(α| ρ)∈ G, and the group isomorphism Ψ(g) : Hg→ H.
The Lie algebra of Hg is hg. So hg = h as vector spaces (this is the tangent
space to H at 1), and
Ψh(g) : hg→ h
is a Lie algebra isomorphism. There is a commutative diagram of maps
(5.4.1) h
expH

hgΨh(g)oo
expHg

H H gΨ(g)oo
Note that if Ψ(g) is not a group automorphism of H, then Hg is not equal to H
as groups. In this case the maps of manifolds
expH, expHg : h→ H
could be distinct.
The data (G, Hg, Ψh) is a twisting setup (as in Deﬁnition 4.3.1), which in gen-
eral is distinct from the twisting setup (G, H, Ψh), because of the possibly distinct
exponential maps. Given a form β∈ Ω2
pws(X)⊗ h and a kite (σ, τ) in (X, x1), let
us denote by
(5.4.2) MI g(α, β| σ, τ)∈ Hg
the multiplicative integral with respect to the twisting setup (G, Hg, Ψh).
We deﬁne a map of Lie groups Φg
0 : Hg→ G by the commutative diagram
H
Φ0

HgΨ(g)oo
Φg
0

G G
AdG(g)oo
Proposition 5.4.3. The data
Cg := ( G, Hg, Ψ, Φg
0)
is a Lie quasi crossed module.
Proof. Let’s write H′ := Hg, G′ := G, u := AdG(g) : G′ → G, v := Ψ(g) :
H′ → H, Ψ′ := Ψ and Φ′
0 := Φg
0. There are commutative diagrams of group
NONABELIAN MULTIPLICATIVE INTEGRATION 75
homomorphisms
(5.4.4) H
Φ0

H′voo
Φ′
0

G G ′uoo
G
Ψ

G′uoo
Ψ′

Aut(H) Aut(H′)
Ad(v)oo
Here Aut(H) = Aut(H′) is the group of automorphisms of the pointed manifold
H = H′, and v is seen as an element of this group. The ﬁrst diagram is just the
deﬁnition of Φ′
0. The second diagram is commutative since for every g′∈ G′ we
have
Ψ(u(g′)) = Ψ(g· g′· g−1) = Ψ(g)· Ψ(g′)· Ψ(g−1)
= v· Ψ(g′)· v−1 = (Ad(v)◦ Ψ′)(g′).
And by general group theory we have a commutative diagram
(5.4.5) H
AdH

H′voo
AdH′

Aut(H) Aut(H′)
Ad(v)
oo
We are given that Ψ◦ Φ0 = AdH (this is condition (∗) of Deﬁnition 5.1.1 for
the Lie quasi crossed module C). Therefore by combining the three commutative
diagrams we see that Ψ′◦ Φ′
0 = AdH′ □
Proposition 5.4.6. The element ΦX is an additive feedback for the Lie quasi crossed
module Cg over the pointed polyhedron (X, x1). Thus
Cg/X := ( G, Hg, Ψ, Φg
0, ΦX)
is a Lie quasi crossed module with additive feedback over (X, x1).
Proof. In the notation used in the proof of the previous proposition, and with
Φ′
X := ΦX, we have to show that Φ′
X(x1) = Lie(Φ′
0), as linear maps h′→ g′. We
have commutative diagrams of linear maps
h
Lie(Φ0)

h′Lie(v)oo
Lie(Φ′
0)

g g ′Lie(u)oo
h
ΦX (x0)

h
Ψh(g)oo
ΦX (x1)
g g
Adg(g)oo
The ﬁrst diagram is the differential of the ﬁrst diagram in (5.4.4), and the second
diagram is the holonomy condition for α relative to C/X. Since ΦX is an additive
feedback for C over (X, x0) we have ΦX(x0) = Lie(Φ0). We know that Ψh(g) =
Lie(v) and Adg(g) = Lie(u). It follows that Φ′
X(x1) = ΦX(x1) = Lie(Φ′
0). □
Proposition 5.4.7. The form α is a connection compatible with Cg/X.
Proof. We continue with the notation of the previous proofs. Let σ be a string
in X initial point σ(v0) = x1 and terminal point x2 := σ(v1). Deﬁne g′ :=
MI(α| σ)∈ G′ = G. Because α is a connection compatible with C/X, and because
76 AMNON YEKUTIELI
Figure 24. The string ρ from x0 to x1, and the kite (σ, τ) in (X, x1).
g· g′ = MI(α| ρ∗ σ), we have a commutative diagram
h
Ψh(g) //
ΦX (x1)

h
ΦX (x0)

h
ΦX (x2)

Ψh(g·g′)oo
g
Adg(g)
// g g
Adg(g·g′)
oo
Since
Ψh(g)−1◦ Ψh(g· g′) = Ψh(g′)
and
Adg(g)−1◦ Adg(g· g′) = Adg(g′)
we see that the diagram
h′
Φ′
X (x1)

h′
Ψ′
h′ (g′)
oo
Φ′
X (x2)

g′ g′Adg′ (g′)
oo
is commutative. □
Theorem 5.4.8. Let
C/X = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module with additive feedback over a pointed polyhedron (X, x0),
let α∈ Ω1
pws(X)⊗ g be a connection compatible with C/X, and let ρ be a string in X,
with initial point ρ(v0) = x0. Deﬁne g := MI(α| ρ), and let
Cg/X = ( G, Hg, Ψ, Φg
0, ΦX)
be the Lie quasi crossed module with additive feedback over (X, x1) constructed above.
Given a form β∈ Ω2
pws(X)⊗ h and a kite (σ, τ) in (X, x1), consider the element
MIg(α, β| σ, τ)∈ Hg
from (5.4.2). Then
Ψ(g)
(
MIg(α, β| σ, τ)
)
= MI(α, β| ρ∗ σ, τ)
in H.
See Figure 24.
NONABELIAN MULTIPLICATIVE INTEGRATION 77
Proof. We can assume that the kite (σ, τ) is nondegenerate. Deﬁne Z := τ(I2)
and g′ := MIg(α| σ). Choose a positively oriented orthonormal linear coordinate
system (s1, s2) on Z.
Take k≥ 0 and i∈{ 1, . . . , 4k}, and deﬁne zi := ( τ◦ τk
i )( 1
2, 1
2 )∈ Z and
g′
i := MI
(
(α| (τ◦ σk
i )∗ (τ◦ τk
i◦ σpr)
)
.
So
MI
(
α| ρ∗ σ∗ (τ◦ σk
i )∗ (τ◦ τk
i◦ σpr)
)
= g· g′· g′
i.
Assume that zi is a smooth point of β|Z. Let Yi be a triangle in Z, and let
˜βi ∈ O(Yi)⊗ h, such that z ∈ Int Yi and β|Yi = ˜βi· ds1∧ ds2. According to
Deﬁnition 4.3.3 and the commutative diagram (5.4.1) we have
RP0
(
α, β| (ρ∗ σ, τ)◦ (σk
i , τk
i )
)
= expH
(
( 1
4 )k· area(Z)· Ψh(g· g′· g′
i)( ˜βi(zi))
)
= ( Ψ(g)◦ expHg )
(
( 1
4 )k· area(Z)· Ψh(g′· g′
i)( ˜βi(zi))
)
= Ψ(g)
(
RPg
0
(
α, β| (σ, τ)◦ (σk
i , τk
i )
))
.
On the other hand, if zi is a singular point of β|Z then
RP0
(
α, β| (ρ∗ σ, τ)◦ (σk
i , τk
i )
)
= 1 = Ψ(g)
(
RPg
0
(
α, β| (σ, τ)◦ (σk
i , τk
i )
))
.
We see that
RPk(α, β| ρ∗ σ, τ) = Ψ(g)
(
RPg
k (α, β| σ, τ)
)
for every k. Passing to the limit k→ ∞ ﬁnishes the proof. □
5.5. Partial Differential Equations. Let α∈ Ω1(I1)⊗ g. For x∈ I1 let σx : I1→ I1
be the linear map deﬁned on vertices by σx(v0, v1) := (v0, x). Let
(5.5.1) g(x) := MI(α| σx)∈ G.
It is well known that the function g : I1→ G deﬁned in this way is smooth, and
moreover it satisﬁes the differential equation
(5.5.2) dlog (g) = α
with initial condition g(0) = 1. See [DF] for the case G = GLn(R), in which
dlog(g) = g−1· dg
as matrices. This ODE determines the function g.
Now consider a Lie quasi-crossed module C, and a smooth connection-cur-
vature pair (α, β) in C/I2. For a point x∈ I2 let τx : I2→ I2 be the linear map
deﬁned on vertices by
τx(v0, v1, v1) :=
(
v0, (t1(x), 0), (0, t2(x))
)
.
And let σ be the empty string, so that (σ, τx) is a kite in (I2, v0). Deﬁne
h(x) := MI(α, β| σ, τx)∈ H.
Presumably the function h : I2→ H is smooth, and it satisﬁes a partial differential
equation generalizing (5.5.2). We did not check this assertion.
In the very recent paper [BGNT] the authors consider a special case: the groups
G and H are unipotent, C is a crossed module, and the pair (α, β) is algebraic.
They write down a partial differential equation, whose unique solution is de-
clared to be the multiplicative integral. Presumably this multiplicative integral
coincides with ours. For more in this direction see Subsection 9.4.
78 AMNON YEKUTIELI
5.6. Quantum Type DG Lie Algebras. Here we explain how Lie quasi crossed
modules arise from deformation theory. This is continued in the following sub-
section.
A differential graded (DG) Lie algebra is a graded R-module f = ⨁
i∈Z fi
equipped with a graded Lie bracket [−,−] and a differential d (of degree 1)
that satisfy the graded Leibniz rule. For instance, if X is a manifold and g is a Lie
algebra, then f := Ω(X)⊗ g is a DG Lie algebra. We say that f is a quantum type
DG Lie algebra if fi = 0 for all i <−1; i.e. f =⨁
i≥−1 fi.
Let us ﬁx a quantum type DG Lie algebra f, and assume that f is nilpotent, and
ﬁnite dimensional in each degree. (The assumptions of ﬁniteness and nilpotence
are for the sake of presentation; the construction works even when f is inﬁnite
dimensional and pronilpotent.)
The Lie bracket [−,−] of f makes the vector space g := f0 into a nilpotent Lie
algebra. We denote by G = exp(g) the corresponding unipotent group. In order
to be concrete, we take G to be the analytic manifold g, made into a Lie group
by the CBH formula (cf. Section 2); in particular 1 G := 0g. The exponential map
expG : g→ G is just the identity map here.
The Lie algebra g acts on the vector space fi (any i) by the adjoint action ad,
namely
ad(α)(β) := [ α, β]
for α∈ g and β∈ fi. Clearly ad (α) is R-linear. There is a second action of g on f1,
which we call the afﬁne action, and it is
af(α)(β) := d(α)− [α, β]
for β∈ f1. The action af is usually not linear – it is an action by afﬁne transfor-
mations. Both these actions integrate (or rather exponentiate) to actions Ad and
Af of the group G on the vector spaces fi and f1 respectively.
An element ω∈ f1 is called an MC element if it satisﬁes the Maurer-Cartan
equation
d(ω) + 1
2 [ω, ω] = 0.
We denote by MC (f) the set of all MC elements. It turns out that the action Af
of G on f1 preserves the subset MC (f). Namely if ω∈ MC(f) and g∈ G, then
ω′ := Af(g)(ω) is also in MC (f). The quotient set by this action is denoted by
MC(f).
Let us write h := f−1. Say an MC element ω is given. Deﬁne an R-linear map
dω : h→ g by the formula
(5.6.1) d ω(β) := d(β) + [ω, β]
for β∈ h. And deﬁne an R-bilinear operation [−,−]ω on h by the formula
(5.6.2) [β1, β2]ω := [dω(β1), β2].
An elementary calculation shows that the vector space h is a nilpotent Lie algebra
with respect to the bracket [−,−]ω, and we denote this Lie algebra by hω. A
similar calculation shows that d ω : hω→ g is a Lie algebra map. Let us deﬁne
Hω := exp(hω), the corresponding unipotent group, with multiplication h1·ω h2
and inverse h−1ω
1 , for hi∈ Hω. So as analytic manifolds we have Hω = hω = h,
and exp Hω : hω→ Hω is the identity map. There is a Lie group map exp (dω) :
Hω→ G. It is easy to see from (5.6.2) that for elements h1, h2∈ Hω one has
Ad
(
exp(dω)(h1)
)
(h2) = AdHω (h1)(h2) = h1·ω h2·ω h−1ω
1 .
NONABELIAN MULTIPLICATIVE INTEGRATION 79
Suppose we are given ω∈ MC(f) and g∈ G. Deﬁne ω′ := Af(g)(ω). A more
difﬁcult calculation shows that there is a commutative diagram of Lie algebra
maps
hω
dω

Ad(g) // hω′
dω′
g
Ad(g) // g
See [Ye5, Section 1]. Hence there is also a commutative diagram of Lie group
maps
Hω
exp(dω)

exp(Ad(g)) // Hω′
exp(dω′ )

G
exp(Ad(g)) // G
Observe that if [−,−]ω⁄= [−,−]ω′ as Lie brackets, then hω⁄= hω′ as Lie algebras,
Hω⁄= Hω′ as Lie groups, and Ψ(g) := exp(Ad(g)) is not a Lie group automor-
phism of Hω; it is only an automorphism of pointed analytic manifolds. At least
we obtain in this way an action Ψ of G on Hω by automorphisms of pointed
analytic manifolds.
Take an MC element ω, and deﬁne the map of Lie groups
Φω := exp(dω) : Hω→ G.
What we have said so far implies that the data
(5.6.3) Cω :=
(
G, Hω, Ψ, Φω
)
is a Lie quasi crossed module.
5.7. Cosimplicial DG Lie Algebras. Here we show how deformation quantiza-
tion gives rise to Lie quasi
crossed modules with additive feedback and connection-curvature pairs.
Suppose we are given a cosimplicial nilpotent quantum type DG Lie algebra f. So
f ={fp,·}p∈N, where each fp,· = ⨁
i≥−1 fp,i is a nilpotent quantum type DG Lie
algebra.
From the cosimplicial object f one constructs its Thom-Sullivan normalization
˜N(f), which is a nilpotent quantum type DG Lie algebra, involving algebraic
differential forms on all the simplices ∆p, p≥ 0. For details see [Ye2, Section 2].
Suppose ˜ω is an MC element of ˜N(f). By deﬁnition ˜ω ={ ˜ωp,q}, where
˜ωp,q∈ Ωq(∆p)⊗ fp,1−q, p∈ N, q∈{ 0, 1, 2}.
Let us ﬁx a number p. We look at the components of ˜ω with index p:
ω := ˜ωp,0∈O (∆p)⊗ fp,1,
α := ˜ωp,1∈ Ω1(∆p)⊗ fp,0
and
β := ˜ωp,2∈ Ω2(∆p)⊗ fp,−1.
Now let us write g := fp,0, h := fp,−1 and X := ∆p. With this notation ω∈
O(X)⊗ fp,1, α∈ Ω1(X)⊗ g and β∈ Ω2(X)⊗ h.
80 AMNON YEKUTIELI
Choose some point x0∈ X. The element ω(x0)∈ fp,1 turns out to be an MC
element of the DG Lie algebra fp,·. As in (5.6.3), we have a Lie quasi crossed
module
Cω(x0) =
(
G, Hω(x0), Ψ, Φω(x0)
)
.
Next we deﬁne
ΦX := dω∈O (X)⊗ Hom(h, g);
see (5.6.1). This is an additive feedback for Cω(x0) over the pointed polyhedron
(X, x0), so we obtain a Lie quasi crossed module with additive feedback
(5.7.1) Cω(x0)/X =
(
G, Hω(x0), Ψ, Φω(x0), ΦX
)
.
Furthermore, it can be shown that the pair (α, β) is a connection-curvature pair
in Cω(x0)/X. Taking any kite (σ, τ) in (X, x0) we thus obtain a group element
MI(α, β| σ, τ)∈ Hω(x0).
In Subsection 9.5 we continue with this setup, and state Conjecture 9.5.2.
NONABELIAN MULTIPLICATIVE INTEGRATION 81
6. S tokes Theorem in Dimension Two
The purpose of this section is to prove Theorem 6.2.1. When H = G (see
Example 6.2.7) this is just a fancy version of Schlesinger’s theorem.
Let (X, x0) be a pointed polyhedron. Recall the notions of Lie quasi crossed
module with additive feedback
(6.0.1) C/X = ( G, H, Ψ, Φ0, ΦX)
over (X, x0), connection-curvature pair (α, β), and multiplicative integral
MI(α, β| σ, τ); see Deﬁnitions 5.2.2, 5.3.1 and 4.4.16 respectively.
6.1. Some Estimates. In this subsection we assume that (X, x0) = ( I2, v0). We ﬁx
a Lie quasi crossed module with additive feedback C/X over (I2, v0), in which
G = H, as in Example 5.1.4. We also ﬁx a connection-curvature pair (α, β) for
C/X. Note that the equality
(6.1.1) β = d(α) + 1
2 [α, α]
holds in Ω2
pws(I2)⊗ g. As in Section 1 we choose a euclidean norm ‖−‖g on the
vector space g; an open neighborhood V0(G) of 1 in G on which log G is well-
deﬁned; a convergence radius ϵ0(G); and a commutativity constant c0(G).
In Proposition 4.5.4 we established certain constants c2′ (α, β) and
ϵ2′ (α, β).
Lemma 6.1.2. There are constants c3(α, β) and ϵ3(α, β) with these properties:
(1) c3(α, β)≥ c2′ (α, β) and 0 < ϵ3(α, β)≤ ϵ2′ (α, β).
(2) Suppose (σ, τ) is a square kite in (I2, v0) such that side(τ) < ϵ3(α, β) and
len(σ)≤ 5. Then
MI(α, β| σ, τ), MI(α| ∂(σ, τ))∈ V0(G)
and
‖‖ logG
(
MI(α, β| σ, τ)
)‖‖ ,
‖‖ logG
(
MI(α| ∂(σ, τ))
)‖‖≤ c3(α, β)· side(τ)2 .
Proof. For MI(α, β| σ, τ) we can use the estimate from Proposition 4.5.2.
For the boundary we have to do some work. Let’s write ϵ := side(τ), and
suppose that ϵ < 1
4 ϵ1(α), where ϵ1(α) is the constant from Deﬁnition 3.3.16.
Consider the closed string ∂τ of length 4ϵ. Write g1 := MI(α| ∂τ)∈ G. According
to Proposition 3.5.11 we know that g1∈ V0(G), and
‖‖ logG(g1)−
∫
∂τ
α
‖‖≤ c0(G)· c1(α)2· (4ϵ)2 .
By the abelian Stokes Theorem (Theorem 1.8.3) we have
∫
∂τ
α =
∫
τ
d(α).
Now ‖‖
∫
τ
d(α)
‖‖≤ area(τ)·‖ α‖Sob = ϵ2·‖ α‖Sob .
We conclude that
‖logG(g1)‖≤
(
c0(G)· c1(α)2· 16 +‖α‖Sob
)
· ϵ2 .
Next let g2 := MI(α| σ)∈ G. Consider the representation Ad g : G→ GL(g).
By Proposition 3.5.10 the norm of the operator Ad g(g2) satisﬁes
‖Adg(g2)‖≤ exp(c4(α, Adg)· 5) .
82 AMNON YEKUTIELI
Figure 25. Computing RP 0(α| ∂τ) for a tiny square kite (σ, τ) in (I2, v0).
Finally we look at g := MI(α| ∂(σ, τ)). By deﬁnition
g = g2· g1· g−1
2 = AdG(g2)(g1).
The logarithm is
logG(g) = Adg(g2)(logG(g1)).
By combining the estimates above we get
‖logG(g)‖≤ exp(c4(α, Adg)· 5)·
(
c0(G)· c1(α)2· 16 +‖α‖Sob
)
· ϵ2 .
We see that we can take the following constants:
ϵ3(α, β) := min
(
ϵ2(α, β), 1
4 ϵ1(α)
)
and
c4(α, β) :=
max
(
c2(α, β), exp(c4(α, Adg)· 5)· (c0(G)· c1(α)2· 16 +‖α‖Sob)
)
.
□
Lemma 6.1.3. There are constants c4(α, β) and ϵ4(α, β) with these properties:
(1) c3(α, β)≤ c4(α, β) and 0 < ϵ4(α, β)≤ ϵ3(α, β).
(2) Suppose (σ, τ) is a square kite in (I2, v0) such that side(τ) < ϵ4(α, β),
len(σ)≤ 5, and α|τ(I2) is smooth. Then
‖‖ logG
(
MI(α, β| σ, τ)
)
− logG
(
MI(α| ∂(σ, τ))
)‖‖≤ c4(α, β)· side(τ)3 .
Proof. Let ϵ := side(τ), Z := τ(I2), and z := τ( 1
2, 1
2 ), which is the midpoint of the
square Z. Denote by (ρ1, . . . ,ρ4) the closed string ∂τ. For any i∈{ 1, . . . , 4} let zi
be the midpoint of the edge ρi(I1). See Figure 25 for an illustration. Let (s1, s2)
be the positively oriented orthonormal linear coordinate system on Z, such that
τ∗(si) = ϵ· (ti− 1
2 ).
So in particular si(z) = 0.
Since α|Z is smooth, there are functions ˜α1, ˜α2∈O (Z)⊗ g such that
α|Z = ˜α1· ds1 + ˜α2· ds2.
The Taylor expansion of ˜αj around z to second order looks like this:
(6.1.4) ˜αj(x) = ˜αj(z) + ∑
1≤k≤2
( ∂
∂sk
˜αj)(z)· sk(x) + ∑
1≤k,l≤2
gj,k,l(x)· sk(x)· sl(x)
for x∈ Z. Here gj,k,l : Z→ g are continuous functions satisfying
(6.1.5) ‖gj,k,l‖≤‖ α‖Sob .
NONABELIAN MULTIPLICATIVE INTEGRATION 83
We deﬁne elements λi∈ g as follows:
(6.1.6)
λ1 := ϵ· ˜α1(z1),
λ2 := ϵ· ˜α2(z2),
λ3 :=−ϵ· ˜α1(z3),
λ4 :=−ϵ· ˜α2(z4).
Then, almost by deﬁnition,
RP0(α| ρi) = expG(λi)
and
(6.1.7) RP 0(α| ∂τ) =
4
∏
i=1
expG(λi).
Now
sk(zi)∈{ 0, 1
2 ϵ,− 1
2 ϵ},
and the value 0 occurs half the time. So the Taylor expansion (6.1.4) for the point
zi has only one summand of order 1 in ϵ (instead of two). Let us deﬁne
µ1 := ϵ· ˜α1(z), µ′
1 :=− 1
2 ϵ2· ( ∂
∂s2
˜α1)(z),
µ2 := ϵ· ˜α2(z), µ′
2 := 1
2 ϵ2· ( ∂
∂s1
˜α2)(z),
µ3 :=−ϵ· ˜α1(z), µ′
3 :=− 1
2 ϵ2· ( ∂
∂s2
˜α1)(z),
µ4 :=−ϵ· ˜α2(z), µ′
4 := 1
2 ϵ2· ( ∂
∂s1
˜α2)(z).
Then using the estimate (6.1.5) for the quadratic terms in (6.1.4) we obtain
(6.1.8)
‖‖ λi− (µi + µ′
i)
‖‖≤ ϵ3·‖ α‖Sob .
We also have these bounds:
(6.1.9) ‖λi‖≤ ϵ·‖ α‖Sob
and
(6.1.10) ‖µi‖≤ ϵ·‖ α‖Sob ,‖µ′
i‖≤ 1
2 ϵ2·‖ α‖Sob .
According to property (iv) of Theorem 2.1.2, the estimates (6.1.8) and (6.1.9)
yield
(6.1.11)
‖‖ logG
(
∏
4
i=1 expG(λi)
)
− logG
(
∏
4
i=1 expG(µi + µ′
i)
)‖‖
≤ 4ϵ3· c0(G)·‖ α‖Sob .
for sufﬁciently small ϵ. Similarly the estimates (6.1.10) give us
(6.1.12)
‖‖ logG
(
∏
4
i=1 expG(µi + µ′
i)
)
− logG
(
∏
4
i=1 expG(µi)
)
− ∑
4
i=1 µ′
i
‖‖
≤ 2ϵ3· c0(G)·‖ α‖2
Sob .
Now µ3 =−µ1 and µ4 =−µ2, and hence
4
∏
i=1
expG(µi) = expG(µ1)· expG(µ2)· expG(−µ1)· expG(−µ2).
According to property (iii) of Theorem 2.1.2 we see that
(6.1.13)
‖‖ logG
(
∏
4
i=1 expG(µi)
)
− [µ1, µ2]
‖‖≤ 2ϵ3· c0(G)·‖ α‖3
Sob .
84 AMNON YEKUTIELI
For the terms µ′
i we have
(6.1.14)
4
∑
i=1
µ′
i =−ϵ2· ( ∂
∂s2
˜α1)(z) + ϵ2· ( ∂
∂s1
˜α2)(z) .
Putting together equations (6.1.7), (6.1.11), (6.1.12), (6.1.13) and (6.1.14) we con-
clude that for some c≥ 1 (depending on (α, β)) the estimate
‖‖ logG
(
RP0(α| ∂τ)
)
− ϵ2·
(
[˜α1(z), ˜α2(z)]− ( ∂
∂s2
˜α1)(z) + ( ∂
∂s1
˜α2)(z)
)‖‖
≤ ϵ3· c
holds for sufﬁciently small ϵ. Using Proposition 3.3.22(2) we get
(6.1.15)
‖‖ logG
(
MI(α| ∂τ)
)
− ϵ2·
(
[˜α1(z), ˜α2(z)]− ( ∂
∂s2
˜α1)(z) + ( ∂
∂s1
˜α2)(z)
)‖‖
≤ ϵ3· c′
for a suitable constant c′.
Since equation (6.1.1) holds, we know that β is smooth on Z. Let ˜β∈O (Z)⊗ g
be such that β|Z = ˜β· ds1∧ ds2. Then (6.1.1) becomes
˜β = [ ˜α1, ˜α2]− ( ∂
∂s2
˜α1) + ( ∂
∂s1
˜α2),
as smooth functions Z→ g. Thus we can rewrite (6.1.15) as
(6.1.16)
‖‖ logG
(
MI(α| ∂τ)
)
− ϵ2· ˜β(z)
)‖‖≤ ϵ3· c′ .
Letting g := MI(α| σ), we have (by Proposition 3.5.8):
MI
(
α| ∂(σ, τ)
)
= g· MI(α| ∂τ)· g−1 = AdG(g)
(
MI(α| ∂τ)
)
.
The map log G sends AdG(g) to Adg(g), and therefore
logG
(
MI
(
α| ∂(σ, τ)
))
= Adg(g)
(
logG
(
MI(α| ∂τ)
))
.
Recall that the length of σ is bounded by 5, so by Proposition 3.4.3 the norm of
the operator Ad g(g) on g is also bounded. Plugging in the estimate (6.1.16) we
now arrive at
(6.1.17)
‖‖ logG
(
MI
(
α| ∂(σ, τ)
))
− ϵ2· Adg(g)
( ˜β(z)
)‖‖≤ ϵ3· c′′′
for a suitable bound c′′′, again depending on (α, β).
Finally, by deﬁnition we have
logG
(
RP0(α, β| σ, τ)
)
= ϵ2· Adg(g)
( ˜β(z)
)
.
According to Proposition 4.5.2(2) we know that
‖‖ logG
(
RP0(α, β| σ, τ)
)
− logG
(
MI(α, β| σ, τ)
)‖‖≤ c2(α, β)· ϵ4 .
Combining this with (6.1.17) we get
‖‖ logG
(
MI(α, β| σ, τ)
)
− logG
(
MI(α| ∂(σ, τ))
)‖‖≤ c4(α, β)· ϵ3
for a sufﬁciently large constant c4(α, β) and for all sufﬁciently small ϵ. This gives
us a value for ϵ4(α, β). □
Deﬁnition 6.1.18. Let us ﬁx constants c4(α, β) and ϵ4(α, β) as in Lemma 6.1.3. A
square kite (σ, τ) in (I2, v0) will be called (α, β)-tiny in this section if side (τ) <
ϵ4(α, β) and len(σ)≤ 5.
NONABELIAN MULTIPLICATIVE INTEGRATION 85
Lemma 6.1.19. Let (σ, τ) be a kite in (I2, v0). Take some k≥ 0. For i∈{ 1, . . . , 4k} let
(σi, τi) := ( σ, τ)◦ (σk
i , τk
i ) = tesk
i (σ, τ).
Then
4k
∏
i=1
MI
(
α| ∂(σi, τi)
)
= MI
(
α| ∂(σ, τ)
)
.
Proof. By Proposition 3.5.8 we get cancellation of the contribution of all inner
edges. □
6.2. Stokes Theorem.
Theorem 6.2.1 (Nonabelian Stokes Theorem in Dimension 2) . Let (X, x0) be a
pointed polyhedron, let C/X be a Lie quasi crossed module with additive feedback over
(X, x0), and let (α, β) be a connection-curvature pair for C/X. Then for any kite (σ, τ)
in (X, x0) one has
Φ0
(
MI(α, β| σ, τ)
)
= MI
(
α| ∂(σ, τ)
)
in G.
Proof. According to Proposition 5.2.6(1) there is a transfer of twisting setups
(idG, Φ0, ΦX) : (G, H, Ψh)→ (G, G, Adg)
parametrized by (X, x0). Hence by Propositions 4.6.5 and 5.3.3(2) we can assume
that G = H. Next, using Propositions 4.1.6, 4.5.3 and 5.3.3(1) we can further
assume that (X, x0) = ( I2, v0), (σ, τ) is a square kite, and len (σ)≤ 1. We need to
prove that
(6.2.2) MI (α, β| σ, τ) = MI(α| ∂(σ, τ))
in G.
Take k large enough such that all the kites
(6.2.3) (σi, τi) := tesk
i (σ, τ)
in the k-th binary tessellation of (σ, τ) are (α, β)-tiny. By Proposition 4.5.1 we
have
MI(α, β| σ, τ) =
4k
∏
i=1
MI
(
α, β| σi, τi).
Using Lemma 6.1.19 we see that it sufﬁces to prove that
MI
(
α, β| σi, τi) = MI
(
α| ∂(σi, τi)
)
for every i. In this way we have reduced the problem to proving that
(6.2.4) MI (α, β| σ, τ) = MI
(
α| ∂(σ, τ)
)
for any (α, β)-tiny kite (σ, τ) in (I2, v0).
So assume (σ, τ) is (α, β)-tiny, with ϵ := side(τ). Take some k≥ 0, and let
(σi, τi) be like in (6.2.3). Then side (τi) = ( 1
2 )k· ϵ. We know that
(6.2.5) MI (α, β| σ, τ) =
4k
∏
i=1
MI(α, β| σi, τi)
and
(6.2.6) MI
(
α| ∂(σ, τ)
)
=
4k
∏
i=1
MI
(
α| ∂(σi, τi)
)
.
86 AMNON YEKUTIELI
Let us do some estimates now. If i is a bad index (in the sense of Deﬁnition
4.4.12), then by Lemma 6.1.2 we know that
‖‖ logG
(
MI(α, β| σi, τi)
)‖‖≤ c3(α, β)· ( 1
2 )2kϵ2
and ‖‖ logG
(
MI(α| ∂(σi, τi))
)‖‖≤ c3(α, β)· ( 1
2 )2kϵ2 .
On the other hand, if i is a index kite, then Lemma 6.1.3 says that
‖‖ logG
(
MI(α, β| σi, τi)
)
− logG
(
MI(α| ∂(σi, τi))
)‖‖≤ c4(α, β)· ( 1
2 )3kϵ3 .
Using these estimates, equations (6.2.5)-(6.2.6), Lemma 4.4.13 and property (iv) of
Theorem 2.1.2, we arrive at‖‖ logG
(
MI(α, β| σ, τ)
)
− logG
(
MI(α| ∂(σ, τ))
)‖‖
≤ 4k· c4(α, β)· ( 1
2 )3kϵ3
| {z }
good indices
+
(
a0 + a1· 2k)
· c3(α, β)· ( 1
2 )2kϵ2
| {z }
bad indices
.
Here ai := ai(α, β, I2) are the constants from Lemma 4.4.13. Since the right hand
side of this inequality tends to 0 as k→ ∞, we conclude that (6.2.4) holds. □
Example 6.2.7. A special case of the corollary is the situation of Example 5.1.4.
Take any differential form α∈ Ω1
pws(X)⊗ g, and let β := d(α) + 1
2 [α, α]. Then
(α, β) is a connection-curvature pair, and the corollary says that
MI(α, β| σ, τ) = MI
(
α| ∂(σ, τ)
)
.
This is just Schlesinger’s theorem [DF].
6.3. The Fundamental Relation. Here is an important consequence of Theorem
6.2.1.
Theorem 6.3.1 (The Fundamental Relation). Let (X, x0) be a pointed polyhedron, let
C/X be a Lie quasi crossed module with additive feedback over (X, x0), let (α, β) be a
connection-curvature pair for C/X, and let (σ, τ) be a kite in (X, x0). Let us write
g := MI
(
α| ∂(σ, τ)
)
∈ G
and
h := MI(α, β| σ, τ)∈ H.
Then
Ψ(g) = AdH(h)
as automorphisms of the pointed manifold (H, 1). In particular, Ψ(g) is a group auto-
morphism of H.
Proof. According to Theorem 6.2.1 we have g = Φ0(h), and by condition (∗) of
Deﬁnition 5.1.1 we know that
Ψ(g) = Ψ(Φ0(h)) = AdH(h).
□
Corollary 6.3.2. In the situation of Theorem 6.3.1, suppose (σ′, τ′) is another kite in
(X, x0). We get a closed string ∂(σ′, τ′) based at x 0, and a kite
(
∂(σ′, τ′)∗ σ, τ
)
.
Then, writing
h′ := MI(α, β| σ′, τ′)∈ H,
one has
MI
(
α, β| ∂(σ′, τ′)∗ σ, τ
)
= AdH(h′)(h)
in H.
NONABELIAN MULTIPLICATIVE INTEGRATION 87
Figure 26. Illustration for Corollary 6.3.2.
See Figure 26.
Proof. Let ρ := ∂(σ′, τ′), which is a closed string based at x0, and let g′ :=
MI(α| ρ)∈ G. By Theorem 6.3.1 we have Ψ(g′) = AdH(h′), so this is a group
automorphism of H. Consider the “moving of the base point” corresponding to
ρ. Since Ψ(g′) is a group automorphism of H, it follows that Hg′
= H, and
MIg′
(α, β| σ, τ) = MI(α, β| σ, τ) = h.
But from Theorem 5.4.8 we get
Ψ(g′)
(
MIg′
(α, β| σ, τ)
)
= MI(α, β| ρ∗ σ, τ).
□
NONABELIAN MULTIPLICATIVE INTEGRATION 89
7. S quare Puzzles
In this section we work with the pointed polyhedron (X, x0) := (I2, v0). Let us
ﬁx some Lie quasi crossed module with additive feedback
C/I2 = ( G, H, Ψ, Φ0, ΦX)
over (I2, v0), and a piecewise smooth connection-curvature pair (α, β) in C/I2.
See Deﬁnitions 5.2.2 and 5.3.1. We will show that under certain homotopical
restrictions, moving little square kites around inside I2 doesn’t alter the multi-
plicative surface integral.
7.1. The Free Monoid with Involution. It will be helpful for us to have some
terminology for abstract words and cancellation.
Recall that a monoid is a unital semigroup. Suppose M, N are monoids. By
homomorphism of monoids we mean a function φ : M→ N that preserves the
multiplications and the units.
Let S be some set, possibly inﬁnite, whose elements we consider as symbols.
A word in S is by deﬁnition a ﬁnite sequence w = ( s1, . . . ,sn) of elements of S.
Thus w is a function
w :{1, . . . ,n}→ S.
The natural number n is the length of w. We denote the set of all these words
by Wrd(S). This is a monoid under the operation of concatenation, which we
denote by∗, and the unit is the empty word 1 : = () . We consider S as a subset
of Wrd(S), namely the words of length 1. In fact Wrd (S) a free monoid: any
function S→ M, where M is a monoid, extends uniquely to a homomorphism of
monoids Wrd(S)→ M.
Next suppose s = ( s1, . . . ,sn) is a sequence of distinct elements of S. We refer
to such a sequence of distinct elements as an alphabet. We denote by
Wrd(s) = Wrd(s1, . . . ,sn)
the subset of Wrd (S) consisting of the words in the alphabet s only. More
precisely, a word w of length m belongs to Wrd (s) if and only if the function
w :{1, . . . ,m}→ S factors as w = s◦ ˜w, for a function (necessarily unique)
˜w :{1, . . . ,m}→{ 1, . . . ,n}.
The elements of Wrd (s) are denoted by w(s), and are called words in s. Clearly
Wrd(s) is a sub-monoid of Wrd(S); and it is also a free monoid, on the n symbols
s1, . . . ,sn. Given a homomorphism of monoids φ : Wrd (S)→ M, and a word
w(s)∈ Wrd(s), we shall use the following “substitution notation”:
w(γ) = w(γ1, . . . ,γn) := φ(w(s))∈ M,
where γ is the sequence
γ = ( γ1, . . . ,γn) :=
(
φ(s1), . . . ,φ(sn)
)
in M.
Let M be a monoid. By an anti-automorphism of M we mean a bijection
ψ : M→ M that reverses the order of multiplication, and preserves the unit. An
involution of the monoid M is an anti-automorphism ψ such that ψ◦ ψ = id. The
pair (M, ψ) is then called a monoid with involution.
90 AMNON YEKUTIELI
Let S be a set. Let S−1 be a new copy of S; i.e. S−1 is a set disjoint from S,
equipped with a bijection ψS : S ≃− →S−1. This bijection extends to an involution
ψS of the set S∪ S−1. We deﬁne
Wrd±1(S) := Wrd(S∪ S−1).
This monoid has a canonical involution ψS, extending the involution on the set
S∪ S−1. We sometimes write w−1 := ψS(w) for a word w∈ Wrd±1(S). Note
however that the product w∗ w−1 is not 1 (unless w = 1, the empty word).
Indeed, the length of w∗ w−1 is twice the length of w (as words in S∪ S−1).
The monoid Wrd±1(S) is a free monoid with involution. Here is what this means:
let (M, ψ) be any monoid with involution, and let f : S→ M be a function. Then
there is a unique homomorphism of monoids φ : Wrd±1(S)→ M that commutes
with the involutions and extends f .
Given a sequence s = (s1, . . . ,sn) of distinct elements of S, we write
Wrd±1(s) = Wrd±1(s1, . . . ,sn)
:= Wrd(s1, . . . ,sn, s−1
1 , . . . ,s−1
n )⊂ Wrd±1(S).
This is also a free monoid with involution.
Suppose the words w and w′ in Wrd±1(S) satisfy this condition:
w = v1∗ u∗ v2 and w′ = v1∗ v2,
where v1 and v2 are some elements of Wrd±1(S), and u is either s∗ s−1 or s−1∗
s for some s ∈ S. Then we say that w′ is gotten from w by cancellation . The
equivalence relation generated by this condition is called cancellation equivalence,
and is denoted by∼can. Thus words w, w′∈ Wrd(S) satisfy w∼can w′ if and only
if there are words
w = w0, w1, . . . ,wr = w′
such that for each i either wi+1 is gotten from wi by cancellation, or vice versa.
Note that the set of equivalence classes Wrd ±1(S)/∼can is a free group, with
basis the image of S.
When we talk about Wrd±1(s1, . . . ,sn), we always mean implicitly that it is the
free monoid with involution on some sequence (s1, . . . ,sn) of distinct elements in
some set S (possibly S ={s1, . . . ,sn}).
If Γ is a group, then by default we put on it the involution ψ(γ) := γ−1. In this
way Γ becomes a monoid with involution.
Let (M, ψ) be a monoid with involution. Given an element m∈ M, deﬁne the
operation Ad(m) : M→ M by
(7.1.1) Ad (m)(m′) := m∗ m′∗ ψ(m).
Warning: Ad(m) is not a homomorphism of monoids (unless M is a group).
Let Y be a ﬁnite graph (i.e. a ﬁnite 1-dimensional cellular complex), with base
point y0 that’s a vertex, and n edges τ1, . . . ,τn. Choose an orientation on each τi
(i.e. a homeomorphism I1∼= τi). The reversely oriented cell is denoted by τ−1
i .
Take an alphabet s = ( s1, . . . ,sn). Any word w(s)∈ Wrd±1(s) gives rise, by the
evaluation si ↦→ τi and s−1
i ↦→ τ−1
i , a sequence of oriented cells w(τ1, . . . ,τn),
which might or might not be a path in Y.
Lemma 7.1.2. In the situation described above, suppose w(τ1, . . . ,τn) is a closed path in
Y based at y 0, such that [w(τ1, . . . ,τn)] = 1 in the fundamental group π1(Y, y0). Then
w(s)∼can 1 in Wrd±1(s).
NONABELIAN MULTIPLICATIVE INTEGRATION 91
Proof. We learned this proof from Y. Glasner. First consider a pointed tree ( ˜Y, ˜y0),
and a sequence ( ˜ρ1, . . . ,˜ρl) of edges in ˜Y which is a path starting at ˜y0. If this
path is closed, then it is cancellation equivalent to a point. This can be seen
by induction on l. Indeed, let i be an index such that the endpoint of the path
( ˜ρ1, . . . ,˜ρi) is at maximal distance from the base vertex ˜y0. Then we must have
˜ρi+1 = ˜ρ−1
i ; so we can cancel these two edges, yielding a shorter closed path.
Getting back to our problem, write (ρ1, . . . ,ρl) := [ w(τ1, . . . ,τn)], where ρi∈
{τ±1
1 , . . . ,τ±1
n }. Then w(s)∼can 1 if and only if (ρ1, . . . ,ρl) is cancellation equiva-
lent to a point. Let p : ( ˜Y, ˜y0)→ (Y, yo) be the universal covering map; so ( ˜Y, ˜y0)
is a pointed tree. Since the closed path (ρ1, . . . ,ρl) is trivial in the fundamental
group of Y, it lifts to a closed path ( ˜ρ1, . . . ,˜ρl) based at ˜y0 in the tree ˜Y. By the
ﬁrst paragraph the path ( ˜ρ1, . . . ,˜ρl) is cancellation equivalent to a point. Hence
so is (ρ1, . . . ,ρl). □
7.2. Generating Sequences. Recall that for k≥ 0, the k-th binary subdivision
sdk I2 of I2 is the cellular decomposition of I2 into 4k squares, each of side ( 1
2 )k.
The 1-skeleton of sd k I2 is the topological space sk 1 sdk I2, and its fundamental
group, based at v0, is π1(sk1 sdk I2). For a closed string σ based at v0 and pat-
terned on sd k I2 we denote by [σ] the corresponding element of π1(sk1 sdk I2).
Deﬁnition 7.2.1. Let k∈ N, and let
ρ♮ =
(
(σ♮
1, τ♮
1 ), . . . ,(σ♮
4k, τ♮
4k )
)
be a sequence of kites in (I2, v0), all patterned on sd k I2. For any i let
a♮
i := [ ∂(σ♮
i , τ♮
i )]∈ π1(sk1 sdk I2).
(1) If the sequence (a♮
1, . . . ,a♮
4k ) is a basis of the group π1(sk1 sdk I2), then we
say that ρ♮ is a generating sequence for sdk I2.
(2) Let (σ, τ) be a kite in (I2, v0) patterned on sdk I2. If τ = τ♮
i for some i then
we say that (σ, τ) is aligned with ρ♮.
The k-th binary tessellation tes k I2 (see Deﬁnition 4.2.5) is an example of a
generating sequence for sd k I2.
Lemma 7.2.2. Let ρ♮ be a generating sequence for sdk I2, and let a ♮
i =
as in the deﬁnition above. Let w (s) ∈ Wrd±1(s) = Wrd±1(s1, . . . ,s4k ) be a word
such that
w(a♮
1, . . . ,a♮
4k ) = 1
in the group π1(sk1 sdk I2). Then
w(s)∼can 1
in Wrd±1(s).
Proof. This is because the sequence (a♮
1, . . . ,a♮
4k ) is a basis of the free group
π1(sk1 sdk I2). □
Lemma 7.2.3. Let σ1, σ2 be linear strings in I2, and let τ : I2→ I2 be a linear map, all
patterned on sdk I2 for some k≥ 0.
92 AMNON YEKUTIELI
(1) Suppose σ1, σ2 are closed strings based at v 0, and [σ1] = [ σ2] in
π1(sk1 sdk I2). Then
MI(α| σ1) = MI(α| σ1)
in G.
(2) Suppose that σi(v0) = v0 and σi(v1) = τ(v0) for i = 1, 2; so that (σi, τ) are
kites in I2 and σ2∗ σ−1
1 is a closed string based at v 0. If [σ2∗ σ−1
1 ] = 1 in
π1(sk1 sdk I2), then
MI(α, β| σ1, τ) = MI(α, β| σ2, τ)
in H.
Proof. (1) Take n := 2k+1· (2k + 1), the number of 1-cells in sd k I2. Let us denote
these 1-cells by τ1, . . . ,τn, and let’s choose an orientation for these cells, as in
Lemma 7.1.2. There are unique words
w1(s), w2(s)∈ Wrd±1(s) = Wrd±1(s1, . . . ,sn)
such that wi(τ1, . . . ,τn) = σi as strings. Lemma 7.1.2 implies that
w1(s)∼can w2(s) in Wrd±1(s). Now Deﬁnition 3.5.7 and Proposition 3.5.8 tell
us that
MI
(
α| w1(τ1, . . . ,τn)
)
= MI
(
α| w2(τ1, . . . ,τn)
)
.
(2) Let gi := MI(α| σi)∈ G. By part (1) we know that
g2· g−1
1 = MI(α| σ2)· MI(α| σ−1
1 ) = MI(α| σ2∗ σ−1
1 ) = 1;
so that g1 = g2. Let g := g1 = g2.
Let σ0 denote the empty string. So σi∗ σ0 = σi for i = 1, 2. Now according to
Theorem 5.4.8 we have
MI(α, β| σi, τ) = Ψ(g)
(
MIg(α, β| σ0, τ)
)
.
for i = 1, 2. But the right hand side is independent of i. □
Lemma 7.2.4. Let ρ♮ be a generating sequence for sdk I2, let a ♮
i be as in deﬁnition 7.2.1,
and let
h♮
i := MI(α, β| σ♮
i , τ♮
i )∈ H.
Suppose (σ, τ) is a kite in (I2, v0) patterned on sdk I2 and aligned with ρ♮. Then there is
a word
w(s)∈ Wrd±1(s) = Wrd±1(s1, . . . ,s4k )
such that
[∂(σ, τ)] = w(a♮
1, . . . ,a♮
4k )
in π1(sk1 sdk I2), and
MI(α, β| σ, τ) = w(h♮
1, . . . ,h♮
4k )
in H.
Proof. Let i be an index such that τ = τ♮
i . Then σ∗ (σ♮
i )−1 is a closed string based
at v0 and patterned on sd k I2. (See Figure 27 for an illustration where k = 1
ρ♮ = tes1 I2.) There is a word u(s)∈ Wrd±1(s) such that
[σ∗ (σ♮
i )−1] = u(a♮
1, . . . ,a♮
4k )
in the group π1(sk1 sdk I2).
NONABELIAN MULTIPLICATIVE INTEGRATION 93
Figure 27. A kite (σ, τ) patterned on sd 1 I2 and aligned with
tes1 I2, the corresponding kite (σ1
i , τ1
i ), and the closed string σ∗
(σ1
i )−1. Here i = 2.
We can also consider the monoid M of ﬁnite sequences of closed strings pat-
terned on sd k I2 and based at v0, where composition is concatenation of se-
quences, and the involution is given by reversal of order and (3.5.4). Consider
the sequence
∂ρ♮ :=
(
∂(σ♮
1, τ♮
1 ), . . . ,∂(σ♮
4k, τ♮
4k )
)
.
The evaluation u(∂ρ♮) of the word u(s) on the sequence ∂ρ♮ is an element of M.
And we have
(7.2.5)
[
u(∂ρ♮)
]
= u(a♮
1, . . . ,a♮
4k )
in the group π1(sk1 sdk I2).
Take
w(s) := u(s)∗ si∗ u(s)−1∈ Wrd±1(s).
It is easy to check that
[∂(σ, τ)] = w(a♮
1, . . . ,a♮
4k )
holds in π1(sk1 sdk I2). Next, using Corollary 6.3.2 recursively, equation (7.2.5)
and Lemma 7.2.3(2), we obtain
w(h♮
1, . . . ,h♮
4k ) = u(h♮
1, . . . ,h♮
4k )· h♮
i· u(h♮
1, . . . ,h♮
4k )−1
= MI
(
α, β| u(∂ρ♮)∗ σ♮
i , τ♮
i
)
= MI
(
α, β| σ, τ
)
.
□
Lemma 7.2.6. Let ρ♮ be a generating sequence for sdk I2, and let
ρ =
(
(σ1, τ1), . . . , (σm, τm)
)
be some sequence of kites in (I2, v0) patterned on sdk I2 and aligned with ρ♮. Write
ai := [ ∂(σi, τi)]∈ π1(sk1 sdk I2)
and
hi := MI(α, β| σi, τi)∈ H.
Let
u(s)∈ Wrd±1(s) = Wrd±1(s1, . . . ,sm)
be a word such that
u(a1, . . . ,am) = 1.
94 AMNON YEKUTIELI
Figure 28. A kite (σ, τ) in (I2, v0), and the kite ﬂip (σ, τ).
Then
u(h1, . . . ,hm) = 1.
Proof. Using Lemma 7.2.4, for each i∈{ 1, . . . ,m} we can ﬁnd a word
wi(t)∈ Wrd±1(t) = Wrd±1(t1, . . . ,t4k )
such that
ai = wi(a♮
1, . . . ,a♮
4k )
and
hi = wi(h♮
1, . . . ,h♮
4k )
(with notation as in the previous lemmas). Deﬁne
w(t) := u
(
w1(t), . . . ,wm(t)
)
∈ Wrd±1(t).
Then
w(a♮
1, . . . ,a♮
4k ) = 1
in π1(sk1 sdk I2), and
w(h♮
1, . . . ,h♮
4k ) = u(h1, . . . ,hm)
in H.
Now according to Lemma 7.2.2 we have w(t)∼can 1 in Wrd±1(t). Hence by
cancellation in the group H we get w(h♮
1, . . . ,h♮
4k ) = 1. □
7.3. The Flip. The ﬂip of I2 is the linear automorphism whose action on vertices
is
ﬂip (v0, v1, v2) := (v0, v2, v1).
Given a kite (σ, τ) in (I2, v0), its ﬂip is the kite
ﬂip (σ, τ) := ( σ, τ◦ ﬂip ).
See Figure 28 for an illustration.
Note that
ﬂip (σ, τ) = ( σ, τ)◦ ﬂip (σ0
1 , τ0
1 ),
where (σ0
1 , τ0
1 ) is the basic kite. By associativity of kite composition it follows that
given any two kites (σ1, τ1) and (σ2, τ3) in I2, one has
(7.3.1) ﬂip
(
(σ1, τ1)◦ (σ2, τ2)
)
= ( σ1, τ1)◦ ﬂip (σ2, τ2)
If (σ, τ) is a kite patterned on sd k I2 for some k, then the effect of ﬂipping is:
(7.3.2) [∂ ﬂip (σ, τ)] = [ ∂(σ, τ)]−1
in π1(sk1 sdk I2).
NONABELIAN MULTIPLICATIVE INTEGRATION 95
Lemma 7.3.3. Let (σ, τ) be a kite in (I2, v0), and let k≥ 0. Then
(7.3.4) MI
(
α, β| ﬂip (σ, τ)
)
=
1
∏
i=4k
MI
(
α, β| ﬂip ((σ, τ)◦ (σk
i , τk
i ))
)
.
Note that the order of the product is reversed!
Proof. By moving the base point from v0 to x0 := τ(v0) along the string σ, and
using Theorem 5.4.8, we now have to prove that (7.3.4) holds for a kite (σ, τ) in
the pointed polyhedron (I2, x0), and moreover σ is the empty string. Next we
use Proposition 4.5.3 for the map of pointed polyhedra τ : (I2, v0)→ (I2, x0) to
reduce to proving (7.3.4) for (σ, τ) = ( σ0
1 , τ0
1 ), the basic kite in (I2, v0).
So we have to prove that
(7.3.5) MI
(
α, β| ﬂip (σ0
1 , τ0
1 )
)
=
1
∏
i=4k
MI
(
α, β| ﬂip (σk
i , τk
i )
)
.
holds.
For any i∈{ 1, . . . , 4k} deﬁne
(σ♮
i , τ♮
i ) := ﬂip (σ0
1 , τ0
1 )◦ (σk
i , τk
i ).
Then
ρ♮ :=
(
(σ♮
1, τ♮
1 ), . . . ,(σ♮
4k, τ♮
4k )
)
is a generating sequence for sd k I2. By Proposition 4.5.1 we know that
(7.3.6) MI
(
α, β| ﬂip (σ0
1 , τ0
1 )
)
=
4k
∏
i=1
h♮
i ,
where h♮
i are as in Lemma 7.2.4. And it is clear from Deﬁnition 4.2.2(2) and
formula (7.3.2) that
(7.3.7)
4k
∏
i=1
a♮
i = [ ∂I2]−1,
where a♮
i are as in Deﬁnition 7.2.1.
Consider another sequence of kites
ρ :=
(
(σ1, τ1), . . . ,(σ4k, τ4k )
)
,
where we deﬁne
(σi, τi) := ﬂip (σk
i , τk
i ).
It is not hard to show, by induction on k, that these kites are aligned with the
generating sequence ρ♮. Let ai and hi be as in Lemma 7.2.6, where we take
m := 4k of course. Again by induction on k one shows that
1
∏
i=4k
ai = [ ∂I2]−1.
Combining this with (7.3.7) we deduce
a4k··· a2· a1· (a♮
4k )−1··· (a♮
2)−1· (a♮
1)−1 = 1
in π1(sk1 sdk I2). Now Lemma 7.2.6 says that
h4k··· h2· h1· (h♮
4k )−1··· (h♮
2)−1· (h♮
1)−1 = 1
96 AMNON YEKUTIELI
in H. Using (7.3.6) we get
1
∏
i=4k
hi = MI
(
α, β| ﬂip (σ0
1 , τ0
1 )
)
.
This is precisely (7.3.5). □
Deﬁnition 7.3.8. In this section, a kite (σ, τ) in (I2, v0) will be called (α, β)-tiny if
it is a square kite, len (σ)≤ 5, and
side(τ) < min
(
ϵ4(α, β), ϵ5(α, Ψh)
)
.
See Lemma 6.1.3 and Proposition 3.5.13 regarding the constants ϵ4(α, β) and
ϵ5(α, Ψh).
Lemma 7.3.9. Let (σ, τ) be a kite in (I2, v0). Then
(7.3.10) MI
(
α, β| ﬂip (σ, τ)
)
= MI(α, β| σ, τ)−1.
Proof. Step 1. Assume (σ, τ) is (α, β)-tiny and β|τ(I2) is smooth. We may assume
that ϵ := side(τ) is positive (since the case ϵ = 0 is trivial).
Since the ﬂip reverses the orientation, it follows that
RP0
(
α, β| ﬂip (σ, τ)
)
= RP0(α, β| σ, τ)−1;
cf. Deﬁnition 4.3.3. Next, by applying Proposition 4.5.2 to both (σ, τ) and
ﬂip (σ, τ), we have
(7.3.11)‖‖ logH
(
MI
(
α, β| ﬂip (σ, τ)
))
− logH
(
MI(α, β| σ, τ)−1)‖‖≤ 2· c2(α, β)· ϵ4 .
Step 2. Again we assume that (σ, τ) is (α, β)-tiny and ϵ := side(τ) is positive; but
we do not assume smoothness.
Take k≥ 0. For each index i∈{ 1, . . . , 4k} we let
(σi, τi) := ( σ, τ)◦ (σk
i , τk
i ) = tesk
i (σ, τ).
Note that side (τi) = ( 1
2 )k· ϵ. The subsets good (τ, k) and bad(τ, k) of{1, . . . , 4k}
were deﬁned in Deﬁnition 4.4.12. According to Lemma 4.4.13, there are constants
aj := aj(α, β, τ(I2))
such that
|bad(τ, k)|≤ a0 + a1· 2k .
If i is a good index, then by step 1 we know that
‖‖ logH
(
MI(α, β| ﬂip (σi, τi))
)
− logH
(
MI(α, β| σi, τi)−1)‖‖
≤ 2· c2(α, β)· ( 1
2 )4k· ϵ4 .
And if i is a bad index, then by Proposition 4.5.2(1) we have
(7.3.12)
‖‖ logH
(
MI(α, β| ﬂip (σi, τi))
)
− logH
(
MI(α, β| σi, τi)−1)‖‖
≤ 2· c1(α, β)· ( 1
2 )2k· ϵ2 .
NONABELIAN MULTIPLICATIVE INTEGRATION 97
The conditions in property (ii) of Theorem 2.1.2 are satisﬁed. Hence, using
Lemma 7.3.3 and Proposition 4.5.1, we obtain these estimates:
‖‖ logH
(
MI(α, β| ﬂip (σ, τ))
)
− logH
(
MI(α, β| σ, τ)−1)‖‖
=
‖‖ logH
( 1
∏
i=4k
MI(α, β| ﬂip (σi, τi))
)
− logH
( 1
∏
i=4k
MI(α, β| σi, τi)−1
)‖‖
≤| good(τ, k)|· 2· c2(α, β)· ( 1
2 )4k· ϵ4
+|bad(τ, k)|· 2· c1(α, β)· ( 1
2 )2k· ϵ2
≤ 4k· 2· c2(α, β)· ( 1
2 )4k· ϵ4 + (a0 + a1· 2k)· 2· c1(α, β)· ( 1
2 )2k· ϵ2 .
As k→ ∞ the last term goes to 0. Hence (7.3.10) holds in this case.
Step 3. Now (σ, τ) is an arbitrary kite in (I2, v0). We may assume that τ(I2) is
2-dimensional, for otherwise things are trivial. As done in the beginning of the
proof of Lemma 7.3.3, we can modify the setup so that (σ, τ) is a square kite and
len(σ)≤ 1. Take k large enough so that all the kites
(σi, τi) := ( σ, τ)◦ (σk
i , τk
i ),
i∈{ 1, . . . , 4k}, are (α, β)-tiny. By Step 2 we know that
MI
(
α, β| ﬂip (σi, τi)
)
= MI(α, β| σi, τi)−1
holds for all i. Hence, using Lemma 7.3.3 and Proposition 4.5.1, we conclude that
MI(α, β| ﬂip (σ, τ)) =
1
∏
i=4k
MI(α, β| ﬂip (σi, τi))
=
1
∏
i=4k
MI(α, β| σi, τi)−1 =
( 4k
∏
i=1
MI(α, β| σi, τi)
)−1
= MI(α, β| σ, τ)−1.
□
7.4. The T urn. The (counterclockwise) turn of I2 is the linear automorphism
turn : I2→ I2 deﬁned on vertices by
turn(v0, v1, v2) := (v1, (1, 1), v0).
The turn of the basic kite (σ0
1 , τ0
1 ) is
turn(σ0
1 , τ0
1 ) :=
(
(v0, v1), turn
)
.
Given any kite (σ, τ) in (I2, v0), its turn is the kite
turn(σ, τ) := ( σ, τ)◦ turn(σ0
1 , τ0
1 ).
See ﬁgure 29.
Observe that for kites (σ1, τ1) and (σ2, τ2) in (I2, v0), one has
(7.4.1) turn
(
(σ1, τ1)◦ (σ2, τ2)
)
= ( σ1, τ1)◦ turn(σ2, τ2).
If (σ, τ) is patterned on sd k I2, then the boundaries satisfy
(7.4.2) [∂ turn(σ, τ)] = [( σ, τ)]
98 AMNON YEKUTIELI
Figure 29. A kite (σ, τ) in (I2, v0), and the kite turn (σ, τ).
in π1(sk1 sdk I2).
Lemma 7.4.3. Let (σ, τ) be a kite in (I2, v0), and let k≥ 0. Then
MI
(
α, β| turn(σ, τ)
)
=
4k
∏
i=1
MI
(
α, β| turn((σ, τ)◦ (σk
i , τk
i ))
)
.
Proof. The proof is very similar to that of Lemma 7.3.3. As we showed there, it
sufﬁces to consider the case (σ, τ) = ( σ0
1 , τ0
1 ). So we have to prove
(7.4.4) MI
(
α, β| turn(σ0
1 , τ0
1 )
)
=
4k
∏
i=1
MI
(
α, β| turn(σk
i , τk
i )
)
.
For any i∈{ 1, . . . , 4k} let
(σ♮
i , τ♮
i ) := turn(σ0
1 , τ0
1 )◦ (σk
i , τk
i ).
The sequence
ρ♮ :=
(
(σ♮
1, τ♮
1 ), . . . ,(σ♮
4k, τ♮
4k )
)
is a generating sequence of kites for sd k I2. Deﬁne elements a♮
i and h♮
i as in Def-
inition 7.2.1 and Lemma 7.2.4, with respect to the this new generating sequence
ρ♮. By Proposition 4.5.1 we know that
(7.4.5) MI
(
α, β| turn(σ0
1 , τ0
1 )
)
=
4k
∏
i=1
h♮
i .
And by induction on k it is not hard to see that
(7.4.6)
4k
∏
i=1
a♮
i = [ ∂I2].
Next consider the sequence of kites
ρ :=
(
(σ1, τ1), . . . ,(σ4k, τ4k )
)
,
where
(σi, τi) := turn(σk
i , τk
i ).
These kites are all aligned with ρ♮. Take ai and hi deﬁned as in Lemma 7.2.6. We
then have
4k
∏
i=1
ai = [ ∂I2].
NONABELIAN MULTIPLICATIVE INTEGRATION 99
Applying Lemma 7.2.6 we conclude that
4k
∏
i=1
hi =
4k
∏
i=1
h♮
i .
Combining this equation with (7.4.5) we can deduce that equation (7.4.4) is true.
□
Lemma 7.4.7. Let (σ, τ) be a kite in (I2, v0). Then
(7.4.8) MI
(
α, β| turn(σ, τ)
)
= MI(α, β| σ, τ).
Proof. The proof is organized like that of Lemma 7.3.9, so we allow ourselves to
be less detailed.
Step 1. Here we assume that (σ, τ) is an (α, β)-tiny kite, the number ϵ := side(τ)
is positive, and β|τ(I2) is smooth. Going back to Deﬁnition 4.3.3, and using its
notation mixed with the present notation, we have
RP0(α, β| σ, τ) = expH
(
ϵ2· Ψh(g)( ˜β(z))
)
.
Recall that
g = MI
(
α| σ∗ (τ◦ σpr)
)
.
The turn does not change the area of the square Z = τ(I2), nor its midpoint z;
it only changes the string that leads from v0 to z. Indeed, the string that is related
to turn(σ, τ) is σ∗ (τ◦ ρ′), where ρ′ is the string
ρ′ := (v0, v1)∗ (v1, y)∗ (y, w),
in I2 with y := ( 1
2, 1) and w := ( 1
2, 1
2 ). The formula for the Riemann product is
RP0(α, β| turn(σ, τ)) = expH
(
ϵ2· Ψh(g′)( ˜β(z))
)
,
with
g′ := MI
(
α| σ∗ (τ◦ ρ′)
)
.
Let ρ′′ := σ−1
pr ∗ ρ′, which is a closed string based at w. The group element
g′′ := MI(α| τ◦ ρ′′)
satisﬁes g′ = g· g′′. Since len (τ◦ ρ′′) = 3ϵ, we know by Proposition 3.5.13 that
‖‖ Ψh(g′′)− 1
‖‖≤ c5(α, Ψh)· 3ϵ .
But by Proposition 3.5.10 we have
‖Ψh(g)‖≤ exp
(
c4(α, Ψh)· 5
)
.
Therefore ‖‖ logH
(
RP0(α, β| turn(σ, τ))
)
− logH
(
RP0(α, β| σ, τ)
)‖‖
= ϵ2·
(
Ψh(g)◦ (Ψh(g′′)− 1)
)
( ˜β(z))
≤ ϵ3· c ,
where we write
c := exp
(
c4(α, Ψh)· 5
)
· 3· c5(α, Ψh)·‖ β‖Sob .
Combining this estimate with Proposition 4.5.2(2), we obtain
(7.4.9)
‖‖ logH
(
MI(α, β| turn(σ, τ))
)
− logH
(
MI(α, β| σ, τ)
)‖‖
≤ 2· c2(α, β)· ϵ4 + c· ϵ3 .
100 AMNON YEKUTIELI
Step 2. In this step we assume that (σ, τ) is an (α, β)-tiny kite and ϵ := side(τ) is
positive; but no smoothness is assumed.
Take k≥ 0, and deﬁne kites (σi, τi) and sets good (τ, k) and bad (τ, k) like in
step 2 of the proof of Lemma 7.3.9. If i∈ good(τ, k) then by equation (7.4.9) in
step 1 we know that
‖‖ logH
(
MI(α, β| turn(σi, τi))
)
− logH
(
MI(α, β| σi, τi)
)‖‖
≤ 2· c2(α, β)· ( 1
2 )4k· ϵ4 + c· ( 1
2 )3k· ϵ3 .
For i∈ bad(τ, k) we use the estimate (7.3.12). As in the proof of Lemma 7.3.9, but
using Lemma 7.4.3 instead of Lemma 7.3.3, we arrive at the estimate
‖‖ logH
(
MI(α, β| turn(σ, τ))
)
− logH
(
MI(α, β| σ, τ)
)‖‖
=
‖‖ logH
( 4k
∏
i=1
MI(α, β| turn(σi, τi))
)
− logH
( 4k
∏
i=1
MI(α, β| σi, τi)
)‖‖
≤| good(τ, k)|·
(
2· c2(α, β)· ( 1
2 )4k· ϵ4 + c· ( 1
2 )3k· ϵ3)
+|bad(τ, k)|·
(
2· c1(α, β)· ( 1
2 )2k· ϵ2)
≤ 4k·
(
2· c2(α, β)· ( 1
2 )4k· ϵ4 + c· ( 1
2 )3k· ϵ3)
+ (a0 + a1· 2k)·
(
2· c1(α, β)· ( 1
2 )2k· ϵ2)
.
As k→ ∞ the last term goes to 0. Hence (7.4.8) holds in this case.
Step 3. For an arbitrary kite (σ, τ) in (I2, v0) we prove that (7.4.8) holds using
step 2, as was done in step 3 of the proof of Lemma 7.3.9, but using Lemma 7.4.3
instead of Lemma 7.3.3. □
7.5. Putting it all Together.
Theorem 7.5.1. Let
C/I2 = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module over (X, x0) := ( I2, v0), let (α, β) be a connection-
curvature pair in C/I2, and let
ρ =
(
(σ1, τ1), . . . , (σm, τm)
)
be a sequence of kites in (I2, v0) patterned on sdk I2, for some k∈ N. For i∈{ 1, . . . ,m}
deﬁne
ai := [ ∂(σi, τi)]∈ π1(sk1 sdk I2)
and
hi := MI(α, β| σi, τi)∈ H.
Suppose
w(s)∈ Wrd±1(s) = Wrd±1(s1, . . . ,sm)
is a word such that
w(a1, . . . ,am) = 1
in π1(sk1 sdk I2). Then
w(h1, . . . ,hm) = 1
in H.
NONABELIAN MULTIPLICATIVE INTEGRATION 101
Proof. We can ﬁnd li∈{ 0, 1} and ji∈{ 0, 1, 2, 3}, such that the kites
(σ′
i , τ′
i ) := ﬂip li
(
turnji (σi, τi)
)
are aligned with the generating sequence tes k I2. Here the exponents li and ji
refer to iteration of the corresponding operation. Let ei := (−1)li,
a′
i := [ ∂(σ′
i , τ′
i )]∈ π1(sk1 sdk I2)
and
h′
i := MI(α, β| σ′
i , τ′
i )∈ H.
Then aei
i = a′
i, and by Lemmas 7.3.9 and 7.4.7 we also have hei
i = h′
i.
Consider the word
u(s) := w
(
se1
1 , . . . ,sem
m
)
∈ Wrd±1(s).
Then
w(a1, . . . ,am) = u(a′
1, . . . ,a′
m)
and
w(h1, . . . ,hm) = u(h′
1, . . . ,h′
m).
Now we can ﬁnish the proof with the use of Lemma 7.2.6. □
Corollary 7.5.2. Let
C/I2 = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module over (X, x0) := ( I2, v0), let (α, β) be a connection-
curvature pair in C/I2, and let
ρ =
(
(σ1, τ1), . . . , (σ4k, τ4k )
)
be a tessellation of I2 patterned on sdk I2 (cf. Deﬁnition 4.2.2). Then
4k
∏
i=1
MI(α, β| σi, τi) = MI(α, β| I2).
Proof. This is an immediate consequence of the theorem, taking m := 4k + 1,
w(s) :=
(
∏
m−1
i=1 si
)
· s−1
m
and (σm, τm) the basic kite. □
NONABELIAN MULTIPLICATIVE INTEGRATION 103
Figure 30. A cubical balloon (σ, τ) in the pointed polyhedron (I3, v0).
8. S tokes Theorem in Dimension Three
The goal of this section is to prove Theorem 8.6.6, which is the ﬁrst version
of the main result of the paper. (The second version, dealing with the triangular
case, is Theorem 9.3.5.)
8.1. Balloons and their Boundaries.
Deﬁnition 8.1.1. Let (X, x0) be a pointed polyhedron. A linear quadrangular bal-
loon in (X, x0) is a pair (σ, τ), where σ is a string in X (see Deﬁnition 3.5.1), and
τ : I3→ X is a linear map. The conditions are that σ(v0) = x0 and σ(v1) = τ(v0).
In other words, a linear quadrangular balloon is the 3-dimensional version of
a linear quadrangular kite. See Figure 30 for an illustration.
All balloons in this section are linear quadrangular ones; so we shall simply
call them balloons. (This will change in Section 9.) If the image of τ is a cube in
X, then we call (σ, τ) a cubical balloon. The length of the side of τ is denoted by
side(τ). If side (τ) > 0 then (σ, τ) is said to be nondegenerate.
If (σ, τ) is a balloon in (X, x0), and (σ′, τ′) is a balloon (resp. a kite) in (I3, v0),
then the composition (σ, τ)◦ (σ′, τ′) (deﬁned like (4.1.2)) is a balloon (resp. a kite)
in (X, x0).
The k-th binary subdivision of I3 is its cellular decomposition into 8 k little
cubes, each of side ( 1
2 )k. We denote this decomposition by sd k I3.
A map σ : Ip→ I3 is said to be patterned on sdk I3 if it is linear, and its image
is a p-cell in sd k I3. A string σ = ( σ1, . . . ,σn) in (I3, v0) is said to be patterned
on sd k I3 if for every i the map σi : I1 → I3 is patterned on sd k I3. A kite or
balloon (σ, τ) in (I3, v0) is said to be patterned on sd k I3 if the string σ and the
map τ : Ip→ I3 (p = 2, 3) are patterned on sd k I3.
The k-th binary tessellation of I3 is the sequence
(8.1.2) tes k I3 =
(
tesk
1 I3, . . . , tesk
8k I3)
=
(
(σk
1, τk
1 ), . . . ,(σk
8k, τk
8k )
)
of balloons patterned on sd k I3, deﬁned as follows. For k = 0 we have the basic
balloon (σ0
1 , τ0
1 ), where σ0
1 is the empty string, and τ0
1 : I3→ I3 is the identity
map.
104 AMNON YEKUTIELI
For k = 1 we choose, once and for all, a sequence
tes1 I3 =
(
(σ1
1 , τ1
1 ), . . . ,(σ1
8 , τ1
8 )
)
balloons patterned on sd 1 I3, satisfying these conditions:
(a) Each of the 3-cells of sd 1 I3 occurs exactly once as τ1
i (I3) for some i.
(b) The maps τ1
i are positively oriented.
(c) The length of each string σ1
i is at most 3.
This can be done of course.
For k≥ 1 we use the recursive deﬁnition
tesk+1 I3 := (tes1 I3)◦ (tesk I3).
Here we use the convention (3.1.1) for composition of sequences.
Given a balloon (σ, τ) in a pointed polyhedron (X, x0), an numbers k∈ N,
i∈{ 1, . . . , 8k}, let
(8.1.3) tes k
i (σ, τ) := ( σ, τ)◦ tesk
i I3 = ( σ, τ)◦ (σk
i , τk
i ).
The k-th binary tessellation of (σ, τ) is the sequence (of length 8 k) of balloons
(8.1.4) tes k(σ, τ) := ( σ, τ)◦ (tesk I3) =
(
tesk
1(σ, τ), . . . , tesk
8k (σ, τ)
)
.
NONABELIAN MULTIPLICATIVE INTEGRATION 105
Figure 31. The kites (σ♭
i , τ♭
i ), i = 1, . . . , 6, that make up the
boundary of I3.
Deﬁnition 8.1.5.
(1) For i∈{ 1, . . . , 6} let ∂iI3 := ( σ♭
i , τ♭
i ) be the kites depicted in Figure 31.
The boundary of I3 is the sequence of kites
∂I3 =
(
∂1I3, . . . ,∂6I3)
=
(
(σ♭
1, τ♭
1 ), . . . ,(σ♭
6, τ♭
6 )
)
.
(2) Given a balloon (σ, τ) in a pointed polyhedron (X, x0), let
∂i(σ, τ) := ( σ, τ)◦ ∂iI3 = ( σ, τ)◦ (σ♭
i , τ♭
i ).
The boundary of (σ, τ) is the sequence of kites
∂(σ, τ) :=
(
∂1(σ, τ), . . . ,∂6(σ, τ)
)
in (X, x0).
If (σ, τ) is a balloon in (I3, v0) patterned on sdk I3, then ∂(σ, τ) is a sequence (of
length 6) of kites patterned on sd k I3, and ∂∂(σ, τ) is a sequence of closed strings
patterned on sd k I3.
Deﬁnition 8.1.6. Let (X, x0) be a pointed polyhedron, let C/X be a Lie quasi
crossed module with additive feedback over (X, x0), and let (α, β) be a piecewise
smooth connection-curvature pair in C/X. Given a balloon (σ, τ) in (X, x0), we
106 AMNON YEKUTIELI
deﬁne
MI(α, β| ∂(σ, τ)) :=
6
∏
1=1
MI(α, β| ∂i(σ, τ))∈ H.
8.2. Some Algebraic Topology. Let us denote by π1(sk1 sdk I3) the fundamental
group of the topological space sk 1 sdk I3, based at v0. If σ is a closed string
patterned on sd k I3 and based at v0, then we denote its class in π1(sk1 sdk I3) by
[σ].
We now look at homology groups. Fix k≥ 0. On each p-cell τ in sd k I3, p∈
{0, 1, 2}, let us choose an orientation (there are two options for p > 0). We denote
by C p(sk2 sdk I3) the free abelian group based on these oriented cells, called the
group of p-chains. The direct sum on all p is a complex (with the usual boundary
operator), and the p-th homology is the singular homology H p(sk2 sdk I3) of the
topological space sk 2 sdk I3. The homology class of a cycle ∑i niτi is denoted by
[∑i niτi]. Observe that a string σ = ( σ1, . . . ,σn) patterned on sd k I3 represents an
element ∑i σi∈ C1(sk2 sdk I3). And a linear map τ : I2→ I3 patterned on sd k I3
represents an element τ∈ C2(sk2 sdk I3).
Recall the free monoid with involution Wrd±1(s) from Subsection 7.1.
Lemma 8.2.1. Let
(
(σ1, τ1), . . . ,(σn, τn)
)
be a sequence of kites patterned on sk2 sdk I3,
for some k≥ 0. Write
ai := [ ∂(σi, τi)]∈ π1(sk1 sdk I3).
Let w(s)∈ Wrd±1(s1, . . . ,sn) be a word such that w (a1, . . . ,an) = 1. Then the 2-chain
w(τ1, . . . ,τn)∈ C2(sk2 sdk I3)
is a cycle.
Proof. Say m is the number of 1-cells in sd k I3. We choose orientations, and ar-
range these oriented 1-cells in a sequence (ρ1, . . . ,ρm). For every i let ui(t)∈
Wrd±1(t1, . . . ,tm) be the word such that
∂(σi, τi) = ui(ρ1, . . . ,ρm)
as strings patterned on sd k I3. Deﬁne
u(t) := w(u1(t), . . . ,un(t))∈ Wrd±1(t).
Then u(ρ1, . . . ,ρm) is a closed string, and its homotopy class is trivial in the group
π1(sk1 sdk I3). According to Lemma 7.1.2 we have u(t)∼can 1 in Wrd±1(t).
On the other hand we have∂(τi) = ∂(σi, τi) as additive 1-chains, i.e. as elements
of C1(sk2 sdk I3). Hence
∂(w(τ1, . . . ,τn)) = w(∂(σ1, τ1), . . . ,∂(σn, τn)) = u(ρ1, . . . ,ρm) = 0
as elements of C 2(sk2 sdk I3). □
Lemma 8.2.2. Recall the boundary of I3 from Deﬁnition 8.1.5. For any i let
a♭
i := [ ∂(σ♭
i , τ♭
i )]∈ π1(sk1 sd0 I3)
and
b♭
i := τ♭
i ∈ C2(sk1 sd0 I3).
Then:
NONABELIAN MULTIPLICATIVE INTEGRATION 107
(1) The fundamental group π1(sk1 sd0 I3) is generated by the sequence of elements
(a♭
1, . . . ,a♭
6), and there is one relation:
∏
i=1,...,6
a♭
i = 1.
Thus π1(sk1 sd0 I3) is a free group of rank 5.
(2) The homology group H2(sk2 sd0 I3) is a free abelian group of rank 1, with basis
[∑i=1,...,6 τi].
Proof. This is obvious from looking at the pictures. □
Given a balloon (σ, τ), its boundary ∂(σ, τ) is a sequence of 6 kites, and ∂∂(σ, τ)
is a sequence of 6 closed strings.
Lemma 8.2.3.
(1) The fundamental group π1(sk1 sd1 I3) is generated by the
sequence of closed strings
∂∂(tes1 I3) =
(
∂∂(σk
1, τk
1 ), . . . ,∂∂(σk
8k, τk
8k )
)
.
This sequence has length 48. There are 20 relations, and they are of two kinds:
(a) For any two distinct kites (σi, τi), (σj, τj) in ∂∂(tes1 I3) such that τi(I2) =
τj(I2), namely for any of the 12 interior faces of sd1 I3, there is a relation
[∂(σi, τi)] = [ gi]· [∂(σj, τj)−1]· [g−1
i ]
for some word g i in the 48 generators.
(b) For any of the 8 balloons (σk
i , τk
i ) in tes1 I3 there is a relation as in Lemma
8.2.2(1).
Thus π1(sk1 sd1 I3) is a free group of rank 28.
(2) The homology group H2(sk2 sd1 I3) is a free abelian group of rank 8, with basis
the 8 boundaries of the 8 balloons in tes1 I3.
Proof. Use Lemma 8.2.2 together with the Van-Campen and Mayer-
Vietoris theorems. □
8.3. Inert Forms. Let (X, x0) be a pointed polyhedron, and let
C/X = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module with additive feedback over (X, x0). Recall that
the additive feedback ΦX is an element ofOpws(X)⊗ Hom(h, g), so for any point
x∈ X we have a linear function ΦX(x) : h→ g.
Suppose Z⊂ X is some sub-polyhedron. As in equation (4.6.4), but restricting
to Z, for every p we have anOpws(Z)-linear homomorphism
ΦX|Z : Ωp
pws(Z)⊗ h→ Ωp
pws(Z)⊗ g.
Note that for p = 0, an element
f∈ Ω0
pws(Z)⊗ h =Opws(Z)⊗ h
is a piecewise smooth function f : Z→ h; and in this case
ΦX|Z( f )(z) = ΦX(z)( f (z))∈ g
for any point z∈ Z.
Deﬁnition 8.3.1. Let Z⊂ X be a subpolyhedron.
108 AMNON YEKUTIELI
(1) A function f∈O pws(Z)⊗ h is called an inert function (relative to C/X) if
ΦX|Z( f ) = 0.
(2) A form γ ∈ Ωp
pws(Z)⊗ h is called an inert p-form (relative to C/X) if
ΦX|Z(γ) = 0.
Let γ∈ Ωp
pws(X)⊗ h. Choose some linear coordinate system s = (s1, . . . ,sn) on
X. Also choose a smoothing triangulation{Xj}j∈J for γ; so that γ|Xj∈ Ωp(Xj)⊗ h
for every j. See Subsection 1.6 for details. For each index j let fj,i∈O (Xj)⊗ h be
the coefﬁcients of γ|Xj relative to s, in the sense of Deﬁnition 1.3.4. Namely
(8.3.2) γ|Xj = ∑
i
fj,i· dsi1∧···∧ dsip∈ Ωp(Xj)⊗ h,
where i = ( i1, . . . ,ip) runs over the set of strictly increasing multi-indices in
{1, . . . ,n}p.
Lemma 8.3.3. In the situation above, the following are equivalent:
(i) The form γ∈ Ωp
pws(X)⊗ h is inert.
(iii) The functions f j,i∈O (Xj)⊗ h are all inert.
We omit the easy proof.
Deﬁnition 8.3.4. The closed subgroup
H0 := Ker(Φ0)⊂ H
is called the inertia subgroup (relative to C/X). Its Lie algebra
h0 := Lie(H0) = Ker(Lie(Φ0))
is called the inertia subalgebra.
Proposition 8.3.5. The subgroup H0 is central in H, and the subalgebra h0 is central in
h.
Proof. Take h∈ H0, so Φ0(h) = 1. By the Pfeiffer condition (i.e. condition ( ∗) of
Deﬁnition 5.1.1) we have
AdH(h) = Ψ(Φ0(h)) = Ψ(1) = idH,
which says that
h∈ Ker(AdH) = Z(H).
Since H0⊂ Z(H) it follows that
h0⊂ Lie(Z(H))⊂ Z(h).
(Note that H could be disconnected, in which case Z (h) could be bigger than
Lie(Z(H)).) □
Recall the notion of tame connection (Deﬁnition 5.3.4).
Lemma 8.3.6. Let α be a tame connection for C/X, let σ be a closed string in X based
at x0, and let g := MI(α| σ)∈ G. Then for any λ∈ h0 one has
Ψh(g)(λ) = λ.
Proof. Let m be the number of pieces in σ, and choose k large enough such that
m≤ 2k+2. We may append to σ a few copies of the constant map x0 at its end, so
that now σ has exactly 2k+2 pieces. The group element g is unchanged.
Denote by σ′ the closed string in I2 which is “k-th subdivision” of the boundary
∂I2, based at v0; so σ′ has 2k+2 = 4· 2k pieces. We can construct a piecewise linear
NONABELIAN MULTIPLICATIVE INTEGRATION 109
map f : I2→ X such that f (v0) = x0, and f◦ σ′ = ρ as strings. According to
Propositions 3.5.9 and 3.3.22(3) we have
g = MI( f∗(α)| σ′) = MI( f∗(α)| ∂I2).
Let β ∈ Ω2
pws(X)⊗ h be such that (α, β) is a connection-curvature pair for
C/X. By Proposition 5.3.3 the pair ( f∗(α), f∗(β)) is a connection-curvature pair
in f∗(C/X). Hence by Theorem 6.2.1 we have g = Φ0(h), where
h := MI( f∗(α), f∗(β)| I2)∈ H.
Since λ∈ Lie(Z(H)) it follows that
Ψh(g)(λ) = Ψh(Φ0(h))(λ) = Adh(h)(λ) = λ.
□
Remark 8.3.7. The lemma above shows that the holonomy group of a tame con-
nection α at x0 acts trivially on the inertia subalgebra h0. Hence the names.
Lemma 8.3.8. Let C/X be a Lie quasi crossed module with additive feedback over
(X, x0), let α be a tame connection for C/X, and let Z⊂ X be a subpolyhedron.
(1) Let f ∈O pws(Z)⊗ h be an inert function relative to C/X. Then there is a
unique function
Ψh,α( f ) : Z→ h0
such that the following condition holds:
(∗) Let σ be a string in X, with initial point x0 and terminal point z := σ(v1)∈
Z, and let g := MI(α| σ)∈ G. Then
Ψh,α( f )(z) = Ψh(g)( f (z)).
(2) The operation Ψh,α is linear over the ringOpws(Z).
(3) The function Ψh,α( f ) is continuous.
Proof. Take a point z∈ Z. Choose any string σ connecting x0 to z, and let
λ := Ψh(g)( f (z))∈ h
as in condition (∗). Since α is a compatible connection (see Deﬁnition 5.2.4), and
since f is inert, we know that
Lie(Φ0)(λ) = ΦX(x0)(λ) = Adg(g)(ΦX(z)( f (z))) = 0.
This shows that λ∈ h0.
If we were to choose another stringσ′ with the same initial and terminal points,
then for g′ := MI(α| σ′) we would have
(Ψh(g′)◦ Ψh(g)−1)(λ) = λ,
this according to Lemma 8.3.6. Hence λ = Ψh(g′)( f (z)). We see that λ is inde-
pendent of the string σ, and we can deﬁne Ψh,α( f )(z) := λ. We obtain a function
Ψh,α( f ) : Z→ h0. This proves part (1).
Part (2) is true because the operator Ψh(g) : h→ h is linear.
It remains to prove part (3). We need to prove that the function
Ψh,α( f ) : Z → h0 is continuous. So let’s ﬁx a point z0 ∈ Z, and a string σ
starting at x0 and ending at z0. Let g := MI(α| σ). For any point z ∈ Z let
σz : I1→ Z be the unique linear map with initial point z0 and terminal point z,
and let gz := MI(α| σz). So
Ψh,α( f )(z) = Ψh(g· gz)( f (z)) = ( Ψh(g)◦ Ψh(gz))( f (z)).
110 AMNON YEKUTIELI
But according to Proposition 3.5.13 we know thatΨh(gz)→ 1∈ End(h) as z→ z0;
and f (z)→ f (z0) by continuity of f . Therefore
Ψh,α( f )(z)→ Ψh,α( f )(z0)
as z→ z0. □
To summarize, the lemma says that there is anOpws(Z)-linear homomorphism
(8.3.9) Ψh,α :{inert functions on Z}→O cont(Z)⊗ h0,
whereOcont(Z) is the ring of continuous functions Z→ R.
Recall the module Ωp
pwc(X) of piecewise continuous differential forms, from
Subsection 1.9.
Proposition 8.3.10. Let α be a tame connection, and let γ∈ Ωp
pws(X)⊗ h be an inert
form. Then there is a unique piecewise continuous form
Ψh,α(γ)∈ Ωp
pwc(X)⊗ h0
with the following property:
(∗) Choose a linear coordinate system s = ( s1, . . . ,sn) on X, and a smoothing tri-
angulation{Xj}j∈J for γ. Let f j,i∈O (Xj)⊗ h be the coefﬁcients of γ|Xj, as in
(8.3.2). Then
Ψh,α(γ)|Xj = ∑
i
Ψh,α( fj,i)· dsi1∧···∧ dsip.
Note that by Lemma 8.3.3 the functions fj,i are inert, so the continuous func-
tions Ψh,α( fj,i)∈O cont(Xj) are deﬁned.
Proof. This is immediate from the uniqueness of the coefﬁcients fj,i, and the prop-
erties of the homomorphism Ψh,α listed in Lemma 8.3.8. □
Remark 8.3.11. Actually a lot more can be said here. Presumably, one can show
that
Ker(ΦX)⊂O pws(X)⊗ h
is the set of piecewise smooth sections of a piecewise smooth vector bundleE over
X, which is a sub-bundle of the trivial vector bundle X× h. And the operation
Ψh,α corresponds to a piecewise smooth isomorphism of vector bundles
E ≃− →X× h0.
If so, then it would follow that for any inert form γ∈ Ωp
pws(Z)⊗ h, the form
Ψh,α(γ) is actually piecewise smooth (not just piecewise continuous). And we
would have anOpws(X)-linear bijection
Ψh,α :{inert p-forms on Z}→ Ωp
pws(Z)⊗ h0.
However we did not verify these assertions.
Suppose we are given a piecewise continuous form δ∈ Ωp
pwc(X)⊗ h and a
piecewise linear map τ : Ip→ X. Extending the formula (1.9.7) linearly to h0-
valued forms we obtain
∫
τ δ∈ h0.
Deﬁnition 8.3.12 (Integration of Inert Forms) . Let C/X be a Lie quasi crossed
module with additive feedback over (X, x0). Given a tame connection α, an inert
form γ∈ Ωp
pws(X)⊗ h and a piecewise linear map τ : Ip→ X, we deﬁne the
twisted multiplicative integral
MI(α, γ| τ)∈ H0
NONABELIAN MULTIPLICATIVE INTEGRATION 111
as follows:
MI(α, γ| τ) := expH
(∫
τ
Ψh,α(γ)
)
.
Proposition 8.3.13. Let f : Y→ X and τ : Ip→ Y be piecewise linear maps between
polyhedra, let α∈ Ω1
pws(X)⊗ g be a tame connection, and let γ∈ Ωp
pws(X)⊗ h be an
inert form. Then f ∗(α)∈ Ω1
pws(Y)⊗ g is a tame connection, f ∗(γ)∈ Ωp
pws(Y)⊗ h is
an inert form, and
MI(α, γ| f◦ τ) = MI
(
f∗(α), f∗(γ)| τ
)
.
Proof. The connection f∗(α) is tame for f∗(C/X) by Corollary 5.3.5. It is easy to
see directly from the deﬁnitions that f∗(γ) is inert, and moreover
Ψh, f∗(α)( f∗(γ)) = f∗(Ψh,α(γ))∈ Ωp
pwc(Y)⊗ h.
And Integration of piecewise continuous forms commutes with pullbacks (see
Subsection 1.9). □
8.4. Combinatorics and Integration. In this subsection we work with the pointed
polyhedron (X, x0) :=
(I3, v0). We ﬁx a Lie quasi crossed module with additive feedback
C/I3 = ( G, H, Ψ, Φ0, ΦX),
and a piecewise smooth connection-curvature pair (α, β) in C/I3. Let us also ﬁx
a euclidean norm ‖−‖ on h, an open set V0(H) in H, and constants ϵ0(H) and
c0(H) as in Section 2.
Lemma 8.4.1. Let (σ, τ) be a balloon in (I3, v0). Then
MI
(
α, β| ∂(σ, τ)
)
∈ H0.
Proof. Let us write h := MI
(
α, β| ∂(σ, τ)
)
∈ H and g := MI
(
α| ∂∂(σ, τ)
)
∈ G.
According to Theorem 6.2.1 we have Φ0(h) = g.
On the other hand, consider the word w(s)∈ Wrd±1(s1, . . . ,s12) such that
∂∂I3 = w(ρ1, . . . ,ρ12),
where ρ1, . . . ,ρ12 are the oriented 1-cells of sd 0 I3. Then [w(ρ1, . . . ,ρ12)] = 1 in
π1(sk1 sd0 I3). By Lemma 7.1.2 we know that w(s)∼can 1 in Wrd±1(s). Now
writing gi := MI(α| ρi) we have g = w(g1, . . . ,g12) = 1 in the group G. We see
that h∈ Ker(Φ0) = H0. □
Lemma 8.4.2. Take k = 0, 1. Let ρ =
(
(σi, τi)
)
i=1,...,n be a sequence of kites in (I3, v0),
all patterned on sdk I3. Write
ai := [ ∂(σi, τi)]∈ π1(sk1 sdk I3)
and
hi := MI(α, β| σi, τi)∈ H.
Let w(s)∈ Wrd±1(s1, . . . ,sn) be a word such that
w(a1, . . . ,an) = 1
in π1(sk1 sdk I3) and
[w(τ1, . . . ,τn)] = 0
in H2(sk2 sdk I3). Then
w(h1, . . . ,hn) = 1
in H.
112 AMNON YEKUTIELI
Observe that by Lemma 8.2.1 the chain w(τ1, . . . ,τn) is a cycle, so we can talk
about its homology class.
Proof. First assume k = 0. Let pi∈{ 1, . . . , 6}, di∈{ 0, 1} and ei∈{ 0, 1, 2, 3} be
such that
τi = ﬂip di (turnei (τ♭
pi )).
as maps I2→ I3. Let a♭
i := [ ∂(σ♭
i , τ♭
i )] and h♭
i := MI(α, β| σ♭
i , τ♭
i ), in the notation of
Deﬁnition 8.1.5. There are words vi(t)∈ Wrd±1(t1, . . . ,t6) such that
[σi]∗ [σ♭
pi ]−1 = vi(a♭
1, . . . ,a♭
6)
in the group π1(sk1 sd0 I3). According to Corollaries 7.5.2 and 6.3.2, repeated, we
have
hi = AdH
(
vi(h♭
1, . . . ,h♭
6)
)(
(h♭
pi )(−1)di)
.
Deﬁne
ui(t) := AdWrd±1(t)(vi(t))(y(−1)di
pi )∈ Wrd±1(t)
using the conjugation operation from (7.1.1). Then hi = ui(h♭
1, . . . ,h♭
6) and ai =
ui(a♭
1, . . . ,a♭
6).
Let
u(t) := w
(
u1(t), . . . ,un(t)
)
∈ Wrd±1(t).
We know that u(a♭
1, . . . ,a♭
6) = 1 in π1(sk1 sd0 I3). Hence by Lemmas 8.2.2(1) and
7.1.2 we have
u(t)∼can AdWrd±1(t)(v(t))
(
(y1··· y6)e)
in Wrd±1(t), for some word v(t) and integer e. Passing to the abelian group
H2(sk2 sd0 I3), with additive notation, we get
e· [τ♭
1 +··· + τ♭
6 ] = [ u(τ♭
1, . . . ,τ♭
6 )] = [ w(τ1, . . . ,τn)] = 0.
Using Lemma 8.2.2(2) we conclude that e = 0, and hence u(t)∼can 1 in Wrd±1(t).
Finally, evaluating in the group H we get
w(h1, . . . ,hn) = u(h♭
1, . . . ,h♭
6) = 1.
For the case k = 1 the proof is the same, only using Lemma 8.2.3 instead of
Lemma 8.2.2, and working with the with words in the monoid Wrd±1(t1, . . . ,t48)
instead of Wrd±1(t1, . . . ,t6). □
8.5. Estimates. We continue with the setup of Subsection 8.4.
Recall the constants c2′ (α, β) and ϵ2′ (α, β) from Proposition 4.5.4.
Among other things, these numbers satisfy c2′ (α, β) ≥ 1 and 0 < ϵ2′ (α, β)
< 1.
Lemma 8.5.1. There are constants c6(α, β) and ϵ6(α, β) with these properties:
(i) c6(α, β)≥ c2′ (α, β) and
0 < ϵ6(α, β)≤ min
( 1
6· c6(α, β)−1· ϵ0(H), ϵ2′ (α, β)
)
.
(ii) Suppose (σ, τ) is a cubical balloon (I3, v0) such that side(τ) < ϵ6(α, β) and
len(σ)≤ 6. Then
MI
(
α, β| ∂(σ, τ)
)
∈ V0(H)
and ‖‖ logH
(
MI
(
α, β| ∂(σ, τ)
))‖‖≤ c6(α, β)· side(τ)3 .
NONABELIAN MULTIPLICATIVE INTEGRATION 113
Proof. The proof is basically the same as that of Lemma 6.1.2, but using Proposi-
tion 4.5.4 instead of Proposition 3.5.11. □
Suppose (σ, τ) is a nondegenerate cubical balloon in (I3, v0). Let us write
ϵ := side(τ); Z := τ(I3), which is an oriented cube in I3; and z0 := τ( 1
2, 1
2, 1
2 ), the
midpoint of Z. Let s = (s1, s2, s3) be the orthonormal linear coordinate system on
Z such that τ∗(si) = ϵ· ti.
Assume that the forms α|Z and β|Z are smooth. Let ˜α1, ˜α2, ˜α3∈O (Z)⊗ g be
the coefﬁcients of α|Z relative to s, namely
α|Z = ∑
1≤i≤3
˜αi· dsi.
And let ˜β1,2, ˜β1,3, ˜β2,3∈O (Z)⊗ h be the coefﬁcients of β|Z relative to s, namely
β|Z = ∑
1≤i<j≤3
˜βi,j· dsi∧ dsj.
Recall the Lie algebra map
ψh = Lie(Ψh) : g→ End(h).
For any i we get a function
ψh(˜αi)∈O (Z)⊗ End(h);
so for any i, j, k there is a function
ψh(˜αi)( ˜βj,k)∈O (Z)⊗ h.
Deﬁne the function
(8.5.2)
˜γ := ∂
∂s1
( ˜β2,3)− ∂
∂s2
( ˜β1,3) + ∂
∂s3
( ˜β1,2)
+ ψh(˜α1)( ˜β2,3)− ψh(˜α2)( ˜β1,3) + ψh(˜α3)( ˜β1,2)∈O (Z)⊗ h.
Let σpr be the following string in Z:
(8.5.3) σpr := τ◦
(
v0, ( 1
2, 0, 0)
)
∗
(
( 1
2, 0, 0), ( 1
2, 1
2, 0)
)
∗
(
( 1
2, 1
2, 0), ( 1
2, 1
2, 1
2 )
)
.
So σpr has initial point τ(v0) and terminal point z0; see Figure 32. Deﬁne
(8.5.4) g0 := MI(α| σpr) and g := MI(α| σ)
in G.
For i∈{ 1, . . . , 6} we consider the points zi∈ Z deﬁned as follows:
z1 := τ( 1
2, 1, 1
2 ), z2 := τ(1, 1
2, 1
2 ), z3 := τ( 1
2, 1
2, 1),
z4 := τ( 1
2, 0, 1
2 ), z5 := τ(0, 1
2, 1
2 ), z6 := τ( 1
2, 1
2, 0).
See Figure 32. We deﬁne the strings
(8.5.5) ρ′
i := ( τ◦ σ♭
i )∗ (τ◦ τ♭
i◦ σpr),
where σpr is the probe in I2; see formula (4.2.4). So ρ′
i has initial point τ(v0) and
terminal point zi. Let
g′
i := MI(α| ρ′
i)∈ G.
114 AMNON YEKUTIELI
Figure 32. Illustration for Subsection 8.5.
For i∈{ 1, . . . , 6} we deﬁne elements λi∈ h as follows:
(8.5.6)
λ1 :=−ϵ2· Ψh(g· g′
1)
( ˜β1,3(z1)
)
,
λ2 := ϵ2· Ψh(g· g′
2)
( ˜β2,3(z2)
)
,
λ3 := ϵ2· Ψh(g· g′
3)
( ˜β1,2(z3)
)
,
λ4 :=−ϵ2· Ψh(g· g′
4)
( ˜β1,3(z4)
)
,
λ5 := ϵ2· Ψh(g· g′
5)
( ˜β2,3(z5)
)
,
λ6 := ϵ2· Ψh(g· g′
6)
( ˜β1,2(z6)
)
.
It is easy to see from Deﬁnition 4.3.3 that
(8.5.7) exp H(λi) = RP0(α, β| ∂i(σ, τ)).
Lemma 8.5.8. There are constants c7(α, β) and ϵ7(α, β) with these properties:
(i) c7(α, β)≥ c6(α, β) and
0 < ϵ7(α, β)≤ min
(
ϵ6(α, β), 1
10 ϵ1(α)
)
.
(ii) Let (σ, τ) be a nondegenerate cubical balloon in (I3, v0) with ϵ := side(τ).
Assume that ϵ < ϵ7(α, β), len(σ)≤ 6, and the forms α|Z and β|Z are smooth.
Then, with λi as in (8.5.6), the following estimate holds:
‖‖ logH
(
MI(α, β| ∂(σ, τ))
)
− ∑
6
i=1 λi
‖‖≤ c7(α, β)· ϵ4 .
Proof. Let us set
c := 12· max
(
c2(α, β), exp(c4(α, Ψh)· 9)·‖ β‖Sob
)
.
According to Proposition 4.5.2(2), if ϵ < ϵ2(α, β) then
(8.5.9)
‖‖ logH
(
MI(α, β| ∂i(σ, τ))
)
− λi
‖‖≤ c2(α, β)· ϵ4≤ 1
12 c· ϵ4 .
And by Proposition 3.5.10 we know that
‖λi‖≤ exp
(
c4(α, Ψh)· 9
)
·‖ β‖Sob· ϵ2≤ 1
12 c· ϵ2 .
NONABELIAN MULTIPLICATIVE INTEGRATION 115
Hence
(8.5.10)
‖‖ logH
(
MI(α, β| ∂i(σ, τ))
)‖‖≤ 1
6 c· ϵ2 .
We will take
ϵ7(α, β) := min
(
ϵ6(α, β), c−1/2· ϵ0(H)1/2)
.
Now assume that ϵ < ϵ7(α, β). Then by property (ii) of Theorem 2.1.2, used in
conjunction with the bound (8.5.10), we get
‖‖ logH
(
∏
6
i=1 MI(α, β| ∂i(σ, τ))
)
− ∑
6
i=1 MI(α, β| ∂i(σ, τ))
‖‖
≤ c0(H)· (c· ϵ2)2 = c0(H)· c2· ϵ4 .
Combining this with (8.5.9) we obtain
(8.5.11)
‖‖ logH
(
∏
6
i=1 MI(α, β| ∂i(σ, τ))
)
− ∑
6
i=1 λi
‖‖
≤
(
c0(H)· c2 + 1
2 c
)
· ϵ4 .
Thus the constant
c7(α, β) := max
(
c0(H)· c2 + 1
2 c, c6(α, β)
)
works. □
Deﬁnition 8.5.12. (1) Let (σ, τ) be a square kite in (I3, v0). We will say that
(σ, τ) is (α, β)-tiny (in this section) if side (τ) < ϵ7(α, β) and len(σ)≤ 9.
(2) Let (σ, τ) be a cubical balloon in (I3, v0). We will say that (σ, τ) is (α, β)-
tiny if side(τ) < ϵ7(α, β) and len(σ)≤ 6.
Note that if (σ, τ) is an (α, β)-tiny cubical balloon, then the kites ∂i(σ, τ) are all
(α, β)-tiny.
Let (σ, τ) be a cubical balloon in (I2, v0). For i∈{ 1, . . . , 6} let ρi be the linear
map I1→ Z such that ρi(v0) = z and ρi(v1) = zi. Recall the string σpr from
(8.5.3). For every i ∈ {1, . . . , 6} the string σpr∗ ρi has initial point τ(v0) and
terminal point zi. Let
gi := MI(α| ρi)∈ G.
The form α|Z is smooth, and hence we have
α′ := ψh(α|Z)∈ Ω1(Z)⊗ End(h).
As in Deﬁnition 1.3.5 there is an associated constant form at z0:
α′(z0)∈ Ω1
const(Z)⊗ End(h).
In this way for every i we get
∫
ρi
α′(z0)∈ End(h).
Lemma 8.5.13. There is a constant c 8(α, β) with this property:
(∗) Let (σ, τ) be a nondegenerate (α, β)-tiny cubical balloon in (I3, v0), with ϵ :=
side(τ). Then, in the notation above, the estimate
‖‖ Ψh(g· g′
i)− Ψh(g· g0)◦
(
1 +
∫
ρi
α′(z0)
)‖‖≤ c8(α, β)· ϵ2
holds for every i∈{ 1, . . . , 6}.
116 AMNON YEKUTIELI
Proof. Consider such a balloon. Recall the strings ρ′
i from formula (8.5.5). Since
ϵ < ϵ7(α, β)≤ 1
10 ϵ1(α), we see that for every i the closed string ρ′
i∗ (σpr∗ ρi)−1
has
len(ρ′
i∗ (σpr∗ ρi)−1) < 10· ϵ≤ ϵ1(α).
And this closed string bounds an area less than 10· ϵ2. Hence by Corollary 3.5.12
we have
‖‖ logG
(
g′
i· (g0· gi)−1)‖‖≤ c0(G)· c1(α)2· (10· ϵ)2 + (10· ϵ2)·‖ α‖Sob .
Therefore there is a constant c′, depending only on α, such that
(8.5.14)
‖‖ Ψh(g′
i)− Ψh(g0· gi)
‖‖≤ c′· ϵ2 .
By Proposition 3.5.10 we know that
‖Ψh(g)‖≤ exp
(
c4(α, Ψh)· 9
)
·‖ α‖Sob
and
‖Ψh(g0)‖≤ exp
(
c4(α, Ψh)· 2ϵ
)
·‖ α‖Sob .
Therefore‖‖ Ψh(g· g′
i)− Ψh(g· g0· gi)
‖‖ =
‖‖ Ψh(g)◦
(
Ψh(g′
i)− Ψh(g0· gi)
)‖‖
≤
‖‖ Ψh(g)
‖‖·
‖‖ Ψh(g′
i)− Ψh(g0· gi)
‖‖
≤ exp
(
c4(α, Ψh)· 9
)
·‖ α‖Sob· c′· ϵ2 .
On the other hand, by Proposition 3.5.13 we have the estimate
‖‖ Ψh(gi)−
(
1 +
∫
ρi
α′(z0)
)‖‖≤ c5(α, Ψh)· 1
4 ϵ2 .
We conclude that the constant
c8(α, β) := exp
(
c4(α, Ψh)· 9
)
·‖ α‖Sob· c′
+ c5(α, Ψh)· 1
4· exp
(
c4(α, Ψh)· 12
)
·‖ α‖2
Sob .
works. □
Lemma 8.5.15. There is a constant c 9(α, β) with this property:
(∗) Let (σ, τ) be a nondegenerate (α, β)-tiny cubical balloon in (I3, v0), with ϵ :=
side(τ). Then, in the notation above, the following estimate holds:
‖‖ ∑
6
i=1 λi− ϵ3· Ψh(g· g0)( ˜γ(z0))
‖‖≤ ϵ4· c9(α, β) .
Proof. The strategy is to try to estimate the elements λi.
We begin with i = 1. Deﬁne
µ1 := ϵ2· Ψh(g· g0)
(
− ˜β1,3(z0)− 1
2· ϵ· ψh(˜α2(z0))( ˜β1,3(z0))
− 1
2· ϵ· ( ∂
∂s2
˜β1,3)(z0)
)
.
The Taylor expansion to ﬁrst order of the function ˜β1,3 around z0 gives us
(8.5.16)
‖‖ ˜β1,3(z1)−
( ˜β1,3(z0)− 1
2 ϵ· ( ∂
∂s2
˜β1,3)(z0)
)‖‖≤ 1
4 ϵ2·‖ β‖Sob .
And Lemma 8.5.13, for i = 1, gives
(8.5.17)
‖‖ Ψh(g· g′
i)− Ψh(g· g0)◦
(
1− 1
2 ϵ· ˜α2(z0)
)‖‖≤ c8(α, β)· ϵ2 .
Let
d := exp
(
c4(α, Ψh)· 9
)
· 1
4·‖ β‖Sob + c8(α, β)· 2·‖ β‖Sob
+ exp
(
c4(α, Ψh)· 9
)
· 1
2·‖ α′‖Sob·‖ β‖Sob .
NONABELIAN MULTIPLICATIVE INTEGRATION 117
By combining the estimates (8.5.16) and (8.5.17) we obtain
(8.5.18) ‖λ1− µ1‖≤ d· ϵ4 .
We do the same thing for λ4: let
µ4 := ϵ2· Ψh(g· g0)
(
˜β1,3(z0)− 1
2· ϵ· ψh(˜α2(z0))( ˜β1,3(z0))
− 1
2· ϵ· ( ∂
∂s2
˜β1,3)(z0)
)
.
The same sort of calculation that got us (8.5.18), now gives the inequality
(8.5.19) ‖λ4− µ4‖≤ d· ϵ4
And clearly
µ1 + µ4 = ϵ3· Ψh(g· g0)
(
−ψh(˜α2(z0))( ˜β1,3(z0))− ( ∂
∂s2
˜β1,3)(z0)
)
.
Plugging inequalities (8.5.18) and (8.5.19) into this we get
(8.5.20)
‖‖ (λ1 + λ4)−
(
ϵ3· Ψh(g· g0)
(
−ψh(˜α2(z0))( ˜β1,3(z0))− ( ∂
∂s2
˜β1,3)(z0)
))‖‖
≤ ϵ4· 2d .
By a similar calculation for the pairs of indices (2, 5) and (3, 6) we get these
analogues of formula (8.5.20):
‖‖ (λ2 + λ5)−
(
ϵ3· Ψh(g· g0)
(
ψh(˜α1(z0))( ˜β2,3(z0)) + ( ∂
∂s1
˜β2,3)(z0)
))‖‖
≤ ϵ4· 2d
and
‖‖ (λ3 + λ6)−
(
ϵ3· Ψh(g· g0)
(
ψh(˜α3(z0))( ˜β1,2(z0)) + ( ∂
∂s3
˜β1,2)(z0)
))‖‖
≤ ϵ4· 2d .
Thus, plugging in the value of ˜γ(z0) from (8.5.2) we get
‖‖ ∑
6
i=1 λi− ϵ3· Ψh(g· g0)( ˜γ(z0))
‖‖≤ ϵ4· 6d .
To ﬁnish we take c8(α, β) := 6d. □
The last two lemmas combined give us:
Lemma 8.5.21. Let (σ, τ) be a nondegenerate (α, β)-tiny cubical balloon in (I3, v0),
with ϵ := side(τ), Z := τ(I3) and z := ( 1
2, 1
2, 1
2 ). Assume that α|Z and β|Z are smooth.
Let ˜γ∈O (Z)⊗ h be the function from equation (8.5.2), and let g , g0∈ G be the group
elements from equation (8.5.4). Then
‖‖ logH
(
MI(α, β| ∂(σ, τ))
)
− ϵ3· Ψh(g· g0)( ˜γ(z0))
‖‖≤ ϵ4· c10(α, β) ,
where
c10(α, β) := c8(α, β) + c9(α, β).
If, moreover, ˜γ happens to be an inert function, then
Ψh(g· g0)( ˜γ(z0)) = Ψh,α( ˜γ)(z0),
and therefore
‖‖ logH
(
MI(α, β| ∂(σ, τ))
)
− ϵ3· Ψh,α( ˜γ)(z0)
‖‖≤ ϵ4· c10(α, β) .
118 AMNON YEKUTIELI
8.6. Stokes Theorem. Here again we are in the general situation: (X, x0) is a
pointed polyhedron,
C/X = ( G, H, Ψ, Φ0, ΦX)
is a Lie quasi crossed module with additive feedback, and (α, β) is a piecewise
smooth connection-curvature pair in C/X.
The Lie group map Ψh : G→ GL(h) induces a Lie algebra map
ψh := Lie(Ψh) : g→ gl(h) = End(h).
By tensoring with Ωpws(X) this induces a map of DG Lie algebras
ψh : Ωpws(X)⊗ g→ Ωpws(X)⊗ End(h).
In this way from the pair α∈ Ω1
pws(X)⊗ g and β∈ Ω2
pws(X)⊗ h we get
ψh(α)(β)∈ Ω3
pws(X)⊗ h.
Deﬁnition 8.6.1. Let (X, x0) be a pointed polyhedron, let
C/X = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module with additive feedback, and let (α, β) be a piece-
wise smooth connection-curvature pair in C/X. The 3 -curvature of (α, β) is the
form
γ := d(β) + ψh(α)(β)∈ Ω3
pws(X)⊗ h.
Recall the notion of orientation of a polyhedron (Subsection 1.8). If Z is an ori-
ented cube, and (s1, s2, s3) is a positively oriented orthonormal linear coordinate
system on Z, then
or(Z) = ds1∧ ds2∧ ds3.
Lemma 8.6.2. Assume that (X, x0) = ( I3, v0), so that we are in the situation of Sub-
section 8.5. Let Z ⊂ I3 be an oriented nondegenerate cube, such that α|Z and β|Z are
smooth. Let ˜γ∈O (Z)⊗ h be the function from formula (8.5.2). Then ˜γ is the coefﬁcient
of γ|Z; Namely
γ|Z = ˜γ· or(Z).
Proof. This amounts to expanding the formula in Deﬁnition 8.6.1 into coordinates.
□
Lemma 8.6.3. Let (σ, τ) be a balloon in (X, x0). Then
MI
(
α, β| ∂(σ, τ)
)
∈ H0.
Proof. By deﬁnition we have
MI
(
α, β| ∂(σ, τ)
)
= ∏
i=1,...,6
MI
(
α, β| (σ, τ)◦ (σ♭
i , τ♭
i )
)
in the notation of Deﬁnition 8.1.5. For every index i we have, by Theorem 6.2.1,
an equality
Φ0
(
MI
(
α, β| (σ, τ)◦ (σ♭
i , τ♭
i )
)
= MI
(
α| ∂
(
(σ, τ)◦ (σ♭
i , τ♭
i )
))
in the group G. Now from Figure 31 we see that the closed string
∂∂I3 = ∏
i=1,...,6
∂(σ♭
i , τ♭
i )
NONABELIAN MULTIPLICATIVE INTEGRATION 119
is cancellation equivalent to the empty string in the monoid of strings inI3. There-
fore the closed string
∂∂(σ, τ) = ∏
i=1,...,6
∂
(
(σ, τ)◦ (σ♭
i , τ♭
i )
)
is cancellation equivalent to the empty string in the monoid of strings in X. By
Proposition 3.5.8 we can conclude that
∏
i=1,...,6
MI
(
α, β| ∂
(
(σ, τ)◦ (σ♭
i , τ♭
i )
))
= 1
in G. Hence
Φ0
(
MI
(
α, β| ∂(σ, τ)
))
= 1.
□
Lemma 8.6.4. Let (σ, τ) be a balloon in (X, x0). Then there is a piecewise linear map
f : (I3, v0)→ (X, x0), and a cubical balloon (σ′, τ′) in (I3, v0), such that len(σ′)≤ 2,
f|τ′(I3) is linear, and
(σ, τ) = f◦ (σ′, τ′)
as balloons in (X, x0).
Proof. Just like the proof of Proposition 4.1.6. □
Lemma 8.6.5. Let (σ, τ) be a balloon in (X, x0). Take any k≥ 0. Then
MI
(
α, β| ∂(tesk(σ, τ))
)
= MI
(
α, β| ∂(σ, τ)
)
.
Proof. Due to the recursive nature of the tessellations it is enough to consider the
case k = 1. As in the ﬁrst paragraph in the proof of Lemma 7.3.3, and using
Lemma 8.6.4, we can assume that (X, x0) = ( I2, v0) and (σ, τ) = ( σ0
1 , τ0
1 ), the
basic balloon.
The assertion is now an easy consequence of Lemma 8.4.2 and Corollary 7.5.2.
□
Theorem 8.6.6 (Nonabelian 3-dimensional Stokes Theorem). Let (X, x0) be a pointed
polyhedron, let C/X be a Lie quasi crossed module with additive feedback, let (α, β) be
a piecewise smooth connection-curvature pair in C/X, and let γ be the 3-curvature of
(α, β). Then:
(1) The form γ is inert.
(2) For any balloon (σ, τ) in (X, x0) one has
MI
(
α, β| ∂(σ, τ)
)
= MI(α, γ| τ)
in H.
Note that assertion (1) of the theorem is a generalized Bianchi identity.
Proof. (1) Since γ is a 3-form, it is enough to prove that the form γ|Z∈ Ω3
pws(Z)⊗
h is inert for every cube Z in X. Given such a cube Z, choose a linear map f :
I3→ X such that Z = f (I3). Then γ|Z is inert if and only if f∗(γ)∈ Ω3
pws(I3)⊗
h is inert, with respect to the induced Lie quasi crossed module with additive
feedback f∗(C/X). Hence we might as well assume that (X, x0) = ( I3, v0).
Now the singular locus of α and the singular locus of β are contained in a ﬁnite
union of polygons in I3. So by continuity it is enough to show that γ|Z is inert
for cubes Z⊂ I3 such that α|Z and β|Z are smooth. In this case γ is also smooth.
Given such a cube Z, choose an orientation on it, and let ˜γ∈O (Z)⊗ h be
the coefﬁcient of γ|Z (in the sense of Deﬁnition 1.8.2). We have to prove that the
120 AMNON YEKUTIELI
function ˜γ is inert; namely that ˜γ(z)∈ Ker(ΦX(z)) for every z∈ Z. Again by
continuity, it is enough to look at z∈ Int Z.
We are allowed to move the cube Z around the point z and to shrink it.
Hence it is enough to take an (α, β)-tiny balloon (σ, τ), and to show that ˜γ(z)∈
Ker(ΦX(z)) for the midpoint z := τ( 1
2, 1
2, 1
2 ) of Z := τ(I3).
Let g and g0 be the group elements from equation (8.5.4). By Lemma 8.6.3 we
have
MI
(
α, β| ∂(σ, τ)∈ H0,
and by Lemma 8.5.1 we have
MI
(
α, β| ∂(σ, τ)
)
∈ V0(H).
Taking logarithms we see that
logH
(
MI
(
α, β| ∂(σ, τ)
)
∈ h0.
By Lemma 8.5.21 it follows that the distance of the element
Ψh(g· g0)( ˜γ(z)) from the linear subspace h0 is at most c10· ϵ4.
Now by Proposition 3.5.10(1) there is a uniform bound on the norm of the oper-
ator Ψh(g· g0)−1; say c′. So the distance of ˜γ(z) from the subspace Ker(ΦX(z))⊂
h is at most c′· c· ϵ.
Since we can make ϵ arbitrarily small, we conclude that ˜γ(z) ∈
Ker(ΦX(z)).
(2) By the functoriality of MI
(
α, β| ∂(σ, τ)
)
and MI(α, γ| τ) (see Propositions 4.5.3
and 8.3.13), and using the construction of Lemma 8.6.4, we can assume that
(X, x0) = ( I3, v0) and len(σ)≤ 2.
Take any k≥ 0. Consider the sequence
tesk(σ, τ) =
(
(σ, τ)◦ (σk
i , τk
i )
)
i=1,...,8k
which was deﬁned in Subsection 8.1. The twisted multiplicative integration of
inert forms is multiplicative:
MI(α, γ| τ) = ∏
i=1,...,8k
MI
(
α, γ| τ◦ τk
i ).
On the other hand, by Lemma 8.6.5 we know that
MI
(
α, β| ∂(σ, τ)
)
= ∏
i=1,...,8k
MI
(
α, β| ∂((σ, τ)◦ (σk
i , τk
i ))
)
.
So it sufﬁces to prove that
MI
(
α, β| ∂((σ, τ)◦ (σk
i , τk
i ))
)
= MI
(
α, γ| τ◦ τk
i )
for every i∈{ 1, . . . , 8k}.
If k is large enough then all the balloons in tes k(σ, τ) are (α, β)-tiny. We con-
clude that it sufﬁces to prove the equality
MI
(
α, β| ∂(σ, τ)
)
= MI(α, γ| τ)
for an (α, β)-tiny balloon (σ, τ) in (I3, v0).
Suppose we are given an (α, β)-tiny balloon (σ, τ), and a natural number k. Let
ϵ := side(τ). For any index i ∈ { 1, . . . , 8k} let Zi :=
(τ◦ τk
i )(I3), which is an oriented cube in I3 of side ( 1
2 )k· ϵ, and let zi := ( τ◦
τk
i )( 1
2, 1
2, 1
2 ). Deﬁne
good(τ, k) :={i| α|Zi and β|Zi are smooth},
NONABELIAN MULTIPLICATIVE INTEGRATION 121
and deﬁne bad (τ, k) to be the complement of good (τ, k) in{1, . . . , 8k}. Since the
singular loci of α and β are contained in a ﬁnite union of polygons, it follows that
|bad(τ, k)|≤ a2(α, β)· 4k + a0(α, β)
for some constants a0(α, β), a2(α, β), that are independent of k; cf. Lemma 4.4.13.
For i∈ good(τ, k) let ˜γi∈O (Zi)⊗ h be the coefﬁcient of γ|Zi, in the sense of
Deﬁnition 1.8.2, and let
µi := ( 1
2 )3k· ϵ3· Ψh,α( ˜γi)(zi)∈ h0.
According to Lemmas 8.5.21 and 8.6.2 we know that
‖‖ logH
(
MI
(
α, β| ∂((σ, τ)◦ (σk
i , τk
i ))
))
− µi
‖‖≤ ( 1
2 )4k· ϵ4· c10(α, β) .
On the other hand, for i∈ bad(τ, k) let µi := 0∈ h. According to Lemma 8.5.1
we have the inequality
‖‖ logH
(
MI
(
α, β| ∂((σ, τ)◦ (σk
i , τk
i ))
))
− µi
‖‖≤ ( 1
2 )3k· ϵ3· c6(α, β) .
Let
RSk(α, γ| τ) :=
8k
∑
i=1
µi∈ h0.
Applying property (iv) of Theorem 2.1.2 with the inequalities above we get
‖‖ logH
(
MI
(
α, β| σ, τ
))
− RSk(α, γ| τ)
‖‖
≤ c0(H)·
(
8k· ( 1
2 )4k· ϵ4· c10(α, β)
+ (a2(α, β)· 4k + a0(α, β))· ( 1
2 )3k· ϵ3· c6(α, β)
)
.
We see that the difference tends to 0 as k→ ∞. But
lim
k→∞
RSk(α, γ| τ) = logH
(
MI(α, γ| τ)
)
.
□
Remark 8.6.7. Part (1) of Theorem 8.6.6 is a variant of the Bianchi identity.
NONABELIAN MULTIPLICATIVE INTEGRATION 123
9. M ultiplicative Integration on Triangular Kites
In this section (X, x0) is a pointed manifold. Recall that by Convention 1.4.7
this means that X is a smooth manifold with sharp corners (cf. Deﬁnition 1.4.2);
so it could be a polyhedron. We introduce triangular kites in (X, x0) and the
corresponding multiplicative integration.
9.1. Triangular Kites and balloons. Recall that the polyhedra I1 and ∆1 are iden-
tiﬁed via the linear isomorphism ∆1 ≃− →I1 that on vertices is (v0, v1)↦→ (v0, v1).
A piecewise smooth path in X is a piecewise smooth map σ : I1→ X. When
convenient we shall view such a path as a piecewise smooth map ∆1→ X using
the identiﬁcation above.
Suppose σ1, σ2 : I1→ X are piecewise smooth paths satisfying σ1(v1) = σ2(v0).
Their product is the piecewise smooth path
σ1∗ σ2 : I1→ X
deﬁned as follows:
(σ1∗ σ2)(a) :=
{
σ1(2a) if 0≤ a≤ 1
2
σ2(2a− 1) if 1
2≤ a≤ 1.
Note that this is the standard product used in homotopy theory, and it is distinct
from the concatenation operation on strings. In particular this product is not
associative nor unital.
The inverse of a piecewise smooth path σ : I1→ X is the piecewise smooth
path σ−1 : I1→ X deﬁned by
σ−1(a) := σ(1− a).
Suppose Z is a polyhedron, f : Z→ X is a piecewise smooth map, and σ =
(σ1, . . . ,σm) is a string in Z, with m ≥ 1. This data gives rise to a piecewise
smooth path f◦ σ in X deﬁned as follows:
(9.1.1) f◦ σ :=
(
( f◦ σ1)∗ ( f◦ σ2)
)
∗···∗ ( f◦ σm).
In this formula we view each f◦ σi as a piecewise smooth path in X, and the
multiplication∗ is that of paths. For the empty string σ (i.e. m = 0) the path f◦ σ
is not always deﬁned; but if X has a base point x0, then we usually deﬁne f◦ σ
to be the constant path x0.
Deﬁnition 9.1.2. A piecewise smooth triangular kitein (X, x0) is a pair (σ, τ), consist-
ing of piecewise smooth maps σ : I1→ X and τ : ∆2→ X, satisfying σ(v0) = x0
and σ(v1) = τ(v0).
See Figure 1 for an illustration.
The boundary of ∆2 is the string
(9.1.3) ∂∆2 := (v0, v1)∗ (v1, v2)∗ (v2, v0)
(consisting of 3 pieces) in ∆2.
Deﬁnition 9.1.4. Let (σ, τ) be a piecewise smooth triangular kite in
(X, x0). Its boundary is the piecewise smooth path
∂(σ, τ) :=
(
σ∗ (τ◦ ∂∆2)
)
∗ σ−1.
See Figure 2.
124 AMNON YEKUTIELI
Figure 33. The boundary of ∆3.
Deﬁnition 9.1.5. A piecewise smooth triangular balloon in (X, x0) is a pair (σ, τ),
consisting of piecewise smooth maps σ : I1 → X and τ : ∆3 → X, satisfying
σ(v0) = x0 and σ(v1) = τ(v0).
See Figure 3 for an illustration.
Let (Z, z0) be a pointed polyhedron. By linear triangular kite in (Z, z0) we mean
the obvious variant of linear quadrangular kite. Namely this is a pair (σ, τ),
consisting of a string σ in Z and a linear map τ : ∆3→ X. These must satisfy
σ(v0) = z0 and σ(v1) = τ(v0). Likewise we deﬁne linear triangular balloons.
Deﬁnition 9.1.6. The boundary of ∆3 is the sequence of linear triangular kites
∂∆3 =
(
∂1∆3, ∂2∆3, ∂3∆3, ∂4∆3)
in (∆3, v0) deﬁned as follows.
• Let σ♭
2, σ♭
3, σ♭
4 be the empty strings in ∆3. And let σ♭
1 : I1→ ∆3 be the linear
map deﬁned on vertices by
σ♭
1(v0, v1) := (v0, v1).
• Let τ♭
i : ∆2→ ∆3 be the linear maps given on vertices by:
τ♭
1 (v0, v1, v2) := (v1, v2, v3),
τ♭
2 (v0, v1, v2) := (v0, v1, v3),
τ♭
3 (v0, v1, v2) := (v0, v3, v2),
τ♭
4 (v0, v1, v2) := (v0, v2, v1).
• The kite are
∂i∆3 := ( σ♭
i , τ♭
i ).
See Figure 33.
Warning: the kites (σ♭
i , τ♭
i ) above should be confused with the quadrangular
kites from Deﬁnition 8.1.5, despite the shared notation.
NONABELIAN MULTIPLICATIVE INTEGRATION 125
Deﬁnition 9.1.7. Let (σ, τ) be a piecewise smooth triangular balloon in (X, x0).
Its boundary is the sequence of piecewise smooth triangular kites
∂(σ, τ) :=
(
∂1(σ, τ), ∂2(σ, τ), ∂3(σ, τ), ∂4(σ, τ)
)
in (X, x0), where
∂i(σ, τ) := ( σ, τ)◦ (σ♭
i , τ♭
i ).
See Figure 4 for an illustration.
9.2. MI on Triangular Kites. As before, (X, x0) is a pointed manifold.
Let
C := ( G, H, Ψ, Φ0)
be a Lie quasi crossed module (Deﬁnition 5.1.1). As usual we write g := Lie(G)
and h := Lie(H). An additive feedback for C over (X, x0) is an element
ΦX∈O (X)⊗ Hom(h, g)
satisfying condition (∗∗) of Deﬁnition 5.2.1. Just like in Deﬁnition 5.2.2, we call
the data
C/X := ( G, H, Ψ, Φ0, ΦX)
a Lie quasi crossed module with additive feedback over (X, x0).
Deﬁnition 9.2.1. Let α∈ Ω1(X)⊗ g, and let σ be a piecewise smooth path in X.
Consider the piecewise smooth differential form
α′ := σ∗(α)∈ Ω1
pws(I1)⊗ g.
We deﬁne
MI(α| σ) := MI(α′| I1)∈ G
(cf. Deﬁnition 3.3.20).
Proposition 9.2.2. Let α∈ Ω1(X)⊗ g.
(1) Suppose σ1 and σ2 are piecewise smooth paths in X such that σ1∗ σ2 is deﬁned.
Then
MI(α| σ1∗ σ2) = MI(α| σ1)· MI(α| σ2).
(2) Let σ be a piecewise smooth path in X. Then
MI(α| σ−1) = MI(α| σ)−1.
(3) Suppose σ′ is a string in a polyhedron Z, f : Z→ X is a piecewise smooth map,
and σ := f◦ σ′ is the path in X gotten by the operation (9.1.1). Then
MI(α| σ) = MI( f∗(α)| σ′).
Proof. (1) We could use the 2-dimensional Stokes Theorem; but there is an ele-
mentary proof. Let σ1
1 , σ1
2 : I1→ I1 be the linear maps belonging to tes 1 I1, as in
Deﬁnition 3.1.2. Let σ : I1→ X be the piecewise smooth map such that σ◦ σ1
i = σi
for i = 1, 2. And let α′ := σ∗(α). Now by deﬁnition of ∗ we have σ = σ1∗ σ2 as
paths in X. Hence
MI(α| σ1∗ σ2) = MI(α| σ) = MI(α′| I1).
Likewise
MI(α| σi) = MI(α| σ◦ σ1
i ) = MI(α′| σ1
i ).
On the other hand, by Proposition 3.3.22(3) we know that
MI(α′| I1) = MI(α′| σ1
1 )· MI(α′| σ1
2 ).
126 AMNON YEKUTIELI
Figure 34. The piecewise linear retraction h : I2→ ∆2.
(2) This is immediate from Proposition 3.5.8(2).
(3) This follows part (1) and induction on the number of pieces in the string
σ′. □
In order to deﬁne MI on triangular kites we shall need the following geometric
construction. Consider the linear triangular kite (σ′, τ′) in (I2, v0), where the
string σ′ has one linear piece σ′ : I1→ I2 deﬁned on vertices by
σ′(v0, v1) := (v0, ( 1
2, 1
2 )).
The linear map τ′ : ∆2→ I2 is deﬁned on vertices by
τ′(v0, v1, v2) := (( 1
2, 1
2 ), (1, 1
2 ), ( 1
2, 1)).
We also need the linear quadrangular kite (σ′, τ′′) in (I2, v0), where the linear
map τ′′ : I2→ I2 is deﬁned on vertices by
τ′′(v0, v1, v2) := (( 1
2, 1
2 ), (1, 1
2 ), ( 1
2, 1)).
We write Z := σ′(I1) and Y := τ′(∆2).
Consider the canonical linear embedding ∆2→ I2 which on vertices is
(v0, v1, v2)↦→ (v0, v1, v2).
Let h : I2→ ∆2 be the piecewise linear retraction which is linear on ∆2 and on
the the triangle complementary to it, and satisﬁes h(1, 1) = v1. See Figure 34.
Lemma 9.2.3. There exists a piecewise linear retraction g : I2→ Y∪ Z, such that
g◦ τ′′ = τ′◦ h
as piecewise linear maps I2→ I2.
Proof. Easy exercise. Cf. proof of Proposition 4.1.6. And see Figure 35. □
Let us ﬁx such a retraction g, which we also view as a piecewise linear map
g : I2→ I2.
Deﬁnition 9.2.4. Let α ∈ Ω1(X)⊗ g and β ∈ Ω1(X)⊗ h. Given a piecewise
smooth triangular kite (σ, τ) in (X, x0) we deﬁne its multiplicative integral
MI(α, β| σ, τ)∈ H
as follows. Let f : I2→ X be the unique piecewise smooth map such that:
• f◦ σ′ = σ as maps I1→ X.
• f◦ τ′ = τ as maps ∆2→ X.
• f = f◦ g as maps I2→ X, where g : I2→ I2 is the chosen retraction.
NONABELIAN MULTIPLICATIVE INTEGRATION 127
Figure 35. The piecewise linear retraction g : I2→ Y∪ Z. Here
w := ( 1
2, 1
2 ).
Figure 36. The piecewise smooth map f : I2 → X such that
f◦ (σ′, τ′) = ( σ, τ).
(See Figure 36.) We get differential forms
α′ := f∗(α)∈ Ω1
pws(I2)⊗ g
and
β′ := f∗(β)∈ Ω2
pws(I2)⊗ h.
We deﬁne
MI(α, β| σ, τ) := MI(α′, β′| σ′, τ′′),
where (σ′, τ′′) is the linear quadrangular kite in (I2, v0) deﬁned above, and
MI(α′, β′| σ′, τ′′) is the multiplicative integral from Deﬁnition 4.4.16.
This deﬁnition might seem strange; but we shall soon see that it has all the
expected good properties.
Proposition 9.2.5 (Functoriality in X). Let e : (Y, y0)→ (X, x0) be a map of pointed
manifolds, let α∈ Ω1(X)⊗ g, let β∈ Ω2(X)⊗ h, and let (σ, τ) be a piecewise smooth
triangular kite in (Y, y0). Then
MI(α, β| e◦ σ, e◦ τ) = MI
(
e∗(α), e∗(β)| σ, τ
)
,
where the latter is calculated with respect to the Lie quasi crossed module with additive
feedback e∗(C/X).
Proof. This is immediate from the deﬁnition, since (e◦ f )∗ = f∗◦ e∗ for a piece-
wise smooth map f : I2→ Y. □
128 AMNON YEKUTIELI
Proposition 9.2.6 (Comparison to Quadrangular Kites) . Let (Z, z0) be a pointed
polyhedron, e : (Z, z0) → (X, x0) a piecewise smooth map preserving base points,
(σ, τ) a piecewise smooth triangular kite in (X, x0), (σ′, τ′) a linear quadrangular kite
in (Z, z0), α∈ Ω1(X)⊗ g and β∈ Ω2(X)⊗ h. Assume that σ = e◦ σ′ as paths in X,
and τ◦ h = e◦ τ′ as maps I2→ X, where h : I2→ ∆2 is the retraction in Figure 34.
Then
MI(α, β| σ, τ) = MI(e∗(α), e∗(β)| σ′, τ′),
where the latter is calculated with respect to the Lie quasi crossed module with additive
feedback e∗(C/X).
Proof. The piecewise smooth map f : I2 → X used in Deﬁnition 9.2.4 can be
factored as f = e◦ f′ for a piecewise linear map f′ : (I2, v0)→ (Z, z0) of pointed
polyhedra. The assertion now follows from Proposition 4.5.3. □
The notion of compatible connection from Deﬁnition 5.2.4 makes sense here
too, only we have to consider α∈ Ω1(X)⊗ g (and replace “string” with “piece-
wise smooth path”).
Proposition 9.2.7 (Moving the Base Point) . Let α ∈ Ω1(X)⊗ g be a connection
compatible with C/X, and let ρ be a piecewise smooth path in X, with initial point x 0
and terminal point x 1. Deﬁne g := MI(α| ρ), and let
Cg/X = ( G, Hg, Ψ, Φg
0, ΦX)
be the Lie quasi crossed module with additive feedback over (X, x1) constructed in Sub-
section 5.4. Given a form β∈ Ω2(X)⊗ h and a piecewise smooth triangular kite (σ, τ)
in (X, x1), consider the element
MIg(α, β| σ, τ)∈ Hg
calculated with respect to the Lie quasi crossed module with additive feedback Cg/X.
Then
Ψ(g)
(
MIg(α, β| σ, τ)
)
= MI(α, β| ρ∗ σ, τ)
in H.
Proof. It is possible to ﬁnd a polyhedron Z, points z0, z1 ∈ Z, a string ρ′ in Z
with initial point z0 and terminal point z1, a linear quadrangular kite (σ′, τ′) in
(Z, z1) and a piecewise smooth map e : Z→ X, such that ρ = e◦ ρ′ as paths and
(σ, τ) = e◦ (σ′, τ′) as kites. Deﬁne α′ := e∗(α) and β′ := e∗(β).
Let C′/Z := e∗(C/X) be the induced Lie quasi crossed module with additive
feedback over the pointed polyhedron (Z, z0). By Proposition 9.2.2(3) we know
that MI(α′| ρ′) = g. Examining the deﬁnition of Cg/X in Subsection 5.4 we see
that
e∗(Cg/X) = ( C′)g/Z
as Lie quasi crossed modules with additive feedback over the pointed polyhedron
(Z, z1). Therefore MI g(α′, β′| σ′, τ′) is unambiguous.
By Proposition 9.2.6 we know that
MIg(α′, β′| σ′, τ′) = MIg(α, β| σ, τ)
and
MI(α′, β′| ρ′∗ σ′, τ′) = MI(α, β| ρ∗ σ, τ).
Finally, by Theorem 5.4.8 we have
MIg(α′, β′| σ′, τ′) = MI(α′, β′| ρ′∗ σ′, τ′).
□
NONABELIAN MULTIPLICATIVE INTEGRATION 129
9.3. Stokes Theorems. We continue with the setup from before: (X, x0) is a
pointed manifold, and
C/X = ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module with additive feedback.
Just like in Deﬁnition 5.3.1, a connection-curvature pair for C/X is a pair (α, β),
with α∈ Ω1(X)⊗ g and β∈ Ω1(X)⊗ h, such that α is a compatible connection,
and the differential equation
ΦX(β) = d(α) + 1
2 [α, α]
holds in Ω2(X)⊗ g.
Recall that for a piecewise smooth triangular kite (σ, τ), its boundary ∂(σ, τ)
was deﬁned in Deﬁnition 9.1.4.
Theorem 9.3.1 (Stokes Theorem for Triangles). Let (X, x0) be a pointed manifold, let
C/X := ( G, H, Ψ, Φ0, ΦX)
be a Lie quasi crossed module with additive feedback over (X, x0), let (α, β) be a
connection-curvature pair for C/X, and let (σ, τ) be a piecewise smooth triangular kite
in (X, x0). Then
Φ0
(
MI(α, β| σ, τ)
)
= MI(α, β| ∂(σ, τ)).
Proof. As in the proof of Proposition 9.2.7, we can ﬁnd a pointed polyhedron
(Z, z0), a linear quadrangular kite (σ′, τ′) in (Z, z0) and a piecewise smooth map
f : Z → X, such that (σ, τ) = f◦ (σ′, τ′) as kites. Deﬁne α′ := f∗(α) and
β′ := f∗(β). According to Proposition 9.2.2(3) we have
MI(α, β| ∂(σ, τ)) = MI(α′| ∂(σ′, τ′)).
And by Proposition 9.2.6 we have
MI(α, β| σ, τ) = MI(α′, β′| σ′, τ′).
Finally by Theorem 6.2.1 we know that
MI(α′| ∂(σ′, τ′)) = Φ0
(
MI(α′, β′| σ′, τ′)
)
.
□
For the 3-dimensional Stokes Theorem we shall need an auxiliary geometric
construction, similar to the one in the previous subsection. Consider the linear
triangular balloon (σ′, τ′) in (I3, v0), where the string σ′ has one linear piece
σ′ : I1→ I3 deﬁned on vertices by
σ′(v0, v1) :=
(
v0, ( 1
2, 1
2, 0)
)
.
The linear map τ′ : ∆3→ I3 is deﬁned on vertices by
τ′(v0, v1, v2, v3) :=
(
( 1
2, 1
2, 0), (1, 1
2, 0), ( 1
2, 1, 0), ( 1
2, 1
2, 1
2 )
)
.
We also need the linear quadrangular balloon (σ′, τ′′) in (I3, v0), where the linear
map τ′′ : I3 → I3 is deﬁned on vertices by the same formula as τ′. We let
Z := σ′(I1) and Y := τ′(∆3). See Figure 37.
Consider the canonical linear embedding ∆3→ I3 which on vertices is
(v0, . . . ,v3)↦→ (v0, . . . ,v3).
Let h : I3→ ∆3 be the piecewise linear retraction h := h2◦ h1, where h1 and h2
are the retractions shown in Figure 38.
130 AMNON YEKUTIELI
Figure 37. The triangular linear balloon (σ′, τ′) and the quad-
rangular linear balloon (σ′, τ′′) in the pointed polyhedron
(I3, v0).
Figure 38. The piecewise linear map h1 retracts the cube I3 to
a prism. The piecewise linear map h2 retracts the prism to the
tetrahedron ∆3.
Lemma 9.3.2. There is a piecewise linear retraction g : I3→ Z∪ Y, such that
g◦ τ′′ = τ′◦ h
as maps I3→ I3.
Proof. Nice exercise in piecewise linear geometry. □
Let us ﬁx such a retraction g, which we also view as a piecewise linear map
g : I3→ I3.
The notions of tame connection and inert differential form , from Subsections 5.3
8.3 respectively, make sense here, and all pertinent results hold. Given a tame
connection α∈ Ω1(X)⊗ g, an inert form γ∈ Ω3(X)⊗ h and a piecewise smooth
balloon (σ, τ) in (X, x0), we deﬁne the twisted multiplicative integral
MI(α, γ| σ, τ)∈ H0
NONABELIAN MULTIPLICATIVE INTEGRATION 131
as follows. Let f : I3→ X be the unique piecewise smooth map satisfying:
• f◦ σ′ = σ as maps I1→ X.
• f◦ τ′ = τ as maps ∆3→ X.
• f = f◦ g as maps I3→ X, where g : I3→ I3 is the chosen retraction.
Now
C′/I3 := f∗(C/X) = ( G, H, Ψ, Φ0, f∗(ΦX))
is a Lie quasi crossed module with additive feedback over (I3, v0),
α′ := f∗(α)∈ Ω1
pws(I3)⊗ g
is a tame connection for C′/X, and
γ′ := f∗(γ)∈ Ω3
pws(I3)⊗ h
is an inert differential form. We deﬁne
(9.3.3) MI (α, γ| σ, τ) := MI
(
α′, γ′| τ′′),
where τ′′ : I3→ I3 is the linear map described above, and MI
(
α′, γ′| τ′′) is the
twisted multiplicative integral from Deﬁnition 8.3.12.
Remark 9.3.4. The reason that the path σ is explicit in the expression
MI(α, γ| σ, τ) is that this operation could depend on the homotopy class of σ,
in case the manifold X is not simply connected. Since polyhedra are always sim-
ply connected, we did not have to worry about strings in Deﬁnition 8.3.12.
It is easy to see that MI (α, γ| σ, τ) makes sense for an inert p-form γ and a
“p-dimensional balloon” (σ, τ), for any p≥ 0. Moreover, for p = 2 this coincides
with the nonabelian MI of Deﬁnition 9.2.4.
Recall the boundary ∂(σ, τ) of a balloon (σ, τ) in (X, x0), from Deﬁnition 9.1.7.
As is our convention for the multiplicative integral of a sequence, we write
MI(α, β| ∂(σ, τ)) := ∏
i=1,...,4
MI(α, β| ∂i(σ, τ)).
As in Deﬁnition 8.6.1, the 3-curvature of (α, β) is the form
γ := d(β) + ψh(α)(β)∈ Ω3(X)⊗ h.
Here is the second version of the main result of the paper (the ﬁrst version was
Theorem 8.6.6.)
Theorem 9.3.5 (Stokes Theorem for Tetrahedra). Let (X, x0) be a pointed manifold,
let C/X be a Lie quasi crossed module with additive feedback, let (α, β) be a connection-
curvature pair for C/X, and let γ be the 3-curvature of (α, β). Then:
(1) The differential form γ is inert.
(2) For any piecewise smooth balloon (σ, τ) in (X, x0) one has
MI
(
α, β| ∂(σ, τ)
)
= MI(α, γ| σ, τ)
in H.
Proof. (1) It sufﬁces to prove that for any piecewise smooth map f : I3→ X the
form
γ′ := f∗(γ)∈ Ω3
pws(I3)⊗ h
is inert. Deﬁne
α′ := f∗(α)∈ Ω1
pws(I3)⊗ g
and
β′ := f∗(β)∈ Ω2
pws(I3)⊗ h.
132 AMNON YEKUTIELI
Then (α′, β′) is a connection curvature pair in C′/I3 (this is a variant of Propo-
sition 5.3.3(1)), and γ′ is the 3-curvature of (α′, β′). But according to Theorem
8.6.6(1) the form γ′ is inert.
(2) Let f : (I3, v0)→ (X, x0) be the pointed piecewise smooth map constructed
just before (9.3.3). By deﬁnition we have
MI(α, γ| σ, τ) := MI
(
α′, γ′| τ′′).
By Proposition 9.2.6 we know that
MI
(
α, β| ∂(σ, τ)
)
= MI
(
α′, β′| ∂(σ′, τ′)
)
.
And by Theorem 8.6.6(2) we know that
MI
(
α′, β′| ∂(σ′, τ′′)
)
= MI
(
α′, γ′| τ′′).
It remains to prove that
(9.3.6) MI
(
α′, β′| ∂(σ′, τ′)
)
= MI
(
α′, β′| ∂(σ′, τ′′)
)
.
By deﬁnition we have
MI
(
α′, β′| ∂(σ′, τ′)
)
= ∏
i=1,...,4
MI(α, β| ∂i(σ′, τ′))
and
MI
(
α′, β′| ∂(σ′, τ′′)
)
= ∏
i=1,...,6
MI(α, β| ∂i(σ′, τ′′)).
Using Proposition 9.2.6 and looking at Figures 37, 33 and 31 we see that
MI
(
α′, β′| ∂1(σ′, τ′′)
)
= 1,
MI
(
α′, β′| ∂2(σ′, τ′′)
)
= 1,
MI
(
α′, β′| ∂3(σ′, τ′′)
)
= MI
(
α′, β′| ∂1(σ′, τ′)
)
,
MI
(
α′, β′| ∂4(σ′, τ′′)
)
= MI
(
α′, β′| ∂2(σ′, τ′)
)
,
MI
(
α′, β′| ∂5(σ′, τ′′)
)
= MI
(
α′, β′| ∂3(σ′, τ′)
)
and
MI
(
α′, β′| ∂6(σ′, τ′′)
)
= MI
(
α′, β′| ∂4(σ′, τ′)
)
.
Thus equation (9.3.6) is true. □
9.4. Rationality of the Multiplicative Integral. Let K be a subﬁeld of R. As com-
mon in algebraic geometry, let us denote by An(K) the set of K-rational points
of An(R); namely those points x∈ An(R) whose coordinates satisfy ti(x)∈ K,
i = 1, . . . ,n.
By (embedded) polyhedron deﬁned over K we mean a polyhedron X⊂ An(R),
such that all the vertices of X belong to An(K). For such X, and for every ﬁeld L
such that K⊂ L⊂ R, we can talk about the set X(L) of L-rational points of X.
The real polyhedron is of course X(R).
Suppose Y is another polyhedron deﬁned over K. It makes sense to talk about
linear maps f : X→ Y deﬁned over K. The condition is of course that for any
vertex v∈ X the point f (v) is in Y(K).
The simplices ∆p are deﬁned over Q. Therefore we have the notion of linear
triangulation of X deﬁned over K. This lets us consider piecewise linear maps
f : Y→ X deﬁned over K. In particular we have kites in X deﬁned over K.
The polyhedron X has a K-subalgebraOalg(X(K))⊂O (X) of K-valued alge-
braic functions on X(K), which is the restriction to X(K) of the polynomial algebra
K[t1, . . . ,tn]⊂O (An(R)). Similarly one can deﬁne the DG algebra Ωalg(X(K))
NONABELIAN MULTIPLICATIVE INTEGRATION 133
of K-valued algebraic differential forms , which is contained in Ω(X). Using linear
triangulations deﬁned over K we can also consider the K-algebraOpwa(X(K)) of
K-valued piecewise algebraic functions, and the DG algebra Ωpwa(X(K)) of K-valued
piecewise algebraic differential forms, which is a DG subalgebra of Ωpws(X).
Suppose X is a polyhedron and Y⊂ Am is an afﬁne algebraic variety, both
deﬁned over K. A map f : X→ Y is said to be algebraic and deﬁned over K if
for every i the function ti◦ f : X(K)→ R belongs toOalg(X(K)). Equivalently, f
extends to a map of algebraic varieties ˜f : An→ Am that’s deﬁned over K. Using
linear triangulations deﬁned over K we can also consider piecewise algebraic
maps f : X→ Y deﬁned over K.
Now assume that we are given a Lie quasi crossed module with additive feed-
back
C = ( G, H, Ψ, Φ0, ΦX)
in which (X, x0) is a pointed polyhedron deﬁned over K, the groups G and H are
afﬁne unipotent linear algebraic groups deﬁned over K, the maps Ψ : G× H→ H
and Φ0 : H→ G are maps of algebraic varieties deﬁned over K, and
ΦX∈O pwa(X(K))⊗K HomK(h(K), g(K)).
We say that C/X is an algebraic unipotent quasi crossed module with additive feedback
deﬁned over K. Note that the Lie groups in this setup are G(R) and H(R). Also
note that exponential maps exp G : g→ G and exp H : h→ H are isomorphisms
of algebraic varieties deﬁned over K – this is because the Lie algebras h and g are
nilpotent.
The polyhedron I1 is deﬁned over Q. Suppose we are given a piecewise alge-
braic differential form
α∈ Ωp
pwa(I1(K))⊗K g(K).
It is not hard to show (using the ODE (5.5.2), and the fact that exp G is algebraic)
that the map g : I1→ G of (5.5.1) is piecewise algebraic and deﬁned over K. In
particular we get
g(1) = MI(α| I1)∈ G(K).
From this it follows that for any polyhedron X deﬁned over K, any
α∈ Ω1
alg(X(K))⊗K g(K)
and any piecewise algebraic string σ in X deﬁned over K, one has
MI(α| σ)∈ G(K).
We are led to make the following conjecture. A connection-curvature pairs
(α, β) is said to be algebraic if α∈ Ω1
alg(X(K))⊗K g(K) and α∈ Ω2
alg(X(K))⊗K
h(K).
Conjecture 9.4.1. Let C/X be an algebraic unipotent quasi crossed module with
additive feedback deﬁned over K, let (α, β) be an algebraic connection-curvature
pair in C/X, and let (σ, τ) be a piecewise algebraic kite in (X, x0). Then
MI(α, β| σ, τ)∈ H(K) .
It seems that the very recent paper [BGNT] may have a proof of this conjecture
in the special case when C/X is a crossed module and the 3-curvature of (α, β)
vanishes. See Subsection 5.5.
134 AMNON YEKUTIELI
9.5. A Conjecture on Descent Data. Suppose f is a cosimplicial nilpotent quan-
tum type DG Lie algebra, just like in Subsection 5.7. Take an MC element
˜ω ={ ˜ωp,q} in the Thom-Sullivan normalization ˜N(f). Then
˜ω0,0∈O (∆0)⊗ f0,1 = f0,1,
˜ω1,1∈ Ω1(∆1)⊗ f1,0
and
˜ω2,2∈ Ω2(∆2)⊗ f2,−1.
Let us write
ω := ˜ω0,0∈ f0,1
(this notation is different from the one on Subsection 5.7),
g := MI( ˜ω1,1| ∆1)∈ exp(f1,0)
and
a := MI( ˜ω2,1, ˜ω2,2| ∆2)∈ exp(f2,−1) ˜ω2,0(v0).
This last multiplicative integral takes place in the Lie quasi crossed module with
additive feedback
C ˜ω2,0(v0)/∆2 =
(
G, H ˜ω2,0(v0), Ψ, Φ ˜ω2,0(v0), Φ∆2
)
as in (5.7.1). In this way we assign to each ˜ω∈ MC( ˜N(f)) a triple
(9.5.1) MI ( ˜ω| ∆) := ( ω, g, a).
On the other hand, for every p the nilpotent quantum type DG Lie alge-
bra fp,· has its Deligne 2-groupoid Del(fp,·), also known as the Deligne crossed
groupoid; see [Ye5, Section 6]. The collection {Del(fp,·)}p∈N is then a cosimpli-
cial crossed groupoid. As explained in [Ye3, Section 5], there is the set of descent
data Desc(Del(f)), and its quotient set Desc(Del(f)).
Consider an MC element ˜ω∈ MC( ˜N(f)), and the triple MI ( ˜ω| ∆) = ( ω, g, a)
from (9.5.1). The 2-dimensional Stokes Theorem (Theorem 9.3.1) implies that
(ω, g, a) satisﬁes the “failure of 1-cocycle” condition of [Ye3, Deﬁnition 5.2]. The
3-dimensional Stokes Theorem (Theorem 9.3.5) implies that (ω, g, a) satisﬁes the
“twisted 2-cocycle” condition of loc. cit. This means that (ω, g, a)∈ Desc(Del(f)).
Recall that the quotient set of MC ( ˜N(f)) by the action of the gauge group
exp( ˜N(f)0) is denoted by MC( ˜N(f)).
Conjecture 9.5.2. Let f be a cosimplicial nilpotent quantum type DG Lie algebra.
Then the function
MI(−| ∆) : MC( ˜N(f))→ Desc(Del(f))
induces a bijection
MC( ˜N(f))→ Desc(Del(f)).
NONABELIAN MULTIPLICATIVE INTEGRATION 135
