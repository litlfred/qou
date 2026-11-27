---
doc_id: arxiv-1503.06237v2
doc_title: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence"
section_id: sec-012-54-connected-reconstruction-and-the-causal-wedge
section_title: "Connected reconstruction and the causal wedge"
section_number: 5.4
pages: 27-28
source_pdf: 1503.06237v2.pdf
source_sha256: 55572e7133514f4a
toc_source: outline
doc_brief: "Holographic quantum error-correcting codes: Toy models for the bulk/boundary correspondence — We propose a family of exactly solvable toy models for the AdS/CFT correspondence based on a novel"
---
Given a subregion A of the boundary, which bulk local operators can be reconstructed
on A? This is not an easy question to answer in general, but at least we can give
a simple description of a large logical subsystem reconstructable on A, namely those
logical operators acting on bulk sites which are reachable using the greedy algorithm
explained in section 4.
Recall that the greedy algorithm associates with any boundary region A a greedy
geodesic γ⋆
A whose boundary matches the boundary of A, such that A and γ⋆
A enclose
a tensor PA which deﬁnes an isometry mapping free bulk legs in PA together with the
legs cut by γ⋆
A to A. Using this isometry applied to any operator acting on a bulk leg
inPA(tensored with the identity acting on all the rest of the isometry’s input indices),
we may push that logical operator through the isometry to obtain its reconstruction on
A. Let’s call the position of a perfect tensor in the network a bulk point and say that
the greedy algorithm reaches a bulk point if it moves the cut past that tensor, hence
using it in the construction of PA
This operator reconstruction procedure can be applied to any boundary region
A. In the special case where A is connected, it provides a precise analog of the AdS-
Rindler reconstruction in holographic codes, which we can formalize with a deﬁnition
and theorem:
– 25 –
Deﬁnition 5. Suppose that A is a connected boundary region. The causal wedge
of A, denotedC[A], is the set of bulk points reached by applying the greedy algorithm
to A.
We then have:
Theorem 5. SupposeA is a connected boundary region. Then any bulk local operator
in the causal wedge C[A] can be reconstructed as a boundary operator supported on A.
We could have formulated a geometric notion of the causal wedge, deﬁning it as the set
of bulk points enclosed between A and the actual minimal geodesic γA, rather than the
greedy geodesic. This geometrical deﬁnition is closer in spirit to how the term “causal
wedge” has been used in the context of AdS/CFT. But we prefer this greedy notion of
causal wedge instead, so that Theorem 5 is correct as stated.
As ﬁgure 12 illustrates, bulk operators near the boundary can be reconstructed on
smaller connected regions than bulk operators near the center, just as for the AdS-
Rindler reconstruction in AdS/CFT. It is natural to wonder how large the connected
region A should be for the operator at the center of the bulk to be reconstructable
on A. This question is studied for the pentagon code in appendix C by investigating
whether the greedy algorithm applied to A reaches the central tensor in the network.
We ﬁnd that a connected region ofNA boundary spins necessarily allows reconstruction
of all operators acting on the center provided that A covers a suﬃciently large fraction
of the boundary, namely
fA≡ NA
Nboundary
> 5 +
√
5
10 ≡fc≈.724. (5.1)
The analogous result for the AdS-Rindler reconstruction is fc = 1/2, but the dis-
creteness of our lattice introduces some additional overhead. It turns out, though, that
because the tensor network is not invariant under translations of the boundary, whether
the connected region A allows reconstruction of the center depends not just on the size
ofA but also on its location. In appendix C we show that, while the condition (5.1) is
needed to guarantee reconstruction of the central operator on an arbitrary connected
region, there are some connected regions with fA = NA
Nboundary
= 3+
√
5
10 ≈.524 that suﬃce
for the reconstruction.
