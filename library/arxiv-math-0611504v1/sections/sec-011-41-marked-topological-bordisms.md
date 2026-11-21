---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-011-41-marked-topological-bordisms
section_title: "Marked topological bordisms"
section_number: 4.1
pages: 20-21
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
toc_source: outline
doc_brief: "Quantum hyperbolic geometry — 25 sections: Front matter; Introduction; Universal QHG"
duplicate_of: "agt-v7-n2-p13-s"
---
r > 0, and r > 2 if g = 0, ﬁx a compact closed oriented base surface S of genus g with a set
V = {v1, . . . , vr} of r marked points. Denote by −S the same surface with the opposite orientation,
and write ∗S for S = +S or −S. Moreover, ﬁx a set of disjoint embedded closed segments avi in S
such that avi has one end point at vi. We say that vi is framed by avi.
We say that two orientation preserving diﬀeomorphisms φ1 : ∗S →Σ1 and φ2 : ∗S →Σ2 are equivalent
if there is an orientation-preserving diﬀeomorphism h : Σ1 →Σ2 such that (φ2)−1 ◦h ◦φ1 pointwise
ﬁxes the segments avi and is isotopic to the identity automorphism of S relatively to {avi}. We write
[∗S, φ] for such an equivalence class.
Let Y be an oriented compact 3-manifold with (possibly empty) boundary ∂Y , with an input/output
bipartition ∂Y = ∂−Y ∪∂+Y of the boundary components (we say that ∂−Y is “at the bottom” of
Y , while ∂+Y is “on the top”). Each boundary component inherits the boundary orientation, via
the usual convention last is the ingoing normal. Let LF be a properly embedded non-empty framed
tangle in Y . This means that LF is a disjoint union of properly embedded orientable ribbons. We split
LF = (LF)i ∪(LF)b, where (LF)i is the internal part of LF made by its closed connected components,
homeomorphic to the annulus S1 × [0, 1], while (LF)b is the union of the components homeomorphic
to the quadrilateral I × [0, 1]. We consider LF up to proper ambient isotopy. For every boundary
QUANTUM HYPERBOLIC GEOMETRY
21
component Σ of Y , we assume that (LF)b∩Σ̸ = ∅, and that (LF)b∩Σ consists of at least two segments
if g(Σ) = 0 (we do not require that every component of (LF)b goes from ∂−towards ∂+). Hence, on
each boundary component Σ of Y we have a set of marked points framed by LF ∩Σ. Also, associated
to ∂± we have a ﬁnite disjoint union α± = `
φ(∗S)∈∂±[∗S, φ] of equivalence classes of diﬀeomorphisms
as above.
Consider the topological (2 + 1)-bordism category with objects the empty set and any ﬁnite union
of the [∗S, φ], and morphisms the triples (Y, LF, α±) as above. We say that (Y, LF, α±) is a bordism
from α−to α+ with support (Y, LF). We allow the case when Y is a closed manifold, so that ∂Y = ∅
and (Y, LF) is a morphism from the empty set to itself. We stress that LF is non-empty in any case.
We can reformulate this category in a setup closer to that of the phase space parameters of Section
3, as follows. If we cut open each avi in S we get an oriented surface F with r boundary bigon
components. This is the domain of an elementary object [∗F, φ], where the target surfaces Σ have
now r boundary components, and the diﬀeomorphisms φ are considered up to isotopy rel(∂).
Consider a bordism (Y, LF, α±). On the boundary of each ribbon component of LF we keep track
of a tangle line X × {0} (X = S1 or I) for the corresponding component of the unframed tangle L,
and there is a longitudinal line X × {1} that speciﬁes the framing of the normal bundle of the parallel
tangle line. These make a pair ¯λ = (λ, λ′) of parallel unframed tangles in Y . Cutting open each ribbon
we get a 3-manifold with corners ˜Y . The boundary ∂˜Y has two “horizontal” parts ∂± ˜Y contained in
∂±Y , and a “vertical” tunnel part eLF. The horizontal parts intersect the tunnel part at the corner
locus; this is a union of bigons contained in ∂Y . Each boundary component Σ of Y corresponds to a
horizontal boundary component of ˜Y , still denoted by Σ. Each tunnel boundary component is made
by the union of two copies of X × (0, 1), glued each to the other at λ ∪λ′. The horizontal boundary
components are the targets of elementary objects [∗F, φ], and each triple ( ˜Y , ˜LF) supports a morphism
between such objects. Clearly, we can recover (Y, LF) from ( ˜Y , ˜LF), so that we have two equivalent
settings to describe the same topological bordism category.
