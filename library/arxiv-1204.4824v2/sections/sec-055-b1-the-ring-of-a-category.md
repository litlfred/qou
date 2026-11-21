---
doc_id: arxiv-1204.4824v2
doc_title: "Spectral networks"
section_id: sec-055-b1-the-ring-of-a-category
section_title: "B.1 The ring of a category"
section_number: null
pages: 78-79
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
toc_source: outline
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
The ring of a category
To any category C we may associate a ring R(C). As an abelian group, R(C) is the free
group on the space of morphisms:
R(C) =
M
f∈Mor(C)
Z · ℓf.
(B.1)
The ring structure in R(C) is deﬁned by
ℓf1 · ℓf2 :=
(
0
if f1 and f2 are not composable,
ℓf1f2
if f1 and f2 are composable.
(B.2)
Any functor F : C →D induces a canonical ring homomorphism F : R(C) →R(D).
More generally, we could deﬁne a twisted version of R(C) by writing
ℓf1 · ℓf2 =
(
0
if f1 and f2 are not composable,
b(f1, f2)ℓf1f2
if f1 and f2 are composable,
(B.3)
where b(f1, f2) is Z2-valued. Associativity requires that b is a cocycle. A change of basis
changes it by a coboundary. We denote the cohomology class of b by σ and the correspond-
ing twisted ring (up to isomorphism) by R(C, σ).
– 76 –
