---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-011-53-bulk-reconstruction-from-tensor-pushing
section_title: "Bulk reconstruction from tensor pushing"
section_number: 5.3
pages: 25-27
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
We now explain how holographic codes realize the AdS-Rindler reconstruction of ﬁgure
11. The basic idea is that, instead of using the full isometry of the entire network
to push a local bulk operator to the boundary, we can instead successively push it
through individual perfect tensors in a manner of our choosing by using the operation of
ﬁgure 2. We illustrate the reconstruction for two diﬀerent bulk points of the pentagon
code in ﬁgure 12. Here we use the deﬁning property of perfect tensors — that the
– 23 –
tensor provides a unitary transformation which maps any three legs of the tensor to
the complementary set of three legs, and therefore also an isometry mapping any set
of three or fewer “incoming” legs to any disjoint set of three “outgoing” legs. In ﬁgure
12, each bulk vertex with arrows showing incoming and outgoing directions indicates
such an isometry, and the complete set of blue legs is a product of such isometries, and
hence also an isometry. The blue operator on the boundary is obtained by conjugating
the blue bulk operator by the blue isometry, and the same applies to the green bulk
and boundary operators. In the construction of the isometry, we regard the dangling
bulk index on each tensor as an incoming index, and therefore require that no more
than two contracted indices are incoming for each blue (or green) tensor. The same
blue isometry, then, can be used to push not just the central blue bulk index to the
boundary, but also any of the other incoming bulk indices (which are not shown in the
ﬁgure) on blue tensors.
Figure 12 . Boundary reconstruction of bulk operators. The blue operator on the central
bulk leg is pushed to an operator supported on a fairly large boundary region, while the
green bulk operator further from the center is pushed to an operator supported on a smaller
boundary region. Bulk legs for the other tensors are not shown.
The boundary operation corresponding to a given bulk local operator manifestly has
the non-uniqueness we described in our discussion of the AdS-Rindler reconstruction.
For example, we could move one of the three blue arrows directed outward from the
central blue vertex to a diﬀerent edge, thus reconstructing the central bulk operator
on a diﬀerent boundary region, or we could have sent the green arrows in the opposite
– 24 –
direction and reconstructed the green bulk operator on a considerably larger boundary
region on the opposite side. No matter which reconstruction we use, the boundary
operator is obtained from the isometric embedding of the bulk indices into the code
subspace of the boundary Hilbert space, and therefore each reconstructed operator
corresponding to a given bulk operator acts on the code subspace in the same way.
In the theory of quantum error-correcting codes, we say that an error is an erasure
(or equivalently a located error) if the set of spins damaged by the error is known,
so this information can be used in recovering from the error. Holographic codes also
provide protection against errors which act at unknown locations on the boundary,
but for the purpose of developing the analogy with the AdS/CFT correspondence we
will focus on protecting against erasure. A logical system can be protected against
erasure of a set of spins in the code block if the full algebra of logical operations has
a realization supported on the complementary set of unerased spins. In AdS/CFT we
might only require reconstruction of a subalgebra of the full logical algebra; for example,
the pentagon code provides better protection for the degrees of freedom deep within the
bulk than for those closer to the boundary. The framework in which a quantum code
protects only a subalgebra of the code’s full logical algebra has been called operator
algebra quantum error correction [36–39].
