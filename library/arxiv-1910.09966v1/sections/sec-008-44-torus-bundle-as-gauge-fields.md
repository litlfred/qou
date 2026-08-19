---
doc_id: arxiv-1910.09966v1
doc_title: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics"
section_id: sec-008-44-torus-bundle-as-gauge-fields
section_title: "Torus Bundle as Gauge Fields"
section_number: 4.4
pages: 18-22
source_pdf: 1910.09966v1.pdf
source_sha256: 21798500c98ed25a
doc_brief: "Braids, 3-manifolds, elementary particles: number theory and symmetry in particle physics — In this paper, we will describe a topological model for elementary par- ticles based on 3-manifolds."
---
Now, we have the following situation: two knot complementsC(K1) andC(K2)
can be connected by a so-called tube T (K1,K 2) along the boundary, a torus.
This tube T (K1,K 2) can be described by the complement of a link with two
components deﬁned by the knots K1,K 2. In the simplest case, it is the 3-
manifold T 2× [0, 1]. The knot complements are fermions. Therefore, both
knot complements have to carry a hyperbolic structure, i.a. a space of constant
negative curvature. The frame bundle of a 3-manifold is always trivial, so that
we need a ﬂat connection of this bundle to describe this space. Let Isom(H3) =
SO(3, 1) be the isometry group of the three-dimensional hyperbolic space. There
are suitable subgroups G1,G 2⊂ Isom(H3) so that (the interior of) C(K1) is
diﬀeomorphic to Isom(H3)/G1 (and similar with C(K2)). As usual, the space
of all ﬂat SO(3, 1) connections of C(K1) is the space of all representations
π1(C(K1))→ SO(3, 1), where SO(3, 1) acts in the adjoint representation on
this space (as gauge transformations). We note the fact that every SO(3, 1)
connections lifts uniquely to aSL(2, C) connection. Now, near the boundary, we
have a ﬂat SL(2, C) connection in C(K1) which is connected to a ﬂat SL(2, C)
connection in C(K2) by T (K1,K 2). The action for a ﬂat connection A with
values in the Lie algebra g of the Lie group G as a subgroup of the SL(2, C) in
a 3-manfold Σ (with vanishing curvature F =DA = 0) is given by
ˆ
Σ
A∧F
also known as background ﬁeld model (BF model). By a small redeﬁnition of
the connection, one can also choose the Chern–Simons action:
CS(A, Σ) =
ˆ
Σ
(
A∧dA + 2
3A∧A∧A
)
.
The variation of the Chern–Simons actionCS(A, Σ) gets ﬂat connectionsDA =
0 as solutions. The ﬂow of solutions A(t) inT (K1,K 2)× [0, 1] (parametrized by
the variable t) between the ﬂat connection A(0) in T (K1,K 2)×{ 0} to the ﬂat
18
connectionA(1) in T (K1,K 2)×{ 1} will be given by the gradient ﬂow equation
(see [54] for instance)
d
dtA(t) =±∗ F (A) =±∗ DA, (19)
where the coordinate t is normal to T (K1,K 2). Therefore, we are able to in-
troduce a connection ˜A in T (K1,K 2)× [0, 1] so that the covariant derivative
in the t-direction agrees with ∂/∂t. Then, we have for the curvature ˜F = D ˜A
where the fourth component is given by ˜F4µ = d ˜Aµ/dt. Thus, we will get the
instanton equation with (anti-)self-dual curvature
˜F =±∗ ˜F.
However, now we have to extend the Chern–Simons action (of the 3-manifold)
to the 4-manifold. It follows that
CS(A,T (K1,K 2)×{ 1})−CS(A,T (K1,K 2)×{ 0}) =
ˆ
T(K1,K2)×[0,1]
tr( ˜F∧ ˜F )
i.e., we obtain the second Chern class and ﬁnally
SEH ([0, 1]×T (K1,K 2)) =
ˆ
T(K1,K2)×[0,1]
tr( ˜F∧ ˜F ) =±
ˆ
T(K1,K2)×[0,1]
tr( ˜F∧∗ ˜F )
i.e., the action of the gauge ﬁeld. The whole procedure remains true for an
extension, i.e.,
SEH (R×T (K1,K 2)) =±
ˆ
T(K1,K2)×R
tr( ˜F∧∗ ˜F ). (20)
The gauge ﬁeld action (20) is only deﬁned along the tubes T (K1,K 2). For the
extension of the action to the whole 4-manifold M, we need some non-trivial
facts from the theory of 3-manifolds. We presented the ideas in [32]. Finally,
we obtain the gauge ﬁeld action
ˆ
M
tr( ˜F∧∗ ˜F ). (21)
Now, we will discuss the possible gauge group. Again, for completeness, we will
present the argumentation in [32] again. The gauge ﬁeld in the action (21) has
values in the Lie algebra of the maximal compact subgroup SU (2) of SL(2, C).
However, in the derivation of the action, we used the connecting tubeT (K1,K 2)
between two tori, which is a cobordism. This cobordismT (K1,K 2) is also known
as torus bundle (see [55] Theorem 1.15), which can be always decomposed into
three elementary pieces—ﬁnite order, Dehn twist and the so-called Anosov map
(named after the russian mathematician Dmitri Anosov).
19
The idea of this construction is very simple: one starts with two trivial
cobordisms T 2× [0, 1] and glues them together by using a diﬀeomorphism g :
T 2→T 2, which we call gluing diﬀeomorphism. From the geometrical point of
view, we have to distinguish between three diﬀerent types of torus bundles. The
three types of torus bundles are distinguished by the splitting of the tangent
bundle:
• ﬁnite order (orders 2, 3, 4, 6): the tangent bundle is three-dimensional,
• Dehn-twist (left/right twist): the tangent bundle is a sum of a two-
dimensional and a one-dimensional bundle,
• Anosov: the tangent bundle is a sum of three one-dimensional bundles.
Following Thurston’s geometrization program (see [56]), these three torus
bundles are admitting a geometric structure, i.e., it has a metric of constant
curvature. Apart from this geometric properties, all torus bundles are deter-
mined by the gluing diﬀeomorphism g : T 2→ T 2, which also determines the
fundamental group of the torus bundle. Therefore, this gluing diﬀeomorphism
also has an inﬂuence on the structure of the diﬀeomorphism group of the torus
bundle, which will be discussed now. From the physical point of view, we have
two types of diﬀeomorphisms: local and global. Any coordinate transformation
can be described by an inﬁnitesimal or local diﬀeomorphism (coordinate trans-
formation). In contrast, there are global diﬀeomorphisms like an orientation
reversing diﬀeomorphism. Two diﬀeomorphisms not connected via a sequence
of local diﬀeomorphism are part of diﬀerent connecting components of the dif-
feomorphism group, i.e., the set of isotopy classes π0(Diff (M)) (also called the
mapping class group). Isotopy classes are important in order to understand the
conﬁguration space topology of general relativity (see Giulini [57]). In princi-
ple, the state space in geometrodynamics is the set of all isotopy classes, where
every class represents one physical situation, or isotopy classes label two diﬀer-
ent physical situations. By deﬁnition, the two 3-manifolds in diﬀerent isotopy
classes cannot be connected by a sequence of local diﬀeomorphisms (local coor-
dinate transformations). Again, these two diﬀerent isotopy classes represent two
diﬀerent physical situations; see [13] for the relation of isotopy classes to particle
properties like spin. In case of the torus bundle, we consider the isotopy classes
π0(Diff (M,∂M )) relative to the boundary represented by the automorphisms
of the fundamental group. Using the geometrization program, we obtain a re-
lation between the isotopy classes π0(Diff (M,∂M )) and the isometry classes
(connecting components of the isometry group) with respect to the geometric
structure of the torus bundle (see, for instance, [58, 59]). Then, the isotopy
classes of the torus bundles are given by
• ﬁnite order: 2 isotopy classes (= no/even twist or odd twist),
• Dehn-twist: 2 isotopy classes (= left or right Dehn twists),
• Anosov: 8 isotopy classes (= all possible orientations of the three line
bundles forming the tangent bundle).
20
From the geometrical point of view, we can rearrange the scheme above:
• torus bundle with no/even twists: one isotopy class,
• torus bundle with twist (Dehn twist or odd ﬁnite twist): three isotopy
classes,
• torus bundle with Anosov map: eight isotopy classes.
This information creates a starting point for the discussion on how to derive
the gauge group. Given a Lie group G with Lie algebra g, the rank of g is
the dimension of the maximal abelian subalgebra, also called Cartan algebra
(see above for a deﬁnition). It is the same as the dimension of the maximal
torus Tn⊂ G. The curvature F of the gauge ﬁeld takes values in the adjoint
representation of the Lie algebra and the action tr(F∧∗F ) forms an element
of the Cartan subalgebra (the Casimir operator). However, each isotopy class
contributes to the action and therefore we have to take the sum over all possible
isotopy classes. Let ta be the generator in the adjoint representation; then, we
obtain for the Lie algebra part of the action tr(F∧∗F )
• torus bundle with no twists: one isotopy class with t2,
• torus bundle with twist: three isotopy classes with t2
1 +t2
2 +t2
3,
• torus bundle with Anosov map: eight isotopy classes with ∑8
a=1t2
a.
The Lie algebra with one generator t corresponds uniquely to the Lie group
U(1) where the three generators t1,t 2,t 3 form the Lie algebra of the SU (2)
group. Then, the last case with eight generators ta has to correspond to the Lie
algebra of the SU (3) group. We remark the similarity with an idea from brane
theory: n parallel branes (each decorated with an U(1) theory) are described
by an U(n) gauge theory (see [60]). Finally, we obtain the maximal group
U(1)×SU (2)×SU (3) as a gauge group for all possible torus bundles (in the
model: connecting tubes between the solid tori).
At the end, we will speculate about the identiﬁcation of the isotopy classes
for the torus bundle with the vector bosons in the gauge ﬁeld theory. Obviously,
the isotopy class of the torus bundle with no twist must be the photon. Then,
the isotopy class of the other bundle of ﬁnite order should be identiﬁed with the
Z0 boson and the two isotopy classes of the Dehn twist bundles are the W±
bosons. Here, we remark that this identiﬁcation is consistent with the deﬁnition
of the charge lateron. Furthermore, we remark that this scheme contains auto-
matically the mixing between the photon and the Z0 boson (the corresponding
torus bundle are both of ﬁnite order). The isotopy classes of the Anosov map
bundle have to correspond to the eight gluons. Later, we expect that these ideas
will lead to an additional relation for the scattering amplitudes induced by the
geometry of the torus bundles.
21
Figure 7: Branching sets— Left: 6-Plat for the knot cpomplement, Center: a
3-Braid as 6-Braid as example, Right: 6-Braid for the link complement
