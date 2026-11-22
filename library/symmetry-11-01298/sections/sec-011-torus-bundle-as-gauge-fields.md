---
doc_id: symmetry-11-01298
doc_title: "Braids, 3-Manifolds, Elementary Particles: Number Theory and Symmetry in Particle Physics"
section_id: sec-011-torus-bundle-as-gauge-fields
section_title: "Torus Bundle as Gauge Fields"
section_number: null
pages: 13-16
source_pdf: symmetry-11-01298.pdf
source_sha256: 595648c84501e8a6
toc_source: outline
doc_brief: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics — In this paper, we will describe a topological model for elementary par- ticles based on 3-manifolds."
duplicate_of: "arxiv-1910.09966v1"
---
Now, we have the following situation: two knot complements C(K1) and C(K2) can be connected
by a so-called tube T(K1, K2) along the boundary, a torus. This tube T(K1, K2) can be described by
the complement of a link with two components deﬁned by the knots K1, K2. In the simplest case, it is
the 3-manifold T2 × [0, 1]. The knot complements are fermions. Therefore, both knot complements
have to carry a hyperbolic structure, i.a. a space of constant negative curvature. The frame bundle of
a 3-manifold is always trivial, so that we need a ﬂat connection of this bundle to describe this space.
Let Isom(H3) = SO(3, 1) be the isometry group of the three-dimensional hyperbolic space. There are
suitable subgroups G1, G2 ⊂Isom(H3) so that (the interior of)C(K1) is diffeomorphic to Isom(H3)/G1
(and similar with C(K2)). As usual, the space of all ﬂat SO(3, 1) connections of C(K1) is the space of
all representations π1(C(K1)) →SO(3, 1), where SO(3, 1) acts in the adjoint representation on this
space (as gauge transformations). We note the fact that every SO(3, 1) connections lifts uniquely to a
SL(2, C) connection. Now, near the boundary, we have a ﬂat SL(2, C) connection in C(K1) which is
connected to a ﬂat SL(2, C) connection in C(K2) by T(K1, K2). The action for a ﬂat connection A with
Symmetry 2019, 11, 1298
14 of 26
values in the Lie algebra g of the Lie group G as a subgroup of the SL(2, C) in a 3-manfold Σ (with
vanishing curvature F = DA = 0) is given by
ˆ
Σ
A ∧F
also known as background ﬁeld model (BF model). By a small redeﬁnition of the connection, one can
also choose the Chern–Simons action:
CS(A, Σ) =
ˆ
Σ

A ∧dA + 2
3 A ∧A ∧A

.
The variation of the Chern–Simons action CS(A, Σ) gets ﬂat connections DA = 0 as solutions. The
ﬂow of solutions A(t) in T(K1, K2) × [0, 1] (parametrized by the variable t) between the ﬂat connection
A(0) in T(K1, K2) × {0} to the ﬂat connection A(1) in T(K1, K2) × {1} will be given by the gradient
ﬂow equation (see [54] for instance)
d
dt A(t) = ± ∗F(A) = ± ∗DA,
(19)
where the coordinate t is normal to T(K1, K2). Therefore, we are able to introduce a connection ˜A in
T(K1, K2) × [0, 1] so that the covariant derivative in the t-direction agrees with ∂/∂t. Then, we have for
the curvature ˜F = D ˜A where the fourth component is given by ˜F4µ = d ˜Aµ/dt. Thus, we will get the
instanton equation with (anti-)self-dual curvature
˜F = ± ∗˜F .
However, now we have to extend the Chern–Simons action (of the 3-manifold) to the 4-manifold. It
follows that
CS(A, T(K1, K2) × {1}) −CS(A, T(K1, K2) × {0}) =
ˆ
T(K1,K2)×[0,1]
tr( ˜F ∧˜F)
i.e., we obtain the second Chern class and ﬁnally
SEH([0, 1] × T(K1, K2)) =
ˆ
T(K1,K2)×[0,1]
tr( ˜F ∧˜F) = ±
ˆ
T(K1,K2)×[0,1]
tr( ˜F ∧∗˜F)
i.e., the action of the gauge ﬁeld. The whole procedure remains true for an extension, i.e.,
SEH(R × T(K1, K2)) = ±
ˆ
T(K1,K2)×R
tr( ˜F ∧∗˜F) .
(20)
The gauge ﬁeld action (20) is only deﬁned along the tubes T(K1, K2). For the extension of the action to
the whole 4-manifold M, we need some non-trivial facts from the theory of 3-manifolds. We presented
the ideas in [32]. Finally, we obtain the gauge ﬁeld action
ˆ
M
tr( ˜F ∧∗˜F).
(21)
Now, we will discuss the possible gauge group. Again, for completeness, we will present the
argumentation in [32] again. The gauge ﬁeld in the action (21) has values in the Lie algebra of
Symmetry 2019, 11, 1298
15 of 26
the maximal compact subgroup SU(2) of SL(2, C). However, in the derivation of the action, we used
the connecting tube T(K1, K2) between two tori, which is a cobordism. This cobordism T(K1, K2) is
also known as torus bundle (see [55] Theorem 1.15), which can be always decomposed into three
elementary pieces—ﬁnite order, Dehn twist and the so-called Anosov map (named after the russian
mathematician Dmitri Anosov).
The idea of this construction is very simple: one starts with two trivial cobordisms T2 × [0, 1]
and glues them together by using a diffeomorphism g : T2 →T2, which we call gluing diffeomorphism.
From the geometrical point of view, we have to distinguish between three different types of torus
bundles. The three types of torus bundles are distinguished by the splitting of the tangent bundle:
•
ﬁnite order (orders 2, 3, 4, 6): the tangent bundle is three-dimensional,
•
Dehn-twist (left/right twist):
the tangent bundle is a sum of a two-dimensional and a
one-dimensional bundle,
•
Anosov: the tangent bundle is a sum of three one-dimensional bundles.
Following Thurston’s geometrization program (see [56]), these three torus bundles are admitting
a geometric structure, i.e., it has a metric of constant curvature.
Apart from this geometric
properties, all torus bundles are determined by the gluing diffeomorphism g : T2 →T2, which
also determines the fundamental group of the torus bundle. Therefore, this gluing diffeomorphism
also has an inﬂuence on the structure of the diffeomorphism group of the torus bundle, which will be
discussed now. From the physical point of view, we have two types of diffeomorphisms: local and
global. Any coordinate transformation can be described by an inﬁnitesimal or local diffeomorphism
(coordinate transformation). In contrast, there are global diffeomorphisms like an orientation reversing
diffeomorphism. Two diffeomorphisms not connected via a sequence of local diffeomorphism are part
of different connecting components of the diffeomorphism group, i.e., the set of isotopy classes
π0(Di f f (M)) (also called the mapping class group).
Isotopy classes are important in order to
understand the conﬁguration space topology of general relativity (see Giulini [57]). In principle,
the state space in geometrodynamics is the set of all isotopy classes, where every class represents one
physical situation, or isotopy classes label two different physical situations. By deﬁnition, the two
3-manifolds in different isotopy classes cannot be connected by a sequence of local diffeomorphisms
(local coordinate transformations). Again, these two different isotopy classes represent two different
physical situations; see [13] for the relation of isotopy classes to particle properties like spin. In
case of the torus bundle, we consider the isotopy classes π0(Di f f (M, ∂M)) relative to the boundary
represented by the automorphisms of the fundamental group. Using the geometrization program, we
obtain a relation between the isotopy classes π0(Di f f (M, ∂M)) and the isometry classes (connecting
components of the isometry group) with respect to the geometric structure of the torus bundle (see, for
instance, [58,59]). Then, the isotopy classes of the torus bundles are given by
•
ﬁnite order: 2 isotopy classes (= no/even twist or odd twist),
•
Dehn-twist: 2 isotopy classes (= left or right Dehn twists),
•
Anosov: 8 isotopy classes (= all possible orientations of the three line bundles forming the tangent
bundle).
From the geometrical point of view, we can rearrange the scheme above:
•
torus bundle with no/even twists: one isotopy class,
•
torus bundle with twist (Dehn twist or odd ﬁnite twist): three isotopy classes,
•
torus bundle with Anosov map: eight isotopy classes.
This information creates a starting point for the discussion on how to derive the gauge group.
Given a Lie group G with Lie algebra g, the rank of g is the dimension of the maximal abelian
subalgebra, also called Cartan algebra (see above for a deﬁnition). It is the same as the dimension of the
maximal torus Tn ⊂G. The curvature F of the gauge ﬁeld takes values in the adjoint representation
Symmetry 2019, 11, 1298
16 of 26
of the Lie algebra and the action tr(F ∧∗F) forms an element of the Cartan subalgebra (the Casimir
operator). However, each isotopy class contributes to the action and therefore we have to take the sum
over all possible isotopy classes. Let ta be the generator in the adjoint representation; then, we obtain
for the Lie algebra part of the action tr(F ∧∗F)
•
torus bundle with no twists: one isotopy class with t2,
•
torus bundle with twist: three isotopy classes with t2
1 + t2
2 + t2
3,
•
torus bundle with Anosov map: eight isotopy classes with ∑8
a=1 t2
a.
The Lie algebra with one generator t corresponds uniquely to the Lie group U(1) where the three
generators t1, t2, t3 form the Lie algebra of the SU(2) group. Then, the last case with eight generators
ta has to correspond to the Lie algebra of the SU(3) group. We remark the similarity with an idea from
brane theory: n parallel branes (each decorated with an U(1) theory) are described by an U(n) gauge
theory (see [60]). Finally, we obtain the maximal group U(1) × SU(2) × SU(3) as a gauge group for all
possible torus bundles (in the model: connecting tubes between the solid tori).
At the end, we will speculate about the identiﬁcation of the isotopy classes for the torus bundle
with the vector bosons in the gauge ﬁeld theory. Obviously, the isotopy class of the torus bundle
with no twist must be the photon. Then, the isotopy class of the other bundle of ﬁnite order should
be identiﬁed with the Z0 boson and the two isotopy classes of the Dehn twist bundles are the W±
bosons. Here, we remark that this identiﬁcation is consistent with the deﬁnition of the charge lateron.
Furthermore, we remark that this scheme contains automatically the mixing between the photon and
the Z0 boson (the corresponding torus bundle are both of ﬁnite order). The isotopy classes of the
Anosov map bundle have to correspond to the eight gluons. Later, we expect that these ideas will lead
to an additional relation for the scattering amplitudes induced by the geometry of the torus bundles.
