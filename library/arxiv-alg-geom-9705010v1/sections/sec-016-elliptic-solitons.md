---
doc_id: arxiv-alg-geom-9705010v1
doc_title: "Seiberg-Witten Integrable Systems"
section_id: sec-016-elliptic-solitons
section_title: "Elliptic solitons"
section_number: null
pages: 26-27
source_pdf: 9705010v1.pdf
source_sha256: 30ab8d0cc2d8f1ae
toc_source: inferred
doc_brief: "Seiberg-Witten Integrable Systems — 32 sections: Front matter; Contents; Introduction"
---
It is curious to note that the same system arises in several rather diﬀerent
contexts. Here is a brief outline of one of these, following the work of Treibich and
Verdier [T], [TV].
Finite dimensional solutions of the KP hierarchy (= inﬁnite dimensional in-
tegrable system) are well understood. They are parametrized by Krichever data,
consisting of a curve C, a point p ∈C, a line bundle L, and local trivializations.
Such data determine a point in the total space of the hierarchy with the property
that the inﬁnite collection of commuting KP ﬂows emanating from the point sweep
out only a ﬁnite dimensional space, isomorphic to J(C). The curve C, the point p
and the trivializations remain ﬁxed, while L moves freely in J(C).
An elliptic soliton is a ﬁnite dimensional solution of KP in which the ﬁrst ﬂow,
KP1, already closes up, i.e. evolves on an elliptic curve inside the possibly larger
Jacobian J(C). The direction of KP1, for points coming from Krichever data, is
the tangent vector at p to the Abel-Jacobi image of C in J(C). So the condition
is that J(C) should contain an elliptic curve E which is tangent at AJ(p) to the
Abel-Jacobi image AJ(C).
Start with an n-sheeted branched cover π : C →E and a point p ∈E with
local coordinate ξ. Let π∗(p) = q0 + · · · + qn−1, and let ξi := ξ ◦π near qi. The
tangent vector ti := ∂/∂ξi lives naturally in Γ(Oqi(qi)). Its image
(AJ)∗ti ∈TAJ(qi)J(C)
can then be identiﬁed with the image of ti under the coboundary map δ for the
sequence
0 →OC →OC(qi) →Oqi(qi) →0.
SEIBERG-WITTEN INTEGRABLE SYSTEMS
27
Similarly, the tangent at π∗p to the image π∗E of E in J(C) is given by Σn−1
i=0 δ(ti) =
δ(Σn−1
i=0 ti). The tangency condition then says that δ(Σn−1
i=0 ti) is proportional to δ(t0),
and therefore equal (by the residue theorem) to δ(nt0). This happens if and only
if there is some f ∈Γ(O(π∗p)) with
Resqi(fπ∗dz) =

1
1 ≤i ≤n −1
1 −n
i = 0,
where dz is a non-zero closed 1-form on E.
This is equivalent to saying that
π : C →E is one of our spectral curves, and fπ∗dz becomes the Seiberg-Witten
diﬀerential.
