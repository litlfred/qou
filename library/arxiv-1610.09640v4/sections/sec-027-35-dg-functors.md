---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-027-35-dg-functors
section_title: "DG Functors"
section_number: 3.5
pages: 64-65
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
Subsection 4.6.
Deﬁnition 3.5.4.Let F,G : C→D be DG functors.
(1) A degreei morphism of DG functorsη:F→G is a degreei morphism of
graded functors, as in Deﬁnition 3.1.39.
(2) Let η: F →G be a degreei morphism of DG functors. For each object
M∈C there is a degreei + 1 morphism dD(ηM) : F (M)→G(M) in D.
We deﬁne the collection of morphismsdD(η) :={dD(ηM)}M∈C.
(3) Astrict morphism of DG functorsis a degree0morphism of graded functors
η:F→G such that dD(η) = 0.
Explanation of item (2) of the deﬁnition: for an objectM∈C, we have
ηM∈HomD
(
F (M),G (M)
{i
.
Now HomD
(
F (M),G (M)
{
is a DG K-module with diﬀerentialdD; see formula
(3.4.2). Thus
dD(ηM)∈HomD
(
F (M),G (M)
{i+1
.
Proposition 3.5.5. In the situation of Deﬁnition3.5.4, the collection of mor-
phisms dD(η) is a degreei + 1 morphism of DG functorsF→G.
Exercise 3.5.6. Prove this proposition.
64
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The categories Str(C) and Ho(C) were introduced in Deﬁnition 3.4.6.
Proposition 3.5.7. Let F : C→D be a DG functor. Then F induces linear
functors Str(F ) : Str(C)→Str(D) and Ho(F ) : Ho(C)→Ho(D).
Proof. Because F is a DG functor, it sends 0-cocycles in HomC(M0,M 1) to 0-
cocycles in HomD(F (M0),F (M1)). The same for0-coboundaries. □
By abuse of notation, and when there is no danger for confusion, we will some-
times writeF instead of Str(F ) or Ho(F ).
Exercise 3.5.8. Let A and C be DG categories, and assume A is small. Deﬁne
DGFun(A, C) to be the set of DG functorsF : A→C. Show that DGFun(A, C)
is a DG category, where the morphisms are from Deﬁnition 3.5.4(1), and their
diﬀerentials are from Deﬁnition 3.5.4(2).
