---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-013-23-dg-schemes
section_title: "DG schemes"
section_number: 2.3
pages: 12-13
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
scheme is a quasi-projective variety. But let us neglect its interesting structure as a topologi-
cal space, and describe its ring of functions locally. By deﬁnition, the locus of cyclic triples
(g×g×V )cyc is an open subset of afﬁne space, and the moment map (2.8) gives rise to a section
of the trivial g bundle:
µ∈ Γ
(
O(g×g×V )cyc⊗ g
)
over (g× g×V )cyc. We may write down the Koszul complex corresponding to this section:
(∧•g,µ ) :=
[
O(g×g×V )cyc⊗∧ dimGg
µ
−→...
µ
−→O (g×g×V )cyc⊗ g
µ
−→O (g×g×V )cyc
]
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 13
Since the Hilbert scheme is smooth, this complex is exact except at the rightmost cohomology
group, where it is isomorphic toOµ−1(0)cyc. Moreover, since all the maps areG–equivariant, we
may write locally:
OHilbn
q.i.s.
∼=
(
∧•adjg,µ
)
=
[
∧dimGadjg
µ
−→...
µ
−→O (g×g×V )cyc/G
]
where adjg denotes the vector bundle on (g× g×V )cyc/G, obtained by descending the trivial
vector bundle g on g× g×V , endowed with theG–action by conjugation. One may write down
the analogous Koszul complex for the mapν of (2.10), but observe that:
(2.12) OFHilbn(C2) is not
q.i.s.
∼= (∧•adjn,ν ) :=
[
∧dimNadjn
ν
−→...
ν
−→O (g×g×V×Fl)cyc/G
]
(recall that adjn denotes the vector bundle on (g× g×V× Fl)cyc/G, obtained by descending
the vector bundle Adjn on Fl, endowed with the G–action by conjugation). The fact that the
Koszul complex (2.12) is not exact anymore boils down to the fact that FHilbn(C2) is not a
local complete intersection, and so we choose to work instead with the dg scheme:
(2.13) OFHilbdg
n (C2) := (∧•adjn,ν )
Note that we think of the left hand side as a sheaf of dg algebras, given precisely by the complex
in (2.12) supported on the smooth scheme (g× g×V× Fl)cyc/G, which is nothing but a ﬂag
variety bundle over the smooth scheme (g× g×V )cyc/G. This will allow us to ignore the
subtleties of the topology of dg schemes.
