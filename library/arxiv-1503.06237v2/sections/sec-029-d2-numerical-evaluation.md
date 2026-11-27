---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-029-d2-numerical-evaluation
section_title: "D.2 Numerical evaluation"
section_number: null
pages: 58-58
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
We may numerically evaluate the probability for the greedy algorithm to absorb the
central tensor given a boundary region constructed by erasing a random set of physical
indices according to an i.i.d. distribution. This gives us a conservative estimate of how
well protected the central qubit is from i.i.d. erasure since an optimal recovery method
can only do better. We perform such estimates for diﬀerent values of the lattice radius
in order to identify the value pc associated to a correctability phase transition. For
the regular pentagon lattice tensor network we ﬁnd that there is no indication of the
central qubit being well protected.
Given that the pentagon code does not have a threshold, we introduce the pen-
tagon/hexagon code as a similar example that does have an erasure threshold in this
context. It is the regular lattice composed of pentagons and hexagons, with two pen-
tagons and two hexagons adjacent at each vertex. Such a lattice might employ [[6, 0, 4]]2
and [[5, 1, 3]]2 tensors. Intuitively, we expect that by diluting the number of logical
legs, we may obtain better protection for the encoded logical qubits. Indeed, for such
a lattice, we ﬁnd that there is a threshold value p∗ such that if the i.i.d. probability
of boundary erasure is smaller than p∗, then the central logical qubit may be recon-
structed with a probability which approaches one as the cutoﬀ radius of the lattice is
increased. Such a statement can be proven using techniques very similar to the thresh-
old proof of section D.1. We have numerically tested the performance of the greedy
recovery algorithm for recovering the central qubit in three possible lattices (see ﬁgure
26) supporting our claim that a lower density of logical legs leads to a higher tolerable
erasure threshold.
