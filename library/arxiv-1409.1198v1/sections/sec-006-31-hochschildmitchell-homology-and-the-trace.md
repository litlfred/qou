---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-006-31-hochschildmitchell-homology-and-the-trace
section_title: "Hochschild–Mitchell homology and the trace"
section_number: 3.1
pages: 13-14
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
a linear category with one object ∗ and whose morphisms Hom( ∗, ∗) are given by the abelian group
R. Composition is given by multiplication in R and the identity morphisms of ∗ corresponds to the
unit 1 R ∈R. Utilizing this observation, it possible to deﬁne the Hochschild–Mitche ll homology of an
arbitrary linear category as follows.
Let C be a small linear category. Deﬁne the Hochschild–Mitchell complex of C
C• =C•(C) : ... − →Cn
dn
− →Cn−1
dn−1
− →...
d2
− →C1
d1
− →C0 − →0,
14 ANNA BELIAKOV A, ZAUR GULIYEV, KAZUO HABIRO, AND AARON D. L AUDA
where
Cn =Cn(C) :=
⨁
x0,...,xn∈Ob(C)
C(xn,x 0) ⊗ C(xn−1,x n) ⊗ · · · ⊗ C(x0,x 1),
dn(σn ⊗σn−1 ⊗ · · · ⊗σ0) :=
n−1∑
i=0
(−1)iσn ⊗ · · · ⊗σn−iσn−i−1 ⊗ · · · ⊗σ0 + (−1)nσ0σn ⊗σn−1 ⊗ · · · ⊗σ1.
The Hochschild–Mitchell homology HH •(C) of C is deﬁned to be the homology of the chain complex
C•(C). One can easily check that if C is a unital ring R regarded as a linear category, then this deﬁnition
agrees with the one given in section 2.2.
In this article we will be especially concerned with the zeroth Hochsch ild–Mitchell homology HH0(C) =
C0/d1(C1) of C. We introduce the notation
Tr(C) := HH 0(C)
which we call the trace of the linear category C. This terminology is justiﬁed by the following observa-
tion. For any x ∈ Ob(C) we denote by C(x,x ) = Hom C(x,x ) = End C(x) the space of its endomorphisms.
Then it is an easy calculation to verify that the trace Tr( C) of the linear category C is given by
Tr(C) =

 ⨁
x∈Ob(C)
C(x,x )

/ Span{fg −gf },
where f and g run through all pairs of morphisms f : x − →y,g : y − →x with x,y ∈ Ob(C).
We denote by [ f ] the equivalence class of f ∈ C (x,x ) in Tr( C). The trace Tr gives rise to a functor
from the category of (small) linear categories to the category of a belian groups.
