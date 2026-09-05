---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-051-92-sections-and-schemes
section_title: "Sections and schemes"
section_number: 9.2
pages: 68-69
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
closely related to FHilbdg
n = FHilbdg
n (C). Namely, lets be an arbitrary section of the tautolog-
ical bundleTn. It deﬁnes a contraction map:
(9.2) ds :∧•T∨
n →∧•−1T∨
n
Recall the construction (1.13):
~ι∗(σ) =ι∗(σ)⊗∧•T∨
n
which is naturally a sheaf of dg modules on TotFHilbdg
n
Tn[1]. If we endow the exterior power
with the differential (9.2), we obtain:
(~ι∗(σ),ds)
which is naturally a sheaf of dg modules on the dg scheme:
TotFHilbdg
n
(Tn[1],s ) := the sheaf of dg algebras (∧•T∨
n ,ds) on FHilbdg
n.
To construct sectionss of the tautological bundleTn, recall that its ﬁbers are given by:
Tn|In⊂...⊂C[x,y] = C[x,y ]/In.
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 69
Therefore every polynomial f ∈ C[x,y ] deﬁnes a section sf ∈ Γ(FHilbn,Tn) for all n, and
these sections are all compatible with each other:
The morphism FHilbn
π
−→FHilbn−1× C therefore induces a map:
TotFHilbdg
n
(Tn[1],sf)
πf
−→TotFHilbdg
n−1×C(Tn−1[1],sf)
and so one has a commutative diagram of maps of dg schemes:
where the vertical maps are simply induced by the map of dg algebras ∧•T∨
n → (∧•T∨
n ,ds).
Note that the dg scheme TotFHilbdg
n
(Tn[1],sf) is C∗× C∗ equivariant if and only if f is an
equivariant section of Tn. It is not hard to see that the only such equivariant sections are
f(x,y ) =xNyM for some (N,M )∈ N0× N0. We denote the corresponding section bysN|M.
Remark 9.1. In [32, Section 7], the differentials were parametrized by copies of the deﬁning
representation of Sn in the rational Cherednik algebra, which can be considered as a non-
commutative deformation of C[x1,...,x n,y 1,...,y n]. One can check that such a copy nat-
urally corresponds to a section of Tn, in particular, f ∈ C[x,y ] corresponds to the subspace
Span(f(xi,yi))1≤i≤n.
