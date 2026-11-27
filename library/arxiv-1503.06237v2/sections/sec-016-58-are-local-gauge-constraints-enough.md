---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-016-58-are-local-gauge-constraints-enough
section_title: "Are local gauge constraints enough?"
section_number: 5.8
pages: 39-40
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
It has recently been argued that in AdS/CFT gauge constraints in the boundary CFT
may pick out a small enough subspace of states to explain the error correcting properties
of AdS/CFT [44]. The idea is that any gauge-invariant state already possess some non-
local entanglement via the imposition of the gauge constraints, and that this might be
enough to resolve the various paradoxes of [1]. 6
We can try to test this idea for the holographic stabilizer codes discussed in section
5.7. Since gauge constraints are spatially local, the argument of Ref. [44] suggests
that the code’s stabilizer group should be locally generated, in the sense that it has
a complete set of generators, each with support on a constant number of neighboring
boundary qubits. In fact, though, holographic stabilizer codes do not have this property
in cases where the greedy entanglement wedge reaches outside the causal wedge. This
property poses no problem for the proposal of [1] however, as those authors argued that
energetic constraints should also be included in deﬁning the code subspace.
Consider for example the disconnected boundary region A = A1∪A2 in the pen-
tagon code, depicted in ﬁgure 13. We have already seen that the full logical algebra of
the central pentagon can be reconstructed on the disconnected regionA1∪A2, but that
no nontrivial logical operator acting on the central pentagon is supported on either
one of the connected components A1, A2. In a stabilizer code, a logical Pauli operator
supported on A1∪A2 is a tensor productO =OA1⊗OA2 of Pauli operators supported
onA1 andA2 separately. In order to preserve the code space, this logical Pauli operator
must commute with all of the code’s stabilizer generators. But if the two components
A1 andA2 are distantly separated and the stabilizer generators are geometrically local,
then no stabilizer generator has nontrivial support on both A1 and A2. Any stabilizer
generator with no support on A2 trivially commutes withOA2, and if it commutes with
O then it must commute with OA1 as well. Likewise, a stabilizer generator with no
support onA1 must commute withOA2 if it commutes withO. ThereforeOA1 andOA2
are logical operators, and at least one is nontrivial if their product is, contradicting the
hypothesis that no nontrivial logical operator is supported on either connected com-
ponent of A. The conclusion is that the stabilizer generators cannot be geometrically
local.
The above argument applies even to higher-dimensional holographic stabilizer codes.
In the case were the boundary is one dimensional, we may simply appeal to a known
6The word “gauge” is sometimes used in quantum information theory in a way that is non-standard
from the point of view of quantum ﬁeld theorists. In quantum ﬁeld theory, states that are not gauge-
invariant have no physical interpretation, and are not really part of the Hilbert space of the theory;
they appear only as a mathematical convenience. This is what the authors of [44] meant by gauge
constraints, and it is what we mean here.
– 37 –
result in quantum coding theory, that a stabilizer code in one dimension with geometri-
cally local generators has constant distance [45, 46]. Therefore, a one-dimensional code
with a local stabilizer cannot have a positive erasure threshold.
