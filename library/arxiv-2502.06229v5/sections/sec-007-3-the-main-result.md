---
doc_id: arxiv-2502.06229v5
doc_title: "Constructing equivalences between fusion categories of quantum groups and of vertex operator algebras via quantum gauge groups"
section_id: sec-007-3-the-main-result
section_title: "The main result"
section_number: 3
pages: 12-14
source_pdf: 2502.06229v5.pdf
source_sha256: 3499c40ea150a617
toc_source: outline
---
Let g be a complex simple Lie algebra and let Rep(Vgk) be the module category of the
corresponding affine vertex operator algebra Vgk at level k ∈N, endowed with the ribbon
13
braided tensor structure introduced by Huang and Lepowsky.
Let A(Vgk) be the Zhu
algebra.
Let V denote the fundamental representation of g for each Lie type, defined in [99], (see
also Sect. 11 for the classical types and G2). We also denote by V the corresponding
quantized representation of Uq(g), q = eiπ/ℓd, the associated object of the quantum group
fusion category C(g, q), with ℓ= k + ˇh, ˇh the dual Coxeter number of g. We use the same
notation for the corresponding representation of the vertex operator algebra Vgk and of the
Zhu algebra A(Vgk). Similarly for the irreducible objects Vλ of the involved categories.
Let AW(g, q) denote the unitary compatible coboundary weak Hopf algebra associated to
C(g, q) via the construction of a weak tensor structure on Wenzl functor W : C(g, q) →Vec
following Theorems 31.16, in [10]. We shall give a brief exposition of AW(g, q) in Sect. 4.
Theorem 3.1. We have that:
(a) The linear representation category Rep(A(Vgk)) admits a natural structure of rib-
bon braided tensor category RepHL(A(Vgk)) obtained as a transport from Huang-
Lepowsky structure on RepHL(Vgk) to Rep(A(Vgk)). In this way, Zhu’s linear equiv-
alence
Z : RepHL(Vgk) →RepHL(A(Vgk))
admits a natural structure of ribbon braided tensor equivalence.
(b) The Zhu algebra A(Vgk) becomes a twisted unitary compatible coboundary weak
quasi-Hopf algebra with structure induced by the weak Hopf algebra AW(g, q) via
Wenzl path and the construction of the Drinfeld twist. Let RepQG(A(Vgk)) be en-
dowed with the corresponding ribbon braided tensor structure.
At the level of representation categories, RepQG(A(Vgk)) becomes a unitary cobound-
ary modular tensor category in this way with the structure derived from C(g, q) and
the equivalence
RepQG(A(Vgk)) −→Rep(AW(g, q)),
obtained in Theorem 2.2 in [10]. Moreover RepQG(A(Vgk)) and RepHL(A(Vgk)) have
the same tensor product bifunctor.
(c) The linear equivalence
Z : RepHL(Vgk) →RepQG(A(Vgk))
endowed with the same natural transformation as in (a) but w.r.t. the new rib-
bon braided tensor structure of RepQG(A(Vgk)) described in (b), satisfies the ribbon
braided tensor equivalence equations for the ribbon structure for all objects, the
braid morphisms for pairs (Vλ, V ) and (Vλ, V ), and the associativity morphisms for
triples
(Vλ, V, V ),
(V, Vλ, V ),
(V, V, Vλ)
with Vλ an arbitrary irreducible object of the fusion category.
(d) If g is of one of the Lie types A, B, C, D, G2 then Zhu’s equivalence in (c) is a
ribbon braided tensor equivalence. Specifically, the composition
RepHL(Vgk)
Z−→RepQG(A(Vgk)) −→Rep(AW(g, q))
TK ribbon equiv
−−−−−−−−−−→C(g, q)
(3.1)
14
C. PINZARI
is a ribbon tensor equivalence by application of the indicated theorems.
We would like to notice that the equivalences described in (3.1) are explicit. The equiv-
alence on the left is Zhu’s linear equivalence endowed with the natural transformations
given by the restriction to the zero modes the braided tensor structure by Huang and
Lepowsky. The fact that the braided tensor structure of the range of Z induced by Huang-
Lepowsky structure in (a) coincides with the structure arising from quantum groups on
the Zhu algebra, follows from our work in (c), done in [10], and the first statement of part
(d), established in this paper. The equivalence on the right is the functor due to Wenzl
enriched with our weak tensor structure by Theorem 2.4. The middle equivalence is an
application of the explicit symmetry provided by our analogue of Drinfeld-Kohno theorem
29.4 in [10], and stated in parts (a) and (b) of Theorem 2.2 in [10]. This symmetry is given
by a Drinfeld twist explicitly defined by the action of the R-matrix, more precisely by the
braided and ribbon structure in the two settings, that allow to see in the vertex operator
algebra setting same structure as that in the quantum group setting.
