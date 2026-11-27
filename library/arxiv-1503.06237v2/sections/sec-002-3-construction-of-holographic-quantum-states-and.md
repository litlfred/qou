---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-002-3-construction-of-holographic-quantum-states-and
section_title: "Construction of holographic quantum states and codes"
section_number: 3
pages: 8-11
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
We have seen how tensors can be interpreted as quantum states or quantum codes. In
this section we construct tensor networks in which the fundamental building blocks are
perfect tensors. Our tensor networks describe states which we call holographic states,
and codes which we call holographic codes.
We shall focus on examples based on tilings of two-dimensional hyperbolic space,
which are speciﬁc realizations of uniform hyperbolic tilings known as hyperbolic tes-
sellations. These tilings have desirable symmetries for constructing a toy model of
the AdS/CFT correspondence. In particular they are discretely scale-invariant, and
there exist graph isomorphisms that bring any point in the graph to the center while
preserving the local structure of the tiling. 2 The machinery we develop may also be
straightforwardly applied to non-uniform and higher-dimensional graphs.
Let’s ﬁrst consider a uniform tiling of a two-dimensional hyperbolic space by
hexagons, with four hexagons adjacent at each vertex, as depicted in Fig 4a. A perfect
tensor with six legs is placed at each hexagon, and legs of perfect tensors are contracted
with neighboring tensors at shared edges of the hexagons. We associate physical spins
with the uncontracted open tensor legs on the boundary of the hyperbolic tiling; the
2Such transformations can be directly visualized using Kaleidotile software [32], which is freely
available and has been of great aid in developing geometric intuition and producing ﬁgures of uniform
hyperbolic tilings in this paper.
– 6 –
(a) Holographic hexagon state
 (b) Holographic pentagon code
Figure 4 . White dots represent physical legs on the boundary. Red dots represent logical
input legs associated to each perfect tensor.
tensor network corresponds to a pure state of these boundary spins, which we call a
holographic state. Note that perfect tensors are not necessarily symmetric under all the
possible permutations of tensor legs, and thus we specify some particular ordering of
tensor legs in the construction.
We may similarly attach a state interpretation to more general networks con-
structed by contracting perfect tensors:
Deﬁnition 3. Consider a tensor network composed of perfect tensors which cover some
geometric manifold with boundary, where all the interior tensor legs are contracted. A
holographic state is a state interpretation of such a tensor network, where physical
degrees of freedom are associated with all uncontracted legs at the boundary of the
manifold.
We now provide an example of a holographic quantum code. As in a holographic
state, we consider a uniform tiling of the hyperbolic disc, this time by pentagons, with
four pentagons adjacent at each vertex. A perfect tensor with six legs is placed at each
pentagon, so that each tensor has one additional uncontracted open leg. This additional
tensor leg is interpreted as a bulk index or logical input for the tensor network (see
Fig. 4b). The entire system can be viewed as a big tensor with logical legs in the bulk
and physical legs on the boundary. We then have the following theorem:
Theorem 1. The pentagon-tiling tensor network is an isometric tensor from the bulk
to the boundary. We call it the holographic pentagon code.
– 7 –
We can prove this theorem by noting that if we order the tensors into layers la-
beled by increasing graph distance from the center, each tensor has at most two legs
contracted with the tensors at the previous layer (this property is a consequence of
the “negative curvature” of the graph). Therefore, even if we regard the pentagon’s
bulk logical index as an input leg, the total number of input legs is at most three, and
we may therefore regard each tensor as an isometry from input legs to output legs.
Applying the perfect tensors layer by layer, and recalling that the product of isometries
is an isometry, we obtain an isometry mapping all the logical indices in the bulk to the
physical indices on the boundary.
We can view this isometry as the encoding transformation of a quantum error-
correcting code, which we call a holographic code. The number of logical v-dimensional
spins is the number Nbulk of pentagons in the tiling, and the number of physical v-
dimensional spins in the code block is the number Nboundary of uncontracted boundary
indices in the tensor network. We show in Appendix C that the rate of the code,
meaning the ratio of the number of logical spins to the number of physical spins,
approaches
Nbulk
Nboundary
→ 1√
5≈.447 (3.1)
in the limit of a large number of layers.
This pentagon code was constructed by successively adding layers of tensors start-
ing from the center and stopping after repeating this procedure a certain number of
times (two layers in ﬁgure 4b). Alternatively, we may ﬁll the bulk using a non-uniform
cutoﬀ, so that the graph distance between the “center” and the boundary varies from
one portion of the boundary to another (as occurs in ﬁgure 4a). By exerting this free-
dom, we may change the corresponding value 3.1 for the rate of the code and even
slightly increase it. By varying the choice of perfect tensor and the shape of the cutoﬀ,
a large family of holographic codes can be constructed:
Deﬁnition 4. Consider a tensor network composed of perfect tensors which cover
some geometric manifold with boundaries. The tensor network is called a holographic
code if it gives rise to an isometric map from uncontracted bulk legs to uncontracted
boundary legs.
Tensor networks with open legs in the bulk were ﬁrst proposed by Vidal [17]. More
recently, Qi [28] constructed a tensor-tree model with an exact unitary mapping between
the bulk and the boundary. The most important diﬀerence between their models and
ours is that their states are not protected against erasure of physical spins because the
code rate is asymptotically unity. In addition our models are more symmetric; since
– 8 –
perfect tensors can be interpreted as isometries along any direction, our models have no
preferred direction in the bulk and all bulk sites are treated equally. In particular, the
pentagon code has the nice feature that, because the 6-leg perfect tensor we construct
in appendix A is symmetric under cyclic permutations of ﬁve of the legs, which we take
to be the contracted legs, the symmetry of the network is just the full symmetry of the
graph.
