---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-017-6-black-holes-and-holography
section_title: "Black holes and holography"
section_number: 6
pages: 40-41
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
In holographic codes, bulk operators are reconstructed only on a subspace of the bound-
ary Hilbert space. This may seem troubling, since the holographic correspondence is
supposed to assign a bulk interpretation to all possible states on the boundary. A
resolution of this confusion was proposed in [1] — a particular bulk operator might not
always be reconstructable because it lies deep inside a black hole for most boundary
states.7 In fact we can see this directly in our models if we incorporate black holes in
a manner that we now describe.
To illustrate the idea, consider the pentagon code, but with the central tensor
removed. The central tensor’s one free bulk index has been replaced by ﬁve bulk
indices, those which had previously been contracted with legs of the missing pentagon;
the tensor network now provides an isometry mapping these ﬁve indices, together with
the bulk legs on the remaining pentagons, to the boundary. Thus the code subspace
of the boundary Hilbert space is larger than for the pure pentagon code. We interpret
this enlarged code space as describing conﬁgurations of the bulk with a black hole in
the center, whose microstate is determined by the input to the new bulk legs. The
entropy of the black hole is the logarithm of the dimension of the Hilbert space of black
hole microstates, or
SBH = log2
(
25− 2
)
≈ 4.9, (6.1)
since only four of the bulk spins are new and we shouldn’t count states that were part
of the original pentagon code subspace. We depict this construction in ﬁgure 18a.
We can construct larger black holes by removing more central layers of the network;
it is clear that their entropy scales with their horizon area, as predicted by Bekenstein
and Hawking [49, 50]. As the black hole grows, the number of bulk legs outside the
black hole decreases, so we can reconstruct fewer and fewer bulk local operators. Even-
tually the black hole eats up the entire network, and our isometry becomes trivial (and
unitary). Thus our model really does assign a bulk interpretations to all boundary
states, as demanded by AdS/CFT — most boundary states correspond to large black
holes in the bulk.
7We are currently agnostic about the reconstruction of bulk operators just inside the horizon, which
must be needed in some form to describe the experience of an infalling observer. This is a topic of
much recent controversy [47, 48], but we will not take sides here.
– 38 –
(a) Black hole
horizon
black hole
A
B wormhole
(a) (b) (b) Wormhole
Figure 18 . A black hole in a holographic code, and the corresponding wormhole geometry.
It is amusing to note that we can also describe conﬁgurations corresponding to
the two-sided wormhole of [2]; we just prepare two networks with central black holes
of equal size, and maximally entangle the bulk legs at their horizons, as shown in
ﬁgure 18b. It would be interesting to make contact with recent speculations about how
the length of the wormhole relates to the complexity of the tensor network describing
the state [51–53], although for that purpose we would probably need to incorporate
dynamics into our model.
