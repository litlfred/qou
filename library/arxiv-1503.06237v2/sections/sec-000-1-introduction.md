---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 3-5
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
The AdS/CFT correspondence, an exact duality between quantum gravity on a (d+1)-
dimensional asymptotically-AdS space and a d-dimensional CFT deﬁned on its bound-
ary, has signiﬁcantly advanced our understanding of quantum gravity, as well as pro-
vided a powerful framework for studying strongly-coupled quantum ﬁeld theories. One
aspect of this duality is a remarkable relationship between geometry and entanglement.
This notion ﬁrst appeared in the proposal [2] that two entangled CFT’s have a bulk dual
connecting them through a wormhole, and was later quantiﬁed by Ryu and Takayanagi
via their proposal that entanglement entropy in the CFT is computed by the area of
a certain minimal surface in the bulk geometry [3, 4]. This latter proposal, known as
the Ryu-Takayanagi (RT) formula, has led to much further work on sharpening the
connection between geometry and entanglement [5–12]
In the condensed matter physics community, improved understanding of quantum
entanglement has led to signiﬁcant progress in the numerical simulation of emergent
phenomena in strongly-interacting systems. A key ingredient of such algorithms is
the use of tensor networks to eﬃciently represent quantum many-body states [13–
15]. Vidal combined this idea with entanglement renormalization to formulate the
Multiscale Entanglement Renormalization Ansatz (MERA) [16, 17], a family of tensor
networks that eﬃciently approximate wave functions with long-range entanglement
of the type exhibited by ground states of local scale-invariant Hamiltonians [18–20].
The key idea is to represent entanglement at diﬀerent length scales using tensors in a
hierarchical array.
In the AdS/CFT correspondence, the emergent radial direction can be regarded
as a renormalization scale [21], and spatial slices have a hyperbolic geometry resem-
bling the exponentially growing tensor networks of MERA. This similarity between
AdS/CFT and MERA was pointed out by Swingle, who argued that some physics of
the AdS/CFT correspondence can be modeled by a MERA-like tensor network where
– 1 –
quantum entanglement in the boundary theory is regarded as a building block for the
emergent bulk geometry [22, 23].
Recently it has been argued in [1] that the emergence of bulk locality in AdS/CFT
can be usefully characterized in the language of quantum error-correcting codes. Cer-
tain paradoxical features of the correspondence arise naturally by interpreting bulk
local operators as logical operators on certain subspaces of states in the CFT, whose
entanglement structure protects these operators from boundary erasures. Moreover,
inspired by [22, 23], it was suggested that there should be tensor network models that
concretely implement these ideas.
In this paper, we propose such a family of exactly solvable toy models of the
bulk/boundary correspondence based on a novel tensor-network construction of quan-
tum error-correcting codes. Other authors have recently used holographic ideas [24, 25]
and related tensor network constructions [26, 27] to build quantum codes with inter-
esting properties or toy models of the bulk/boundary correspondence [28], but our
approach diﬀers from previous work by combining the following properties, all of which
are desirable for a model of AdS/CFT:
• Exactly solvable: Many of the properties of our models can be shown explic-
itly. In particular, an exact prescription for mapping bulk operators to boundary
operators can be obtained, and we can give examples where the Ryu-Takayanagi
formula holds exactly for all connected boundary regions.
• QECC: Our models are quantum error-correcting codes, where the bulk/boundary
legs of the tensor network correspond to input/outputs of an encoding quantum
circuit. In this sense they realize explicitly the proposal of [1].
• Bulk uniformity: The tensor network is supported on a uniform tiling of a
hyperbolic space, known as a hyperbolic tessellation. If the tiling is extended to
an inﬁnite system, the tensor network has no inherent directionality and all the
locations in the bulk can be treated on an equal footing (see Fig. 4b).
The rest of this paper is organized as follows: In section 2, we introduce a class of
tensors called perfect tensors, which are associated with pure quantum states of many
spins such that the entanglement is maximal across any partition of the spins into two
sets of equal size. In section 3, we construct holographic states and codes by building
networks of perfect tensors. These codes have properties reminiscent of the AdS/CFT
correspondence, elucidated in the rest of the paper, where the code’s logical/physical
degrees of freedom are interpreted as the bulk/boundary degrees of freedom of a CFT
with a gravitational dual.
– 2 –
In section 4, we study the entanglement structure of holographic states, showing
that the Ryu-Takayanagi formula is exactly satisﬁed for any connected boundary region,
developing a graphical representation of multipartite entanglement, and conﬁrming the
negativity of tripartite information [9]. In section 5, we investigate the dictionary
relating bulk and boundary observables, deﬁne a lattice version of the causal wedge,
and explain how bulk local operators in the causal wedge can be reconstructed on
the boundary; we also deﬁne a lattice version of the entanglement wedge, and oﬀer
evidence supporting the entanglement wedge hypothesis proposed in [40–42], see also
[67]. We brieﬂy discuss how to describe black holes using holographic codes in section 6.
Section 7 contains our conclusions, and many details appear in the appendices.
