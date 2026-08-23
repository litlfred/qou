---
doc_id: arxiv-1204.4824v2
doc_title: "Prepared for submission to JHEP Spectral networks"
section_id: sec-045-b1-the-ring-of-a-category
section_title: "B.1 The ring of a category"
section_number: null
pages: 78-79
source_pdf: 1204.4824v2.pdf
source_sha256: bf01cbaa5a8712c8
doc_brief: "Spectral networks — We introduce new geometric objects called spectral networks. Spectral net- works are networks of trajectories on Riemann surfaces obeying certain local rules."
---
To any category C we may associate a ring R(C). As an abelian group, R(C) is the free
group on the space of morphisms:
R(C) =
⨁
f∈Mor(C)
Z·𝓁f. (B.1)
The ring structure in R(C) is deﬁned by
𝓁f1·𝓁f2 :=
{
0 if f1 and f2 are not composable,
𝓁f1f2 if f1 and f2 are composable.
(B.2)
Any functor F :C→D induces a canonical ring homomorphism F :R(C)→R(D).
More generally, we could deﬁne a twisted version of R(C) by writing
𝓁f1·𝓁f2 =
{
0 if f1 and f2 are not composable,
b(f1,f 2)𝓁f1f2 if f1 and f2 are composable,
(B.3)
where b(f1,f 2) is Z2-valued. Associativity requires that b is a cocycle. A change of basis
changes it by a coboundary. We denote the cohomology class ofb byσ and the correspond-
ing twisted ring (up to isomorphism) by R(C,σ ).
– 76 –
