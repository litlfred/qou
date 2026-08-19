---
doc_id: disssubmission
doc_title: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVER"
section_id: sec-043-34-tannakian-categories-53
section_title: "Tannakian categories 53"
section_number: 3.4
pages: 61-62
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "INAUGURAL-DISSERTATION Erlangung der Doktorwürde an der Naturwissenschaftlich-Mathematischen Gesamtfakultät der Ruprecht-Karls-Universität Heidelberg TANNAKIAN CATEGORIES OF PERVERSE SHEAVES — 121 sec"
---
diagrams in [41, appendix A.5.4] show that the morphism
Λ = H•(X,1)
coev∗ // H•(X,P∨∗intP) = H•(X,P∨∗∗ P) = H∨⊗ΛH
is the coevaluation in the category of vector spaces, and dually forev. Since
the category of vector spaces of ﬁnite dimension overΛ is rigid, it follows
that on hypercohomologyγ−idP induces the zero morphism. Accordingly
the perverse subquotientQ = P/ker(γ−idP) of P has H•(X,Q) = 0. By
deﬁnition ofPint it follows thatQ = 0 and hence thatγ−idP = 0. □
This in particular allows to deﬁne the Tannaka groups we are interested
in, generalizing those in corollary 2.14. ForP∈ P we denote by⟨P⟩⊂ P
the full subcategory of all objects which are isomorphic to subquotients of
convolution powers ofP⊕P∨. Recall that full subcategories of this form
are said to be ﬁnitely tensor generated. By construction they inherit fromP
the structure of a rigid symmetric monoidalΛ-linear abelian category, and
we claim that they are neutral Tannakian in the following sense.
COROLLARY 3.10. For every P∈ P there exists an afﬁne algebraic
group G= G(P) overΛ and an equivalence
ω : ⟨P⟩ ∼−→RepΛ(G)
with the rigid symmetric monoidalΛ-linear abelian category RepΛ(G) of
ﬁnite-dimensional algebraic representations of G.
Proof. ConsiderP as an object of the lifted categoryPint⊂ P. By
theorem 3.1 there exists a characterχ∈ Π(X) such that all constituents
of all convolution powers
(P⊕P∨)χ∗int···∗ int(P⊕P∨)χ
have their hypercohomology concentrated in degree zero (indeed these are
countably many conditions, and identifyingΠ(X)l as in [41, sect. 3.2] with
the set ofΛ-valued points of the afﬁne schemeSpec(Λ⊗Zl Zl[[t1, . . . ,tn]])
for somen >0 one checks thatΠ(X)l cannot be covered by countably many
proper closed subsets — for this one may proceed by induction onn, using
the description of ideals given in proposition A.2.2.3 of loc. cit.). For such
a character χ the functorQ↦→ H0(X,Qχ) is a ﬁbre functor from⟨P⟩ to
the category of ﬁnite-dimensional vector spaces, and our corollary follows
from theorem 3.9 via the Tannakian formalism [33, th. 2.11]. □
The above ﬁbre functor depends on the chosen character twist (though
all choices lead to isomorphic Tannaka groups), and this is the reason why
we have restricted ourselves to ﬁnitely tensor generated subcategories. For
a more canonical construction one may as in [41, th. 3.7.5] take the functor
which to a perverse sheaf assigns the generic ﬁbre of its Mellin transform,
54 Chapter 3 – Perverse sheaves on semiabelian varieties
but then the ﬁbre functor is only deﬁned over a large extension ﬁeld ofΛ,
and the descent toΛ again involves non-canonical choices.
REMARK 3.11. If P∈ P(X) is a semisimple perverse sheaf, then G(P)
is a reductive algebraic group, and over k= C this group coincides with the
one that has been deﬁned in corollary 2.14.
Proof. The groupG(P) acts faithfully on the representationV = ω(P)
which in the case at hand is semisimple, whereas the unipotent radical of
an algebraic group acts trivially on every irreducible representation. So
the unipotent radical must be trivial, i.e.G(P) is reductive. The remaining
statement follows easily from the universal property of the localizationD
together with the last statement of corollary 2.9. □
