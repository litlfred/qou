---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-009-51-ads-rindler-reconstruction-as-error-correctio
section_title: "AdS-Rindler reconstruction as error correction"
section_number: 5.1
pages: 23-25
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
We begin by brieﬂy recalling the main point emphasized in [1], which is that in
AdS/CFT a bulk local observable can be realized by many diﬀerent operators in the
CFT. In fact, if x is any point in the bulk, and Y is any point on the boundary, the
AdS/CFT dictionary can be chosen so that it maps the bulk local ﬁeld φ(x) to a CFT
operatorO[φ(x)] which has no support in an open set containing Y , and therefore
commutes with any local ﬁeld of the CFT supported near Y . Since Y is an arbitrary
boundary point, if the CFT operator corresponding to φ(x) were actually unique, we
would conclude that O commutes with all local ﬁelds in the CFT, and therefore is a
multiple of the identity because the local ﬁeld algebra is irreducible. This paradox is
evaded once we recognize that the correspondence is not unique. IfY,Z are two distinct
boundary points, the CFT operator corresponding toφ(x) can be chosen to be eitherO,
which commutes with CFT local ﬁelds supported near Y , orO′, which commutes with
CFT local ﬁelds supported near Z, where O andO′ are inequivalent CFT operators
even though they can be used interchangeably for describing bulk physics.
– 21 –
Figure 11. Bulk ﬁeld reconstruction in the causal wedge. On the left is a spacetime diagram,
showing the full spacetime extent of the causal wedge C[A] associated with a boundary sub-
regionA that lies within a boundary time slice Σ. The point x lies withinC[A] and thus any
operator atx can be reconstructed onA. On the right is a bulk time slice containing x and Σ,
which has a geometry similar to that of our tensor networks. The point x can simultaneously
lie in distinct causal wedges, so φ(x) has multiple representations in the CFT.
This novel feature of AdS/CFT, that a bulk local observable can be represented
by boundary CFT operators in multiple ways, is illustrated in ﬁgure 11. The idea
is that any ﬁxed-time CFT subregion A deﬁnes a subregion in the bulk, the causal
wedgeC[A]. For any point x∈C [A], bulk quantum ﬁeld theory ensures that any bulk
local operator φ(x) can be represented in the CFT as some nonlocal operator on A.
This representation is called the AdS-Rindler reconstruction of the operator [34, 35].
Because a given bulk point x can lie within distinct causal wedges associated with
diﬀerent boundary regions, the bulk operator φ(x) can have distinct representations in
the CFT with diﬀerent spatial support.
In [1] the non-uniqueness of the CFT operator corresponding to the bulk operator
φ(x) was interpreted as indicating that φ(x) is a logical operator preserving a code
subspace of the Hilbert space of the CFT. This code subspace is protected against
“errors” in which parts of the boundary are “erased.” If the boundary operator corre-
sponding to φ(x) acts on a subsystem of the CFT which is protected against erasure
of the boundary region Ac, then this operator can be represented in the CFT as an
operator supported on A, the complement of the erased region. Thus we may inter-
pret the AdS-Rindler reconstruction of φ(x) on boundary region A as correcting for
the erasure of Ac; choosing the erased portion of the boundary in diﬀerent ways leads
– 22 –
to diﬀerent reconstructions of φ(x). Moreover, operators near the center of the bulk
are “well protected” in the sense that a large region needs to be erased to prevent
their reconstruction, while operators near the boundary can be erased more easily by
removing a smaller part of the boundary [1].
We may think of this code subspace as the low-energy sector of the CFT correspond-
ing to a relatively smooth dual classical geometry. All CFT operators are physical, and
thus have some bulk interpretation, but the “logical” operators are special ones which
map low-energy states to other low-energy states. The same logical action can be re-
alized by distinct CFT operators, as these distinct operators act on high-energy CFT
states (those outside the code subspace) diﬀerently even though they act on low-energy
states in the same way.
