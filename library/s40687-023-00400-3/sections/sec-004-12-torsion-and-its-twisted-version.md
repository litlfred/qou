---
doc_id: s40687-023-00400-3
doc_title: "Twisted Neumann–Zagier matrices"
section_id: sec-004-12-torsion-and-its-twisted-version
section_title: "Torsion and its twisted version"
section_number: 1.2
pages: 3-4
source_pdf: s40687-023-00400-3.pdf
source_sha256: fd7638a8cf512a99
toc_source: outline
doc_brief: "TWISTED NEUMANN–ZAGIER MATRICES — The Neumann–Zagier matrices of an ideal triangulation are integer matrices with symplectic properties whose entries encode the number of tetrahedra that wind around"
duplicate_of: "arxiv-2109.00379v1"
---
Before discussing twisting matters further, let us recall a key motivating example. A basic
invariant of a compact 3-manifold is the order of the torsion of its ﬁrst homology. The
behavior of this invariant for all cyclic covers of a knot complement is determined by a
single Laurent polynomial, the Alexander polynomial. Explicitly, we have
tor(H1(M(n); Z))
 =

ωn=1
K(ω)
(1)
where K(t) ∈Z[t±1] is the Alexander polynomial of a knot K ⊂S3, M(n) is the n-
fold cyclic cover of M = S3 \ K, and the left-hand side is the order of the torsion
part of H1(M(n); Z). This classical result connecting the torsion of the ﬁrst homology
to the Alexander polynomial (see, e.g., [12, (6.3), p.417]) is deeply rooted in the idea that
the Alexander polynomial is the torsion of the inﬁnite cyclic cover of M twisted by the
abelianization map α : π1(M) →H1(M; Z) = Z. In other words, we have
The twisted torsion determines the torsion of the cyclic covers
(2)
This idea has been extended in several directions. Among them, one can deﬁne the
torsion of a 3-manifold using interesting representations of its fundamental group. For
example, when M is a cusped hyperbolic 3-manifold, one can deﬁne a torsion using a
(lifted)geometricSL2(C)-representationρ ofthefundamentalgroupofitscomplement,or
a symmetric power thereof. There are some technical diﬃculties that one must overcome,
stemmingfromthefactthatsometimesthecorrespondingchaincomplexesarenotacyclic,
hence the torsion depends on a choice of peripheral curves, as well as normalization issues,
since the torsion is usually well deﬁned up to a sign. These issues have been addressed
in detail by [5,11,23]. Among the several torsion nvariants, we will be interested in the
adjoint (Reidemeister) torsion τγ (M) of a one-cusped hyperbolic 3-manifold (such as a
knot complement) using the adjoint representation Adρ = Sym2(ρ) : π1(M) →SL3(C),
where γ is a ﬁxed peripheral curve. The adjoint torsion τγ (M) ∈F×/± is a nonzero
element of the trace ﬁeld F of M, well deﬁned up to a sign [23]. Just as in the case of
the Alexander polynomial, there is a version of the adjoint twisted Alexander polynomial
τ(M, α, t) ∈F[t±1]/(±tZ) (abbreviated by τ(M, t) when α is clear) deﬁned in [5,11,27]
using an epimorphism α : π1(M) →Z. Here, the ambiguity is given by multiplication by
an element of ±tZ := {±tr | r ∈Z}.
Two key properties of the adjoint twisted Alexander polynomial are the behavior under
ﬁnite cyclic covers [11]
τ(M(n), tn) =

ωn=1
τ(M, ω t)
(3)
and the relation with the adjoint torsion [28], namely
τ(M, 1) = 0,
d
dt

t=1
τ(M, t) = τλ(M)
(4)
where λ is the canonical longitude, i.e., the peripheral curve satisfying α(λ) = 0.
37
Page 4 of 23
Fig. 1 An ideal tetrahedron
