---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-023-b-proof-of-rt-for-negatively-curved-planar-graph
section_title: "B Proof of RT for negatively curved planar graphs"
section_number: null
pages: 47-50
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
As we have presented in eq. 4.4, there is an upper bound on the amount of entanglement
a tensor network state can have based on the minimal cut γA dividing the network into
two tensors P and Q. In this section, we will explain how to guarantee that this
upper bound is saturated for connected regions in a certain class of holographic states.
Namely, we shall focus on holographic states associated to planar graphs with non-
positive curvature.
We argued that proving the RT formula amounts to showing that the tensors P
and Q can be interpreted as unitary transformations, from the minimal geodesic cut
γA together with some subregion of A orAc to the rest of A orAc respectively. We will
show that this is indeed the case by giving unitary circuit interpretations to the tensor
networks for each of them.
Indeed, the following are necessary and suﬃcient conditions for a circuit interpre-
tation of a network of perfect tensors:
• Covering: Each edge (contracted or uncontracted index) is assigned a direction-
ality.
• Flow: Each tensor has an equal number of incoming and outgoing indices.
• Acyclic: The resulting directionality has no closed cycles (no loops).
The covering condition is necessary to interpret the direction in which each tensor in
the network processes information by having well deﬁned inputs and outputs. The ﬂow
condition is necessary for the interpretation of every tensor to be that of a unitary
gate. The acyclic condition is non-local and guarantees that the order of application of
the operations in the network is consistent, where an inconsistency may be thought of
as the presence of closed time-like curves in the circuit picture. These conditions are
enough to show that the interpretation is that of a unitary quantum circuit.
One additional condition is required in order to prove the saturation of the RT
entanglement entropy, for a simply connected boundary region A.
• Equal time interpretation: The minimal cutγA is crossed in the same direction
by the directed interpretation of each link that it cuts.
This condition allows viewing the geodesic as an “equal time” curve in the unitary
circuit interpretation of the tensor network.
Let us ﬁrst describe the construction for the circuit interpretation. The steps may
be readily visualized in ﬁgure 19a.
– 45 –
In a planar graph we can associate a minimal cut γA to a path through the dual
graph, and since we are taking A to be connected, this path will also be connected. We
may associate two nodes in the dual lattice at the end points of a simply connected
boundary region A, which will also be the endpoints of γA in the dual lattice. We will
take one of these nodes to be the starting node and label it 0. We may then label all
other nodes in the dual lattice according to the distance (number of steps/cuts) from
the starting node. Since γA is a minimal geodesic, this labeling monotonically increases
along the nodes it traverses.
We may now assign an orientation to edges (contracted indices) in the tensor net-
work. The orientation is chosen such that, from the two adjacent nodes of the dual
lattice, the node with higher label is always found to the right. This orientation may
be interpreted as the direction of “ﬂow of information” through the circuit.
We now argue that this orientation gives a unitary circuit interpretation forP (and
thus for Q by exchanging A and Ac). We emphasize that the argument rests on the
following assumptions about the graph:
• Planar embedding: The tensor network may be laid out in a planar fashion
with the boundary of the network corresponding to a simple boundary on the
embedding.
• Perfect tensors: Tensors in the network have an even number of legs and are
unitary along any balanced distribution of the legs.
• Curvature: The network is expected to represent an AdS bulk and thus is
expected to have the discrete analogue of negative curvature. We have not tried
to deﬁne this idea in general, but the aspect of it we need here is that the distance
function between two nodes of the network has no local maxima away from the
boundary.
We have already used the planar embedding assumption implicitly by constructing
the dual lattice and referring to right and left. It is however less obvious that we
have also made a restricted use of the perfect tensor assumption. Namely, we have
used the fact that each tensor has an even number of legs. Because of this, the dual
lattice is bipartite. In other words, nodes may be labeled with two “colors” which
we shall conveniently call ‘even’ and ‘odd’ such that two nodes of the same color are
never adjacent. In particular, the parity of the distance labeling coincides with the
“color”. Hence, two neighboring nodes can not have the same value label making the
directionality of the tensor index between them always be well deﬁned (i.e. satisﬁes
covering condition).
– 46 –
To ensure the ﬂow condition, it suﬃces to count the number of incoming indices
minus the number of outgoing indices and verify that this value is zero. Due to the
triangle inequality, and the bipartite nature, labels for neighboring nodes can only diﬀer
by one. Hence, the diﬀerence between the number of outgoing and incoming indices
for any tensor in the network is given by ∑2n
j=1 (fj+1−fj) = 0, where fj are the labels
associated to the 2n nodes immediately surrounding the tensor taken in cyclic order.
The acyclic condition is a bit more subtle since it is a non-local property. We
will prove that the presence of a cycle in this context implies the existence of an
interior local maximum for the labeling. Let us assume that our construction produces
some cycle C in the tensor network. Depending on the orientation of C (clockwise or
counterclockwise), the the node label values immediately to the interior of the loop will
be larger or smaller than those immediately to the exteriors. In the counterclockwise
case, we may chose a node in the interior of C with lowest possible label. The label for
this node is smaller than those of all its neighbors, including those in the exterior of C,
(a) Circuit interpretation construction
 (b) Bulk operator reconstruction circuit
Figure 19 . Here we illustrate how to construct a unitary circuit interpretation of a holo-
graphic state which witnesses the RT entanglement for a simply connected boundary region.
(a) The following steps for the construction are illustrated: i) Label the node located at one
end of the boundary as 0. ii) Label all other nodes according to the distance from this node.
iii) Direct all tensor indices such that the larger label lies to the right. (b) In the example,
the circuit interpretation for the network has depth 12. For this reason we provide a full se-
quential presentation of the circuit interpretation along one side of the geodesic, condensing
the remaining 7 gates into UAc. Note that there are outputs that are produced directly by
UA, without going through UAc as well as inputs that are fed directly to UAc without going
through UA.
– 47 –
Figure 20 . The ﬁrst few levels of the unwrapped pentagon code. The dangling logical legs
are not shown, and the “hollow” lines and dots are identiﬁed with the solid ones on the other
side. The tensors in the top row have all remaining non-logical legs extended outwards and
treated as physical qubits.
which contradicts the assumption that it is deﬁned based on a graph distance function.
In the clockwise case, we may choose a node in the interior ofC with the largest possible
label. In this case the label for this node is larger than that of all its neighbors, including
those outside ofC. In other words, we have found an interior maximum for the distance
function. This is in contradiction with our stand-in assumption associated to negatively
curved surface homeomorphic to the disc, which leads us to the conclusion that our
construction produces no loops.
Finally, it is straightforward to show that the geodesicγA can be provided an equal
time interpretation in the circuit. Firstly, it completely splits the circuits in two parts.
Secondly, the direction associated to all contracted indices crossed by γA is uniform
since the nodes it transverses are by deﬁnition labeled in strict ascending order.
