---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-029-24-the-andre-kahn-quotient
section_title: "The Andr´e-Kahn quotient"
section_number: 2.4
pages: 40-41
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
For the Tannakian arguments to be given below, we want to work with
rigid symmetric monoidal categories which are at the same time semisimple
abelian categories. To obtain such a categoryD that is as close as possible
to the triangulated categoryD, we will apply a general quotient construction
introduced by Andr´e and Kahn in [1]. In what follows we always assume
that axioms (D1) – (D4) from the previous section, i.e. all axioms except
for the hard Lefschetz axiom, are satisﬁed.
The construction of Andr´e and Kahn works as follows. By rigidity we
have for eachK∈ D an isomorphismHomD(K,K) ∼−→HomD(1,K∗K∨)
which in what follows we denote byf↦→ f ♯. We then deﬁne the categorical
tracetr(f )∈ EndD(1) = Λ of an endomorphismf∈ HomD(K,K) to be the
composite morphism
tr(f ) : 1
f ♯
// K∗K∨
SK,K∨
// K∨∗K
evK // 1
where as usualSK,K∨ denotes the symmetry constraint andevK denotes the
evaluation morphism. Following section 7.1 of loc. cit. we then deﬁne the
Andr´e-Kahn radicalND on objectsK,L∈ D by
ND(K,L) = {f∈ HomD(K,L)|∀ g∈ HomD(L,K) : tr(g◦ f ) =0}.
This is an ideal ofD in the sense that for all objectsK,K′,L,L′∈ D and all
morphismsh1∈ HomD(K′,K), h2∈ HomD(L,L′) one can show
h2◦ND(K,L)◦h1⊆ ND(K′,L′).
